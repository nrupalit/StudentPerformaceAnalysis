import pandas as pd
from flask import *
import os
import matplotlib.pyplot as plt
import seaborn as sns
import pyrebase
import plotly.plotly as py
import plotly.graph_objs as go
import plotly.figure_factory as FF
import plotly
import numpy as np
import pandas as pd
import json
config = {
    "apiKey": "AIzaSyCF1VG058_G7KJZanDHYMiepwiftA19Hs8",
    "authDomain": "hackathon-e7251.firebaseapp.com",
    "databaseURL": "https://hackathon-e7251.firebaseio.com",
    "projectId": "hackathon-e7251",
    "storageBucket": "hackathon-e7251.appspot.com",
    "messagingSenderId": "164726432502"
}
firebase = pyrebase.initialize_app(config)
df = pd.read_csv('final.csv')
dat = pd.read_csv('final.csv')
dat.set_index('name', inplace=True)
# df.set_index('name', inplace=True)
import xlrd
data = pd.read_excel('attend_class_old(3).xlsx')
storage = firebase.storage()
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def barebones():
    bar = bar_plot()
    ut_all = ut_bar_plot()
    return render_template('index.html', plot1=bar, plot2=ut_all)

def bar_plot():
    min = df[['CCTOTAL','CCTOTAL', 'ISTOTAL','OSTOTAL','DSTOTAL','SWSTOTAL']].min().astype(int)
    mean = df[['CCTOTAL','CCTOTAL', 'ISTOTAL','OSTOTAL','DSTOTAL','SWSTOTAL']].mean().astype(int)
    max = df[['CCTOTAL','CCTOTAL', 'ISTOTAL','OSTOTAL','DSTOTAL','SWSTOTAL']].max().astype(int)
    stack1 = go.Bar(x=min, name='Minimum', textposition='inside', marker=dict(color='#107750'))
    stack2 = go.Bar(x=mean, name='Mean', textposition='inside', marker=dict(color='#005d67'))
    stack3 = go.Bar(x=max, name='Maximum', text=['CG', 'CC', 'IS', 'OS', 'DS', 'SWS'], textposition='inside', marker=dict(color='#003f5c'))
    data = [stack1, stack2, stack3]
    

    layout = go.Layout(title='Maximum, Mean and Minimum Score',plot_bgcolor='rgb(230, 230,230)', barmode='stack')

    fig = go.Figure(data=data, layout=layout)

    graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)

    return graphJSON

def ut_bar_plot():
    stack3 = go.Bar(x=df[['CGTOTAL','CCTOTAL','DSTOTAL','ISTOTAL','OSTOTAL','SWSTOTAL']].min().astype(int), orientation = 'h', name='Minimum in UT1', textposition='inside', marker=dict(color='#107750', opacity=1))
    stack4 = go.Bar(x=df[['CGTOTAL','CCTOTAL','DSTOTAL','ISTOTAL','OSTOTAL','SWSTOTAL']].max().astype(int), orientation = 'h', name='Maximum in UT1', text=['CG','CC','DS','IS','OS','SWS'], textposition='inside', marker=dict(color='#107750', opacity=0.8))
    stack5 = go.Bar(x=df[['CGTOTAL2','CCTOTAL2','DSTOTAL2','ISTOTAL2','OSTOTAL2','SWSTOTAL2']].min().astype(int), orientation = 'h', name='Minimum in UT2', textposition='inside', marker=dict(color='#005d67', opacity=1))
    stack6 = go.Bar(x=df[['CGTOTAL2','CCTOTAL2','DSTOTAL2','ISTOTAL2','OSTOTAL2','SWSTOTAL2']].max().astype(int), orientation = 'h', name='Maximum in UT2', text=['CG','CC','DS','IS','OS','SWS'], textposition='inside', marker=dict(color='#005d67', opacity=0.8))
    data=[ stack3, stack5, stack4, stack6]
    updatemenus = list([dict(type="buttons",active=0,buttons=list([dict(label = 'Internal Assessment',method = 'update',args = [{'visible': [True, True, True, True]},{'title': 'Maximum, Minimum Score in both Unit Tests'}]),dict(label = 'Unit One',method = 'update',args = [{'visible': [True, False, True, False]},{'title': 'Maximum, Minimum Score in Unit One'}]),dict(label = 'Unit Two',method = 'update',args = [{'visible': [False, True, False, True]},{'title': 'Maximum, Minimum Score in Unit Two'}])]), showactive = True,)])
    layout = dict(title='Maximum, Minimum Score in both Unit Tests',plot_bgcolor='rgb(230, 230,230)', barmode='overlay', showlegend=False,updatemenus=updatemenus)

    fig = dict(data=data, layout=layout)

    graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)

    return graphJSON   



@app.route('/subjectpie', methods=['GET','POST'])

