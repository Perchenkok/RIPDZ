"""HW URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""


from django.contrib import admin
from django.urls import path
from assk import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as dv

urlpatterns = [
    path('question/<int:pk>', views.question, name = 'question'),
    path('admin/', admin.site.urls),
    path('index/', views.index, name = 'index'),
    path('login/', dv.LoginView.as_view(), name='login'),
    path('logout/', dv.LogoutView.as_view(), name='logout'),
    path('newquestion/', views.newPost, name='newquestion'),
    path('newanswer/', views.AddAnswer, name='newanswer'),
    path('', views.redirectStartPageIndexPronto, name = 'redirecta')
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
