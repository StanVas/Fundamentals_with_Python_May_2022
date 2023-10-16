import re

number_of_barcodes = int(input())
pattern = r'([@][#]{1,})([A-Z][A-Za-z0-9]{4,}[A-Z])([@][#]{1,})'
for num in range(number_of_barcodes):
    barcode = input()
    result = re.findall(pattern, barcode)
    if not result:
        print("Invalid barcode")
    else:
        digits = re.findall(r'\d', barcode)
        if not digits:
            print("Product group: 00")
        else:
            print(f"Product group: {''.join(digits)}")
