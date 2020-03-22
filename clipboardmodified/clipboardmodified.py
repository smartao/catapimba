#!/usr/bin/python3
import pyperclip


def main():
    # Recebendo valor do clipboard
    string = pyperclip.paste()

    esp = "  "  # Espacamento usado no comeco do arquivo

    # Validando qual e o delimitador do objeto
    if ';' in string:
        delimitador = ";"
    elif ',' in string:
        delimitador = ","
    elif '.' in string:
        delimitador = "."
    else:
        delimitador = " "

    # Transformando a string em uma lista
    lines = string.split(delimitador)

    # percorre todos os indicies da lista 'lines'
    for i in range(len(lines)):
        lines[i] = esp * 3 + '"' + lines[i] + '",'
    text = '\n'.join(lines)  # Juntando tudo em uma string
    pyperclip.copy(text)  # Colando de volta no clipboard


if __name__ == '__main__':
    main()
