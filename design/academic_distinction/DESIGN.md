---
name: Academic Distinction
colors:
  surface: '#faf8ff'
  surface-dim: '#d2d9f4'
  surface-bright: '#faf8ff'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#f2f3ff'
  surface-container: '#e9edff'
  surface-container-high: '#e1e8ff'
  surface-container-highest: '#dae2fc'
  on-surface: '#131b2e'
  on-surface-variant: '#434651'
  inverse-surface: '#283044'
  inverse-on-surface: '#edf0ff'
  outline: '#747782'
  outline-variant: '#c4c6d3'
  surface-tint: '#375ca8'
  primary: '#3459a5'
  on-primary: '#ffffff'
  primary-container: '#4f72c0'
  on-primary-container: '#fefcff'
  inverse-primary: '#b0c6ff'
  secondary: '#3d6658'
  on-secondary: '#ffffff'
  secondary-container: '#bce9d7'
  on-secondary-container: '#416b5c'
  tertiary: '#00694c'
  on-tertiary: '#ffffff'
  tertiary-container: '#008561'
  on-tertiary-container: '#f5fff7'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#d9e2ff'
  primary-fixed-dim: '#b0c6ff'
  on-primary-fixed: '#001945'
  on-primary-fixed-variant: '#1a438f'
  secondary-fixed: '#bfecda'
  secondary-fixed-dim: '#a4d0bf'
  on-secondary-fixed: '#002118'
  on-secondary-fixed-variant: '#244e41'
  tertiary-fixed: '#87f8ca'
  tertiary-fixed-dim: '#6adbaf'
  on-tertiary-fixed: '#002115'
  on-tertiary-fixed-variant: '#00513a'
  background: '#faf8ff'
  on-background: '#131b2e'
  surface-variant: '#dae2fc'
typography:
  h1:
    fontFamily: Lexend
    fontSize: 40px
    fontWeight: '700'
    lineHeight: '1.2'
    letterSpacing: -0.02em
  h2:
    fontFamily: Lexend
    fontSize: 32px
    fontWeight: '600'
    lineHeight: '1.3'
    letterSpacing: -0.01em
  h3:
    fontFamily: Lexend
    fontSize: 24px
    fontWeight: '600'
    lineHeight: '1.4'
    letterSpacing: '0'
  body-lg:
    fontFamily: Inter
    fontSize: 18px
    fontWeight: '400'
    lineHeight: '1.6'
    letterSpacing: '0'
  body-md:
    fontFamily: Inter
    fontSize: 16px
    fontWeight: '400'
    lineHeight: '1.5'
    letterSpacing: '0'
  body-sm:
    fontFamily: Inter
    fontSize: 14px
    fontWeight: '400'
    lineHeight: '1.5'
    letterSpacing: '0'
  label-caps:
    fontFamily: Inter
    fontSize: 12px
    fontWeight: '600'
    lineHeight: '1'
    letterSpacing: 0.05em
rounded:
  sm: 0.25rem
  DEFAULT: 0.5rem
  md: 0.75rem
  lg: 1rem
  xl: 1.5rem
  full: 9999px
spacing:
  base: 8px
  xs: 4px
  sm: 12px
  md: 24px
  lg: 40px
  xl: 64px
  container-max: 1280px
  gutter: 24px
---

## Brand & Style
The design system is engineered to project an aura of academic excellence and institutional reliability, now enhanced with an **Expressive** visual energy. The brand personality remains authoritative and accessible, catering to students and educators who value clarity, but with a more vibrant and engaging color story that encourages active participation.

The aesthetic follows a **Corporate / Modern** style, characterized by intentional whitespace and high-precision alignment. By utilizing an expressive color palette against a structured grid, the design system ensures that educational content remains the focal point while providing a more modern, energetic environment conducive to intellectual growth and creative problem-solving.

## Colors
The color strategy for this design system prioritizes professional trust while introducing organic, expressive tones to differentiate content types.

- **Primary (Cornflower Blue):** Used for core branding, active navigation states, and primary headings to establish a foundation of stability and intelligence.
- **Secondary (Sage Green):** Reserved for supporting actions, secondary navigation, and success states, providing a calming, organic contrast.
- **Tertiary (Teal):** Used for accents, specialized highlights, and distinct interactive elements like progress indicators.
- **Neutral (Muted Slate):** A sophisticated range of cool-toned grays used to define hierarchy, borders, and secondary text, ensuring the interface remains balanced and readable.

Information density is managed through varying levels of saturation, ensuring that functional elements stand out against the refined neutral backdrop.

## Typography
Readability is the cornerstone of this design system. We utilize **Lexend** for headings; its design is rooted in educational research to improve reading proficiency. It provides a modern, friendly, yet highly structured appearance. 

For the UI and long-form body copy, **Inter** provides a systematic and neutral counterpoint, ensuring that complex data tables and board notifications are legible at any scale. We employ a rigorous typographic scale to ensure clear information hierarchy, using heavier weights for headers and increased line-height for body copy to prevent reader fatigue.

## Layout & Spacing
This design system utilizes a **Fixed Grid** model for desktop and a **Fluid Grid** for mobile devices. 

- **Desktop:** A 12-column layout with a 24px gutter, centered within a 1280px max-width container. 
- **Mobile:** A 4-column fluid layout with 16px side margins.

The spacing rhythm is built on an 8px base unit. We prioritize "breathable" layouts, using generous padding (the `lg` and `xl` tokens) between major content sections to reduce cognitive load, which is essential for educational dashboards.

## Elevation & Depth
To maintain a professional and clean aesthetic, the design system utilizes **Tonal Layers** and **Low-Contrast Outlines** instead of heavy drop shadows. 

Depth is communicated through subtle shifts in surface color. For example, the main background uses the lightest neutral, while interactive cards sit on white surfaces with a 1px border in a light muted slate. Shadows, where necessary for high-level modals, are "ambient": extremely diffused, low-opacity (8-10%), and slightly tinted with the Primary Cornflower Blue to maintain color harmony across the expressive palette.

## Shapes
The shape language balances approachability with structure. A **Rounded (0.5rem)** corner radius is the standard for buttons, input fields, and cards. This softened geometry makes the academy board feel modern and welcoming to students. 

Larger containers, such as course module cards or search bars, utilize the `rounded-lg` (1rem) token to create a distinct visual "nesting" effect. This consistent rounding ensures that even high-density information feels organized and less intimidating.

## Components

### Buttons
Primary buttons use the Primary (Cornflower Blue) background with white text. Hover states involve a subtle darkening of the blue. Secondary buttons use the Sage Green for a softer, supportive action feel, while ghost buttons utilize the muted slate border.

### Cards
Cards are the primary vehicle for "Lessons" and "Assignments." They feature a white background, a 1px neutral border, and a 0.5rem corner radius. On hover, the border color shifts to the Primary blue to indicate interactivity.

### Form Fields
Input fields are clean and minimalist. They feature a light gray background that transitions to a white background with a Cornflower Blue border on focus. Labels use the `label-caps` typography style for clarity.

### Progress Indicators
Since this is an educational board, progress bars are critical. Use a thick, rounded track in a light neutral gray, with the Tertiary Teal indicating completion for a distinct, high-contrast visual cue.

### Chips & Badges
Used for lesson tags (e.g., "Grammar," "Level B2"). These should be pill-shaped with low-saturation versions of the Sage or Teal backgrounds and high-saturation text to ensure they are legible but not distracting.