from unicodedata import name
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='indexPage'),
    path('r0',views.reg0, name="reg0Page"),
    path('r1',views.reg1, name="reg1Page"),
    path('r2',views.reg2, name="reg2Page"),
    path('r3',views.reg3, name="reg3Page"),
    path('l1',views.log1, name="log1Page"),
    path('l2',views.log2, name="log2Page"),
    path('fp',views.resetPwd, name="resetPwdPage")
]