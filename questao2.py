'''
2) Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo valor sempre será a soma dos 2 valores anteriores (exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...), escreva um programa na linguagem que desejar onde, informado um número, ele calcule a sequência de Fibonacci e retorne uma mensagem avisando se o número informado pertence ou não a sequência.>?
'''
def seq_fibonacci (numero):
    fibonacci = [0, 1]
    cont = 0
    while (cont < numero):
        termo = fibonacci[cont] + fibonacci[cont + 1]
        fibonacci.append(termo)
        if numero == termo:
            print(fibonacci)
            print(f'{numero} faz parte do fibonacci')
            break
        elif numero < termo:
            print(fibonacci)
            print(f'{numero} não faz parte do fibonacci')
            break
        else:
            cont += 1
numero = int(input('Digite um número: '))            
seq_fibonacci(numero)
