from inventory_report.reports.colored_report import ColoredReport
from inventory_report.reports.simple_report import SimpleReport

BLUE = "\033[36m"
GREEN = "\033[32m"
RED = "\033[31m"
RESET = "\033[0m"

product_data = [
        {
            "id": 1,
            "nome_do_produto": "Quebra-cabeça",
            "nome_da_empresa": "Estrela",
            "data_de_fabricacao": "2015-09-17",
            "data_de_validade": "2025-09-17",
            "numero_de_serie": "FR488",
            "instrucoes_de_armazenamento": "instrucao12",
        }
    ]


def test_decorar_relatorio():
    report = SimpleReport.generate(product_data)
    colored = ColoredReport(report)

    assert colored == (
        f"{GREEN}Data de fabricação mais antiga:{RESET}"
        f"{BLUE}2015-09-17{RESET}"
        f"{GREEN}Data de validade mais próxima:{RESET}"
        f"{BLUE}2025-09-17{RESET}"
        f"{GREEN}Empresa com mais produtos:{RESET}"
        f"{RED}Estrela{RESET}"
    )
