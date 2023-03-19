import pandas as pd 
import json 
import random 
import math

if __name__=="__main__":
    csv_dataset = pd.read_csv('dataset.csv')
    r = list(range(len(csv_dataset)))
    random.shuffle(r)
    train_end_index = math.floor(len(r)*0.80)
    test_end_index =  train_end_index + math.floor((len(r) - train_end_index)/2)

    training_indices = r[:train_end_index]
    testing_indices = r[train_end_index:test_end_index]
    validation_indices = r[test_end_index::]
    
    with open('train_dataset.jsonl', 'w') as out:
       
        for row in training_indices:
            prompt = "Curiosity is defined as the attempt to obtain new information which is not present in the initial single exchange. Curious questions should also maintain contextuality and sequentiality in the conversation. Where contextuality is showing comprehension of the given information in the single exchange. And, maintaing sequentiality is to ensure that output relates to the conversation in their given sequence. Based on this, create a question to continue the following single exchange that is curious and maintains contextuality and sequentiality. \n Question: " + csv_dataset["Single Exchange"][row] + "\nQuestion: "
            completion = csv_dataset["Curious Question"][row]
            data = {"prompt":prompt,"completion":completion}
            json.dump(data, out)
            out.write("\n")

    with open('test_dataset.jsonl', 'w') as out:
       
        for row in testing_indices:
            prompt = "Curiosity is defined as the attempt to obtain new information which is not present in the initial single exchange. Curious questions should also maintain contextuality and sequentiality in the conversation. Where contextuality is showing comprehension of the given information in the single exchange. And, maintaing sequentiality is to ensure that output relates to the conversation in their given sequence. Based on this, create a question to continue the following single exchange that is curious and maintains contextuality and sequentiality. \n Question: " + csv_dataset["Single Exchange"][row] + "\nQuestion: "
            completion = csv_dataset["Curious Question"][row]
            data = {"prompt":prompt,"completion":completion}
            json.dump(data, out)
            out.write("\n")

    with open('val_dataset.jsonl', 'w') as out:
       
        for row in validation_indices:
            prompt = "Curiosity is defined as the attempt to obtain new information which is not present in the initial single exchange. Curious questions should also maintain contextuality and sequentiality in the conversation. Where contextuality is showing comprehension of the given information in the single exchange. And, maintaing sequentiality is to ensure that output relates to the conversation in their given sequence. Based on this, create a question to continue the following single exchange that is curious and maintains contextuality and sequentiality. \n Question: " + csv_dataset["Single Exchange"][row] + "\nQuestion: "
            completion = csv_dataset["Curious Question"][row]
            data = {"prompt":prompt,"completion":completion}
            json.dump(data, out)
            out.write("\n")