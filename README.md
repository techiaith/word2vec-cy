# Model Iaith Fectorau Cymraeg

Model Iaith Fectorau Word2vec ar sail adnoddau ymchwil yr Uned Technolegau Iaith a gasglwyd o ffynonellau amrywiol

*A Word2vec Language Model based on the Language Technologies Unit's research resources collected from various resources.*

Gweler https://github.com/techiaith/word2vec-cy/tags am ffeil .bin y model.

*See https://github.com/techiaith/word2vec-cy/tags for the model's .bin file.*

I'w ddefnyddio:

*To use:*

`pip install gensim`

Yna:

*Then:*

```
import gensim
from gensim.models import KeyedVectors

model = KeyedVectors.load_word2vec_format('model_w2v_cy_0_1a.bin', binary=True)

print ("MODEL SIZE:", len(model.vocab)) # 292,769

# Find words that are similar to 'athro' (=male teacher)
# whilst subtracting vectors associated with 'dynion' (='men')
similar_to_athro = model.most_similar(positive=['athro','dynes'],negative=["dynion"], topn=10)

# The top result should be 'athrawes' (female teacher) as subtracting 'dynion' substracts
# both maleness and the plural aspect found in 'athrawon' (='teachers')
print (similar_to_athro)

# RESULTS
# [('athrawes', 0.6252711415290833),
#  ('ymarferwr', 0.5185580253601074),
#  ('ymarferydd', 0.4801478385925293),
#  ('tiwtor', 0.4783634543418884),
#  ('aseswr', 0.47702139616012573),
#  ('addysgwr', 0.46662962436676025),
#  ('Athrawes', 0.4643784761428833),
#  ('mentor', 0.4534262418746948),
#  ('cymhorthydd', 0.44562190771102905),
#  ('hyfforddai', 0.44232702255249023)]
```

Ariannwyd creu'r model hwn gan Lywodraeth Cymru fel rhan o broject Iriaith.

*The creation of this model was financed by the Welsh Government as part of the Iriaith project.*

At ddiben gwerthuso'r project, mae rhestr o bob gair a'i fector cyfatebol ar gael fel a ganlyn:

*For project evaluation purposes, a list of all words and their corresponding vectors is available using:*

[Rhybudd: ~300k fector | Warning: ~300k vectors]

```
for word in enumerate(model.vocab):
    print (word, model[word])
```
