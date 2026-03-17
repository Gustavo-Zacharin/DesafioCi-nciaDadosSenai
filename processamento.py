def validar_notas(notas):
    return isinstance(notas, list) and len(notas) > 0

def calcular_media(notas):
    soma = 0
    for nota in notas:
        soma += nota
    return soma / len(notas)

def filtrar_recuperacao(alunos):
    return [aluno for aluno in alunos if aluno[1] < 7.0]