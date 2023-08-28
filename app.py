from flask import Flask,jsonify, make_response,render_template
import os
from py2neo import Graph
import logging
from json2html import *
import pandas as pd
from getDFforHTML import get_full_df_html, get_short_df_html,get_table_html_data
from creatingMaps import create_map_from_new_xls,creat_simple_map,get_df,get_all_but_lat_lng

ROOT_PATH = os.path.realpath(os.path.dirname(__file__))
path_to_xls = ROOT_PATH + "/static/data/Hospital Rankings.xlsx"
print(f"root path : {ROOT_PATH}")
logging.basicConfig(level=logging.INFO)
# template_dir = os.path.dirname(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
temp_dir = "templates"

app = Flask(__name__,template_folder=temp_dir,static_folder='static')
# graph = Graph("bolt://localhost:7687", auth=("neo4j", "12345678"))

app = Flask(__name__)

# query = """
# MATCH ()-[r]->()
# RETURN count(r) as count
# """

# query="""
# MATCH (author:Author)-[r1:Wrote]->(article:Article)-[r2:Published_in]->(publisher:Publisher)
# WHERE publisher.fullJournalName='International journal of molecular sciences'
# RETURN author,r1,article,r2,publisher
# """

# query="""
# MATCH (a:Author)
# WHERE a.authorName CONTAINS 'Zhang'
# RETURN a.authorName, a.Id
# """

# query="""
# MATCH (n)
# RETURN count(n) as count
# """

# query="""
# MATCH (author:Author)-[r1:Wrote]->(article:Article)
# WHERE article.Id="37062040"
# RETURN author,r1,article
# """

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/cypherquery')
def cypherquery():
    # query_result = graph.run(query)
    # app.logger.info(f"MHz, type is {type(query_result)}")
    # df=query_result.to_data_frame()
    # df.to_excel('neo4jqu.xlsx')
    # # df_data = get_full_df_html(df)
    # df_data = get_short_df_html(df) #encoding="utf-8"
    # html_table = str(df_data.to_html())
    # html_data = get_table_html_data(html_table)
    # html_table = df_data
    html_data=''
    query = ''
    return render_template("cypherquery.html", html_data=html_data, query=query)

@app.route('/global_uni_qs_2024')
def global_uni_qs_2024():
    sheet = '2024 QSWorld University Ranking'
    iframe = create_map_from_new_xls(sheet=sheet,path_to_xls=path_to_xls,popup_text_col = 'University')
    df_data = get_all_but_lat_lng(sheet=sheet,path_to_xls=path_to_xls) #encoding="utf-8"
    html_table = str(df_data.to_html())
    html_data = get_table_html_data(html_table)
    return render_template('global_uni_qs_2024.html', iframe=iframe, html_data=html_data)
    

@app.route('/global_uni_qs_2023')
def global_uni_qs_2023():
    sheet = 'QS World University Ranking'
    iframe = create_map_from_new_xls(sheet=sheet,path_to_xls=path_to_xls,popup_text_col = 'Institution')
    df_data = get_all_but_lat_lng(sheet=sheet,path_to_xls=path_to_xls) #encoding="utf-8"
    html_table = str(df_data.to_html())
    html_data = get_table_html_data(html_table)
    return render_template('global_uni_qs_2023.html', iframe=iframe, html_data=html_data)
    

@app.route('/global_uni_shanghai')
def global_uni_shanghai():
    sheet = 'Shanghai Ranking'
    iframe = create_map_from_new_xls(sheet=sheet,path_to_xls=path_to_xls,popup_text_col = 'University')
    df_data = get_all_but_lat_lng(sheet=sheet,path_to_xls=path_to_xls) #encoding="utf-8"
    html_table = str(df_data.to_html())
    html_data = get_table_html_data(html_table)
    return render_template('global_uni_shanghai.html', iframe=iframe, html_data=html_data)
    

@app.route('/global_uni_shanghai_clinical_med')
def global_uni_shanghai_clinical_med():
    sheet = 'ShanghaiRankingClinicalMedicine'
    iframe = create_map_from_new_xls(sheet=sheet,path_to_xls=path_to_xls,popup_text_col = 'Name')
    df_data = get_all_but_lat_lng(sheet=sheet,path_to_xls=path_to_xls) #encoding="utf-8"
    html_table = str(df_data.to_html())
    html_data = get_table_html_data(html_table)
    return render_template('global_uni_shanghai_clinical_med.html', iframe=iframe, html_data=html_data)
    

