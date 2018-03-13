import xlrd

from library.getPath import data_path


def get_data(filename):
    wb = xlrd.open_workbook(data_path(filename))
    sheet = wb.sheet_by_name('Sheet1')
    data = []
    for i in range(1, sheet.nrows):
        data.append(sheet.row_values(i))
    return data


# print(get_data('api_data.xls'))




