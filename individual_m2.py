print('Já possuimos uma lista de candidatos e suas respectivas notas.\n\
Solicitaremos as notas mínimas em cada avaliação e em seguida, se houver, entregaremos \
\num ou mais candidatos que condizem com suas expectativas\n')

# Lista de resultados dos candidatos
resultados = [
    {'nome': 'Aricécia', 'resultado': 'e5_t4_p4_s7'},
    {'nome': 'Deusarina', 'resultado': 'e3_t5_p6_s8'},
    {'nome': 'Asdrubal', 'resultado': 'e7_t6_p3_s5'},
    {'nome': 'Gumercindo', 'resultado': 'e6_t7_p7_s9'},
    {'nome': 'Mariquita', 'resultado': 'e4_t4_p8_s8'},
    {'nome': 'Vencesleu', 'resultado': 'e7_t5_p7_s8'},
    {'nome': 'Napoleão', 'resultado': 'e7_t6_p3_s5'},
    {'nome': 'Jucicleide', 'resultado': 'e9_t8_p7_s9'},
    {'nome': 'Pácido', 'resultado': 'e4_t3_p5_s8'},
]

# Busca dos candidatos
def buscar_candidatos(resultados, criterios):
    candidatos_selecionados = []
    for candidato in resultados:
        nota_e = float(candidato['resultado'][1])
        nota_t = float(candidato['resultado'][4])
        nota_p = float(candidato['resultado'][7])
        nota_s = float(candidato['resultado'][10])
        
        if nota_e >= criterios['e'] and nota_t >= criterios['t'] and nota_p >= criterios['p'] and nota_s >= criterios['s']:
            candidatos_selecionados.append(candidato)
        
    return candidatos_selecionados
        
# Critérios de avaliação
criterios = {}
criterios['e'] = float(input("Digite a nota mínima desejada para a etapa de entrevista: "))
criterios['t'] = float(input("Digite a nota mínima desejada para o teste teórico: "))
criterios['p'] = float(input("Digite a nota mínima desejada para o teste prático: "))
criterios['s'] = float(input("Digite a nota mínima desejada para a avaliação de soft skills: "))

candidatos_selecionados = buscar_candidatos(resultados, criterios)

if len(candidatos_selecionados)> 0:
    print("\nCandidatos selecionados:\n")
    for candidato in candidatos_selecionados:
        nome = candidato['nome']
        nota_e = int(candidato['resultado'][1])
        nota_t = int(candidato['resultado'][4])
        nota_p = int(candidato['resultado'][7])
        nota_s = int(candidato['resultado'][10])
        print(f"Nome: {nome}, Notas: e={nota_e}, t={nota_t}, p={nota_p}, s={nota_s}")
else:
    print('\nCandidato não encontrado\n')



