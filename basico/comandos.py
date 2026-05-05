# Usamos comandos de entrada e saída de informação

print("Hello World!")  # O comando print mostra informações na tela


# Como utilizar o print e o input no código?

nome = input("Informe o seu nome: ")  
# Aqui usamos o input para receber uma informação do usuário
# e armazenar na variável 'nome'

print(nome)  
# Aqui mostramos na tela a informação guardada na variável 'nome'


# O que podemos fazer com essas poucas linhas de código?
# Exemplo: uma conta de soma

print("Seja bem-vindo ao calculador de soma")

# O input sempre retorna uma string (texto)
# Para fazer contas, usamos int() para converter para número inteiro

numero1 = int(input("Informe o primeiro número: "))
numero2 = int(input("Informe o segundo número: "))

resultado = numero1 + numero2

print("O resultado da soma foi:", resultado)

print(f"Sua conta deu {resultado}, o primeiro número é {numero1} e o segundo é {numero2}")
# Usando f-string (print(f"")) o código fica mais moderno e organizado
