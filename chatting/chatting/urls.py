from django.contrib import admin
from django.urls import path, include

from chat import urls as chat_urls


urlpatterns = [
    # 元のコードは→url(r'^chat/', include('chat.urls')),
    path('chat/', include(chat_urls)),
    # 元のコードは→url(r'^admin/', admin.site.urls),
    path('admin/', admin.site.urls),
]