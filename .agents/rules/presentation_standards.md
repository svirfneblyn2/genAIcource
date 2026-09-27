# Presentation Standards & Architecture Guidelines

## Golden Rules of GenAI Course Presentations

1. **Title Slide Independence:** Slide 01 is a standalone topic poster. It must NEVER contain instructor credentials, emails, or logistics. Those belong to Slides 02, 03, and 04.
2. **Zero Clipping:** Never allow any diagram to push the slide footer offscreen. Always apply `.visual-slide` class and strict `min-height: 0; overflow: hidden;` CSS.
3. **Strict 90-Minute Budgeting:**
   - Block 1 (00:00–12:00): Intro, bio, roadmap, Git workflow.
   - Block 2 (12:00–29:00): Real-world AI, taxonomy, classical ML vs GenAI.
   - Block 3 (29:00–55:00): Paradigms (Karpathy), hype trap, tokens, T9 probabilities, RAG vs hallucinations.
   - Midpoint Break (55:00–60:00): 5-minute timer + chat prompt.
   - Block 4 (60:00–70:00): The 10/90 Iceberg, Blast Radius matrix.
   - Block 5 (70:00–80:00): 4 failures vs 4 wins (CodeMie @ Dawn Foods), Decision Tree live teardowns.
   - Block 6 (80:00–90:00): Homework memo walkthrough (Glovo courier), Q&A.
4. **Bilingual Parity:** Both Russian and English versions must be created, audited, and exported to PDF simultaneously.
