#!/usr/bin/python3

import pandas as pd

def main():
    flightcsv = pd.read_csv("airline_flights.csv")

    # organize data by origin and destination airport
    flightcsv_tofrom = flightcsv.groupby(['ORG_AIR', 'DEST_AIR']).size()
    print(flightcsv_tofrom.head())

    # Dispaly the number of flights between Huston (IAH)
    # and Atlanta (ATL) in both directions
    print("\nFlight from ATL to IAH and IAH to ATL")
    print(flightcsv_tofrom.loc[[("ATL", "IAH"), ("IAH", "ATL")]])

    # display first 5 entries of the flightcsv dataframe
    # print(flightsv.head())
    print()
    print(flightcsv)

    # display first 5 entries of the ciscojson dataframe            
    # print(ciscojson.head())

    # ciscodf = pd.concat([ciscocsv, ciscojson])
    # uncomment the line below to "fix" the index issue
    # ciscodf = pd.concat([ciscocsv, ciscojson], ignore_index=True, sort=False)

    # print(ciscodf)

if __name__ == "__main__":
    main()
