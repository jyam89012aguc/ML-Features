import numpy as np
import pandas as pd
from technology_helpers import _to_num, _clean, _safe_div, _log, _mean, _std, _sum, _min, _max, _z, _pct_change, _diff, _rank, _skew, _kurt, _autocorr, _corr, _slope, _ewm, _event_flag, _event_count, _event_rate, _clip_z

def cg_f081_company_identity_metadata_core00_2nd_v001_signal(ticker, name, exchange, category, siccode, scalemarketcap):
    return _clean(_slope(_to_num(siccode), 4))
def cg_f081_company_identity_metadata_core01_2nd_v002_signal(ticker, name, exchange, category, siccode, scalemarketcap):
    return _clean(_slope(_to_num(scalemarketcap), 4))
def cg_f081_company_identity_metadata_core02_2nd_v003_signal(ticker, name, exchange, category, siccode, scalemarketcap):
    return _clean(_slope(_event_flag(ticker), 4))
def cg_f081_company_identity_metadata_core03_2nd_v004_signal(ticker, name, exchange, category, siccode, scalemarketcap):
    return _clean(_slope(_event_flag(exchange), 4))
def cg_f081_company_identity_metadata_core04_2nd_v005_signal(ticker, name, exchange, category, siccode, scalemarketcap):
    return _clean(_slope(_event_flag(category), 4))
def cg_f081_company_identity_metadata_core05_2nd_v006_signal(ticker, name, exchange, category, siccode, scalemarketcap):
    return _clean(_slope(_event_count(ticker, 4), 4))
def cg_f081_company_identity_metadata_core06_2nd_v007_signal(ticker, name, exchange, category, siccode, scalemarketcap):
    return _clean(_slope(_event_rate(ticker, 8), 4))
def cg_f081_company_identity_metadata_core07_2nd_v008_signal(ticker, name, exchange, category, siccode, scalemarketcap):
    return _clean(_slope(_to_num(exchange == 'NASDAQ'), 4))
def cg_f081_company_identity_metadata_core08_2nd_v009_signal(ticker, name, exchange, category, siccode, scalemarketcap):
    return _clean(_slope(_to_num(category == 'Domestic'), 4))
def cg_f081_company_identity_metadata_core09_2nd_v010_signal(ticker, name, exchange, category, siccode, scalemarketcap):
    return _clean(_slope(_to_num(siccode) / 1000.0, 4))
def cg_f081_company_identity_metadata_core10_2nd_v011_signal(ticker, name, exchange, category, siccode, scalemarketcap):
    return _clean(_slope(_to_num(siccode), 8))
def cg_f081_company_identity_metadata_core11_2nd_v012_signal(ticker, name, exchange, category, siccode, scalemarketcap):
    return _clean(_slope(_to_num(scalemarketcap), 8))
def cg_f081_company_identity_metadata_core12_2nd_v013_signal(ticker, name, exchange, category, siccode, scalemarketcap):
    return _clean(_slope(_event_flag(ticker), 8))
def cg_f081_company_identity_metadata_core13_2nd_v014_signal(ticker, name, exchange, category, siccode, scalemarketcap):
    return _clean(_slope(_event_flag(exchange), 8))
def cg_f081_company_identity_metadata_core14_2nd_v015_signal(ticker, name, exchange, category, siccode, scalemarketcap):
    return _clean(_slope(_event_flag(category), 8))
def cg_f081_company_identity_metadata_core15_2nd_v016_signal(ticker, name, exchange, category, siccode, scalemarketcap):
    return _clean(_slope(_event_count(ticker, 4), 8))
def cg_f081_company_identity_metadata_core16_2nd_v017_signal(ticker, name, exchange, category, siccode, scalemarketcap):
    return _clean(_slope(_event_rate(ticker, 8), 8))
def cg_f081_company_identity_metadata_core17_2nd_v018_signal(ticker, name, exchange, category, siccode, scalemarketcap):
    return _clean(_slope(_to_num(exchange == 'NASDAQ'), 8))
def cg_f081_company_identity_metadata_core18_2nd_v019_signal(ticker, name, exchange, category, siccode, scalemarketcap):
    return _clean(_slope(_to_num(category == 'Domestic'), 8))
