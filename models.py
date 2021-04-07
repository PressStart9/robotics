from django.db import models


class Posts(models.Model):
    post_id = models.IntegerField()
    author_image = models.TextField()
    author_name = models.TextField()
    posting_date = models.DateTimeField()
    main_history = models.ForeignKey('self', blank=True, null=True, related_name='copy_history',
                                     on_delete=models.CASCADE)
    text = models.TextField(null=True)

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'
        ordering = ['-posting_date']


class Attachments(models.Model):
    atach_id = models.IntegerField()
    connect_post = models.ForeignKey(Posts, null=True, related_name='atachs', on_delete=models.CASCADE)
    type = models.TextField()
    preview = models.TextField(blank=True)
    url = models.TextField()
    width = models.IntegerField(blank=True, null=True)
    height = models.IntegerField(blank=True, null=True)

