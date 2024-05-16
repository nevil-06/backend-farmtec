from django.contrib import admin
from django.urls import path, include
from farm_app import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('register/', views.UserRegistrationView.as_view(), name='user-register'),
    path('login/', views.UserLoginView.as_view(), name='user-login'),


    path('api/extendedusers', views.ExtendedUserLists.as_view()),
    path('api/extendedusers/<int:pk>', views.ExtendedUserRetrieveUpdate.as_view()),
    path('api/farmers', views.FarmerLists.as_view()),
    path('api/farmers/<int:pk>', views.FarmerRetrieveUpdate.as_view()),
    path('api/lands', views.LandLists.as_view()),
    path('api/lands/<int:pk>', views.LandRetrieveUpdateDestroy.as_view()),
    path('api/landapplications', views.LandApplicationLists.as_view()),
    path('api/landapplications/<int:pk>', views.LandApplicationRetrieveUpdateDestroy.as_view()),
    path('api/agreements', views.LandAgreementLists.as_view()),
    path('api/agreements/<int:pk>', views.LandAgreementRetrieveUpdateDestroy.as_view()),
    path('predict', views.crop_prediction_view, name='predict'),
    path('upload_images/', views.ImageUploadView.as_view(), name='upload_images'),
    path('api/storage', views.StorageLists.as_view()),



    path('api-auth/', include('rest_framework.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)