
from generator import views
from django.urls import path

urlpatterns = [
    # path("admin/", admin.site.urls),
    path("about", views.about),
]
