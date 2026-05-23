# Monte Carlo Retirement Simulator v2

A modern, installable, and offline-ready retirement planning app built as a single-file Progressive Web App (PWA). Designed for both desktop and mobile, with advanced simulation, tax, Social Security, and scenario comparison features.

---

## Features
- Advanced Monte Carlo simulation with customizable market, spending, and risk models
- Tax-aware withdrawal modeling (federal, state, single/married)
- Social Security estimation (claim age, COLA, FRA)
- Multiple account types: retirement, brokerage, HSA, T-Bill ladder, pensions
- Spending guardrails, floor/ceiling, and market-responsive policies
- Scenario save/load and side-by-side comparison
- Mobile-first, responsive UI
- Installable as a PWA (works offline, add to home screen)
- No backend, no dependencies, no build step

---

## Quick Start
1. **Download or clone this repository.**
2. **Open `index.html` (or `RetirementSimulator_v2.html`) in your browser.**
   - For full PWA features, see [Deployment](#deployment).
3. **Start planning!**

---

## Deployment
### GitHub Pages (Recommended)
1. Create a new GitHub repository.
2. Upload all files:
   - `index.html` (rename from `RetirementSimulator_v2.html` for root access)
   - `manifest.webmanifest`, `service-worker.js`, `icon-192.png`, `icon-512.png`
3. Go to **Settings → Pages** and set the source to the main branch and root (`/`).
4. Access your app at:
   - `https://<your-username>.github.io/<repo-name>/`
5. Open on any device. Use “Install app” or “Add to Home screen” for PWA experience.

### Local Server
1. Open a terminal in your project folder.
2. Run:
   ```
   python -m http.server 8000
   ```
3. Visit `http://localhost:8000/` in your browser.

### Direct File Use
- Open `index.html` directly in your browser (some browsers may restrict PWA features for local files).

---

## Mobile Installation
### Android (Google Pixel, Samsung, etc.)
1. Open Chrome and navigate to your deployed app URL (GitHub Pages or local server).
2. Tap the three-dot menu (top right).
3. Tap **“Add to Home screen”** or **“Install app”**.
4. Follow the prompts. The app icon will appear on your home screen.
5. Launch from the icon for a full-screen, offline-capable experience.

### iOS (iPhone/iPad)
1. Open Safari and go to your app URL.
2. Tap the **Share** button, then **“Add to Home Screen”**.
3. The app will install and launch like a native app.

---

## Testing
- Open `RetirementSimulator_v2.tests.html` in your browser.
- Click **“Run Saved Test Suite”** to validate all features.
- Use `html_regression_check.py` to ensure HTML structure is valid.

---

## Customization
- **Icons:** Replace `icon-192.png` and `icon-512.png` for your own branding.
- **App Name/Description:** Edit `manifest.webmanifest`.
- **Offline Files:** Update `service-worker.js` if you add new files.
- **UI/Logic:** All code is in a single HTML file for easy editing.

---

## License
MIT License. Free for personal and commercial use.

---

## Credits
Developed by [Your Name]. Powered by modern browser APIs and open-source tools.
