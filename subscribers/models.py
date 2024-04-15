from django.db import models
from customusers.models import CustomUser

class Subscriber(models.Model):
    subscribing_user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="subscribinguser_subscriber_set")
    subscribed_user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="subscribeduser_subscriber_set")



