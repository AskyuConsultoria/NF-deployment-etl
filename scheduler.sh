#!/bin/bash

HORA=$1
MINUTO=$2

if [ -z "$HORA" ] ; then
    HORA=17
fi

if [ -z "$MINUTO" ]; then
    MINUTO=0
fi

SCRIPT="/home/ubuntu/NF-deployment-etl/run.sh"

LOG="/home/ubuntu/NF-deployment-etl/run.log"

CRON_LINHA="$MINUTO $HORA * * * $SCRIPT >> $LOG 2>&1"

# Remove qualquer linha que contenha o caminho do script
crontab -l 2>/dev/null | grep -v "$SCRIPT" | crontab -

# Adiciona a nova linha
(crontab -l 2>/dev/null; echo "$CRON_LINHA") | crontab -

echo "Crontab atualizado para executar às $HORA:$MINUTO"
