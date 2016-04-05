from django.conf.urls import url
from .views import (
    image_list,
    image_upload,
    )

urlpatterns = [
    url(r'^$', image_list),
    url(r'^upload/$', image_upload),
]
