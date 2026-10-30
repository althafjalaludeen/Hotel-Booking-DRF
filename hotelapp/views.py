from django.shortcuts import get_object_or_404
from hotelapp.models import HotelDB, RoomDB, CustomerDB, BookingDB
from hotelapp.serializers import HotelSerializer, RoomSerializer, CustomerSerializer, BookingSerializer
from rest_framework.views import APIView
from rest_framework.response import Response


#class for listing all hotels and creating a new hotel
class HotelListCreateView(APIView):
    def get(self, request):
        qs = HotelDB.objects.all()
        serializer_instance = HotelSerializer(qs, many=True)
        return Response(serializer_instance.data)

    def post(self, request):
        form_data = request.data
        serializer_instance = HotelSerializer(data=form_data)
        if serializer_instance.is_valid():
            serializer_instance.save()
            return Response({"message": "Hotel added successfully."})
        else:
            return Response(serializer_instance.errors)

# class for retrieving, updating, and deleting a specific hotel
class HotelRetrieveUpdateDeleteView(APIView):
    def get(self, request, pk):
        qs = get_object_or_404(HotelDB, pk=pk)
        serializer_instance = HotelSerializer(qs)
        return Response(serializer_instance.data)

    def put(self, request, pk):
        form_data = request.data
        qs = get_object_or_404(HotelDB, pk=pk)
        serializer_instance = HotelSerializer(qs, data=form_data)
        if serializer_instance.is_valid():
            serializer_instance.save()
            return Response({"message": "Hotel updated successfully."})
        else:
            return Response(serializer_instance.errors)

    def delete(self, request, pk):
        qs = get_object_or_404(HotelDB, pk=pk)
        qs.delete()
        return Response({"message": "Hotel deleted successfully."})

# class for listing all rooms and creating a new room
class RoomListCreateView(APIView):
    def get(self, request):
        qs = RoomDB.objects.all()
        serializer_instance = RoomSerializer(qs, many=True)
        return Response(serializer_instance.data)

    def post(self, request):
        form_data = request.data
        serializer_instance = RoomSerializer(data=form_data)
        if serializer_instance.is_valid():
            serializer_instance.save()
            return Response({"message": "Room added successfully."})
        else:
            return Response(serializer_instance.errors)

# class for retrieving, updating, and deleting a specific room
class RoomRetrieveUpdateDeleteView(APIView):
    def get(self, request, pk):
        qs = get_object_or_404(RoomDB, pk=pk)
        serializer_instance = RoomSerializer(qs)
        return Response(serializer_instance.data)

    def put(self, request, pk):
        form_data = request.data
        qs = get_object_or_404(RoomDB, pk=pk)
        serializer_instance = RoomSerializer(qs, data=form_data)
        if serializer_instance.is_valid():
            serializer_instance.save()
            return Response({"message": "Room updated successfully."})
        else:
            return Response(serializer_instance.errors)

    def delete(self, request, pk):
        qs = get_object_or_404(RoomDB, pk=pk)
        qs.delete()
        return Response({"message": "Room deleted successfully."})

# class for listing all customers and creating a new customer
class CustomerListCreateView(APIView):
    def get(self, request):
        qs = CustomerDB.objects.all()
        serializer_instance = CustomerSerializer(qs, many=True)
        return Response(serializer_instance.data)

    def post(self, request):
        form_data = request.data
        serializer_instance = CustomerSerializer(data=form_data)
        if serializer_instance.is_valid():
            serializer_instance.save()
            return Response({"message": "Customer added successfully."})
        else:
            return Response(serializer_instance.errors)

# class for retrieving, updating, and deleting a specific customer
class CustomerRetrieveUpdateDeleteView(APIView):
    def get(self, request, pk):
        qs = get_object_or_404(CustomerDB, pk=pk)
        serializer_instance = CustomerSerializer(qs)
        return Response(serializer_instance.data)

    def put(self, request, pk):
        form_data = request.data
        qs = get_object_or_404(CustomerDB, pk=pk)
        serializer_instance = CustomerSerializer(qs, data=form_data)
        if serializer_instance.is_valid():
            serializer_instance.save()
            return Response({"message": "Customer updated successfully."})
        else:
            return Response(serializer_instance.errors)

    def delete(self, request, pk):
        qs = get_object_or_404(CustomerDB, pk=pk)
        qs.delete()
        return Response({"message": "Customer deleted successfully."})

# class for listing all bookings and creating a new booking
class BookingListCreateView(APIView):
    def get(self, request):
        qs = BookingDB.objects.all()
        serializer_instance = BookingSerializer(qs, many=True)
        return Response(serializer_instance.data)

    def post(self, request):
        form_data = request.data
        serializer_instance = BookingSerializer(data=form_data)
        if serializer_instance.is_valid():
            serializer_instance.save()
            return Response({"message": "Booking added successfully."})
        else:
            return Response(serializer_instance.errors)

# class for retrieving, updating, and deleting a specific booking
class BookingRetrieveUpdateDeleteView(APIView):
    def get(self, request, pk):
        qs = get_object_or_404(BookingDB, pk=pk)
        serializer_instance = BookingSerializer(qs)
        return Response(serializer_instance.data)

    def put(self, request, pk):
        form_data = request.data
        qs = get_object_or_404(BookingDB, pk=pk)
        serializer_instance = BookingSerializer(qs, data=form_data)
        if serializer_instance.is_valid():
            serializer_instance.save()
            return Response({"message": "Booking updated successfully."})
        else:
            return Response(serializer_instance.errors)

    def delete(self, request, pk):
        qs = get_object_or_404(BookingDB, pk=pk)
        qs.delete()
        return Response({"message": "Booking deleted successfully."})