from django.urls import path
from .views import HomeView, PageDetail

app_name = 'pages'
urlpatterns = [    
    path('pages/<slug:handle>/', PageDetail.as_view(template='page'), name="detail"),
    path('', HomeView.as_view(), name='home')
]
