cleUnified Portal For Hall Automation
==================================

The application was made as a course project of [CS253A](https://www.cse.iitk.ac.in/users/isaha/Courses/sdo22.shtml/): Software Development and Operations in spring 2022 under the guidance of [Dr. Indranil Saha](https://www.cse.iitk.ac.in/users/isaha/).

Unified Portal for Hall Automation is a merged platform designed for the residents of various halls at IITK to access day to day hall functionalities. This portal aims to digitalize various services provided by the hall that includes mess, canteen and various other services. Through this portal, you can book your mess extras, order your canteen food, request room cleaning, book various Hall facilities, and many more.

Broadly, the application will support the following:

* Students can pre-book extras in mess and order food in canteen.
* Students can book the hall's guest room, gym and sports courts online and also schedule cleaning services.
* Students can access their pending mess and canteen bills.
* Special permissions have been provided to the Hall Manager, Mess manager, Canteen Owner and the sports secretary to facilitate all these services.

## How to run the software locally?

* Make sure you have python and pip installed in your system
* Now run this command in terminal `pip install requirements.txt`

Give the following commands to start the backend server.

```
python manage.py collectstatic
```

```
python manage.py makemigrations
```

```
python manage.py migrate
```

```
python manage.py runserver
```

## Directory Hierarchy

```
|—— .gitignore
|—— Booking
|    |—— admin.py
|    |—— apps.py
|    |—— migrations
|        |—— __init__.py
|    |—— models.py
|    |—— templates
|        |—— booking_error.html
|        |—— Booking_manager.html
|        |—— courts.html
|        |—— guestroom.html
|        |—— secy_add_equipments.html
|        |—— secy_validate_request.html
|        |—— secy_validate_return.html
|        |—— sports_equipments.html
|    |—— tests.py
|    |—— urls.py
|    |—— views.py
|    |—— __init__.py
|—— Canteen
|    |—— admin.py
|    |—— apps.py
|    |—— migrations
|        |—— __init__.py
|    |—— models.py
|    |—— templates
|        |—— Owner_Modify_Menu.html
|        |—— Owner_New_Order.html
|        |—— Owner_Pending_Order.html
|        |—— Owner_Students_Bill.html
|        |—— Student_Cart.html
|        |—— Student_Orders_History.html
|        |—— Student_Pending_Order.html
|        |—— Student_Place_Order.html
|    |—— tests.py
|    |—— urls.py
|    |—— views.py
|    |—— __init__.py
|—— Cleaning
|    |—— admin.py
|    |—— apps.py
|    |—— migrations
|        |—— __init__.py
|    |—— models.py
|    |—— templates
|        |—— Cleaning_hall.html
|        |—— Lodge_Request.html
|        |—— Past_Request.html
|        |—— Pending_Request.html
|    |—— tests.py
|    |—— urls.py
|    |—— views.py
|    |—— __init__.py
|—— Home
|    |—— admin.py
|    |—— apps.py
|    |—— migrations
|        |—— __init__.py
|    |—— models.py
|    |—— static
|        |—— hall_image.jpg
|    |—— templates
|        |—— Home.html
|    |—— tests.py
|    |—— urls.py
|    |—— views.py
|    |—— __init__.py
|—— Login
|    |—— admin.py
|    |—— apps.py
|    |—— migrations
|        |—— __init__.py
|    |—— models.py
|    |—— static
|        |—— Login
|            |—— upha.png
|            |—— vector.png
|    |—— templates
|        |—— Login.html
|        |—— OTP.html
|        |—— Reset_Password.html
|        |—— Set_Password.html
|        |—— SignUp.html
|    |—— tests.py
|    |—— urls.py
|    |—— views.py
|    |—— __init__.py
|—— manage.py
|—— Mess
|    |—— admin.py
|    |—— apps.py
|    |—— migrations
|        |—— __init__.py
|    |—— models.py
|    |—— templates
|        |—— Manager_Extra_Items.html
|        |—— Manager_Modify_BDMR.html
|        |—— Manager_Modify_Menu.html
|        |—— Manager_Rebate_Requests.html
|        |—— Manager_Students_Pending_Bills.html
|        |—— Manager_View_Feedback.html
|        |—— Manager_View_Orders.html
|        |—— Student_Apply_For_Rebate.html
|        |—— Student_Booked_Extras.html
|        |—— Student_Book_Extras.html
|        |—— Student_Order_History.html
|        |—— Student_Regular_Menu.html
|    |—— tests.py
|    |—— urls.py
|    |—— views.py
|    |—— __init__.py
|—— My_Account
|    |—— admin.py
|    |—— apps.py
|    |—— migrations
|        |—— __init__.py
|    |—— models.py
|    |—— templates
|        |—— Canteen.html
|        |—— Mess.html
|    |—— tests.py
|    |—— urls.py
|    |—— views.py
|    |—— __init__.py
|—— templates
|    |—— error.html
|    |—— staff_base.html
|    |—— static
|        |—— booking__1__1.png
|        |—— football.png
|        |—— home_1.png
|        |—— hostel.png
|        |—— household_1.png
|        |—— logo_black_1.png
|        |—— main_display.png
|        |—— power_1.png
|        |—— rectangle_5.png
|        |—— staff_base.css
|        |—— student_base.css
|        |—— styles.css
|        |—— wallet_1.png
|    |—— student_base.html
|—— UPHA
|    |—— asgi.py
|    |—— settings.py
|    |—— urls.py
|    |—— wsgi.py
|    |—— __init__.py
```
