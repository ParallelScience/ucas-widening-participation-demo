# Results: Benchmarking Structural Inequality in English Higher Education Progression, 2009/10–2022/23

## Overview

This analysis used the Department for Education’s published national-level widening participation dataset for England, covering academic years 2009/10 to 2022/23, to compare inequalities in progression to higher education by age 19 across multiple pupil characteristics. The central distinction throughout is between:

- **overall HE progression**: entry to any higher education; and
- **high-tariff progression**: entry to a more selective provider from the full state-school cohort.

A third metric, the **Conversion Ratio**, was derived to isolate selectivity conditional on having entered HE:

\[
\text{Conversion Ratio} = \frac{\text{number of high-tariff HE students}}{\text{number of HE students}}
\]

This separates barriers to entering HE at all from barriers to reaching selective institutions once in HE’s applicant and entrant pipeline.

Unknown categories were excluded from substantive gap calculations, in line with the design brief. Uncertainty around rates was represented using **95% Wilson score intervals**; gap uncertainty for differences was propagated from component variances, and ratio uncertainty was estimated using a log-scale delta method. Trend analysis was intentionally limited to a **single simple linear regression** on annual gap series, reflecting the modest number of time points and the instruction not to fit structural-break models or project parity dates. The years **2020/21 onward** are treated as a **COVID-affected descriptive period**, not as a separately estimated regime.

Across the full period, the results show a clear asymmetry. **Overall POLAR gaps narrowed modestly but significantly**, whereas **high-tariff POLAR gaps widened in absolute terms**, despite some narrowing in relative terms because disadvantaged groups started from an extremely low base. In 2022/23, the largest disparities in the system were not solely by area disadvantage: some of the starkest divides were by **detailed ethnicity**, **SEN provision**, and care-related vulnerability. The evidence therefore points to a layered pattern of inequality: access gaps into HE remain large, and selective access gaps often compound them further.

---

## Data quality, scope, and interpretive caution

The underlying file contains **666 rows**, of which **624** remained after excluding **42 `Unknown` rows** from primary comparisons. The data are aggregated, national statistics rather than person-level observations. This has several implications.

First, the estimates are precise for large groups, but volatility can still arise where subgroup numerators are small even if denominators are not. The sparsity check showed especially small minimum cohort sizes within **Ethnicity Minor** categories, and to a lesser extent in some vulnerable-status breakdowns. For example, the minimum observed subgroup denominator in Ethnicity Minor was **111**, far smaller than the large national categories used elsewhere. Consequently, the most extreme rankings for finely disaggregated ethnic groups should be interpreted as substantively important but potentially more sensitive to small-number variation than broad categories such as sex, FSM, or POLAR.

Second, trend inference is necessarily limited by the annual time series length. For POLAR there are only **14 annual observations**. The fitted slopes therefore support statements about the **direction and approximate average yearly change** over the period, but not stronger causal claims about policy interventions, regime changes, or post-pandemic structural breaks.

Third, the COVID-affected years should not be read as establishing a new long-run trajectory. They are best treated as recent descriptive observations in a period shaped by non-standard assessment, admissions, and progression conditions.

---

## POLAR inequality over time: overall progression to any HE

### Levels and trajectory

Figure `data/polar_trend_gaps.png` shows the long-run trajectories for POLAR quintiles Q1 and Q5. Across the full period, both groups increased their overall HE progression rates, but the increase was larger in percentage terms for the most disadvantaged group.

- **Q1 overall progression** rose from **18.0%** in **2009/10** to **31.7%** in **2022/23**.
- **Q5 overall progression** rose from **51.3%** to **62.1%** over the same period.

Because Q1 improved faster than Q5 in absolute terms, the **Q5–Q1 absolute gap in overall progression** narrowed:

- **2009/10**: **33.3 percentage points**
- **2022/23**: **30.4 percentage points**

The year-by-year series indicates that the overall gap was highest in the early years, peaking at **34.1 pp** in **2011/12**, then gradually declining to around **30–31 pp** in the later period. The shrinkage is real but limited in substantive magnitude: after 14 years, the gap remains about **30 percentage points**, meaning the most advantaged POLAR group still progresses to HE at nearly double the rate of the most disadvantaged group.

### Relative inequality

Relative inequality narrowed more sharply than the absolute gap because the disadvantaged baseline rate rose materially.

- The **overall Q5:Q1 progression ratio** fell from **2.85** in **2009/10** to **1.96** in **2022/23**.

Thus, by 2022/23 the most advantaged group was still progressing to HE at almost **twice** the rate of the most disadvantaged group, but this is substantially less unequal than the near-**threefold** disparity at the start of the series.

### Trend model

The linear trend fitted to the annual absolute POLAR gap confirms a statistically reliable narrowing:

