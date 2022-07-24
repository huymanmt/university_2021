def get_student_mark(data_mark):
    studentCode = data_mark['studentCode']
    tinh = data_mark['groupName']
    toan = data_mark['TOAN']
    van = data_mark['VAN']
    ngoaingu = data_mark['NGOAINGU']
    code_ngoaingu = data_mark['CODE_NGOAINGU']
    ly = data_mark['LY']
    hoa = data_mark['HOA']
    sinh = data_mark['SINH']
    su = data_mark['SU']
    dia = data_mark['DIA']
    gdcd = data_mark['GDCD']
    diemthi_obj = [{
            'So bao danh': studentCode,
            'Tinh': tinh,
            'Toan': toan,
            'Van': van,
            'Ngoai ngu': ngoaingu,
            'Ma ngoai ngu': code_ngoaingu,
            'Ly': ly,
            'Hoa': hoa,
            'Sinh': sinh,
            'Su': su,
            'Dia': dia,
            'GDCD': gdcd
        }]
    return diemthi_obj

def get_mark_2022(data_mark):
    studentCode = data_mark['SOBAODANH']
    toan = data_mark['TOAN']
    van = data_mark['VAN']
    ngoaingu = data_mark['NGOAI_NGU']
    code_ngoaingu = data_mark['MA_MON_NGOAI_NGU']
    ly = data_mark['LY']
    hoa = data_mark['HOA']
    sinh = data_mark['SINH']
    su = data_mark['SU']
    dia = data_mark['DIA']
    gdcd = data_mark['GIAO_DUC_CONG_DAN']
    diemthi_obj = [{
            'Sbd': studentCode,
            'Toan': toan,
            'Van': van,
            'Ngoaingu': ngoaingu,
            'Ma_ngoai_ngu': code_ngoaingu,
            'Ly': ly,
            'Hoa': hoa,
            'Sinh': sinh,
            'Su': su,
            'Dia': dia,
            'GDCD': gdcd
        }]
    return diemthi_obj