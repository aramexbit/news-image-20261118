# Build log — news-image-20261118 (NOT submitted)

- Built: 18 Nov 2026 ~08:40–08:50 WIB by builder subagent (parent: main agent).
- Gate verified live before building: competition open, deadline 2026-11-20T00:00:00Z,
  submissionCount 1,541 at build time (was 1,108 at the 08:12 WIB analysis snapshot).
- Facts verified against live news before writing: Reuters/AP/BBC/CNN/IMD/India MEA.
  Corrections vs top-rank consensus applied in the image:
  * Cyclone Akvan: sustained 120–130 km/h, gusts to 145 km/h, landfall Fri 20 Nov noon
    (top rank often wrote "winds to 145" without the gust qualifier).
  * MT Tara Gas: 21 of 24 Indians evacuated, 2 injured in hospital, 1 missing
    (top rank omitted the missing/injured).
  * An-12: toll is the defence ministry's figure (19); some outlets say 17 — attributed.
  * Bahrain: Iran's "hit" on the Sheikh Isa radar is Iran's claim; CENTCOM says intercepted.
- Design: 32 stories. Two BIG painted hero panels (~45% of the page): Kerch Bridge
  collapse (640 px wide) + Bahrain firefight. 8 featured cards, 22 briefs, numbered
  world map (dots 1–10), sources footer. Drawn in code (Pillow), no network.
- Revisions in-session: v1 render → fixed Bahrain deck clipping, flattened Kerch clouds,
  removed Bahrain "sun" glow, spread map dots; v2 → soft semi-transparent smoke.
- Verification:
  * build_entry.py run 2x → identical sha256 225877e8fe3aed3e0b09abb6cf4043b69ad821adabd6b4863d751c2602111793
  * main.py run 2x (MAKEFUN_OUTPUT_DIR) → identical sha256 (same as above)
  * entry.png 1024x1024, 194,312 bytes (<= 1 MiB)
  * Visual check: full image + hero zoom read by builder; all text legible, no
    clipping/overlap; hero dramatic; date + story count correct.
  * makefun check (kit news-image-20261118-kit): 4 passed (competition_open,
    snapshot, license_osi MIT, entrypoint main.py python3.13); 1 failed =
    transcripts_present (expected: transcripts are bundled at submit time from the
    top-level session); 5 checks deferred to submission (repo public/owner/
    created-after-open/commit-in-repo/duplicate — repo IS public, created
    2026-11-18T01:47:47Z after opening, commit pushed).
- Repo: https://github.com/aramexbit/news-image-20261118
  commit 95b50b2f456d12ead8945e3ae99c3e52792f1f3a (main), pushed.
- NOT submitted. Remaining submit-time steps for parent/user: check quota
  (daily/total/can_submit), bundle transcripts, submit, record claim code.
- Honest gaps: hero art is code-painted vector illustration, not a photograph —
  it reads dramatic at full-page scale but stylised up close (smoke/fire are
  flat shapes). Map dots 6/7/8 in Europe and 2/5/9/10 in Asia are close together
  but distinguishable. No local grade exists for this competition (server grades).

## v2 (18 Nov 2026 ~09:00 WIB, NOT submitted)

- User complaint (twice): v1 hero looked flat/cartoonish, LESS realistic than
  the rank-1 example (artch0), and bigger made it worse. Root cause: v1 heroes
  were Pillow-painted shapes (ellipse smoke, spike fire, line bridge).
- Fix: 2 photorealistic hero images generated with the media pipeline (0
  regenerations needed — both first attempts were clean, no text/watermark):
  assets/hero_kerch.jpg (steel arch bridge collapsed into a stormy strait,
  black smoke, fire at the break) and assets/hero_bahrain.jpg (night city,
  orange missile trails, explosions, radar dome foreground). Pasted into the
  hero panels by paste_photo() in build_entry.py (fixed crop, saturation
  1.15x, contrast 1.05x). The v1 painted hero functions (hero_kerch,
  hero_bahrain, smoke, fireburst) were DELETED from build_entry.py.
- main.py v2 now COMPOSES entry.png at runtime from local assets via
  build_entry.build() (no network); falls back to copying the prebuilt
  entry.png if Pillow is unavailable. Footer now discloses: "Hero images
  are AI-generated illustrations."
- Vivid colours: NAVY (8,46,150), RED (238,18,58), GOLD (242,192,28).
  Layout, 32 stories and all verified facts unchanged from v1.
- Verification v2:
  * build_entry.py 2x → identical sha256
    323c1b652b9f85d31eb7cb05c43a2b0bd5dec08b1934de693d94d7394926f219
  * main.py 2x (MAKEFUN_OUTPUT_DIR) → identical sha256 (same as above,
    compose path, not the fallback)
  * entry.png 1024x1024, 705,549 bytes (<= 1 MiB)
  * Visual check by builder: heroes read as photographs, no text/watermark
    inside the photos, all headlines/decks legible, no clipping/overlap,
    date + "32 STORIES" correct.
- Remaining gaps (honest): heroes are AI-generated illustrations, not real
  event photos (disclosed in the footer); Bahrain photo crops the radar dome
  at the left edge (half dome visible — still dramatic); map dots in
  Europe/Asia still cluster (unchanged from v1); featured-story icons are
  still small flat drawings by design. No local grade exists (server grades).
