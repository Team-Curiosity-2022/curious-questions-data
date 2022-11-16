import pandas as pd

csv1 = pd.read_csv("Curious Questions Dataset - Sheet1.csv")
csv2 = pd.read_csv("Capstone Opening Questions Survey Team Responses - Form Responses 1.csv")
print(csv2.columns[5:])
i = 0
for col in csv2.columns[5:]:
    for response in csv2[col]:
        csv1.loc[i,'Question'] = col 
        csv1.loc[i, 'Answer'] = response
        i+=1
csv1.to_csv("dataset.csv",index=False)
print(csv1.head())