def cg_f081_company_identity_metadata_core19_2nd_v020_signal(ticker, name, exchange, category, siccode, scalemarketcap):
    return _clean(_slope(_to_num(siccode) / 1000.0, 8))
def cg_f081_company_identity_metadata_core20_2nd_v021_signal(ticker, name, exchange, category, siccode, scalemarketcap):
    return _clean(_diff(_to_num(siccode), 4))
def cg_f081_company_identity_metadata_core21_2nd_v022_signal(ticker, name, exchange, category, siccode, scalemarketcap):
    return _clean(_diff(_to_num(scalemarketcap), 4))
def cg_f081_company_identity_metadata_core22_2nd_v023_signal(ticker, name, exchange, category, siccode, scalemarketcap):
    return _clean(_diff(_event_flag(ticker), 4))
def cg_f081_company_identity_metadata_core23_2nd_v024_signal(ticker, name, exchange, category, siccode, scalemarketcap):
    return _clean(_diff(_event_flag(exchange), 4))
def cg_f081_company_identity_metadata_core24_2nd_v025_signal(ticker, name, exchange, category, siccode, scalemarketcap):
    return _clean(_diff(_event_flag(category), 4))
def cg_f081_company_identity_metadata_core25_2nd_v026_signal(ticker, name, exchange, category, siccode, scalemarketcap):
    return _clean(_diff(_event_count(ticker, 4), 4))
def cg_f081_company_identity_metadata_core26_2nd_v027_signal(ticker, name, exchange, category, siccode, scalemarketcap):
    return _clean(_diff(_event_rate(ticker, 8), 4))
def cg_f081_company_identity_metadata_core27_2nd_v028_signal(ticker, name, exchange, category, siccode, scalemarketcap):
    return _clean(_diff(_to_num(exchange == 'NASDAQ'), 4))
def cg_f081_company_identity_metadata_core28_2nd_v029_signal(ticker, name, exchange, category, siccode, scalemarketcap):
    return _clean(_diff(_to_num(category == 'Domestic'), 4))
def cg_f081_company_identity_metadata_core29_2nd_v030_signal(ticker, name, exchange, category, siccode, scalemarketcap):
    return _clean(_diff(_to_num(siccode) / 1000.0, 4))
def cg_f081_company_identity_metadata_core30_2nd_v031_signal(ticker, name, exchange, category, siccode, scalemarketcap):
    return _clean(_z(_slope(_to_num(siccode), 4), 8))
def cg_f081_company_identity_metadata_core31_2nd_v032_signal(ticker, name, exchange, category, siccode, scalemarketcap):
    return _clean(_z(_slope(_to_num(scalemarketcap), 4), 8))
def cg_f081_company_identity_metadata_core32_2nd_v033_signal(ticker, name, exchange, category, siccode, scalemarketcap):
    return _clean(_z(_slope(_event_flag(ticker), 4), 8))
def cg_f081_company_identity_metadata_core33_2nd_v034_signal(ticker, name, exchange, category, siccode, scalemarketcap):
    return _clean(_z(_slope(_event_flag(exchange), 4), 8))
def cg_f081_company_identity_metadata_core34_2nd_v035_signal(ticker, name, exchange, category, siccode, scalemarketcap):
    return _clean(_z(_slope(_event_flag(category), 4), 8))
def cg_f081_company_identity_metadata_core35_2nd_v036_signal(ticker, name, exchange, category, siccode, scalemarketcap):
    return _clean(_z(_slope(_event_count(ticker, 4), 4), 8))
def cg_f081_company_identity_metadata_core36_2nd_v037_signal(ticker, name, exchange, category, siccode, scalemarketcap):
    return _clean(_z(_slope(_event_rate(ticker, 8), 4), 8))
def cg_f081_company_identity_metadata_core37_2nd_v038_signal(ticker, name, exchange, category, siccode, scalemarketcap):
    return _clean(_z(_slope(_to_num(exchange == 'NASDAQ'), 4), 8))
