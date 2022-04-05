Data best practices
===================

Downloading new data
--------------------

* First check if the data is already present in NIRD by looking in
  /projects/NS9039K/data.

* Check the size of the data download. For large downloads (>1TB),
  you should also check that there is sufficient storage space before commencing
  the download. This can be checked using the command: ::

    dusage -p ns9039k

* Newly downloaded external data should be stored in the shared data structure
  /projects/NS9039K/data/external. The type of data will determine which
  directory to store this in, please follow the guidance in the
  :doc:`data structure documentation <storage_structure>`.
  This documentation also contains information on how to document the data with
  a README file.

* If you need help with the data retrieval process please contact
  our
  `internal support <https://bjerknescpu.github.io/BCPU-documentation/support/support.html>`_.

Compressing files
-----------------

In order to remain within the NS9039K project space quota, we should try to
compress NetCDF4 files. By using lossless compression, we can reduce file sizes
without losing any information in the files. Compressed files can,
however, take longer to load for subsequent analysis, so for data that will be
used in tasks where high I/O speed is required, compression is not recommended.

If you need help with compressing your NetCDF4 files,
please contact our
`internal support <https://bjerknescpu.github.io/BCPU-documentation/support/support.html>`_.

Data archival
-------------

Research data that may be of public interest can be moved to the
`Research Data Archive <https://documentation.sigma2.no/nird_archive/user-guide.html>`_.
If you have data which you no longer need to regularly access, but that you
think would be of interest to others, or that further work could be based around
in the future then this could be suitable for the archive. Contact our
`internal support <https://bjerknescpu.github.io/BCPU-documentation/support/support.html>`_
to find out more.
