import openpyxl
ex_doc = openpyxl.load_workbook('/Users/satishbhambri/Downloads/DeAnna Toggl_projects_2017-01-01_to_2017-12-31 (1).xls.xlsx')

print type(ex_doc)

print ex_doc['Time(h)'].values

