from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('', views.ad_list, name='ad_list'),
    path('edit/<int:ad_id>/', views.edit_ad, name='edit_ad'),
    path('delete/<int:ad_id>/', views.delete_ad, name='delete_ad'),
    path('favorite/<int:ad_id>/', views.toggle_favorite, name='toggle_favorite'),
    path('ad/<int:ad_id>/', views.ad_detail, name='ad_detail'),
    path('login/', views.login_view, name='login'),
    path('signup/', views.signup_view, name='signup'),
    path('create/', views.create_ad, name='create_ad'),
    path('favorites/', views.favorites, name='favorites'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('ad/<int:ad_id>/add_comment/', views.add_comment, name='add_comment'),
    path('comment/<int:comment_id>/edit/', views.edit_comment, name='edit_comment'),
    path('comment/<int:comment_id>/delete/', views.delete_comment, name='delete_comment'),
]



if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
