import os
import pandas as pd
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import seaborn as sns

# Ensure display function exists when running as a standalone script
try:
    from IPython.display import display
except Exception:
    def display(*args):
        for arg in args:
            print(arg)

# Automatically save all figures to output_plots directory
os.makedirs("output_plots", exist_ok=True)
_fig_counter = 1

def _show_and_save():
    global _fig_counter
    filename = f"output_plots/figure_{_fig_counter:02d}.png"
    plt.savefig(filename, bbox_inches="tight", dpi=150)
    print(f"  [Saved plot to {filename}]")
    plt.close()
    _fig_counter += 1

plt.show = _show_and_save

pd.set_option("display.max_columns", None)
pd.set_option("display.float_format", lambda x: f"{x:,.2f}")

df = pd.read_csv("seasonal_agriculture_performance_dataset.csv")

print("Rows:", df.shape[0])
print("Columns:", df.shape[1])

# NaN

#data type and non null counts
display(df.head())
print("Shape:", df.shape)
display(df.dtypes.to_frame("Data Type"))
df.info()

# NaN

missing = df.isnull().sum()
print("Missing Values:")
display(missing[missing > 0].to_frame("Count"))

print("Missing Value Percentage:")
display((missing[missing > 0] / len(df) * 100).round(2).to_frame("Percentage"))

print("Duplicate Records:", df.duplicated().sum())

# NaN

#numerical summary statistics
df.describe()

# NaN

df = df.drop_duplicates().copy()

numeric_cols = df.select_dtypes(include=np.number).columns
categorical_cols = df.select_dtypes(include="object").columns

for col in numeric_cols:
    if df[col].isnull().sum() > 0:
        df[col] = df[col].fillna(df[col].median())

for col in categorical_cols:
    if df[col].isnull().sum() > 0:
        df[col] = df[col].fillna(df[col].mode()[0])

print("Missing Values After Cleaning:", df.isnull().sum().sum())
print("Duplicate Records After Cleaning:", df.duplicated().sum())


# NaN

display(df.describe().T)

for col in ["State", "District", "Crop", "Season", "Irrigation_Method"]:
    print("\n" + col)
    display(df[col].value_counts().to_frame("Count"))

# NaN

outlier_results = []

for col in numeric_cols:
    q1 = df[col].quantile(0.25)
    q3 = df[col].quantile(0.75)
    iqr = q3 - q1
    lower = q1 - 1.5 * iqr
    upper = q3 + 1.5 * iqr
    count = ((df[col] < lower) | (df[col] > upper)).sum()
    outlier_results.append([col, q1, q3, lower, upper, count])

outlier_df = pd.DataFrame(
    outlier_results,
    columns=["Variable", "Q1", "Q3", "Lower Limit", "Upper Limit", "Outlier Count"]
).sort_values("Outlier Count", ascending=False)

display(outlier_df)

# NaN

# Median and standard deviation

statistical_summary = pd.DataFrame({
    "Mean": df[numeric_cols].mean(),
    "Median": df[numeric_cols].median(),
    "Std_Dev": df[numeric_cols].std(),
    "Min": df[numeric_cols].min(),
    "Max": df[numeric_cols].max()
})

statistical_summary

# NaN

# Seasonal descriptive summary

season_summary = df.groupby("Season")[numeric_cols].agg(["mean", "median", "std"])
season_summary

# NaN

for col in [
    "Yield_Tonnes_Ha",
    "Profit_INR",
    "Revenue_INR",
    "Rainfall_mm",
    "Water_Used_m3",
    "Disease_Pest_Risk_pct"
]:
    plt.figure(figsize=(8, 4))
    sns.boxplot(x=df[col])
    plt.title(f"Outlier Analysis: {col}")
    plt.xlabel(col)
    plt.tight_layout()
    plt.show()

# NaN

df.sample(5, random_state=42)

# NaN

#sesson distribution
plt.figure(figsize=(8, 5))
sns.countplot(data=df, x="Season")
plt.title("Number of Records by Season")
plt.xlabel("Season")
plt.ylabel("Count")
plt.tight_layout()
plt.show()

