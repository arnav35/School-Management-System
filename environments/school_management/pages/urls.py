from django.urls import path
from .views import HomePageView, AboutPageView, SignupView

urlpatterns = [
	path('signup/', SignupView.as_view(), name='signup'),
	path('about/', AboutPageView.as_view(), name='about'),
	path('', HomePageView.as_view(), name='home'),
]
