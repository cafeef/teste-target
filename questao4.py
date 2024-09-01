'''
4) Dado o valor de faturamento mensal de uma distribuidora, detalhado por estado:
• SP – R$67.836,43
• RJ – R$36.678,66
• MG – R$29.229,88
• ES – R$27.165,48
• Outros – R$19.849,53
Escreva um programa na linguagem que desejar onde calcule o percentual de representação que cada estado teve dentro do valor total mensal da distribuidora.
'''
def calculo_porcentagem(representacao):
    total = sum(representacao[1])
    tamanho = len(representacao[1])
    for i in range(0, tamanho):
        elemento = round(representacao[1][i])
        porcentagem = round((elemento/total) * 100, 2)
        print(f'{representacao[0][i]}: {porcentagem}%')
        
representacao = [['SP', 'RJ', 'MG', 'ES', 'OUTROS'], [67836.43, 36678.66, 29229.88, 27165.48, 19849.53]]
calculo_porcentagem(representacao)
