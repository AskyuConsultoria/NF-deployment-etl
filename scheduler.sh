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

# Verifica se já existe essa linha no crontab
(crontab -l 2>/dev/null | grep -F "$SCRIPT") >/dev/null

if [ $? -eq 0 ]; then
    echo "A tarefa já está agendada no crontab."
else
    (crontab -l 2>/dev/null; echo "$CRON_LINHA") | crontab -
    echo "Tarefa adicionada ao crontab com sucesso!"
fi
