# Dados do sistema dado
# cnd -> condicao 1 : pinhao 1 e coroa 1
# cnd -> condicao 2 : pinhao 2 e coroa 2

potencia_Hp        = 5
cnd_1_rpm_min      = 500
cnd_1_rpm_min      = 600
cnd_2_rpm          = 100
angulo_pressao_phi = 20
modulo_coroas_mm   = 3
num_dentes_coroa_1 = 60
num_dentes_pinhao_2= 43 

material           = 'aco'
lim_res_fadg_Se_Mpa= 700    #dado do slide de teoria de dalha por fadiga
lim_res_fadg_Sut_Mpa= lim_res_fadg_Se_Mpa / 0.5
E_Gpa              = 190
v                  = 0.27
grau_AGMA          = 1
dureza_final_HB    = 350
tempo_vida_anos    = 5
temp_operacao_C    = 121
confiabilidade     = 90     # %
razao_vel_par_1_m_v= 0.8

#   Determinar a distancia entre centros dos pares engrenados, visando manter o paralelismo entre os pares

# a partir da razao de velocidades mv na condicao 1

razao_engr_m_g = razao_vel_par_1_m_v