def cg_f081_company_identity_metadata_core38_2nd_v039_signal(ticker, name, exchange, category, siccode, scalemarketcap):
    return _clean(_z(_slope(_to_num(category == 'Domestic'), 4), 8))
def cg_f081_company_identity_metadata_core39_2nd_v040_signal(ticker, name, exchange, category, siccode, scalemarketcap):
    return _clean(_z(_slope(_to_num(siccode) / 1000.0, 4), 8))
def cg_f081_company_identity_metadata_core40_2nd_v041_signal(ticker, name, exchange, category, siccode, scalemarketcap):
    return _clean(_z(_slope(_to_num(siccode), 8), 12))
def cg_f081_company_identity_metadata_core41_2nd_v042_signal(ticker, name, exchange, category, siccode, scalemarketcap):
    return _clean(_z(_slope(_to_num(scalemarketcap), 8), 12))
def cg_f081_company_identity_metadata_core42_2nd_v043_signal(ticker, name, exchange, category, siccode, scalemarketcap):
    return _clean(_z(_slope(_event_flag(ticker), 8), 12))
def cg_f081_company_identity_metadata_core43_2nd_v044_signal(ticker, name, exchange, category, siccode, scalemarketcap):
    return _clean(_z(_slope(_event_flag(exchange), 8), 12))
def cg_f081_company_identity_metadata_core44_2nd_v045_signal(ticker, name, exchange, category, siccode, scalemarketcap):
    return _clean(_z(_slope(_event_flag(category), 8), 12))
def cg_f081_company_identity_metadata_core45_2nd_v046_signal(ticker, name, exchange, category, siccode, scalemarketcap):
    return _clean(_z(_slope(_event_count(ticker, 4), 8), 12))
def cg_f081_company_identity_metadata_core46_2nd_v047_signal(ticker, name, exchange, category, siccode, scalemarketcap):
    return _clean(_z(_slope(_event_rate(ticker, 8), 8), 12))
def cg_f081_company_identity_metadata_core47_2nd_v048_signal(ticker, name, exchange, category, siccode, scalemarketcap):
    return _clean(_z(_slope(_to_num(exchange == 'NASDAQ'), 8), 12))
def cg_f081_company_identity_metadata_core48_2nd_v049_signal(ticker, name, exchange, category, siccode, scalemarketcap):
    return _clean(_z(_slope(_to_num(category == 'Domestic'), 8), 12))
def cg_f081_company_identity_metadata_core49_2nd_v050_signal(ticker, name, exchange, category, siccode, scalemarketcap):
    return _clean(_z(_slope(_to_num(siccode) / 1000.0, 8), 12))
def cg_f081_company_identity_metadata_core50_2nd_v051_signal(ticker, name, exchange, category, siccode, scalemarketcap):
    return _clean(_z(_diff(_to_num(siccode), 4), 8))
def cg_f081_company_identity_metadata_core51_2nd_v052_signal(ticker, name, exchange, category, siccode, scalemarketcap):
    return _clean(_z(_diff(_to_num(scalemarketcap), 4), 8))
def cg_f081_company_identity_metadata_core52_2nd_v053_signal(ticker, name, exchange, category, siccode, scalemarketcap):
    return _clean(_z(_diff(_event_flag(ticker), 4), 8))
def cg_f081_company_identity_metadata_core53_2nd_v054_signal(ticker, name, exchange, category, siccode, scalemarketcap):
    return _clean(_z(_diff(_event_flag(exchange), 4), 8))
def cg_f081_company_identity_metadata_core54_2nd_v055_signal(ticker, name, exchange, category, siccode, scalemarketcap):
    return _clean(_z(_diff(_event_flag(category), 4), 8))
def cg_f081_company_identity_metadata_core55_2nd_v056_signal(ticker, name, exchange, category, siccode, scalemarketcap):
    return _clean(_z(_diff(_event_count(ticker, 4), 4), 8))
def cg_f081_company_identity_metadata_core56_2nd_v057_signal(ticker, name, exchange, category, siccode, scalemarketcap):
    return _clean(_z(_diff(_event_rate(ticker, 8), 4), 8))
def cg_f081_company_identity_metadata_core57_2nd_v058_signal(ticker, name, exchange, category, siccode, scalemarketcap):
    return _clean(_z(_diff(_to_num(exchange == 'NASDAQ'), 4), 8))
