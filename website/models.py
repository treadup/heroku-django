import os
from django.db import models

class StoredFile(models.Model):
    file = models.FileField(upload_to="files")

    def filename(self):
        return os.path.basename(self.file.name)

    def path(self):
        return self.file.path

    def url(self):
        return self.file.url

    def __str__(self):
        if self.file:
            return self.file.name
        return f"StoredFile ({self.pk})"
