from django.db import models


class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    # When working with images, you have to install the python
    # pillow package.
    image = models.ImageField(upload_to='portfolio/images/')
    # blank means default to false ? As in it can be false
    # What this means is that it isn't required ?
    url = models.URLField(blank=True)

    def __str__(self):
        return self.title
