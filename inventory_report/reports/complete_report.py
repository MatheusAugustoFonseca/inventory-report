from inventory_report.reports.simple_report import SimpleReport
from collections import Counter


class CompleteReport(SimpleReport):
    @staticmethod
    def generate(products):
        report = SimpleReport.generate(products)

        companies_stocks = Counter(
            product["nome_da_empresa"] for product in products
        )
        report += "\nProdutos estocados por empresa:\n"
        for company, count in companies_stocks.items():
            report += f"- {company}: {count}\n"
        return report
