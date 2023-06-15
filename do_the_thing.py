from helper_functions import extract_title
from helper_functions import convert_to_text
from helper_functions import extract_PI
from helper_functions import extract_date
from helper_functions import calculate_title
from helper_functions import file_size
#from helper_functions import extract_font_and_margin
from helper_functions import extract_phd
from helper_functions import extract_Early_Track
from helper_functions import extract_submitted_by
from helper_functions import check_pi_and_submitter
from excel_functions import add_info_to_excel
from helper_functions import extract_first_eight_chars
#from helper_functions import extract_narrative
import re
import os
from PyPDF2 import PdfReader
import textract


def check_all(pdf_directory):

    all_pdfs = []

    for file in os.listdir(pdf_directory):
        print(file)

        all_info = {}

        pdf_path = os.path.join(pdf_directory, file)

        # open the file
        with open(pdf_path, "rb") as f:
            proposal = PdfReader(f)

            # # get font sizes
            # font_sizes = get_font_sizes(proposal)
            # print(font_sizes)

            # convert to text
            pdf_text = convert_to_text(proposal)

            # extract title
            title = extract_title(pdf_text)
            all_info["title"] = title

            # calculate title length and pass/fail
            title_length, length_pass = calculate_title(title)
            all_info["title length"] = title_length
            all_info["length check"] = length_pass

            # extract PI
            pi = extract_PI(pdf_text)
            all_info["PI"] = pi

            # extract submitted by
            submitted_by = extract_submitted_by(pdf_path)
            all_info["submitted by"] = submitted_by

            pi_vs_submitter_alert = check_pi_and_submitter(pi, submitted_by)
            all_info["pi_submitter_alert"] = pi_vs_submitter_alert

            # extract date
            date = extract_date(pdf_text)
            all_info["date"] = date

            # extract proposal number
            first_eight_chars = extract_first_eight_chars(pdf_path)
            all_info["proposal number"] = first_eight_chars

            # extract file size
            pdf_size, file_check = file_size(pdf_path)
            all_info["file size"] = pdf_size
            all_info["file check"] = file_check

            #answering the PHD question
            phd = extract_phd(pdf_text)
            all_info["phd"] = phd
            
            #answering the early track 
            EarlyTrack = extract_Early_Track(proposal)
            all_info["EarlyTrack"] = EarlyTrack

            #extract_narrative(pdf_text)



            # # check margin sizes
            # font_size, left_margin, right_margin, top_margin, bottom_margin = extract_font_and_margin(
            #   pdf_path)
            # all_info["font size"] = font_size
            # all_info["left margin"] = left_margin
            # all_info["right_margin"] = right_margin
            # all_info["top_margin"] = top_margin
            # all_info["bottom_margin"] = bottom_margin

            # print(all_info,)

            # print("**********")

            all_pdfs.append(all_info) 
            
    for pdf_info in all_pdfs:
        print(pdf_info)
        print("----------------------")




    # add all collected info to excel
    #excel_path = "/Users/cstone/Documents/RapidPrototypingLab/GitRepos/proposal_checks/text_excel.xlsx"
    excel_path = "template.xlsx"
    add_info_to_excel(excel_path, all_pdfs)
            

    # add all collected info to the excel
    




check_all("PDF FILES") 

