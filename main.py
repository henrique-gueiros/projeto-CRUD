import os
os.system('cls') 
import random
 #manos, a gente vai usar esse csv depois e vai colocar pra limpar o terminal depois tambem pra poder organizar melhor os "os" que a gente importar aqui
 #esse def dos componentes a gente vai usar pra armazenar os dados de país nome da receita e etc

def banco_dados():
    try:
        with open('receitas.txt', 'r', newline='', encoding='utf8') as filetxt:
            
            dados=[]
            for i in filetxt:
                nome, pais, ingredientes, preparo, favorito = i
                ingredientes = ingredientes.split(', ') #separei os ingredientes por vírgula pra ficar mais fácil
                favorito = favorito == "True"
                receita = (nome, pais, ingredientes, preparo, favorito)
                dados.append(receita)
            return dados
    except FileNotFoundError:
        return dados

    #def p/ adicionar receita no banco de dados == csv
def add():
    with open('receitas.txt','a',newline='', encoding='utf8') as filetxt:
        while True:
            try:

                nome = input('Nome de receita:')
                filetxt.write(nome)
                filetxt.write('\n')
                pais = input('país de origem da receita: ')
                filetxt.write(pais)
                filetxt.write('\n')
                ingredientes = input("Ingredientes: ")
                filetxt.write(ingredientes)
                filetxt.write('\n')
                modo_preparo = input("Modo de preparo: ")
                filetxt.write(modo_preparo)
                filetxt.write('\n')
                
                favorito = input("Você quer adicionar essa receita aos Favoritos? (s/n): ") 
                if favorito == 's':
                    file=open('favoritos.txt','a',encoding='utf8')
                    file.write(nome)
                    file.write(pais)
                    file.write(ingredientes)
                    file.write(modo_preparo)
                    file.write('\n')
                    file.close()
                else:
                    


                    break
            except ValueError:
                print('Erro ao adicionar receita')
                    
    
def salvar_receita(receitas):
    with open('receitas.txt','w',newline='') as filetxt:
        return
    
    
def excluir():
            
    receitas = banco_dados()

    if not receitas:
        print('Não há receitas cadastradas')
        return

    for receita in receitas:
        print(receita[receita])

    try:
        nome_receita = input('Digite o nome da receita que deseja excluir: ')
        for receita in receitas:
            if receita == nome_receita:
                receitas.remove(receita)
                print('Receita excluída')
                banco_dados()
                return
        print('Receita não encontrada')
    except Exception as e:
        print('Erro ao excluir receita:', str(e))
        return

def vizualizar():
    try:
        with open('receitas.txt', 'r', newline='', encoding='utf8') as filetxt:

            for p,v in enumerate (filetxt):
                print(f'{p}. {v}', end='')
            return
            
    except FileNotFoundError:
        print('O arquivo que você deseja vizualizar não foi encontrado!')

def favoritar():
    try:
        with open('receitas.txt', 'r', newline='', encoding='utf8') as filetxt:

            for p,v in enumerate (filetxt):
                print(f'{p}. {v}', end='')
                
    except FileNotFoundError:
        print('O arquivo que você deseja favoritar não foi encontrado!')

    while True:    
        try:
            with open('favoritos.txt', 'a', newline='', encoding='utf8'):
                favoritar = (input('Digite a receita que você deseja favoritar: '))

                
                file=open('favoritos.txt','a',encoding='utf8')
                file.write(favoritar)
                file.close()
                        #adc em um vetor ou arquivo csv/txt? provavelmente precisa ser um write/writerow
            return            
                                               
        except FileNotFoundError:
            print(' não encontrada, digite novamente!')
            return
        except IndexError:
            print(' não encontrada, digite novamente!')
            return

def editar():
    receitas = banco_dados()
    if not receitas:
        print('Não há receitas cadastradas')
        return
    for i,receita in enumerate(receitas,start=1):
        print(f'{i}. {receita.nome}')
    try:
        editar = int(input('Digite o número da receita que deseja editar: '))
        if editar > len(receitas):
            print(' não encontrada')
            return
        if 0 < editar < len(receitas):
            receitas_editadas = receitas.pop(editar-1)
            nome = input('Novo nome da receita: ')
            pais = input('Novo país de origem da receita: ')
            ingredientes = input("Novos ingredientes: ")
            modo_preparo = input("Novo modo de preparo: ")
            receitas_editadas.nome = nome
            receitas_editadas.pais = pais
            receitas_editadas.ingredientes = ingredientes
            receitas_editadas.preparo = modo_preparo
            receitas.append(receitas_editadas)
            salvar_receita(receitas)
            print(' editada com sucesso!')
    except ValueError:
        print('Erro ao editar receita')
        return   
def filtrar_por_pais():
    pais = input("Digite o país que deseja filtrar: ")
    receitas_filtradas = []
    for receita in banco_dados():
        if receita[1] == pais:
            receitas_filtradas.append(receita)
    if not receitas_filtradas:
        print("Não há receitas cadastradas para esse país.")
    else:
        for i, receita in enumerate(receitas_filtradas, start=1):
            print(f"{i}. {receita[0]} (de {receita[1]})")
    
def sugestao_aleatoria():
    receitas = banco_dados()
    if not receitas:
        return "Não há receitas cadastradas"
    random_receita = random.choice(receitas)
    return f" sugerida: {random_receita.nome} (de {random_receita.pais})"


    
                 

def main():
    global dados 
    dados = banco_dados() 
     
    
    while True:
        print('\n==MENU==')
        print('1. Adicionar receitas ')
        print('2. Visualizar receitas ')
        print('3. Excluir receitas ')
        print('4. Favoritar receitas ')
        print('5. Editar receita')
        print('6. Filtrar por paises')
        print('7 Sugerir receita aleatoria ')
        print('8. ')
        print('9. Sair\n')
            
        opcao=int(input('Digite a operação desejada: '))
        print()
            
        if opcao == 1:
            add()
        if opcao == 2:
            vizualizar()
        if opcao == 3:
            excluir()
        if opcao == 4:
            favoritar() 
        if opcao == 5:
            editar()
        if opcao == 6:
            filtrar_por_pais()
        if opcao == 7:
            sugestao_aleatoria()
        if opcao == 8:
            add()
        if opcao == 9:
            print('Programa finalizado')
            break
        
if __name__ == '__main__':
    main()

def excluir_tudo():
    try:
        with open('receitas.txt', 'w', encoding='utf8') as file:
            file.truncate()
    except FileNotFoundError:
        print('Arquivo não encontrado')

excluir_tudo()