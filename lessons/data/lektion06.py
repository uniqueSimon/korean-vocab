"""Lektion 6: 🤫 비밀과 약속 — Vertrauen & Aufgaben"""

TITLE = '🤫 비밀과 약속 — Vertrauen & Aufgaben'
UNIT = 9  # TOPIK vocabulary PDF number; every word must be in it
ANKI_FILE = 'topik-9-promise-problem.apkg'
IMG_PREFIX = 'topik9p'  # keep stable: Anki stores pictures by file name

# word, pronunciation, part of speech, German, English, OpenMoji codepoints (1-2), -요 form or None,
# example sentence (Korean, German, English), note
WORDS = [
    ('믿다', '믿따', 'v.', 'glauben, vertrauen', 'to believe, to trust', ['1FAF6'], '믿어요', ('우리는 서로 믿어요.', 'Wir vertrauen einander.', 'We trust each other.'), 'N을/를 믿어요: 친구를 믿어요. Aussprache: 믿어요 [미더요].'),
    ('약속', '약쏙', 'n.', 'Versprechen, Verabredung', 'promise, appointment', ['1F91D'], None, ('내일 약속이 있어요.', 'Ich habe morgen eine Verabredung.', 'I have plans tomorrow.'), '약속하다 = versprechen. 약속해요? = Versprochen?'),
    ('지키다', '지키다', 'v.', 'halten, schützen, bewachen', 'to keep, to guard', ['1F6E1'], '지켜요', ('저는 약속을 지켜요.', 'Ich halte mein Versprechen.', 'I keep my promise.'), '약속을 지키다 = Versprechen halten, 나라를 지키다 = das Land verteidigen.'),
    ('나라', '나라', 'n.', 'Land, Staat', 'country, nation', ['1F1F0-1F1F7', '1F30F'], None, ('한국은 작은 나라예요.', 'Korea ist ein kleines Land.', 'Korea is a small country.'), '우리 나라 = unser Land (Koreaner meinen Korea). 다른 나라 = ein anderes Land.'),
    ('가르치다', '가르치다', 'v.', 'unterrichten, beibringen', 'to teach', ['1F9D1-200D-1F3EB'], '가르쳐요', ('선생님이 한국어를 가르쳐요.', 'Die Lehrerin unterrichtet Koreanisch.', 'The teacher teaches Korean.'), 'Gegenteil: 배우다 = lernen. 가르치 + 어요 → 가르쳐요.'),
    ('쉽다', '쉽따', 'adj.', 'leicht, einfach', 'to be easy', ['1F44C'], '쉬워요', ('이 문제는 쉬워요.', 'Diese Aufgabe ist leicht.', 'This question is easy.'), 'ㅂ-unregelmäßig: 쉽 → 쉬워요. Vor Nomen: 쉬운 문제.'),
    ('어렵다', '어렵따', 'adj.', 'schwierig, schwer', 'to be difficult', ['1F92F'], '어려워요', ('외국어는 어려워요.', 'Fremdsprachen sind schwierig.', 'Foreign languages are difficult.'), 'ㅂ-unregelmäßig: 어렵 → 어려워요. Vor Nomen: 어려운 문제.'),
    ('문제', '문제', 'n.', 'Problem, Aufgabe (im Test)', 'problem, question', ['2753', '1F4DD'], None, ('문제가 있어요.', 'Es gibt ein Problem.', 'There is a problem.'), '문제없어요 = kein Problem. 문제의 답 = die Lösung der Aufgabe.'),
    ('풀다', '풀다', 'v.', 'lösen', 'to solve, to untie', ['1F4A1'], '풀어요', ('동생이 문제를 풀어요.', 'Mein Geschwister löst die Aufgabe.', 'My sibling solves the problem.'), 'Auch: aufknoten, lüften. 비밀을 풀다 = ein Rätsel lösen.'),
    ('비밀', '비밀', 'n.', 'Geheimnis', 'secret', ['1F92B'], None, ('이건 비밀이에요!', 'Das ist ein Geheimnis!', "This is a secret!"), '비밀을 지키다 = ein Geheimnis bewahren. 이건 = 이것은. Aussprache: 비밀을 [비미를].'),
]

# Zusammenhang tab: pairs shown side by side
PAIRS = [
    ('쉽다 👌', '어렵다 🤯'),
    ('문제 ❓', '답 ✅'),
    ('가르치다 🧑‍🏫', '배우다 📖'),
    ('약속을 지키다 🤝', '비밀을 지키다 🤫'),
]

