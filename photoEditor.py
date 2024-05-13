#pillow kutuphanesi icinden kullanacagimiz kutuphaneleri import ettik
#pillow indirmek icin python -m pip install pillow
from PIL import Image , ImageEnhance , ImageFilter
#Os modülü Python’da hazır olarak gelen , dosya ve dizinlerde kolaylıkla işlemler yapmamızı sağlayan bir modüldür.
import os

#fotograflarin bulundugu dosyanin yolu
path = '.\photoEditor\images'
#editli fotograflari kaydedecegimiz dosyanin uzantisi
pathOut = '.\photoEditor\editedImages'

for fileName in os.listdir(path):
    img = Image.open(f"{path}/{fileName}")

    #BLUR
    edit= img.filter(ImageFilter.BLUR)

    #Sharp
    enchancer = ImageEnhance.Sharpness(edit)
    edit = enchancer.enhance(2)

    # Diger kullanabilecegimiz filterlar
    # CONTOUR, DETAIL, EDGE_ENHANCE, EDGE_ENHANCE_MORE, EMBOSS, FIND_EDGES, SMOOTH, SMOOTH_MORE

    #Editli fotografi dosyaya kaydetme
    clean_name = os.path.splitext(fileName)[0]
    
    edit.save(f"{pathOut}/{clean_name}_edited.jpg")
    #dosyanın kaydedileceği yolun ve dosya adının birleşimidir.