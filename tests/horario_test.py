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

import os
import sys


def append_to_path() -> str:
    """
    Função para adicionar o diretório do projeto ao python path

    """

    project = "CalculadoraHorario" + "/"

    abs_path = os.path.abspath(__file__)
    new_path = abs_path[: abs_path.rfind(project) + len(project)] + "src/"
    sys.path.append(new_path)

    return new_path


append_to_path()

from calculo_horario import Horario


class TestHorarios():
    """
    Classe de testes

    ### Methods:
        - test_3_intervalos_comp: teste com 3 intervalos completos
        - test_3_intervalos_incomp: teste com 2 intervalos completos
          e 1 intervalo aberto
        - test_2_intervalos_comp: teste com 2 intervalos completos
        - test_2_intervalos_incomp: teste com 1 intervalos completo
          e 1 intervalo aberto
        - test_1_intervalo_comp: teste com 1 intervalo completo
        - test_1_intervalo_incomp: teste com 1 intervalo aberto
        - test_carga_completa: teste com a carga horário do dia cumprida
        - test_carga_excedida: teste com a carga horário do dia excedida
    """

    def test_3_intervalos_comp(self):

        h = Horario(["09:00", "12:00", "13:00", "14:00", "15:00", "18:30"])

        msgList = h.calcular()

        assert (msgList[0] == 'Total de horas já registradas: 7:30:00')

        assert (msgList[1] == 'Previsão de horário de saída: 19:30:00')

        assert (msgList[2] == 'Total de horas faltantes: 1:00:00')

    def test_3_intervalos_incomp(self):

        h = Horario(["09:00", "12:00", "13:00", "14:00", "15:00"])

        msgList = h.calcular()

        assert (msgList[0] == 'Total de horas já registradas: 4:00:00')

        assert (msgList[1] == 'Previsão de horário de saída: 19:30:00')

        assert (msgList[2] == 'Total de horas faltantes: 4:30:00')

    def test_2_intervalos_comp(self):

        h = Horario(["09:00", "12:00", "13:00", "14:00"])

        msgList = h.calcular()

        assert (msgList[0] == 'Total de horas já registradas: 4:00:00')

        assert (msgList[1] == 'Previsão de horário de saída: 18:30:00')

        assert (msgList[2] == 'Total de horas faltantes: 4:30:00')

    def test_2_intervalos_incomp(self):

        h = Horario(["09:00", "12:00", "13:00"])

        msgList = h.calcular()

        assert (msgList[0] == 'Total de horas já registradas: 3:00:00')

        assert (msgList[1] == 'Previsão de horário de saída: 18:30:00')

        assert (msgList[2] == 'Total de horas faltantes: 5:30:00')

    def test_1_intervalo_comp(self):

        h = Horario(["09:00", "12:00"])

        msgList = h.calcular()

        assert (msgList[0] == 'Total de horas já registradas: 3:00:00')

        assert (msgList[1] == 'Previsão de horário de saída: 18:30:00')

        assert (msgList[2] == 'Total de horas faltantes: 5:30:00')

    def test_1_intervalo_incomp(self):

        h = Horario(["09:00"])

        msgList = h.calcular()

        assert (msgList[0] == 'Total de horas já registradas: 0:00:00')

        assert (msgList[1] == 'Previsão de horário de saída: 18:30:00')

        assert (msgList[2] == 'Total de horas faltantes: 8:30:00')

    def test_carga_completa(self):

        h = Horario(["09:00", "12:00", "13:00", "18:30"])

        msgList = h.calcular()

        assert (msgList[0] == 'Total de horas já registradas: 8:30:00')

        assert (msgList[1] == 'Carga horária cumprida')

    def test_carga_excedida(self):

        h = Horario(["09:00", "12:00", "13:00", "19:00"])

        msgList = h.calcular()

        assert (msgList[0] == 'Total de horas já registradas: 9:00:00')

        assert (msgList[1] == 'Carga horária cumprida')

        assert (msgList[2] == 'Total de horas excedidas: 0:30:00')


if __name__ == "__main__":
    print("")