# Zusammenhang tab: (pattern, explanation); HTML allowed
GRAMMAR = [
    ('ㅂ-unregelmäßig', '쉽다 → 쉬워요, 어렵다 → 어려워요. Vor Nomen: 쉬운 문제, 어려운 문제.'),
    ('N을/를 지키다', '약속을 지켜요 (Versprechen halten), 비밀을 지켜요 (Geheimnis bewahren), 나라를 지켜요 (Land verteidigen).'),
    ('N에게 N을 가르치다', '동생에게 한국어를 가르쳐요 = Ich bringe meinem Geschwister Koreanisch bei.'),
    ('N을/를 믿다', '친구를 믿어요 = Ich vertraue meinem Freund. 서로 믿어요 = einander vertrauen.'),
    ('V-지 마세요', 'Bitte nicht …: 말하지 마세요 = Sag es nicht! 가지 마세요 = Geh nicht!'),
    ('Aussprache', '믿다 [믿따], 쉽다 [쉽따], 약속을 [약쏘글], 비밀을 [비미를].'),
]

DIALOGUE_TITLE = ('비밀이에요!', 'Das ist ein Geheimnis!')
# speaker A (female) / B (male), Korean, German, English
DIALOGUE = [
    ('A', '오빠, 이 문제가 어려워요.', 'Bruder, diese Aufgabe ist schwierig.', 'Brother, this question is hard.'),
    ('B', '제가 가르쳐요. 같이 풀어요!', 'Ich bringe es dir bei. Lösen wir sie zusammen!', "I'll teach you. Let's solve it together!"),
    ('A', '와, 정말 쉬워요!', 'Wow, das ist ja wirklich leicht!', "Wow, it's really easy!"),
    ('A', '오빠, 비밀이 있어요.', 'Bruder, ich habe ein Geheimnis.', 'Brother, I have a secret.'),
    ('B', '뭐예요?', 'Was denn?', 'What is it?'),
    ('A', '내일 엄마 생일이에요. 선물을 사요!', 'Morgen ist Mamas Geburtstag. Ich kaufe ein Geschenk!', "Tomorrow is Mom's birthday. I'm buying a present!"),
    ('A', '엄마에게 말하지 마세요. 약속해요?', 'Sag es Mama nicht. Versprochen?', "Don't tell Mom. Promise?"),
    ('B', '네, 약속해요. 비밀을 지켜요.', 'Ja, versprochen. Ich bewahre das Geheimnis.', "Yes, I promise. I'll keep the secret."),
    ('A', '오빠를 믿어요!', 'Ich vertraue dir!', 'I trust you!'),
]

STORY_TITLE = ('선생님의 문제', 'Die Aufgabe der Lehrerin')
# (Korean, German), one sentence each
STORY = [
    ('우리 선생님은 다른 나라에서 왔어요.', 'Unsere Lehrerin kommt aus einem anderen Land.'),
    ('선생님은 한국어를 가르쳐요.', 'Sie unterrichtet Koreanisch.'),
    ('한국어는 어려워요. 그런데 수업이 정말 좋아요.', 'Koreanisch ist schwer. Aber der Unterricht ist richtig gut.'),
    ('오늘 선생님이 문제를 줘요.', 'Heute gibt uns die Lehrerin Aufgaben.'),
    ('이 문제는 쉬워요. 저는 빨리 풀어요.', 'Diese Aufgabe ist leicht. Ich löse sie schnell.'),
    ('그런데 이 문제는 정말 어려워요.', 'Aber diese Aufgabe ist wirklich schwer.'),
    ('친구가 답을 알아요.', 'Mein Freund kennt die Antwort.'),
    ('친구가 말해요. „이건 비밀이에요!“', 'Mein Freund sagt: „Das ist ein Geheimnis!“'),
    ('저는 친구를 믿어요.', 'Ich vertraue meinem Freund.'),
    ('우리는 같이 문제를 풀어요.', 'Wir lösen die Aufgabe zusammen.'),
    ('선생님이 말해요. „답이 맞아요!“', 'Die Lehrerin sagt: „Die Antwort ist richtig!“'),
    ('우리는 매일 같이 공부해요. 그건 우리 약속이에요.', 'Wir lernen jeden Tag zusammen. Das ist unser Versprechen.'),
    ('우리는 약속을 지켜요.', 'Wir halten unser Versprechen.'),
]
