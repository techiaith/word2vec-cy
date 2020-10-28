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

# Example combining multiple words
similar_to_ysgol = model.most_similar(positive=['ysgol','darlithiau','myfyrwyr'],
                                         negative=["plant",'dosbarth','dosbarthiadau'], topn=1)

print (similar_to_ysgol)
# RESULTS: [('prifysgol', 0.34344300627708435)]

# The 'canonical' example of "king is to man as queen is to woman" in Welsh.
similar_to_brenin = model.most_similar(positive=['brenin', 'dynes'],negative=["dyn"], topn=2)
print (similar_to_brenin)
# RESULTS: [('brenhines', 0.5559254884719849), ('frenhines', 0.5395671129226685)]
