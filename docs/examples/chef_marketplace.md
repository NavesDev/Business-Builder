# Example: Freelance Chef Marketplace

This example shows the kind of output Business Builder produces for the following idea:

> "I want to build a subscription-based platform that connects freelance chefs with home diners."

---

## Business Architecture (excerpt)

**Core Domains:** User Management, Chef Profiles, Booking & Scheduling, Payments, Reviews & Ratings, Notifications

**Key Entities:**
- `User` (id, name, email, role: diner|chef, created_at)
- `ChefProfile` (id, user_id, bio, cuisine_types, hourly_rate, availability)
- `Booking` (id, diner_id, chef_id, date, status, total_price)
- `Payment` (id, booking_id, amount, currency, provider_ref, status)

---

## Revenue Model (excerpt)

**Recommended:** Marketplace (commission 15%) + optional SaaS tier for chefs  
**Year 1 ARR estimate:** $120k (based on 500 active chefs, 4 bookings/month avg)

---

## Viability Score

**74 / 100** — Medium-High feasibility. Strong demand signal; key risk is supply-side onboarding of quality chefs.