def cg_f081_company_identity_metadata_core58_2nd_v059_signal(ticker, name, exchange, category, siccode, scalemarketcap):
    return _clean(_z(_diff(_to_num(category == 'Domestic'), 4), 8))
def cg_f081_company_identity_metadata_core59_2nd_v060_signal(ticker, name, exchange, category, siccode, scalemarketcap):
    return _clean(_z(_diff(_to_num(siccode) / 1000.0, 4), 8))
def cg_f081_company_identity_metadata_core60_2nd_v061_signal(ticker, name, exchange, category, siccode, scalemarketcap):
    return _clean(_rank(_slope(_to_num(siccode), 4), 12))
def cg_f081_company_identity_metadata_core61_2nd_v062_signal(ticker, name, exchange, category, siccode, scalemarketcap):
    return _clean(_rank(_slope(_to_num(scalemarketcap), 4), 12))
def cg_f081_company_identity_metadata_core62_2nd_v063_signal(ticker, name, exchange, category, siccode, scalemarketcap):
    return _clean(_rank(_slope(_event_flag(ticker), 4), 12))
def cg_f081_company_identity_metadata_core63_2nd_v064_signal(ticker, name, exchange, category, siccode, scalemarketcap):
    return _clean(_rank(_slope(_event_flag(exchange), 4), 12))
def cg_f081_company_identity_metadata_core64_2nd_v065_signal(ticker, name, exchange, category, siccode, scalemarketcap):
    return _clean(_rank(_slope(_event_flag(category), 4), 12))
def cg_f081_company_identity_metadata_core65_2nd_v066_signal(ticker, name, exchange, category, siccode, scalemarketcap):
    return _clean(_rank(_slope(_event_count(ticker, 4), 4), 12))
def cg_f081_company_identity_metadata_core66_2nd_v067_signal(ticker, name, exchange, category, siccode, scalemarketcap):
    return _clean(_rank(_slope(_event_rate(ticker, 8), 4), 12))
def cg_f081_company_identity_metadata_core67_2nd_v068_signal(ticker, name, exchange, category, siccode, scalemarketcap):
    return _clean(_rank(_slope(_to_num(exchange == 'NASDAQ'), 4), 12))
def cg_f081_company_identity_metadata_core68_2nd_v069_signal(ticker, name, exchange, category, siccode, scalemarketcap):
    return _clean(_rank(_slope(_to_num(category == 'Domestic'), 4), 12))
def cg_f081_company_identity_metadata_core69_2nd_v070_signal(ticker, name, exchange, category, siccode, scalemarketcap):
    return _clean(_rank(_slope(_to_num(siccode) / 1000.0, 4), 12))
def cg_f081_company_identity_metadata_core70_2nd_v071_signal(ticker, name, exchange, category, siccode, scalemarketcap):
    return _clean(_rank(_diff(_to_num(siccode), 4), 12))
def cg_f081_company_identity_metadata_core71_2nd_v072_signal(ticker, name, exchange, category, siccode, scalemarketcap):
    return _clean(_rank(_diff(_to_num(scalemarketcap), 4), 12))
def cg_f081_company_identity_metadata_core72_2nd_v073_signal(ticker, name, exchange, category, siccode, scalemarketcap):
    return _clean(_rank(_diff(_event_flag(ticker), 4), 12))
def cg_f081_company_identity_metadata_core73_2nd_v074_signal(ticker, name, exchange, category, siccode, scalemarketcap):
    return _clean(_rank(_diff(_event_flag(exchange), 4), 12))
def cg_f081_company_identity_metadata_core74_2nd_v075_signal(ticker, name, exchange, category, siccode, scalemarketcap):
    return _clean(_rank(_diff(_event_flag(category), 4), 12))
def cg_f081_company_identity_metadata_core75_2nd_v076_signal(ticker, name, exchange, category, siccode, scalemarketcap):
    return _clean(_rank(_diff(_event_count(ticker, 4), 4), 12))
