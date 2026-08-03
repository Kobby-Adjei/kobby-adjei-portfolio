# kobby-adjei.vercel.app

Portfolio. Two case studies, one habit: getting a fuzzy judgement into a form
someone else can apply, disagree with, or prove wrong.

- **The Renovation** — a product UI run as one movement: one thesis, five
  principles, twenty-one logged changes.
- **The Tournament** — a blind evaluation of 23 AI models on clip selection;
  297 candidates judged before model identities were revealed.

## Running it

Static site, no build step.

```bash
python3 -m http.server 4200 --bind 127.0.0.1
```

## Deploying

```bash
vercel deploy --prod --yes
vercel alias set <deployment-url> kobby-adjei.vercel.app
```

## Structure

```
index.html         home
renovation.html    case one
tournament.html    case two
assets/site.css    all styling; one accent per case (rose = craft, blue = measured)
assets/ics.*       img-comparison-slider (MIT) for the before/after wipes
assets/*.jpg       paired before/after frames, matched dimensions, top-anchored
```
