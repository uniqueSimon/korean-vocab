"""Lektion 7: 🏆 정답과 성공 — Wahrheit, Wahl & Erfolg"""

TITLE = '🏆 정답과 성공 — Wahrheit, Wahl & Erfolg'
UNIT = 10  # TOPIK vocabulary PDF number; every word must be in it
ANKI_FILE = 'topik-10-truth-success.apkg'
IMG_PREFIX = 'topik10s'  # keep stable: Anki stores pictures by file name

# word, pronunciation, part of speech, German, English, OpenMoji codepoints (1-2), -요 form or None,
# example sentence (Korean, German, English), note
WORDS = [
    ('진실', '진실', 'n.', 'Wahrheit', 'truth', ['1F50D'], None, ('진실을 알아요.', 'Ich kenne die Wahrheit.', 'I know the truth.'), '진실을 말해요 = die Wahrheit sagen. Alltäglicher: 사실 = Tatsache.'),
    ('밝히다', '발키다', 'v.', 'aufdecken, klarstellen, erhellen', 'to reveal, to light up', ['1F526'], '밝혀요', ('그 사람이 진실을 밝혀요.', 'Die Person deckt die Wahrheit auf.', 'That person reveals the truth.'), '밝다 = hell → 밝히다 = hell machen, ans Licht bringen. Aussprache [발키다].'),
    ('사실', '사실', 'n.', 'Tatsache; eigentlich', 'fact; actually', ['1F4F0', '2705'], None, ('그건 사실이 아니에요.', 'Das stimmt nicht.', "That's not true."), '사실은 … = eigentlich, ehrlich gesagt: 사실은 저도 몰라요.'),
    ('정답', '정답', 'n.', 'richtige Antwort, Lösung', 'correct answer', ['2B55'], None, ('정답이 뭐예요?', 'Was ist die richtige Antwort?', 'What is the correct answer?'), '정 (richtig) + 답 (Antwort). 정답이에요! = Richtig! In Korea steht ⭕ für richtig.'),
    ('고르다', '고르다', 'v.', 'auswählen, aussuchen', 'to choose, to select', ['1F5F3'], '골라요', ('정답을 골라요.', 'Ich wähle die richtige Antwort.', 'I choose the correct answer.'), '르-unregelmäßig: 고르 + 아요 → 골라요 (wie 모르다 → 몰라요).'),
    ('직접', '직쩝', 'adv.', 'selbst, persönlich, direkt', 'directly, in person', ['1F64B'], None, ('제가 직접 만들었어요.', 'Ich habe es selbst gemacht.', 'I made it myself.'), 'Steht vor dem Verb: 직접 골라요 = selbst aussuchen. Aussprache [직쩝].'),
    ('실패하다', '실패하다', 'v.', 'scheitern, misslingen', 'to fail', ['1F4C9'], '실패해요', ('어제 다이어트에 실패했어요.', 'Gestern ist meine Diät gescheitert.', 'Yesterday I failed my diet.'), 'N에 실패하다. 실패 = Misserfolg. Gegenteil: 성공하다.'),
    ('성공하다', '성공하다', 'v.', 'Erfolg haben, gelingen', 'to succeed', ['1F3C6'], '성공해요', ('우리 팀이 성공했어요!', 'Unser Team hat es geschafft!', 'Our team succeeded!'), 'N에 성공하다. 성공 = Erfolg.'),
    ('다이어트', '다이어트', 'n.', 'Diät', 'diet', ['1F957', '1F3C3'], None, ('저는 다이어트를 해요.', 'Ich mache eine Diät.', "I'm on a diet."), 'Lehnwort aus dem Englischen (diet). 다이어트를 하다 = eine Diät machen.'),
    ('결심', '결씸', 'n.', 'Entschluss, Vorsatz', 'decision, resolution', ['1F4AA'], None, ('저는 결심했어요.', 'Ich habe einen Entschluss gefasst.', "I've made up my mind."), '결심하다 = sich fest vornehmen: 다이어트를 결심했어요. Aussprache [결씸].'),
]

