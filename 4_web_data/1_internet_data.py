import urllib.request

print("open a url")
web_url = urllib.request.urlopen("http://www.google.com")
print(f"result code: {web_url.getcode()}")
print("\n")

print("read data from the open url")
data = web_url.read()
print(f"data: {data}")