- **Slope**: **−0.328 percentage points per year**
- **95% CI**: **[−0.412, −0.244]**
- **p < 0.001**
- **R² = 0.858**

Because the 95% confidence interval excludes zero, the evidence supports the conclusion that the **overall POLAR gap narrowed over 2009/10–2022/23**. The fit is strong in descriptive terms. The Durbin–Watson statistic of **1.88** does not suggest severe residual autocorrelation, so the simple trend line is an adequate summary of the broad direction.

The relative gap series shows an even stronger downward pattern:

- **Relative-gap slope**: **−0.074 per year**
- **95% CI**: **[−0.083, −0.066]**
- **p < 0.001**
- **R² = 0.969**

On both absolute and relative measures, then, the overall POLAR access gap has **narrowed**, not widened. However, the pace of change is modest relative to the size of the residual inequality.

---

## POLAR inequality over time: high-tariff progression

### Levels and trajectory

The picture changes sharply when attention shifts from any HE to high-tariff providers. Figure `data/polar_trend_gaps.png` shows that high-tariff participation remains low for Q1 throughout, while Q5 retains much higher access.

- **Q1 high-tariff progression** rose from **3.0%** in **2009/10** to **7.1%** in **2022/23**.
- **Q5 high-tariff progression** rose from **20.3%** to **26.8%**.

In relative terms, Q1 more than doubled from a very low base. Yet the absolute distance between groups remained extremely large and in the latest year was larger than at the start.

The **Q5–Q1 high-tariff absolute gap** was:

- **17.3 pp** in **2009/10**
- **19.7 pp** in **2022/23**

The series fluctuates around the high teens, with a visible increase in the most recent year. The COVID-affected period does not show a clean break in level, but it does show persistence of a large disadvantage and a marked widening in 2022/23.

### Relative inequality

The relative ratio tells a somewhat different story because Q1 begins from a very small denominator.

- **High-tariff Q5:Q1 ratio** fell from **6.58** in **2009/10** to **3.77** in **2022/23**.

Thus, proportional inequality narrowed: the most advantaged quintile moved from being about **6.6 times** as likely as Q1 pupils to enter high-tariff providers to about **3.8 times** as likely. But this should not be mistaken for parity or near-parity. When one group’s baseline is only 3–7%, even substantial proportional gains can coexist with a persistent and policy-salient absolute exclusion gap.

### Trend model

The linear trend for the **absolute** high-tariff gap indicates a statistically significant widening:

- **Slope**: **+0.125 percentage points per year**
- **95% CI**: **[+0.040, +0.210]**
- **p = 0.008**
- **R² = 0.460**

Because the confidence interval excludes zero, the evidence supports the conclusion that the **absolute POLAR high-tariff gap widened** over the period.

By contrast, the **relative** high-tariff ratio declined significantly:

- **Slope**: **−0.230 per year**
- **95% CI**: **[−0.256, −0.203]**
- **p < 0.001**
- **R² = 0.968**

This combination—**absolute widening but relative narrowing**—is substantively important. It indicates that disadvantaged students have improved their high-tariff progression rate from a very low base, but the advantaged group has retained or increased its absolute lead. In policy terms, the selective-provider pipeline remains structurally unequal even where proportional disparities have reduced.

---

## Contrasting overall access with selective access

The principal substantive finding is that **the story is more favourable for access to any HE than for access to high-tariff HE**.

### In 2022/23

For POLAR:

- **Overall progression**
  - Q1: **31.7%**
  - Q5: **62.1%**
  - Absolute gap: **30.4 pp**
  - Ratio: **1.96**

- **High-tariff progression**
  - Q1: **7.1%**
  - Q5: **26.8%**
  - Absolute gap: **19.7 pp**
  - Ratio: **3.77**

The high-tariff gap is smaller in percentage-point terms than the overall gap, but far larger in **proportional** terms. That is, selective institutions remain much more stratified than HE as a whole.

### Conversion Ratio: selectivity conditional on entering HE

The Conversion Ratio clarifies how much of the inequality arises after HE entry becomes possible. Figure `data/compounding_disadvantage.png` shows the 2022/23 percentage of HE entrants who go on to high-tariff providers.

For POLAR:

- **Q5 Conversion Ratio**: approximately **43.2%**
- **Q1 Conversion Ratio**: approximately **22.6%**
- **Selectivity penalty**: **20.6 pp**
- **Ratio**: **1.92×**

This means that among students who do progress to HE, those from the most advantaged POLAR quintile are almost **twice as likely** as those from the most disadvantaged quintile to enter a high-tariff institution. The disadvantage therefore does not end at HE entry; it intensifies within the distribution of institutional selectivity.

