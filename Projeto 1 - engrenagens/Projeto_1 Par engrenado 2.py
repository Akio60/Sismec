#   Vitor Akio Isawa
#   Projeto 1 - Sistemas Mecânicos - Dimensionamento de engrenagens
#       
#   Analise do segundo par engrenado
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

#Par engrenado 2--------------------------#
# Dados do projeto

material           = 'aco'
pot_Hp             = 5
cnd_2_rpm_min_movido      = 700
cnd_2_rpm_max_movido      = 700
cnd_2_rads_min_movido     = rpm2rad(cnd_2_rpm_min_movido)
cnd_2_rads_max_movido     = rpm2rad(cnd_2_rpm_max_movido)
ang_pres_phi       = 20
ang_pres_phi_rad   = angle2rad(ang_pres_phi)
modulo_mm          = 3
num_dent_n_g1      = 60
num_dent_n_p2      = 43 
E_Gpa              = 190
v                  = 0.27
grau_AGMA          = 1
dureza_final_HB    = 350
temp_vida_anos     = 5
temp_operacao_C    = 121
confiabilidade     = 90     # %
dist_centros_C_mm  = 162.0
dist_centros_C_pol = mm2pol(dist_centros_C_mm)

#---------------desenvovilmento geometrico--------------#

#Par engrenado 2--------------------------#
# a partir da razao de velocidades mv na condicao 1
diam_prim_dp_p_mm   =  num_dent_n_p2 * modulo_mm
diam_prim_dp_p_pol  = mm2pol(diam_prim_dp_p_mm)
diam_prim_dp_g_mm   = 2 * ( dist_centros_C_mm -  (diam_prim_dp_p_mm / 2) )  
diam_prim_dp_g_pol  = mm2pol(diam_prim_dp_g_mm)
diam_prim_dp_g_m    = diam_prim_dp_g_mm / 1000

#Par engrenado 2--------------------------#
paso_diam_pd        = num_dent_n_p2 / diam_prim_dp_p_pol

#Par engrenado 2--------------------------#
num_dent_n_g2       = paso_diam_pd * diam_prim_dp_g_pol

#Par engrenado 2--------------------------#
razao_engr_mg_1     = num_dent_n_g2 / num_dent_n_p2
razao_vel_m_v2      = 1 / razao_engr_mg_1

#Par engrenado 2--------------------------#
cnd_2_rpm_max_motor  = cnd_2_rpm_max_movido  / razao_vel_m_v2
cnd_2_rads_max_motor = cnd_2_rads_max_movido / razao_vel_m_v2 

#Par engrenado 2--------------------------#
# Dados da tabela do slide 17 do arquivo ENGRENAGENS CILINDRICAS DE DENTES RETOS - Parte 1.pdf

adendo_a1_pol         = 1.000 / paso_diam_pd
dedendo_b1_pol        = 1.250 / paso_diam_pd
prof_trab_1_pol       = 2.000 / paso_diam_pd
pro_total_1_pol       = 2.250 / paso_diam_pd
esp_circ_ref_1_pol    = 1.571 / paso_diam_pd
raio_arred_1_pol      = 0.300 / paso_diam_pd 
folg_min_c1_pol       = 0.250 / paso_diam_pd
larg_min_topo_1_pol   = 0.250 / paso_diam_pd

# conversao para mm
adendo_a1_mm         = pol2mm(adendo_a1_pol)
dedendo_b1_mm        = pol2mm(dedendo_b1_pol)
prof_trab_1_mm       = pol2mm(prof_trab_1_pol)
pro_total_1_mm       = pol2mm(pro_total_1_pol)
esp_circ_ref_1_mm    = pol2mm(esp_circ_ref_1_pol)
raio_arred_1_mm      = pol2mm(raio_arred_1_pol) 
folg_min_c1_mm       = pol2mm(folg_min_c1_pol)
larg_min_topo_1_mm   = pol2mm(larg_min_topo_1_pol)

#Par engrenado 2--------------------------#
diam_ext_de_p1_mm = diam_prim_dp_p_mm + 2 * adendo_a1_mm
diam_ext_de_g1_mm = diam_prim_dp_g_mm + 2 * adendo_a1_mm

