# django-api-exercise

To properly run the project, you will have to have docker and docker-compose installed in your system.  
After cloning the repository, in the root of the project run the following:
```shell
docker-compose -f docker-compose.dev.yaml up
``` 
Now you will be able to access the endpoints and data, accessing http://localhost:8000/api/
```json
{
    "properties": "http://localhost:8000/api/properties/",
    "listing": "http://localhost:8000/api/listing/",
    "booking": "http://localhost:8000/api/booking/"
}
```

## Endpoints:
### Properties
#### Description
http://localhost:8000/api/properties/  
The endpoint retrieves the list of properties or one specific property.
#### Details
Listing all properties --> http://localhost:8000/api/properties/  
Getting data from one property --> http://localhost:8000/api/properties/<property_code>  
Response example:
```json
{
    "id": 6,
    "property_code": "MAGA8966",
    "guests_max_number": 8,
    "bathrooms_quantity": 2,
    "accepts_animals": false,
    "cleaning_cost": "100.00",
    "activation_date": "2024-03-12",
    "creation_timestamp": "2024-03-10T18:21:19.935000Z",
    "update_timestamp": "2024-03-10T18:21:19.935000Z"
}
```
### Listing
#### Description
http://localhost:8000/api/listing/  
Retrieves all listing properties available to be booked.
#### Details
Response example:
```json
[
    {
        "id": 5,
        "published_platform": "booking.com",
        "published_platform_fee": "20.00",
        "creation_timestamp": "2024-03-10T18:22:11.554000Z",
        "update_timestamp": "2024-03-10T18:22:11.554000Z",
        "property": 5
    },
    {
        "id": 4,
        "published_platform": "airbnb",
        "published_platform_fee": "10.00",
        "creation_timestamp": "2024-03-10T18:21:58.421000Z",
        "update_timestamp": "2024-03-10T18:21:58.421000Z",
        "property": 2
    } 
]
```
### Booking
#### Description
http://localhost:8000/api/booking/  
Retrieves all or one booking.
#### Details
Listing all properties --> http://localhost:8000/api/booking/  
Getting data from one property --> http://localhost:8000/api/booking/<booking_code>  
Response example:
```json
{
    "id": 9,
    "booking_code": "UZSP2061",
    "checkin_date": "2024-03-21",
    "checkout_date": "2024-03-30",
    "total_value": "200.00",
    "comments": "qweqwe",
    "guests_quantity": 3,
    "creation_timestamp": "2024-03-10T18:27:03.286000Z",
    "update_timestamp": "2024-03-10T18:27:03.286000Z",
    "listing": 2
}
```