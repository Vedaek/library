from django.shortcuts import redirect, render
from library.forms import AddBookForm, AddStudentForm, UpdateStudentForm, UserRegistrationForm
from library.models import Student
from library.models import Book
from django.contrib.auth.decorators import login_required


@login_required
def student_list_view(request):
    data = Student.objects.all()
    return render(request,"library/studlist.html",{'data':data})

@login_required
def student_detail_view(request,id):
    obj = Student.objects.get(pk=id)
    return render(request, "library/studdetail.html",{'obj':obj})

@login_required
def book_list_view(request):
    data = Book.objects.all()
    return render(request,"library/booklist.html",{'data':data})

@login_required
def book_detail_view(request,id):
    obj = Book.objects.get(pk=id)
    return render(request, "library/bookdetail.html",{'obj':obj})

@login_required
def student_add_view(request):
    form = AddStudentForm()
    if request.method == "POST":
        form = AddStudentForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect("/std/stdlist/")
    return render(request,"library/studadd.html",{'form':form})

@login_required
def book_add_view(request):
    form = AddBookForm()
    if request.method == "POST":
        form = AddBookForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect("/book/booklist/")
    return render(request,"library/bookadd.html",{'form':form})

@login_required
def student_update_view(request,id):
    obj = Student.objects.get(pk=id)
    form = UpdateStudentForm(instance=obj)
    if request.method == "POST":
        form = UpdateStudentForm(request.POST,request.FILES,instance=obj)
        if form.is_valid():
            form.save()
            return redirect(f"/std/stddetail/{obj.id}/")
    return render(request,"library/studupdate.html",{'form':form})

@login_required
def student_delete_view(request,id):
    obj = Student.objects.get(pk=id)
    if request.method == "POST":
        obj.delete()
        return redirect("/std/stdlist/")
    return render(request,"library/studdelete.html",{'obj':obj})

@login_required
def book_delete_view(request,id):
    obj = Book.objects.get(pk=id)
    if request.method == "POST":
        obj.delete()
        return redirect("/book/booklist/")
    return render(request,"library/bookdelete.html",{'obj':obj})

def admin_register_view(request):
    form = UserRegistrationForm()
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/login/")
    return render(request,"library/register.html",{'form':form})
    




