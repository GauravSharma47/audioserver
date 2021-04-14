import requests
import json
song_data={"name":"Safarnama","duration":180,"ID":5}
audiobook_data={"name":"Little Things","duration":1900,"ID":5,"author":"Gaurav","narrator":"sharma"}
podcast_data={"name":"Safarnama","duration":5000,"ID":5,"host":"saloni","participants":["tin","tan","pop"]}
# print(requests.post("http://127.0.0.1:8000/create/song",data=song_data).content)
# print(requests.post("http://127.0.0.1:8000/create/audiobook",data=audiobook_data).content)
# print(requests.post("http://127.0.0.1:8000/create/podcast",data=podcast_data).content)
print(requests.post("http://127.0.0.1:8000/update/song/3",data={"name":"sawal"}).content)