#!/bin/bash
#[NOM:t2GetByBoth.cgi][INFO:Extrae las lineas de ficheros MASK, que tienen etc.match(tipo) ]
echo "Content-type: text/plain;charset=utf-8"
echo ""

read params
  id=$(echo $params |cut -d'&' -f1 | cut -d'=' -f2)
tipo=$(echo $params |cut -d'&' -f2 | cut -d'=' -f2)
mask=$(echo $params |cut -d'&' -f3 | cut -d'=' -f2)

ahora=$(date +%Y%m%d-%H%M%S)
echo "[id0:$id][hora:$ahora][cgi:$0][fich:$mask.$tipo]" >> retoSYS/trazas

for f in $(ls model/*$mask*)
do
let n=$(head -1 $f | grep $tipo | wc -l)

if [ $n -gt 0 ]; then
echo $f
fi
done

echo "[error:$?]"
