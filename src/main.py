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


def hora(strhora: str) -> bool:
    """
    realiza a consistência dos dados de entrada

    ### Parameters:
        - strhora: valor passado como parâmetro na chamada do programa

    """

    if (
        re.search(
            r"((^0?[0-9])|(^1[0-9])|(^2[0-3])){1}[:]{1}([0-5][0-9]){1}$",
            strhora,
            re.IGNORECASE)
    ):
        return True
    elif (re.search(r"((^2[4-9]){1}|(^[3-9][0-9]))$", strhora, re.IGNORECASE)):
        raise ValueError
    raise KeyError


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
            if hora(arg):
                if len(arg) < 5:
                    arg = "0" + arg
                parser.add_argument(
                    dest=list_args.append(arg),
                    type=hora,
                    help="Hora Chegada ",
                    default="00:00"
                )
        except ValueError:
            print('Hora fornecida não pode ser maior que 23:59')
            exit()
        except KeyError:
            print(f'Formato inválido para a hora "{arg}". Utilize o formato '
                  '"00:00"')
            exit()

    h = Horario(list_args)

    h.calcular()


if __name__ == "__main__":
    main()
