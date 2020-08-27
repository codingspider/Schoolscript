from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse
from .models import *
from .form import *
from django.contrib import messages
import mimetypes
# Create your views here.

def author(request):
    authors=Author.objects.all().order_by('-id')
    contex = {'authors':authors}
    return render(request, 'author/index.html',contex)

def author_create(request):
    form = AuthorForm()
    if request.method=='POST':
        author=request.POST
        form = AuthorForm(request.POST) 
        if form.is_valid():
           author=form.save()
           messages.success(request,'Data store successfull',extra_tags='success')
           return redirect('/author_list')
    context = {'form':form}
    return render(request, 'author/create.html',context)

def author_edit(request, pk):
    author=Author.objects.get(id=pk)
    form = AuthorForm(instance=author)
    if request.method=='POST':
        form = AuthorForm(request.POST, instance=author)
        if form.is_valid():
           form.save()
           messages.success(request,'Data update successfull',extra_tags='success')
           return redirect('/author_list')

    context={'form':form}
    return render(request, 'author/create.html',context)

def author_delete(request,pk):
    author=Author.objects.get(id=pk)
    author.delete()
    messages.success(request,'Data delete successfull',extra_tags='success')
    return redirect('/author_list') 


#-----------------------publisher------------------------

def publisher(request):
    publishers=Publisher.objects.all().order_by('-id')
    contex = {'publishers':publishers}
    return render(request, 'publisher/index.html',contex)

def publisher_create(request):
    form = PublisherForm()
    if request.method=='POST':
        publisher=request.POST
        form = PublisherForm(request.POST) 
        if form.is_valid():
           publisher=form.save()
           messages.success(request,'Data store successfull',extra_tags='success')
           return redirect('/publisher_list')
    context = {'form':form}
    return render(request, 'publisher/create.html',context)

def publisher_edit(request, pk):
    publisher=Publisher.objects.get(id=pk)
    form = PublisherForm(instance=publisher)
    if request.method=='POST':
        form = PublisherForm(request.POST, instance=publisher)
        if form.is_valid():
           form.save()
           messages.success(request,'Data update successfull',extra_tags='success')
           return redirect('/publisher_list')

    context={'form':form}
    return render(request, 'publisher/create.html',context)

def publisher_delete(request,pk):
    publisher=Publisher.objects.get(id=pk)
    publisher.delete()
    messages.success(request,'Data delete successfull',extra_tags='success')
    return redirect('/publisher_list')


#-----------------------subject------------------------

def subject(request):
    subjects=Subject.objects.all().order_by('-id')
    contex = {'subjects': subjects}
    return render(request, 'subject/index.html',contex)

def subject_create(request):
    form = SubjectForm()
    if request.method=='POST':
        subject=request.POST
        form = SubjectForm(request.POST) 
        if form.is_valid():
           subject=form.save()
           messages.success(request,'Data store successfull',extra_tags='success')
           return redirect('/subject_list')
    context = {'form':form}
    return render(request, 'subject/create.html',context)

def subject_edit(request, pk):
    subject=Subject.objects.get(id=pk)
    form = SubjectForm(instance=subject)
    if request.method=='POST':
        form = SubjectForm(request.POST, instance=subject)
        if form.is_valid():
           form.save()
           messages.success(request,'Data update successfull',extra_tags='success')
           return redirect('/subject_list')

    context={'form':form}
    return render(request, 'subject/create.html',context)

def subject_delete(request,pk):
    subject=Subject.objects.get(id=pk)
    subject.delete()
    messages.success(request,'Data delete successfull',extra_tags='success')
    return redirect('/subject_list')


#-----------------------book_language------------------------


def book_language(request):
    book_languages=BookLanguage.objects.all().order_by('-id')
    contex = {'book_languages':book_languages}
    return render(request, 'book_language/index.html',contex)

def book_language_create(request):
    form = BookLanguageForm()
    if request.method=='POST':
        book_language=request.POST
        form = BookLanguageForm(request.POST) 
        if form.is_valid():
           book_language=form.save()
           messages.success(request,'Data store successfull',extra_tags='success')
           return redirect('/book_language_list')
    context = {'form':form}
    return render(request, 'book_language/create.html',context)

def book_language_edit(request, pk):
    book_language=BookLanguage.objects.get(id=pk)
    form = BookLanguageForm(instance=book_language)
    if request.method=='POST':
        form = BookLanguageForm(request.POST, instance=book_language)
        if form.is_valid():
           form.save()
           messages.success(request,'Data update successfull',extra_tags='success')
           return redirect('/book_language_list')

    context={'form':form}
    return render(request, 'book_language/create.html',context)

