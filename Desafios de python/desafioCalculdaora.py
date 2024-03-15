import math


def calculadoraSimples(num1, num2, opera):
    
    if opera == 1:
       return num1 + num2
    elif opera == 2:
       return num1 - num2 
    elif opera == 3:
       return num1 * num2 
    elif opera == 4:
        if num2 != 0:
            return num1 / num2
        else:
            return "Não é possivel dividor por zero"
    else:
        return "Operacao invalida"         

def calculadoraAvancada(num1,num2, opera):
    if opera == 1:
        return num1**num2
    elif opera == 2:
        return num1**2
    elif opera == 3:
         
        if num1 <= 0 or num2 <= 0:
            return "Base e valor devem ser maiores que zero."
        resultado = 0
        while num1 >= num2:
            num1 /= num2
            resultado += 1
        return resultado
    elif opera == 4:
      
        seno = calculoTrigonometria(num1, 'sin')
        cosseno = calculoTrigonometria(num1, 'cos')
        tangente = calculoTrigonometria(num1, 'tan')
        return seno, cosseno, tangente
    else:
        return "Operação inválida"

def calculoTrigonometria(x, func='sin', terms=10):
    def fatorial(n):
        if n == 0:
            return 1
        else:
            return n * fatorial(n-1)
    x_radianos = math.radians(x)
    x_radianos %= 2 * math.pi
    resultado = 0
    for n in range(terms):
        sinal = (-1) ** n
        if func == 'sin':
            term = (x_radianos ** (2*n + 1)) / fatorial(2*n + 1)
        elif func == 'cos':
            term = (x_radianos ** (2*n)) / fatorial(2*n)
        elif func == 'tan':
            term = (x_radianos ** (2*n + 1)) / fatorial(2*n + 1)
            resultado += sinal * term
            continue
        resultado += sinal * term
    return resultado

    
sair = 1
while sair == 1:
    try:
        calc = int(input("Qual calculadora você quer usar? \n0 - Simples\n1 - Avancada\n "))
    
       
        if calc == 0:
             
             opera = int(input("Qual operacao voce deseja realizar? \n1 - Soma\n2 - Subtracao\n3 - Multiplicacao  \n4 - Divisao\n0 - Alterar Calculadora \n  "))
             num1 = float(input("Digite um número: "))
             num2 = float(input("Digite mais um número: "))
             if opera == 0:
                 continue
             resultado = calculadoraSimples(num1,num2,opera)
             
        elif calc == 1:
            
            opera = int(input("Qual operacao avancada voce deseja realizar? \n1 - Exponenciacao\n2 - Raiz Quadrada\n3 - Logaritmos  \n4 - Trigonometria \n0 - Alterar Calculadora\n " ))
            
            if opera == 0:
                continue
            elif opera == 1:
                num1 = float(input("Valor Base: "))
                num2 = float(input("Valor Expoente: "))
            elif opera == 2:
                num1 = float(input("Valor Base: "))
                num2 = float(input("Valor Raiz: "))
            elif opera == 3:
                num1 = float(input("Valor: "))
                num2 = float(input("Valor Base: "))
            elif opera == 4:
                num1 = int(input("Ângulo (em radianos): "))
                resultado = calculadoraAvancada(num1, None, opera)
                print(f"Seno: {resultado[0]:.2f}")
                print(f"Cosseno: {resultado[1]:.2f}")
                print(f"Tangente: {resultado[2]:.2f}")
                
                continue
            
            resultado = calculadoraAvancada(num1,num2, opera)
        
        else: 
            print("Opção inválida. Por favor, escolha 0 para Simples ou 1 para Avançada.")
            
        print("Resultado: ", resultado)

    except ValueError:
        print("Erro, Digite um valor valido. Tente novamente")
        continue
    
    

    sair = int(input("Deseja realizar outra operacao? \n1 = Sim \n0 = Nao \n"))
    if sair == 0:
        print("Obrigado por usar nossa calculadora")