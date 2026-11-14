"""Lektion 5: 👪 우리 가족 — Familie & Alter"""

TITLE = '👪 우리 가족 — Familie & Alter'
UNIT = 9  # TOPIK vocabulary PDF number; every word must be in it
ANKI_FILE = 'topik-9-family.apkg'
IMG_PREFIX = 'topik9f'  # keep stable: Anki stores pictures by file name

# word, pronunciation, part of speech, German, English, OpenMoji codepoints (1-2), -요 form or None,
# example sentence (Korean, German, English), note
WORDS = [
    ('엄마', '엄마', 'n.', 'Mama, Mutter', 'mom, mother', ['1F469', '1F476'], None, ('우리 엄마는 의사예요.', 'Meine Mama ist Ärztin.', 'My mom is a doctor.'), '엄마 = Mama (familiär), höflich: 어머니. Papa = 아빠.'),
    ('오빠', '오빠', 'n.', 'älterer Bruder (einer Frau)', 'older brother (of a female)', ['1F467', '1F468'], None, ('저는 오빠가 있어요.', 'Ich habe einen älteren Bruder.', 'I have an older brother.'), 'Nur Frauen sagen 오빠. Männer sagen 형.'),
    ('동생', '동생', 'n.', 'jüngeres Geschwister', 'younger brother/sister', ['1F9D2'], None, ('동생이 있어요?', 'Hast du jüngere Geschwister?', 'Do you have a younger sibling?'), '여동생 = jüngere Schwester, 남동생 = jüngerer Bruder.'),
    ('태어나다', '태어나다', 'v.', 'geboren werden', 'to be born', ['1F476'], '태어나요', ('아이가 태어나요.', 'Ein Kind wird geboren.', 'A baby is born.'), 'Meist Vergangenheit: 서울에서 태어났어요 = Ich bin in Seoul geboren.'),
    ('아이', '아이', 'n.', 'Kind, Baby', 'child, kid', ['1F6DD'], None, ('아이가 몇 살이에요?', 'Wie alt ist das Kind?', 'How old is the child?'), '아이들 = Kinder. 어린 아이 = kleines Kind.'),
    ('어리다', '어리다', 'adj.', 'jung, klein (vom Alter)', 'to be young', ['1F423'], '어려요', ('동생은 나이가 어려요.', 'Mein Geschwister ist noch klein.', 'My sibling is young.'), 'Vor Nomen: 어린 아이. Gegenteil: 나이가 많다.'),
    ('나이', '나이', 'n.', 'Alter', 'age', ['1F382'], None, ('나이가 많아요.', 'Er/Sie ist alt.', 'He/She is old.'), 'Alter mit koreanischen Zahlen + 살: 다섯 살, 스물다섯 살.'),
    ('어른', '어른', 'n.', 'Erwachsener', 'adult, grown-up', ['1F9D1', '1F474'], None, ('오빠는 어른이에요.', 'Mein Bruder ist erwachsen.', 'My brother is an adult.'), '어른에게 [어르네게]: zu Erwachsenen spricht man höflich.'),
    ('인사하다', '인사하다', 'v.', 'grüßen', 'to greet', ['1F647'], '인사해요', ('선생님께 인사해요.', 'Ich grüße die Lehrerin.', 'I greet the teacher.'), '인사 = Gruß. 께 = höfliches 에게 (선생님께, 어른께).'),
]

# Zusammenhang tab: pairs shown side by side
PAIRS = [
    ('아이 🧒', '어른 🧑'),
    ('나이가 어려요 🐣', '나이가 많아요 🎂'),
    ('오빠 👧→👨', '형 👦→👨'),
]

# Zusammenhang tab: (pattern, explanation); HTML allowed
GRAMMAR = [
    ('오빠 / 형 · 언니 / 누나', 'Ältere Geschwister hängen vom Sprecher ab: Frau → 오빠 (Bruder), 언니 (Schwester); Mann → 형, 누나.'),
    ('N 살', 'Alter mit koreanischen Zahlen: 한 살, 다섯 살, 열아홉 살, 스물다섯 살. 몇 살이에요? = Wie alt?'),
    ('나이가 많다 / 어리다', 'alt / jung (Personen). 어리다 → 어려요; vor Nomen: 어린 아이.'),
    ('태어났어요', '„geboren werden“ steht meist in der Vergangenheit: 서울에서 태어났어요.'),
    ('N께 인사해요', '께 = höfliches 에게 für Respektspersonen: 선생님께, 어른께.'),
    ('Aussprache', '어른에게 [어르네게], 어린 아이 [어리나이]: der Endkonsonant bindet zum nächsten Vokal.'),
]

DIALOGUE_TITLE = ('우리 가족', 'Meine Familie')
# speaker A (female) / B (male), Korean, German, English
DIALOGUE = [
    ('A', '동생이 있어요?', 'Hast du jüngere Geschwister?', 'Do you have a younger sibling?'),
    ('B', '네, 여동생이 있어요. 나이가 어려요.', 'Ja, eine jüngere Schwester. Sie ist noch klein.', 'Yes, a younger sister. She is young.'),
    ('A', '동생은 몇 살이에요?', 'Wie alt ist sie?', 'How old is she?'),
    ('B', '다섯 살이에요.', 'Fünf Jahre.', "She's five."),
    ('A', '저는 오빠가 있어요.', 'Ich habe einen älteren Bruder.', 'I have an older brother.'),
    ('B', '오빠는 나이가 많아요?', 'Ist dein Bruder viel älter?', 'Is your brother much older?'),
    ('A', '스물다섯 살이에요. 어른이에요!', 'Er ist 25. Ein Erwachsener!', "He's 25. A grown-up!"),
    ('B', '오빠는 서울에서 태어났어요?', 'Ist dein Bruder in Seoul geboren?', 'Was your brother born in Seoul?'),
    ('A', '네, 우리 가족은 서울에서 태어났어요.', 'Ja, unsere Familie ist in Seoul geboren.', 'Yes, our family was born in Seoul.'),
]

STORY_TITLE = ('동생이 태어나요', 'Ein Geschwisterchen kommt')
# (Korean, German), one sentence each
STORY = [
    ('저는 학생이에요.', 'Ich bin Schülerin.'),
    ('저는 열아홉 살이에요.', 'Ich bin 19 Jahre alt.'),
    ('우리 엄마는 의사예요.', 'Meine Mama ist Ärztin.'),
    ('아빠는 회사원이에요.', 'Papa ist Angestellter.'),
    ('저는 오빠가 있어요.', 'Ich habe einen älteren Bruder.'),
    ('오빠는 스물다섯 살이에요. 어른이에요.', 'Mein Bruder ist 25. Er ist erwachsen.'),
    ('오늘 동생이 태어나요!', 'Heute wird mein Geschwisterchen geboren!'),
    ('아이가 정말 작아요.', 'Das Kind ist wirklich klein.'),
    ('저는 동생에게 인사해요. „안녕!“', 'Ich begrüße mein Geschwisterchen. „Hallo!“'),
    ('어른들이 아이를 봐요.', 'Die Erwachsenen schauen das Kind an.'),
    ('동생은 나이가 어려요. 그런데 정말 귀여워요.', 'Mein Geschwisterchen ist noch so klein. Aber wirklich süß.'),
    ('오늘은 정말 특별한 생일이에요.', 'Heute ist ein ganz besonderer Geburtstag.'),
]

DICTATION = [
    '동생이 있어요.',
    '아이가 태어나요.',
    '나이가 어려요.',
    '어른에게 인사해요.',
    '오빠는 스물다섯 살이에요.',
]