def sub_pie():
    if request.method == 'POST':
        select = request.form['selection']
        if select == 'SWS':
            labels = ['SWSQ1', 'SWSQ2', 'SWSQ3', 'SWSQ4', 'SWSQ5', 'SWSQ6']
            values = df[['SWSQ1', 'SWSQ2', 'SWSQ3', 'SWSQ4', 'SWSQ5', 'SWSQ6']].sum().astype(int)
            title = 'System and Web Security Score'
        elif select == 'DS':
            labels = ['DSQ1', 'DSQ2', 'DSQ3', 'DSQ4', 'DSQ5', 'DSQ6']
            values = df[['DSQ1', 'DSQ2', 'DSQ3', 'DSQ4', 'DSQ5', 'DSQ6']].sum().astype(int)
            title = 'Data Structure Score'
        elif select == 'OS':
            labels = ['OSQ1', 'OSQ2', 'OSQ3', 'OSQ4', 'OSQ5', 'OSQ6']
            values = df[['OSQ1', 'OSQ2', 'OSQ3', 'OSQ4', 'OSQ5', 'OSQ6']].sum().astype(int)
            title = 'Operating System Score'
        elif select == 'IS':
            labels = ['ISQ1', 'ISQ2', 'ISQ3', 'ISQ4', 'ISQ5', 'ISQ6']
            values = df[['ISQ1', 'ISQ2', 'ISQ3', 'ISQ4', 'ISQ5', 'ISQ6']].sum().astype(int)
            title = 'Intelligent System Score'
        elif select == 'CC':
            labels = ['CCQ1','CCQ2', 'CCQ3', 'CCQ4', 'CCQ5', 'CCQ6']
            values = df[['CCQ1','CCQ2', 'CCQ3', 'CCQ4', 'CCQ5', 'CCQ6']].sum().astype(int)
            title = 'Cloud Computing Score'
        elif select == 'CG':
            labels = ['CGQ1', 'CGQ2', 'CGQ3', 'CGQ4', 'CGQ5', 'CGQ6']
            values = df[['CGQ1', 'CGQ2', 'CGQ3', 'CGQ4', 'CGQ5', 'CGQ6']].sum().astype(int)
            title = 'Computer Graphics Score'
        trace = go.Pie(labels=labels, values=values, text=labels, name='Minimum', marker=dict(colors=['#003f5c','#444e86','#955196','#dd5182','#ff6e54','#ffa600']),hole=0.9)
        data = [trace]
        layout = go.Layout(title=title,plot_bgcolor='rgb(230, 230,230)')
        fig = go.Figure(data=data, layout=layout)
        graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
        return render_template('subjectwisepie.html', plot_pie=graphJSON)
    return render_template('index.html')




@app.route('/utpieselect', methods=['GET', 'POST'])

def utpieselect():
    if request.method == 'POST':
        # plt.clf()
        ut = request.form['ut']
        select = request.form['selections']
        if select == 'SWS' and ut == 'ut1':
            labels = ['SWSQ1', 'SWSQ2', 'SWSQ3']
            values = df[['SWSQ1', 'SWSQ2', 'SWSQ3']].sum().astype(int)
            title = 'System and Web Security Score of Unit Test One'
        elif select == 'SWS' and ut == 'ut2':
            labels = ['SWSQ4', 'SWSQ5', 'SWSQ6']
            values = df[['SWSQ4', 'SWSQ5', 'SWSQ6']].sum().astype(int)
            title = 'System and Web Security Score of Unit Test One'
        elif select == 'DS' and ut == 'ut1':
            labels = ['DSQ1', 'DSQ2', 'DSQ3']
            values = df[['DSQ1', 'DSQ2', 'DSQ3']].sum().astype(int)
            title = 'Data Structures Score of Unit Test One'
        elif select == 'DS' and ut == 'ut2':
            labels = ['DSQ4', 'DSQ5', 'DSQ6']
            values = df[['DSQ4', 'DSQ5', 'DSQ6']].sum().astype(int)
            title = 'Data Structures Score of Unit Two'
        elif select == 'OS' and ut == 'ut1':
            labels = ['OSQ1', 'OSQ2', 'OSQ3']
            values = df[['OSQ1', 'OSQ2', 'OSQ3']].sum().astype(int)
            title = 'Operating System Score of Unit One'
        elif select == 'OS' and ut == 'ut2':
            labels = ['OSQ4', 'OSQ5', 'OSQ6']
            values = df[['OSQ4', 'OSQ5', 'OSQ6']].sum().astype(int)
            title = 'Operating System Score of Unit Two'
        elif select == 'IS' and ut == 'ut1':
            labels = ['ISQ1', 'ISQ2', 'ISQ3']
            values = df[['ISQ1', 'ISQ2', 'ISQ3']].sum().astype(int)
            title = 'Intelligent System Score of Unit One'
        elif select == 'IS' and ut == 'ut2':
            labels = ['ISQ4', 'ISQ5', 'ISQ6']
            values = df[['ISQ4', 'ISQ5', 'ISQ6']].sum().astype(int)
            title = 'Intelligent System Score of Unit Two'
        elif select == 'CC' and ut == 'ut1':
            labels = ['CCQ1', 'CCQ2', 'CCQ3']
            values = df[['CCQ1', 'CCQ2', 'CCQ3']].sum().astype(int)
            title = 'Cloud Computing Score of Unit One'
        elif select == 'CC' and ut == 'ut2':
            labels = ['CCQ4', 'CCQ5', 'CCQ6']
            values = df[['CCQ4', 'CCQ5', 'CCQ6']].sum().astype(int)
            text = 'Cloud Computing Score of Unit Two'
        elif select == 'CG' and ut == 'ut1':
            labels = ['CGQ1', 'CGQ2', 'CGQ3']
            values = df[['CGQ1', 'CGQ2', 'CGQ3']].sum().astype(int)
            text = 'Computer Graphics Score of Unit One'
        elif select == 'CG' and ut == 'ut2':
            labels = ['CGQ4', 'CGQ5', 'CGQ6']
            values = df[['CGQ4', 'CGQ5', 'CGQ6']].sum().astype(int)
            text = 'Computer Graphics Score of Unit Two'
        trace = go.Pie(labels=labels, values=values, text=labels, marker=dict(colors=['#003f5c','#444e86','#955196','#dd5182','#ff6e54','#ffa600']),hole=0.9)
        data = [trace]
        layout = go.Layout(title=title ,plot_bgcolor='rgb(230, 230,230)')
        fig = go.Figure(data=data, layout=layout)
        graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
        return render_template('subjectwiseutpie.html', plot_pie=graphJSON)
    return render_template('index.html')

