from django.urls import path
from . import views

app_name="api-v1"

urlpatterns = [
    path('post/',views.PostListView,name='api-post-list'),
    path('post/<int:id>/',views.PostDetail,name='api-post-detail'),
]