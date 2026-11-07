# Constantinople modern DSM research reference

Applies to `constantinople-modern-dsm-reference.tif`, an integer-window crop of one public Copernicus GLO-30 COG tile. It is a modern digital surface model, including buildings, infrastructure and vegetation. It does not represent bare earth, the ancient city surface, historical coastlines or verified locations of historical features. Its presence in this research repository does not approve a campaign map, select a site or authorize game use. No endorsement by the Copernicus programme, European Union, ESA, DLR or Airbus is implied.

Source: [Copernicus DEM product description](https://dataspace.copernicus.eu/explore-data/data-collections/copernicus-contributing-missions/collections-description/COP-DEM), [public GLO-30 AWS mirror readme](https://copernicus-dem-30m.s3.amazonaws.com/readme.html), and the [complete GLO-30 licence (PDF)](https://docs.sentinel-hub.com/api/latest/static/files/data/dem/resources/license/License-COPDEM-30.pdf). The official current product page describes GLO-30 as a DSM that includes buildings, infrastructure and vegetation and documents WGS84-G1150 / EPSG:4326, vertical EGM2008 / EPSG:3855, metre units and RasterPixelIsPoint. These vertical-datum and surface-class statements come from product documentation; they are not extracted from a vertical datum tag in the downloaded TIFF. The public AWS mirror readme identifies GLO-30 Public, says tiles are free to the general public under the linked licence, describes the one-degree S3 tile layout and explains that shared southern/eastern edge samples are removed from public COGs.

Original source notice required by Article 6(a):

> © DLR e.V. 2010-2014 and © Airbus Defence and Space GmbH 2014-2018 provided under COPERNICUS by the European Union and ESA; all rights reserved.

Modified-data notice required by Article 6(b):

> produced using Copernicus WorldDEM-30 © DLR e.V. 2010-2014 and © Airbus Defence and Space GmbH 2014-2018 provided under COPERNICUS by the European Union and ESA; all rights reserved.

Liability notice required for distribution or public communication under Article 6(c):

> The organisations in charge of the Copernicus programme by law or by delegation do not incur any liability for any use of the Copernicus WorldDEM-30.

The complete licence also requires users to avoid implying official endorsement and to bind downstream users to the applicable Article 6 obligations. This notice does not replace or broaden the complete licence. The product page describes GLO-30 as free and open; WorldDEM-10 is a separate product and is outside this reference.

Processing details, the requested bbox and actual sample-centre/outer-cell bounds, integer window, CRS, transform, source and crop hashes, byte sizes, tool versions, and exact sample-equality verification are recorded in [`constantinople-modern-dsm-processing.json`](../constantinople-modern-dsm-processing.json). One tile only was retrieved. The crop was losslessly DEFLATE re-encoded without resampling, filling, value edits or reprojection.
