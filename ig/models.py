from django.db import models as m

from django.contrib.auth.models import User

from uuid import uuid4 as u4

class Profile(m.Model):

    user = m.OneToOneField(User, on_delete = m.CASCADE)

    name = m.CharField(max_length = 333)

    avatar = m.ImageField(upload_to = 'uploads/avatar')

    def __str__(self):

        return self.name

class Post(m.Model):

    uid = m.UUIDField(default = u4)

    user = m.ForeignKey(User, on_delete = m.CASCADE)

    caption = m.TextField()

    photo = m.ImageField(upload_to = 'uploads/posts')

    created_at = m.DateTimeField(auto_now_add = True)
    updated_at = m.DateTimeField(auto_now = True)

    def __str__(self):

        if self.caption:

            return self.caption
        
        else: 

            return 'Unnamed'