import numpy as np
import pandas as pd
from technology_helpers import _to_num, _clean, _safe_div, _log, _mean, _std, _sum, _min, _max, _z, _pct_change, _diff, _rank, _skew, _kurt, _autocorr, _corr, _slope, _ewm, _event_flag, _event_count, _event_rate, _clip_z

def cg_f082_sector_industry_tech_filter_core00_2nd_v001_signal(sector, industry, sicsector, sicindustry, famasector, famaindustry):
    return _clean(_slope(_to_num(sicsector), 4))
def cg_f082_sector_industry_tech_filter_core01_2nd_v002_signal(sector, industry, sicsector, sicindustry, famasector, famaindustry):
    return _clean(_slope(_to_num(sicindustry), 4))
def cg_f082_sector_industry_tech_filter_core02_2nd_v003_signal(sector, industry, sicsector, sicindustry, famasector, famaindustry):
    return _clean(_slope(_event_flag(sector), 4))
def cg_f082_sector_industry_tech_filter_core03_2nd_v004_signal(sector, industry, sicsector, sicindustry, famasector, famaindustry):
    return _clean(_slope(_event_flag(industry), 4))
def cg_f082_sector_industry_tech_filter_core04_2nd_v005_signal(sector, industry, sicsector, sicindustry, famasector, famaindustry):
    return _clean(_slope(_event_flag(famasector), 4))
def cg_f082_sector_industry_tech_filter_core05_2nd_v006_signal(sector, industry, sicsector, sicindustry, famasector, famaindustry):
    return _clean(_slope(_event_flag(famaindustry), 4))
def cg_f082_sector_industry_tech_filter_core06_2nd_v007_signal(sector, industry, sicsector, sicindustry, famasector, famaindustry):
    return _clean(_slope(_event_count(sector, 4), 4))
def cg_f082_sector_industry_tech_filter_core07_2nd_v008_signal(sector, industry, sicsector, sicindustry, famasector, famaindustry):
    return _clean(_slope(_event_rate(industry, 8), 4))
def cg_f082_sector_industry_tech_filter_core08_2nd_v009_signal(sector, industry, sicsector, sicindustry, famasector, famaindustry):
    return _clean(_slope(_to_num(famasector), 4))
def cg_f082_sector_industry_tech_filter_core09_2nd_v010_signal(sector, industry, sicsector, sicindustry, famasector, famaindustry):
    return _clean(_slope(_to_num(famaindustry), 4))
def cg_f082_sector_industry_tech_filter_core10_2nd_v011_signal(sector, industry, sicsector, sicindustry, famasector, famaindustry):
    return _clean(_slope(_to_num(sicsector), 8))
def cg_f082_sector_industry_tech_filter_core11_2nd_v012_signal(sector, industry, sicsector, sicindustry, famasector, famaindustry):
    return _clean(_slope(_to_num(sicindustry), 8))
def cg_f082_sector_industry_tech_filter_core12_2nd_v013_signal(sector, industry, sicsector, sicindustry, famasector, famaindustry):
    return _clean(_slope(_event_flag(sector), 8))
def cg_f082_sector_industry_tech_filter_core13_2nd_v014_signal(sector, industry, sicsector, sicindustry, famasector, famaindustry):
    return _clean(_slope(_event_flag(industry), 8))
def cg_f082_sector_industry_tech_filter_core14_2nd_v015_signal(sector, industry, sicsector, sicindustry, famasector, famaindustry):
    return _clean(_slope(_event_flag(famasector), 8))
def cg_f082_sector_industry_tech_filter_core15_2nd_v016_signal(sector, industry, sicsector, sicindustry, famasector, famaindustry):
    return _clean(_slope(_event_flag(famaindustry), 8))
def cg_f082_sector_industry_tech_filter_core16_2nd_v017_signal(sector, industry, sicsector, sicindustry, famasector, famaindustry):
    return _clean(_slope(_event_count(sector, 4), 8))
def cg_f082_sector_industry_tech_filter_core17_2nd_v018_signal(sector, industry, sicsector, sicindustry, famasector, famaindustry):
    return _clean(_slope(_event_rate(industry, 8), 8))
def cg_f082_sector_industry_tech_filter_core18_2nd_v019_signal(sector, industry, sicsector, sicindustry, famasector, famaindustry):
    return _clean(_slope(_to_num(famasector), 8))
