import math
import os

def ksi2Mpa(ksi):
    return float(ksi) * 6.8965517241379
def Mpa2ksi(Mpa):
    return float(Mpa) * 0.145038
def psi2Mpa(psi):
    return float(psi) * 0.006894744825494
def Mpa2psi(Mpa):
    return float(Mpa) * 145.038
def mm2ft(mm):
    return mm*0.0032808399
def mm2pol(mm):
    return float(mm) / 25.4
def pol2mm(pol):
    return float(pol) * 25.4
def angle2rad(angle):
    return angle * math.pi / 180
def hp2W(hp):
    return hp * 745.7
def rpm2rad(RPM):
    return RPM * 2 * math.pi /60
def m2ft(m):
    return m * 3.28084
def N2lb(N):
    return N*0.2248
def ftmin2ms(ftmin):
    return ftmin * 0.00508
#------------------------------------------------#
#   Dados do enunciado

potencia_motor_HP       = 5
velocidade_cnd1_min_rpm = 500
velocidade_cnd1_max_rpm = 600
velocidade_cnd2_rpm     = 700

angulo_de_pressao_phi   = 20
angulo_de_pressao_rad   = angle2rad(angulo_de_pressao_phi)

diam_coroa_1_mm         = 180
diam_coroa_2_mm         = 195
diam_polia_mm           = 100
diam_polia_m            = diam_polia_mm      / 1000
raio_coroa_1_mm         = diam_coroa_1_mm    /  2
raio_coroa_2_mm         = diam_coroa_2_mm    /  2
raio_coroa_1_m          = raio_coroa_1_mm    /  1000
raio_coroa_2_m          = raio_coroa_2_mm    /  1000

razao_fp1_fp2           = 5

raio_de_entalhe_mm      = 0.25
raio_de_concordancia_mm = 0.25
raio_de_escalonamento_mm= 0.25

raio_de_entalhe_in      =mm2pol(raio_de_entalhe_mm      )
raio_de_concordancia_in =mm2pol(raio_de_concordancia_mm )
raio_de_escalonamento_in=mm2pol(raio_de_escalonamento_mm)



def fn( fp1, fp2 ):
    return fp1 - fp2
def fs( fp1, fp2 ):
    return fp1 + fp2

# polia montada por interferencia
# ou seja, possui coeficiente de tensao unitario

# dados do material do eixo
# aco SAE 1045
ACO_Sut_Mpa         =   627.0
ACO_Sy__Mpa         =   531.0
confiabilidade      =   90
eixo                =   "usinado"
temp_operacao_max_C =   400

# dimensoes dadas da secoes do eixo
L_1_mm  =   60
L_2_mm  =   50
L_3_mm  =   100
L_4_mm  =   70
L_5_mm  =   70

# distancias que caracterizam os pontos centrais dos elementos
L_d1_mm =   35
L_d2_mm =   18
L_d3_mm =   14
L_d4_mm =   35
L_d5_mm =   20

# dados do projeto
coeficiente_seguranca               = 3
# para iniciar as iteracaoes, utilizar D/dcrit e entao
# para cara iteracao estimando o diametro d, é possivel obter a nova
# relacao D/d
relacao_escalonamento_fixa_D_dcrit  = 1.2
# calcular o concentradores de tensao relativo apos a segunda iteracao
# arredondar os valores de sai#ra para numeros inteiros em mm

# ------------------------------------------- #
def momento_inercia_eixo_solido(diametro):
    return math.pi * (diametro ** 4) / 64

def tensao_flexao_alternada(fator_concentracao_tensao_fadiga_fletor_alternada_Kf,
                            momento_alternado_Ma,
                            raio_r,
                            momento_inercia_I):
    return fator_concentracao_tensao_fadiga_fletor_alternada_Kf * momento_alternado_Ma * raio_r / momento_inercia_I

def tensao_flexao_media(fator_concentracao_tensao_fadiga_media,
                            momento_medio,
                            raio,
                            momento_inercia_I):
    return fator_concentracao_tensao_fadiga_media * momento_medio * raio / momento_inercia_I


#---------------------------------------------#

#   etapa 1
potencia_motor_W        = hp2W (potencia_motor_HP)
torque_cnd1_min_Nm      = potencia_motor_W   / (2 * math.pi * velocidade_cnd1_max_rpm  / 60)
torque_cnd1_max_Nm      = potencia_motor_W   / (2 * math.pi * velocidade_cnd1_min_rpm  / 60)

