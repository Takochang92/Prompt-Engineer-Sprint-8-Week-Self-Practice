# Prompt Engineer Sprint — 8-Week Practice Log

A hands-on 8-week self-training project building toward a Junior Prompt Engineer role at an AI-driven trading startup.

## What I'm Building

- Python automation scripts (API calls, data fetching, alert systems)
- Linux server operation basics (cron jobs, logging, process management)
- Prompt engineering workflows and reusable template library
- A complete monitoring and alert system as the capstone project

## Weekly Progress

| Week   | Theme                                             | Status         |
| ------ | ------------------------------------------------- | -------------- |
| Week 1 | Python basics — API calls, CSV, logging           | ✅ In progress |
| Week 2 | Automation — scrapers, schedulers, notifications  | ⬜ Upcoming    |
| Week 3 | Prompt engineering — template library             | ⬜ Upcoming    |
| Week 4 | AI output validation and project spec design      | ⬜ Upcoming    |
| Week 5 | Core project: data ingestion and condition engine | ⬜ Upcoming    |
| Week 6 | Core project: alert system and Linux deployment   | ⬜ Upcoming    |
| Week 7 | Portfolio cleanup and resume update               | ⬜ Upcoming    |
| Week 8 | Interview prep and application                    | ⬜ Upcoming    |

## Weekly Deliverables

### Week 1

- `fetch_rate.py` — Fetches live BTC/USD price from Coinbase API and saves to CSV

## Tech Stack

- **Language:** Python 3.14
- **Tools:** Cursor, Claude, ChatGPT, Git
- **Environment:** macOS M2, venv

## What I Learned

### Week 1 — Day 1
- Set up Python virtual environment (venv) from scratch
- Made first API call using `requests` library
- Read and understood error tracebacks independently
- Switched to a working API when the original one was down
- Saved structured data to CSV
- Set up Git and pushed to GitHub with clean folder structure

### Week 1 — Day 2
- Added `try/except` error handling to prevent crashes
- Replaced `print` with `logging` module (file + terminal output)
- Understood logging levels: DEBUG / INFO / WARNING / ERROR / CRITICAL

### Week 1 — Day 3
- Used `schedule` to run job automatically every 5 minutes
- Learned the difference between `"w"` (overwrite) and `"a"` (append) in CSV
- Used `global` variable to share state between function calls
- Built a price change alert: triggers `logging.warning` when BTC moves over 1%
- Memorized correct startup sequence: root dir → activate venv → cd week1 → run script

### Week 1 — Day 4
- Installed `pandas` and `matplotlib` for data analysis and charting
- Read CSV into a DataFrame and renamed columns
- Converted string data to float using `astype(float)` for calculation
- Plotted a line chart with `df.plot()` and saved as PNG using `plt.savefig()`
- Learned `savefig()` vs `show()` difference, and supported export formats (PNG, PDF, SVG)
- Formatted datetime output using `strftime()` to remove microseconds
- Fixed `schedule` not running on startup by calling `job()` once before the loop
