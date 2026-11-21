# Lessons

Each lesson is one data file in `data/`. Everything else (audio, pictures, Anki deck, HTML, overview tabs) is generated.

```
lessons/
  build.py              shared engine
  template.html         shared page template (Wörter, Zusammenhang, Dialog, Geschichte, Diktat)
  data/lektion01.py …   lesson content only
  lektion-1/ …          generated: index.html, audio/, img/, anki/*.apkg
../index.html           generated overview with one tab per lesson
```

## Add a lesson

1. Copy the latest data file, e.g. `data/lektion04.py` → `data/lektion05.py` (the number = lesson number).
2. Edit it: `TITLE`, `UNIT` (TOPIK PDF number), a new `ANKI_FILE` and `IMG_PREFIX`, then `WORDS`, `PAIRS`,
   `GRAMMAR`, `DIALOGUE`, `STORY`, `DICTATION`. Picture codes are OpenMoji/emoji codepoints (e.g. `"1F3AC"`).
3. Build (from the project root):

   ```
   practice/.venv/bin/python lessons/build.py 5     # only lesson 5 (+ overview)
   practice/.venv/bin/python lessons/build.py       # all lessons
   ```

   Add `--no-audio` to skip TTS while iterating on text. Existing audio and pictures are reused.
   Add `--anki-push` to add/update the cards directly in the running Anki desktop (needs the AnkiConnect add-on, code `2055492159`;
   existing cards are matched by their Korean word and updated). Then sync Anki to AnkiWeb for the iPhone.
   In the page itself, the Wörter tab has a **📥 In Anki übernehmen** button doing the same (desktop only). Add the page origin to
   AnkiConnect's config (Tools → Add-ons → AnkiConnect → Config) `webCorsOriginList`, e.g. `"https://uniquesimon.github.io"` (`"null"` for a local file).
4. Open `index.html`, import `lessons/lektion-5/anki/<ANKI_FILE>` into Anki.

The build checks that every word is in the given TOPIK PDF and isn't already used in another lesson.
Anki notes get a fixed GUID per word, so re-importing a deck updates the cards instead of duplicating them.

## Veröffentlichen (iPhone)

Live: https://uniquesimon.github.io/korean-vocab/

Nach einem Build: `git add -A && git commit -m "Lektion N" && git push` – GitHub Pages aktualisiert sich nach ~1 Minute.
