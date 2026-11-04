#!/usr/bin/env python3
"""Check an audit run's OUTPUT.json against protocol/output-schema.md.

    python protocol/validate.py runs/<run>/OUTPUT.json

Exits 0 when clean, 1 when any rule fails. It checks only whether the
contract was followed, never whether a claim is true. A file can pass this
and still be worthless; that is what the adversary role is for.

The rule this exists for is C5. `docs/claim-ledger.md` says a comparison
statistic is uninterpretable without the free-parameter count on both
sides, and that is the rule most often broken in the literature this
repository audits. It is also the one no reader checks by eye, because the
statistic is right there and looks like a result.
"""

import json
import re
import sys
from collections import Counter

KINDS = {"THEOREM", "SCHEME", "POSTULATE", "FIT", "INTERPRETATION"}
CONF = {"SOURCED", "LEAD", "INFERENCE", "UNKNOWN"}
STATUS = {"supported", "contested", "superseded", "untested",
          "unverified-in-this-run"}
# Wording that marks a statistic as not usable as a result.
UNINTERPRETABLE = ("uninterpretable", "not applicable", "none computed",
                   "none -", "none;", "no chi-squared", "not a timescape")
# An objection may attack the programme as a whole rather than one step.
PROGRAMME = re.compile(r"^\s*(the\s+)?programme\s*$", re.I)
LOCATOR = re.compile(r"(arXiv:|doi|10\.\d{4}/)", re.I)


def seq(x):
    return x if isinstance(x, list) else []


def text(x):
    return x if isinstance(x, str) else ""


def marked_uninterpretable(comp):
    """True when the entry itself says the statistic is not usable."""
    blob = " ".join(text(comp.get(k)).lower()
                    for k in ("statistic", "interpretation_scale"))
    return any(p in blob for p in UNINTERPRETABLE)


class Report:
    def __init__(self):
        self.fail = []
        self.note = []

    def bad(self, rule, where, detail):
        self.fail.append((rule, where, detail))


