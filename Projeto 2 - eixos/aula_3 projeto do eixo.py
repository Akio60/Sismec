import math

#   Dados do enunciado

potencia_motor_HP     = 5
velocidade_cnd1_min_rpm = 500
velocidade_cnd1_max_rpm = 600
velocidade_cnd2_rpm     = 700

angulo_de_pressao_phi   = 20
diam_coroa_1_mm         = 180
diam_coroa_2_mm         = 195
diam_polia_mm           = 100

razao_fp1_fp2           = 5

raio_de_entalhe_mm      = 0.25
raio_de_concordancia_mm = 0.25
raio_de_escalonamento_mm= 0.25

def fn( fp1, fp2 ):
    return fp1 - fp2
def fs( fp1, fp2 ):
    return fp1 + fp2

# polia montada por interferencia
# ou seja, possui coeficiente de tensao unitario

# dados do material do eixo
# aco SAE 1045
ACO_Sut_Mpa         =   627 
ACO_Sy__Mpa         =   531
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
#   etapa 1
potencia_motor_W   = hp2W (potencia_motor_HP)
torque_cnd1_min_Nm = potencia_motor_W / (2 * math.pi * velocidade_cnd1_max_rpm)
torque_cnd1_max_Nm = potencia_motor_W / (2 * math.pi * velocidade_cnd1_max_rpm)
torque_cnd2_Nm     = potencia_motor_W / (2 * math.pi * velocidade_cnd2_rpm)

#------------------------------------------------#
#   etapa 2
# utilizando o maior torque

forca_associada_torque_cnd1_fn   = torque_cnd1_max_Nm
forca_associada_torque_cnd2_fn   = torque_cnd2_Nm
forca_flete_eixo_cnd1_Fs         = 1.5 * forca_associada_torque_cnd1_fn
forca_flete_eixo_cnd2_Fs         = 1.5 * forca_associada_torque_cnd2_fn

#------------------------------------------------#
# etapa 3

def forca_tangencial_engrenagem_Fgtan(Torque, raio_engrenagem):
    return Torque/raio_engrenagem
def forca_radial_engrenagem_Fgradial(forca_Fgtan, angulo_acao_rad):
    return forca_Fgtan * math.sin(angulo_acao_rad)


