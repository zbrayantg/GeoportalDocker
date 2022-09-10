from django.urls import path
from . import views

app_name = 'BIF'

urlpatterns = [
    path('', views.home, name="Home"),
    path('reporte/', views.reporte, name="reporte"),
    path('reporte/<slug:search>', views.reporte, name='views.reporte'),
    path('mapa/', views.mapa, name="mapa"),
    path('mapa/<slug:search>', views.mapa, name='views.mapa'),
    path('reporte/upload_csv/', views.upload_csv, name="upload_csv"),
    path('reporte/upload_pdf/', views.upload_pdf, name="upload_pdf"),
    path('show_pdf/<str:id>', views.show_pdf, name="show_pdf")
]
