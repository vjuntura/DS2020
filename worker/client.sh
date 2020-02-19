#!/bin/sh
while :
do
	#Get random number between 1 and 100
	r=$(shuf -i 1-100 -n 1)

	#GET the restAPI with sensor name and value
	wget "manager:5000/?value=$r&sensor=$(hostname)" --spider
	sleep 1
done
