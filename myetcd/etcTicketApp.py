#!/usr/bin/python3
"""Russell Zachary Feeser Using etcd to design a RESTful ticket server"""

import requests

ETCD = "http://127.0.0.1:2379/v2/keys/tickets"

## read all available tickets
## use a GET on a directory to return all results
def gettickets():
    resp = requests.get(ETCD)
    resp = resp.json()
    if resp.get("errorCode"):
        return False
    else:
        ticketlist = []
        for ticket in resp.get("node").get("nodes"):
            ticketlist.append(ticket.get("key").lstrip("/tickets/"))
        return ticketlist


## get a specific ticket
## pass in the ticket to GET
def getoneticket(ticketid):
    pass

## create a ticket
## use a POST to create a new resource
def createticket(descofissue):
   resp = requests.post(ETCD, data={'value': descofissue })
   resp = resp.json()
   resp = resp.get("node").get("key").lstrip("/tickets/")
   return resp

## update a ticket
## pass in the ticket to PUT
def updateticket(descofissue):
    pass

## delete a ticket
## pass in the ticket to DELETE
def deleteticket(ticketid):
    pass

## delete ALL tickets
## use the api parameter ?dir=true&recursive=true to remove a directory
def deletealltickets():
    pass

def main():

    ## Enter a while true loop (run until a break condition)
    while True:

        ## pop up a menu
        print("""
        1) Read all available tickets
        2) Get ticket
        3) Create ticket
        4) Update ticket
        5) Delete ticket
        6) Exit
        7) DANGER! Delete all tickets
        """)

        ## collect input from user
        userinput = ""
        while userinput == "":
            userinput = input("> ")

        ## user wants ALL available tickets
        if userinput == "1":
            ticketlist = gettickets()
            if ticketlist:
                for ticket in ticketlist:
                    print(f"Ticket ID - {ticket}")
            else:
                print("There are no tickets in the system")
            
        ## user wants info on a single ticket
        elif userinput == "2":
            ticketid = input("What is the ticket ID? ")
            getoneticket(ticketid)

        ## user wants to create a ticket
        elif userinput == "3":
            descofissue = input("Give a short 140 char description of the issue: ")
            createdticket = createticket(descofissue)
            print(f"Ticket {createdticket} has been created.")

        ## user wants to update a ticket
        elif userinput == "4":
            descofissue = input("What is the updated 140 char description of the issue: ")
            updateticket(descofissue)

        ## user wants to delete a ticket
        elif userinput == "5":
            ticketid = input("What is the ticket ID? ")
            deleteticket(ticketid)

        ## user wants to exit
        elif userinput == "6":
            break

        elif userinput == "7":
            deletealltickets()

        ## user inputs a non valid option
        else:
            print("That is not a valid option")


    print("Thanks for using the Alta3 RESTful ticketing service")

if __name__ == "__main__":
    main()
