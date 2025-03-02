import requests                    
import json   
from bs4 import BeautifulSoup 
from fastapi import FastAPI 



# what are the steps to retrieving comic?
#   First, different websites need to be configured differently since the layout of the HTML is different from page to page,
# so there must be packages for different websites. The website will include 

# creating api so that when frontend access the api route, respective functions will trigger
app = FastAPI()


@app.get("/api/website/{url}")
def get_website(url: str) -> BeautifulSoup:
    """Get the raw html content of the website"""

    response = requests.get(url).text                   # request raw html texts for beautifulsoup to parse
    soup = BeautifulSoup(response, "html.parser")       # parse html; can't request raw html alone
    
    return soup

@app.get("/api/comics/{url}")
def get_comics(url: str):
    """Load comics from the website, should be the element displayed in their website"""
    pass

@app.get("/api/chapters/{comic_name}")
def get_chapters(comic_name: str):
    """Load chapters from the website"""
    pass

def download_chapters():
    """Downloads the chapter and store in some directory"""


def main():
    solo_leveling = {"url" : "https://w5.solo-leveling-manga.com/", "multiple_comics" : False}
    print(type(get_website(solo_leveling["url"])))
    pass





if __name__ == "__main__":
    main()