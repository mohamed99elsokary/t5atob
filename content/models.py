from django.db import models
from leactures import models as leactures_models

# Create your models here.
class Content(models.Model):
    # relations
    lecture = models.ForeignKey(leactures_models.Lecture, on_delete=models.CASCADE)
    # fields
    index = models.IntegerField()
    text = models.TextField()
    video_url = models.URLField(max_length=200, null=True, blank=True, default=None)
    image_url = models.ImageField(
        upload_to="media/", null=True, blank=True, default=None
    )

    def __str__(self):
        return f"{self.lecture.name} {self.lecture.category.name}"
