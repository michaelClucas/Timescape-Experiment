# Output contract

Runs write `OUTPUT.json` alongside the prose `OUTPUT.md`. Prose is for
reading, JSON is for comparing runs mechanically. They must agree; prose
is authoritative, and any divergence is a review finding.

## Schema (informal)

```json
{
  "run": "01-audit-derivation-chain",
  "model": "string",
  "date": "YYYY-MM-DD",
  "scaffold_version": "v0",

  "chain": [
    {
      "id": "D6",
      "statement": "string",
      "kind": "THEOREM|SCHEME|POSTULATE|FIT|INTERPRETATION",
      "kind_confidence": "SOURCED|LEAD|INFERENCE|UNKNOWN",
      "kind_disagrees_with_seed": true,
      "support": [{ "locator": "arXiv:xxxx.xxxxx", "section": "string" }],
      "strongest_objection": "O2",
      "if_this_fails": "string: how much of the conclusion collapses",
      "weight": 1
    }
  ],

  "ledger": [
    {
      "id": "C3",
      "statement": "string",
      "source": { "locator": "string", "section": "string" },
      "dataset": "string, with release and cuts",
      "n_objects": 0,
      "method": "string, including standardisation treatment",
      "free_params": { "timescape": 0, "comparison_model": 0 },
      "comparison": { "statistic": "string", "value": 0,
                      "interpretation_scale": "string" },
      "systematics": ["string"],
      "responses": [{ "locator": "string", "position": "string" }],
      "status": "supported|contested|superseded|untested|unverified-in-this-run",
      "status_changer": "string"
    }
  ],

  "objections": [
    {
      "id": "O1",
      "attacks": "D4",
      "position_a": { "holders": ["string"], "claim": "string",
                      "key_assumption": "string", "sources": [] },
      "position_b": { "holders": ["string"], "claim": "string",
                      "key_assumption": "string", "sources": [] },
      "turns_on": "string: what the disagreement actually turns on",
      "resolved": false,
      "resolution_note": "string, required when resolved is true"
    }
  ],

  "rivals": [
    { "name": "string", "mechanism": "string",
      "differs_from_timescape_in": "string",
      "constraint_status": "string", "sources": [] }
  ],

  "discriminating_measurements": [
    { "observable": "string", "timescape_predicts": "string",
      "rival_predicts": "string", "rival": "string",
      "current_precision": "string", "needed_precision": "string",
      "already_decided": false }
  ],

  "seed_corrections": [
    { "file": "docs/derivation-chain.md", "item": "D5",
      "was": "string", "should_be": "string", "sources": [] }
  ],

  "open_questions": [
    { "question": "string", "why_it_matters": "string",
      "what_would_settle_it": "string", "priority": 1 }
  ],

  "unverified_leads": [ { "claim": "string", "needed": "string" } ]
}
```

## Rules

- `weight` on a chain step is 0-3: how much of the conclusion depends on
  it. The distribution of weight across the chain is the main result of
  Run 01, so fill it for every step.
- `free_params` is required in every ledger entry that has a `comparison`.
  Set either side to `null` only if the count genuinely could not be
  established, and then say so in `status`.
- `objections[].resolved` defaults to `false`. Setting it `true` requires
  `resolution_note` with a locator showing the field resolved it, not the
  run's own judgement.
- `seed_corrections` being non-empty is a good sign. The seed docs were
  written without retrieval and are expected to be wrong in places.
- Extension proposals do not belong in this schema. They have their own
  contract in `EXTENSION-RULES.md` and their own run numbers.
