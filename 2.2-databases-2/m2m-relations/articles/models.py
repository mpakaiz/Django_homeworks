from django.db import models


class Article(models.Model):

    title = models.CharField(max_length=256, verbose_name='Название')
    text = models.TextField(verbose_name='Текст')
    published_at = models.DateTimeField(verbose_name='Дата публикации')
    image = models.ImageField(null=True, blank=True, verbose_name='Изображение',)
    tag = models.ManyToManyField('Tag', through='Scope')
    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'
        ordering = ['-published_at']

    def __str__(self):
        return self.title

class Section(models.Model):

    name = models.CharField(max_length=256, verbose_name='Раздел')
    article = models.ManyToManyField(Article, through='Relationship')

    def __str__(self):
        return self.name


class Relationship(models.Model):

    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='positions')
    Section = models.ForeignKey(Section, on_delete=models.CASCADE, related_name='positions')
    main = models.BooleanField(null=True)

class Tag(models.Model):

    name = models.CharField(max_length=50, verbose_name='Tag')

    def __str__(self):
        return self.name

class Scope(models.Model):

    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='scopes')
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE, related_name='scopes')
    is_main = models.BooleanField()
