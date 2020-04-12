#!/bin/bash

# Usado para caso precise deletar os SP que foram criados pelo
# Comadno ./createsp.sh

arq="splist.csv" # Arquivo csv para ser lido
dirlog="logs" # Diretorio de logs
validacao="FALSE" # Para caso precise executar apenas uma vez

for i in $(ls $dirlog)
do
    for appid in $(cat $dirlog/$i | grep -iE \"appid | cut -d" " -f 4 | sed 's/\"//g;s/\,//g')
    do
        # Deletando SP criado
        az ad sp delete --id $appid
    done
    
    # Se verdadeiro executar apenas uma vez o loop
    if [ $validacao == "TRUE" ];then
        break
    fi
done