This is the core “compounding disadvantage” result. A disadvantaged group first faces lower overall progression; then, conditional on entering HE, it faces a second barrier in conversion into the selective segment.

---

## Cross-dimensional equity benchmarking in 2022/23

Figure `data/equity_benchmarking.png` and the ranking file `data/cross_dimensional_rankings.csv` compare the largest within-topic gaps for the latest year. The ranking uses the highest- and lowest-progressing categories within each breakdown topic and orders topics by the **absolute overall progression gap**.

### Ranked by overall HE progression gap

1. **Ethnicity Minor**: **72.5 pp**
   - Advantaged: **Chinese**
   - Disadvantaged: **Traveller of Irish Heritage**
   - Relative ratio: **7.30**
   - High-tariff gap: **44.1 pp**
   - High-tariff ratio: **9.65**

2. **SEN Provision**: **41.9 pp**
   - Advantaged: **No SEN provision**
   - Disadvantaged: **Education, health and care plan**
   - Relative ratio: **5.51**
   - High-tariff gap: **15.5 pp**
   - High-tariff ratio: **10.69**

3. **Children in Need**: **34.0 pp**
   - Advantaged: **All Other Pupils**
   - Disadvantaged: **Children in Need**
   - Relative ratio: **3.43**
   - High-tariff gap: **14.0 pp**
   - High-tariff ratio: **8.00**

4. **Looked After Status**: **32.0 pp**
   - Advantaged: **All Other Pupils**
   - Disadvantaged: **Looked after continuously for 12 months or more**
   - Relative ratio: **3.13**
   - High-tariff gap: **13.0 pp**
   - High-tariff ratio: **7.50**

5. **SEN Status**: **30.5 pp**
   - Advantaged: **No identified SEN**
   - Disadvantaged: **Any special educational need**
   - Relative ratio: **2.47**
   - High-tariff gap: **12.8 pp**
   - High-tariff ratio: **3.98**

6. **POLAR**: **30.4 pp**
   - Advantaged: **Q5**
   - Disadvantaged: **Q1**
   - Relative ratio: **1.96**
   - High-tariff gap: **19.7 pp**
   - High-tariff ratio: **3.77**

7. **Ethnicity Major**: **26.6 pp**
   - Advantaged: **Asian / Asian British**
   - Disadvantaged: **White**
   - Relative ratio: **1.64**
   - High-tariff gap: **10.4 pp**
   - High-tariff ratio: **1.76**

8. **FSM Status**: **20.8 pp**
   - Advantaged: **All Other Pupils**
   - Disadvantaged: **Free School Meals**
   - Relative ratio: **1.72**
   - High-tariff gap: **10.7 pp**
   - High-tariff ratio: **2.75**

9. **Disadvantage**: **19.9 pp**
   - Advantaged: **All Other Pupils**
   - Disadvantaged: **Disadvantaged**
   - Relative ratio: **1.62**
   - High-tariff gap: **11.2 pp**
   - High-tariff ratio: **2.62**

10. **First Language**: **17.1 pp**
    - Advantaged: **Other than English**
    - Disadvantaged: **English**
    - Relative ratio: **1.39**
    - High-tariff gap: **4.1 pp**
    - High-tariff ratio: **1.28**

11. **Sex**: **13.2 pp**
    - Advantaged: **Female**
    - Disadvantaged: **Male**
    - Relative ratio: **1.33**
    - High-tariff gap: **4.5 pp**
    - High-tariff ratio: **1.34**

### Interpretation of the ranking

Three substantive points follow.

First, **area disadvantage is important but not uniquely dominant**. POLAR ranks in the middle of the distribution: a very large gap remains, but some other dimensions show even larger inequalities, especially when highly vulnerable groups or finely disaggregated ethnic groups are examined.

Second, **SEN- and care-related vulnerabilities stand out strongly**. The gaps for SEN provision, children in need, and looked-after status all exceed or closely match the POLAR gap in overall HE progression. This suggests that educational vulnerability and social care exposure are major lines of stratification in post-19 progression.

Third, detailed ethnicity shows the **largest internal disparities**, but these results require careful interpretation because some categories are small. The Chinese versus Traveller of Irish Heritage contrast is undeniably large in the published data, but because Ethnicity Minor includes very small cohorts in some years, this ranking should be interpreted as a marker of severe inequality rather than a precision-equivalent comparator to broad national categories.

---

## Compounding disadvantage and selectivity penalties

Figure `data/compounding_disadvantage.png` provides the clearest demonstration that inequality compounds between “any HE” and “high-tariff HE”. For selected major dimensions in 2022/23, the Conversion Ratio gaps are:

- **POLAR (Q5 vs Q1)**: **20.6 pp**, ratio **1.92×**
- **Disadvantage (Other vs Disadvantaged)**: **13.1 pp**, ratio **1.61×**
- **FSM Status (Other vs FSM)**: **12.5 pp**, ratio **1.59×**
- **SEN Status (No SEN vs Any SEN)**: **12.8 pp**, ratio **1.62×**
- **Sex (Female vs Male)**: **0.5 pp**, ratio **1.01×**

These results help disentangle two mechanisms.

### 1. Access barriers into HE

Disadvantaged groups are already less likely to enter HE at all. This is visible in the overall progression gaps for POLAR, FSM, disadvantage, and SEN.

### 2. Selective allocation within HE

Conditional on entering HE, disadvantaged groups then have a lower probability of entering a high-tariff provider. The size of this within-HE selectivity penalty is substantial for POLAR, disadvantage, FSM, and SEN, but negligible for sex.

This matters for policy interpretation. A small sex difference in Conversion Ratio despite a larger overall HE gap implies that male disadvantage is concentrated more in **entering HE** than in **selective allocation once in HE**. By contrast, POLAR, FSM, and SEN exhibit both kinds of penalty. These dimensions are therefore associated with a more structurally layered form of inequality.

The POLAR case is particularly stark. In 2022/23, roughly **43%** of HE entrants from Q5 went to a high-tariff provider, compared with about **23%** from Q1. Thus, even once access to HE has been achieved, the disadvantaged group remains sharply under-represented in the selective sector.

---

## Reading the COVID-affected period

The period from **2020/21 to 2022/23** is shaded in Figure `data/polar_trend_gaps.png` and should be interpreted descriptively. Several observations are relevant.

- The **overall POLAR gap** stayed close to **30 pp** during this period:
  - **29.7 pp** in 2020/21
  - **30.1 pp** in 2021/22
  - **30.4 pp** in 2022/23

- The **high-tariff POLAR gap** remained high and then increased:
  - **17.8 pp** in 2020/21
  - **18.1 pp** in 2021/22
  - **19.7 pp** in 2022/23

These years do not overturn the long-run findings, but they do underscore that the selective gap has not eased in recent observations. Since only three post-2020 points are available, and because these years were shaped by exceptional admissions and assessment conditions, the prudent interpretation is that the COVID-affected period **did not produce visible convergence at the selective end**. It may instead have preserved or accentuated pre-existing inequality, but the present design does not support stronger causal attribution.

---

## Policy-oriented interpretation

From a widening participation perspective, the evidence supports four principal conclusions.

### 1. Access to any HE has become somewhat more equal, but inequality remains entrenched

The POLAR overall gap narrowed significantly by about **0.33 pp per year**, and the relative ratio fell from **2.85** to **1.96**. This is meaningful progress, but it is not transformation. In 2022/23, the most advantaged POLAR quintile still had an overall progression rate of **62.1%**, against **31.7%** for the most disadvantaged.

### 2. Selective higher education remains markedly less equal than higher education overall

For high-tariff providers, the absolute POLAR gap **widened** by about **0.13 pp per year** on average. The 2022/23 gap of **19.7 pp** is larger than in 2009/10. The proportional gap has narrowed, but primarily because disadvantaged groups improved from extremely low starting points. The selective pipeline therefore remains substantially more stratified than the HE system as a whole.

### 3. Disadvantage is multi-dimensional

POLAR is not the only, or always the largest, cleavage. In 2022/23, very large inequalities were also evident by **SEN provision**, **care-related status**, and **detailed ethnicity**. A policy framework focused too narrowly on area disadvantage would miss other major forms of educational exclusion.

### 4. Some inequalities are compounded after HE entry

The Conversion Ratio results show that for POLAR, FSM, disadvantage, and SEN, the path from school to selective HE contains two hurdles: lower overall progression and lower conversion into high-tariff institutions among those who do progress. This is why high-tariff equity cannot be inferred from overall HE participation alone.

---

## Concluding statement

Taken together, the figures and tables show a system in which **headline access has improved more than selective access**. The long-run trend for POLAR indicates that **overall participation gaps are narrowing**, but only gradually. At the same time, the gap in access to **high-tariff institutions has widened in absolute terms**, and the Conversion Ratio evidence shows that this is not simply a reflection of lower HE participation overall: disadvantaged groups are also less likely to convert HE entry into selective HE entry.

The latest-year benchmarking reinforces the broader policy message. Structural inequality in English higher education is not reducible to a single disadvantage measure. Area disadvantage, FSM, SEN, care experience, and ethnicity all reveal substantial and in some cases severe disparities. For policy audiences, the practical implication is that widening participation should be judged not only by whether more disadvantaged pupils enter higher education, but also by **where they enter**, because institutional selectivity remains a major site of persistent inequality.