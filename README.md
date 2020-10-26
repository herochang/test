
# MAC Address Vendor lookup CLI

MAC lookup CLI allows you to retrieve information about a MAC address.
The python script can be used to query https://macaddress.io/ to get vendor related information about a device MAC Address.

## Getting Started

### Prepare：

You need a standard installation of Python3 that can be obtained here
All you need to get started is sign up for an account here and obtain your API key.

### Usage

Using this tool requires signing up for a macaddress.io account and getting an API key here.
Export the API key as an environment variable MACADDRESSIO_API_KEY before running the script.

macOS and Linux
export MAC_ADDRESS_IO_API_KEY="your-api-key"
On linux and MacOS

Example:

**export MAC_ADDRESS_IO_API_KEY=at_VKIvhPfcPffhywNDMx61r0E1gAhKW**



Basic run

    ./mac_lookup.py 44:38:39:ff:ef:57

This should give output of the company name. For the above example it would show:

Cumulus Networks, Inc

Complete information run
Example:

    ./mac_lookup.py 44:38:39:ff:ef:57 -r

Output:

    {"vendorDetails":{"oui":"443839","isPrivate":false,"companyName":"Cumulus Networks, Inc","companyAddress":"650 Castro Street, suite 120-245 Mountain View CA 94041 US","countryCode":"US"},"blockDetails":{"blockFound":true,"borderLeft":"443839000000","borderRight":"443839FFFFFF","blockSize":16777216,"assignmentBlockSize":"MA-L","dateCreated":"2012-04-08","dateUpdated":"2015-09-27"},"macAddressDetails":{"searchTerm":"44:38:39:ff:ef:57","isValid":true,"virtualMachine":"Not detected","applications":["Multi-Chassis Link Aggregation (Cumulus Linux)"],"transmissionType":"unicast","administrationType":"UAA","wiresharkNotes":"No details","comment":""}}


## Running with Docker




## Security
