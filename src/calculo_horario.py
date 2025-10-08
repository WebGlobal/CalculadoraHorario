###############################################################################
##           __          __  _      _____ _       _           _              ##
##           \ \        / / | |    / ____| |     | |         | |             ##
##            \ \  /\  / /__| |__ | |  __| | ___ | |__   __ _| |             ##
##             \ \/  \/ / _ \ '_ \| | |_ | |/ _ \| '_ \ / _` | |             ##
##              \  /\  /  __/ |_) | |__| | | (_) | |_) | (_| | |             ##
##               \/  \/ \___|_.__/ \_____|_|\___/|_.__/ \__,_|_|             ##
##                                                                           ##
##        Copyright (c) 2021 WebGlobal - Todos os Direitos Reservados        ##
##                                                                           ##
###############################################################################

from datetime import timedelta


class Horario():
    """
    Classe que realiza o cálculo do horário de saída,
    horas trabalhadas/horas excedidas para os dados fornecidos.

    ### Methods:
        - calcular: realiza o cálculo do horário de saída,
          horas trabalhadas/horas excedidas
        - horarioImprimir: imprime o resultado obtido na função saidaCalcular
        - saidaCalcular: realiza o cálculo dos horarios

    """

    def __init__(self, list_args: list):
        """
        Inicializa a lista de horários da classe

        ### Parameters:
            - list_args (list): lista de horários passada como argumento na
              chamada do programa
        """

        self.horas_dia = timedelta(hours=8, minutes=30)
        self.timedeltaList = []

        for arg in list_args:
            self.timedeltaList.append(timedelta(hours=int(arg[0:2]),
                                                minutes=int(arg[3:])))

        self.timedeltaList = sorted(self.timedeltaList)

    def calcular(self) -> list:
        """
        Realiza a chamada das funções saidaCalcular e horarioImprimir para
        o cálculo e impressão horário de saída,
        horas trabalhadas/horas excedidas

        ### Returns:
            list: lista com todas as mensagens geradas
        """

        total_reg, prev_saida, horas_excedidas, horas_faltantes = \
            self.saidaCalcular(self.timedeltaList)

        msgList = self.horarioImprimir(
            total_reg=total_reg,
            prev_saida=prev_saida,
            horas_excedidas=horas_excedidas,
            horas_faltantes=horas_faltantes
        )

        return msgList

    def horarioImprimir(self,
                        total_reg: object,
                        prev_saida: object,
                        horas_excedidas: object,
                        horas_faltantes: object):
        """
        Realiza a escrita na tela os valores obtidos na função saidaCalcular

        ### Parameters:
            - total_reg (datetime): total de horas já registrada
            - prev_saida (datetime): previsão de saída para o dia, considerando
              8,5 horas trabalhadas
            - horas_excedidas (datetime): total de horas que excedem as
              8,5 horas diárias, caso a carga horária tenha sido ultrapassada
            - horas_faltantes (datetime): total de horas que faltam para
              completar as 8,5 horas diárias, caso a carga horária não tenha
              sido ultrapassada
        """

        msgList = []
        print(f"Total de horas já registradas: {total_reg}")
        msgList.append(f"Total de horas já registradas: {total_reg}")
        if total_reg < self.horas_dia:
            msgList.append(f"Previsão de horário de saída: {prev_saida}")
            print(f"Previsão de horário de saída: {prev_saida}")
        else:
            msgList.append("Carga horária cumprida")
            print('Carga horária cumprida')

        if horas_excedidas:
            msgList.append(f"Total de horas excedidas: {horas_excedidas}")
            print(f"Total de horas excedidas: {horas_excedidas}")

        if horas_faltantes:
            msgList.append(f"Total de horas faltantes: {horas_faltantes}")
            print(f"Total de horas faltantes: {horas_faltantes}")

        return msgList

    def saidaCalcular(self, timedeltaList: list):
        """
        Realiza a chamada das funções saidaCalcular e horarioImprimir para
        o cálculo e impressão horário de saída,
        horas trabalhadas/horas excedidas

        ### Parameters:
            - timedeltaList (list): lista de horários passada como argumento
              na chamada do programa no formato timedelta

        ### Returns:
            list: lista com os valores cálculados para
            total_reg (total de horas já registrada),
            prev_saida (previsão de saída para o dia),
            horas_excedidas (total de horas que excedem as 8,5 horas diárias),
            horas_faltantes (total de horas que faltam para completar as 8,5
            horas diárias)
        """

        prev_saida = None
        horas_excedidas = None
        horas_faltantes = None

        duracoes = []

        if len(timedeltaList) % 2 == 0:
            tamLista = len(timedeltaList)
        else:
            tamLista = len(timedeltaList) - 1

        hora_almoco = False
        intervalo = 0
        for i in range(0, tamLista, 2):
            duracoes.append(timedeltaList[i+1] - timedeltaList[i])
            if intervalo != 0:
                if self.timedeltaList[i] - intervalo >= timedelta(hours=1):
                    hora_almoco = True
            intervalo = self.timedeltaList[i+1]

        if len(timedeltaList) > 1 and len(timedeltaList) % 2 != 0:

            if (timedeltaList[-1] - timedeltaList[-2] >= timedelta(hours=1)):
                hora_almoco = True

        total_reg = sum(duracoes, timedelta())

        prev_saida = self.horas_dia - total_reg + timedeltaList[-1]

        if not hora_almoco:
            prev_saida += + timedelta(hours=1)

        if total_reg >= self.horas_dia:
            horas_excedidas = total_reg - self.horas_dia
        else:
            horas_faltantes = self.horas_dia - total_reg

        return total_reg, prev_saida, horas_excedidas, horas_faltantes


if __name__ == "__main__":
    print("")
