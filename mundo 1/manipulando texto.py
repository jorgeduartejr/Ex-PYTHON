frase = "Curso em Video Python"
frase[9:13]   'De 9 até 13, incluido o 9 e excluindo o 13'
frase[9:21:2] 'De 9 até 21, pulando de 2 em 2'
frase[:5] 'É igual a de 0 até 5'
frase[15:] 'É igual a 15 até o final'
frase[9::3] 'Vai de 9 até o final, pulado de 3 em 3'

len(frase) 'Analisar quantos caracteres aparece na frase'

frase.count('o') 'Contar quantas vezes aparece a letra (o)'
frase.count('o',0,13) 'Contar de 0 a 13'
frase.find('deo') 'Encontrar onde esta dizendo deo'

frase.find('Android') 'Se nao existir a função str, ele retorna o comando -1'
'Curso' in frase 'ele dirá se existe a palava, com true ou false'

frase.replace('Python','Android') 'Ele substitui a palavra Python em android'
frase.upper() 'transforma o que esta em minusculo em maiusculo'
frase.lower() 'transforma o que esta em maisculo em minusculo'
frase.capitalize() 'Joga em tudo para minusculo, menos a primeira letra da frase'
frase.title() 'analisa onde tem espaço, e o começo de cada palavra fica maiscula'
frase.strip() 'remove todos os espaços inuteis, os do começo e do final'
frase.rstrip() 'remove os espaços da direita'
frase.lstrip() 'remove os espaços da esquerda'

Divisão de strings
frase.split() 'divisão da sua string, nos espaços'
Junção de stings
'-'join(frase) 'onde tem espaço na frase coloca um traço'
'Para printar um texto grande, coloca tudo em """xxx""" '





