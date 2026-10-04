#!/usr/bin/env python3
"""Discovery Radar scanner scaffold.

Reads a source registry + places atlas, runs the two-pass loop
(check known / hunt unknown), dedupes, verifies, and writes a digest.

Bring your own platform client: implement check_source() and
discover_sources() for wherever your scene lives (Instagram, etc.).
The loop, schema, and verification contract are the framework.

Usage: python3 scan.py --registry registry.yaml --atlas places.yaml --out run/
"""
import argparse, json, os, sys
from datetime import date

try:
    import yaml
except ImportError:
    sys.exit("pip install pyyaml")

TODAY = str(date.today())

# ---- platform hooks: implement these for your source platform ----
def check_source(source):
    """Return list of finding dicts: {title, date, venue, url, section}.
    Read-only. Never follow/like/post."""
    raise NotImplementedError

def discover_sources(area, section, known_handles):
    """Return list of new source dicts (schema/sources.schema.yaml)."""
    raise NotImplementedError

def verify_finding(f):
    """Return True only if date/time/venue check out against the source
    and the event hasn't already happened. When in doubt: False."""
    raise NotImplementedError
# ------------------------------------------------------------------

def load_seen(out):
    p = os.path.join(out, "seen.json")
    return set(json.load(open(p))) if os.path.exists(p) else set()

def save_seen(out, seen):
    json.dump(sorted(seen), open(os.path.join(out, "seen.json"), "w"), indent=1)

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--registry", required=True)
    ap.add_argument("--atlas", required=True)
    ap.add_argument("--out", required=True)
    a = ap.parse_args()
    os.makedirs(a.out, exist_ok=True)

    registry = yaml.safe_load(open(a.registry))
    seen = load_seen(a.out)
    digest = [f"# Discovery Radar digest — {TODAY} ({registry.get('area')})", ""]
    new_sources = []

    for section, sources in registry.get("sections", {}).items():
        digest.append(f"## {section}")
        for s in sources:
            if not s.get("active", True):
                continue
            try:
                findings = check_source(s)
            except NotImplementedError:
                findings = []
            for f in findings:
                fid = f.get("url") or f.get("title")
                if fid in seen:
                    continue
                try:
                    ok = verify_finding(f)
                except NotImplementedError:
                    ok = False
                if not ok:
                    continue  # stale/unverifiable: dropped, never surfaced
                seen.add(fid)
                digest.append(f"- **{f['title']}** — {f.get('date','?')} @ {f.get('venue','?')} ({f.get('url','')})")
        try:
            found = discover_sources(registry.get("area"), section,
                                     [s["handle"] for s in sources])
        except NotImplementedError:
            found = []
        for ns in found:
            ns.setdefault("added", TODAY)
            ns.setdefault("added_by", "auto")
            new_sources.append((section, ns))
        digest.append("")

    if new_sources:
        digest.append("## New sources")
        for section, ns in new_sources:
            digest.append(f"- {ns['handle']} ({section}) — {ns.get('why','')}")
        # merge into registry copy
        for section, ns in new_sources:
            registry["sections"].setdefault(section, []).append(ns)
        yaml.safe_dump(registry, open(os.path.join(a.out, "registry.next.yaml"), "w"),
                       sort_keys=False, allow_unicode=True)

    save_seen(a.out, seen)
    md = "\n".join(digest)
    open(os.path.join(a.out, f"digest-{TODAY}.md"), "w").write(md)
    print(md)

if __name__ == "__main__":
    main()
