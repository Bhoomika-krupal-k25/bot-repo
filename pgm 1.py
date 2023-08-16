import requests

url = "http://api.textmebot.com/send.php"
params = {
    "recipient": "+917795976054",  # Replace with the recipient's phone number
    "apikey": "u6er2Tw7ae5x",  # Replace with your API key
    "text": "This is a test",
    "file": "NEW_IMAGE_PATH"  # Replace with the new path of the image file
}

response = requests.get(url, params=params)
print(response.text)


