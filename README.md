# stapel-booking

Composite: bookable resources — calendar + listings.

## Assemble (one line)

```bash
pip install stapel-tools
stapel-assemble mybooking --libs booking
cd mybooking && make test
```

That expands `booking` through the STAPEL_LIBS `requires`
closure and wires every member module into INSTALLED_APPS,
requirements.txt, urls.py and CONFIG.MD, then runs the verify gates.

## Manual wiring (no scaffold)

```python
# settings.py
from stapel_booking import preset

INSTALLED_APPS = [
    # ... django/stapel-core baseline (incl. stapel_core.django.projections)
    "stapel_calendar",
    "stapel_listings",
    "stapel_booking",
]
for _k, _v in preset.SETTINGS_DEFAULTS.items():
    globals().setdefault(_k, _v)

# urls.py
from django.urls import include, path

urlpatterns = [
    path("calendar/", include("stapel_calendar.urls")),
    path("listings/", include("stapel_listings.urls")),
]
```

## Config checklist (fill these, in the generated project's CONFIG.MD too)

| Key | Note |
|-----|------|
| `STAPEL_CALENDAR[...]` | presets/slots — see stapel-calendar CONFIG.MD |
| `STAPEL_LISTINGS["BASE_CURRENCY"]` | default `USD` — set your currency |
| `STAPEL_LISTINGS["DEFAULT_LISTING_TTL_DAYS"]` | default 30 (a bookable resource usually wants `None`) |
