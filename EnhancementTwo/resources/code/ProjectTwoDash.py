##Author: Ilyass Hmamou -Email: ilyass.hmamou@snhu.edu
##Date created: September 25, 2023
##Last updated: November 26, 2023
##Description: A dash app that allows users to interact with the animal shelter database ACC, 
#             It provides users with:
#                  1- An interactive datatable to view the data
#                  2- Two server-side filtering options, a dropdown to filter by animal rescue type and buttons 
#                     to filter by animal_type 
#Version2: Enhancement related to  update_dashboard() to offer more efficient and scalable code
################################################################################################################
# Setup the Jupyter version of Dash
from jupyter_dash import JupyterDash

# Configure the necessary Python module imports for dashboard components
import dash
import dash_leaflet as dl
from dash import dcc
from dash import html
import plotly.express as px
from dash import dash_table as dt
from dash.dependencies import Input, Output, State
from dash.exceptions import PreventUpdate
import base64

# Configure OS routines
import os

# Configure the plotting routines
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


from animalShelter import AnimalShelter

###########################
# Data Manipulation / Model
###########################

username = "accuser"
password = "SNHU1234"

# Connect to database via CRUD Module
db = AnimalShelter(username, password)

# sending the read method an empty document requests all documents be returned
df = pd.DataFrame.from_records(db.readAll({}))

#########################
# Dashboard Layout / View
#########################
app = JupyterDash(__name__)

#Add in Grazioso Salvare’s logo
image_filename = 'Grazioso Salvare Logo.png'
encoded_image = base64.b64encode(open(image_filename, 'rb').read())

app.layout = html.Div([
    #set up the page header, this includes the 'Grazioso Salvare Logo', and a unique identifier for the author
    html.A([
            html.Img(
                #select image path
                src='data:image/png;base64,{}'.format(encoded_image.decode()),
                #set up image style attributes, including the size and the location in page 
                style={
                    'height' : '25%',
                    'width' : '25%',
                    'float' : 'right',
                    'position' : 'relative',
                    'padding-top' : 0,
                    'padding-right' : 0
                })
    ], href='https://www.snhu.edu'),
    #author unique identifier
    html.Center(html.B(html.H1('[Ilyass Hmamou] - CS-340 Dashboard'))),
    html.Hr(),
    # buttons at top of table to filter the data set to find cats or dogs
    html.Div(className='row',
        style={'display' : 'flex'},
        children=[
            html.Span("Filter by:", style={'margin': 6}),
            html.Span(
                html.Button(id='submit-button-one', n_clicks=0, children='Cats'),
                style={'margin': 6}
            ),
            html.Span(
                html.Button(id='submit-button-two', n_clicks=0, children='Dogs'),
                style={'margin': 6}
            ),
            html.Span(
                html.Button(id='reset-buttons', n_clicks=0, children='Reset', style={'background-color': 'red', 'color': 'white'}),
                style={'margin': 6,}
            ),
            #dropdown for Rescue type
            html.Span("or", style={'margin': 6}),
            html.Span([
                dcc.Dropdown(
                    id='filter-type',
                    options=[
                        {'label': 'Water Rescue', 'value': 'wr'},
                        {'label': 'Mountain or Wilderness Rescue', 'value': 'mwr'},
                        {'label': 'Disaster Rescue or Individual Tracking', 'value': 'drit'}
                    ],
                    placeholder="Select a Dog Rescue Category Filter",
                    style={'marginLeft': 5, 'width': 350}
                )
            ])
        ]
    ),
    html.Hr(),
    dt.DataTable(
        id='datatable-id',
        columns=[
            {"name": i, "id": i, "deletable": False, "selectable": True} for i in df.columns
        ],
        data=df.to_dict('records'),
        #Set up the features for your interactive data table to make it user-friendly for your client
        editable=False,
        filter_action="native",
        sort_action="native",
        sort_mode="multi",
        column_selectable=False,
        row_selectable="single",
        row_deletable=False,
        selected_columns=[],
        selected_rows=[0],
        page_action="native",
        page_current=0,
        page_size=10,
    ),
    html.Br(),
    html.Hr(),
    #This sets up the dashboard so that your chart and your geolocation chart are side-by-side
    html.Div(className='row',
         style={'display' : 'flex'},
             children=[
        html.Div(
            #dcc.Graph(id='graph-id'),
            id='graph-id',
            className='col s12 m6',

            ),
        html.Div(
            id='map-id',
            className='col s12 m6',
            )
        ])
])


