#!/usr/local/bin/bash


readarray -t ccaa < ~/github/sueldo-altos-cargos/csv/ccaa.csv

for (( i=0; i<${#ccaa[@]}; ++i )); do

    csvgrep -c CCAA -r "${ccaa[$i]}$" ~/github/sueldo-altos-cargos/csv/sueldos.csv >> ~/github/sueldo-altos-cargos/csv/"${ccaa[$i]}"-sueldo.csv

done
