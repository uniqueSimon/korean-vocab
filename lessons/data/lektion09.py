"""Lektion 9: 🎧 건강과 이야기 — Körper, Gesundheit & Musik"""

TITLE = '🎧 건강과 이야기 — Körper, Gesundheit & Musik'
UNIT = 11  # TOPIK vocabulary PDF number; every word must be in it
ANKI_FILE = 'topik-11-health-music.apkg'
IMG_PREFIX = 'topik11a'  # keep stable: Anki stores pictures by file name

# word, pronunciation, part of speech, German, English, OpenMoji codepoints (1-2), -요 form or None,
# example sentence (Korean, German, English), note
WORDS = [
    ('점심시간', '점심시간', 'n.', 'Mittagspause', 'lunchtime', ['1F371'], None, ('점심시간에 밥을 먹어요.', 'In der Mittagspause esse ich.', 'I eat during lunchtime.'), '점심 (Mittagessen) + 시간 (Zeit). 점심시간은 보통 열두 시예요.'),
    ('천천히', '천천히', 'adv.', 'langsam', 'slowly', ['1F422'], None, ('천천히 말해 주세요.', 'Bitte sprechen Sie langsam.', 'Please speak slowly.'), 'Adverb auf -히, wie 열심히. Gegenteil: 빨리 = schnell.'),
    ('움직이다', '움지기다', 'v.', 'sich bewegen, bewegen', 'to move', ['1F3C3'], '움직여요', ('몸을 움직여요.', 'Ich bewege meinen Körper.', 'I move my body.'), 'Aussprache [움지기다]. Auch transitiv: 의자를 움직이다.'),
    ('몸', '몸', 'n.', 'Körper', 'body', ['1F4AA'], None, ('몸이 아파요.', 'Mein Körper tut weh. (Ich fühle mich krank.)', 'My body hurts.'), '몸이 좋아요 = fit sein, 몸에 좋아요 = gut für den Körper.'),
    ('건강', '건강', 'n.', 'Gesundheit', 'health, wellbeing', ['1F9D8'], None, ('건강이 좋아요.', 'Meine Gesundheit ist gut.', 'My health is good.'), '건강하다 = gesund sein. 건강에 좋아요 = gesund.'),
    ('나쁘다', '나쁘다', 'adj.', 'schlecht', 'bad', ['1F44E'], '나빠요', ('몸에 나빠요.', 'Das ist schlecht für den Körper.', "It's bad for your body."), 'ㅡ-Verb: 나쁘다 → 나빠요 (wie 쓰다 → 써요). Gegenteil: 좋다.'),
    ('재미있다', '재미읻따', 'adj.', 'interessant, lustig, spannend', 'interesting, fun', ['1F604'], '재미있어요', ('이 영화는 재미있어요.', 'Dieser Film ist spannend.', 'This movie is fun.'), '재미 = Spaß + 있다. Aussprache [재미읻따]. Oft = „macht Spaß“.'),
    ('재미없다', '재미업따', 'adj.', 'langweilig', 'not interesting', ['1F610'], '재미없어요', ('이 책은 재미없어요.', 'Dieses Buch ist langweilig.', 'This book is boring.'), 'Gegenteil von 재미있다. Aussprache [재미업따].'),
    ('이야기', '이야기', 'n.', 'Geschichte, Gespräch', 'story', ['1F4D6'], None, ('재미있는 이야기를 해요.', 'Ich erzähle eine spannende Geschichte.', 'I tell an interesting story.'), '이야기하다 = erzählen, sich unterhalten.'),
    ('듣다', '듣따', 'v.', 'hören, zuhören', 'to listen to, to hear', ['1F442'], '들어요', ('이야기를 들어요.', 'Ich höre die Geschichte.', 'I listen to the story.'), 'ㄷ-unregelmäßig: 듣다 → 들어요, 들었어요. Aber 닫다 → 닫아요 (regelmäßig).'),
    ('음악', '으막', 'n.', 'Musik', 'music', ['1F3B5'], None, ('음악을 좋아해요.', 'Ich mag Musik.', 'I like music.'), '음악을 듣다 = Musik hören. Aussprache [으막].'),
]

