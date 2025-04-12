#!/bin/bash

ODATE=$1

if [ -z "$ODATE" ]; then
    ODATE=$(TZ=America/Sao_Paulo date +%Y-%m-%d)
    cat $ODATE
fi

sudo docker run --rm \
  -v ~/raw/NFS:/app/raw \
  -v ~/trusted/NFS:/app/trusted \
  --env-file /home/ubuntu/.env \
 python-image \
  --odate $ODATE 