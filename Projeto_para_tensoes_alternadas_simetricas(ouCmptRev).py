#   Aula 2
#   Projeto para tensoes alternadas dimetricas ou completamente reversas
#------------------------------------------------------------
import os
import aula_1
import aula_2
os.system('cls')

#  1. Determinar numero de ciclos n
#           A partir de um dado numero de ciclos, e aplicado
#           na curva S-N para se determinar S_f que eh o limite
#           de resistencia a fadiga nao corrigido
#           OBS: Cada curva eh dada por cada material
#           OBS2: Para acima de 10^6 de ciclos é considerado 
#           vida infinita
#   Aqui é definido S_e e S_ut
n   = input('insira o numero de ciclos do equipamento\n')
S_e = input('insira o valor obtido no grafico S-N para S_e dado o numero de ciclos no material designado(em MPa)\n')
S_ut= input('insira o valor de S_ut dado o S_e e o material escolhido (em MPa)\n')

#  2. Determinar a faixa da carga alternada e pico a pico 
#     (ou faixa de carregamento)
def carga_alternada_Sigma_a(tensao_max, tensao_min):
    return ((tensao_max - tensao_min) / 2)

def carga_media_Sigma_m(tensao_max, tensao_min):
    return ((tensao_max + tensao_min) / 2)

#  3. Determinar os fatores de concentracao de tensao 
#     geometricos (Kt ou Kts), tomando em base a geometria
#     da peca e do entalhe
#           OBS: Verificar as tabelhas para cada tipo de entalhe
K_t = input('insira o valor obtido para K_t dado na tabela referente a geometria\n')

#  4. Selecionar o material da peca e definir as propriedades
#     do material [S_ut S_y S_e_dot S_f_dot q]

S_ut_ksi = aula_1.Mpa2ksi(S_ut)
print('Dado do valor de Sut em ksi :', S_ut_ksi,'ksi,')
const_Neuber = input('insira o valor da constante de Neuber referente\n')
raio_entalhe = input('insira o valor do raio de entalhe r\n')
q = aula_2.fatorSensibilidadeAoEntalhe_q_porConsNeuber(const_Neuber, raio_entalhe)

#  5. Determinar os fatores de concentracao em fadiga K_f a 
#     partir do fator de concentracao geometrico k_t e da 
#     sensibilidade ao entalhe q

K_f = 1 + q * (K_t - 1)

#  6. A Partir da analise de tensaoes deve se determinar a 
#     componente alternada nominal sigma_a_nom e, 
#     atraves do fator de concentracao de tensoes 
#     em fadiga K_f_I (?), obter a componente real sigma_a

sigma_a_nom = carga_alternada_Sigma_a()
sigma_a = K_f * sigma_a_nom

#  7. Determinar as tensoes principais alternadas nas 
#     localizacoes criticas, ja considerando o efeito de 
#     fatores de concentracao de tensoes

#  8. Estimar a tensao efetiva de von mises nas regioes criticas

#  9. Determinar os fatores de correcao para resistencia a 
#     fadiga [S_e_dot S_f_dot] [C_car C_tam C_sup C_temp C_con]
#------------------------------------------------------------------------
with open('Fatores_de_concentracao_de_tensoes_em_fadiga.py','r') as file:
    definir_fatores = file.read()
fatores_C = {}
exec (definir_fatores,fatores_C)

C_carga = fatores_C['C_carga']
C_tam   = fatores_C['C_tam']
C_temp  = fatores_C['C_temp']
C_sup   = fatores_C['C_sup']
C_conf  = fatores_C['C_conf']
#-------------------------------------------------------------------------

# 10. Calcular a resistencia a fadiga cortrigida para o ciclo 
#     de vida n, se a curva s-n apresenta cotovelo que 
#     caracteriza o limite de resistencia a fadiga para 
#     vida infinita, entao, S_f = S_e

# 11. Comparara a tensao alternada efetiva de von mises com a 
#     reistencia a fadiga corrigida, obitida da curva S-N, 
#     para o ciclo de vida desejado.

# 12. Calcular o farot de seguranca N_f = S_f / sigma_n_l
#------------------------------------------------------------
#
#
#
#------------------------------------------------------------
__NUM_CICLOS_n__ = 100000
