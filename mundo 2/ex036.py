vcasa = float(input('Qual o valor da casa ?'))
salario = float(input('Qual é o seu salário mensal ?'))
anos = int(input('Quantos anos você irá pagar ?'))

parcel = (anos * 12)  # multiplica o tempo inserido para pagamento, para descobrir as parcelas
prest = (vcasa / parcel)  # descobre o valor das prestações
maxprest = (salario * 0.30)
if prest <= maxprest:
    print('O emprestimo pode ser aprovado!')
else:
    print('Infelizmente seu emprétimo não pode ser feito.')