def cg_f081_company_identity_metadata_core76_2nd_v077_signal(ticker, name, exchange, category, siccode, scalemarketcap):
    return _clean(_rank(_diff(_event_rate(ticker, 8), 4), 12))
def cg_f081_company_identity_metadata_core77_2nd_v078_signal(ticker, name, exchange, category, siccode, scalemarketcap):
    return _clean(_rank(_diff(_to_num(exchange == 'NASDAQ'), 4), 12))
def cg_f081_company_identity_metadata_core78_2nd_v079_signal(ticker, name, exchange, category, siccode, scalemarketcap):
    return _clean(_rank(_diff(_to_num(category == 'Domestic'), 4), 12))
def cg_f081_company_identity_metadata_core79_2nd_v080_signal(ticker, name, exchange, category, siccode, scalemarketcap):
    return _clean(_rank(_diff(_to_num(siccode) / 1000.0, 4), 12))
def cg_f081_company_identity_metadata_core80_2nd_v081_signal(ticker, name, exchange, category, siccode, scalemarketcap):
    return _clean(_mean(_slope(_to_num(siccode), 4), 4))
def cg_f081_company_identity_metadata_core81_2nd_v082_signal(ticker, name, exchange, category, siccode, scalemarketcap):
    return _clean(_mean(_slope(_to_num(scalemarketcap), 4), 4))
def cg_f081_company_identity_metadata_core82_2nd_v083_signal(ticker, name, exchange, category, siccode, scalemarketcap):
    return _clean(_mean(_slope(_event_flag(ticker), 4), 4))
def cg_f081_company_identity_metadata_core83_2nd_v084_signal(ticker, name, exchange, category, siccode, scalemarketcap):
    return _clean(_mean(_slope(_event_flag(exchange), 4), 4))
def cg_f081_company_identity_metadata_core84_2nd_v085_signal(ticker, name, exchange, category, siccode, scalemarketcap):
    return _clean(_mean(_slope(_event_flag(category), 4), 4))
def cg_f081_company_identity_metadata_core85_2nd_v086_signal(ticker, name, exchange, category, siccode, scalemarketcap):
    return _clean(_mean(_slope(_event_count(ticker, 4), 4), 4))
def cg_f081_company_identity_metadata_core86_2nd_v087_signal(ticker, name, exchange, category, siccode, scalemarketcap):
    return _clean(_mean(_slope(_event_rate(ticker, 8), 4), 4))
def cg_f081_company_identity_metadata_core87_2nd_v088_signal(ticker, name, exchange, category, siccode, scalemarketcap):
    return _clean(_mean(_slope(_to_num(exchange == 'NASDAQ'), 4), 4))
def cg_f081_company_identity_metadata_core88_2nd_v089_signal(ticker, name, exchange, category, siccode, scalemarketcap):
    return _clean(_mean(_slope(_to_num(category == 'Domestic'), 4), 4))
def cg_f081_company_identity_metadata_core89_2nd_v090_signal(ticker, name, exchange, category, siccode, scalemarketcap):
    return _clean(_mean(_slope(_to_num(siccode) / 1000.0, 4), 4))
def cg_f081_company_identity_metadata_core90_2nd_v091_signal(ticker, name, exchange, category, siccode, scalemarketcap):
    return _clean(_mean(_diff(_to_num(siccode), 4), 4))
def cg_f081_company_identity_metadata_core91_2nd_v092_signal(ticker, name, exchange, category, siccode, scalemarketcap):
    return _clean(_mean(_diff(_to_num(scalemarketcap), 4), 4))
def cg_f081_company_identity_metadata_core92_2nd_v093_signal(ticker, name, exchange, category, siccode, scalemarketcap):
    return _clean(_mean(_diff(_event_flag(ticker), 4), 4))
def cg_f081_company_identity_metadata_core93_2nd_v094_signal(ticker, name, exchange, category, siccode, scalemarketcap):
    return _clean(_mean(_diff(_event_flag(exchange), 4), 4))
def cg_f081_company_identity_metadata_core94_2nd_v095_signal(ticker, name, exchange, category, siccode, scalemarketcap):
    return _clean(_mean(_diff(_event_flag(category), 4), 4))
