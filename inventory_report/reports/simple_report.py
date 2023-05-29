from datetime import datetime
from collections import Counter


class SimpleReport:
    @staticmethod
    def generate(products):
        production_dates = list()
        expiration_dates = list()
        companies = list()

        for product in products:
            production_date = product.get("data_de_fabricacao")
            expiration_date = product.get("data_de_validade")
            expiration_date_obj = datetime.strptime(
                expiration_date, "%Y-%m-%d"
            ).date()
            company = product.get("nome_da_empresa")
            production_dates.append(production_date)
            if expiration_date_obj >= str(datetime.now().date()):
                expiration_dates.append(expiration_date_obj)
            companies.append(company)

            earliest_date = min(production_dates)
            latest_expiry_date = min(production_dates)
            most_products_company = Counter(companies).most_common(1)[0][0]
            report = (
                f"Data de fabricação mais antiga: {earliest_date}\n"
                f"Data de fabricação mais próxima: {latest_expiry_date}\n"
                f"Empresa com mais produtos: {most_products_company}\n"
            )
            return report
