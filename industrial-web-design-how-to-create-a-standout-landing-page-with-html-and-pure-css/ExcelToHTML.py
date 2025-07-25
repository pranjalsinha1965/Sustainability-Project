import pandas as pd

# Load data from Excel file
data = pd.read_excel('C:/Users/KIIT/Desktop/Book1.xlsx', engine='openpyxl')

# Write data to HTML file with formatting
with open('Railway.html', 'w') as f:
    f.write(data.to_html(index=False, classes='table', header=True, border=1, justify='left'))

# 1. Add this feature to importExportProject
