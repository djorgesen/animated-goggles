from django.urls import path
from django.views.generic import TemplateView
from .views import TriangleCalculationView, SecondsConverterView, PythagoreanCalculateView, RecursiveLauncherView

urlpatterns = [
    path('', TemplateView.as_view(template_name="pages/index.html"), name='index'),
    path('triangle/', TemplateView.as_view(template_name="pages/triangle.html"), name='triangle'),
    path('triangle/calculate/', TriangleCalculationView.as_view(), name='calculate-triangle'),
    path('time/', TemplateView.as_view(template_name='pages/timeconverter.html'), name='time'),
    path('time/calculate/', SecondsConverterView.as_view(), name='seconds-converter'),
    path('pythagorean/', TemplateView.as_view(template_name='pages/pythagorean.html'), name='pythagorean'),
    path('pythagorean/calculate/', PythagoreanCalculateView.as_view(), name='pythagorean-calculate'),
    path('repeat/', TemplateView.as_view(template_name='pages/recursive_string.html'), name='repeat'),
    path('repeat/it/', RecursiveLauncherView.as_view(), name='repeat-the-string'),

]
