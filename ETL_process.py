import pandas as pd
import mysql.connector
import psycopg2


def extract_data():
    #Extract data from MySQL database
    connection = mysql.connector.connect(host='localhost', database='university', user='huyman',password='Man@28081999')
    cursor = connection.cursor()
    sql = '''SELECT * FROM mark_2019
    UNION
    SELECT * FROM mark_2020
    UNION
    SELECT * FROM mark_2021
    UNION
    SELECT * FROM mark_2022;'''
    cursor.execute(sql)
    data = cursor.fetchall()
    extracted_data = pd.DataFrame(data)
    extracted_data.index += 1
    return extracted_data

def transform_data(data):
    #Change column name
    new_col_name = ['year','studentID','mathematics_score','literature_score','foreign_language_score',
    'foreign_language_type','physics_score','chemistry_score','biology_score',
    'history_score','geography_score','civic_education_score']
    data.columns = new_col_name
    #Deduplicate
    data.drop_duplicates(subset=['year','studentID'], keep = 'first')

    #Normalize student code
    student_code = data['studentID'].astype(str)
    data['studentID'] = student_code.str.zfill(8)

    #Update foreign language code
    data['foreign_language_type'] = data['foreign_language_type'].replace(['N1'], 'English score')
    data['foreign_language_type'] = data['foreign_language_type'].replace(['N2'], 'Russian score')
    data['foreign_language_type'] = data['foreign_language_type'].replace(['N3'], 'French score')
    data['foreign_language_type'] = data['foreign_language_type'].replace(['N4'], 'Chinese score')
    data['foreign_language_type'] = data['foreign_language_type'].replace(['N5'], 'German score')
    data['foreign_language_type'] = data['foreign_language_type'].replace(['N6'], 'Japanese score')
    data['foreign_language_type'] = data['foreign_language_type'].replace(['N7'], 'Korean score')
    data['foreign_language_type'] = data['foreign_language_type'].replace([''], 'No information')

    #Create province_id column
    list_provinceID = []
    for p_id in data['studentID']:
        province_ID = p_id[0:2]
        list_provinceID.append(province_ID)
    data.insert(1, column='provinceID', value=list_provinceID)
    return data

def load_data(data):
    data.to_csv('./output/diemthi.csv', index =  True, mode='a')
    pg_conn = psycopg2.connect(database='university',user='huyman',password='1999',host='localhost', port='5432')
    cursor = pg_conn.cursor()
    sql = '''COPY fact_score FROM './output/diemthi.csv' DELIMITER ',' CSV HEADER;'''
    cursor.execute(sql)
    pg_conn.commit()
    cursor.close()

extract = extract_data()
tranform = transform_data(extract)
load = load_data(tranform)