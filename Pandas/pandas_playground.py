# Pandas:
# https://pandas.pydata.org/docs/index.html
# https://www.youtube.com/watch?v=PcvsOaixUh8

import pandas as pd

df1 = pd.DataFrame(
    {
        "Name": [
            "Braund, Mr. Owen Harris",
            "Allen, Mr. William Henry",
            "Bonnell, Miss. Elizabeth",
        ],
        "Age": [22, 35, 58],
        "Sex": ["male", "male", "female"],
    }
)

# Print 1) Dataframe 2) Series (Column)  3) Cell / Element
# print(df1, "\n")
# print(df1["Age"], "\n")
# print(df1["Age"][0], "\n")

# Create Series
# loc = pd.Series(["Baltimore", "Washington DC", "Boston", "Arlington", "Bethesda"])
# print(loc)

# Basic statistics
# print(df1.describe())

# Load .csv file into DataFrame
df_csv = pd.read_csv('sample.csv')
df_xlsx = pd.read_excel('sample.xlsx')
# print(df_xlsx)

# Save as to_* functions
# df1.to_csv("df1.csv")
# df1.to_excel("df1.xlsx", sheet_name="pythonData", index=False)

# Select Series(s)
age_sex = df1[["Age", "Sex"]]
print(age_sex)