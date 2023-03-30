from django.db import models
from datetime import datetime


class Regular_menu(models.Model):
    Day_Choices = (
        ("Monday", "Monday"),
        ("Tuesday", "Tuesday"),
        ("Wednesday", "Wednesday"),
        ("Thursday", "Thursday"),
        ("Friday", "Friday"),
        ("Saturday", "Saturday"),
        ("Sunday", "Sunday"),
    )
    Meal_Choices = (("Breakfast", "Breakfast"), ("Lunch", "Lunch"), ("Dinner", "Dinner"))
    Day = models.CharField(
        max_length=9,
        choices=Day_Choices,
        default="Monday",
        blank=True,
    )
    Meal = models.CharField(
        max_length=9,
        choices=Meal_Choices,
        default="Breakfast",
        blank=True,
    )
    Items = models.CharField(
        max_length=100,
        blank=True,
    )
    Rating = models.FloatField(
        default=0.0,
        blank=True,
    )


class Extras(models.Model):
    Meal_Choices = (
        ("Breakfast", "Breakfast"),
        ("Lunch", "Lunch"),
        ("Dinner", "Dinner"),
    )
    Meal = models.CharField(
        max_length=9,
        choices=Meal_Choices,
        default="Breakfast",
        blank=True,
    )
    Meal_Date = models.DateField(blank=True,)
    Item_Name = models.CharField(max_length=50,blank=True,)
    Price = models.IntegerField(default=20,blank=True,)
    Start_Time = models.DateTimeField(blank=True,)
    End_Time = models.DateTimeField(blank=True,)
    Capacity = models.IntegerField(default=200,blank=True,)
    Available_Orders = models.IntegerField(default=200,blank=True,)

class Orders(models.Model):
    Meal_Choices = (
        ("Breakfast", "Breakfast"),
        ("Lunch", "Lunch"),
        ("Dinner", "Dinner"),
    )
    Meal = models.CharField(
        max_length=9,
        choices=Meal_Choices,
        default="Breakfast",
    )
    Order_Date_Time = models.DateTimeField()
    Meal_Date = models.DateField()
    User_Name = models.CharField(max_length=20)
    Item_Name = models.CharField(max_length=50)
    Quantity = models.IntegerField(default=1)
    Price = models.IntegerField(default=20)
    Amount = models.IntegerField(default=20)
    History_Status = models.BooleanField(default=False)


class Datewise_BDMR(models.Model):
    Date = models.DateField(primary_key=True)
    BDMR = models.FloatField(default=0.0)


class Bill(models.Model):
    Year = models.IntegerField(default=2023)
    Bill_Month = models.IntegerField(default=1)
    Month_Name = models.TextField(max_length=9, default="January")
    Total_Days = models.IntegerField(default=0)
    rebate_days = models.IntegerField(default=0)
    User_Name = models.CharField(max_length=20)
    Basic_Amount = models.FloatField(default=0)
    Extras_Amount = models.FloatField(default=0)
    Mess_Bill = models.FloatField(default=0)

    def messbillcalc(self):
        if self.Total_Days:
            self.Mess_Bill = self.Extras_Amount + (
                (self.Basic_Amount) / (self.Total_Days)
            ) * (self.Total_Days - self.rebate_days)
        else:
            self.Mess_Bill = self.Extras_Amount


class Rebate(models.Model):
    Date_From = models.DateField()
    Date_To = models.DateField()
    Rebate_Days = models.IntegerField(default=0)
    User_Name = models.CharField(max_length=20)
    status = models.IntegerField(default=0)

    def date_diff(self):
        date_format = "%Y-%m-%d %H:%M:%S"
        a = datetime.strptime(str(self.Date_From), date_format)
        b = datetime.strptime(str(self.Date_To), date_format)
        delta = b - a
        return abs((delta).days) + 1


class Rating_Regular(models.Model):

    Meal_Choices = (("Breakfast", "Breakfast"),
        ("Lunch", "Lunch"),
        ("Dinner", "Dinner"),)
    Day_Choices = (
        ("Monday", "Monday"),
        ("Tuesday", "Tuesday"),
        ("Wednesday", "Wednesday"),
        ("Thursday", "Thursday"),
        ("Friday", "Friday"),
        ("Saturday", "Saturday"),
        ("Sunday", "Sunday"),
    )

    Meal = models.CharField(
        max_length=9,
        choices=Meal_Choices,
    )

    Day = models.CharField(
        max_length=9,
        choices=Day_Choices,
    )

    User_Name = models.CharField(max_length=20)
    Rating_Value = models.FloatField(default=0.0)