@app.route('/global_uni_the')
def global_uni_the():
    sheet = 'Times Higher Education Ranking'
    iframe = create_map_from_new_xls(sheet=sheet,path_to_xls=path_to_xls,popup_text_col = 'University')
    df_data = get_all_but_lat_lng(sheet=sheet,path_to_xls=path_to_xls) #encoding="utf-8"
    html_table = str(df_data.to_html())
    html_data = get_table_html_data(html_table)
    return render_template('global_uni_the.html', iframe=iframe, html_data=html_data)
    

@app.route('/global_institutes')
def global_institutes():
    sheet = 'SCImago Ranking'
    iframe = create_map_from_new_xls(sheet=sheet,path_to_xls=path_to_xls,popup_text_col = 'Institution')
    df_data = get_all_but_lat_lng(sheet=sheet,path_to_xls=path_to_xls) #encoding="utf-8"
    html_table = str(df_data.to_html())
    html_data = get_table_html_data(html_table)
    return render_template('global_institutes.html', iframe=iframe, html_data=html_data)
    

@app.route('/global_hospitals')
def global_hospitals():
    sheet = 'Newsweek Top 250 Hospitals'
    iframe = create_map_from_new_xls(sheet=sheet,path_to_xls=path_to_xls,popup_text_col = 'Hospital')
    df_data = get_all_but_lat_lng(sheet=sheet,path_to_xls=path_to_xls) #encoding="utf-8"
    html_table = str(df_data.to_html())
    html_data = get_table_html_data(html_table)
    return render_template('global_hospitals.html', iframe=iframe, html_data=html_data)
    

@app.route('/global_hospitals_cardiacSurgery')
def global_hospitals_cardiacSurgery():
    sheet = 'NWBestSpecializedCardiacSurgery'
    iframe = create_map_from_new_xls(sheet=sheet,path_to_xls=path_to_xls,popup_text_col = 'Hospital')
    df_data = get_all_but_lat_lng(sheet=sheet,path_to_xls=path_to_xls) #encoding="utf-8"
    html_table = str(df_data.to_html())
    html_data = get_table_html_data(html_table)
    return render_template('global_hospitals_cardiacSurgery.html', iframe=iframe, html_data=html_data)
    

@app.route('/global_hospitals_cardiology')
def global_hospitals_cardiology():
    sheet = 'NWBestSpecializedCardiology'
    iframe = create_map_from_new_xls(sheet=sheet,path_to_xls=path_to_xls,popup_text_col = 'Hospital')
    df_data = get_all_but_lat_lng(sheet=sheet,path_to_xls=path_to_xls) #encoding="utf-8"
    html_table = str(df_data.to_html())
    html_data = get_table_html_data(html_table)
    return render_template('global_hospitals_cardiology.html', iframe=iframe, html_data=html_data)
    

@app.route('/global_hospitals_neurology')
def global_hospitals_neurology():
    sheet = 'NWBestSpecializedNeurology'
    iframe = create_map_from_new_xls(sheet=sheet,path_to_xls=path_to_xls,popup_text_col = 'Hospital')
    df_data = get_all_but_lat_lng(sheet=sheet,path_to_xls=path_to_xls) #encoding="utf-8"
    html_table = str(df_data.to_html())
    html_data = get_table_html_data(html_table)
    return render_template('global_hospitals_neurology.html', iframe=iframe, html_data=html_data)
    

@app.route('/global_hospitals_neurosurgery')
def global_hospitals_neurosurgery():
    sheet = 'NWBestSpecializedNeurosurgery'
    iframe = create_map_from_new_xls(sheet=sheet,path_to_xls=path_to_xls,popup_text_col = 'Hospital')
    df_data = get_all_but_lat_lng(sheet=sheet,path_to_xls=path_to_xls) #encoding="utf-8"
    html_table = str(df_data.to_html())
    html_data = get_table_html_data(html_table)
    return render_template('global_hospitals_neurosurgery.html', iframe=iframe, html_data=html_data)
    

