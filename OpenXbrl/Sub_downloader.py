import requests
import re
import pandas as pd
import time
from bs4 import BeautifulSoup

class Sub_Downloader() :
    
    def _load_url(self, url : str) :
    
    # Helper function to download URLs from EDGAR
    
    # Wait a bit as per SEC Edgar rate use requirements
        time.sleep(0.11)
  
        response = requests.get(url,headers={"User-Agent": "Mozilla/5.0"})
        if response.status_code != 200:
            raise Exception(f"Failed to fetch data from URL: {url}")
            #raise error if not able too retrieve error
        return response.content
     # end _load_url()
    

    def generate_flat_html( self, url : str ) -> str :
   
    #Filters out Index and return flat html of report :
    #Parameters:
        #url   : valid SEC EDGAR url of primary filing document
    #Returns:
      #flat html of report

    # Assume can ignore all before Table of Contents
    # This skips some XBRL and standard title page

        raw_file = (self._load_url( url ))
        soup = BeautifulSoup(raw_file,"html")

        doc_start_pattern = re.compile(r'<DOCUMENT>')
        doc_end_pattern = re.compile(r'</DOCUMENT>')

        type_pattern = re.compile(r'<TYPE>[^\n]+')
        #Either 10-K or 10-Q

        doc_start_is = [x.end() for x in doc_start_pattern.finditer(raw_file)]
        doc_end_is = [x.start() for x in doc_end_pattern.finditer(raw_file)]
        #Locate start and end of document

        doc_types = [x[len('<TYPE>'):] for x in type_pattern.findall(raw_file)]
        document = {}

        match = 0
        docType = ''
        file_name = ''
        for doc_type, doc_start, doc_end in zip(doc_types, doc_start_is, doc_end_is):
            if doc_type == '10-K':
                document[doc_type] = raw_file[doc_start:doc_end]
                docType = "10-K"
                match = 10
                #skips Table of Contents
                file_name = 'Output_10k.html'
                #return html for 10-K files

            elif doc_type == '10-Q':
                document[doc_type] = raw_file[doc_start:doc_end]
                docType = "10-Q"
                match = 3
                #skips Table of Contents
                file_name = 'Output_10q.html'
                #return html for 10-Q files

        regex = re.compile(r'(>Item(\s|&#160;|&nbsp;)(1)\.{0,1})|(ITEM\s(1))')

        match_positions = [match.start() for match in regex.finditer(document[docType])]

        document_content = document[docType][match_positions[match]:]

        document_content  = BeautifulSoup(document_content, 'lxml')

        refined_content = document_content.prettify()

        print(refined_content)
        with open(file_name, "w",encoding="utf-8") as text_file:
            text_file.write(refined_content)
        #save as html file

        text_file.close()
        # end generate_flat_html()