def check(doc, rep):
    chain = seq(doc.get("chain"))
    ledger = seq(doc.get("ledger"))
    objs = seq(doc.get("objections"))

    chain_ids = {s.get("id") for s in chain if s.get("id")}
    obj_ids = {o.get("id") for o in objs if o.get("id")}

    # ---- chain ----
    for i, s in enumerate(chain):
        sid = s.get("id") or "chain[%d]" % i
        if s.get("kind") not in KINDS:
            rep.bad(1, sid, "kind %r not in %s" % (s.get("kind"), sorted(KINDS)))
        if s.get("kind_confidence") not in CONF:
            rep.bad(2, sid, "kind_confidence %r not in %s"
                    % (s.get("kind_confidence"), sorted(CONF)))
        w = s.get("weight")
        if not isinstance(w, int) or not 0 <= w <= 3:
            rep.bad(3, sid, "weight %r is not an integer 0-3" % (w,))
        if not text(s.get("if_this_fails")).strip():
            rep.bad(4, sid, "no if_this_fails: a weight with no account of what collapses")
        if s.get("kind") == "THEOREM" and not seq(s.get("support")):
            rep.bad(5, sid, "THEOREM with no support; a theorem claim needs its source")
        so = s.get("strongest_objection")
        if so and so not in obj_ids:
            rep.bad(6, sid, "strongest_objection %r names no objection" % so)

    for sid, n in Counter(s.get("id") for s in chain).items():
        if n > 1:
            rep.bad(7, str(sid), "chain id appears %d times" % n)

    # ---- ledger: C5, the rule this file exists for ----
    for i, e in enumerate(ledger):
        eid = e.get("id") or "ledger[%d]" % i
        comp = e.get("comparison") or {}
        fp = e.get("free_params") or {}
        st = e.get("status")

        if st not in STATUS:
            rep.bad(8, eid, "status %r not in %s" % (st, sorted(STATUS)))
        if not text(e.get("statement")).strip():
            rep.bad(9, eid, "no statement")

        if comp:
            if "free_params" not in e:
                rep.bad(10, eid, "has a comparison but no free_params block")
            else:
                missing = [k for k in ("timescape", "comparison_model")
                           if fp.get(k) is None]
                has_value = comp.get("value") is not None
                if missing and has_value and not marked_uninterpretable(comp):
                    rep.bad(11, eid,
                            "C5: reports value %r with %s null and the statistic "
                            "not marked uninterpretable"
                            % (comp.get("value"), " and ".join(missing)))
        if not text(e.get("dataset")).strip() and comp.get("value") is not None:
            rep.bad(12, eid, "reports a value with no dataset recorded")
        if st == "supported":
            if not seq(e.get("responses")):
                rep.bad(13, eid,
                        "status 'supported' with no responses recorded; "
                        "EVIDENCE-RULES requires confirmation from outside "
                        "the proposing group")

    # ---- objections ----
    for i, o in enumerate(objs):
        oid = o.get("id") or "objections[%d]" % i
        att = o.get("attacks")
        if att and att not in chain_ids and not PROGRAMME.match(text(att)):
            rep.bad(14, oid,
                    "attacks %r names no chain step, and is not the reserved "
                    "value 'programme'" % att)
        if o.get("resolved") is True and not text(o.get("resolution_note")).strip():
            rep.bad(15, oid, "resolved with no resolution_note")
        if o.get("resolved") is True:
            # The note may point at locators recorded elsewhere in the entry
            # ("with locators above"), so search the whole objection.
            if not LOCATOR.search(json.dumps(o)):
                rep.bad(16, oid,
                        "resolved with no locator anywhere in the entry; the "
                        "schema requires showing the field resolved it")
        for side in ("position_a", "position_b"):
            p = o.get(side) or {}
            if not text(p.get("key_assumption")).strip():
                rep.bad(17, "%s.%s" % (oid, side),
                        "no key_assumption: the disagreement's load-bearing "
                        "assumption is the point of the entry")

    # ---- counts ----
    counts = doc.get("counts")
    if counts:
        actual = {"chain": len(chain), "ledger": len(ledger),
                  "objections": len(objs),
                  "rivals": len(seq(doc.get("rivals"))),
                  "discriminating_measurements":
                      len(seq(doc.get("discriminating_measurements")))}
        for k, want in actual.items():
            if k in counts and counts[k] != want:
                rep.bad(18, "counts." + k,
                        "declared %r, actual %d" % (counts[k], want))

    rep.note.append("chain %d  (%s)" % (
        len(chain), ", ".join("%s %d" % (k, v) for k, v in
                              sorted(Counter(s.get("kind") for s in chain).items()) if k)))
    rep.note.append("weights: " + ", ".join(
        "%s=%s" % (s.get("id"), s.get("weight")) for s in chain))
    rep.note.append("ledger %d  (%s)" % (
        len(ledger), ", ".join("%s %d" % (k, v) for k, v in
                               sorted(Counter(e.get("status") for e in ledger).items()) if k)))
    rep.note.append("objections %d, resolved %d" % (
        len(objs), sum(1 for o in objs if o.get("resolved"))))


def main(argv):
    if len(argv) != 2:
        print(__doc__)
        return 2
    with open(argv[1], encoding="utf-8") as fh:
        doc = json.load(fh)

    rep = Report()
    check(doc, rep)

    for n in rep.note:
        print("   " + n)

    if rep.fail:
        print("\nVIOLATIONS (%d)" % len(rep.fail))
        for rule, where, detail in sorted(rep.fail, key=lambda x: (x[0], str(x[1]))):
            print("  rule %-2d  %-22s %s" % (rule, where, detail))
        print("\nFAIL: %d violations" % len(rep.fail))
        return 1

    print("\nPASS: no violations")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
