
while True:
    try:
        valor = int(input("[INFO] Digite um número válido: "))
        break
    except ValueError:
        print("ERROR: Entre com um número válido seu anima, n sabe ler?")
print(f"[SUCESS] parabens seu bosta, seu numero é {valor}")