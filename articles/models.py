from django.db import models


class Article(models.Model):
    title = models.CharField(max_length=300, blank=False, null=False)
    description = models.TextField(blank=False, null=False)
    cover = models.ImageField(upload_to='articles_covers', blank=False, null=False)
    date = models.DateField(blank=True, null=True)
    article = models.TextField(blank=False, null=False)
    ARTICLE_TYPES = [
        ('Akt I', 'Akt I'),
        ('Akt II', 'Akt II'),
        ('Akt III', 'Akt III'),
        ('Inne', 'Inne')
    ]
    act = models.CharField(max_length=10, choices=ARTICLE_TYPES, blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True, editable=False, null=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False, null=True)

    def __str__(self):
        return self.title
