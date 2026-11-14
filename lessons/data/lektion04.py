"""Lektion 4: 🎬 영화와 모양 — Film, Form & Vergleich"""

TITLE = '🎬 영화와 모양 — Film, Form & Vergleich'
UNIT = 8  # TOPIK vocabulary PDF number; every word must be in it
ANKI_FILE = 'topik-8-movies-shapes.apkg'
IMG_PREFIX = 'topik8m'  # keep stable: Anki stores pictures by file name

# word, pronunciation, part of speech, German, English, OpenMoji codepoints (1-2), -요 form or None,
# example sentence (Korean, German, English), note
WORDS = [
    ('영화', '영화', 'n.', 'Film', 'movie', ['1F3AC'], None, ('영화를 봐요.', 'Ich schaue einen Film.', 'I watch a movie.'), '영화를 보다 = einen Film sehen (Objekt 을/를).'),
    ('만화', '만화', 'n.', 'Comic, Manga', 'comic, cartoon', ['1F4D6'], None, ('만화를 읽어요.', 'Ich lese einen Comic.', 'I read a comic.'), '만화 영화 = Zeichentrickfilm.'),
    ('제목', '제목', 'n.', 'Titel', 'title', ['1F3F7'], None, ('영화 제목이 뭐예요?', 'Wie heißt der Film? (Was ist der Titel?)', "What is the movie's title?"), 'N + 제목 = Titel von N (영화 제목, 책 제목).'),
    ('글', '글', 'n.', 'Text, Schrift', 'writing, text', ['1F4DD'], None, ('글을 써요.', 'Ich schreibe einen Text.', 'I write a text.'), '글을 쓰다 = Text schreiben; 글자 = Buchstabe.'),
    ('짓다', '짇따', 'v.', 'bauen; (Namen) geben', 'to build, make', ['1F3D7'], '지어요', ('제목을 지어요.', 'Ich denke mir einen Titel aus.', 'I make up a title.'), 'ㅅ-unregelmäßig: 짓 → 지어요. Auch: 집을 짓다 = ein Haus bauen.'),
    ('모양', '모양', 'n.', 'Form, Gestalt', 'shape', ['1F537'], None, ('별 모양이에요.', 'Es hat Sternform.', "It's star-shaped."), 'N 모양 = Form von N (별 모양, 하트 모양).'),
    ('별', '별', 'n.', 'Stern', 'star', ['2B50'], None, ('별이 예뻐요.', 'Die Sterne sind schön.', 'The stars are pretty.'), '별이 빛나다 = ein Stern leuchtet.'),
    ('다르다', '다르다', 'adj.', 'verschieden, anders sein', 'to be different', ['1F34E', '1F34A'], '달라요', ('모양이 달라요.', 'Die Form ist anders.', 'The shape is different.'), '르-unregelmäßig: 달라요. NICHT 틀리다 (= falsch sein)!'),
    ('같다', '갇따', 'adj.', 'gleich sein', 'to be the same', ['1F34E', '1F34E'], '같아요', ('모양이 같아요.', 'Die Form ist gleich.', 'The shape is the same.'), 'A와 같아요 = gleich wie A. Gegenteil: 다르다.'),
    ('서로', '서로', 'adv.', 'einander, gegenseitig', 'each other', ['1F91D'], None, ('서로 좋아해요.', 'Sie mögen einander.', 'They like each other.'), 'Adverb vor dem Verb: 서로 인사해요 = einander grüßen.'),
    ('열심히', '열씨미', 'adv.', 'fleißig, eifrig', 'hard, diligently', ['1F4AA'], None, ('열심히 공부해요.', 'Ich lerne fleißig.', 'I study hard.'), 'Vor dem Verb: 열심히 일해요 / 공부해요.'),
]

# Zusammenhang tab: pairs shown side by side
PAIRS = [
    ('같다 🍎🍎', '다르다 🍎🍊'),
    ('영화 🎬', '만화 📖'),
    ('제목 🏷️', '글 📝'),
]

