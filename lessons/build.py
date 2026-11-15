#!/usr/bin/env python3
"""Builds every lesson in lessons/data/ into lessons/lektion-N/ plus the overview page ../index.html.

Each lesson = one data file lessons/data/lektionNN.py (words, dialog, story, dictation, grammar notes).
Output per lesson: index.html, audio/<speed>/*.mp3, img/*.png, anki/<ANKI_FILE> (cards with pictures, no audio).

Usage:  practice/.venv/bin/python lessons/build.py [N ...] [--no-audio]
        (no N = all lessons; the overview page is always rebuilt)
Pictures: OpenMoji (CC BY-SA 4.0, https://openmoji.org).
"""
import asyncio
import glob
import html
import importlib.util
import io
import json
import os
import re
import sys
import urllib.request

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)


def load(path, name):
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


base = load(os.path.join(ROOT, "practice", "build.py"), "base")  # PDF parsing + edge-tts helpers

VOICE_A, VOICE_B = base.VOICE_A, base.VOICE_B
# one native TTS take per tempo-slider step: (rate, read with commas between words so the voice pauses naturally)
RATES = {"s10": ("-10%", False), "s25": ("-25%", False), "s40": ("-40%", True), "s50": ("-50%", True)}
OPENMOJI = "https://cdn.jsdelivr.net/gh/hfg-gmuend/openmoji@15.0.0/color/618x618/{}.png"
ANKI_MODEL_ID, ANKI_DECK_ID, ANKI_DECK = 1788512780154, 1788523233273, "Koreanisch::Start"  # user's "Einfach" type / deck


def commas(text):
    return re.sub(r"(?<![,.?!]) ", ", ", text)


def picture(codes, prefix, img_dir):
    """Compose the emoji(s) on a soft background → img/<prefix>-<codes>.png."""
    from PIL import Image
    out = os.path.join(img_dir, prefix + "-" + "-".join(c.lower() for c in codes) + ".png")
    if os.path.exists(out):
        return out
    os.makedirs(img_dir, exist_ok=True)
    size = 300
    canvas = Image.new("RGB", (size * len(codes) + 40 * (len(codes) + 1), size + 80), "#f3f7ef")
    for i, code in enumerate(codes):
        raw = urllib.request.urlopen(OPENMOJI.format(code), timeout=30).read()
        im = Image.open(io.BytesIO(raw)).convert("RGBA").resize((size, size), Image.LANCZOS)
        canvas.paste(im, (40 + i * (size + 40), 40), im)
    canvas.save(out)
    return out


def anki(words, lesson, out_dir):
    import genanki
    css = (".card{font-family:arial;font-size:20px;line-height:1.5;text-align:center;color:black;background:white}"
           ".card img{max-width:260px;height:auto;border-radius:10px}")
    model = genanki.Model(
        ANKI_MODEL_ID, "Einfach",
        fields=[{"name": "Vorderseite"}, {"name": "Rückseite"}],
        templates=[{"name": "Karte 1", "qfmt": "{{Vorderseite}}",
                    "afmt": "{{FrontSide}}\n\n<hr id=answer>\n\n{{Rückseite}}"}], css=css)
    deck = genanki.Deck(ANKI_DECK_ID, ANKI_DECK)
    for w in words:
        front = (f"<img src='{os.path.basename(w['img'])}'><br><b>{w['de']}</b><br><br>"
                 f"<span style='color:#888'>{w['ex']['de']}</span>")
        yo = f" → {w['yo']}" if w["yo"] else ""
        back = (f"<span style='font-size:135%'><b>{w['word']}</b>{yo}</span> [{w['pron']}]"
                f"<br><br>{w['ex']['ko']}<br><span style='color:#888'>{w['ex']['de']}</span>"
                f"<br><br><span style='color:#888;font-size:85%'>{w['note']}</span>")
        # fixed GUID per word → re-importing updates the existing card instead of duplicating it
        deck.add_note(genanki.Note(model=model, fields=[front, back],
                                   tags=["koreanisch", f"topik{lesson.UNIT:02d}"],
                                   guid=genanki.guid_for(f"topik{lesson.UNIT}", w["word"])))
    os.makedirs(os.path.join(out_dir, "anki"), exist_ok=True)
    out = os.path.join(out_dir, "anki", lesson.ANKI_FILE)
    pkg = genanki.Package(deck)
    pkg.media_files = [w["img"] for w in words]
    pkg.write_to_file(out)
    return out


