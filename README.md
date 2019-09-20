<h2> Queue it Up </h2>
Spotipy/Django Web Application Game

<h3>Create virtual environment and install django</h3>

In desired directory run (This only needs to be done the first time)

<I>python -m venv venv</I>
 
Activate Virutal Environment (You'll need to do this every time you reopen cmd)
 
<I>C:\> venv\Scripts\activate.bat</I>

Install Django

<I>(venv) $ pip install Django</I>

Useful Django tutorial for additional help https://realpython.com/get-started-with-django-1/


<h3>Additional libraries needed</h3>

install spotipy

<I>pip install spotipy</I>

<I>pip install git+https://github.com/plamere/spotipy.git --upgrade</I>

add util_custom to \Lib\site-packages\spotipy

add value of client secret to client secret variable at the top of party/views.py

Note: client secret has been removed from github to abide by Spotify's terms and conditions


<h3>To Create Access to other Devices from Your IP Address</h3>

edit party/view and change my_IP and my_PORT at the top of the page

edit queue_it_up/settings and add IP address to ALLOWED_HOSTS

From cmd line run

<I>python manage.py runserver 0.0.0.0:value of my_PORT</I>


<h3>Add More Categories</h3>

Open the Python Shell by Entering:

<I>python manage.py shell</I>

Paste the Following code with new Categories in the cat list

<I>from party.Models import Library

cats = ["new cat1", "new cat2"]

for x in cats:
    l = Library(name = x)
    l.save()</I>




