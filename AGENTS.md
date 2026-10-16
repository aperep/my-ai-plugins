# Marketplace instructions

Use the [marketplace guide](README.md) for layout and validation.
Reusable rules belong in plugins; personal storage paths and policies belong
in consumer repositories. Check `git check-attr guard -- <path>` before edits;
never stamp your own work as reviewed.

Repository routines live in [maintenance](docs/MAINTENANCE.md); durable planned
work lives in the repo-wide [roadmap](docs/ROADMAP.md).

## Personal branch workflow

Make only personal-branch changes directly on `aperep`. For any shared change,
switch to `main` before editing, implement and commit there, then merge `main`
into `aperep`. Preserve personal overrides when resolving conflicts. Never
merge `aperep` into `main`. See the [branch workflow](docs/DUAL.md#public-and-personal-branches).
