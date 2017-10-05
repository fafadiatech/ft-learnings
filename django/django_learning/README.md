# List of useful Django Application

## django-taggit

``` python
>>> from blog.models import Blog
>>> post = Blog()
>>> post.title = "Test Post"
>>> post.blurb = "Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."
>>> post.save()
>>> post.tags.add("django", "sample")
>>> post.save()
>>>
>>> for item in Blog.objects.all():
...    print item.title, item.tags.all()
...
Test Post <QuerySet [<Tag: sample>, <Tag: django>]>
```
