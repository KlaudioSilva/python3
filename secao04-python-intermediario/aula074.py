'''
Closure e funções que retornam outras funções
'''

def criar_saudacao(saudacao):
    def saudar(nome):
        return f'{saudacao}, {nome}'
    return saudar

dar_bom_dia = criar_saudacao('Bom dia')
dar_boa_noite = criar_saudacao('Boa noite')

for nome in ['Klaudio', 'Elma', 'João Pedro', 'Arthur']:
    print(dar_bom_dia(nome))
    print(dar_boa_noite(nome))