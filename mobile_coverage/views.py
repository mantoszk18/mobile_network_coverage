from django.contrib.postgres.aggregates import ArrayAgg

from rest_framework import views, generics
from rest_framework.response import Response

from address_geocoding.france_gouv_addresses import FranceAddressProcessor

from .serializers import NetworkCoverageSerializer
from .models import NetworkCoveragePoint, NetworkType


class FindNetworkCoverageView(views.APIView):

    def get(self, request):
        points_queryset = NetworkCoveragePoint.objects.all()
        query = self.request.query_params.get('q')

        # for now the city level precision is used
        # for more precise location retrieval, I would use some external GIS api
        location_cities = self.get_cities(query)
        filtered_queryset = points_queryset.filter(location__city__in=location_cities)
        aggregated_networks = filtered_queryset.values_list('operator__name').annotate(ntwrks=ArrayAgg('networks'))
        all_networks = NetworkType.objects.values_list(flat=True)

        result = {operator: self.aggregate_networks(networks, all_networks)
                  for operator, networks in aggregated_networks}

        return Response(result)

    def get_cities(self, query):
        # TODO: this processor should be retrieved dynamically based on the sites settings
        processor = FranceAddressProcessor()
        processor.address_search({'q': query})

        return processor.get_cities()

    def aggregate_networks(self, networks, all_networks):
        return { network: True if network in networks else False for network in all_networks}