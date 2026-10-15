# Issue: VIP domestic shipping policy

The product meeting approved one change for the US store:

- VIP customers with a subtotal of **$75 or more** receive free domestic shipping.
- The existing **$100 free-shipping threshold still applies to everyone**.
- International shipping behavior must not change.
- Add tests for the VIP threshold boundary and one non-VIP regression case.
- Preserve the existing error behavior for negative subtotals.

Acceptance: all unit tests pass and the change is reviewable as a small pull request.
