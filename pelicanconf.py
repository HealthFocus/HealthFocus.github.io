#!/usr/bin/env python
# -*- coding: utf-8 -*- #

from pathlib import Path

root_path = Path(__file__).parent

SITEURL = "http://localhost:8000"

AUTHOR = "HF Software Solutions, Inc"
SITENAME = "Health Focus"
EMAIL = "support@healthfocus.io"
PHONE = "+1 248 238 5833"
OFFICE_ADDRESS = "8031 Main Street, Suite 201, Dexter, Michigan 48130"

PAGE_URL = "{slug}"
PAGE_SAVE_AS = "{slug}/index.html"

PATH = "content"

TIMEZONE = "America/Detroit"

DEFAULT_LANG = "en"

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Social widget
SOCIAL = (
    (
        "LinkedIn",
        "https://www.linkedin.com/company/hf-software-solutions-inc",
        "linkedin",
    ),
)

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True
THEME = "themes/healthfocus"

PARTNERS = (
    ("Huron Valley Physicians Association", "client-1.png", "https://www.hvpa.com"),
    ("Livingston Physician Organization", "client-2.png", "https://www.lpollc.com"),
    ("Great Lakes Physicians Organization", "client-3.png", "https://www.glpo.org"),
    ("Northern Physician Organization", "client-4.png", "https://www.npoinc.org"),
    (
        "Holland Physician Hospital Organization",
        "client-5.png",
        "https://www.hollandpho.org",
    ),
    (
        "St. Mary" "s Physician Hospital Organization",
        "client-6.png",
        "https://healthcare.ascension.org/",
    ),
)

TEAM = (
    {
        "name": "James W. Morris",
        "title": "Chief Executive Officer",
        "img": "james.jpg",
        "description": "When not at his desk, you might catch him at the airport with his camera before embarking on a world-wide adventure.",
        "social": (
            (
                "LinkedIn",
                "https://www.linkedin.com/in/james-morris-baa41827",
                "ri-linkedin-box-fill",
            ),
        ),
    },
    {
        "name": "Debra Roberts",
        "title": "VP, Operations",
        "img": "debra.jpg",
        "description": "If you"
        "re looking for Deb, just follow the sun! When not in Michigan, you"
        "ll commonly find her on the beach in Florida.",
        "social": (
            (
                "LinkedIn",
                "https://www.linkedin.com/in/debra-roberts-99392113/",
                "ri-linkedin-box-fill",
            ),
        ),
    },
    {
        "name": "Michael Wilson",
        "title": "Enterprise Architect",
        "img": "michael.jpg",
        "description": "Michael"
        "s artistic side extends beyond network and UML diagramming to include figures in pen & ink.",
        "social": (
            (
                "LinkedIn",
                "https://www.linkedin.com/in/michaeldavidwilson/",
                "ri-linkedin-box-fill",
            ),
        ),
    },
    {
        "name": "Jonah Group",
        "title": "Project Development",
        "img": "jonah.jpg",
        "description": "Health Focus relies on rapidly scalable teams in order to support targeted feature deployments and front-end development.",
        "social": (
            ("Website", "https://jonahgroup.com", "ri-computer-fill"),
            ("Facebook", "https://www.facebook.com/jonahgroup/", "ri-facebook-fill"),
            ("Twitter", "https://twitter.com/JonahGroup", "ri-twitter-fill"),
            (
                "LinkedIn",
                "https://www.linkedin.com/company/the-jonah-group/",
                "ri-linkedin-box-fill",
            ),
        ),
    },
)

GALLERY = sorted(
    [i.name for i in root_path.joinpath("content/images/gallery").glob("*.jpg")]
)
