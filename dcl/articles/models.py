from django.db.models import (
    CharField,
    ImageField,
    Model,
    SlugField,
)


class Article(Model):
    title = CharField(max_length=255)
    slug = SlugField()
    image = ImageField(
        blank=True,
        upload_to='images'
    )
