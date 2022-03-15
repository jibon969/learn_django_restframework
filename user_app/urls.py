from django.urls import path, include

urlpatterns = [
    path('account/', include('user_app.api.urls')),
]
