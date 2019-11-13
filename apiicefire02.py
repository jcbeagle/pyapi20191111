#!/usr/bin/python3
"""Alta3 Research - Exploring OpenAPIs with requests"""
# documentation for this API is at
# https://anapioficeandfire.com/Documentation

import requests

AOIF = "https://www.anapioficeandfire.com/api/books"

def main():
    ## Send HTTPS GET to the API of ICE and Fire
    gotresp = requests.get(AOIF)
    
    ## Decode the response
    got_dj = gotresp.json()
    
    ## loop across responce
    for singlebook in got_dj:
        ## display the names of each book
        ## all of the below statments do the same thing
        # print(singlebook["name"] + ",", "pages -", singlebook["numberOfPages"])
        # print("{}, pages - {}".format(singlebook["name"], singlebook["numberOfPages"])
        print(f"{singlebook['name']}, pages - {singlebook['numberOfPages']}")
        print(f"\tAPI URL -> {singlebook['url']}\n")
        print(f"\tISBN -> {singlebook['isbn']}\n")
        print(f"\tPUBLISHER -> {singlebook['publisher']}\n")
        print(f"\tNo. of CHARACTERS -> {len(singlebook['characters'])}\n")
    
if __name__ == "__main__":
    main()
