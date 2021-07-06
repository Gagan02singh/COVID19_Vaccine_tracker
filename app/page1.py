from dash.dependencies import Output, Input, State
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import dash_bootstrap_components as dbc
import plotly.graph_objects as go
import dash
import pandas as pd
import numpy as np
from numerize import numerize
from navbar import *


external_stylesheets = [dbc.themes.BOOTSTRAP,'/assets/dashboard.css']
app = dash.Dash(__name__,external_stylesheets=external_stylesheets,meta_tags=[{'name':'viewport',
                                                                                'content':'width=device-width,initial-scale=1.0'}])
app.config.suppress_callback_exceptions = True

server = app.server

line_chart_dropdown1_page1_default = ['India']
bar_chart_dropdown_page1_default = ['Israel','United Kingdom','United States', 'Italy'\
                                    ,'Germany','Canada']

def Page1():

    #base_checklist_labels = df_vaccinations['location'].unique().tolist()
    #checklist_options= [{'label':i,'value':i} for i in base_checklist_labels]
    map_dropdown_options= [
                            {'label':'World',
                            'value':'world'},
                            {'label':'Asia',
                            'value':'asia'},
                            {'label':'Africa',
                            'value':'africa'},
                            {'label':'Europe',
                            'value':'europe'},
                            {'label':'North America',
                            'value':'north america'},
                            {'label':'South America',
                            'value':'south america'}
                            ]
    
    #manufacturers_countries=['Chile','Czechia','Germany','Iceland','Italy','Latvia','Lithuania','Romania','United States']
    manufacturers_countries = df_vaccinations_by_manufacturer.location.unique().tolist()
    area_chart_dropdown2_options =  [{'label':i,'value':i} for i in manufacturers_countries]

    line_chart_dropdown1_page1 = html.Div(
                    dcc.Dropdown(
                            id = 'line_chart_dropdown1_page1',
                            options=dropdown_options, # options in list, properly formatted
                            value=line_chart_dropdown1_page1_default,# we can set a default value
                            multi = True
                        ),style = {'width' : '80%'}
                )
    
    area_chart_dropdown1_page1 = html.Div(
                    dcc.Dropdown(
                            id = 'area_chart_dropdown1_page1',
                            options=dropdown_options, # options in list, properly formatted
                            value='Canada'# we can set a default value
                        ),style = {'width':'30%'}
                )

    area_chart_dropdown2_page1 = html.Div(
                    dcc.Dropdown(
                            id = 'area_chart_dropdown2_page1',
                            options=area_chart_dropdown2_options, # options in list, properly formatted
                            value='United States'# we can set a default value
                        ),style = {'width':'30%'}
                )


    line_chart_dropdown2_page1 = html.Div(
                    dcc.Dropdown(
                            id = 'line_chart_dropdown2_page1',
                            options=[{
                                        'label':'Cumulative',
                                        'value':'Cumulative'},
                                    {
                                      'label':'New per day',
                                      'value':'New per day'}
                                    ], # options in list, properly formatted
                            value='Cumulative'# we can set a default value
                        ),style = {'width' : '30%'}
                )
            
    map_plot_dropdown_page1 = html.Div(
                                dcc.Dropdown(
                                    id = 'map_plot_dropdown_page1',
                                    options = map_dropdown_options,
                                    value='world'
                                ),style= {'width' : '30%','margin-bottom':'2%'}
                            )

    bar_chart_dropdown_page1 = html.Div(
                    dcc.Dropdown(
                            id = 'bar_chart_dropdown_page1',
                            options=dropdown_options, # options in list, properly formatted
                            value=bar_chart_dropdown_page1_default,# we can set a default value
                            multi = True
                        ),style = {'width' : '80%'}
                )


    line_chart =  dcc.Loading(
                        html.Div(
                            dcc.Graph(id='line_graph',style={'height':'100%'}),style = { 'width':'100%','height':'100%'}
                                ),type = "cube")

    area_chart_1 = dcc.Loading(
                        html.Div(
                            dcc.Graph(id='area_chart_1',style={'height':'100%'}),style = {'width':'100%','height':'100%'}
                            ),type = "cube")

    area_chart_2 = dcc.Loading(
                        html.Div(
                            dcc.Graph(id='area_chart_2',style={'height':'100%'}),style = {'width':'100%','height':'100%'}
                            ),type = "cube",style={'height':'100%'})

    map_plot = dcc.Loading(
                        html.Div(
                            dcc.Graph(id = 'map_plot',style={'height':'100%'}),style={'width':'100%','padding-bottom':'1%','height':'100%'}
                                ),type = "cube"
                        )

    bar_chart = dcc.Loading(
                        html.Div(
                            dcc.Graph(id='bar_chart',style={'height':'100%'}),style = {'width':'100%','height':'100%'}
                        ),type = "cube"
                    )
    
    #interval_heading = html.Div(
    #                        html.H5("Interval")
    #                   )

    card_4 = [
            #dbc.CardHeader("Card header"),
            dbc.CardBody(
                [
                     dbc.Row(
                        [ 
                            dbc.Col(
                                [
                                    html.H5(id = "card_4", className="card-title c1"),
                                     html.P(
                                          "Total Cases",
                                          className="card-text c2"
                                     )
                                ],style={'padding':0,'margin-left':'2%'}
                            )
                        ],style = {'padding':'1.5em','height':'100%'},justify="center",align="center"
                    )
                ],style={'padding':0}
            )

    ]

    card_5 = [
        dbc.CardBody(
                [
                dbc.Row(
                        [ 
                            dbc.Col(
                                [
                                    html.H5(id = "card_5", className="card-title c1"),
                                    html.P(
                                         "New Cases",
                                    className="card-text c2"
                                    )
                                ],style={'padding':0,'margin-left':'2%'}
                            )
                        ],style = {'padding':'1.5em','height':'100%'},justify="center",align="center"
                    )
                ],style={'padding':0}
            )
            #dbc.CardHeader("Card header"),
    ]

    card_6 = [
            #dbc.CardHeader("Card header"),
            dbc.CardBody(
                [
                dbc.Row(
                        [ 
                            dbc.Col(
                                [
                                    html.H5(id = "card_6", className="card-title c1"),
                                    html.P(
                                        "Total Deaths",
                        
                                        className="card-text c2"
                                    )
                                ],style={'padding':0,'margin-left':'2%'}
                            )
                        ],style = {'padding':'1.5em','height':'100%'},justify="center",align="center"
                    )
                ],style={'padding':0}
            )
    ]

    card_7 = [


            dbc.CardBody(
                [
                dbc.Row(
                        [ 
                            dbc.Col(
                                [
                                     html.H5(id = "card_7", className="card-title c1"),
                                     html.P(
                                        "New Deaths",
                        
                                         className="card-text c2"
                                    )
                                ],style={'padding':0,'margin-left':'2%'}
                            )
                        ],style = {'padding':'1.5em','height':'100%'},justify="center",align="center"
                    )
                ],style={'padding':0}
            )
            #dbc.CardHeader("Card header"),
            
    ]

    card_area_chart_1 = [ 
                        dbc.CardBody(children = [html.H5( "Fully vaccinated vs Atleast 1 dose",className='sub-title',style={'color':'white','margin-bottom':0}),
                                                 html.P( "Fully vaccinated - Share of the total population that have received all doses prescribed by the vaccination\
                                                         protocol.",className="d1",style={'color':'#909090','margin-top':0,'margin-bottom':0}),
                                                 html.P( "At least 1 dose -  Share of the total population that received at least one vaccine dose. This may not equal the share that are fully \
                                                         vaccinated if the vaccine requires two doses.",className="d1",style={'color':'#909090','margin-top':0,'margin-bottom':0}) ]
                        ,className= "card-title plot-header",style={'margin':'0%','margin-top':'2%','margin-bottom':'5%'}),
                        dbc.CardHeader(area_chart_dropdown1_page1,className= "plot-dropdown"),
                        dbc.CardBody(
                        [  
                        #html.H5("",style={'margin':'0%','padding':'0','padding-left':'2%'}),
                        area_chart_1
                        ],className= "plot-body")
                    ]

    card_area_chart_2 = [ 
                        dbc.CardBody(children = [html.H5("Doses administered by manufacturers",className='sub-title',style={'color':'white','margin-bottom':0}),
                                                 html.P("This is counted as a single dose, and may not equal the total number of people \
                                                     vaccinated, depending on the specific dose regime.",className="d1",style={'color':'#909090','margin-top':0})
                                                ],
                        className= "card-title plot-header",style={'margin':'0%','margin-top':'2%','margin-bottom':'4%'}),
                        dbc.CardHeader(area_chart_dropdown2_page1,className= "plot-dropdown"),
                        dbc.CardBody(
                        [  
                        #html.H5("",style={'margin':'0%','padding':'0','padding-left':'2%'}),
                        area_chart_2
                        ],className = "plot-body")
                    ]
    
    card_line_chart = [
                        dbc.CardBody(children = [html.H5("Doses administered",id = 'line_chart_title',className='sub-title',style={'color':'white','margin-bottom':0}),
                                                 html.P("Total number of vaccination doses administered. This is counted as a single dose, and may not equal the total number of people vaccinated,\
                                                     depending on the specific dose regime.",className="d1",style={'color':'#909090','margin-top':0})]
                                    ,className= "card-title plot-header",style={'margin':'0%','margin-top':'2%'}),
                        dbc.CardHeader(line_chart_dropdown1_page1,style={'padding-top':'3%'},className= "plot-dropdown"),
                        dbc.CardBody(html.H5("Interval",style={'color':'white','margin-bottom':'0.2%'}),className= "card-title plot-header",style={'margin':'0%','font-size':'1em'}),
                        dbc.CardHeader(line_chart_dropdown2_page1,style={'margin':'0','padding-top':'0'},className= "plot-dropdown"),
                        dbc.CardBody(
                        [  
                        line_chart
                        ],className="plot-body")
                    ]
    
    card_map = [
                dbc.CardBody(
                        [
                        html.H5("Population fully vaccinated",className="sub-title",style={'color':'white','margin-top':'1%','margin-bottom':0}),
                        html.P("Share of the total population that have received all doses prescribed by the vaccination protocol.",className="d1",style={'color':'#909090','margin-bottom':'5%'}),
                        map_plot_dropdown_page1,
                        map_plot
                        ]
                    ,className="map-card")
                ]
    
    card_bar_chart = [ 
                        dbc.CardBody(children = [html.H5("Fully vaccinated vs Atleast 1 dose",className='sub-title',style={'color':'white','margin-bottom':0}),
                                                 html.P( "Fully vaccinated - Share of the total population that have received all doses prescribed by the vaccination\
                                                         protocol.",className="d1",style={'color':'#909090','margin-top':0,'margin-bottom':0}),
                                                 html.P( "At least 1 dose -  Share of the total population that received at least one vaccine dose. This may not equal the share that are fully \
                                                         vaccinated if the vaccine requires two doses.",className="d1",style={'color':'#909090','margin-top':0,'margin-bottom':0})]
                        
                                    ,className= "card-title plot-header",style={'margin':'0%','margin-top':'2%','margin-bottom':'3%'}),
                        dbc.CardHeader(bar_chart_dropdown_page1,className="plot-dropdown"),
                        dbc.CardBody(
                        [  
                        #html.H5("",style={'margin':'0%','padding':'0','padding-left':'2%'}),
                        bar_chart
                        ],className="plot-body")
                    ]

    page1 = html.Div(children=[
            
            navbar(),

            dbc.Row(
                [
                    dbc.Col([
                        dbc.Row([
                            dbc.Col(dbc.Card(card_4,className="card text-center", color="#272a2c", inverse=True,style={'height':'100%','padding':0}),style ={'padding-bottom':'1em'},width=12),
                            dbc.Col(dbc.Card(card_5, className="card text-center",color="#272a2c", inverse=True,style={'height':'100%','padding':0}),style ={'padding-bottom':'1em'},width=12),
                        
                            dbc.Col(dbc.Card(card_6, className="card text-center",color="#272a2c", inverse=True,style={'height':'100%','padding':0}),style ={'padding-bottom':'1em'},width=12),
                            dbc.Col(dbc.Card(card_7,className="card text-center card7", color="#272a2c", inverse=True,style={'height':'100%','padding':0}),width=12)
                        ],style={'height':'100%'})
                    ],style = {'padding':0,'margin-right':'1em'},className="stats_2"),

                    dbc.Col(
                        dbc.Card(card_map,color = "#272a2c",style={'height':'100%'}),style={'padding-left':0,'padding-right':0},md=9
                    )
                ],style={'margin':'1em','margin-top':0}
                    
            ),

            dbc.Row(
                [
                dbc.Col(
                    dbc.Card(card_line_chart,color = "#272a2c",style={'height':'100%'})
                    ,className='c3',style={'padding-left':0,'margin-bottom':'1em'},lg=6,xs=12),
                dbc.Col(
                    dbc.Card(card_area_chart_1,color="#272a2c",style={'height':'100%'})
                ,style={'padding-left':0,'padding-right':0,'margin-bottom':'1em'},lg=6,xs=12)
                ],style={'height':'30%','margin-left':'1em','margin-right':'1em'}),

            
            dbc.Row(
                [
                dbc.Col(
                    dbc.Card(card_area_chart_2,color = "#272a2c",style={'height':'100%'})
                    ,className='c3',style={'padding-left':0,'margin-bottom':'1em'},xs=12,lg=6
                ),
                dbc.Col(
                    dbc.Card(card_bar_chart,color="#272a2c",style={'height':'100%'})
                ,style={'padding-left':0,'padding-right':0,'margin-bottom':'1em'},xs=12,lg=6)
                ]
            ,style = {'height':'30%','margin-left':'1em','margin-right':'1em'}),
            
            dbc.Row(
                [
                dbc.Col(
                        html.A(
                            [
                                html.Img(src=app.get_asset_url('linkedin_1.png'),style = {'height':'40px', 'width':'40px','background-color':'white','border-radius':'50%'})
                            ],href="https://www.linkedin.com/in/gagan02singh/"),
                        style={'padding':0,'padding-top':'0.5em','padding-right':'0.3em'},width={"size":"auto"}),
                dbc.Col(
                        html.A(
                        [
                            html.Img(src=app.get_asset_url('gmail_1.png'), style={'height':'40px', 'width':'40px','background-color':'white','border-radius':'50%'})
                        ],href="mailto:singhgaganpreet02@gmail.com"),
                        style={'padding':0,'padding-top':'0.5em'},width={"size":"auto"})
                ],justify="center",style={'padding-top':'4em','background-color':'#272a2c','color':'white','margin-left':'1em','margin-right':'1em'}
            ),
            dbc.Row(
                [
                    html.P("© Developed by GAGANPREET SINGH",style = {'margin-bottom':0}),
                ]
                ,justify="center",style={'background-color':'#272a2c','color':'white','margin-left':'1em','margin-right':'1em'}
            ),
            dbc.Row(
                [
                    html.P('Coded in Dash, Deployed on AWS',style = {'color':'#909090'})
                ]
                ,justify="center",style={'padding-bottom':'1em','background-color':'#272a2c','color':'white','margin-left':'1em','margin-right':'1em'}
            )


        ],style= {'background-color':'#000000'}
    )
    return page1

