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
        with open('receitas.csv','a',newline='', encoding='utf8') as filecsv:
            while True:
                try:

                    escritorcsv = csv.writer(filecsv)

                    nome = input('Nome de receita:')
                    pais = input('país de origem da receita: ')
                    ingredientes = input("Ingredientes: ")
                    modo_preparo = input("Modo de preparo: ")

                    escritorcsv.writerow([nome, pais, ingredientes, modo_preparo])
                    break
                except ValueError:
                    print('Erro ao adicionar receita')
                    
    
    def salvar_receita(receitas):
        with open('receitas.csv','w',newline='') as filecsv:
            escritorcsv = csv.DictWriter(filecsv,fieldnames=['nome','pais','ingredientes','modo_preparo'])
            escritorcsv.writeheader()
            escritorcsv.writerows(receitas)
    
    
    def excluir():
            
            receitas = Receita.banco_dados()
            
            if not receitas:
                print('Não há receitas cadastradas')
                return
            for i,receitas in enumerate(receitas,start=1):
                print(f'{i}. {receitas[0]}')
            
            try:
                excluir = int(input('Digite o número da receita que deseja excluir: '))
                if excluir > len(receitas):
                    print('Receita não encontrada')
                    return

                if 0 < excluir < len(receitas):
                    receitas_excluidas = receitas.pop(excluir)
                    print('Receita excluida')
                    Receita.banco_dados()
            
            except ValueError:
                print('Erro ao excluir receita')
                return

    def vizualizar():
        try:
            with open('receitas.csv', 'r', newline='', encoding='utf8') as filecsv:

                leitor = csv.reader(filecsv)

                for p,v in enumerate (leitor):
                    print(f'{p}. {v}')
                return
            
        except FileNotFoundError:
            print('O arquivo que você deseja vizualizar não foi encontrado!')

    def favoritar():
        try:
            with open('receitas.csv', 'r', newline='', encoding='utf8') as filecsv:

                leitor = csv.reader(filecsv)

                for p,v in enumerate (leitor):
                    print(f'{p}. {v}')
                return
                
        except FileNotFoundError:
            print('O arquivo que você deseja favoritar não foi encontrado!')

        while True:    
            try:
                    with open('receitas.csv', 'a', newline='', encoding='utf8'):
                        favoritar = int(input('Digite a receita que você deseja favoritar: '))

                        for i in leitor:
                            if i == favoritar:
                                #adc em um vetor ou arquivo csv/txt? provavelmente precisa ser um write/writerow
                                novo = input('Deseja adicionar outra receita as favoritas? [S]-Sim//[N]-Não:')
                                if novo == 'N':
                                    print('Receitas adicionadas!')
                                    break
                                 
            except FileNotFoundError:
                print('Receita não encontrada, digite novamente!')
            except IndexError:
                print('Receita não encontrada, digite novamente!')
    
    def main():
        dados = Receita.banco_dados()
        print(dados)
    
        while True:
            print('\n==MENU==')
            print('1. Adicionar receitas ')
            print('2. Visualizar receitas ')
            print('3. Excluir receitas ')
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
                Receita.excluir()
            if opcao == 4:
                Receita.vizualizar()
            if opcao == 5:
            
            if opcao == 6:
            
            if opcao == 7:
            
            if opcao == 8:
                
            if opcao == 9:
                print('Programa finalizado')
                break
        
        






