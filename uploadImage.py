from qiniu import *
import qiniu.config
import json
from win32con import *
import win32clipboard
import ctypes
from ctypes.wintypes import *
import sys
import time
import os
from PIL import Image
from qiniu.services.storage.upload_progress_recorder import UploadProgressRecorder

class BITMAPFILEHEADER(ctypes.Structure):
    _pack_ = 1  # structure field byte alignment
    _fields_ = [
        ('bfType', WORD),  # file type ("BM")
        ('bfSize', DWORD),  # file size in bytes
        ('bfReserved1', WORD),  # must be zero
        ('bfReserved2', WORD),  # must be zero
        ('bfOffBits', DWORD),  # byte offset to the pixel array
    ]
SIZEOF_BITMAPFILEHEADER = ctypes.sizeof(BITMAPFILEHEADER)

class BITMAPINFOHEADER(ctypes.Structure):
    _pack_ = 1  # structure field byte alignment
    _fields_ = [
        ('biSize', DWORD),
        ('biWidth', LONG),
        ('biHeight', LONG),
        ('biPLanes', WORD),
        ('biBitCount', WORD),
        ('biCompression', DWORD),
        ('biSizeImage', DWORD),
        ('biXPelsPerMeter', LONG),
        ('biYPelsPerMeter', LONG),
        ('biClrUsed', DWORD),
        ('biClrImportant', DWORD)
    ]
SIZEOF_BITMAPINFOHEADER = ctypes.sizeof(BITMAPINFOHEADER)

def GetNowTime():
    return time.strftime("%Y-%m-%d_%H_%M_%S",time.localtime(time.time()))

def uploadImage(localfile,access_key,secret_key,bucket_name):
        print("aaa")
        q = Auth(access_key, secret_key)
        #服务器上的文件名
        key = localfile
        print("bbb")
        token = q.upload_token(bucket_name, key, 3600)
        print("ccc")
        #要上传文件的本地路径
        put_file(token, key, localfile)
        print("ddd")
        ret, info = put_file(token, key, localfile,upload_progress_recorder= UploadProgressRecorder())
        print(info)
        return key

def set_clipboard(text):
	win32clipboard.OpenClipboard()
	win32clipboard.EmptyClipboard()
	win32clipboard.SetClipboardText(text.encode('utf-8'),
					win32clipboard.CF_TEXT)
	win32clipboard.CloseClipboard()

def upload():
    win32clipboard.OpenClipboard()
    try:
        if win32clipboard.IsClipboardFormatAvailable(win32clipboard.CF_DIB):
            data = win32clipboard.GetClipboardData(win32clipboard.CF_DIB)
        else:
            print('clipboard does not contain an image in DIB format')
            sys.exit(1)
    finally:
        win32clipboard.CloseClipboard()

    bmih = BITMAPINFOHEADER()
    ctypes.memmove(ctypes.pointer(bmih), data, SIZEOF_BITMAPINFOHEADER)
    
    #这个验证有问题，会让正常的图片无法通过
    #if bmih.biCompression != BI_BITFIELDS:  # RGBA?
        #print('insupported compression type {}'.format(bmih.biCompression))
        #sys.exit(1)

    bmfh = BITMAPFILEHEADER()
    ctypes.memset(ctypes.pointer(bmfh), 0, SIZEOF_BITMAPFILEHEADER)  # zero structure
    bmfh.bfType = ord('B') | (ord('M') << 8)
    bmfh.bfSize = SIZEOF_BITMAPFILEHEADER + len(data)  # file size
    SIZEOF_COLORTABLE = 0
    bmfh.bfOffBits = SIZEOF_BITMAPFILEHEADER + SIZEOF_BITMAPINFOHEADER + SIZEOF_COLORTABLE

    #webp格式加载速度快,需要转化为webp
    bmp_filename = '%s.png'%GetNowTime()
    with open(bmp_filename, 'wb') as bmp_file:
        bmp_file.write(bmfh)
        bmp_file.write(data)
        bmp_file.close()
        
    #转换格式,经测试显示效果无异，webp所占空间仅为png的1% ，截图在这里：![](http://7xrrni.com1.z0.glb.clouddn.com/2016-11-08_17_24_41.png.webp?imageView2/0/w/800)
    im = Image.open(bmp_filename)
    f,ext = os.path.splitext(bmp_filename)
    webp_path = "%s.webp"%f
    im.save(webp_path, "WEBP")

    access_key = "7E1ZYNajHehnCRrBAutgcdz3Q5T4_2bgxXq8_TnB"
    secret_key = "gm-Wbv8-N5NanZS-l2CuKiYvChCfBA4Evzv8DhIE"
    bucket_name = "orzangleli"
    domain_name = "7xrrni.com1.z0.glb.clouddn.com"
    try:
        key = uploadImage(webp_path,access_key,secret_key,bucket_name)
    except Exception as e:
        print("发生错误:%s"%e)
    else:
        #print(os.getcwd())
        os.remove("%s\%s"%(os.getcwd(),bmp_filename))
        os.remove("%s\%s"%(os.getcwd(),webp_path))
        #800表示如果图片长度超过800，则长度变为800，宽度自动缩放
        set_clipboard("![](http://%s/%s?imageView2/0/w/800)"%(domain_name,key))
    

if __name__ == "__main__":
    upload()


































    
