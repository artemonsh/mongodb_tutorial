Запуск MongoDB в Docker контейнере
```
docker run --name mongodb_container \
      -e MONGO_INITDB_ROOT_USERNAME=admin \
      -e MONGO_INITDB_ROOT_PASSWORD=secretpassword \
      -p 27017:27017 \
      mongo:latest
```

Видео: https://www.youtube.com/watch?v=AiXIBbuAkoY