def cg_f082_sector_industry_tech_filter_core19_2nd_v020_signal(sector, industry, sicsector, sicindustry, famasector, famaindustry):
    return _clean(_slope(_to_num(famaindustry), 8))
def cg_f082_sector_industry_tech_filter_core20_2nd_v021_signal(sector, industry, sicsector, sicindustry, famasector, famaindustry):
    return _clean(_diff(_to_num(sicsector), 4))
def cg_f082_sector_industry_tech_filter_core21_2nd_v022_signal(sector, industry, sicsector, sicindustry, famasector, famaindustry):
    return _clean(_diff(_to_num(sicindustry), 4))
def cg_f082_sector_industry_tech_filter_core22_2nd_v023_signal(sector, industry, sicsector, sicindustry, famasector, famaindustry):
    return _clean(_diff(_event_flag(sector), 4))
def cg_f082_sector_industry_tech_filter_core23_2nd_v024_signal(sector, industry, sicsector, sicindustry, famasector, famaindustry):
    return _clean(_diff(_event_flag(industry), 4))
def cg_f082_sector_industry_tech_filter_core24_2nd_v025_signal(sector, industry, sicsector, sicindustry, famasector, famaindustry):
    return _clean(_diff(_event_flag(famasector), 4))
def cg_f082_sector_industry_tech_filter_core25_2nd_v026_signal(sector, industry, sicsector, sicindustry, famasector, famaindustry):
    return _clean(_diff(_event_flag(famaindustry), 4))
def cg_f082_sector_industry_tech_filter_core26_2nd_v027_signal(sector, industry, sicsector, sicindustry, famasector, famaindustry):
    return _clean(_diff(_event_count(sector, 4), 4))
def cg_f082_sector_industry_tech_filter_core27_2nd_v028_signal(sector, industry, sicsector, sicindustry, famasector, famaindustry):
    return _clean(_diff(_event_rate(industry, 8), 4))
def cg_f082_sector_industry_tech_filter_core28_2nd_v029_signal(sector, industry, sicsector, sicindustry, famasector, famaindustry):
    return _clean(_diff(_to_num(famasector), 4))
def cg_f082_sector_industry_tech_filter_core29_2nd_v030_signal(sector, industry, sicsector, sicindustry, famasector, famaindustry):
    return _clean(_diff(_to_num(famaindustry), 4))
def cg_f082_sector_industry_tech_filter_core30_2nd_v031_signal(sector, industry, sicsector, sicindustry, famasector, famaindustry):
    return _clean(_z(_slope(_to_num(sicsector), 4), 8))
def cg_f082_sector_industry_tech_filter_core31_2nd_v032_signal(sector, industry, sicsector, sicindustry, famasector, famaindustry):
    return _clean(_z(_slope(_to_num(sicindustry), 4), 8))
def cg_f082_sector_industry_tech_filter_core32_2nd_v033_signal(sector, industry, sicsector, sicindustry, famasector, famaindustry):
    return _clean(_z(_slope(_event_flag(sector), 4), 8))
def cg_f082_sector_industry_tech_filter_core33_2nd_v034_signal(sector, industry, sicsector, sicindustry, famasector, famaindustry):
    return _clean(_z(_slope(_event_flag(industry), 4), 8))
def cg_f082_sector_industry_tech_filter_core34_2nd_v035_signal(sector, industry, sicsector, sicindustry, famasector, famaindustry):
    return _clean(_z(_slope(_event_flag(famasector), 4), 8))
def cg_f082_sector_industry_tech_filter_core35_2nd_v036_signal(sector, industry, sicsector, sicindustry, famasector, famaindustry):
    return _clean(_z(_slope(_event_flag(famaindustry), 4), 8))
def cg_f082_sector_industry_tech_filter_core36_2nd_v037_signal(sector, industry, sicsector, sicindustry, famasector, famaindustry):
    return _clean(_z(_slope(_event_count(sector, 4), 4), 8))
def cg_f082_sector_industry_tech_filter_core37_2nd_v038_signal(sector, industry, sicsector, sicindustry, famasector, famaindustry):
    return _clean(_z(_slope(_event_rate(industry, 8), 4), 8))
def cg_f082_sector_industry_tech_filter_core38_2nd_v039_signal(sector, industry, sicsector, sicindustry, famasector, famaindustry):
    return _clean(_z(_slope(_to_num(famasector), 4), 8))
