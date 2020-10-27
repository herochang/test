#!/usr/bin/env python3
import argparse
import logging
import os
import re
import sys
import urllib.request
import json

# To get a logger for the script
log = logging.getLogger(__name__)
logging.basicConfig(level=logging.DEBUG)
log.setLevel(logging.DEBUG)


def request_url(mac_address, api_key):
    req_url = "https://api.macaddress.io/v1"
    query_params = {"output": "json", "search": mac_address}
    encoded_url = "{0}?{1}".format(req_url, urllib.parse.urlencode(query_params))
    auth_header = {"X-Authentication-Token": api_key}
    req = urllib.request.Request(encoded_url, headers=auth_header)
    return req

def get_response(request):
    """
    Returns response obtained from the request
    Args: request URL object
    Return: json output
    """

    try:
        response = urllib.request.urlopen(request)
        output = response.read().decode("utf-8")
        return output
    except urllib.error.HTTPError:
        logging.error(
            "status code:{0} message:{1}".format(response.status, response.msg)
        )
        exit(response.status)
    finally:
        response.close()


def validate_macaddress(mac_address):
    """
    function to validate mac address
    Args: mac_address
    Type mac_address: str
    Return: True if valid format
    """

    return re.match("^([0-9A-Fa-f]{2}[:.-]?){5}([0-9A-Fa-f]{2})$", mac_address.strip())


def formatted_output(response):
    output_str = ""
    try:
        response_dict = json.loads(response)
        if 'vendorDetails' in response_dict.keys():
            output_str = response_dict['vendorDetails']['companyName']
        else:
            output_str = None
    except ValueError as e:
        logging.error("Could not load JSON output to string.")
    return output_str

class bcolors:
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'

    def disable(self):
        self.OKGREEN = ''
        self.WARNING = ''
        self.FAIL = ''
        self.ENDC = ''

def main():
    """Main function
    """

    parser = argparse.ArgumentParser(description="Query macaddress.io vendor associated with the mac address")

    parser.add_argument("macaddr", type=str, help="MAC Address of the device")

    parser.add_argument(
        "-r",
        "--rawjson",
        help="return raw json",
        action="store_true",
    )

    args = parser.parse_args()
    mac_address = args.macaddr


    try:
        api_key = os.environ["MAC_ADDRESS_IO_API_KEY"]
        if api_key == "":
            logging.error("Please set the environment variable MAC_ADDRESS_IO_API_KEY")
            sys.exit(1)
    except KeyError:
        logging.error("Please set the environment variable MAC_ADDRESS_IO_API_KEY")
        sys.exit(1)
    if not validate_macaddress(mac_address):
        logging.error("Mac_address is invalid")
        sys.exit(1)
    response = get_response(request_url(mac_address, api_key))

    if args.rawjson:
        print(response)
        sys.exit(0)
    name_output = formatted_output(response)
    if len(name_output.strip()) == 0:
        print (bcolors.WARNING + "Not found companyName"+ bcolors.ENDC)
    else:
        print (bcolors.OKGREEN + name_output+ bcolors.ENDC)


if __name__ == "__main__":
    main()
