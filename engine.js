// Trencher Math engine - hypothetical arithmetic on labeled norms only.
// No verdicts about what any trencher can cut through: soil, roots and rock
// are the rental counter's and the manual's call. Always get utilities
// located before any dig.

function plural(n, one, many) { return n === 1 ? one : many; }

function aAn(n) {
  const s = String(n);
  return (n === 11 || n === 18 || s.startsWith("8")) ? "An" : "A";
}

function fixed1(x) { return (Math.floor(x * 10 + 0.5) / 10).toFixed(1); }

function trenchHours(length, claim) {
  if (!(length > 0)) throw new Error("the trench length must be above zero");
  if (!(claim > 0)) throw new Error("the claimed feet per hour must be above zero");
  return length / claim;
}

function trenchTruth(length, claim) {
  const hours = trenchHours(length, claim);
  let verdict;
  if (hours <= 1) verdict = "done before lunch";
  else if (hours <= 3) verdict = "a working morning";
  else if (hours <= 6) verdict = "an honest afternoon";
  else verdict = "a two-day rental honestly";
  return `The trencher claims ${claim} feet an hour; your ${length}-foot run is ${fixed1(hours)} ${plural(hours === 1 ? 1 : 0, "hour", "hours")} - ${verdict}.`;
}

function spoilCubicFeet(length, width, depth) {
  if (!(length > 0)) throw new Error("the trench length must be above zero");
  if (!(width > 0)) throw new Error("the width must be above zero");
  if (!(depth > 0)) throw new Error("the depth must be above zero");
  return length * (width / 12) * (depth / 12);
}

function spoilTruth(length, width, depth, barrow) {
  if (!(barrow > 0)) throw new Error("the barrow size must be above zero");
  const spoil = spoilCubicFeet(length, width, depth);
  const loads = Math.ceil(spoil / barrow);
  let verdict;
  if (loads <= 5) verdict = "a few trips with the barrow";
  else if (loads <= 15) verdict = "a working pile";
  else if (loads <= 40) verdict = "a mountain honestly";
  else verdict = "call it a second pile";
  return `${aAn(length)} ${length}-foot trench ${width} ${plural(width, "inch", "inches")} wide and ${depth} ${plural(depth, "inch", "inches")} deep lifts about ${fixed1(spoil)} cubic feet of spoil - ${loads} ${plural(loads, "barrow load", "barrow loads")} of ${barrow} cubic feet, ${verdict}.`;
}

function clockText(start, hours) {
  const totalMinutes = Math.floor(start * 60 + hours * 60 + 0.5);
  const h24 = Math.floor(totalMinutes / 60) % 24;
  const m = totalMinutes % 60;
  const suffix = h24 >= 12 ? "PM" : "AM";
  const h12 = h24 % 12 === 0 ? 12 : h24 % 12;
  return `${h12}:${String(m).padStart(2, "0")} ${suffix}`;
}

function daylightTruth(start, length, claim) {
  if (!(start >= 0 && start < 24)) throw new Error("the start hour must be between 0 and 24");
  const hours = trenchHours(length, claim);
  const finish = clockText(start, hours);
  const endHour = start + hours;
  let verdict;
  if (endHour <= 12) verdict = "morning coffee is safe";
  else if (endHour <= 17) verdict = "home for dinner";
  else verdict = "a headlamp job honestly";
  return `Starting at ${clockText(start, 0)} with ${fixed1(hours)} ${plural(hours === 1 ? 1 : 0, "hour", "hours")} of trenching puts the last scoop down at about ${finish} - ${verdict}.`;
}

if (typeof module !== "undefined") {
  module.exports = { trenchHours, trenchTruth, spoilCubicFeet, spoilTruth, clockText, daylightTruth };
}
