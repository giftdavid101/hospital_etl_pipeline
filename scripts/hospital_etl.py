# Etl pipeline for a hospital
import pandas as pd
import os

# STEP 1: EXTRACTION

# Extract data from the csv
def extract_data(file_name):
    try:
        # Get the current working directory
        dir_path = os.path.dirname(__file__)
        # Construct file path
        file_path = os.path.join(dir_path, 'data',file_name)
        # Check if path is valid
        if os.path.exists(file_path):
            # Read csv and print first five rows
            data = pd.read_csv(file_path)
            print(data.head())
            return data
        # Give feedback if path is not found
        else:
            print(f"File {file_name} not found in the data folder.")
            return None 

    # Give error feedback if extraction fails
    except Exception as e:
        print("error exttracting data as{e}")
        return None

# coming up next is transformation.....

# STEP 2: TRANSFORMATION

def transform_data(data):
    data.drop('patient_name', axis=1, inplace=True)



if __name__ == "__main__":
    print("Running ETL pipeline directly")
    dir_path = os.path.dirname(__file__)
    data_dir = os.path.join(dir_path, 'data')
    for file_name in os.listdir(data_dir):
        if file_name.endswith(".csv"):
            extract_data(file_name)