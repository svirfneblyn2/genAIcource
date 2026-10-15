# Lesson 07: Live Demo Step-by-Step Runbook
**Course:** GenAI Basics • Module 3 • Lesson 07  
**End-to-End Case Study:** Project Northstar (VIP Free Shipping Rule Rollout)  
**File Location:** `demo_assets/` (inside directory `L07/`)  

---

## 1. Pre-Class Setup (15–20 Minutes Prior to Broadcast)

1. **Verify Sample Code Repository:**
   * Open a terminal inside `demo_assets/sample_repo`.
   * Run the baseline verification:
     ```bash
     python smoke_check.py
     ```
   * Confirm terminal outputs: `Ran 4 tests in 0.000s ... OK ... BASELINE TESTS PASS`.
2. **Arrange Display Tabs & Windows:**
   * **Window 1:** VS Code open to `demo_assets/sample_repo`. Ensure `ISSUE.md` and `.github/copilot-instructions.md` are visible in the file explorer.
   * **Window 2:** Microsoft Word (or web Microsoft 365 Copilot Chat) with `demo_assets/meeting_notes_fixture.docx` opened.
   * **Window 3 (Emergency Fallbacks):** Backup tabs open to ensure resilience against connectivity or tenant license timeouts:
     * `demo_assets/fallback_outputs/m365_expected_brief.md`
     * `demo_assets/fallback_outputs/github_expected_review.md`
     * `demo_assets/sample_repo/expected_solution/shipping.py`

---

## 2. Part 1: Microsoft 365 Copilot Demo (6 Minutes)
*Slide Deck: Slide 16*  
*Objective:* Demonstrate meeting document grounding and the Microsoft Learn 4-ingredient prompt standard.

### Step 1: Anchor Context
* In Word (or M365 Copilot Chat), attach `meeting_notes_fixture.docx` using the `/` reference prompt or attachment clip.
* Spoken cue: *"We do not ask the model to invent rules. We ground the request directly in authoritative executive meeting minutes."*

### Step 2: Input the 4-Ingredient Prompt
Paste the following prompt into the chat input:

```text
[Goal]: Draft a structured customer support rollout brief for the new VIP Free Shipping rule.
[Context]: We are releasing this update this weekend. Tier-1 support operators need unambiguous activation thresholds and exclusion workflows.
[Source]: Rely strictly on attached meeting_notes_fixture.docx. Do not invent ungrounded business policies!
[Expectations]: Format output in Markdown with three distinct sections:
1. Eligibility Criteria for Free Shipping;
2. Edge Cases and Exceptions;
3. Open Business Questions Requiring Clarification.
Length: Under 250 words. Include explicit paragraph citations linking claims back to source notes.
```

### Step 3: Audience Verification Highlights
1. **Order Threshold:** Point out that Copilot identified the $50 order minimum required for free shipping eligibility.
2. **Open Dispute:** Show that Copilot highlighted the unresolved meeting debate — *"Does the business reimburse delivery fees when orders are delayed by extreme weather?"*
3. **Source Citations:** Hover over bracketed citations to demonstrate trace links back into `meeting_notes_fixture.docx`.

*Fallback action:* If cloud connection stalls, switch immediately to tab `demo_assets/fallback_outputs/m365_expected_brief.md` stating: *"Here is our pre-verified evidence artifact generated under identical constraints."*

---

## 3. Part 2: GitHub Copilot Agent Mode in VS Code (7 Minutes)
*Slide Deck: Slide 17*  
*Objective:* Demonstrate autonomous multi-file edits, terminal test execution, and human diff inspection.

### Step 1: Inspect Task in VS Code
* Open `ISSUE.md`: display requirements for the `VIPShippingCalculator` class.
* Open `.github/copilot-instructions.md`: point out constraints: *"Always include unit tests with pytest and preserve existing public signatures"*.

### Step 2: Trigger Agent Mode
* Open Copilot in VS Code (`Ctrl+I` or sidebar in **Agent Mode / Copilot Edits**).
* Input prompt:

```text
@workspace Read ISSUE.md and instructions in .github/copilot-instructions.md.
1. Propose an implementation plan to introduce VIP free shipping on orders >= $50.
2. Update the calculate_shipping method in sample_repo/shipping.py.
3. Add boundary unit tests in sample_repo/test_shipping.py (VIP <$50, VIP >=$50, non-VIP).
4. Run python smoke_check.py in terminal and verify all tests pass.
```

### Step 3: The Human Checkpoint
1. **Plan Inspection:** Highlight that the agent outputs a structured plan before touching code.
2. **Terminal Authorization:** Point out that VS Code halts and requests explicit developer authorization (**Allow / Approve**) to execute `python smoke_check.py`.
3. **Side-by-Side Diff Review:** Open the suggested diff in `shipping.py`.  
   *Speaker cue:* *"Notice what I am checking: Did the agent inadvertently remove the validation check for negative package weights? No, legacy validation remains intact, and the VIP branch is inserted cleanly. This is the human responsibility layer."*
4. Click **Accept Edits** and verify in terminal:
   ```bash
   python smoke_check.py
   ```
   Confirm test count increased (e.g., from 4 to 6) and test status is `OK`.

---

## 4. Part 3: Local Release Checklist Verification (2 Minutes)
*Slide Deck: Slides 14 & 19*  
*Objective:* Complete the durable evidence chain before staging rollout.

1. Open `demo_assets/release_checklist.txt`.
2. Review checklist entries:
   * `[x] Unit tests pass (smoke_check.py)`
   * `[x] Rollout brief approved by Support Lead`
   * `[ ] Staging feature flag VIP_SHIPPING_ENABLED set to true`
3. Summary cue: *"We connected three systems: M365 (document synthesis), GitHub (code and automated tests), Local OS (release preflight). At no point did we accept conversational output without verifiable evidence."*
