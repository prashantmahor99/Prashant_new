# Git & GitHub - DevOps Assignment

This repository is a ready-to-run Flask project used to practice the complete Git workflow required by the assignment: repository setup, SSH clone, branches, merges, conflict resolution, parallel feature development, sequential commits, soft reset, re-commit, rebase, and GitHub push.

## Application features

- `GET /api` reads JSON from `data/api_data.json` and returns it as JSON.
- `/` shows a To-Do form.
- `POST /submitto` accepts Item Name, Item Description, Item ID, Item UUID and Item Hash.
- Form data is stored in MongoDB Atlas.
- `/success` confirms a successful save.

## Run locally

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
# Edit .env and insert your MongoDB Atlas URI
python3 app.py
```

Open `http://127.0.0.1:5000/` and `http://127.0.0.1:5000/api`.

## Important

Do not commit `.env` or any real MongoDB password. Add genuine terminal/browser/GitHub screenshots to the `screenshots/` folder before final submission.
