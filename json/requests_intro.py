import requests

# response = requests.get("https://xkcd.com/353")
#
# """help funtions"""
# # print(dir(response))
# # print(help(response))
#
# """text"""
# # print(response.text)
#
# """images"""
# image_response = requests.get("https://imgs.xkcd.com/comics/python.png")
# with open("comic.png", "wb") as file:
#     file.write(image_response.content)
#
# """status_code"""
# print(response.status_code)
# print(response.ok)  # Everything other 400 errors will be ignored
#
# header_response = requests.get("https://google.com")
# print(header_response.headers)
#
# """params"""
# payload = \
#     {
#         "count": 2,
#         "page": 25
#     }
# params_response = requests.get("https://httpbin.org/get", params=payload)
#
# print(params_response.text)
# print(params_response.url)  # https://httpbin.org/get?count=2&page=25
#
# """"post request"""
# payload = {
#     "username": "Gautam",
#     "password": "test"
# }
# data_response = requests.post("https://httpbin.org/post", data=payload)
# data_dict = data_response.json()
# print(data_dict['form'])
#
# """basic auth"""
#
# auth_response = requests.get("https://httpbin.org/basic-auth/Gautam/test", auth=("Gautam", "test"))
# # print(auth_response.text)
# print(auth_response)
#
# """time out"""
# delay_response = requests.get("https://httpbin.org/delay/6", timeout=3)
# print(delay_response)

"""redirects"""
redirect_response = requests.get("https://httpbin.org/absolute-redirect/5")
print("-------------------")
print(redirect_response.history)
print(redirect_response.status_code)
print(redirect_response.url)


def print_response_history(resp):
    if resp.history:
        print("History")
        for r in resp.history:
            print("Status Code", r.status_code)
            print("Url", r.url)

        print("Final")
        print(resp.status_code, resp.url)

    else:
        print("There were no redirects")


# print_response_history(redirect_response)
redirect_response_1 = requests.get("https://httpbin.org/redirect-to?url=https://yahoo.com")
print_response_history(redirect_response_1)

"""To stop redirects"""
redirect_response_2 = requests.get("https://httpbin.org/redirect-to?url=https://yahoo.com", allow_redirects=False)
print_response_history(redirect_response_2)