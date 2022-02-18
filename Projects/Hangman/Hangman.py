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
|         
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
|         
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

print(len(newDesert.variety)*" _ ")
def getInput():
    while(True):
      # ask for input
      Character = input(f"name a letter for this dessert: ")
      special_char = "[@_!#$%^&*()<>?/\|}{~:]"

      # Validate input
      if(len(Character) != 1):
          print("error, just put a letter: ")
          continue

      if(Character.isnumeric()):
          print("error, no numbers, just a letter: ")
          continue

      if(Character in special_char):
          print("Error, no special charcter, just a letter: ")
          continue

      return Character


def printword()
   temp: str = ""

   for(Character in word)


print(getInput())
