# https://judge.softuni.org/Contests/Practice/Index/2303#1
import re

number_of_barcodes = int(input())
valid_barcodes = []

for _ in range(number_of_barcodes):
    barcode = input()
    barcode_pattern = r'\@\#+[A-Z][A-Za-z0-9]{4,}[A-Z]\@\#+'
    match = re.findall(barcode_pattern, barcode)
    if not match:
        print('Invalid barcode')
    elif match:
        valid_barcodes.append(barcode)

    for barcode in valid_barcodes:
        extract_number = re.findall('\d', barcode)
        if not extract_number:
            print('Product group: 00')
        else:
            print(f"Product group: {''.join(extract_number)}")
        valid_barcodes = []
