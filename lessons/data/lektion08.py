"""Lektion 8: 🏢 직장 생활 — Arbeit, Alltag & Müll"""

TITLE = '🏢 직장 생활 — Arbeit, Alltag & Müll'
UNIT = 10  # TOPIK vocabulary PDF number; every word must be in it
ANKI_FILE = 'topik-10-work-life.apkg'
IMG_PREFIX = 'topik10w'  # keep stable: Anki stores pictures by file name

# word, pronunciation, part of speech, German, English, OpenMoji codepoints (1-2), -요 form or None,
# example sentence (Korean, German, English), note
WORDS = [
    ('새롭다', '새롭따', 'adj.', 'neu, frisch', 'to be new, fresh', ['1F195'], '새로워요', ('기억이 새로워요.', 'Die Erinnerung ist noch frisch.', 'The memory is still fresh.'), 'ㅂ-unregelmäßig: 새로워요. Vor Nomen: 새로운 직장. Kurzform: 새 집.'),
    ('기억', '기억', 'n.', 'Erinnerung, Gedächtnis', 'memory', ['1F9E0'], None, ('좋은 기억이에요.', 'Das ist eine schöne Erinnerung.', "It's a good memory."), '기억하다 = sich erinnern. 기억을 잃다 = das Gedächtnis verlieren.'),
    ('잃어버리다', '이러버리다', 'v.', 'verlieren', 'to lose', ['1F45B', '2753'], '잃어버려요', ('지갑을 잃어버렸어요.', 'Ich habe meinen Geldbeutel verloren.', 'I lost my wallet.'), 'Meist Vergangenheit. Aussprache [이러버리다]: das ㅎ in 잃 ist stumm.'),
    ('줍다', '줍따', 'v.', 'aufheben, auflesen', 'to pick up', ['1F90F'], '주워요', ('쓰레기를 주워요.', 'Ich hebe Müll auf.', 'I pick up trash.'), 'ㅂ-unregelmäßig: 줍 → 주워요.'),
    ('버리다', '버리다', 'v.', 'wegwerfen', 'to throw away', ['1F6AE'], '버려요', ('휴지를 버려요.', 'Ich werfe das Taschentuch weg.', 'I throw away the tissue.'), '쓰레기를 버리다 = Müll wegbringen. Steckt auch in 잃어버리다.'),
    ('휴지', '휴지', 'n.', 'Taschentuch, Klopapier', 'tissue, toilet paper', ['1F9FB'], None, ('휴지 있어요?', 'Hast du ein Taschentuch?', 'Do you have a tissue?'), '휴지통 = Papierkorb, Mülleimer.'),
    ('쓰레기', '쓰레기', 'n.', 'Müll, Abfall', 'trash, rubbish', ['1F5D1'], None, ('쓰레기가 많아요.', 'Es gibt viel Müll.', "There's a lot of trash."), '쓰레기통 = Mülleimer.'),
    ('생활', '생활', 'n.', 'Leben, Alltag', 'life, living', ['1F3E1'], None, ('한국 생활은 어때요?', 'Wie ist das Leben in Korea?', 'How is life in Korea?'), '직장 생활 = Berufsleben, 학교 생활 = Schulleben.'),
    ('직장', '직짱', 'n.', 'Arbeitsplatz, Job', 'workplace, job', ['1F3E2'], None, ('직장에 다녀요.', 'Ich bin berufstätig.', 'I go to work.'), '직장인 = Berufstätige(r). Aussprache [직짱].'),
    ('출근', '출근', 'n.', 'Arbeitsbeginn, Weg zur Arbeit', 'going to work', ['1F305', '1F3E2'], None, ('출근 시간은 아홉 시예요.', 'Arbeitsbeginn ist um neun.', 'Work starts at nine.'), '출근하다 = zur Arbeit gehen: 아침에 출근해요.'),
    ('퇴근', '퇴근', 'n.', 'Feierabend', 'leaving work', ['1F306', '1F3E0'], None, ('퇴근 시간이에요!', 'Feierabend!', "It's time to go home!"), '퇴근하다 = Feierabend machen. Gegenteil: 출근.'),
]

