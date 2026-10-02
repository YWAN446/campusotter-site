# CampusOtter site

The public website for CampusOtter. It is one page of plain HTML and CSS,
served by GitHub Pages from the `main` branch. There is nothing to build.

## Files

| File | What it is |
|---|---|
| `index.html` | The page. All the words are here. |
| `styles.css` | Colors, type, and layout. |
| `logo.png` | The logo. The original is in the app repository under `design/logo/`. |
| `favicon.png`, `apple-touch-icon.png` | The logo at small sizes, for browser tabs and phones. |
| `og_image.png` | The picture shown when the link is shared. Made by `tools/make_og_image.py`. |

## Before announcing the site

1. **Check the sign-in buttons.** They point to the live app at
   https://campusotter.vercel.app. The address is set near the top of
   `index.html` as `window.CAMPUSOTTER_APP_URL`. Change it there if the app
   moves to its own domain.
2. **Let search engines in.** Delete the line
   `<meta name="robots" content="noindex">` from `index.html`.
3. **Check the claims.** The schools section says CampusOtter is planned to
   come with a GrantOtter institution subscription. Change it if the plan
   changes.

## Changing the page

Edit the file, commit, and push. GitHub Pages republishes in about a minute.

To see the page before pushing, open `index.html` in a browser.
