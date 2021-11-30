import os
from PIL import Image

logo_file = 'replacer.png'
logoIm = Image.open(logo_file)
logoIm = logoIm.convert('RGBA')
logoWidth, logoHeight = logoIm.size


os.chdir('E://FM_Transmitter//Documents//Results//results_old_FMTX_LP_25MHz_DAC_version')
subdirs = [x[0] for x in os.walk('.')]
print(subdirs)

ONLY_CLEANUP = True
KEYWORD = 'VHFTX'

listOfDirs = list()
for (dirpath, dirnames, filenames) in os.walk('E://FM_Transmitter//Documents//Results//results_old_FMTX_LP_25MHz_DAC_version'):
    if len(filenames) != 0 :
        listOfDirs.append(dirpath)

for dir in listOfDirs:
    for filename in os.listdir(dir):
        if not KEYWORD in filename and '.jpg' in filename:
            os.remove(dir +'\\' + filename)

if not ONLY_CLEANUP:
    for dir in listOfDirs:
        for filename in os.listdir(dir):
            if not (filename.endswith('.png') or filename.endswith('.jpg')) or filename == logo_file:
                continue
            im = Image.open(dir +'\\' + filename)
            width, height = im.size
            """ -----------------------------------------------------------"""
            RESIZE_ENABLED = False
            sq_fit_size = 700
            if RESIZE_ENABLED:
                if width > sq_fit_size and height > sq_fit_size and False:
                    if width > height:
                        height = int((sq_fit_size)/width) * height
                        width = sq_fit_size
                    else:
                        width = int((sq_fit_size/height) * width)
                        height = sq_fit_size

                print("Resizing%s" % (filename))
                im = im.resize((width, height))
            """ -----------------------------------------------------------"""
            print("Adding logo to %s" % (filename))
            im.paste(logoIm, (width - logoWidth, 0), logoIm)
            #im.paste(logoIm, (0, 0), logoIm)
            im.save(dir +'\\' + KEYWORD + '_' + filename)