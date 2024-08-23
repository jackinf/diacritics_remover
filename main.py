import pandas as pd
import unidecode
import re
import argparse
import os

def convert_to_string(value):
    """Convert value to string, return empty string if conversion fails."""
    try:
        return str(value) if not pd.isna(value) else ""
    except:
        return ""

def remove_diacritics(text):
    text = convert_to_string(text)
    return unidecode.unidecode(text)

def fix_spaces(text):
    text = convert_to_string(text)
    return text.replace(" ", "")

def fix_dot_dash(text):
    text = convert_to_string(text)
    return text.replace("-", "").replace(".", "")

def fix_comma_apostrophe(text):
    text = convert_to_string(text)
    return text.replace(",", "").replace("'", "").replace("/", "").replace("#", "")

def remove_brackets(text):
    text = convert_to_string(text)
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
                df[column] = df[column].apply(lambda x: func(x))

    # Save the modified DataFrame to a new Excel file
    df.to_excel(output_file, index=False)
    print(f"Processed file saved to: {output_file}")

def main():
    # Create argument parser
    parser = argparse.ArgumentParser(description="Process an Excel file with specified transformations.")
    parser.add_argument('input_file', type=str, help='The name of the input Excel file (e.g., input_file.xlsx)')
    parser.add_argument('output_file', type=str, nargs='?', default=None,
                        help='The name of the output Excel file (e.g., output_file_processed.xlsx). If not provided, will append "_processed" to the input file name.')

    # Parse arguments
    args = parser.parse_args()

    # Determine the output file name
    if args.output_file is None:
        base, ext = os.path.splitext(args.input_file)
        args.output_file = f"{base}_processed{ext}"

    # Process the Excel file
    process_excel(args.input_file, args.output_file)

if __name__ == "__main__":
    main()
