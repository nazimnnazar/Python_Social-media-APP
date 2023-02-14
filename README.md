# Python_Social-media-APP


A social media web-application with Python Django .
## Installation

```bash
    $ python -m venv venv
    $ source venv/Scripts/activate
    (venv) pip install -r requirements.txt
    (venv) cd Django_Social_Network_App
    (venv) python manage.py makemigrations
    (venv) python manage.py migrate
    (venv) python manage.py createsuperuser
    (venv) python manage.py runserver
```
## Features :
<li>Create, Edit, Delete Posts with customized text, pictures and links</li>
<li>Like, Comment / Reply, Save and Search posts</li>
<li>Follow and Unfollow users to view their posts</li>
<li>Sign Up, Login, OAuth 2.0(Google, Github), Logout, Forgot Password</li>
<li>Public Profile view</li>
<li>Friend Request</li>
<li>Notifications</li>
<li>Chats using websockets</li>
<li>Video Calls</li>






## Add django-allauth config

https://django-allauth.readthedocs.io/en/latest/installation.html#post-installation

## Others

- To use other DB edit this https://github.com/Ronik22/Django_Social_Network_App/blob/main/myproject/settings.py#L107
- To use other providers edit this https://github.com/Ronik22/Django_Social_Network_App/blob/main/myproject/settings.py#L205
- To use redis instead edit this https://github.com/Ronik22/Django_Social_Network_App/blob/main/myproject/settings.py#L197

