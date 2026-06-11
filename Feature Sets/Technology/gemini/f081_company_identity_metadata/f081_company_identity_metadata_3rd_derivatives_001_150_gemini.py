import numpy as np
import pandas as pd
from technology_helpers import _to_num, _clean, _safe_div, _log, _mean, _std, _sum, _min, _max, _z, _pct_change, _diff, _rank, _skew, _kurt, _autocorr, _corr, _slope, _ewm, _event_flag, _event_count, _event_rate, _clip_z

def cg_f081_company_identity_metadata_core00_3rd_v001_signal(ticker, name, exchange, category, siccode, scalemarketcap):
    return _clean(_diff(_diff(_to_num(siccode), 4), 4))
def cg_f081_company_identity_metadata_core01_3rd_v002_signal(ticker, name, exchange, category, siccode, scalemarketcap):
    return _clean(_diff(_diff(_to_num(scalemarketcap), 4), 4))
def cg_f081_company_identity_metadata_core02_3rd_v003_signal(ticker, name, exchange, category, siccode, scalemarketcap):
    return _clean(_diff(_diff(_event_flag(ticker), 4), 4))
def cg_f081_company_identity_metadata_core03_3rd_v004_signal(ticker, name, exchange, category, siccode, scalemarketcap):
    return _clean(_diff(_diff(_event_flag(exchange), 4), 4))
def cg_f081_company_identity_metadata_core04_3rd_v005_signal(ticker, name, exchange, category, siccode, scalemarketcap):
    return _clean(_diff(_diff(_event_flag(category), 4), 4))
def cg_f081_company_identity_metadata_core05_3rd_v006_signal(ticker, name, exchange, category, siccode, scalemarketcap):
    return _clean(_diff(_diff(_event_count(ticker, 4), 4), 4))
def cg_f081_company_identity_metadata_core06_3rd_v007_signal(ticker, name, exchange, category, siccode, scalemarketcap):
    return _clean(_diff(_diff(_event_rate(ticker, 8), 4), 4))
def cg_f081_company_identity_metadata_core07_3rd_v008_signal(ticker, name, exchange, category, siccode, scalemarketcap):
    return _clean(_diff(_diff(_to_num(exchange == 'NASDAQ'), 4), 4))
def cg_f081_company_identity_metadata_core08_3rd_v009_signal(ticker, name, exchange, category, siccode, scalemarketcap):
    return _clean(_diff(_diff(_to_num(category == 'Domestic'), 4), 4))
def cg_f081_company_identity_metadata_core09_3rd_v010_signal(ticker, name, exchange, category, siccode, scalemarketcap):
    return _clean(_diff(_diff(_to_num(siccode) / 1000.0, 4), 4))
def cg_f081_company_identity_metadata_core10_3rd_v011_signal(ticker, name, exchange, category, siccode, scalemarketcap):
    return _clean(_slope(_diff(_to_num(siccode), 4), 8))
def cg_f081_company_identity_metadata_core11_3rd_v012_signal(ticker, name, exchange, category, siccode, scalemarketcap):
    return _clean(_slope(_diff(_to_num(scalemarketcap), 4), 8))
def cg_f081_company_identity_metadata_core12_3rd_v013_signal(ticker, name, exchange, category, siccode, scalemarketcap):
    return _clean(_slope(_diff(_event_flag(ticker), 4), 8))
def cg_f081_company_identity_metadata_core13_3rd_v014_signal(ticker, name, exchange, category, siccode, scalemarketcap):
    return _clean(_slope(_diff(_event_flag(exchange), 4), 8))
def cg_f081_company_identity_metadata_core14_3rd_v015_signal(ticker, name, exchange, category, siccode, scalemarketcap):
    return _clean(_slope(_diff(_event_flag(category), 4), 8))
def cg_f081_company_identity_metadata_core15_3rd_v016_signal(ticker, name, exchange, category, siccode, scalemarketcap):
    return _clean(_slope(_diff(_event_count(ticker, 4), 4), 8))
def cg_f081_company_identity_metadata_core16_3rd_v017_signal(ticker, name, exchange, category, siccode, scalemarketcap):
    return _clean(_slope(_diff(_event_rate(ticker, 8), 4), 8))
def cg_f081_company_identity_metadata_core17_3rd_v018_signal(ticker, name, exchange, category, siccode, scalemarketcap):
    return _clean(_slope(_diff(_to_num(exchange == 'NASDAQ'), 4), 8))
