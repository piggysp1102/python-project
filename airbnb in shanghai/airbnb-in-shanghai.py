# _*_ coding:utf-8 _*_
"""
@File     : main.py
@Project  : airbnb
@Time     : 2022/11/11 15:36
@Author   : MYW
@Software : PyCharm
@License  : (C)Copyright 2018-2028, Taogroup-NLPR-CASIA
@Last Modify Time      @Version     @Desciption
--------------------       --------        -----------
2022/11/11 15:36        1.0             None
"""
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
df= pd.read_csv('airbnb-SH-listings.csv/listings-locations.csv')
import json
with open('geojson-china/data-master/json/geo/china/province-city/shanghai.geojson', encoding= 'utf-8') as f:
    districts_map = json.load(f)
districts_map['features']
col = "aliceblue, antiquewhite, aqua, aquamarine, azure,beige, bisque, black, blanchedalmond, blue,blueviolet, brown, burlywood, cadetblue,chartreuse, chocolate".split(",")
nei = set(df['neighbourhood'].values.tolist())
k_v = {k:v for k,v in zip(nei,col)}
df['col'] = df['neighbourhood'].apply(lambda x:k_v[x])
# go.Scattermapbox

# G = go.Scattermapbox(
#     mode='markers',
#     lat=df.latitude,
#     lon=df.longitude,
#     hovertext=df.name,
#     color=df.col,
#     marker_symbol = 'marker',
#     marker_size = 3
# )
fig = px.scatter_mapbox(df,
                        lon = 'longitude',  #输入经度坐标
                        lat = 'latitude',  #输入纬度

                        color ="col", #对应excel的color栏，每个值代表一种颜色
                        hover_name ='name',#可以对应excel里面的某一栏
                        hover_data = None,#可以对应excel里面的某一栏
                        # color_continuous_scale = px.colors.carto.Temps
                       )


# fig = go.Figure(data = G)

fig.update_layout(
   mapbox =  {'accesstoken': 'pk.eyJ1IjoicGlnZ3lzcDExMDIiLCJhIjoiY2t4ajc1YzlhMHJvcjJ2cXdhb3I5c3JwMiJ9.8Y2WR2f5TrE5DqEyO-rt3g', 'center':{ 'lat':31.224361,'lon':121.469170}, 'zoom':8},
   margin = {'l':0, 'r':0, 't':0, 'b':0} )
geo = dict(
        scope = 'asia',
        showland = True,
        landcolor = 'rgb(212,212,212)',
        subunitcolor = 'rgb(255,255,255)',
        countrycolor = 'rgb(255,255,255)',
        showlakes = True,
        showcountries = True,
        resolution = 50,
        projection = dict(
            type = 'conic conformal',
            rotation_lon = -100
        ),
        lonaxis = dict(
            showgrid = True,
            gridwidth = 0.5,
            range = [120.8, 122],
            dtick = 0.1
        ),
        lataxis = dict(
            showgrid = True,
            gridwidth = 0.5,
            range = [30.5,32],
            dtick = 0.1)
    ),

fig.show()