#!/bin/bash
i=1
url="/artykul/zdjecia/castle-triathlon-malbork-2017-w-sobote-rywalizowali-na-1-4,4232614,artgal,27224282,t,id,tm,zid.html"
while true 
do
     img=$(curl -s http://malbork.naszemiasto.pl$url | grep -B 5 "zdjecie" | grep "ppstatic" | egrep -o "<img alt=\"\" src=[^>]*>" | sed 's/<img alt="" src=\"\([^"]*\).*/\1/g')
     wget -O $i.jpg $img
     i=$(($i+1))
     url=$(curl -s http://malbork.naszemiasto.pl$url | grep "następne zdjęcie" | egrep -o "href=[^>]*>" | sed 's/href=\"\([^"]*\).*/\1/g')
done
