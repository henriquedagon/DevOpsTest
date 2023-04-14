#!/bin/bash

OUTFILE=output.txt


while [ true ]; do
    date +'%F %T' >> ${OUTFILE}
    sleep 60
done