#Par engrenado 2--------------------------#
raio_prim_p1_mm   = diam_prim_dp_p_mm / 2
raio_prim_p1_m    = raio_prim_p1_mm / 1000   # conversao para m
raio_prim_p1_ft   = m2ft(raio_prim_p1_m)
raio_prim_p1_pol  = mm2pol(raio_prim_p1_mm)

#Par engrenado 2--------------------------#
raio_prim_g1_mm   = diam_prim_dp_g_mm / 2
raio_prim_g1_ft   = mm2ft(raio_prim_g1_mm)

#Par engrenado 2--------------------------#
z_1               = (raio_prim_p1_mm + adendo_a1_mm) ** 2 - (raio_prim_p1_mm * math.cos(ang_pres_phi_rad)) ** 2
z_2               = (raio_prim_g1_mm + adendo_a1_mm) ** 2 - (raio_prim_g1_mm * math.cos(ang_pres_phi_rad)) ** 2 
linha_acao_Z      = (z_1 ** 0.5) + (z_2 ** 0.5) - dist_centros_C_mm * math.sin(ang_pres_phi_rad)

#Par engrenado 2--------------------------#
paso_circ_pc      = math.pi * diam_prim_dp_g_mm / num_dent_n_g1

#Par engrenado 2--------------------------#
paso_base_pb      = paso_circ_pc * math.cos(ang_pres_phi_rad)

#Par engrenado 2--------------------------#
razao_contato_mp  = linha_acao_Z / paso_base_pb

#Par engrenado 2--------------------------#
velocidade_tang_v_t_max_ft_min = 2 * math.pi * cnd_2_rpm_max_movido * raio_prim_g1_ft
velocidade_tang_v_t_min_ft_min = 2 * math.pi * cnd_2_rpm_min_movido * raio_prim_g1_ft
velocidade_tang_v_t_max_ms     = ftmin2ms(velocidade_tang_v_t_max_ft_min)

#Par engrenado 2--------------------------#
#considerando uma proximidade de ambas velocidades tang
# a partir da tabela _ do slide _ aula _
indice_qualidade_Qv            = 9

#Par engrenado 2--------------------------#
# dado : largura da face pode estar entre 8/pd e 16/pd
# utilizaremos a media
largura_de_face_F_pol          = 8/ paso_diam_pd
largura_de_face_F_mm           = pol2mm(largura_de_face_F_pol)
largura_de_face_F_m            = largura_de_face_F_mm / 1000

#--------------------Analise Dinamica-------------------#

#Par engrenado 2--------------------------#
# Note que o torque e inversamente proporcional a velocidade de rotacao
pot_W             = hp2W(pot_Hp)
torque_t          = pot_W / cnd_2_rads_max_motor
forca_tang_wt_min = torque_t / raio_prim_p1_m
forca_tang_wt_max = torque_t / raio_prim_p1_m
forca_tang_wt_max_lb        = N2lb (forca_tang_wt_max)

#Par engrenado 2--------------------------#
forca_res_w_min   = forca_tang_wt_min / math.cos(ang_pres_phi_rad)
forca_res_w_max   = forca_tang_wt_max / math.cos(ang_pres_phi_rad)

#Par engrenado 2--------------------------#
# Número de ciclos de projeto
num_ciclos        = temp_vida_anos * 365 * 24 * 60 * cnd_2_rpm_max_movido

#Par engrenado 2--------------------------#
# fator geometrico de resis flex pinhao / eng
# interlpolado da tabela 1 slide 10 parte 2 ,HSPTC p 43, g 65
# interpolando os dados da tabela (aprox.)
fator_geometrico_resist_flex_Jp = 0.415  
fator_geometrico_resist_flex_Jg = 0.43

#Par engrenado 2--------------------------#
# Fator Dinamico Kv S.I.(para 6 < Qv < 11)
B                       = ((12 - indice_qualidade_Qv) ** (2/3)) / 4  
A                       = 50 + (56 * (1 - B))
v_t_max = (A + (indice_qualidade_Qv - 3) ** 2)/200
fator_dinamico_kv_min   = (A / ( A + ((200 * v_t_max) ** 0.5))) ** B
fator_dinamico_kv_max   = (A / ( A + ((200 * velocidade_tang_v_t_max_ms) ** 0.5))) ** B

#Par engrenado 2--------------------------#
# fator de aplicacao k_a
# -> choques moderados na maquina movida
# -> uniforme na maquina motoraa 
fator_aplicacao_k_a     = 1.25

