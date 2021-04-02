from django.urls import path
from rajsekhar import views
urlpatterns = [
 path('',views.home,name="home"),
 path("demo/",views.chk),
 path("ht/",views.homepage),
 path("lg/",views.lgn),
 path("rg/",views.reg,name="register"),
 path("bt/",views.bthm),
 path("about/",views.about,name="about"),
 path("cont/",views.cont,name="cont"),
]