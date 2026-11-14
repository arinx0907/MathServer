from django.shortcuts import render


def churn_calculator(request):

    Lost_Customers = float(request.POST.get('LostCust', '0') or '0')
    Starting_Customers = float(request.POST.get('StartCust', '0') or '0')

    if request.method == 'POST' and Starting_Customers != 0:
        Churn_Percentage = (Lost_Customers / Starting_Customers) * 100
    else:
        Churn_Percentage = 0

    print("Lost Customers =", Lost_Customers)
    print("Starting Customers =", Starting_Customers)
    print("Churn Percentage =", Churn_Percentage)

    return render(
        request,
        'myapp/calc.html',
        {
            'Lost_Customers': Lost_Customers,
            'Starting_Customers': Starting_Customers,
            'Churn_Percentage': Churn_Percentage
        }
    )
