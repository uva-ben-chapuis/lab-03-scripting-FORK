#!/bin/bash
set -euo pipefail

curl -O https://s3.amazonaws.com/ds2002-resources/labs/lab3-bundle.tar.gz

tar -xzf lab3-bundle.tar.gz

awk '!/^[[:space:]]*$/' lab3_data.tsv > cleaned.tsv

sed 's/\t/,/g' cleaned.tsv > converted.csv

ROWS=$(tail -n +2 converted.csv | wc -l | tr -d ' ')

echo "Data rows remaining: $ROWS"

tar -czf converted-archive.tar.gz converted.csv