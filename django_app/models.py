from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now
class Suggests(models.Model):
    author = models.CharField(max_length=300, verbose_name="Имя")
    title = models.CharField(max_length=300, verbose_name="Наименование")
    image = models.ImageField(verbose_name="Изображение", upload_to="images/products", default=None, null=True, blank=True)
    description = models.TextField(verbose_name="Описание")
    date = models.DateTimeField(auto_now_add=True, verbose_name="Дата")

    class Meta:
        """Вспомогательный класс"""

        app_label = "django_app"
        ordering = ("-date", "title")
        verbose_name = "Предложение"
        verbose_name_plural = "Предложения"

    def __str__(self):
        return self.title

class PostComments(models.Model):


    post = models.ForeignKey(to=Suggests, verbose_name="К какому посту", max_length=200, on_delete=models.CASCADE)
    author = models.ForeignKey(to=User, verbose_name="Автор", max_length=200, on_delete=models.CASCADE)  # +-
    text = models.TextField("Текст комментария", default="")
    date_time = models.DateTimeField("Дата и время создания", default=now)
    rating = models.IntegerField(default=0)

    class Meta:
        app_label = "django_app"
        ordering = ("-date_time", "post")
        verbose_name = "Комментарий к посту"
        verbose_name_plural = "Комментарии к постам"

    def __str__(self):
        return f"{self.date_time} {self.author.username} {self.post.title} {self.text[:20]}"