# Zusammenhang tab: (pattern, explanation); HTML allowed
GRAMMAR = [
    ('A와/과 같아요', '„gleich wie“: 이것은 저것과 같아요. 같다 = gleich, 다르다 = anders (A와 달라요).'),
    ('다르다 → 달라요', '르-unregelmäßig: 다르 + 아요 → 달라요 (wie 모르다 → 몰라요).'),
    ('Adjektiv + 모양', '모양이 같아요 / 달라요; 별 모양 = Sternform (N + 모양).'),
    ('서로', 'Adverb „einander“: 서로 좋아해요. Steht vor dem Verb.'),
    ('열심히', 'Adverb „fleißig“: 열심히 공부해요 / 일해요. Vor dem Verb.'),
    ('짓다 → 지어요', 'ㅅ-unregelmäßig: ㅅ fällt vor Vokal weg (제목을 지어요, 집을 지어요).'),
    ('Aussprache', '짓다 [짇따], 같다 [갇따], 열심히 [열씨미].'),
]

DIALOGUE_TITLE = ('영화 제목', 'Filmtitel')
# speaker A (female) / B (male), Korean, German, English
DIALOGUE = [
    ('A', '어제 영화를 봤어요.', 'Gestern habe ich einen Film gesehen.', 'I watched a movie yesterday.'),
    ('B', '영화 제목이 뭐예요?', 'Wie heißt der Film?', "What's the movie's title?"),
    ('A', '「별」이에요. 만화 영화예요.', '„Stern“. Es ist ein Zeichentrickfilm.', 'It\'s "Star". It\'s an animated movie.'),
    ('B', '그래요? 저는 만화를 좋아해요.', 'Echt? Ich mag Comics.', 'Really? I like comics.'),
    ('A', '그림 모양이 정말 예뻐요. 별 모양이에요.', 'Die Zeichnungen sind wirklich schön. Sie haben Sternform.', 'The drawings are really pretty. Star-shaped.'),
    ('B', '저는 글을 써요. 제목을 지어요.', 'Ich schreibe Texte. Ich erfinde Titel.', 'I write texts. I make up titles.'),
    ('A', '우리는 취미가 같아요. 서로 열심히 해요!', 'Wir haben dasselbe Hobby. Lasst uns beide fleißig sein!', "We have the same hobby. Let's both work hard!"),
]

STORY_TITLE = ('영화 「별」', 'Der Film „Stern“')
# (Korean, German), one sentence each
STORY = [
    ('저는 친구랑 영화를 봐요.', 'Ich sehe mit einem Freund einen Film.'),
    ('우리는 표와 팝콘을 사요.', 'Wir kaufen Tickets und Popcorn.'),
    ('영화 제목은 「별」이에요.', 'Der Filmtitel ist „Stern“.'),
    ('만화 영화예요.', 'Es ist ein Zeichentrickfilm.'),
    ('영화에 별이 많아요.', 'Im Film gibt es viele Sterne.'),
    ('큰 별과 작은 별이 있어요.', 'Es gibt große und kleine Sterne.'),
    ('별의 모양이 서로 달라요.', 'Die Sterne haben verschiedene Formen.'),
    ('그런데 두 별은 모양이 같아요.', 'Aber zwei Sterne haben die gleiche Form.'),
    ('영화가 끝나요.', 'Der Film ist zu Ende.'),
    ('제 친구는 작가예요.', 'Mein Freund ist Autor.'),
    ('친구는 카페에서 열심히 글을 써요.', 'Mein Freund schreibt im Café fleißig einen Text.'),
    ('저는 그 글의 제목을 지어요.', 'Ich denke mir den Titel für den Text aus.'),
]

DICTATION = [
    '영화를 봐요.',
    '모양이 달라요.',
    '모양이 같아요.',
    '제목을 지어요.',
    '열심히 공부해요.',
]
