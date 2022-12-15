from streamlit_folium import st_folium
import folium

# 地図生成
folium_map = folium.Map(location=[35.690921, 139.700258],zoom_start=15)

# マーカープロット
folium.Marker(location=[35.690921, 139.700258]).add_to(folium_map)

# 地図表示
folium_map
