from django.db import models
from core import models as core_models


class Video(core_models.TimeStamppedModel):

    video_content = models.FileField(upload_to="video_content")
    thumbnail = models.Imagefield(upload_to="video_thumbnail")
    title = models.CharField(max_length="128")
    caption = models.TextField(null=True, blank=True)
    is_like_or_hate = models.BooleanField(default=True)
    is_varified = models.BooleanField(default=False)
