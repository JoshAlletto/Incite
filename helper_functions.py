import os
import re

def convert_to_text(pdf):
    """ convert_to_text

    Description: 
        Converts PDF from PDF reader to string of all text

    Inputs: 
        pdf (PDFREeader object): PDF reader object intitialized with the pdf file path 

    Returns: 
        proposal_text (string): one string containing all contents of pdf file 
    
    """
    proposal_text = ""
    for page in pdf.pages:
        proposal_text += page.extract_text()
    return proposal_text

def extract_title(proposal_text):
    """ extract_title

    Description:
        Extracts the title from the proposal text 

    Inputs:
        proposal_text (string): The text containing the proposal contents.

    Returns:
        title (string): The extracted title or none if found.
    """
    title = re.search(r"Title:(.*?)\n", proposal_text, re.I)
    title = title.group(1).strip() if title else None
    return title

def extract_PI(proposal_text):
    """ extract_PI
    
      Description:
        Extracts the Principal Investigator (PI) from the proposal text

    Inputs:
        proposal_text (string): The text containing the proposal contents.

    Returns:
        principal_investigator (string): The extracted PI or none if not found.
    """
    principal_investigator = re.search(r"Principal Investigator:(.*?)\n",
                                        proposal_text, re.I)
    principal_investigator = principal_investigator.group(
        1).strip() if principal_investigator else None
    return principal_investigator

def extract_date(proposal_text):
    """ extract_date

    Description:
        Extracts the date/time generated from the proposal text

    Inputs:
        proposal_text (string): The text containing the proposal contents.

    Returns:
        date (string): The extracted date/time or None if not found.
    """
    date = re.search(r"Date/Time Generated:(.*?)\n", proposal_text, re.I)
    date = date.group(1).strip() if date else None
    return date

def calculate_title(title):
    """ calculate_title

    Description:
        Calculates the length of the title and checks if it passes a maximum length of 80 characters.

    Inputs:
        title (string): The title to be evaluated.

    Returns:
        title_length (int): The length of the title.
        length_pass (bool): Indicates if the title length is within the maximum limit with a True or False.
    """
    title_length = len(title.strip())
    length_pass = False

    if title_length <= 80:
        length_pass = True

    return title_length, length_pass

def extract_first_eight_chars(pdf_path):
    """ extract_first_eight_chars

    Description:
        Extracts the first eight characters from the base name of the PDF file

    Inputs:
        pdf_path (string): The path to the PDF file.

    Returns:
        first_eight_chars (string): The first eight characters of the PDF base name.
    """
    pdf_filename = os.path.splitext(os.path.basename(pdf_path))[0]
    first_eight_chars = pdf_filename[:8]
    return first_eight_chars

def file_size(pdf_path):
    """ file_size

    Description:
        Calculates the size of a PDF file in megabytes and checks if it is within a maximum size of 15MB.

    Inputs:
        pdf_path (string): The path to the PDF file.

    Returns:
        file_size (float): The size of the PDF file in megabytes, rounded to two decimal places.
        file_check (bool): Indicates if the file size is within the maximum limit (True) or not (False).
    """
    file_size = os.path.getsize(pdf_path) / (1024 * 1024)
    file_size = round(file_size,2)
    file_check = False

    if file_size <= 15:
        file_check = True

    return file_size, file_check

def extract_phd(pdf_text):
    """ extract_phd

    Description:
        Extracts the year when the PhD was obtained from the PDF text.

    Inputs:
        pdf_text (string): The text content of the PDF file.

    Returns:
        phd_year (string): The extracted year when the PhD was obtained.
    """
    question = "what year was your PhD?"
    index = pdf_text.find(question)
    return (pdf_text[index + 43:index + 46])

