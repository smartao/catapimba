#!/bin/bash

arq="splist.csv" # Arquivo csv para ser lido
dirlog="logs" # Diretorio de logs
readscope="TRUE" # Para caso nao precise ler os escopos
validacao="FALSE" # Para caso precise executar apenas uma vez

# Removendo todos os espacos do arquivo
sed -i 's/ /-/g' $arq

# Lendo a lista de todos service principal
for i in `cat splist.csv`
do
	# Atribuindo valores as variaiveis
    # id=`echo $i|cut -d, -f1`
    role=`echo $i|cut -d, -f2`
	name=`echo $i|cut -d, -f3`
    displayname=`echo $name | sed 's/-/ /g'`
    
    homepage=`echo $i|cut -d, -f4`
    logoutUrl=`echo $i|cut -d, -f5`
    scope=`echo $i|cut -d, -f6`

    # Criando o service principal com permissão padrão de leitura
    if [ $role != "NAOENCONTRADO" ];then
        if [ $readscope == "TRUE" ];then
            az ad sp create-for-rbac --name $name --role "$role" \ 
            --scopes "$scope" | tee $dirlog/$name.log
        else
            az ad sp create-for-rbac --name $name --role "$role" | tee $dirlog/$name.log
        fi
    else 
        az ad sp create-for-rbac --name $name --role "reader" | tee $dirlog/$name.log
    fi
    
    # Pegando o id do novo service principal
    newid=`cat $dirlog/$name.log | grep appId | cut -d" " -f 4 | sed 's/\"//g;s/\,//g'`
    
    # Caso existe, atualizando o service principal com home page
    if [ $homepage != "None" ];then
        az ad app update --id $newid --homepage $homepage
    fi
    
    # Se verdadeiro executar apenas uma vez o loop
    if [ $validacao == "TRUE" ];then
        break
    fi

 done