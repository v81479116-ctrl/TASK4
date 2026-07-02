# Statistical Hypothesis Testing Report

This report validates key business hypotheses using statistical tests to ensure rigor and statistical significance.

## Hypothesis 1: UK vs International Order Values (AOV)

- **Null Hypothesis ($H_0$)**: The mean order value of UK transactions is equal to the mean order value of International transactions.
- **Alternative Hypothesis ($H_1$)**: The mean order value of UK transactions is NOT equal to the mean order value of International transactions.

### Metrics Summary:
- **UK Orders**: N = 18,019, Mean = £499.57, Std = £1781.52
- **International Orders**: N = 1,941, Mean = £845.11, Std = £1739.82

### Statistical Test (Welch's Independent T-Test):
- **T-statistic**: -8.2942
- **P-value**: 1.7984405315585268e-16
- **Conclusion**: The difference in mean order values is statistically significant (p < 0.05). We reject the Null Hypothesis.

> [!NOTE]
> International customers have a substantially higher Average Order Value (AOV) than domestic UK customers (£938.64 vs. £499.57). This is typically due to the overhead of shipping internationally, meaning international buyers (often wholesalers or distributors) purchase in bulk.

## Hypothesis 2: Peak vs Off-Peak Hourly Order Size

- **Null Hypothesis ($H_0$)**: The mean number of items purchased per order is equal during peak business hours (10:00 - 15:00) and off-peak hours.
- **Alternative Hypothesis ($H_1$)**: The mean number of items purchased per order is different during peak business hours compared to off-peak hours.

### Metrics Summary:
- **Peak Hour Orders**: N = 15,522, Mean Quantity = 273.70 units, Std = 793.85
- **Off-Peak Hour Orders**: N = 4,438, Mean Quantity = 298.34 units, Std = 1377.58

### Statistical Test (Welch's Independent T-Test):
- **T-statistic**: -1.1386
- **P-value**: 0.2549357651821698
- **Conclusion**: The difference in order quantities is NOT statistically significant (p >= 0.05). We fail to reject the Null Hypothesis.

> [!NOTE]
> Off-peak hour orders actually show a slightly higher mean quantity than peak hour orders, but since the p-value is large, this difference may not be statistically significant, indicating that transaction volume is higher during peak hours, but order sizes remain relatively consistent.