def cg_f081_company_identity_metadata_core18_3rd_v019_signal(ticker, name, exchange, category, siccode, scalemarketcap):
    return _clean(_slope(_diff(_to_num(category == 'Domestic'), 4), 8))
def cg_f081_company_identity_metadata_core19_3rd_v020_signal(ticker, name, exchange, category, siccode, scalemarketcap):
    return _clean(_slope(_diff(_to_num(siccode) / 1000.0, 4), 8))
def cg_f081_company_identity_metadata_core20_3rd_v021_signal(ticker, name, exchange, category, siccode, scalemarketcap):
    return _clean(_diff(_slope(_to_num(siccode), 4), 4))
def cg_f081_company_identity_metadata_core21_3rd_v022_signal(ticker, name, exchange, category, siccode, scalemarketcap):
    return _clean(_diff(_slope(_to_num(scalemarketcap), 4), 4))
def cg_f081_company_identity_metadata_core22_3rd_v023_signal(ticker, name, exchange, category, siccode, scalemarketcap):
    return _clean(_diff(_slope(_event_flag(ticker), 4), 4))
def cg_f081_company_identity_metadata_core23_3rd_v024_signal(ticker, name, exchange, category, siccode, scalemarketcap):
    return _clean(_diff(_slope(_event_flag(exchange), 4), 4))
def cg_f081_company_identity_metadata_core24_3rd_v025_signal(ticker, name, exchange, category, siccode, scalemarketcap):
    return _clean(_diff(_slope(_event_flag(category), 4), 4))
def cg_f081_company_identity_metadata_core25_3rd_v026_signal(ticker, name, exchange, category, siccode, scalemarketcap):
    return _clean(_diff(_slope(_event_count(ticker, 4), 4), 4))
def cg_f081_company_identity_metadata_core26_3rd_v027_signal(ticker, name, exchange, category, siccode, scalemarketcap):
    return _clean(_diff(_slope(_event_rate(ticker, 8), 4), 4))
def cg_f081_company_identity_metadata_core27_3rd_v028_signal(ticker, name, exchange, category, siccode, scalemarketcap):
    return _clean(_diff(_slope(_to_num(exchange == 'NASDAQ'), 4), 4))
def cg_f081_company_identity_metadata_core28_3rd_v029_signal(ticker, name, exchange, category, siccode, scalemarketcap):
    return _clean(_diff(_slope(_to_num(category == 'Domestic'), 4), 4))
def cg_f081_company_identity_metadata_core29_3rd_v030_signal(ticker, name, exchange, category, siccode, scalemarketcap):
    return _clean(_diff(_slope(_to_num(siccode) / 1000.0, 4), 4))
def cg_f081_company_identity_metadata_core30_3rd_v031_signal(ticker, name, exchange, category, siccode, scalemarketcap):
    return _clean(_z(_diff(_diff(_to_num(siccode), 4), 4), 8))
def cg_f081_company_identity_metadata_core31_3rd_v032_signal(ticker, name, exchange, category, siccode, scalemarketcap):
    return _clean(_z(_diff(_diff(_to_num(scalemarketcap), 4), 4), 8))
def cg_f081_company_identity_metadata_core32_3rd_v033_signal(ticker, name, exchange, category, siccode, scalemarketcap):
    return _clean(_z(_diff(_diff(_event_flag(ticker), 4), 4), 8))
def cg_f081_company_identity_metadata_core33_3rd_v034_signal(ticker, name, exchange, category, siccode, scalemarketcap):
    return _clean(_z(_diff(_diff(_event_flag(exchange), 4), 4), 8))
def cg_f081_company_identity_metadata_core34_3rd_v035_signal(ticker, name, exchange, category, siccode, scalemarketcap):
    return _clean(_z(_diff(_diff(_event_flag(category), 4), 4), 8))
def cg_f081_company_identity_metadata_core35_3rd_v036_signal(ticker, name, exchange, category, siccode, scalemarketcap):
    return _clean(_z(_diff(_diff(_event_count(ticker, 4), 4), 4), 8))
def cg_f081_company_identity_metadata_core36_3rd_v037_signal(ticker, name, exchange, category, siccode, scalemarketcap):
    return _clean(_z(_diff(_diff(_event_rate(ticker, 8), 4), 4), 8))
def cg_f081_company_identity_metadata_core37_3rd_v038_signal(ticker, name, exchange, category, siccode, scalemarketcap):
    return _clean(_z(_diff(_diff(_to_num(exchange == 'NASDAQ'), 4), 4), 8))
