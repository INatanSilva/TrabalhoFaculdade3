def escolha_servico():
    while True:
        servico = input('Escolha o serviço (DIG/ICO/IBO/FOT): ').upper()
        input()
        if servico in ['DIG', 'ICO', 'IBO', 'FOT']:
            return servico
        else:
            print('Opção inválida. Tente novamente...')
            
def num_pagina():
    while True:
        try:
            num_paginas = int(input('Digite o número de páginas: '))
            if num_paginas < 10:
                return num_paginas
            elif 10 <= num_paginas < 100:
                return (num_paginas) - int(num_paginas * 0.1)
            elif 100 <= num_paginas < 1000:
                return (num_paginas) - int(num_paginas * 0.15)
            elif 1000 <= num_paginas < 10000:
                return (num_paginas) - int(num_paginas * 0.2)
            elif num_paginas >= 10000:
                print('Número de páginas maior ou igual a 10000 não é aceito. Tente novamente...')
            else:
                print('Número de páginas inválido. Tente novamente...')
        except ValueError:
            print('Digite um valor numérico. Tente novamente...')

def servico_extra():
    while True:
        print('Deseja adicionar mais algum serviço?')
        print('1 - Encadernação Simples - R$10,00')
        print('2 - Encardenação Capa Dura - R$25,00')
        print('0 - Desejo mais nada')
        adicional = input()
        if adicional in ['1', '2', '0']:
            return adicional
        else:
            print('Opção inválida. Tente novamente...')

def main():
    # Boas-vindas
    print('Bem-vindo ao Sistema de Cobrança da Copiadora Natan Dos Santos Silva')
    print('DIG - Digitalização')
    print('ICO - Impressão Colorida')
    print('IPB - Impressão Preto e Branco')
    print('FOT - Fotocópia')
    
    # Escolha do serviço
    servico = escolha_servico()
    
    # Número de páginas
    num_paginas_descontado = num_pagina()
    
    # Serviço adicional
    adicional = servico_extra()

    # Cálculo do valor total
    valor_servico = {'DIG': 1.10, 'ICO': 1.00, 'IBO': 0.40, 'FOT': 0.20}
    extra = {'1': 10, '2': 25, '0': 0}
    total_pagar = valor_servico[servico] * num_paginas_descontado + extra[adicional]

    # Exibição do resultado
    print(f'\nServiço escolhido: {servico}')
    print(f'Número de páginas: {num_paginas_descontado}')
    print(f'Serviço adicional: {adicional} - {"" if adicional == "0" else "Encadernação simples" if adicional == "1" else "Encadernação de capa dura"}')
    print(f'Total a pagar: R$ {total_pagar:.2f}')

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f'Ocorreu um erro: {e}')