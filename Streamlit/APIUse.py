import requests

url = "https://jsonplaceholder.typicode.com/posts"

response = requests.get(url)

data =[
    {"UserId": 1, "Id": 1, "title": "Post 1", "body": "This is the body of post 1."},
    {"UserId": 2, "Id": 2, "title": "Post 2", "body": "This is the body of post 2."},
    {"UserId": 3, "Id": 3, "title": "Post 3", "body": "This is the body of post 3."},
    ]

if response.status_code == 200:
    data = response.json()
    print("First post:")
    # for i in range(10):
    print(data[0])

response = requests.post(url, json={
    "userId": 2,
    "title": "Post 2",
    "body": "This is the body of post 2.",
    "Id": 2
})

if response.status_code == 201:
    data = response.json()
    print("Post created successfully.")
else:
    print("Failed to create post 2.")

response = requests.post(url, json={
    "userId": 2,
    "title": "Post 2",
    "body": "This is the body of post 2.",
    "Id": 2
})
if response.status_code == 202:
    data = response.json()
    print("Request accepted successfully.")
else:
    print("Failed to accept post 3.")

response = requests.post(url, json={
    "userId": 3,
    "title": "Post 3",
    "body": "This is the body of post 3.",
    "Id": 3
})
if response.status_code == 204:
    data = response.json()
    print("Success but no data")
else:
    print("post .")


response = requests.post(url, json={
    "userId": 4,
    "title": "Post 4",
    "body": "This is the body of post 4",
    "Id": 4
})
if response.status_code == 401:
    data = response.json()
    print("Invalid request")
else:
    print("post 4 failed.")





    


