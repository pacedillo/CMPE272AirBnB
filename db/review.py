import datetime
from mongoengine import Document, StringField, DateTimeField, FloatField, BooleanField, DateField


class review(Document):
    listing_id = StringField(required=True, max_length=200)
    date = DateTimeField(default=datetime.datetime.utcnow())  # currently incorrect, need to change
    available = BooleanField(default=False)  #need to check
    price = FloatField(min_value=0)
    # published = DateTimeField(default=datetime.datetime.utcnow())
    # publisher = StringField(max_length=200)
    id= StringField(required=True, max_length=200)
    reviewer_id= StringField(required=True, max_length=200)
    reviewer_name= StringField(required=True, max_length=200)
    comments= StringField(required=True, max_length=8000)
    # watch out for improper string inputs for '=- ...', used bullet points, need to figure out how to make columns
    # active
    # max summary length from db is 7519 characters


