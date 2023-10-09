#Receber as avaliações e fazer append pra um dicionario
applicant = {}
runMenu = True

def createApplicant():
    name = input("Qual é o nome do candidato?")
    print("=" * 20, "\n")
    print("Somente notas de 1 a 10")

    interview = int(input("Digite a nota da entrevista:"))
    theoretical = int(input("Digite a nota do teste teórico:"))
    practice = int(input("Digite a nota do teste prático:"))
    soft = int(input("Digite a nota da avaliação de soft skills:"))

    applicant[name] = [interview, theoretical, practice, soft]


def findApplicant():
    #listar opções
    options = ["Entrevista", "teste teórico", "teste prático", "soft skills", "Todos"]

    for i in range(len(options)):
        print(f'[{i}] {options[i]}')
    
    run = True
    
    while run:
        arr = []
        search = input("Selecione um critério: (E/T/P/S) ").upper()
        searchGrade = int(input("Digite a nota: "))

        if search == "E":
            arr.insert(0, searchGrade)
        elif search == "T":
            arr.insert(1, searchGrade)
        elif search == "P":
            arr.insert(2, searchGrade)
        elif search == "S":
            arr.insert(3, searchGrade)
        else:
            run = False

    # f"e{interview}_t{theoretical}_p{practice}_s{soft}"

def menu():
    #mostra as opções
    while runMenu:
        options = ["Inscrever Candidato", "Buscar Candidato", "Sair"]

        for i in range(len(options)):
            print(f'[{i+1}] {options[i]}')

        option = int(input("Digite a opção desejada:"))

        if option == 1:
            createApplicant()
            print(applicant)
        elif option == 2:
            findApplicant()
        elif option == 3:
            keep = False

menu()