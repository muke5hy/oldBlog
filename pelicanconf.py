#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Mukesh'
SITENAME = 'Mukesh Yadav'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

THEME = "pelican-themes/resume"


#Profile information
NAME = 'Mukesh YAdav'
TAGLINE = 'Architect | Engineering Manager'
PIC = 'https://secure.gravatar.com/avatar/8bc7685b1c8b11a604567415bcfd0929'

#sidebar links
EMAIL = 'mak.gnu@gmail.com'
PHONE = '(+91) 9773451231'
WEBSITE = 'mukeshyadav.com'
LINKEDIN = 'muke5hy'
GITHUB = 'muke5hy'
TWITTER = '@muke5hy'

CAREER_SUMMARY = 'I am a full-stack developer currently working as a software developer at Zomato. I am a Google Summer of Code mentor for CLTK. I also participated in GSoC last year as a student. I have also worked at Aspiring Minds and various other startups mainly working on Web and Android.'

SKILLS = [
	{
		'title': 'JAVA',
   		'level': '90'
   	},
  	{
  		'title': 'Javascript &amp; jQuery',
   		'level': '95'
   	},
    {
  		'title': 'HTML5 &amp; CSS',
  		'level': '95'
  	},
  	{
  		'title': 'Python',
  		'level': '90'
  	},
  	{
  		'title': 'PHP',
  		'level': '85'
  	}
]

PROJECT_INTRO = 'You can list your side projects or open source libraries in this section. '

PROJECTS = [
	{
		'title': 'Open Source Contributions',
		'tagline': 'Active contributor in FOSSASIA, worked on the Open Event project (both server and android app).Active contributor in CLTK, worked on the CLTK Web app and API.Made valuable contributions in phpBB, implemented a live search feature.Also made a few contributions to Processing.org and phpMyAdmin.'
	},
	{
		'title': 'Music Hub',
		'tagline': 'Android app that connects multiple devices via wifi and plays music in all connected devices simultaneously to create a loud stereo-like sound effect.'
	},
	{
		'title': 'Music Timer',
		'tagline': 'Android app that monitors phone’s movement to detect whether the user’s asleep and pause music playback accordingly.'
	}
]

LANGUAGES = [
	{
		'name': 'Hindi',
		'description': 'Native'
	},
	{
		'name': 'English',
		'description': 'Professional'
	},
	{
		'name': 'Urdu',
		'description': 'Amateur'
	}
]

INTERESTS = [
	'Gaming',
	'Cricket'
]

EXPERIENCES = [
	{
		'job_title': 'Software Development Engineer',
		'time': 'Oct 2016 - Present',
		'company': 'Zomato, Gurgaon IN',
		'details': 'Part of the web team working on developing a smart POS system for restaurants.'	
	},
	{
		'job_title': 'Web developer',
		'time': 'Aug 2016 - Dec 2016',
		'company': 'Archimedes Digital, WFH',
		'details': 'Worked on developing an online catalog for museums using scans of various objects (artifacts, books etc). Developed a highly zoomable image viewer and integrated linting and test suites to be used across projects.'
	},
	{
		'job_title': 'Google Summer of Code Student',
		'time': 'May 2016 - Aug 2016',
		'company': 'Classical Language Toolkit (CLTK), WFH',
		'details': 'Worked on the CLTK webapp - a modern reading environment to study classical languages. Updated the webapp to provide definitions, translations and commentary along with the text. Added functionality to add annotations and bookmarks to enhance the reading experience for user. Working on extending user profile to include annotations, bookmarks and other social networks.'	
	},
	{
		'job_title': 'Research and Development Intern',
		'time': 'May 2015 - June 2015',
		'company': 'Aspiring Minds, Gurgaon IN',
		'details': 'Developed a CRM-simulation module integrated into the employability assessment platform AMCAT. Created the frontend for the module and wrote backend code for question delivery and scoring. Designed the database schemas for the module compatible with the current platform’s database.'
	}
]

EDUCATIONS = [
	{
		'degree': 'B.E in Information Technology',
		'meta': 'Netaji Subhas Institute of Technology (NSIT)',
		'time': '2013'
	},
	{
		'degree': 'Bsc IT ',
		'meta': 'Mumbai University',
		'time': '2008'
	}
]