@app.route('/global_hospitals_oncology')
def global_hospitals_oncology():
    sheet = 'NWBestSpecializedOncology'
    iframe = create_map_from_new_xls(sheet=sheet,path_to_xls=path_to_xls,popup_text_col = 'Hospital')
    df_data = get_all_but_lat_lng(sheet=sheet,path_to_xls=path_to_xls) #encoding="utf-8"
    html_table = str(df_data.to_html())
    html_data = get_table_html_data(html_table)
    return render_template('global_hospitals_oncology.html', iframe=iframe, html_data=html_data)
    

@app.route('/global_hospitals_smart')
def global_hospitals_smart():
    sheet = 'Newsweek Best Smart Hospitals'
    iframe = create_map_from_new_xls(sheet=sheet,path_to_xls=path_to_xls,popup_text_col = 'Hospital')
    df_data = get_all_but_lat_lng(sheet=sheet,path_to_xls=path_to_xls) #encoding="utf-8"
    html_table = str(df_data.to_html())
    html_data = get_table_html_data(html_table)
    return render_template('global_hospitals_smart.html', iframe=iframe, html_data=html_data)
    

@app.route('/global_uni_sustain')
def global_uni_sustain():
    sheet = 'QS University Sustainability'
    iframe = create_map_from_new_xls(sheet=sheet,path_to_xls=path_to_xls,popup_text_col = 'University')
    df_data = get_all_but_lat_lng(sheet=sheet,path_to_xls=path_to_xls) #encoding="utf-8"
    html_table = str(df_data.to_html())
    html_data = get_table_html_data(html_table)
    return render_template('global_uni_sustain.html', iframe=iframe, html_data=html_data)
    

@app.route('/africa_hospitals')
def africa_hospitals():
    sheet = 'African Exponent'
    iframe = create_map_from_new_xls(sheet=sheet,path_to_xls=path_to_xls,popup_text_col = 'Hospital')
    df_data = get_all_but_lat_lng(sheet=sheet,path_to_xls=path_to_xls) #encoding="utf-8"
    html_table = str(df_data.to_html())
    html_data = get_table_html_data(html_table)
    return render_template('africa_hospitals.html', iframe=iframe, html_data=html_data)
    

@app.route('/africa_institutes')
def africa_institutes():
    sheet = 'Scimago (Africa)'
    iframe = create_map_from_new_xls(sheet=sheet,path_to_xls=path_to_xls,popup_text_col = 'Institution')
    df_data = get_all_but_lat_lng(sheet=sheet,path_to_xls=path_to_xls) #encoding="utf-8"
    html_table = str(df_data.to_html())
    html_data = get_table_html_data(html_table)
    return render_template('africa_institutes.html', iframe=iframe, html_data=html_data)
    

@app.route('/africa_uni_qs')
def africa_uni_qs():
    sheet = 'QS Ranking (Africa)'
    iframe = create_map_from_new_xls(sheet=sheet,path_to_xls=path_to_xls,popup_text_col = 'University')
    df_data = get_all_but_lat_lng(sheet=sheet,path_to_xls=path_to_xls) #encoding="utf-8"
    html_table = str(df_data.to_html())
    html_data = get_table_html_data(html_table)
    return render_template('africa_uni_qs.html', iframe=iframe, html_data=html_data)
    

@app.route('/africa_uni_the')
def africa_uni_the():
    sheet = 'THE Ranking (Africa) Rank'
    iframe = create_map_from_new_xls(sheet=sheet,path_to_xls=path_to_xls,popup_text_col = 'University')
    df_data = get_all_but_lat_lng(sheet=sheet,path_to_xls=path_to_xls) #encoding="utf-8"
    html_table = str(df_data.to_html())
    html_data = get_table_html_data(html_table)
    return render_template('africa_uni_the.html', iframe=iframe, html_data=html_data)
    

@app.route('/china_hospitals')
def china_hospitals():
    sheet = 'Fudan Ranking'
    iframe = create_map_from_new_xls(sheet=sheet,path_to_xls=path_to_xls,popup_text_col = 'Hospital')
    df_data = get_all_but_lat_lng(sheet=sheet,path_to_xls=path_to_xls) #encoding="utf-8"
    html_table = str(df_data.to_html())
    html_data = get_table_html_data(html_table)
    return render_template('china_hospitals.html', iframe=iframe, html_data=html_data)
    

