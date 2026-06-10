import os
import numpy as np
import pandas as pd
from statsmodels.stats.proportion import proportion_confint


def parse_time_period(tp_val):
    """Parses a YYYYYY time_period integer into a year and academic cycle label."""
    tp_str = str(tp_val)
    if len(tp_str) == 6:
        year_int = int(tp_str[:4])
        cycle_str = f"{tp_str[:4]}/{tp_str[4:]}"
        return year_int, cycle_str
    else:
        # Fallback
        return np.nan, "Unknown"


def calculate_wilson_ci(count, total):
    """Calculates Wilson score confidence intervals, handling boundary cases."""
    if pd.isna(count) or pd.isna(total) or total <= 0 or count < 0 or count > total:
        return np.nan, np.nan
    low, high = proportion_confint(count, total, alpha=0.05, method='wilson')
    return low, high


def propagate_conversion_ratio_uncertainty(row):
    """
    Propagates uncertainty for the Conversion Ratio:
    Conversion Ratio = number_of_high_tariff_he_students / number_of_he_students.
    Since high-tariff students are a subset of all HE students, this is also a proportion.
    We can model this directly as a binomial proportion with n = number_of_he_students
    and x = number_of_high_tariff_he_students, applying the Wilson interval.
    """
    n = row['number_of_he_students']
    x = row['number_of_high_tariff_he_students']
    if pd.isna(n) or pd.isna(x) or n <= 0 or x < 0 or x > n:
        return np.nan, np.nan, np.nan
    ratio = x / n
    low, high = proportion_confint(x, n, alpha=0.05, method='wilson')
    return ratio, low, high


def calculate_gap_metrics(group_1_row, group_2_row, prefix=""):
    """
    Calculates absolute and relative gaps between two groups with propagated CIs.
    Group 1 is usually the advantaged group (e.g. Q5), Group 2 the disadvantaged (e.g. Q1).
    
    Absolute Gap = p1 - p2
    Relative Ratio = p1 / p2
    """
    p1 = group_1_row[f'{prefix}progression_rate'] / 100.0
    p2 = group_2_row[f'{prefix}progression_rate'] / 100.0
    
    n1 = group_1_row['number_of_students']
    n2 = group_2_row['number_of_students']
    
    if pd.isna(p1) or pd.isna(p2) or pd.isna(n1) or pd.isna(n2) or n1 <= 0 or n2 <= 0:
        return {}
        
    # Standard errors of individual proportions (using standard binomial approximation for delta method)
    var1 = (p1 * (1 - p1)) / n1
    var2 = (p2 * (1 - p2)) / n2
    
    # Absolute Gap
    abs_gap = p1 - p2
    abs_se = np.sqrt(var1 + var2)
    abs_low = abs_gap - 1.96 * abs_se
    abs_high = abs_gap + 1.96 * abs_se
    
    # Relative Ratio (Delta Method on Log Scale)
    if p2 > 0 and p1 > 0:
        rel_ratio = p1 / p2
        # Var(log(R)) = Var(p1)/p1^2 + Var(p2)/p2^2
        log_var = (var1 / (p1**2)) + (var2 / (p2**2))
        log_se = np.sqrt(log_var)
        log_low = np.log(rel_ratio) - 1.96 * log_se
        log_high = np.log(rel_ratio) + 1.96 * log_se
        rel_low = np.exp(log_low)
        rel_high = np.exp(log_high)
    else:
        rel_ratio, rel_low, rel_high = np.nan, np.nan, np.nan
        
    return {
        f'{prefix}abs_gap': abs_gap * 100.0,  # convert back to percentage points
        f'{prefix}abs_low': abs_low * 100.0,
        f'{prefix}abs_high': abs_high * 100.0,
        f'{prefix}rel_ratio': rel_ratio,
        f'{prefix}rel_low': rel_low,
        f'{prefix}rel_high': rel_high
    }