torque_cnd1_medio_Nm    = (torque_cnd1_min_Nm + torque_cnd1_max_Nm) / 2
torque_cnd1_alternado_Nm= (torque_cnd1_max_Nm - torque_cnd1_min_Nm) / 2
torque_cnd2_Nm          = potencia_motor_W   / (2 * math.pi * velocidade_cnd2_rpm      / 60)

#------------------------------------------------#
#   etapa 2
# notar a direcao das forcas para abitrariamente decidir o sinal da euqacao

forca_associada_torque_cnd1_fn_medio_N      = torque_cnd1_medio_Nm    /   raio_coroa_1_m
forca_associada_torque_cnd1_fn_alternado_N  = torque_cnd1_alternado_Nm/   raio_coroa_1_m
forca_associada_torque_cnd2_fn_N            = torque_cnd2_Nm          /   raio_coroa_2_m

forca_flete_eixo_cnd1_Fs_medio              = 1.5 * forca_associada_torque_cnd1_fn_medio_N
forca_flete_eixo_cnd1_Fs_alternado          = 1.5 * forca_associada_torque_cnd1_fn_alternado_N
forca_flete_eixo_cnd2_Fs                    = 1.5 * forca_associada_torque_cnd2_fn_N

#------------------------------------------------#
# etapa 3
#sinais colocados abritariamente para condizer com os eixos
forca_tangencial_engrenagem_cnd1_medio_Fgztan     = -torque_cnd1_medio_Nm     / raio_coroa_1_m
forca_tangencial_engrenagem_cnd1_alternado_Fgztan = -torque_cnd1_alternado_Nm / raio_coroa_1_m
forca_tangencial_engrenagem_cnd2_Fgztan           = -torque_cnd2_Nm           / raio_coroa_2_m

forca_radial_engrenagem_cnd1_medio_Fgyradial      = -forca_tangencial_engrenagem_cnd1_medio_Fgztan     * math.tan(angulo_de_pressao_rad)
forca_radial_engrenagem_cnd1_alternado_Fgyradial  = -forca_tangencial_engrenagem_cnd1_alternado_Fgztan * math.tan(angulo_de_pressao_rad)
forca_radial_engrenagem_cnd2_Fgyradial            = -forca_tangencial_engrenagem_cnd2_Fgztan           * math.tan(angulo_de_pressao_rad)

#------------------------------------------------#
# etapa 4
# Resolvendo para as equacoes de quilibrio momento, considerando individualmente cada condicao de engrenamento

# 4.1 - distancias de centros
# consideracoes a partir do mancal 1 , da esquerda para direita
# da imagem do projeto apresentado

distancia_coroa_1_mm = L_d1_mm + L_2_mm - L_d2_mm
distancia_coroa_2_mm = L_d1_mm + L_2_mm + L_3_mm + L_d3_mm
distancia_polia_mm   = L_d1_mm + L_2_mm + L_3_mm + L_4_mm + L_5_mm - L_d5_mm
distancia_mancal2_mm = L_d1_mm + L_2_mm + L_3_mm + L_4_mm + L_d4_mm

distancia_coroa_1_m  = distancia_coroa_1_mm / 1000
distancia_coroa_2_m  = distancia_coroa_2_mm / 1000
distancia_polia_m    = distancia_polia_mm   / 1000
distancia_mancal2_m  = distancia_mancal2_mm / 1000

#--------------------------

def R2(fg, dist_coroa, fs, dist_polia, dist_mancal):
    return -(fg * dist_coroa + fs * dist_polia)/dist_mancal
def R1(fg, fs, R2):
    return -fg - fs - R2

R2y_cnd1_medio     = R2(forca_radial_engrenagem_cnd1_medio_Fgyradial    , distancia_coroa_1_m, forca_flete_eixo_cnd1_Fs_medio, distancia_polia_m, distancia_mancal2_m)
R1y_cnd1_medio     = R1(forca_radial_engrenagem_cnd1_medio_Fgyradial    , forca_flete_eixo_cnd1_Fs_medio, R2y_cnd1_medio)
R2z_cnd1_medio     = R2(forca_tangencial_engrenagem_cnd1_medio_Fgztan   , distancia_coroa_1_m, 0, distancia_polia_m, distancia_mancal2_m)
R1z_cnd1_medio     = R1(forca_tangencial_engrenagem_cnd1_medio_Fgztan   , 0, R2z_cnd1_medio)


