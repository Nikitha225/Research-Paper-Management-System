import json
from pdf_to_json import pdf_to_json
from clean_json_data import clean_json_data
from push_data_to_db import get_database
from output_json import output_json_data
import os

class PDFParser:

  def __init__(self, path):
    self.filePath = path
    self.jsonPath = path[:-4] + '.json'
    self.outputJsonPath = path[:-4] + '_output.json'
    self.parse_pdf_to_json()
    
    

  def clean(self):
    try:
      # os.remove(self.filePath)
      os.remove(self.jsonPath)
      os.remove(self.outputJsonPath)
    except Exception as e:
      print('An unexpected error happened in main.py > clean function' + str(e))

  
  def parse_pdf_to_json(self):
    try:
      pdf_to_json(self.filePath)
      clean_json_data(self.jsonPath)
      output_json_data(self.jsonPath)
      self.insert_data_to_db()
    except:
       print('An unexpected error happened in main.py > parse_pdf_to_json function')
       self.clean()

  
  def insert_data_to_db(self):
    try:
      dbname = get_database()
      collection_name = dbname["documents"]
      with open(self.outputJsonPath, "r", errors="ignore") as read_file:
        json_data = json.load(read_file)
        collection_name.insert_one(json_data)
      # self.clean()
      print("------------------- stage 4 -------------------------\n")
      print("Pushed the output Json to database successfully and cleaned the json files \n")
    except:
       print('An unexpected error happened in main.py > insert_data_to_db function')
       self.clean()




PDFParser('./NetSquid.pdf')
