import ezsheets


spreadsheet = ezsheets.upload('path/to/your/spreadsheet.xlsx')

spreadsheet_id = spreadsheet.spreadsheetId

output_path_excel = 'path/to/downloaded/file.xlsx'
output_path_ods = 'path/to/downloaded/file.ods'


spreadsheet.downloadAsExcel(output_path_excel)

spreadsheet.downloadAsODS(output_path_ods)

print(f"Spreadsheet ID: {spreadsheet_id}")
print(f"Downloaded as Excel: {output_path_excel}")
print(f"Downloaded as ODS: {output_path_ods}")
