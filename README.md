## What? Why?

- Docker brings up the service
- More secure, eg docker mounts the shared folder read-only
- Remote access to the nicotine UI

## Typical Usage

After adjusting `docker-compose.yml` to mount your shares and a download folder from the host, browse http://localhost:6080 after either:

##### With upnp port forwarding
```
./upnp-and-run.sh
```

##### Without
```
docker-compose up -d
```

## Notes

The web interface is only on localhost but that can be changed.

If your host system's user id (`$ id -u`) isn't 1000 you will have to edit `downloads-ownership.py`

## Bugs

 - upnp process needs to be repeated after a while.
