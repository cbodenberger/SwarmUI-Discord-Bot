import http.client
import json

conn = http.client.HTTPConnection('209.25.140.99:7860')
headers = {
    'Content-Type': 'application/json',
}
json_data = {}
conn.request('POST', '/API/GetNewSession', json.dumps(json_data), headers)
response = conn.getresponse()
body_bytes = response.read()
body_string = body_bytes.decode('utf-8') # Decode to a string if desired
json_output = body_bytes
data = json.loads(json_output)
session_id = data["session_id"]
print(f"JSON Session ID: {session_id}")