# Zusammenhang tab: pairs shown side by side
PAIRS = [
    ('출근 🌅', '퇴근 🌆'),
    ('버리다 🚮', '줍다 🤏'),
    ('새 지갑 👛', '새로운 생활 🏡'),
]

# Zusammenhang tab: (pattern, explanation); HTML allowed
GRAMMAR = [
    ('출근하다 / 퇴근하다', 'Nomen + 하다 → Verb: 아침에 출근해요, 저녁에 퇴근해요.'),
    ('ㅂ-unregelmäßig', '줍다 → 주워요, 새롭다 → 새로워요 (wie 쉽다 → 쉬워요).'),
    ('-어버리다', '버리다 als Hilfsverb = „ganz weg, leider“: 잃어버렸어요 = (leider) verloren.'),
    ('새 / 새로운', '새 + Nomen (konkret): 새 지갑. 새로운 + Nomen (eher abstrakt): 새로운 생활, 새로운 직장.'),
    ('N통', '통 = Behälter: 쓰레기통, 휴지통 = Mülleimer.'),
    ('Aussprache', '잃어버리다 [이러버리다], 직장 [직짱], 새롭다 [새롭따].'),
]

DIALOGUE_TITLE = ('새로운 직장', 'Der neue Job')
# speaker A (female) / B (male), Korean, German, English
DIALOGUE = [
    ('A', '새로운 직장은 어때요?', 'Wie ist der neue Job?', "How's the new job?"),
    ('B', '좋아요. 그런데 아침 일찍 출근해요.', 'Gut. Aber ich muss früh morgens zur Arbeit.', 'Good. But I go to work early in the morning.'),
    ('A', '퇴근은 몇 시예요?', 'Wann hast du Feierabend?', 'What time do you get off?'),
    ('B', '여섯 시에 퇴근해요.', 'Um sechs.', 'I get off at six.'),
    ('A', '직장 생활은 어려워요?', 'Ist das Berufsleben schwer?', 'Is working life hard?'),
    ('B', '네, 어려워요. 그런데 사람들이 좋아요.', 'Ja, schon. Aber die Leute sind nett.', 'Yes, it is. But the people are nice.'),
    ('B', '아, 어제 지갑을 잃어버렸어요.', 'Ach, gestern habe ich meinen Geldbeutel verloren.', 'Oh, I lost my wallet yesterday.'),
    ('A', '정말요?', 'Wirklich?', 'Really?'),
    ('B', '네. 그런데 회사 사람이 지갑을 주웠어요!', 'Ja. Aber ein Kollege hat ihn aufgehoben!', 'Yes. But a coworker picked it up!'),
    ('A', '와, 좋은 사람이에요!', 'Wow, was für ein netter Mensch!', "Wow, what a nice person!"),
]

STORY_TITLE = ('새로운 생활', 'Ein neues Leben')
# (Korean, German), one sentence each
STORY = [
    ('저는 새로운 직장에 다녀요.', 'Ich habe einen neuen Job.'),
    ('아침 일찍 출근해요.', 'Ich gehe früh morgens zur Arbeit.'),
    ('버스 정류장에서 지갑을 잃어버렸어요!', 'An der Bushaltestelle habe ich meinen Geldbeutel verloren!'),
    ('그런데 한 사람이 지갑을 주웠어요.', 'Aber jemand hat ihn aufgehoben.'),
    ('그 사람은 우리 회사 사람이에요!', 'Die Person arbeitet in meiner Firma!'),
    ('회사 밖에 쓰레기가 많아요.', 'Draußen vor der Firma liegt viel Müll.'),
    ('우리는 같이 쓰레기를 주워요.', 'Wir sammeln zusammen den Müll auf.'),
    ('저는 휴지를 쓰레기통에 버려요.', 'Ich werfe die Taschentücher in den Mülleimer.'),
    ('직장 생활은 어려워요. 그런데 사람들이 좋아요.', 'Das Berufsleben ist schwer. Aber die Leute sind nett.'),
    ('저녁 여섯 시에 퇴근해요.', 'Um sechs Uhr abends habe ich Feierabend.'),
    ('오늘은 정말 좋은 기억이에요.', 'Heute ist eine richtig schöne Erinnerung.'),
    ('새로운 생활이 정말 좋아요!', 'Das neue Leben gefällt mir wirklich!'),
]
