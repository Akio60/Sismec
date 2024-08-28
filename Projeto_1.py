#   Vitor Akio Isawa
#   Projeto 1 - Sistemas Mecânicos - Dimensionamento de engrenagens
#       
#       Dimensionamento geométrico
#       Analise dinamica
# 
#-------------------------------------------------------#



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

paso_circ_pc      = math.pi * diam_prim_dp_g1_mm / num_dent_n_g1
paso_base_pb      = paso_circ_pc * math.cos(ang_pres_phi_rad)
razao_contato_mp  = linha_acao_Z / paso_base_pb

#-------------------------------------------------------#

raio_prim_p1_m    = raio_prim_p1_mm / 1000   # conversao para m


raio_prim_p1_ft         = m2ft(raio_prim_p1_m)
velocidade_tang_v_t_max = 2 * math.pi * cnd_1_rpm_max * raio_prim_p1_ft
velocidade_tang_v_t_min = 2 * math.pi * cnd_1_rpm_min * raio_prim_p1_ft

#considerando uma proximidade de ambas velocidades tang
# a partir da tabela _ do slide _ aula _
indice_qualidade_Qv     = 8

# dado : largura da face pode estar entre 8/pd e 16/pd
# utilizaremos a media
largura_de_face_F_pol        = 12 / paso_diam_pd_1
largura_de_face_F_mm         = pol2mm(largura_de_face_F_pol)
#-------------------------------------------------------#

print("#-------------------------------------------------------#")
print("#--------------Dimensionamento geometrico---------------#")
print("#-------------------------------------------------------#")
print("\nRazao engrenamento mg\n", round(razao_engr_mg_1,3) , "")
print("Passo diametral pd 1\n",round(paso_diam_pd_1,3) , " dentes / pol")
print("Diametro primitivo da coroa dpg 1\n",round(diam_prim_dp_g1_mm,3) , " mm")
print("Adendo  a 1\n",round(adendo_a1,3) , " mm")
print("Dedendo b 1\n",round(dedendo_b1,3) , " mm")
print("Folga min na raiz do dente c 1\n",round(folg_min_c1,3) , " mm")
print("Numero dentes pinhao np 1\n",round(num_dent_n_p1,0) , "dentes")
print("Numero dentes coroa ng 1\n",round(num_dent_n_g1,0) , " dentes")
print("diametro primitivo pinhao dpp 1\n",round(diam_prim_dp_p1_mm,3) , " mm")  
print("Diametro externo do pinhao dep 1\n",diam_ext_de_p1, "mm")
print("Diametro externo do pinhao deg 1\n",diam_ext_de_g1, "mm")
print("Distancia entre centros C\n",dist_centros_C, "mm")
print("Comprimento da linha de acao Z\n",round(linha_acao_Z,3), "mm")
print("Razao de contato mp [DEVE SER 1 < mp < 2 ] \n",round(razao_contato_mp,3), "")
print("indice de qualidade \n", indice_qualidade_Qv)
print("largura de face F (12/pd) \n", round(largura_de_face_F_mm,3), "mm")

#
#--------------------Analise Dinamica-------------------#

# Note que o torque e inversamente proporcional a velocidade de rotacao
pot_W             = hp2W(pot_Hp)
torque_t_max      = pot_W / cnd_1_rads_min
torque_t_min      = pot_W / cnd_1_rads_max
forca_tang_wt_min = torque_t_min / raio_prim_p1_m
forca_tang_wt_max = torque_t_max / raio_prim_p1_m

forca_res_w_min   = forca_tang_wt_min / math.cos(ang_pres_phi_rad)
forca_res_w_max   = forca_tang_wt_max / math.cos(ang_pres_phi_rad)


# ---------------------#
# fator geometrico de resis flex pinhao / eng
# interlpolado da tabela 1 slide 10 parte 2
fator_geo_resist_flex_Jp = 0.27  
fator_geo_resist_flex_Jg = 0.28

# ---------------------#
# Fator Dinamico Kv S.I.(para 6 < Qv < 11)
B                   = ((12 - indice_qualidade_Qv) ** (2/3)) / 4  
A                   = 50 + 56 * (1 - B)
fator_dinamico_kv_min   = (A / ( A + (200 * velocidade_tang_v_t_max) ** 0.5)) ** B
fator_dinamico_kv_max   = (A / ( A + (200 * velocidade_tang_v_t_max) ** 0.5)) ** B

# ---------------------#
# fator de aplicacao k_a
# -> choques moderados na maquina movida
# -> uniforme na maquina motoraa 

fator_aplicacao_k_a = 1.50

#---------------------#
# Fato de distribuicao de carga
# para largura de face <2 in
fator_distrib_k_m   = 1.6

