import os
import numpy as np
import pandas as pd
from scipy import stats
from statsmodels.stats.stattools import durbin_watson


def calculate_simple_regression(x, y):
    """
    Fits a simple linear regression using scipy.stats.linregress and
    computes 95% confidence intervals and diagnostic statistics.
    """
    n = len(x)
    if n <= 2:
        return {}
    
    slope, intercept, r_value, p_value, std_err = stats.linregress(x, y)
    r_squared = r_value ** 2
    
    # Calculate residuals and Durbin-Watson statistic
    y_pred = slope * x + intercept
    residuals = y - y_pred
    dw_stat = durbin_watson(residuals)
    rmse = np.sqrt(np.mean(residuals**2))
    
    # t-critical value for 95% CI with n-2 degrees of freedom
    df = n - 2
    t_crit = stats.t.ppf(0.975, df)
    
    slope_low = slope - t_crit * std_err
    slope_high = slope + t_crit * std_err
    
    return {
        'slope': slope,
        'slope_stderr': std_err,
        'slope_95_low': slope_low,
        'slope_95_high': slope_high,
        'intercept': intercept,
        'r_squared': r_squared,
        'p_value': p_value,
        'durbin_watson': dw_stat,
        'rmse': rmse
    }


if __name__ == "__main__":
    # Ensure all pandas outputs are printed in full
    pd.set_option("display.max_rows", None)
    pd.set_option("display.max_columns", None)
    pd.set_option("display.width", 250)

    # 1. Load data from Step 1
    clean_data_path = "data/wp_processed_clean.csv"
    polar_gaps_path = "data/polar_gap_trends.csv"
    
    print(f"Loading processed clean dataset from: {clean_data_path}")
    df_clean = pd.read_csv(clean_data_path)
    
    print(f"Loading POLAR gap trends from: {polar_gaps_path}")
    df_polar_gaps = pd.read_csv(polar_gaps_path)

    # 2. Benchmarking for the latest academic year (2022/23)
    latest_year = 2022
    df_latest = df_clean[df_clean['year'] == latest_year]
    print(f"\n--- CROSS-DIMENSIONAL EQUITY BENCHMARKING (Latest Year: 2022/23) ---")

    topics = df_latest['breakdown_topic'].unique()
    benchmarking_results = []

    for topic in topics:
        topic_df = df_latest[df_latest['breakdown_topic'] == topic]
        if len(topic_df) < 2:
            continue
            
        # Find category with highest progression rate (Advantaged) and lowest (Disadvantaged)
        highest_row = topic_df.loc[topic_df['progression_rate'].idxmax()]
        lowest_row = topic_df.loc[topic_df['progression_rate'].idxmin()]
        
        adv_cat = highest_row['breakdown']
        disadv_cat = lowest_row['breakdown']
        
        p_adv = highest_row['progression_rate']
        p_disadv = lowest_row['progression_rate']
        
        abs_gap = p_adv - p_disadv
        rel_ratio = p_adv / p_disadv if p_disadv > 0 else np.nan
        
        # Repeat for high-tariff if available
        ht_adv = highest_row['high_tariff_progression_rate']
        ht_disadv = lowest_row['high_tariff_progression_rate']
        
        ht_abs_gap = ht_adv - ht_disadv
        ht_rel_ratio = ht_adv / ht_disadv if ht_disadv > 0 else np.nan
        
        benchmarking_results.append({
            'breakdown_topic': topic,
            'advantaged_category': adv_cat,
            'disadvantaged_category': disadv_cat,
            'overall_advantaged_rate': p_adv,
            'overall_disadvantaged_rate': p_disadv,
            'overall_abs_gap': abs_gap,
            'overall_rel_ratio': rel_ratio,
            'high_tariff_advantaged_rate': ht_adv,
            'high_tariff_disadvantaged_rate': ht_disadv,
            'high_tariff_abs_gap': ht_abs_gap,
            'high_tariff_rel_ratio': ht_rel_ratio
        })

    df_benchmarking = pd.DataFrame(benchmarking_results)
    # Rank topics by the magnitude of the absolute overall HE progression gap
    df_benchmarking = df_benchmarking.sort_values(by='overall_abs_gap', ascending=False)
    
    # Save benchmarking rankings
    benchmarking_path = "data/cross_dimensional_rankings.csv"
    df_benchmarking.to_csv(benchmarking_path, index=False)
    print(f"Saved cross-dimensional benchmarking rankings to: {benchmarking_path}")
    print("Schema:", list(df_benchmarking.columns))
    print("\nRanked Equity Gaps across Breakdown Topics (2022/23):")
    print(df_benchmarking[['breakdown_topic', 'advantaged_category', 'disadvantaged_category', 'overall_abs_gap', 'overall_rel_ratio', 'high_tariff_abs_gap', 'high_tariff_rel_ratio']].to_string(index=False))

    # 3. POLAR Gap Trend Regression Analysis
    print("\n--- POLAR GAP TREND REGRESSION ANALYSIS (2009/10 to 2022/23) ---")
    
    x_years = df_polar_gaps['year'].values
    
    metrics_to_fit = {
        'overall_abs_gap': df_polar_gaps['abs_gap'].values,
        'overall_rel_ratio': df_polar_gaps['rel_ratio'].values,
        'high_tariff_abs_gap': df_polar_gaps['high_tariff_abs_gap'].values,
        'high_tariff_rel_ratio': df_polar_gaps['high_tariff_rel_ratio'].values
    }
    
    regression_records = []
    
    for name, y_values in metrics_to_fit.items():
        # Mask NaNs if any exist
        mask = ~np.isnan(y_values)
        fit_results = calculate_simple_regression(x_years[mask], y_values[mask])
        fit_results['metric'] = name
        regression_records.append(fit_results)
        
    df_reg_results = pd.DataFrame(regression_records)
    # Reorder columns for readability
    col_order = ['metric', 'slope', 'slope_stderr', 'slope_95_low', 'slope_95_high', 'intercept', 'r_squared', 'p_value', 'durbin_watson', 'rmse']
    df_reg_results = df_reg_results[col_order]
    
    regression_results_path = "data/regression_results.csv"
    df_reg_results.to_csv(regression_results_path, index=False)
    print(f"\nSaved regression analysis results to: {regression_results_path}")
    print("Schema:", list(df_reg_results.columns))
    
    print("\nPOLAR Gap Linear Trend Fitting Statistics:")
    print(df_reg_results.to_string(index=False))