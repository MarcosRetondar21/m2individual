# Lista de resultados dos candidatos
resultados = [
    {'nome': 'joão Pedro', 'resultado': 'e5_t4_p4_s7'},
    {'nome': 'Maria Fernanda', 'resultado': 'e3_t5_p6_s8'},
    {'nome': 'Asdrubal', 'resultado': 'e7_t6_p3_s5'},
    {'nome': 'Gumercindo', 'resultado': 'e6_t7_p7_s9'},
    {'nome': 'Mariquita', 'resultado': 'e4_t4_p8_s8'},
]

# Busca dos candidatos
def buscar_candidatos(resultados, criterios):
    candidatos_selecionados = []
    for candidato in resultados:
        nota_e = int(candidato['resultado'][1])
        nota_t = int(candidato['resultado'][4])
        nota_p = int(candidato['resultado'][7])
        nota_s = int(candidato['resultado'][10])
        
        if nota_e >= criterios['e'] and nota_t >= criterios['t'] and nota_p >= criterios['p'] and nota_s >= criterios['s']:
            candidatos_selecionados.append(candidato)
        
    return candidatos_selecionados
        
# Critérios de avaliação
criterios = {}
criterios['e'] = int(input("Digite a nota mínima desejada para a etapa de entrevista: "))
criterios['t'] = int(input("Digite a nota mínima desejada para o teste teórico: "))
criterios['p'] = int(input("Digite a nota mínima desejada para o teste prático: "))
criterios['s'] = int(input("Digite a nota mínima desejada para a avaliação de soft skills: "))

candidatos_selecionados = buscar_candidatos(resultados, criterios)

if len(candidatos_selecionados)> 0:
    print("Candidatos selecionados:")
    for candidato in candidatos_selecionados:
        nome = candidato['nome']
        nota_e = int(candidato['resultado'][1])
        nota_t = int(candidato['resultado'][4])
        nota_p = int(candidato['resultado'][7])
        nota_s = int(candidato['resultado'][10])
        print(f"Nome: {nome}, Notas: e={nota_e}, t={nota_t}, p={nota_p}, s={nota_s}")
else:
    print('Candidato não encontrado')





