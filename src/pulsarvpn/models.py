from django.db import models


class SecretKeys(models.Model):
    key = models.CharField(
    max_length=1500,
    blank= False,
    verbose_name=u"Client Key"
    )




    def __unicode__(self):
        return self.key
