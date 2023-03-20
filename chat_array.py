import pandas as pd 
import json 
import random 
import math

if __name__=="__main__":
    csv_dataset = pd.read_csv('dataset.csv')
    r = list(range(len(csv_dataset)))
    random.shuffle(r)
    
    
    with open('train_dataset.txt', 'w') as out:
        for row in r:
            prompt = "Curiosity is defined as the attempt to obtain new information which is not present in the initial single exchange. Curious questions should also maintain contextuality and sequentiality in the conversation. Where contextuality is showing comprehension of the given information in the single exchange. And, maintaing sequentiality is to ensure that output relates to the conversation in their given sequence. Based on this, create a question to continue the following single exchange that is curious and maintains contextuality and sequentiality. \n Question: " + csv_dataset["Single Exchange"][row] + "\nQuestion: "
            data1 = {"role": "user","content":prompt}
            json.dump(data1, out)
            out.write(",\n")
           
            completion = csv_dataset["Curious Question"][row]
            data2 = {"role": "assistant", "content": completion}
            json.dump(data2, out)
            out.write(",\n")