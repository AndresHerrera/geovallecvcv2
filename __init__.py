# -*- coding: utf-8 -*-
"""
/***************************************************************************
 GeoValleCVC
                                 A QGIS plugin
 PlugIn para QGIS - Modelo Geoidal CVC del Valle del Cauca v2
 Generated by Plugin Builder: http://g-sherman.github.io/Qgis-Plugin-Builder/
                             -------------------
        begin                : 2020-01-10
        copyright            : (C) 2020 by Andres Herrera
        email                : fandresherrera@hotmail.com
        git sha              : $Format:%H$
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
 This script initializes the plugin, making it known to QGIS.
"""


# noinspection PyPep8Naming
def classFactory(iface):  # pylint: disable=invalid-name
    """Load GeoValleCVC class from file GeoValleCVC.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    #
    from .geovallecvc import GeoValleCVC
    return GeoValleCVC(iface)
