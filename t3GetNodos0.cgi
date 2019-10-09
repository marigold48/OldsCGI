#!/bin/bash
#[NOM:t2GetByType.cgi][INFO:Lista los _nodos0 de ficheros con etc.match(tipo)]

echo "Content-type: text/plain;charset=utf-8"
echo ""

read params
  id=$(echo $params |cut -d'&' -f1 | cut -d'=' -f2)
tipo=$(echo $params |cut -d'&' -f2 | cut -d'=' -f2)
mask=$(echo $params |cut -d'&' -f3 | cut -d'=' -f2)

ahora=$(date +%Y%m%d-%H%M%S)
echo "[id:$id][hora:"$ahora"][cgi:"$0"][fich:"$mask"]" >> retoSYS/trazas


for f in $(ls model/*$mask*)
do
   nodo0=$(head -1 $f)
   if [[ $nodo0 == *"etc·:$tipo"* ]]
   then
      echo  "·[fich·:$f]$nodo0";
   fi
done

echo "[error:$?]"
