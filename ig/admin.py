from django.contrib import admin as a

from .models import *

a.site.register(Profile)
a.site.register(Post)