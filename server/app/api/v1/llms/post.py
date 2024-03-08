import sys
import requests

text = " ".join(sys.argv[1:])
url = 'http://127.0.0.1:5000/morya-model/generate'
data = {
    'text': text,
    'max_length': 256,
    'max_new_tokens': 100
}
try:
    response = requests.post(url, json=data, timeout=100)
    # Check to see if respose is succesful
    if response.status_code == 200:
        print(response.json())
    else:
        print(f'Error: Model Generation Error {response.status_code}')
except requests.exceptions.RequestException as e:
    print(f'Returned: {e}')
