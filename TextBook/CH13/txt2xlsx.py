import openpyxl
import sys

def read_text_file(file_path):
   
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()
    return lines

def write_to_excel(file_paths, output_excel_path):
    
    wb = openpyxl.Workbook()
    sheet = wb.active

    for col_index, file_path in enumerate(file_paths):
        lines = read_text_file(file_path)
        col_letter = openpyxl.utils.get_column_letter(col_index + 1)

        for row_index, line in enumerate(lines):
            sheet[f'{col_letter}{row_index + 1}'] = line.strip()

    wb.save(output_excel_path)

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("使用法: python script.py 出力Excelファイル テキストファイル1 テキストファイル2 ...")
        sys.exit(1)

    output_excel_path = sys.argv[1]
    text_file_paths = sys.argv[2:]

    write_to_excel(text_file_paths, output_excel_path)

    print('完了')
