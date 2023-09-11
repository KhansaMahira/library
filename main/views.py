from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'title': 'Untuk Negeriku',
        'amount': 1,
        'author': 'Mohammad Hatta',
        'publisher': 'PT Kompas Media Nusantara',
        'book_category': 'Biografi',
        'isbn': '978-602-412-422-9',
    }

    return render(request, "main.html", context)