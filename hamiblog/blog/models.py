from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField()

    class Meta:
        ordering = ("title",)
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return '/%s/' % self.slug

class Post(models.Model):
    ACTIVE = "active"
    DRAFT = "draft"

    CHOICES_STATUS = (
        (ACTIVE, "Active"),
        (DRAFT, "Draft"),
    )

    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name="posts"
    )
    title = models.CharField(max_length=255)
    slug = models.SlugField()
    intro = models.TextField()
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=10, choices=CHOICES_STATUS, default=DRAFT)
    image = models.ImageField(upload_to="uploads/", null=True, blank=True)

    class Meta:
        ordering = ("-created_at",)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return '/%s/%s/' % (self.category.slug ,self.slug)


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
    name = models.CharField(max_length=255)
    email = models.EmailField()
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name