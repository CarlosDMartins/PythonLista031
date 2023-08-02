'''8) Fazer um programa que calcule e apresente a quantidade de litros que um automóvel gastará em uma viagem. O
programa deve coletar as seguintes informações: Distância a percorrer na viagem, em quilômetros; qual é o
valor do consumo médio do automóvel, em quilômetros por litro.'''

dist = float(input("Qual é a distância percorrida em km?"))

cons = float(input("Quanto o automóvel consome por km?"))

litros = dist / cons

print("O automóvel gastará:", litros)

