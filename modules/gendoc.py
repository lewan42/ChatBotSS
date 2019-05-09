
from docxtpl import DocxTemplate

class GenDoc():
    def get(self, src_file, values, out_File):
        "Генерация документа"
        doc = DocxTemplate(src_file)
        doc.render(values)
        doc.save(out_File)