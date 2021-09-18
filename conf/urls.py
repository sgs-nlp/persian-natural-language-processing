from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
                  path('', include('plp_index.urls')),

                  path('template-view/', include('template_views.urls')),

                  path('prerequisite', include('prerequisites.urls')),
                  path('api/prerequisite/', include('prerequisites.apis.urls')),

                  path('classification', include('classifications.urls')),
                  path('api/classification/', include('classifications.apis.urls')),

                  path('extraction/keywords/', include('keywords_extractions.urls')),
                  path('api/extraction/keywords/', include('keywords_extractions.apis.urls')),

                  path('extraction/stopwords/', include('stopwords_lists.urls')),
                  path('api/extraction/stopwords/', include('stopwords_lists.apis.urls')),

                  path('similarity/', include('similarities.urls')),
                  path('api/similarity/', include('similarities.apis.urls')),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
