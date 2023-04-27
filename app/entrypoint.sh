#!/bin/bash

# Logs start up
service ssh start

OUTFILE=output/output.txt

rm -rf ${OUTFILE}

date +'%F %T' >> ${OUTFILE}

while [ true ]; do
    sleep 60
done