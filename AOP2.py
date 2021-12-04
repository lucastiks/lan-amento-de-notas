notaInvalidaAop = ('Atenção! Apenas números entre 0 e 1 são permitidos, por favor, tente novamente.')
notaInvalidaAop2 = ('Atenção! Apenas números entre 0 e 2 são permitidos, por favor, tente novamente.')
notaInvalidaProvaRegular = ('Atenção! Apenas números entre 0 e 6 são permitidos, por favor, tente novamente.')
quantidadeAlunos = int(input('Quantos alunos a turma possui? '))
i = 0
for i in range (quantidadeAlunos):
    while True:
        notaAop1 = float(input(f'Insira a nota obtida pelo aluno {i + 1} na AOP1 (0-1): ').replace(',' , '.'))
        if notaAop1 <0 or notaAop1 > 1:
            print(notaInvalidaAop)
        else:
            break

    while True:
        notaAop2 = float(input(f'Insira a nota obtida pelo aluno {i + 1} na AOP2 (0-2): ').replace(',' , '.'))
        if notaAop2 < 0 or notaAop2 > 2:
            print(notaInvalidaAop2)
        else:
            break

    while True:
        notaAop3 = float(input(f'Insira a nota obtida pelo aluno {i + 1} na AOP3 (0-1): ').replace(',' , '.'))
        if notaAop3 < 0 or notaAop3 > 1:
            print(notaInvalidaAop)
        else:
            break
    while True:
        notaProvaRegular = float(input(f'Insira a nota obtida pelo aluno {i + 1} na Prova Regular (0-6): ' \
                                      ).replace(',' , '.'))
        if notaProvaRegular < 0 or notaProvaRegular > 6:
            print(notaInvalidaProvaRegular)
        else:
            break

    mediaModulo = notaAop1 + notaAop2 + notaAop3 + notaProvaRegular

    if  mediaModulo >= 7.0:
        print(f'O aluno {i + 1} obteve a nota {mediaModulo:.2f} e está Aprovado!')
        print('-' * 45)
    else:
        notaProvaRecuperação = float(input('Insira sua nota da Prova de Recuperação (0-10): ').replace(',' , '.'))
        mediaGeral = (mediaModulo + notaProvaRecuperação) / 2
        if mediaGeral >= 5.0:
            print(f'O aluno {i + 1} obteve a nota {mediaGeral:.2f} e está Aprovado!')
            print('-' * 45)
        else:
            print(f'O aluno {i + 1} obteve a nota {mediaGeral:.2f} e está Reprovado!')
            print('-' * 45)