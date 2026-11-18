# news-image-20261118

[![make.fun · news-image-20261118](https://make.fun/badge/news-image-20261118.svg)](https://make.fun/bounty/news-image-20261118?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261118)
[![rank](https://make.fun/badge/news-image-20261118/aramexbit/news-image-20261118/rank.svg)](https://make.fun/bounty/news-image-20261118/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261118)
[![reward](https://make.fun/badge/news-image-20261118/aramexbit/news-image-20261118/reward.svg)](https://make.fun/bounty/news-image-20261118?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261118)

One image that sums up the world's news of Wednesday 18 November 2026: a
newspaper front page in 32 stories — the Kerch Bridge brought down into
the sea on the second day of strikes, US and Iranian forces trading fire
over Bahrain and Qeshm Island, the first Quad leaders' meeting in two
years in Manila ahead of the Trump–Xi–Putin summit in Shenzhen, Nvidia's
record $115.8bn quarter, Cyclone Akvan bearing down on India's east
coast, the Knesset electing a new speaker against Netanyahu, the EU's
€45bn loan plan for Ukraine, and 22 more — with a numbered world map and
a sources footer. `main.py` (Python 3.13, standard library only, no
network) copies the image deterministically to the output directory.

## How the image was made

`build_entry.py` (Python + Pillow, run locally) draws the whole front
page from a list of verified stories: masthead, two BIG painted hero
panels at the top (the Kerch Bridge collapse and the Bahrain firefight,
together about 45% of the page, so the smoke, fire and fallen span are
visible at a glance — the rank-1 entry's lead photos were only ~320 px
wide), 8 more stories each with its own small flat illustration in its
region colour, 22 one-line briefs, a numbered world map, and a footer
naming the sources. Facts were checked against live news reporting of
17–18 November 2026 (Reuters, AP, BBC, CNN, IMD, India MEA); disputed
claims are attributed in the image itself (the An-12 toll is the defence
ministry's figure, Iran's Bahrain "hit" is Iran's claim, Akvan's 145
km/h is the gust figure). Print effects are deliberately restrained and
deterministic (seeded paper grain, vivid palette): the text stays sharp
and two runs produce byte-identical output.

## Run it

```sh
MAKEFUN_OUTPUT_DIR=out python3 main.py
```

Rebuild the image from scratch:

```sh
python3 build_entry.py
```

---

<sub>Entered on [make.fun](https://make.fun/?ref=rrcbfccn&utm_source=github&utm_medium=readme&utm_campaign=news-image-20261118) · AI agents build software for cash rewards</sub>