def extract_Early_Track(pdf):
    """ extract_Early_Track

    Description:
        Extracts the answer to a question related to the Early Track from the PDF.

    Inputs:
        pdf (PDFReader object): PDF reader object initialized with the PDF file.

    Returns:
        answer (string): The extracted answer to the Early Track question or None if not found.
    """
    question = "Choosing this does not reduce your chances of receiving an award."
    num_pages = len(pdf.pages)
    answer = None
    for page_num in range(num_pages):
        page = pdf.pages[page_num]
        text = page.extract_text()
        if not text.find(question) == -1:
            text_lines = text.split("\n")
            text_list = [line.strip() for line in text_lines if line.strip()]

            for i in range(len(text_list)):
                if text_list[i].startswith("If you are within"):
                    num_lines_remaining = len(text_list[i:])
                    if num_lines_remaining >= 5:
                        answer = text_list[i + 2]
                    else:  # answer got cut off
                        next_page = pdf.pages[page_num + 1]
                        next_page_text = next_page.extract_text()
                        next_text_lines = next_page_text.split("\n")
                        next_text_list = [
                            line.strip() for line in next_text_lines if line.strip()
                        ]
                        answer = next_text_list[4 - num_lines_remaining]
    return answer

def extract_submitted_by(pdf_path):
    """ extract_submitted_by

    Description:
        Extracts the name of the submitter from the PDF file name.

    Inputs:
        pdf_path (string): The path to the PDF file.

    Returns:
        submitter (string): The name of the submitter extracted from the PDF file name.
    """ 
    basename = (os.path.basename(pdf_path))
    submitter = ((os.path.splitext(basename)[0]).split("_"))[2]
    
    return submitter

def check_pi_and_submitter(pi, submitted_by):
    """ check_pi_and_submitter

    Description:
        Checks if the last name of the Principal Investigator (PI) is present in the "submitted by" string.

    Inputs:
        pi (string): The name of the Principal Investigator.
        submitted_by (string): The "submitted by" string.

    Returns:
        alert_to_same (bool): Indicates if the last name of the PI is not present in the "submitted by" string (True) or not (False).
    """
    # first_name = None
    last_name = None
    alert_to_same = False

    try: 
        last_name = pi.split(" ")[-1]
        last_name = (last_name.lower()).strip()
    except Exception as e: 
        print(e)

    # check if last name in submitted by string
    if not last_name == None:
        if not last_name in (submitted_by.lower()).strip():
            alert_to_same = True
    return alert_to_same
#def extract_narrative(pdf_text):
    pdf_text = pdf_text.lower()
    count = pdf_text.count("significance of research")
    print("appears: times")
    print(count)


    

    

    
    


# def extract_font_and_margin(pdf_path):
#   with pdfplumber.open(pdf_path) as pdf:
#     page = pdf.pages[0]

#   font_sizes = get_font_sizes(pdf_path)
#   for font_size in font_sizes:
#     print(font_size)

#   font_size = []
#   for text in page.extract.words():
#     font_size.append(text["size"])

#   left_margin = page.crop((0, 0, 10, page.height)).width
#   right_margin = page.crop((page.width - 10, 0, page.width, page.height)).width
#   top_margin = page.crop((0, 0, page.width, 10)).height
#   bottom_margin = page.crop(
#     (0, page.height - 10, page.width, page.height)).height

#   return font_size, left_margin, right_margin, top_margin, bottom_margin

# ------------------
# def get_font_sizes(pdf):

#   print("method called")

#   font_sizes = set()
#   num_pages = len(pdf.pages)
#   for page_num in range(num_pages):
#     print(page_num)
#     page = pdf.pages[page_num]
#     resources = page['/Resources']
#     if '/Resources' in page.extract_text():
#       print("FOUND RESOURCES")
#     else:
#       print("no resources found")

#     print(resources)
#     if '/Font' in resources:
#       fonts = resources['/Font']
#       for font in fonts.values():
#         if '/BaseFont' in font:
#           font_size = font['/BaseFont']
#           font_sizes.add(font_size)

#     return font_sizes

# def get_font_sizes(pdf_path):
#   with pdfplumber.open(pdf_path) as pdf:
#     for page in pdf.pages:
#       for obj in page.extract_words():
#         text = obj['text']
#         # size = obj['size']
#         # font = obj['fontname']

#         print(f"Text: {text}")
