from django.contrib import admin
from django.urls import path
from django.conf.urls import url,include
from django.conf.urls.static import static
from django.views.static import serve
from django.conf import settings
from railapp import views
urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^$',views.home,name='home'),
    path('login/',views.login,name='login'),
    url(r'^signup/$',views.signup,name='signup'),
    url(r'^logout',views.user_logout,name="logout"),
    url(r'^assets/(?P<path>.*)$', serve,{'document_root': settings.ASSETS}),
]
