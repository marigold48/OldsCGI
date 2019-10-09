echo "creando BD SQLite"
cat tablas_cursos.txt | sqlite3 /usr/lib/cgi-bin/Kurso/retoSYS/retoCursos.sqlite
