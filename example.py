import gensim
from gensim.models import KeyedVectors

wv = KeyedVectors.load("word2vec.wordvectors", mmap='r')

print ("MODEL SIZE:", len(wv)) # 606,672

# Find words that are similar to 'athro' (=male teacher)
# whilst subtracting vectors associated with 'dynion' (='men')
similar_to_athro = wv.most_similar(positive=['athro','dynes'],negative=["dynion"], topn=10)

# The top result should be 'athrawes' (female teacher) as subtracting 'dynion' substracts
# both maleness and the plural aspect found in 'athrawon' (='teachers')
print (similar_to_athro)

# RESULTS
# [
#   ('athrawes', 0.6307817697525024),
#   ('addysgwr', 0.49690163135528564),
#   ('ymarferydd', 0.4902088940143585),
#   ('ymarferwr', 0.4869019687175751),
#   ('tiwtor', 0.47302836179733276),
#   ('Athrawes', 0.4660254120826721),
#   ('asesydd', 0.44042980670928955),
#   ('mentor', 0.43998128175735474),
#   ('cynorthwywraig', 0.43860816955566406),
#   ('aseswr', 0.43835097551345825)]


# Example combining multiple words
similar_to_ysgol = wv.most_similar(positive=['ysgol','darlithiau','myfyrwyr'],
                                         negative=["plant",'dosbarth','dosbarthiadau'], topn=3)

print (similar_to_ysgol)
# RESULTS:
# [('Athrofa', 0.34376001358032227),
#  ('prifysgol', 0.3392615020275116),
#  ('Prifysgol', 0.3346062898635864)]


# The 'canonical' example of "king is to man as queen is to woman" in Welsh.
similar_to_brenin = wv.most_similar(positive=['brenin', 'dynes'],negative=["dyn", "dynion"], topn=1)
print (similar_to_brenin)
# RESULTS: [('Brenhines', 0.2902812063694)]

