from django.core import serializers
from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.urls import reverse, reverse_lazy
from django.views import View
from django.views.generic import CreateView, UpdateView, DeleteView, ListView, DetailView

from .models import *
from .form import *
from django.contrib import messages
import mimetypes
# Create your views here.


class AuthorListView(View):
    form_class = AuthorForm
    model = Author

    def get(self, request):
        authors = Author.objects.all().order_by('-id')
        contex = {'authors': authors}
        return render(request, 'author/index.html', contex)


class AuthorCreateView(CreateView):
    model = Author
    form_class = AuthorForm
    template_name = 'author/create.html'
    success_url = reverse_lazy('authors')

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            instance = form.save()
            ser_instance = serializers.serialize('json', [instance, ])
            return JsonResponse({"instance": ser_instance}, status=200)
        else:
            return JsonResponse({"error": form.errors}, json_dumps_params={'indent': 2})


class AuthorEditView(UpdateView):
    model = Author
    template_name = 'author/update.html'
    context_object_name = 'author'
    fields = ('name',  'description',)
    success_url = reverse_lazy('authors')


class AuthorUpdateView(View):
    form_class = AuthorForm

    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():
            author = Author.objects.get(pk=request.POST.get('author_id'))
            author.name = request.POST.get('name')
            author.description = request.POST.get('description', )
            author.save()
            return JsonResponse({"instance": 'messages'}, status=200)
        else:
            return JsonResponse({"error": form.errors}, json_dumps_params={'indent': 2})


class AuthorDeleteView(DeleteView):
    def get(self, request):
        id1 = request.GET.get('id', None)
        Author.objects.get(id=id1).delete()
        data = {
            'deleted': True
        }
        return JsonResponse(data)


#-----------------------publisher------------------------
class PublisherListView(ListView):
    form_class = PublisherForm
    model = Publisher

    def get(self, request):
        publishers = Publisher.objects.all().order_by('-id')
        contex = {'publishers': publishers}
        return render(request, 'publisher/index.html', contex)


class PublisherAddView(CreateView):
    model = Publisher
    form_class = PublisherForm
    template_name = 'publisher/create.html'
    success_url = reverse_lazy('publishers')

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            instance = form.save()
            ser_instance = serializers.serialize('json', [instance, ])
            return JsonResponse({"instance": ser_instance}, status=200)
        else:
            return JsonResponse({"error": form.errors}, json_dumps_params={'indent': 2})


class PublisherEditView(UpdateView):
    model = Publisher
    template_name = 'publisher/update.html'
    context_object_name = 'publisher'
    fields = ('name', 'description',)
    success_url = reverse_lazy('publishers')


class PublisherUpdateView(View):
    form_class = PublisherForm

    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():
            rooms = Publisher.objects.get(pk=request.POST.get('publisher_id'))
            rooms.name = request.POST.get('name')
            rooms.description = request.POST.get('description', )
            rooms.save()
            return JsonResponse({"instance": 'messages'}, status=200)
        else:
            return JsonResponse({"error": form.errors}, json_dumps_params={'indent': 2})


class PublisherDeleteView(DeleteView):
    def get(self, request):
        id1 = request.GET.get('id', None)
        Publisher.objects.get(id=id1).delete()
        data = {
            'deleted': True
        }
        return JsonResponse(data)


#-----------------------subject------------------------
class SubjectListView(ListView):
    form_class = SubjectForm
    model = Subject

    def get(self, request):
        publishers = Subject.objects.all().order_by('-id')
        contex = {'subjects': publishers}
        return render(request, 'subject/index.html', contex)


class SubjectAddView(CreateView):
    model = Subject
    form_class = SubjectForm
    template_name = 'subject/create.html'
    success_url = reverse_lazy('subjects')

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            instance = form.save()
            ser_instance = serializers.serialize('json', [instance, ])
            return JsonResponse({"instance": ser_instance}, status=200)
        else:
            return JsonResponse({"error": form.errors}, json_dumps_params={'indent': 2})


