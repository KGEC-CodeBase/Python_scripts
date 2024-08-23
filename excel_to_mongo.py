import pandas as pd
from pymongo import MongoClient
import urllib.parse

def load_excel(file_path):
    return pd.read_excel(file_path,usecols =['Name', 'Email', 'Contact', 'Roll', 'Department','Year'])

def connect_to_mongodb(uri, db_name, collection_name):
    client = MongoClient(uri)
    db = client[db_name]
    collection = db[collection_name]
    return collection


def insert_data_to_mongodb(collection, data):
    
    student_array_objects = data.to_dict(orient="records")

    result = collection.insert_many(student_array_objects)

if __name__ == "__main__":
    file_path = "path_to_your_file"

    student_data = load_excel(file_path)
    
    username = urllib.parse.quote_plus('')
    password = urllib.parse.quote_plus('')

    collection = connect_to_mongodb(f"mongodb+srv://{username}:{password}@cluster0.rncye.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0","Student_db","Students")

    insert_data_to_mongodb(collection, student_data)

    print("All data inserted successfully.")
