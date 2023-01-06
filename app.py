import pandas as pd
import streamlit as st
import numpy as np
import seaborn as sns
import plotly_express as px
import matplotlib as plt
import plotly.graph_objects as go


st.set_page_config(page_title='Portafolio Titanic ', layout='centered', page_icon='⛵️')


#COSAS QUE PODEMOS USAR EN NUESTRA APP

df = pd.read_csv('https://raw.githubusercontent.com/HerculesCastro/TrabajosClase/main/titanic.csv')

# EMPIEZA NUESTRA APP

st.title('Trabajo sobre Titanic 🌊⛵️🌊')
st.image('https://cdn.pixabay.com/photo/2021/03/04/16/32/ship-6068668__340.png', width = 150)
st.text('Trabajo sobre titanic ')

st.text('Este proyecto va sobre DATOS interesantes sobre sucesos del TITANIC \ntenemos estudios y graficos')


#----------------------COLUMNAS------------------------------------------
col1, col2 = st.columns(2)
with col1:
    ##################################### ABORDANTES TITANIC SEGUN GENERO  /// GRAFICO DONUT ###################################
    labels = ['Hombres', 'Mujeres']
    contador = df['Sex'].value_counts() # Cuenta la cantidad de personas
    colors = ['deepblue', 'pink'] # Colores del grafico 
    grafico = go.Figure(data=[go.Pie(labels=labels, values=contador , hole=0.3, marker_colors = colors, pull =[0,0.1], textfont_size=15,)]) # CODIGO GRAFICO
    grafico.update_traces(textinfo='value') # Muestra el valor en vez de el porciento
    grafico.update_layout(title_text='Abordantes en el TITANIC segun su genero') # Titulo del grafico 
    st.plotly_chart(grafico) # Muestra el grafico


with col2:
    ##################################### SUPERVIVIENTES TITANIC SEGUN GENERO  /// GRAFICO PASTEL ###################################
    labels = ['Mujeres', 'Hombres'] # Titulos 
    sobrevivientes = df['Survived'].value_counts() # Contador 
    colors = ['#FB99FF', '#3359FF'] # Colores para el grafico 
    gsobre = go.Figure(data=[go.Pie(labels=labels, values=sobrevivientes, marker_colors = colors, pull=[0, 0.2], textfont_size=15,
    marker_line_width = 0, marker_line_color = 'white')]) # Color el el contorno
    gsobre.update_traces(textinfo='value') # Muestra el valor en vez de el porciento
    gsobre.update_layout(title_text='Sobrevivientes TITANIC segun su genero') # Titulo del grafico 
    st.plotly_chart(gsobre)

# STORY TELLING

st.write(''' ___________________________________________________________________________________________________
            Como podemos observar en los graficos, aunque si hubieron mas pasajeros masculinos que femeninos   
            la tasa de superviviencia es mas elevada en las mujeres que en los hombres como podemos ver en el  
            grafico de la derecha, el porque, es, que la mayoria de los hombres, dieron prioridad a los ninos, 
            mujeres y a los hombres de la clase alta. La conclusion que podemos sacar es de que, la mayoria    
            de tripulantes se quedaron en el barco ayudando a dichos pasajeros para ayudar en la supervivencia.
            ''')
            

#df['Age'](kind='pie', y='Age', shadow=False)

#edad = px.pie(df, values='Age', names= 'Age')
#st.plotly_chart(edad)





#################################### RELACION EDAD A PRECIO DEL BILLETE  /// GRAFICO SCATTER ########################################
precios = px.scatter(df, x='Age', y='Fare', color='Age', size='Fare', hover_data=['Age'], title='Relacion edad a precio del billete',
labels={
                     "Age": "Edad de los tripulantes",
                     "Fare": "Precio del billete",
                 })

precios.update_layout(
    #font_family="Courier New",
    font_color="#05a3ff",
    #title_font_family="Times New Roman",
    title_font_color="white",
    legend_title_font_color="#828282")
st.plotly_chart(precios)


#################################################### RELACION PRECIO PAGADO CON TIPO DE CABINA ##################################################################
# fmri = sns.load_dataset('titanic')
# tipos_de_clase = df['Pclass'].value_counts()

# # Plot the responses for different events and regions
# base = sns.lineplot(x=[tipos_de_clase], y=df["Fare"],
#              hue=tipos_de_clase,
#              data=fmri)
# st.plotly_chart(base)







# SIDEBAR

st.set_option('deprecation.showPyplotGlobalUse', False)
st.sidebar.image("https://i.ibb.co/vvBmkpX/ezgif-com-gif-maker.png", width=50)
st.sidebar.title("GHOST")
st.sidebar.write("---")
st.sidebar.audio('http://www.sonidosmp3gratis.com/sounds/ringtones-titanic-flute.mp3')
st.sidebar.download_button('Descargate el CSV', 'titanic.csv')

if st.sidebar.button("Mostrar Tablas 🌊"):
    st.dataframe(df)

######################## TIPOS DE CLASES ############################

prueba = sns.distplot(df['Embarked'].value_counts())
st.pyplot(prueba)

