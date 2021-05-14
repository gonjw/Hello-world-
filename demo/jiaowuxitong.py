import urllib.request
response=urllib.request.urlopen('http://218.199.113.111/jsxsd/' )
html=response.read()
html=html.decode('utf-8')
print(html)