def book_language_delete(request,pk):
    book_language=BookLanguage.objects.get(id=pk)
    book_language.delete()
    messages.success(request,'Data delete successfull',extra_tags='success')
    return redirect('/book_language_list')


#-----------------------rack------------------------


def rack(request):
    racks=Rack.objects.all().order_by('number')
    contex = {'racks':racks}
    return render(request, 'rack/index.html',contex)

def rack_create(request):
    form = RackForm()
    if request.method=='POST':
        rack=request.POST
        form = RackForm(request.POST) 
        if form.is_valid():
           rack=form.save()
           messages.success(request,'Data store successfull',extra_tags='success')
           return redirect('/rack_list')
    context = {'form':form}
    return render(request, 'rack/create.html',context)

def rack_edit(request, pk):
    rack=Rack.objects.get(id=pk)
    form = RackForm(instance=rack)
    if request.method=='POST':
        form = RackForm(request.POST, instance=rack)
        if form.is_valid():
           form.save()
           messages.success(request,'Data update successfull',extra_tags='success')
           return redirect('/rack_list')

    context={'form':form}
    return render(request, 'rack/create.html',context)

def rack_delete(request,pk):
    rack=Rack.objects.get(id=pk)
    rack.delete()
    messages.success(request,'Data delete successfull',extra_tags='success')
    return redirect('/rack_list')



#-----------------------book------------------------


def book(request):
    books=Book.objects.all().order_by('-id')
    contex = {'books':books}
    return render(request, 'book/index.html',contex)

def book_view(request, pk):
    book=Book.objects.get(id=pk)
    issue_list=BookIssue.objects.filter(book=pk, status=0)
    context={'book':book, 'issue_list':issue_list}
    return render(request, 'book/view.html',context)

def book_create(request):
    form = BookForm()
    if request.method=='POST':
        book=request.POST
        form = BookForm(request.POST, request.FILES) 
        if form.is_valid():
           book=form.save()
           messages.success(request,'Data store successfull',extra_tags='success')
           return redirect('/book_list')
    context = {'form':form}
    return render(request, 'book/create.html',context)

def book_edit(request, pk):
    book=Book.objects.get(id=pk)
    form = BookForm(instance=book)
    if request.method=='POST':
        form = BookForm(request.POST, request.FILES, instance=book)
        if form.is_valid():
           form.save()
           messages.success(request,'Data update successfull',extra_tags='success')
           return redirect('/book_list')

    context={'form':form}
    return render(request, 'book/create.html',context)

def book_delete(request,pk):
    book=Book.objects.get(id=pk)
    book.delete()
    messages.success(request,'Data delete successfull',extra_tags='success')
    return redirect('/book_list')


def ebook(request):
    ebooks=EBook.objects.all().order_by('-id')
    contex = {'ebooks':ebooks}
    return render(request, 'ebook/index.html',contex)

def ebook_view(request, pk):
    ebook=EBook.objects.get(id=pk)
    context={'ebook':ebook}
    return render(request, 'ebook/view.html',context)

def ebook_create(request):
    form = EBookForm()
    if request.method=='POST':
        ebook=request.POST
        form = EBookForm(request.POST, request.FILES) 
        if form.is_valid():
           ebook=form.save()
           messages.success(request,'Data store successfull',extra_tags='success')
           return redirect('/ebook_list')
    context = {'form':form}
    return render(request, 'ebook/create.html',context)


def ebook_edit(request, pk):
    ebook=EBook.objects.get(id=pk)
    form = EBookForm(instance=ebook)
    if request.method=='POST':
        form = EBookForm(request.POST, request.FILES, instance=ebook)
        if form.is_valid():
           form.save()
           messages.success(request,'Data update successfull',extra_tags='success')
           return redirect('/ebook_list')

    context={'form':form}
    return render(request, 'ebook/create.html',context)


def ebook_delete(request, pk):
    ebook=EBook.objects.get(id=pk)
    ebook.delete()
    messages.success(request,'Data delete successfull',extra_tags='success')
    return redirect('/ebook_list')


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
    total_issue=BookIssue.objects.filter(book=pk, status=0).count()
    total_qty=Book.objects.filter(id=pk).get()
    if total_qty.qty > total_issue:
        print(total_qty)
    else:
        messages.success(request,'Insuficient quantity',extra_tags='error')
        return redirect('/book_list')
    form = BookIssueForm()
    if request.method=='POST':
        book_issue=request.POST
        form = BookIssueForm(request.POST) 
        if form.is_valid():
           book_issue=form.save()
           messages.success(request,'Data store successfull',extra_tags='success')
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
