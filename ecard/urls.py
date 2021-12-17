"""ecard URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from app import views as app_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),
    path('', app_views.CardList.as_view(), name='home'),

    # path('ecard/', app_views.CardList.as_view()),
    path('ecard/<int:pk>/', app_views.CardDetail.as_view(), name='card_detail'),
    path('ecard/new/', app_views.AddCard.as_view(), name='add_card'),
    path('ecard/edit/',app_views.EditCard.as_view(), name='edit_card'),
    path('ecard/me/', app_views.UserCreatedList.as_view(), name='my_cards'),
    # path("", core_views.recipe_list, name="homepage"),
    # path('', habit_tracker_views.home, name='home'),
    # path('admin/', admin.site.urls),
    # path('auth/', include('djoser.urls')),
    # path('auth/', include('djoser.urls.authtoken')),
    # path('add_habit/', habit_tracker_views.add_habit, name="add_habit"),
    # path('habit_library/', habit_tracker_views.habit_library, name="habit_library"),
    # 
# path('api/habit_library',api_views.HabitLibraryView.as_view(), name="api_habit_library"),

    path('ecard/card_list/', app_views.CardList.as_view(), name='card_list'),
    path('ecard/card_detail/<int:pk>/', app_views.CardDetail.as_view(), name='card_detail'),
    path('ecard/delete_card/<int:pk>', app_views.DeleteCard.as_view(), name='delete_card'),
]

