from dash.dependencies import Output, Input, State
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import dash_bootstrap_components as dbc
import dash
import pandas as pd
import numpy as np
from numerize import numerize
import os
import datetime



external_stylesheets = [dbc.themes.BOOTSTRAP]
app = dash.Dash(__name__,external_stylesheets=external_stylesheets)
app.config.suppress_callback_exceptions = True

df_vaccinations = pd.read_csv('/mnt/efs-data/covid-19-data/public/data/vaccinations/vaccinations.csv')
df_population = pd.read_csv('/mnt/efs-data/covid-19-data/public/data/jhu/locations.csv')
df_full_data= pd.read_csv('/mnt/efs-data/covid-19-data/public/data/jhu/full_data.csv')
df_vaccinations_by_manufacturer = pd.read_csv('/mnt/efs-data/covid-19-data/public/data/vaccinations/vaccinations-by-manufacturer.csv')

df_vaccinations_by_country = df_vaccinations.groupby(['location'],as_index = False)['total_vaccinations'].max()
df_vaccinations_by_country_exclude_region = df_vaccinations_by_country[~df_vaccinations_by_country.location.isin(['World','Africa','Asia','North America','South America','Europe','European Union'])]
df_vaccinations_by_country_exclude_region = pd.merge(df_vaccinations_by_country_exclude_region,df_population,left_on= 'location',right_on='location',how= 'inner')
df_vaccinations_by_country_exclude_region['total_vaccinations_per_hundred'] = round(100*(df_vaccinations_by_country_exclude_region['total_vaccinations']/df_vaccinations_by_country_exclude_region['population']),2)

df_fully_vaccinated_by_country = df_vaccinations.groupby(['location'],as_index = False).agg({'people_vaccinated': ['max'],\
                                                                                             'people_fully_vaccinated': ['max']})
df_fully_vaccinated_by_country.columns= ['location','1_dose','fully_vaccinated']
df_fully_vaccinated_by_country = pd.merge(df_fully_vaccinated_by_country,df_population,left_on= 'location',right_on='location',how= 'inner')
df_fully_vaccinated_by_country['%_fully_vaccinated'] = round(100*(df_fully_vaccinated_by_country['fully_vaccinated']/df_fully_vaccinated_by_country['population']),2)
df_fully_vaccinated_by_country['%_1_dose'] = round(100*(df_fully_vaccinated_by_country['1_dose']/df_fully_vaccinated_by_country['population']),2)

base_dropdown_labels = df_vaccinations['location'].unique().tolist()
dropdown_options= [{'label':i,'value':i} for i in base_dropdown_labels]

#last_date_modified =  datetime.datetime.fromtimestamp(os.path.getmtime('vaccinations.csv')).strftime('%m/%d/%Y')
last_date_modified = df_vaccinations.query("location == 'Canada'").date.tail(1).to_list()[0]



def navbar():

    title = html.Div(
                html.H1('COVID-19 Vaccine Tracker',className= 'title',style = {'color':'white'})
                #dcc.Markdown('''
                 # Global Covid-19 Vaccine Tracker
                #        ''')
                    )

    date_updated = html.H5(dbc.Badge("last updated: {}".format(last_date_modified), className="ml-1",color = "dark"))

    dropdown = html.Div(dcc.Dropdown(
                            id='dropdown_navbar',
                            options=dropdown_options, # options in list, properly formatted
                            value='Canada' # we can set a default value
                        ),style = {'padding-bottom':'1%'}
                    )
    

    card_1 = [
            #dbc.CardHeader("Card header"),
                   dbc.CardBody(
                    [   dbc.Row(
                        [ 
                            dbc.Col(
                                html.Div(html.Img(src=app.get_asset_url('doses_administered_1.jpg'), style={'border-radius':'50%'},className="navbar_images")),
                                style={'padding':0,'padding-top':'0.5em','padding-bottom':'0.5em'}
                            ),
                            dbc.Col(
                                [
                                    html.H5(id='card_1', className="card-title c1"),
                                    html.P(
                                        "Doses given",
                                        className="card-text c2"
                                        )
                                ],width =7,style={'padding':0,'margin-left':'2%'}
                            )
                        ],style = {'padding':'1.5em','height':'100%'},justify="center",align="center"
                    )
                ],style={'padding':0}
            )
    
    ]

    card_2 = [
            #dbc.CardHeader("Card header"),
            dbc.CardBody(
                [
                     dbc.Row(
                        [ 
                            dbc.Col(
                                html.Div(html.Img(src=app.get_asset_url('fully_vaccinated.png'), style={'border-radius':'50%'},className="navbar_images")),
                                style={'padding':0,'padding-top':'0.5em','padding-bottom':'0.5em'}
                            ),
                            dbc.Col(
                                [
                                    html.H5(id = "card_2", className="card-title c1"),
                                    html.P(
                                        "Fully vaccinated",
                                        className="card-text c2"
                                    )
                                ],width =7,style={'padding':0,'margin-left':'2%'}
                            )
                        ],style = {'padding':'1.5em','height':'100%'},justify="center",align="center"
                    )
                ],style={'padding':0}
            )
    ]

    card_3 = [
            #dbc.CardHeader("Card header"),
            dbc.CardBody(
                [
                     dbc.Row(
                        [ 
                            dbc.Col(
                                html.Div(html.Img(src=app.get_asset_url('population1.png'), style={'border-radius':'50%'},className="navbar_images")),
                                style={'padding':0,'padding-top':'0.5em','padding-bottom':'0.5em'}
                            ),
                            dbc.Col(
                                [
                                    html.H5(id = "card_3", className="card-title c1"),
                                    html.P(
                                            "population fully vaccinated",
                                            className="card-text c2"
                                        )
                                ],width =7,style={'padding':0,'margin-left':'2%'}
                            )
                        ],style = {'padding':'1.5em','height':'100%'},justify="center",align="center"
                    )
                ],style={'padding':0}
            )
    ]


    cards = dbc.CardDeck(
        [    
                dbc.Card(card_1,className="card text-center",color="#272a2c", inverse=True),
                dbc.Card(card_2,className="card text-center", color="#272a2c", inverse=True),
                dbc.Card(card_3,className="card text-center card_3", color="#272a2c", inverse=True),
         
        ])


    Navbar = html.Div(
    [
        dbc.Row(
             [
                dbc.Col(title,width={"size": 8}),
                dbc.Col(date_updated,width={"size": "auto"})
             ],justify= "between"
        ,style = {'margin-bottom':'2%'}),
        #title,
        #date_updated,
        dbc.Row([
            dbc.Col(html.H5("Select your country", className="card-title",style = {'color':'white'}),width={"size": "auto"}),
            dbc.Col(dropdown,width=5)
            ],justify="center",style = {'margin-bottom':'6%'}),
        cards
    ],style = {'padding':'1em'}
    )
    return Navbar


app.layout = navbar()


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
    
        else:
            total_population = df_population[df_population['location'] == "{}".format(value)]['population'].tolist()[0]

        if np.isnan(fully_vaccinated) == True:
            return '-'
        else:
            return str(round(100*(fully_vaccinated/total_population),2))+'%'
    except:
        return '-'

#if __name__ == '__main__':
#    app.run_server(debug=True)