def cg_f082_sector_industry_tech_filter_core39_2nd_v040_signal(sector, industry, sicsector, sicindustry, famasector, famaindustry):
    return _clean(_z(_slope(_to_num(famaindustry), 4), 8))
def cg_f082_sector_industry_tech_filter_core40_2nd_v041_signal(sector, industry, sicsector, sicindustry, famasector, famaindustry):
    return _clean(_z(_slope(_to_num(sicsector), 8), 12))
def cg_f082_sector_industry_tech_filter_core41_2nd_v042_signal(sector, industry, sicsector, sicindustry, famasector, famaindustry):
    return _clean(_z(_slope(_to_num(sicindustry), 8), 12))
def cg_f082_sector_industry_tech_filter_core42_2nd_v043_signal(sector, industry, sicsector, sicindustry, famasector, famaindustry):
    return _clean(_z(_slope(_event_flag(sector), 8), 12))
def cg_f082_sector_industry_tech_filter_core43_2nd_v044_signal(sector, industry, sicsector, sicindustry, famasector, famaindustry):
    return _clean(_z(_slope(_event_flag(industry), 8), 12))
def cg_f082_sector_industry_tech_filter_core44_2nd_v045_signal(sector, industry, sicsector, sicindustry, famasector, famaindustry):
    return _clean(_z(_slope(_event_flag(famasector), 8), 12))
def cg_f082_sector_industry_tech_filter_core45_2nd_v046_signal(sector, industry, sicsector, sicindustry, famasector, famaindustry):
    return _clean(_z(_slope(_event_flag(famaindustry), 8), 12))
def cg_f082_sector_industry_tech_filter_core46_2nd_v047_signal(sector, industry, sicsector, sicindustry, famasector, famaindustry):
    return _clean(_z(_slope(_event_count(sector, 4), 8), 12))
def cg_f082_sector_industry_tech_filter_core47_2nd_v048_signal(sector, industry, sicsector, sicindustry, famasector, famaindustry):
    return _clean(_z(_slope(_event_rate(industry, 8), 8), 12))
def cg_f082_sector_industry_tech_filter_core48_2nd_v049_signal(sector, industry, sicsector, sicindustry, famasector, famaindustry):
    return _clean(_z(_slope(_to_num(famasector), 8), 12))
def cg_f082_sector_industry_tech_filter_core49_2nd_v050_signal(sector, industry, sicsector, sicindustry, famasector, famaindustry):
    return _clean(_z(_slope(_to_num(famaindustry), 8), 12))
def cg_f082_sector_industry_tech_filter_core50_2nd_v051_signal(sector, industry, sicsector, sicindustry, famasector, famaindustry):
    return _clean(_z(_diff(_to_num(sicsector), 4), 8))
def cg_f082_sector_industry_tech_filter_core51_2nd_v052_signal(sector, industry, sicsector, sicindustry, famasector, famaindustry):
    return _clean(_z(_diff(_to_num(sicindustry), 4), 8))
def cg_f082_sector_industry_tech_filter_core52_2nd_v053_signal(sector, industry, sicsector, sicindustry, famasector, famaindustry):
    return _clean(_z(_diff(_event_flag(sector), 4), 8))
def cg_f082_sector_industry_tech_filter_core53_2nd_v054_signal(sector, industry, sicsector, sicindustry, famasector, famaindustry):
    return _clean(_z(_diff(_event_flag(industry), 4), 8))
def cg_f082_sector_industry_tech_filter_core54_2nd_v055_signal(sector, industry, sicsector, sicindustry, famasector, famaindustry):
    return _clean(_z(_diff(_event_flag(famasector), 4), 8))
def cg_f082_sector_industry_tech_filter_core55_2nd_v056_signal(sector, industry, sicsector, sicindustry, famasector, famaindustry):
    return _clean(_z(_diff(_event_flag(famaindustry), 4), 8))
def cg_f082_sector_industry_tech_filter_core56_2nd_v057_signal(sector, industry, sicsector, sicindustry, famasector, famaindustry):
    return _clean(_z(_diff(_event_count(sector, 4), 4), 8))
def cg_f082_sector_industry_tech_filter_core57_2nd_v058_signal(sector, industry, sicsector, sicindustry, famasector, famaindustry):
    return _clean(_z(_diff(_event_rate(industry, 8), 4), 8))
