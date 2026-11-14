"""Lektion 3: 🙋 질문과 대답 — Fragen & Antworten"""

TITLE = '🙋 질문과 대답 — Fragen & Antworten'
UNIT = 8  # TOPIK vocabulary PDF number; every word must be in it
ANKI_FILE = 'topik-8-asking-answering.apkg'
IMG_PREFIX = 'topik8'  # keep stable: Anki stores pictures by file name

# word, pronunciation, part of speech, German, English, OpenMoji codepoints (1-2), -요 form or None,
# example sentence (Korean, German, English), note
WORDS = [
    ('질문', '질문', 'n.', 'Frage', 'question', ['2753'], None, ('질문이 있어요.', 'Ich habe eine Frage.', 'I have a question.'), '질문이 있어요 = „es gibt eine Frage“ (이/가).'),
    ('묻다', '묻따', 'v.', 'fragen', 'to ask', ['1F64B', '2753'], '물어요', ('이름을 물어요.', 'Ich frage nach dem Namen.', 'I ask (for) the name.'), 'ㄷ-unregelmäßig: 묻 → 물어요, 물었어요 (wie 듣다 → 들어요).'),
    ('대답하다', '대다파다', 'v.', 'antworten', 'to answer', ['1F642', '1F4AC'], '대답해요', ('질문에 대답해요.', 'Ich antworte auf die Frage.', 'I answer the question.'), '대답 + 하다. Auf eine Frage = 질문에 (에).'),
    ('답', '답', 'n.', 'Antwort, Lösung', 'answer', ['1F4A1'], None, ('답이 맞아요.', 'Die Antwort ist richtig.', 'The answer is correct.'), 'Kurzform von 대답. Auch: Lösung einer Aufgabe.'),
    ('맞다', '맏따', 'adj.', 'richtig sein, stimmen', 'to be correct', ['2B55'], '맞아요', ('그 답이 맞아요.', 'Diese Antwort ist richtig.', 'That answer is correct.'), 'Gegenteil: 틀리다. Mit 이/가: 답이 맞아요.'),
    ('틀리다', '틀리다', 'adj.', 'falsch sein', 'to be wrong', ['274C'], '틀려요', ('답이 틀려요.', 'Die Antwort ist falsch.', 'The answer is wrong.'), 'NICHT 다르다 (= anders sein)!'),
    ('이름', '이름', 'n.', 'Name', 'name', ['1F4DB'], None, ('이름이 뭐예요?', 'Wie heißt du? (Was ist dein Name?)', 'What is your name?'), '이름 + 이/가 뭐예요?'),
    ('적다', '적따', 'v.', 'aufschreiben, notieren', 'to write down', ['270D', '1F4DD'], '적어요', ('이름을 적어요.', 'Ich schreibe den Namen auf.', 'I write down the name.'), 'Achtung: 적다 = „wenig sein“ (적은 월급) — klingt gleich, Kontext entscheidet.'),
    ('말', '말', 'n.', 'Wort, Sprache, Gesagtes', 'speech, language, words', ['1F5E3'], None, ('말을 해요.', 'Ich spreche.', 'I speak.'), '말을 하다 = sprechen; 한국어로 말해요 = auf Koreanisch sprechen.'),
    ('외국어', '외구거', 'n.', 'Fremdsprache', 'foreign language', ['1F30D', '1F5E3'], None, ('외국어를 공부해요.', 'Ich lerne eine Fremdsprache.', 'I study a foreign language.'), '외국 (Ausland) + 어 (Sprache).'),
]

# Zusammenhang tab: pairs shown side by side
PAIRS = [
    ('맞다 ⭕', '틀리다 ❌'),
    ('질문 ❓', '답 💡'),
    ('묻다 🙋', '대답하다 💬'),
]

# Zusammenhang tab: (pattern, explanation); HTML allowed
GRAMMAR = [
    ('묻다 → 물어요', 'ㄷ-unregelmäßig: ㄷ wird vor Vokal zu ㄹ (듣다 → 들어요). 물었어요 = ich fragte.'),
    ('N에 대답해요', 'antworten <i>auf</i> etwas: 질문에 대답해요.'),
    ('답이 맞아요 / 틀려요', '맞다 und 틀리다 sind Adjektive → Subjekt mit 이/가.'),
    ('N로 말해요', 'in einer Sprache sprechen: 한국어로 말해요.'),
    ('이름이 뭐예요?', 'Wie heißt du? / Wie ist der Name?'),
    ('적다 (2×)', 'aufschreiben (이름을 적어요) <i>oder</i> wenig sein (월급이 적어요).'),
]

DIALOGUE_TITLE = ('한국어 수업', 'Koreanisch-Unterricht')
# speaker A (female) / B (male), Korean, German, English
DIALOGUE = [
    ('A', '질문이 있어요?', 'Hast du eine Frage?', 'Do you have a question?'),
    ('B', '네, 있어요. 이 답이 맞아요?', 'Ja. Ist diese Antwort richtig?', 'Yes. Is this answer correct?'),
    ('A', '아니요, 틀려요.', 'Nein, sie ist falsch.', "No, it's wrong."),
    ('B', '그럼 이 답이 맞아요?', 'Dann ist diese Antwort richtig?', 'Then is this answer correct?'),
    ('A', '네, 맞아요! 이름을 적어요.', 'Ja, richtig! Schreib den Namen auf.', 'Yes, correct! Write down your name.'),
    ('B', '네. 저는 외국어를 공부해요.', 'Ja. Ich lerne eine Fremdsprache.', 'Okay. I study a foreign language.'),
    ('A', '한국어로 말해요!', 'Sprich auf Koreanisch!', 'Speak in Korean!'),
]

STORY_TITLE = ('한국어 수업', 'Der Koreanischunterricht')
# (Korean, German), one sentence each
STORY = [
    ('오늘 한국어 수업이 있어요.', 'Heute habe ich Koreanischunterricht.'),
    ('한국어는 외국어예요.', 'Koreanisch ist eine Fremdsprache.'),
    ('저는 의자에 앉아요.', 'Ich setze mich auf den Stuhl.'),
    ('선생님이 한국어로 말해요.', 'Die Lehrerin spricht Koreanisch.'),
    ('저는 선생님의 말을 들어요.', 'Ich höre der Lehrerin zu.'),
    ('선생님이 제 이름을 물어요.', 'Die Lehrerin fragt nach meinem Namen.'),
    ('저는 한국어로 대답해요.', 'Ich antworte auf Koreanisch.'),
    ('선생님이 질문을 해요.', 'Die Lehrerin stellt eine Frage.'),
    ('저는 수첩에 답을 적어요.', 'Ich schreibe die Antwort in mein Notizbuch.'),
    ('이 답은 맞아요.', 'Diese Antwort ist richtig.'),
    ('그런데 저 답은 틀려요.', 'Aber jene Antwort ist falsch.'),
    ('수업이 일찍 끝나요.', 'Der Unterricht endet früh.'),
]

DICTATION = [
    '질문에 대답해요.',
    '답이 틀려요.',
    '이름을 적어요.',
    '이름을 물어요.',
    '외국어를 공부해요.',
]
