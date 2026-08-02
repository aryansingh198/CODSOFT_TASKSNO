# CODSOFT_TASKSNO — Artificial Intelligence Internship

Virtual AI Internship @ [CodSoft](https://www.codsoft.in) | Duration: 05 July 2026 – 05 August 2026

This repo contains 3 completed tasks (minimum requirement) for the CodSoft AI internship.
Each task ships in **two forms**:
- a **CLI script** (`.py`) — the core algorithm, runnable in any terminal
- a **browser GUI** (`_gui.html`) — same logic ported to JS, for a clean demo-video experience (just double-click the file, no server needed)

## Tasks Completed

### Task 1 — Chatbot with Rule-Based Responses
Files: `task1_chatbot.py` · `task1_chatbot_gui.html`

A chatbot using regex pattern matching to identify user intent (greetings, time/date,
small talk, "who are you", etc.) and respond from predefined rule sets — the classic
intro to NLP and conversation flow, no ML model involved.

Run CLI:
```bash
python3 task1_chatbot.py
```
GUI: open `task1_chatbot_gui.html` in any browser — styled as a terminal-chat window.

### Task 2 — Tic-Tac-Toe AI
Files: `task2_tictactoe.py` · `task2_tictactoe_gui.html`

An unbeatable AI opponent built with the **Minimax algorithm + Alpha-Beta Pruning**.
Play as `X` against the AI (`O`).

Run CLI:
```bash
python3 task2_tictactoe.py
```
GUI: open `task2_tictactoe_gui.html` — clickable board with live win/draw/loss tracker.

### Task 4 — Recommendation System
Files: `task4_recommendation.py` · `task4_recommendation_gui.html`

A hybrid demo showing:
- **Content-Based Filtering** — recommends movies with similar genres via cosine similarity.
- **Collaborative Filtering** — recommends movies based on similar users' ratings.

Run CLI:
```bash
python3 task4_recommendation.py
```
GUI: open `task4_recommendation_gui.html` — pick a movie / user from a dropdown, see
live-ranked recommendations with similarity bars for both techniques side by side.

## Tech Stack
- Python 3 (standard library only — no external dependencies required)
- HTML / CSS / vanilla JS for the GUI versions (no build step, no server, no dependencies)
- Same algorithms implemented in both languages, so CLI output and GUI output always agree

## Author
Aryan Singh — B.Tech CSE, UTU Dehradun | Team AetherX

## Submission Checklist (per CodSoft instructions)
- [ ] Update LinkedIn profile
- [x] Push this repo to GitHub as `CODSOFT_TASKSNO`
- [ ] Record a short demo video for each task
- [ ] Post video on LinkedIn, tag @CODSOFT, use #codsoft #internship #artificialintelligence
- [ ] Submit GitHub repo link via the task submission form (shared by email)
