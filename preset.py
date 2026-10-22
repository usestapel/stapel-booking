"""Preset for the "booking" scenario — plain data, importable without
Django settings (projections-and-composition §3).

Scenario: bookable resources (coworking, equipment rental, scheduled services): a listing is the resource, calendar carries its availability/slots.

A generated project (stapel-assemble … --libs booking) gets the
same wiring from the STAPEL_LIBS registry; this module is the single source
a hand-written settings.py/urls.py copies from instead.
"""

# Dotted app paths, in mount order. L1 libraries (stapel-attributes) are pip
# dependencies, NOT Django apps — deliberately absent here.
#
# stapel_categories is a member, not an option: publishing a listing calls the
# ``categories.features`` comm Function (STAPEL_LISTINGS
# CATEGORY_FEATURES_FUNCTION), and without a provider every publish answers
# 500. A resource is still a listing in a category.
INSTALLED_APPS = [
    "stapel_calendar",
    "stapel_categories",
    "stapel_listings",
    "stapel_booking",
]

# (url_prefix, urlconf_module) — mount each one with
#   path(prefix, include(module))
# The composite itself mounts NO urls (http=False): it only carries glue.
#
# stapel-categories and stapel-listings contribute only ``v1/`` and expect the
# host to supply ``<mod>/api/`` (the canon every client calls); calendar bakes
# ``api/v1/`` in itself. The stapel-tools registry mounts the same prefixes
# (stapel-preset-gate).
URL_INCLUDES = [
    ("calendar/", "stapel_calendar.urls"),
    ("categories/api/", "stapel_categories.urls"),
    ("listings/api/", "stapel_listings.urls"),
]

# Scenario defaults for STAPEL_<MOD> settings dicts. Merge them into the
# project's settings, e.g.:
#   from stapel_booking import preset
#   STAPEL_REVIEWS = {**preset.SETTINGS_DEFAULTS.get("STAPEL_REVIEWS", {})}
SETTINGS_DEFAULTS: dict = {
    "STAPEL_LISTINGS": {
        # stapel-listings defaults to MODERATION_GATE "pre": a published
        # listing waits for a moderation.completed verdict. This scenario
        # installs no stapel-moderation, so nothing would ever deliver one and
        # every resource would stay PENDING, never bookable. A host that adds
        # moderation sets this back to False.
        "AUTO_APPROVE_ON_PUBLISH": True,
    },
}
