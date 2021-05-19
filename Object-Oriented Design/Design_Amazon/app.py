# timeit module for function times
# functools module for lru cache - default maxsize is 128


class Item:
    def __init__(self):
        review = ""


    def addReview(self, review):
        pass




class Cache:

    def __init__(self, type):
        type = self.type


import requests

cache = dict()

def get_article_from_server(url):
    print("Fetching from the server")
    response = requests.get(url)
    return response.text

def get_article(url):
    print("Getting article")
    if url not in cache:
        cache[url] = get_article_from_server(url)

get_article("https://realpython.com/sorting-algorithms-python/")
get_article("https://realpython.com/sorting-algorithms-python/")