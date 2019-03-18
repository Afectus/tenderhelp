from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', RedirectView.as_view(pattern_name='check_business_entity'), name='index'),
    path('rsmpnalogapp/', include('app.rsmpnalogapp.urls'))
]
