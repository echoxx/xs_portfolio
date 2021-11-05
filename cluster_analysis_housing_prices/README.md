# xs_portfolio
Finding the next Austin
Cluster analysis of housing prices in US cities
xandersnyder@gmail.com

Index of files & folders

merge_data.py - a script to take individual time series from /data, merge and reshape them. Saves two csvs: one with the housing price index, and one with growth in housing price index.

cluster_US.ipynb - contains analysis and writeup. Note that the maps made with Folium, which is a more intuitive way to understand groupings of cities, does not appeart automatically in github. I therefore saved the three maps - map0.html, map6.html, and map7.html - separately, to avoid haing to rerun the notebook, which takes about 3 minutes on a local machine with 32gb.

The .png files are the K-means and Gaussian Mixture Model clusters. The image itself is fairly large, and it is easier to zoom in on the cluster plot when viewing the .png than in the notebook itself.

/data - stores all housing price data, and location where any merged data is saved. All housing price indices are from the U.S. Federal Housing Finance Agency, accessed via FRED.




