#!/uusr/bin/python3
'''Joe Beagle ||  joe.beagle@kp.org'''

import urllib.request
import json

MAJORTOM = 'http://api.open-notify.org/astros.json'

def main():
    '''reading json from api'''
    # call the API
    groundctrl = urllib.request.urlopen(MAJORTOM)

    helmet = groundctrl.read()

    print(helmet)

    helmetson = json.loads(helmet.decode("utf-8"))

    print(type(helmet))

    print(type(helmetson))

    print(helmetson["number"])

    print(helmetson["people"])

    print(helmetson["people"][0])

    print(helmetson["people"][1])

    print(helmetson["people"][-1])

    # Display a list
    for astro in helmetson["people"]:
        print(astro)

    #display the names only
    for astro in helmetson["people"]:
        print(astro["name"])





if __name__ == "__main__":
    main()
    

