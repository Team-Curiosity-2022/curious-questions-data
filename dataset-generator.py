import pandas as pd

csv1 = pd.read_csv("Curious Questions Prolific.csv")
csv2 = pd.read_csv("Survey Responses Prolific.csv")
print(csv2.columns[5:])
i = 0
for col in csv2.columns[5:]:
    for response in csv2[col]:
        csv1.loc[i,'Single Exchange'] = "Question: "+ col +" Answer: "+ response
        i+=1
csv1.to_csv("dataset-prolific.csv",index=False)
print(csv1.head())