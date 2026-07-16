# CONFIG.MD — stapel-booking

Config registry ({static-scaffold-and-config.md} §2). This composite reads
NO configuration keys of its own — every key belongs to a member module
(calendar, listings (attributes transitively)); see each member's CONFIG.MD (the scaffold aggregates them all
into the generated project's CONFIG.MD automatically).

Scenario defaults live in `stapel_booking.preset.SETTINGS_DEFAULTS` — they are
settings-dict PRESETS for member keys, not new keys.

## stapel-booking

| Key | Source | Purpose | Required | Default |
|-----|--------|---------|----------|---------|
