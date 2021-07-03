from django.contrib import admin
from django.urls import path
from . import views

urlpatterns =[
 path("",views.index, name="index"),
 path("book",views.book, name="book"),
 path("login",views.login_view,name ="login"),
 path("register",views.register, name= "register"),
 path("logout",views.logout_view,name="logout"),
 path("home",views.home,name="home"),
 path("cancel/<int:id>",views.cancel,name="cancel"),
 path("booktest",views.book_test, name= "test"),
 path("bookmed",views.book_medicine, name= "med"),
 path("canceltest/<int:id>",views.cancel_test, name= "canceltest"),
 path("bookmed/<int:id>",views.cancel_med, name= "cancelmed"),
 path("ftc",views.ftc, name= "ftc"),
 path("fm",views.fm, name= "fm"),
 path("fh",views.fh, name= "fh"),
 path("dept",views.dept,name="dept"),
 path("hosp",views.hosp,name="hosp"),
 path("doc",views.doc,name="doc"),
]