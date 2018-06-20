from PIL import Image
# from urllib import request
import requests


def thumbnail_img(url, size=(64, 64), img_typ='.jpg'):
    """
    save thumbnail of img by url
    :param url:
    :param size:
    :param format:
    :return:
    """
    file_data = requests.get(url, stream=True).raw
    import time
    file_name = "{}_{}.{}".format(time.time(), url.replace('/', '_', -1), img_typ)
    # file_name = "test_{}.jpg"
    img = Image.open(file_data)
    # img.thumbnail(size)
    new_img = img.resize(size)
    new_img.save(file_name)
    print('saved..', file_name)


def main():

    # url = 'http://47.91.255.0/test.jpg'
    # thumbnail_img(url, size=(60, 45))
    import threading

    image_urls = [
        'http://47.91.255.0/test.jpg',
        'http://47.91.255.0/test.jpg',
        'http://47.91.255.0/test.jpg',
    ]

    for url in image_urls:
        t = threading.Thread(target=thumbnail_img, args=(url, ))
        t.start()

    import multiprocessing
    print('end')


if __name__ == '__main__':
    main()