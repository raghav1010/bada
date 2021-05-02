from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path, re_path, reverse_lazy
from django.views.generic.base import RedirectView
from tester.sample import views 

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


schema_view = get_schema_view(
   openapi.Info(
      title="Bada-Bazaar API",
      default_version='v1',
      description="Test description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)


urlpatterns = [
    path('swagger', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    # admin portal
    path('admin/', admin.site.urls),

    # api endpoint
    path('User', include("tester.sample.urls")),
    path('', include("tester.business.urls")),
    # path('api/v1/', include("onemm.leaves.urls"), name="leaves"),

    # redirecting the url taken from offical document
    # redirect to the http version
    # re_path(r'^$', RedirectView.as_view(url=reverse_lazy(views.RedirectView), permanent=False)),
    # path('api/', views.RedirectView, name="redirect"),

    
    

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
