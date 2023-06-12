import os
#import textract
import pdfplumber
import re
import math


def pdf_to_text(pdf_folder_path):
    # Get the current directory path
    current_directory = os.getcwd()
    # Specify the folder names
    pdf_folder = "PDF FILES"
    text_folder = "Text files"
    # Construct the full directory paths
    pdf_directory = os.path.join(current_directory, pdf_folder)
    text_directory = os.path.join(current_directory, text_folder)
    # Iterate over the PDF files in the directory
    for filename in os.listdir(pdf_directory):
        if filename.endswith('.pdf'):
        # Full path of the PDF file
            pdf_path = os.path.join(pdf_directory, filename)
            # Read the text content from the PDF file
            text_content = textract.process(pdf_path, method='pdfminer')
            # Create the text file path
            text_filename = os.path.splitext(filename)[0] + '.txt'
            text_path = os.path.join(text_directory, text_filename)
            # Save the extracted text to a text file
            with open(text_path, 'w', encoding='utf-8') as text_file:
                text_file.write(text_content.decode('utf-8'))
            print(f"Converted {filename} to {text_filename}")


def convert_to_text(pdf):
    proposal_text = ""
    for page in pdf.pages:
        proposal_text += page.extract_text()
    return proposal_text


def extract_title(proposal_text):
    title = re.search(r"Title:(.*?)\n", proposal_text, re.I)
    title = title.group(1).strip() if title else None
    return title


def extract_PI(proposal_text):
    principal_investigator = re.search(r"Principal Investigator:(.*?)\n",
                                        proposal_text, re.I)
    principal_investigator = principal_investigator.group(
        1).strip() if principal_investigator else None
    return principal_investigator


def extract_date(proposal_text):
    date = re.search(r"Date/Time Generated:(.*?)\n", proposal_text, re.I)
    date = date.group(1).strip() if date else None
    return date


def calculate_title(title):
    title_length = len(title.strip())
    length_pass = False

    if title_length <= 80:
        length_pass = True

    return title_length, length_pass


def file_size(pdf_path):
    file_size = os.path.getsize(pdf_path) / (1024 * 1024)
    file_size = round(file_size,2)
    file_check = False

    if file_size <= 15:
        file_check = True

    return file_size, file_check


def extract_phd(pdf_text):
    question = "what year was your PhD?"
    index = pdf_text.find(question)
    return (pdf_text[index + 43:index + 46])


def extract_Early_Track(pdf):
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
    basename = (os.path.basename(pdf_path))
    submitter = ((os.path.splitext(basename)[0]).split("_"))[2]
    
    return submitter

def check_pi_and_submitter(pi, submitted_by):
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
        if last_name in (submitted_by.lower()).strip():
            alert_to_same = True

    return alert_to_same



    

    

    
    


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