@app.route('/horizontalbar', methods=['GET', 'POST'])
def horizontalbar():
    if request.method == 'POST':
        select = request.form['selections']
        uts = request.form['uts']
        if select == 'SWS' and uts == 'ut1':
            t1 = df['SWSQ1']
            t2 = df['SWSQ2']
            t3 = df['SWSQ3']
            text1 = 'SWSQ1'
            text2 = 'SWSQ2'
            text3 = 'SWSQ3'
            title = 'System and Web Security Score of Unit Test One'
        elif select == 'SWS' and uts == 'ut2':
            t1 = df['SWSQ4']
            t2 = df['SWSQ5']
            t3 = df['SWSQ6']
            text1 = 'SWSQ4'
            text2 = 'SWSQ5'
            text3 = 'SWSQ6'
            title = 'System and Web Security Score of Unit Test One'
        elif select == 'DS' and uts == 'ut1':
            t1 = df['DSQ1']
            t2 = df['DSQ2']
            t3 = df['DSQ3']
            text1 = 'DSQ1'
            text2 = 'DSQ2'
            text3 = 'DSQ3'
            title = 'Data Structures Score of Unit Test One'
        elif select == 'DS' and uts == 'ut2':
            t1 = df['DSQ4']
            t2 = df['DSQ5']
            t3 = df['DSQ6']
            text1 = 'DSQ4'
            text2 = 'DSQ5'
            text3 = 'DSQ6'
            title = 'Data Structures Score of Unit Two'
        elif select == 'OS' and uts == 'ut1':
            t1 = df['OSQ1']
            t2 = df['OSQ2']
            t3 = df['OSQ3']
            text1 = 'OSQ1'
            text2 = 'OSQ2'
            text3 = 'OSQ3'
            title = 'Operating System Score of Unit One'
        elif select == 'OS' and uts == 'ut2':
            t1 = df['OSQ4']
            t2 = df['OSQ5']
            t3 = df['OSQ6']
            text1 = 'OSQ4'
            text2 = 'OSQ5'
            text3 = 'OSQ6'
            title = 'Operating System Score of Unit Two'
        elif select == 'IS' and uts == 'ut1':
            t1 = df['ISQ1']
            t2 = df['ISQ2']
            t3 = df['ISQ3']
            text1 = 'ISQ1'
            text2 = 'ISQ2'
            text3 = 'ISQ3'
            title = 'Intelligent System Score of Unit One'
        elif select == 'IS' and uts == 'ut2':
            t1 = df['ISQ4']
            t2 = df['ISQ5']
            t3 = df['ISQ6']
            text1 = 'ISQ4'
            text2 = 'ISQ5'
            text3 = 'ISQ6'
            title = 'Intelligent System Score of Unit Two'
        elif select == 'CC' and uts == 'ut1':
            t1 = df['CCQ1']
            t2 = df['CCQ2']
            t3 = df['CCQ3']
            text1 = 'CCQ1' 
            text2 = 'CCQ2'
            text3 = 'CCQ3'
            title = 'Cloud Computing Score of Unit One'
        elif select == 'CC' and uts == 'ut2':
            t1 = df['CCQ4']
            t2 = df['CCQ5']
            t3 = df['CCQ6']
            text1 = 'CCQ4' 
            text2 = 'CCQ5'
            text3 = 'CCQ6'
            text = 'Cloud Computing Score of Unit Two'
        elif select == 'CG' and uts == 'ut1':
            t1 = df['CGQ1']
            t2 = df['CGQ2']
            t3 = df['CGQ3']
            text1 = 'CGQ1'
            text2 = 'CGQ2'
            text3 = 'CGQ3'
            text = 'Computer Graphics Score of Unit One'
        elif select == 'CG' and uts == 'ut2':
            t1 = df['CGQ4']
            t2 = df['CGQ5']
            t3 = df['CGQ6']
            text1 = 'CGQ4'
            text2 = 'CGQ5'
            text3 = 'CGQ6'
            text = 'Computer Graphics Score of Unit Two'
        x = df['name']
        trace1 = go.Bar(x=x, y=t1, name=text1, marker=dict(color='#107750', opacity=0.8))
        trace2 = go.Bar(x=x, y=t2, name=text2, marker=dict(color='#7c9b23', opacity=0.8))
        trace3 = go.Bar(x=x, y=t3, name=text3, marker=dict(color='#ffa600', opacity=0.8))
        layout = go.Layout(title=title ,xaxis=dict(tickfont=dict(size=8)), barmode='stack', bargap= 0.3)
        fig = go.Figure(data=[trace1, trace2, trace3], layout=layout)

        graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)

        return render_template('allstud.html', plot_pie2=graphJSON)
    return render_template('index.html')