def cg_f082_sector_industry_tech_filter_core58_2nd_v059_signal(sector, industry, sicsector, sicindustry, famasector, famaindustry):
    return _clean(_z(_diff(_to_num(famasector), 4), 8))
def cg_f082_sector_industry_tech_filter_core59_2nd_v060_signal(sector, industry, sicsector, sicindustry, famasector, famaindustry):
    return _clean(_z(_diff(_to_num(famaindustry), 4), 8))
def cg_f082_sector_industry_tech_filter_core60_2nd_v061_signal(sector, industry, sicsector, sicindustry, famasector, famaindustry):
    return _clean(_rank(_slope(_to_num(sicsector), 4), 12))
def cg_f082_sector_industry_tech_filter_core61_2nd_v062_signal(sector, industry, sicsector, sicindustry, famasector, famaindustry):
    return _clean(_rank(_slope(_to_num(sicindustry), 4), 12))
def cg_f082_sector_industry_tech_filter_core62_2nd_v063_signal(sector, industry, sicsector, sicindustry, famasector, famaindustry):
    return _clean(_rank(_slope(_event_flag(sector), 4), 12))
def cg_f082_sector_industry_tech_filter_core63_2nd_v064_signal(sector, industry, sicsector, sicindustry, famasector, famaindustry):
    return _clean(_rank(_slope(_event_flag(industry), 4), 12))
def cg_f082_sector_industry_tech_filter_core64_2nd_v065_signal(sector, industry, sicsector, sicindustry, famasector, famaindustry):
    return _clean(_rank(_slope(_event_flag(famasector), 4), 12))
def cg_f082_sector_industry_tech_filter_core65_2nd_v066_signal(sector, industry, sicsector, sicindustry, famasector, famaindustry):
    return _clean(_rank(_slope(_event_flag(famaindustry), 4), 12))
def cg_f082_sector_industry_tech_filter_core66_2nd_v067_signal(sector, industry, sicsector, sicindustry, famasector, famaindustry):
    return _clean(_rank(_slope(_event_count(sector, 4), 4), 12))
def cg_f082_sector_industry_tech_filter_core67_2nd_v068_signal(sector, industry, sicsector, sicindustry, famasector, famaindustry):
    return _clean(_rank(_slope(_event_rate(industry, 8), 4), 12))
def cg_f082_sector_industry_tech_filter_core68_2nd_v069_signal(sector, industry, sicsector, sicindustry, famasector, famaindustry):
    return _clean(_rank(_slope(_to_num(famasector), 4), 12))
def cg_f082_sector_industry_tech_filter_core69_2nd_v070_signal(sector, industry, sicsector, sicindustry, famasector, famaindustry):
    return _clean(_rank(_slope(_to_num(famaindustry), 4), 12))
def cg_f082_sector_industry_tech_filter_core70_2nd_v071_signal(sector, industry, sicsector, sicindustry, famasector, famaindustry):
    return _clean(_rank(_diff(_to_num(sicsector), 4), 12))
def cg_f082_sector_industry_tech_filter_core71_2nd_v072_signal(sector, industry, sicsector, sicindustry, famasector, famaindustry):
    return _clean(_rank(_diff(_to_num(sicindustry), 4), 12))
def cg_f082_sector_industry_tech_filter_core72_2nd_v073_signal(sector, industry, sicsector, sicindustry, famasector, famaindustry):
    return _clean(_rank(_diff(_event_flag(sector), 4), 12))
def cg_f082_sector_industry_tech_filter_core73_2nd_v074_signal(sector, industry, sicsector, sicindustry, famasector, famaindustry):
    return _clean(_rank(_diff(_event_flag(industry), 4), 12))
def cg_f082_sector_industry_tech_filter_core74_2nd_v075_signal(sector, industry, sicsector, sicindustry, famasector, famaindustry):
    return _clean(_rank(_diff(_event_flag(famasector), 4), 12))
def cg_f082_sector_industry_tech_filter_core75_2nd_v076_signal(sector, industry, sicsector, sicindustry, famasector, famaindustry):
    return _clean(_rank(_diff(_event_flag(famaindustry), 4), 12))
