#   Dados do enunciado

potencia_motor_1_HP     = 5
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

# caracteristicas do material do eixo
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