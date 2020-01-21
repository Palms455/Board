from django.views.generic.edit import CreateView

class ArticleFormView(CreateView):
    form_class = ArticleForm
    template_name = 'Upload.html'

    # You can skip this method if you change "ArtileForm" to "form"
    # in your template.
    def get_context_data(self, **kwargs):
        cd = super(ArticleFormView, self).get_context_data(**kwargs)
        cd['ArtileForm'] = cd['form']
        return cd
compose_article = ArticleFormView.as_view()