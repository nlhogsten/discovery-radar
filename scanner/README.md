# Scanner

The run loop. Every run does two passes over every active area × section:

**Pass 1 — check the known.** For each active source, read recent posts/stories
(read-only) for event, meetup, or place signals newer than the last scan.
Snapshot follower counts for velocity tracking.

**Pass 2 — hunt the unknown.** Find *new* sources:
- related/suggested accounts of existing sources,
- hashtag co-occurrence (which accounts post the scene's tags),
- follower overlap (who do two trusted sources both follow),
- velocity outliers *within the area* (a 300-follower account gaining 100 in a
  week in Honolulu matters; raw counts don't transfer across areas).

New sources auto-add with `added_by: auto` and a `why` note. They are never
auto-removed — ratings tune ranking only.

**Verification (non-negotiable).** Every surfaced event is checked against its
source for date, time, venue, and that it hasn't already happened. Stale or
unverifiable items are dropped, never surfaced. (Born from a hallucinated
film screening that made it into a digest once. Never again.)

**Digest.** Per run: new items first (home area first), new sources
discovered, travel-flagged notables. Tight — highlights, not an inventory.

## scan.py

Runnable scaffold. Reads a registry + atlas, iterates areas × sections ×
sources, and calls the two hooks you implement for your source platform
(`check_source` / `discover_sources`). Keeps `seen.json` for dedupe and
writes digest markdown. Bring your own platform client (e.g. an Instagram
reader); the loop, schema, and verification contract are the framework.

Usage: `python3 scanner/scan.py --registry registry.yaml --atlas places.yaml --out run/`
