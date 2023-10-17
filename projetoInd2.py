# Dicionário para armazenar candidatos e suas notas em diferentes categorias
applicant = {
    "Mario": ["E8", "T3", "P5", "S7"],
    "Paula": ["E4", "T6", "P5", "S9"],
}

# Variável para controlar o loop principal do menu
runMenu = True

# Função para criar um novo candidato
def createApplicant():
    #Solicita e armazena o nome do candidato
    name = input("\nQual é o nome do candidato?  ")
    print("=" * 20, "\n")
    print("Somente notas de 1 a 10")

    #Solicita e armazena nota da entrevista, do teste teórico, prático e de soft skills
    interview = int(input("Digite a nota da entrevista:"))
    theoretical = int(input("Digite a nota do teste teórico:"))
    practice = int(input("Digite a nota do teste prático:"))
    soft = int(input("Digite a nota da avaliação de soft skills:"))

    # Armazena as notas no formato de strings com prefixo da categoria
    applicant[name] = [f'E{interview}', f'T{theoretical}', f'P{practice}', f'S{soft}']

# Função para buscar candidatos com base em critérios de notas
def findInDictionary(grades):
    for key, values in applicant.items():
        allConditionsTrue = True

        for grade in grades:
            category = grade[0]

            for value in values:
                if value.startswith(category):

                    # Compara os valores da nota miníma e da lista.
                    if int(value[1:]) < int(grade[1:]):
                        # Se não cumprir a nota, o candidato não será mostrado 
                        allConditionsTrue = False
                        break

            if not allConditionsTrue:
                break

        # Imprime os candidatos que cumprirem todos os filtros
        if allConditionsTrue:
            print(f'\n\033[33m{key} - {"_".join(values)}')

# Função para buscar candidatos com base em critérios específicos
def findApplicant():
    # Lista de opções para critérios de busca
    options = ["Entrevista", "teste teórico", "teste prático", "soft skills", "Todos"]

    for i in range(len(options)):
        print(f'\n-> {options[i]}') if i == 0 else print(f'-> {options[i]}')

    run = True
    grade = []

    while run:
          # Solicita o critério de busca
        search = input("\033[35m\nSelecione um critério: (E/T/P/S) ou 0 para sair ").upper()

        # Finaliza o loop caso seja digitado 0
        if search == '0':
            num = int(search)
            if num == 0:
                break

        # Solicita nota do critério
        searchGrade = int(input("Digite a nota: "))

        # Adiciona critério à lista de notas
        if search == "E":
            grade.append(f"{search}{searchGrade}")
        elif search == "T":
            grade.append(f"{search}{searchGrade}")
        elif search == "P":
            grade.append(f"{search}{searchGrade}")
        elif search == "S":
            grade.append(f"{search}{searchGrade}")
        else:
            print("Somente aceitamos, (E/T/P/S) ou 0 para sair \n")

    findInDictionary(grade)

# Função principal para exibir o menu e controlar as opções
def menu():
    while runMenu:
        print("\n", "\033[35m*" * 40)
        # Lista de opções do menu
        options = ["Inscrever Candidato", "Buscar Candidato", "Sair"]

        for i in range(len(options)):
            print(f'\033[37m[{i + 1}] {options[i]}')

        #Armazena a opção e direciona para a opção solicitada
        option = int(input("\nDigite a opção desejada: "))

        if option == 1:
            createApplicant()
        elif option == 2:
            findApplicant()
        elif option == 3:
            break
        else:
            print("Erro de digitação! Selecione uma das opções.")

# Chama a função menu para iniciar o programa
menu()