@app.route('/china_uni')
def china_uni():
    sheet = 'Shanghai Ranking (China)'
    iframe = create_map_from_new_xls(sheet=sheet,path_to_xls=path_to_xls,popup_text_col = 'University')
    df_data = get_all_but_lat_lng(sheet=sheet,path_to_xls=path_to_xls) #encoding="utf-8"
    html_table = str(df_data.to_html())
    html_data = get_table_html_data(html_table)
    return render_template('china_uni.html', iframe=iframe, html_data=html_data)
    

@app.route('/brazil_hospitals')
def brazil_hospitals():
    sheet = 'Newsweek (Brazil)'
    iframe = create_map_from_new_xls(sheet=sheet,path_to_xls=path_to_xls,popup_text_col = 'Hospital')
    df_data = get_all_but_lat_lng(sheet=sheet,path_to_xls=path_to_xls) #encoding="utf-8"
    html_table = str(df_data.to_html())
    html_data = get_table_html_data(html_table)
    return render_template('brazil_hospitals.html', iframe=iframe, html_data=html_data)
    

@app.route('/brazil_uni_the')
def brazil_uni_the():
    sheet = 'THE Ranking (Brazil)'
    iframe = create_map_from_new_xls(sheet=sheet,path_to_xls=path_to_xls,popup_text_col = 'University')
    df_data = get_all_but_lat_lng(sheet=sheet,path_to_xls=path_to_xls) #encoding="utf-8"
    html_table = str(df_data.to_html())
    html_data = get_table_html_data(html_table)
    return render_template('brazil_uni_the.html', iframe=iframe, html_data=html_data)
    

@app.route('/germany_uni_qs')
def germany_uni_qs():
    sheet = 'QS Ranking (Germany)'
    iframe = create_map_from_new_xls(sheet=sheet,path_to_xls=path_to_xls,popup_text_col = 'University')
    df_data = get_all_but_lat_lng(sheet=sheet,path_to_xls=path_to_xls) #encoding="utf-8"
    html_table = str(df_data.to_html())
    html_data = get_table_html_data(html_table)
    return render_template('germany_uni_qs.html', iframe=iframe, html_data=html_data)
    

@app.route('/germany_hospitals')
def germany_hospitals():
    sheet = 'Stern Hospital Ranking'
    iframe = create_map_from_new_xls(sheet=sheet,path_to_xls=path_to_xls,popup_text_col = 'Hospital')
    df_data = get_all_but_lat_lng(sheet=sheet,path_to_xls=path_to_xls) #encoding="utf-8"
    html_table = str(df_data.to_html())
    html_data = get_table_html_data(html_table)
    return render_template('germany_hospitals.html', iframe=iframe, html_data=html_data)
    

@app.route('/usa_uni_qs')
def usa_uni_qs():
    sheet = 'QS Ranking (US)'
    iframe = create_map_from_new_xls(sheet=sheet,path_to_xls=path_to_xls,popup_text_col = 'University')
    df_data = get_all_but_lat_lng(sheet=sheet,path_to_xls=path_to_xls) #encoding="utf-8"
    html_table = str(df_data.to_html())
    html_data = get_table_html_data(html_table)
    return render_template('usa_uni_qs.html', iframe=iframe, html_data=html_data)
    

@app.route('/usa_uni_newsWorld')
def usa_uni_newsWorld():
    sheet = 'USN&WorldReport Universities US'
    iframe = create_map_from_new_xls(sheet=sheet,path_to_xls=path_to_xls,popup_text_col = 'University')
    df_data = get_all_but_lat_lng(sheet=sheet,path_to_xls=path_to_xls) #encoding="utf-8"
    html_table = str(df_data.to_html())
    html_data = get_table_html_data(html_table)
    return render_template('usa_uni_newsWorld.html', iframe=iframe, html_data=html_data)
    

@app.route('/usa_hospitals')
def usa_hospitals():
    sheet = 'U.S. News and World Report'
    iframe = create_map_from_new_xls(sheet=sheet,path_to_xls=path_to_xls,popup_text_col = 'Hospital')
    df_data = get_all_but_lat_lng(sheet=sheet,path_to_xls=path_to_xls) #encoding="utf-8"
    html_table = str(df_data.to_html())
    html_data = get_table_html_data(html_table)
    return render_template('usa_hospitals.html', iframe=iframe, html_data=html_data)
    

