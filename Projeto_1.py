#   Vitor Akio Isawa
#   Projeto 1 - Sistemas Mecânicos - Dimensionamento de engrenagens
#       
#       Dimensionamento geométrico
#       Analise dinamica
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

#-------------------------------------------------------#
# Dados do projeto
# cnd -> condicao 1 : pinhao 1 e coroa 1
# cnd -> condicao 2 : pinhao 2 e coroa 2

material           = 'aco'
pot_Hp             = 5
cnd_1_rpm_min      = 500
cnd_1_rpm_max      = 600
cnd_1_rads_min     = rpm2rad(cnd_1_rpm_min)
cnd_1_rads_max     = rpm2rad(cnd_1_rpm_max)
cnd_2_rpm          = 1000
ang_pres_phi       = 20
ang_pres_phi_rad   = angle2rad(ang_pres_phi)
modulo_mm          = 3
num_dent_n_g1      = 60
num_dent_n_p2      = 43 
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
#
#---------------desenvovilmento geometrico--------------#
#
#-------------------------------------------------------#

# a partir da razao de velocidades mv na condicao 1
razao_engr_mg_1   = 1 / razao_vel_m_v1
num_dent_n_p1     = num_dent_n_g1 / razao_engr_mg_1

# A unidade de saida do passo diametral deve ser em num_dentes/pol
# a fim de facilitar as especificacoes de engrenagens
diam_prim_dp_g1_mm  = modulo_mm * num_dent_n_g1
diam_prim_dp_g1_pol = mm2pol(diam_prim_dp_g1_mm)

diam_prim_dp_p1_pol = diam_prim_dp_g1_pol * razao_vel_m_v1
diam_prim_dp_p1_mm  = pol2mm(diam_prim_dp_p1_pol)

paso_diam_pd_1      = num_dent_n_g1 / diam_prim_dp_g1_pol

#-------------------------------------------------------#
# Dados da tabela do slide 17 do arquivo ENGRENAGENS CILINDRICAS DE DENTES RETOS - Parte 1.pdf

adendo_a1_pol         = 1.000 / paso_diam_pd_1
dedendo_b1_pol        = 1.250 / paso_diam_pd_1
prof_trab_1_pol       = 2.000 / paso_diam_pd_1
pro_total_1_pol       = 2.250 / paso_diam_pd_1
esp_circ_ref_1_pol    = 1.571 / paso_diam_pd_1
raio_arred_1_pol      = 0.300 / paso_diam_pd_1 
folg_min_c1_pol       = 0.250 / paso_diam_pd_1
larg_min_topo_1_pol   = 0.350 / paso_diam_pd_1

# conversao para mm
adendo_a1_mm         = pol2mm(adendo_a1_pol)
dedendo_b1_mm        = pol2mm(dedendo_b1_pol)
prof_trab_1_mm       = pol2mm(prof_trab_1_pol)
pro_total_1_mm       = pol2mm(pro_total_1_pol)
esp_circ_ref_1_mm    = pol2mm(esp_circ_ref_1_pol)
raio_arred_1_mm      = pol2mm(raio_arred_1_pol) 
folg_min_c1_mm       = pol2mm(folg_min_c1_pol)
larg_min_topo_1_mm   = pol2mm(larg_min_topo_1_pol)

#-------------------------------------------------------#
diam_ext_de_p1_mm = diam_prim_dp_p1_mm + 2 * dedendo_b1_mm
diam_ext_de_g1_mm = diam_prim_dp_g1_mm + 2 * dedendo_b1_mm

#-------------------------------------------------------#
raio_prim_p1_mm   = diam_prim_dp_p1_mm / 2
raio_prim_p1_m    = raio_prim_p1_mm / 1000   # conversao para m
raio_prim_p1_ft   = m2ft(raio_prim_p1_m)

#-------------------------------------------------------#
raio_prim_g1_mm   = diam_prim_dp_g1_mm / 2

#-------------------------------------------------------#
dist_centros_C_mm = (raio_prim_p1_mm) + (raio_prim_g1_mm)

#-------------------------------------------------------#
z_1               = (raio_prim_p1_mm + adendo_a1_mm) ** 2 - (raio_prim_p1_mm * math.cos(ang_pres_phi_rad)) ** 2
z_2               = (raio_prim_g1_mm + adendo_a1_mm) ** 2 - (raio_prim_g1_mm * math.cos(ang_pres_phi_rad)) ** 2 
linha_acao_Z      = (z_1 ** 0.5) + (z_2 ** 0.5) - dist_centros_C_mm * math.sin(ang_pres_phi_rad)

