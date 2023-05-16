#%%
import numpy as np
import os,glob

NH_path = '../crop_image/200pixel_fits'
fig_path = 'Fig_T(CO 1-0)'
mol = 'T(CO 1-0)'
result_path = f'../PDFchem/{fig_path}'
pixel_width = 200

nrows=np.int8(4678//pixel_width+1)
ncols=np.int8(3010//pixel_width)


print("""
<!DOCTYPE html>
<html>
<head>
	<style>
		table {
			border-collapse: collapse;
			table-layout: fixed;
			width: 50%;
#			margin: auto;
		}
		td {
			padding: 0;
			width: 50%;
			position: relative;
			cursor: pointer;
			border: none;
		}
		img {
			width: 100%;
			height: 100%;
			object-fit: contain;
		}
		.overlay {
			display: none;
			position: fixed;
			top: 0;
			right: 0;
			bottom: 0;
			left: 50%;
			background-color: rgba(0,0,0,0);
			z-index: 999;
		}
		.overlay img {
			max-width: 100%;
			max-height: 100%;
			margin: auto;
			display: block;
			position: absolute;
			top: 0;
			right: 0;
			bottom: 0;
			left: 0;
		}
	</style>
</head>
<body>
	<h1>PDFchem Results</h1>
	<h2>Click any pixel to see the result.</h2>
	<table>
"""
)
#%%
for row in range(nrows):
    print('<tr>')
    y0 = (nrows-row-1) 
    for col in range(ncols):
        # Calculate the coordinates of the current small figure
        if os.path.exists(f'{result_path}/{mol}_{y0:02d}_{col:02d}.png'):
            print(f'<td><img src="{NH_path}/small_data_NH_{y0:02d}_{col:02d}.png" data-link="{result_path}/{mol}_{y0:02d}_{col:02d}.png"></td>')
        else:
            print(f'<td><spacer> </spacer></td>')
    print('</tr>')


print("""
	</table>
	<div class="overlay">
		<img id="linked-image" src="">
	</div>
	<script>
		var overlay = document.querySelector(".overlay");
		var linkedImage = document.querySelector("#linked-image");
		var images = document.querySelectorAll("img");
		for (var i = 0; i < images.length; i++) {
			images[i].addEventListener("click", function() {
				linkedImage.src = this.dataset.link;
				overlay.style.display = "block";
			});
		}
		overlay.addEventListener("click", function() {
			overlay.style.display = "none";
		});
	</script>
</body>
</html>
""")


# %%