def cg_f082_sector_industry_tech_filter_core76_2nd_v077_signal(sector, industry, sicsector, sicindustry, famasector, famaindustry):
    return _clean(_rank(_diff(_event_count(sector, 4), 4), 12))
def cg_f082_sector_industry_tech_filter_core77_2nd_v078_signal(sector, industry, sicsector, sicindustry, famasector, famaindustry):
    return _clean(_rank(_diff(_event_rate(industry, 8), 4), 12))
def cg_f082_sector_industry_tech_filter_core78_2nd_v079_signal(sector, industry, sicsector, sicindustry, famasector, famaindustry):
    return _clean(_rank(_diff(_to_num(famasector), 4), 12))
def cg_f082_sector_industry_tech_filter_core79_2nd_v080_signal(sector, industry, sicsector, sicindustry, famasector, famaindustry):
    return _clean(_rank(_diff(_to_num(famaindustry), 4), 12))
def cg_f082_sector_industry_tech_filter_core80_2nd_v081_signal(sector, industry, sicsector, sicindustry, famasector, famaindustry):
    return _clean(_mean(_slope(_to_num(sicsector), 4), 4))
def cg_f082_sector_industry_tech_filter_core81_2nd_v082_signal(sector, industry, sicsector, sicindustry, famasector, famaindustry):
    return _clean(_mean(_slope(_to_num(sicindustry), 4), 4))
def cg_f082_sector_industry_tech_filter_core82_2nd_v083_signal(sector, industry, sicsector, sicindustry, famasector, famaindustry):
    return _clean(_mean(_slope(_event_flag(sector), 4), 4))
def cg_f082_sector_industry_tech_filter_core83_2nd_v084_signal(sector, industry, sicsector, sicindustry, famasector, famaindustry):
    return _clean(_mean(_slope(_event_flag(industry), 4), 4))
def cg_f082_sector_industry_tech_filter_core84_2nd_v085_signal(sector, industry, sicsector, sicindustry, famasector, famaindustry):
    return _clean(_mean(_slope(_event_flag(famasector), 4), 4))
def cg_f082_sector_industry_tech_filter_core85_2nd_v086_signal(sector, industry, sicsector, sicindustry, famasector, famaindustry):
    return _clean(_mean(_slope(_event_flag(famaindustry), 4), 4))
def cg_f082_sector_industry_tech_filter_core86_2nd_v087_signal(sector, industry, sicsector, sicindustry, famasector, famaindustry):
    return _clean(_mean(_slope(_event_count(sector, 4), 4), 4))
def cg_f082_sector_industry_tech_filter_core87_2nd_v088_signal(sector, industry, sicsector, sicindustry, famasector, famaindustry):
    return _clean(_mean(_slope(_event_rate(industry, 8), 4), 4))
def cg_f082_sector_industry_tech_filter_core88_2nd_v089_signal(sector, industry, sicsector, sicindustry, famasector, famaindustry):
    return _clean(_mean(_slope(_to_num(famasector), 4), 4))
def cg_f082_sector_industry_tech_filter_core89_2nd_v090_signal(sector, industry, sicsector, sicindustry, famasector, famaindustry):
    return _clean(_mean(_slope(_to_num(famaindustry), 4), 4))
def cg_f082_sector_industry_tech_filter_core90_2nd_v091_signal(sector, industry, sicsector, sicindustry, famasector, famaindustry):
    return _clean(_mean(_diff(_to_num(sicsector), 4), 4))
def cg_f082_sector_industry_tech_filter_core91_2nd_v092_signal(sector, industry, sicsector, sicindustry, famasector, famaindustry):
    return _clean(_mean(_diff(_to_num(sicindustry), 4), 4))
def cg_f082_sector_industry_tech_filter_core92_2nd_v093_signal(sector, industry, sicsector, sicindustry, famasector, famaindustry):
    return _clean(_mean(_diff(_event_flag(sector), 4), 4))
def cg_f082_sector_industry_tech_filter_core93_2nd_v094_signal(sector, industry, sicsector, sicindustry, famasector, famaindustry):
    return _clean(_mean(_diff(_event_flag(industry), 4), 4))
def cg_f082_sector_industry_tech_filter_core94_2nd_v095_signal(sector, industry, sicsector, sicindustry, famasector, famaindustry):
    return _clean(_mean(_diff(_event_flag(famasector), 4), 4))
