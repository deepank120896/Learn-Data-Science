import re

text = """Giraffes have aroused
 the curiosity of __PLURAL_NOUN__
 since earliest times. The
 giraffe is the tallest of all
 living __PLURAL_NOUN__, but
 scientists are unable to
 explain how it got its long
 __PART_OF_THE_BODY__. The
 giraffe's tremendous height,
 which might reach __NUMBER__
 __PLURAL_NOUN__, comes from
 it legs and __BODYPART__.
"""


def mad_libs(mls):
	print("\n")
	print("THE STORY ->")
	print(mls)
	print("\n")
	hints = re.findall('__.*?__',text)

	if hints is not None:
		for word in hints:
			q = "Enter a {} : ".format(word)
			new = input(q)
			mls = mls.replace(word,new,1)
		print("\n")
		mls = mls.replace("\n","")
		print(mls)
	else:
		print("Invalid mad libs string")

mad_libs(text)