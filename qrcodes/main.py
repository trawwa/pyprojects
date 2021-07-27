import pyqrcode
import png
from pyqrcode import QRCode

s = "https://www.google.com/search?q=%D1%82%D1%8B+%D0%BF%D0%B8%D0%B4%D0%BE%D1%80&client=ms-android-samsung-ss&prmd=ivmn&sxsrf=ALeKk01_dl5py4a3xfMIUUKIkVEEmwbGKQ:1627297276729&source=lnms&tbm=isch&sa=X&ved=2ahUKEwiR2v3gyoDyAhXgAxAIHe1VDioQ_AUoAXoECAMQAQ&biw=412&bih=814&dpr=2.63#imgrc=CbJhw_DQvEwl7M"
url = pyqrcode.create(s)
url.svg("myqr1.svg", scale = 8)
url.png('myqr1.png', scale = 6)