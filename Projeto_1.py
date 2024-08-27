import math
import os
import aula_1
import aula_2

os.system('cls')

#   conversor ksi para Mpa e vice versa
def ksi2Mpa(ksi):
    return float(ksi) * 6.8965517241379
def Mpa2ksi(Mpa):
    return float(Mpa) * 0.145038
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
#-------------------------------------------------------#
# Dados do sistema

# cnd -> condicao 1 : pinhao 1 e coroa 1
# cnd -> condicao 2 : pinhao 2 e coroa 2

pot_Hp             = 5
cnd_1_rpm_min      = 500
cnd_1_rpm_max      = 600
cnd_1_rads_min     = rpm2rad(cnd_1_rpm_min)
cnd_1_rads_max     = rpm2rad(cnd_1_rpm_max)
cnd_2_rpm          = 1000
ang_pres_phi       = 20
ang_pres_phi_rad   = angle2rad(ang_pres_phi)
mod_gears_mm       = 3
num_dent_n_g1      = 60
num_dent_n_p2      = 43 

material           = 'aco'
lim_res_fadg_Se_Mpa= 700    #dado do slide de teoria de dalha por fadiga
lim_res_fadg_Sut_Mpa= lim_res_fadg_Se_Mpa / 0.5
E_Gpa              = 190
v                  = 0.27
grau_AGMA          = 1
dureza_final_HB    = 350
temp_vida_anos     = 5
temp_operacao_C    = 121
confiabilidade     = 90     # %
razao_vel_m_v1     = 0.8
#-------------------------------------------------------#

#   Calculo da geometria das engrenagens do par 1

# a partir da razao de velocidades mv na condicao 1
razao_engr_mg_1   = 1 / razao_vel_m_v1
num_dent_n_p1     = num_dent_n_g1 / razao_engr_mg_1


# A unidade de saida do passo diametral deve ser em num_dentes/pol
# a fim de facilitar as especificacoes de engrenagens
diam_prim_dp_g1_mm  = mod_gears_mm * num_dent_n_g1
diam_prim_dp_g1_pol = mm2pol(diam_prim_dp_g1_mm)
diam_prim_dp_p1_pol = diam_prim_dp_g1_pol * razao_vel_m_v1
diam_prim_dp_p1_mm  = pol2mm(diam_prim_dp_p1_pol)
paso_diam_pd_1      = num_dent_n_g1 / diam_prim_dp_g1_pol

#-------------------------------------------------------#
# Dados da tabela do slide 17 do arquivo ENGRENAGENS CILINDRICAS DE DENTES RETOS - Parte 1.pdf
# saindo em pol
adendo_a1         = 1.000 / paso_diam_pd_1
dedendo_b1        = 1.250 / paso_diam_pd_1
prof_trab_1       = 2.000 / paso_diam_pd_1
pro_total_1       = 2.250 / paso_diam_pd_1
esp_circ_ref_1    = 1.571 / paso_diam_pd_1
raio_arred_1      = 0.300 / paso_diam_pd_1 
folg_min_c1       = 0.250 / paso_diam_pd_1
larg_min_topo_1   = 0.350 / paso_diam_pd_1
# conversao para mm
adendo_a1         = pol2mm(adendo_a1)
dedendo_b1        = pol2mm(dedendo_b1)
prof_trab_1       = pol2mm(prof_trab_1)
pro_total_1       = pol2mm(pro_total_1)
esp_circ_ref_1    = pol2mm(esp_circ_ref_1)
raio_arred_1      = pol2mm(raio_arred_1) 
folg_min_c1       = pol2mm(folg_min_c1)
larg_min_topo_1   = pol2mm(larg_min_topo_1)
#-------------------------------------------------------#

diam_ext_de_p1    = diam_prim_dp_p1_mm + 2 * dedendo_b1
diam_ext_de_g1    = diam_prim_dp_g1_mm + 2 * dedendo_b1

raio_prim_p1_mm   = diam_prim_dp_p1_mm / 2
raio_prim_g1      = diam_prim_dp_g1_mm / 2
dist_centros_C    = (raio_prim_p1_mm) + (raio_prim_g1)

#-------------------------------------------------------#
z_1               = (raio_prim_p1_mm + adendo_a1) ** 2 - (raio_prim_p1_mm * math.cos(ang_pres_phi_rad)) ** 2
z_2               = (raio_prim_g1 + adendo_a1) ** 2 - (raio_prim_g1 * math.cos(ang_pres_phi_rad)) ** 2 
linha_acao_Z      = (z_1 ** 0.5) + (z_2 ** 0.5) - dist_centros_C * math.sin(ang_pres_phi_rad)

#-------------------------------------------------------#
# razao_contato_mp  = linha_acao_Z * paso_diam_pd_1 /(math.pi * math.cos(ang_pres_phi_rad))