def cg_f081_company_identity_metadata_core95_2nd_v096_signal(ticker, name, exchange, category, siccode, scalemarketcap):
    return _clean(_mean(_diff(_event_count(ticker, 4), 4), 4))
def cg_f081_company_identity_metadata_core96_2nd_v097_signal(ticker, name, exchange, category, siccode, scalemarketcap):
    return _clean(_mean(_diff(_event_rate(ticker, 8), 4), 4))
def cg_f081_company_identity_metadata_core97_2nd_v098_signal(ticker, name, exchange, category, siccode, scalemarketcap):
    return _clean(_mean(_diff(_to_num(exchange == 'NASDAQ'), 4), 4))
def cg_f081_company_identity_metadata_core98_2nd_v099_signal(ticker, name, exchange, category, siccode, scalemarketcap):
    return _clean(_mean(_diff(_to_num(category == 'Domestic'), 4), 4))
def cg_f081_company_identity_metadata_core99_2nd_v100_signal(ticker, name, exchange, category, siccode, scalemarketcap):
    return _clean(_mean(_diff(_to_num(siccode) / 1000.0, 4), 4))
def cg_f081_company_identity_metadata_core100_2nd_v101_signal(ticker, name, exchange, category, siccode, scalemarketcap):
    return _clean(_slope(_mean(_to_num(siccode), 4), 4))
def cg_f081_company_identity_metadata_core101_2nd_v102_signal(ticker, name, exchange, category, siccode, scalemarketcap):
    return _clean(_slope(_mean(_to_num(scalemarketcap), 4), 4))
def cg_f081_company_identity_metadata_core102_2nd_v103_signal(ticker, name, exchange, category, siccode, scalemarketcap):
    return _clean(_slope(_mean(_event_flag(ticker), 4), 4))
def cg_f081_company_identity_metadata_core103_2nd_v104_signal(ticker, name, exchange, category, siccode, scalemarketcap):
    return _clean(_slope(_mean(_event_flag(exchange), 4), 4))
def cg_f081_company_identity_metadata_core104_2nd_v105_signal(ticker, name, exchange, category, siccode, scalemarketcap):
    return _clean(_slope(_mean(_event_flag(category), 4), 4))
def cg_f081_company_identity_metadata_core105_2nd_v106_signal(ticker, name, exchange, category, siccode, scalemarketcap):
    return _clean(_slope(_mean(_event_count(ticker, 4), 4), 4))
def cg_f081_company_identity_metadata_core106_2nd_v107_signal(ticker, name, exchange, category, siccode, scalemarketcap):
    return _clean(_slope(_mean(_event_rate(ticker, 8), 4), 4))
def cg_f081_company_identity_metadata_core107_2nd_v108_signal(ticker, name, exchange, category, siccode, scalemarketcap):
    return _clean(_slope(_mean(_to_num(exchange == 'NASDAQ'), 4), 4))
def cg_f081_company_identity_metadata_core108_2nd_v109_signal(ticker, name, exchange, category, siccode, scalemarketcap):
    return _clean(_slope(_mean(_to_num(category == 'Domestic'), 4), 4))
def cg_f081_company_identity_metadata_core109_2nd_v110_signal(ticker, name, exchange, category, siccode, scalemarketcap):
    return _clean(_slope(_mean(_to_num(siccode) / 1000.0, 4), 4))
def cg_f081_company_identity_metadata_core110_2nd_v111_signal(ticker, name, exchange, category, siccode, scalemarketcap):
    return _clean(_slope(_mean(_to_num(siccode), 8), 8))
def cg_f081_company_identity_metadata_core111_2nd_v112_signal(ticker, name, exchange, category, siccode, scalemarketcap):
    return _clean(_slope(_mean(_to_num(scalemarketcap), 8), 8))
def cg_f081_company_identity_metadata_core112_2nd_v113_signal(ticker, name, exchange, category, siccode, scalemarketcap):
    return _clean(_slope(_mean(_event_flag(ticker), 8), 8))
def cg_f081_company_identity_metadata_core113_2nd_v114_signal(ticker, name, exchange, category, siccode, scalemarketcap):
    return _clean(_slope(_mean(_event_flag(exchange), 8), 8))
