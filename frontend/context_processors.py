from frontend.models import Post,Category

def get_categories(request):
    categories=Category.objects.all()
    return {"categories":categories}