R2y_cnd1_alternado = R2(forca_radial_engrenagem_cnd1_alternado_Fgyradial, distancia_coroa_1_m, forca_flete_eixo_cnd1_Fs_alternado, distancia_polia_m, distancia_mancal2_m)
R1y_cnd1_alternado = R1(forca_radial_engrenagem_cnd1_alternado_Fgyradial, forca_flete_eixo_cnd1_Fs_alternado, R2y_cnd1_alternado)
R2z_cnd1_alternado = R2(forca_tangencial_engrenagem_cnd1_alternado_Fgztan, distancia_coroa_1_m, 0, distancia_polia_m, distancia_mancal2_m)
R1z_cnd1_alternado = R1(forca_tangencial_engrenagem_cnd1_alternado_Fgztan, 0, R2z_cnd1_alternado)

def norm(valor1, valor2):
  return math.sqrt(valor1**2+valor2**2)



# CALCULO DOS MOMENTOS MEDIOS NORMALIZADOS EM CADA PONTO
# SEÇÃO 1

momento_norm_A_cnd1 = 0

soma_my_B_cnd1 = R1y_cnd1_medio*(L_d1_mm/1000)
soma_mz_B_cnd1 = R1z_cnd1_medio*(L_d1_mm/1000)
momento_norm_B_cnd1 = norm(soma_my_B_cnd1, soma_mz_B_cnd1)

# SEÇÃO 2

soma_my_C_cnd1 = R1y_cnd1_medio*((L_2_mm-L_d2_mm+L_d1_mm)/1000)
soma_mz_C_cnd1 = R1z_cnd1_medio*((L_2_mm-L_d2_mm+L_d1_mm)/1000)
momento_norm_C_cnd1 = norm(soma_my_C_cnd1, soma_mz_C_cnd1)

soma_my_D_cnd1 = R1y_cnd1_medio*((L_2_mm+L_d1_mm)/1000)+forca_radial_engrenagem_cnd1_medio_Fgyradial*(L_d2_mm/1000)
soma_mz_D_cnd1 = R1z_cnd1_medio*((L_2_mm+L_d1_mm)/1000)+forca_tangencial_engrenagem_cnd1_medio_Fgztan*(L_d2_mm/1000)
momento_norm_D_cnd1 = norm(soma_my_D_cnd1, soma_mz_D_cnd1)

# SEÇÃO 3

soma_my_E_cnd1 = R1y_cnd1_medio*((L_2_mm+L_3_mm/2+L_d1_mm)/1000)+forca_radial_engrenagem_cnd1_medio_Fgyradial*((L_3_mm/2+L_d2_mm)/1000)
soma_mz_E_cnd1 = R1z_cnd1_medio*((L_2_mm+L_3_mm/2+L_d1_mm)/1000)+forca_tangencial_engrenagem_cnd1_medio_Fgztan*((L_3_mm/2+L_d2_mm)/1000)
momento_norm_E_cnd1 = norm(soma_my_E_cnd1, soma_mz_E_cnd1)

# SEÇÃO 4

soma_my_F_cnd1 = R1y_cnd1_medio*((L_2_mm+L_3_mm+L_d1_mm)/1000)+forca_radial_engrenagem_cnd1_medio_Fgyradial*((L_3_mm+L_d2_mm)/1000)
soma_mz_F_cnd1 = R1z_cnd1_medio*((L_2_mm+L_3_mm+L_d1_mm)/1000)+forca_tangencial_engrenagem_cnd1_medio_Fgztan*((L_3_mm+L_d2_mm)/1000)
momento_norm_F_cnd1 = norm(soma_my_F_cnd1, soma_mz_F_cnd1)

soma_my_G_cnd1 = R1y_cnd1_medio*((L_2_mm+L_3_mm+L_d3_mm+L_d1_mm)/1000)+forca_radial_engrenagem_cnd1_medio_Fgyradial*((L_3_mm+L_d3_mm+L_d2_mm)/1000)
soma_mz_G_cnd1 = R1z_cnd1_medio*((L_2_mm+L_3_mm+L_d3_mm+L_d1_mm)/1000)+forca_tangencial_engrenagem_cnd1_medio_Fgztan*((L_3_mm+L_d3_mm+L_d2_mm)/1000)
momento_norm_G_cnd1 = norm(soma_my_G_cnd1, soma_mz_G_cnd1)

