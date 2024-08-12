#   Projeto para tensoes alternadas dimetricas ou completamente reversas
#------------------------------------------------------------
#  1. Determinar numero de ciclos n
#           A partir de um dado numero de ciclos, e aplicado
#           na curva S-N para se determinar S_f que eh o limite
#           de resistencia a fadiga nao corrigido
#           OBS: Cada curva eh dada por cada material

#  2. Determinar a faixa da carga alternada e pico a pico

#  3. Determinar os fatores de concentracao de tensao 
#     geometricos (Kt ou Kts), tomando em base a geometria
#     da peca e do entalhe

#  4. Selecionar o material da peca e definir as propriedades
#     do material [S_ut S_y S_e_dot S_f_dot q]

#  5. Determinar os fatores de concentracao em fadiga K_f a 
#     partir do fator de concentracao geometrico k_t e da 
#     sensibilidade ao entalhe q

#  6. A Partir da analise de tensaoes deve se determinar a 
#     componente alternada nominal sigma_a_nom e, 
#     atraves do fator de concentracao de tensoes 
#     em fadiga K_f_I (?), obter a componente real sigma_a
#           Para Esse item, utilizaremos os casos da aula 1

#  7. Determinar as tensoes principais alternadas nas 
#     localizacoes criticas, ja considerando o efeito de 
#     fatores de concentracao de tensoes

#  8. Estimar a tensao efetiva de von mises nas regioes criticas

#  9. Determinar os fatores de correcao para resistencia a 
#     fadiga [S_e_dot S_f_dot] [C_car C_tam C_sup C_temp C_con]

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
