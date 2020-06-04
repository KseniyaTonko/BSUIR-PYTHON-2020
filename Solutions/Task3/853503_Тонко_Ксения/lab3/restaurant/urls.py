from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include
from . import views
from django.contrib.auth import views as vs
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('admin/', admin.site.urls),
    path('cook_form/', views.add_cook, name='cook-form'),
    path('', views.index, name='index'),
    path('cook/<int:pk>/delete', views.delete_cook, name='cook-delete'),
    path('dishes/', views.DishListView.as_view(), name='dishes'),
    path('cooks/', views.CookListView.as_view(), name='cooks'),
    path('events/', views.EventListView.as_view(), name='events'),
    path('stocks/', views.StockListView.as_view(), name='stocks'),
    path('dish/<int:pk>', views.DishDetailView.as_view(), name='dish-detail'),
    path('cook/<int:pk>', views.CookDetailView.as_view(), name='cook-detail'),
    path('cook/<int:pk>/edit/', views.edit_cook, name='cook_edit'),
    path('event/<int:pk>', views.EventDetailView.as_view(), name='event-detail'),
    path('stock/<int:pk>', views.StockDetailView.as_view(), name='stock-detail'),
    path('login/', vs.LoginView.as_view(), name='login'),
    path('logout/', vs.LogoutView.as_view(), name='logout'),
    path('contact', views.cont),
    path('show_contact', views.show_contacts, name='contacts'),
    path('edit_contact/<int:id>', views.edit_contact),
    path('update_contact/<int:id>', views.update_contact),
    path('delete_contact/<int:id>', views.delete_contact),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
