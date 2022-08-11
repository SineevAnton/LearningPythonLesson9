import pafy

print('Wanna download some video from youtube? Please enter the URL: ')
url = input()
#url = 'https://www.youtube.com/watch?v=KXVGCngSd7o'

def download(url):
    try:
        v = pafy.new(url)
        streams = v.streams

        avaliable_streams = {}
        count = 1

        for stream in streams:
            avaliable_streams[count] = stream
            print(f'{count}: {stream}')
            count += 1

        stream_count = int(input("Choose the number: "))
        d = streams[stream_count - 1].download()

        print('Downloading successful!')

    except:
        print('Something wrong...')

download(url)