def cg_f082_sector_industry_tech_filter_core95_2nd_v096_signal(sector, industry, sicsector, sicindustry, famasector, famaindustry):
    return _clean(_mean(_diff(_event_flag(famaindustry), 4), 4))
def cg_f082_sector_industry_tech_filter_core96_2nd_v097_signal(sector, industry, sicsector, sicindustry, famasector, famaindustry):
    return _clean(_mean(_diff(_event_count(sector, 4), 4), 4))
def cg_f082_sector_industry_tech_filter_core97_2nd_v098_signal(sector, industry, sicsector, sicindustry, famasector, famaindustry):
    return _clean(_mean(_diff(_event_rate(industry, 8), 4), 4))
def cg_f082_sector_industry_tech_filter_core98_2nd_v099_signal(sector, industry, sicsector, sicindustry, famasector, famaindustry):
    return _clean(_mean(_diff(_to_num(famasector), 4), 4))
def cg_f082_sector_industry_tech_filter_core99_2nd_v100_signal(sector, industry, sicsector, sicindustry, famasector, famaindustry):
    return _clean(_mean(_diff(_to_num(famaindustry), 4), 4))
def cg_f082_sector_industry_tech_filter_core100_2nd_v101_signal(sector, industry, sicsector, sicindustry, famasector, famaindustry):
    return _clean(_slope(_mean(_to_num(sicsector), 4), 4))
def cg_f082_sector_industry_tech_filter_core101_2nd_v102_signal(sector, industry, sicsector, sicindustry, famasector, famaindustry):
    return _clean(_slope(_mean(_to_num(sicindustry), 4), 4))
def cg_f082_sector_industry_tech_filter_core102_2nd_v103_signal(sector, industry, sicsector, sicindustry, famasector, famaindustry):
    return _clean(_slope(_mean(_event_flag(sector), 4), 4))
def cg_f082_sector_industry_tech_filter_core103_2nd_v104_signal(sector, industry, sicsector, sicindustry, famasector, famaindustry):
    return _clean(_slope(_mean(_event_flag(industry), 4), 4))
def cg_f082_sector_industry_tech_filter_core104_2nd_v105_signal(sector, industry, sicsector, sicindustry, famasector, famaindustry):
    return _clean(_slope(_mean(_event_flag(famasector), 4), 4))
def cg_f082_sector_industry_tech_filter_core105_2nd_v106_signal(sector, industry, sicsector, sicindustry, famasector, famaindustry):
    return _clean(_slope(_mean(_event_flag(famaindustry), 4), 4))
def cg_f082_sector_industry_tech_filter_core106_2nd_v107_signal(sector, industry, sicsector, sicindustry, famasector, famaindustry):
    return _clean(_slope(_mean(_event_count(sector, 4), 4), 4))
def cg_f082_sector_industry_tech_filter_core107_2nd_v108_signal(sector, industry, sicsector, sicindustry, famasector, famaindustry):
    return _clean(_slope(_mean(_event_rate(industry, 8), 4), 4))
def cg_f082_sector_industry_tech_filter_core108_2nd_v109_signal(sector, industry, sicsector, sicindustry, famasector, famaindustry):
    return _clean(_slope(_mean(_to_num(famasector), 4), 4))
def cg_f082_sector_industry_tech_filter_core109_2nd_v110_signal(sector, industry, sicsector, sicindustry, famasector, famaindustry):
    return _clean(_slope(_mean(_to_num(famaindustry), 4), 4))
def cg_f082_sector_industry_tech_filter_core110_2nd_v111_signal(sector, industry, sicsector, sicindustry, famasector, famaindustry):
    return _clean(_slope(_mean(_to_num(sicsector), 8), 8))
def cg_f082_sector_industry_tech_filter_core111_2nd_v112_signal(sector, industry, sicsector, sicindustry, famasector, famaindustry):
    return _clean(_slope(_mean(_to_num(sicindustry), 8), 8))
def cg_f082_sector_industry_tech_filter_core112_2nd_v113_signal(sector, industry, sicsector, sicindustry, famasector, famaindustry):
    return _clean(_slope(_mean(_event_flag(sector), 8), 8))
def cg_f082_sector_industry_tech_filter_core113_2nd_v114_signal(sector, industry, sicsector, sicindustry, famasector, famaindustry):
    return _clean(_slope(_mean(_event_flag(industry), 8), 8))