def build(n, lesson, vocab, with_audio):
    out_dir = os.path.join(HERE, f"lektion-{n}")
    audio_dir, img_dir = os.path.join(out_dir, "audio"), os.path.join(out_dir, "img")
    jobs = []
    name = lambda t, v=VOICE_A: base.audio_name(t, v, "")

    def clip(text, voice=VOICE_A):
        jobs.extend((commas(text) if c else text, voice, rate, os.path.join(audio_dir, d, name(text, voice)))
                    for d, (rate, c) in RATES.items())
        return name(text, voice)

    words = []
    for word, pron, pos, de, en, codes, yo, (ko, ex_de, ex_en), note in lesson.WORDS:
        assert word in vocab[lesson.UNIT], f"Lektion {n}: {word} is not in TOPIK PDF #{lesson.UNIT}"
        words.append({"word": word, "pron": pron, "pos": pos, "de": de, "en": en, "yo": yo, "note": note,
                      "img": picture(codes, lesson.IMG_PREFIX, img_dir), "audio": clip(word),
                      "yoAudio": clip(yo) if yo else None,
                      "ex": {"ko": ko, "de": ex_de, "en": ex_en, "audio": clip(ko)}})
    dialogue = [{"spk": spk, "ko": ko, "de": de, "en": en, "audio": clip(ko, VOICE_B if spk == "B" else VOICE_A)}
                for spk, ko, de, en in lesson.DIALOGUE]
    story = [{"ko": ko, "de": de, "audio": clip(ko)} for ko, de in lesson.STORY]
    dictation = [{"ko": ko, "audio": clip(ko)} for ko in lesson.DICTATION]

    if with_audio:
        for d in RATES:
            os.makedirs(os.path.join(audio_dir, d), exist_ok=True)
        asyncio.run(base.synthesize(jobs))

    data = {"words": [{**w, "img": "img/" + os.path.basename(w["img"])} for w in words],
            "pairs": lesson.PAIRS, "grammar": lesson.GRAMMAR,
            "dialogueTitle": lesson.DIALOGUE_TITLE, "dialogue": dialogue,
            "storyTitle": lesson.STORY_TITLE, "story": story, "dictation": dictation}
    with open(os.path.join(HERE, "template.html"), encoding="utf-8") as f:
        page = f.read()
    for key, value in {"N": str(n), "TITLE": html.escape(lesson.TITLE), "UNIT": str(lesson.UNIT),
                       "WORDLIST": " · ".join(w["word"] for w in words), "ANKI_FILE": lesson.ANKI_FILE}.items():
        page = page.replace("{{" + key + "}}", value)
    page = page.replace("/*DATA*/", "const DATA = " + json.dumps(data, ensure_ascii=False) + ";")
    with open(os.path.join(out_dir, "index.html"), "w", encoding="utf-8") as f:
        f.write(page)
    print(f"Lektion {n}: lessons/lektion-{n}/index.html, {os.path.relpath(anki(words, lesson, out_dir), ROOT)}")


OVERVIEW = """<!doctype html>
<html lang="de">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Korean · Lektionen</title>
<style>
  html, body { margin:0; height:100%; }
  body { display:flex; flex-direction:column; font-family:-apple-system, "Apple SD Gothic Neo", "Noto Sans KR", sans-serif; background:#f6f8f4; color:#222; }
  #lessons { display:flex; gap:6px; flex-wrap:nowrap; overflow-x:auto; -webkit-overflow-scrolling:touch; padding:8px 16px; background:#2e8b57; flex:none; }
  #lessons button { flex:none; white-space:nowrap; border:none; border-radius:8px; padding:6px 12px; cursor:pointer; background:#ffffff33; color:#fff; text-align:left; font-size:15px; font-weight:600; }
  #lessons button small { display:block; font-size:11px; font-weight:400; opacity:.9; }
  #lessons button.active { background:#fff; color:#2e8b57; }
  iframe { flex:1; width:100%; border:0; }
</style>
</head>
<body>
<nav id="lessons"></nav>
<iframe id="frame" title="Lektion"></iframe>
<script>
// generated by lessons/build.py
const LESSONS = /*LESSONS*/;
const nav = document.getElementById("lessons"), frame = document.getElementById("frame");
function show(i) {
  frame.src = LESSONS[i].dir + "/index.html";
  [...nav.children].forEach((b, j) => b.classList.toggle("active", j === i));
  nav.children[i].scrollIntoView({ block: "nearest", inline: "nearest" });
  location.hash = i + 1;
}
LESSONS.forEach((l, i) => {
  const b = document.createElement("button");
  b.innerHTML = `${l.name}<small>${l.note}</small>`;
  b.onclick = () => show(i);
  nav.appendChild(b);
});
const start = parseInt(location.hash.slice(1)) - 1;
show(start >= 0 && start < LESSONS.length ? start : LESSONS.length - 1);
</script>
</body>
</html>
"""


def overview(lessons, numbers):
    items = []
    for n, lesson in lessons:
        nums = sorted(numbers[lesson.UNIT, w[0]] for w in lesson.WORDS)
        items.append({"name": f"Lektion {n}", "dir": f"lessons/lektion-{n}",
                      "note": f"TOPIK #{lesson.UNIT} · Nr. {nums[0]}–{nums[-1]}"})
    with open(os.path.join(ROOT, "index.html"), "w", encoding="utf-8") as f:
        f.write(OVERVIEW.replace("/*LESSONS*/", json.dumps(items, ensure_ascii=False)))
    print("Overview: index.html")


def main():
    args = sys.argv[1:]
    lessons = []
    for path in sorted(glob.glob(os.path.join(HERE, "data", "lektion*.py"))):
        n = int(re.search(r"lektion(\d+)\.py$", path).group(1))
        lessons.append((n, load(path, f"lektion{n}")))
    seen = {}
    for n, lesson in lessons:
        for w in lesson.WORDS:
            assert w[0] not in seen, f"{w[0]} is in Lektion {seen[w[0]]} and Lektion {n}"
            seen[w[0]] = n

    pdf_vocab = base.parse_vocab()
    vocab, numbers = {}, {}
    for v in pdf_vocab:
        vocab.setdefault(v["unit"], set()).add(v["word"])
        numbers[v["unit"], v["word"]] = int(v["n"])
    wanted = {int(a) for a in args if a.isdigit()}
    for n, lesson in lessons:
        if not wanted or n in wanted:
            build(n, lesson, vocab, "--no-audio" not in args)
    overview(lessons, numbers)


if __name__ == "__main__":
    main()
