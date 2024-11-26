## Typical Usage

After adjusting `docker-compose.yml` to mount your shares and a download folder from the host,

##### With upnp port forwarding
```
upnp-and-run.sh
```

##### Without
```
docker-compose up -d
```

## Notes

The web interface is only on localhost but that can be changed.
