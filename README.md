# Nista's Goodbye Website 💗

A mobile-friendly Flask website with an interactive letter, floating hearts, optional music, and a final reveal.

## Run locally

1. Install Python 3.10+.
2. In this folder, run:
   ```bash
   python -m venv .venv
   ```
3. Activate the environment:
   - Windows: `.venv\Scripts\activate`
   - macOS/Linux: `source .venv/bin/activate`
4. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
5. Run locally:
   ```bash
   flask --app api.index run --debug
   ```
6. Open `http://127.0.0.1:5000`.

## Deploy on Vercel

1. Create a GitHub repository and upload `api/index.py`, `requirements.txt`, and `vercel.json`.
2. Go to https://vercel.com/ and sign in with GitHub.
3. Choose **Add New → Project**, import your repository, and deploy.
4. Vercel will provide a public HTTPS link you can send to Nista.

## Personalize it

- In `api/index.py`, edit the letter inside the `id="letter"` element.
- Change `Your roomie` to your name/nickname.
- To use your own music, replace the URL inside the `<source src="...">` element with a direct link to an audio file you have permission to use. Some audio hosts block direct playback; test it after deployment.
- You can add your own photos by placing them in a public folder and referencing their deployed URL in the HTML.

Note: browser autoplay restrictions mean music only starts after she taps the music button. Vercel's free-plan terms and deployment limits can change, so check the current Vercel dashboard/plan details.