app.layout = Page1()




@app.callback(
    Output('card_1','children'),
    [Input('dropdown_navbar', 'value')]
)
def update_card_1(value):
    total_vaccinations = df_vaccinations[df_vaccinations['location'] == "{}".format(value)]['total_vaccinations'].dropna().tail(1).tolist()[0]
    if np.isnan(total_vaccinations) == True:
        return '-'
    else:
        return numerize.numerize(total_vaccinations,2)


@app.callback(
    Output('card_2','children'),
    [Input('dropdown_navbar', 'value')]
)
def update_card_2(value):
    try:
        fully_vaccinated = df_vaccinations[df_vaccinations['location'] == "{}".format(value)]['people_fully_vaccinated'].dropna().tail(1).tolist()[0]
        if np.isnan(fully_vaccinated) == True:
            return '-'
        else:
            return numerize.numerize(fully_vaccinated,0)
    except:
        return '-'

@app.callback(
    Output('card_3','children'),
    [Input('dropdown_navbar', 'value')]
)
def update_card_3(value):
    try:
        fully_vaccinated = df_vaccinations[df_vaccinations['location'] == "{}".format(value)]['people_fully_vaccinated'].dropna().tail(1).tolist()[0]
        if value == 'World':
            total_population = df_population.population.sum()
        elif value in ['Africa','Asia','North America','South America','Europe']:
            total_population = df_population[df_population['continent'] == "{}".format(value)]['population'].sum()
        else:
            total_population = df_population[df_population['location'] == "{}".format(value)]['population'].tolist()[0]

        if np.isnan(fully_vaccinated) == True:
            return '-'
        else:
            return str(round(100*(fully_vaccinated/total_population),2))+'%'
    except:
        return '-'



