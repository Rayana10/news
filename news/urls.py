from django.urls import path
from news.views import news_home, create, NewsDetailView, NewsUptadelView, NewsDeleteView

urlpatterns = [
    path('', news_home, name='news_home'),
    path('create', create, name='create_news'),
    path('<int:pk>', NewsDetailView.as_view(), name='news_detail'),
    path('<int:pk>/update', NewsUptadelView.as_view(), name='news_update'),
    path('<int:pk>/delete', NewsDeleteView.as_view(), name='news_delete')
    
]
