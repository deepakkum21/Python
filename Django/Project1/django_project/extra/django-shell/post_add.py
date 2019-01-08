# python manage.py shell
import json
from blog.models import Post
with open('Posts.json') as json_file:
    posts_json = json.load(json_file)

for post in posts_json:
    post = Post(title=post['title'], content=post['content'],author_id=post['user_id'])
    post.save()

exit()