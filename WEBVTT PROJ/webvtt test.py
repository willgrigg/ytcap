import webvtt

# I wanted the file to to open in 'Create' mode ('x').
# This just ensures that I don't overwrite a pre-existing file.

vtt_file_name = 'Messages For The Future'
file = open(vtt_file_name+' transcript.txt', 'x')

# Holds the normalized caption text
text = ''

# Appends each caption to the text variable
for caption in webvtt.read(vtt_file_name+'.vtt'):
    text += caption.text + ' '

# Newlines are replaced w/ spaces to increase readability
text = text.replace('\n', ' ')
file.write(text)

file.close()
