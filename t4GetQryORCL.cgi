#!/bin/bash
#[NOM:t2GetQueryORCL.cgi][INFO:Ejecuta la sentencia SQL en Oracle]

echo "Content-type: text/plain;charset=utf-8"
echo ""

read params

  id=$(echo $params |cut -d'&' -f1 | cut -d'=' -f2)
  bd=$(echo $params |cut -d'&' -f2 | cut -d'=' -f2)
  SO=$(echo $params |cut -d'&' -f3 | cut -d'=' -f2)
stmt=$(echo $params |cut -d'&' -f4 | cut -d'=' -f2)

ahora=$(date +%Y%m%d-%H%M%S)
echo "[id:$id][hora:$ahora][cgi:$0][fich:$bd]" >> retoSYS/trazas


NL=$'\n'
echo "connect $bd" > temp/"stmt_$id.sql"
echo "set trimspool ON" >>  temp/"stmt_$id.sql"
echo "set colsep |" >>  temp/"stmt_$id.sql"
echo "set linesize 1000" >> temp/"stmt_$id.sql"
echo "set pagesize 1000" >> temp/"stmt_$id.sql"
echo "spool temp/ORA_$id.log" >> temp/"stmt_$id.sql"

echo $stmt > temp/"aux1_$id.txt"
. base64.sh -a decode -f temp/"aux1_$id.txt" >> temp/"stmt_$id.sql"

echo "$NL" >> temp/"stmt_$id.sql"
echo "spool off" >> temp/"stmt_$id.sql"

if [ $SO = CENTOS ]
then
	export ORACLE_HOME=/u01/app/oracle/product/11.2.0/xe
	export ORACLE_SID=XE
	export PATH=$PATH:$ORACLE_HOME/bin/
else
	export ORACLE_HOME=/usr/lib/oracle/xe/app/oracle/product/10.2.0/server
	export ORACLE_SID=XE
	export PATH=$PATH:$ORACLE_HOME/bin/
fi

sqlplus /nolog @temp/"stmt_$id.sql" > temp/nada

cat "temp/ORA_$id.log" | sed 's/  //g' | sed 's/ |/|/g' | sed 's/| /|/g'

