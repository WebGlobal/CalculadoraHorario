from datetime import timedelta, time

class Horario():
    def __init__(self,
                 hora_ini1, hora_fim1 = None,
                 hora_ini2= None ,hora_fim2= None,
                 hora_ini3= None, hora_fim3= None):

        self.horas_dia = timedelta(hours = 8, minutes = 30)

        self.dic = {}

        if  hora_ini1 is not None:
            self.dic['dthora_ini1'] = timedelta(hours = int(hora_ini1[0:2]), minutes = int(hora_ini1[3:]))
        if  hora_fim1 is not None:
            self.dic['dthora_fim1'] = timedelta(hours = int(hora_fim1[0:2]), minutes = int(hora_fim1[3:]))
        if  hora_ini2 is not None:
            self.dic['dthora_ini2'] = timedelta(hours = int(hora_ini2[0:2]), minutes = int(hora_ini2[3:]))
        if  hora_fim2 is not None:
            self.dic['dthora_fim2'] = timedelta(hours = int(hora_fim2[0:2]), minutes = int(hora_fim2[3:]))
        if  hora_ini3 is not None:
            self.dic['dthora_ini3'] = timedelta(hours = int(hora_ini3[0:2]), minutes = int(hora_ini3[3:]))
        if  hora_fim3 is not None:
            self.dic['dthora_fim3'] = timedelta(hours = int(hora_fim3[0:2]), minutes = int(hora_fim3[3:]))

    def calcular(self):

        self.entradasValidar()
        total_reg, prev_saida = self.saidaCalcular()
        msgList = self.horarioImprimir(total_reg, prev_saida)

        return msgList

    def horarioImprimir(self, total_reg, prev_saida):

        msgList = []
        print(f"Total de horas já registradas: {total_reg}")
        msgList.append(f"Total de horas já registradas: {total_reg}")
        if total_reg < self.horas_dia:
            msgList.append(f"Previsão de horário de saída: {prev_saida}")
            print(f"Previsão de horário de saída: {prev_saida}")
        else:
            msgList.append(f"Carga horária cumprida")
            print('Carga horária cumprida')

        return msgList

    def entradasValidar (self):

        dic_keys = list(self.dic.keys())

        if ('dthora_ini1' not in dic_keys):
            raise ValueError
        else:
            if ('dthora_fim1' in dic_keys):
                if not self.intervaloValidar(dt_ini = self.dic['dthora_ini1'], dt_fim = self.dic['dthora_fim1']):
                    raise ValueError

        if ('dthora_ini2' in dic_keys):
            if ('dthora_ini1' not in dic_keys or
                'dthora_fim1' not in dic_keys):
                raise ValueError
            else:
                if not self.intervaloValidar(dt_ini = self.dic['dthora_fim1'], dt_fim = self.dic['dthora_ini2']):
                    raise ValueError

        if ('dthora_fim2' in dic_keys):
            if ('dthora_ini1' not in dic_keys or
                'dthora_fim1' not in dic_keys or
                'dthora_ini2' not in dic_keys):
                raise ValueError
            else:
                if not self.intervaloValidar(dt_ini = self.dic['dthora_ini2'], dt_fim = self.dic['dthora_fim2']):
                    raise ValueError

        if ('dthora_ini3' in dic_keys):
            if ('dthora_ini1' not in dic_keys or
                'dthora_fim1' not in dic_keys or
                'dthora_ini2' not in dic_keys or
                'dthora_fim2' not in dic_keys):
                raise ValueError
            else:
                if not self.intervaloValidar(dt_ini = self.dic['dthora_fim2'], dt_fim = self.dic['dthora_ini3']):
                    raise ValueError

        if ('dthora_fim3' in dic_keys):
            if ('dthora_ini1' not in dic_keys or
                'dthora_fim1' not in dic_keys or
                'dthora_ini2' not in dic_keys or
                'dthora_fim2' not in dic_keys or
                'dthora_ini3' not in dic_keys):
                raise ValueError
            else:
                if not self.intervaloValidar(dt_ini = self.dic['dthora_ini3'], dt_fim = self.dic['dthora_fim3']):
                    raise ValueError

    def intervaloValidar(self, dt_ini, dt_fim):
        if dt_ini > dt_fim:
            return False
        return True

    def saidaCalcular(self):

        calc_saida = None
        prev_saida = None

        if 'dthora_fim3' in self.dic:
            duracoes = [self.dic['dthora_fim3'] - self.dic['dthora_ini3'],
                        self.dic['dthora_fim2'] - self.dic['dthora_ini2'],
                        self.dic['dthora_fim1'] - self.dic['dthora_ini1']]
            calc_saida = self.dic['dthora_fim3']

        elif 'dthora_ini3' in self.dic:
            duracoes = [self.dic['dthora_fim2'] - self.dic['dthora_ini2'],
                        self.dic['dthora_fim1'] - self.dic['dthora_ini1']]
            calc_saida = self.dic['dthora_ini3']

        elif 'dthora_fim2' in self.dic:
            duracoes = [self.dic['dthora_fim2'] - self.dic['dthora_ini2'],
                        self.dic['dthora_fim1'] - self.dic['dthora_ini1']]
            calc_saida = self.dic['dthora_fim2']

        elif 'dthora_ini2' in self.dic:
            duracoes = [self.dic['dthora_fim1'] - self.dic['dthora_ini1']]
            calc_saida = self.dic['dthora_ini2']

        elif 'dthora_fim1' in self.dic:
            duracoes = [self.dic['dthora_fim1'] - self.dic['dthora_ini1']]

            calc_saida = self.dic['dthora_fim1'] + timedelta(hours = 1)

        elif 'dthora_ini1' in self.dic:
            duracoes = [timedelta(hours = 0)]
            calc_saida = self.dic['dthora_ini1'] + timedelta(hours = 1)

        total_reg = sum(duracoes, timedelta())

        saldo_horas_dia = self.horas_dia - total_reg

        if calc_saida is not None:
            prev_saida = saldo_horas_dia + calc_saida

        return total_reg, prev_saida

