from .models import Category

def category_renderer(request):

    return {'menu': Category.objects.all() }
