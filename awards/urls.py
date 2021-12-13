from django.urls import include,path,re_path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('',views.index, name = 'home'),
    path('search/', views.searchprofile, name='search'),
    path('newproject/',views.addProject,name = 'project'),
    path('accounts/profile/',views.profile,name = 'profile'),
    path('editprofile/',views.editprofile,name = 'editprofile'), 
    path('awards/<id>/',views.projects,name = 'projects'),
    path(r'ratings/', include('star_ratings.urls', namespace='ratings')),
    path('rate/<id>/',views.rate,name = 'rate'),
    path('api/profile',views.ProfileList.as_view()),
    path('api/projects',views.ProjectList.as_view())


]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)