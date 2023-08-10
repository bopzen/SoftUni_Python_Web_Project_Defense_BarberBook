# SoftUni_Python_Web_Project_Defense_BarberBook

This is my project for SoftUni Python Web Frameworks Module.

The project is deployed in PythonAnywhere and you can access it from the following link:
http://barberbook.pythonanywhere.com/


# **Barberbook**

**Barberbook is a web application developed with Django. The main purpose of the application is to allow clients to book barbershop appointments 
online and also barbershops to be able to manage their appointments.**

## Short Functionality Description:

The app has 2 types of users: **Client** and **Barbershop**. Each user is extended to its respective ClientProfile or BarbershopProfile depending on the User Role field.

- Client Profile can register, login, logout, delete profile, change password, edit their details, add profile picture, manage their reservations, write a review for barbershops that they have visited.
- Barbershop Profile can register, login, logout, delete profile, change password, edit their details, services, barbers, working hours, add profile picture and barbershop photos, manage their reservations.
- Barbershops can be searched via search field, via list of barbershops and via map
- Reservation process is based on 6 steps where the client chooses the barbershop, the barber, the service, the date and the time based on the availability and confirms the reservation.
- The application also has a responsive design for mobile version


## Short Tech Description:

### Models (total 10):
- AppUser
- ClientProfile
- BarbershopProfile
- ServiceCategory
- BarbershopService
- BarbershopWorkingHours
- BarbershopPicture
- Barber
- Reservation
- Review

DB Schema for the models excluding the build-in Django models:
![db-schema.png](site-images%2Fdb-schema.png)

### Views (total 42):
- Most of the views are Class Based Views and some of the views are Function Based Views

### Templates (total 44):
- Django Template Language is used with some additional help of Bootstrap, Javascript, jQuery and LeafLetMap library for the dynamic parts

### API:
- Very simple public API showing all reservations made on the website

### **The project is developed using the following technologies:**
- **For Back-end:** Python, Django Framework
- **For Front-end:** Custom HTML, CSS and additional components built with Bootstrap, Javascript, jQuery, LeafLet Maps Library
- **For Database:** PostgreSQL
- **For API:** Django REST Framework

[![My Skills](https://skillicons.dev/icons?i=py,django,js,html,css,bootstrap,jquery,postgres)](https://skillicons.dev)

### **Screenshots of the web application:**
- Home Page
![home-page.png](site-images%2Fhome-page.png)


- Register Page
![register-page.png](site-images%2Fregister-page.png)


- Login Page
![login-page.png](site-images%2Flogin-page.png)


- Client Profile Page
![client-profile.png](site-images%2Fclient-profile.png)


- Client Reservations List Page
![client-reservations-list.png](site-images%2Fclient-reservations-list.png)


- Client Reviews List Page
![client-reviews-list.png](site-images%2Fclient-reviews-list.png)


- Barbershop Profile Page
![barbershop-profile.png](site-images%2Fbarbershop-profile.png)


- Barbershop Reservations List Page
![barbershop-reservations-list.png](site-images%2Fbarbershop-reservations-list.png)


- Barbershops List Page
![barbershops-list.png](site-images%2Fbarbershops-list.png)


- Barbershops Map Page
![barbershops-map.png](site-images%2Fbarbershops-map.png)


- Barbershop Search Page
![search-page.png](site-images%2Fsearch-page.png)


- Admin Page
![admin-page.png](site-images%2Fadmin-page.png)


- API Page
![REST-API.png](site-images%2FREST-API.png)

- Export to Excel

![export-to-excel.png](site-images%2Fexport-to-excel.png)

Mobile version: 

- Mobile Home Page

![mobile-home-page.png](site-images%2Fmobile-home-page.png)


- Mobile Reservation List Page

![mobile-reservation-list.png](site-images%2Fmobile-reservation-list.png)


- Mobile Map Page

![mobile-map-page.png](site-images%2Fmobile-map-page.png)
