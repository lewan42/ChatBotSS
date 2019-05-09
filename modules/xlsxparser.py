import openpyxl

class XLSXExporter():

    def export(self, path):
        wb = openpyxl.load_workbook(path)
        sheet = wb.active 
        text = ""
        for row in range(1, sheet.max_row):
            for column in range(1, sheet.max_column):
                value = sheet.cell(row, column).value
                if value:
                    text += str(value) + "\t"
                else:
                    text += "\t"
            text += "\n"
        
        return text