# Discovery Radar

A personal event-and-place discovery system for people who are "not in the network."

The problem: the interesting stuff — underground shows, small art openings, run clubs, tech meetups, good work cafes — is announced on Instagram stories 24–72 hours out by accounts you'd never find through search. Crawlers can't see it. Aggregators don't list it. The network *is* the discovery mechanism, and if you're not in it, you're out.

Discovery Radar builds the network for you:

- **Source registry** — venues, crews, promoters, DJs, organizers, hashtags. Organizations *and* individuals. Each with type, confidence, follower-velocity tracking, and a rating score.
- **Two passes, every run** — (1) check known sources for new event/place signals; (2) hunt for *new* sources via related accounts, hashtag co-occurrence, and within-area velocity outliers. New sources auto-add; the registry is a living thing.
- **Ratings, not removals** — you rate *findings*; ratings tune ranking. A source is never auto-removed (it may post something you like next month).
- **Places atlas** — evergreen work/eat/visit guide (work cafes carry laptop-camping verdicts). Built once, refreshed by the same runs.
- **Verification rule** — every surfaced event is checked against its source for date, time, venue, and that it hasn't already happened. Stale or unverifiable items are dropped, never surfaced.
- **Areas** — scoped per area (city/island), each toggleable. Growth is normalized *within* an area: a 2k-follower account can be a primary scene node in Honolulu and a nobody in Tokyo.

No personal data ships in this repo. Your registry (the actual accounts, your ratings) lives in your own workspace; this is the framework.

Built with [Muse](https://muse.ai) as a Muse-usable skill. MIT licensed, copyright Nate Hogsten.
