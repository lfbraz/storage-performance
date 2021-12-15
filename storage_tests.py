import time
import matplotlib.pyplot as plt

from osgeo import gdal
import glob


def run(local=True):
    start_time = time.time()

    # Set Local or File Share
    project_path = 'C:' if local else 'Z:'
    project_path += '\\NE1_HR_LC_SR'

    dir = project_path + '\\NE1_HR_LC_SR.tif'
    evi_file = glob.glob(dir)

    EVI = gdal.Open(evi_file[0])

    EVIBand = EVI.GetRasterBand(1)                  # Read the band (layer)
    EVIData = EVIBand.ReadAsArray().astype('float') # Import band as an array with type float

    EVI_meta = EVI.GetMetadata()                   # Store metadata in dictionary
    rows, cols = EVI.RasterYSize, EVI.RasterXSize  # Number of rows,columns

    # Projection information
    geotransform = EVI.GetGeoTransform()
    proj= EVI.GetProjection()

    # Band metadata
    EVIFill = EVIBand.GetNoDataValue()            # Returns fill value
    EVIStats = EVIBand.GetStatistics(True, True)  # returns min, max, mean, and standard deviation
    EVI = None                                    # Close the GeoTIFF file
    print('Min EVI: {}\nMax EVI: {}\nMean EVI: {}\nSD EVI: {}'.format(EVIStats[0],EVIStats[1], EVIStats[2], EVIStats[3]))

    # Persist stats file    
    filename = 'evi-stats-' + time.strftime("%Y%m%d-%H%M%S")

    with open(project_path + '\\logs\\' + filename, 'w') as f:
        f.write('Min EVI: {}\nMax EVI: {}\nMean EVI: {}\nSD EVI: {}'.format(EVIStats[0],EVIStats[1], EVIStats[2], EVIStats[3]))

    # Persist image
    # plt.ioff()
    # plt.imshow(EVIData)
    # plt.savefig("C:\\NE1_HR_LC_SR\\myevi.png")

    print("--- %s seconds ---" % (time.time() - start_time))

if __name__ == '__main__':
    run(False)