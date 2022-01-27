from ..abc import AbstractDocument
import pandas as pd


class ExcelDocument(AbstractDocument):

    async def parse(self, file_bytes):
        excel_file = pd.read_excel(file_bytes, skiprows=6, nrows=10)  # useful info starts from 6th row

        lessons = excel_file['ТО-21-1']
        changes = {'group_name': 'ТО-21-1',
                   'changelist': []}
        for string_index in range(0, len(lessons), 2):
            lesson_name = lessons[string_index]
            teacher_name = lessons[string_index+1]

            if isinstance(lesson_name, float):
                continue
            changes['changelist'].append({'number': string_index//2 + 1,
                                          'lesson_name': lesson_name,
                                          'teacher_name': teacher_name})

        return changes
