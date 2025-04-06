from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=100, verbose_name="Имя") #first_name VARCHAR(100)
    surname = models.CharField(max_length=100, verbose_name="Фамилия")
    birth_date = models.DateField(verbose_name="Дата рождения")
    profile = models.URLField(
        max_length=255,
        null=True,
        blank=True,
        verbose_name="Ссылка на соц.сети")
    is_deleted = models.BooleanField(
        default=False,
        verbose_name="Удален",
        help_text="если True- автор удален, если False-не удален")
    rating = models.FloatField(
        validators=[
            MinValueValidator(1),
            MaxValueValidator(10)
        ],
        default=0.0, verbose_name="Рейтинг"
    )
    deleted_at = models.DateTimeField(
        null=True,
        blank=True,
        verbose_name="Дата удаления автора")

    def __str__(self):
        return self.name

class Publisher(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=255, null=True)
    city = models.CharField(max_length=100, null=True)
    country = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Book(models.Model):
    GENRE_CHOICES = [
        ('Fiction','Fiction'),
        ('Non-Fiction','Non-Fiction'),
        ('Science Fiction','Science Fiction'),
        ('Fantasy','Fantasy'),
        ('Mystery','Mystery'),
        ('Biography','Biography'),

    ]
    title = models.CharField(max_length=120)
    author = models.ForeignKey(Author, on_delete=models.PROTECT)
    genre = models.CharField(max_length=50, choices=GENRE_CHOICES, default='Non-Fiction')
    description = models.TextField(null=True, blank=True)
    count_pages = models.PositiveSmallIntegerField( # 32000 symbols
        validators=[
            MinValueValidator(1),
            MaxValueValidator(10000)
        ],
        null=True,
        blank=True)
    public_date = models.DateField()
    publisher = models.ForeignKey(Publisher, on_delete=models.PROTECT, null=True)

    def __str__(self):
        return self.title



