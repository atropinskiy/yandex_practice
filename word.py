import docx
import os


doc = docx.Document("F:/MyGit/yandex_practice/datasets/sample.docx")


print(len(doc.paragraphs))