from django.db.models import Sum
from .models import DetalleSolicitud  # Asegúrate de importar DetalleSolicitud
from .models import Solicitud

def obtener_suma_cantidades(producto_id, año, mes):
    return DetalleSolicitud.objects.filter(
        producto_id=producto_id,
        estado=1,  # Solo DetalleSolicitud con estado 1
        solicitud__estado=2,  # Solo Solicitudes con estado 2
        solicitud__fecha_solicitud__year=año,
        solicitud__fecha_solicitud__month=mes
    ).aggregate(Sum('cantidad'))['cantidad__sum'] or 0  # Devuelve 0 si no hay resultados



def obtener_anios():
    return Solicitud.objects.filter(estado=2).values('fecha_solicitud__year').distinct()
