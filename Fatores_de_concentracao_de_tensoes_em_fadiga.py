# Falta fazer o de confiabilidade


#   tipo de carregamento
def definir_fator_Kc(tipo_de_carregamento):
    match tipo_de_carregamento:
        case '1': #   Flexao alternada
            return 1.0
        case '2': #   Carga Axial
            return 0.7
        case _: #   Casos excedentes
            return "ERROR"

#   tamanho da peca (em mm)
def definir_fator_Ks(tamanho):
    tamanho = int (tamanho)
    if 0 < tamanho < 8:
        return 1.0
    elif 8 < tamanho < 250:
        return 1.189 * tamanho ** (-0.097)
    else:
        return "ERROR"
    
#   temperatura em Celsius
def definir_fator_Kt(temperatura):
    temperatura = int (temperatura)
    if 0 < temperatura < 450:
        return 1.0
    elif 450 < temperatura < 550:
        return 1-0.0058*(temperatura - 450)
    else:
        return "ERROR"

#   superficie  (Valores definidos para Mpa)
def definir_fator_Ksup(superficie, S_ut):
    match superficie:
        case '1': #   Polimento fino comercial
            A = 1.58
            b = -0.085
        case '2': #   Usinado ou estampado a frio
            A = 4.51
            b = -0.265
        case '3': #   Rolado a quente
            A = 57.7
            b = -0.718
        case '4': #   Forjado
            A = 272
            b = -0.995
        case _: #   Casos extras
            return "ERROR"
    C_sup = A*(int(S_ut)**b) 
    if C_sup > 1:
        return 1
    else:
        return C_sup  # Saida em Mpa

#confiabilidade
def definir_fator_Kconf(confiabilidade):
    confiabilidade = int (confiabilidade)
    return 0.0

print("-------------------------------------")
tipo_de_carregamento    = input("insira o tipo de carregamento\n 1-Flexao alternada  \n 2-Carga Axial\n")
print("-------------------------------------")
tamanho                 = input("insira o tamanho em mm (verificar caso dado esteja em in)\n")
print("-------------------------------------")
temperatura             = input("insira a temperatura de operacao em C\n")
print("-------------------------------------")
superficie              = input("insira o tipo de superficie\n 1-Polimento\n 2-Usinado\n 3-Rolado\n 4-Forjado\n")
S_ut                    = input("insira a S_ut em MPa\n")
print("-------------------------------------")
confiabilidade          = input("insira o valor da confiabilidade em %\n")
print("-------------------------------------")

C_carga = definir_fator_Kc(tipo_de_carregamento)
C_tam   = definir_fator_Ks(tamanho)
C_temp  = definir_fator_Kt(temperatura)
C_sup   = definir_fator_Ksup(superficie,S_ut)
C_conf  = definir_fator_Kconf(confiabilidade)

print("C_carga =",C_carga)
print("C_tam =",C_tam)
print("C_temp =",C_temp)
print("C_sup =",C_sup)
print("C_conf =",C_conf)