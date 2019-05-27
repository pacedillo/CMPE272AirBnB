import datetime
from db.book import Book
from mongoengine import Document, StringField, DateTimeField, ReferenceField, ListField, FloatField, BooleanField, \
    URLField, ListField

class listing(Document):
    #customer_name = StringField(required=True, max_length=200)
    #books = ListField(ReferenceField(Book, required=True))
    #shipping_address = StringField(required=True, max_length=200)
    #total_price = FloatField(min_value=0)
    #order_status = StringField(required=True, max_length=50, default="processing")
    #order_date = DateTimeField(default=datetime.datetime.now)
    id = StringField(required=True, max_length=200)
    #listing_url = Stringfield(required=True, max_length=200)  #Will need to check if there is a better field)
    listing_url = URLField()
    scrape_id = StringField(required=True, max_length=200)
    last_scraped = DateTimeField(default=datetime.datetime.now)
    name = StringField(required=True, max_length=200)
    summary = StringField(required=True, max_length=3000)
    # watch out for improper string inputs for '=- ...', used bullet points, need to figure out how to make columns
    # active
    # max summary length from db is 2526 characters
    space = StringField(required=True, max_length=2500)
    # watch out for improper string inputs for '=- ...', used bullet points, need to figure out how to make columns
    # active
    # max summary length from db is 2156 characters
    description = StringField(required=True, max_length=3000)
    # watch out for improper string inputs for '=- ...', used bullet points, need to figure out how to make columns
    # active
    # max summary length from db is 2742 characters
    experiences_offered = StringField(required=True, max_length=200)
    neighborhood_overview = StringField(required=True, max_length=2000)
    # watch out for improper string inputs for '=- ...', used bullet points, need to figure out how to make columns
    # active
    # max summary length from db is 1503 characters
    notes = StringField(required=True, max_length=3000)
    # watch out for improper string inputs for '=- ...', used bullet points, need to figure out how to make columns
    # active
    # max summary length from db is 2290 characters
    transit = StringField(required=True, max_length=2500)
    # watch out for improper string inputs for '=- ...', used bullet points, need to figure out how to make columns
    # active
    # max summary length from db is 1969 characters
    access = StringField(required=True, max_length=2500)
    # watch out for improper string inputs for '=- ...', used bullet points, need to figure out how to make columns
    # active
    # max summary length from db is 1289 characters
    interaction = StringField(required=True, max_length=2500)
    # watch out for improper string inputs for '=- ...', used bullet points, need to figure out how to make columns
    # active
    # max summary length from db is 1457 characters
    house_rules = StringField(required=True, max_length=2000)
    # watch out for improper string inputs for '=- ...', used bullet points, need to figure out how to make columns
    # active
    # max summary length from db is 1666 characters
    thumbnail_url = StringField(required=True, max_length=200)
    medium_url = StringField(required=True, max_length=200)
    picture_url = StringField(required=True, max_length=200)
    xl_picture_url = StringField(required=True, max_length=200)
    host_id = StringField(required=True, max_length=200)
    host_url = StringField(required=True, max_length=200)
    host_name = StringField(required=True, max_length=200)
    host_since = DateTimeField(default=datetime.datetime.now)
    host_location = StringField(required=True, max_length=200)
    host_about = StringField(required=True, max_length=8000)
    # watch out for improper string inputs for '=- ...', used bullet points, need to figure out how to make columns
    # active
    # max summary length from db is 7705 characters
    host_response_time = StringField(required=True, max_length=200)
    host_response_rate = StringField(required=True, max_length=4, unique=True, regex=r"(\d+(\.\d+)?%")
    host_acceptance_rate = StringField(required=True, max_length=200)
    host_is_superhost = BooleanField(default=False)  # need to check
    host_thumbnail_url= StringField(required=True, max_length=200)
    host_picture_url= StringField(required=True, max_length=200)
    host_neighbourhood = StringField(required=True, max_length=200)
    host_listings_count = FloatField(min_value=0)
    host_total_listings_count = FloatField(min_value=0)
    host_verifications = StringField(required=True, max_length=200)
    host_has_profile_pic = BooleanField(default=False)  # need to check
    host_identity_verified = BooleanField(default=False)  # need to check
    street = StringField(required=True, max_length=200)
    neighbourhood= StringField(required=True, max_length=200)
    neighbourhood_cleansed = StringField(required=True, max_length=200)
    neighbourhood_group_cleansed = StringField(required=True, max_length=200)
    city = StringField(required=True, max_length=200)
    state = StringField(required=True, max_length=200)
    zipcode = StringField(required=True, max_length=200)
    market = StringField(required=True, max_length=200)
    smart_location = StringField(required=True, max_length=200)
    country_code = StringField(required=True, max_length=200)
    country = StringField(required=True, max_length=200)
    latitude = FloatField(min_value=-180.000, max_value=180.000)
    longitude = FloatField(min_value=-180.000, max_value=180.000)
    is_location_exact = BooleanField(default=False)
    property_type = StringField(required=True, max_length=200)  #can be list
    room_type = StringField(required=True, max_length=200)
    accommodates = FloatField(min_value=0)
    bathrooms = FloatField(min_value=0)
    bedrooms = FloatField(min_value=0)
    beds = FloatField(min_value=0)
    bed_type = StringField(required=True, max_length=200)
    amenities = StringField(required=True, max_length=200)  # need to check how to list this
    square_feet = FloatField(min_value=0)
    price = FloatField(min_value = 0)
    weekly_price = FloatField(min_value = 0)
    monthly_price = FloatField(min_value = 0)
    security_deposit = FloatField(min_value = 0)
    cleaning_fee = FloatField(min_value = 0)
    guests_included = FloatField(min_value = 0)
    extra_people = FloatField(min_value = 0)
    minimum_nights = FloatField(min_value = 0)
    maximum_nights = FloatField(min_value = 0)
    calendar_updated = StringField(required=True, max_length=200) # need to check if this is correct
    has_availability = BooleanField(default=False)
    availability_30 = FloatField(min_value = 0)
    availability_60 = FloatField(min_value = 0)
    availability_90 = FloatField(min_value = 0)
    availability_365 = FloatField(min_value = 0)
    calendar_last_scraped = DateTimeField(default=datetime.datetime.now)
    number_of_reviews = FloatField(min_value = 0)
    first_review = DateTimeField(default=datetime.datetime.now)
    last_review = DateTimeField(default=datetime.datetime.now)
    review_scores_rating =FloatField(min_value=0, max_value=100)
    review_scores_accuracy = FloatField(min_value = 0, max_value=10)
    review_scores_cleanliness = FloatField(min_value = 0, max_value=10)
    review_scores_checkin = FloatField(min_value = 0, max_value=10)
    review_scores_communication = FloatField(min_value = 0, max_value=10)
    review_scores_location = FloatField(min_value = 0, max_value=10)
    review_scores_value = FloatField(min_value = 0, max_value=10)
    requires_license = BooleanField(default=True)
    license = StringField(required=True, max_length=200)
    jurisdiction_names = StringField(required=True, max_length=200)
    instant_bookable = BooleanField(default=True)
    is_business_travel_ready = BooleanField(default=True)
    cancellation_policy = StringField(required=True, max_length=200)  #can be list
    require_guest_profile_picture = BooleanField(default=True)
    require_guest_phone_verification = BooleanField(default=True)
    calculated_host_listings_count = FloatField(min_value=0)
    reviews_per_month = FloatField(min_value=0)


