# -*- coding: utf-8 -*-
from import_export import resources
from .models import *


class paquete_resouce(resources.ModelResource):
    class Meta:
        model = Paquete
        fields = ('id', 'archivo', 'consecutivo', 'contrato', 'factura',
            'ciclo',
              'mes', 'ano', 'cliente', 'direccion', 'barrio', 'municipio',
              'departamento', 'distribuidor', 'ruta', 'zona', 'telefono',
              'segmento', 'tarifa', 'idbarrio', 'iddepartamento', 'idmunicipio',
              'servicio', 'cupon', 'total_mes_factura', 'valor_pagar',
              'numero_fiscal', 'factura_interna', 'telefono_contacto')
