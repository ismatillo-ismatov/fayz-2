from django.urls import path
from .views import *

app_name = 'blog'

urlpatterns =[
path('',PostTemplateView.as_view(),name="index"),
    path('collection',PostDetailView.as_view(),name="collection"),
    # path('shoes',PostShoesView.as_view(),name="shoes"),
    path('racing',PostRaceingView.as_view(),name="racing"),
    path('create',PostCreateView.as_view(),name="create"),
    path('post/<int:pk>/update',PostUpdateView.as_view(),name="update"),
    path("post/<int:pk>/delete",PostDeleteView.as_view(),name="delete"),
    path('post/shoes',PostViews.as_view(),name="shoes"),
    path('detail/<int:pk>',PostDetail.as_view(),name="detail")
    ]
