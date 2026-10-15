# Trencher Math

Honest trenching arithmetic. The spec sheet claims a hundred feet an hour; Trencher Math divides,
multiplies and tells you what the clock says when the last scoop lands.

## What it does

Three panels of hypothetical arithmetic on labeled norms:

- **The trench truth** - your run vs. the claimed feet per hour: the honest hours.
- **The spoil truth** - length, width and depth into cubic feet and wheelbarrow loads.
- **The daylight truth** - start hour plus honest hours into a finish time, judged as a day.

## The boundary

Trencher Math keeps schedule, spoil and daylight arithmetic only. It gives no verdicts about what
any trencher can cut through - soil, roots and rock are the rental counter's and the manual's
call. Always have utilities located before any dig: in the US call 811, elsewhere call your local
before-you-dig line. Every figure is hypothetical arithmetic on labeled norms, not a statement
about any real machine or jobsite.

## Files

- `index.html` - landing page
- `app.html` - the app
- `engine.js` - the arithmetic (shared by the page and the tests)
- `oracle.py` - a Python mirror of the engine, float for float
- `expected.json` - oracle output for its inline cases
- `test.js` - runs the engine against `expected.json`

## Test

```
python3 oracle.py   # regenerates expected.json from its inline cases
node test.js        # 29 cases / 29 checks
```

Live at https://ilanis-agent.github.io/trenchermath/
