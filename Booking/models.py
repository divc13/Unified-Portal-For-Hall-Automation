from django.db import models

# Create your models here.
class sports_equipments_request(models.Model):
    #Equipment quantity status

    #Equipment choices
    CRICKET_BAT = 'CB'
    TABLE_TENNIS = 'TT'
    BADMINTON = 'BM'
    HOCKEY = 'HK'
    BASKETBALL = 'BB'
    FOOTBALL = 'FB'
    EQUIPMENT_CHOICES = [
        (CRICKET_BAT, 'Cricket Bat'),
        (TABLE_TENNIS, 'Table Tennis'),
        (BADMINTON, 'Badminton'),
        (BASKETBALL,  'Basketball'),
        (HOCKEY, 'Hockey'),
        (FOOTBALL,'Football')
    ]


    equipment_selected = models.CharField(
        max_length=100,
        choices=EQUIPMENT_CHOICES,
        default=CRICKET_BAT
    )
 

    #Essentials
    date = models.DateField()
    name = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    argument = models.CharField(max_length=150, default='Default_value')
    secy_validation = models.CharField(max_length=10,default='NO')
    student_return_request = models.CharField(max_length=20,default='NO')
    
    def __str__(self):
        return self.argument


class sports_equipments_registered(models.Model):
    #Equipment choices
    CRICKET_BAT = 'CB'
    TABLE_TENNIS = 'TT'
    BADMINTON = 'BM'
    HOCKEY = 'HK'
    BASKETBALL = 'BB'
    FOOTBALL = 'FB'
    EQUIPMENT_CHOICES = [
        (CRICKET_BAT, 'Cricket Bat'),
        (TABLE_TENNIS, 'Table Tennis'),
        (BADMINTON, 'Badminton'),
        (BASKETBALL,  'Basketball'),
        (HOCKEY, 'Hockey'),
        (FOOTBALL, 'Football')
    ]

    equipments = models.CharField(
        max_length=2,
        choices=EQUIPMENT_CHOICES,
        default=CRICKET_BAT
    )
    quantity = models.IntegerField()

    def __str__(self):
        return self.equipments

class Guestroom(models.Model):

    room = models.CharField(max_length=1)

    #status choices
    BOOK = 'book'
    UNAVAILABLE = 'unavailable'

    STATUS_CHOICES = [
        (BOOK,'Book'),
        (UNAVAILABLE, 'Item is Booked')
    ]

    status = models.CharField(
        max_length=100,
        choices = STATUS_CHOICES
    )
    checkin_date = models.DateField()
    checkout_date = models.DateField()
    price = models.CharField(max_length=100)
    manager_validation = models.CharField(max_length=10,default='NO')


    #Essentials
    date = models.DateField()
    name = models.CharField(max_length=100)
    username = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Courts(models.Model):
    CRICKET = 'Cricket'
    TABLE_TENNIS = 'Table Tennis'
    BADMINTON = 'Badminton'
    HOCKEY = 'Hockey'
    BASKETBALL = 'Basketball'
    FOOTBALL = 'Football'
    SPORTS_CHOICES = [
        (CRICKET, 'Cricket'),
        (TABLE_TENNIS, 'Table Tennis'),
        (BADMINTON, 'Badminton'),
        (BASKETBALL,  'Basketball'),
        (HOCKEY, 'Hockey'),
        (FOOTBALL, 'Football')
    ]

    sports = models.CharField(
        max_length=100,
        choices=SPORTS_CHOICES,
        default=CRICKET
    )

    day_of_booking = models.DateField()
    time_of_checkin = models.TimeField()
    time_of_checkout = models.TimeField()

    #Essentials
    date = models.DateField()
    name = models.CharField(max_length=100)
    username = models.CharField(max_length=100)

    def __str__(self):
        return self.sports
    
class sports_equipmnents_store(models.Model):
    
    CRICKET_BAT = 'CB'
    TABLE_TENNIS = 'TT'
    BADMINTON = 'BM'
    HOCKEY = 'HK'
    BASKETBALL = 'BB'
    FOOTBALL = 'FB'
    EQUIPMENT_CHOICES = [
        (CRICKET_BAT, 'Cricket Bat'),
        (TABLE_TENNIS, 'Table Tennis'),
        (BADMINTON, 'Badminton'),
        (BASKETBALL,  'Basketball'),
        (HOCKEY, 'Hockey'),
        (FOOTBALL, 'Football')
    ]

    equipments_store = models.CharField(
        max_length=2,
        choices=EQUIPMENT_CHOICES,
        default=CRICKET_BAT
    )
    quantity_store= models.IntegerField()

    def __str__(self):
        return self.equipments_store