#-------------------------------------------------------#
paso_circ_pc      = math.pi * diam_prim_dp_g1_mm / num_dent_n_g1

#-------------------------------------------------------#
paso_base_pb      = paso_circ_pc * math.cos(ang_pres_phi_rad)

#-------------------------------------------------------#
razao_contato_mp  = linha_acao_Z / paso_base_pb

#-------------------------------------------------------#
velocidade_tang_v_t_max = 2 * math.pi * cnd_1_rpm_max * raio_prim_p1_ft
velocidade_tang_v_t_min = 2 * math.pi * cnd_1_rpm_min * raio_prim_p1_ft

#-------------------------------------------------------#
#considerando uma proximidade de ambas velocidades tang
# a partir da tabela _ do slide _ aula _
indice_qualidade_Qv     = 8

#-------------------------------------------------------#
# dado : largura da face pode estar entre 8/pd e 16/pd
# utilizaremos a media
largura_de_face_F_pol        = 12 / paso_diam_pd_1

#-------------------------------------------------------#
#--------------------conversao de unidades--------------#
largura_de_face_F_mm= pol2mm(largura_de_face_F_pol)
raio_prim_p1_pol    = mm2pol(raio_prim_p1_mm)
dist_centros_C_pol  = mm2pol(dist_centros_C_mm)


#-------------------------------------------------------#
#--------------------Analise Dinamica-------------------#

# Note que o torque e inversamente proporcional a velocidade de rotacao
pot_W             = hp2W(pot_Hp)
torque_t_max      = pot_W / cnd_1_rads_min
torque_t_min      = pot_W / cnd_1_rads_max
forca_tang_wt_min = torque_t_min / raio_prim_p1_m
forca_tang_wt_max = torque_t_max / raio_prim_p1_m
forca_tang_wt_max_lb        = N2lb (forca_tang_wt_max)

#----------------------#
forca_res_w_min   = forca_tang_wt_min / math.cos(ang_pres_phi_rad)
forca_res_w_max   = forca_tang_wt_max / math.cos(ang_pres_phi_rad)

#----------------------#
# Número de ciclos de projeto
num_ciclos = temp_vida_anos * 365 * 24 * 60 * cnd_1_rpm_max

# ---------------------#
# fator geometrico de resis flex pinhao / eng
# interlpolado da tabela 1 slide 10 parte 2 ,HSPTC p 48, g 60
# interpolando os dados da tabela (aprox.)
fator_geometrico_resist_flex_Jp = 0.415  
fator_geometrico_resist_flex_Jg = 0.43

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
fator_distribuicao_carga_k_m   = 1.6

# ---------------------#
# Fator de tamanho
# considerando o tamanho do dente como a soma do dedendo e adendo
# 7.75mm, consideraremos 1.25
fator_tamanho_k_s   = 1.25

# ---------------------#
# Fator de espessura da borda
# fator utilizado para engrenagens vazadas
fator_espessura_borda_k_b = 1.0

# Fator IDLER (engrenagens intermediarias)
# 1.42 para engrenagens intermediarias
# 1.0 para engrenagens fixas
fator_idler_k_i     = 1.0


# Fator de acabamento superficial
# sem padroes pela AGMA
fator_acabamento_superficie_c_f = 1.0

# Coeficiente elástico
# dada a tabela 4 no slide 24 na aula 2
# 
# VERIFICAR O USO DO V=0.27
coef_elastico_c_p_Mpa = 191


# Fator geométrico I
# considerando as equacoes de par externo
# verificar resultados
raio_curvatura_pinhao_p_p_pol = ((((raio_prim_p1_pol + (1 / paso_diam_pd_1))**2)-((raio_prim_p1_pol * math.cos(ang_pres_phi_rad)) ** 2)) ** (1/2)) - (math.pi / paso_diam_pd_1) * math.cos(ang_pres_phi_rad)
raio_curvatura_engren_p_g_pol = dist_centros_C_pol * math.sin(ang_pres_phi_rad) - raio_curvatura_pinhao_p_p_pol

