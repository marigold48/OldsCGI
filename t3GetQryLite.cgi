#!/bin/bash
#[NOM:t2GetQueryLite.cgi][INFO:Ejecuta la sentencia SQL en SQLite3]

echo "Content-type: text/plain;charset=utf-8"
echo ""

read params

  id=$(echo $params |cut -d'&' -f1 | cut -d'=' -f2)
  bd=$(echo $params |cut -d'&' -f2 | cut -d'=' -f2)
stmt=$(echo $params |cut -d'&' -f3 | cut -d'=' -f2)

ahora=$(date +%Y%m%d-%H%M%S)
echo "[id0:$id][hora:$ahora][cgi:$0][fich:$bd]" >> retoSYS/trazas


echo ".headers ON" > temp/"stmt_$id.sql"
echo $stmt > temp/"aux1_$id.txt"
. base64.sh -a decode -f temp/"aux1_$id.txt" >> temp/"stmt_$id.sql"

cat temp/"stmt_$id.sql" | sqlite3 $bd

echo "[error:$?]"

#rm -f temp/"aux1_$id.txt"
#rm -f temp/"stmt_$id.sql"

