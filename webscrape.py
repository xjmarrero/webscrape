from urllib import urlopen
from bs4 import BeautifulSoup

webpage = urlopen('http://twitter.com/Rihanna').read()

string_webpage = str(BeautifulSoup(webpage))

def get_links(url):
    result = []
    split_url = url.split('href')
    for each in split_url[0:]:
        if (each.find("http") != -1):
            start_quote = each.find("\"")
            end_quote = each.find("\"", start_quote+1)
            result.append(each[start_quote+1 : end_quote])
    return result

print get_links(string_webpage)