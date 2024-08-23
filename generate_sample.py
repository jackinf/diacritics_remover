if __name__ == '__main__':
    import pandas as pd

    # Create a dictionary with sample data
    data = {
        "Worker": ["John Doe", "Jane Smith"],
        "Team Member ID": ["12345", "67890"],
        "Grafana Email": ["john.doe@example.com", "jane.smith@example.com"],
        "Active Status": ["Activeååå", "Inactive"],
        "Termination Date": ["2024-01-01", ""],
        "Legacy ID": ["A1B2C3", "D4E5F6"],
        "Legal Name - First Name": ["John", "Jane"],
        "Legal Name - Last Name": ["Doe", "Smith"],
        "Company": ["Company A", "Company B"],
        "Pay Group": ["Group 1", "Group 2"],
        "Primary Address - Formatted Line 1": ["123 Elm St", "456 Oak Ave"],
        "Primary Address - Formatted Line 2": ["Apt 1", "Suite 200"],
        "Primary Home Address - City": ["Springfield", "Shelbyville"],
        "Primary Address - State/Province": ["IL", "IL"],
        "Primary Home Address - Postal Code": ["62701", "62702"],
        "Country": ["USA", "USA"],
        "Cost Center - ID": ["001", "002"],
        "Social Security Number - Formatted": ["123-45-6789", "987-65-4321"],
        "National Identifiers": ["ID123", "ID456"],
        "Team Member Type": ["Full-Time", "Part-Time"],
        "Currency": ["USD", "USD"],
        "Account Type": ["Checking", "Savings"],
        "Payment Method": ["Direct Deposit", "Check"],
        "Account Name": ["John Doe", "Jane Smith"],
        "IBAN": ["US1234567890", "US0987654321"],
        "Account Number": ["1234567890", "0987654321"],
        "Bank ID": ["BANK1", "BANK2"],
        "Bank Identification Code": ["BIC123", "BIC456"],
        "Bank Name": ["Bank A", "Bank B"],
        "Branch ID": ["BRANCH1", "BRANCH2"],
        "Amount": [1000.00, 2000.00],
        "Percent": [5.5, 10.0],
        "Payment Order": ["Order1", "Order2"],
        "Balance": [5000.00, 10000.00]
    }

    # Convert the dictionary into a DataFrame
    df = pd.DataFrame(data)

    # Save the DataFrame to an Excel file
    file_path = 'sample_data.xlsx'
    df.to_excel(file_path, index=False)

    print(f"Sample file created at: {file_path}")
