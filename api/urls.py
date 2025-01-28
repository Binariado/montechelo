from django.urls import path, include

urlpatterns = [
    path('', include('api.account.urls')),
    path('', include('api.to_do.urls')),
]
