"""
This module contains classes that can process location data received from French government api.
"""
from .address_processor import AddressProcessor


class FranceAddressProcessor(AddressProcessor):
    """
    This is a processor specific to the French government api serving French-based data.

    Due to shortage of time and not enough research with the api, it has been simplified
    in getting the single values. (this is used for the reverse search for example)

    """
    FRANCE_GOUV_API_URL = 'https://api-adresse.data.gouv.fr/'

    def __init__(self):
        super().__init__(self.FRANCE_GOUV_API_URL)

    def get_features(self):
        return self.found_locations.get('features', [])

    def get_cities(self):
        return set([location.get('properties',{}).get('city') for location in self.get_features()])

    def get_city(self):
        cities = self.get_cities()
        return cities.pop() if cities else None

    def get_names(self):
        return set([location.get('properties', {}).get('name') for location in self.get_features()])

    def get_name(self):
        names = self.get_names()
        return names.pop() if names else None

    def get_streets(self):
        return set([location.get('properties', {}).get('street') for location in self.get_features()])

    def get_street(self):
        streets = self.get_streets()
        return streets.pop() if streets else None

    def get_house_number(self):
        house_numbers = [location.get('properties', {}).get('housenumber') for location in self.get_features()]
        return house_numbers[0] if house_numbers else None
