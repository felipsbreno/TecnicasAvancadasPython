# Demonstração das funções de string templates
from string import Template


def main():
    # Formatação tradicional usando o método format()
    frase = "Você está assistindo {0} com {1}".format(
        "Python Avançado", "Jessica Temporal")
    print(frase)

    # TODO: Crie um template com placeholders
    templ = Template("Você está assistindo o ${curso} com a ${instrutora}")
    # TODO: Use o método substitute passando argumentos nomeados
    frase_2 = templ.substitute(
        curso="Python Avançado", instrutora="Anna Hommann")
    print(frase_2)
    # TODO: Use  o método substitute com um dicionário
    dados = {
        "curso": "Python Avançado",
        "instrutora": "Anna Hommann",
    }

    frase_3 = templ.substitute(dados)
    print(frase_3)


if __name__ == "__main__":
    main()
