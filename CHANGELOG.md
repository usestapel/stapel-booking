# Changelog

## [0.1.4] - 2026-08-02

Packaging / contract only. Patch.

### Added
- `docs/llms.txt` — the fifth contract artifact — is now emitted, drift-gated
  by `make contract`/`contract-check`, and badged in the README.
  `docs/capabilities.json` remains hand-written (stapel-catalog sweep); these
  targets manage only `docs/llms.txt` and never touch `capabilities.json`.
  This composite preset has no axes/surface/extension_points at all, so the
  generated llms.txt is just header + "Fits with" — thin but honest.
- Canonical `ci.yml` with coverage, `codecov.yml`, Python 3.14 classifier,
  badge canon (this repo has never published to PyPI, so badges are the
  truncated license+status set with an honest install-from-source line).

### Fixed
- `docs/capabilities.json`'s hand-maintained `version` field had drifted to
  `0.1.2` (missed the 0.1.3 bump); corrected to match `pyproject.toml`.
  Content unchanged.
- `docs/llms.txt`/`docs/capabilities.json`/`docs/flows.json`/`docs/errors.json`/
  `CONFIG.MD` are now listed in `package-data` so they ship in the wheel.

## [0.1.2] - 2026-07-17

Fleet follow-up to stapel-core 0.12.0 (legacy shim sweep). Also re-pins
`stapel-attributes`'s ceiling — it had a breaking bump to 0.4.0 since
0.1.1, outside this composite's old `<0.4` ceiling. Suite green.

### Changed
- `stapel-core` ceiling `<0.12` → `<0.13`.
- `stapel-attributes` ceiling `<0.4` → `<0.5`.

## [0.1.1] - 2026-07-17

### Changed
- `stapel-core` ceiling raised `>=0.10,<0.11` → `>=0.10,<0.12` (core 0.11
  fleet re-pin). Member-module pins (calendar, listings, attributes)
  already satisfied by their own 0.11-fleet patch releases. Suite green
  as-is.

## [0.1.0] - 2026-07-16

### Added

- Initial composite (projections-and-composition §3): pyproject pins over
  the member modules, `preset` (INSTALLED_APPS/urls/STAPEL_* defaults),
  AppConfig app slot, minimal tests.
