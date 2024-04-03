import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap
import pycountry

m = Basemap(projection='mill', llcrnrlat=-60, urcrnrlat=90, llcrnrlon=-180, urcrnrlon=180)

m.drawcoastlines()
m.drawcountries()
m.drawstates()

country_codes = [country.alpha_3 for country in pycountry.countries]

for country_code in country_codes:
    try:
        country = pycountry.countries.get(alpha_3=country_code)
        country_name = country.name
        country_bounding_box = country.bounding_box
        min_lon, min_lat, max_lon, max_lat = country_bounding_box
        lon = (min_lon + max_lon) / 2
        lat = (min_lat + max_lat) / 2
        x, y = m(lon, lat)
        plt.text(x, y, country_code, fontsize=8, ha='center')
    except AttributeError:
        pass

plt.title('World Map')
plt.show()
