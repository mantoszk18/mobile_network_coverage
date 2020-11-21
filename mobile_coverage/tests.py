from django.test import TestCase

"""
Since w don't have any logic in the models and are not using serializers, there are no tests for those.

But we do have logic in the view (and even some custom methods there).
That's the place which should be tested with an integration test. Testing the endpoint.

"""