# SEÇÃO 5

soma_my_H_cnd1 = R1y_cnd1_medio*((L_2_mm+L_3_mm+L_4_mm+L_d1_mm)/1000)+forca_radial_engrenagem_cnd1_medio_Fgyradial*((L_3_mm+L_4_mm+L_d2_mm)/1000)
soma_mz_H_cnd1 = R1z_cnd1_medio*((L_2_mm+L_3_mm+L_4_mm+L_d1_mm)/1000)+forca_tangencial_engrenagem_cnd1_medio_Fgztan*((L_3_mm+L_4_mm+L_d2_mm)/1000)
momento_norm_H_cnd1 = norm(soma_my_H_cnd1, soma_mz_H_cnd1)

soma_my_I_cnd1 = R1y_cnd1_medio*((L_d1_mm+L_2_mm+L_3_mm+L_4_mm+L_d4_mm)/1000)+forca_radial_engrenagem_cnd1_medio_Fgyradial*((L_3_mm+L_4_mm+L_d2_mm+L_d4_mm)/1000)
soma_mz_I_cnd1 = R1z_cnd1_medio*((L_d1_mm+L_2_mm+L_3_mm+L_4_mm+L_d4_mm)/1000)+forca_tangencial_engrenagem_cnd1_medio_Fgztan*((L_3_mm+L_4_mm+L_d2_mm+L_d4_mm)/1000)
momento_norm_I_cnd1 = norm(soma_my_I_cnd1, soma_mz_I_cnd1)

soma_my_J_cnd1 = R1y_cnd1_medio*((L_d1_mm+L_2_mm+L_3_mm+L_4_mm+L_5_mm-L_d5_mm)/1000)+forca_radial_engrenagem_cnd1_medio_Fgyradial*((L_d2_mm+L_3_mm+L_4_mm+L_5_mm-L_d5_mm)/1000) + R2y_cnd1_medio*((L_5_mm-L_d5_mm)/1000)
soma_mz_J_cnd1 = R1z_cnd1_medio*((L_d1_mm+L_2_mm+L_3_mm+L_4_mm+L_5_mm-L_d5_mm)/1000)+forca_tangencial_engrenagem_cnd1_medio_Fgztan*((L_d2_mm+L_3_mm+L_4_mm+L_5_mm-L_d5_mm)/1000) + R2z_cnd1_medio*((L_5_mm-L_d5_mm)/1000)
momento_norm_J_cnd1 = norm(soma_my_J_cnd1, soma_mz_J_cnd1)


#------------------------------------------------#
# etapa 5
# Coeficiente de correcao
# confiabilidade para 90%
C_conf  = 0.897

# temperatura < 450
C_temp  = 1

# considerando d < 8 mm , caso contrario reavaliar
c_tam   = 1

# Flexao = 1 , Carga axial = 0.7
c_carr  = 1
#------------------------------------------------#
# etapa 6
# Coeficiente de correcao de superficie
# Equacao para eixo usinado
c_sup   = 4.51 * (ACO_Sut_Mpa ** (-0.265))

#------------------------------------------------#
# etapa 8
# Resistencia a fadiga corrigida
# Limite de resistencia a fadiga Se' em vida infinita
# para aco < 200 ksi
limite_res_fadiga_S_e_dot_Mpa = 0.5 * ACO_Sut_Mpa
limite_res_fadiga_S_e_Mpa     = C_conf * C_temp * c_tam * c_carr * c_sup * limite_res_fadiga_S_e_dot_Mpa

#------------------------------------------------#
# etapa 9
# Sensibilidade ao entalhe (flexao)
# analise para 90.93 ksi
constante_neuber_flexao_a   = 0.070

# Sensibilidade ao entalhe (torcao)
# analise para 110.93 ksi
constante_neuber_torcao_as  = 0.055

sensibilidade_do_material_flexao_q  = 1 / (1 + (constante_neuber_flexao_a  / (raio_de_entalhe_in ** 0.5)))
sensibilidade_do_material_torcao_qs = 1 / (1 + (constante_neuber_torcao_as / (raio_de_entalhe_in ** 0.5)))
# a sensibilidade é adimensional