@app.route('/formone', methods=['GET', 'POST'])
def formone():
    if request.method == 'POST':
        return redirect(url_for('lineutwise'))
    return render_template('index.html')


@app.route('/lineutwise', methods=['GET', 'POST'])
def lineutwise():
    # df.set_index('name', inplace=True) 
    if request.method == 'POST':
        name = request.form['search']
        select = request.form['selections']
        names = df.loc[df['name'] == name]
        if select == 'ut1':
            selection = names[['OSTOTAL', 'DSTOTAL', 'ISTOTAL', 'SWSTOTAL', 'CCTOTAL', 'CGTOTAL']].astype(int)
            text = ['OSTOTAL', 'DSTOTAL', 'ISTOTAL', 'SWSTOTAL', 'CCTOTAL', 'CGTOTAL']
            title = 'Unit One'
        elif select == 'ut2':
            selection = names[['OSTOTAL2', 'DSTOTAL2', 'ISTOTAL2', 'SWSTOTAL2', 'CCTOTAL2', 'CGTOTAL2']].astype(int)
            text = ['OSTOTAL2', 'DSTOTAL2', 'ISTOTAL2', 'SWSTOTAL2', 'CCTOTAL2', 'CGTOTAL2']
            title = 'Unit Two'
        elif select == 'Internal Assessment':
            selection = names[['OSFULL', 'DSFULL', 'ISFULL', 'SWSFULL', 'CCFULL', 'CGFULL']].astype(int)
            text = ['OSFULL', 'DSFULL', 'ISFULL', 'SWSFULL', 'CCFULL', 'CGFULL']
            title = 'Internal Assessment'
        names = selection.values
        y=names[0]
        title = name + ' - ' + title
        trace = go.Scatter(y=y, text=text, mode='lines+text+markers', textposition='top center')
        layout = go.Layout(title=title ,xaxis=dict(tickfont=dict(size=8)))
        fig = go.Figure(data=[trace], layout=layout)
        graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
        return render_template('subjectwiseutpie.html', plot_pie=graphJSON)
    return render_template('formone.html')   
    
@app.route('/lineutwiseviewer', methods=['GET', 'POST'])
def lineutwiseviewer():
    a = storage.child("LineUTWise/lineutwise.png").get_url(None)
    if request.method == 'POST':
        return redirect(url_for('barebones'))
    return render_template('lineutwiseviewer.html', a=a)


@app.route('/formtwo', methods=['GET', 'POST'])
def formtwo():
    if request.method == 'POST':
        return redirect(url_for('coutwise'))
    return render_template('index.html')