plt.figure(figsize=(10, 5))
sns.countplot(data=df, x="Crop")
plt.title("Number of Records by Crop")
plt.xlabel("Crop")
plt.ylabel("Count")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# NaN

# Univariate: Yield distribution

plt.figure(figsize=(8, 5))
sns.histplot(data=df, x="Yield_Tonnes_Ha", kde=True)
plt.title("Distribution of Agricultural Yield")
plt.xlabel("Yield (tonnes/ha)")
plt.ylabel("Frequency")
plt.tight_layout()
plt.show()

# NaN

# Univariate: Rainfall distribution

plt.figure(figsize=(8, 5))
sns.histplot(data=df, x="Rainfall_mm", kde=True, color="teal")
plt.title("Distribution of Rainfall (mm)")
plt.xlabel("Rainfall (mm)")
plt.ylabel("Frequency")
plt.tight_layout()
plt.show()

# NaN

# Univariate: Profit distribution

plt.figure(figsize=(8, 5))
sns.histplot(data=df, x="Profit_INR", kde=True, color="coral")
plt.title("Distribution of Profit (INR)")
plt.xlabel("Profit (INR)")
plt.ylabel("Frequency")
plt.tight_layout()
plt.show()

# NaN

plt.figure(figsize=(9, 5))
sns.boxplot(data=df, x="Season", y="Yield_Tonnes_Ha")
plt.title("Yield Across Seasons")
plt.xlabel("Season")
plt.ylabel("Yield (Tonnes/Ha)")
plt.tight_layout()
plt.show()

plt.figure(figsize=(9, 5))
sns.boxplot(data=df, x="Season", y="Profit_INR")
plt.title("Profit Across Seasons")
plt.xlabel("Season")
plt.ylabel("Profit (INR)")
plt.tight_layout()
plt.show()

plt.figure(figsize=(9, 5))
sns.scatterplot(data=df, x="Rainfall_mm", y="Yield_Tonnes_Ha", hue="Season")
plt.title("Rainfall vs Yield")
plt.xlabel("Rainfall (mm)")
plt.ylabel("Yield (Tonnes/Ha)")
plt.tight_layout()
plt.show()

# NaN

# Univariate: Season distribution (Pie Chart)

plt.figure(figsize=(7, 7))
df['Season'].value_counts().plot.pie(autopct='%1.1f%%', startangle=90, cmap='viridis')
plt.title('Distribution of Records by Season')
plt.ylabel('')  # Hide the default 'Season' label on the y-axis
plt.tight_layout()
plt.show()

# NaN

season_crop = df.groupby(
    ["Season", "Crop"],
    observed=True
).agg(
    Average_Yield=("Yield_Tonnes_Ha", "mean"),
    Average_Profit=("Profit_INR", "mean"),
    Average_Revenue=("Revenue_INR", "mean"),
    Average_Water_Efficiency=("Water_Efficiency_t_per_1000m3", "mean"),
    Average_Disease_Risk=("Disease_Pest_Risk_pct", "mean")
).reset_index()

display(season_crop.sort_values("Average_Profit", ascending=False).head(15))

yield_pivot = df.pivot_table(
    index="Season",
    columns="Crop",
    values="Yield_Tonnes_Ha",
    aggfunc="mean",
    observed=True
)

plt.figure(figsize=(12, 6))
sns.heatmap(yield_pivot, annot=True, fmt=".2f", cmap="YlGnBu")
plt.title("Average Yield by Season and Crop")
plt.xlabel("Crop")
plt.ylabel("Season")
plt.tight_layout()
plt.show()

# NaN

correlation = df.select_dtypes(include=np.number).corr()

plt.figure(figsize=(16, 12))
sns.heatmap(correlation, center=0, cmap="coolwarm")
plt.title("Correlation Matrix")
plt.tight_layout()
plt.show()

yield_corr = correlation["Yield_Tonnes_Ha"].drop("Yield_Tonnes_Ha")
yield_corr = yield_corr.reindex(yield_corr.abs().sort_values(ascending=False).index)

