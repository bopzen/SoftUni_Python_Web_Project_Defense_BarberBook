from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from BarberBook import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('BarberBook.common.urls')),
    path('account/', include('BarberBook.account.urls')),
    path('barber/', include('BarberBook.barber.urls')),
    path('barbershop/', include('BarberBook.barbershop.urls')),
    path('client/', include('BarberBook.client.urls')),
    path('reservation/', include('BarberBook.reservation.urls')),
    path('review/', include('BarberBook.review.urls'))
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


admin.site.site_header = 'BarberBook Administrator'
admin.site.site_title = 'BarberBook Administrator Page'
admin.site.index_title = 'BarberBook Administrator Page'
