import requests
import json

response_API = requests.get('https://api.twitter.com/2/tweets/search/recent?query=from:twitterdev')
# print(response_API.status_code)

# getting the data from the api
data = response_API.text
json_data = json.loads(data)
# pretyfier json
json_prettyfy = json.dumps(json_data, indent=2)
print(json_prettyfy)

# get all persons from api
def get_persons():
    persons = json_data['results']
    for p in persons:
        names = p['name']
        height = p['height']
        print(f'\v Name: {names} \n  Height: {height} ')



# get_persons()
# print(json_data['results'][0]['name'])
# results = json_data['results'][0]


# luke = results[0]
# print(results)
# print("luke: ", luke.items())
# dict_variable = {key:value for (key,value) in luke.items()}
# print("dict:", dict_variable)
# results_list = [x for x in luke if "" in x]
# print("results:", results_list)



# for k,v in enumerate(results):
#     print("key: ", k, "value: ", v)
#     print()

# for k in st_persons.keys():
#     print(k)

# print(st_persons)
# response_API = requests.get('https://gmail.googleapis.com/$discovery/rest?version=v1')
# data = response_API.text
# parse_json = json.loads(data)
# info = parse_json['description']
# key = parse_json['parameters']['key']['description']
# print(info)
