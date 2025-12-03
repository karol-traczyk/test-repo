# test-repo
Refresh

## CSS Tips

### Organization & architecture
- Use a predictable naming scheme (BEM, SUIT, or your own documented pattern) so selectors like `card__title--highlight` explain their role without comments.
- Layer styles by responsibility—start with base/reset rules, add layout primitives, then components and utilities—so overrides stay intentional.
- Keep selectors shallow; prefer class-based hooks (`.btn` + `.btn--primary`) instead of chained descendants to control specificity.

### Reusability & maintainability
- Define shared tokens as CSS variables to reuse colors, spacing, and typography consistently:

```css
:root {
  --color-primary: #1f7aec;
  --space-md: 1rem;
  --font-base: clamp(1rem, 2vw, 1.125rem);
}

.text-muted { color: var(--color-primary); }
.gap-md { gap: var(--space-md); }
```

- Pair small utility classes with semantic components so layout tweaks (`.gap-md`, `.pad-lg`) never require editing multiple files.
- Extract repeated values into tokens (design system files, `:root`, or preprocessors) to avoid one-off hex codes or magic numbers.
- Reserve `!important` for escape hatches (debug utilities, third-party overrides); treat it as a last resort and document its use.

### Modern CSS features
- Lean on Flexbox for one-dimensional layout:

```css
.toolbar {
  display: flex;
  align-items: center;
  gap: 0.75rem;
  flex-wrap: wrap;
}
```

- Use Grid when both rows and columns matter:

```css
.card-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(16rem, 1fr));
  gap: 1.5rem;
}
```

- Use `clamp()` or responsive units for fluid typography/spacing to avoid media-query bloat.
- Define custom properties on `:root` and adjust them with prefers-* media queries (`prefers-reduced-motion`, `prefers-color-scheme`) so experiences adapt to user settings.

### Performance & best practices
- Audit bundles regularly: remove unused selectors, split critical CSS from async-loaded chunks, and keep payloads small.
- Group related styles, delete dead code after refactors, and document utility files so future contributors know what is safe to prune.
- Test across breakpoints and browsers (especially low/high DPI and reduced-motion) to catch cascade or layout regressions early.
