#   Vitor Akio Isawa
#   Projeto 1 - Sistemas Mecânicos - Dimensionamento de engrenagens
#       
#       Desafio
# 
#-------------------------------------------------------#
import math
import os

os.system('cls')

#   conversor ksi para Mpa e vice versa
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
    return hp * 754.7
def rpm2rad(RPM):
    return RPM * 2 * math.pi /60
def m2ft(m):
    return m * 3.28084
def N2lb(N):
    return N*0.2248
def ftmin2ms(ftmin):
    return ftmin * 0.00508
def angle2rad(angle):
    return angle * math.pi / 180
def rad2angle(rad):
    return rad * 180/ math.pi

Distancia_entre_centros_C   = 162.0  
diam_prim_dp_g1_mm          = 180  
diam_prim_dp_p1_mm          = 144.0
raio_prim_rp_g_mm           = diam_prim_dp_g1_mm / 2
raio_prim_rp_p_mm           = diam_prim_dp_p1_mm / 2
n_dentes_p1                 = 48
diam_prim_dp_p1_pol         = mm2pol(diam_prim_dp_p1_mm)
passo_diam                  = n_dentes_p1 / diam_prim_dp_p1_pol
adendo_a_pol                = 1/passo_diam
adendo_a_mm                 = pol2mm(adendo_a_pol)

# atraves da nova distancia entre centros, conseguimos obter o novo angulo de pressao
Distancia_entre_centros_C_nova  = Distancia_entre_centros_C * 1.02
raio_prim_rp_p_mm_novo          = Distancia_entre_centros_C_nova - raio_prim_rp_g_mm
novo_cos    = (raio_prim_rp_p_mm + raio_prim_rp_g_mm)/Distancia_entre_centros_C_nova
novo_phi = math.acos(novo_cos)

# a partir do novo angulo de pressao, obtemos a linha Z
z_1               = (raio_prim_rp_p_mm_novo + adendo_a_mm) ** 2 - (raio_prim_rp_p_mm_novo * math.cos(novo_phi)) ** 2
z_2               = (raio_prim_rp_g_mm + adendo_a_mm) ** 2 - (raio_prim_rp_g_mm * math.cos(novo_phi)) ** 2 
linha_acao_Z      = (z_1 ** 0.5) + (z_2 ** 0.5) - Distancia_entre_centros_C_nova * math.sin(novo_phi)


#Par engrenado 1--------------------------#
paso_circ_pc      = math.pi * diam_prim_dp_p1_mm / n_dentes_p1

#Par engrenado 1--------------------------#
paso_base_pb      = paso_circ_pc * math.cos(novo_phi)

#Par engrenado 1--------------------------#
# com o novo passo base e anova linha de acao Z, obtemos a razao de contato
razao_contato_mp  = linha_acao_Z / paso_base_pb


print("o novo angulo de pressao obtido foi : "      ,   round(rad2angle(novo_phi),2))
print("o raio primitivo engrenagem obtido foi : "   ,   round(raio_prim_rp_g_mm,1))
print("o raio primitivo pinhao obtido foi : "       ,   round(raio_prim_rp_p_mm_novo,1))
print("a nova razao de contato obtida foi : "       ,   round(razao_contato_mp,3))


