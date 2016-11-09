# OneKeyUploadImage
## Abstract
OneKeyUploadImage is a project to help you upload image saved in clipboard by srceenshot software with onekey.可以帮助你一键上传截屏软件保存在剪切板中的图片。

**If you feel this project does make you upload images conveniently,please do not hesitate to star the project.**

I will write Readme in next days...


## Usage
### Install Modules
To use this project,please insure that you have install these modules:

	from pynput.keyboard import Key, Listener
	
	from qiniu import *
	import qiniu.config
	from win32con import *
	import win32clipboard
	import ctypes
	from ctypes.wintypes import *
	import sys
	import time
	import os
	from PIL import Image
	from qiniu.services.storage.upload_progress_recorder import UploadProgressRecorder
    
### Run
- Download this project
- Modify your own config in the file "uploadImage.py".

        	access_key = "7E1ZYNajHehnCRrBAutgcdz3Q5T4_2bgxXq8_TnB"
	        secret_key = "gm-Wbv8-N5NanZS-l2CuKiYvChCfBA4Evzv8DhIE"
	        bucket_name = "orzangleli"
	        domain_name = "7xrrni.com1.z0.glb.clouddn.com"
    
- Open the file *main_keyListener.py* in the IDLE
- Run the script.

Now,if you take a srceenshot into the clipboard,you can just press "Shift + Alt + A" to activate the script tu upload the image.
After sveral seconds,you will hava a markdown image tag in your clipboard,you can just press "Ctrl + V" to paste that.

Default I compress the image into "webp" format.


## MIT License

Copyright (c) 2016 orzangleli

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