def cg_f082_sector_industry_tech_filter_core114_2nd_v115_signal(sector, industry, sicsector, sicindustry, famasector, famaindustry):
    return _clean(_slope(_mean(_event_flag(famasector), 8), 8))
def cg_f082_sector_industry_tech_filter_core115_2nd_v116_signal(sector, industry, sicsector, sicindustry, famasector, famaindustry):
    return _clean(_slope(_mean(_event_flag(famaindustry), 8), 8))
def cg_f082_sector_industry_tech_filter_core116_2nd_v117_signal(sector, industry, sicsector, sicindustry, famasector, famaindustry):
    return _clean(_slope(_mean(_event_count(sector, 4), 8), 8))
def cg_f082_sector_industry_tech_filter_core117_2nd_v118_signal(sector, industry, sicsector, sicindustry, famasector, famaindustry):
    return _clean(_slope(_mean(_event_rate(industry, 8), 8), 8))
def cg_f082_sector_industry_tech_filter_core118_2nd_v119_signal(sector, industry, sicsector, sicindustry, famasector, famaindustry):
    return _clean(_slope(_mean(_to_num(famasector), 8), 8))
def cg_f082_sector_industry_tech_filter_core119_2nd_v120_signal(sector, industry, sicsector, sicindustry, famasector, famaindustry):
    return _clean(_slope(_mean(_to_num(famaindustry), 8), 8))
def cg_f082_sector_industry_tech_filter_core120_2nd_v121_signal(sector, industry, sicsector, sicindustry, famasector, famaindustry):
    return _clean(_diff(_mean(_to_num(sicsector), 4), 4))
def cg_f082_sector_industry_tech_filter_core121_2nd_v122_signal(sector, industry, sicsector, sicindustry, famasector, famaindustry):
    return _clean(_diff(_mean(_to_num(sicindustry), 4), 4))
def cg_f082_sector_industry_tech_filter_core122_2nd_v123_signal(sector, industry, sicsector, sicindustry, famasector, famaindustry):
    return _clean(_diff(_mean(_event_flag(sector), 4), 4))
def cg_f082_sector_industry_tech_filter_core123_2nd_v124_signal(sector, industry, sicsector, sicindustry, famasector, famaindustry):
    return _clean(_diff(_mean(_event_flag(industry), 4), 4))
def cg_f082_sector_industry_tech_filter_core124_2nd_v125_signal(sector, industry, sicsector, sicindustry, famasector, famaindustry):
    return _clean(_diff(_mean(_event_flag(famasector), 4), 4))
def cg_f082_sector_industry_tech_filter_core125_2nd_v126_signal(sector, industry, sicsector, sicindustry, famasector, famaindustry):
    return _clean(_diff(_mean(_event_flag(famaindustry), 4), 4))
def cg_f082_sector_industry_tech_filter_core126_2nd_v127_signal(sector, industry, sicsector, sicindustry, famasector, famaindustry):
    return _clean(_diff(_mean(_event_count(sector, 4), 4), 4))
def cg_f082_sector_industry_tech_filter_core127_2nd_v128_signal(sector, industry, sicsector, sicindustry, famasector, famaindustry):
    return _clean(_diff(_mean(_event_rate(industry, 8), 4), 4))
def cg_f082_sector_industry_tech_filter_core128_2nd_v129_signal(sector, industry, sicsector, sicindustry, famasector, famaindustry):
    return _clean(_diff(_mean(_to_num(famasector), 4), 4))
def cg_f082_sector_industry_tech_filter_core129_2nd_v130_signal(sector, industry, sicsector, sicindustry, famasector, famaindustry):
    return _clean(_diff(_mean(_to_num(famaindustry), 4), 4))
def cg_f082_sector_industry_tech_filter_core130_2nd_v131_signal(sector, industry, sicsector, sicindustry, famasector, famaindustry):
    return _clean(_z(_diff(_mean(_to_num(sicsector), 4), 4), 8))
def cg_f082_sector_industry_tech_filter_core131_2nd_v132_signal(sector, industry, sicsector, sicindustry, famasector, famaindustry):
    return _clean(_z(_diff(_mean(_to_num(sicindustry), 4), 4), 8))
