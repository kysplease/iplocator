import argparse
import requests
import webbrowser
from colorama import Fore, init


def locate(ip, pp):
    init(autoreset=True)  # initiate colorama, automatically reset color

    r = requests.get("http://ip-api.com/json/{}".format(ip))  # get json data about the IP

    json = r.json()  # store json data in "json" variable

    if json.get("status") == "success":  # display the data if the request was successful
        keys = ["query", "country", "countryCode", "region", "regionName", "city",
                "zip", "timezone", "lat", "lon", "org", "isp", "as"]

        for i in range(0, len(keys)):
            print("{}{}: {}".format(Fore.LIGHTGREEN_EX, keys[i].upper(),
                                    json.get(keys[i])))

        if pp:  # if the pinpoint parameter was supplied, open google maps at the latitude and longitude of the IP
            webbrowser.open("https://www.google.com/maps/search/?api=1&query={},{}".format(
                json.get(keys[8]), json.get(keys[9])), autoraise=True)
    else:
        print("{}IP location failed! Maybe the address is invalid or down?".format(Fore.LIGHTRED_EX))  # display if request was unsuccessful


def main():  # parse arguments
    init()  # initiate colorama without automatically resetting the color

    iplocator = """{} \t[+++] IPLocator v1.1 by kysplease [+++]
  _____ _____  _                     _             
 |_   _|  __ \| |                   | |            
   | | | |__) | |     ___   ___ __ _| |_ ___  _ __ 
   | | |  ___/| |    / _ \ / __/ _` | __/ _ \| '__|
  _| |_| |    | |___| (_) | (_| (_| | || (_) | |   
 |_____|_|    |______\___/ \___\__,_|\__\___/|_|   {}""".format(Fore.LIGHTGREEN_EX,
                                                                Fore.RED)

    print(iplocator)

    parser = argparse.ArgumentParser()
    parser.add_argument("ip", help="IP to locate")
    parser.add_argument("-pp", "--pinpoint", action='store_true',
                        default=False, dest='pp',
                        help="Open the latitude and longitude in google maps, default is false")
    args = parser.parse_args()

    locate(args.ip, args.pp)

if __name__ == '__main__':
    main()
