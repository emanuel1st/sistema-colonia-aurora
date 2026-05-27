# =========================================================
# SISTEMA INTELIGENTE DA COLÔNIA ESPACIAL
# =========================================================

import random
import time

# =========================================================
# FUNÇÕES
# =========================================================

def carregando():
    print("\nCarregando sistema", end="")

    for i in range(5):
        print(".", end="")
        time.sleep(0.5)

    print("\n")


def pausar():
    input("\nPressione ENTER para continuar...")


# =========================================================
# DADOS DA COLÔNIA
# =========================================================

energia_solar = random.randint(20, 80)
energia_eolica = random.randint(10, 50)
energia_reserva = random.randint(10, 100)

temperatura = random.randint(-20, 35)
vento = random.randint(5, 20)
umidade = random.randint(10, 90)

consumo_suporte = random.randint(20, 40)
consumo_lab = random.randint(10, 30)
consumo_comunicacao = random.randint(5, 20)
consumo_secundarios = random.randint(5, 25)

# =========================================================
# CÁLCULOS
# =========================================================

energia_total = (
    energia_solar +
    energia_eolica +
    energia_reserva
)

consumo_total = (
    consumo_suporte +
    consumo_lab +
    consumo_comunicacao +
    consumo_secundarios
)

# =========================================================
# TELA INICIAL
# =========================================================

print("=" * 55)
print("BEM-VINDO AO SISTEMA INTELIGENTE DA COLÔNIA")
print("=" * 55)

input("\nPressione ENTER para iniciar...")

carregando()

# =========================================================
# MENU
# =========================================================

while True:

    print("\n========== MENU PRINCIPAL ==========")
    print("1 - Energia")
    print("2 - Clima")
    print("3 - Consumo")
    print("4 - Análise Energética")
    print("5 - Decisão Automática")
    print("6 - Previsão de Energia Eólica")
    print("0 - Encerrar Sistema")

    opcao = input("\nDeseja saber o status de qual informação
                  ? ")

    # =====================================================
    # STATUS ENERGIA
    # =====================================================

    if opcao == "1":

        print("\n========== STATUS ENERGÉTICO ==========")

        print("Energia Solar:", energia_solar)
        print("Energia Eólica:", energia_eolica)
        print("Reserva de Energia:", energia_reserva)
        print("Energia Total:", energia_total)

        if energia_total < 50:
            print("ALERTA: energia crítica!")

        elif energia_total < 100:
            print("Nível moderado de energia.")

        else:
            print("Energia em nível excelente.")

        pausar()

    # =====================================================
    # STATUS CLIMA
    # =====================================================

    elif opcao == "2":

        print("\n========== STATUS CLIMÁTICO ==========")

        print("Temperatura:", temperatura, "°C")
        print("Velocidade do vento:", vento, "km/h")
        print("Umidade:", umidade, "%")

        if temperatura < -10:
            print("ALERTA: temperatura extremamente baixa!")

        elif temperatura > 30:
            print("ALERTA: temperatura muito alta!")

        else:
            print("Temperatura dentro dos padrões.")

        pausar()

    # =====================================================
    # STATUS CONSUMO
    # =====================================================

    elif opcao == "3":

        print("\n========== CONSUMO DA COLÔNIA ==========")

        print("Suporte à Vida:", consumo_suporte)
        print("Laboratório:", consumo_lab)
        print("Comunicação:", consumo_comunicacao)
        print("Sistemas Secundários:", consumo_secundarios)

        print("\nConsumo Total:", consumo_total)

        if consumo_total > 90:
            print("ALERTA: consumo muito elevado!")

        elif consumo_total < 50:
            print("Consumo controlado.")

        else:
            print("Consumo moderado.")

        pausar()

    # =====================================================
    # ANÁLISE ENERGÉTICA
    # =====================================================

    elif opcao == "4":

        print("\n========== ANÁLISE DE ENERGIA ==========")

        print("Energia Total:", energia_total)
        print("Consumo Total:", consumo_total)

        if consumo_total > energia_total:
            print("ALERTA: consumo maior que geração!")
            print("Modo economia ativado.")

        elif energia_total > consumo_total + 40:
            print("SUGESTÃO: armazenar energia excedente.")

        else:
            print("Sistema energético estável.")

        pausar()

    # =====================================================
    # DECISÃO AUTOMÁTICA
    # =====================================================

    elif opcao == "5":

        print("\n========== DECISÃO AUTOMÁTICA ==========")

        if energia_total < 50 and consumo_total > 70:

            print("AÇÃO: desligar sistemas secundários.")
            print("AÇÃO: manter apenas suporte à vida.")

        elif energia_total < 80:

            print("AÇÃO: reduzir consumo da base.")

        elif energia_total > 120:

            print("AÇÃO: armazenar energia excedente.")

        else:

            print("AÇÃO: sistema operando normalmente.")

        pausar()

    # =====================================================
    # PREVISÃO
    # =====================================================

    elif opcao == "6":

        print("\n========== PREVISÃO DE ENERGIA ==========")

        previsao = 2.5 * vento

        print("Velocidade atual do vento:", vento, "km/h")
        print("Previsão de energia eólica:", round(previsao, 1))

        if previsao < 25:
            print("Baixa geração eólica prevista.")

        elif previsao < 40:
            print("Geração moderada prevista.")

        else:
            print("Excelente geração eólica prevista.")

        pausar()

    # =====================================================
    # ENCERRAR
    # =====================================================

    elif opcao == "0":

        print("\nEncerrando sistema da colônia...")
        break

    # =====================================================
    # ERRO
    # =====================================================

    else:

        print("\nOpção inválida!")