def cg_f081_company_identity_metadata_core114_2nd_v115_signal(ticker, name, exchange, category, siccode, scalemarketcap):
    return _clean(_slope(_mean(_event_flag(category), 8), 8))
def cg_f081_company_identity_metadata_core115_2nd_v116_signal(ticker, name, exchange, category, siccode, scalemarketcap):
    return _clean(_slope(_mean(_event_count(ticker, 4), 8), 8))
def cg_f081_company_identity_metadata_core116_2nd_v117_signal(ticker, name, exchange, category, siccode, scalemarketcap):
    return _clean(_slope(_mean(_event_rate(ticker, 8), 8), 8))
def cg_f081_company_identity_metadata_core117_2nd_v118_signal(ticker, name, exchange, category, siccode, scalemarketcap):
    return _clean(_slope(_mean(_to_num(exchange == 'NASDAQ'), 8), 8))
def cg_f081_company_identity_metadata_core118_2nd_v119_signal(ticker, name, exchange, category, siccode, scalemarketcap):
    return _clean(_slope(_mean(_to_num(category == 'Domestic'), 8), 8))
def cg_f081_company_identity_metadata_core119_2nd_v120_signal(ticker, name, exchange, category, siccode, scalemarketcap):
    return _clean(_slope(_mean(_to_num(siccode) / 1000.0, 8), 8))
def cg_f081_company_identity_metadata_core120_2nd_v121_signal(ticker, name, exchange, category, siccode, scalemarketcap):
    return _clean(_diff(_mean(_to_num(siccode), 4), 4))
def cg_f081_company_identity_metadata_core121_2nd_v122_signal(ticker, name, exchange, category, siccode, scalemarketcap):
    return _clean(_diff(_mean(_to_num(scalemarketcap), 4), 4))
def cg_f081_company_identity_metadata_core122_2nd_v123_signal(ticker, name, exchange, category, siccode, scalemarketcap):
    return _clean(_diff(_mean(_event_flag(ticker), 4), 4))
def cg_f081_company_identity_metadata_core123_2nd_v124_signal(ticker, name, exchange, category, siccode, scalemarketcap):
    return _clean(_diff(_mean(_event_flag(exchange), 4), 4))
def cg_f081_company_identity_metadata_core124_2nd_v125_signal(ticker, name, exchange, category, siccode, scalemarketcap):
    return _clean(_diff(_mean(_event_flag(category), 4), 4))
def cg_f081_company_identity_metadata_core125_2nd_v126_signal(ticker, name, exchange, category, siccode, scalemarketcap):
    return _clean(_diff(_mean(_event_count(ticker, 4), 4), 4))
def cg_f081_company_identity_metadata_core126_2nd_v127_signal(ticker, name, exchange, category, siccode, scalemarketcap):
    return _clean(_diff(_mean(_event_rate(ticker, 8), 4), 4))
def cg_f081_company_identity_metadata_core127_2nd_v128_signal(ticker, name, exchange, category, siccode, scalemarketcap):
    return _clean(_diff(_mean(_to_num(exchange == 'NASDAQ'), 4), 4))
def cg_f081_company_identity_metadata_core128_2nd_v129_signal(ticker, name, exchange, category, siccode, scalemarketcap):
    return _clean(_diff(_mean(_to_num(category == 'Domestic'), 4), 4))
def cg_f081_company_identity_metadata_core129_2nd_v130_signal(ticker, name, exchange, category, siccode, scalemarketcap):
    return _clean(_diff(_mean(_to_num(siccode) / 1000.0, 4), 4))
def cg_f081_company_identity_metadata_core130_2nd_v131_signal(ticker, name, exchange, category, siccode, scalemarketcap):
    return _clean(_z(_diff(_mean(_to_num(siccode), 4), 4), 8))
def cg_f081_company_identity_metadata_core131_2nd_v132_signal(ticker, name, exchange, category, siccode, scalemarketcap):
    return _clean(_z(_diff(_mean(_to_num(scalemarketcap), 4), 4), 8))
def cg_f081_company_identity_metadata_core132_2nd_v133_signal(ticker, name, exchange, category, siccode, scalemarketcap):
    return _clean(_z(_diff(_mean(_event_flag(ticker), 4), 4), 8))
