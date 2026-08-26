# P8-APS-PUBLISHING-CAP — findings (2026-08-25)

Research-only verification of the APS app publishing/production-review cap (queue item
P8-APS-PUBLISHING-CAP, from BIMpossible_PHASE-STATUS.md Phase 8). Public docs only; no
console login performed. Verification level: verified-against-public-docs; the two
Left-Flags below need a signed-in console check by the owner.

## Answer: there is NO Autodesk review gate for production — but there IS a new mandatory enrollment step

1. **Production status is self-serve.** No Autodesk approval/review is required to run an
   APS app in production. Customer data access is granted per-customer by their ACC
   account admin, not by Autodesk. The only review process is optional App Store listing.

2. **NEW (Dec 2025) — mandatory enrollment + developer-hub migration.** Every APS
   developer must enroll in a Free or Paid offering and migrate apps into a "developer
   hub" (usage/billing workspace). Deadline conflict between sources: APS blog says
   migrate by **2026-02-18** ([blog](https://aps.autodesk.com/blog/aps-business-model-evolution));
   NTI says non-enrolled access was suspended after **2026-01-16**
   ([NTI](https://www.nti-group.com/uk/blog/uk/2026/important-change-autodesk-platform-services/)).
   Either way it is an enrollment/billing step, not a review. Migration how-to:
   [developer-hub blog](https://aps.autodesk.com/blog/how-create-developer-hub-and-migrate-your-applications).
   **ACTION: confirm the BIMpossible APS app is enrolled/migrated — if not, it may already be suspended.**

3. **No caps tied to unpublished status.** Limits follow pricing tier, identical for
   private vs listed apps:
   - Free tier: monthly caps on the four "rated" APIs (Model Derivative, Design
     Automation, Flow Graph Engine, Reality Capture) — ~20 complex translations +
     ~300k API-call equivalent/month; app suspended for the rest of the month if exceeded.
   - Non-rated APIs (Data Management, ACC, OAuth) have no monetized caps, only standard
     per-minute rate limits ([OAuth](https://aps.autodesk.com/en/docs/oauth/v2/developers_guide/rate-limiting/forge-rate-limits/),
     [Model Derivative](https://aps.autodesk.com/en/docs/model-derivative/v2/developers_guide/rate-limiting/forge-rate-limits)).
   - Paid: Flex tokens (min 100, 1-yr expiry) or pay-as-you-go; "Basic Interactions" =
     1 token per 300k non-translation calls.
   - For BIMpossible (mostly Data Management/ACC reads + AEC DM + 3LO): free tier likely
     suffices at launch; Model Derivative translation volume is the binding constraint.

4. **Customer onboarding path (3LO into customer hubs):** customer's account admin adds
   the app under Account Admin → Custom Integrations (+ client ID, product selection).
   Auto-activated for all accounts created since ~Feb 2021; only legacy BIM 360
   enterprise accounts still need the bim360appsactivations email path.
   ([admin help](https://help.autodesk.com/cloudhelp/ENU/BIM-360-Admin-Help/files/GUID-0C83B441-C611-4574-8DA0-45D5CFC235FA.htm))

5. **Private SaaS = no marketplace requirements.** App Store listing, review, and revenue
   share apply only if listing; a private SaaS needs only: APS app + offering enrollment +
   developer hub + per-customer custom-integration approval.

## Left-Flags
- (a) Jan-16 vs Feb-18 2026 suspension-date conflict — check enrollment state in the APS
  console while signed in.
- (b) Exact free-tier cap numbers came from secondary sources; the APS pricing page 403s
  anonymously — confirm signed in.
- (c) Dec-2025 pricing raised Model Derivative/Design Automation rates — worth a cost
  model before launch.
