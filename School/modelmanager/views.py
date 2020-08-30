from django.db.models import Count
from django.shortcuts import render

# Create your views here.
from .models import Document


def modelmanager(request):
    # data = Document.objects.greter_than(800)
    # data = Document.objects.pdfs().greter_than(800).all()
    # data = Document.objects.all()
    # data = Document.objects.annotate(book_count=Count('file_type')).order_by('id')
    data = Document.objects.greter_than(800).all()
    # data = Document.objects.all()
    # # data.objects.filter(title='Matilda')
    # data2 = Document.objects.count()

    return render(request, 'manager/index.html', {'data': data })