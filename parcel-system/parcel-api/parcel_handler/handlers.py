import xml.etree.ElementTree as ET
from .factory import DepartmentFactory

class ParcelHandler:
    def __init__(self, xml_file):
        self.factory = DepartmentFactory()
        self.xml_file = xml_file

    def parse_parcels(self):
        tree = ET.parse(self.xml_file)
        root = tree.getroot()

        parcels = []
        for parcel in root.find('parcels'):
            name = parcel.find('Receipient/Name').text
            weight = float(parcel.find('Weight').text)
            value = float(parcel.find('Value').text)
            parcels.append({'name': name, 'weight': weight, 'value': value})
        return parcels

    def handle_parcels(self):
        parcels = self.parse_parcels()
        for parcel in parcels:
            department = self.factory.get_department(parcel['weight'], parcel['value'])
            department.process(parcel)
