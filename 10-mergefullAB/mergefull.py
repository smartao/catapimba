#!/usr/bin/python3
import openpyxl
from openpyxl.utils import column_index_from_string

# ######### Variavies de configuracoes #########

# Arquivo que contem o grupo maior de elementos
# com todos os elementos que DEVEM permanacer
arqA = "srv-novos.xlsx"
abaA = "Aplicacoes"
colMatchA = "C"
inicioA = 6  # Numero da linha que os dados iniciam

# Arquivo que contem o grupo de elementos ja editados
# com os elementos que seram removidos.
# Se os elementos existirem os dados já preenchidos seram copiados
arqB = "srv-de-para.xlsx"
abaB = "Servidores"
colMatchB = "B"
inicioB = 8  # Numero da linha que os dados iniciam

arqMerge = "merge.xlsx"  # Arquivo que tera os dados mesclados das planilhas
abaMerge = "ServidoresMerge"  # Aba que recebera os dados mesclados

# ##############################################

# Abrindo arquivos
wb1 = openpyxl.load_workbook(arqA)
wb2 = openpyxl.load_workbook(arqB)
wb3 = openpyxl.load_workbook(arqMerge)

# Abrind abas das planilhas
sheetA = wb1.get_sheet_by_name(abaA)
sheetB = wb2.get_sheet_by_name(abaB)
sheetMerge = wb3.get_sheet_by_name(abaMerge)

# Listas que serao utilizadas
srv1 = []
linha = []
coluna = []
srv2 = []

# Percorrendo planilha os vms e armazenando nas listas
for row in range(inicioA, sheetA.max_row + 1):
    srv1.append(sheetA[colMatchA + str(row)].value)

for row in range(inicioB, sheetB.max_row + 1):
    srv2.append(sheetB[colMatchB + str(row)].value)
    linha.append(row)

# Limpando todos os dados da planilha de merge
for row in sheetMerge.rows:
    for cell in row:
        sheetMerge.cell(row=cell.row, column=cell.column).value = ""

a = inicioB  # Comcecando de 2 para pular a primeinha linha

# Verificand
for srv in srv1:
    if srv in srv2:
        index = srv2.index(srv)
        # Percorrendo todas as colunas do arquivo
        for col in range(1, sheetB.max_column + 1):
            # Gravando todos valores das colunas do arquivoB no arquivo Merge
            sheetMerge.cell(row=a, column=col).value = sheetB.cell(
                row=index+inicioB, column=col).value
        # Gravando na ultima coluna o valor COMUM
        sheetMerge.cell(row=a, column=sheetB.max_column+1).value = "Comum"
    else:
        # Caso o item seja incomum, gravar apenas o nome do servidor
        sheetMerge.cell(row=a, column=column_index_from_string(
            colMatchB)).value = srv
        # Gravando na ultima coluna o valor INCOMUM
        sheetMerge.cell(row=a, column=sheetB.max_column+1).value = "Incomum"
    a = a + 1

for col in range(1, sheetB.max_column + 1):
    # Gravando os valores do cabecalho da primeira linha
    # inicioB-1 = Valor do cabecalho da planilha B
    sheetMerge.cell(
        row=inicioB-1, column=col).value = sheetB.cell(row=inicioB-1, column=col).value

# Salva as alteracoes no arquivo de merge
wb3.save(arqMerge)
