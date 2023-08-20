"""
URL configuration for materiel project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from lycee import views
from lycee.views import CreateEnseignantView
from lycee.views import CreateMaterielView
from lycee.views import InfoMaterielView
from lycee.views import InfoEnseignantView
from lycee.views import CreateEmpruntView
from lycee.views import CreatePassassionView
from lycee.views import InfoPassassionView
from lycee.views import InfoEmpruntView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name="index"),
    path('lycee/enseignant/create', CreateEnseignantView.as_view(), name="create_enseignant"),
    path('lycee/materiel/create', CreateMaterielView.as_view(), name="create_materiel"),
    path('lycee/materiel/info', InfoMaterielView, name="info_materiel"),
    path('lycee/enseignant/info', InfoEnseignantView, name="info_enseignant"),
    path('lycee/emprunt/create', CreateEmpruntView.as_view(), name="create_emprunt"),
    path('lycee/passassion/create', CreatePassassionView, name="create_passassion"),
    path('lycee/passassion/info', InfoPassassionView, name="info_passassion"),
    path('lycee/emprunt/info', InfoEmpruntView, name="info_emprunt")
]
