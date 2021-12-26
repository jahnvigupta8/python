text = "X-DSPAM-Confidence:    0.8475";
epos = text.find(':')
print text[epos+1:]
