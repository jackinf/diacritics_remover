import pandas as pd
import unidecode
import re
import argparse

def remove_diacritics(text):
    return unidecode.unidecode(text)

def fix_spaces(text):
    return text.replace(" ", "")

def fix_dot_dash(text):
    return text.replace("-", "").replace(".", "")

def fix_comma_apostrophe(text):
    return text.replace(",", "").replace("'", "").replace("/", "").replace("#", "")

def remove_brackets(text):
    text = re.sub(r'\(.*?\)', '', text)
    return ' '.join(text.split())

def process_excel(input_file, output_file):
    # Read the Excel file
    df = pd.read_excel(input_file, sheet_name=0)

    # Define header names for transformations
    transformations = {
        "Worker": [remove_brackets, remove_diacritics, fix_dot_dash, fix_comma_apostrophe],
        "Team Member ID": [],
        "Grafana Email": [],
        "Active Status": [remove_diacritics],
        "Termination Date": [],
        "Legacy ID": [],
        "Legal Name - First Name": [remove_diacritics, fix_dot_dash, fix_comma_apostrophe],
        "Legal Name - Last Name": [remove_diacritics, fix_dot_dash, fix_comma_apostrophe],
        "Company": [remove_diacritics],
        "Pay Group": [remove_diacritics],
        "Primary Address - Formatted Line 1": [remove_diacritics, fix_dot_dash, fix_comma_apostrophe],
        "Primary Address - Formatted Line 2": [remove_diacritics, fix_dot_dash, fix_comma_apostrophe],
        "Primary Home Address - City": [remove_diacritics, fix_dot_dash, fix_comma_apostrophe],
        "Primary Address - State/Province": [remove_diacritics, fix_dot_dash, fix_comma_apostrophe],
        "Primary Home Address - Postal Code": [fix_dot_dash, fix_comma_apostrophe],
        "Country": [remove_diacritics],
        "Cost Center - ID": [],
        "Social Security Number - Formatted": [],
        "National Identifiers": [],
        "Team Member Type": [],
        "Currency": [],
        "Account Type": [],
        "Payment Method": [],
        "Account Name": [remove_diacritics],
        "IBAN": [fix_spaces],
        "Account Number": [fix_dot_dash, fix_spaces],
        "Bank ID": [fix_dot_dash, fix_spaces],
        "Bank Identification Code": [],
        "Bank Name": [remove_diacritics],
        "Branch ID": [],
        "Amount": [],
        "Percent": [],
        "Payment Order": [],
        "Balance": []
    }

    # Process each column based on its header
    for column in df.columns:
        if column in transformations:
            for func in transformations[column]:
                df[column] = df[column].astype(str).apply(func)

    # Save the modified DataFrame to a new Excel file
    df.to_excel(output_file, index=False)
    print(f"Processed file saved to: {output_file}")

def main():
    # Create argument parser
    parser = argparse.ArgumentParser(description="Process an Excel file with specified transformations.")
    parser.add_argument('input_file', type=str, help='The name of the input Excel file (e.g., input_file.xlsx)')
    parser.add_argument('output_file', type=str, help='The name of the output Excel file (e.g., output_file_processed.xlsx)')

    # Parse arguments
    args = parser.parse_args()

    # Process the Excel file
    process_excel(args.input_file, args.output_file)

if __name__ == "__main__":
    main()
