# Great for working with text in PDFs with complex layouts (tables, columns)
import pdfplumber
# For organizing and manipulating the extracted data
import pandas as pd
# For searching and matching
import re

# Define the PDF file path
pdf_path = r"C:\Users\rocke\Downloads\DLTAwardnees_2016.pdf"

# Initialize an empty list to store extracted data
data = []

# Open the PDF file
with pdfplumber.open(pdf_path) as pdf:
    # Iterate through each page in the PDF
    for page in pdf.pages:
        # Extract text from the page
        text = page.extract_text()

        # Check if text extraction was successful
        if text:
            # Split text into lines for easier processing
            lines = text.split('\n')

            # Initialize a dictionary to hold the extracted fields
            record = {
                "Field Contact": None,
                "Obligation Date": None,
                "Rural Development Approved Grant": None,
                "Program": None,
                "State": None,
                "Counties": None,
                "Recipient": None,
                "Recipient Contact": None,
                "Mailing Address": None,
                "Email Address": None,
                "Telephone": None,
                "Project Description": None,
                "Other Funding": None,
                "Total Project Cost": None,
            }

            # Use patterns for matching (re package)
            patterns = {
                "Field Contact": r'Field Contact:\s*(.*)',
                "Obligation Date": r'Obligation Date:s*(.*)',
                "Rural Development Approved Grant": r'Rural Development has approved a grant of \s*(.*)',
                "Program": r'Program:\s*(.*)',
                "State": r'State:\s*(.*)',
                "Counties": r'Counties:\s*(.*)',
                "Recipient": r'Recipient:\s*(.*)',
                "Recipient Contact": r'Recipient Contact:\s*(.*)',
                "Mailing Address": r'Mailing Address:\s*(.*)',
                "Email Address": r'Email Address:\s*(.*)',
                "Telephone": r'Telephone:\s*(.*)',
                "Project Description": r'Project Description:\s*(.*)',
                "Other Funding": r'Other Funding:\s*(.*)',
                "Total Project Cost": r'Total Project Cost:\s*(.*)'
            }

            # Iterate through each line to find and extract relevant information using regex
            for line in lines:
                for key, pattern in patterns.items():
                    match = re.search(pattern, line)
                    if match:
                        record[key] = match.group(1).strip()


            # Append the extracted record to the data list if it contains any relevant data
            if any(record.values()):
                data.append(record)

# Create a DataFrame from the list of records
df = pd.DataFrame(data)

# Save the DataFrame to an Excel file
excel_path = 'extracted_data.xlsx'
df.to_excel(excel_path, index=False)