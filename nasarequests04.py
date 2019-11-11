#!/usr/bin/python3

import requests

NASAAPI = "https://api.nasa.gov/planetary/apod?"

def main():
    #get Cred's
    with open("/home/student/creds", "r") as mycreds:
        nasacreds = mycreds.read()

    #remove any new lines
    nasacreds = nasacreds.strip("\n")

    # Make a call to Nasa API site
    apodresp = requests.get(NASAAPI + "api_key=" +nasacreds)

    # Strip off Json
    apod = apodresp.json()

    print(apod)

    print()

    print(apod["title"] + "\n")

    print(apod["date"] + "\n")
    
    print(apod["explanation"] + "\n")

    print(apod["url"] + "\n")


if __name__ == "__main__":
    main()


