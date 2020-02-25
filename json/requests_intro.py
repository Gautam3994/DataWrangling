import requests

response = requests.get("https://xkcd.com/353")

"""help funtions"""
# print(dir(response))
# print(help(response))

"""text"""
# print(response.text)

"""images"""
image_response = requests.get("https://imgs.xkcd.com/comics/python.png")
with open("comic.png", "wb") as file:
    file.write(image_response.content)

"""status_code"""
print(response.status_code)
print(response.ok)  # Everything other 400 errors will be ignored

header_response = requests.get("https://google.com")
print(header_response.headers)

"""params"""
payload = \
    {
        "count": 2,
        "page": 25
    }
params_response = requests.get("https://httpbin.org/get", params=payload)

print(params_response.text)