def test_3_intervalos_comp():

    h = Horario(hora_ini1="09:00",
                hora_fim1="12:00",
                hora_ini2="13:00",
                hora_fim2="14:00",
                hora_ini3="15:00",
                hora_fim3="18:30")

    msgList = h.calcular()

    assert (msgList[0] == 'Total de horas já registradas: 7:30:00')

    assert (msgList[1] == 'Previsão de horário de saída: 19:30:00')

def test_3_intervalos_incomp():

    h = Horario(hora_ini1="09:00",
                hora_fim1="12:00",
                hora_ini2="13:00",
                hora_fim2="14:00",
                hora_ini3="15:00")

    msgList = h.calcular()

    assert (msgList[0] == 'Total de horas já registradas: 4:00:00')

    assert (msgList[1] == 'Previsão de horário de saída: 19:30:00')

def test_2_intervalos_comp():

    h = Horario(hora_ini1="09:00",
                hora_fim1="12:00",
                hora_ini2="13:00",
                hora_fim2="14:00")

    msgList = h.calcular()

    assert (msgList[0] == 'Total de horas já registradas: 4:00:00')

    assert (msgList[1] == 'Previsão de horário de saída: 18:30:00')

def test_2_intervalos_incomp():

    h = Horario(hora_ini1="09:00",
                hora_fim1="12:00",
                hora_ini2="13:00")

    msgList = h.calcular()

    assert (msgList[0] == 'Total de horas já registradas: 3:00:00')

    assert (msgList[1] == 'Previsão de horário de saída: 18:30:00')

def test_2_intervalos_incomp():

    h = Horario(hora_ini1="09:00",
                hora_fim1="12:00",
                hora_ini2="13:00")

    msgList = h.calcular()

    assert (msgList[0] == 'Total de horas já registradas: 3:00:00')

    assert (msgList[1] == 'Previsão de horário de saída: 18:30:00')

def test_1_intervalo_comp():

    h = Horario(hora_ini1="09:00",
                hora_fim1="12:00")


    msgList = h.calcular()

    assert (msgList[0] == 'Total de horas já registradas: 3:00:00')

    assert (msgList[1] == 'Previsão de horário de saída: 18:30:00')

def test_1_intervalo_incomp():

    h = Horario(hora_ini1="09:00")

    msgList = h.calcular()

    assert (msgList[0] == 'Total de horas já registradas: 0:00:00')

    assert (msgList[1] == 'Previsão de horário de saída: 18:30:00')

def test_carga_completa():

    h = Horario(hora_ini1="09:00",
                hora_fim1="12:00",
                hora_ini2="13:00",
                hora_fim2="19:00")

    msgList = h.calcular()

    assert (msgList[0] == 'Total de horas já registradas: 9:00:00')

    assert (msgList[1] == 'Carga horária cumprida')


if __name__ == "__main__":
    print("")
