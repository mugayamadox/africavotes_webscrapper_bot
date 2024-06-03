
#import modules
import time
import re
import mechanicalsoup
import matplotlib.pyplot as plt
import pandas as pd

#instantiate mechanicalsoup browser
browser = mechanicalsoup.Browser()

#scrape a page
page = browser.get("https://africavotes.com/p/miss.and.mr.tourism.kigezi.region.2024")

#fetch names of contestants, all names are contained in the 'u' tag
named = page.soup.find_all('u')
names = []
for name in named:
    #create regex that filters to retain first name and initial of second name
    match = re.search(r"^(\w+)\s+(\w)", name.text)
    name= match.group(1) + (" " + match.group(2) if match else "")
    names.append(name)

#fetch votes of contestants
voted = page.soup.find_all('b')[2:15]
votes = []
for vote in voted:
    #clean the votes by removing 'Votes' text whitespaces and '.' then cast them to int
    vote = vote.text
    vote = vote.strip("Votes")
    vote = vote.replace(" ", "")
    vote = vote.replace(",", "")
    votes.append(int(vote))

#Create a plot showing the contestants and number of votes
plt.bar(names, votes)
plt.xticks(rotation=45, ha='right')  
plt.title("MISS AND MISTER TOURISM KIGEZI")
plt.xlabel("contestants name")
plt.ylabel("Number of votes")
plt.show()


