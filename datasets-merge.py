import pandas as pd

# get dataset generated from prolific 100 records and team 20 records
prolific = pd.read_csv("dataset-prolific.csv")
team = pd.read_csv("dataset-team.csv")

# merge in one final database and save to new file
dataset = team.merge(prolific, how='outer')
dataset.to_csv("dataset.csv", index=False)

# For debugging purposes print the first and last 5 rows of new database
print(dataset.head())
print(dataset.tail())