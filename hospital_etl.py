# Etl pipeline for a hospital
import pandas as pd
import os

# Extract data from the csv
def extract_data(file_name):
    try:
        # Get the current working directory
        dir_path = os.path.dirname(__file__)
        # Construct file path
        file_path = os.path.join(dir_path, 'data',file_name)
        if os.path.exists(file_path):
            data = pd.read_csv(file_path)
            print(data.head())
            return data
        else:
            print(f"File {file_name} not found in the data folder.")
        
    except Exception as e:
        print("error exttracting data as{e}")




if __name__ == "__main__":
    print("Running ETL pipeline directly")
    dir_path = os.path.dirname(__file__)
    data_dir = os.path.join(dir_path, 'data')
    for file_name in os.listdir(data_dir):
        if file_name.endswith(".csv"):
            extract_data(file_name)