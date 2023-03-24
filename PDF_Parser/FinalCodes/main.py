import json
from pdf_to_json import pdf_to_json
from clean_json_data import clean_json_data
from push_data_to_db import get_database

class PDFParser:

  def __init__(self, path):
    self.filePath = path
    self.jsonPath = path[:-4] + '.json'
    self.cleanedJsonPath = path[:-4] + '_clean.json'
  
  def parse_pdf_to_json(self):
    try:
      pdf_to_json(self.filePath)
      clean_json_data(self.jsonPath)
    except:
       print('An unexpected error happened in main.py > parse_pdf_to_json function')

  
  def insert_data_to_db(self):
    try:
      dbname = get_database()
      collection_name = dbname["researchPaperDocs"]
      with open(self.cleanedJsonPath, "r", errors="ignore") as read_file:
              json_data = json.load(read_file)
              collection_name.insert_one(json_data)
    except:
       print('An unexpected error happened in main.py > insert_data_to_db function')

pdfParser = PDFParser('./NetSquid/NetSquid.pdf')
pdfParser.parse_pdf_to_json()
pdfParser.insert_data_to_db()