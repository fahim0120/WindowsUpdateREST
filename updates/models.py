from django.db import models

class Participant(models.Model):
    restart_group = models.BooleanField()
    message_group = models.CharField(max_length=30)
    mturk_id = models.CharField(max_length=30)
    hash_id = models.CharField(max_length=30)
    install_date = models.DateTimeField()
    windows_version = models.CharField(max_length=50)
    dot_net_version = models.CharField(max_length=30)

    def __str__(self):
        return f'Restart: {self.restart_group} Message: {self.message_group} MTurk: {self.mturk_id}'


class Notification(models.Model):
    # participant = models.ForeignKey(Participant, on_delete=models.CASCADE)
    mturk_id = models.CharField(max_length=30)
    sequence = models.IntegerField()
    noti_date = models.DateTimeField()
    duration = models.FloatField()
    response = models.CharField(max_length=20)

    def __str__(self):
        return f'MTurk: {self.mturk_id} Sequence: {self.sequence} Response: {self.response}'



