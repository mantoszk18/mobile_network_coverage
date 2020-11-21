from django.db import models


class Operator(models.Model):
    """Mobile telecoms operator"""

    code = models.CharField(max_length=5, primary_key=True, help_text="MCC + MNC code of the French operators")
    name = models.CharField(max_length=30)


class NetworkType(models.Model):
    """Type of the network. Like 2G, 3G, etc."""

    network_type = models.CharField(max_length=5, primary_key=True)


class Location(models.Model):
    """Basic information about location pointed by x and y coordinates"""

    x_coord = models.IntegerField()
    y_coord = models.IntegerField()
    name = models.CharField(max_length=200, null=True)
    city = models.CharField(max_length=100, null=True)
    street = models.CharField(max_length=100, null=True)
    house_number = models.CharField(max_length=10, null=True)  # there can be numbers like 21B


class NetworkCoveragePoint(models.Model):
    """Info about what type of coverage does have a given operator at a specific location"""

    operator = models.ForeignKey(Operator, on_delete=models.CASCADE, db_index=True)
    location = models.ForeignKey(Location, on_delete=models.CASCADE, db_index=True)
    networks = models.ManyToManyField(NetworkType, related_name='points', db_index=True)