def cg_f081_company_identity_metadata_core38_3rd_v039_signal(ticker, name, exchange, category, siccode, scalemarketcap):
    return _clean(_z(_diff(_diff(_to_num(category == 'Domestic'), 4), 4), 8))
def cg_f081_company_identity_metadata_core39_3rd_v040_signal(ticker, name, exchange, category, siccode, scalemarketcap):
    return _clean(_z(_diff(_diff(_to_num(siccode) / 1000.0, 4), 4), 8))
def cg_f081_company_identity_metadata_core40_3rd_v041_signal(ticker, name, exchange, category, siccode, scalemarketcap):
    return _clean(_z(_slope(_diff(_to_num(siccode), 4), 8), 12))
def cg_f081_company_identity_metadata_core41_3rd_v042_signal(ticker, name, exchange, category, siccode, scalemarketcap):
    return _clean(_z(_slope(_diff(_to_num(scalemarketcap), 4), 8), 12))
def cg_f081_company_identity_metadata_core42_3rd_v043_signal(ticker, name, exchange, category, siccode, scalemarketcap):
    return _clean(_z(_slope(_diff(_event_flag(ticker), 4), 8), 12))
def cg_f081_company_identity_metadata_core43_3rd_v044_signal(ticker, name, exchange, category, siccode, scalemarketcap):
    return _clean(_z(_slope(_diff(_event_flag(exchange), 4), 8), 12))
def cg_f081_company_identity_metadata_core44_3rd_v045_signal(ticker, name, exchange, category, siccode, scalemarketcap):
    return _clean(_z(_slope(_diff(_event_flag(category), 4), 8), 12))
def cg_f081_company_identity_metadata_core45_3rd_v046_signal(ticker, name, exchange, category, siccode, scalemarketcap):
    return _clean(_z(_slope(_diff(_event_count(ticker, 4), 4), 8), 12))
def cg_f081_company_identity_metadata_core46_3rd_v047_signal(ticker, name, exchange, category, siccode, scalemarketcap):
    return _clean(_z(_slope(_diff(_event_rate(ticker, 8), 4), 8), 12))
def cg_f081_company_identity_metadata_core47_3rd_v048_signal(ticker, name, exchange, category, siccode, scalemarketcap):
    return _clean(_z(_slope(_diff(_to_num(exchange == 'NASDAQ'), 4), 8), 12))
def cg_f081_company_identity_metadata_core48_3rd_v049_signal(ticker, name, exchange, category, siccode, scalemarketcap):
    return _clean(_z(_slope(_diff(_to_num(category == 'Domestic'), 4), 8), 12))
def cg_f081_company_identity_metadata_core49_3rd_v050_signal(ticker, name, exchange, category, siccode, scalemarketcap):
    return _clean(_z(_slope(_diff(_to_num(siccode) / 1000.0, 4), 8), 12))
def cg_f081_company_identity_metadata_core50_3rd_v051_signal(ticker, name, exchange, category, siccode, scalemarketcap):
    return _clean(_z(_diff(_slope(_to_num(siccode), 4), 4), 8))
def cg_f081_company_identity_metadata_core51_3rd_v052_signal(ticker, name, exchange, category, siccode, scalemarketcap):
    return _clean(_z(_diff(_slope(_to_num(scalemarketcap), 4), 4), 8))
def cg_f081_company_identity_metadata_core52_3rd_v053_signal(ticker, name, exchange, category, siccode, scalemarketcap):
    return _clean(_z(_diff(_slope(_event_flag(ticker), 4), 4), 8))
def cg_f081_company_identity_metadata_core53_3rd_v054_signal(ticker, name, exchange, category, siccode, scalemarketcap):
    return _clean(_z(_diff(_slope(_event_flag(exchange), 4), 4), 8))
def cg_f081_company_identity_metadata_core54_3rd_v055_signal(ticker, name, exchange, category, siccode, scalemarketcap):
    return _clean(_z(_diff(_slope(_event_flag(category), 4), 4), 8))
def cg_f081_company_identity_metadata_core55_3rd_v056_signal(ticker, name, exchange, category, siccode, scalemarketcap):
    return _clean(_z(_diff(_slope(_event_count(ticker, 4), 4), 4), 8))
def cg_f081_company_identity_metadata_core56_3rd_v057_signal(ticker, name, exchange, category, siccode, scalemarketcap):
    return _clean(_z(_diff(_slope(_event_rate(ticker, 8), 4), 4), 8))
