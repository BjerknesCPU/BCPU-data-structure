ERA data
========

This page contains information on how data from the ECMWF ERA5, ERA20C and
ERA-Interim (ERAI) datasets are stored in our NS9039K data structure in
NIRD.

Files from ERA5, ERA20C or ERAI should all be named following the same
conventions:

<**ERA_dataset**>_<**parameter_number**>_<**date**>(-<**end_date**>)(_<**months**>)_(<**frequency**>).<**extension**>

using the following definitions:

<**ERA_dataset**> : which dataset (ERA5/ERA20C/ERAI)

<**parameter_number**> : Three-digit number from the
`parameter table <https://apps.ecmwf.int/codes/grib/param-db?&filter=grib1&table=128>`_.

<**date**> : date of data (e.g. 201901)

<**end_date**> : (optional) end date of data if range is specified (e.g. 201912)

<**months**> : (optional) which months of the year (e.g. '_DJF_')

<**frequency**> : (optional) dependent on time step selected (e.g. 6-hourly, 12-hourly)

<**extension**> : file extension which is '.grib' or '.nc'

For example:

* ERAI_167_198001-199912.nc

* ERA5_034_1979.nc

ERA5
----

Download instructions
`here <https://confluence.ecmwf.int/display/CKB/How+to+download+ERA5>`_.

ERA5 data is stored in NIRD in the structure
/projects/NS9039K/data/external/reanalysis/ECWMF/ERA5/original/<**ERA5-dataset**>/<**product_type**>/<**variable_name**>/

Where <**ERA5-dataset**> is a subset of ERA5 which can be searched
`here <https://cds.climate.copernicus.eu/#!/search?text=ERA5&type=dataset>`_

<**product_type**> can be found on the 'Download data' tab, for example:
` for hourly_single-level_prelim <https://cds.climate.copernicus.eu/cdsapp#!/dataset/reanalysis-era5-single-levels-preliminary-back-extension>`_

<**variable_name**> is the short name of the variable (e.g. tas or uas) which can be found in the
`parameter table <https://apps.ecmwf.int/codes/grib/param-db?&filter=grib1&table=128>`_.

ERA20C
------

Download
`here <https://apps.ecmwf.int/datasets/data/era20c-daily/levtype=sfc/type=an/>`_.

ERA20C data is stored in NIRD in the structure
/projects/NS9039K/data/external/reanalysis/ECWMF/ERA20C/original/<**Type_of_level**>/<**Type**>/<**ERA-20C_sets**>/<**variable_name**>/

This structure is identical to that of the download page above.

<**variable_name**> is the short name of the variable (e.g. tas or uas) which can be found in the
`parameter table <https://apps.ecmwf.int/codes/grib/param-db?&filter=grib1&table=128>`_.

ERA-Interim
-----------

Download
`here <https://apps.ecmwf.int/datasets/data/interim-full-daily/levtype=sfc/>`_.

ERAI data is stored in NIRD in the structure
/projects/NS9039K/data/external/reanalysis/ECWMF/ERAI/original/<**Type_of_level**>/<**ERA_Interim_Fields**>/<**variable_name**>/

This structure is identical to that of the download page above.

<**variable_name**> is the short name of the variable (e.g. tas or uas) which can be found in the
`parameter table <https://apps.ecmwf.int/codes/grib/param-db?&filter=grib1&table=128>`_.
