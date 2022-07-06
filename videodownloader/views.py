from __future__ import unicode_literals
import youtube_dl
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response


# facebook
def get_facebook_video(url):
    ydl_opts = {'nocheckcertificate': True}
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        url = ydl.extract_info(url, download=False)
        download_url = dict()
        download_url_audio = dict()
        download_url_video = dict()
        formats = url['entries'][0]['formats']
        print(formats)
        for format in formats:
            if 'height' and 'width' in format:
                if format['height'] is None and format['width'] is None:
                    audio_quality = format['format'].split()
                    download_url_audio[audio_quality[2]] = format['url']

                elif format['height'] is not None and format['width'] is not None:
                    video_quality = format['format'].split()
                    download_url_video[video_quality[2]] = format['url']
        download_url['audio_urls'] = download_url_audio
        download_url['video_urls'] = download_url_video
        return download_url


# tiktok with youtube_dl
# def get_tiktok_video(url):
#     ydl_opts = {'nocheckcertificate': True}
#     with youtube_dl.YoutubeDL(ydl_opts) as ydl:
#         url = ydl.extract_info(
#             'https://v16-webapp.tiktok.com/eaec1621a707df4efa6a2dbf792f81b0/62c454fc/video/tos/useast2a/tos-useast2a-pve-0037-aiso/8b1c2f22afb44046979ce7175693e32e/?a=1988&ch=0&cr=0&dr=0&lr=tiktok_m&cd=0%7C0%7C1%7C0&cv=1&br=4322&bt=2161&btag=80000&cs=0&ds=3&ft=eXd.6HKVMyq8ZIrjMwe2Ngnhml7Gb&mime_type=video_mp4&qs=0&rc=ZmRlNDhnNDQ0O2RlODRnPEBpamhtZWY6ZndoZDMzZjczM0BeXi5gNF9fNi4xXzMzNS8yYSMyb2locjRva25gLS1kMWNzcw%3D%3D&l=202207050912140102451582252210CA57',
#             download=False)
#         formats = url['formats']
#         download_url = dict()
#         url_count = 1
#         for format in formats:
#             download_url['url'+str(url_count)] = format['url']


# instagram
def get_instagram_video(url):
    ydl_opts = {'nocheckcertificate': True}
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        url = ydl.extract_info(url, download=False)
        formats = url['formats']
        download_url = dict()
        for format in formats:
            video_quality = format['format'].split()
            download_url[video_quality[2]] = format['url']
        download_url['audio_urls'] = dict()
    return download_url


# youtube
def get_youtube_video(url):
    ydl_opts = {'nocheckcertificate': True}
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        url = ydl.extract_info(url, download=False)
        formats = url['formats']
        download_url = dict()
        download_url_audio = dict()
        download_url_video = dict()
        for format in formats:

            if format['height'] is None and format['width'] is None:
                audio_quality = format['format'].split()
                download_url_audio[audio_quality[0]] = format['url']

            elif format['height'] is not None and format['width'] is not None:
                video_quality = format['format'].split()
                download_url_video[video_quality[2]] = format['url']
        download_url['audio_urls'] = download_url_audio
        download_url['video_urls'] = download_url_video
    return download_url


# twitter
def get_twitter_video(url):
    ydl_opts = {'nocheckcertificate': True}
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        url = ydl.extract_info(url, download=False)
        formats = url['formats']
        download_url = dict()
        for format in formats:
            video_quality = format['format'].split()
            download_url[video_quality[2]] = format['url']
        download_url['audio_urls'] = dict()
    return download_url


# snack video
def get_snackvideo_video(url):
    ydl_opts = {'nocheckcertificate': True}
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        url = ydl.extract_info(url, download=False)
        formats = url['formats']
        download_url = dict()
        for format in formats:
            download_url[str(format['height']) + '*' + str(format['width'])] = format['url']
        download_url['audio_urls'] = dict()
    return download_url


@api_view(['GET'])
def video_download(request):
    try:
        response = ''
        if request.method == 'GET':
            url = request.data.get('url')
            if 'facebook.com' in url:
                response = get_facebook_video(url)
            elif 'instagram.com' in url:
                response = get_instagram_video(url)
            elif 'youtube.com' in url:
                response = get_youtube_video(url)
            elif 'twitter.com' in url:
                response = get_twitter_video(url)
            # elif 'tiktok.com' in url:
            #     response = get_tiktok_video(url)
            elif 'snackvideo.com' in url:
                response = get_snackvideo_video(url)

            return Response({'data': response}, status=status.HTTP_200_OK)

    except Exception as e:
        return Response({'Error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
