from osgeo.gdal import *  
from osgeo.gdalnumeric import *  
from osgeo.gdalconst import * 

class Utils():
    def trunc(f, n):
		return ('%.*f' % (n + 1, f))[:-1]