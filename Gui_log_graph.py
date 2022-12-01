
import streamlit as st
import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=True)
st.set_page_config(layout="wide")
from import_txt import search_str
from graph_data_analyzer import creat_graph

def main():
##----------------------------------------------------------------------------------------------------------------------
##----------------------------------------------main page---------------------------------------------------------------
##----------------------------------Neural Network - by Oren Niazov-----------------------------------------------------
##----------------------------------------------------------------------------------------------------------------------
    global Run_Function, Dataset
    st.title('Graph from log file')

    if st.button('Run Function'):
        st.write('Running Function')
        Run_Function = 'Run Function'
    else:
        st.write('Press run function to start')
        Run_Function = 'Dont Run Function'
##---------------------------------------------------sidebar------------------------------------------------------------
##-------------------------------------------choose Datatype&Dataset----------------------------------------------------
##----------------------------------------------------------------------------------------------------------------------
    firstTextSearch = "'graph_title': 'DS1 Flatness and Tilt 0.0'"

    with st.sidebar:
        st.sidebar.title('choose log.txt')
        st.title('choose log.txt')
        logFileText = st.selectbox(
            'choose log.txt',
            ('log.txt', 'log.txt', 'log.txt'))

        if logFileText=='log.txt':
            Dataset = st.selectbox(
                'choose Dataset',
                ('fake_regression0', 'fake_regression1', 'fake_regression2'))

        elif log=='Classification':
            Dataset = st.selectbox(
                'choose Dataset',
                ('fake_classification0', 'classification1', 'fake_classification2'))
            st.write('Dataset:', Dataset)
        else:
            print('pay attention: something wrong with the Datatype choose')


##---------------------------------------------------sidebar------------------------------------------------------------
##-----------------------------------------download files you want to share---------------------------------------------
##----------------------------------------------------------------------------------------------------------------------
        with open("graph_data_analyzer.py") as file:
            btn = st.download_button(
                label="Download graph_data_analyzer.py Python Resources File",
                data=file,
            )

        with open("import_txt.py") as file:
            btn = st.download_button(
                label="Download import_txt Python Resources File",
                data=file,
            )

##----------------------------------------------------------------------------------------------------------------------
##----------------------------------------------main page---------------------------------------------------------------
##----------------------------------Neural Network - Run Function-------------------------------------------------------
##----------------------------------------------------------------------------------------------------------------------
    if Run_Function == 'Run Function':
        NumberDataLines, DataLines = search_str(logFileText, firstTextSearch)
        print(Fore.GREEN + str(NumberDataLines))
        print(Fore.GREEN + str(len(NumberDataLines)))
        DataLines = DataLines[0][79:]
        # print(DataLines)
        DataLines = ast.literal_eval(DataLines)
        print(type(DataLines))
        DataLines = [DataLines]
        create_graph(DataLines)

##-------------------------------------------main page------------------------------------------------------------------
##----------------------------------------tabs and Graphs---------------------------------------------------------------
##----------------------------------------------------------------------------------------------------------------------

        tab1, tab2, tab3 = st.tabs([ "NN graph", "Loss Function Per Epoch", "Predict Table", "Python Code"])
        with tab1:
            st.header("NN graph")
            NN_graph = Image.open('graphs\DS1 Flatness and Tilt 0.0.png')
            st.image(NN_graph, caption='NN_graph.png')

        with tab2:
            st.header("Loss Function Per Epoch")
            LossFunctionPerEpoch = Image.open('graphs\DS1 Flatness and Tilt 0.0.png')
            st.image(LossFunctionPerEpoch, caption='Loss Function Per Epoch')

        with tab3:
            st.header("Python Code")
            st.code(open("graph_data_analyzer.py").read(), language="python")

    elif Run_Function == 'Dont Run Function':
        print('press run function')
    else:
        print('Error with running button')


##-----------------------------------------------------------------------------------------------------------
main()



