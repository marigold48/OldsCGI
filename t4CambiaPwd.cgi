#!/bin/bash
#[NOM:t4CambiaPwd.cgi][INFO:Cambia usuario|password encriptados]

echo "Content-type: text/plain;charset=utf-8"
echo ""
read params
  id=$(echo $params |cut -d'&' -f1 | cut -d'=' -f2)
 usr=$(echo $params |cut -d'&' -f2 | cut -d'=' -f2)
pwd0=$(echo $params |cut -d'&' -f3 | cut -d'=' -f2)
pwd1=$(echo $params |cut -d'&' -f4 | cut -d'=' -f2)

ahora=$(date +%Y%m%d-%H%M%S)
echo "[id0:$id][hora:$ahora][cgi:$0][fich:NdN]" >> retoSYS/trazas

tira=$(echo $usr$pwd0 | md5sum)

cat retoSYS/retoUsrsPwds.txt | grep -v $tira > temp/"aux1$id"

echo $usr$pwd1 | md5sum >>  temp/"aux1$id"

cat temp/"aux1$id" > retoSYS/retoUsrsPwds.txt

echo "[error:$?]"
