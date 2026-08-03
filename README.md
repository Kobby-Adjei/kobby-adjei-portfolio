# FlmLnk Case Studies

Live at [kobby-adjei.vercel.app](https://kobby-adjei.vercel.app).

Two pieces of work at FlmLnk, a marketing tool for filmmakers.

### The Renovation

**Why.** The product looked like every other AI app released that year, and inconsistent against its own screens.

**What.** Twenty-one changes logged, seven shown as before and after, including the June build and the current
build running side by side on the same account.

**How.** I inspected the product against a competitor to separate real bugs from opinions, audited FlmLnk's own
screens against each other to find which faults repeated, then rebuilt against five stated design principles.

### The Tournament

**Why.** A frontier model chose which moments became clips, and it was the most expensive call in the product. The
question was whether a cheaper model could do the same job without a drop in quality.

**What.** A cheaper model scored higher, at roughly 78 percent lower cost per usable clip. A human review of the
leading pairs then showed the measurement itself was faulty, so no winner has been declared.

**How.** I wrote a rubric from ten human reviewer notes, then scored 297 candidates from 23 models blind, without
knowing which model produced which, and unsealed the mapping only after scoring. A follow-up human review of
rendered video found a tenth of a second of audio was cutting words in half and deciding the results, so that
comparison is still confounded.

---

Static site, no build step.
