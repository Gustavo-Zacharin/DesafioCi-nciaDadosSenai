def validar_notas(notas):
    return isinstance(notas, list) and len(notas) > 0

def calcular_media(notas):
    soma = 0
    for nota in notas:
        soma += nota
    return soma / len(notas)

def filtrar_recuperacao(alunos):
    return [dados for dados in alunos if dados[1] < 7.0]

def encontrar_top_student(alunos):
    return max(alunos, key=lambda x: x[1])

def gerar_relatorio(alunos, recuperacao, top):
    with open("resultado.txt", "w") as arquivo:
        arquivo.write("RELATÓRIO ACADÊMICO\n\n")

        arquivo.write("Todos os alunos:\n")
        for nome, media in alunos:
            arquivo.write(f"{nome}: {media:.2f}\n")

        arquivo.write("\nAlunos em recuperação:\n")
        for nome, media in recuperacao:
            arquivo.write(f"{nome}: {media:.2f}\n")

        arquivo.write("\nTop Student:\n")
        arquivo.write(f"{top[0]}: {top[1]:.2f}\n")