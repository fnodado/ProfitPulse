from django.forms import ModelForm
from .models import Trade

class TradeForm(ModelForm):
    class Meta:
        model = Trade
        fields = ['trade_type', 'symbol',
                  'price', 'stop_loss', 'take_profit',
                  'current_price']

    def __init__(self, *args, **kwargs):
        super(TradeForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'input'})