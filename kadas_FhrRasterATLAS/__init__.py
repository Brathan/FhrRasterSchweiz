# -*- coding: utf-8 -*-


def classFactory(iface):
    from .kadas_FhrRasterATLAS import KadasExample
    return KadasExample(iface)
