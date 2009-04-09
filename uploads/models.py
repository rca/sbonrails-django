import hashlib
import time

from django.contrib.auth.models import User
from django.db import models

class File(models.Model):
    user = models.ForeignKey(User)
    name = models.CharField(max_length=50)
    file = models.FileField(upload_to='uploads/%Y/%m/%d')
    download_key = models.CharField(max_length=40, blank=True, unique=True,
                                    help_text='leave blank for autofill')

    def __unicode__(self):
        return self.name

    def save(self):
        """
        Set the download key if not given before saving
        """

        if not self.download_key:
            sha1 = hashlib.sha1('%s:%s:%s' % \
                                    (self.user.id, self.name, time.time()))
            self.download_key = sha1.hexdigest()

        super(File, self).save()
