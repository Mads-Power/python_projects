import threading
import time
import requests
import json

response_API = requests.get('https://swapi.dev/api/people/')
# print(response_API.status_code)

# getting the data from the api
data = response_API.text
json_data = json.loads(data)
json_prettyfy = json.dumps(json_data, indent=2)


# get all persons from api
start_time = time.time()
def get_persons():
    persons = json_data['results']
    for p in persons:
        names = p['name']
        height = p['height']
        print(f'\v Name: {names} \n  Height: {height} ')



# create new thread
x1 = threading.Thread(target=get_persons, args=())
x1.start()
print('Done')
print("--- %s seconds ---" % (time.time() - start_time))

get_persons()
# def count(n):
#     for i in range(1,n+1):
#         print(i)
#         time.sleep(0.01)
# for _ in range(2):
#     x = threading.Thread(target=count, args=(10,))
#     x.start()
#
# print("active count", threading.activeCount())
# print('Done')