def cg_f081_company_identity_metadata_core57_3rd_v058_signal(ticker, name, exchange, category, siccode, scalemarketcap):
    return _clean(_z(_diff(_slope(_to_num(exchange == 'NASDAQ'), 4), 4), 8))
def cg_f081_company_identity_metadata_core58_3rd_v059_signal(ticker, name, exchange, category, siccode, scalemarketcap):
    return _clean(_z(_diff(_slope(_to_num(category == 'Domestic'), 4), 4), 8))
def cg_f081_company_identity_metadata_core59_3rd_v060_signal(ticker, name, exchange, category, siccode, scalemarketcap):
    return _clean(_z(_diff(_slope(_to_num(siccode) / 1000.0, 4), 4), 8))
def cg_f081_company_identity_metadata_core60_3rd_v061_signal(ticker, name, exchange, category, siccode, scalemarketcap):
    return _clean(_rank(_diff(_diff(_to_num(siccode), 4), 4), 12))
def cg_f081_company_identity_metadata_core61_3rd_v062_signal(ticker, name, exchange, category, siccode, scalemarketcap):
    return _clean(_rank(_diff(_diff(_to_num(scalemarketcap), 4), 4), 12))
def cg_f081_company_identity_metadata_core62_3rd_v063_signal(ticker, name, exchange, category, siccode, scalemarketcap):
    return _clean(_rank(_diff(_diff(_event_flag(ticker), 4), 4), 12))
def cg_f081_company_identity_metadata_core63_3rd_v064_signal(ticker, name, exchange, category, siccode, scalemarketcap):
    return _clean(_rank(_diff(_diff(_event_flag(exchange), 4), 4), 12))
def cg_f081_company_identity_metadata_core64_3rd_v065_signal(ticker, name, exchange, category, siccode, scalemarketcap):
    return _clean(_rank(_diff(_diff(_event_flag(category), 4), 4), 12))
def cg_f081_company_identity_metadata_core65_3rd_v066_signal(ticker, name, exchange, category, siccode, scalemarketcap):
    return _clean(_rank(_diff(_diff(_event_count(ticker, 4), 4), 4), 12))
def cg_f081_company_identity_metadata_core66_3rd_v067_signal(ticker, name, exchange, category, siccode, scalemarketcap):
    return _clean(_rank(_diff(_diff(_event_rate(ticker, 8), 4), 4), 12))
def cg_f081_company_identity_metadata_core67_3rd_v068_signal(ticker, name, exchange, category, siccode, scalemarketcap):
    return _clean(_rank(_diff(_diff(_to_num(exchange == 'NASDAQ'), 4), 4), 12))
def cg_f081_company_identity_metadata_core68_3rd_v069_signal(ticker, name, exchange, category, siccode, scalemarketcap):
    return _clean(_rank(_diff(_diff(_to_num(category == 'Domestic'), 4), 4), 12))
def cg_f081_company_identity_metadata_core69_3rd_v070_signal(ticker, name, exchange, category, siccode, scalemarketcap):
    return _clean(_rank(_diff(_diff(_to_num(siccode) / 1000.0, 4), 4), 12))
def cg_f081_company_identity_metadata_core70_3rd_v071_signal(ticker, name, exchange, category, siccode, scalemarketcap):
    return _clean(_rank(_slope(_diff(_to_num(siccode), 4), 8), 12))
def cg_f081_company_identity_metadata_core71_3rd_v072_signal(ticker, name, exchange, category, siccode, scalemarketcap):
    return _clean(_rank(_slope(_diff(_to_num(scalemarketcap), 4), 8), 12))
def cg_f081_company_identity_metadata_core72_3rd_v073_signal(ticker, name, exchange, category, siccode, scalemarketcap):
    return _clean(_rank(_slope(_diff(_event_flag(ticker), 4), 8), 12))
def cg_f081_company_identity_metadata_core73_3rd_v074_signal(ticker, name, exchange, category, siccode, scalemarketcap):
    return _clean(_rank(_slope(_diff(_event_flag(exchange), 4), 8), 12))
def cg_f081_company_identity_metadata_core74_3rd_v075_signal(ticker, name, exchange, category, siccode, scalemarketcap):
    return _clean(_rank(_slope(_diff(_event_flag(category), 4), 8), 12))
def cg_f081_company_identity_metadata_core75_3rd_v076_signal(ticker, name, exchange, category, siccode, scalemarketcap):
    return _clean(_rank(_slope(_diff(_event_count(ticker, 4), 4), 8), 12))
