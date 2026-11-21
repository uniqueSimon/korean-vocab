"""Lektion 1: ⛰️ 산 위, 산 아래 — Messen, oben & unten"""

TITLE = '⛰️ 산 위, 산 아래 — Messen, oben & unten'
UNIT = 7  # TOPIK vocabulary PDF number; every word must be in it
ANKI_FILE = 'topik-7-up-down.apkg'
IMG_PREFIX = 'topik7'  # keep stable: Anki stores pictures by file name

# word, pronunciation, part of speech, German, English, OpenMoji codepoints (1-2), -요 form or None,
# example sentence (Korean, German, English), note
WORDS = [
    ('길이', '기리', 'n.', 'Länge, Abstand', 'length, distance', ['1F4CF', '2194'], None, ('다리 길이가 길어요.', 'Die Beinlänge ist lang.', 'The leg length is long.'), 'Von 길다 (lang) abgeleitet: 길다 → 길이. Ebenso 높다 → 높이.'),
    ('재다', '재다', 'v.', 'messen', 'to measure', ['1F4D0'], '재요', ('길이를 재요.', 'Ich messe die Länge.', 'I measure the length.'), 'Objekt mit 을/를: 온도를 재요, 길이를 재요.'),
    ('온도', '온도', 'n.', 'Temperatur', 'temperature', ['1F321'], None, ('온도를 재요.', 'Ich messe die Temperatur.', 'I measure the temperature.'), '온도가 높아요/낮아요 (nicht 크다/작다).'),
    ('높다', '놉따', 'adj.', 'hoch sein', 'to be high', ['26F0', '2B06'], '높아요', ('산이 높아요.', 'Der Berg ist hoch.', 'The mountain is high.'), 'Gegenteil: 낮다. Aussprache: ㅍ-Endung klingt wie ㅂ [놉따].'),
    ('낮다', '낟따', 'adj.', 'niedrig sein', 'to be low', ['1F3E0', '2B07'], '낮아요', ('산이 낮아요.', 'Der Berg ist niedrig.', 'The mountain is low.'), 'Gegenteil: 높다. Aussprache [낟따].'),
    ('산', '산', 'n.', 'Berg', 'mountain', ['26F0'], None, ('산에 올라가요.', 'Ich steige auf den Berg.', 'I climb the mountain.'), '산에 = auf/zum Berg (Ziel). Vgl. 산책하다 (spazieren) — anderes Wort.'),
    ('올라가다', '올라가다', 'v.', 'hinaufgehen, steigen', 'to go up', ['1F9D7', '2B06'], '올라가요', ('위로 올라가요.', 'Ich gehe nach oben.', 'I go up.'), '위로 = nach oben (Richtung 로). Gegenteil: 내려가다.'),
    ('내려가다', '내려가다', 'v.', 'hinuntergehen, sinken', 'to go down', ['1F6B6', '2B07'], '내려가요', ('아래로 내려가요.', 'Ich gehe nach unten.', 'I go down.'), '아래로 = nach unten. Gegenteil: 올라가다.'),
    ('위', '위', 'n.', 'oben, Oberseite', 'top, higher part', ['1F53C'], None, ('가방 위에 책이 있어요.', 'Auf der Tasche liegt ein Buch.', 'There is a book on the bag.'), 'Ortswort steht NACH dem Nomen: 가방 위에 (auf der Tasche).'),
    ('아래', '아래', 'n.', 'unten, Unterseite', 'bottom, lower part', ['1F53D'], None, ('산 아래에 집이 있어요.', 'Unter dem Berg ist ein Haus.', 'There is a house below the mountain.'), 'Gegenteil: 위. 아래에 = unten/darunter.'),
]

# Zusammenhang tab: pairs shown side by side
PAIRS = [
    ('높다 ⬆️', '낮다 ⬇️'),
    ('위 🔼', '아래 🔽'),
    ('올라가다 🧗', '내려가다 🚶'),
]

# Zusammenhang tab: (pattern, explanation); HTML allowed
GRAMMAR = [
    ('N 위에 / N 아래에', 'Das Ortswort steht NACH dem Nomen: 가방 위에 = auf der Tasche.'),
    ('위로 / 아래로', '로 = Richtung: nach oben / nach unten (위로 올라가요).'),
    ('산이 높아요', '높다/낮다 sind Adjektive → Subjekt mit 이/가. Auch: 온도가 높아요.'),
    ('길다 → 길이', 'Adjektiv-Stamm + 이 = Nomen (길다 → 길이, 높다 → 높이).'),
    ('온도를 재요', '재다 nimmt ein Objekt mit 을/를.'),
    ('Aussprache', '높다 [놉따], 낮다 [낟따]: Endkonsonant wird ㅂ/ㄷ.'),
]

DIALOGUE_TITLE = ('산에서', 'Am Berg')
# speaker A (female) / B (male), Korean, German, English
DIALOGUE = [
    ('A', '산이 높아요?', 'Ist der Berg hoch?', 'Is the mountain high?'),
    ('B', '네, 높아요. 위로 올라가요.', 'Ja, er ist hoch. Wir gehen nach oben.', "Yes, it's high. Let's go up."),
    ('A', '산 위는 온도가 낮아요?', 'Ist die Temperatur oben niedrig?', 'Is the temperature low at the top?'),
    ('B', '네, 낮아요. 온도를 재요.', 'Ja, niedrig. Wir messen die Temperatur.', "Yes, low. Let's measure the temperature."),
    ('A', '산 아래에 집이 있어요?', 'Gibt es unten am Berg ein Haus?', 'Is there a house at the foot of the mountain?'),
    ('B', '네, 있어요. 아래로 내려가요.', 'Ja. Wir gehen nach unten.', "Yes. Let's go down."),
    ('A', '이 산은 낮아요?', 'Ist dieser Berg niedrig?', 'Is this mountain low?'),
    ('B', '아니요, 높아요!', 'Nein, er ist hoch!', "No, it's high!"),
]

STORY_TITLE = ('산에 가요', 'Auf den Berg')
# (Korean, German), one sentence each
STORY = [
    ('오늘 날씨가 맑아요.', 'Heute ist das Wetter klar.'),
    ('저는 친구랑 산에 가요.', 'Ich gehe mit einem Freund auf den Berg.'),
    ('산이 높아요.', 'Der Berg ist hoch.'),
    ('우리는 산 위로 올라가요.', 'Wir steigen auf den Berg hinauf.'),
    ('산 아래에 호수가 있어요.', 'Unten am Berg ist ein See.'),
    ('산 위는 기온이 낮아요.', 'Oben auf dem Berg ist die Temperatur niedrig.'),
    ('친구가 온도를 재요.', 'Mein Freund misst die Temperatur.'),
    ('저는 텐트의 길이를 재요.', 'Ich messe die Länge des Zelts.'),
    ('우리는 산 위에서 라면을 먹어요.', 'Wir essen oben auf dem Berg Ramen.'),
    ('저녁에 아래로 내려가요.', 'Am Abend gehen wir hinunter.'),
]
