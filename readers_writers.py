import json
import csv
from zope.interface import implementer
from interfaces import IDataReader, IDataWriter
from models import StudentApplication
from enums import PrivilegesEnum

@implementer(IDataReader)
class JsonReader:
    def read(self, file_path: str):
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        return [StudentApplication(**{
            'name': d['name'],
            'family_children': d['family_children'],
            'privileges': [PrivilegesEnum[p] for p in d['privileges']]
        }) for d in data]

@implementer(IDataWriter)
class JsonWriter:
    def write(self, file_path: str, data):
        serializable_data = [{
            'name': app.name,
            'family_children': app.family_children,
            'privileges': [p.name for p in app.privileges]
        } for app in data]
        with open(file_path, 'w', encoding='utf-8') as f:
            json.dump(serializable_data, f, ensure_ascii=False, indent=4)

@implementer(IDataReader)
class CsvReader:
    def read(self, file_path: str):
        applications = []
        with open(file_path, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                privileges = [PrivilegesEnum[p.strip()] for p in row['privileges'].split('|') if p.strip()]
                applications.append(StudentApplication(
                    name=row['name'],
                    family_children=int(row['family_children']),
                    privileges=privileges
                ))
        return applications

@implementer(IDataWriter)
class CsvWriter:
    def write(self, file_path: str, data):
        with open(file_path, 'w', newline='', encoding='utf-8') as csvfile:
            fieldnames = ['name', 'family_children', 'privileges']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            for app in data:
                writer.writerow({
                    'name': app.name,
                    'family_children': app.family_children,
                    'privileges': '|'.join(p.name for p in app.privileges)
                })
