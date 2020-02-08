eval $(docker-machine env manager)
docker stack rm clstr
docker-compose build
docker push sakorkko/hajariworker
docker push sakorkko/hajarimanager
docker stack deploy --compose-file docker-compose.yml clstr
