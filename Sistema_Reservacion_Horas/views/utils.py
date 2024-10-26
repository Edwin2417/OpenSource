from django.core.paginator import Paginator

def paginar_objetos(request, objetos, cantidad_por_pagina):
    paginator = Paginator(objetos, cantidad_por_pagina)
    page_number = request.GET.get('page')
    return paginator.get_page(page_number)
