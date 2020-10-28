# Model Iaith Fectorau Iriaith

Model Iaith Fectorau Word2vec ar sail CYMES, Corpws Ymchwil Mewnol Enfawr Safonol yr Uned Technolegau Iaith a gasglwyd o ffynonellau amrywiol at ddibenion ymchwil fel cynhyrchu modelau iaith. |  A Word2vec Language Model based on CYMES, the Language Technologies Unit Standard Large Research Corpus which was collected from various sources for research purposes including the development of language models.

I'w ddefnyddio | To use:

`pip install gensim`

Yna | Then:

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
```

For a list of all words and their corresponding vectors:  

[Rhybudd: ~300k fector | Warning: ~300k vectors]

```
for word in enumerate(model.vocab):
    print (word, model[word])
```
