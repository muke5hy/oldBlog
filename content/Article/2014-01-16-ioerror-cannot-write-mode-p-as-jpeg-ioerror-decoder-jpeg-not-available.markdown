Title: ! 'IOError: cannot write mode P as JPEG | IOError: decoder jpeg not available'
Date: 2014-01-16 17:03:24.000000000 +05:30
Modified: 
Category: 
Tags: Python
Slug: ioerror-cannot-write-mode-p-as-jpeg-ioerror-decoder-jpeg-not-available
Authors: mukesh
Summary: 

uninstall PIL

	pip uninstall PIL

	sudo apt-get install libjpeg-dev libfreetype6-dev zlib1g-dev libpng12-dev

	pip install PIL --upgrade
    
    
If everything works 

you will see 
	
	--------------------------------------------------------------------
    PIL 1.1.7 SETUP SUMMARY
    --------------------------------------------------------------------
    version       1.1.7
    platform     linux2 2.7.4 (default, Sep 26 2013, 03:20:26)
                  [GCC 4.7.3]
    --------------------------------------------------------------------
    *** TKINTER support not available
    *** JPEG support not available
    *** ZLIB (PNG/ZIP) support not available
    *** FREETYPE2 support not available
    *** LITTLECMS support not available
    --------------------------------------------------------------------
    To add a missing option, make sure you have the required
    library, and set the corresponding ROOT variable in the
    setup.py script.
	
If the issue does resolve 

	pip uninstall PIL
    
and install Pillow 

	pip install pillow
      
You will see something like this at once its installed. 
  	
   --------------------------------------------------------------------
      PIL SETUP SUMMARY
      --------------------------------------------------------------------
      version      Pillow 2.3.0
      platform     linux2 2.7.4 (default, Sep 26 2013, 03:20:26)
                   [GCC 4.7.3]
      --------------------------------------------------------------------
      *** TKINTER support not available
      --- JPEG support available
      --- ZLIB (PNG/ZIP) support available
      --- LIBTIFF support available
      --- FREETYPE2 support available
      --- LITTLECMS2 support available
      *** WEBP support not available
      *** WEBPMUX support not available
      --------------------------------------------------------------------