# Zusammenhang tab: pairs shown side by side
PAIRS = [
    ('성공하다 🏆', '실패하다 📉'),
    ('정답 ⭕', '틀린 답 ❌'),
    ('진실 🔍', '비밀 🤫'),
]

# Zusammenhang tab: (pattern, explanation); HTML allowed
GRAMMAR = [
    ('-했어요 (Vergangenheit)', '하다 → 했어요: 실패했어요, 성공했어요, 결심했어요.'),
    ('르-unregelmäßig', '고르다 → 골라요, 모르다 → 몰라요: ㄹ wird verdoppelt, ㅡ fällt weg.'),
    ('N에 성공하다 / 실패하다', '다이어트에 성공했어요 = Die Diät hat geklappt. 다이어트에 실패했어요 = Die Diät ist gescheitert.'),
    ('사실은 …', 'Am Satzanfang „eigentlich, ehrlich gesagt“: 사실은 저도 다이어트를 했어요.'),
    ('-기로 결심하다', 'beschließen zu …: 운동하기로 결심했어요 = Ich habe beschlossen, Sport zu machen.'),
    ('Aussprache', '밝히다 [발키다], 직접 [직쩝], 결심 [결씸], 사실이 [사시리].'),
]

DIALOGUE_TITLE = ('다이어트', 'Die Diät')
# speaker A (female) / B (male), Korean, German, English
DIALOGUE = [
    ('A', '다이어트를 해요?', 'Machst du eine Diät?', 'Are you on a diet?'),
    ('B', '네, 어제 결심했어요.', 'Ja, gestern habe ich mich dazu entschlossen.', 'Yes, I decided yesterday.'),
    ('A', '사실은 저도 다이어트를 했어요.', 'Ehrlich gesagt habe ich auch eine Diät gemacht.', 'Actually, I was on a diet too.'),
    ('B', '정말요? 성공했어요?', 'Wirklich? Hat es geklappt?', 'Really? Did you succeed?'),
    ('A', '아니요, 실패했어요. 케이크가 정말 맛있어요!', 'Nein, gescheitert. Kuchen ist einfach so lecker!', 'No, I failed. Cake is just so tasty!'),
    ('B', '하하. 저는 매일 운동해요.', 'Haha. Ich mache jeden Tag Sport.', 'Haha. I work out every day.'),
    ('B', '음식은 직접 만들어요.', 'Das Essen koche ich selbst.', 'I make my food myself.'),
    ('A', '와, 화이팅! 꼭 성공해요!', 'Wow, viel Erfolg! Du schaffst das bestimmt!', "Wow, fighting! You'll make it!"),
]

STORY_TITLE = ('퀴즈 쇼', 'Die Quizshow')
# (Korean, German), one sentence each
STORY = [
    ('오늘 저는 퀴즈 쇼에 가요.', 'Heute gehe ich zu einer Quizshow.'),
    ('한 사람이 질문을 해요. „정답을 고르세요!“', 'Ein Mann stellt Fragen. „Wählen Sie die richtige Antwort!“'),
    ('이 문제는 쉬워요. 저는 빨리 정답을 골라요.', 'Diese Aufgabe ist leicht. Ich wähle schnell die richtige Antwort.'),
    ('그런데 이 질문은 어려워요.', 'Aber diese Frage ist schwer.'),
    ('„이건 사실이에요?“', '„Ist das eine Tatsache?“'),
    ('저는 몰라요. 그런데 직접 골라요.', 'Ich weiß es nicht. Aber ich entscheide selbst.'),
    ('„사실이 아니에요!“', '„Das stimmt nicht!“'),
    ('그 사람이 진실을 밝혀요.', 'Der Mann deckt die Wahrheit auf.'),
    ('„정답이에요!“', '„Richtig!“'),
    ('저는 퀴즈 쇼에서 성공했어요!', 'Ich habe es in der Quizshow geschafft!'),
    ('친구는 실패했어요.', 'Mein Freund ist gescheitert.'),
    ('우리는 같이 케이크를 먹어요.', 'Wir essen zusammen Kuchen.'),
    ('다이어트는 내일 결심해요!', 'Den Entschluss zur Diät fasse ich morgen!'),
]
