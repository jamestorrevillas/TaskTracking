from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('capabilities/', include('capabilities.urls', namespace='capabilities')),
    path('leader/', include('leader.urls', namespace='leader')),

]
