# Jerusalem: additional topographic controls

Collected by Luna and checked by gpt-6, 27 October 2026. These are source-control notes for the open map decision, not approved routes, new historical episodes or additions to the registered 50 local research resources. Luna's follow-up materialization stopped at a usage limit without a product. Root completed this note in its own unit. No new historical map image was successfully downloaded in this delivery.

## Keep distinct editions and sheets distinct

The [OpenJerusalem archival record](https://www.archives.openjerusalem.org/index.php/informationobject/browse?creators=182703&languages=en&media=print&names=769&sf_culture=el&sort=alphabetic&sortDir=asc&topLod=0) identifies `JM-NLI/ELCC/Pal751/sheet17`, **Sheet XVII**, 1880, covering Jerusalem and its surroundings. It attributes the survey to Conder and Kitchener, 1872–1877, with maps drawn in May 1878. Its digitization link identifies NLI record `NNL_MAPS_JER002368494`, image `FL50537899`. The series record and a particular sheet image are separate identifiers.

The [David Rumsey collection's Sheet XVII record](https://www.davidrumsey.com/luna/servlet/detail/RUMSEY~8~1~240983~5512359:Sheet-XVII--Palestine-Exploration-M), list number `6930.020`, image number `6930020`, provides an independent directly inspected copy record: sheet date 1880, scale 1:63,360, object 53 × 57 cm. Its bound volume has publication date **1882** and a note describing a likely third issue with a different printing. Do not silently label that digital copy as the identical 1880 first impression or as the Wilson 1865 map. The nineteenth-century relief and drainage can be comparative evidence; its streets, walls and buildings cannot be transplanted into c.30–33 CE.

NLI catalogue pages and the documented public IIIF manifest/image-info requests returned HTTP403 on this attempt. The [official Image API documentation](https://www.nli.org.il/en/research-and-teach/open-library/image-api) and [Presentation API documentation](https://www.nli.org.il/en/research-and-teach/open-library/presentation-api) explain the interfaces; they are not a successful image response or a rights grant for a particular scan. No preview, dimensions, checksum or confirmed per-image licence is fabricated. A series-wide NLI identifier mentioned during collection is insufficient to prove that a selected image is Sheet XVII. No scan was copied from Rumsey without inspecting applicable reuse terms.

The existing local Wilson 1865 preview and its own metadata remain a distinct reference. Any overlay needs documented control points, transformation and positional residuals before a point can be classified as ridge, ravine or crossing. An unreferenced visual resemblance does not certify the waypoint geometry.

## Modern drainage context

The Israel Nature and Parks Authority's [Ein Khaniya audio-guide text](https://www.parks.org.il/article/enhaniya-audio/), dated 27 October 2022, describes Nahal Refaim beginning around the present German Colony/Emek Refaim area and becoming more incised westward, joining Sorek and ultimately draining toward the Mediterranean. The accessible text also identifies seasonal flow. This supports a modern regional drainage relationship, not an ancient route, bridge or precise crossing. Current neighbourhood names locate the explanation; they are not first-century settlements to paint into the scene. Restored terraces and later buildings described in that guide likewise do not prove a c.30–33 CE footprint. No INPA photograph, audio recording or long text passage is copied.

The [Geological Survey of Israel report GSI/08/2014](https://www.gov.il/BlobFolder/reports/arkin-ecker-report-2014/he/report_regional_geology_GSI-08-2014.pdf) is a candidate for a further regional hydrogeological check. Luna located an indexed figure34/p45 reference, but the PDF access attempt was blocked; root has not verified that figure's contents, coordinate reference system or reuse terms. Do not report an indexed description as an inspected figure or derive a drainage line from it.

## Decision carried forward

Both route candidates still require a measured overlay and topographic interpretation. General westward drainage does not locate a safe footpath through each supplied coordinate. The map builder receives no licence to fill Hinnom, turn Kidron into navigable water, add a Roman bridge without evidence or substitute a later mapped street for an ancient road. The draft binding remains blocked for a historical build, while the native household controller can be tested on an explicitly synthetic physical fixture.


## Complete design-frame surface reference

The previous modern crop covered the activity cluster, not the entire padded 340 × 340 frame. The [new full-frame derivative](24-modern-surface-frame-crop.tif), [processing metadata](24-modern-surface-frame-metadata.json) and [scientific preview](24-modern-surface-frame-preview.png) cover every cell of the existing cosine-corrected frame. It is a lossless 763 × 649 source window with 495,187 surface samples from the already pinned Copernicus tile. Its source hash, exact integer window, WGS84 transform, complete-cell bounds and output/preview hashes are recorded. An alternative Pillow TIFF decoder reproduced every sample read by Rasterio; this is a decoder check by the same architect, not a separate model review.

No values were filled, smoothed, resampled or converted to native elevation. Buildings and vegetation remain part of this modern DSM. The colours encode surface height, not water. This closes the data-coverage gap for later terrain inspection; it does not close the ancient-ground, route, native-footprint or engine gates. The existing source and licence obligations apply, with modification, liability and no-endorsement notices retained in the metadata and original licence note. The new window is a derivative of an existing source, not another registered historical reference.
