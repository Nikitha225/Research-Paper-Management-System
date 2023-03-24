from PDFParser import PDFParser
import sys

def main(pdfPath):
    pdfPath = pdfPath.strip()
    pdfParser = PDFParser(pdfPath)


if __name__ == '__main__':
    main(sys.argv[1])