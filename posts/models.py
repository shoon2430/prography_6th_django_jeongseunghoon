from django.db import models
from core import models as core_model


class Comment(core_model.Core):

    user = models.ForeignKey("users.User", on_delete=models.CASCADE)
    post = models.ForeignKey("Post", related_name="comments", on_delete=models.CASCADE)
    contents = models.TextField(blank=False)
    visibility = models.BooleanField(default="N")

    class Meta:
        ordering = ("created",)

    def __str__(self):
        return str(f"{self.post.title}_{self.pk}")


class Post(core_model.Core):

    CATEGORY_NOTICE = "notice"
    CATEGORY_DAILYLIFE = "dailylife"
    CATEGORY_COMMUNITY = "community"
    CATEGORY_QnA = "qa"

    CATEGORY_LIST = (
        (CATEGORY_NOTICE, "Notice"),
        (CATEGORY_DAILYLIFE, "Dailylife"),
        (CATEGORY_COMMUNITY, "Community"),
        (CATEGORY_QnA, "Q&A"),
    )

    category = models.CharField(
        choices=CATEGORY_LIST, default=CATEGORY_COMMUNITY, max_length=10
    )
    title = models.CharField(max_length=300, blank=True, null=True)
    writer = models.ForeignKey(
        "users.User", related_name="posts", on_delete=models.CASCADE
    )
    description = models.TextField(blank=True, null=True)

    class Meta:
        ordering = ("created",)

    def __str__(self):
        return str(self.pk)

    def get_comment_count(self):
        comments = Comment.objects.filter(post=self)
        return comments.count()
