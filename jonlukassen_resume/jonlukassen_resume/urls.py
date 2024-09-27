from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

#from experience.views import introduction_home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('introduction.urls')),  # Root URL leads to introduction page
    # Assign base paths for each app
    path('experience/', include('experience.urls')),  # Work Experience app
    path('projects/', include('projects.urls')),  # Side Projects app
    path('github/', include('github.urls')),  # GitHub app
    path('salesforce/', include('salesforce.urls')),  # Salesforce app
    path('resume/', include('resume.urls')),  # Resume/Contact app
]

# Serve media files in development
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
