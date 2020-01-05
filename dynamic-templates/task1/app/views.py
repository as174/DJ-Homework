from django.shortcuts import render
import csv
from app.settings import INFLATION_CSV

def inflation_view(request):
    template_name = 'inflation.html'

    # чтение csv-файла и заполнение контекста
    inflation_list = []
    with open(INFLATION_CSV, encoding='utf8', newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=';')
        for row in reader:
            row_list = []
            for cell in row:
                if cell:
                    row_list.append(cell)
                else:
                    row_list.append('-')
            inflation_list.append(row_list)


    context = {
                'table_header': inflation_list[0],
                'table_body': inflation_list[1:]
                }

    return render(request, template_name,
                  context)