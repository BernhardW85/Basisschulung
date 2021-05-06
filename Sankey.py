import pandas as pd
import plotly.graph_objects as go

dict_nodes = {}
dict_links = {}
data = {}
convert_source = []
convert_target = []

nodes_id = {}

df_nodes = pd.read_excel(
    r"G:\_2021\21.012_ka-Energieholz2021\2_KP1_Marktteilnehmerinnen und Teilnehmer\Holzströme in Österreich\programm\input.xlsx",
    index_col=None, sheet_name="Nodes")
df_links = pd.read_excel(
    r"G:\_2021\21.012_ka-Energieholz2021\2_KP1_Marktteilnehmerinnen und Teilnehmer\Holzströme in Österreich\programm\input.xlsx",
    index_col=None, sheet_name="Links")

dict_nodes['id'] = df_nodes['id'].tolist()
dict_nodes['label'] = df_nodes['label'].tolist()
dict_nodes['color'] = df_nodes['color'].tolist()

nodes_id = dict(zip(dict_nodes['label'], dict_nodes['id']))

for index, row in df_links.iterrows():
    #     print(df_links.iloc[index]['source'])
    convert_source.append(nodes_id[df_links.iloc[index]['source']])
    convert_target.append(nodes_id[df_links.iloc[index]['target']])

df_links['source'] = convert_source
df_links['target'] = convert_target

dict_links['source'] = df_links['source'].tolist()
dict_links['target'] = df_links['target'].tolist()
dict_links['value'] = df_links['value'].tolist()
dict_links['label'] = df_links['label'].tolist()
dict_links['color'] = df_links['color'].tolist()

# print(df_nodes)
# print(dict_nodes)
# print(df_links)
# print(dict_links)
# print(nodes_id)

data['node'] = dict_nodes
data['link'] = dict_links

data['data'] = data
data['data']['type'] = "sankey"

# print(data)

# override gray link colors with 'source' colors
opacity = 0.4
# change 'magenta' to its 'rgba' value to add opacity
# data['data'][0]['node']['color'] = ['rgba(255,0,255, 0.8)' if color == "magenta" else color for color in data['data'][0]['node']['color']]
# data['data'][0]['link']['color'] = [data['data'][0]['node']['color'][src].replace("0.8", str(opacity))
#                                     for src in data['data'][0]['link']['source']]

fig = go.Figure(data=[go.Sankey(
    valueformat=".0f",
    valuesuffix=" Mio. FM",
    # Define nodes
    node=dict(
        pad=15,
        thickness=15,
        line=dict(color="black", width=0.5),
        label=data['data']['node']['label'],
        color=data['data']['node']['color']
    ),
    # Add links
    link=dict(
        source=data['data']['link']['source'],
        target=data['data']['link']['target'],
        value=data['data']['link']['value'],
        label=data['data']['link']['label'],
        color=data['data']['link']['color']
    ))])

fig.update_layout(title_text="Holzflussbild Österreich<br>2019",
                  font_size=10)
fig.update_traces(arrangement="freeform", selector=dict(type='sankey'))

fig.write_html(
    r"G:\_2021\21.012_ka-Energieholz2021\2_KP1_Marktteilnehmerinnen und Teilnehmer\Holzströme in Österreich\Holzfluss_test.html")
fig.write_image(
    r"G:\_2021\21.012_ka-Energieholz2021\2_KP1_Marktteilnehmerinnen und Teilnehmer\Holzströme in Österreich\Holzfluss_test.png")

fig.show()