#Par engrenado 2--------------------------#
# Fato de distribuicao de carga
# para largura de face <2 in
fator_distribuicao_carga_k_m   = 1.6

#Par engrenado 2--------------------------#
# Fator de tamanho
# considerando o tamanho do dente como a soma do dedendo e adendo
# 7.75mm, consideraremos 1.25
fator_tamanho_k_s       = 1.0

#Par engrenado 2--------------------------#
# Fator de espessura da borda
# fator utilizado para engrenagens vazadas
fator_espessura_borda_k_b = 1.0

#Par engrenado 2--------------------------#
# Fator IDLER (engrenagens intermediarias)
# 1.42 para engrenagens intermediarias
# 1.0 para engrenagens fixas
fator_idler_k_i         = 1.0

#Par engrenado 2--------------------------#
# Fator de acabamento superficial
# sem padroes pela AGMA
fator_acabamento_superficie_c_f = 1.0

#Par engrenado 2--------------------------#
# Coeficiente elástico
# dada a tabela 4 no slide 24 na aula 2
# 
# VERIFICAR O USO DO V=0.27
E_Mpa = E_Gpa * 1000
coef_elastico_c_p_Mpa   = (1/(math.pi * (( (1 - ( v**2 ) ) / E_Mpa)+( (1 - ( v**2 ) ) / E_Mpa)))) ** 0.5
coef_elastico_c_p_pa    = coef_elastico_c_p_Mpa * 1000_000

#Par engrenado 2--------------------------#
# Fator geométrico I
# considerando as equacoes de par externo
# verificar resultados
raio_curvatura_pinhao_p_p_pol = ((((raio_prim_p1_pol + (1 / paso_diam_pd))**2)-((raio_prim_p1_pol * math.cos(ang_pres_phi_rad)) ** 2)) ** (1/2)) - (math.pi / paso_diam_pd) * math.cos(ang_pres_phi_rad)
raio_curvatura_engren_p_g_pol = dist_centros_C_pol * math.sin(ang_pres_phi_rad) - raio_curvatura_pinhao_p_p_pol
fator_geometria_sup_I   = math.cos(ang_pres_phi_rad)/(((1 / raio_curvatura_pinhao_p_p_pol) + (1 / raio_curvatura_engren_p_g_pol)) * diam_prim_dp_p_pol)

#Par engrenado 2--------------------------#
# Fator de vida KL         - parte superior da sombreada
# Verificar a figura 12 da parte 3 da aula de engrenagens
# utilizei uma aproximacao para 1.5 x 10^9 ciclos
fator_vida_k_L          = 1.3558 * (num_ciclos ** (-0.0178))

#Par engrenado 2--------------------------#
# Fator de temperatura k_t
# como a temperatura de 121 C é o limite ( 250F) pode se utilizar 1
fator_temperatura_k_t   = 1

#Par engrenado 2--------------------------#
# Fator de confiabilidade k_r
# para 90% de confiabilidade, usando a tabela 7 da aula 3 de engrenagens
fator_confiabilidade_k_r= 0.85

#Par engrenado 2--------------------------#
fator_temperatura_c_t       = fator_temperatura_k_t

#Par engrenado 2--------------------------#
fator_confiabilidade_c_r    = fator_confiabilidade_k_r

#Par engrenado 2--------------------------#
# fator de vida cl   - usar limite superior da borda 10 ^9 ciclos
# foi pensado utilizando os dados da tabela 14 da aula 3 de engrenagens
fator_vida_c_L              = 1.4488 * (num_ciclos ** (-0.023))

#Par engrenado 2--------------------------#
# fator de dureza ch
# sabendo que ambas engrenagens possuem o mesmo material
# a razao entre as durezas sempre será 1, resultando em :
faotr_dureza_c_h            = 1

#Par engrenado 2--------------------------#
# Tensao de superficie nos dentes da engrenagem
tensao_contato_sigma_c              = coef_elastico_c_p_Mpa * ((forca_tang_wt_max * fator_aplicacao_k_a * fator_distribuicao_carga_k_m * fator_tamanho_k_s *fator_acabamento_superficie_c_f / (largura_de_face_F_mm * fator_geometria_sup_I * diam_prim_dp_g_mm * fator_dinamico_kv_max) ) **0.5)

