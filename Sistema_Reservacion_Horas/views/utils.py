from django.core.paginator import Paginator

def paginar_objetos(request, queryset, num_por_pagina=4):
    """
    Función auxiliar para paginar objetos.
    :param request: El request actual
    :param queryset: El conjunto de objetos a paginar
    :param num_por_pagina: Número de objetos por página
    :return: Un objeto de paginación (page_obj)
    """
    paginator = Paginator(queryset, num_por_pagina)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return page_obj