def cg_f082_sector_industry_tech_filter_core132_2nd_v133_signal(sector, industry, sicsector, sicindustry, famasector, famaindustry):
    return _clean(_z(_diff(_mean(_event_flag(sector), 4), 4), 8))
def cg_f082_sector_industry_tech_filter_core133_2nd_v134_signal(sector, industry, sicsector, sicindustry, famasector, famaindustry):
    return _clean(_z(_diff(_mean(_event_flag(industry), 4), 4), 8))
def cg_f082_sector_industry_tech_filter_core134_2nd_v135_signal(sector, industry, sicsector, sicindustry, famasector, famaindustry):
    return _clean(_z(_diff(_mean(_event_flag(famasector), 4), 4), 8))
def cg_f082_sector_industry_tech_filter_core135_2nd_v136_signal(sector, industry, sicsector, sicindustry, famasector, famaindustry):
    return _clean(_z(_diff(_mean(_event_flag(famaindustry), 4), 4), 8))
def cg_f082_sector_industry_tech_filter_core136_2nd_v137_signal(sector, industry, sicsector, sicindustry, famasector, famaindustry):
    return _clean(_z(_diff(_mean(_event_count(sector, 4), 4), 4), 8))
def cg_f082_sector_industry_tech_filter_core137_2nd_v138_signal(sector, industry, sicsector, sicindustry, famasector, famaindustry):
    return _clean(_z(_diff(_mean(_event_rate(industry, 8), 4), 4), 8))
def cg_f082_sector_industry_tech_filter_core138_2nd_v139_signal(sector, industry, sicsector, sicindustry, famasector, famaindustry):
    return _clean(_z(_diff(_mean(_to_num(famasector), 4), 4), 8))
def cg_f082_sector_industry_tech_filter_core139_2nd_v140_signal(sector, industry, sicsector, sicindustry, famasector, famaindustry):
    return _clean(_z(_diff(_mean(_to_num(famaindustry), 4), 4), 8))
def cg_f082_sector_industry_tech_filter_core140_2nd_v141_signal(sector, industry, sicsector, sicindustry, famasector, famaindustry):
    return _clean(_rank(_slope(_mean(_to_num(sicsector), 4), 4), 12))
def cg_f082_sector_industry_tech_filter_core141_2nd_v142_signal(sector, industry, sicsector, sicindustry, famasector, famaindustry):
    return _clean(_rank(_slope(_mean(_to_num(sicindustry), 4), 4), 12))
def cg_f082_sector_industry_tech_filter_core142_2nd_v143_signal(sector, industry, sicsector, sicindustry, famasector, famaindustry):
    return _clean(_rank(_slope(_mean(_event_flag(sector), 4), 4), 12))
def cg_f082_sector_industry_tech_filter_core143_2nd_v144_signal(sector, industry, sicsector, sicindustry, famasector, famaindustry):
    return _clean(_rank(_slope(_mean(_event_flag(industry), 4), 4), 12))
def cg_f082_sector_industry_tech_filter_core144_2nd_v145_signal(sector, industry, sicsector, sicindustry, famasector, famaindustry):
    return _clean(_rank(_slope(_mean(_event_flag(famasector), 4), 4), 12))
def cg_f082_sector_industry_tech_filter_core145_2nd_v146_signal(sector, industry, sicsector, sicindustry, famasector, famaindustry):
    return _clean(_rank(_slope(_mean(_event_flag(famaindustry), 4), 4), 12))
def cg_f082_sector_industry_tech_filter_core146_2nd_v147_signal(sector, industry, sicsector, sicindustry, famasector, famaindustry):
    return _clean(_rank(_slope(_mean(_event_count(sector, 4), 4), 4), 12))
def cg_f082_sector_industry_tech_filter_core147_2nd_v148_signal(sector, industry, sicsector, sicindustry, famasector, famaindustry):
    return _clean(_rank(_slope(_mean(_event_rate(industry, 8), 4), 4), 12))
def cg_f082_sector_industry_tech_filter_core148_2nd_v149_signal(sector, industry, sicsector, sicindustry, famasector, famaindustry):
    return _clean(_rank(_slope(_mean(_to_num(famasector), 4), 4), 12))
def cg_f082_sector_industry_tech_filter_core149_2nd_v150_signal(sector, industry, sicsector, sicindustry, famasector, famaindustry):
    return _clean(_rank(_slope(_mean(_to_num(famaindustry), 4), 4), 12))