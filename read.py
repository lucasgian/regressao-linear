// https://pt.stackoverflow.com/questions/97269/como-ler-um-arquivo-csv-em-python
import csv, sys
nome_ficheiro = 'ficheiro.csv'
with open(nome_ficheiro, 'rb') as ficheiro:
    reader = csv.reader(ficheiro)
    try:
        for linha in reader:
            print linha
    except csv.Error as e:
        sys.exit('ficheiro %s, linha %d: %s' % (nome_ficheiro, reader.line_num, e))