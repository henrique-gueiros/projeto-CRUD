import os
import random

os.system('cls')

def banco_dados():
    try:
        with open('receitas.txt', 'r', encoding='utf8') as filetxt:
            dados = []
            for linha in filetxt:
                partes = linha.strip().split('|')
                if len(partes) == 4:
                    nome, pais, ingredientes, preparo = partes
                    ingredientes = ingredientes.split(', ')
                    receita = {'nome': nome, 'pais': pais, 'ingredientes': ingredientes, 'preparo': preparo}
                    dados.append(receita)
            return dados
    except FileNotFoundError:
        return []

def inicializa_arquivo():
    with open('receitas.txt', 'w', encoding='utf8') as filetxt:
        filetxt.write("Paella|Espanha|Camarão, Arroz, Ervilhas|Fogo alto\n")
        filetxt.write("Hambúrguer|Estados Unidos|Pão, Carne, Queijo|Na brasa\n")
            
def add():
    with open('receitas.txt', 'a', encoding='utf8') as filetxt:
        try:
            nome = input('Nome da receita: ')
            pais = input('País de origem da receita: ')
            ingredientes = input("Ingredientes (digitar cada um separado por vírgula): ").split(', ')
            modo_preparo = input("Modo de preparo: ")
            filetxt.write(f"{nome}|{pais}|{', '.join(ingredientes)}|{modo_preparo}\n")
        except ValueError:
            print('Erro ao adicionar receita (valor digitado em algum campo é inválido).')

def visualizar():
    try:
        with open('receitas.txt', 'r', encoding='utf8') as filetxt:
            receitas = filetxt.readlines()
            if not receitas:
                print("Não há receitas para vizualizar")
            for p, v in enumerate(receitas):
                t = p + 1
                print(f'Receita {t}: {v}', end='')
           
            
    except FileNotFoundError:
        print('O arquivo que você deseja visualizar não foi encontrado!')

def excluir():
    try:
        with open('receitas.txt', 'r', encoding='utf8') as filetxt:
            receitas = filetxt.readlines()
        if not receitas:
            print("Sem receitas disponíveis para excluir")
            return
        print('Receitas disponíveis para excluir:')
        for p, v in enumerate(receitas):
            t = p + 1
            print(f'Receita {t}: {v}', end='')

        try:
            receita_excluida = int(input('Digite o número da receita que deseja excluir: '))
            if 1 <= receita_excluida <= len(receitas):
                del receitas[receita_excluida - 1]
            else:
                print('Número inválido')
        except ValueError:
            print('Número inválido')

        with open('receitas.txt', 'w', encoding='utf8') as filetxt:
            filetxt.writelines(receitas)
        print("Receita removida\n")

    except FileNotFoundError:
        print('Não há receitas disponíveis para excluir.')

def favoritar():
   
    try:
        with open('receitas.txt', 'r', encoding='utf8') as filetxt:
            receitas = filetxt.readlines()
        if not receitas:
            print("Sem receitas disponíveis para favoritar")
            return

        nome_receita = input("Digite o nome da receita que deseja adicionar como favorita: ")

        with open('receitas.txt', 'w', encoding='utf8') as filetxt:
            for linha in receitas:
                if nome_receita in linha and '*' not in linha:
                    linha = linha.strip() + " *\n"
                filetxt.write(linha)
        print("Receita adicionada aos favoritos!\n")
    except FileNotFoundError:
        print("Ainda não há receitas cadastradas.\n")

def editar():
    receitas = banco_dados()
    if not receitas:
        print('Não há receitas cadastradas')
        return
    for i, receita in enumerate(receitas, start=1):
        print(f'{i}. {receita["nome"]}')
    try:
        editando = int(input('Digite o número da receita que deseja editar: '))
        if editando > len(receitas):
            print('Receita não encontrada')
            return
        if 0 < editando <= len(receitas):
            receita_editada = receitas[editando - 1]
            nome = input('Novo nome da receita: ')
            pais = input('Novo país de origem da receita: ')
            ingredientes = input("Novos ingredientes: ").split(', ')
            modo_preparo = input("Novo modo de preparo: ")
            receita_editada['nome'] = nome
            receita_editada['pais'] = pais
            receita_editada['ingredientes'] = ingredientes
            receita_editada['preparo'] = modo_preparo

            with open('receitas.txt', 'w', encoding='utf8') as filetxt:
                for receita in receitas:
                    filetxt.write(f"{receita['nome']}|{receita['pais']}|{', '.join(receita['ingredientes'])}|{receita['preparo']}\n")

            print('Receita editada com sucesso!')
    except ValueError:
        print('Erro ao editar receita desejada')
        return

def filtrar_por_pais():
    try:
        pais = input("Digite o país que deseja filtrar: ")
        receitas_filtradas = [receita for receita in banco_dados() if receita['pais'] == pais]
        if not receitas_filtradas:
            print("Não há receitas cadastradas para esse país.")
        else:
            for i, receita in enumerate(receitas_filtradas, start=1):
                print(f"{i}. {receita['nome']} (de {receita['pais']})")
    except ValueError:
        print("Erro ao filtrar receitas por país, digite um país válido.")

def sugestao_aleatoria():
    receitas = banco_dados()
    if not receitas:
        return "Não há receitas cadastradas"
    random_receita = random.choice(receitas)
    return f"Receita sugerida: {random_receita['nome']} (de {random_receita['pais']})"

def filtrar_por_ingredientes():
    receitas = banco_dados()
    if not receitas:
        print("Não há receitas cadastradas")
        return
    ingredientes = input("Digite os ingredientes que deseja filtrar (separados por vírgula): ").split(', ')
    receitas_filtradas = [receita for receita in banco_dados() if all(ingrediente in receita['ingredientes'] for ingrediente in ingredientes)]
    if not receitas_filtradas:
        print("Não há receitas cadastradas com esses ingredientes.")
    else:
        for i, receita in enumerate(receitas_filtradas, start=1):
            print(f"{i}. {receita['nome']} (de {receita['pais']})")



def main():
    try:
        inicializa_arquivo()

        while True:
            print('\n== MENU ==')
            print('1. Adicionar receitas')
            print('2. Visualizar receitas')
            print('3. Excluir receitas')
            print('4. Favoritar receitas')
            print('5. Editar receita')
            print('6. Filtrar por países')
            print('7. Sugerir receita aleatória')
            print('8. Filtrar por ingredientes')
            print('9. Sair\n')

            opcao = int(input('Digite a operação desejada: '))
            print()

            if opcao == 1:
                add()
            elif opcao == 2:
                visualizar()
            elif opcao == 3:
                excluir()
            elif opcao == 4:
                favoritar()
            elif opcao == 5:
                editar()
            elif opcao == 6:
                filtrar_por_pais()
            elif opcao == 7:
                print(sugestao_aleatoria())
            elif opcao == 8:
                filtrar_por_ingredientes()
            elif opcao == 9:
                print('Programa finalizado')
                break
    
    except ValueError:
        print('Opção inválida. Tente novamente(escolha uma opção de 1 a 9).')

if __name__ == '__main__':
    main()

def excluir_tudo():
    try:
        with open('receitas.txt', 'w', encoding='utf8') as file:
            file.truncate()
    except FileNotFoundError:
        print('Arquivo não encontrado')

excluir_tudo()