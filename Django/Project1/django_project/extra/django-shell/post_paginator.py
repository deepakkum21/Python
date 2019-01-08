# python manage.py shell
from django.core.paginator import Paginator
posts = ['post1','post2','post3','post4','post5','post6','post7']
post_paginator = Paginator(posts, 3) # (paginatorobject, no of pages)
post_paginator.num_pages
# output -> 3

for page in post_paginator.page_range:
    print(page)
# 1
# 2
# 3

# to get total no of item is all pages
# paginatorobj.count
post_paginator.count
# 7

# to get the particular page
p1 = post_paginator.page(1)
p1
# <Page 1 of 3>

# to know currently which page no it is reffering
p1.number
# 1

# to get the list of objects that current page is having
p1.object_list
# ['post1', 'post2', 'post3']

# to know wheather it has the previous page or not
p1.has_previous()
# False

# to know wheather it has the next page or not
p1.has_next()
# True

# to know the page no of next page
p1.next_page_number()
# 2