@app.callback(
    Output('card_4','children'),
    [Input('dropdown_navbar', 'value')]
)
def update_card_4(value):
    total_cases = df_full_data[df_full_data['location'] == "{}".format(value)]['total_cases'].dropna().tail(1).tolist()[0]
    if np.isnan(total_cases) == True:
        return '-'
    else:
        return numerize.numerize(total_cases,2)




@app.callback(
    Output('card_5','children'),
    [Input('dropdown_navbar', 'value')]
)
def update_card_5(value):
    new_cases = df_full_data[df_full_data['location'] == "{}".format(value)]['new_cases'].dropna().tail(1).tolist()[0]
    if np.isnan(new_cases) == True:
        return '-'
    else:
        return numerize.numerize(new_cases,2)



@app.callback(
    Output('card_6','children'),
    [Input('dropdown_navbar', 'value')]
)
def update_card_6(value):
    total_deaths = df_full_data[df_full_data['location'] == "{}".format(value)]['total_deaths'].dropna().tail(1).tolist()[0]
    if np.isnan(total_deaths) == True:
        return '-'
    else:
        return numerize.numerize(total_deaths,2)



@app.callback(
    Output('card_7','children'),
    [Input('dropdown_navbar', 'value')]
)
def update_card_7(value):
    new_deaths = df_full_data[df_full_data['location'] == "{}".format(value)]['new_deaths'].dropna().tail(1).tolist()[0]
    if np.isnan(new_deaths) == True:
        return '-'
    else:
        return numerize.numerize(new_deaths,2)




