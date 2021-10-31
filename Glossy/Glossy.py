import sys
from configure import auth_key
import requests
import pprint
from time import sleep
 
#global constants
headers = {
   "authorization": auth_key,
   "content-type": "application/json"
}
transcript_endpoint = "https://api.assemblyai.com/v2/transcript"
upload_endpoint = 'https://api.assemblyai.com/v2/upload'
 
#Function to pass the mp4 to the upload endpoint
def read_file(filename):
   with open(filename, 'rb') as _file:
       while True:
           data = _file.read(5242880)
           if not data:
               break
           yield data
 
#upload audio/video file
upload_response = requests.post(
   upload_endpoint,
   headers=headers, data=read_file(<"your filepath">)
)
print('Audio file uploaded')
 
#send the transcription request 
transcript_request = {'audio_url': upload_response.json()['upload_url'], "iab_categories": True}
transcript_response = requests.post(transcript_endpoint, json=transcript_request, headers=headers)
print('Transcription Requested')
pprint.pprint(transcript_response.json())

#polling
polling_response = requests.get(transcript_endpoint+"/"+transcript_response.json()['id'], headers=headers)
filename = transcript_response.json()['id'] + '.txt'
# if our status isn’t complete or encounters an error, sleep and then poll again
while polling_response.json()['status'] != 'completed' or polling_response.json()['status'] == 'error':
   sleep(30)
   polling_response = requests.get(transcript_endpoint+"/"+transcript_response.json()['id'], headers=headers)
   print("File is", polling_response.json()['status'])
with open(filename, 'w') as f:
   f.write(polling_response.json()['text'])
print('Transcript saved to', filename)
