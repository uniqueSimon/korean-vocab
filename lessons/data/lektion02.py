"""Lektion 2: 🏫 수업 시간 — Im Klassenzimmer"""

TITLE = '🏫 수업 시간 — Im Klassenzimmer'
UNIT = 7  # TOPIK vocabulary PDF number; every word must be in it
ANKI_FILE = 'topik-7-classroom.apkg'
IMG_PREFIX = 'topik7c'  # keep stable: Anki stores pictures by file name

# word, pronunciation, part of speech, German, English, OpenMoji codepoints (1-2), -요 form or None,
# example sentence (Korean, German, English), note
WORDS = [
    ('책상', '책쌍', 'n.', 'Schreibtisch, Pult', 'desk', ['1F4DD', '1F4DA'], None, ('책상 위에 책이 있어요.', 'Auf dem Schreibtisch liegt ein Buch.', 'There is a book on the desk.'), '책 (Buch) + 상 (Tisch). Aussprache [책쌍].'),
    ('의자', '의자', 'n.', 'Stuhl', 'chair', ['1FA91'], None, ('의자 아래에 가방이 있어요.', 'Unter dem Stuhl ist eine Tasche.', 'There is a bag under the chair.'), 'Ortswort nach dem Nomen: 의자 아래에.'),
    ('앉다', '안따', 'v.', 'sich setzen, sitzen', 'to sit', ['1FA91', '2B07'], '앉아요', ('의자에 앉아요.', 'Ich setze mich auf den Stuhl.', 'I sit on the chair.'), 'Ziel mit 에: 의자에 앉아요. Aussprache [안따] (ㅈ bleibt stumm). Gegenteil: 일어나다.'),
    ('자리', '자리', 'n.', 'Platz, Sitzplatz', 'seat, spot', ['1F4BA'], None, ('여기 자리가 있어요.', 'Hier ist ein Platz frei.', 'There is a seat here.'), '자리에 앉다 = sich hinsetzen; 자리에서 일어나다 = aufstehen.'),
    ('일찍', '일찍', 'adv.', 'früh', 'early', ['1F305', '23F0'], None, ('일찍 일어나요.', 'Ich stehe früh auf.', 'I get up early.'), 'Adverb: steht vor dem Verb (일찍 끝나요).'),
    ('끝나다', '끈나다', 'v.', 'enden, zu Ende sein', 'to end, finish', ['1F3C1'], '끝나요', ('수업이 끝나요.', 'Der Unterricht endet.', 'The class ends.'), 'Intransitiv, Subjekt mit 이/가: 수업이 끝나요. Aussprache [끈나다].'),
    ('수업', '수업', 'n.', 'Unterricht, Kurs', 'class, lesson', ['1F469-200D-1F3EB'], None, ('한국어 수업이 있어요.', 'Ich habe Koreanischunterricht.', 'I have Korean class.'), '수업이 있어요 = es gibt Unterricht.'),
    ('걸리다', '걸리다', 'v.', 'dauern; hängen', 'to take (time); to hang', ['23F3'], '걸려요', ('한 시간이 걸려요.', 'Es dauert eine Stunde.', 'It takes one hour.'), 'Zeit: 시간이 걸려요 (한, 두, 세 시간). Auch: 그림이 걸려요 = das Bild hängt.'),
    ('그림', '그림', 'n.', 'Bild, Zeichnung', 'picture, drawing', ['1F5BC'], None, ('그림을 봐요.', 'Ich schaue ein Bild an.', 'I look at a picture.'), 'Verb dazu: 그림을 그리다 (ein Bild zeichnen) — kommt später.'),
]

# Zusammenhang tab: pairs shown side by side
PAIRS = [
    ('앉다 🪑', '일어나다 🧍'),
    ('수업 👩\u200d🏫', '끝나다 🏁'),
    ('책상 📚', '의자 🪑'),
]

# Zusammenhang tab: (pattern, explanation); HTML allowed
GRAMMAR = [
    ('N에 앉다', 'sich setzen <i>auf/an</i>: 의자에 앉아요, 자리에 앉아요.'),
    ('수업이 끝나요', '끝나다 ist intransitiv → Subjekt mit 이/가 (수업이, 시간이 …).'),
    ('시간이 걸려요', 'Dauer: 한 시간, 두 시간, 세 시간 + 이 걸려요. 걸리다 heißt auch „hängen“ (그림이 걸려요).'),
    ('일찍', 'Adverb vor dem Verb: 일찍 일어나요, 일찍 끝나요.'),
    ('Aussprache', '앉다 [안따], 끝나다 [끈나다], 책상 [책쌍].'),
]

DIALOGUE_TITLE = ('수업 시간에', 'Im Unterricht')
# speaker A (female) / B (male), Korean, German, English
DIALOGUE = [
    ('A', '여기 자리 있어요?', 'Ist hier ein Platz frei?', 'Is there a seat here?'),
    ('B', '네, 있어요. 의자에 앉아요.', 'Ja. Setz dich auf den Stuhl.', 'Yes. Sit on the chair.'),
    ('A', '수업이 일찍 끝나요?', 'Endet der Unterricht früh?', 'Does the class end early?'),
    ('B', '아니요, 한 시간이 걸려요.', 'Nein, es dauert eine Stunde.', 'No, it takes one hour.'),
    ('A', '책상 위에 그림이 있어요.', 'Auf dem Schreibtisch ist ein Bild.', 'There is a picture on the desk.'),
    ('B', '네, 그림을 봐요.', 'Ja, schau dir das Bild an.', 'Yes, look at the picture.'),
]

STORY_TITLE = ('한국어 학교', 'Die Schule')
# (Korean, German), one sentence each
STORY = [
    ('저는 학생이에요.', 'Ich bin Schüler.'),
    ('오늘 아침에 수업이 있어요.', 'Heute Morgen habe ich Unterricht.'),
    ('저는 버스로 학교에 가요.', 'Ich fahre mit dem Bus zur Schule.'),
    ('한 시간이 걸려요.', 'Es dauert eine Stunde.'),
    ('저는 일찍 가요.', 'Ich gehe früh los.'),
    ('학교에 책상과 의자가 많아요.', 'In der Schule gibt es viele Tische und Stühle.'),
    ('여기가 제 자리예요.', 'Hier ist mein Platz.'),
    ('저는 의자에 앉아요.', 'Ich setze mich auf den Stuhl.'),
    ('책상 위에 그림이 있어요.', 'Auf dem Tisch liegt ein Bild.'),
    ('예쁜 그림이에요.', 'Es ist ein schönes Bild.'),
    ('오늘은 수업이 일찍 끝나요.', 'Heute endet der Unterricht früh.'),
    ('저는 친구랑 카페에 가요.', 'Ich gehe mit einem Freund ins Café.'),
]
