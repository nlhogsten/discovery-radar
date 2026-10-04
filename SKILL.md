# discovery-radar skill

Personal event-and-place discovery for people "not in the network."
Full framework in this repo; your registry (actual accounts, ratings)
lives in your workspace, never here.

## The loop

Every run, per active area × interest section:

1. **Check the known** — read recent posts/stories of registry sources
   (read-only: never follow, like, DM, or post) for new event/meetup/place
   signals. Snapshot follower counts for velocity.
2. **Hunt the unknown** — related accounts, hashtag co-occurrence, follower
   overlap, within-area velocity outliers. Auto-add with `added_by: auto`.
3. **Verify** — date, time, venue checked against the source; event must not
   have happened already. Stale/unverifiable items are dropped, never surfaced.
4. **Digest** — new items first (home area first), then new sources discovered.
   Tight: highlights, not an inventory.

## Files

- `schema/sources.schema.yaml` — registry schema with annotated example
- `schema/places.schema.yaml` — places atlas schema with annotated example
- `scanner/scan.py` — runnable scaffold; implement `check_source`,
  `discover_sources`, `verify_finding` for your platform
- `dashboard/README.md` — how a dashboard attaches as container

## Rules

- Ratings tune ranking; sources are never auto-removed.
- Growth is normalized within-area, never by raw counts.
- No personal data in this repo. Ever.
