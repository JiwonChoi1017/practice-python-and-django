from typing import Any, Dict
from django.http import HttpResponseRedirect
from django.views import View
from django.views.generic.base import TemplateView
from django.views.generic import ListView, DetailView

"""
CreateView:
    クラスベースビューの一つで、データの登録や作成をするときに使われるもの。
    FormViewはデータ保存に限らず、フォームに入力したデータを自由に処理できるので自由度は高いが、
    データ保存に関して言えば、CreateViewより多くの記述が必要になるので
    もしフォーム作成の目的がデータ保存であれば、CreateViewを使った方が便利。
"""
from django.views.generic.edit import CreateView

from .forms import ReviewForm
from .models import Review

# Create your views here.


class ReviewView(CreateView):
    model = Review
    form_class = ReviewForm
    template_name = "reviews/review.html"
    success_url = "/thank-you"


class ThankYouView(TemplateView):
    template_name = "reviews/thank_you.html"

    def get_context_data(self, **kwargs: Any):
        context = super().get_context_data(**kwargs)
        context["message"] = "This works!"

        return context


class ReviewListView(ListView):
    template_name = "reviews/review_list.html"
    model = Review
    context_object_name = "reviews"

    # def get_queryset(self) -> QuerySet[Any]:
    #     data = super().get_queryset().filter(rating__gt=4)

    #     return data


class SingleReviewView(DetailView):
    template_name = "reviews/single_review.html"
    model = Review

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        loaded_review = self.object
        request = self.request
        favorite_id = request.session.get("favorite_review")
        context["is_favorite"] = favorite_id == str(loaded_review.id)

        return context


class AddFavoriteView(View):
    def post(self, request):
        review_id = request.POST["review_id"]
        request.session["favorite_review"] = review_id
        return HttpResponseRedirect("/reviews/" + review_id)
