import math, json

def plural(n, one, many):
    return one if n == 1 else many

def a_an(n):
    s = str(n)
    return "An" if (n == 11 or n == 18 or s.startswith("8")) else "A"

def fixed1(x):
    return f"{math.floor(x * 10 + 0.5) / 10:.1f}"

def trench_hours(length, claim):
    if not (length > 0):
        raise ValueError("the trench length must be above zero")
    if not (claim > 0):
        raise ValueError("the claimed feet per hour must be above zero")
    return length / claim

def trench_truth(length, claim):
    hours = trench_hours(length, claim)
    if hours <= 1:
        verdict = "done before lunch"
    elif hours <= 3:
        verdict = "a working morning"
    elif hours <= 6:
        verdict = "an honest afternoon"
    else:
        verdict = "a two-day rental honestly"
    return f"The trencher claims {claim} feet an hour; your {length}-foot run is {fixed1(hours)} {plural(1 if hours == 1 else 0, 'hour', 'hours')} - {verdict}."

def spoil_cubic_feet(length, width, depth):
    if not (length > 0):
        raise ValueError("the trench length must be above zero")
    if not (width > 0):
        raise ValueError("the width must be above zero")
    if not (depth > 0):
        raise ValueError("the depth must be above zero")
    return length * (width / 12) * (depth / 12)

def spoil_truth(length, width, depth, barrow):
    if not (barrow > 0):
        raise ValueError("the barrow size must be above zero")
    spoil = spoil_cubic_feet(length, width, depth)
    loads = math.ceil(spoil / barrow)
    if loads <= 5:
        verdict = "a few trips with the barrow"
    elif loads <= 15:
        verdict = "a working pile"
    elif loads <= 40:
        verdict = "a mountain honestly"
    else:
        verdict = "call it a second pile"
    return f"{a_an(length)} {length}-foot trench {width} {plural(width, 'inch', 'inches')} wide and {depth} {plural(depth, 'inch', 'inches')} deep lifts about {fixed1(spoil)} cubic feet of spoil - {loads} {plural(loads, 'barrow load', 'barrow loads')} of {barrow} cubic feet, {verdict}."

def clock_text(start, hours):
    total_minutes = math.floor(start * 60 + hours * 60 + 0.5)
    h24 = (total_minutes // 60) % 24
    m = total_minutes % 60
    suffix = "PM" if h24 >= 12 else "AM"
    h12 = 12 if h24 % 12 == 0 else h24 % 12
    return f"{h12}:{m:02d} {suffix}"

def daylight_truth(start, length, claim):
    if not (0 <= start < 24):
        raise ValueError("the start hour must be between 0 and 24")
    hours = trench_hours(length, claim)
    finish = clock_text(start, hours)
    end_hour = start + hours
    if end_hour <= 12:
        verdict = "morning coffee is safe"
    elif end_hour <= 17:
        verdict = "home for dinner"
    else:
        verdict = "a headlamp job honestly"
    return f"Starting at {clock_text(start, 0)} with {fixed1(hours)} {plural(1 if hours == 1 else 0, 'hour', 'hours')} of trenching puts the last scoop down at about {finish} - {verdict}."

FNS = {"trenchTruth": trench_truth, "spoilTruth": spoil_truth, "daylightTruth": daylight_truth}

cases = [
 {"fn":"trenchTruth","args":[80,100]},
 {"fn":"trenchTruth","args":[100,100]},
 {"fn":"trenchTruth","args":[250,100]},
 {"fn":"trenchTruth","args":[500,100]},
 {"fn":"trenchTruth","args":[800,100]},
 {"fn":"trenchTruth","args":[120,60]},
 {"fn":"trenchTruth","args":[0,100]},
 {"fn":"trenchTruth","args":[80,0]},
 {"fn":"spoilTruth","args":[80,6,18,3]},
 {"fn":"spoilTruth","args":[10,4,12,3]},
 {"fn":"spoilTruth","args":[30,6,12,3]},
 {"fn":"spoilTruth","args":[100,8,24,3]},
 {"fn":"spoilTruth","args":[300,8,24,3]},
 {"fn":"spoilTruth","args":[80,1,1,3]},
 {"fn":"spoilTruth","args":[80,6,18,6]},
 {"fn":"spoilTruth","args":[0,6,18,3]},
 {"fn":"spoilTruth","args":[80,0,18,3]},
 {"fn":"spoilTruth","args":[80,6,0,3]},
 {"fn":"spoilTruth","args":[80,6,18,0]},
 {"fn":"daylightTruth","args":[9,80,100]},
 {"fn":"daylightTruth","args":[8,250,100]},
 {"fn":"daylightTruth","args":[13,500,100]},
 {"fn":"daylightTruth","args":[15,800,100]},
 {"fn":"daylightTruth","args":[10,120,60]},
 {"fn":"daylightTruth","args":[6,50,100]},
 {"fn":"daylightTruth","args":[-1,80,100]},
 {"fn":"daylightTruth","args":[24,80,100]},
 {"fn":"daylightTruth","args":[9,0,100]},
 {"fn":"daylightTruth","args":[9,80,0]}
]

out = []
for c in cases:
    try:
        out.append({"fn": c["fn"], "args": c["args"], "out": FNS[c["fn"]](*c["args"])})
    except ValueError as e:
        out.append({"fn": c["fn"], "args": c["args"], "err": str(e)})
json.dump(out, open("expected.json", "w"), indent=1)
print(f"{len(out)} cases")
