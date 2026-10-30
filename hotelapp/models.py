from django.db import models


class HotelDB(models.Model):
    hotel_name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    address = models.TextField()
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    rating = models.FloatField()

    def __str__(self):
        return self.hotel_name

class RoomDB(models.Model):
    hotel = models.ForeignKey(HotelDB, on_delete=models.CASCADE)
    room_number = models.CharField(max_length=10)
    room_type = models.CharField(max_length=50)
    price_per_night = models.PositiveIntegerField()
    capacity = models.PositiveIntegerField()

    def __str__(self):
        return self.room_number

class CustomerDB(models.Model):
    customer_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    age = models.PositiveIntegerField()

    def __str__(self):
        return self.customer_name

class BookingDB(models.Model):
    customer = models.ForeignKey(CustomerDB, on_delete=models.CASCADE)
    room = models.ForeignKey(RoomDB, on_delete=models.CASCADE)
    check_in_date = models.DateField()
    check_out_date = models.DateField()
    number_of_nights = models.PositiveIntegerField(editable=False,null=True)
    total_amount = models.PositiveIntegerField(editable=False,null=True)
    status = models.CharField(max_length=20, default='Pending')
    created_at = models.DateTimeField(auto_now_add=True)

# The Below method calculates the number of nights and total amount based on the check-in and check-out dates, and the room's price per night. 
# It overrides the save method to perform these calculations before saving the booking instance to the database.

    def save(self, *args, **kwargs):

        # The if statement checks if the check-out date is less than or equal to the check-in date. 
        # If it is, a ValueError is raised with a message indicating that the check-out date must be after the check-in date. 
        # This ensures that the booking dates are valid and prevents any logical errors in the booking process.

        if self.check_out_date <= self.check_in_date:
            raise ValueError("Check-out date must be after check-in date.")

        self.number_of_nights = (self.check_out_date - self.check_in_date).days
        room_object = RoomDB.objects.get(id=self.room_id)
        self.total_amount = self.number_of_nights * room_object.price_per_night
        super().save(*args, **kwargs)

    def __str__(self):
        return self.customer.customer_name
