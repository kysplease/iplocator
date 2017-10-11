import argparse
import requests
from colorama import Fore, init
init(autoreset=True)

parser = argparse.ArgumentParser(description="IPLocator v1.0 by kysplease")
parser.add_argument("ip", help="IP to locate")
args = parser.parse_args()

r = requests.get("http://ip-api.com/json/{}".format(args.ip))

data = dict(r.json())

if data.get("status") == "success":
    keys = ["query", "country", "countryCode", "region", "regionName", "city",
            "zip", "timezone", "lon", "lat", "org", "isp", "as"]

    for i in range(0, len(keys)):
        print("{}{}: {}".format(Fore.LIGHTGREEN_EX, keys[i].upper(),
                                      data.get(keys[i])))

else:
    print("{}IP location failed! Maybe the address is invalid or down?".format(Fore.LIGHTRED_EX))