#Par engrenado 2--------------------------#
# Tensão de flexão no dente do engrenagem
tensao_flexao_engrenagem_sigma_b    = forca_tang_wt_max * fator_aplicacao_k_a * fator_distribuicao_carga_k_m * fator_tamanho_k_s * fator_espessura_borda_k_b * fator_idler_k_i / ( largura_de_face_F_mm * modulo_mm * fator_geometrico_resist_flex_Jg * fator_dinamico_kv_max)

#Par engrenado 2--------------------------#
# Tensão de flexão no dente do pinhao
tensao_flexao_pinhao_sigma_b        = forca_tang_wt_max * fator_aplicacao_k_a * fator_distribuicao_carga_k_m * fator_tamanho_k_s * fator_espessura_borda_k_b * fator_idler_k_i / ( largura_de_face_F_mm * modulo_mm * fator_geometrico_resist_flex_Jp * fator_dinamico_kv_max)

#Par engrenado 2--------------------------#
# Resistência à fadiga de flexão Sfb'
# Equacao dada para grau 1 AGMA conforme o slide 8 da aula 3 de engrenagens
resistencia_fadiga_flexao_Sfb_dot_psi       = -274 + 167 * dureza_final_HB - (0.152 * (dureza_final_HB ** 2))
resistencia_fadiga_flexao_Sfb_dot_mpa       = psi2Mpa(resistencia_fadiga_flexao_Sfb_dot_psi)

#Par engrenado 2--------------------------#
# Resistência à fadiga de flexão corrigida Sfb
# equacao do slide 3 da aula de engrenagens pt 3
resistencia_fadiga_flexao_Sfb_mpa           = resistencia_fadiga_flexao_Sfb_dot_mpa * fator_vida_k_L / (fator_temperatura_k_t * fator_confiabilidade_k_r)
resistencia_fadiga_flexao_Sfb_psi           = Mpa2psi(resistencia_fadiga_flexao_Sfb_mpa)

#Par engrenado 2--------------------------#
# Resistencia a fadiga de superficie
# utilizaremos o grafico referente ao grau 1 da agma 
# dado na figura 15 do slide 3 da aula de engrenagens
# equacao com HB da resultado em psi
resistencia_fadiga_superficie_Sfc_dot_psi   = 26_000 + 327 * dureza_final_HB
resistencia_fadiga_superficie_Sfc_dot_mpa   = psi2Mpa(resistencia_fadiga_superficie_Sfc_dot_psi)

#Par engrenado 2--------------------------#
# utilizando os fatores de correcao
resistencia_fadiga_superficie_Sfc_mpa       = resistencia_fadiga_superficie_Sfc_dot_mpa * fator_vida_c_L * faotr_dureza_c_h / ( fator_temperatura_c_t * fator_confiabilidade_c_r)
resistencia_fadiga_superficie_Sfc_psi       = Mpa2psi(resistencia_fadiga_superficie_Sfc_mpa)


print("#-------------------------------------------------------#")
print("#--------------Dimensionamento geometrico---------------#")
print("#-------------------------------------------------------#")
print("\nRazao engrenamento mg\n",                  round(razao_engr_mg_1,3) , "")
print("Passo diametral pd 1\n",                     round(paso_diam_pd,3) , "     dentes / pol")
print("Diametro primitivo da coroa dpg 1\n",        round(diam_prim_dp_g_mm,3) , "     mm")
print("Adendo  a 1\n",                              round(adendo_a1_mm,3) , "     mm")
print("Dedendo b 1\n",                              round(dedendo_b1_mm,3) , "     mm")
print("Folga min na raiz do dente c 1\n",           round(folg_min_c1_mm,3) , "     mm")
print("Numero dentes pinhao np 1\n",                round(num_dent_n_p2,0) , "     dentes")
print("Numero dentes coroa ng 1\n",                 round(num_dent_n_g2,0) , "     dentes")
print("Diametro primitivo pinhao dpp 1\n",          round(diam_prim_dp_p_mm,3) , "     mm")  
print("Diametro externo do pinhao dep 1\n",         diam_ext_de_p1_mm, "     mm")
print("Diametro externo do pinhao deg 1\n",         diam_ext_de_g1_mm, "     mm")
print("Distancia entre centros C\n",                dist_centros_C_mm, "     mm")
print("Comprimento da linha de acao Z\n",           round(linha_acao_Z,3), "     mm")
print("Razao de contato mp [DEVE SER 1 < mp < 2 ] \n",round(razao_contato_mp,3), "")
print("indice de qualidade Q_v\n",                  indice_qualidade_Qv)
print("Largura de face F  \n",                      round(largura_de_face_F_mm,3), "     mm")
print("Velocidade tangencial  \n",                  round(velocidade_tang_v_t_max_ms,3), "     m/s")



