from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('hot/', views.hot_questions, name='hot_questions'),
    path('tag/<str:name>/', views.tag_questions, name='tag_questions'),
    path('question/<int:pk>/', views.answers_for_question, name='answers_for_questions'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('signup/', views.signup, name='signup'),
    path('ask/', views.ask, name='ask'),
    path('settings/', views.settings, name='settings'),
    path('votes/', views.votes, name='votes'),
    path('correct/', views.is_correct, name='correct'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
