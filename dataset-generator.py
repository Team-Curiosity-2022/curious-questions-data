import pandas as pd

# Csv1 contains one empty col for Single Exchange storage 
# and Curious Questions generated manually by the team for each single exchange
csv1 = pd.read_csv("Curious Questions Prolific.csv")

# Single Exchanges (Team Static Question + User response pairs) 
# are collected through Prolific survey form and contained in csv2
csv2 = pd.read_csv("Survey Responses Prolific.csv")
# Skip first 5 columns as they contain reference data (eg. date, prolificID etc...)
# Static questions are contained in the headers of columns 6 to 10
static_questions = csv2.columns[5:] 

i = 0
for question in static_questions:
    for response in csv2[question]:
        # merge Question-Answer pairs with Curious Questions in csv1 column1
        csv1.loc[i,'Single Exchange'] = "Question: "+ question +" Answer: "+ response
        i+=1

# Save to new file
csv1.to_csv("dataset-prolific.csv",index=False)

# For debugging purposes print the first 5 rows of new database
print(csv1.head())