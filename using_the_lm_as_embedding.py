from flair.data import Sentence
from flair.embeddings import FlairEmbeddings

sentence = Sentence('расчете на душу населения ниже среднекраевого уровня приход на потребительский	 рынок г Алейска '
                    'крупных торговых сетей г Барнаула Мария-Ра Аникс Новэкс Магнит Холди и др отрицательно влияет на '
                    'динамику оборота розничной торговли района в районе не развито бытовое обслуживание населения '
                    'отсутствуют комплексные приемные пункты')

# init emdeddings from your trained LM
char_lm_embeddings = FlairEmbeddings('resources/taggers/language_model/best-lm.pt')

# embed sentence
print(char_lm_embeddings.embed(sentence))