# Sales Data Analysis (Python, Pandas, Matplotlib)

This project performs exploratory data analysis (EDA) on a retail sales dataset (`sales_data_sample.csv`).  
It demonstrates data cleaning, aggregation with Pandas, visualizations with Matplotlib, and basic business insights for an e‑commerce / retail context. AI assistance (Perplexity AI) was used for debugging, structuring the analysis, and refining insights.

---

## 🚀 Project Goals

- Clean a raw sales dataset (nulls, duplicates, inconsistent values).
- Analyze monthly sales performance.
- Identify top‑selling products.
- Evaluate product line (category) performance.
- Detect repeat customers and low‑performing categories (optional extension).
- Present clear, business‑oriented insights supported by charts.

---

## 📂 Dataset

**File:** `sales_data_sample.csv`  
Each row represents an order line item.

**Key columns used:**

- `ORDERNUMBER` – Unique order ID  
- `ORDERDATE` – Date of the order  
- `STATUS` – Order status (e.g., Shipped, Cancelled)  
- `PRODUCTCODE` – Product identifier  
- `PRODUCTLINE` – Product category (Classic Cars, Vintage Cars, etc.)  
- `QUANTITYORDERED` – Units ordered  
- `PRICEEACH` – Unit price  
- `SALES` – Line revenue (quantity × price)  
- `CUSTOMERNAME` – Customer name  

Only orders with `STATUS == 'Shipped'` are used in the analysis.

---

## 🧹 Data Cleaning Steps

The script `data_clean.py` performs:

1. **Loading data**
   - Reads `sales_data_sample.csv` with correct encoding.

2. **Handling missing values**
   - Fills missing `ADDRESSLINE2` with `"N/A"`.
   - Fills missing `STATE` with `"Unknown"`.
   - Fills missing `POSTALCODE` with `"00000"`.

3. **Removing duplicates**
   - Drops duplicate rows based on `ORDERNUMBER` and `ORDERLINENUMBER`.

4. **Date conversion and filtering**
   - Converts `ORDERDATE` to a proper datetime type.
   - Filters rows to keep only `STATUS == 'Shipped'`.

5. **Feature engineering**
   - Creates `ORDER_MONTH` by extracting the year‑month from `ORDERDATE` for time‑series analysis.

These steps ensure the analysis is based on clean, reliable, and business‑valid sales data.

---

## 📊 Analysis & Visualizations

All analysis is done in `data_clean.py` using Pandas and Matplotlib.

### 1. Monthly Sales Trend

- Groups data by `ORDER_MONTH` and sums `SALES`.
- Plots a line chart showing **monthly revenue over time**.
- Helps identify growth, seasonality, and peak months (e.g., strong Q4 performance).

**Business use:**  
Understand seasonality, forecast demand, and plan inventory/marketing around high‑revenue months.

---

### 2. Top 10 Products by Sales

- Groups by `PRODUCTCODE` and sums `SALES`.
- Sorts in descending order and selects the **top 10 products**.
- Plots a horizontal bar chart of `PRODUCTCODE` vs total `SALES`.

**Business use:**  
Identify the key revenue‑driving SKUs and prioritize them for stock, pricing, and promotions.

---

### 3. Sales by Product Line (Category)

- Groups by `PRODUCTLINE` and sums `SALES`.
- Plots a bar chart showing revenue by product line (e.g., Classic Cars, Vintage Cars, Motorcycles, etc.).

**Business use:**  
- Understand which categories drive most revenue.
- Spot low‑performing categories that may need a change in pricing, promotion, or catalog strategy.

---

### 4. Repeat Customers (Console Output)

- Groups by `CUSTOMERNAME` and counts unique `ORDERNUMBER` values.
- Identifies customers with more than one order as **repeat customers**.
- Prints the top 50 repeat customers and their order counts in the console.

**Business use:**  
Helps identify loyal customers for retention campaigns, loyalty programs, and targeted marketing.

---

## 💡 Example Business Insights

From this analysis, a decision‑maker can derive insights such as:

- Which months have the highest and lowest sales.
- Which 10 products contribute the most to total revenue.
- Which product lines are high‑performing vs low‑performing.
- How many customers buy repeatedly and who they are.

These insights can support actions like inventory planning, pricing, targeted discounts, and category strategy.

---

## 🛠️ Tech Stack

- **Language:** Python  
- **Libraries:** 
  - `pandas` for data loading, cleaning, and aggregation  
  - `matplotlib` for visualizations  
- **Tools:** VS Code / any Python IDE, Git, GitHub  
- **AI Used:** Perplexity AI was used for:
  - Debugging groupby and plotting issues
  - Structuring the EDA flow
  - Drafting this README and business interpretations

---

## ▶️ How to Run

1. Clone the repository or copy the project folder.
2. Place `sales_data_sample.csv` in the project root (or `data/` if you adjust the path).
3. Install dependencies:
   ```bash
   pip install pandas matplotlib
   ```
4. Run the analysis script:
   ```bash
   python data_clean.py
   ```
5. The script will:
   - Show three charts (monthly sales, top products, product line sales).
   - Print top repeat customers in the terminal.

---

## 📦 Possible Extensions

- Add SQL version of the analysis (load CSV into SQLite/MySQL and run equivalent queries).
- Save charts as PNG files and embed them directly in this README.
- Add more metrics (average order value, country‑wise sales, deal size analysis).
- Wrap analysis into a Jupyter notebook for an interactive portfolio presentation.

---

## 👤 Author

- **Krishna Bhatia** – Data Science & Analytics Enthusiast  
- **AI Collaboration** – Perplexity AI (support for coding, debugging, and documentation)

Feel free to fork, modify, or extend this project for your own portfolio or learning.
