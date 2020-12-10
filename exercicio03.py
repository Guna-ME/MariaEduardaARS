produto = int(input('Digite o valor do produto: R$'))

def pagamento(variavel):
    opc = int(input('''
    1- A vista
    2- Prazo 1x no cartão
    3- Prazo da loja 5x
    4- Prazo da loja 10x
    Insira a opção de pagamento: '''))

    if opc==1:
        print('Valor original:     R$', produto)
        print('Desconto ganho:     R$', produto * 0.50)
        print('Valor com desconto: R$', produto * 0.50)
        consultar()

    elif opc==2:
        print('Valor original:     R$', produto)
        print('Desconto ganho:     R$', produto * 0.10)
        print('Valor com desconto: R$', produto * 0.90)

    elif opc==3:
        print('Valor original:     R$', produto)
        print('Taxa:               R$', produto * 0.2)
        print('Valor com taxa:     R$', produto + 10%)
        print('Valor das parcelas: R$', produto / 5)
        consultar()

    elif opc==4:
        print('Valor original:     R$', produto)
        print('Taxa:               R$', produto * 0.2)
        print('Valor com taxa:     R$', produto + 50%)
        print('Valor das parcelas: R$', produto / 10)
        consultar()
   