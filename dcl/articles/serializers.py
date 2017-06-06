from easy_thumbnails.exceptions import InvalidImageFormatError
from easy_thumbnails.files import get_thumbnailer
from rest_framework.serializers import (
    CharField,
    SerializerMethodField,
    ModelSerializer,
    URLField,
)
from .models import Article


class ArticleDemoThumbSerializer(ModelSerializer):
    """
    Maps Article model to DemoThumb component
    """
    title = CharField(source='name')
    url = URLField(source='get_absolute_url')
    src = SerializerMethodField()

    def get_src(self, obj):
        """
        Get src returns url to image for src field
        """
        image_field = getattr(obj, self.Meta.thumbnail_source)
        if image_field:
            thumbnailer = get_thumbnailer(image_field)
            thumbnail_options = {
                'size': self.Meta.thumbnail_size
            }

            if (
                hasattr(self.Meta, 'thumbnail_crop') and
                self.Meta.thumbnail_crop
            ):
                thumbnail_options['crop'] = True

            try:
                return thumbnailer.get_thumbnail(thumbnail_options).url
            except InvalidImageFormatError:
                return ''
        else:
            return ''

    class Meta:
        model = Article
        fields = ('title', 'src', 'url', )
        thumbnail_size = (366, 236)
        thumbnail_crop = True
        thumbnail_source = 'image'
