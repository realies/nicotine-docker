from alpine:edge
run apk update && apk upgrade && \
 apk add --virtual build-dependencies py3-pip && \
 apk add bash supervisor xvfb x11vnc ttf-dejavu openbox dbus \
  # dark theme
  gtk+3.0 adwaita-icon-theme --no-cache && \
 apk add novnc nicotine-plus --update-cache --repository http://dl-3.alpinelinux.org/alpine/edge/testing/ --allow-untrusted && \
 # create and activate a virtual environment to install Python dependencies inside
 python3 -m venv /root/venv && \
 . /root/venv/bin/activate && \
 pip install mutagen && \
 mkdir -p /root/nicotine-downloads && \
 sed -i "s/scale', false/scale', true/" /usr/share/novnc/vnc_lite.html && \
 ln -s /root/nicotine-downloads /usr/share/novnc && \
 apk del build-dependencies && \
 rm -rf /var/cache/apk/*

env GTK_THEME=Adwaita:dark

add etc /etc
add usr /usr
entrypoint ["/usr/bin/supervisord","-c","/etc/supervisord.conf"]
