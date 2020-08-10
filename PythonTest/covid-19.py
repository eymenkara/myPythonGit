import pandas as pd

covid_filepath = "/Users/eymenkara/Desktop/covid.csv"
covid_data = pd.read_csv(covid_filepath)

print(covid_data.columns)
print(covid_data.describe())
print(covid_data.head())
