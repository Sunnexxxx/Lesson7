from django.db import models


GENRE_CHOICES = (
    (1, "Фентези"),
    (2, "Фантастика"),
    (3, "Детектив")
)


class Book(models.Model):
    title = models.CharField(max_length=255)
    genre = models.IntegerField(null=True,
                                choices=GENRE_CHOICES)
    pages = models.PositiveIntegerField()

    class Meta:
        # db_table = ""
        ordering = ['title']

    def __str__(self):
        return f"{self.title} - {self.pages}"


class Author(models.Model):
    first_name = models.CharField(max_length=255,
                                  null=True,
                                  blank=True,
                                  )
    last_name = models.CharField(max_length=255)
    age = models.PositiveIntegerField(default=60,
                                      unique=True)

    class Meta:
        # db_table = ""
        # app_label = 'library'
        verbose_name = 'Автор'
        verbose_name_plural = 'Авторы'
        ordering = ['first_name']
        unique_together = ('first_name', 'last_name', 'age')

    def __str__(self):
        return f"{self.first_name} - {self.last_name} - {self.age}"


class TestTable(models.Model):
    second_id = models.IntegerField()

    def __str__(self):
        return f"{self.id} - {self.second_id}"