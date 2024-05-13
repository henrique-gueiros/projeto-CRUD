import os
os.system('cls') 
import csv
 #manos, a gente vai usar esse csv depois e vai colocar pra limpar o terminal depois tambem pra poder organizar melhor os "os" que a gente importar aqui
 #esse def dos componentes a gente vai usar pra armazenar os dados de país nome da receita e etc

class Receita:
    def __init__(self, nome, pais, ingredientes, preparo, favorito): 
        pass
        self.nome = nome
        self.pais = pais
        self.ingredientes = ingredientes
        self.preapro = preparo
        self.favorito = favorito

    def banco_dados():
        with open('receitas.csv', 'r', newline='', encoding='utf8') as filecsv:
            dados=[]
            for i in filecsv:
                nome, pais, ingredientes, preparo, favorito = i
                ingredientes = ingredientes.split(', ') #separei os ingredientes por vírgula pra ficar mais fácil
                receita = Receita(nome, pais, ingredientes, preparo, favorito)
                dados.append(receita)
        return dados

    #def p/ adicionar receita no banco de dados == csv
    def add():
        with open('receitas.csv','w',newline='', encoding='utf8') as filecsv:

            escritorcsv = csv.writer(filecsv)

            nome = input('Nome de receita:')
            pais = input('país de origem da receita: ')
            ingredientes = input("Ingredientes: ")
            modo_preparo = input("Modo de preparo: ")

            escritorcsv.writerow([nome, pais, ingredientes, modo_preparo])
        
        






