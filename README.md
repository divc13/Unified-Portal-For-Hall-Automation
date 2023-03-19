Unified Portal For Hall Automation
==================================

The application was made as a course project of [CS253A](https://www.cse.iitk.ac.in/users/isaha/Courses/sdo22.shtml/): Software Development and Operations in spring 2022 under the guidance of [Dr. Indranil Saha](https://www.cse.iitk.ac.in/users/isaha/).

Unified Portal for Hall Automation is a merged platform designed for the residents of various halls at IITK to access day to day hall functionalities. This portal aims to digitalize various services provided by the hall that includes mess, canteen and various other services. Through this portal, you can book your mess extras, order your canteen food, request room cleaning, book various Hall facilities, and many more.

Broadly, the application will support the following:

* Students can pre-book extras in mess and order food in canteen.
* Students can access their pending mess and canteen bills

## Papar Information

- Title:  `paper name`
- Authors:  `A`,`B`,`C`
- Preprint: [https://arxiv.org/abs/xx]()
- Full-preprint: [paper position]()
- Video: [video position]()

## Install & Dependence

- python
- pytorch
- numpy

## Dataset Preparation

| Dataset   | Download  |
| --------- | --------- |
| dataset-A | [download]() |
| dataset-B | [download]() |
| dataset-C | [download]() |

## Use

- for train
  ```
  python train.py
  ```
- for test
  ```
  python test.py
  ```

## Pretrained model

| Model   | Download  |
| ------- | --------- |
| Model-1 | [download]() |
| Model-2 | [download]() |
| Model-3 | [download]() |

## Directory Hierarchy

```
|—— Booking
|    |—— admin.py
|    |—— apps.py
|    |—— migrations
|        |—— 0001_initial.py
|        |—— __init__.py
|        |—— __pycache__
|            |—— 0001_initial.cpython-310.pyc
|            |—— __init__.cpython-310.pyc
|    |—— models.py
|    |—— templates
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
|    |—— __pycache__
|        |—— admin.cpython-310.pyc
|        |—— apps.cpython-310.pyc
|        |—— models.cpython-310.pyc
|        |—— urls.cpython-310.pyc
|        |—— views.cpython-310.pyc
|        |—— __init__.cpython-310.pyc
|—— Canteen
|    |—— admin.py
|    |—— apps.py
|    |—— migrations
|        |—— 0001_initial.py
|        |—— __init__.py
|        |—— __pycache__
|            |—— 0001_initial.cpython-310.pyc
|            |—— __init__.cpython-310.pyc
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
|    |—— __pycache__
|        |—— admin.cpython-310.pyc
|        |—— apps.cpython-310.pyc
|        |—— models.cpython-310.pyc
|        |—— urls.cpython-310.pyc
|        |—— views.cpython-310.pyc
|        |—— __init__.cpython-310.pyc
|—— Cleaning
|    |—— admin.py
|    |—— apps.py
|    |—— migrations
|        |—— 0001_initial.py
|        |—— 0002_rename_username_cleaning_request_user_name.py
|        |—— __init__.py
|        |—— __pycache__
|            |—— 0001_initial.cpython-310.pyc
|            |—— 0002_rename_username_cleaning_request_user_name.cpython-310.pyc
|            |—— __init__.cpython-310.pyc
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
|    |—— __pycache__
|        |—— admin.cpython-310.pyc
|        |—— apps.cpython-310.pyc
|        |—— models.cpython-310.pyc
|        |—— urls.cpython-310.pyc
|        |—— views.cpython-310.pyc
|        |—— __init__.cpython-310.pyc
|—— db.sqlite3
|—— Home
|    |—— admin.py
|    |—— apps.py
|    |—— migrations
|        |—— __init__.py
|        |—— __pycache__
|            |—— __init__.cpython-310.pyc
|    |—— models.py
|    |—— static
|        |—— hall_image.jpg
|    |—— templates
|        |—— Home.html
|    |—— tests.py
|    |—— urls.py
|    |—— views.py
|    |—— __init__.py
|    |—— __pycache__
|        |—— admin.cpython-310.pyc
|        |—— apps.cpython-310.pyc
|        |—— models.cpython-310.pyc
|        |—— urls.cpython-310.pyc
|        |—— views.cpython-310.pyc
|        |—— __init__.cpython-310.pyc
|—— Login
|    |—— admin.py
|    |—— apps.py
|    |—— migrations
|        |—— 0001_initial.py
|        |—— 0002_alter_user_class_designation.py
|        |—— __init__.py
|        |—— __pycache__
|            |—— 0001_initial.cpython-310.pyc
|            |—— 0002_alter_user_class_designation.cpython-310.pyc
|            |—— __init__.cpython-310.pyc
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
|    |—— __pycache__
|        |—— admin.cpython-310.pyc
|        |—— apps.cpython-310.pyc
|        |—— models.cpython-310.pyc
|        |—— urls.cpython-310.pyc
|        |—— views.cpython-310.pyc
|        |—— __init__.cpython-310.pyc
|—— manage.py
|—— Mess
|    |—— admin.py
|    |—— apps.py
|    |—— migrations
|        |—— 0001_initial.py
|        |—— __init__.py
|        |—— __pycache__
|            |—— 0001_initial.cpython-310.pyc
|            |—— __init__.cpython-310.pyc
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
|    |—— __pycache__
|        |—— admin.cpython-310.pyc
|        |—— apps.cpython-310.pyc
|        |—— models.cpython-310.pyc
|        |—— urls.cpython-310.pyc
|        |—— views.cpython-310.pyc
|        |—— __init__.cpython-310.pyc
|—— My_Account
|    |—— admin.py
|    |—— apps.py
|    |—— migrations
|        |—— __init__.py
|        |—— __pycache__
|            |—— __init__.cpython-310.pyc
|    |—— models.py
|    |—— templates
|        |—— Canteen.html
|        |—— Mess.html
|    |—— tests.py
|    |—— urls.py
|    |—— views.py
|    |—— __init__.py
|    |—— __pycache__
|        |—— admin.cpython-310.pyc
|        |—— apps.cpython-310.pyc
|        |—— models.cpython-310.pyc
|        |—— urls.cpython-310.pyc
|        |—— views.cpython-310.pyc
|        |—— __init__.cpython-310.pyc
|—— static_files
|    |—— admin
|        |—— css
|            |—— autocomplete.css
|            |—— base.css
|            |—— changelists.css
|            |—— dark_mode.css
|            |—— dashboard.css
|            |—— fonts.css
|            |—— forms.css
|            |—— login.css
|            |—— nav_sidebar.css
|            |—— responsive.css
|            |—— responsive_rtl.css
|            |—— rtl.css
|            |—— vendor
|                |—— select2
|                    |—— LICENSE-SELECT2.md
|                    |—— select2.css
|                    |—— select2.min.css
|            |—— widgets.css
|        |—— fonts
|            |—— LICENSE.txt
|            |—— README.txt
|            |—— Roboto-Bold-webfont.woff
|            |—— Roboto-Light-webfont.woff
|            |—— Roboto-Regular-webfont.woff
|        |—— img
|            |—— calendar-icons.svg
|            |—— gis
|                |—— move_vertex_off.svg
|                |—— move_vertex_on.svg
|            |—— icon-addlink.svg
|            |—— icon-alert.svg
|            |—— icon-calendar.svg
|            |—— icon-changelink.svg
|            |—— icon-clock.svg
|            |—— icon-deletelink.svg
|            |—— icon-no.svg
|            |—— icon-unknown-alt.svg
|            |—— icon-unknown.svg
|            |—— icon-viewlink.svg
|            |—— icon-yes.svg
|            |—— inline-delete.svg
|            |—— LICENSE
|            |—— README.txt
|            |—— search.svg
|            |—— selector-icons.svg
|            |—— sorting-icons.svg
|            |—— tooltag-add.svg
|            |—— tooltag-arrowright.svg
|        |—— js
|            |—— actions.js
|            |—— admin
|                |—— DateTimeShortcuts.js
|                |—— RelatedObjectLookups.js
|            |—— autocomplete.js
|            |—— calendar.js
|            |—— cancel.js
|            |—— change_form.js
|            |—— collapse.js
|            |—— core.js
|            |—— filters.js
|            |—— inlines.js
|            |—— jquery.init.js
|            |—— nav_sidebar.js
|            |—— popup_response.js
|            |—— prepopulate.js
|            |—— prepopulate_init.js
|            |—— SelectBox.js
|            |—— SelectFilter2.js
|            |—— urlify.js
|            |—— vendor
|                |—— jquery
|                    |—— jquery.js
|                    |—— jquery.min.js
|                    |—— LICENSE.txt
|                |—— select2
|                    |—— i18n
|                        |—— af.js
|                        |—— ar.js
|                        |—— az.js
|                        |—— bg.js
|                        |—— bn.js
|                        |—— bs.js
|                        |—— ca.js
|                        |—— cs.js
|                        |—— da.js
|                        |—— de.js
|                        |—— dsb.js
|                        |—— el.js
|                        |—— en.js
|                        |—— es.js
|                        |—— et.js
|                        |—— eu.js
|                        |—— fa.js
|                        |—— fi.js
|                        |—— fr.js
|                        |—— gl.js
|                        |—— he.js
|                        |—— hi.js
|                        |—— hr.js
|                        |—— hsb.js
|                        |—— hu.js
|                        |—— hy.js
|                        |—— id.js
|                        |—— is.js
|                        |—— it.js
|                        |—— ja.js
|                        |—— ka.js
|                        |—— km.js
|                        |—— ko.js
|                        |—— lt.js
|                        |—— lv.js
|                        |—— mk.js
|                        |—— ms.js
|                        |—— nb.js
|                        |—— ne.js
|                        |—— nl.js
|                        |—— pl.js
|                        |—— ps.js
|                        |—— pt-BR.js
|                        |—— pt.js
|                        |—— ro.js
|                        |—— ru.js
|                        |—— sk.js
|                        |—— sl.js
|                        |—— sq.js
|                        |—— sr-Cyrl.js
|                        |—— sr.js
|                        |—— sv.js
|                        |—— th.js
|                        |—— tk.js
|                        |—— tr.js
|                        |—— uk.js
|                        |—— vi.js
|                        |—— zh-CN.js
|                        |—— zh-TW.js
|                    |—— LICENSE.md
|                    |—— select2.full.js
|                    |—— select2.full.min.js
|                |—— xregexp
|                    |—— LICENSE.txt
|                    |—— xregexp.js
|                    |—— xregexp.min.js
|    |—— booking__1__1.png
|    |—— football.png
|    |—— hall_image.jpg
|    |—— home_1.png
|    |—— hostel.png
|    |—— household_1.png
|    |—— Login
|        |—— upha.png
|        |—— vector.png
|    |—— logo_black_1.png
|    |—— main_display.png
|    |—— power_1.png
|    |—— rectangle_5.png
|    |—— staff_base.css
|    |—— student_base.css
|    |—— styles.css
|    |—— upha.png
|    |—— vector.png
|    |—— wallet_1.png
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
|    |—— __pycache__
|        |—— settings.cpython-310.pyc
|        |—— urls.cpython-310.pyc
|        |—— wsgi.cpython-310.pyc
|        |—— __init__.cpython-310.pyc
```

## Code Details

### Tested Platform

- software
  ```
  OS: Debian unstable (May 2021), Ubuntu LTS
  Python: 3.8.5 (anaconda)
  PyTorch: 1.7.1, 1.8.1
  ```
- hardware
  ```
  CPU: Intel Xeon 6226R
  GPU: Nvidia RTX3090 (24GB)
  ```

### Hyper parameters

```

```

## References

- [paper-1]()
- [paper-2]()
- [code-1](https://github.com)
- [code-2](https://github.com)

## License

## Citing

If you use xxx,please use the following BibTeX entry.

```

```
