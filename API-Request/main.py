import requests
import csv

def request_api():
    url = 'https://jsonplaceholder.typicode.com/posts'

    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        if data:
            return data
        else:
            print("No data received from the API.")
    else:
        print(f"Error: {response.status_code}")

def save_to_csv(data, filename):
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['userId', 'ID', 'Title', 'Body'])
        for item in data:
            writer.writerow([ item['userId'], item['id'], item['title'], item['body']])

if __name__ == "__main__":
    data = request_api()
    if data:
        save_to_csv(data, 'posts.csv')
        print("Data saved to posts.csv")