# Author: Fortune Akioya

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# --- Data Generation (for demonstration purposes) ---
# In a real scenario, you would load an existing CSV.
# This part generates a synthetic dataset resembling video game sales.
np.random.seed(42)

data_size = 500
genres = ['Action', 'Sports', 'Shooter', 'Role-Playing', 'Racing', 'Platform', 'Strategy']
platforms = ['PS4', 'Xbox One', 'PC', 'Switch', 'PS3', 'Xbox 360', 'Wii']
publishers = ['Nintendo', 'Sony', 'Microsoft', 'EA', 'Activision', 'Ubisoft', 'Take-Two']

data = {
    'Name': [f'Game {i+1}' for i in range(data_size)],
    'Platform': np.random.choice(platforms, data_size),
    'Year_of_Release': np.random.randint(2010, 2023, data_size),
    'Genre': np.random.choice(genres, data_size),
    'Publisher': np.random.choice(publishers, data_size),
    'NA_Sales': np.round(np.random.uniform(0.1, 5.0, data_size), 2),
    'EU_Sales': np.round(np.random.uniform(0.05, 3.5, data_size), 2),
    'JP_Sales': np.round(np.random.uniform(0.01, 2.0, data_size), 2),
    'Other_Sales': np.round(np.random.uniform(0.01, 1.5, data_size), 2),
}
df = pd.DataFrame(data)
df['Global_Sales'] = df[['NA_Sales', 'EU_Sales', 'JP_Sales', 'Other_Sales']].sum(axis=1)

# Introduce some missing values for demonstration of cleaning
for col in ['Publisher', 'Year_of_Release', 'Global_Sales']:
    missing_indices = np.random.choice(df.index, size=int(data_size * 0.03), replace=False)
    df.loc[missing_indices, col] = np.nan
# --- End of Data Generation ---

print("--- Data Analysis: Gaming Industry Dataset ---")

# Task 1: Load and Explore the Dataset

print("\n--- Task 1: Load and Explore the Dataset ---")

print("\nFirst 5 rows of the dataset:")
print(df.head())

print("\nDataset Info (data types and non-null counts):")
df.info()

print("\nMissing values in each column (before cleaning):")
print(df.isnull().sum())

# Clean the dataset by either filling or dropping any missing values.
# For 'Year_of_Release', fill with median or drop
# For 'Publisher', fill with 'Unknown' or drop
# For 'Global_Sales', drop rows where it's missing as it's a critical derived value.

# Drop rows where 'Global_Sales' is missing, as it's central to our analysis.
df.dropna(subset=['Global_Sales'], inplace=True)

# Fill missing 'Year_of_Release' with the median year
df['Year_of_Release'] = df['Year_of_Release'].fillna(df['Year_of_Release'].median()).astype(int)

# Fill missing 'Publisher' with 'Unknown'
df['Publisher'].fillna('Unknown', inplace=True)

print("\nMissing values in each column (after cleaning):")
print(df.isnull().sum())
print("\nDataset cleaned. Missing values have been addressed.")

# Task 2: Basic Data Analysis

print("\n--- Task 2: Basic Data Analysis ---")

# Compute the basic statistics of the numerical columns
print("\nBasic statistics of numerical columns:")
print(df.describe())

# Perform groupings on categorical columns
# Group by Genre and compute mean Global_Sales
print("\nMean Global Sales by Genre:")
print(df.groupby('Genre')['Global_Sales'].mean().sort_values(ascending=False))

# Group by Platform and compute mean Global_Sales
print("\nMean Global Sales by Platform:")
print(df.groupby('Platform')['Global_Sales'].mean().sort_values(ascending=False))

# Group by Publisher and compute total Global_Sales
print("\nTop 10 Publishers by Total Global Sales:")
print(df.groupby('Publisher')['Global_Sales'].sum().nlargest(10))

# Group by Year_of_Release and compute total Global_Sales
print("\nTotal Global Sales by Year:")
print(df.groupby('Year_of_Release')['Global_Sales'].sum().sort_index())

