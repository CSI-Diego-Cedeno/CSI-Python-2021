# import webbrowser
# webbrowser .open("https://www.elnuevodia.com")

import requests 
res = requests.get("https://www.gutenberg.org/cache/epub/67771/pg67771.txt")
print(len(res.text))
print(res.text[:300])