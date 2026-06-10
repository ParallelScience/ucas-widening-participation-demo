

Iteration 0:
### Summary: Benchmarking Structural Inequality in English HE (2009/10–2022/23)

**Dataset & Methodology**
- **Source:** DfE "Widening participation in higher education" (2009/10–2022/23).
- **Scope:** 666 rows (624 used; `Unknown` excluded). National-level aggregate rates.
- **Metrics:** Overall progression rate, High-tariff progression rate, and "Conversion Ratio" (High-tariff/Overall).
- **Uncertainty:** 95% Wilson score intervals for rates; propagated variance for gaps; Delta Method for ratios.
- **Trend Analysis:** Simple linear regression (14 annual points). 2020/21–2022/23 flagged as COVID-affected (descriptive only).

**Key Findings**
1. **Overall HE Access:** Modest, statistically significant narrowing of the POLAR Q5–Q1 absolute gap (slope: -0.328 pp/year; 95% CI: [-0.412, -0.244]). Relative ratio improved from 2.85 to 1.96.
2. **High-Tariff Access:** Absolute POLAR gap **widened** (slope: +0.125 pp/year; 95% CI: [+0.040, +0.210]). While relative inequality narrowed, the absolute exclusion gap remains persistent and policy-salient.
3. **Compounding Disadvantage:** A "selectivity penalty" exists; among HE entrants, Q5 students are ~1.9x more likely than Q1 to enter high-tariff providers. This confirms that inequality persists *after* initial HE entry.
4. **Cross-Dimensional Benchmarking (2022/23):** POLAR is not the sole driver. Largest absolute gaps found in **Ethnicity Minor** (72.5 pp), **SEN Provision** (41.9 pp), and **Children in Need** (34.0 pp).

**Limitations & Constraints**
- **Trend Inference:** Limited to 14 points; no structural-break modeling or parity projections.
- **Data Sparsity:** Small cohorts in `Ethnicity Minor` and vulnerable status groups require cautious interpretation of extreme rankings.
- **COVID-19:** Recent years show no clear convergence in selective access; treated as descriptive observations.

**Future Directions**
- **Prioritize:** Investigate the "selectivity penalty" for non-POLAR dimensions (e.g., SEN, Looked After Status) to determine if they mirror the POLAR compounding effect.
- **Methodological Note:** Future analyses should maintain the dual-metric framework (Overall vs. High-Tariff) as they capture distinct structural barriers. Avoid over-interpreting the 2020/21+ period as a new trend.
- **Data Handling:** Continue using the absolute path `/Users/boris/Desktop/ucas-widening-participation/Iteration0/input_files/data/wp_all_characteristics.csv`.
        