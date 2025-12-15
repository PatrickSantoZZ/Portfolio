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

def filter_by_user(data, user_id):
    return [item for item in data if item['userId'] == user_id]

def save_to_csv(data, filename):
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['userId', 'ID', 'Title', 'Body'])
        for item in data:
            writer.writerow([ item['userId'], item['id'], item['title'], item['body']])

if __name__ == "__main__":
    data = request_api()
    if data:
        # small addition to filter by user id
        #filtered_data = filter_by_user(data, 1)
        #save_to_csv(filtered_data, 'filtered_posts.csv')
        #print("Filtered data saved to filtered_posts.csv")
        save_to_csv(data, 'posts.csv')
        print("Data saved to posts.csv")
    else:
        print("No data received from the API/Function.")