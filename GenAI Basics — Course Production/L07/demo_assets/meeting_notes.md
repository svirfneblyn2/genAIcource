# Project Northstar — meeting notes

Date: 8 September 2026
Participants: Product, Engineering, Support

Decisions
- Add free domestic shipping for VIP customers at a subtotal of $75 or more.
- Keep the existing $100 free-shipping threshold for all customers.
- Do not change international shipping.
- Release behind a configuration flag first; Support wants a one-paragraph explanation before rollout.

Open questions
- Who owns the feature flag rollout?
- What metric will detect an unexpected shipping-margin increase?

Action items
- Engineering: implement + tests.
- Product: create rollout note.
- Support: update macro after staging verification.
