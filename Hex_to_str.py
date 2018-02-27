import unicodedata    
raw_text = u"here $%6757 dfgdfg"
convert = unicodedata.normalize('NFKD', raw_text).encode('ascii','ignore')


print convert
