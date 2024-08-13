# Aula 2

# Fator de sensibilidade ao entalhe [q]
# dado K_f (dinamico) ou em fadiga
#      K_t (estatico) ou geometrico
def fatorSensibilidadeAoEntalhe_q_porFatoresDeConcentracao(fator_concentracao_dinamico, fator_concentracao_geometrico):
    return ((fator_concentracao_dinamico - 1) / (fator_concentracao_geometrico - 1))
# a partir dos valores de concentracao, e possivel calcular as tensoes reais
#   PS: O fator de concentracao geometrico e dado pela geometria local, 
#   ou seja, ha uma tabela com as curvas relacionadas a relacao entre 
#   seccoes do eixo, onde e utilizado o fator de concentracao e o raio 
#   de entalhe [ver tabelas]

# Para usar o metodo de constante de neuber, utilizar a tabela em [ksi] e [in]
def fatorSensibilidadeAoEntalhe_q_porConsNeuber(const_Neuber, raio_de_entalhe):
    return (1 / (1+(int(const_Neuber) / (raio_de_entalhe**(0.5)))))