# ---------------------#
# Fator de tamanho
# considerando o tamanho do dente como a soma do dedendo e adendo
# 7.75mm, consideraremos 1.25
fator_tamanho_k_s   = 1.25

# ---------------------#
# Fator de espessura da borda
# fator utilizado para engrenagens vazadas
fator_esp_borda_k_b = 1.0

# Fator IDLER (engrenagens intermediarias)
# 1.42 para engrenagens intermediarias
# 1.0 para engrenagens fixas
fator_idler_k_i     = 1.0


# Fator de acabamento superficial
# sem padroes pela AGMA
fator_acab_supf_c_f = 1.0

# Coeficiente elástico
# dada a tabela 4 no slide 24 na aula 2
# 
# VERIFICAR O USO DO V=0.27
coef_elastico_c_p_Mpa = 191


# Fator geométrico I
# considerando as equacoes de par externo
# verificar resultados
raio_curvatura_pinhao_p_p = ((((raio_prim_p1_m + (1 / paso_diam_pd_1))**2)-((raio_prim_p1_m * math.cos(ang_pres_phi_rad)) ** 2)) ** (1/2)) - (math.pi / paso_diam_pd_1) * math.cos(ang_pres_phi_rad)
raio_curvatura_engren_p_g = dist_centros_C * math.sin(ang_pres_phi_rad) - raio_curvatura_pinhao_p_p
fator_geometria_sup_I     = math.cos(ang_pres_phi_rad)/(((1 / raio_curvatura_pinhao_p_p) + (1 / raio_curvatura_engren_p_g)) * diam_prim_dp_p1_mm)


# Tensão de flexão no dente do pinhão


# Tensão de flexão no dente da engrenagem


# Tensão superficial do par
tensao_contato_sigma_c = coef_elastico_c_p_Mpa * (((forca_tang_wt_max * fator_aplicacao_k_a * fator_distrib_k_m * fator_tamanho_k_s * fator_acab_supf_c_f) / (largura_de_face_F_mm * 1000 * fator_geometria_sup_I * diam_prim_dp_p1_mm * 1000 * fator_dinamico_kv_max) ) ** 0.5)

# Número de ciclos de projeto
num_ciclos = temp_vida_anos * 365 * 24 * 60 * cnd_1_rpm_max

print("\n#-------------------------------------------------------#")
print("#--------------------Analise Dinamica-------------------#")
print("#-------------------------------------------------------#")
print("\nCarga tangencial min Wt\n", round(forca_tang_wt_min,1) , "N")
print("Carga tangencial max Wt\n", round(forca_tang_wt_max,1) , "N")
print("Fator geométrico de resistência a flexão do pinhão Jp\n", round(fator_geo_resist_flex_Jp,3) , "")
print("Fator geométrico de resistência a flexão do p Jg\n", round(fator_geo_resist_flex_Jg,3) , "")
print("Fator dinamico Kv e Cv min \n", round(fator_dinamico_kv_min,3) )
print("Fator dinamico Kv e Cv max \n", round(fator_dinamico_kv_max,3) )
print("Fator aplicacao Ka e Ca \n", fator_aplicacao_k_a)
print("Fator distribuicao de carga Km e Cm\n", fator_distrib_k_m)
print("Fator de tamanho Ks e Cs\n",fator_tamanho_k_s)
print("Fator de espessura da borda Kb\n",fator_esp_borda_k_b)
print("Fator idler Ki\n",fator_idler_k_i)
print("Fator de acabamento superficial Kf\n",fator_acab_supf_c_f)
print("Coeficiente elastico Cp\n", coef_elastico_c_p_Mpa, " Mpa")
print("Fator geometrico I\n", round(fator_geometria_sup_I,5))
print("# Tensão de flexão no dente do pinhão I\n")
print("# Tensão de flexão no dente da engrenagem I\n")
print("Tensão superficial do par sigma_c\n",tensao_contato_sigma_c , "Mpa")
print("Número de ciclos de projeto N_ciclos\n", num_ciclos/1000000,"x 10^6 ciclos")
print("# Resistência à fadiga de flexão Sfb'\n")
print("# Fator de vida I\n")
print("# Fator de temperatura Kt\n")
print("# Fator de confiabilidade\n")
print("# Resistência à fadiga de flexão corrigida Sfb\n")
print("# Resistência à fadiga de superfície Sfc'\n")
print("# Fator de vida superficial Cl\n")
print("# Fator de dureza Ch\n")
print("# Resistência à fadiga de superfície corrigida Sfc\n")
print("# Coeficiente de segurança de falha por flexao no dente do pinhao Nbp\n")
print("# Coeficiente de segurança de falha por flexão no dente da engrenagem Nbg\n")
print("# Coeficiente de segurança de falha superficial\n")
print("\n#-------------------------------------------------------#")


