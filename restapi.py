
class xyz(dict):
    def __str__(self):
        return json.dumps(self)


import json

import requests

url = ('https://newsapi.org/v2/everything?q=tesla&from=2023-09-05&sortBy=publishedAt&apiKey'
       '=ee776817c6504cd1a9ac6a32f6764269')


response = requests.get(url)
data = xyz(response.json())
# print(data)
file = open("data.json", "w")
file.write(str(data))



f = open("data.json", "r")
new_data = json.loads(f.read())

post_response = requests.post(url , json=new_data)
print(post_response.json())

# print(new_data)