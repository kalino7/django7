from django.test import TestCase

# Create your tests here.
from .models import *

class FlightTestCase(TestCase):
    
    def setUp(self):
        # special function that create a seperate db for only test purposes.

        # now create dummy data for testDB
        airport1 =  Airport.objects.create(code="AAA", city="City A")
        airport2 =  Airport.objects.create(code="BBB", city="City B")


        # create flight
        Flight.objects.create(origin=airport1, destination=airport2, duration=145)
        Flight.objects.create(origin=airport2, destination=airport1, duration=145)
        # below flights should fail
        Flight.objects.create(origin=airport2, destination=airport2, duration=145)
        Flight.objects.create(origin=airport2, destination=airport1, duration=-100)

    # now run test
    def test_valid_flight(self):
        """Testing if a flight is valid"""
        air1 = Airport.objects.get(code="AAA")
        air2 = Airport.objects.get(code="BBB")
        flight_record = Flight.objects.get(origin=air1, destination=air2, duration =145)
        self.assertTrue(flight_record.is_valid_flight()) 
    
    def test_invalid_flight_destination(self):
        """Testing invalidity of the destination"""
        air1 = Airport.objects.get(code="BBB")
        flight_record = Flight.objects.get(origin=air1, destination=air1)
        self.assertFalse(flight_record.is_valid_flight()) 
    
    def test_invalid_flight_duration(self):
        """Testing invalid duration"""
        flight_record = Flight.objects.get(duration=-100)
        self.assertFalse(flight_record.is_valid_flight()) 