"""
This module helps converting address queries to specific geolocation data.
As well as does reverse geocoding of a specific location.

"""
import requests
import pyproj

from urllib.parse import urljoin


class AddressProcessor:
    """
    This class allows querying external geo-apis for information about given locations.

    Just inherit from it and run init with a concrete api URL.
    This is a parent class to any specific geolocation processors.

    """

    def __init__(self, api_url, search_keyword='search', reverse_keyword='reverse'):
        self.api_url = api_url
        self.search_url = urljoin(api_url, search_keyword)
        self.reverse_url = urljoin(api_url, reverse_keyword)
        self.found_locations = {}

    def address_search(self, query: dict) -> dict:
        """
        This method tries to retrieve location information based on the passed textual query.

        """
        response = requests.get(self.search_url, query)
        self.found_locations = response.json()
        return self.found_locations

    def location_search(self, params: dict) -> dict:
        """
        Method retrieves a location information based on the params parameter.

        Args:
            params: a dictionary with usually a longitude and lattitude of the location

        Returns:
            a dictionary with location(s) data

        """
        response = requests.get(self.reverse_url, params)
        self.found_locations = response.json()
        return self.found_locations

    @staticmethod
    def convert_lambert_to_GPS(x:int, y:int):
        """Does an tough conversion from Lambert93 to GPS (WGS84) coordinates"""
        lambert = pyproj.Proj('+proj=lcc +lat_1=49 +lat_2=44 +lat_0=46.5 +lon_0=3 '
                              '+x_0=700000 +y_0=6600000 +ellps=GRS80 +towgs84=0,0,0,0,0,0,0 +units=m +no_defs')
        wgs84 = pyproj.Proj('+proj=longlat +ellps=WGS84 +datum=WGS84 +no_defs')
        long, lat = pyproj.transform(lambert, wgs84, x, y)

        return long, lat

    def get_cities(self):
        raise NotImplementedError

    def get_city(self):
        raise NotImplementedError

    def get_names(self):
        raise NotImplementedError

    def get_name(self):
        raise NotImplementedError

    def get_streets(self):
        raise NotImplementedError

    def get_street(self):
        raise NotImplementedError

    def get_house_number(self):
        raise NotImplementedError