class SubjectEditView(UpdateView):
    model = Subject
    template_name = 'subject/update.html'
    context_object_name = 'room'
    fields = ('name', 'description',)
    success_url = reverse_lazy('subjects')


class SubjectUpdateView(View):
    form_class = SubjectForm

    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():
            subject = Subject.objects.get(pk=request.POST.get('subject_id'))
            subject.name = request.POST.get('name')
            subject.description = request.POST.get('description', )
            subject.save()
            return JsonResponse({"instance": 'messages'}, status=200)
        else:
            return JsonResponse({"error": form.errors}, json_dumps_params={'indent': 2})


class SubjectDeleteView(DeleteView):
    def get(self, request):
        id1 = request.GET.get('id', None)
        Subject.objects.get(id=id1).delete()
        data = {
            'deleted': True
        }
        return JsonResponse(data)


#-----------------------book_language------------------------

class BookLanguageListView(ListView):
    model = BookLanguage
    context_object_name = 'book_language'
    form_class = BookLanguageForm
    initial = {'key': 'value'}
    template_name = 'book_language/index.html'

    def get(self, request):
        book_languagess = BookLanguage.objects.all().order_by('-id')
        form = self.form_class(initial=self.initial)
        context = {'book_languages': book_languagess, 'form': form}
        return render(request, self.template_name, context)


class BookLanguageAddView(CreateView):
    model = BookLanguage
    form_class = BookLanguageForm
    template_name = 'book_language/create.html'
    success_url = reverse_lazy('book_language_list')

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            instance = form.save()
            ser_instance = serializers.serialize('json', [instance, ])
            return JsonResponse({"instance": ser_instance}, status=200)
        else:
            return JsonResponse({"error": form.errors}, json_dumps_params={'indent': 2})


class BookLanguageEditView(UpdateView):
    model = BookLanguage
    template_name = 'book_language/update.html'
    context_object_name = 'room'
    fields = ('name', 'description',)
    success_url = reverse_lazy('room_list')


class BookLanguageUpdateView(View):
    form_class = BookLanguageForm

    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():
            rooms = BookLanguage.objects.get(pk=request.POST.get('book_lang_id'))
            rooms.name = request.POST.get('name')
            rooms.description = request.POST.get('description', )
            rooms.save()
            return JsonResponse({"instance": 'messages'}, status=200)
        else:
            return JsonResponse({"error": form.errors}, json_dumps_params={'indent': 2})


class BookLanguageDeleteView(DeleteView):
    def get(self, request):
        id1 = request.GET.get('id', None)
        BookLanguage.objects.get(id=id1).delete()
        data = {
            'deleted': True
        }
        return JsonResponse(data)


#-----------------------rack------------------------

class RackListView(ListView):
    model = Rack
    context_object_name = 'rack'
    form_class = RackForm
    initial = {'key': 'value'}
    template_name = 'rack/index.html'

    def get(self, request):
        racks = Rack.objects.all().order_by('-id')
        form = self.form_class(initial=self.initial)
        context = {'racks': racks, 'form': form}
        return render(request, self.template_name, context)


class RackAddView(CreateView):
    model = Rack
    form_class = RackForm
    template_name = 'rack/create.html'
    success_url = reverse_lazy('rack_list')

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            instance = form.save()
            ser_instance = serializers.serialize('json', [instance, ])
            return JsonResponse({"instance": ser_instance}, status=200)
        else:
            return JsonResponse({"error": form.errors}, json_dumps_params={'indent': 2})


class RoomEditView(UpdateView):
    model = Rack
    template_name = 'rack/update.html'
    context_object_name = 'rack'
    fields = ('number', 'name', )
    success_url = reverse_lazy('room_list')


class RoomUpdateView(View):
    form_class = RackForm

    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():
            rooms = Rack.objects.get(pk=request.POST.get('rack_id'))
            rooms.number = request.POST.get('number')
            rooms.name = request.POST.get('name', )
            rooms.save()
            return JsonResponse({"instance": 'messages'}, status=200)
        else:
            return JsonResponse({"error": form.errors}, json_dumps_params={'indent': 2})


