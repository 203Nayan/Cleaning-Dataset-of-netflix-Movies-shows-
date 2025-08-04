import pandas as pd

df = pd.read_csv('C:\Users\nayan\OneDrive\Documents\netflix_titles.csv')

print("Missing values before cleaning:\n", df.isnull().sum())

df.dropna(subset=['title'], inplace=True)

df['description'].fillna('No Description', inplace=True)

df.drop_duplicates(inplace=True)

df['type'] = df['type'].str.lower().str.strip()
df['country'] = df['country'].str.title().str.strip()

df['date_added'] = pd.to_datetime(df['date_added'], errors='coerce')

df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_')

df['release_year'] = df['release_year'].astype(int)

df.to_csv('netflix_cleaned.csv', index=False)

summary = {
    'rows_after_cleaning': len(df),
    'columns': list(df.columns),
    'missing_values_after': df.isnull().sum().to_dict()
}

print("✅ Cleaning completed. Summary:")
for k, v in summary.items():
    print(f"{k}: {v}")
