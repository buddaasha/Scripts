import requests
import csv
import os
import subprocess

def fetch_data(api_url):
    try:
        response = requests.get(api_url)
        response.raise_for_status()  # Raise an exception for bad requests
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
        return None


def save_to_csv(response_data, csv_file):
    fieldnames = list(response_data.keys()) if data else []
    print(fieldnames)

    with open(csv_file, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerow(response_data)


def return_current_directry():
    result = subprocess.run(['pwd'], stdout=subprocess.PIPE, text=True)

    if result.returncode==0:
        current_directory = result.stdout.strip()
    else:
        print(f"Error: {result.stderr}")
    return current_directory


def create_csv_file(folder_path):
    try:
        new_csv_file = os.path.join(folder_path, 'output_data.csv')
    except requests.exceptions.RequestException as e:
        print(f"Error creating a csv file:{e}")


if __name__ == "__main__":
    # Replace 'https://api.example.com/endpoint' with the actual API endpoint URL
    api_url = input("Enter your desired API to pull data into CSV: ")

    # Place csv file in a desired location
    folder_path = return_current_directry()
    csv_file = os.path.join(folder_path, 'output_data.csv')

    # Fetch data from the API endpoint
    response_data = fetch_data(api_url)

    # Save data to CSV file
    if response_data:
        save_to_csv(response_data, csv_file)

