from bfdemo.models import Comment
from django.contrib.auth.models import User

u = User.objects.get(id=1)
print(u)

Comment.objects.all().delete()

print(Comment.objects.count())

new_comments = []
for i in range(500):
    new_comments.append(Comment(user=u, comment='Oh! That is awesome!'))
    if (i % 100) == 0:
        print(i)
Comment.objects.bulk_create(new_comments)

print(Comment.objects.count())