profit_corr = correlation["Profit_INR"].drop("Profit_INR")
profit_corr = profit_corr.reindex(profit_corr.abs().sort_values(ascending=False).index)

print("Top correlations with Yield")
display(yield_corr.head(10).to_frame("Correlation"))

print("Top correlations with Profit")
display(profit_corr.head(10).to_frame("Correlation"))


# NaN

season_summary = df.groupby(
    "Season",
    observed=True
).agg(
    Average_Yield=("Yield_Tonnes_Ha", "mean"),
    Average_Production=("Production_Tonnes", "mean"),
    Average_Revenue=("Revenue_INR", "mean"),
    Average_Cost=("Total_Cost_INR", "mean"),
    Average_Profit=("Profit_INR", "mean"),
    Average_Rainfall=("Rainfall_mm", "mean"),
    Average_Temperature=("Avg_Temperature_C", "mean"),
    Average_Humidity=("Humidity_pct", "mean"),
    Average_Water_Used=("Water_Used_m3", "mean"),
    Average_Water_Efficiency=("Water_Efficiency_t_per_1000m3", "mean"),
    Average_Disease_Risk=("Disease_Pest_Risk_pct", "mean")
).sort_values("Average_Profit", ascending=False)

display(season_summary)

# NaN

# Key Seasonal Performance Comparison
print("=== SEASONAL AGRICULTURAL PERFORMANCE SUMMARY ===\n")
print(season_summary[['Average_Yield', 'Average_Profit', 'Average_Water_Efficiency', 'Average_Disease_Risk']])


# NaN


for metric in [
    "Average_Yield",
    "Average_Profit",
    "Average_Revenue",
    "Average_Water_Used",
    "Average_Water_Efficiency",
    "Average_Disease_Risk"
]:
    plt.figure(figsize=(9, 5))
    season_summary[metric].plot(kind="bar")
    plt.title(f"{metric.replace('_', ' ')} by Season")
    plt.xlabel("Season")
    plt.ylabel(metric.replace("_", " "))
    plt.xticks(rotation=0)
    plt.tight_layout()
    plt.show()

# NaN

irrigation_summary = df.groupby(
    "Irrigation_Method",
    observed=True
).agg(
    Average_Yield=("Yield_Tonnes_Ha", "mean"),
    Average_Profit=("Profit_INR", "mean"),
    Average_Water_Used=("Water_Used_m3", "mean"),
    Average_Water_Efficiency=("Water_Efficiency_t_per_1000m3", "mean")
).sort_values("Average_Profit", ascending=False)

display(irrigation_summary)

plt.figure(figsize=(9, 5))
sns.barplot(
    data=df,
    x="Irrigation_Method",
    y="Water_Efficiency_t_per_1000m3",
    estimator="mean",
    errorbar=None
)
plt.title("Average Water Efficiency by Irrigation Method")
plt.xlabel("Irrigation Method")
plt.ylabel("Water Efficiency (t/1000 m³)")
plt.xticks(rotation=30)
plt.tight_layout()
plt.show()


# NaN

crop_summary = df.groupby(
    "Crop",
    observed=True
).agg(
    Average_Yield=("Yield_Tonnes_Ha", "mean"),
    Average_Profit=("Profit_INR", "mean"),
    Average_Revenue=("Revenue_INR", "mean"),
    Average_Cost=("Total_Cost_INR", "mean"),
    Average_Water_Efficiency=("Water_Efficiency_t_per_1000m3", "mean")
).sort_values("Average_Profit", ascending=False)

display(crop_summary)

