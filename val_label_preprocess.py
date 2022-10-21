import xml.etree.ElementTree as ET
import os
 
xmlRootDir = 'ILSVRC/Annotations/CLS-LOC/val/'#ILSVRC/Annotations/CLS-LOC/train/'# 'bbox/'
ls_xmls = sorted(os.listdir(xmlRootDir))
#files = os.listdir('bbox/'+dirs[0]+'/')
 
def fine_bbox(node, width, height):
        bbox = [[],[],[],[]]
        bndbox = node.find('bndbox')
        xmin = max(float(bndbox.find('xmin').text)/width, 0.0)
        ymin = max(float(bndbox.find('ymin').text)/height, 0.0)
        xmax = min(float(bndbox.find('xmax').text)/width, 1.0)
        ymax = min(float(bndbox.find('ymax').text)/height, 1.0)
        bbox[0].append(xmin)
        bbox[1].append(ymin)
        bbox[2].append(xmax)
        bbox[3].append(ymax)
        return bbox

def parseXML(filename):
    bbox = [[],[],[],[]]
    tree = ET.parse(filename)
    root = tree.getroot()
    size = root.find('size')
    width = float(size.find('width').text)
    height = float(size.find('height').text)
    for node in root.iter("object"):
        label = node.find('name').text
    return label

 
bboxfile = open('imagenet_2012_validation_synset_labels.txt', 'w')
content = ''
i = 0
for folder in range(1):
    folderpath = xmlRootDir + '/'
    #files = os.listdir(folderpath)
    for xmlfile in ls_xmls:
        i+=1
        label = parseXML(folderpath+xmlfile)
        #print(label)
        content += label
        #for j in range(4):
        #    content += ','+';'.join([str(x) for x in bbox[j]])
        content += '\n'
        print("processing {}/{}\r".format(i, len(ls_xmls)))
bboxfile.writelines(content)
bboxfile.close()
