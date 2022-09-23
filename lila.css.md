# Stylesheet Documentation · **`lila.css`**
**Rules:** 128 · 
**Comments:** 23 · 
**Total:** 166
---
## `*`

This selector affects the following properties:
- `font-family`
- `box-sizing`
## `html`

This selector affects the following properties:
- `font-family`
- `scroll-behavior`

>  Make the body a nice central block 
## `body`

This selector affects the following properties:
- `color`
- `background`
- `font-size`
- `line-height`
- `margin`
## `body:not(.no-grid)`

This selector affects the following properties:
- `display`
- `grid-template-columns`
## `body:not(.no-grid) > *`

This selector affects the following properties:
- `grid-column`

>  ================ HEADER ================ 
## `body.dark nav, body.dark header, body.dark nav`

This selector affects the following properties:
- `color`

>  Make the header bg full width, but the content inline with body 
## `body > header`

This selector affects the following properties:
- `background-repeat`
- `background-size`
- `background-position`
- `text-align`
- `position`
- `box-sizing`
- `align-items`
- `justify-content`
- `z-index`
## `body > header.tall`

This selector affects the following properties:
- `padding-top`
- `padding-bottom`
## `body > header.with-nav`

This selector affects the following properties:
- `padding-top`
## `body > header:not(.no-grid)`

This selector affects the following properties:
- `grid-column`
## `body > header h1`

This selector affects the following properties:
- `max-width`
- `margin`
## `body > header p`

This selector affects the following properties:
- `max-width`
- `margin`

>  ================ COVER ================ 
## `body > header::before`

This selector affects the following properties:
- `background-attachment`
- `background-position`
- `background-repeat`
- `background-size`
- `content`
- `position`
- `top`
- `right`
- `bottom`
- `left`
## `body > header.transparent-2::before`

This selector affects the following properties:
- `opacity`
## `body > header.transparent-3::before`

This selector affects the following properties:
- `opacity`
## `body > header.transparent-35::before`

This selector affects the following properties:
- `opacity`
## `body > header.transparent-5::before`

This selector affects the following properties:
- `opacity`
## `body > header.transparent-8::before`

This selector affects the following properties:
- `opacity`
## `img.blog-image`

This selector affects the following properties:
- `width`
- `-o-object-fit`
- `object-fit`
- `max-height`
## `span.ox-label`

This selector affects the following properties:
- `color`
- `opacity`
- `text-decoration`
## `span.ox-label::before`

This selector affects the following properties:
- `content`
## `span.ox-label::after`

This selector affects the following properties:
- `content`

>  ================ NAVBAR ================ 
## `nav`

This selector affects the following properties:
- `z-index`
- `line-height`
- `overflow`
- `top`
- `width`
- `font-size`
- `-webkit-backdrop-filter`
- `backdrop-filter`
## `nav.floating`

This selector affects the following properties:
- `position`
- `background-color`
- `box-shadow`
## `nav.stay-left`

This selector affects the following properties:
- `position`
## `nav ul, nav ol`

This selector affects the following properties:
- `align-content`
- `align-items`
- `display`
- `flex-direction`
- `justify-content`
- `list-style-type`
- `margin`
- `padding`
## `nav ul li`

This selector affects the following properties:
- `display`
## `.dropdown`

This selector affects the following properties:
- `position`
- `display`
## `.dropdown-content`

This selector affects the following properties:
- `display`
- `position`
- `z-index`
- `min-width`
- `box-shadow`
## `.dropdown-content a`

This selector affects the following properties:
- `float`
- `display`
## `.dropdown:hover, .dropdown-content`

This selector affects the following properties:
- `display`
## `nav .logo`

This selector affects the following properties:
- `float`
- `height`
- `transition`
- `margin-top`
- `margin-left`
## `nav .logo:hover`

This selector affects the following properties:
- `cursor`
- `transform`
## `nav a`

This selector affects the following properties:
- `margin`
- `padding`
- `display`
- `text-decoration`
- `transition`
## `nav a i.bi`

This selector affects the following properties:
- `display`
## `nav a.current`

This selector affects the following properties:
- `color`
- `border-top`
## `nav a.colored`

This selector affects the following properties:
- `border-color`
## `nav a:hover`

This selector affects the following properties:
- `color`
- `border-color`
- `position`
## `nav a.right`

This selector affects the following properties:
- `color`
## `nav a:not(.dark), nav a:visited:not(.dark), nav a:active:not(.dark), nav a.current:not(.dark)`

This selector affects the following properties:
- `color`
## `nav a:last-child`

This selector affects the following properties:
- `margin-right`

>  ================ MAIN ================ 
## `main`

This selector affects the following properties:
- `padding-top`
## `body > footer`

This selector affects the following properties:
- `margin-top`
- `padding`
- `color`
- `font-size`
- `text-align`
- `border-top`
- `opacity`
## `.hover-invert:hover`

This selector affects the following properties:
- `filter`
- `transition`
## `.hover-invert`

