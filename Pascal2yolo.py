#!/usr/bin/env python
# coding: utf-8

# In[15]:


from bs4 import BeautifulSoup
import glob


# In[18]:


for name in glob.glob('./annotations/*'):
    
    filename = name.split('\\')[1]
    filename = filename.split('.')[0]
    
    with open(name, 'r') as f:
        data = f.read()

    Bs_data = BeautifulSoup(data, "xml")
    
    with open('./classes.txt', 'r') as f:
        classes = f.read().splitlines()
        
    width = Bs_data.find_all('width')
    width = int(width[0].get_text())
    
    height = Bs_data.find_all('height')
    height = int(height[0].get_text())
    
    tags = Bs_data.find_all('name')
    x_mins = Bs_data.find_all('xmin')
    x_maxs = Bs_data.find_all('xmax')
    y_mins = Bs_data.find_all('ymin')
    y_maxs = Bs_data.find_all('ymax')
    
    yolo = ''

    for tag, xmin, xmax, ymin, ymax in zip(tags, x_mins, x_maxs, y_mins, y_maxs):
    
        if tag.get_text() in classes:
            category = classes.index(tag.get_text())
    
        xmin = int(xmin.get_text())
        xmax = int(xmax.get_text())
        ymin = int(ymin.get_text())
        ymax = int(ymax.get_text())
    
        x_coord = (xmin + xmax) / 2 / width
        y_coord = (ymin + ymax) / 2 / height
        shape_width = (xmax - xmin) / width
        shape_height = (ymax - ymin) / height
    
        yolo = yolo + str(category) +' '+str(format(x_coord,'.6f')) +' '+str(format(y_coord,'.6f'))+' '+str(format(shape_width,'.6f'))+' '+str(format(shape_height,'.6f'))+'\n'

    f = open('./yolo_format/'+filename+'.txt', "a")
    f.write(yolo)
    f.close()


# In[ ]:




