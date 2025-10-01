import argparse
import re
import sys
from calculo_horarioD import Horario

def hora(strhora):
    if (re.search(r"((0[0-9])|(1[0-9])|(2[0-3])){1}[:]{1}([0-5][0-9]){1}", strhora, re.IGNORECASE)):
        return strhora
    raise ValueError

def main():

    parser = argparse.ArgumentParser(
        description="Classificador de Categorias/Produtos | Debugger | CLI Application",
        epilog="WebGlobal 2021 - All Rights Reserved",
    )

    list_args = []

    for arg in sys.argv[1:]:
        try:
            if hora(arg):

                parser.add_argument(
                dest= list_args.append(arg),
                type=hora,
                help="Hora Chegada ",
                default="00:00"
                )
        except:
            print(f'Formato inválido para a hora "{arg}". Utilize o formato "00:00"')
            exit()

    h = Horario(list_args)

    h.calcular()

if __name__ == "__main__":
    main()
