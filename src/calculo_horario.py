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

        self.entradasValidar(self.dic)
        total_reg, prev_saida = self.saidaCalcular(self.dic)

        self.horarioImprimir(total_reg, prev_saida)

    def horarioImprimir(self, total_reg, prev_saida ):
        print(f"Total de horas já registradas: {total_reg}")
        if total_reg < self.horas_dia:
            print(f"Previsão de horário de saída: {prev_saida}")
        else:
            print('Carga horária cumprida')

    def entradasValidar (self, dic):

        dic_keys = list(self.dic.keys())

        if ('dthora_ini1' not in dic_keys):
            raise ValueError
        else:
            if ('dthora_fim1' in dic_keys):
                if not self.intervaloValidar(dt_ini = dic['dthora_ini1'], dt_fim = dic['dthora_fim1']):
                    raise ValueError

        if ('dthora_ini2' in dic_keys):
            if ('dthora_ini1' not in dic_keys or
                'dthora_fim1' not in dic_keys):
                raise ValueError
            else:
                if not self.intervaloValidar(dt_ini = dic['dthora_fim1'], dt_fim = dic['dthora_ini2']):
                    raise ValueError

        if ('dthora_fim2' in dic_keys):
            if ('dthora_ini1' not in dic_keys or
                'dthora_fim1' not in dic_keys or
                'dthora_ini2' not in dic_keys):
                raise ValueError
            else:
                if not self.intervaloValidar(dt_ini = dic['dthora_ini2'], dt_fim = dic['dthora_fim2']):
                    raise ValueError

        if ('dthora_ini3' in dic_keys):
            if ('dthora_ini1' not in dic_keys or
                'dthora_fim1' not in dic_keys or
                'dthora_ini2' not in dic_keys or
                'dthora_fim2' not in dic_keys):
                raise ValueError
            else:
                if not self.intervaloValidar(dt_ini = dic['dthora_fim2'], dt_fim = dic['dthora_ini3']):
                    raise ValueError

        if ('dthora_fim3' in dic_keys):
            if ('dthora_ini1' not in dic_keys or
                'dthora_fim1' not in dic_keys or
                'dthora_ini2' not in dic_keys or
                'dthora_fim2' not in dic_keys or
                'dthora_ini3' not in dic_keys):
                raise ValueError
            else:
                if not self.intervaloValidar(dt_ini = dic['dthora_ini3'], dt_fim = dic['dthora_fim3']):
                    raise ValueError

    def intervaloValidar(self, dt_ini, dt_fim):
        if dt_ini > dt_fim:
            return False
        return True

    def saidaCalcular(self, dic):

        calc_saida = None
        prev_saida = None

        if 'dthora_fim3' in dic:
            duracoes = [dic['dthora_fim3'] - dic['dthora_ini3'],
                        dic['dthora_fim2'] - dic['dthora_ini2'],
                        dic['dthora_fim1'] - dic['dthora_ini1']]

        elif 'dthora_ini3' in dic:
            duracoes = [dic['dthora_fim2'] - dic['dthora_ini2'],
                        dic['dthora_fim1'] - dic['dthora_ini1']]
            calc_saida = dic['dthora_ini3']

        elif 'dthora_fim2' in dic:
            duracoes = [dic['dthora_fim2'] - dic['dthora_ini2'],
                        dic['dthora_fim1'] - dic['dthora_ini1']]
            calc_saida = dic['dthora_fim2']

        elif 'dthora_ini2' in dic:
            duracoes = [dic['dthora_fim1'] - dic['dthora_ini1']]
            calc_saida = dic['dthora_ini2']

        elif 'dthora_fim1' in dic:
            duracoes = [dic['dthora_fim1'] - dic['dthora_ini1']]

            calc_saida = dic['dthora_fim1'] + timedelta(hours = 1)

        elif 'dthora_ini1' in dic:
            duracoes = [timedelta(hours = 0)]
            calc_saida = dic['dthora_ini1'] + timedelta(hours = 1)

        total_reg = sum(duracoes, timedelta())

        saldo_horas_dia = self.horas_dia - total_reg


        if calc_saida is not None:
            prev_saida = saldo_horas_dia + calc_saida

        return total_reg, prev_saida

if __name__ == "__main__":
    print("")
