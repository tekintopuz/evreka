from django.contrib import admin
from django.urls import path
from navigation.views import LastTwoHoursRecord
from bin.views import CollectionFrequcencyView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('navigations', LastTwoHoursRecord.as_view(), name="last_two_hours"),
    path('collection-frequency', CollectionFrequcencyView.as_view(), name="collection_frequency"),
]
