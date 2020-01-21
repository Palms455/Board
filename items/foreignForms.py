class ArticleForm(forms.ModelForm):
    author = forms.CharField()

    class Meta:
        model = Article
        fields = ['title', 'author', 'content']
        widgets = {
            'content': forms.Textarea(attrs={'cols': 75, 'rows': 50}),
        }

    def save(self, commit=True):
        author, created = Author.objects.get_or_create(
            author_name=self.cleaned_data['author'],
            defaults={'author_intro': ''}
        )
        self.cleaned_data['author'] = author.id
        return super(ArticleForm, self).save(commit)