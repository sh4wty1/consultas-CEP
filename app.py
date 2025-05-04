"""
Este script consulta o endereço a partir de um CEP usando a API ViaCEP.
Ele recebe o CEP, faz a requisição HTTP e exibe os dados formatados.
"""

import requests


def search_cep(cep_input):
    """Consultar CEP

    Args:
        cep (int): CEP utilizado na busca pela API.

    Returns:
        dict | None: retorna um dicionário Python com os dados do CEP ou None se a requisição falhar.
    """
    response = requests.get(f"https://viacep.com.br/ws/{cep_input}/json/", timeout=5)

    if response.status_code == 200:
        data = response.json()
        return data
    print(f"Erro na requisição: {response.status_code}")
    input("Pressione qualquer tecla para fechar...")


while True:
    cep = input("Qual cep deseja consultar? ")
    results = search_cep(cep)

    print(f"Resultados para o CEP {results["cep"]}:")
    print(f"Rua: {results["logradouro"]}")
    print(f"Cidade: {results["localidade"]}")
    print(f"Bairro: {results["bairro"]}")
    print(f"Estado: {results["estado"]}")
    print(f"Região: {results["regiao"]}")
    print(f"DDD do telefone: {results["ddd"]}")
    print("CTRL + C para fechar.")
