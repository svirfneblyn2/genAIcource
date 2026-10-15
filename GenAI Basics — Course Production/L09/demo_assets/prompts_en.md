# L09 — the prompts behind the lesson’s artifacts

Every artifact on the slides was made on 13 Oct 2026 in claude.ai (Opus 5.5) with these sentences — each in a new chat (originally in Russian; English versions below).
Demo data: `tickets_en.csv` — made-up courier-support tickets (it deliberately contains customer emails and empty owners).

| Slide | Type | Prompt |
|---|---|---|
| 10 | Slides | Make a 5-slide deck for new couriers of the «Bystro» delivery service: how to accept an order, how to talk to the customer, what to do if the address isn’t found, road safety, summary. |
| 11 | Docs | Make a document: a guide for a new courier-service support agent — 5 rules for answering a customer and reply templates for 3 common complaints. |
| 12 | Design | Make a design: a landing page for the «Bystro» courier service — delivery in 30 minutes, prices, an “Order” button. |
| 13 | Diagram | Draw a diagram: how a customer complaint is handled in a courier service — from the first contact to closing. *(Claude offered Figma — we clicked Decline and wrote: “No Figma: draw it right here, in the artifact.”)* |
| 14 | Mini app | Make a mini app: a coach for a new support agent. Claude plays an unhappy courier-service customer, I answer, then Claude grades my answer on 3 criteria. |

## Live demo (slide 16)

1. New chat → “+” → Add files → `tickets_en.csv`. Text:
   ```
   Make a dashboard for the support lead: what should we tackle first at the morning stand-up? Don't show customer emails.
   ```
2. Check aloud: urgent on top (T-110 — a P1 with no owner), no emails, numbers match the file (11 open, 4 urgent, 2 without an owner).
3. In the same chat:
   ```
   Make 3 slides for the stand-up from this.
   ```

If you don’t like the result, be precise: “move urgent tickets without an owner to the top”, not “make it better”.

## Demo project (slide 17)

Projects → New project “L09 demo: courier support”. Instructions:
```
You help the support lead of the «Bystro» courier service.
- Answer briefly.
- P1 — urgent, P2 — normal, P3 — can wait.
- Never show customer emails or phone numbers.
- Take the data from tickets_en.csv in this project.
```
Context → add `tickets_en.csv`.
