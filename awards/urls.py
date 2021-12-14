from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns=[
    url('^$',views.landing, name='landing'),
    url(r'^accounts/profile/$', views.profile, name='profile'),
    url(r'^new/profile/$', views.edit, name='new-profile'),
    url(r'^new/post$', views.new_post, name='new_post'),
    url(r'^project/(\d+)$', views.single_project, name='project'),
    url(r'^rating/(\d+)$', views.review_rating, name="review"),
    url(r'^search/', views.search_results, name='search_results'),
    url(r'^api/Projects/$', views.ProjectsList.as_view()),
    url(r'^api/merch1/$', views.ProjectsList2.as_view())

]   