import argparse
import re
import sys
from calculo_horarioD import Horario

def hora(strhora):

    if (re.search(r"((^0?[0-9])|(^1[0-9])|(^2[0-3])){1}[:]{1}([0-5][0-9]){1}", strhora, re.IGNORECASE)):
        return True
    elif (re.search(r"((^2[4-9]){1}|(^[3-9][0-9]))", strhora, re.IGNORECASE)):
        raise ValueError
    raise KeyError

def main():

    parser = argparse.ArgumentParser(
        description="Classificador de Categorias/Produtos | Debugger | CLI Application",
        epilog="WebGlobal 2021 - All Rights Reserved",
    )

    list_args = []

    for arg in sys.argv[1:]:
        try:
            if hora(arg):
                if len(arg) < 5:
                    arg = "0" + arg
                parser.add_argument(
                dest= list_args.append(arg),
                type=hora,
                help="Hora Chegada ",
                default="00:00"
                )
        except ValueError:
            print(f'Hora fornecida não pode ser maior que 23:59')
            exit()
        except KeyError:
            print(f'Formato inválido para a hora "{arg}". Utilize o formato "00:00"')
            exit()

    h = Horario(list_args)

    h.calcular()

if __name__ == "__main__":
    main()
