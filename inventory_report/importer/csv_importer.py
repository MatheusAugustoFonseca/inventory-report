from inventory_report.importer.importer import Importer
import csv


class CsvImporter(Importer):
    @classmethod
    def import_data(cls, file_path):
        if not file_path.lower().endswith(".csv"):
            raise ValueError("Arquivo inválido")

        with open(file_path, encoding="utf8") as csv_file:
            csv_reader = csv.DictReader(csv_file)
            data = [row for row in csv_reader]
        return data
