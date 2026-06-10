1. **Data Preparation and Sparsity Assessment**
   - Load the dataset from `/Users/boris/Desktop/ucas-widening-participation/Iteration0/input_files/data/wp_all_characteristics.csv`.
   - Parse `time_period` into an integer year (start of academic cycle).
   - Perform a data sparsity check: identify subgroups with consistently low cohort sizes (e.g., Looked After Status). Flag these in the analysis to ensure volatility is interpreted with caution.
   - Filter out `Unknown` categories from primary gap calculations, retaining them only for data quality validation.

2. **Statistical Uncertainty Estimation**
   - Calculate 95% Wilson score intervals for all `progression_rate` and `high_tariff_progression_rate` values.
   - For absolute gaps ($Rate_{A} - Rate_{B}$), calculate the variance of the difference as the sum of the individual variances ($Var(p_1) + Var(p_2)$) to derive the confidence interval.
   - For gap ratios ($Rate_{A} / Rate_{B}$), use the Delta Method to propagate uncertainty and derive the 95% confidence interval for the ratio.

3. **Defining the Dual-Metric Framework**
   - Calculate the "Conversion Ratio" ($number\_of\_high\_tariff\_he\_students / number\_of\_he\_students$) for each subgroup.
   - Explicitly distinguish in all reporting between the "High-Tariff Progression Rate" (access from the total cohort) and the "Conversion Ratio" (institutional selection bias given HE entry).
   - Apply uncertainty propagation to the Conversion Ratio to ensure selectivity penalties are statistically defensible.

4. **Trend Analysis of Gaps**
   - Isolate POLAR Q1 and Q5 series for overall and high-tariff progression.
   - Fit a simple linear regression to the absolute and relative gaps over the 14-year period.
   - Extract the slope coefficient and 95% confidence interval.
   - Perform a visual inspection of residuals to check for non-linear patterns or autocorrelation, noting any limitations of the linear model in the final narrative.

5. **Cross-Dimensional Equity Benchmarking**
   - For the most recent academic year, calculate the absolute and relative gaps between the most advantaged and most disadvantaged categories for every `breakdown_topic`.
   - Rank these dimensions by the magnitude of the absolute gap to identify the primary drivers of inequality.

6. **Compounding Disadvantage Analysis**
   - Visualize the "drop-off" from overall HE progression to high-tariff progression for selected groups.
   - Quantify the "selectivity penalty" by comparing the Conversion Ratios of disadvantaged groups against their more advantaged counterparts.

7. **Visualization Strategy**
   - Generate time-series plots for POLAR Q1 vs Q5 progression, including shaded regions for Wilson confidence intervals.
   - Produce a ranked bar chart of equity gaps across all breakdown topics for the latest year.
   - Annotate the 2020/21–2022/23 period as COVID-affected in all plots and include summary statistics (slope/significance) for trends.

8. **Synthesis and Reporting**
   - Compile a policy-audience narrative contrasting the "access gap" (overall) with the "selectivity gap" (high-tariff).
   - Use the calculated slopes, confidence intervals, and gap ratios to provide a definitive statement on the trajectory of equity gaps, ensuring that small-cohort volatility and the COVID-19 period are contextualized as descriptive observations.