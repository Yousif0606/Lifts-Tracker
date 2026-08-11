# Lifts-Tracker

A command-line tool for tracking progressive overload in the gym.

Set up a workout split for each day of the week, log weight/reps/sets each
session, and see your progress over time as a percentage above your starting
weight — all persisted to a local JSON file between runs.

## Features

- Set up a workout split per day of the week (Mon–Sun)
- Log weight (kg), reps, and sets per exercise, with every session saved as
  its own dated entry — full history, not just the latest number
- Automatic progressive-overload tracking: shows `%` change from your first
  logged (baseline) weight for that exercise
- Replace or delete an exercise from a day's split, with confirmation before
  anything destructive
- Persists between runs via `workouts.json` — pick up where you left off

## Usage

```sh
python3 main.py
```

You'll get a simple menu:

```
l - log weight | c - change weight | q - quit
```

- **l** — log a session: pick a day, then either build out that day's split
  (first time) or log a new weight/reps/sets for each exercise already on it
  (type `same` to leave a value unchanged)
- **c** — pick a day, then an exercise on it, and either replace it with a
  fresh exercise or delete it from the split
- **q** — save and exit

## Running tests

```sh
python3 -m unittest discover -v
```

## Project structure

- `main.py` — entry point; loads saved data, starts the menu
- `tracker.py` — app logic: the menu loop, logging/adding/changing exercises
- `storage.py` — reads and writes `workouts.json`; knows nothing about
  exercises, just persists whatever dict it's given
- `test_tracker.py`, `test_storage.py` — unit tests

## Status

Core loop is working end-to-end (set up a split, log sessions, track
progress, persist across runs). Possible next steps: refactor the core
logic into classes, maybe a lightweight UI on top of the same tracker logic.

## Built with

Python 3, stdlib only (`unittest` for tests) — no external dependencies.