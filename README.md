# Model Iaith Fectorau Cymraeg

Model Iaith Fectorau Word2vec ar sail adnoddau ymchwil yr Uned Technolegau Iaith a gasglwyd o ffynonellau amrywiol.

*A Word2vec Language Model based on the Language Technologies Unit's research resources collected from various resources.*

Gweler https://github.com/techiaith/word2vec-cy/tags a chlicio ar 'Latest' i gael at y data.

*See https://github.com/techiaith/word2vec-cy/tags and click on 'Latest' to access the data.*

NODYN: Mae'r model hwn ddwywaith yn fwy na'r model blaenorol (600k vs 300k), ond, oherwydd newidiadau i'r fersiwn ddiweddaraf o Gensim, nid oedd modd i ni hidlo geirffurfiau annilys ohono.  
O ganlyniad, mae'r model yn cynnwys tocynnau fel 'Bangor1' a '•Darlithydd' nad ydynt yn cynrychioli geirffurfiau dilys.  
Bwriadwn geisio datrys hyn yn y dyfodol. Yn y cyfamser, oherwydd y cynnydd ym maint y ffeil, dosbarthwn y 'Keyed Vectors' (y fectorau a'u hallweddi) yn hytrach na ffeil .bin y "model" go iawn.

*NOTE: This model is twice the size of the previous model (600k vs 300k), but, due to changes in the latest version of Gensim, some of this increase in size is because we have not been able to filter out non-valid wordforms.*  
*As a result, the model includes vectors for tokens such as 'Bangor1' and '•Darlithydd' which do not represent valid wordforms.*  
*We will attempt to mitigate this in future versions. In the meantime, due to the increase in the size of the files, we have changed to distributing the keyed vectors file rather than the true binary "model".*

I'w ddefnyddio gyda Gensim 4:

*To use with Gensim 4:*

`pip install gensim`

Yna:

*Then:*

```
import gensim
from gensim.models import KeyedVectors

wv = KeyedVectors.load("word2vec.wordvectors", mmap='r')

print ("MODEL SIZE:", len(wv)) # 606,672


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

Ariannwyd creu'r model hwn gan Lywodraeth Cymru.

*The creation of this model was financed by the Welsh Government.*

