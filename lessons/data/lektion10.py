"""Lektion 10: 🚌 길과 교통 — Fluss, Bus & Straße"""

TITLE = '🚌 길과 교통 — Fluss, Bus & Straße'
UNIT = 11  # TOPIK vocabulary PDF number; every word must be in it
ANKI_FILE = 'topik-11-traffic.apkg'
IMG_PREFIX = 'topik11b'  # keep stable: Anki stores pictures by file name

# word, pronunciation, part of speech, German, English, OpenMoji codepoints (1-2), -요 form or None,
# example sentence (Korean, German, English), note
WORDS = [
    ('흐르다', '흐르다', 'v.', 'fließen', 'to flow', ['1F30A'], '흘러요', ('강이 흘러요.', 'Der Fluss fließt.', 'The river flows.'), 'ㄹ-Einschub (르-unregelmäßig): 흐르다 → 흘러요, wie 모르다 → 몰라요.'),
    ('강', '강', 'n.', 'Fluss', 'river', ['1F3DE'], None, ('강이 넓어요.', 'Der Fluss ist breit.', 'The river is wide.'), '한강 = der Han-Fluss in Seoul. 강 근처 = in der Nähe des Flusses.'),
    ('건너다', '건너다', 'v.', 'überqueren', 'to cross', ['1F309'], '건너요', ('강을 건너요.', 'Ich überquere den Fluss.', 'I cross the river.'), 'N을/를 건너다: 길을 건너다, 횡단보도를 건너다.'),
    ('횡단보도', '횡단보도', 'n.', 'Zebrastreifen', 'crosswalk', ['1F6A6'], None, ('횡단보도를 건너요.', 'Ich gehe über den Zebrastreifen.', 'I cross at the crosswalk.'), '횡단 (Überquerung) + 보도 (Gehweg). Aussprache [횡단보도].'),
    ('기다리다', '기다리다', 'v.', 'warten', 'to wait', ['23F3'], '기다려요', ('버스를 기다려요.', 'Ich warte auf den Bus.', "I'm waiting for the bus."), 'Im Koreanischen mit Akkusativ: N을/를 기다리다 = auf N warten.'),
    ('버스', '버스', 'n.', 'Bus', 'bus', ['1F68C'], None, ('버스가 와요.', 'Der Bus kommt.', 'The bus is coming.'), '버스 정류장 = Bushaltestelle.'),
    ('타다', '타다', 'v.', 'fahren (mit), einsteigen', 'to ride, to get on', ['1F68F'], '타요', ('버스를 타요.', 'Ich fahre mit dem Bus.', 'I take the bus.'), 'N을/를 타다 = mit N fahren (Bus, Zug, Taxi, Fahrrad). Auch: reiten, Ski fahren.'),
    ('내리다', '내리다', 'v.', 'aussteigen; fallen', 'to get off', ['1F6AA'], '내려요', ('여기에서 내려요.', 'Ich steige hier aus.', 'I get off here.'), 'N에서 내리다 = aus N aussteigen. Auch: 비가 내려요 = es regnet.'),
    ('차', '차', 'n.', 'Auto; Tee', 'car', ['1F697'], None, ('차가 많아요.', 'Es gibt viele Autos.', 'There are many cars.'), 'Dasselbe Wort bedeutet auch „Tee“ (녹차 = grüner Tee).'),
    ('운전하다', '운전하다', 'v.', 'Auto fahren, lenken', 'to drive', ['1F9D1', '1F697'], '운전해요', ('차를 운전해요.', 'Ich fahre Auto.', 'I drive a car.'), '운전 (das Fahren) + 하다. 운전사 = Fahrer(in).'),
    ('낮', '낟', 'n.', 'Tag (Tageszeit), Tagsüber', 'day, daytime', ['1F31E'], None, ('낮에 일해요.', 'Tagsüber arbeite ich.', 'I work during the day.'), 'Aussprache [낟]; 낮에 [나제]. Nicht verwechseln mit 낮다 (niedrig sein).'),
    ('밤', '밤', 'n.', 'Nacht', 'night', ['1F319'], None, ('밤에 자요.', 'Nachts schlafe ich.', 'I sleep at night.'), '밤에 [바메] = nachts. Gegenteil: 낮. Auch: Kastanie.'),
]

