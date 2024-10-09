from Temporizador import Temporizador

def main():
    print("Dentro de main")
    TON_00 = Temporizador("Temporizador de bajo", 5)
    TON_01 = Temporizador("Temporizador de alto", 1)
    TON_0 = Temporizador("Temporizador de alto", 26)

    while True:
        TON_00.entrada = not TON_01.salida
        TON_00.actualizar()

        TON_01.entrada = TON_02.salida
        TON_01.actualizar()

        TON_02.entrada = TON_00.salida
        TON_02.actualizar()


        salida = TON_00.salida and not TON_01.salida


        print("Salida:", salida)

if __name__ == "__main__":
    main()