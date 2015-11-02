import gdal
ds=gdal.Open('p219r063_TC_2005.tif')
bound= ds.GetRasterBand(1)
print bound.GetNoDataValue()
print bound.GetMinimum()
print bound.GetMaximum()
print bound.GetScale()
ctable=bound.GetColorTable()
print ctable.GetCount()
for i in range(0,ctable.GetCount()):
	entry=ctable.GetColorEntry(i)
	print ctable.GetColorEntryAsRGB(i,entry)
