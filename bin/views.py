from rest_framework.response import Response
from rest_framework.views import APIView

from bin.models import Bin
from bin.serializers import BinCollectionSerializer


class CollectionFrequcencyView(APIView):
    def get(self, request):
        bins = Bin.objects.all()
        serializer = BinCollectionSerializer(bins, many=True)
        return Response(serializer.data)
