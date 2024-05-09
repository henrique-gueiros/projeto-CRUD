import os
os.system('cls') 
import csv
 #manos, a gente vai usar esse csv depois e vai colocar pra limpar o terminal depois tambem pra poder organizar melhor os "os" que a gente importar aqui
 #esse def dos componentes a gente vai usar pra armazenar os dados de país nome da receita e etc

class receita:
    def __init__(self, nome, pais, ingredientes, preparo):
        self.nome = nome 
        self.pais = pais 
        self.ingredientes = ingredientes 
        self.preparo = preparo