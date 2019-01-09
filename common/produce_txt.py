#product val txt
import xml.etree.ElementTree as ET
def parse_rec(filename):
    """ Parse a PASCAL VOC xml file """
    tree = ET.parse(filename)
    objects = []
    size_info=tree.find('size')
    for obj in tree.findall('object'):
        obj_struct = {}
        obj_struct['name'] = obj.find('name').text
        obj_struct['pose'] = obj.find('pose').text
        obj_struct['truncated'] = int(obj.find('truncated').text)
        obj_struct['difficult'] = int(obj.find('difficult').text)
        obj_struct['width']=float(size_info.find('width').text)
        obj_struct['height']=float(size_info.find('height').text)
        bbox = obj.find('bndbox')
        obj_struct['bbox'] = [float(bbox.find('xmin').text),
                              float(bbox.find('ymin').text),
                              float(bbox.find('xmax').text),
                              float(bbox.find('ymax').text)]
        objects.append(obj_struct)

    return objects
import os
the_classes=[c.strip() for c in open('/home/wushuanchen/PycharmProjects/pytorch-retinanet-master/data/voc.names').readlines()]
f=open('/home/wushuanchen/PycharmProjects/pytorch-retinanet-master/data/voc12_train.txt','w')
the_root_path='/home/wushuanchen/datasets/voc/VOC2012/ImageSets/Main/train.txt'
val_imgs=open(the_root_path,'r').readlines()
val_imgs=[val_img.strip() for val_img in val_imgs]
for img in val_imgs:
    filename='/home/wushuanchen/datasets/voc/VOC2012/Annotations/%s.xml'%(img)
    img_name='%s.jpg'%(img)
    objects=parse_rec(filename)
    the_write_list=[img_name]
    for object in objects:
        object_class=str(the_classes.index(object['name']))
        width=object['width']
        height=object['height']
        bbox = [str(box) for box in object['bbox']]
        the_write_list.extend(bbox)
        the_write_list.append(object_class)
    f.writelines( ' '.join(the_write_list))
    f.write('\n')
f.close()




