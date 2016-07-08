# -*- encoding: utf-8 -*-

from PyPDF2 import PdfFileReader
import os

def printMeta():
    for dirpath, dirnames, files in os.walk("doc_pdf"):
        for name in files:
            ext = name.lower().rsplit('.', 1)[-1]
            if ext in ['pdf']:
                print "[+] Metadata for file: %s " %(dirpath+os.path.sep+name)
                pdfFile = PdfFileReader(file(dirpath+os.path.sep+name, 'rb'))
                docInfo = pdfFile.getDocumentInfo()
                for metaItem in docInfo:
                    print '[+] ' + metaItem + ':' + docInfo[metaItem]
            
printMeta()