'''
5) Escreva um programa que inverta os caracteres de um string.

IMPORTANTE:
a) Essa string pode ser informada através de qualquer entrada de sua preferência ou pode ser previamente definida no código;
b) Evite usar funções prontas, como, por exemplo, reverse;
'''
def inverte_string (string_original):
    string_lista = list(string_original)
    string_invertida = ''
    i = len(string_original) - 1
    while i >= 0:
        string_invertida = string_invertida + string_lista[i]
        i -= 1
    print(f'A string invertida é: {string_invertida}')

string_original = input('Digite a string que deseja inverter: ')
inverte_string(string_original)