plt.figure(figsize=(10, 6))
sns.barplot(
    data=df,
    x="Crop",
    y="Yield_Tonnes_Ha",
    estimator="mean",
    errorbar=None
)
plt.title("Average Yield by Crop")
plt.xlabel("Crop")
plt.ylabel("Average Yield (Tonnes/Ha)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()


# NaN

state_summary = df.groupby(
    "State",
    observed=True
).agg(
    Average_Yield=("Yield_Tonnes_Ha", "mean"),
    Average_Profit=("Profit_INR", "mean"),
    Average_Water_Efficiency=("Water_Efficiency_t_per_1000m3", "mean"),
    Average_Disease_Risk=("Disease_Pest_Risk_pct", "mean")
).sort_values("Average_Profit", ascending=False)

display(state_summary)

plt.figure(figsize=(11, 6))
sns.barplot(
    data=df,
    x="State",
    y="Profit_INR",
    estimator="mean",
    errorbar=None
)
plt.title("Average Profit by State")
plt.xlabel("State")
plt.ylabel("Average Profit (INR)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# NaN

plt.figure(figsize=(12, 6))
sns.boxplot(data=df, x="Irrigation_Method", y="Yield_Tonnes_Ha", hue="Season")
plt.title("Yield by Irrigation Method and Season")
plt.xlabel("Irrigation Method")
plt.ylabel("Yield (tonnes/ha)")
plt.legend(title="Season")
plt.tight_layout()
plt.show()

# NaN

best_profit_season = season_summary["Average_Profit"].idxmax()
best_yield_season = season_summary["Average_Yield"].idxmax()
best_water_season = season_summary["Average_Water_Efficiency"].idxmax()
highest_risk_season = season_summary["Average_Disease_Risk"].idxmax()

best_crop = crop_summary["Average_Profit"].idxmax()
best_irrigation = irrigation_summary["Average_Water_Efficiency"].idxmax()
best_state = state_summary["Average_Profit"].idxmax()

yield_variable = yield_corr.index[0]
profit_variable = profit_corr.index[0]

print("1.", best_profit_season, "has the highest average profit.")
print("2.", best_yield_season, "has the highest average yield.")
print("3.", best_water_season, "has the highest average water efficiency.")
print("4.", highest_risk_season, "has the highest average disease/pest risk.")
print("5.", best_crop, "has the highest average profit among crops.")
print("6.", best_irrigation, "has the highest average water efficiency.")
print("7.", best_state, "has the highest average profit among states.")
print("8.", yield_variable, "has the strongest absolute correlation with yield, while", profit_variable, "has the strongest absolute correlation with profit.")


# NaN

print("Recommendations")

print("1. Seasonal planning can prioritize", best_profit_season, "because it has the highest average profit.")
print("2. Conditions associated with", best_yield_season, "can be studied for improved yield planning.")
print("3. Water-efficient irrigation practices should be considered using the irrigation comparison.")
print("4. Additional disease and pest management attention can be given during", highest_risk_season + ".")
print("5. Crop selection should consider both crop and season.")
print("6. Regional performance differences can be used for targeted planning.")
print("7. Variables strongly associated with yield and profit can be monitored during future analysis.")
print("8. Cost, revenue, water usage and profit should be considered together for resource planning.")


# NaN

print("Limitations")

print("1. The analysis is limited to variables available in the provided dataset.")
print("2. Missing numerical values were handled using median imputation.")
print("3. Correlation indicates association and does not establish causation.")
print("4. IQR outliers are not necessarily incorrect observations.")
print("5. The dataset may not capture every real-world agricultural factor.")
print("6. Economic outcomes depend on the market conditions represented in the dataset.")


# NaN

print("Conclusion")

print(
    "The analysis identifies seasonal differences in agricultural performance "
    "by comparing yield, production, environmental conditions, resource usage, "
    "water efficiency, disease risk and economic outcomes."
)

print(
    "Crop, irrigation and regional analyses provide additional evidence for "
    "understanding differences within the agricultural dataset."
)

print(
    "The findings can support evidence-based seasonal agricultural planning "
    "and identify areas requiring further investigation."
)

# NaN

requirements = pd.DataFrame({
    "Requirement": [
        "Dataset loading",
        "Top 5 rows",
        "Shape and structure",
        "Data types",
        "Missing values",
        "Duplicate records",
        "Data cleaning",
        "Descriptive statistics",
        "Outlier investigation",
        "Univariate analysis",
        "Bivariate analysis",
        "Multivariate analysis",
        "Correlation analysis",
        "Seasonal comparison",
        "Student-designed analysis",
        "Meaningful insights",
        "Recommendations",
        "Limitations",
        "Conclusion"
    ],
    "Status": ["Completed"] * 19
})

display(requirements)
