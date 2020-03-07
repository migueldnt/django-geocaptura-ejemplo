export $(cat database.env | xargs) 
export PGPASSWORD=$PG_PASSWORD
#psql -h $PG_HOST -U $PG_USER -d postgres -p $PG_PORT -c "select 2+2;" 

psql -h $PG_HOST -U $PG_USER -d postgres -p $PG_PORT -w -c "create database ${PG_DB};"
psql -h $PG_HOST -U $PG_USER -d $PG_DB -p $PG_PORT -w -c "create extension postgis;"