import requests
import csv
from sys import argv


URL_BASE = "https://apitempo.inmet.gov.br/estacao/diaria/{}/{}/{}"


def baixa_dados(dt_inicial, dt_final, cod_estacao):
    url = URL_BASE.format(
        dt_inicial,
        dt_final,
        cod_estacao
    )
    print(f"Baixando dados da estação {cod_estacao}...")
    response = requests.get(url)
    print("Dados baixados com sucesso!")
    return response.json()


def escreve_csv(dados, cod_estacao):
    filename = f"{cod_estacao}.csv"
    print(f"Criando arquivo {filename}...")
    with open(filename, "w") as csv_file:
        fieldnames = dados[0].keys()
        writer = csv.DictWriter(
            csv_file,
            fieldnames=fieldnames
        )
        writer.writeheader()
        for dado in dados:
            writer.writerow(dado)
    print(f"Arquivo {filename} criado com sucesso!")


def main():
    dt_inicial = argv[1]
    dt_final = argv[2]
    lista_codigos = argv[3].split(',')
    for codigo in lista_codigos:
        dados = baixa_dados(
            dt_inicial,
            dt_final,
            codigo
        )
        escreve_csv(dados, codigo)


main()