#! python3
import pyperclip, re
#Find common typos such as multiple spaces between words, accidentally accidentally repeated words, or multiple exclamation marks at the end of sentences. Those are annoying!!


sentence = 'I need need to learn regex... regex from scratch!'

# remove punctuation
# the unicode flag makes it work for more letter types (non-ascii)
no_punc = re.sub(r'[^\w\s]', '', sentence, re.UNICODE)
print('No punctuation:', no_punc)

no_punc = re.sub(r'[^\w\s]', '', sentence, re.UNICODE)
print('No punctuation:', no_punc)

# remove duplicates
re_output = re.sub(r'\b(\w+)( \1\b)+', r'\1', no_punc)
print('No duplicates:', re_output)