#############################################
# Interaction Between Components / Controller
#############################################

# This callback add interactive dropdown filter option to the dashboard to find dogs per category
# or interactive button filter option to the dashboard to find all cats or all dogs
@app.callback(
    Output('datatable-id', 'data'),
    [Input('filter-type', 'value'),
     Input('submit-button-one', 'n_clicks'),
     Input('submit-button-two', 'n_clicks')]
)
# in this block, the code Checks the parameters passed through the call back
# and decides what type of data is required from the database 
#and lastly returns the data for the dashboard the refresh the datatable and display the new data
def update_dshboard(selected_filter, btn1, btn2):
    #if Disaster Rescue or Individual Tracking option selected
    if (selected_filter == 'drit'):
        # call the readAll method from the AnimalShelter class
        # pass parameters identifying the selected type of rescue
        df = pd.DataFrame(list(db.readAll(
                {
                    "animal_type":"Dog",
                    "breed":{"$in":[
                        "Doberman Pinscher","German Shepherd","Golden Retriever","Bloodhound","Rottweiler"]},
                    "sex_upon_outcome":"Intact Male",
                    "age_upon_outcome_in_weeks": {"$gte":20},
                    "age_upon_outcome_in_weeks":{"$lte":300}
                }
            )
        ))
    # if Mountain or Wilderness Rescue option is selected
    elif (selected_filter == 'mwr'):
        # call the readAll method from the AnimalShelter class
        # pass parameters identifying the selected type of rescue
        df = pd.DataFrame(list(db.readAll(
                {
                    "animal_type":"Dog",
                    "breed":{"$in":[
                        "German Shepherd","Alaskan Malamute","Old English Sheepdog",
                        "Siberian Husky","Rottweiler"]},
                    "sex_upon_outcome":"Intact Male",
                    "age_upon_outcome_in_weeks":{"$gte":26},
                    "age_upon_outcome_in_weeks":{"$lte":156}
                }
            )
        ))
    # if Water Rescue option is selected  
    elif (selected_filter == 'wr'):
        # call the readAll method from the AnimalShelter class
        # pass parameters identifying the selected type of rescue
        df = pd.DataFrame(list(db.readAll(
                {
                    "animal_type":"Dog",
                    "breed":{"$in":["Labrador Retriever Mix","Chesapeake Bay Retriever","Newfoundland"]},
                    "sex_upon_outcome":"Intact Female",
                    "age_upon_outcome_in_weeks":{"$gte":26},
                    "age_upon_outcome_in_weeks":{"$lte":156}
                }
            )
        ))
    # higher number of button clicks to determine filter type
    elif (int(btn1) > int(btn2)):
        # call the readAll method from the AnimalShelter class
        # pass parameters animal_type = Cat
        df = pd.DataFrame(list(db.readAll({"animal_type":"Cat"})))
    elif (int(btn2) > int(btn1)):
        # call the readAll method from the AnimalShelter class
        # pass parameters animal_type = Dog
        df = pd.DataFrame(list(db.readAll({"animal_type":"Dog"})))
    else:
        # when reset button is clicked, call readAll method with no parameters to return all the data
        df = pd.DataFrame.from_records(db.readAll({}))
        

    data = df.to_dict('records')

    return data

# This callback reset the clicks of the cat and dog filter button
@app.callback(
    [Output('submit-button-one', 'n_clicks'),
     Output('submit-button-two', 'n_clicks')],
    [Input('reset-buttons', 'n_clicks')]
)
def update(reset):
    return 0, 0

def disaster_rescue_filter():
    return {
        "animal_type": "Dog",
        "breed": {"$in": ["Doberman Pinscher", "German Shepherd", "Golden Retriever", "Bloodhound", "Rottweiler"]},
        "sex_upon_outcome": "Intact Male",
        "age_upon_outcome_in_weeks": {"$gte": 20, "$lte": 300}
    }


def mountain_wilderness_rescue_filter():
    return {
        "animal_type": "Dog",
        "breed": {"$in": ["German Shepherd", "Alaskan Malamute", "Old English Sheepdog", "Siberian Husky", "Rottweiler"]},
        "sex_upon_outcome": "Intact Male",
        "age_upon_outcome_in_weeks": {"$gte": 26, "$lte": 156}
    }


