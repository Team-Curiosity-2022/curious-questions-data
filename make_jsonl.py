import pandas as pd 
import json 

if __name__=="__main__":
    csv_dataset = pd.read_csv('dataset.csv')
    with open('new_dataset.jsonl', 'w') as out:
        for row in range(1,len(csv_dataset)):
            prompt = "Therapist: " + csv_dataset["Question"][row] + "\nPatient: " + csv_dataset["Answer"][row] + "\nTherapist: "
            completion = csv_dataset["Curious Question"][row]
            data = {"prompt":prompt,"completion":completion}
            json.dump(data, out)
            out.write("\n")