paso_circ_pc      = math.pi * diam_prim_dp_g1_mm / num_dent_n_g1
paso_base_pb      = paso_circ_pc * math.cos(ang_pres_phi_rad)
razao_contato_mp  = linha_acao_Z / paso_base_pb

#-------------------------------------------------------#
# Note que o torque e inversamente proporcional a velocidade de rotacao
#--------------------Analise Dinamica-------------------#

pot_W             = hp2W(pot_Hp)
torque_t_max      = pot_W / cnd_1_rads_min
torque_t_min      = pot_W / cnd_1_rads_max

raio_prim_p1_m    = raio_prim_p1_mm / 1000   # conversao para m

forca_tang_wt_min = torque_t_min / raio_prim_p1_m
forca_tang_wt_max = torque_t_max / raio_prim_p1_m

forca_res_w_min   = forca_tang_wt_min / math.cos(ang_pres_phi_rad)
forca_res_w_max   = forca_tang_wt_max / math.cos(ang_pres_phi_rad)

raio_prim_p1_ft         = m2ft(raio_prim_p1_m)
velocidade_tang_v_t_max = 2 * math.pi * cnd_1_rpm_max * raio_prim_p1_ft
velocidade_tang_v_t_min = 2 * math.pi * cnd_1_rpm_min * raio_prim_p1_ft
#considerando uma proximidade de ambas velocidades tang
indice_qualidade_Qv     = 8
# largura da face pode estar entre 8/pd e 16/pd
largura_de_face_F = 12 / paso_diam_pd_1

print("#-------------------------------------------------------#")
print("#--------------Dimensionamento geometrico---------------#")
print("#-------------------------------------------------------#")
print("Razao engrenamento mg\n", round(razao_engr_mg_1,3) , "")
print("Passo diametral pd 1\n",round(paso_diam_pd_1,3) , " dentes / pol")
print("Diametro primitivo da coroa dpg 1\n",round(diam_prim_dp_g1_mm,3) , " mm")
print("Adendo a 1\n",round(adendo_a1,3) , " mm")
print("Dedendo b 1\n",round(dedendo_b1,3) , " mm")
print("Folga min na raiz do dente c 1\n",round(folg_min_c1,3) , " mm")
print("Numero dentes pinhao np 1\n",round(num_dent_n_p1,0) , "dentes")
print("Numero dentes coroa ng 1\n",round(num_dent_n_g1,0) , " dentes")
print("diametro primitivo pinhao dpp 1\n",round(diam_prim_dp_p1_mm,3) , " mm")  
print("Diametro externo do pinhao dep 1\n",diam_ext_de_p1, "mm")
print("Diametro externo do pinhao deg 1\n",diam_ext_de_g1, "mm")
print("Distancia entre centros C\n",dist_centros_C, "mm")
print("Comprimento da linha de acao Z\n",round(linha_acao_Z,3), "mm")
print("Razao de contato [DEVE SER 1 < mp < 2 ] \n",round(razao_contato_mp,3), "")
print("indice de qualidade \n", indice_qualidade_Qv)
print("largura de face F \n", round(largura_de_face_F,3))

print("\n Para essa parte somente falta indice de qualidade e a \nlargura da face, a serem definidos a partir do projeto\n cinematico")
print("#-------------------------------------------------------#")
print("#--------------------Analise Dinamica-------------------#")
print("#-------------------------------------------------------#")
print("Carga tangencial min Wt\n", round(forca_tang_wt_min,3) , "N")
print("Carga tangencial max Wt\n", round(forca_tang_wt_max,3) , "N")

# largura de face deve estar entre 8/pd e 16/pd

#fator geometrico de resis flex pinhao / eng

# Fator Dinamico Kv

print(velocidade_tang_v_t_max)
print(velocidade_tang_v_t_min)

B                   = ((12 - indice_qualidade_Qv) ** (2/3)) / 4  
A                   = 50 + 56 * (1 - B)
fator_dinamico_kv_min   = (A / ( A + (200 * velocidade_tang_v_t_max) ** 0.5)) ** B
fator_dinamico_kv_max   = (A / ( A + (200 * velocidade_tang_v_t_max) ** 0.5)) ** B

print("Fator dinamico Kv min \n", fator_dinamico_kv_min)
print("Fator dinamico Kv max \n", fator_dinamico_kv_max)

# ---------------------#
# fator de aplicacao k_a
# -> choques moderados na maquina movida
# -> uniforme na maquina motoraa 

fator_aplicacao_k_a = 1.50
print("Fator aplicacao Kv \n", fator_aplicacao_k_a)

#---------------------#
# Fato de distribuicao de carga
# para largura de face <2 in
fator_distrib_k_m = 1.6
print("Fator distribuicao de carga Km \n", fator_distrib_k_m)









