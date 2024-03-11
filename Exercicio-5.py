#5) Escreva um programa que inverta os caracteres de um string.

#IMPORTANTE:

#a) Essa string pode ser informada através de qualquer entrada de sua preferência ou pode ser previamente definida no código;

#b) Evite usar funções prontas, como, por exemplo, reverse;

def inverte_string(string):
    nova_string = ""
    for i in range(len(string) - 1, -1, -1):
        nova_string += string[i]
    return nova_string

texto = input("Informe uma string: ")
print("String invertida:", inverte_string(texto))