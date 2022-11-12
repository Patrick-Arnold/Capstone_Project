# -- Imports --
import pandas as pd
import numpy as np

# Import and clean data
def import_and_clean_data(filepath):
    
    # Import dataframe
    df = pd.read_csv(filepath)
    
    # Mark columns for removal
    remove = ['dob_yy', 'f_facility', 'bfacil3', 'mage_impflg', 'mage_repflg', 'mager14', 'mager9', 'mrace31', 'mrace6', 'mrace15',
           'mraceimp', 'mhispx', 'f_mhisp', 'mracehisp', 'mar_p', 'mar_imp', 'f_mar_p', 'f_meduc', 'fagerpt_flg', 'fagerec11',
           'frace31', 'frace15', 'fhispx', 'f_fhisp', 'lbo_rec', 'tbo_rec', 'illb_r', 'illb_r11', 'ilop_r',
           'ilop_r11', 'ilp_r11', 'f_mpcb', 'precare5', 'previs_rec', 'f_tpcv', 'f_wic', 'cig0_r', 'cig1_r', 'cig2_r',
           'cig3_r', 'f_cigs_0', 'f_cigs_1', 'f_cigs_2', 'f_cigs_3', 'cig_rec', 'f_tobaco', 'f_m_ht', 'bmi_r', 'pwgt_r',
           'f_pwgt', 'f_dwgt', 'wtgain_rec', 'f_wtgain', 'f_rf_pdiab', 'f_rf_gdiab', 'f_rf_phyper', 'f_rf_ghyper', 
           'f_rf_eclamp', 'f_rf_ppb', 'f_rf_inf_drg', 'f_rf_inf_art', 'rf_cesar', 'f_rf_cesar', 'f_rf_ncesar',
           'no_risks', 'f_ip_gonor', 'f_ip_syph', 'f_ip_chlam', 'f_ip_hepatb', 'f_ip_hepatc', 'no_infec', 'ob_ecvs', 'ob_ecvf',
           'f_ob_succ', 'f_ob_fail', 'ld_indl', 'ld_augm', 'ld_anes', 'f_ld_indl', 'f_ld_augm', 'f_ld_ster', 'f_ld_antb',
           'f_ld_chor', 'f_ld_anes', 'no_lbrdlv', 'me_pres', 'me_rout', 'me_trial', 'f_me_pres', 'f_me_rout', 'f_me_trial',
           'rdmeth_rec', 'dmeth_rec', 'f_dmeth_rec', 'mm_mtr', 'mm_plac', 'mm_rupt', 'mm_uhyst', 'mm_aicu', 'f_mm_mtr',
           'f_mm_rupt', 'f_mm_uhyst', 'f_mm_aicu', 'no_mmorb', 'mtran', 'pay', 'f_pay', 'f_pay_rec', 'apgar5r',
           'f_apgar5', 'apgar10', 'apgar10r', 'imp_plur', 'setorder_r', 'imp_sex', 'dlmp_mm', 'dlmp_yy', 'compgst_imp',
           'obgest_flg', 'gestrec10', 'gestrec3', 'lmpused', 'oegest_comb', 'oegest_r10', 'dbwt', 'bwtr12', 'bwtr4',
           'ab_aven1', 'ab_aven6', 'ab_nicu', 'ab_surf', 'ab_anti', 'ab_seiz', 'f_ab_vent', 'f_ab_vent6',
           'f_ab_surfac', 'f_ab_antibio', 'f_ab_seiz', 'no_abnorm', 'ca_anen', 'ca_mnsb', 'ca_cchd', 'ca_cdh', 'ca_omph', 
           'ca_gast', 'f_ca_anen', 'f_ca_menin', 'f_ca_heart', 'f_ca_hernia', 'f_ca_ompha', 'f_ca_gastro', 'ca_limb',
           'ca_cleft', 'ca_clpal', 'ca_disor', 'ca_hypo', 'f_ca_limb', 'f_ca_cleftlp', 'f_ca_cleft', 'f_ca_downs', 
           'f_ca_chrom', 'f_ca_hypos', 'no_congen', 'itran', 'ilive', 'bfed', 'f_bfed', 'f_mm_', 'f_ab_nicu', 'fracehisp',
           'oegest_r3', 'dob_mm', 'dob_tt', 'dob_wk', 'restatus', 'frace6', 'fhisp_r', 'feduc', 'ilp_r', 'attend', 'pay_rec']
    
    # Remove marked columns
    df.drop(remove, axis=1, inplace=True)

    # Renaming columns for interpretability
    rename = ['birth_place', 'mother_age', 'mother_native',
          'mother_race', 'mother_hispanic', 'marital_status', 'mother_education', 'father_age',
          'living_children', 'deceased_children', 'terminations', 
          'months_prenatal_care', 'prenatal_visits', 'food_assistance', 'prepregnancy_daily_cig',
          'first_tri_daily_cig', 'second_tri_daily_cig', 'third_tri_daily_cig', 'height', 'bmi', 'delivery_weight',
          'weight_gain', 'diabetes', 'gestational_diabetes', 'hypertension', 'gestational_hypertension', 'eclampsia',
          'previous_premature_birth', 'infertility_treatment', 'fertility_drugs', 'assisted_reproduction',
          'previous_cesareans', 'gonorrhea', 'syphilis', 'chlamydia', 'hepatitis_b', 'hepatitis_c', 'steroids', 'antibiotics',
          'chorioamnionitis', 'apgar_score', 'plural_pregnancy', 'infant_sex', 'weeks_gestation',
          'down_syndrome']
    
    df.columns = rename
    
    # Homogenize missing value identifiers by converting to NaN
    # Bin variables that are difficult to interpret
    df['birth_place'].replace(to_replace=list(range(2, 8)), value="other", inplace=True)
    df['birth_place'].replace(to_replace=1, value="hospital", inplace=True)
    df['birth_place'].replace(to_replace=9, value=np.nan, inplace=True)
    
    df['mother_native'].replace(to_replace=1, value='Y', inplace=True)
    df['mother_native'].replace(to_replace=2, value='N', inplace=True)
    df['mother_native'].replace(to_replace=3, value=np.nan, inplace=True)
    
    df['mother_race'].replace({1: 'white', 2: 'black', 3: 'native_american', 4: 'asian/pi'}, inplace=True)
    
    df['mother_hispanic'].replace(to_replace=0, value='N', inplace=True)
    df['mother_hispanic'].replace(to_replace=list(range(1, 6)), value='Y', inplace=True)
    df['mother_hispanic'].replace(to_replace=9, value=np.nan, inplace=True)
    
    df['marital_status'].replace({1: 'married', 2: 'unmarried'}, inplace=True)
    
    df['mother_education'].replace(to_replace=list(range(1, 6)), value="hs_or_lower", inplace=True)
    df['mother_education'].replace(to_replace=list(range(6, 9)), value="college_or_higher", inplace=True)
    df['mother_education'].replace(to_replace=9, value=np.nan, inplace=True)
    
    df['father_age'].replace(to_replace=99, value=np.nan, inplace=True)
    
    df['living_children'].replace(to_replace=99, value=np.nan, inplace=True)
    
    df['deceased_children'].replace(to_replace=99, value=np.nan, inplace=True)
    
    df['terminations'].replace(to_replace=99, value=np.nan, inplace=True)
    
    df['months_prenatal_care'].replace(to_replace=99, value=np.nan, inplace=True)
    
    df['prenatal_visits'].replace(to_replace=99, value=np.nan, inplace=True)
    
    df['food_assistance'].replace(to_replace='U', value=np.nan, inplace=True)
    
    df['prepregnancy_daily_cig'].replace(to_replace=99, value=np.nan, inplace=True)
    
    df['first_tri_daily_cig'].replace(to_replace=99, value=np.nan, inplace=True)
    
    df['second_tri_daily_cig'].replace(to_replace=99, value=np.nan, inplace=True)
    
    df['third_tri_daily_cig'].replace(to_replace=99, value=np.nan, inplace=True)
    
    df['height'].replace(to_replace=99, value=np.nan, inplace=True)
    
    df['bmi'].replace(to_replace=99, value=np.nan, inplace=True)
    
    df['delivery_weight'].replace(to_replace=999, value=np.nan, inplace=True)
    
    df['weight_gain'].replace(to_replace=99, value=np.nan, inplace=True)
    
    df['diabetes'].replace(to_replace='U', value=np.nan, inplace=True)
    
    df['gestational_diabetes'].replace(to_replace='U', value=np.nan, inplace=True)
    
    df['hypertension'].replace(to_replace='U', value=np.nan, inplace=True)
    
    df['gestational_hypertension'].replace(to_replace='U', value=np.nan, inplace=True)
    
    df['eclampsia'].replace(to_replace='U', value=np.nan, inplace=True)
    
    df['previous_premature_birth'].replace(to_replace='U', value=np.nan, inplace=True)
    
    df['infertility_treatment'].replace(to_replace='U', value=np.nan, inplace=True)
    
    df['fertility_drugs'].replace(to_replace='U', value=np.nan, inplace=True)
    df['fertility_drugs'].replace(to_replace='X', value='N', inplace=True)
    
    df['assisted_reproduction'].replace(to_replace='U', value=np.nan, inplace=True)
    df['assisted_reproduction'].replace(to_replace='X', value='N', inplace=True)
    
    df['previous_cesareans'].replace(to_replace=99, value=np.nan, inplace=True)
    
    df['gonorrhea'].replace(to_replace='U', value=np.nan, inplace=True)
    
    df['syphilis'].replace(to_replace='U', value=np.nan, inplace=True)
    
    df['chlamydia'].replace(to_replace='U', value=np.nan, inplace=True)
    
    df['hepatitis_b'].replace(to_replace='U', value=np.nan, inplace=True)
    
    df['hepatitis_c'].replace(to_replace='U', value=np.nan, inplace=True)
    
    df['steroids'].replace(to_replace='U', value=np.nan, inplace=True)
    
    df['antibiotics'].replace(to_replace='U', value=np.nan, inplace=True)
    
    df['chorioamnionitis'].replace(to_replace='U', value=np.nan, inplace=True)
    
    df['weeks_gestation'].replace(to_replace=99, value=np.nan, inplace=True)
    
    df['down_syndrome'].replace(to_replace='U', value=np.nan, inplace=True)
    df['down_syndrome'].replace(to_replace='P', value='C', inplace=True)
    
    return df