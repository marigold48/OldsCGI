#!/bin/bash
#[NOM:t2BorraFich.cgi][INFO:Mueve un fichero a temp]
echo "Content-type: text/plain;charset=utf-8"
echo ""

read params
   id=$(echo $params |cut -d'&' -f1 | cut -d'=' -f2)
fich1=$(echo $params |cut -d'&' -f2 | cut -d'=' -f2)
fich2=$(echo $params |cut -d'&' -f3 | cut -d'=' -f2)

ahora=$(date +%Y%m%d-%H%M%S)
echo "[id0:$id][hora:$ahora][cgi:$0][fich:$fich1]" >> retoSYS/trazas

if [ -f dbases/$fich1 ]
then
   cp dbases/$fich1 dbases/$fich2
else
   cp model/$fich1 model/$fich2
fi
echo "[error:$?]"

