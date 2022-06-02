# Importing the modules
import pandas as pd
from scipy.cluster.vq import whiten

# Store RGB values of all pixels in lists r, g and b
r = []
g = []
b = []
for row in batman_image:
	for temp_r, temp_g, temp_b, temp in row:
		r.append(temp_r)
		g.append(temp_g)
		b.append(temp_b)

# only printing the size of these lists
# as the content is too big
print(len(r))
print(len(g))
print(len(b))

# Saving as DataFrame
batman_df = pd.DataFrame({'red' : r,
						'green' : g,
						'blue' : b})

# Scaling the values
batman_df['scaled_color_red'] = whiten(batman_df['red'])
batman_df['scaled_color_blue'] = whiten(batman_df['blue'])
batman_df['scaled_color_green'] = whiten(batman_df['green'])
