#!/bin/bash

arq="splist.csv" # Arquivo csv para ser lido
dirlog="logs" # Diretorio de logs

# Removendo todos os espacos do arquivo
sed -i 's/ /-/g' $arq

# Lendo a lista de todos service principal
for i in `cat splist.csv`
do
	# Atribuindo valores as variaiveis
    # id=`echo $i|cut -d, -f1`
	name=`echo $i|cut -d, -f2`
    displayname=`echo $name | sed 's/-/ /g'`
    homepage=`echo $i|cut -d, -f3`
    logoutUrl=`echo $i|cut -d, -f4`

    # Criando o service princiapl com permissão padrão de leitura
    az ad sp create-for-rbac --name $name --role reader | tee $dirlog/$name.log

    # Pegando o id do novo service principal
    newid=`cat $dirlog/$name.log | grep appId | cut -d" " -f 4 | sed 's/\"//g;s/\,//g'`
    
   # Caso existe, atualizando o service principal com home page
   if [ $homepage != "None" ];then
        az ad app update --id $newid --homepage $homepage
   fi


done