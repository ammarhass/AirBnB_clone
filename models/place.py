#!/usr/bin/python3
""" class place"""


class Place(BaseModel):
    '''Define Place class'''
    name = ""
    city_id = ""
    user_id = ""
    name = ""
    description
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longtude = 0.0
    amenity_ids = []
