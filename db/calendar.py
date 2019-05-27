import datetime
from mongoengine import Document, StringField, DateTimeField, FloatField, BooleanField, DateField


class calendar(Document):
    listing_id = StringField(required=True, max_length=200)
    date = DateTimeField(default=datetime.datetime.utcnow())  # currently incorrect, need to change
    available = BooleanField(default=False)  #need to check
    price = FloatField(min_value=0)
    # published = DateTimeField(default=datetime.datetime.utcnow())
    # publisher = StringField(max_length=200)

