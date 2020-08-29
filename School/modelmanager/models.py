from django.db import models


class DocumentQuerySet(models.QuerySet):
    def pdfs(self):
        return self.filter(file_type='pdf')

    def smaller_than(self, size):
        return self.filter(size=size)

    def greter_than(self, size):
        return self.filter(size=size)


class DocumentManager(models.Manager):
    def get_queryset(self):
        return DocumentQuerySet(self.model, using=self._db)  # Important!

    def pdfs(self):
        return self.get_queryset().pdfs()

    def smaller_than(self, size):
        return self.get_queryset().smaller_than(size)

    def greter_than(self, size):
        return self.get_queryset().greter_than(size)


class Document(models.Model):
    name = models.CharField(max_length=30)
    size = models.PositiveIntegerField(default=0)
    file_type = models.CharField(max_length=10, blank=True)
    objects = DocumentManager()
