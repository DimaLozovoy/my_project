from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from services.products_module.models import Product

from django.template.defaulttags import register


@register.filter
def get_range(value):
    return range(1, value + 1)


def index(request):
    if not request.user.is_authenticated():
        return redirect('auth')

    product = Product.objects.all()
    paginator = Paginator(products, 1)ц

    products = Product.objects.all()
    paginator = Paginator(products, 10)

    page_number = request.GET.get('page',  1)
    page_obj = paginator.get_page(page_number)
    context = {'products': page_obj ,'pages_count': paginator.num_pages, 'page_number': page_number}
    return render(request, 'index.html', context)