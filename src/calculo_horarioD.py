from datetime import timedelta, time

class Horario():
    def __init__(self, list_args):

        self.horas_dia = timedelta(hours = 8, minutes = 30)
        self.timedeltaList = []

        for arg in list_args:
            self.timedeltaList.append(timedelta(hours = int(arg[0:2]), minutes = int(arg[3:])))

        self.timedeltaList = sorted(self.timedeltaList)

    def calcular(self):

        # self.entradasValidar()
        total_reg, prev_saida, horas_excedidas = self.saidaCalcular()
        msgList = self.horarioImprimir(total_reg, prev_saida, horas_excedidas)

        return msgList

    def horarioImprimir(self, total_reg, prev_saida, horas_excedidas ):

        msgList = []
        print(f"Total de horas já registradas: {total_reg}")
        msgList.append(f"Total de horas já registradas: {total_reg}")
        if total_reg < self.horas_dia:
            msgList.append(f"Previsão de horário de saída: {prev_saida}")
            print(f"Previsão de horário de saída: {prev_saida}")
        else:
            msgList.append(f"Carga horária cumprida")
            print('Carga horária cumprida')

        if horas_excedidas:
            msgList.append(f"Total de horas excedidas: {horas_excedidas}")
            print(f"Total de horas excedidas: {horas_excedidas}")

        return msgList

    def saidaCalcular(self):

        prev_saida = None
        horas_excedidas = None

        duracoes = []

        if len(self.timedeltaList) % 2 == 0:
            tamLista = len(self.timedeltaList)
        else:
            tamLista = len(self.timedeltaList) - 1

        hora_almoco = False
        intervalo = 0
        for i in range(0,tamLista,2):
            duracoes.append(self.timedeltaList[i+1] - self.timedeltaList[i])
            if intervalo !=0:
                if self.timedeltaList[i] - intervalo >= timedelta(hours = 1):
                    hora_almoco = True
            intervalo = self.timedeltaList[i+1]


        if len(self.timedeltaList) >1  and len(self.timedeltaList) % 2 != 0:
            if self.timedeltaList[-1] - self.timedeltaList[-2] >= timedelta(hours = 1):
                hora_almoco = True

        total_reg = sum(duracoes, timedelta())

        prev_saida = self.horas_dia - total_reg + self.timedeltaList[-1]

        if not hora_almoco:
            prev_saida += + timedelta(hours = 1)

        if total_reg >= self.horas_dia:
            horas_excedidas = total_reg - self.horas_dia

        return total_reg, prev_saida, horas_excedidas

def test_3_intervalos_comp():

    h = Horario(["09:00", "12:00", "13:00", "14:00", "15:00", "18:30"])

    msgList = h.calcular()

    assert (msgList[0] == 'Total de horas já registradas: 7:30:00')

    assert (msgList[1] == 'Previsão de horário de saída: 19:30:00')

def test_3_intervalos_incomp():

    h = Horario(["09:00", "12:00", "13:00", "14:00", "15:00"])

    msgList = h.calcular()

    assert (msgList[0] == 'Total de horas já registradas: 4:00:00')

    assert (msgList[1] == 'Previsão de horário de saída: 19:30:00')

def test_2_intervalos_comp():

    h = Horario(["09:00", "12:00", "13:00", "14:00"])

    msgList = h.calcular()

    assert (msgList[0] == 'Total de horas já registradas: 4:00:00')

    assert (msgList[1] == 'Previsão de horário de saída: 18:30:00')

def test_2_intervalos_incomp():

    h = Horario(["09:00", "12:00", "13:00"])

    msgList = h.calcular()

    assert (msgList[0] == 'Total de horas já registradas: 3:00:00')

    assert (msgList[1] == 'Previsão de horário de saída: 18:30:00')

def test_1_intervalo_comp():

    h = Horario(["09:00", "12:00"])


    msgList = h.calcular()

    assert (msgList[0] == 'Total de horas já registradas: 3:00:00')

    assert (msgList[1] == 'Previsão de horário de saída: 18:30:00')

def test_1_intervalo_incomp():

    h = Horario(["09:00"])

    msgList = h.calcular()

    assert (msgList[0] == 'Total de horas já registradas: 0:00:00')

    assert (msgList[1] == 'Previsão de horário de saída: 18:30:00')

def test_carga_completa():

    h = Horario(["09:00", "12:00", "13:00", "18:30"])

    msgList = h.calcular()

    assert (msgList[0] == 'Total de horas já registradas: 8:30:00')

    assert (msgList[1] == 'Carga horária cumprida')

def test_carga_excedida():

    h = Horario(["09:00", "12:00", "13:00", "19:00"])

    msgList = h.calcular()

    assert (msgList[0] == 'Total de horas já registradas: 9:00:00')

    assert (msgList[1] == 'Carga horária cumprida')

    assert (msgList[2] == 'Total de horas excedidas: 0:30:00')


if __name__ == "__main__":
    print("")
