from inventory_report.importer.importer import Importer
import xml.etree.ElementTree as ET


class XmlImporter(Importer):
    @classmethod
    def import_data(cls, file_path):
        if not file_path.lower().endswith(".xml"):
            raise ValueError("Arquivo inválido")

        with open(file_path) as xml_file:
            elem_tree = ET.parse(xml_file)
            root = elem_tree.getroot()
            data = [
                {elem.tag: elem.text for elem in record}
                for record in root.findall("record")
            ]
        return data
