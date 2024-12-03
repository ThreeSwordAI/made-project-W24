import os
import requests
import zipfile
import pandas as pd
from sqlalchemy import create_engine
from io import BytesIO


data_dir = "../data"
os.makedirs(data_dir, exist_ok=True)

# the datasets I need for the project
datasets = {
    "New Hampshire": "https://stacks.stanford.edu/file/druid:yg821jf8611/yg821jf8611_nh_statewide_2020_04_01.csv.zip",
    "Rhode Island": "https://stacks.stanford.edu/file/druid:yg821jf8611/yg821jf8611_ri_statewide_2020_04_01.csv.zip",
    "Connecticut": "https://stacks.stanford.edu/file/druid:yg821jf8611/yg821jf8611_ct_hartford_2020_04_01.csv.zip",
    "Vermont": "https://stacks.stanford.edu/file/druid:yg821jf8611/yg821jf8611_vt_statewide_2020_04_01.csv.zip",
    "Massachusetts": "https://stacks.stanford.edu/file/druid:yg821jf8611/yg821jf8611_ma_statewide_2020_04_01.csv.zip",
    "Maryland": "https://stacks.stanford.edu/file/druid:yg821jf8611/yg821jf8611_md_statewide_2020_04_01.csv.zip",
    "Virginia": "https://stacks.stanford.edu/file/druid:yg821jf8611/yg821jf8611_va_statewide_2020_04_01.csv.zip"
}
    

# Columns that will I work on
target_columns = [
    'date', 'time', 'zone', 'race', 'sex', 'type', 'arrest_made', 
    'warning_issued', 'outcome', 'contraband_found', 'contraband_drugs', 
    'contraband_weapons', 'contraband_alcohol', 'contraband_other', 
    'frisk_performed', 'search_conducted', 'search_basis', 'reason_for_search', 
    'reason_for_stop', 'vehicle_make', 'vehicle_model', 'state'
]

# Mapping for column renaming. It will slove Issue 2
rename_mapping = {
    'subject_race': 'race',
    'raw_race': 'race',
    'raw_RACE_CDE': 'race',
    'raw_OperatorRace': 'race',
    'raw_subject_race_code': 'race',
    'raw_Race': 'race',
    'raw_driver_race': 'race',
    'subject_sex': 'sex',
    'raw_OperatorSex': 'sex',
    'raw_driver_gender': 'sex',
    'zone': 'zone',
    'department_id': 'zone',
    'district': 'zone',
    'arrest_made': 'arrest_made',
    'raw_Arrest_Made': 'arrest_made',
    'warning_issued': 'warning_issued',
    'outcome': 'outcome',
    'raw_ResultOfStop': 'outcome',
    'raw_Outcome': 'outcome',
    'raw_result_of_contact_description': 'outcome',
    'contraband_found': 'contraband_found',
    'contraband_drugs': 'contraband_drugs',
    'contraband_weapons': 'contraband_weapons',
    'contraband_alcohol': 'contraband_alcohol',
    'contraband_other': 'contraband_other',
    'frisk_performed': 'frisk_performed',
    'search_conducted': 'search_conducted',
    'search_person': 'search_conducted',
    'search_basis': 'search_basis',
    'raw_BasisForStop': 'search_basis',
    'raw_search_authorization_code': 'search_basis',
    'raw_stop_search_description': 'search_basis',
    'reason_for_search': 'reason_for_search',
    'reason_for_stop': 'reason_for_stop',
    'raw_stop_reason_description': 'reason_for_stop',
    'vehicle_make': 'vehicle_make',
    'vehicle_model': 'vehicle_model',
    'state': 'state',
}

dataframes = []

for state, url in datasets.items():
    print(f"Processing {state}...")

    response = requests.get(url)
    if response.status_code == 200:
        with zipfile.ZipFile(BytesIO(response.content)) as zip_ref:
            with zip_ref.open(zip_ref.namelist()[0]) as csv_file:
                df = pd.read_csv(csv_file, low_memory=False)
                df['state'] = state  # Add state name
                df = df.rename(columns=rename_mapping)
                df = df.loc[:, ~df.columns.duplicated()]
                df = df.reindex(columns=target_columns).fillna("000")

                dataframes.append(df)
    else:
        print(f"Failed to download {state} data.")


combined_df = pd.concat(dataframes, ignore_index=True, sort=False)


#csv_output_path = os.path.join(data_dir, 'traffic_data.csv')
#combined_df.to_csv(csv_output_path, index=False)
#print(f"Data has been saved to CSV file at {csv_output_path}.")


sqlite_output_path = os.path.join(data_dir, 'traffic_data_cleaned.sqlite')
engine = create_engine(f"sqlite:///{sqlite_output_path}")


combined_df.to_sql('traffic_data', con=engine, if_exists='replace', index=False)
print(f"Data has been saved to SQLite database at {sqlite_output_path}.")
