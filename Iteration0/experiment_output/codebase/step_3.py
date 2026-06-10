import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats

# Set scientific plotting parameters
plt.rcParams['text.usetex'] = False
plt.rcParams['font.family'] = 'sans-serif'
plt.rcParams['font.size'] = 10
plt.rcParams['axes.unicode_minus'] = False

def calculate_trend_confidence_band(x, y, x_grid, slope, intercept, r_squared, p_value):
    """
    Calculates the 95% confidence band for a fitted simple linear regression line.
    """
    n = len(x)
    y_pred_orig = slope * x + intercept
    residuals = y - y_pred_orig
    rmse = np.sqrt(np.sum(residuals**2) / (n - 2))
    
    mean_x = np.mean(x)
    sum_sq_x = np.sum((x - mean_x)**2)
    
    # standard error of prediction for each point in x_grid
    se_pred = rmse * np.sqrt(1/n + (x_grid - mean_x)**2 / sum_sq_x)
    
    # t-critical value
    t_crit = stats.t.ppf(0.975, df=n-2)
    
    y_grid = slope * x_grid + intercept
    ci_lower = y_grid - t_crit * se_pred
    ci_upper = y_grid + t_crit * se_pred
    
    return y_grid, ci_lower, ci_upper

if __name__ == '__main__':
    # Ensure data directory paths are correct
    clean_data_path = "data/wp_processed_clean.csv"
    polar_gaps_path = "data/polar_gap_trends.csv"
    rankings_path = "data/cross_dimensional_rankings.csv"
    regression_path = "data/regression_results.csv"

    print(f"Loading datasets for visualization...")
    df_clean = pd.read_csv(clean_data_path)
    df_polar_gaps = pd.read_csv(polar_gaps_path)
    df_rankings = pd.read_csv(rankings_path)
    df_regression = pd.read_csv(regression_path)
    latest_year = df_clean['year'].max()

    # -------------------------------------------------------------
    # FIGURE 1: POLAR RATES & GAP TRENDS (TWO-PANEL)
    # -------------------------------------------------------------
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6), dpi=300)
    
    years = df_polar_gaps['year'].values
    cycles = df_polar_gaps['academic_cycle'].values
    
    # Left Panel: Progression Rates over time
    q1_data = df_clean[(df_clean['breakdown_topic'] == 'POLAR') & (df_clean['breakdown'] == 'Q1 - Most Disadvantaged')].sort_values('year')
    q5_data = df_clean[(df_clean['breakdown_topic'] == 'POLAR') & (df_clean['breakdown'] == 'Q5 - Most Advantaged')].sort_values('year')
    
    ax1.plot(q5_data['year'], q5_data['progression_rate'], label='Q5 - Most Advantaged (Overall HE)', color='#003366', linewidth=2, marker='o')
    ax1.fill_between(q5_data['year'], q5_data['progression_rate_low'], q5_data['progression_rate_high'], color='#003366', alpha=0.15)
    
    ax1.plot(q5_data['year'], q5_data['high_tariff_progression_rate'], label='Q5 - Most Advantaged (High-Tariff)', color='#006699', linewidth=2, marker='s', linestyle='--')
    ax1.fill_between(q5_data['year'], q5_data['high_tariff_progression_rate_low'], q5_data['high_tariff_progression_rate_high'], color='#006699', alpha=0.15)
    
    ax1.plot(q1_data['year'], q1_data['progression_rate'], label='Q1 - Most Disadvantaged (Overall HE)', color='#cc0000', linewidth=2, marker='o')
    ax1.fill_between(q1_data['year'], q1_data['progression_rate_low'], q1_data['progression_rate_high'], color='#cc0000', alpha=0.15)
    
    ax1.plot(q1_data['year'], q1_data['high_tariff_progression_rate'], label='Q1 - Most Disadvantaged (High-Tariff)', color='#ff6666', linewidth=2, marker='s', linestyle='--')
    ax1.fill_between(q1_data['year'], q1_data['high_tariff_progression_rate_low'], q1_data['high_tariff_progression_rate_high'], color='#ff6666', alpha=0.15)
    
    ax1.set_title("Progression Rates by POLAR Quintile (with 95% Wilson CIs)", fontsize=11, fontweight='bold')
    ax1.set_xlabel("Academic Year (Cycle Start)", fontsize=10)
    ax1.set_ylabel("Progression Rate (%)", fontsize=10)
    ax1.set_xticks(years)
    ax1.set_xticklabels(cycles, rotation=45, ha='right')
    ax1.grid(True, linestyle=':', alpha=0.6)
    ax1.legend(loc='upper left', fontsize=9)
    ax1.axvspan(2020, 2022, color='gray', alpha=0.12, label='COVID-Affected Period')
    ax1.text(2021, 5, "COVID-Affected\nPeriod", color='dimgray', fontsize=8, ha='center', fontweight='semibold')
    
    # Right Panel: Absolute Gaps and Linear Trend Fits
    overall_gap = df_polar_gaps['abs_gap'].values
    ht_gap = df_polar_gaps['high_tariff_abs_gap'].values
    reg_overall = df_regression[df_regression['metric'] == 'overall_abs_gap'].iloc[0]
    reg_ht = df_regression[df_regression['metric'] == 'high_tariff_abs_gap'].iloc[0]
    x_grid = np.linspace(years.min(), years.max(), 100)
    
    y_grid_ov, ci_low_ov, ci_high_ov = calculate_trend_confidence_band(years, overall_gap, x_grid, reg_overall['slope'], reg_overall['intercept'], reg_overall['r_squared'], reg_overall['p_value'])
    ax2.scatter(years, overall_gap, color='#003366', zorder=3, label='Observed Overall Gap (Q5 - Q1)')
    ax2.plot(x_grid, y_grid_ov, color='#003366', linewidth=2, label='Overall Gap Trend Fit')
    ax2.fill_between(x_grid, ci_low_ov, ci_high_ov, color='#003366', alpha=0.1)
    
    y_grid_ht, ci_low_ht, ci_high_ht = calculate_trend_confidence_band(years, ht_gap, x_grid, reg_ht['slope'], reg_ht['intercept'], reg_ht['r_squared'], reg_ht['p_value'])
    ax2.scatter(years, ht_gap, color='#cc0000', zorder=3, label='Observed High-Tariff Gap (Q5 - Q1)')
    ax2.plot(x_grid, y_grid_ht, color='#cc0000', linewidth=2, linestyle='--', label='High-Tariff Gap Trend Fit')
    ax2.fill_between(x_grid, ci_low_ht, ci_high_ht, color='#cc0000', alpha=0.1)
    
    text_ov = f"Overall Gap Slope:\n{reg_overall['slope']:.3f} pp/yr\n95% CI: [{reg_overall['slope_95_low']:.3f}, {reg_overall['slope_95_high']:.3f}]\np < 0.001"
    text_ht = f"High-Tariff Gap Slope:\n{reg_ht['slope']:.3f} pp/yr\n95% CI: [{reg_ht['slope_95_low']:.3f}, {reg_ht['slope_95_high']:.3f}]\np = {reg_ht['p_value']:.3f}"
    ax2.text(2010, 24, text_ov, color='#003366', fontsize=8.5, bbox=dict(facecolor='white', alpha=0.8, edgecolor='#003366', boxstyle='round,pad=0.4'))
    ax2.text(2010, 11, text_ht, color='#cc0000', fontsize=8.5, bbox=dict(facecolor='white', alpha=0.8, edgecolor='#cc0000', boxstyle='round,pad=0.4'))
    
    ax2.set_title("Absolute POLAR Gaps with Linear Trend 95% Confidence Bands", fontsize=11, fontweight='bold')
    ax2.set_xlabel("Academic Year (Cycle Start)", fontsize=10)
    ax2.set_ylabel("Absolute Gap (Percentage Points)", fontsize=10)
    ax2.set_xticks(years)
    ax2.set_xticklabels(cycles, rotation=45, ha='right')
    ax2.grid(True, linestyle=':', alpha=0.6)
    ax2.legend(loc='upper right', fontsize=9)
    ax2.axvspan(2020, 2022, color='gray', alpha=0.12)
    
    plt.tight_layout()
    plt.savefig("data/polar_trend_gaps.png", dpi=300)
    plt.close()

    # -------------------------------------------------------------
    # FIGURE 2: CROSS-DIMENSIONAL BENCHMARKING
    # -------------------------------------------------------------
    fig, ax = plt.subplots(figsize=(11, 6), dpi=300)
    df_rankings_sorted = df_rankings.sort_values(by='overall_abs_gap', ascending=True)
    y_pos = np.arange(len(df_rankings_sorted))
    bar_width = 0.35
    rects1 = ax.barh(y_pos + bar_width/2, df_rankings_sorted['overall_abs_gap'], bar_width, label='Overall Progression Gap', color='#1f77b4', alpha=0.9)
    rects2 = ax.barh(y_pos - bar_width/2, df_rankings_sorted['high_tariff_abs_gap'], bar_width, label='High-Tariff Progression Gap', color='#ff7f0e', alpha=0.9)
    labels = []
    for idx, row in df_rankings_sorted.iterrows():
        topic = row['breakdown_topic']
        adv = row['advantaged_category'].replace(" - Most Advantaged", "").replace("No Identified special educational need", "No SEN").replace("All Other Pupils", "Other")
        disadv = row['disadvantaged_category'].replace(" - Most Disadvantaged", "").replace("Education, health and care plan", "EHCP").replace("Looked after continuously for 12 months or more", "Looked After")
        labels.append(f"{topic}\n({adv} vs {disadv})")
    ax.set_yticks(y_pos)
    ax.set_yticklabels(labels, fontsize=8)
    ax.set_xlabel("Absolute Gap in 2022/23 (Percentage Points)", fontsize=10)
    ax.set_title("Benchmarking Structural Inequality: Equity Gaps across Breakdown Topics (2022/23)", fontsize=12, fontweight='bold')
    ax.legend(loc='lower right', fontsize=10)
    ax.grid(True, axis='x', linestyle=':', alpha=0.6)
    for rect in rects1:
        width = rect.get_width()
        ax.annotate(f'{width:.1f} pp', xy=(width, rect.get_y() + rect.get_height() / 2), xytext=(3, 0), textcoords="offset points", ha='left', va='center', fontsize=7.5, color='#1f77b4', fontweight='bold')
    plt.tight_layout()
    plt.savefig("data/equity_benchmarking.png", dpi=300)
    plt.close()

    # -------------------------------------------------------------
    # FIGURE 3: COMPOUNDING DISADVANTAGE
    # -------------------------------------------------------------
    key_dimensions = [('POLAR', 'Q5 - Most Advantaged', 'Q1 - Most Disadvantaged'), ('Disadvantage', 'All Other Pupils', 'Disadvantaged'), ('FSM Status', 'All Other Pupils', 'Free School Meals'), ('SEN Status', 'No Identified special educational need', 'Any special educational need'), ('Sex', 'Female', 'Male')]
    compounding_data = []
    for topic, adv, disadv in key_dimensions:
        adv_row = df_clean[(df_clean['year'] == latest_year) & (df_clean['breakdown_topic'] == topic) & (df_clean['breakdown'] == adv)]
        disadv_row = df_clean[(df_clean['year'] == latest_year) & (df_clean['breakdown_topic'] == topic) & (df_clean['breakdown'] == disadv)]
        if not adv_row.empty and not disadv_row.empty:
            adv_row, disadv_row = adv_row.iloc[0], disadv_row.iloc[0]
            compounding_data.append({'Topic': topic, 'Adv_Label': adv.replace(" - Most Advantaged", ""), 'Disadv_Label': disadv.replace(" - Most Disadvantaged", ""), 'Adv_Conv_Ratio': adv_row['conversion_ratio'] * 100, 'Adv_Conv_Low': adv_row['conversion_ratio_low'] * 100, 'Adv_Conv_High': adv_row['conversion_ratio_high'] * 100, 'Disadv_Conv_Ratio': disadv_row['conversion_ratio'] * 100, 'Disadv_Conv_Low': disadv_row['conversion_ratio_low'] * 100, 'Disadv_Conv_High': disadv_row['conversion_ratio_high'] * 100})
    df_comp = pd.DataFrame(compounding_data)
    fig, ax = plt.subplots(figsize=(10, 5.5), dpi=300)
    for idx, row in df_comp.iterrows():
        ax.plot([row['Disadv_Conv_Ratio'], row['Adv_Conv_Ratio']], [idx, idx], color='gray', linestyle='-', linewidth=1.5, zorder=1)
        ax.errorbar(row['Adv_Conv_Ratio'], idx, xerr=[[row['Adv_Conv_Ratio'] - row['Adv_Conv_Low']], [row['Adv_Conv_High'] - row['Adv_Conv_Ratio']]], fmt='o', color='#003366', markersize=9, capsize=4, label='Advantaged Category' if idx == 0 else "", zorder=2)
        ax.errorbar(row['Disadv_Conv_Ratio'], idx, xerr=[[row['Disadv_Conv_Ratio'] - row['Disadv_Conv_Low']], [row['Disadv_Conv_High'] - row['Disadv_Conv_Ratio']]], fmt='o', color='#cc0000', markersize=9, capsize=4, label='Disadvantaged Category' if idx == 0 else "", zorder=2)
        penalty = row['Adv_Conv_Ratio'] - row['Disadv_Conv_Ratio']
        ratio_penalty = row['Adv_Conv_Ratio'] / row['Disadv_Conv_Ratio'] if row['Disadv_Conv_Ratio'] > 0 else np.nan
        ax.text((row['Adv_Conv_Ratio'] + row['Disadv_Conv_Ratio'])/2, idx + 0.15, f"-{penalty:.1f} pp (Ratio: {ratio_penalty:.2f}x)", ha='center', va='bottom', fontsize=8.5, fontweight='bold', color='#333333')
    ax.set_yticks(np.arange(len(df_comp)))
    ax.set_yticklabels([f"{r['Topic']}\n({r['Adv_Label']} vs {r['Disadv_Label']})" for _, r in df_comp.iterrows()], fontsize=9)
    ax.set_xlabel("Conversion Ratio (%) — Prop. of HE Enrollees entering High-Tariff Providers (with 95% Wilson CIs)", fontsize=10)
    ax.set_title("Compounding Disadvantage: Selectivity Penalty across Key Dimensions (2022/23)", fontsize=11, fontweight='bold')
    ax.legend(loc='lower right', fontsize=9)
    ax.grid(True, axis='x', linestyle=':', alpha=0.6)
    ax.set_xlim(left=0)
    plt.tight_layout()
    plt.savefig("data/compounding_disadvantage.png", dpi=300)
    plt.close()
    print("Visualizations generation completed successfully!")