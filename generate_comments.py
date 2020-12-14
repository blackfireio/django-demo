# This file can be run as following for testing:
# blackfire-python run ./manage.py shell < generate_comments.py
from bfdemo.models import Comment
from django.contrib.auth.models import User

u = User.objects.get(id=1)

new_comments = []
for i in range(2):
    new_comments.append(Comment(user=u, comment='Blackfire is cool!'))
Comment.objects.bulk_create(new_comments)

c = Comment(user=u, comment='a comment')
c.save()

cs = list(Comment.objects.all())

print(Comment.objects.count())