fator_geometria_sup_I     = math.cos(ang_pres_phi_rad)/(((1 / raio_curvatura_pinhao_p_p_pol) + (1 / raio_curvatura_engren_p_g_pol)) * diam_prim_dp_p1_pol)

# ---------------------#
# Fator de vida KL
# Verificar a figura 12 da parte 3 da aula de engrenagens
# utilizei uma aproximacao para 1.5 x 10^9 ciclos
fator_vida_k_L          = 0.85

# ---------------------#
# Fator de temperatura k_t
# como a temperatura de 121 C é o limite ( 250F) pode se utilizar 1
fator_temperatura_k_t   = 1

# ---------------------#
# Fator de confiabilidade k_r
# para 90% de confiabilidade, usando a tabela 7 da aula 3 de engrenagens
fator_confiabilidade_k_r= 0.85

# ---------------------#
# Tensão de flexão no dente do engrenagem

# ---------------------#
# Tensão de flexão no dente do pinhao

# Tensão superficial do par
fator_lewis_x               = 2
fator_adimensional_Y        = 2 * math.pi  * fator_lewis_x / (3 * paso_circ_pc)
tensao_contato_sigma_b_mpa  = forca_tang_wt_max / (modulo_mm * largura_de_face_F_mm * fator_adimensional_Y)

# -----------------------------#
# Resistência à fadiga de flexão Sfb'
# Equacao dada para grau 1 AGMA conforme o slide 8 da aula 3 de engrenagens
resistencia_fadiga_flexao_Sfb_dot_psi = -274 + 167 * dureza_final_HB - (0.152 * (dureza_final_HB ** 2))
resistencia_fadiga_flexao_Sfb_dot_mpa = psi2Mpa(resistencia_fadiga_flexao_Sfb_dot_psi)


# -----------------------------#
# Resistência à fadiga de flexão corrigida Sfb
# equacao do slide 3 da aula de engrenagens pt 3
resistencia_fadiga_flexao_Sfb_mpa   = resistencia_fadiga_flexao_Sfb_dot_mpa * fator_vida_k_L / (fator_temperatura_k_t * fator_confiabilidade_k_r)
resistencia_fadiga_flexao_Sfb_psi   = Mpa2psi(resistencia_fadiga_flexao_Sfb_mpa)

# -----------------------------#
# Resistencia a fadiga de superficie
# -----------------------------#
# utilizaremos o grafico referente ao grau 1 da agma 
# dado na figura 15 do slide 3 da aula de engrenagens
# equacao com HB da resultado em psi
resistencia_fadiga_superficie_Sfc_dot_psi   = 26_000 + 327 * dureza_final_HB
resistencia_fadiga_superficie_Sfc_dot_mpa   = psi2Mpa(resistencia_fadiga_superficie_Sfc_dot_psi)

# -----------------------------#
fator_temperatura_c_t       = fator_temperatura_k_t

# -----------------------------#
fator_confiabilidade_c_r    = fator_confiabilidade_k_r

# -----------------------------#
# fator de vida cl
# foi pensado utilizando os dados da tabela 14 da aula 3 de engrenagens
fator_vida_c_L              = 0.85

# -----------------------------#
# fator de dureza ch
# sabendo que ambas engrenagens possuem o mesmo material
# a razao entre as durezas sempre será 1, resultando em :
faotr_dureza_c_h            = 1

# -----------------------------#
# utilizando os fatores de correcao
resistencia_fadiga_superficie_Sfc_mpa = resistencia_fadiga_superficie_Sfc_dot_mpa * fator_vida_c_L * faotr_dureza_c_h / ( fator_temperatura_c_t * fator_confiabilidade_c_r)
resistencia_fadiga_superficie_Sfc_psi = Mpa2psi(resistencia_fadiga_superficie_Sfc_mpa)





