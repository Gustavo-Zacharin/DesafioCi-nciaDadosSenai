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