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

File permissions
----------------

It is important that we apply the correct file permissions to data which we
place in the /projects/NS9039K/data directory so that other members of our team
can use the data.

Use the command ``ls -l`` to check file permissions, which are displayed as e.g.
``-rw-r--r--``. In this output, permissions are provided for three groups;
'user', 'group' and 'other'. The first character ``-`` corresponds to the file
type, ``-`` indicating that it is a file, a ``d`` indicating a directory.
The next three characters ``rw-`` are the 'user' permissions, the user being the
owner of the file. The following three characters ``r--`` correspond to the
'group', and the last ``r--`` to 'other'. Each character corresponds to a type
of permission defined below:

``r`` : read

``w`` : write

``x`` : execute

The 'user' in this example ``rw-`` has the permissions: read, write and not
execute. The 'group' has permissions ``r--``: read, not write and not execute.

Permissions are modified by the file owner using the ``chmod`` command. To
find out more about this command, use ``man chmod``. The group can be modified
by the file owner using the command ``chgrp``, and in the NS9039K data directory
should always be 'ns9039k', e.g. ``chgrp ns9039k <file>``.

For shared data, we want to make sure that other users in our group have read
access to the files. This means we usually want permissions ``-rw-rw-r--``.
To apply these permissions apply:

``-rw-rw-r--`` : ``chmod 664 <files>``

Remember that for directories, we should always have read and execute
permissions for the user and the group, for example:

``drwxrwxr-x`` : ``chmod 775 <directories>``

Compressing files
-----------------

In order to remain within the NS9039K project space quota, we should try to
compress NetCDF4 files. By using lossless compression, we can reduce file sizes
without losing any information in the files. Compressed files can,
however, take longer to load for subsequent analysis, so for data that will be
used in tasks where high I/O speed is required, compression is not recommended.

The ``nccopy`` command can be used to compress NetCDF data, for example::

  nccopy -k 4 -s -d <compression_level> <filename> <compressed_filename>

where compression_level is the deflation level, from 1 (faster but lower
compression) to 9 (slower but higher compression). The recommended value for
this is 5.

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
