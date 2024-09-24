import uuid
from email.policy import default

from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    # Link Profile to Django's built-in User model (one-to-one relationship)
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    first_name = models.CharField(max_length=255, blank = True, null = True)
    last_name = models.CharField(max_length=255, blank = True, null = True)
    location = models.CharField(max_length=200, blank=True, null=True, default="Earth")
    email = models.EmailField(unique=True, blank = True, null = True)
    profile_image = models.ImageField(null=True, blank=True, upload_to='static/images/profiles/', default="static/images/profiles/user-default.png")
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)

    # Trading preferences
    preferred_trading_platform = models.CharField(max_length=255)
    preferred_markets = models.CharField(max_length=255, default="Forex")
    risk_reward_ratio = models.FloatField(default=0.5)  # 1:2 ratio

    # Account settings
    initial_balance = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
    stop_loss_enabled = models.BooleanField(default=True)
    max_trades_per_day = models.IntegerField(default=3)
    dynamic_balance_update = models.BooleanField(default=True)

    # Performance tracking
    total_profit = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
    total_loss = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
    total_trades = models.IntegerField(default=0)

    def __str__(self):
        return str(self.user.username)

    @property
    def imageURL(self):
        try:
            url = self.profile_image.url
        except:
            url = ''
        return url