from django.shortcuts import render

from .models import db_table

def index(request):
    db_record = db_table(db_text_column='ใในใ', db_num_column=1)
    db_record.save()

    params = {'db_records': db_records}
    return render(request, 'dbtest/index.html', params)