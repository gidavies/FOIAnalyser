from docx import Document
from presidio_analyzer import AnalyzerEngine

import sys

# Args: 
# 0: Script name
# 1: Word doc to analyze
# 2: FOI Profile (Victim, Suspect, Informant)

if len(sys.argv) == 3:
    doc = sys.argv[1]
    foiprofile = sys.argv[2]
else:
    exampleusage = sys.argv[0] + " worddoc.docx" + " victim"
    raise ValueError('Arguments required: word doc and FOI profile e.g.: ' + exampleusage)

print("\n===============================================")
print("\nPreparing to analyse:", doc)
print("FOI profile:", foiprofile)
print("\n===============================================")

document = Document(doc)

print("\n===============================================")
print("\nDocument properties for", doc)
print("Author:", document.core_properties.author)
print("Last Modified By:", document.core_properties.last_modified_by)
print("Date:", document.core_properties.modified)
print("\n===============================================")

paras = document.paragraphs

doctext = ""
for i in paras:
    doctext += i.text

print("\n===============================================")
print("Extracted text from", doc)
print(doctext)
print("\n===============================================")

engine = AnalyzerEngine()

response = engine.analyze(correlation_id=0,
                          text = doctext,
                          entities=[],
                          language='en',
                          all_fields=True,
                          score_threshold=0.5)

for item in response:
    print("Start = {}, end = {}, entity = {}, confidence = {}".format(item.start,
                                                                      item.end,
                                                                      item.entity_type,
                                                                      item.score))