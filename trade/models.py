from django.db import models
from users.models import Profile

# Create your models here.
# Trades model
class Trade(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='trades')
    trade_type = models.CharField(max_length=50)  # Could be 'buy' or 'sell'
    symbol = models.CharField(max_length=50)
    date = models.DateField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stop_loss = models.DecimalField(max_digits=10, decimal_places=2)
    take_profit = models.DecimalField(max_digits=10, decimal_places=2)
    current_price = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=20)  # Could be 'open', 'closed', etc.

    def __str__(self):
        return f"Trade {self.symbol} by {self.profile.user.username}"

    class Meta:
        db_table = 'trade_transaction' #Modify the table name