from rest_framework import serializers
from .models import Participant, Notification

class ParticipantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Participant
        fields = '__all__'

    def create(self, validated_data):
        return Participant.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.restart_group = validated_data.get('restart_group', instance.restart_group)
        instance.message_group = validated_data.get('message_group', instance.message_group)
        instance.mturk_id = validated_data.get('mturk_id', instance.mturk_id)
        instance.hash_id = validated_data.get('hash_id', instance.hash_id)
        instance.install_date = validated_data.get('install_date', instance.install_date)
        instance.windows_version = validated_data.get('windows_version', instance.windows_version)
        instance.dot_net_version = validated_data.get('dot_net_version', instance.dot_net_version)
        instance.save()
        return instance



class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = '__all__'

    def create(self, validated_data):
        return Notification.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.mturk_id = validated_data.get('mturk_id', instance.mturk_id)
        instance.sequence = validated_data.get('sequence', instance.sequence)
        instance.noti_date = validated_data.get('noti_date', instance.noti_date)
        instance.duration = validated_data.get('duration', instance.duration)
        instance.response = validated_data.get('response', instance.response)
        instance.save()
        return instance
