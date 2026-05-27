from django.core.paginator import Paginator
def lista_produtos(request):
    busca = request.GET.get('busca')

    produtos = Produto.objects.all()

    if busca:
        produtos = produtos.filter(nome__icontains=busca)

    paginator = Paginator(produtos, 5)

    page = request.GET.get('page')
    produtos = paginator.get_page(page)

    return render(request, 'lista.html', {'produtos': produtos})