from django.shortcuts import render

def home(request):
    return render(request, 'index.html')

def mock_test(request):
    return render(request, 'mock_test.html')

def pdf_notes(request):
    return render(request, 'pdf_notes.html')

def videos(request):
    return render(request, 'videos.html')

def about(request):
    return render(request, 'about.html')