def cg_f081_company_identity_metadata_core76_3rd_v077_signal(ticker, name, exchange, category, siccode, scalemarketcap):
    return _clean(_rank(_slope(_diff(_event_rate(ticker, 8), 4), 8), 12))
def cg_f081_company_identity_metadata_core77_3rd_v078_signal(ticker, name, exchange, category, siccode, scalemarketcap):
    return _clean(_rank(_slope(_diff(_to_num(exchange == 'NASDAQ'), 4), 8), 12))
def cg_f081_company_identity_metadata_core78_3rd_v079_signal(ticker, name, exchange, category, siccode, scalemarketcap):
    return _clean(_rank(_slope(_diff(_to_num(category == 'Domestic'), 4), 8), 12))
def cg_f081_company_identity_metadata_core79_3rd_v080_signal(ticker, name, exchange, category, siccode, scalemarketcap):
    return _clean(_rank(_slope(_diff(_to_num(siccode) / 1000.0, 4), 8), 12))
def cg_f081_company_identity_metadata_core80_3rd_v081_signal(ticker, name, exchange, category, siccode, scalemarketcap):
    return _clean(_rank(_diff(_slope(_to_num(siccode), 4), 4), 12))
def cg_f081_company_identity_metadata_core81_3rd_v082_signal(ticker, name, exchange, category, siccode, scalemarketcap):
    return _clean(_rank(_diff(_slope(_to_num(scalemarketcap), 4), 4), 12))
def cg_f081_company_identity_metadata_core82_3rd_v083_signal(ticker, name, exchange, category, siccode, scalemarketcap):
    return _clean(_rank(_diff(_slope(_event_flag(ticker), 4), 4), 12))
def cg_f081_company_identity_metadata_core83_3rd_v084_signal(ticker, name, exchange, category, siccode, scalemarketcap):
    return _clean(_rank(_diff(_slope(_event_flag(exchange), 4), 4), 12))
def cg_f081_company_identity_metadata_core84_3rd_v085_signal(ticker, name, exchange, category, siccode, scalemarketcap):
    return _clean(_rank(_diff(_slope(_event_flag(category), 4), 4), 12))
def cg_f081_company_identity_metadata_core85_3rd_v086_signal(ticker, name, exchange, category, siccode, scalemarketcap):
    return _clean(_rank(_diff(_slope(_event_count(ticker, 4), 4), 4), 12))
def cg_f081_company_identity_metadata_core86_3rd_v087_signal(ticker, name, exchange, category, siccode, scalemarketcap):
    return _clean(_rank(_diff(_slope(_event_rate(ticker, 8), 4), 4), 12))
def cg_f081_company_identity_metadata_core87_3rd_v088_signal(ticker, name, exchange, category, siccode, scalemarketcap):
    return _clean(_rank(_diff(_slope(_to_num(exchange == 'NASDAQ'), 4), 4), 12))
def cg_f081_company_identity_metadata_core88_3rd_v089_signal(ticker, name, exchange, category, siccode, scalemarketcap):
    return _clean(_rank(_diff(_slope(_to_num(category == 'Domestic'), 4), 4), 12))
def cg_f081_company_identity_metadata_core89_3rd_v090_signal(ticker, name, exchange, category, siccode, scalemarketcap):
    return _clean(_rank(_diff(_slope(_to_num(siccode) / 1000.0, 4), 4), 12))
def cg_f081_company_identity_metadata_core90_3rd_v091_signal(ticker, name, exchange, category, siccode, scalemarketcap):
    return _clean(_mean(_diff(_diff(_to_num(siccode), 4), 4), 4))
def cg_f081_company_identity_metadata_core91_3rd_v092_signal(ticker, name, exchange, category, siccode, scalemarketcap):
    return _clean(_mean(_diff(_diff(_to_num(scalemarketcap), 4), 4), 4))
def cg_f081_company_identity_metadata_core92_3rd_v093_signal(ticker, name, exchange, category, siccode, scalemarketcap):
    return _clean(_mean(_diff(_diff(_event_flag(ticker), 4), 4), 4))
def cg_f081_company_identity_metadata_core93_3rd_v094_signal(ticker, name, exchange, category, siccode, scalemarketcap):
    return _clean(_mean(_diff(_diff(_event_flag(exchange), 4), 4), 4))
