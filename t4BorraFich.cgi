#!/bin/bash
#[NOM:t2BorraFich.cgi][INFO:Mueve un fichero a temp]
echo "Content-type: text/plain;charset=utf-8"
echo ""

read params
  id=$(echo $params |cut -d'&' -f1 | cut -d'=' -f2)
fich=$(echo $params |cut -d'&' -f2 | cut -d'=' -f2)

ahora=$(date +%Y%m%d-%H%M%S)
echo "[id0:$id][hora:$ahora][cgi:$0][fich:$fich]" >> retoSYS/trazas

mv model/$fich temp/$fich

echo "[error:$?]"

