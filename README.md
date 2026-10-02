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
| `campusotter-promo.mp4` | The one-minute promo video (1080p, 32 MB). It is the file the video project in the app repository's `video/` folder renders to `out/campusotter.mp4`. To replace it, copy the new file over this one. |
| `promo-poster.jpg` | The still shown before the video plays: the frame at 13 seconds. |
| `campusotter-promo.en.vtt` | English captions for the video, timed from the video project's `audio/timeline.json`. Update it if the narration changes. |

## Things to keep an eye on

1. **Check the sign-in buttons.** They point to the live app at
   https://campusotter.vercel.app. The address is set near the top of
   `index.html` as `window.CAMPUSOTTER_APP_URL`. Change it there if the app
   moves to its own domain.
2. **Check the claims.** The schools section says CampusOtter is planned to
   come with a GrantOtter institution subscription. Change it if the plan
   changes.

## Changing the page

Edit the file, commit, and push. GitHub Pages republishes in about a minute.

To see the page before pushing, open `index.html` in a browser.
