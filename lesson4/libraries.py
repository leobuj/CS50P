# Libraries are useful code that allows us to leverage powerful 
# code that has been written by someone else
# Some problems have already been solved. use those solutions


# Accomplished with the 'import' keyword
# The standard is the import everything at the start of the file.
# For the sake of this exercise, we'll import when we need it.

import random

coin = random.choice(["heads","tails"])
print(coin)


# If we only need a specific function, we can also specify.
from random import choice


# Need a random integer? Easy
from random import randint
print("Let's get a random int from 1 to 10!: ", randint(1 , 10))

# Need a shuffler? Done.
from random import shuffle
cards = ["J", "K", "Q", "A", "J"]
print("Before shuffling: ", cards)
shuffle(cards)
print("After shuffling, ", cards)

# Stats work? very handy
import statistics
print("The mean of [100, 90] is: ", statistics.mean([100, 90]))



# Packages also exist as code that other users have written for other specific problems
# You need to install these packages to get them to work.
# 'pip install cowsay'
import cowsay

cowsay.cow("hello!")
cowsay.trex("hello!!!!!!!!!")


# Let's also use a library to leverage API endpoints and extract some data.
# 'pip install requests'

import requests
import sys

# This API returns JSON formatted data, so we're gonna have to do some things to make it readable.
# Most APIs return JSON data, and it often has dicts within dicts. Learn how to parse through them and 
# read the response so you understand how to dig through it.
response = requests.get("https://itunes.apple.com/search?entity=song&limit=8&term=daft_punk")
print(response.json())

o = response.json()
for result in o["results"]:
    print(result["trackName"])