print("#-------------------------------------------------------#")
print("#--------------Dimensionamento geometrico---------------#")
print("#-------------------------------------------------------#")
print("\nRazao engrenamento mg\n",                  round(razao_engr_mg_1,3) , "")
print("Passo diametral pd 1\n",                     round(paso_diam_pd_1,3) , " dentes / pol")
print("Diametro primitivo da coroa dpg 1\n",        round(diam_prim_dp_g1_mm,3) , " mm")
print("Adendo  a 1\n",                              round(adendo_a1_mm,3) , " mm")
print("Dedendo b 1\n",                              round(dedendo_b1_mm,3) , " mm")
print("Folga min na raiz do dente c 1\n",           round(folg_min_c1_mm,3) , " mm")
print("Numero dentes pinhao np 1\n",                round(num_dent_n_p1,0) , "dentes")
print("Numero dentes coroa ng 1\n",                 round(num_dent_n_g1,0) , " dentes")
print("Diametro primitivo pinhao dpp 1\n",          round(diam_prim_dp_p1_mm,3) , " mm")  
print("Diametro externo do pinhao dep 1\n",         diam_ext_de_p1_mm, "mm")
print("Diametro externo do pinhao deg 1\n",         diam_ext_de_g1_mm, "mm")
print("Distancia entre centros C\n",                dist_centros_C_mm, "mm")
print("Comprimento da linha de acao Z\n",           round(linha_acao_Z,3), "mm")
print("Razao de contato mp [DEVE SER 1 < mp < 2 ] \n",round(razao_contato_mp,3), "")
print("indice de qualidade Q_v\n",                  indice_qualidade_Qv)
print("Largura de face F (12/pd) \n",               round(largura_de_face_F_mm,3), "mm")



print("\n#-------------------------------------------------------#")
print("#--------------------Analise Dinamica-------------------#")
print("#-------------------------------------------------------#")
print("\nCarga tangencial min Wt\n",                                round(forca_tang_wt_min,1) , "N")
print("Carga tangencial max Wt\n",                                  round(forca_tang_wt_max,1) , "N")
print("Fator geométrico de resistência a flexão do pinhão Jp\n",    round(fator_geometrico_resist_flex_Jp,3) , "")
print("Fator geométrico de resistência a flexão do p Jg\n",         round(fator_geometrico_resist_flex_Jg,3) , "")
print("Fator dinamico Kv e Cv min \n",                              round(fator_dinamico_kv_min,3) )
print("Fator dinamico Kv e Cv max \n",                              round(fator_dinamico_kv_max,3) )
print("Fator aplicacao Ka e Ca \n",                                 fator_aplicacao_k_a)
print("Fator distribuicao de carga Km e Cm\n",                      fator_distribuicao_carga_k_m)
print("Fator de tamanho Ks e Cs\n",                                 fator_tamanho_k_s)
print("Fator de espessura da borda Kb\n",                           fator_espessura_borda_k_b)
print("Fator idler Ki\n",                                           fator_idler_k_i)
print("Fator de acabamento superficial Kf\n",                       fator_acabamento_superficie_c_f)
print("Coeficiente elastico Cp\n",                                  coef_elastico_c_p_Mpa, " Mpa")
print("Fator geometrico I\n",                                       round(fator_geometria_sup_I,5))
print("Número de ciclos de projeto N_ciclos\n",                     num_ciclos/1_000_000,"x 10^6 ciclos")
print("Fator de vida kl\n",                                         fator_vida_k_L)
print("Fator de vida superficial Cl\n",                             fator_vida_c_L)
print("Fator de temperatura Kt\n",                                  fator_temperatura_k_t)
print("Fator de confiabilidade\n",                                  fator_confiabilidade_k_r)
print("Fator de dureza Ch\n",                                       faotr_dureza_c_h)
print("Tensão superficial do par sigma_c\n",                        round(tensao_contato_sigma_b_mpa,2) , "Mpa")
print("# Tensão de flexão no dente do pinhão I\n",                  )
print("# Tensão de flexão no dente da engrenagem I\n",              )
print("Resistência à fadiga de flexão Sfb'\n",                      round(resistencia_fadiga_flexao_Sfb_dot_mpa,2) , "Mpa" )
print("Resistência à fadiga de flexão corrigida Sfb\n",             round(resistencia_fadiga_flexao_Sfb_mpa,2) , "Mpa"  )
print("Resistência à fadiga de superfície Sfc'\n",                  round(resistencia_fadiga_superficie_Sfc_dot_mpa,2) , "Mpa" )
print("Resistência à fadiga de superfície corrigida Sfc\n",         round(resistencia_fadiga_superficie_Sfc_mpa,2) , "Mpa" )
print("# Coeficiente de segurança de falha por flexao no dente do pinhao Nbp\n")
print("# Coeficiente de segurança de falha por flexão no dente da engrenagem Nbg\n")
print("# Coeficiente de segurança de falha superficial\n",         )
print("\n#-------------------------------------------------------#",    )

print(num_dent_n_p1/num_dent_n_g1)

