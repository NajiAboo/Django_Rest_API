
from django.conf.urls import url
from django.urls import path

from .views import (StatusAPIView,
                    StatusAPIDetailView,
                   # StatusCreateAPIView, 
                   # StatusDetailPIView, 
                    #StatusUpdateAPIView,
                    #StatusDeleteAPIView,
                    )

urlpatterns = [
     path('', StatusAPIView.as_view()),
     #path('/create/', StatusCreateAPIView.as_view()),
     path('/<int:id>', StatusAPIDetailView.as_view()),
     #path('/<int:pk>/update', StatusUpdateAPIView.as_view()),
     #path('/<int:pk>/delete', StatusDeleteAPIView.as_view()),
    # url(r'^(?p<id>.*)/$', StatusDetailAPIView.as_view()),
    # url(r'^(?p<id>.*)/update/$', StatusUpdateAPIView.as_view()),
    # url(r'^(?p<id>.*)/delete/$', StatusDeleteAPIView.as_view()),     
]