# Zusammenhang tab: pairs shown side by side
PAIRS = [
    ('낮 🌞', '밤 🌙'),
    ('타다 🚌', '내리다 🚪'),
    ('건너다 🚶', '기다리다 ⏳'),
]

# Zusammenhang tab: (pattern, explanation); HTML allowed
GRAMMAR = [
    ('르-unregelmäßig', '흐르다 → 흘러요 (wie 모르다 → 몰라요): vor -아/어 wird 르 zu ㄹ라 / ㄹ러.'),
    ('N을/를 타다', 'Im Koreanischen mit Akkusativ: 버스를 타요 (mit dem Bus fahren), 차를 타요.'),
    ('N에서 내리다', 'Aussteigen mit 에서: 여기에서 내려요, 강 근처에서 내려요.'),
    ('N을/를 기다리다', 'Warten auf + Akkusativ: 버스를 기다려요, 친구를 기다려요.'),
    ('N을/를 건너다', 'Überqueren + Akkusativ: 횡단보도를 건너요, 강을 건너요.'),
    ('낮에 / 밤에', '에 bei Tageszeiten: 낮에 = tagsüber, 밤에 = nachts. Aussprache 낮 [낟], 낮에 [나제].'),
]

DIALOGUE_TITLE = ('버스 정류장', 'An der Bushaltestelle')
# speaker A (female) / B (male), Korean, German, English
DIALOGUE = [
    ('A', '버스를 기다려요?', 'Wartest du auf den Bus?', 'Are you waiting for the bus?'),
    ('B', '네. 차가 많아서 늦어요.', 'Ja. Es sind viele Autos, deshalb kommt er spät.', "Yes. There are lots of cars, so it's late."),
    ('A', '저는 보통 버스를 타요.', 'Ich fahre normalerweise mit dem Bus.', 'I usually take the bus.'),
    ('B', '저도요. 운전은 어려워요.', 'Ich auch. Autofahren ist schwer.', 'Me too. Driving is hard.'),
    ('A', '어디에서 내려요?', 'Wo steigst du aus?', 'Where do you get off?'),
    ('B', '강 근처에서 내려요.', 'In der Nähe des Flusses.', 'Near the river.'),
    ('A', '강이 정말 예뻐요. 물이 천천히 흘러요.', 'Der Fluss ist richtig schön. Das Wasser fließt langsam.', 'The river is really pretty. The water flows slowly.'),
    ('B', '네. 횡단보도를 건너요. 그리고 강이 있어요.', 'Ja. Man geht über den Zebrastreifen, und da ist der Fluss.', "Yes. You cross the crosswalk, and there's the river."),
    ('A', '낮에도 예뻐요?', 'Ist er auch tagsüber schön?', 'Is it pretty during the day too?'),
    ('B', '낮에도 밤에도 예뻐요!', 'Tagsüber und nachts schön!', 'Pretty by day and by night!'),
]

STORY_TITLE = ('버스 여행', 'Eine Busfahrt')
# (Korean, German), one sentence each
STORY = [
    ('저는 버스 정류장에서 버스를 기다려요.', 'Ich warte an der Haltestelle auf den Bus.'),
    ('차가 정말 많아요.', 'Es sind wirklich viele Autos unterwegs.'),
    ('버스가 와요. 저는 버스를 타요.', 'Der Bus kommt. Ich steige ein.'),
    ('버스는 강을 건너요.', 'Der Bus überquert den Fluss.'),
    ('강이 천천히 흘러요.', 'Der Fluss fließt langsam.'),
    ('저는 횡단보도 앞에서 내려요.', 'Ich steige vor dem Zebrastreifen aus.'),
    ('횡단보도에서 친구를 기다려요.', 'Am Zebrastreifen warte ich auf meinen Freund.'),
    ('친구는 차를 운전해요.', 'Mein Freund fährt Auto.'),
    ('친구는 낮에 일해요.', 'Mein Freund arbeitet tagsüber.'),
    ('밤에 강은 정말 예뻐요.', 'Nachts ist der Fluss wirklich schön.'),
    ('우리는 같이 횡단보도를 건너요.', 'Wir überqueren zusammen den Zebrastreifen.'),
    ('오늘은 정말 좋은 날이에요!', 'Heute ist wirklich ein schöner Tag!'),
]
