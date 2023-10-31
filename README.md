# Model Iaith Fectorau Cymraeg

Model Iaith Fectorau Word2vec ar sail adnoddau ymchwil yr Uned Technolegau Iaith a gasglwyd o ffynonellau amrywiol.

*A Word2vec Language Model based on the Language Technologies Unit's research resources collected from various resources.*

Gweler https://github.com/techiaith/word2vec-cy/tags a chlicio ar 'Latest' i gael at y data.

*See https://github.com/techiaith/word2vec-cy/tags and click on 'Latest' to access the data.*

NODYN: Mae ffurfiau'r model hwn bellach i gyd mewn llythrennau bach.

*NOTE: The forms found found in this model are now in lower case.*

I'w ddefnyddio gyda Gensim 4:

*To use with Gensim 4:*

`pip install gensim`

Yna:

*Then:*

```
import gensim
from gensim.models import KeyedVectors

wv = KeyedVectors.load("word2vec.wordvectors", mmap='r')

print ("MODEL SIZE:", len(wv)) # 518,260


# Find words that are similar to 'athro' (=male teacher)
# whilst subtracting vectors associated with 'dynion' (='men')
similar_to_athro = wv.most_similar(positive=['athro','dynes'],negative=["dynion"], topn=10)

# The top result should be 'athrawes' (female teacher) as subtracting 'dynion' substracts
# both maleness and the plural aspect found in 'athrawon' (='teachers')
print (similar_to_athro)

# RESULTS
[('athrawes', 0.6490613222122192),
('addysgwr', 0.4838572144508362),
('ymarferydd', 0.4762175381183624),
('ymarferwr', 0.4626823663711548),
('aseswr', 0.462118536233902),
('tiwtor', 0.4528316557407379),
('hyfforddai', 0.4441806972026825),
('mentor', 0.43711039423942566),
('asesydd', 0.4269064962863922),
('prifathrawes', 0.4217046797275543)]
```

Ariannwyd creu'r model hwn gan Lywodraeth Cymru.

*The creation of this model was financed by the Welsh Government.*

