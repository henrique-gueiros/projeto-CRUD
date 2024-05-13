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
        try:
            with open('receitas.csv', 'r', newline='', encoding='utf8') as filecsv:
                leitor_csv = csv.reader(filecsv)
                next(leitor_csv)
                dados=[]
                for i in filecsv:
                    nome, pais, ingredientes, preparo, favorito = i
                    ingredientes = ingredientes.split(', ') #separei os ingredientes por vírgula pra ficar mais fácil
                    favorito = favorito == "True"
                    receita = Receita(nome, pais, ingredientes, preparo, favorito)
                    dados.append(receita)
            return dados
        except FileNotFoundError:
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
    
    def main():
        dados = Receita.banco_dados()
        print(dados)
    
        while True:
            print('\n==MENU==')
            print('1. Adicionar receitas ')
            print('2. Visualizar receitas ')
            print('3. ')
            print('4. ')
            print('5. ')
            print('6. ')
            print('8. ')
            print('9. Sair')
            
            opcao=int(input('Digite a operaçao desejada: '))
            
            if opcao == 1:
                Receita.add()
            if opcao == 2:
                Receita.banco_dados() 
            if opcao == 3:
            
            if opcao == 4:
            
            if opcao == 5:
            
            if opcao == 6:
            
            if opcao == 7:
            
            if opcao == 8:
                
            if opcao == 9:
                print('Programa finalizado')
                break
        
        






