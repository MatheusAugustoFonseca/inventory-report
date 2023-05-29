import csv
import json
from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport


class Inventory:
    @staticmethod
    def import_data(file_path, report_type):
        if ".csv" in file_path:
            with open(file_path, encoding="utf8") as csv_file:
                csv_reader = csv.DictReader(csv_file)
                data = [row for row in csv_reader]
        if ".json" in file_path:
            with open(file_path) as json_file:
                data = json.load(json_file)
        if report_type == "simples":
            return SimpleReport.generate(data)
        return CompleteReport.generate(data)
