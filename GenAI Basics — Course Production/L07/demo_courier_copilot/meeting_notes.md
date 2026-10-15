# Meeting: Prime delivery rule

Date: 5 October 2026 (Monday)
Participants: Anna (product), Pavel (developer), Ola (support)

Decisions
- Prime subscribers get free delivery from a $75 order inside the city zone.
- Free delivery from $100 stays for everyone.
- Deliveries outside the zone do not change.
- Release behind a feature flag first; Ola wants a short explanation for the support team before the release.

Open questions
- Who owns the feature flag rollout?
- Which number shows early that delivery costs went up unexpectedly?

Action items
- Pavel: implement the rule and write tests.
- Anna: write the one-page brief and open the issue.
- Ola: update the support reply after the check on staging.
