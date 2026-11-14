# Ex.03 Design a Website for Server Side Processing
## Date:

## AIM:
To create a web page to calculate Churn Rate using server-side scripts.

## FORMULA:
Churn Rate = (CustLost / InitCust) * 100
<br> InitCust --> Initial Customers Count
<br> CustLost --> Customers Lost Count

## DESIGN STEPS:

### Step 1:
Clone the repository from GitHub.

### Step 2:
Create Django Admin project.

### Step 3:
Create a New App under the Django Admin project.

### Step 4:
Create a HTML file to implement form based input and output.

### Step 5:
Create python programs for views and urls to perform server side processing.

### Step 6:
Receive input values from the form using request.POST.get().

### Step 7:
Calculate the Result using the given formula.

### Step 8:
Display the calculated result in the server console.

### Step 9:
Render the result to the HTML template.

### Step 10:
Publish the website in Localhost.

## PROGRAM:
calc.html
```
<html>
    <head>
        <title>Customer Churn</title>
    </head>

    <body>

        <h1>Harini Shree S (26014130)</h1>
        <h2>Customer Churn Rate Calculator</h2>

        <form method="POST">
            {% csrf_token %}

            <label>Lost Customers:</label>
            <input type="number" step="any"
                   value="{{ Lost_Customers }}"
                   name="LostCust">

            <br><br>

            <label>Starting Customers:</label>
            <input type="number" step="any"
                   value="{{ Starting_Customers }}"
                   name="StartCust">

            <br><br>

            <button type="submit">Calculate Churn</button>

            <br><br>

            <label>Calculated Churn Rate:</label>
            <input type="number" step="any"
                   value="{{ Churn_Percentage }}"
                   readonly>

        </form>

    </body>
</html>
```
views.py
```
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
```
urls.py
```
from django.contrib import admin
from django.urls import path
from myapp import views

urlpatterns = [
    path('', views.churn_calculator, name='customer_churn'),
]
```

## OUTPUT - SERVER SIDE:
<img width="1920" height="1080" alt="Screenshot (48)" src="https://github.com/user-attachments/assets/7f8c5d3b-8b51-481f-9769-9e17bbf818c9" />


## OUTPUT - WEBPAGE:
<img width="1920" height="1080" alt="Screenshot (47)" src="https://github.com/user-attachments/assets/96b4c5c6-d51a-4b78-930b-9e0637b18f69" />


## RESULT:
The the web page to calculate Churn Rate using server-side scripts is created successfully.
