from django.urls import include, path

urlpatterns = [
    path('api/', include('notes.api.urls')),
]