@app.route('/coutwise', methods=['GET', 'POST'])
def coutwise():
    if request.method == 'POST':
        name = request.form['search']
        select = request.form['selections']
        uts = request.form['uts']
        names = df.loc[df['name'] == name]
        if select == 'SWS' and uts == 'ut1':
            name1 = names[['SWSQ1', 'SWSQ2', 'SWSQ3']]
            text = ['SWSQ1', 'SWSQ2', 'SWSQ3']
            title = 'System and Web Security Score of Unit Test One'
        elif select == 'SWS' and uts == 'ut2':
            name1 = names[['SWSQ4', 'SWSQ5', 'SWSQ6']]
            text = ['SWSQ4', 'SWSQ5', 'SWSQ6']
            title = 'System and Web Security Score of Unit Test One'
        elif select == 'DS' and uts == 'ut1':
            name1 = names[['DSQ1', 'DSQ2', 'DSQ3']]
            text = ['DSQ1', 'DSQ2', 'DSQ3']
            title = 'Data Structures Score of Unit Test One'
        elif select == 'DS' and uts == 'ut2':
            name1 = names[['DSQ4', 'DSQ5', 'DSQ6']]
            text = ['DSQ4', 'DSQ5', 'DSQ6']
            title = 'Data Structures Score of Unit Two'
        elif select == 'OS' and uts == 'ut1':
            name1 = names[['OSQ1', 'OSQ2', 'OSQ3']]
            text = ['OSQ1', 'OSQ2', 'OSQ3']
            title = 'Operating System Score of Unit One'
        elif select == 'OS' and uts == 'ut2':
            name1 = names[['OSQ4', 'OSQ5', 'OSQ6']]
            text = ['OSQ4', 'OSQ5', 'OSQ6']
            title = 'Operating System Score of Unit Two'
        elif select == 'IS' and uts == 'ut1':
            name1 = names[['ISQ1', 'ISQ2', 'ISQ3']]
            text = ['ISQ1', 'ISQ2', 'ISQ3']
            title = 'Intelligent System Score of Unit One'
        elif select == 'IS' and uts == 'ut2':
            name1 = names[['ISQ4', 'ISQ5', 'ISQ6']]
            text = ['ISQ4', 'ISQ5', 'ISQ6']
            title = 'Intelligent System Score of Unit Two'
        elif select == 'CC' and uts == 'ut1':
            name1 = names[['CCQ1', 'CCQ2', 'CCQ3']]
            text = ['CCQ1', 'CCQ2', 'CCQ3']
            title = 'Cloud Computing Score of Unit One'
        elif select == 'CC' and uts == 'ut2':
            name1 = names[['CCQ4', 'CCQ5', 'CCQ6']]
            text = ['CCQ4', 'CCQ5', 'CCQ6']
            title = 'Cloud Computing Score of Unit Two'
        elif select == 'CG' and uts == 'ut1':
            name1 = names[['CGQ1', 'CGQ2', 'CGQ3']]
            text = ['CGQ1', 'CGQ2', 'CGQ3']
            title = 'Computer Graphics Score of Unit One'
        elif select == 'CG' and uts == 'ut2':
            name1 = names[['CGQ4', 'CGQ5', 'CGQ6']]
            text = ['CGQ4', 'CGQ5', 'CGQ6']
            title = 'Computer Graphics Score of Unit Two'
        elif select == 'SWS' and uts == 'Internal Assessment':
            name1 = names[['SWSQ1', 'SWSQ2', 'SWSQ3', 'SWSQ4', 'SWSQ5', 'SWSQ6']].astype(int)
            text = ['SWSQ1', 'SWSQ2', 'SWSQ3', 'SWSQ4', 'SWSQ5', 'SWSQ6']
            title = 'System and Web Security Full Score'
        elif select == 'DS' and uts == 'Internal Assessment':
            name1 = names[['DSQ1', 'DSQ2', 'DSQ3', 'DSQ4', 'DSQ5', 'DSQ6']].astype(int)
            text = ['DSQ1', 'DSQ2', 'DSQ3', 'DSQ4', 'DSQ5', 'DSQ6']
            title = 'Data Structures Full Score'
        elif select == 'IS' and uts == 'Internal Assessment':
            name1 = names[['ISQ1', 'ISQ2', 'ISQ3', 'ISQ4', 'ISQ5', 'ISQ6']].astype(int)
            text = ['ISQ1', 'ISQ2', 'ISQ3', 'ISQ4', 'ISQ5', 'ISQ6']
            title = 'Intelligent System Security Full Score'
        elif select == 'CC' and uts == 'Internal Assessment':
            name1 = names[['CCQ1', 'CCQ2', 'CCQ3', 'CCQ4', 'CCQ5', 'CCQ6']].astype(int)
            text = ['CCQ1', 'CCQ2', 'CCQ3', 'CCQ4', 'CCQ5', 'CCQ6']
            title = 'Cloud Computing Full Score'
        elif select == 'CG' and uts == 'Internal Assessment':
            name1 = names[['CGQ1', 'CGQ2', 'CGQ3', 'CGQ4', 'CGQ5', 'CGQ6']].astype(int)
            text = ['CGQ1', 'CGQ2', 'CGQ3', 'CGQ4', 'CGQ5', 'CGQ6']
            title = 'Computer Graphics Full Score'
        mid = name1.values
        y=mid[0]
        title = name + ' - ' + title
        trace = go.Scatter(y=y, text=text, mode='lines+text+markers', textposition='top center')
        layout = go.Layout(title=title ,xaxis=dict(tickfont=dict(size=8)))
        fig = go.Figure(data=[trace], layout=layout)
        graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
        return render_template('subjectwiseutpie.html', plot_pie=graphJSON)
        # return render_template('subjectwiseutpie.html', m=y)
    return render_template('formtwo.html')
    


@app.route('/coutwiseviewer', methods=['GET', 'POST'])
def coutwiseviewer():
    a = storage.child("CoUtWise/coutwise.png").get_url(None)
    if request.method == 'POST':
        return redirect(url_for('barebones'))
    return render_template('coutwiseviewer.html', a=a)


@app.route('/formthree', methods=['GET', 'POST'])
def formthree():
    if request.method == 'POST':
        return redirect(url_for('indivipie'))
    return render_template('index.html')


