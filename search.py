# MrGoogle -- do a google search using 'search.py "frogs" '.

from selenium import webdriver
import sys

# conversion from list to string
def convert(s):
    str1 = ""
    return(str1.join(s))

#assign the arguements passed to variable search_s
search_s = sys.argv[1:]

# convert to string
search_s = convert(search_s)
# structure time!
search_s = search_s.replace(' ', '+')

browser = webdriver.Firefox()

for i in range(1):
    matched_elem = browser.get("https://www.google.com/search?q=" + search_s + "&start=" + str(i))
