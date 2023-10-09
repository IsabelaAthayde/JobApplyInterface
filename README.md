# JobApplyInterface

#Receber as avaliações e fazer append pra um dicionario
applicant = {
    "Fantasma": ["E8", "T3", "P5","S7"]
}
runMenu = True

def createApplicant():
    name = input("Qual é o nome do candidato?")
    print("=" * 20, "\n")
    print("Somente notas de 1 a 10")

    interview = int(input("Digite a nota da entrevista:"))
    theoretical = int(input("Digite a nota do teste teórico:"))
    practice = int(input("Digite a nota do teste prático:"))
    soft = int(input("Digite a nota da avaliação de soft skills:"))

    applicant[name] = [f'E{interview}', f'T{theoretical}', f'P{practice}', f'S{soft}']

def findInDictionary(searchGrade):

    for grade in searchGrade:
        for value in applicant:
            print(applicant)

def findApplicant():
    #listar opções
    options = ["Entrevista", "teste teórico", "teste prático", "soft skills", "Todos"]

    for i in range(len(options)):
        print(f'-> {options[i]}')
    
    run = True
    
    while run:
        grade = []
        search = input("Selecione um critério: (E/T/P/S) ou 0 para sair ").upper()

        if int(search) == 0:
            break

        searchGrade = int(input("Digite a nota: "))

        if search == "E":
            grade.append(f"{search}{searchGrade}")
            findInDictionary(grade)
        elif search == "T":
            grade.append(f"{search}{searchGrade}")
            findInDictionary(grade)
        elif search == "P":
            grade.append(f"{search}{searchGrade}")
            findInDictionary(grade)
        elif search == "S":
            grade.append(f"{search}{searchGrade}")
            findInDictionary(grade)
        else:
            print("Somente aceitamos, (E/T/P/S) ou 0 para sair \n")


        

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
