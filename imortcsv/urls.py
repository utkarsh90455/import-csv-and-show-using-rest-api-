from django.conf.urls import url
from . import views

urlpatterns=[

    url(r'^$',views.csv_upload,name="index"),
    url(r'^search/$',views.csv_search,name="index"),
    url(r'^csv/api/$', views.csvApi.as_view(), name="index")
]