@app.route('/hong_kong_institutes')
def hong_kong_institutes():
    sheet = 'Scimago (Hong Kong)'
    iframe = create_map_from_new_xls(sheet=sheet,path_to_xls=path_to_xls,popup_text_col = 'Institution')
    df_data = get_all_but_lat_lng(sheet=sheet,path_to_xls=path_to_xls) #encoding="utf-8"
    html_table = str(df_data.to_html())
    html_data = get_table_html_data(html_table)
    return render_template('hong_kong_institutes.html', iframe=iframe, html_data=html_data)
    

@app.route('/hong_kong_uni_shanghai')
def hong_kong_uni_shanghai():
    sheet = 'Shanghai Ranking (Hong Kong)'
    iframe = create_map_from_new_xls(sheet=sheet,path_to_xls=path_to_xls,popup_text_col = 'University')
    df_data = get_all_but_lat_lng(sheet=sheet,path_to_xls=path_to_xls) #encoding="utf-8"
    html_table = str(df_data.to_html())
    html_data = get_table_html_data(html_table)
    return render_template('hong_kong_uni_shanghai.html', iframe=iframe, html_data=html_data)
    

@app.route('/tiwan_institutes')
def tiwan_institutes():
    sheet = 'Scimago (Taiwan)'
    iframe = create_map_from_new_xls(sheet=sheet,path_to_xls=path_to_xls,popup_text_col = 'Institution')
    df_data = get_all_but_lat_lng(sheet=sheet,path_to_xls=path_to_xls) #encoding="utf-8"
    html_table = str(df_data.to_html())
    html_data = get_table_html_data(html_table)
    return render_template('tiwan_institutes.html', iframe=iframe, html_data=html_data)
    

@app.route('/taiwan_uni_shanghai')
def taiwan_uni_shanghai():
    sheet = 'Shanghai Ranking (Taiwan)'
    iframe = create_map_from_new_xls(sheet=sheet,path_to_xls=path_to_xls,popup_text_col = 'University')
    df_data = get_all_but_lat_lng(sheet=sheet,path_to_xls=path_to_xls) #encoding="utf-8"
    html_table = str(df_data.to_html())
    html_data = get_table_html_data(html_table)
    return render_template('taiwan_uni_shanghai.html', iframe=iframe, html_data=html_data)
    

@app.route('/germany_hospitals_brainTumor')
def germany_hospitals_brainTumor():
    sheet = 'FocusSpecialtyBraintumor'
    iframe = create_map_from_new_xls(sheet=sheet,path_to_xls=path_to_xls,popup_text_col = 'Hospital')
    df_data = get_all_but_lat_lng(sheet=sheet,path_to_xls=path_to_xls) #encoding="utf-8"
    html_table = str(df_data.to_html())
    html_data = get_table_html_data(html_table)
    return render_template('germany_hospitals_brainTumor.html', iframe=iframe, html_data=html_data)
    

@app.route('/germany_hospitals_breastCancer')
def germany_hospitals_breastCancer():
    sheet = 'FocusSpecialtyBreastcancer'
    iframe = create_map_from_new_xls(sheet=sheet,path_to_xls=path_to_xls,popup_text_col = 'Hospital')
    df_data = get_all_but_lat_lng(sheet=sheet,path_to_xls=path_to_xls) #encoding="utf-8"
    html_table = str(df_data.to_html())
    html_data = get_table_html_data(html_table)
    return render_template('germany_hospitals_breastCancer.html', iframe=iframe, html_data=html_data)
    

@app.route('/germany_hospitals_cardiology')
def germany_hospitals_cardiology():
    sheet = 'FocusSpecialtyCardiology'
    iframe = create_map_from_new_xls(sheet=sheet,path_to_xls=path_to_xls,popup_text_col = 'Hospital')
    df_data = get_all_but_lat_lng(sheet=sheet,path_to_xls=path_to_xls) #encoding="utf-8"
    html_table = str(df_data.to_html())
    html_data = get_table_html_data(html_table)
    return render_template('germany_hospitals_cardiology.html', iframe=iframe, html_data=html_data)
    

