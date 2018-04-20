## Typical Usage

##### Using Docker CLI
```
docker run -d --name nicotine --restart=always \
-v /persistent/nicotine:/root/.nicotine \
-v /persistent/downloads:/root/nicotine-downloads \
-p 6080:6080 \
realies/nicotine
```

##### Using Docker Compose
```
docker-compose up -d
```
