from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,"book/home.html",{})

def about(request):
    return render(request,"book/about.html",{})

def login(request):
    return render(request, 'login.html')

def search(request):
    query = request.GET.get('query', '')
    if query:
        # Search for books based on the query
        results = Book.objects.filter(title__icontains=query)  # Adjust as needed
    else:
        results = Book.objects.none()
    return render(request, 'book/search_results.html', {'results': results, 'query': query})

def book_detail(request, id):
    book = get_object_or_404(Book, id=id)
    return render(request, 'book/book_detail.html', {'book': book})

def genre_fiction(request):
    # Logic for fiction genre
    return render(request, 'book/genre_fiction.html')

def genre_nonfiction(request):
    # Logic for non-fiction genre
    return render(request, 'book/genre_nonfiction.html')

def genre_sci_fi(request):
    return render(request, 'book/genre_sci_fi.html')