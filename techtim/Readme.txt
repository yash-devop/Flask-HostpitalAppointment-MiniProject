1)base.html :
 Our Project Register.html or the html whose data has to be Changed.
  Means our website FORMS are gonna stored in base html

2)create an Index.html:

In this , we have to make changes using Jinja code   {% block title/content %}{{data from app.py}}{% endblock %}

3) Base.html works using Index.html
means same jinja code we have to apply in index.html


G:\ProgramData\MySQL\MySQL Server 8.0\Data



create table users( Name varchar(50), Gender varchar(8), AadharNumber varchar(20) PRIMARY KEY, Address varchar(500), PhoneNumber integer(15), Pincode varchar(7), Fever varchar(5), LossOfSmellandTaste varchar(5), Other varchar(100), MedicalHistory varchar(200), AppointmentDate varchar(50))  


Name, Gender, AadharNumber, Address, PhoneNumber, Pincode, Fever, LossOfSmellandTaste, Other, MedicalHistory, AppointmentDate