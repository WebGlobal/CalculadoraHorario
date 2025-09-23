import argparse
import re
from calculo_horario import Horario

def hora(strhora):
    if (re.search(r"((0[0-9])|(1[0-9])|(2[0-3])){1}[:]{1}([0-5][0-9]){1}", strhora, re.IGNORECASE)):
        return strhora
    raise ValueError

def main():

    parser = argparse.ArgumentParser(
        description="Classificador de Categorias/Produtos | Debugger | CLI Application",
        epilog="WebGlobal 2021 - All Rights Reserved",
    )

    parser.add_argument(
        "-hora_ini1",
        "-hi1",
        dest="hora_ini1",
        type=hora,
        help="Hora Chegada 1",
        default="00:00",
        required=True
    )

    parser.add_argument(
        "-hora_fim1",
        "-hf1",
        dest="hora_fim1",
        type=hora,
        help="Hora Saída 1",
        default=None,
        required=False
    )

    parser.add_argument(
        "-hora_ini2",
        "-hi2",
        dest="hora_ini2",
        type=hora,
        help="Hora Chegada 2",
        default=None,
        required=False
    )

    parser.add_argument(
        "-hora_fim2",
        "-hf2",
        dest="hora_fim2",
        type=hora,
        help="Hora Saída 2",
        default=None,
        required=False
    )

    parser.add_argument(
        "-hora_ini3",
        "-hi3",
        dest="hora_ini3",
        type=hora,
        help="Hora Chegada 3",
        default=None,
        required=False
    )

    parser.add_argument(
        "-hora_fim3",
        "-hf3",
        dest="hora_fim3",
        type=hora,
        help="Hora Saída 3",
        default=None,
        required=False
    )

    args = parser.parse_args()

    Horario(hora_ini1=args.hora_ini1,
            hora_fim1=args.hora_fim1,
            hora_ini2=args.hora_ini2,
            hora_fim2=args.hora_fim2,
            hora_ini3=args.hora_ini3,
            hora_fim3=args.hora_fim3)

if __name__ == "__main__":
    main()
