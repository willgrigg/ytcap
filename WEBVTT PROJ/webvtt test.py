import webvtt

vtt_file_name = 'Messages For The Future'
transcript = open(vtt_file_name+' transcript.txt', 'a')

for caption in webvtt.read(vtt_file_name+'.vtt'):
##    print(caption.start)
##    print(caption.end)
    transcript.write(caption.text)

transcript.close()
