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
