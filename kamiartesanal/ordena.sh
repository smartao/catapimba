#!/bin/bash

# Arquivo gerado pelo todoist
ARQENTRADA=ordemtemp.txt
# Arquivo de saida usado para gerar os post
ARQSAIDA=ordem.xls

# Filtrando apenas dados validos
grep -i postar $ARQENTRADA | cut -d" " -f 2 

# Removendo arquivo temporario
rm $ARQENTRADA
