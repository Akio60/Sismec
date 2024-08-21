# Dados do sistema dado
# cnd -> condicao 1 : pinhao 1 e coroa 1
# cnd -> condicao 2 : pinhao 2 e coroa 2

pot_Hp             = 5
cnd_1_rpm_min      = 500
cnd_1_rpm_min      = 600
cnd_2_rpm          = 100
ang_pres_phi       = 20
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

#   Determinar a distancia entre centros dos pares engrenados, visando manter o paralelismo entre os pares

# a partir da razao de velocidades mv na condicao 1

razao_engr_mg_1   = 1 / razao_vel_m_v1
num_dent_n_p1     = num_dent_n_g1 / razao_engr_mg_1

diam_prim_dp_g1   = mod_gears_mm * num_dent_n_g1
paso_diam_pd_1    = num_dent_n_g1 / diam_prim_dp_g1

diam_prim_dp_p1   = diam_prim_dp_g1 * razao_vel_m_v1
diam_prim_dp_p1_dot   = num_dent_n_p1 / paso_diam_pd_1

adendo_a1         = 1.000 / paso_diam_pd_1
dedendo_b1        = 1.250 / paso_diam_pd_1
prof_trab_1       = 2.000 / paso_diam_pd_1
pro_total_1       = 2.250 / paso_diam_pd_1
esp_circ_ref_1    = 1.571 / paso_diam_pd_1
raio_arred_1      = 0.300 / paso_diam_pd_1 
folg_min_1        = 0.250 / paso_diam_pd_1
larg_min_topo_1   = 0.350 / paso_diam_pd_1