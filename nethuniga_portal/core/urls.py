from django.urls import path
from .views import home, mock_test, pdf_notes, videos, about, contact

urlpatterns = [
    path('', home, name='home'),
    path('mock-test/', mock_test, name='mock_test'),
    path('pdfs/', pdf_notes, name='pdf_notes'),
    path('videos/', videos, name='videos'),
    path('about/', about, name='about'),
]