@app.route('/germany_hospitals_lungTumor')
def germany_hospitals_lungTumor():
    sheet = 'FocusSpecialtyLungTumor'
    iframe = create_map_from_new_xls(sheet=sheet,path_to_xls=path_to_xls,popup_text_col = 'Hospital')
    df_data = get_all_but_lat_lng(sheet=sheet,path_to_xls=path_to_xls) #encoding="utf-8"
    html_table = str(df_data.to_html())
    html_data = get_table_html_data(html_table)
    return render_template('germany_hospitals_lungTumor.html', iframe=iframe, html_data=html_data)
    

@app.route('/germany_hospitals_stroke')
def germany_hospitals_stroke():
    sheet = 'FocusSpecialtyStroke'
    iframe = create_map_from_new_xls(sheet=sheet,path_to_xls=path_to_xls,popup_text_col = 'Hospital')
    df_data = get_all_but_lat_lng(sheet=sheet,path_to_xls=path_to_xls) #encoding="utf-8"
    html_table = str(df_data.to_html())
    html_data = get_table_html_data(html_table)
    return render_template('germany_hospitals_stroke.html', iframe=iframe, html_data=html_data)
    

@app.route('/usa_hospitals_neurologyNeurosurgery')
def usa_hospitals_neurologyNeurosurgery():
    sheet = 'USNEWS NeurologyNeurosurgery'
    iframe = create_map_from_new_xls(sheet=sheet,path_to_xls=path_to_xls,popup_text_col = 'Hospital')
    df_data = get_all_but_lat_lng(sheet=sheet,path_to_xls=path_to_xls) #encoding="utf-8"
    html_table = str(df_data.to_html())
    html_data = get_table_html_data(html_table)
    return render_template('usa_hospitals_neurologyNeurosurgery.html', iframe=iframe, html_data=html_data)
    

@app.route('/usa_hospitals_pulmonologyLungSurgery')
def usa_hospitals_pulmonologyLungSurgery():
    sheet = 'USNEWS PulmonologyLungSurgery'
    iframe = create_map_from_new_xls(sheet=sheet,path_to_xls=path_to_xls,popup_text_col = 'Hospital')
    df_data = get_all_but_lat_lng(sheet=sheet,path_to_xls=path_to_xls) #encoding="utf-8"
    html_table = str(df_data.to_html())
    html_data = get_table_html_data(html_table)
    return render_template('usa_hospitals_pulmonologyLungSurgery.html', iframe=iframe, html_data=html_data)
    

@app.route('/usa_hospitals_cancer')
def usa_hospitals_cancer():
    sheet = 'USNEWS Top Hospitals Cancer'
    iframe = create_map_from_new_xls(sheet=sheet,path_to_xls=path_to_xls,popup_text_col = 'Hospital')
    df_data = get_all_but_lat_lng(sheet=sheet,path_to_xls=path_to_xls) #encoding="utf-8"
    html_table = str(df_data.to_html())
    html_data = get_table_html_data(html_table)
    return render_template('usa_hospitals_cancer.html', iframe=iframe, html_data=html_data)
    

@app.route('/usa_hospitals_cardiology')
def usa_hospitals_cardiology():
    sheet = 'USNEWS Top Hospitals Cardiology'
    iframe = create_map_from_new_xls(sheet=sheet,path_to_xls=path_to_xls,popup_text_col = 'Hospital')
    df_data = get_all_but_lat_lng(sheet=sheet,path_to_xls=path_to_xls) #encoding="utf-8"
    html_table = str(df_data.to_html())
    html_data = get_table_html_data(html_table)
    return render_template('usa_hospitals_cardiology.html', iframe=iframe, html_data=html_data)
    

@app.route('/usa_hospitals_rheumatology')
def usa_hospitals_rheumatology():
    sheet = 'USNEWSTopHospitals Rheumatology'
    iframe = create_map_from_new_xls(sheet=sheet,path_to_xls=path_to_xls,popup_text_col = 'Hospital')
    df_data = get_all_but_lat_lng(sheet=sheet,path_to_xls=path_to_xls) #encoding="utf-8"
    html_table = str(df_data.to_html())
    html_data = get_table_html_data(html_table)
    return render_template('usa_hospitals_rheumatology.html', iframe=iframe, html_data=html_data)
    


if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5000)
    # app.run()

