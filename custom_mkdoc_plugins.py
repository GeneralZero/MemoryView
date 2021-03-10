import mkdocs
import re
import os, shutil


files_to_copy = {'css/main.css': 'site/assets/stylesheets/custom.css',
'js/main.js': 'site/assets/javascripts/custom.js',
'css/highlighting/dracula.css': 'site/assets/stylesheets/dracula.css',
'js/katex_init.js': 'site/assets/javascripts/katex_init.js',
'js/svgbob.js': 'site/assets/javascripts/svgbob.js',
'css/sortable/sortable-theme-light.css': 'site/assets/stylesheets/sortable-theme-light.css',
'js/sortable.min.js': 'site/assets/javascripts/sortable.min.js',

}

def copy_files(*args, **kwargs):
	for source, destination in files_to_copy.items():
		shutil.copy(source, destination)


def reorder_nav(nav, config, files, **kwargs):
	"""
	The nav event is called after the site navigation is created and can be used to alter the site navigation.
	Here we call our own method which will walk the page tree recursively looking for any folders containing
	only a single page, and attempt to collapse them to keep the nav uncluttered.
	"""

	nav.items = _process_nav_items_recursive(nav)
	return nav



def _process_nav_items_recursive(nav_items):

	nav_folders = []
	nav_files = []

	for nav_item in nav_items:
		if nav_item.children:
			# Check for the name of the folder in the parrent
			#if nav_item.title + ".md" in nav_item.parent:
			#	#Set the main page to the parrent index
			#	#Remove the index version

			# Check for the name of the folder in the child directory
			#if nav_item.title + ".md" in nav_item.children:
			#	#Set the main page to the child index
			#	#Remove the index version

			# Check for the index.md file in the child directory
			#if "index.md" in nav_item.children:
			#	#Set the main page to the child index
			#	#Remove the index version

			
			# If there is more than one child, we want to recurse over them so that
			# we can collapse folders of single pages at any depth in the tree.
			nav_item.children = ( _process_nav_items_recursive( nav_item.children ) )
			nav_folders.append(nav_item)

		else:
			# No child items, just add this directly.
			nav_files.append(nav_item)

	return nav_folders + nav_files
