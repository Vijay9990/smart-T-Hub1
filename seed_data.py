import pymongo
from datetime import datetime, timedelta

# Connect to MongoDB
mongo_uri = os.getenv("MONGO_URI")
client = pymongo.MongoClient(mongo_uri)

# Clear existing data
db.rider.delete_many({})
db.driver.delete_many({})
db.location.delete_many({})
db.rides.delete_many({})
db.booking.delete_many({})
db.payment.delete_many({})
db.review.delete_many({})

# Seed locations
locations = [
    {
        "location_name": "Downtown",
        "latitude": "40.7128",
        "longitude": "-74.0060",
        "status": "active"
    },
    {
        "location_name": "Uptown",
        "latitude": "40.7831",
        "longitude": "-73.9712",
        "status": "active"
    },
    {
        "location_name": "Midtown",
        "latitude": "40.7549",
        "longitude": "-73.9840",
        "status": "active"
    }
]
db.location.insert_many(locations)

# Seed riders
riders = [
    {
        "name": "John Doe",
        "email": "john@example.com",
        "password": "password123",
        "phone": "1234567890",
        "status": "active"
    },
    {
        "name": "Jane Smith",
        "email": "jane@example.com",
        "password": "password123",
        "phone": "0987654321",
        "status": "active"
    }
]
db.rider.insert_many(riders)

# Seed drivers
drivers = [
    {
        "name": "Mike Johnson",
        "email": "mike@example.com",
        "password": "password123",
        "phone": "1112223333",
        "license_number": "DL123456",
        "vehicle_number": "ABC123",
        "vehicle_type": "Sedan",
        "status": "active"
    },
    {
        "name": "Sarah Williams",
        "email": "sarah@example.com",
        "password": "password123",
        "phone": "4445556666",
        "license_number": "DL789012",
        "vehicle_number": "XYZ789",
        "vehicle_type": "SUV",
        "status": "active"
    }
]
db.driver.insert_many(drivers)

# Get inserted IDs
location_ids = [str(loc["_id"]) for loc in db.location.find()]
driver_ids = [str(driver["_id"]) for driver in db.driver.find()]
rider_ids = [str(rider["_id"]) for rider in db.rider.find()]

# Seed rides
rides = [
    {
        "driver_id": driver_ids[0],
        "from_location": location_ids[0],
        "to_location": location_ids[1],
        "date": (datetime.now() + timedelta(days=1)).strftime("%Y-%m-%d"),
        "time": "10:00",
        "price": 25.00,
        "seats": 4,
        "status": "active"
    },
    {
        "driver_id": driver_ids[1],
        "from_location": location_ids[1],
        "to_location": location_ids[2],
        "date": (datetime.now() + timedelta(days=2)).strftime("%Y-%m-%d"),
        "time": "15:30",
        "price": 30.00,
        "seats": 4,
        "status": "active"
    }
]
db.rides.insert_many(rides)

# Get ride IDs
ride_ids = [str(ride["_id"]) for ride in db.rides.find()]

# Seed bookings
bookings = [
    {
        "ride_id": ride_ids[0],
        "rider_id": rider_ids[0],
        "seats": 2,
        "status": "confirmed",
        "booking_date": datetime.now().strftime("%Y-%m-%d")
    },
    {
        "ride_id": ride_ids[1],
        "rider_id": rider_ids[1],
        "seats": 1,
        "status": "confirmed",
        "booking_date": datetime.now().strftime("%Y-%m-%d")
    }
]
db.booking.insert_many(bookings)

# Get booking IDs
booking_ids = [str(booking["_id"]) for booking in db.booking.find()]

# Seed payments
payments = [
    {
        "booking_id": booking_ids[0],
        "amount": 50.00,
        "payment_date": datetime.now().strftime("%Y-%m-%d"),
        "status": "completed"
    },
    {
        "booking_id": booking_ids[1],
        "amount": 30.00,
        "payment_date": datetime.now().strftime("%Y-%m-%d"),
        "status": "completed"
    }
]
db.payment.insert_many(payments)

# Seed reviews
reviews = [
    {
        "ride_id": ride_ids[0],
        "rider_id": rider_ids[0],
        "driver_id": driver_ids[0],
        "rating": 5,
        "review": "Great ride, very comfortable and on time!",
        "review_date": datetime.now().strftime("%Y-%m-%d")
    },
    {
        "ride_id": ride_ids[1],
        "rider_id": rider_ids[1],
        "driver_id": driver_ids[1],
        "rating": 4,
        "review": "Good service, would ride again.",
        "review_date": datetime.now().strftime("%Y-%m-%d")
    }
]
db.review.insert_many(reviews)

print("Database seeded successfully!") 