def cg_f081_company_identity_metadata_core94_3rd_v095_signal(ticker, name, exchange, category, siccode, scalemarketcap):
    return _clean(_mean(_diff(_diff(_event_flag(category), 4), 4), 4))
def cg_f081_company_identity_metadata_core95_3rd_v096_signal(ticker, name, exchange, category, siccode, scalemarketcap):
    return _clean(_mean(_diff(_diff(_event_count(ticker, 4), 4), 4), 4))
def cg_f081_company_identity_metadata_core96_3rd_v097_signal(ticker, name, exchange, category, siccode, scalemarketcap):
    return _clean(_mean(_diff(_diff(_event_rate(ticker, 8), 4), 4), 4))
def cg_f081_company_identity_metadata_core97_3rd_v098_signal(ticker, name, exchange, category, siccode, scalemarketcap):
    return _clean(_mean(_diff(_diff(_to_num(exchange == 'NASDAQ'), 4), 4), 4))
def cg_f081_company_identity_metadata_core98_3rd_v099_signal(ticker, name, exchange, category, siccode, scalemarketcap):
    return _clean(_mean(_diff(_diff(_to_num(category == 'Domestic'), 4), 4), 4))
def cg_f081_company_identity_metadata_core99_3rd_v100_signal(ticker, name, exchange, category, siccode, scalemarketcap):
    return _clean(_mean(_diff(_diff(_to_num(siccode) / 1000.0, 4), 4), 4))
def cg_f081_company_identity_metadata_core100_3rd_v101_signal(ticker, name, exchange, category, siccode, scalemarketcap):
    return _clean(_mean(_slope(_diff(_to_num(siccode), 4), 8), 4))
def cg_f081_company_identity_metadata_core101_3rd_v102_signal(ticker, name, exchange, category, siccode, scalemarketcap):
    return _clean(_mean(_slope(_diff(_to_num(scalemarketcap), 4), 8), 4))
def cg_f081_company_identity_metadata_core102_3rd_v103_signal(ticker, name, exchange, category, siccode, scalemarketcap):
    return _clean(_mean(_slope(_diff(_event_flag(ticker), 4), 8), 4))
def cg_f081_company_identity_metadata_core103_3rd_v104_signal(ticker, name, exchange, category, siccode, scalemarketcap):
    return _clean(_mean(_slope(_diff(_event_flag(exchange), 4), 8), 4))
def cg_f081_company_identity_metadata_core104_3rd_v105_signal(ticker, name, exchange, category, siccode, scalemarketcap):
    return _clean(_mean(_slope(_diff(_event_flag(category), 4), 8), 4))
def cg_f081_company_identity_metadata_core105_3rd_v106_signal(ticker, name, exchange, category, siccode, scalemarketcap):
    return _clean(_mean(_slope(_diff(_event_count(ticker, 4), 4), 8), 4))
def cg_f081_company_identity_metadata_core106_3rd_v107_signal(ticker, name, exchange, category, siccode, scalemarketcap):
    return _clean(_mean(_slope(_diff(_event_rate(ticker, 8), 4), 8), 4))
def cg_f081_company_identity_metadata_core107_3rd_v108_signal(ticker, name, exchange, category, siccode, scalemarketcap):
    return _clean(_mean(_slope(_diff(_to_num(exchange == 'NASDAQ'), 4), 8), 4))
def cg_f081_company_identity_metadata_core108_3rd_v109_signal(ticker, name, exchange, category, siccode, scalemarketcap):
    return _clean(_mean(_slope(_diff(_to_num(category == 'Domestic'), 4), 8), 4))
def cg_f081_company_identity_metadata_core109_3rd_v110_signal(ticker, name, exchange, category, siccode, scalemarketcap):
    return _clean(_mean(_slope(_diff(_to_num(siccode) / 1000.0, 4), 8), 4))
def cg_f081_company_identity_metadata_core110_3rd_v111_signal(ticker, name, exchange, category, siccode, scalemarketcap):
    return _clean(_mean(_diff(_slope(_to_num(siccode), 4), 4), 4))
def cg_f081_company_identity_metadata_core111_3rd_v112_signal(ticker, name, exchange, category, siccode, scalemarketcap):
    return _clean(_mean(_diff(_slope(_to_num(scalemarketcap), 4), 4), 4))
def cg_f081_company_identity_metadata_core112_3rd_v113_signal(ticker, name, exchange, category, siccode, scalemarketcap):
    return _clean(_mean(_diff(_slope(_event_flag(ticker), 4), 4), 4))
