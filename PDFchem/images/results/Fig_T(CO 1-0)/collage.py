# After all the individual plots are generated, run this script to collage them
# onto the original map's grid.
# %%

import matplotlib, datetime
import matplotlib.pyplot as mpl
import numpy as np
import os,glob
from PIL import Image, ImageFont, ImageDraw  

matplotlib.rc('font',size=9)
matplotlib.pyplot.ioff()

########## 
# set the prefix of the file names here
result_mol = 'T(CO 1-0)'
########## 

# These resolutions are for Orion A
pixel_width= 200
pixel_threshold = 0.8*pixel_width**2
#pdf_path =  str(pixel_width) +'pixel_pdf'
nrows=np.int8(4678//pixel_width+1)
ncols=np.int8(3010//pixel_width)

#%%
small_size = (pixel_width*2, pixel_width*2)
new_fig = Image.new("RGB", (3010*2+100, 4678*2+100), 'white')
myFont = ImageFont.truetype('DejaVuSansMono.ttf', 13)

for row in range(nrows):
    for col in range(ncols):
        # Calculate the coordinates of the current small figure
        if os.path.exists(f'{result_mol}_{row:02d}_{col:02d}.png'):
            #print(f'{row},{col}')
            with Image.open(f'{result_mol}_{row:02d}_{col:02d}.png') as im:
                im = im.resize((pixel_width*2,pixel_width*2))
                x0 = col * (small_size[0])
                y0 = (nrows-row-1) * (small_size[1])- int(small_size[1]/2)
                new_fig.paste(im, (x0,y0))
        #I1 = ImageDraw.Draw(new_fig)
new_fig.save(f'{result_mol}_collage.png',dpi=(300,300))