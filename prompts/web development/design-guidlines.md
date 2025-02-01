---
tags: [web development, tailwindcss, design, colours]
models: [claude-3-5-sonnet-20240620, gpt-4o]
created: 2025-01-31
updated: 2025-01-31
---

## Description

This prompt helps generate a consistent design system for web development projects using Tailwind CSS. The resulting design system can be included into the project's cursorrules file to achieve consistent styling across the project. Without any additional context, the primary colour will usually some kind of neutral blue. By providing a primary colour to start from or a description of the brand or project, you can achieve some variation in the output.

## Prompt

Please help me create some basic design guidelines for my web development project using Tailwind CSS. The design guidelines should contain the main styling variables for the project. The styling may only contain Tailwind classes and the colours should be from the Tailwind CSS colour palette.

Please provide your answer in the following format:

Colors:
- primary colour:
  - foreground-light: [color]-[shade]
  - background-light: [color]-[shade]
  - foreground-dark: [color]-[shade]
  - background-dark: [color]-[shade]
- secondary colour:
  - foreground-light: [color]-[shade]
  - background-light: [color]-[shade]
  - foreground-dark: [color]-[shade]
  - background-dark: [color]-[shade]
- accent colour:
  - foreground-light: [color]-[shade]
    - background-light: [color]-[shade]
  - foreground-dark: [color]-[shade]
  - background-dark: [color]-[shade]
- feedback colours (success, warning, error, info):
  - foreground-success: [color]-[shade]
  - background-success: [color]-[shade]
  - foreground-warning: [color]-[shade]
  - background-warning: [color]-[shade]
  - foreground-error: [color]-[shade]
  - background-error: [color]-[shade]
  - foreground-info: [color]-[shade]
  - background-info: [color]-[shade]
- background colour:
  - light: [color]-[shade]
  - dark: [color]-[shade]
- text colour:
  - light: [color]-[shade]
  - dark: [color]-[shade]
- border colour:
  - light: [color]-[shade]
  - dark: [color]-[shade]

Font size and weight:
- h1: text-[size], font-[weight]
- h2: text-[size], font-[weight]
- h3: text-[size], font-[weight]
- h4: text-[size], font-[weight]
- h5: text-[size], font-[weight]
- h6: text-[size], font-[weight]
- small: text-[size], font-[weight]
- code: text-[size], font-[weight]

Spacing:
- container-padding: p-[size]
- section-spacing: space-y-[size]
- component-gap: gap-[size]
- content-spacing: space-y-[size]
- max-content-width: max-w-[size]

Borders:
- border radius: rounded-[size]
- border-width: border-[size]

Box shadows:
- box-shadow: shadow-[size]

Additional considerations:
1. Ensure sufficient contrast ratios between background and text colours
2. Surface colours should be subtle and not compete with content
3. Dark theme colours should not be simply inverted light theme colours
4. State colours (info, success, warning, danger) should be consistent across themes
5. Consider colour psychology when selecting state colours:
   - Info: Usually blue tones
   - Success: Usually green tones
   - Warning: Usually amber/yellow tones
   - Danger: Usually red tones
6. Body text should always be the default font size and weight and should form the basis of the font size and weight scale
7. Follow the project's brand guidelines if they exist
8. Ensure all interactive elements have visible focus states for accessibility
9. Consider reduced motion preferences
10. Ensure spacing scales are consistent with typography scale
11. Plan for responsive adjustments of spacing and typography
12. Include focus styles that work for both mouse and keyboard users

Reference the official Tailwind CSS colour palette at https://tailwindcss.com/docs/colours for available colours and shades.