def cg_f081_company_identity_metadata_core113_3rd_v114_signal(ticker, name, exchange, category, siccode, scalemarketcap):
    return _clean(_mean(_diff(_slope(_event_flag(exchange), 4), 4), 4))
def cg_f081_company_identity_metadata_core114_3rd_v115_signal(ticker, name, exchange, category, siccode, scalemarketcap):
    return _clean(_mean(_diff(_slope(_event_flag(category), 4), 4), 4))
def cg_f081_company_identity_metadata_core115_3rd_v116_signal(ticker, name, exchange, category, siccode, scalemarketcap):
    return _clean(_mean(_diff(_slope(_event_count(ticker, 4), 4), 4), 4))
def cg_f081_company_identity_metadata_core116_3rd_v117_signal(ticker, name, exchange, category, siccode, scalemarketcap):
    return _clean(_mean(_diff(_slope(_event_rate(ticker, 8), 4), 4), 4))
def cg_f081_company_identity_metadata_core117_3rd_v118_signal(ticker, name, exchange, category, siccode, scalemarketcap):
    return _clean(_mean(_diff(_slope(_to_num(exchange == 'NASDAQ'), 4), 4), 4))
def cg_f081_company_identity_metadata_core118_3rd_v119_signal(ticker, name, exchange, category, siccode, scalemarketcap):
    return _clean(_mean(_diff(_slope(_to_num(category == 'Domestic'), 4), 4), 4))
def cg_f081_company_identity_metadata_core119_3rd_v120_signal(ticker, name, exchange, category, siccode, scalemarketcap):
    return _clean(_mean(_diff(_slope(_to_num(siccode) / 1000.0, 4), 4), 4))
def cg_f081_company_identity_metadata_core120_3rd_v121_signal(ticker, name, exchange, category, siccode, scalemarketcap):
    return _clean(_slope(_diff(_diff(_to_num(siccode), 4), 4), 4))
def cg_f081_company_identity_metadata_core121_3rd_v122_signal(ticker, name, exchange, category, siccode, scalemarketcap):
    return _clean(_slope(_diff(_diff(_to_num(scalemarketcap), 4), 4), 4))
def cg_f081_company_identity_metadata_core122_3rd_v123_signal(ticker, name, exchange, category, siccode, scalemarketcap):
    return _clean(_slope(_diff(_diff(_event_flag(ticker), 4), 4), 4))
def cg_f081_company_identity_metadata_core123_3rd_v124_signal(ticker, name, exchange, category, siccode, scalemarketcap):
    return _clean(_slope(_diff(_diff(_event_flag(exchange), 4), 4), 4))
def cg_f081_company_identity_metadata_core124_3rd_v125_signal(ticker, name, exchange, category, siccode, scalemarketcap):
    return _clean(_slope(_diff(_diff(_event_flag(category), 4), 4), 4))
def cg_f081_company_identity_metadata_core125_3rd_v126_signal(ticker, name, exchange, category, siccode, scalemarketcap):
    return _clean(_slope(_diff(_diff(_event_count(ticker, 4), 4), 4), 4))
def cg_f081_company_identity_metadata_core126_3rd_v127_signal(ticker, name, exchange, category, siccode, scalemarketcap):
    return _clean(_slope(_diff(_diff(_event_rate(ticker, 8), 4), 4), 4))
def cg_f081_company_identity_metadata_core127_3rd_v128_signal(ticker, name, exchange, category, siccode, scalemarketcap):
    return _clean(_slope(_diff(_diff(_to_num(exchange == 'NASDAQ'), 4), 4), 4))
def cg_f081_company_identity_metadata_core128_3rd_v129_signal(ticker, name, exchange, category, siccode, scalemarketcap):
    return _clean(_slope(_diff(_diff(_to_num(category == 'Domestic'), 4), 4), 4))
def cg_f081_company_identity_metadata_core129_3rd_v130_signal(ticker, name, exchange, category, siccode, scalemarketcap):
    return _clean(_slope(_diff(_diff(_to_num(siccode) / 1000.0, 4), 4), 4))
def cg_f081_company_identity_metadata_core130_3rd_v131_signal(ticker, name, exchange, category, siccode, scalemarketcap):
    return _clean(_diff(_diff(_diff(_to_num(siccode), 4), 4), 4))
def cg_f081_company_identity_metadata_core131_3rd_v132_signal(ticker, name, exchange, category, siccode, scalemarketcap):
    return _clean(_diff(_diff(_diff(_to_num(scalemarketcap), 4), 4), 4))
