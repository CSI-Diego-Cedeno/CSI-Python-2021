import json, ssl
import os
from pathlib import Path
import urllib.request
from Dessert import Dessert

ssl._create_default_https_context = ssl._create_unverified_context

DessertURL = "https://random-data-api.com/api/dessert/random_dessert"

req = urllib.request.Request(DessertURL)
requestData = json.loads(urllib.request.urlopen(req).read())

# Deserialize  
newDesert:Dessert = Dessert(**requestData)

print(newDesert.variety)

Steps = ["""
|---------|
|         |
|         O
|
|
|
|
|
""",
"""
|---------|
|         |
|         O
|         |
|
|
|
|
""",
"""
|--------|
|        |
|        O
|        |
|       -|
|
|
|
""",
"""
|--------|
|        |
|        O
|        |
|       -|-
|        
|
|
""",
"""
|--------|
|        |
|        O
|        |
|       -|-
|       /
|
|
""",
"""
|--------|
|        |
|        O
|        |
|       -|-
|       / \
|
|
"""
]


print(Steps[0])

print(newDesert.variety)

print(len(newDesert.variety)*" _ ")

def get_input():
    while(True):
      # ask for input
      Character = input(f"name a letter for this dessert: ")

      # Validate input
      if(len(Character) != 1):
          print("error, just put a letter: ")
          continue
      return Character
      if(Character.isnumeric()):
          print("error, no numbers, just a letter: ")
          continue
      return Character


print(get_input)()
