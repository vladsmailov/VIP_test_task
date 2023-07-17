from typing import List

import pandas as pd

from src.core.db.models import Product


class Report:
    """Базовый класс отчета."""
    def __init__(self, columns):
        self.columns = columns

    def create_workbook(self):
        """Метод создания таблицы отчета."""
        sheet = {}
        for column in self.columns:
            sheet[column] = []
        workbook = pd.DataFrame(sheet)
        return workbook

    def add_data(self, workbook: pd.DataFrame, data: List[Product], name):
        """Метод добавления данных в таблицу."""
        pass

    @staticmethod
    def save_to_excel(workbook: pd.DataFrame, start, end, decimal_number):
        """Метод сохранения данных в файл excel."""
        workbook.to_excel(
            f'./reports/{decimal_number+start+end}.xlsx',
            sheet_name='Products',
            index=False
        )

    @staticmethod
    def parse_data(data) -> List:
        """Метод для парсинга данных в нужный формат."""
        parsed_data = []
        for products in data:
            for product in products:
                parsed_data.append(product)
        return [parsed_data]


class ThreeParametersReport(Report):
    """Класс создания отчета на основе ТЗ."""
    def __init__(self, columns):
        super().__init__(columns)

    def add_data(self, workbook, data: List[Product], name):
        """Метода добавления данных в талбицу."""
        if not data:
            print("Данные отсутствуют, создан пустой отчет.")
            return workbook
        for product in data[0]:
            first_part = product.created_at.strftime("%y")
            second_part = product.created_at.strftime("%m")
            third_part = str(product.sequence_number)
            if len(third_part) < 6:
                while len(third_part) < 6:
                    third_part = '0' + third_part
            if product.updated_at:
                date = product.updated_at.strftime("%d.%m.%y")
                time = product.updated_at.strftime("%H:%M:%S")
            else:
                date = product.created_at.strftime("%d.%m.%y")
                time = product.created_at.strftime("%H:%M:%S")
            new_line = pd.DataFrame({
                'Serial_number': [f'{first_part}{second_part}{third_part}'],
                'Valid': [product.status.name],
                'Date': [f'{date}'],
                'Time': [f'{time}'],
                'Sensor_name': [f'{name}'],
                'RM_ID': [''],
                'Operator': [''],
                'UID': ['']
            })
            workbook = pd.concat([workbook, new_line], ignore_index=True)
        return workbook