def cg_f081_company_identity_metadata_core132_3rd_v133_signal(ticker, name, exchange, category, siccode, scalemarketcap):
    return _clean(_diff(_diff(_diff(_event_flag(ticker), 4), 4), 4))
def cg_f081_company_identity_metadata_core133_3rd_v134_signal(ticker, name, exchange, category, siccode, scalemarketcap):
    return _clean(_diff(_diff(_diff(_event_flag(exchange), 4), 4), 4))
def cg_f081_company_identity_metadata_core134_3rd_v135_signal(ticker, name, exchange, category, siccode, scalemarketcap):
    return _clean(_diff(_diff(_diff(_event_flag(category), 4), 4), 4))
def cg_f081_company_identity_metadata_core135_3rd_v136_signal(ticker, name, exchange, category, siccode, scalemarketcap):
    return _clean(_diff(_diff(_diff(_event_count(ticker, 4), 4), 4), 4))
def cg_f081_company_identity_metadata_core136_3rd_v137_signal(ticker, name, exchange, category, siccode, scalemarketcap):
    return _clean(_diff(_diff(_diff(_event_rate(ticker, 8), 4), 4), 4))
def cg_f081_company_identity_metadata_core137_3rd_v138_signal(ticker, name, exchange, category, siccode, scalemarketcap):
    return _clean(_diff(_diff(_diff(_to_num(exchange == 'NASDAQ'), 4), 4), 4))
def cg_f081_company_identity_metadata_core138_3rd_v139_signal(ticker, name, exchange, category, siccode, scalemarketcap):
    return _clean(_diff(_diff(_diff(_to_num(category == 'Domestic'), 4), 4), 4))
def cg_f081_company_identity_metadata_core139_3rd_v140_signal(ticker, name, exchange, category, siccode, scalemarketcap):
    return _clean(_diff(_diff(_diff(_to_num(siccode) / 1000.0, 4), 4), 4))
def cg_f081_company_identity_metadata_core140_3rd_v141_signal(ticker, name, exchange, category, siccode, scalemarketcap):
    return _clean(_z(_slope(_diff(_diff(_to_num(siccode), 4), 4), 4), 8))
def cg_f081_company_identity_metadata_core141_3rd_v142_signal(ticker, name, exchange, category, siccode, scalemarketcap):
    return _clean(_z(_slope(_diff(_diff(_to_num(scalemarketcap), 4), 4), 4), 8))
def cg_f081_company_identity_metadata_core142_3rd_v143_signal(ticker, name, exchange, category, siccode, scalemarketcap):
    return _clean(_z(_slope(_diff(_diff(_event_flag(ticker), 4), 4), 4), 8))
def cg_f081_company_identity_metadata_core143_3rd_v144_signal(ticker, name, exchange, category, siccode, scalemarketcap):
    return _clean(_z(_slope(_diff(_diff(_event_flag(exchange), 4), 4), 4), 8))
def cg_f081_company_identity_metadata_core144_3rd_v145_signal(ticker, name, exchange, category, siccode, scalemarketcap):
    return _clean(_z(_slope(_diff(_diff(_event_flag(category), 4), 4), 4), 8))
def cg_f081_company_identity_metadata_core145_3rd_v146_signal(ticker, name, exchange, category, siccode, scalemarketcap):
    return _clean(_z(_slope(_diff(_diff(_event_count(ticker, 4), 4), 4), 4), 8))
def cg_f081_company_identity_metadata_core146_3rd_v147_signal(ticker, name, exchange, category, siccode, scalemarketcap):
    return _clean(_z(_slope(_diff(_diff(_event_rate(ticker, 8), 4), 4), 4), 8))
def cg_f081_company_identity_metadata_core147_3rd_v148_signal(ticker, name, exchange, category, siccode, scalemarketcap):
    return _clean(_z(_slope(_diff(_diff(_to_num(exchange == 'NASDAQ'), 4), 4), 4), 8))
def cg_f081_company_identity_metadata_core148_3rd_v149_signal(ticker, name, exchange, category, siccode, scalemarketcap):
    return _clean(_z(_slope(_diff(_diff(_to_num(category == 'Domestic'), 4), 4), 4), 8))
def cg_f081_company_identity_metadata_core149_3rd_v150_signal(ticker, name, exchange, category, siccode, scalemarketcap):
    return _clean(_z(_slope(_diff(_diff(_to_num(siccode) / 1000.0, 4), 4), 4), 8))