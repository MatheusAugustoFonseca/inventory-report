from inventory_report.inventory.product import Product


def test_cria_produto():
    id = 11
    nome_do_produto = 'Copo Stanley'
    nome_da_empresa = 'Stanley'
    data_de_fabricacao = '2022-05-28'
    data_de_validade = '2042-05-28'
    numero_de_serie = 'ST01 2022 0505 2828 0055 BR'
    instrucoes_de_armazenamento = 'instrucao 11'

    product = Product(
        id,
        nome_do_produto,
        nome_da_empresa,
        data_de_fabricacao,
        data_de_validade,
        numero_de_serie,
        instrucoes_de_armazenamento,
    )

    assert product.id == id
    assert product.nome_do_produto == nome_do_produto
    assert product.nome_da_empresa == nome_da_empresa
    assert product.data_de_fabricacao == data_de_fabricacao
    assert product.data_de_validade == data_de_validade
    assert product.numero_de_serie == numero_de_serie
    assert product.instrucoes_de_armazenamento == instrucoes_de_armazenamento