@app.route('/indivipie', methods=['GET', 'POST'])
def indivipie():
    if request.method == 'POST':
        # plt.clf()
        name = request.form['search']
        names = df.loc[df['name'] == name]
        select = request.form['selections']
        ut = request.form['uts']
        select = request.form['selections']
        if select == 'SWS' and ut == 'ut1':
            labels = ['SWSQ1', 'SWSQ2', 'SWSQ3']
            val = names[['SWSQ1', 'SWSQ2', 'SWSQ3']].sum().astype(int)
            title = 'System and Web Security Score of Unit Test One'
        elif select == 'SWS' and ut == 'ut2':
            labels = ['SWSQ4', 'SWSQ5', 'SWSQ6']
            val = names[['SWSQ4', 'SWSQ5', 'SWSQ6']].sum().astype(int)
            title = 'System and Web Security Score of Unit Test One'
        elif select == 'DS' and ut == 'ut1':
            labels = ['DSQ1', 'DSQ2', 'DSQ3']
            val = names[['DSQ1', 'DSQ2', 'DSQ3']].sum().astype(int)
            title = 'Data Structures Score of Unit Test One'
        elif select == 'DS' and ut == 'ut2':
            labels = ['DSQ4', 'DSQ5', 'DSQ6']
            val = names[['DSQ4', 'DSQ5', 'DSQ6']].sum().astype(int)
            title = 'Data Structures Score of Unit Two'
        elif select == 'OS' and ut == 'ut1':
            labels = ['OSQ1', 'OSQ2', 'OSQ3']
            val = names[['OSQ1', 'OSQ2', 'OSQ3']].sum().astype(int)
            title = 'Operating System Score of Unit One'
        elif select == 'OS' and ut == 'ut2':
            labels = ['OSQ4', 'OSQ5', 'OSQ6']
            val = names[['OSQ4', 'OSQ5', 'OSQ6']].sum().astype(int)
            title = 'Operating System Score of Unit Two'
        elif select == 'IS' and ut == 'ut1':
            labels = ['ISQ1', 'ISQ2', 'ISQ3']
            val = names[['ISQ1', 'ISQ2', 'ISQ3']].sum().astype(int)
            title = 'Intelligent System Score of Unit One'
        elif select == 'IS' and ut == 'ut2':
            labels = ['ISQ4', 'ISQ5', 'ISQ6']
            val = names[['ISQ4', 'ISQ5', 'ISQ6']].sum().astype(int)
            title = 'Intelligent System Score of Unit Two'
        elif select == 'CC' and ut == 'ut1':
            labels = ['CCQ1', 'CCQ2', 'CCQ3']
            val = names[['CCQ1', 'CCQ2', 'CCQ3']].sum().astype(int)
            title = 'Cloud Computing Score of Unit One'
        elif select == 'CC' and ut == 'ut2':
            labels = ['CCQ4', 'CCQ5', 'CCQ6']
            val = names[['CCQ4', 'CCQ5', 'CCQ6']].sum().astype(int)
            title = 'Cloud Computing Score of Unit Two'
        elif select == 'CG' and ut == 'ut1':
            labels = ['CGQ1', 'CGQ2', 'CGQ3']
            val = names[['CGQ1', 'CGQ2', 'CGQ3']].sum().astype(int)
            title = 'Computer Graphics Score of Unit One'
        elif select == 'CG' and ut == 'ut2':
            labels = ['CGQ4', 'CGQ5', 'CGQ6']
            val = names[['CGQ4', 'CGQ5', 'CGQ6']].sum().astype(int)
            title = 'Computer Graphics Score of Unit Two'
        text = name + ' - ' + title
        trace = go.Pie(labels=labels, values=val, text=labels, marker=dict(colors=['#003f5c','#444e86','#955196','#dd5182','#ff6e54','#ffa600']),hole=0.9)
        data = [trace]
        layout = go.Layout(title=text ,plot_bgcolor='rgb(230, 230,230)')
        fig = go.Figure(data=data, layout=layout)
        graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
        return render_template('subjectwiseutpie.html', plot_pie=graphJSON)
    return render_template('formthree.html')

@app.route('/indivipieviewer', methods=['GET', 'POST'])
def indivipieviewer():
    a = storage.child("IndividualPie/indivipie.png").get_url(None)
    if request.method == 'POST':
        return redirect(url_for('barebones'))
    return render_template('indivipieviewer.html', a=a)


@app.route('/formfour', methods=['GET', 'POST'])
def formfour():
    if request.method == 'POST':
        return redirect(url_for('indiviallcopie'))
    return render_template('index.html')


