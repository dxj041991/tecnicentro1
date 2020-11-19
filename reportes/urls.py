from django.urls import path

from reportes.views import ReportSaleView

urlpatterns = [
    # reports
    path('venta/', ReportSaleView.as_view(), name='sale_report'),
]