This selector affects the following properties:
- `transition`
## `div.row`

This selector affects the following properties:
- `display`
- `width`
## `div.input-box`

This selector affects the following properties:
- `display`
## `div.input-box input`

This selector affects the following properties:
- `width`
## `.progress`

This selector affects the following properties:
- `margin`
- `max-width`
- `background-color`
- `border-radius`
## `.progress .bar`

This selector affects the following properties:
- `height`
- `width`
- `--percentage`
- `-webkit-animation`
- `animation`
- `background`
- `border-radius`
## `.progress p`

This selector affects the following properties:
- `color`
- `padding-left`
- `text-shadow`
## `h1`

This selector affects the following properties:
- `font-size`
## `h2`

This selector affects the following properties:
- `font-size`
- `margin-top`
## `h3`

This selector affects the following properties:
- `font-size`
- `margin-top`
## `h4`

This selector affects the following properties:
- `font-size`
## `h5`

This selector affects the following properties:
- `font-size`
## `h6`

This selector affects the following properties:
- `font-size`

>  Fix line height when title wraps 
## `h1, h2, h3`

This selector affects the following properties:
- `line-height`

>  Reduce header size on mobile 

>  ================== UTILITY/TOOLTIP ================== 
## `.tooltip`

This selector affects the following properties:
- `position`
- `display`
- `border-bottom`
## `.tooltip .tip`

This selector affects the following properties:
- `opacity`
- `background-color`
- `color`
- `width`
- `font-size`
- `font-weight`
- `text-align`
- `border-radius`
- `padding`
- `position`
- `z-index`
- `transition`
## `.tooltip:hover .tip`

This selector affects the following properties:
- `opacity`

>  Format links & buttons 
## `main a, footer a, main a:visited, footer a:visited`

This selector affects the following properties:
- `color`
- `text-decoration`
- `transition`
## `a.plain, footer a.plain, a.plain:visited, footer a.plain:visited`

This selector affects the following properties:
- `color`
- `text-decoration`
## `nav a:hover, main a:hover, footer a:hover`

This selector affects the following properties:
- `opacity`
## `textarea:hover, input:hover, select:hover`

This selector affects the following properties:
- `opacity`
## `button, [role=button], input[type=submit], input[type=reset], input[type=button]`

This selector affects the following properties:
- `border`
- `border-radius`
- `font-size`
- `padding`
- `margin`
- `color`
- `background`
- `box-shadow`
- `transition`
## `button[disabled], [role=button][aria-disabled=true], input[type=submit][disabled], input[type=reset][disabled], input[type=button][disabled], input[type=checkbox][disabled], input[type=radio][disabled], select[disabled]`

This selector affects the following properties:
- `opacity`
- `cursor`
## `input:disabled, textarea:disabled, select:disabled`

This selector affects the following properties:
- `cursor`
- `background-color`
## `input[type=range]`

This selector affects the following properties:
- `padding`
## `abbr`

This selector affects the following properties:
- `cursor`
## `button:focus, button:enabled, [role=button], [role=button]:not([aria-disabled=true]), input[type=submit], input[type=submit]:enabled, input[type=reset], input[type=reset]:enabled, input[type=button], input[type=button]:enabled`

This selector affects the following properties:
- `transition`
## `button:focus, button:enabled:hover, [role=button]:focus, [role=button]:not([aria-disabled=true]):hover, input[type=submit]:focus, input[type=submit]:enabled:hover, input[type=reset]:focus, input[type=reset]:enabled:hover, input[type=button]:focus, input[type=button]:enabled:hover`

This selector affects the following properties:
- `filter`
- `cursor`

>  Format the expanding box 
## `details`

This selector affects the following properties:
- `background`
- `border-radius`
- `margin-bottom`
## `summary`

This selector affects the following properties:
- `cursor`
- `font-weight`
- `padding`
## `details[open]`

This selector affects the following properties:
- `padding`
## `details[open] summary + *`

This selector affects the following properties:
- `margin-top`
## `details[open] summary`

This selector affects the following properties:
- `margin-bottom`
- `padding`
## `details[open] > *:last-child`

This selector affects the following properties:
- `margin-bottom`

>  Format tables 
## `table`

This selector affects the following properties:
- `border-collapse`
- `width`
- `margin`
## `td, th`

This selector affects the following properties:
- `text-align`
- `padding`
## `th`

This selector affects the following properties:
- `background`
- `font-weight`
## `tr:nth-child(even) .fancy`

This selector affects the following properties:
- `background`
## `table caption`

This selector affects the following properties:
- `font-weight`
- `margin-bottom`

>  Format forms 
## `textarea, select, input`

This selector affects the following properties:
- `font-size`
- `font-family`
- `padding`
- `margin-bottom`
- `color`
- `background`
- `border`
- `border-radius`
- `box-shadow`
- `box-sizing`
- `-moz-appearance`
- `-webkit-appearance`
- `appearance`
## `select, input[type=checkbox], input[type=radio]`