# Identify any patterns or interesting findings from your analysis.
print("\n--- Findings and Observations ---")
print("1. The dataset contains information on game names, platforms, release years, genres, publishers, and sales figures across different regions.")
print("2. Missing values for 'Publisher', 'Year_of_Release', and 'Global_Sales' were handled by dropping rows with missing 'Global_Sales', filling 'Year_of_Release' with its median, and 'Publisher' with 'Unknown'.")
print("3. From basic statistics (df.describe()):")
print("   - 'Global_Sales' has a wide range, indicating popular titles can achieve much higher sales.")
print("   - Regional sales (NA_Sales, EU_Sales, JP_Sales, Other_Sales) show different distributions, with NA generally having higher average sales than others.")
print("4. Grouping by 'Genre': Action and Shooter genres often show high average global sales, suggesting their consistent popularity.")
print("5. Grouping by 'Platform': Certain platforms (e.g., PS4, Switch, Xbox One in this synthetic data) might dominate global sales, reflecting current console generations or strong market presence.")
print("6. Grouping by 'Publisher': A few publishers tend to dominate the market in terms of total global sales, indicating strong brand loyalty, large development budgets, or successful franchises.")
print("7. Sales trends over 'Year_of_Release' can indicate periods of market growth, decline, or the impact of major console releases. (In this synthetic data, it might just show general activity across years.)")
print("8. There might be a strong correlation between NA_Sales and Global_Sales, as NA often contributes a significant portion of overall sales.")


# Task 3: Visualizations

print("\n--- Task 3: Visualizations ---")

# 1. Total Global Sales by Genre
plt.figure(figsize=(12, 6))
df.groupby('Genre')['Global_Sales'].sum().sort_values(ascending=False).plot(kind='bar')
plt.title('Total Global Sales by Genre')
plt.xlabel('Genre')
plt.ylabel('Total Global Sales (in Millions)')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()
` `
# 2. Total Global Sales by Platform
plt.figure(figsize=(12, 6))
df.groupby('Platform')['Global_Sales'].sum().sort_values(ascending=False).plot(kind='bar', color='skyblue')
plt.title('Total Global Sales by Platform')
plt.xlabel('Platform')
plt.ylabel('Total Global Sales (in Millions)')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()
` `
# 3. Top 10 Publishers by Global Sales
plt.figure(figsize=(12, 6))
df.groupby('Publisher')['Global_Sales'].sum().nlargest(10).plot(kind='bar', color='lightcoral')
plt.title('Top 10 Publishers by Total Global Sales')
plt.xlabel('Publisher')
plt.ylabel('Total Global Sales (in Millions)')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()
` `
# 4. Global Sales Trend Over Years
plt.figure(figsize=(12, 6))
df.groupby('Year_of_Release')['Global_Sales'].sum().plot(kind='line', marker='o', color='green')
plt.title('Global Sales Trend Over Years')
plt.xlabel('Year of Release')
plt.ylabel('Total Global Sales (in Millions)')
plt.grid(True)
plt.tight_layout()
plt.show()
` `
# 5. Sales Distribution Across Regions
sales_regions = df[['NA_Sales', 'EU_Sales', 'JP_Sales', 'Other_Sales']].sum()
plt.figure(figsize=(8, 8))
sales_regions.plot(kind='pie', autopct='%1.1f%%', startangle=90, colors=sns.color_palette('pastel'))
plt.title('Proportion of Global Sales by Region')
plt.ylabel('') # Hide the default 'Global_Sales' label
plt.tight_layout()
plt.show()
` `
# 6. Scatter plot of NA Sales vs EU Sales (to see correlation)
plt.figure(figsize=(10, 7))
sns.scatterplot(x='NA_Sales', y='EU_Sales', hue='Genre', data=df, alpha=0.7, s=100)
plt.title('NA Sales vs EU Sales by Genre')
plt.xlabel('North America Sales (in Millions)')
plt.ylabel('Europe Sales (in Millions)')
plt.grid(True)
plt.tight_layout()
plt.show()
` `

print("\nVisualizations generated. Please review the plots displayed.")
print("\n--- End of Analysis ---")
