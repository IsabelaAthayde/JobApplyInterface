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

def findInDictionary(grades):
    for key, values in applicant.items():
        todas_condicoes_atendidas = True
        
        for grade in grades:
            quesito = grade[0]
            nota_minima = int(grade[1:])

            if any(value.startswith(quesito) for value in values):
                for value in values:
                    if value.startswith(quesito):
                        numeric_value = int(value[1:])
                        if numeric_value < nota_minima:
                            todas_condicoes_atendidas = False
                            break
            else:
                todas_condicoes_atendidas = False
            
            if not todas_condicoes_atendidas:
                break
        
        if todas_condicoes_atendidas:
            print(f'{key} - {"_".join(values)}')

def findApplicant():
    #listar opções
    options = ["Entrevista", "teste teórico", "teste prático", "soft skills", "Todos"]

    for i in range(len(options)):
        print(f'-> {options[i]}')
    
    run = True
    grade = []
    while run:
        
        search = input("Selecione um critério: (E/T/P/S) ou 0 para sair ").upper()

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
