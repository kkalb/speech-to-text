from django.views.generic.edit import CreateView
from django.views.generic.edit import DeleteView
from django.views.generic.edit import UpdateView
from django.views.generic.list import ListView

from speech_to_text.main.models import Text


class TextCreateView(CreateView):
    model = Text
    fields = ["data"]


text_create_view = TextCreateView.as_view()


class TextUpdateView(UpdateView):
    model = Text
    fields = ["data"]


text_update_view = TextUpdateView.as_view()


class TextDeleteView(DeleteView):
    model = Text

    def get_success_url(self) -> str:
        return "/text"


text_delete_view = TextDeleteView.as_view()


class TextListView(ListView):
    model = Text
    paginate_by = 5

    def get_queryset(self, *args, **kwargs):
        qs = super().get_queryset(*args, **kwargs)
        return qs.order_by("-id")


text_list_view = TextListView.as_view()
