"""
This command imports location data from a CSV to the database.

The reverse geocoding part could be done in bulk (as some sites allow that), but would require some refactoring.

"""
import csv

from django.core.management.base import BaseCommand, CommandError

from address_geocoding.france_gouv_addresses import FranceAddressProcessor
from mobile_coverage.models import Location, NetworkCoveragePoint, NetworkType, Operator


NETWORK_TYPES_START_INDEX = 3  # TODO: this needs to be tied to the specific AdressProcessor
OPERATOR_KEY = 'Operateur'


class Command(BaseCommand):
    help = 'Imports location data from a CSV file into the database.'

    def add_arguments(self, parser):
        parser.add_argument('filename', type=str, help='Filename with path')
        parser.add_argument('-d', dest='delimiter', type=str, default=';', help='CSV file column delimiter')
        #parser.add_argument('update_existing', type=bool)

    def handle(self, *args, **options):
        #shouldUpdateExisting = options.get('update_existing', False)
        filename = options.get('filename')
        delimiter = options.get('delimiter')

        with open(filename) as location_data:
            reader = csv.DictReader(location_data, delimiter=delimiter)

            network_types = reader.fieldnames[NETWORK_TYPES_START_INDEX:]
            # first update any missing network types
            for network_type in network_types:
                NetworkType(network_type).save()

            for row in reader:

                try:
                    location = Location.objects.get(x_coord=row['X'], y_coord=row['Y'])
                except Location.DoesNotExist:
                    # first query the Processor for location data
                    long, lat = FranceAddressProcessor.convert_lambert_to_GPS(row['X'], row['Y'])
                    params = {'lon': long, 'lat': lat}
                    processor = FranceAddressProcessor()
                    processor.location_search(params)

                    location = Location(x_coord=row['X'], y_coord=row['Y'],
                                     name=processor.get_name(),
                                     city=processor.get_city(),
                                     street=processor.get_street(),
                                     house_number=processor.get_house_number())
                    location.save()

                point, created = NetworkCoveragePoint.objects.get_or_create(operator_id=row[OPERATOR_KEY], location=location)

                for network_type in network_types:
                    if int(row[network_type]):
                        point.networks.add(NetworkType.objects.get(network_type=network_type))
