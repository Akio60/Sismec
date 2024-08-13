## 1. Teoria de falha por fadiga
#       - Cargas alternadas em fadiga
#           -Alternada simetrica    (alterna no 0)
#           -Ciclica pulsante       (oscila somente acima e etangenciando o eixo x)
#           -Ciclica                (oscila acima do eixo, sem encontro no eixo x)
#
# Obs: essa informação é necessária para conhecimento do numero de ciclos de vida do equipamento.
#
#       - Principais diagramas
#           -Curva S-N , relaciona o n de ciclos com o limite de resistencia a fadiga S_f

# Variaveis a definir
theta_max = 0
theta_min = 0 
S_y_Uniaxial = 0
S_ut = 0
S_yz = 0


# Tensao alternada
theta_a = (theta_max - theta_min)/2
# Tensao media
theta_m = (theta_max + theta_min)/2
# Variacao da tensao
delta_theta = theta_max - theta_min
# modulo de elasticidade do material        ##DEFINIR VALOR##
E = 1
# Coeficiente de poisson
v = 0

# Energia de deformacao  [ Ud ]

# referente ao estado uniaxial de tensao:
U_d_Uniaxial = ((1 + v) * S_y_Uniaxial^2) / (3 * E)

# Multiplo 
# Definir theta1,2 atraves dos metodos de resistencia dos materiais
theta_1 = 0 
theta_2 = 0
S_y_Multiplo = (theta_1^2 + theta_2^2 - theta_1 * theta_2) ** (1 / 2)
U_d_Multiplo = (1+v) * (theta_1^2 + theta_2^2 - theta_1 * theta_2) / (3 * E)

# Tal -> tensao cisalhante/cortante         #Verificar
Tal_max = S_yz # verificar
S_y_Torcional = (3*(Tal_max^2))


# Aco
if S_ut < 200: #ksi
    S_e = 0.5 * S_ut
else:
    S_e = 100  #ksi

# Ferro fundido
if S_ut < 200: #ksi
    S_e = 0.4 * S_ut
else:
    S_e = 24  #ksi


# A_95 -> dado  pela area tencionada acima de 95% da tensao maxima, verificar valores

#   conversor ksi para Mpa e vice versa
def ksi2Mpa(ksi):
    return float(ksi) * 6.8965517241379
def Mpa2ksi(Mpa):
    return float(Mpa) * 0.145038

# dot sao as tensoes nao corrigidas
#S_e_dot = 1
#S_f_dot = 1
#S_e = float(C_carga) * float(C_tam) * float(C_temp) * float(C_sup) * float(C_conf) * S_e_dot
#S_f = C_carga * C_tam * C_temp * C_sup * C_conf * S_f_dot
# S_fs = 0,577 * S_f