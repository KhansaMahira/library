from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'author_name': 'Khansa Mahira',
        'author_class': 'PBP D',
        'application_name': 'Library',
        'name': 'Untuk Negeriku',
        'amount': 1,
        'description': 'This book was written by Mohammad Hatta. It was published by PT Kompas Media Nusantara in 2011.',
        'book_category': 'Biografi',
        'isbn': '978-602-412-422-9',
    }

    return render(request, "main.html", context)