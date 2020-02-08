#!/bin/bash
docker-machine rm -y manager worker1 worker2 worker3
docker stack rm clstr
docker-machine create --driver virtualbox manager
docker-machine create --driver virtualbox worker1
docker-machine create --driver virtualbox worker2
docker-machine create --driver virtualbox worker3
eval $(docker-machine env manager)
Ip=`docker-machine ip manager`
docker-machine ssh manager "docker swarm init --advertise-addr ${Ip}"
Token=`docker-machine ssh manager docker swarm join-token worker | grep token | awk '{ print $5 }'`
docker-machine ssh worker1 "docker swarm join --token ${Token} ${Ip}:2377"
docker-machine ssh worker2 "docker swarm join --token ${Token} ${Ip}:2377"
docker-machine ssh worker3 "docker swarm join --token ${Token} ${Ip}:2377"
docker-compose build
docker stack deploy --compose-file docker-compose.yml clstr
echo "You can connect with the ip:"
echo ${Ip}
echo "Use the port 8080 for the visualizer."
echo "Any of the workers ip addresses for for all cases work as well."