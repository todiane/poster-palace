from django.db import models


class About(models.Model):
    title = models.CharField(max_length=200)
    subtitle = models.CharField(max_length=500, null=True, blank=True)
    image = models.ImageField()
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField()

    class Meta:
        verbose_name = "About Poster Palace"
        verbose_name_plural = "About Poster Palace"

    def __str__(self):
        return self.title
