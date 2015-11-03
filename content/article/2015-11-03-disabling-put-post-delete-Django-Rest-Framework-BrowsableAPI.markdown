Title: Disabling Put Post Delete Django Rest Framework BrowsableAPI
Date: 2015-11-03 10:30:12.000000000 +05:30
Slug: disabling-put-post-delete-Django-Rest-Framework-BrowsableAPI
Authors: Mukesh
Modified: 
Category: 
Tags: Django, DRF, Python
Status: draft
Summary: 

        Disabling PUT/POST/DELETE from BrowsableAPI of DRF

If you are building a Rest Full Service in Django then you must be familiar with Django-Rest-Framework AKA DRF. DRF helps you to build API with very less code footprint. 

DRF has BrowsableAPI which gives a frontend to view API and do some test, by using this you can do GET/PUT/POST/DELETE etc in your browser. Hence you do not require script or POSTMAN/CURL to test. Although these feature is very usefull on development server but for the prodcution you really do not want the PUT/POST/DELETE actions. 

To disable these action we need to extend BrowsableAPIRenderer and change the `display_edit_forms` and `delete_form` to False. Lets create a file `BrowsableAPIRendererGet` some where in your project where you place common files or tools. I keep them in base.lib package, so create `base/lib/BrowsableAPIRenderer.py`.

`base/lib/BrowsableAPIRenderer.py`

	from rest_framework.renderers import BrowsableAPIRenderer

	class BrowsableAPIRendererGet(BrowsableAPIRenderer):
	    """Renders the browsable api, but excludes the forms."""

	    def get_context(self, *args, **kwargs):
	        context = super().get_context(*args, **kwargs)
	        context['display_edit_forms'] = False
	        context['delete_form'] = False
	        return context

Once you done with that call the custom renderer from your settings file hence in you settings.py add following in `DEFAULT_RENDERER_CLASSES`


	REST_FRAMEWORK = {
	    'DEFAULT_RENDERER_CLASSES': (
	        'rest_framework.renderers.JSONRenderer',
	        'base.lib.BrowsableAPIRenderer.BrowsableAPIRendererGet',
	    )
	}

Now all done you can brows the API but you will not be able to do PUT/POST/DELETE actions. You might want to create diffrent settings file for development and production in case you require PUT/POST/DELETE along with GET. 
