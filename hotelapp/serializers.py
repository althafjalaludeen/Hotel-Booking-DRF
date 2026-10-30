from rest_framework import serializers
from hotelapp.models import HotelDB, BookingDB, RoomDB, CustomerDB
from django.utils import timezone

# Serializer for HotelDB model
class HotelSerializer(serializers.ModelSerializer):
    class Meta:
        model = HotelDB
        fields = '__all__'
        
# Serializer for RoomDB model
class RoomSerializer(serializers.ModelSerializer):
    availability_status = serializers.SerializerMethodField()
    class Meta:
        model = RoomDB
        fields = '__all__'

    def get_availability_status(self, obj):
        today = timezone.localdate()

        existing_booking = BookingDB.objects.filter(
            room=obj,
            check_in_date__lte=today,
            check_out_date__gt=today
        ).exclude(status='Cancelled').exists()

        if existing_booking:
            return "Booked"

        return "Available"



# Serializer for CustomerDB model
class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomerDB
        fields = '__all__'  

# Serializer for BookingDB model
class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookingDB
        fields = '__all__'
        read_only_fields = ('number_of_nights', 'total_amount', 'created_at')

    def validate(self, validated_data): 
        room = validated_data.get('room') 
        check_in_date = validated_data.get('check_in_date') 
        check_out_date = validated_data.get('check_out_date')

        # checks if the room is available for the given check-in and check-out dates.
        existing_bookings = BookingDB.objects.filter(
            room=room, check_in_date__lt=check_out_date, 
            check_out_date__gt=check_in_date).exclude(status='Cancelled')

        if self.instance:
            existing_bookings = existing_bookings.exclude(id = self.instance.id)

        if existing_bookings.exists():
            raise serializers.ValidationError("The room is not available for the selected dates.")

        return validated_data
