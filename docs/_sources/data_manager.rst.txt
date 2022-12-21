Data manager notes
==================

These notes are intended for the data manager(s) of NS9039K.  

Updating the data structure 
---------------------------

The data structure currently holds external data products. As we built a culture of 
using the new data structure, it is important to encourage team members to download 
any new external data products (e.g. CMIP6 data) into the new data structure. 

The new structure also requires all users to move their personal directories from 
/projects/NS9039K/shared/ to /projects/NS9039K/users. This may be a disruptive 
process, and has largely not been started. The practicallity of this move could 
be reassessed, but if it is decided to move all personal directories, then the 
data manager(s) should assist users in doing so. 

Internal data is still largely stored in /projects/NS9039K/shared/ and on Betzy.
Transferring this into the structure in /projects/NS9039K/data/internal would 
help the new structure to be more widely used.

When making updates to the structure itself, the documentation in this repository 
should be modified accordingly. There is also a version and 'Release tag' system
whereby major changes should be given a new GitHub tag and version number. This 
will help us to keep track of major changes and refer back to previous versions 
of the data structure. Documentation on Releases and Tags can be found 
`here <https://docs.github.com/en/repositories/releasing-projects-on-github/managing-releases-in-a-repository>`_. 


Updating the data structure map
-------------------------------

The data manager(s) should update the data structure map roughly once a month. 
This is done by the following steps. 

1. Take a clone of the BCPU-data-structure code, it is recommended to clone this into /projects/NS9039K/www/$USER/ because this allows for changes to be checked `here <http://ns9039k.web.sigma2.no>`_ before pushing them. 
2. Run ``python data_structure_map.py``. 
3. Add, commit and push changes to the external repository. 


Note that in order for the data structure map to show all relevant directories,
there must be a README.json in each dataset in /projects/NS9039K/data/. These
README.json files contain some basic metadata that is read in by the script 
which generates the data map image. 

Data compression
----------------

It is important to compress files in NS9039K so that we can remain within our
allocation quota. Compression of NetCDF files is a common task that members of
the team have to perform, and the data manager can assist with this task.

When compressing files for another user, the permissions of the file are lost.
The current system that we use, is that the data manager has some additional
permissions to change the file ownership back to the original user after
compressing files.

New permissions will have to be requested for the data manager from
support@metacenter.no. Last time it was Thierry Toutain who set this
up for us.

Currently there is a script set up with additional permissions.

The the internal script does this:
| chown -R --from=tbi045 $1 /trd-project4/NS9039K/$2

The current script is applied like this:
| sudo /usr/local/bin/chown_ns9039k.sh $1 $2

| $1 is the username of the user to transfer ownership to.
| $2 is the relative path to the desired files from /trd-project4/NS9039K/.

Updating mailing lists
----------------------

The data manager manages two mailing lists; bcpu-data@uib.no and bcpu-support@uib.no. Mahaut (mahaut.vareilles@uib.no) is an administrator of these lists, and can provide other users with administrative access. 

**bcpu-data** : a mailing list that the data manager uses to inform users about changes to data in the NIRD NS9039K project space (or in other shared areas such as the BETZY nn9039k project space). This could, for example, be used to remind users to reduce storage usage so that the team does not exceed our quotas. 

The bcpu-data@uib.no mailing list should be updated regularly so that it contains all users who are in the NS9039K NIRD project. It should therefore either be updated every time a new user is added, or at regular intervals (e.g. before sending out an important email to the list). My advice for updating the list is to log into the `Metacentre portal <https://www.metacenter.no/>`_ as an admin, and select 'Projects' > 'NS9039K' > 'List Users' where you can get a list of user emails. Copy these emails into a spreadsheet software (e.g. LibreOffice Calc) and then separate by column so that you get a list of email addresses (one per line). Then add these as members of the mailing list as described below (by pasting into the correct box on the list administration page). 

**bcpu-support** : a mailing list that team-members can write to regarding technical and data issues, documented further `here <https://bjerknescpu.github.io/BCPU-documentation/support/support.html>`_.

The administrator page to manage these mailing lists can only be accessed using the `UiB VPN <https://hjelp.uib.no/tas/public/ssp/content/detail/service?unid=a566dafec92a4d35bba974f0733f3663>`_ or through the internal network. The website for this is https://tjinfo.uib.no/fixlist. 

Once on this page, select 'Listeadministrajon' and then select the desired list in the drop-down menu. From here, members can be added with one address per line in the box at the bottom headed 'Nye medlemmer'.





