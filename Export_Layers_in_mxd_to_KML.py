def main():
    pass

if __name__ == '__main__':
    main()

import os,arcpy

from arcpy import env

env.overwriteoutput = True

# Output folder where the Google Earth Files will be saved
folder = r"Your path here"

# Specificy the map document you wish to export from
mxd = arcpy.mapping.MapDocument(r"Your mxd here")

# "Layers" is the dataframe to export layers from
df = arcpy.mapping.ListDataFrames(mxd, "Layers")[0]

# Build a list of layers in the dataframe
layers = arcpy.mapping.ListLayers(mxd, "*", df)

for layer in layers:
    outKML = os.path.join(folder, "{}.kmz".format(layer))
    arcpy.LayerToKML_conversion(layer, outKML)
else:
    arcpy.AddMessage('There are no layer files in {}'.format(arcpy.env.workspace))


