from docxtpl import DocxTemplate

def docGen(templateFile, values, outputFile):
    doc = DocxTemplate(templateFile)
    doc.render(values)
    doc.save(outputFile)

values = {
    "course" : "3",
    "group" : "РИС",
    "fio" : "Европян А. Б.",
    "mobile" : "8 800 555 35 35",
    "active" : "учебной",
}
docGen("documents/SchApp.docx", values, "docOut.docx")