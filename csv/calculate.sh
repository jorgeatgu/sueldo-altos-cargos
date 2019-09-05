#!/usr/local/bin/bash


readarray -t ccaa < ~/github/sueldo-altos-cargos/csv/ccaa.csv

for (( i=0; i<${#ccaa[@]}; ++i )); do

    csvstat --max ~/github/sueldo-altos-cargos/csv/"${ccaa[$i]}"-sueldo.csv >>  ~/github/sueldo-altos-cargos/csv/"${ccaa[$i]}"-max-min-mean.csv &&
    csvstat --min ~/github/sueldo-altos-cargos/csv/"${ccaa[$i]}"-sueldo.csv >>  ~/github/sueldo-altos-cargos/csv/"${ccaa[$i]}"-max-min-mean.csv &&
    csvstat --mean ~/github/sueldo-altos-cargos/csv/"${ccaa[$i]}"-sueldo.csv >>  ~/github/sueldo-altos-cargos/csv/"${ccaa[$i]}"-max-min-mean.csv

done
