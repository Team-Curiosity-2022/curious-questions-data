import pandas as pd 

if __name__=="__main__":
    csv_dataset = pd.read_csv('dataset.csv')
    with open('dataset.jsonl', 'w') as out:
        for row in range(1,len(csv_dataset)):
            prompt = "Question: " + csv_dataset["Question"][row] + "\nAnswer: " + csv_dataset["Answer"][row] + "\nQuestion: "
            completion = csv_dataset["Curious Question"][row]
            data = {"prompt":prompt,"completion":completion}
            print(data)
            out.write(str(data))
            out.write("\n")
