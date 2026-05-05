# Agora que você compreendeu os comandos básicos de Python, vamos para a estrutura do código

# Utilizamos o if, elif e else para verificar condições

idade = int(input("Informe sua idade (tem que ser maior que 16 anos para acessar esse aplicativo): "))

if idade < 16:
    print("Idade inválida, você não pode acessar esse aplicativo!!")  
# Aqui o if (se) é utilizado para fazer uma verificação. O (<) significa menor que e o (>) maior que.

elif idade >= 16 and idade < 100:
    print("Seja bem-vindo ao aplicativo")
# Nessa parte utilizamos o (and), que significa "e". Também existe o (or), que significa "ou". Eles servem para combinar condições.

else:
    print("Informação incorreta")


# Agora vamos para a parte de laços (loop)

for i in range(5):
    print(i)

# O for é um laço que serve para repetir um código várias vezes.
# O "in" significa "em". Ele liga a variável (i) com os valores que vão ser percorridos.
# O range() cria uma sequência de números.
# O laço começa no 0 porque o range() sempre inicia do zero, a menos que você diga outro número.


# Agora vamos compreender o while

contador = 0

while contador < 3:
    print(contador)
    contador += 1

# O while (enquanto) executa um bloco de código enquanto a condição for True (verdadeira).
# Quando a condição vira False (falsa), ele sai do loop.
# Nesse exemplo, ele repete enquanto o contador for menor que 3.