@app.route('/indiviallcopie', methods=['GET', 'POST'])
def indiviallcopie():
    if request.method == 'POST':
        name = request.form['search']
        names = df.loc[df['name'] == name]
        select = request.form['selections']
        if select == 'SWS':
            labels = ['SWSQ1', 'SWSQ2', 'SWSQ3', 'SWSQ4', 'SWSQ5', 'SWSQ6']
            val = names[['SWSQ1', 'SWSQ2', 'SWSQ3', 'SWSQ4', 'SWSQ5', 'SWSQ6']].sum().astype(int)
            title = 'System and Web Security Score '
        elif select == 'DS':
            labels = ['DSQ1', 'DSQ2', 'DSQ3','DSQ4', 'DSQ5', 'DSQ6']
            val = names[['DSQ1', 'DSQ2', 'DSQ3', 'DSQ4', 'DSQ5', 'DSQ6']].sum().astype(int)
            title = 'Data Structures Score'
        elif select == 'OS':
            labels = ['OSQ1', 'OSQ2', 'OSQ3', 'OSQ4', 'OSQ5', 'OSQ6']
            val = names[['OSQ1', 'OSQ2', 'OSQ3', 'OSQ4', 'OSQ5', 'OSQ6']].sum().astype(int)
            title = 'Operating System Score'
        elif select == 'IS':
            labels = ['ISQ1', 'ISQ2', 'ISQ3', 'ISQ4', 'ISQ5', 'ISQ6']
            val = names[['ISQ1', 'ISQ2', 'ISQ3']].sum().astype(int)
            title = 'Intelligent System Score'
        elif select == 'CC':
            labels = ['CCQ1', 'CCQ2', 'CCQ3', 'CCQ4', 'CCQ5', 'CCQ6']
            val = names[['CCQ1', 'CCQ2', 'CCQ3', 'CCQ4', 'CCQ5', 'CCQ6']].sum().astype(int)
            title = 'Cloud Computing Score'
        elif select == 'CG':
            labels = ['CGQ1', 'CGQ2', 'CGQ3', 'CGQ4', 'CGQ5', 'CGQ6']
            val = names[['CGQ1', 'CGQ2', 'CGQ3', 'CGQ4', 'CGQ5', 'CGQ6']].sum().astype(int)
            title = 'Computer Graphics Score'
        text = name + ' - ' + title
        trace = go.Pie(labels=labels, values=val, text=labels, marker=dict(colors=['#003f5c','#444e86','#955196','#dd5182','#ff6e54','#ffa600']),hole=0.9)
        data = [trace]
        layout = go.Layout(title=text ,plot_bgcolor='rgb(230, 230,230)')
        fig = go.Figure(data=data, layout=layout)
        graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
        return render_template('subjectwiseutpie.html', plot_pie=graphJSON)
    return render_template('formfour.html')
    
@app.route('/indiviallcopieviewer', methods=['GET', 'POST'])
def indiviallcopieviewer():
    a = storage.child("IndiviAllCoPie/indiviallcopie.png").get_url(None)
    if request.method == 'POST':
        return redirect(url_for('barebones'))
    return render_template('indiviallcopieviewer.html', a=a)


@app.route('/markslessthan', methods=['GET', 'POST'])
def markslessthan():
    if request.method == 'POST':
        nos = request.form['nos']
        selections = request.form['selections']
        uts = request.form['uts']
        if selections == 'SWS' and uts == 'Unit One':
            fillers = 'SWSTOTAL'
        elif selections == 'SWS' and uts == 'Unit Two':
            fillers = 'SWSTOTAL2'
        elif selections == 'OS' and uts == 'Unit One':
            fillers = 'OSTOTAL'
        elif selections == 'OS' and uts == 'Unit Two':
            fillers = 'OSTOTAL2'
        elif selections == 'DS' and uts == 'Unit One':
            fillers = 'DSTOTAL'
        elif selections == 'DS' and uts == 'Unit Two':
            fillers = 'DSTOTAL2'
        elif selections == 'IS' and uts == 'Unit One':
            fillers = 'ISTOTAL'
        elif selections == 'IS' and uts == 'Unit Two':
            fillers = 'ISTOTAL2'
        elif selections == 'CC' and uts == 'Unit One':
            fillers = 'CCTOTAL'
        elif selections == 'CC' and uts == 'Unit Two':
            fillers = 'CCTOTAL2'
        elif selections == 'CG' and uts == 'Unit One':
            fillers = 'CGTOTAL'
        elif selections == 'CG' and uts == 'Unit Two':
            fillers = 'CGTOTAL2'
        dff = pd.read_csv('final.csv')
        dff.set_index('Roll. No', inplace=True)
        x = dff.loc[(dff[fillers]<int(nos))]
        y = x[fillers]
        x = x[['name', fillers]]
        names = x['name']
        
        x.to_csv('lessmarks.csv')
        storage.child("CSV/lessmarks.csv").put("lessmarks.csv")
        sns.set(style="darkgrid")
        try:
            
            # Initialize the matplotlib figure
            #f, ax = plt.subplots(figsize=(6, 15))
            plt.clf()
            sns.set_color_codes("dark")
            sns.barplot(x=y, y=names, data=x,
                        color="g")
            #sns.set(xlabel='Marks', ylabel='Name of Students')
            sns.despine(left=True, bottom=True)
            plt.tight_layout()
            plt.xlabel("Marks")
            plt.ylabel("Name of Students")
            plt.title(selections+" marks less than "+nos+" in "+uts)
            if os.path.isfile('lessthan.png'):
                os.remove('lessthan.png')
            plt.savefig('lessthan.png')
        except ValueError:
            return redirect(url_for('barebones'))
        storage.child("CSV/lessthan.png").put("lessthan.png")
        b = storage.child("CSV/lessthan.png").get_url(None)
        a = storage.child("CSV/lessmarks.csv").get_url(None)
        plt.clf()
        plt.cla()
        plt.close()
        return render_template('lessmarks.html', a=a, b=b)

    return render_template('index.html')

