import requests

# URL of the file to download
url = ''
fileType = url.split('.')[-1]

# GET requests is sent to the url
response = requests.get(url)

# Check for response status code
if response.status_code == 200:
    # If successful saves the file
    with open('file.{fileType}', 'wb') as file:
        file.write(response.content)
    print('File downloaded successfully')
# If it fails:
else:
    print('Failed to download file')
