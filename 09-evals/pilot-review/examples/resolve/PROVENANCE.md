# Resolve snapshot provenance

The [published report](published-report.json) is copied byte for byte from
[`evals/latest_report.json` at revision 074246e](https://github.com/ellehelvig/peopleops-resolution-agent/blob/074246e4e026e310e16616b11b44f3fe73cd5a59/evals/latest_report.json).
Its SHA-256 is `d05c639ab7c424aff0fecc5c6a8cd53e17ee184d8d78aa6efa50bca3d548c114`.
The [original MIT license](https://github.com/ellehelvig/peopleops-resolution-agent/blob/074246e4e026e310e16616b11b44f3fe73cd5a59/LICENSE)
is copyright 2026 Elle Helvig, also the owner of this playbook.

The report was generated on 24 September 2026. It records 60 of 60 baseline cases
and 0 of 16 developer-authored synthetic paraphrases passing. Five paraphrase
cases concern missed Employee Relations or legal routing. These are recorded test
outcomes, not a measured rate of employee harm or general field accuracy.

`routing.json` wraps those JSON data in the pilot-review artifact contract.
`packet.json` references that wrapper's exact hash, source revision, observation
date, dataset ID, and method ID. The wrapper does not refresh the observation
date or establish independent validation. The local adapter rechecks count
consistency and keeps the failures visible. Other required criteria are absent.

At the documented 3 November 2026 review date, the preserved report is older than
the demonstration policy's 30-day limit. It cannot produce an eligible result,
even if its familiar regression cases pass.

No live model was called and no recorded result was improved for this example.
The fictional requests in the report were already public in the source project.