This selector affects the following properties:
- `cursor`

>  Drop-down arrow 
## `select`

This selector affects the following properties:
- `background-image`
- `background-position`
- `background-size`
- `background-repeat`
## `select[multiple]`

This selector affects the following properties:
- `background-image`
## `input[type=checkbox], input[type=radio]`

This selector affects the following properties:
- `vertical-align`
- `position`
## `input[type=radio]`

This selector affects the following properties:
- `border-radius`
## `input[type=checkbox]:checked, input[type=radio]:checked`

This selector affects the following properties:
- `background`
## `input[type=checkbox]:checked::after`

This selector affects the following properties:
- `content`
- `width`
- `height`
- `border-radius`
- `position`
- `top`
- `left`
- `background`
- `border-right`
- `border-bottom`
- `font-size`
- `transform`

>  Make the textarea wider than other inputs 
## `textarea`

This selector affects the following properties:
- `width`

>  Makes input fields wider on smaller screens 

>  Ensures the checkbox and radio inputs do not have a set width like other input fields 
## `input[type=checkbox], input[type=radio]`

This selector affects the following properties:
- `width`
- `margin`
## `input[type=file]`

This selector affects the following properties:
- `border`
- `background-color`
## `hr`

This selector affects the following properties:
- `color`
- `border-right`
- `margin`
## `mark`

This selector affects the following properties:
- `padding`
- `border-radius`
- `color`
- `background`
## `div.marks mark`

This selector affects the following properties:
- `line-height`
## `main img, main video`

This selector affects the following properties:
- `max-width`
- `height`
- `border-radius`
- `box-shadow`
## `img.blurred`

This selector affects the following properties:
- `filter`
## `.icon`

This selector affects the following properties:
- `vertical-align`
- `padding-right`
- `display`
- `width`
- `height`
- `margin-right`
- `stroke-width`
- `stroke`
- `fill`
## `figure`

This selector affects the following properties:
- `margin`
- `text-align`
## `figcaption`

This selector affects the following properties:
- `font-size`
- `color`
- `margin-bottom`
## `blockquote`

This selector affects the following properties:
- `margin`
- `padding`
- `border-left`
- `color`
- `font-style`
## `cite`

This selector affects the following properties:
- `font-size`
- `font-style`
## `blockquote p, blockquote cite`

This selector affects the following properties:
- `margin-top`
- `margin-bottom`

>  Use mono font for code elements 
## `code, pre, pre span, kbd, samp, p code, pre code, pre font b`

This selector affects the following properties:
- `font-family`
- `color`
- `line-height`
- `letter-spacing`
## `pre font b`

This selector affects the following properties:
- `color`
## `kbd`

This selector affects the following properties:
- `color`
- `border`
- `border-radius`
- `padding`
## `pre`

This selector affects the following properties:
- `padding`
- `max-width`
- `overflow`
- `background`
- `border-radius`
- `color`

>  Fix embedded code within pre 
## `pre code`

This selector affects the following properties:
- `color`
- `background`
- `margin`
- `padding`
## `p code`

This selector affects the following properties:
- `padding`
- `border-radius`
- `background-color`
## `ul.bullets`

This selector affects the following properties:
- `list-style`
## `ul.bullets li`

This selector affects the following properties:
- `line-height`
## `ul.bullets li::before`

This selector affects the following properties:
- `content`
- `display`
- `width`
- `margin-left`
- `font-size`
- `position`
- `top`
## `ul.bullets.in-red li::before`

This selector affects the following properties:
- `color`
## `ul.bullets.in-green li::before`

This selector affects the following properties:
- `color`
## `.copy-to-clipboard`

This selector affects the following properties:
- `display`
- `transition`
- `font-size`
- `font-style`
- `margin-bottom`
- `opacity`
## `.copy-to-clipboard:hover`

This selector affects the following properties:
- `cursor`
- `width`
- `opacity`
## `.copy-to-clipboard:active`

This selector affects the following properties:
- `color`
- `opacity`
## `.copy-to-clipboard.copied`

This selector affects the following properties:
- `color`
## `.copy-to-clipboard.copied::after`

This selector affects the following properties:
- `content`
## `.copy-to-clipboard::after`

This selector affects the following properties:
- `content`

>  ================ FOOTER ================ 
## `button.to-top`

This selector affects the following properties:
- `color`
- `background-color`
- `padding`
- `margin`
- `float`
## `button.to-top.icon`

This selector affects the following properties:
- `-webkit-clip-path`
- `clip-path`

>  Tools 
## `.clickable.toggle-big::before`

This selector affects the following properties:
- `content`
## `.clickable.toggle-big`

This selector affects the following properties:
- `float`
- `position`
- `width`
## `.blog-details`

This selector affects the following properties:
- `opacity`

>  Main stuff 
## `*:focus`

This selector affects the following properties:
- `outline`

> # sourceMappingURL=lila.css.map 
