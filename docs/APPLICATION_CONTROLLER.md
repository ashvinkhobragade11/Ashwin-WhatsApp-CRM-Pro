# APPLICATION CONTROLLER

## Purpose

The ApplicationController is the central coordinator of Ashwin WhatsApp CRM Pro.

It is responsible for:

- Application Startup
- Login Navigation
- Dashboard Navigation
- Logout Flow
- Window Lifecycle
- Future Module Navigation

---

## Responsibilities

- Initialize application
- Open Login Window
- Open Dashboard
- Manage User Session
- Handle Logout
- Handle Application Exit

---

## Design Principle

UI windows should never decide application flow.

ApplicationController owns all navigation decisions.