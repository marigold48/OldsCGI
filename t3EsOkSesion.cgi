#!/bin/bash
#[NOM:t2EsOkSesion.cgi][INFO:Devuelve la Sesion que contiene el IdSesion]

echo "Content-type: text/plain;charset=utf-8"
echo ""
read params
  id=$(echo $params |cut -d'&' -f1 | cut -d'=' -f2)

ahora=$(date +%Y%m%d-%H%M%S)
echo "[id0:$id][hora:$ahora][cgi:$0][fich:NdN]" >> retoSYS/trazas

cat retoSYS/retoSesiones.txt | grep $id

