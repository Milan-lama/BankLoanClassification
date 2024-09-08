from django.urls import path
from model_prediction.views import PredictionView
urlpatterns = [
    path('prediction/',PredictionView.as_view())
]