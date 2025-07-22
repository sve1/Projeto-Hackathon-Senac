
aluno1 = input("Cadastre o Primeiro Aluno: ")
nota1_aluno1 = float(input(f"Digite a nota 1 de {aluno1}: "))
nota2_aluno1 = float(input(f"Digite a nota 2 de {aluno1}: "))

aluno2 = input("Cadastre o Segundo Aluno: ")
nota1_aluno2 = float(input(f"Digite a nota 1 de {aluno2}: "))
nota2_aluno2 = float(input(f"Digite a nota 2 de {aluno2}: "))

aluno3 = input("Cadastre o Terceiro Aluno: ")
nota1_aluno3 = float(input(f"Digite a nota 1 de {aluno3}: "))
nota2_aluno3 = float(input(f"Digite a nota 2 de {aluno3}: "))

alunos = {
    aluno1: [nota1_aluno1, nota2_aluno1],
    aluno2: [nota1_aluno2, nota2_aluno2],
    aluno3: [nota1_aluno3, nota2_aluno3]
}


print("\nAlunos cadastrados:")
for nome in alunos:
    print(f"- {nome}")



pesquisa = input("\nDigite o nome do aluno que deseja consultar: ")



if pesquisa in alunos:
    notas = alunos[pesquisa]
    media = sum(notas) / len(notas)
    situacao = "Aprovado" if media >= 7 else "Reprovado"
    
    print(f"\nNome: {pesquisa}")
    print(f"Notas: {notas}")
    print(f"Média: {media:.2f}")
    print(f"Situação: {situacao}")

else:
    print("Aluno não encontrado.")
    nova_pesquisa = input("Deseja tentar novamente? (s/n): ")
    if nova_pesquisa.lower() == "s":
        pesquisa = input("Digite o nome do aluno novamente: ")
        if pesquisa in alunos:
            notas = alunos[pesquisa]
            media = sum(notas) / len(notas)
            situacao = "Aprovado" if media >= 7 else "Reprovado"

            print(f"\nNome: {pesquisa}")
            print(f"Notas: {notas}")
            print(f"Média: {media:.2f}")
            print(f"Situação: {situacao}")
        else:
            print("Encerrando. Obrigado por usar a aplicação, criado por Diego Maciel")
    else:
        print("Encerrando. Obrigado por usar a aplicação, criado por Diego Maciel")


    
