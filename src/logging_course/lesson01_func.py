import traceback

# Como desligo esse print em prod?
# Qual a gravidade do print? Foi correto? Foi erro?
# De onde veio essa mensagem? Cadê o contexto? Arquivo, módulo, linha, data?
# E se eu quiser salvar os erros em um arquivo, enviar por e-mail, Socket, etc?


def dividir(x: float, y: float) -> float:
    print(f"Recebi x={x} e y={y}")  # isso é debug

    if y == 0:
        msg = f"Não posso dividir {x} por {y}"
        raise ZeroDivisionError(msg)  # E agora?

    resultado = x / y
    print(f"O resultado é {resultado}")  # isso é info
    return resultado


try:
    dividir(10, 2)
    dividir(10, 0)
except ZeroDivisionError:
    traceback.print_exc()
