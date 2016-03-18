# aashe-conference

[![Build Status](https://travis-ci.org/AASHE/aashe-conference.svg?branch=master)](https://travis-ci.org/AASHE/aashe-conference) [![Coverage Status](https://coveralls.io/repos/github/AASHE/aashe-conference/badge.svg?branch=master)](https://coveralls.io/github/AASHE/aashe-conference?branch=master)

http://conference.aashe.org/

AASHE Conference micro-site.

## Hosting

This is currently hosted on heroku usinag an Nginx proxy on 'sustain' pointing to
the AASHE-proxy Heroku App. See documentation in django-integration-settings for
details.

## Deployment

To deploy, simply push to the Heroku remote:

    git push heroku master

Use Heroku control panel to promote to staging and production.

## Database

For the initial installation, run syncdb and migrate as usual. After this is complete, set an environment variable CMS=True. This enables the registration of content types in content/models.py.

After setting this variable, simply run syncdb again to create the content type tables.

This is only necessary for the creation of the database (due to circular dependencies with the medialibrary tables). For future deployments, run syncdb to load new content types (FeinCMS does not use migrations) and migrate as you normally would.

## Documentation

The following documents detail the various content types and interfaces, hosted in the "Conference/Website Documentation" shared folder on AASHE's google drive.

Content Types - https://docs.google.com/document/d/1QQTW6RmYZ8geOCqCqdMt8umET9RV2yZG6e4DF4b6sFg
Page Editing Interface - https://docs.google.com/document/d/1buRjs9pZH7WJzx6ax64vlZmU9O1b6b7FjBa8duPyvYo