def cg_f081_company_identity_metadata_core133_2nd_v134_signal(ticker, name, exchange, category, siccode, scalemarketcap):
    return _clean(_z(_diff(_mean(_event_flag(exchange), 4), 4), 8))
def cg_f081_company_identity_metadata_core134_2nd_v135_signal(ticker, name, exchange, category, siccode, scalemarketcap):
    return _clean(_z(_diff(_mean(_event_flag(category), 4), 4), 8))
def cg_f081_company_identity_metadata_core135_2nd_v136_signal(ticker, name, exchange, category, siccode, scalemarketcap):
    return _clean(_z(_diff(_mean(_event_count(ticker, 4), 4), 4), 8))
def cg_f081_company_identity_metadata_core136_2nd_v137_signal(ticker, name, exchange, category, siccode, scalemarketcap):
    return _clean(_z(_diff(_mean(_event_rate(ticker, 8), 4), 4), 8))
def cg_f081_company_identity_metadata_core137_2nd_v138_signal(ticker, name, exchange, category, siccode, scalemarketcap):
    return _clean(_z(_diff(_mean(_to_num(exchange == 'NASDAQ'), 4), 4), 8))
def cg_f081_company_identity_metadata_core138_2nd_v139_signal(ticker, name, exchange, category, siccode, scalemarketcap):
    return _clean(_z(_diff(_mean(_to_num(category == 'Domestic'), 4), 4), 8))
def cg_f081_company_identity_metadata_core139_2nd_v140_signal(ticker, name, exchange, category, siccode, scalemarketcap):
    return _clean(_z(_diff(_mean(_to_num(siccode) / 1000.0, 4), 4), 8))
def cg_f081_company_identity_metadata_core140_2nd_v141_signal(ticker, name, exchange, category, siccode, scalemarketcap):
    return _clean(_rank(_slope(_mean(_to_num(siccode), 4), 4), 12))
def cg_f081_company_identity_metadata_core141_2nd_v142_signal(ticker, name, exchange, category, siccode, scalemarketcap):
    return _clean(_rank(_slope(_mean(_to_num(scalemarketcap), 4), 4), 12))
def cg_f081_company_identity_metadata_core142_2nd_v143_signal(ticker, name, exchange, category, siccode, scalemarketcap):
    return _clean(_rank(_slope(_mean(_event_flag(ticker), 4), 4), 12))
def cg_f081_company_identity_metadata_core143_2nd_v144_signal(ticker, name, exchange, category, siccode, scalemarketcap):
    return _clean(_rank(_slope(_mean(_event_flag(exchange), 4), 4), 12))
def cg_f081_company_identity_metadata_core144_2nd_v145_signal(ticker, name, exchange, category, siccode, scalemarketcap):
    return _clean(_rank(_slope(_mean(_event_flag(category), 4), 4), 12))
def cg_f081_company_identity_metadata_core145_2nd_v146_signal(ticker, name, exchange, category, siccode, scalemarketcap):
    return _clean(_rank(_slope(_mean(_event_count(ticker, 4), 4), 4), 12))
def cg_f081_company_identity_metadata_core146_2nd_v147_signal(ticker, name, exchange, category, siccode, scalemarketcap):
    return _clean(_rank(_slope(_mean(_event_rate(ticker, 8), 4), 4), 12))
def cg_f081_company_identity_metadata_core147_2nd_v148_signal(ticker, name, exchange, category, siccode, scalemarketcap):
    return _clean(_rank(_slope(_mean(_to_num(exchange == 'NASDAQ'), 4), 4), 12))
def cg_f081_company_identity_metadata_core148_2nd_v149_signal(ticker, name, exchange, category, siccode, scalemarketcap):
    return _clean(_rank(_slope(_mean(_to_num(category == 'Domestic'), 4), 4), 12))
def cg_f081_company_identity_metadata_core149_2nd_v150_signal(ticker, name, exchange, category, siccode, scalemarketcap):
    return _clean(_rank(_slope(_mean(_to_num(siccode) / 1000.0, 4), 4), 12))