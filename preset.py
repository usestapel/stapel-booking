"""Preset for the "booking" scenario — plain data, importable without
Django settings (projections-and-composition §3).

Scenario: bookable resources (coworking, equipment rental, scheduled services): a listing is the resource, calendar carries its availability/slots.

A generated project (stapel-assemble … --libs booking) gets the
same wiring from the STAPEL_LIBS registry; this module is the single source
a hand-written settings.py/urls.py copies from instead.
"""

# Dotted app paths, in mount order. L1 libraries (stapel-attributes) are pip
# dependencies, NOT Django apps — deliberately absent here.
INSTALLED_APPS = [
    "stapel_calendar",
    "stapel_listings",
    "stapel_booking",
]

# (url_prefix, urlconf_module) — mount each one with
#   path(prefix, include(module))
# The composite itself mounts NO urls (http=False): it only carries glue.
URL_INCLUDES = [
    ("calendar/", "stapel_calendar.urls"),
    ("listings/", "stapel_listings.urls"),
]

# Scenario defaults for STAPEL_<MOD> settings dicts. Merge them into the
# project's settings, e.g.:
#   from stapel_booking import preset
#   STAPEL_REVIEWS = {**preset.SETTINGS_DEFAULTS.get("STAPEL_REVIEWS", {})}
SETTINGS_DEFAULTS: dict = {}
