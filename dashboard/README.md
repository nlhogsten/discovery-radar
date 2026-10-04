# Dashboard attachment contract

Discovery Radar is a standalone system (this repo). The dashboard is a
*container*: it renders the radar, it doesn't own it.

The dashboard project for a radar area shows:

- **Radar** — findings feed per interest section. This is the hero: analysis of
  specific events/things happening, not a directory. Empty until the first scan.
- **Sources** — the registry, browsable per section: handle, type, followers,
  velocity, confidence, rating. The network you're building, visible.
- **Places** — a *subcategory*: the evergreen atlas (work/eat/visit) under the
  radar, not a peer of sources.
- **Areas** — per-area separation, on/off toggles, add-area flow.
- **Ratings** — 👍/👎 on findings, sources, and places. Ratings tune scores;
  nothing is ever auto-removed.
- **Digests** — scan history.

The registry YAML in the user's workspace is canonical; the dashboard keeps a
synced store for rendering. The twice-weekly scan job writes to both.