@app.route('/lessmarksviewer', methods=['GET', 'POST'])
def lessmarksviewer():
    if request.method == 'POST':
        button = request.form['submit']
        if button == 'download':
            return render_template('lessmarks.html')
        elif button == 'reverts':
            return redirect(url_for('barebones'))
    return render_template('lessmarks.html')

@app.route('/wholeattendance', methods=['GET', 'POST'])
def wholeattendance():
    if request.method == 'POST':
        nos = request.form['nos']
        a = data.loc[(data['Attendance']<int(nos))]
        a = a[['Student Name', 'Attendance']]
        a.to_csv('attendance.csv')
        try:

            # Initialize the matplotlib figure
            #f, ax = plt.subplots(figsize=(6, 15))
            plt.clf()
            sns.set_color_codes("bright")
            sns.barplot(x=a['Attendance'], y=a['Student Name'], data=a,
                        color="r")
            #sns.set(xlabel='Marks', ylabel='Name of Students')
            sns.despine(left=True, bottom=True)
            plt.tight_layout()
            plt.xlabel("Attendance")
            plt.ylabel("Name of Students")
            plt.title("Attendance of students below "+nos)
            if os.path.isfile('attendance.png'):
                os.remove('attendance.png')
            plt.savefig('attendance.png')
            plt.clf()
            plt.cla()
            plt.close()
            storage.child("attendance/attendance.png").put("attendance.png")
            a = storage.child("attendance/attendance.png").get_url(None)
        except ValueError:
            return redirect(url_for('wholeattendance'))
        storage.child("attendance/attendance.csv").put("attendance.csv")
        b = storage.child("attendance/attendance.csv").get_url(None)
        return render_template('attendanceviewer.html', b=b, a=a)
    return render_template('index.html')

@app.route('/attendanceviewer', methods=['GET', 'POST'])
def attendanceviewer():
    if request.method == 'POST':
        button = request.form['submit']
        if button == 'download':
            return render_template('attendanceviewer.html')
        elif button == 'reverts':
            return redirect(url_for('barebones'))
    return render_template('attendanceviewer.html')


@app.route('/subatte', methods=['GET', 'POST'])
def subatte():
    if request.method == 'POST':
        nos = request.form['nos']
        selections = request.form['selections']
        if selections == 'SWS':
            select = 'SWSPER'
        elif selections == 'OS':
            select = 'OSPER'
        elif selections == 'DS':
            select = 'DSPER'
        elif selections == 'IS':
            select = 'ISPER'
        elif selections == 'CC':
            select = 'CCPER'
        elif selections == 'CG':
            select = 'CGPER'

        a = data.loc[(data[select] < int(nos))]
        a = a[['Student Name', select]]
        a.to_csv('subjectattendance.csv')
        try:

            # Initialize the matplotlib figure
            #f, ax = plt.subplots(figsize=(6, 15))
            plt.clf()
            sns.set_color_codes("bright")
            sns.barplot(x=a[select], y=a['Student Name'], data=a,
                        color="r")
            #sns.set(xlabel='Marks', ylabel='Name of Students')
            sns.despine(left=True, bottom=True)
            plt.tight_layout()
            plt.xlabel("Attendance of "+selections)
            plt.ylabel("Name of Students")
            plt.title("Attendance of students below "+nos+" in "+selections)
            if os.path.isfile('subjectattendance.png'):
                os.remove('subjectattendance.png')
            plt.savefig('subjectattendance.png')
            plt.clf()
            plt.cla()
            plt.close()
            storage.child(
                "attendance/subjectattendance.png").put("subjectattendance.png")
            a = storage.child("attendance/subjectattendance.png").get_url(None)
        except ValueError:
            return redirect(url_for('basic'))
        storage.child(
            "attendance/subjectattendance.csv").put("subjectattendance.csv")
        b = storage.child("attendance/subjectattendance.csv").get_url(None)
        return render_template('subjectattendanceviewer.html', b=b, a=a)
    return render_template('index.html')


@app.route('/subjectattendance', methods=['GET', 'POST'])
def subjectattendanceviewer():
    if request.method == 'POST':
        button = request.form['submit']
        if button == 'download':
            return render_template('subjectattendanceviewer.html')
        elif button == 'reverts':
            return redirect(url_for('barebones'))
    return render_template('subjectattendanceviewer.html')



@app.route("/search")
def search():
	text = request.args['searchText']  # get the text to search for
	# create an array with the elements of BRAZIL_STATES that contains the string
	# the case is ignored
	result = [c for c in dat.index.values.astype(
		'unicode') if text.lower() in c.lower()]
	# return as JSON
	return json.dumps({"results": result})


if __name__ == '__main__':
    app.run(debug = True)