class RackDeleteView(DeleteView):
    def get(self, request):
        id1 = request.GET.get('id', None)
        Rack.objects.get(id=id1).delete()
        data = {
            'deleted': True
        }
        return JsonResponse(data)



#-----------------------book------------------------

class BookListView(ListView):
    model = Book
    context_object_name = 'types'
    form_class = BookForm
    initial = {'key': 'value'}
    template_name = 'book/index.html'

    def get(self, request):
        books = Book.objects.all().order_by('-id')
        form = self.form_class(initial=self.initial)
        context = {'books': books, 'form': form}
        return render(request, self.template_name, context)


class BookAddView (CreateView):
    model = Book
    form_class = BookForm
    template_name = 'book/create.html'
    success_url = reverse_lazy('book_list')

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save()
            ser_instance = serializers.serialize('json', [instance, ])
            return JsonResponse({"instance": ser_instance}, status=200)
        else:
            return JsonResponse({"error": form.errors}, json_dumps_params={'indent': 2})


class BookEditView(UpdateView):
    model = Book
    template_name = 'book/update.html'
    context_object_name = 'room'
    fields = ('title', 'book_number', 'isbn_number', 'price', 'qty','publisher', 'author', 'subject', 'book_language', 'rack',
              'description', 'image', 'status',
              )
    success_url = reverse_lazy('book_list')


class BookUpdateView(View):
    model = Book
    form_class = BookForm

    def post(self, request):
        form = self.form_class(request.POST, request.FILES)

        if form.is_valid():
            book = Book.objects.get(pk=request.POST.get('book_id'))
            book.image = request.FILES.get('image')
            book.book_number = request.POST.get('book_number', )
            book.isbn_number = request.POST.get('isbn_number', )
            book.price = request.POST.get('price', )
            book.qty = request.POST.get('qty', )
            book.publisher_id = request.POST.get('publisher_id', )
            book.author_id = request.POST.get('author_id', )
            book.subject_id = request.POST.get('subject_id', )
            book.book_language_id = request.POST.get('book_language_id', )
            book.rack_id = request.POST.get('rack_id', )
            book.status = request.POST.get('status', )
            book.title = request.POST.get('title', )
            book.description = request.POST.get('description', )
            book.save()

            return JsonResponse({"instance": 'messages'}, status=200)
        else:
            return JsonResponse({"error": form.errors}, json_dumps_params={'indent': 2})


class BookDeleteView(DeleteView):
    def get(self, request):
        id1 = request.GET.get('id', None)
        Book.objects.get(id=id1).delete()
        data = {
            'deleted': True
        }
        return JsonResponse(data)


class BookDetailView(DetailView):
    queryset = Book.objects.all()
    template_name = "book/view.html"

    # def get(self, request, pk):
    #     book = Book.objects.filter(pk=pk)
    #     return render(request, 'book/view.html', {'book': book})


class EbookListView(ListView):
    model = EBook
    context_object_name = 'types'
    form_class = EBookForm
    initial = {'key': 'value'}
    template_name = 'ebook/index.html'

    def get(self, request):
        ebooks = EBook.objects.all().order_by('-id')
        form = self.form_class(initial=self.initial)
        context = {'ebooks': ebooks, 'form': form}
        return render(request, self.template_name, context)


def ebook_view(request, pk):
    ebook=EBook.objects.get(id=pk)
    context={'ebook':ebook}
    return render(request, 'ebook/view.html',context)


class AddEbookView(CreateView):
    model = EBook
    form_class = EBookForm
    template_name = 'ebook/create.html'
    success_url = reverse_lazy('ebook_list')

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save()
            ser_instance = serializers.serialize('json', [instance, ])
            return JsonResponse({"instance": ser_instance}, status=200)
        else:
            return JsonResponse({"error": form.errors}, json_dumps_params={'indent': 2})