print("\n#-------------------------------------------------------#")
print("#--------------------Analise Dinamica-------------------#")
print("#-------------------------------------------------------#")
print("\nNúmero de ciclos de projeto N_ciclos\n",                   round( num_ciclos/1_000_000_000,3) ,"     x 10^9 ciclos")
print("Carga tangencial min Wt\n",                                  round(forca_tang_wt_min,1) , "      N")
print("Carga tangencial max Wt\n",                                  round(forca_tang_wt_max,1) , "     N")
print("Fator geométrico de resistência a flexão do pinhão Jp\n",    round(fator_geometrico_resist_flex_Jp,3) , "")
print("Fator geométrico de resistência a flexão do p Jg\n",         round(fator_geometrico_resist_flex_Jg,3) , "")
print("Fator dinamico Kv e Cv \n",                                  round(fator_dinamico_kv_max,3) )
print("Fator aplicacao Ka e Ca \n",                                 fator_aplicacao_k_a)
print("Fator distribuicao de carga Km e Cm\n",                      fator_distribuicao_carga_k_m)
print("Fator de tamanho Ks e Cs\n",                                 fator_tamanho_k_s)
print("Fator de espessura da borda Kb\n",                           fator_espessura_borda_k_b)
print("Fator idler Ki\n",                                           fator_idler_k_i)
print("Fator de acabamento superficial Kf\n",                       fator_acabamento_superficie_c_f)
print("Fator geometrico I\n",                                       round(fator_geometria_sup_I,5))
print("Fator de vida kl\n",                                         round(fator_vida_k_L,2))
print("Fator de vida superficial Cl\n",                             round(fator_vida_c_L,2))
print("Fator de temperatura Kt\n",                                  fator_temperatura_k_t)
print("Fator de confiabilidade\n",                                  fator_confiabilidade_k_r)
print("Fator de dureza Ch\n",                                       faotr_dureza_c_h)
print("Coeficiente elastico Cp\n",                                  round(coef_elastico_c_p_Mpa,2), "     [Mpa]^0.5")
print("\n#-------------------------------------------------------#")
print("Tensão superficial do par sigma_c\n",                        round(tensao_contato_sigma_c,2) , "     Mpa")
print("Tensão de flexão no dente do pinhão I\n",                    round(tensao_flexao_pinhao_sigma_b,2) , "     Mpa")
print("Tensão de flexão no dente da engrenagem I\n",                round(tensao_flexao_engrenagem_sigma_b,2) , "     Mpa")
print("\n#-------------------------------------------------------#")
print("Resistência à fadiga de flexão Sfb'\n",                      round(resistencia_fadiga_flexao_Sfb_dot_mpa,2) , "     Mpa" )
print("Resistência à fadiga de flexão corrigida Sfb\n",             round(resistencia_fadiga_flexao_Sfb_mpa,2) , "     Mpa"  )
print("Resistência à fadiga de superfície Sfc'\n",                  round(resistencia_fadiga_superficie_Sfc_dot_mpa,2) , "     Mpa" )
print("Resistência à fadiga de superfície corrigida Sfc\n",         round(resistencia_fadiga_superficie_Sfc_mpa,2) , "     Mpa" )
print("\n#-------------------------------------------------------#")
print("Coeficiente de segurança de falha por flexao no dente do pinhao Nbp\n"     , round(resistencia_fadiga_flexao_Sfb_mpa / tensao_flexao_pinhao_sigma_b,2)      )
print("Coeficiente de segurança de falha por flexão no dente da engrenagem Nbg\n" , round(resistencia_fadiga_flexao_Sfb_mpa / tensao_flexao_engrenagem_sigma_b ,2) )
print("Coeficiente de segurança de falha superficial\n"                           , round(resistencia_fadiga_superficie_Sfc_mpa / tensao_contato_sigma_c,2)        )
print("\n#-------------------------------------------------------#",    )
