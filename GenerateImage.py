import GetSessionID
import http.client
import json

conn = http.client.HTTPConnection('209.25.140.99:7860')
headers = {
    'Content-Type': 'application/json',
}
json_data = {
    'session_id': GetSessionID.session_id,
    'images': 1,
    'prompt': 'a cat',
    'model': 'waiNSFWIllustrious_v140',
    'width': 1024,
    'height': 1024,
}
conn.request(
    'POST',
    '/API/GenerateText2Image',
    json.dumps(json_data),
    # '{"session_id":"sid","images":1,"prompt":"a cat","model":"OfficialStableDiffusion/sd_xl_base_1.0","width":1024,"height":1024}',
    headers
)
response = conn.getresponse()
body_bytes = response.read()
body_string = body_bytes.decode('utf-8') # Decode to a string if desired
json_output = body_bytes
data = json.loads(json_output)
image_output = data["images"]
http_add = "http://209.25.140.99:7860/" + image_output[0]
Link = http_add.replace(" ", "%20")
print(f" {Link} ")