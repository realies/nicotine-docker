#!/bin/sh
# TODO allow nicotine to do upnp port forwarding as if it was on the host.

# Check if upnpc is installed
if ! command -v upnpc; then
    echo "upnpc could not be found. Please install miniupnpc"
    exit 1
fi
upnpc -r 2234 tcp 
docker compose up -d