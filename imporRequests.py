import requests
import csv
import os

def fetch_data(api_url):
    try:
        response = requests.get(api_url)
        response.raise_for_status()  # Raise an exception for bad requests
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
        return None

def save_to_csv(data, csv_file):
    fieldnames = list(data.keys()) if data else []
    print(fieldnames)

    with open(csv_file, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerow(data)

if __name__ == "__main__":
    # Replace 'https://api.example.com/endpoint' with the actual API endpoint URL
    api_url = 'https://api.publicapis.org/entries'

    # Place csv file in a desired location
    folder_path = '/Volumes/HOOLIGAN/PERSONAL/Automation/PythonLearning/APIResponse/output'
    csv_file = os.path.join(folder_path, 'output_data.csv')

    # Fetch data from the API endpoint
    response_data = fetch_data(api_url)

    # Save data to CSV file
    if response_data:
        save_to_csv(response_data, csv_file)

