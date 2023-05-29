from inventory_report.importer.importer import Importer
import json


class JsonImporter(Importer):
    @classmethod
    def import_data(cls, file_path):
        if not file_path.lower().endswith(".json"):
            raise ValueError("Arquivo inválido")

        with open(file_path) as json_file:
            data = json.load(json_file)
        return data
