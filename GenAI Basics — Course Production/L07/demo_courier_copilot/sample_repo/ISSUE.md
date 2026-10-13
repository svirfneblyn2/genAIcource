# Issue #12: Free delivery for Prime customers from $75

The product meeting approved one change for the courier app:

- Prime customers with a subtotal of **$75 or more** get free delivery **inside the city zone**.
- The existing **free delivery from $100 still applies to everyone**.
- Deliveries **outside the zone must not change** (fee stays $18.00).
- Add tests for the Prime boundary (75 and 74.99) and one non-Prime regression case.
- Keep the existing error for a negative subtotal.

Acceptance: all unit tests pass and the change is a small pull request.
