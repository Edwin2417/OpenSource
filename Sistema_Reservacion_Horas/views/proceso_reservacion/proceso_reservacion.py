from django.shortcuts import render, get_object_or_404, redirect
from Sistema_Reservacion_Horas.models.aulas_model import ProcesoReservacionHoras, AulasLaboratorios, Estado
from Sistema_Reservacion_Horas.forms.proceso_reservacion_forms import ProcesoReservacionHorasForm
from django.http import HttpResponseForbidden

def admin_required(view_func):
    def wrapper(request, *args, **kwargs):
        tipo_usuario = request.session.get('tipo_usuario')
        if tipo_usuario != 'Administrador':
            return HttpResponseForbidden("No tienes permiso para acceder a esta sección.")
        return view_func(request, *args, **kwargs)
    return wrapper

# Vista para listar las reservaciones de horas
# Vista para listar las reservaciones de horas
def listar_reservaciones(request):
    usuario_id = request.session.get('usuario_id')
    tipo_usuario = request.session.get('tipo_usuario')

    # Verifica si el usuario es administrador
    if tipo_usuario == 'Administrador':
        query = request.GET.get('q', '')  # Para búsquedas
        if query:
            reservaciones = ProcesoReservacionHoras.objects.filter(empleado__nombre__icontains=query)  # Filtra por nombre de empleado
        else:
            reservaciones = ProcesoReservacionHoras.objects.all()  # Muestra todas las reservaciones si no hay búsqueda
    else:
        # Si no es administrador, filtra por el usuario que está logueado
        query = request.GET.get('q', '')  # Para búsquedas
        if query:
            reservaciones = ProcesoReservacionHoras.objects.filter(usuario__identificador=usuario_id, empleado__nombre__icontains=query)  # Filtra por nombre de empleado y usuario logueado
        else:
            reservaciones = ProcesoReservacionHoras.objects.filter(usuario__identificador=usuario_id)  # Muestra solo las reservaciones del usuario logueado

    return render(request, 'reservaciones/listar_reservaciones.html', {'reservaciones': reservaciones})


# Vista para agregar una nueva reservación de horas
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from Sistema_Reservacion_Horas.models.aulas_model import ProcesoReservacionHoras, AulasLaboratorios


# Vista para agregar una nueva reservación de horas
# Vista para agregar una nueva reservación de horas
from Sistema_Reservacion_Horas.models.aulas_model import ProcesoReservacionHoras, AulasLaboratorios, Estado


# Vista para agregar una nueva reservación de horas
def agregar_reservacion(request):
    if request.method == 'POST':
        form = ProcesoReservacionHorasForm(request.POST)
        if form.is_valid():
            # Obtener el aula seleccionada
            aula = form.cleaned_data['aula']

            # Verificar si los cupos reservados están por debajo de la capacidad
            if aula.cupos_reservados < aula.capacidad and aula.cupos_reservados < 30:
                form.save()  # Guardar la reservación
                # Incrementar los cupos reservados
                aula.cupos_reservados += 1
                aula.save()  # Guardar los cambios en el aula

                # Actualizar el estado del aula
                if aula.cupos_reservados == aula.capacidad:
                    aula.estado = Estado.objects.get(
                        descripcion='Inactivo')  # Cambia 'nombre' por el campo correspondiente en tu modelo
                else:
                    aula.estado = Estado.objects.get(
                        descripcion='Activo')  # Cambia 'nombre' por el campo correspondiente en tu modelo
                aula.save()

                messages.success(request, 'Reservación creada con éxito.')
                return redirect('listar_reservaciones')
            else:
                messages.error(request,
                               'No se puede hacer la reservación: los cupos están completos o superan el límite permitido.')
    else:
        usuario_id = request.session.get('usuario_id')
        form = ProcesoReservacionHorasForm(user=usuario_id)

    return render(request, 'reservaciones/agregar_reservacion.html', {'form': form})


# Vista para editar una reservación existente
def editar_reservacion(request, pk):
    reservacion = get_object_or_404(ProcesoReservacionHoras, pk=pk)
    aula_anterior = reservacion.aula  # Guarda el aula anterior

    if request.method == 'POST':
        form = ProcesoReservacionHorasForm(request.POST, instance=reservacion, user=request.user)
        if form.is_valid():
            aula_nueva = form.cleaned_data['aula']  # Obtiene el aula seleccionada

            if aula_nueva != aula_anterior:
                # Decrementa los cupos reservados del aula anterior
                aula_anterior.cupos_reservados -= 1
                aula_anterior.save()

                # Verificar el estado del aula anterior después de la reducción
                if aula_anterior.cupos_reservados < aula_anterior.capacidad:
                    aula_anterior.estado = Estado.objects.get(descripcion='Activo')
                    aula_anterior.save()

                # Verifica si el aula nueva tiene capacidad y no supera 30
                if aula_nueva.cupos_reservados < aula_nueva.capacidad and aula_nueva.cupos_reservados < 30:
                    form.save()  # Guardar la reservación

                    # Incrementar los cupos reservados del aula nueva
                    aula_nueva.cupos_reservados += 1
                    aula_nueva.save()  # Guardar los cambios en el aula nueva

                    # Actualizar el estado del aula nueva
                    if aula_nueva.cupos_reservados == aula_nueva.capacidad:
                        aula_nueva.estado = Estado.objects.get(descripcion='Inactivo')
                    else:
                        aula_nueva.estado = Estado.objects.get(descripcion='Activo')
                    aula_nueva.save()

                    messages.success(request, 'Reservación editada con éxito.')
                    return redirect('listar_reservaciones')
                else:
                    # Restaurar el cupo del aula anterior si no se puede agregar en la nueva
                    aula_anterior.cupos_reservados += 1
                    aula_anterior.save()
                    messages.error(request, 'No se puede hacer la reservación: los cupos están completos o superan el límite permitido en el aula seleccionada.')
            else:
                # Si no hay cambio de aula, simplemente guarda la reservación
                form.save()
                messages.success(request, 'Reservación editada con éxito.')
                return redirect('listar_reservaciones')
    else:
        form = ProcesoReservacionHorasForm(instance=reservacion, user=request.user)

    return render(request, 'reservaciones/editar_reservacion.html', {'form': form, 'reservacion': reservacion})


from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from Sistema_Reservacion_Horas.models.aulas_model import ProcesoReservacionHoras, AulasLaboratorios, Estado

def eliminar_reservacion(request, pk):
    reservacion = get_object_or_404(ProcesoReservacionHoras, pk=pk)
    aula = reservacion.aula  # Guarda el aula relacionada

    if request.method == 'POST':
        # Decrementar los cupos reservados del aula relacionada
        aula.cupos_reservados -= 1
        aula.save()

        # Eliminar la reservación
        reservacion.delete()

        # Actualizar el estado del aula después de la eliminación
        if aula.cupos_reservados == aula.capacidad:
            aula.estado = Estado.objects.get(descripcion='Inactivo')  # Cambia 'nombre' por el campo correspondiente en tu modelo
        else:
            aula.estado = Estado.objects.get(descripcion='Activo')  # Cambia 'nombre' por el campo correspondiente en tu modelo
        aula.save()

        messages.success(request, 'Reservación eliminada con éxito.')
        return redirect('listar_reservaciones')

    return render(request, 'reservaciones/eliminar_reservacion.html', {'reservacion': reservacion})