# Zusammenhang tab: pairs shown side by side
PAIRS = [
    ('재미있다 😄', '재미없다 😐'),
    ('몸에 좋아요 👍', '몸에 나빠요 👎'),
    ('천천히 🐢', '빨리 🐇'),
]

# Zusammenhang tab: (pattern, explanation); HTML allowed
GRAMMAR = [
    ('ㄷ-unregelmäßig', '듣다 → 들어요, 들었어요 (ㄷ wird vor einem Vokal zu ㄹ).'),
    ('ㅡ-Verben', '나쁘다 → 나빠요 (wie 크다 → 커요, 쓰다 → 써요).'),
    ('재미있다 / 재미없다', '재미 = Spaß. 있다/없다 → „hat Spaß“ = spannend, „hat keinen Spaß“ = langweilig.'),
    ('몸에 좋다 / 나쁘다', 'N에 좋아요 / 나빠요 = gut / schlecht für N: 몸에 좋아요, 건강에 나빠요.'),
    ('-히 → Adverb', '천천히 (langsam), 열심히 (fleißig): Adverbien auf -히 beschreiben, wie etwas geschieht.'),
    ('Aussprache', '음악 [으막], 움직이다 [움지기다], 재미있다 [재미읻따], 재미없다 [재미업따].'),
]

DIALOGUE_TITLE = ('점심시간', 'Mittagspause')
# speaker A (female) / B (male), Korean, German, English
DIALOGUE = [
    ('A', '점심시간이에요. 같이 밥 먹어요!', 'Mittagspause! Lass uns zusammen essen!', "It's lunchtime. Let's eat together!"),
    ('B', '좋아요. 그런데 몸이 안 좋아요.', 'Gern. Aber mir geht es nicht gut.', "Sure. But I don't feel well."),
    ('A', '왜요?', 'Warum?', 'Why?'),
    ('B', '어제 너무 많이 먹었어요.', 'Ich habe gestern zu viel gegessen.', 'I ate too much yesterday.'),
    ('A', '그건 몸에 나빠요. 천천히 먹어요.', 'Das ist schlecht für den Körper. Iss langsam.', "That's bad for your body. Eat slowly."),
    ('B', '네. 밥 먹고 조금 움직여요.', 'Ja. Nach dem Essen bewege ich mich ein bisschen.', "Yes. I'll move around a bit after eating."),
    ('A', '좋은 생각이에요! 저는 음악을 들어요.', 'Gute Idee! Ich höre Musik.', 'Good idea! I listen to music.'),
    ('B', '무슨 음악이에요?', 'Was für Musik?', 'What kind of music?'),
    ('A', '한국 음악이에요. 정말 재미있어요!', 'Koreanische Musik. Sie ist richtig gut!', "Korean music. It's really fun!"),
    ('B', '와, 저도 같이 들어요!', 'Wow, ich höre mit!', "Wow, I'll listen with you!"),
]

STORY_TITLE = ('점심시간', 'Die Mittagspause')
# (Korean, German), one sentence each
STORY = [
    ('점심시간이에요.', 'Es ist Mittagspause.'),
    ('저는 친구와 같이 밥을 먹어요.', 'Ich esse mit einem Freund zusammen.'),
    ('우리는 천천히 먹어요. 건강에 좋아요.', 'Wir essen langsam. Das ist gut für die Gesundheit.'),
    ('밥을 먹고 조금 움직여요.', 'Nach dem Essen bewegen wir uns ein bisschen.'),
    ('몸이 좋아요.', 'Der Körper fühlt sich gut an.'),
    ('친구가 재미있는 이야기를 해요.', 'Mein Freund erzählt eine spannende Geschichte.'),
    ('저는 이야기를 들어요.', 'Ich höre zu.'),
    ('이야기는 정말 재미있어요!', 'Die Geschichte ist wirklich spannend!'),
    ('그런데 어제 영화는 재미없었어요.', 'Aber der Film gestern war langweilig.'),
    ('저는 음악도 들어요.', 'Ich höre auch Musik.'),
    ('음악이 정말 좋아요.', 'Die Musik ist richtig schön.'),
    ('점심시간이 끝나요.', 'Die Mittagspause ist zu Ende.'),
]
