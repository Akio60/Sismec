## 1. Teoria de falha por fadiga
#       - Cargas alternadas em fadiga
#           -Alternada simetrica    (alterna no 0)
#           -Ciclica pulsante       (oscila somente acima e etangenciando o eixo x)
#           -Ciclica                (oscila acima do eixo, sem encontro no eixo x)
#
# Obs: essa informação é necessária para conhecimento do numero de ciclos de vida do equipamento.
#
# 
include math
# Variaveis a declarar
theta_max = 0
theta_min = 0 
S_y_Uniaxial = 0
v = 0
# Tensão alternada
theta_a = (theta_max - theta_min)/2
# Tensão média
theta_m = (theta_max + theta_min)/2
# Variação da tensão
delta_theta = theta_max - theta_min

# Energia de deformação  [ Ud ]
# 
U_d_Uniaxial = ((1 + v) * S_y_Uniaxial^2) / (3 * E)
#   - A partir das tensoes principais e do diagrama de tenao deformacao
# referente ao estado uniaxial de tensão:
theta_1 = S_y_Uniaxial, 
theta_2 = theta_3 = 0

#   - Resultando em:
S_y_Multiplo = (theta_1^2 + theta_2^2 - theta_1 * theta_2)**(1/2)
U_d_Multiplo = (1+v) * (theta_1^2 + theta_2^2 - theta_1 * theta_2) / 3 * E


Tal_max = S_yz # verificar
S_y_Torcional = (3*pow(2,Tal_max))


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


#
# E -> obtido no ensaior de tração
# Fator de segurança é calculado no diagrama S-N com as componentes medias e alternada da tensão (thetha_a e thetha_m)
#
#

# A_95 -> dado  pela area tencionada acima de 95% da tensao maxima, verificar valores


#tipo de carregamento
def definir_fator_Kc(tipo_de_carregamento);
    match tipo_de_carregamento:
        case 1: # Flexao alternada
            return 1
        case 2: # Carga Axial
            return 0,7
        case _: #   Casos excedentes
            return "ERROR"

#tamanho da peca (em mm)
def definir_fator_Ks(tamanho):
    if 0 < tamanho < 8:
        return 1
    elif 8 < tamanho < 250:
        return 1.189 * tamanho ** (-0.097)
    else:
        return "ERROR"
    
#temperatura
def definir_fator_Kt(temperatura)

#superficie  -> Verificar tabela no slide
def definir_fator_Ksup(superficie)
    
#confiabilidade
def definir_fator_Kconf(confiabilidade)


tipo_de_carregamento    = input("insira o tipo de carregamento\n 1- Flexao alternada  \n 2- Carga Axial")
tamanho                 = input("insira o tamanho em mm (verificar caso dado esteja em in)")
temperatura             = input("insira a temperatura de operacao em C")
superficie              = input("insira o tipo de superficie\n 1-  \n 2-  \n3-  ")
confiabilidade          = input("insira o tipo de carregamento\n 1-  \n 2-  \n3-  ")

C_carga = definir_fator_Kc(tipo_de_carregamento)
C_tam   = definir_fator_Ks(tamanho)
C_temp  = definir_fator_Kt(temperatura)
C_sup   = definir_fator_Ksup(superficie)
C_conf  = definir_fator_Kconf(confiabilidade)

S_e = C_carga * C_tam * C_temp * C_sup * C_conf * S_e_dot
S_f = C_carga * C_tam * C_temp * C_sup * C_conf * S_f_dot
S_fs = 0,577 S_f