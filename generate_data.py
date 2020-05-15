from bfdemo.models import Comment
from django.contrib.auth.models import User

u = User.objects.get(id=1)
print(u)

new_comments = [Comment(user=u, comment='Oh! That is awesome!') for i in range(1000)]
Comment.objects.bulk_create(new_comments)
