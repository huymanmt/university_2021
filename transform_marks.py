import pandas as pd

df = pd.read_csv('output/diemthi.csv')
df['Toan'] = df['Toan'].fillna(0)
df['Van'] = df['Van'].fillna(0)
df['Ngoai_ngu'] = df['Ngoai_ngu'].fillna(0)
df['Ma_ngoai_ngu'] = df['Ma_ngoai_ngu'].fillna('Vang thi')
df['Ma_ngoai_ngu'] = df['Ma_ngoai_ngu'].replace(['N1'], 'Tieng Anh')
df['Ma_ngoai_ngu'] = df['Ma_ngoai_ngu'].replace(['N2'], 'Tieng Nga')
df['Ma_ngoai_ngu'] = df['Ma_ngoai_ngu'].replace(['N3'], 'Tieng Phap')
df['Ma_ngoai_ngu'] = df['Ma_ngoai_ngu'].replace(['N4'], 'Tieng Nhat')
df['Ma_ngoai_ngu'] = df['Ma_ngoai_ngu'].replace(['N5'], 'Tieng Duc')
df['Ma_ngoai_ngu'] = df['Ma_ngoai_ngu'].replace(['N6'], 'Tieng Nhat')
df['Ma_ngoai_ngu'] = df['Ma_ngoai_ngu'].replace(['N7'], 'Tieng Han')

df.to_csv('output/diemthi_transform.csv', index=False)
