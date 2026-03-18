from processamento import(
    validar_notas,
    calcular_media,
    filtrar_recuperacao,
    encontrar_top_student,
    gerar_relatorio
)

def alunos():
    dados = [
        ("Joseph", [9, 9.5, 10, 5.8, 4.6, 3.91]),
        ("Ana", [4.5, 6, 10, 2.9, 5.3, 8]),
        ("Charlie", [10, 9, 10, 1, 2.4, 1.1]),
        ("Tony", [7, 6.5, 7.7, 5.8, 4, 10]),
        ("Cristiano", [10, 9.5, 3, 5, 7.78]),
    ]

    alunos_validos = []

    for nome, notas in dados:
        if validar_notas(notas):
            media = calcular_media(notas)
            alunos_validos.append((nome, media))  # corrigido
            print(f"{nome}: média de {media:.2f}")
        else:
            print(f"Dados inválidos para {nome}")

    recuperacao = filtrar_recuperacao(alunos_validos)

    print("\nAlunos em recuperação:")
    for nome, media in recuperacao:
        print(f"{nome} - média: {media:.2f}")

    top = encontrar_top_student(alunos_validos)
    print(f"\nAluno Destaque: {top}")

    gerar_relatorio(alunos_validos, recuperacao, top)

alunos()