@app.callback(
    Output('area_chart_dropdown1_page1','value'),
    [Input('dropdown_navbar', 'value')]
)
def update_area_chart_dropdown1_page1(value):
    return value


@app.callback(
    Output('line_chart_dropdown1_page1','value'),
    [Input('dropdown_navbar', 'value')]
)
def update_line_chart_dropdown1_page1_default(value):
    global line_chart_dropdown1_page1_default
    line_chart_dropdown1_page1_default.append(value)
    return list(set(line_chart_dropdown1_page1_default))


@app.callback(
    Output('bar_chart_dropdown_page1','value'),
    [Input('dropdown_navbar', 'value')]
)
def update_bar_chart_dropdown_page1_default(value):
    global bar_chart_dropdown_page1_default
    bar_chart_dropdown_page1_default.append(value)
    return list(set(bar_chart_dropdown_page1_default))


@app.callback(
    Output('line_graph','figure'),
    [Input('line_chart_dropdown1_page1','value'),Input('line_chart_dropdown2_page1','value')]
)
def update_line_graph(countries,interval):
    mask = df_vaccinations.location.isin(countries)
    if interval == 'Cumulative':
        y_axis = "total_vaccinations"
    else:
        y_axis = "daily_vaccinations"

    fig = px.line(df_vaccinations[mask], x="date", y=y_axis, title='',color = 'location',template="plotly_dark")\
          .update_traces(connectgaps=True)\
          .update_traces(mode='lines')
    fig.update_traces(hovertemplate=None)
    
    fig.update_layout(hovermode="x unified",legend=dict(
                                          yanchor="top",
                                          y=0.99,
                                          xanchor="left",
                                          x=0.01),
                                          margin={"r":20,"t":100,"l":20,"b":50},
                                          dragmode="pan"
    )

    fig.update_xaxes(showgrid = False)
    fig.update_yaxes(showgrid = False)
    return fig