if __name__ == "__main__":
    # Disable truncation for pretty pandas outputs
    pd.set_option("display.max_rows", None)
    pd.set_option("display.max_columns", None)
    pd.set_option("display.width", 200)

    # 1. Load the dataset
    input_path = "/Users/boris/Desktop/ucas-widening-participation/Iteration0/input_files/data/wp_all_characteristics.csv"
    print(f"Loading dataset from: {input_path}")
    df = pd.read_csv(input_path)
    
    # 2. Temporal parsing
    parsed_temporal = df['time_period'].apply(parse_time_period)
    df['year'] = [x[0] for x in parsed_temporal]
    df['academic_cycle'] = [x[1] for x in parsed_temporal]
    
    # 3. Separate Unknown categories for validation
    df_unknown = df[df['breakdown'].str.lower().str.contains('unknown', na=False)].copy()
    df_clean = df[~df['breakdown'].str.lower().str.contains('unknown', na=False)].copy()
    
    print(f"\nTotal rows loaded: {len(df)}")
    print(f"Clean rows: {len(df_clean)} | Unknown/Excluded rows: {len(df_unknown)}")
    
    # 4. Data sparsity check
    print("\n--- COHORT SPARSITY CHECK (by breakdown_topic) ---")
    sparsity_summary = df_clean.groupby('breakdown_topic').agg(
        min_cohort_size=('number_of_students', 'min'),
        median_cohort_size=('number_of_students', 'median'),
        max_cohort_size=('number_of_students', 'max'),
        total_records=('number_of_students', 'count')
    ).sort_values(by='min_cohort_size')
    print(sparsity_summary.to_string())
    
    # Flag small cohorts (e.g., median cohort size < 5000)
    flagged_topics = sparsity_summary[sparsity_summary['median_cohort_size'] < 5000].index.tolist()
    print(f"\nFlagged high-volatility topics (median cohort < 5000): {flagged_topics}")

    # 5. Statistical Uncertainty Estimation (Wilson CIs)
    print("\nCalculating Wilson Score CIs for progression rates...")
    
    # Overall progression CIs
    overall_ci = df_clean.apply(
        lambda r: calculate_wilson_ci(r['number_of_he_students'], r['number_of_students']), axis=1
    )
    df_clean['progression_rate_low'] = [x[0]*100 for x in overall_ci]
    df_clean['progression_rate_high'] = [x[1]*100 for x in overall_ci]
    
    # High-tariff progression CIs
    ht_ci = df_clean.apply(
        lambda r: calculate_wilson_ci(r['number_of_high_tariff_he_students'], r['number_of_students']), axis=1
    )
    df_clean['high_tariff_progression_rate_low'] = [x[0]*100 for x in ht_ci]
    df_clean['high_tariff_progression_rate_high'] = [x[1]*100 for x in ht_ci]

    # 6. Conversion Ratio and uncertainty propagation
    print("Calculating Conversion Ratio and propagated uncertainty bounds...")
    conversion_stats = df_clean.apply(propagate_conversion_ratio_uncertainty, axis=1)
    df_clean['conversion_ratio'] = [x[0] for x in conversion_stats]
    df_clean['conversion_ratio_low'] = [x[1] for x in conversion_stats]
    df_clean['conversion_ratio_high'] = [x[2] for x in conversion_stats]

    # Save clean processed dataset
    processed_clean_path = "data/wp_processed_clean.csv"
    df_clean.to_csv(processed_clean_path, index=False)
    print(f"\nSaved processed clean dataset: {processed_clean_path}")
    print("Schema:", list(df_clean.columns))

    # Save unknown validation set
    unknowns_path = "data/wp_unknown_validation.csv"
    df_unknown.to_csv(unknowns_path, index=False)
    print(f"Saved unknown categories validation set: {unknowns_path}")
    
    # 7. Compute POLAR Topic Gaps over time
    polar_df = df_clean[df_clean['breakdown_topic'] == 'POLAR'].copy()
    
    polar_gaps = []
    years = sorted(polar_df['year'].unique())
    
    for yr in years:
        yr_data = polar_df[polar_df['year'] == yr]
        q1_row = yr_data[yr_data['breakdown'] == 'Q1 - Most Disadvantaged']
        q5_row = yr_data[yr_data['breakdown'] == 'Q5 - Most Advantaged']
        
        if q1_row.empty or q5_row.empty:
            continue
            
        q1_row = q1_row.iloc[0]
        q5_row = q5_row.iloc[0]
        
        cycle_lbl = q1_row['academic_cycle']
        
        # Calculate overall progression gap metrics
        overall_gaps = calculate_gap_metrics(q5_row, q1_row, prefix="")
        # Calculate high-tariff progression gap metrics
        ht_gaps = calculate_gap_metrics(q5_row, q1_row, prefix="high_tariff_")
        
        gap_record = {
            'year': yr,
            'academic_cycle': cycle_lbl,
            'q1_overall_rate': q1_row['progression_rate'],
            'q5_overall_rate': q5_row['progression_rate'],
            'q1_ht_rate': q1_row['high_tariff_progression_rate'],
            'q5_ht_rate': q5_row['high_tariff_progression_rate']
        }
        gap_record.update(overall_gaps)
        gap_record.update(ht_gaps)
        polar_gaps.append(gap_record)
        
    polar_gaps_df = pd.DataFrame(polar_gaps)
    
    # Save the gap tracking metrics
    gap_metrics_path = "data/polar_gap_trends.csv"
    polar_gaps_df.to_csv(gap_metrics_path, index=False)
    print(f"\nSaved POLAR gap trend metrics: {gap_metrics_path}")
    print("Schema:", list(polar_gaps_df.columns))
    
    print("\n--- SUMMARY OF POLAR PROGRESSION GAPS (Q5 - Q1) OVER TIME ---")
    summary_cols = [
        'academic_cycle', 'abs_gap', 'abs_low', 'abs_high', 'rel_ratio', 
        'high_tariff_abs_gap', 'high_tariff_abs_low', 'high_tariff_abs_high', 'high_tariff_rel_ratio'
    ]
    print(polar_gaps_df[summary_cols].to_string(index=False))