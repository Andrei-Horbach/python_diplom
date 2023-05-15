from django.contrib import admin
from django.urls import path
from v_kraskah import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name="index"),  # Главная страница
    path('categorys/', views.CategoryListView.as_view(), name="categorys"),  # Категории занятий
    path('category/<int:pk>', views.CategoryDetailView.as_view(), name="category"),  # Конкретная книга
    path('price/', views.PriceListView.as_view(), name="price"),  # Прайс-лист
    path('teachers/', views.TeacherListView.as_view(), name='teachers'),  # Преподаватели
    path('call_back/', views.call_back, name='call_back'),
    path('answer/', views.answer, name='answer'),

]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
if settings.DEBUG:
    urlpatterns += staticfiles_urlpatterns() + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
