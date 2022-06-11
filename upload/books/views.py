from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
# Create your views here.


from .forms import BookForm
from .models import Book

def book_upload(request):
    if request.method=='POST':
        form = BookForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponse('file save successful')
    else:
        form = BookForm()
        return render(request, 'books/upload.html', {'form':form})
    

def book_download(request):
    if request.method=='POST':
        title=request.POST['title']
        document=request.FILES['document']
        book=Book.objects.create(title=title,document=document)
        book.save()
    object=Book.objects.all()
    return render(request, 'books/download.html', {'object':object})

class Load(CreateView):
    template_name='books/load.html'
    model=Book
    fields=['document']
    success_url=reverse_lazy('load')
    def get_context_data(self,**kwargs):
        context=super().get_context_data(**kwargs)
        context['object']=Book.objects.all()
        return context
    
    

        
        
 



    
        
            
            