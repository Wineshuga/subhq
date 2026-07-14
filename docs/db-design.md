# Database Design

## Overview

The application consists of four core entities:

- Users
- Services
- Subscriptions
- Payments

## Relationships

- A user can have many subscriptions.
- A subscription belongs to one user.
- A service can have many subscriptions.
- A subscription can have many payments.
- A payment belongs to one subscription.

## Design Decisions

### Services table

A separate Services table is used to avoid storing duplicate service
information.

### Payments

Payments are stored independently so every renewal creates a new payment
record, allowing payment history to be preserved.

### Subscription pricing

Subscription price is stored on the subscription instead of the service
because different users may have different pricing plans or rates.