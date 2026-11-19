from django.shortcuts import render


def churncalculator(request):

    LostCus = float(request.POST.get('LostCust', '0') or '0')
    StartCus = float(request.POST.get('StartCust', '0') or '0')

    if request.method == 'POST' and StartCus != 0:
        Churn= (LostCus / StartCus) * 100
    else:
        Churn = 0

    print("Lost Customers =", LostCus)
    print("Starting Customers =", StartCus)
    print("Churn Percentage =", Churn)

    return render(
        request,
        'myapp/calc.html',
        {
            'LostCus': LostCus,
            'StartCus': StartCus,
            'Churn': Churn
        }
    )
