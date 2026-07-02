# Data Storytelling & Business Intelligence Report

**Author**: Data Analytics Intern  
**Company**: ApexPlanet Software Pvt. Ltd.  
**Dataset**: Online Retail Transactions (Dec 2010 - Dec 2011)

---

## 1. Executive Summary

This report provides a data-driven narrative of our online retail operations. By analyzing **534,129 transactions** spanning a 12-month period, we identify key growth drivers, diagnose seasonal and operational patterns, segment our customer base using RFM (Recency, Frequency, Monetary) modeling, and statistically validate differences in purchasing behaviors.

### Core Metrics Summary:
- **Total Net Revenue**: £9.74 Million (£9,742,030.56)
- **Total Completed Orders**: 19,960
- **Total Registered Customers**: 4,321
- **Average Order Value (AOV)**: £488.08
- **Customer Retention Rate**: 65.58%

---

## 2. Data Immersion & Wrangling Summary

Prior to conducting our analysis, a rigorous data cleaning process was executed to address several quality concerns in the raw dataset:
1. **Encoding Issues**: Handled non-UTF-8 characters (e.g., British Pound symbol `£`) using `ISO-8859-1` encoding.
2. **Missing Customer IDs**: Approximately 25% of transactions lacked a `CustomerID`. These rows were preserved for revenue calculation by mapping them to unique placeholder IDs (`Guest_<InvoiceNo>`) to prevent data loss.
3. **Anomalies and Outliers**:
   - Dropped 5,268 duplicate transactions.
   - Flagged cancellations (marked by invoice prefix 'C') and filtered out transactions with negative/zero quantities that were not cancellations (mostly damaged/lost inventory write-offs).
   - Removed zero-price transactions (free giveaways, manual entries) to keep financial metrics clean.

---

## 3. Business Performance Insights (SQL & EDA)

### Monthly Sales Trends
The sales distribution shows strong seasonality, with peak revenue during the holiday season.

- **Peak Month**: November 2011 generated the highest revenue of **£1.46 Million** (15% of total annual sales) and engaged **1,835 active customers**.
- **Low Point**: February 2011 recorded the lowest sales at **£497,026**.
- **Observation**: There is a clear upward trend from September through November, corresponding to holiday inventory preparation by retailers.

### Geographic Revenue Distribution
While the United Kingdom remains our core market (representing **92.4%** of total revenue), international expansion exhibits strong growth.
- **Top 5 International Markets by Revenue**:
  1. **Netherlands**: £285,446.34 (9 customers, AOV: £3,036.66)
  2. **EIRE (Ireland)**: £283,140.52 (31 customers, AOV: £983.13)
  3. **Germany**: £228,678.40 (94 customers, AOV: £500.39)
  4. **France**: £209,625.37 (90 customers, AOV: £534.76)
  5. **Australia**: £138,453.81 (9 customers, AOV: £2,429.01)

---

## 4. Customer Segmentation Deep-Dive (RFM Analysis)

Using Recency, Frequency, and Monetary scores, our **4,321 registered customers** were classified into distinct strategic segments:

| Customer Segment | Customer Count | Percentage | Business Rationale & Action Plan |
| :--- | :--- | :--- | :--- |
| **Loyal Customers** | 1,165 | 26.96% | Buy frequently and recently. *Strategy: Introduce loyalty rewards and cross-sell premium products.* |
| **Lost** | 981 | 22.70% | Long time since last purchase, low frequency, and low spend. *Strategy: Do not spend heavily on re-acquisition. Focus on other cohorts.* |
| **About to Sleep** | 857 | 19.83% | Below average recency and frequency. *Strategy: Re-engage with personalized discounts or 'We Miss You' campaigns.* |
| **Champions** | 804 | 18.61% | Highly recent, frequent, and top-spending customers. *Strategy: Offer early access to new products, personalized rewards, and premium support.* |
| **Recent/New Customers** | 205 | 4.74% | Purchased very recently but only once. *Strategy: Welcome emails, introductory guides, and second-purchase incentives.* |
| **At Risk** | 175 | 4.05% | High frequency and spend historically, but haven't purchased in a long time. *Strategy: Immediate outreach, feedback surveys, and win-back offers.* |
| **Promising Customers** | 134 | 3.10% | Average recency and spend, showing potential. *Strategy: Target with product recommendation engines to increase purchase frequency.* |

---

## 5. Statistical Validation (Hypothesis Testing)

To ensure our findings are robust and not random noise, we formulated and tested two primary hypotheses:

### Hypothesis 1: UK vs. International Order Value
- **Null Hypothesis ($H_0$)**: Mean order value of UK transactions = Mean order value of International transactions.
- **Result**: Welch's T-Test yielded a **T-statistic of -8.29** and a **P-value of $1.8 \times 10^{-16}$** (p < 0.05).
- **Conclusion**: **Reject the Null Hypothesis.** International orders have a statistically significant higher average order value (£845.11) compared to UK orders (£499.57). 
- **Business Interpretation**: International customers (such as those in the Netherlands and Australia) are primarily B2B buyers importing goods in bulk, leading to higher AOV to offset international shipping logistics.

### Hypothesis 2: Peak vs. Off-Peak Order Sizes
- **Null Hypothesis ($H_0$)**: Mean order quantity during peak hours (10:00 - 15:00) = Mean order quantity during off-peak hours.
- **Result**: Welch's T-Test yielded a **T-statistic of -1.14** and a **P-value of 0.255** (p >= 0.05).
- **Conclusion**: **Fail to reject the Null Hypothesis.**
- **Business Interpretation**: While peak hours handle the vast majority of invoice volume, the actual quantity of items per order does not significantly differ between busy and quiet times. Order size is consistent throughout the day.

---

## 6. Strategic Recommendations

1. **Leverage B2B International Buyers**:
   - Since international orders represent significantly higher order values (AOV: £845.11 vs £499.57), introduce tailored volume discounts and optimized shipping tiers for top international hubs (Netherlands, Australia, EIRE).
2. **Win Back 'At Risk' Customers**:
   - 175 of our historically high-value customers (At Risk) are slipping away. Deploy automated, targeted reactivation email campaigns highlighting new arrivals or offering free shipping.
3. **Nurture New Customers**:
   - Convert the **205 Recent/New Customers** into Loyal Customers by offering a "second order discount" within 14 days of their first purchase.
4. **Capitalize on Peak Ordering Times**:
   - Align live customer chat, warehouse staffing, and flash sales to the peak window between **10:00 AM and 3:00 PM**, where over 70% of transactions occur.