from django.shortcuts import render

from trade.forms import TradeForm


# Create your views here.
def create_trade(request):
    form = TradeForm()
    print("create_trade")

    # Check if the request is POST (when form is submitted)
    if request.method == "POST":
        print(request.POST)
        if form.is_valid():
            print("valid")
            trade = form.save(commit=False)
            print(trade)
        else:
            print("invalid")
            print("error:" , form.errors.as_data())

    context = {'form': form}
    return render(request, "trade/trade_form.html", context)
