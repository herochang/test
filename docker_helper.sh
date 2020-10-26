#!/bin/sh

display_usage() {
        echo 'This container has to be run using docker run --env MAC_ADDRESS_IO_API_KEY=key <image_name> mac_lookup.py <MAC_ADDRESS>'
        echo 'Example: docker run --env MAC_ADDRESS_IO_API_KEY=$SELF_API_KEY herochang/test:latest mac_lookup.py 44:38:39:ff:ef:57'
        }
display_usage
