#!/bin/bash
set -euo pipefail
IFS=$'\n\t'

pip3 install . --break-system-packages

echo "Easy difficulty"

offset=408

mkdir -p cases/easy
for i in $(seq 1 5) ; do
	mystery-o-matic scenarios/simple.template.sol static/ cases/easy/$i --seed $(($offset + 1000 + $i * 20)) --difficulty easy --mode latex --max-time-slots 8 --nplaces 3 --location mansion --difficulty easy
done

for i in $(seq 6 15) ; do
	mystery-o-matic scenarios/simple.template.sol static/ cases/easy/$i --seed $(($offset + 1000 + $i * 20)) --mode latex --max-time-slots 9 --nplaces 4 --location mansion --difficulty easy
done

echo "Medium difficulty"

mkdir -p cases/medium
for i in $(seq 1 15) ; do
	mystery-o-matic scenarios/simple.template.sol static/ cases/medium/$i --seed $(($offset + 2000 + $i * 20)) --mode latex --max-time-slots 9 --nmoves 5 --nplaces 5 --nchars 4
done

echo "Hard difficulty"

mkdir -p cases/hard
for i in $(seq 1 15) ; do
	mystery-o-matic scenarios/simple.template.sol static/ cases/hard/$i --seed $(($offset + 3000 + $i * 20)) --mode latex --max-time-slots 10 --nmoves 6 --nplaces 5 --nchars 4
done
