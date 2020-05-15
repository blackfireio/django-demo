from bfdemo.models import Comment
from django.contrib.auth.models import User

u = User.objects.get(id=1)
print(u)

for c in Comment.objects.all():
    c.delete()

print(Comment.objects.count())

new_comments = []
for i in range(100):
    new_comments.append(Comment(user=u, comment='Oh! That is awesome!'))
Comment.objects.bulk_create(new_comments)

print(Comment.objects.count())
