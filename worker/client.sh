#!/bin/sh
while :
do
	r=$(shuf -i 1-100 -n 1)
	wget "manager:5000/?value=$r&sensor=$(hostname)" --spider
	sleep 1
done