
from django.contrib import admin
from django.urls import path,include
from rest_framework.routers import DefaultRouter

from django.conf import settings
from django.conf.urls.static import static
from demo import views

router=DefaultRouter()
router.register('demo',views.StudentModelviewset,basename='demo')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path("ckeditor5/", include('django_ckeditor_5.urls')),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


