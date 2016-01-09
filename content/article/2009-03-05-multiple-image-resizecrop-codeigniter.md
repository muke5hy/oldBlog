Title: Multiple Image resize/crop in Codeigniter
Date: 2009-03-05 08:53
Author: Mukesh
Category: CodeIgniter
Tags: CodeIgniter, php
Slug: multiple-image-resizecrop-codeigniter
Status: published

I have moved my blog to [makdotgnu.com](http://www.makdotgnu.com/ "makdotgnu")
------------------------------------------------------------------------------

 

Well Codeigniter is a very light Framework compare to Zend and Cake PHP.

Codeigniter provides a image manipulation class. To upload and resize
(thumb) in one size we need to just load the library and call resize()
method.

`$config['image_library'] = 'gd2'; $config['source_image'] = $this->data['full_path']; $config['new_image'] = $this->image_path; $config['create_thumb'] = TRUE; $config['maintain_ratio'] = TRUE; $config['thumb_marker'] = ""; $config['width'] = 640; $config['height'] = 480;$this->load->library('image_lib',$config); $this->image_lib->resize() $this->data['full_path'] //is a full path of the of the uploaded image. To Resize the images in multiple sizes we need to use the clear() of image_lib class.$this->load->library('image_lib'); $this->image_lib->clear(); $this->image_lib->initialize($config); if ( ! $this->image_lib->resize()) { $this->upload_error = $this->image_lib->display_errors(); $this->image_lib->clear(); return false; }`

In \$config I'm passing the different values in a loop and changing the
image size.