class EbookEditView(UpdateView):
    model = EBook
    template_name = 'ebook/update.html'
    context_object_name = 'room'
    fields = ('title', 'book_number', 'isbn_number', 'price', 'publisher','author', 'subject', 'book_language',
              'description', 'image', 'file', 'status')
    success_url = reverse_lazy('ebook_list')


class EbookUpdateView(View):
    form_class = EBookForm

    def post(self, request):
        form = self.form_class(request.POST, request.FILES)

        if form.is_valid():
            ebooks = EBook.objects.get(pk=request.POST.get('ebook_id'))
            ebooks.title = request.POST.get('title')
            ebooks.book_number = request.POST.get('book_number', )
            ebooks.isbn_number = request.POST.get('isbn_number', )
            ebooks.price = request.POST.get('price', )
            ebooks.description = request.POST.get('description', )
            ebooks.publisher_id = request.POST.get('publisher_id', )
            ebooks.author_id = request.POST.get('author_id', )
            ebooks.subject_id = request.POST.get('subject_id', )
            ebooks.book_language_id = request.POST.get('book_language_id', )
            ebooks.description = request.POST.get('description', )
            ebooks.image = request.FILES.get('image', )
            ebooks.file = request.FILES.get('file', )
            ebooks.status = request.POST.get('status', )
            ebooks.save()
            return JsonResponse({"instance": 'messages'}, status=200)
        else:
            return JsonResponse({"error": form.errors}, json_dumps_params={'indent': 2})


class EbookDeleteView(DeleteView):
    def get(self, request):
        id1 = request.GET.get('id', None)
        EBook.objects.get(id=id1).delete()
        data = {
            'deleted': True
        }
        return JsonResponse(data)


def book_issue(request):
    book_issues=BookIssue.objects.filter(status=0).order_by('-id')
    contex = {'book_issues':book_issues, 'title':'Issue Book'}
    return render(request, 'book_issue/index.html',contex)

def book_return(request):
    book_issues=BookIssue.objects.filter(status=1).order_by('-id')
    contex = {'book_issues':book_issues, 'title':'Return Book'}
    return render(request, 'book_issue/index.html',contex)

def book_issue_view(request, pk):
    book_issue=BookIssue.objects.get(id=pk)
    context={'book_issue':book_issue}
    return render(request, 'book_issue/view.html',context)


def book_issue_create(request,pk):
    total_issue = BookIssue.objects.filter(book=pk, status=0).count()
    total_qty = Book.objects.filter(id=pk).get()
    if total_qty.qty > total_issue:
        print(total_qty)
    else:
        messages.success(request,'Insuficient quantity', extra_tags='error')
        return redirect('/book_list')
    form = BookIssueForm()
    if request.method == 'POST':
        book_issue = request.POST
        form = BookIssueForm(request.POST)
        if form.is_valid():
           book_issue = form.save()
           messages.success(request,'Data store successfull', extra_tags='success')
           return redirect('/book_issue_list')
    context = {'form':form, 'book':pk}
    return render(request, 'book_issue/create.html',context)

def book_issue_edit(request, pk):
    book_issue=BookIssue.objects.get(id=pk)
    form = BookIssueForm(instance=book_issue)
    if request.method=='POST':
        form = BookIssueForm(request.POST, instance=book_issue)
        if form.is_valid():
           form.save()
           messages.success(request,'Data update successfull',extra_tags='success')
           return redirect('/book_issue_list')

    context={'form':form,'book':book_issue.book.id}
    return render(request, 'book_issue/create.html',context)

def make_return(request,pk):
    #book_issue=BookIssue.objects.get(id=pk)
    BookIssue.objects.filter(pk=pk).update(status=1)
    messages.success(request,'Data delete successfull',extra_tags='success')
    return redirect('/book_issue_list')

def book_issue_delete(request,pk):
    book_issue=BookIssue.objects.get(id=pk)
    book_issue.delete()
    messages.success(request,'Data delete successfull',extra_tags='success')
    return redirect('/book_issue_list')
