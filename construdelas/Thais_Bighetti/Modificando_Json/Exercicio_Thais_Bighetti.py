import json

"""
1 - Leiam o arquivo json transformando o em um dicionário
2 - classificação dependente do gênero:
mulheres: 1,50 - 1,55 - Estatura baixa
1,56 - 1,70 - Estatura mediana
1,71 - 1,89 - Alta estatura
-----------------------------------------------------------------------------------
Homens: 1,50 - 1,60 - Baixa estatura
1,61 - 1,75 - estatura mediana
1,76 - 1,89 - Alta estatura
-----------------------------------------------------------------------------------
3 - Se a pessoa obeteve a maior potuação entre as pessoas da lista
4 - a lista pontuacao
5 - a média da pontuacao
6 - Nome da pessoa
-----------------------------------------------------------------------------------
gerar um novo json:
{ 'Nome Completo': 'Chica da Silva',
'Estatura': 'Baixa' | 'Média' | 'Alta',
'Maior Pontuacao': True | False,
'Pontuacao': [13, 7, 29, 4, 1, 11, 2, 22],
'Media da Pontuacao': 11,125
}
"""

arquivo = open("../../../../Jason/exercicios.json", "r")
dicio = json.load(arquivo)

for pessoas in dicio['Pessoas'] :
    pontuacao = pessoas['Pontuacao']
    if max(pessoas['Pontuacao']) > 29 :
        pessoas['Pontuacao'] = True
    else :
        pessoas['Pontuacao'] = False
    nova_pontuacao = {'Maior Pontuação' : pessoas['Pontuacao'],
                      'Pontuação' : pontuacao,
                      'Média da Pontuação' : sum(pontuacao) / len(pontuacao)}

    altura = pessoas['Altura']
    if pessoas['Gênero'] == "F" :
        if (altura >= 1.5) and (altura <= 1.55) :
            pessoas['Altura'] = 'Baixa'
        elif altura <= 1.7 :
            pessoas['Altura'] = 'Média'
        else :
            pessoas['Altura'] = 'Alta'
    else :
        if (altura >= 1.5) and (altura <= 1.60) :
            pessoas['Altura'] = 'Baixa'
        elif altura <= 1.75 :
            pessoas['Altura'] = 'Média'
        else :
            pessoas['Altura'] = 'Alta'


    pessoas.update(nova_pontuacao)
    del pessoas['Pontuacao']
    print(pessoas)

pessoas = {'Pessoas' : dicio['Pessoas']}
dicio = {'Pessoas' : pessoas}
dados_json = json.dumps(dicio['Pessoas'], indent=4)
arquivo = open("../../../../Jason/exercicios2.json", "a")
arquivo.write(dados_json)
arquivo.close()




