from django.conf.urls import url
from .views import *


urlpatterns = [
    url(r'^$', index, name="index"),
    url(r"editTutorial/(?P<tutorial>.+)",editTutorial,name="edit"),
    url(r"view/(?P<tutorial>\d+)",viewTutorial,name="view"),
    url(r"editComponent/(?P<primaryKey>\d+)",editComponent,name="submit"),
    url(r"addComponent/(?P<tutorial>\d+)",addComponent,name="addComponent"),
    url(r"^search/",searchView,name="search"),
    url(r"^addTutorial/",addTutorial,name="addTutorial")

    #url(r"profile",profile,name="profile"),
]