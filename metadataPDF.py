import pyPdf 
import optparse 
from pyPdf import PdfFileReader
import sys, re, os
import myparser

from pdfminer.psparser import PSKeyword, PSLiteral
from pdfminer.pdfparser import PDFDocument, PDFParser
from pdfminer.pdftypes import PDFStream, PDFObjRef, resolve1, stream_value
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter, process_pdf
from pdfminer.pdfdevice import PDFDevice, TagExtractor
from pdfminer.converter import XMLConverter, HTMLConverter, TextConverter
from pdfminer.cmapdb import CMapDB
from pdfminer.layout import LAParams


def printMeta(fileName):
 pdfFile = PdfFileReader(file(fileName, 'rb'))
 docInfo = pdfFile.getDocumentInfo()
 print '[*] PDF MetaData For: ' + str(fileName)
 for metaItem in docInfo:
  print '[+] ' + metaItem.encode('utf-8') + ':' + docInfo[metaItem].encode('utf-8')

def getHostnames(text):
 em=myparser.parser(text)
 print em.hostnames()
 
def getPeople_linkedin(text):
 em=myparser.parser(text)
 print em.people_linkedin()
 
def getURLS(text):
 em=myparser.parser(text)
 print em.fileurls()
 
def getEmails(text):
 em=myparser.parser(text)
 print em.emails()

def getText(fileName):
 try:
  password =''
  pagenos = set()
  maxpages = 0
  codec = 'utf-8'
  caching = True
  laparams = LAParams()
  rsrcmgr = PDFResourceManager(caching=caching)
  outfp = file('temppdf.txt','w')
  device = TextConverter(rsrcmgr, outfp, codec=codec, laparams=laparams)
  fname= fileName
  fp = file(fname, 'rb')
  process_pdf(rsrcmgr, device, fp, pagenos, maxpages=maxpages, password=password,caching=caching, check_extractable=True)
  fp.close()
  device.close()
  outfp.close()
  infp = file('temppdf.txt','rb')
  text=infp.read()
  infp.close()
  os.remove('temppdf.txt')
  return text
 except Exception,e:
  return e

def getData(fileName):
 doc = PDFDocument()
 fp = file(fileName, 'rb')
 parser = PDFParser(fp)
 try:
  parser.set_document(doc)
  doc.set_parser(parser)
 except:
  return "error"
   
 parser.close()
 fp.close()
 try:
  for xref in doc.xrefs:
   info_ref=xref.trailer.get('Info')
   if info_ref:
    info=resolve1(info_ref)
   metadata=info
   if metadata == None:
    return "Empty metadata"
   else:
    if metadata.has_key('Author'):
     print("Author "+metadata['Author'])
    if metadata.has_key('Company'):
     print("Company "+metadata['Company'])
    if metadata.has_key('Producer'):
     print("Producer "+metadata['Producer'])
    if metadata.has_key('Creator'):
     print("Creator "+metadata['Creator'])         
 except Exception,e:
  print "\t [x] Error in PDF extractor"
  return e 
  

def main():
 parser = optparse.OptionParser('usage %prog '+ '--FILE ')
 parser.add_option('--FILE', dest='fileName', type='string', help='specify PDF file name')
 (options, args) = parser.parse_args()
 fileName = options.fileName
 if fileName == None:
  print parser.usage 
  exit(0) 
 else: 
  printMeta(fileName)
  getData(fileName)
  text=getText(fileName)
  getEmails(text)
  getURLS(text)
  getPeople_linkedin(text)
  
if __name__ == '__main__':
 main()