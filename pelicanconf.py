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

# Pretty URLs - Will also have to update link to privacy-policy in themes/healthfocus/templates/base.html
# PAGE_URL = "{slug}"
# PAGE_SAVE_AS = "{slug}/index.html"
PAGE_URL = "{slug}.html"
PAGE_SAVE_AS = "{slug}.html"

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
    (
        "The Physician Alliance",
        "client-7.png",
        "https://thephysicianalliance.org/",
    ),    
)

TEAM = (
    {
        "name": "James W. Morris",
        "title": "Chief Executive Officer",
        "img": "james.jpg",
        "description": "James has worked in pharmaceutical, urgent care, and physician organization settings as a technologist and technical director.",
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
        "description": "Deb has extensive management experience working with physician organizations and directly with practice units.",
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
        "description": "Michael has worked as a developer and manager on both the insurance and physician organization sides.",
        "social": (
            (
                "LinkedIn",
                "https://www.linkedin.com/in/michaeldavidwilson/",
                "ri-linkedin-box-fill",
            ),
        ),
    },
    {
        "name": "James Malayang",
        "title": "Customer Success Manager",
        "img": "",
        "description": "James is our newest member of the Health Focus team. He has a background in healthcare project management and"
        " will be working to ensure that our customers' needs are addressed promptly.",
        "social": (
            (
                "LinkedIn",
                "https://www.linkedin.com/in/james-malayang-150bba17/",
                "ri-linkedin-box-fill",
            ),
        ),
    },
    {
        "name": "Timothy Potvin",
        "title": "Database Developer",
        "img": "",
        "description": "Tim works closely with our team during QC cycles to improve data mapping and integrity.",
        "social": (
            (
                "LinkedIn",
                "https://www.linkedin.com/in/timothy-potvin-7a7547219/",
                "ri-linkedin-box-fill",
            ),
        ),
    },
    {
        "name": "Ralph Luis",
        "title": "Database Developer",
        "img": "",
        "description": "Ralph supports and maintains the many data interfaces feeding the Health Focus warehouses.",
        "social": (
            (
                "LinkedIn",
                "https://www.linkedin.com/in/ralph-luis-4b8a307b/",
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

LOAD_CONTENT_CACHE = False
DIRECT_TEMPLATES = ['index']