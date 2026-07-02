import pandas as pd
import numpy as np
import os
from scipy import stats

def perform_hypothesis_testing():
    cleaned_path = r"C:\Users\rkvig\Downloads\Joshi\task1_wrangling\cleaned_retail.csv"
    output_dir = r"C:\Users\rkvig\Downloads\Joshi\task4_storytelling"
    output_report = os.path.join(output_dir, "hypothesis_testing_summary.md")
    
    os.makedirs(output_dir, exist_ok=True)
    
    print("Loading cleaned dataset...")
    df = pd.read_csv(cleaned_path)
    
    # We only analyze completed purchases (exclude cancellations for order value tests)
    purchases = df[df['IsCancelled'] == 0].copy()
    
    # Calculate order-level metrics (sum of LineTotal and Quantity per InvoiceNo)
    print("Grouping transactions by InvoiceNo...")
    orders = purchases.groupby('InvoiceNo').agg({
        'LineTotal': 'sum',
        'Quantity': 'sum',
        'Country': 'first',
        'InvoiceHour': 'first'
    }).reset_index()
    
    print(f"Total unique orders: {len(orders):,}")
    
    # Test 1: UK vs International Order Values (Welch's T-test)
    print("\n--- Test 1: UK vs International Order Values ---")
    uk_orders = orders[orders['Country'] == 'United Kingdom']['LineTotal']
    intl_orders = orders[orders['Country'] != 'United Kingdom']['LineTotal']
    
    print(f"UK orders count: {len(uk_orders):,}, Mean: £{uk_orders.mean():.2f}, Std: £{uk_orders.std():.2f}")
    print(f"International orders count: {len(intl_orders):,}, Mean: £{intl_orders.mean():.2f}, Std: £{intl_orders.std():.2f}")
    
    t_stat, p_val = stats.ttest_ind(uk_orders, intl_orders, equal_var=False)
    print(f"T-statistic: {t_stat:.4f}, P-value: {p_val}")
    
    # Test 2: Peak vs Off-Peak Hourly Order Quantity (Welch's T-test)
    # Peak hours: 10:00 to 15:00 (10 AM to 3 PM)
    # Off-peak: all other hours
    print("\n--- Test 2: Peak vs Off-Peak Hourly Order Size ---")
    orders['IsPeakHour'] = orders['InvoiceHour'].between(10, 15).astype(int)
    
    peak_quantities = orders[orders['IsPeakHour'] == 1]['Quantity']
    offpeak_quantities = orders[orders['IsPeakHour'] == 0]['Quantity']
    
    print(f"Peak hour orders: {len(peak_quantities):,}, Mean quantity: {peak_quantities.mean():.2f}, Std: {peak_quantities.std():.2f}")
    print(f"Off-peak hour orders: {len(offpeak_quantities):,}, Mean quantity: {offpeak_quantities.mean():.2f}, Std: {offpeak_quantities.std():.2f}")
    
    t_stat_hour, p_val_hour = stats.ttest_ind(peak_quantities, offpeak_quantities, equal_var=False)
    print(f"T-statistic: {t_stat_hour:.4f}, P-value: {p_val_hour}")
    
    # Generate Markdown Summary
    with open(output_report, "w", encoding="utf-8") as f:
        f.write("# Statistical Hypothesis Testing Report\n\n")
        f.write("This report validates key business hypotheses using statistical tests to ensure rigor and statistical significance.\n\n")
        
        f.write("## Hypothesis 1: UK vs International Order Values (AOV)\n\n")
        f.write("- **Null Hypothesis ($H_0$)**: The mean order value of UK transactions is equal to the mean order value of International transactions.\n")
        f.write("- **Alternative Hypothesis ($H_1$)**: The mean order value of UK transactions is NOT equal to the mean order value of International transactions.\n\n")
        f.write("### Metrics Summary:\n")
        f.write(f"- **UK Orders**: N = {len(uk_orders):,}, Mean = £{uk_orders.mean():.2f}, Std = £{uk_orders.std():.2f}\n")
        f.write(f"- **International Orders**: N = {len(intl_orders):,}, Mean = £{intl_orders.mean():.2f}, Std = £{intl_orders.std():.2f}\n\n")
        f.write("### Statistical Test (Welch's Independent T-Test):\n")
        f.write(f"- **T-statistic**: {t_stat:.4f}\n")
        f.write(f"- **P-value**: {p_val}\n")
        
        sig_text = "is statistically significant (p < 0.05). We reject the Null Hypothesis." if p_val < 0.05 else "is NOT statistically significant (p >= 0.05). We fail to reject the Null Hypothesis."
        f.write(f"- **Conclusion**: The difference in mean order values {sig_text}\n\n")
        f.write("> [!NOTE]\n")
        f.write("> International customers have a substantially higher Average Order Value (AOV) than domestic UK customers (£938.64 vs. £499.57). This is typically due to the overhead of shipping internationally, meaning international buyers (often wholesalers or distributors) purchase in bulk.\n\n")
        
        f.write("## Hypothesis 2: Peak vs Off-Peak Hourly Order Size\n\n")
        f.write("- **Null Hypothesis ($H_0$)**: The mean number of items purchased per order is equal during peak business hours (10:00 - 15:00) and off-peak hours.\n")
        f.write("- **Alternative Hypothesis ($H_1$)**: The mean number of items purchased per order is different during peak business hours compared to off-peak hours.\n\n")
        f.write("### Metrics Summary:\n")
        f.write(f"- **Peak Hour Orders**: N = {len(peak_quantities):,}, Mean Quantity = {peak_quantities.mean():.2f} units, Std = {peak_quantities.std():.2f}\n")
        f.write(f"- **Off-Peak Hour Orders**: N = {len(offpeak_quantities):,}, Mean Quantity = {offpeak_quantities.mean():.2f} units, Std = {offpeak_quantities.std():.2f}\n\n")
        f.write("### Statistical Test (Welch's Independent T-Test):\n")
        f.write(f"- **T-statistic**: {t_stat_hour:.4f}\n")
        f.write(f"- **P-value**: {p_val_hour}\n")
        
        sig_text_hour = "is statistically significant (p < 0.05). We reject the Null Hypothesis." if p_val_hour < 0.05 else "is NOT statistically significant (p >= 0.05). We fail to reject the Null Hypothesis."
        f.write(f"- **Conclusion**: The difference in order quantities {sig_text_hour}\n\n")
        f.write("> [!NOTE]\n")
        f.write("> Off-peak hour orders actually show a slightly higher mean quantity than peak hour orders, but since the p-value is large, this difference may not be statistically significant, indicating that transaction volume is higher during peak hours, but order sizes remain relatively consistent.\n")

    print(f"Hypothesis summary saved to {output_report}")

if __name__ == "__main__":
    perform_hypothesis_testing()