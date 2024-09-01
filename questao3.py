'''
3) Dado um vetor que guarda o valor de faturamento diário de uma distribuidora, faça um programa, na linguagem que desejar, que calcule e retorne:
• O menor valor de faturamento ocorrido em um dia do mês;
• O maior valor de faturamento ocorrido em um dia do mês;
• Número de dias no mês em que o valor de faturamento diário foi superior à média mensal.

IMPORTANTE:
a) Usar o json ou xml disponível como fonte dos dados do faturamento mensal;
b) Podem existir dias sem faturamento, como nos finais de semana e feriados. Estes dias devem ser ignorados no cálculo da média;
'''
def analise_faturamento (dados):
    i, numero_dias = 0, 0
    tamanho = len(dados[1])
    media = sum(dados[1])/tamanho
    print(f'A média do faturamento é: {media}')
    print(f'O maior faturamento foi de: R${max(dados[1])}')
    print(f'O menor faturamento foi de: R${min(dados[1])}')
    for i in range(0, tamanho):
        if dados[1][i] > media:
            numero_dias += 1
    print(f'Foram {numero_dias} dias em que o faturamento foi maior que a média')

import json
data_JSON = """
{
    "dia": [
        "segunda",
        "terca",
        "quarta",
        "quinta",
        "sexta"
    ],
    "valores": [
        2000,
        3200,
        1200,
        1500,
        2300
    ]
}
"""
dados_faturamento = json.loads(data_JSON)
dados = [dados_faturamento["dia"], dados_faturamento["valores"]]
analise_faturamento(dados)