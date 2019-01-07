## profile-user
PS C:\Users\deepak\Desktop\Git\python repo\Python\Django\Project1\django_project> python manage.py shell
Python 3.7.2 (tags/v3.7.2:9a3ffc0492, Dec 23 2018, 22:20:52) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license" for more information.
(InteractiveConsole)
>>> from django.contrib.auth.models import User
>>> user = User.objects.filter(username='deepak')
>>> user = User.objects.filter(username='deepak').first()
>>> user
<User: deepak>
>>> user.profile
<Profile: deepak Profile>
>>> user.profile.image
<ImageFieldFile: profile_pics/P_20160819_153359_BF.jpg>
>>> user.profile.image.size
963905
>>> user.profile.image.width
C:\Users\deepak\AppData\Local\Programs\Python\Python37-32\lib\site-packages\PIL\TiffImagePlugin.py:763: UserWarning: Possibly corrupt EXIF data.  Expecting to read 10926 bytes but only got 339. Skipping tag 37500
  " Skipping tag %s" % (size, len(data), tag))
C:\Users\deepak\AppData\Local\Programs\Python\Python37-32\lib\site-packages\PIL\TiffImagePlugin.py:763: UserWarning: Possibly corrupt EXIF data.  Expecting to read 8 bytes but only got 0. Skipping tag 33434
  " Skipping tag %s" % (size, len(data), tag))
C:\Users\deepak\AppData\Local\Programs\Python\Python37-32\lib\site-packages\PIL\TiffImagePlugin.py:780: UserWarning: Corrupt EXIF data.  Expecting to
read 2 bytes but only got 0.
  warnings.warn(str(msg))
C:\Users\deepak\AppData\Local\Programs\Python\Python37-32\lib\site-packages\PIL\TiffImagePlugin.py:763: UserWarning: Possibly corrupt EXIF data.  Expecting to read 10926 bytes but only got 2387. Skipping tag 37500
  " Skipping tag %s" % (size, len(data), tag))
C:\Users\deepak\AppData\Local\Programs\Python\Python37-32\lib\site-packages\PIL\TiffImagePlugin.py:763: UserWarning: Possibly corrupt EXIF data.  Expecting to read 10926 bytes but only got 6483. Skipping tag 37500
  " Skipping tag %s" % (size, len(data), tag))
2592
>>> user.profile.image.url
'profile_pics/P_20160819_153359_BF.jpg'
>>> user = User.objects.filter(username='newUser').first()
>>> user
<User: newUser>
>>> user.profile.image
<ImageFieldFile: default.jpg>