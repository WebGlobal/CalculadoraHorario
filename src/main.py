###############################################################################
##           __          __  _      _____ _       _           _              ##
##           \ \        / / | |    / ____| |     | |         | |             ##
##            \ \  /\  / /__| |__ | |  __| | ___ | |__   __ _| |             ##
##             \ \/  \/ / _ \ '_ \| | |_ | |/ _ \| '_ \ / _` | |             ##
##              \  /\  /  __/ |_) | |__| | | (_) | |_) | (_| | |             ##
##               \/  \/ \___|_.__/ \_____|_|\___/|_.__/ \__,_|_|             ##
##                                                                           ##
##        Copyright (c) 2025 WebGlobal - Todos os Direitos Reservados        ##
##                                                                           ##
###############################################################################

import argparse
import re
import sys
from calculo_horario import Horario
from datetime import datetime

def validar_hora(entrada_horas):
    """
    Valida se a string de entrada está no formato HH:MM (24 horas).
    """
    try:
        # Tenta converter a string para um objeto time usando o formato %H:%M
        hora = datetime.strptime(entrada_horas, '%H:%M')

        return hora
    except ValueError:
        raise ValueError

def main():
    """
    Função principal

    """

    parser = argparse.ArgumentParser(
        description="Calculadora de Horários",
        epilog="WebGlobal 2021 - All Rights Reserved",
    )

    list_args = []

    for arg in sys.argv[1:]:
        try:
            hora = validar_hora(arg)
            parser.add_argument(
                dest=list_args.append(hora),
                type=validar_hora,
                help="Hora Chegada ",
                default="00:00"
            )

        except ValueError:
            print(f'Formato inválido para a hora "{arg}" ou hora fornecida'
                   'maior que 23:59. Utilize o formato "00:00"')
            exit()

    h = Horario(list_args)

    h.calcular()

if __name__ == "__main__":
    main()
