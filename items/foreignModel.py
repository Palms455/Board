class Article(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField(max_length = 5000)
    author = models.ForeignKey('Author', on_delete=models.CASCADE)

class Author(models.Model):
    author_name = models.CharField(max_length=200)
    author_intro = models.TextField(max_length = 3000)