k_t_suposto       = 3.5
k_ts_suposto      = 2.0

k_f_provisorio    = 1 + sensibilidade_do_material_flexao_q  * (k_t_suposto  - 1)
k_fsm_provisorio  = 1 + sensibilidade_do_material_torcao_qs * (k_ts_suposto - 1)

d = (((32 * coeficiente_seguranca / math.pi) * ( ((k_f_provisorio * torque_cnd1_alternado_Nm / limite_res_fadiga_S_e_Mpa) ** 2) + (0.75 * ((torque_cnd1_medio_Nm / ACO_Sy__Mpa)**2))) ** 0.5 )   ) ** 0.3333



os.system('cls')

print(Mpa2ksi(ACO_Sut_Mpa))
print(round(d     ,2))

print()
print("Torque medio:     \nMmed:" , round(torque_cnd1_medio_Nm,2),     " Nm")
print("Torque alternado: \nMalt:" , round(torque_cnd1_alternado_Nm,2), " Nm")

print("Forca da engrenagem em y (media):                       \nFgy med:  " , round(forca_radial_engrenagem_cnd1_medio_Fgyradial     ,2),"  N")
print("Forca da engrenagem em y (alternada):                   \nFgy alt:  " , round(forca_radial_engrenagem_cnd1_alternado_Fgyradial ,2),"  N")

print("Forca da engrenagem em z (media):                       \nFgz med:  " , round(forca_tangencial_engrenagem_cnd1_medio_Fgztan    ,2),"  N")
print("Forca da engrenagem em z (alternada):                   \nFgz alt:  " , round(forca_tangencial_engrenagem_cnd1_alternado_Fgztan,2),"  N")

print("Forca da polia associada ao Torque (media):             \nFn med:  " , round(forca_associada_torque_cnd1_fn_medio_N     ,2),       "  N")
print("Forca da polia associada ao Torque (alternada):         \nFn alt:  " , round(forca_associada_torque_cnd1_fn_alternado_N ,2),       "  N")

print("Forca da polia associada ao Momento fletor (media):     \nFs med:  " , round(forca_flete_eixo_cnd1_Fs_medio     ,2),              "  N")
print("Forca da polia associada ao Momento fletor (alternada): \nFs alt:  " , round(forca_flete_eixo_cnd1_Fs_alternado ,2),              "  N")

print()
print("R1y (media): \n",     round(R1y_cnd1_medio,2),    "  N")
print("R1z (media): \n",     round(R1z_cnd1_medio,2),    "  N")
print("R2y (media): \n",     round(R2y_cnd1_medio,2),    "  N")
print("R2z (media): \n",     round(R2z_cnd1_medio,2),    "  N")

print()
print("R1y (alternada): \n", round(R1y_cnd1_alternado,2),"  N")
print("R1z (alternada): \n", round(R1z_cnd1_alternado,2),"  N")
print("R2y (alternada): \n", round(R2y_cnd1_alternado,2),"  N")
print("R2z (alternada): \n", round(R2z_cnd1_alternado,2),"  N")
print()

print("SEÇÃO 1")
print("momento nomalizado no ponto A: \n", round(momento_norm_A_cnd1, 2),"  Nm")
print("momento nomalizado no ponto B: \n", round(momento_norm_B_cnd1, 2),"  Nm")

print("SEÇÃO 2")
print("momento nomalizado no ponto C: \n", round(momento_norm_C_cnd1, 2),"  Nm")
print("momento nomalizado no ponto D: \n", round(momento_norm_D_cnd1, 2),"  Nm")

print("SEÇÃO 3")
print("momento nomalizado no ponto E: \n", round(momento_norm_E_cnd1, 2),"  Nm")
print("momento nomalizado no ponto F: \n", round(momento_norm_F_cnd1, 2),"  Nm")

print("SEÇÃO 4")
print("momento nomalizado no ponto G: \n", round(momento_norm_G_cnd1, 2),"  Nm")
print("momento nomalizado no ponto H: \n", round(momento_norm_H_cnd1, 2),"  Nm")

print("SEÇÃO 5")
print("momento nomalizado no ponto I: \n", round(momento_norm_I_cnd1, 2),"  Nm")
print("momento nomalizado no ponto J: \n", round(momento_norm_J_cnd1, 2),"  Nm")



print()

