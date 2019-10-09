#!/bin/bash
#[NOM:t2GetByMask.cgi][INFO:Lista los ficheros MASK]

echo "Content-type: text/plain;charset=utf-8"
echo ""

read params
  id=$(echo $params |cut -d'&' -f1 | cut -d'=' -f2)
mask=$(echo $params |cut -d'&' -f2 | cut -d'=' -f2)

ahora=$(date +%Y%m%d-%H%M%S)
echo "[id:$id][hora:$ahora][cgi:$0][fich:$mask]" >> retoSYS/trazas

ls dbases/*$mask*

echo "[error:$?]"
