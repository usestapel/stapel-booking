# stapel-booking — docs/capabilities.json surface patch + docs/llms.txt
# emission/drift gate (contract-pipeline.md §2-3).
#
# docs/capabilities.json here is otherwise HAND-WRITTEN (authored in the
# stapel-catalog sweep, commit 7192633 "docs: author capabilities.json for the
# stapel-catalog sweep") — this composite preset mounts no urls and has no
# gate registry, no docs/schema.json, nothing for a codegen step to derive
# provides/axes/extension_points/requires from. `make contract` now patches in
# the two derivable things: module/version from pyproject, and the `surface`
# section (discoverability-design.md §1.2) — the symbols a product is meant to
# CALL instead of writing its own. stapel-booking's surface_roots
# (docs/capabilities.meta.json) is deliberately EMPTY: the composite is
# transparent INSTALLED_APPS/urls/config glue over stapel-calendar +
# stapel-listings and has no permission classes, functions, capability fields
# or templates of its own — so `surface` stays `[]` until that changes. The
# rest of the document stays hand-edited.
#
# Second: docs/llms.txt, the fifth contract artifact (stapel_tools.llms_txt),
# rendered straight from the capabilities.json the step above produces.
#
# PYTHON must have stapel-tools importable (the workspace venv, or
# `pip install stapel-tools`).
PYTHON ?= python3

.PHONY: contract contract-check

contract:
	$(PYTHON) -m stapel_tools.surface . --patch
	$(PYTHON) -m stapel_tools.llms_txt .

# Drift gate: regenerate into a temp dir and diff against the committed docs/llms.txt.
contract-check:
	$(PYTHON) -m stapel_tools.surface . --patch --check
	@tmp=$$(mktemp -d); \
	$(PYTHON) -m stapel_tools.llms_txt . --out "$$tmp" || { rm -rf "$$tmp"; exit 1; }; \
	if ! diff -q docs/llms.txt "$$tmp/llms.txt" >/dev/null 2>&1; then \
		echo "DRIFT: docs/llms.txt is stale — run 'make contract' and commit it"; \
		diff docs/llms.txt "$$tmp/llms.txt" | head -20; \
		rm -rf "$$tmp"; exit 1; \
	fi; \
	rm -rf "$$tmp"; \
	echo "contract-check: docs/llms.txt up to date"
