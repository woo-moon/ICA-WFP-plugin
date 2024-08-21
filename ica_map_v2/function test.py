from qgis._core import QgsVectorLayer, QgsSymbol

shapefile_path = 'C:/Users/xiaomeng.wu/OneDrive - World Food Programme/Documents/WFP File/ICAExtension/Test on functions/20240729 test/result/reprojected_SI_layer.shp'
layer = QgsVectorLayer(shapefile_path, "layer", "ogr")
symbol = QgsSymbol.defaultSymbol(layer.geometryType())
print(symbol)