import openpyxl
import sys

def read_excel_file(file_path):
   
    wb = openpyxl.load_workbook(file_path)
    sheet = wb.active
    columns_data = []

    for col in sheet.iter_cols(values_only=True):
        columns_data.append(list(col))
    
    return columns_data

def write_to_text_files(columns_data, output_file_paths):
   
    for col_index, data in enumerate(columns_data):
        with open(output_file_paths[col_index], 'w', encoding='utf-8') as file:
            for item in data:
                if item is not None:
                    file.write(str(item) + '\n')

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("使用法: python script.py 入力Excelファイル テキストファイル1 テキストファイル2 ...")
        sys.exit(1)

    input_excel_path = sys.argv[1]
    output_text_file_paths = sys.argv[2:]

    columns_data = read_excel_file(input_excel_path)
    
    if len(output_text_file_paths) < len(columns_data):
        print("エラー: 出力テキストファイルの数が入力Excelファイルの列の数より少ないです。")
        sys.exit(1)

    write_to_text_files(columns_data, output_text_file_paths)

    print('完了')
