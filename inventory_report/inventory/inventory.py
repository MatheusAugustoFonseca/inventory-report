# import csv
# import json
from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport
# import xml.etree.ElementTree as ET
from inventory_report.importer.csv_importer import CsvImporter
from inventory_report.importer.json_importer import JsonImporter
from inventory_report.importer.xml_importer import XmlImporter


class Inventory:
    @staticmethod
    def import_data(file_path, report_type):
        # if ".csv" in file_path:
        #     with open(file_path, encoding="utf8") as csv_file:
        #         csv_reader = csv.DictReader(csv_file)
        #         data = [row for row in csv_reader]
        # if ".json" in file_path:
        #     with open(file_path) as json_file:
        #         data = json.load(json_file)
        # if ".xml" in file_path:
        #     with open(file_path) as xml_file:
        #         elem_tree = ET.parse(xml_file)
        #         root = elem_tree.getroot()
        #         data = [
        #             {elem.tag: elem.text for elem in record}
        #             for record in root.findall("record")
        #         ]
        if file_path.endswith(".csv"):
            data = CsvImporter.import_data(file_path)
        if file_path.endswith(".json"):
            data = JsonImporter.import_data(file_path)
        if file_path.endswith(".xml"):
            data = XmlImporter.import_data(file_path)

        if report_type == "simples":
            return SimpleReport.generate(data)
        return CompleteReport.generate(data)
