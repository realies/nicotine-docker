## What? Why?

- Docker brings up the service
- More secure, eg docker mounts the shared folder read-only
- Remote access to the nicotine UI

## Typical Usage

Adjust `docker-compose.yml` to mount your shares and a download folder from the host, then:

#### With vncviewer
```
./bin/nico
```
Faster and better to copy+paste with. It seems to favour the middle-click selection buffer. It also doesn't like copying from Qt or gtk apps (on wayland?), though pasting into the browser's address bar, selecting that, and then pasting into vncviewer works for me.

#### With browser

Browse http://localhost:6080 after either:

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
 - UI slowness. should peel the top layer off the python code a put into javascript, to lower UI latency, eg to be able to scroll shares smoothly.
