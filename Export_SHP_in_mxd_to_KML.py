#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      MullerC
#
# Created:     06-06-2017
# Copyright:   (c) MullerC 2017
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    pass

if __name__ == '__main__':
    main()

import os,arcpy

# Output folder where the Google Earth Files will be saved
folder = r"I:\0200\0243\0243-198\5\Google\2017-06-06\New"

# Specificy the map document you wish to export from
mxd = arcpy.mapping.MapDocument(r"E:\Temp\243-0050_Master_Plan_Layout_Rev02.mxd")

# "Layers" is the dataframe to export layers from
df = arcpy.mapping.ListDataFrames(mxd, "Layers")[0]

# Build a list of layers in the dataframe
layers = arcpy.mapping.ListLayers(mxd, "*", df)

for layer in layers:
    outKML = os.path.join(folder, "{}.kmz".format(layer))
    arcpy.LayerToKML_conversion(layer, outKML)
else:
    arcpy.AddMessage('There are no layer files in {}'.format(arcpy.env.workspace))


