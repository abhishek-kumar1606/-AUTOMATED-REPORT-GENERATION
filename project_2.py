import pandas as pd
import matplotlib.pyplot as plt
from fpdf import FPDF

# Step 1: Read data
df = pd.read_csv("data.csv")

# Step 2: Analyze data
total_sales = df["Sales"].sum()
average_sales = df["Sales"].mean()
max_sales = df["Sales"].max()
min_sales = df["Sales"].min()

# Step 3: Create a simple chart
plt.plot(df["Date"], df["Sales"], marker="o", color="blue")
plt.title("Daily Sales")
plt.xlabel("Date")
plt.ylabel("Sales ($)")
plt.grid(True)
plt.tight_layout()
plt.savefig("sales_chart.png")
plt.close()

# Step 4: Generate PDF report
pdf = FPDF()
pdf.add_page()

pdf.set_font("Arial", "B", 16)
pdf.cell(0, 10, "Sales Report", ln=True, align="C")

pdf.set_font("Arial", "", 12)
pdf.ln(10)
pdf.cell(0, 10, f"Total Sales: ${total_sales:,.2f}", ln=True)
pdf.cell(0, 10, f"Average Sales: ${average_sales:,.2f}", ln=True)
pdf.cell(0, 10, f"Highest Sales: ${max_sales:,.2f}", ln=True)
pdf.cell(0, 10, f"Lowest Sales: ${min_sales:,.2f}", ln=True)

pdf.ln(10)
pdf.image("sales_chart.png", x=30, w=150)

pdf.output("Simple_Sales_Report.pdf")

print("✅ Report generated: Simple_Sales_Report.pdf")
