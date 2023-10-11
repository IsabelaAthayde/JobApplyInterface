#Receber as avaliações e fazer append pra um dicionario
applicant = {
    "Mario": ["E8", "T3", "P5","S7"],
    "Paula": ["E4", "T6", "P5","S9"],
    "Yasmin": ["E9", "T7", "P10","S9"],
    "Paula": ["E2", "T5", "P4","S4"],
}
runMenu = True

def createApplicant():
    name = input("\nQual é o nome do candidato?  ")
    print("=" * 20, "\n")
    print("Somente notas de 1 a 10")

    interview = int(input("Digite a nota da entrevista:"))
    theoretical = int(input("Digite a nota do teste teórico:"))
    practice = int(input("Digite a nota do teste prático:"))
    soft = int(input("Digite a nota da avaliação de soft skills:"))

    applicant[name] = [f'E{interview}', f'T{theoretical}', f'P{practice}', f'S{soft}']

def findInDictionary(grades):
    for key, values in applicant.items():
        allConditionsTrue = True
        
        for grade in grades:
            category = grade[0]

        
            for value in values:
                if value.startswith(category):

                    if int(value[1:]) < int(grade[1:]):
                        allConditionsTrue = False
                        break
            
            if not allConditionsTrue:
                break
        
        if allConditionsTrue:
            print(f'\n\033[33m{key} - {"_".join(values)}')

def findApplicant():
    #listar opções
    options = ["Entrevista", "teste teórico", "teste prático", "soft skills", "Todos"]

    for i in range(len(options)):
        print(f'\n-> {options[i]}') if i == 0 else print(f'-> {options[i]}')
    
    run = True
    grade = []
    while run:
        
        search = input("\033[35m\nSelecione um critério: (E/T/P/S) ou 0 para sair ").upper()

        if search == '0':
            num = int(search)
            if num == 0:
                break
                

        searchGrade = int(input("Digite a nota: "))

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


def menu():
    #mostra as opções
    while runMenu:
        print("\n", "\033[35m*" * 40)
        options = ["Inscrever Candidato", "Buscar Candidato", "Sair"]

        for i in range(len(options)):
            print(f'\033[37m[{i+1}] {options[i]}')

        option = int(input("\nDigite a opção desejada: "))

        if option == 1:
            createApplicant()
        elif option == 2:
            findApplicant()
        elif option == 3:
            break
        else:
            print("Erro de digitação! Selecione uma das opções.")

menu()