def water_rescue_filter():
    return {
        "animal_type": "Dog",
        "breed": {"$in": ["Labrador Retriever Mix", "Chesapeake Bay Retriever", "Newfoundland"]},
        "sex_upon_outcome": "Intact Female",
        "age_upon_outcome_in_weeks": {"$gte": 26, "$lte": 156}
    }


def cat_filter():
    return {"animal_type": "Cat"}


def dog_filter():
    return {"animal_type": "Dog"}


def reset_filter():
    return {}


def update_dashboard(selected_filter, btn1, btn2):
    filter_cases = {
        'drit': disaster_rescue_filter,
        'mwr': mountain_wilderness_rescue_filter,
        'wr': water_rescue_filter,
        'cat': cat_filter,
        'dog': dog_filter,
        'reset': reset_filter
    }

    selected_filter_fn = filter_cases.get(selected_filter, reset_filter)
    df = pd.DataFrame(list(db.readAll(selected_filter_fn())))

    data = df.to_dict('records')
    return data


def update_buttons(reset):
    if reset:
        return 0, 0
    else:
        raise PreventUpdate


# This callback add interactive dropdown filter option to the dashboard to find dogs per category
# or interactive button filter option to the dashboard to find all cats or all dogs
@app.callback(
    Output('datatable-id', 'data'),
    [Input('filter-type', 'value'),
     Input('submit-button-one', 'n_clicks'),
     Input('submit-button-two', 'n_clicks')]
)
def callback_update_dashboard(selected_filter, btn1, btn2):
    return update_dashboard(selected_filter, btn1, btn2)


# This callback reset the clicks of the cat and dog filter button
@app.callback(
    [Output('submit-button-one', 'n_clicks'),
     Output('submit-button-two', 'n_clicks')],
    [Input('reset-buttons', 'n_clicks')]
)
def callback_update_buttons(reset):
    return update_buttons(reset)


#This callback will highlight a cell on the data table when the user selects it
@app.callback(
    Output('datatable-id', 'style_data_conditional'),
    [Input('datatable-id', 'selected_columns')]
)
def update_styles(selected_columns):
    return [{
        'if': { 'column_id': i },
        'background_color': '#D2F3FF'
    } for i in selected_columns]


#function to update the pie chart
@app.callback(
    Output('graph-id', "children"),
    [Input('datatable-id', "derived_viewport_data")])
def update_graphs(viewData):
    # imports the currently displayed data
    dff = pd.DataFrame.from_dict(viewData)
    #creates the values needed for the names (breed) and values (recurring counts)
    names = dff['breed'].value_counts().keys().tolist()
    values = dff['breed'].value_counts().tolist()
    #creates a pie chart based on the data above
    return [
        dcc.Graph(            
            figure = px.pie(
                data_frame=dff, 
                values = values, 
                names = names, 
                color_discrete_sequence=px.colors.sequential.RdBu,
                width=800, 
                height=500   
            )
        )
    ]


@app.callback(
    Output('map-id', "children"),
    [Input('datatable-id', "derived_virtual_data"),
     Input('datatable-id', "derived_virtual_selected_rows")])
def update_map(viewData, index):
    
    #Add geolocation chart
    dff = pd.DataFrame.from_dict(viewData)
    # Because we only allow single row selection, the list can 
    # be converted to a row index here
    if index is None:
       row = 0
    else: 
       row = index[0]
    # Austin TX is at [30.75,-97.48]
    return [
        dl.Map(style={'width': '1000px', 'height': '500px'},
           center=[30.75,-97.48], zoom=10, children=[
           dl.TileLayer(id="base-layer-id"),
           # Marker with tool tip and popup
           # Column 13 and 14 define the grid-coordinates for 
           # the map
           # Column 4 defines the breed for the animal
           # Column 9 defines the name of the animal
           dl.Marker(position=[dff.iloc[row,13],dff.iloc[row,14]],children=[
                dl.Tooltip(dff.iloc[row,4]),
                dl.Popup([
                    html.H1("Animal Name"),
                    html.P(dff.iloc[row,9])
                ])
            ])
        ])
    ]
app.run_server(debug=True)