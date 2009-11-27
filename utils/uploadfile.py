import os,datetime,random
from django.conf import settings
def genfilename(filext):
	randomfilename = datetime.datetime.now().strftime("%Y%m%d%H%M%S") + str(random.randrange(0, 100, 2)).rjust(2,'0') + random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
	randomfilename ="%s%s" % (randomfilename , filext)
	return randomfilename

def randomfilename(filename):
	if len(filename)>0:
		base, ext = os.path.splitext(filename)
		ran_filename = datetime.datetime.now().strftime("%Y%m%d%H%M%S") + str(random.randrange(0, 100, 2)).rjust(2,'0') + random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
		ran_filename = "%s%s" % (ran_filename , ext)
		return ran_filename
	else:
		return datetime.datetime.now().strftime("%Y%m%d%H%M%S") + str(random.randrange(0, 100, 2)).rjust(2,'0') +".tmp"

def handle_uploaded_file(f):
    UPLOAD_TO = 'attachment/%s/' % (datetime.datetime.now().strftime('%Y/%m/%d'))
    SAVE_TO   = os.path.join(settings.MEDIA_ROOT,UPLOAD_TO)

    if not os.path.exists(SAVE_TO):
        os.makedirs(SAVE_TO)

    try:
        fileext=os.path.splitext(f.name)[1]
    except:
        fileext='.tmp'

    filename     = genfilename(fileext)
    upfilename   = os.path.join(UPLOAD_TO,filename)
    diskfilename = os.path.join(SAVE_TO,filename)

    destination = open(diskfilename, 'wb+')
    for chunk in f.chunks():
        destination.write(chunk)
    destination.close()
    #try:
    #    im = PIL.Image.open(filename)
    #    im=im.convert('RGB')
    #    name = settings.STATIC_UPLOAD+'face/u%s.png' % (datetime.datetime.now().strftime('%Y-%m-%d'))
    #    im.save(file(name, 'wb'), 'PNG')
    #except:
    #    return "ERROR"

    return upfilename,diskfilename