@app.callback(
    Output('line_chart_title','children'),
    [Input('line_chart_dropdown2_page1','value')]
)
def update_line_chart_title(interval):
    if interval == 'Cumulative':
        return  "Doses Administered"
    else:
        return  "Daily doses Administered"




@app.callback(
    Output('area_chart_1','figure'),
    [Input('area_chart_dropdown1_page1','value')]
)
def update_area_chart_1(country):
    mask =  df_vaccinations[df_vaccinations['location'] == "{}".format(country)]
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=mask['date'], y=mask['people_vaccinated'], fill='tonexty',name= "At least 1 dose",connectgaps=True))# fill down to xaxis
    fig.add_trace(go.Scatter(x=mask['date'], y=mask['people_fully_vaccinated'], fill='tozeroy',name= "fully vaccinated",connectgaps=True))  # fill to trace0 y
    
    #fig.update_traces(hovertemplate="<br>".join([
    #                                        "ColX: %{x:.2f}",
    #                                        "ColY: %{y:.2f}"
    #                                        ])
    #                )*/

    fig.update_traces(hovertemplate= None)
    fig.update_layout(title='',
                   xaxis_title='Date',
                   yaxis_title='Total people',
                   template = "plotly_dark",
                   hovermode="x unified",
                   legend=dict(
                            yanchor="top",
                            y=0.99,
                            xanchor="left",
                            x=0.01
                        ),
                    margin={"r":20,"t":100,"l":20,"b":50},
                    dragmode="pan"
                   )

    fig.update_xaxes(showgrid = False)
    fig.update_yaxes(showgrid = False)

    return fig


