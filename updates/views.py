from django.shortcuts import render
from .models import Participant, Notification, Ping
from .serializers import ParticipantSerializer, NotificationSerializer, PingSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated


class ParticipantView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        participants = Participant.objects.all()
        serializer = ParticipantSerializer(participants, many=True)
        return Response(serializer.data)

    def post(self, request):
        # print("DEBUG IN PARTICIPANT: ", type(request.data))
        serializer = ParticipantSerializer(data=request.data)

        # print(request.data, serializer.is_valid(), serializer.validated_data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class NotificationView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        notifications = Notification.objects.all()
        serializer = NotificationSerializer(notifications, many=True)
        return Response(serializer.data)

    def post(self, request):
        # print("DEBUG IN NOTIFICATION: ", type(request.data))
        serializer = NotificationSerializer(data=request.data)

        # print(request.data, serializer.is_valid(), serializer.validated_data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PingView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        pings = Ping.objects.all()
        serializer = PingSerializer(pings, many=True)
        return Response(serializer.data)

    def post(self, request):
        # print("DEBUG IN PING: ", type(request.data))
        serializer = PingSerializer(data=request.data)

        # print(request.data, serializer.is_valid(), serializer.validated_data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
