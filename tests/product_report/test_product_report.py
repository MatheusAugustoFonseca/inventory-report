from inventory_report.inventory.product import Product


def test_relatorio_produto():
    # pass  # Seu teste deve ser escrito aqui
    produto = Product(
        1,
        "MESA",
        "Forces of Nature",
        "2022-05-04",
        "2023-02-09",
        "FR48",
        "Conservar ao abrigo de luz",
    )

    assert produto.__repr__() == (
        "O produto MESA fabricado em 2022-05-04 por "
        "Forces of Nature com validade até 2023-02-09 "
        "precisa ser armazenado Conservar ao abrigo de luz."
    )

    #     "id": 1,
    # "nome_do_produto": "MESA",
    # "nome_da_empresa": "Forces of Nature",
    # "data_de_fabricacao": "2022-05-04",
    # "data_de_validade": "2023-02-09",
    # "numero_de_serie": "FR48",
    # "instrucoes_de_armazenamento": "Conservar ao abrigo de luz"