@app.callback(
    Output('area_chart_2','figure'),
    [Input('area_chart_dropdown2_page1','value')]
)
def update_area_chart_2(country):
    manufacturers = ['Johnson&Johnson','Sinovac','Pfizer/BioNTech','Oxford/AstraZeneca','Moderna']
    mask =  df_vaccinations_by_manufacturer[df_vaccinations_by_manufacturer['location'] == "{}".format(country)]
    fig = go.Figure()
    fig = go.Figure()
    for i in manufacturers:
        fig.add_trace(go.Scatter(x= mask[mask['vaccine'] == "{}".format(i)]['date'], y=round(mask[mask['vaccine'] == "{}".format(i)]['total_vaccinations'],2),\
                             connectgaps=True,name = i ,stackgroup = 'one'))    
    
    fig.update_traces(hovertemplate=None)
    fig.update_layout(title='',
                   xaxis_title='Date',
                   yaxis_title='Total doses',
                   template = "plotly_dark",
                    hovermode="x unified",
                    legend=dict(
                                yanchor="top",
                                y=0.99,
                                xanchor="left",
                                x=0.01
                                    ),
                    margin={"r":20,"t":100,"l":20,"b":50},
                    dragmode="pan"
                        )
    
    fig.update_xaxes(showgrid = False)
    fig.update_yaxes(showgrid = False)

    return fig



@app.callback(
    Output('map_plot','figure'),
    [Input('map_plot_dropdown_page1','value')]
)
def update_map(region):
    

    fig = go.Figure(data=go.Choropleth(
    locationmode= "country names",
    locations = df_fully_vaccinated_by_country['location'],
    z = df_fully_vaccinated_by_country['%_fully_vaccinated'],
    #hover_name = "country",
    #text = [df_fully_vaccinated_by_country['%_fully_vaccinated'],'%'],
    text = '%',
    colorscale = 'sunset',
    autocolorscale=False,
    reversescale=True,
    #marker_line_color='darkgray',
    marker_line_width=0.5,
    colorbar_title = 'percentage'))

    fig.update_traces(hoverinfo='location+z+text', selector=dict(type='choropleth'))

    fig.update_layout(
    geo = dict(scope=region),
    margin={"r":0,"t":0,"l":0,"b":0},
    paper_bgcolor = '#000000',
    plot_bgcolor = '#000000',
    font_color='white',
    geo_bgcolor="#000000"
    
    #template = "plotly_dark"
    #autosize = False,
    #height = 500,
    )

    fig.update_geos(visible=False,showcountries=True)

    #fig.update_traces(geo_bgcolor="#000000")

    #if region =='world':
    #    fig.update_geos(projection_type="natural earth")

    #fig.update_geos(lataxis_showgrid=True, lonaxis_showgrid=True)

    return fig


@app.callback(
    Output('bar_chart','figure'),
    [Input('bar_chart_dropdown_page1','value')])
def update_bar_chart(countries):

    mask = df_fully_vaccinated_by_country[df_fully_vaccinated_by_country.location.isin(countries)]
    fig = go.Figure(data =[go.Bar(y=mask.location,\
                              x=mask['%_1_dose'],\
                     #marker_color = px.colors.qualitative.Dark24
                              name = 'At least 1 dose',
                              orientation='h'),
                      go.Bar(y=mask.location,\
                             x=mask['%_fully_vaccinated'],\
                     #marker_color = px.colors.qualitative.Dark24
                             name = 'fully vaccinated',
                             orientation='h'),
              
                    ])
    fig.update_xaxes(ticksuffix = '%',showgrid = False)
    fig.update_yaxes(showgrid = False)
    fig.update_layout(barmode='overlay',template="plotly_dark",yaxis={'categoryorder':'total ascending'},
                                                                        legend=dict(
                                                                                   yanchor="top",
                                y=0.99,
                                xanchor="left",
                                x=0.01
                                                                                    ),margin={"r":20,"t":100,"l":20,"b":50},
                                                                                    dragmode="pan"
    )

    return fig




if __name__ == '__main__':
    app.run_server(debug=True,host='0.0.0.0', port=8080)