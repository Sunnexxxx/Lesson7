from django.db import models
from django.utils.text import slugify


class Ticket(models.Model):
    ticket_id = models.PositiveIntegerField(default=1111)

    def __str__(self):
        return f"{self.id} - {self.ticket_id}"


GENRE_CHOICES = (
    (1, "Фентези"),
    (2, "Фантастика"),
    (3, "Детектив")
)


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


class Book(models.Model):
    title = models.CharField(max_length=255)
    genre = models.IntegerField(null=True,
                                choices=GENRE_CHOICES)
    pages = models.PositiveIntegerField()
    author = models.ForeignKey(Author,
                               on_delete=models.CASCADE,
                               null=True)
    slug = models.SlugField(max_length=255,
                            null=True,
                            unique=True,
                            blank=True)

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        if not self.slug:
            self.slug = slugify(f"{self.title}-{self.pages}-{self.author.first_name}")
        super().save(force_insert, force_update, using, update_fields)

    class Meta:
        # db_table = ""
        ordering = ['title']

    def __str__(self):
        return f"{self.title} - {self.pages}"

    def get_absolute_url(self):
        return f"book_list/{self.slug}"


class Reader(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    ticket = models.OneToOneField(Ticket,
                                  on_delete=models.CASCADE)
    liked_books = models.ManyToManyField(Book)

    def __str__(self):
        return f"{self.first_name} - {self.last_name}"


class TestTable(models.Model):
    second_id = models.IntegerField()

    def __str__(self):
        return f"{self.id} - {self.second_id}"