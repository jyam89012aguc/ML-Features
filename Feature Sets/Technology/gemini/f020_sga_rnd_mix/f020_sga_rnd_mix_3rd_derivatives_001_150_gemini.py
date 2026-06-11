import numpy as np
import pandas as pd
from technology_helpers import _to_num, _clean, _safe_div, _log, _mean, _std, _sum, _min, _max, _z, _pct_change, _diff, _rank, _skew, _kurt, _autocorr, _corr, _slope, _ewm, _event_flag, _event_count, _event_rate, _clip_z

def cg_f020_sga_rnd_mix_core00_3rd_v001_signal(sgna, rnd, opex):
    return _clean(_diff(_diff(sgna, 4), 4))
def cg_f020_sga_rnd_mix_core01_3rd_v002_signal(sgna, rnd, opex):
    return _clean(_diff(_diff(rnd, 4), 4))
def cg_f020_sga_rnd_mix_core02_3rd_v003_signal(sgna, rnd, opex):
    return _clean(_diff(_diff(opex, 4), 4))
def cg_f020_sga_rnd_mix_core03_3rd_v004_signal(sgna, rnd, opex):
    return _clean(_diff(_diff(_safe_div(rnd, sgna.abs() + 1.0), 4), 4))
def cg_f020_sga_rnd_mix_core04_3rd_v005_signal(sgna, rnd, opex):
    return _clean(_diff(_diff(_safe_div(rnd, opex), 4), 4))
def cg_f020_sga_rnd_mix_core05_3rd_v006_signal(sgna, rnd, opex):
    return _clean(_diff(_diff(_safe_div(sgna, opex), 4), 4))
def cg_f020_sga_rnd_mix_core06_3rd_v007_signal(sgna, rnd, opex):
    return _clean(_diff(_diff(sgna + rnd, 4), 4))
def cg_f020_sga_rnd_mix_core07_3rd_v008_signal(sgna, rnd, opex):
    return _clean(_diff(_diff(_safe_div(sgna + rnd, opex), 4), 4))
def cg_f020_sga_rnd_mix_core08_3rd_v009_signal(sgna, rnd, opex):
    return _clean(_diff(_diff(_log(sgna.abs() + 1.0), 4), 4))
def cg_f020_sga_rnd_mix_core09_3rd_v010_signal(sgna, rnd, opex):
    return _clean(_diff(_diff(_log(rnd.abs() + 1.0), 4), 4))
def cg_f020_sga_rnd_mix_core10_3rd_v011_signal(sgna, rnd, opex):
    return _clean(_slope(_diff(sgna, 4), 8))
def cg_f020_sga_rnd_mix_core11_3rd_v012_signal(sgna, rnd, opex):
    return _clean(_slope(_diff(rnd, 4), 8))
def cg_f020_sga_rnd_mix_core12_3rd_v013_signal(sgna, rnd, opex):
    return _clean(_slope(_diff(opex, 4), 8))
def cg_f020_sga_rnd_mix_core13_3rd_v014_signal(sgna, rnd, opex):
    return _clean(_slope(_diff(_safe_div(rnd, sgna.abs() + 1.0), 4), 8))
def cg_f020_sga_rnd_mix_core14_3rd_v015_signal(sgna, rnd, opex):
    return _clean(_slope(_diff(_safe_div(rnd, opex), 4), 8))
def cg_f020_sga_rnd_mix_core15_3rd_v016_signal(sgna, rnd, opex):
    return _clean(_slope(_diff(_safe_div(sgna, opex), 4), 8))
def cg_f020_sga_rnd_mix_core16_3rd_v017_signal(sgna, rnd, opex):
    return _clean(_slope(_diff(sgna + rnd, 4), 8))
def cg_f020_sga_rnd_mix_core17_3rd_v018_signal(sgna, rnd, opex):
    return _clean(_slope(_diff(_safe_div(sgna + rnd, opex), 4), 8))
def cg_f020_sga_rnd_mix_core18_3rd_v019_signal(sgna, rnd, opex):
    return _clean(_slope(_diff(_log(sgna.abs() + 1.0), 4), 8))
def cg_f020_sga_rnd_mix_core19_3rd_v020_signal(sgna, rnd, opex):
    return _clean(_slope(_diff(_log(rnd.abs() + 1.0), 4), 8))
def cg_f020_sga_rnd_mix_core20_3rd_v021_signal(sgna, rnd, opex):
    return _clean(_diff(_slope(sgna, 4), 4))
def cg_f020_sga_rnd_mix_core21_3rd_v022_signal(sgna, rnd, opex):
    return _clean(_diff(_slope(rnd, 4), 4))
def cg_f020_sga_rnd_mix_core22_3rd_v023_signal(sgna, rnd, opex):
    return _clean(_diff(_slope(opex, 4), 4))
def cg_f020_sga_rnd_mix_core23_3rd_v024_signal(sgna, rnd, opex):
    return _clean(_diff(_slope(_safe_div(rnd, sgna.abs() + 1.0), 4), 4))
def cg_f020_sga_rnd_mix_core24_3rd_v025_signal(sgna, rnd, opex):
    return _clean(_diff(_slope(_safe_div(rnd, opex), 4), 4))
def cg_f020_sga_rnd_mix_core25_3rd_v026_signal(sgna, rnd, opex):
    return _clean(_diff(_slope(_safe_div(sgna, opex), 4), 4))
def cg_f020_sga_rnd_mix_core26_3rd_v027_signal(sgna, rnd, opex):
    return _clean(_diff(_slope(sgna + rnd, 4), 4))
def cg_f020_sga_rnd_mix_core27_3rd_v028_signal(sgna, rnd, opex):
    return _clean(_diff(_slope(_safe_div(sgna + rnd, opex), 4), 4))
def cg_f020_sga_rnd_mix_core28_3rd_v029_signal(sgna, rnd, opex):
    return _clean(_diff(_slope(_log(sgna.abs() + 1.0), 4), 4))
def cg_f020_sga_rnd_mix_core29_3rd_v030_signal(sgna, rnd, opex):
    return _clean(_diff(_slope(_log(rnd.abs() + 1.0), 4), 4))
def cg_f020_sga_rnd_mix_core30_3rd_v031_signal(sgna, rnd, opex):
    return _clean(_z(_diff(_diff(sgna, 4), 4), 8))
def cg_f020_sga_rnd_mix_core31_3rd_v032_signal(sgna, rnd, opex):
    return _clean(_z(_diff(_diff(rnd, 4), 4), 8))
def cg_f020_sga_rnd_mix_core32_3rd_v033_signal(sgna, rnd, opex):
    return _clean(_z(_diff(_diff(opex, 4), 4), 8))
def cg_f020_sga_rnd_mix_core33_3rd_v034_signal(sgna, rnd, opex):
    return _clean(_z(_diff(_diff(_safe_div(rnd, sgna.abs() + 1.0), 4), 4), 8))
def cg_f020_sga_rnd_mix_core34_3rd_v035_signal(sgna, rnd, opex):
    return _clean(_z(_diff(_diff(_safe_div(rnd, opex), 4), 4), 8))
def cg_f020_sga_rnd_mix_core35_3rd_v036_signal(sgna, rnd, opex):
    return _clean(_z(_diff(_diff(_safe_div(sgna, opex), 4), 4), 8))
def cg_f020_sga_rnd_mix_core36_3rd_v037_signal(sgna, rnd, opex):
    return _clean(_z(_diff(_diff(sgna + rnd, 4), 4), 8))
def cg_f020_sga_rnd_mix_core37_3rd_v038_signal(sgna, rnd, opex):
    return _clean(_z(_diff(_diff(_safe_div(sgna + rnd, opex), 4), 4), 8))
def cg_f020_sga_rnd_mix_core38_3rd_v039_signal(sgna, rnd, opex):
    return _clean(_z(_diff(_diff(_log(sgna.abs() + 1.0), 4), 4), 8))
def cg_f020_sga_rnd_mix_core39_3rd_v040_signal(sgna, rnd, opex):
    return _clean(_z(_diff(_diff(_log(rnd.abs() + 1.0), 4), 4), 8))
def cg_f020_sga_rnd_mix_core40_3rd_v041_signal(sgna, rnd, opex):
    return _clean(_z(_slope(_diff(sgna, 4), 8), 12))
def cg_f020_sga_rnd_mix_core41_3rd_v042_signal(sgna, rnd, opex):
    return _clean(_z(_slope(_diff(rnd, 4), 8), 12))
def cg_f020_sga_rnd_mix_core42_3rd_v043_signal(sgna, rnd, opex):
    return _clean(_z(_slope(_diff(opex, 4), 8), 12))
def cg_f020_sga_rnd_mix_core43_3rd_v044_signal(sgna, rnd, opex):
    return _clean(_z(_slope(_diff(_safe_div(rnd, sgna.abs() + 1.0), 4), 8), 12))
def cg_f020_sga_rnd_mix_core44_3rd_v045_signal(sgna, rnd, opex):
    return _clean(_z(_slope(_diff(_safe_div(rnd, opex), 4), 8), 12))
def cg_f020_sga_rnd_mix_core45_3rd_v046_signal(sgna, rnd, opex):
    return _clean(_z(_slope(_diff(_safe_div(sgna, opex), 4), 8), 12))
def cg_f020_sga_rnd_mix_core46_3rd_v047_signal(sgna, rnd, opex):
    return _clean(_z(_slope(_diff(sgna + rnd, 4), 8), 12))
def cg_f020_sga_rnd_mix_core47_3rd_v048_signal(sgna, rnd, opex):
    return _clean(_z(_slope(_diff(_safe_div(sgna + rnd, opex), 4), 8), 12))
def cg_f020_sga_rnd_mix_core48_3rd_v049_signal(sgna, rnd, opex):
    return _clean(_z(_slope(_diff(_log(sgna.abs() + 1.0), 4), 8), 12))
def cg_f020_sga_rnd_mix_core49_3rd_v050_signal(sgna, rnd, opex):
    return _clean(_z(_slope(_diff(_log(rnd.abs() + 1.0), 4), 8), 12))
def cg_f020_sga_rnd_mix_core50_3rd_v051_signal(sgna, rnd, opex):
    return _clean(_z(_diff(_slope(sgna, 4), 4), 8))
def cg_f020_sga_rnd_mix_core51_3rd_v052_signal(sgna, rnd, opex):
    return _clean(_z(_diff(_slope(rnd, 4), 4), 8))
def cg_f020_sga_rnd_mix_core52_3rd_v053_signal(sgna, rnd, opex):
    return _clean(_z(_diff(_slope(opex, 4), 4), 8))
def cg_f020_sga_rnd_mix_core53_3rd_v054_signal(sgna, rnd, opex):
    return _clean(_z(_diff(_slope(_safe_div(rnd, sgna.abs() + 1.0), 4), 4), 8))
def cg_f020_sga_rnd_mix_core54_3rd_v055_signal(sgna, rnd, opex):
    return _clean(_z(_diff(_slope(_safe_div(rnd, opex), 4), 4), 8))
def cg_f020_sga_rnd_mix_core55_3rd_v056_signal(sgna, rnd, opex):
    return _clean(_z(_diff(_slope(_safe_div(sgna, opex), 4), 4), 8))
def cg_f020_sga_rnd_mix_core56_3rd_v057_signal(sgna, rnd, opex):
    return _clean(_z(_diff(_slope(sgna + rnd, 4), 4), 8))
def cg_f020_sga_rnd_mix_core57_3rd_v058_signal(sgna, rnd, opex):
    return _clean(_z(_diff(_slope(_safe_div(sgna + rnd, opex), 4), 4), 8))
def cg_f020_sga_rnd_mix_core58_3rd_v059_signal(sgna, rnd, opex):
    return _clean(_z(_diff(_slope(_log(sgna.abs() + 1.0), 4), 4), 8))
def cg_f020_sga_rnd_mix_core59_3rd_v060_signal(sgna, rnd, opex):
    return _clean(_z(_diff(_slope(_log(rnd.abs() + 1.0), 4), 4), 8))
def cg_f020_sga_rnd_mix_core60_3rd_v061_signal(sgna, rnd, opex):
    return _clean(_rank(_diff(_diff(sgna, 4), 4), 12))
def cg_f020_sga_rnd_mix_core61_3rd_v062_signal(sgna, rnd, opex):
    return _clean(_rank(_diff(_diff(rnd, 4), 4), 12))
def cg_f020_sga_rnd_mix_core62_3rd_v063_signal(sgna, rnd, opex):
    return _clean(_rank(_diff(_diff(opex, 4), 4), 12))
def cg_f020_sga_rnd_mix_core63_3rd_v064_signal(sgna, rnd, opex):
    return _clean(_rank(_diff(_diff(_safe_div(rnd, sgna.abs() + 1.0), 4), 4), 12))
def cg_f020_sga_rnd_mix_core64_3rd_v065_signal(sgna, rnd, opex):
    return _clean(_rank(_diff(_diff(_safe_div(rnd, opex), 4), 4), 12))
def cg_f020_sga_rnd_mix_core65_3rd_v066_signal(sgna, rnd, opex):
    return _clean(_rank(_diff(_diff(_safe_div(sgna, opex), 4), 4), 12))
def cg_f020_sga_rnd_mix_core66_3rd_v067_signal(sgna, rnd, opex):
    return _clean(_rank(_diff(_diff(sgna + rnd, 4), 4), 12))
def cg_f020_sga_rnd_mix_core67_3rd_v068_signal(sgna, rnd, opex):
    return _clean(_rank(_diff(_diff(_safe_div(sgna + rnd, opex), 4), 4), 12))
def cg_f020_sga_rnd_mix_core68_3rd_v069_signal(sgna, rnd, opex):
    return _clean(_rank(_diff(_diff(_log(sgna.abs() + 1.0), 4), 4), 12))
def cg_f020_sga_rnd_mix_core69_3rd_v070_signal(sgna, rnd, opex):
    return _clean(_rank(_diff(_diff(_log(rnd.abs() + 1.0), 4), 4), 12))
def cg_f020_sga_rnd_mix_core70_3rd_v071_signal(sgna, rnd, opex):
    return _clean(_rank(_slope(_diff(sgna, 4), 8), 12))
def cg_f020_sga_rnd_mix_core71_3rd_v072_signal(sgna, rnd, opex):
    return _clean(_rank(_slope(_diff(rnd, 4), 8), 12))
def cg_f020_sga_rnd_mix_core72_3rd_v073_signal(sgna, rnd, opex):
    return _clean(_rank(_slope(_diff(opex, 4), 8), 12))
def cg_f020_sga_rnd_mix_core73_3rd_v074_signal(sgna, rnd, opex):
    return _clean(_rank(_slope(_diff(_safe_div(rnd, sgna.abs() + 1.0), 4), 8), 12))
def cg_f020_sga_rnd_mix_core74_3rd_v075_signal(sgna, rnd, opex):
    return _clean(_rank(_slope(_diff(_safe_div(rnd, opex), 4), 8), 12))
def cg_f020_sga_rnd_mix_core75_3rd_v076_signal(sgna, rnd, opex):
    return _clean(_rank(_slope(_diff(_safe_div(sgna, opex), 4), 8), 12))
def cg_f020_sga_rnd_mix_core76_3rd_v077_signal(sgna, rnd, opex):
    return _clean(_rank(_slope(_diff(sgna + rnd, 4), 8), 12))
def cg_f020_sga_rnd_mix_core77_3rd_v078_signal(sgna, rnd, opex):
    return _clean(_rank(_slope(_diff(_safe_div(sgna + rnd, opex), 4), 8), 12))
def cg_f020_sga_rnd_mix_core78_3rd_v079_signal(sgna, rnd, opex):
    return _clean(_rank(_slope(_diff(_log(sgna.abs() + 1.0), 4), 8), 12))
def cg_f020_sga_rnd_mix_core79_3rd_v080_signal(sgna, rnd, opex):
    return _clean(_rank(_slope(_diff(_log(rnd.abs() + 1.0), 4), 8), 12))
def cg_f020_sga_rnd_mix_core80_3rd_v081_signal(sgna, rnd, opex):
    return _clean(_rank(_diff(_slope(sgna, 4), 4), 12))
def cg_f020_sga_rnd_mix_core81_3rd_v082_signal(sgna, rnd, opex):
    return _clean(_rank(_diff(_slope(rnd, 4), 4), 12))
def cg_f020_sga_rnd_mix_core82_3rd_v083_signal(sgna, rnd, opex):
    return _clean(_rank(_diff(_slope(opex, 4), 4), 12))
def cg_f020_sga_rnd_mix_core83_3rd_v084_signal(sgna, rnd, opex):
    return _clean(_rank(_diff(_slope(_safe_div(rnd, sgna.abs() + 1.0), 4), 4), 12))
def cg_f020_sga_rnd_mix_core84_3rd_v085_signal(sgna, rnd, opex):
    return _clean(_rank(_diff(_slope(_safe_div(rnd, opex), 4), 4), 12))
def cg_f020_sga_rnd_mix_core85_3rd_v086_signal(sgna, rnd, opex):
    return _clean(_rank(_diff(_slope(_safe_div(sgna, opex), 4), 4), 12))
def cg_f020_sga_rnd_mix_core86_3rd_v087_signal(sgna, rnd, opex):
    return _clean(_rank(_diff(_slope(sgna + rnd, 4), 4), 12))
def cg_f020_sga_rnd_mix_core87_3rd_v088_signal(sgna, rnd, opex):
    return _clean(_rank(_diff(_slope(_safe_div(sgna + rnd, opex), 4), 4), 12))
def cg_f020_sga_rnd_mix_core88_3rd_v089_signal(sgna, rnd, opex):
    return _clean(_rank(_diff(_slope(_log(sgna.abs() + 1.0), 4), 4), 12))
def cg_f020_sga_rnd_mix_core89_3rd_v090_signal(sgna, rnd, opex):
    return _clean(_rank(_diff(_slope(_log(rnd.abs() + 1.0), 4), 4), 12))
def cg_f020_sga_rnd_mix_core90_3rd_v091_signal(sgna, rnd, opex):
    return _clean(_mean(_diff(_diff(sgna, 4), 4), 4))
def cg_f020_sga_rnd_mix_core91_3rd_v092_signal(sgna, rnd, opex):
    return _clean(_mean(_diff(_diff(rnd, 4), 4), 4))
def cg_f020_sga_rnd_mix_core92_3rd_v093_signal(sgna, rnd, opex):
    return _clean(_mean(_diff(_diff(opex, 4), 4), 4))
def cg_f020_sga_rnd_mix_core93_3rd_v094_signal(sgna, rnd, opex):
    return _clean(_mean(_diff(_diff(_safe_div(rnd, sgna.abs() + 1.0), 4), 4), 4))
def cg_f020_sga_rnd_mix_core94_3rd_v095_signal(sgna, rnd, opex):
    return _clean(_mean(_diff(_diff(_safe_div(rnd, opex), 4), 4), 4))
def cg_f020_sga_rnd_mix_core95_3rd_v096_signal(sgna, rnd, opex):
    return _clean(_mean(_diff(_diff(_safe_div(sgna, opex), 4), 4), 4))
def cg_f020_sga_rnd_mix_core96_3rd_v097_signal(sgna, rnd, opex):
    return _clean(_mean(_diff(_diff(sgna + rnd, 4), 4), 4))
def cg_f020_sga_rnd_mix_core97_3rd_v098_signal(sgna, rnd, opex):
    return _clean(_mean(_diff(_diff(_safe_div(sgna + rnd, opex), 4), 4), 4))
def cg_f020_sga_rnd_mix_core98_3rd_v099_signal(sgna, rnd, opex):
    return _clean(_mean(_diff(_diff(_log(sgna.abs() + 1.0), 4), 4), 4))
def cg_f020_sga_rnd_mix_core99_3rd_v100_signal(sgna, rnd, opex):
    return _clean(_mean(_diff(_diff(_log(rnd.abs() + 1.0), 4), 4), 4))
def cg_f020_sga_rnd_mix_core100_3rd_v101_signal(sgna, rnd, opex):
    return _clean(_mean(_slope(_diff(sgna, 4), 8), 4))
def cg_f020_sga_rnd_mix_core101_3rd_v102_signal(sgna, rnd, opex):
    return _clean(_mean(_slope(_diff(rnd, 4), 8), 4))
def cg_f020_sga_rnd_mix_core102_3rd_v103_signal(sgna, rnd, opex):
    return _clean(_mean(_slope(_diff(opex, 4), 8), 4))
def cg_f020_sga_rnd_mix_core103_3rd_v104_signal(sgna, rnd, opex):
    return _clean(_mean(_slope(_diff(_safe_div(rnd, sgna.abs() + 1.0), 4), 8), 4))
def cg_f020_sga_rnd_mix_core104_3rd_v105_signal(sgna, rnd, opex):
    return _clean(_mean(_slope(_diff(_safe_div(rnd, opex), 4), 8), 4))
def cg_f020_sga_rnd_mix_core105_3rd_v106_signal(sgna, rnd, opex):
    return _clean(_mean(_slope(_diff(_safe_div(sgna, opex), 4), 8), 4))
def cg_f020_sga_rnd_mix_core106_3rd_v107_signal(sgna, rnd, opex):
    return _clean(_mean(_slope(_diff(sgna + rnd, 4), 8), 4))
def cg_f020_sga_rnd_mix_core107_3rd_v108_signal(sgna, rnd, opex):
    return _clean(_mean(_slope(_diff(_safe_div(sgna + rnd, opex), 4), 8), 4))
def cg_f020_sga_rnd_mix_core108_3rd_v109_signal(sgna, rnd, opex):
    return _clean(_mean(_slope(_diff(_log(sgna.abs() + 1.0), 4), 8), 4))
def cg_f020_sga_rnd_mix_core109_3rd_v110_signal(sgna, rnd, opex):
    return _clean(_mean(_slope(_diff(_log(rnd.abs() + 1.0), 4), 8), 4))
def cg_f020_sga_rnd_mix_core110_3rd_v111_signal(sgna, rnd, opex):
    return _clean(_mean(_diff(_slope(sgna, 4), 4), 4))
def cg_f020_sga_rnd_mix_core111_3rd_v112_signal(sgna, rnd, opex):
    return _clean(_mean(_diff(_slope(rnd, 4), 4), 4))
def cg_f020_sga_rnd_mix_core112_3rd_v113_signal(sgna, rnd, opex):
    return _clean(_mean(_diff(_slope(opex, 4), 4), 4))
def cg_f020_sga_rnd_mix_core113_3rd_v114_signal(sgna, rnd, opex):
    return _clean(_mean(_diff(_slope(_safe_div(rnd, sgna.abs() + 1.0), 4), 4), 4))
def cg_f020_sga_rnd_mix_core114_3rd_v115_signal(sgna, rnd, opex):
    return _clean(_mean(_diff(_slope(_safe_div(rnd, opex), 4), 4), 4))
def cg_f020_sga_rnd_mix_core115_3rd_v116_signal(sgna, rnd, opex):
    return _clean(_mean(_diff(_slope(_safe_div(sgna, opex), 4), 4), 4))
def cg_f020_sga_rnd_mix_core116_3rd_v117_signal(sgna, rnd, opex):
    return _clean(_mean(_diff(_slope(sgna + rnd, 4), 4), 4))
def cg_f020_sga_rnd_mix_core117_3rd_v118_signal(sgna, rnd, opex):
    return _clean(_mean(_diff(_slope(_safe_div(sgna + rnd, opex), 4), 4), 4))
def cg_f020_sga_rnd_mix_core118_3rd_v119_signal(sgna, rnd, opex):
    return _clean(_mean(_diff(_slope(_log(sgna.abs() + 1.0), 4), 4), 4))
def cg_f020_sga_rnd_mix_core119_3rd_v120_signal(sgna, rnd, opex):
    return _clean(_mean(_diff(_slope(_log(rnd.abs() + 1.0), 4), 4), 4))
def cg_f020_sga_rnd_mix_core120_3rd_v121_signal(sgna, rnd, opex):
    return _clean(_slope(_diff(_diff(sgna, 4), 4), 4))
def cg_f020_sga_rnd_mix_core121_3rd_v122_signal(sgna, rnd, opex):
    return _clean(_slope(_diff(_diff(rnd, 4), 4), 4))
def cg_f020_sga_rnd_mix_core122_3rd_v123_signal(sgna, rnd, opex):
    return _clean(_slope(_diff(_diff(opex, 4), 4), 4))
def cg_f020_sga_rnd_mix_core123_3rd_v124_signal(sgna, rnd, opex):
    return _clean(_slope(_diff(_diff(_safe_div(rnd, sgna.abs() + 1.0), 4), 4), 4))
def cg_f020_sga_rnd_mix_core124_3rd_v125_signal(sgna, rnd, opex):
    return _clean(_slope(_diff(_diff(_safe_div(rnd, opex), 4), 4), 4))
def cg_f020_sga_rnd_mix_core125_3rd_v126_signal(sgna, rnd, opex):
    return _clean(_slope(_diff(_diff(_safe_div(sgna, opex), 4), 4), 4))
def cg_f020_sga_rnd_mix_core126_3rd_v127_signal(sgna, rnd, opex):
    return _clean(_slope(_diff(_diff(sgna + rnd, 4), 4), 4))
def cg_f020_sga_rnd_mix_core127_3rd_v128_signal(sgna, rnd, opex):
    return _clean(_slope(_diff(_diff(_safe_div(sgna + rnd, opex), 4), 4), 4))
def cg_f020_sga_rnd_mix_core128_3rd_v129_signal(sgna, rnd, opex):
    return _clean(_slope(_diff(_diff(_log(sgna.abs() + 1.0), 4), 4), 4))
def cg_f020_sga_rnd_mix_core129_3rd_v130_signal(sgna, rnd, opex):
    return _clean(_slope(_diff(_diff(_log(rnd.abs() + 1.0), 4), 4), 4))
def cg_f020_sga_rnd_mix_core130_3rd_v131_signal(sgna, rnd, opex):
    return _clean(_diff(_diff(_diff(sgna, 4), 4), 4))
def cg_f020_sga_rnd_mix_core131_3rd_v132_signal(sgna, rnd, opex):
    return _clean(_diff(_diff(_diff(rnd, 4), 4), 4))
def cg_f020_sga_rnd_mix_core132_3rd_v133_signal(sgna, rnd, opex):
    return _clean(_diff(_diff(_diff(opex, 4), 4), 4))
def cg_f020_sga_rnd_mix_core133_3rd_v134_signal(sgna, rnd, opex):
    return _clean(_diff(_diff(_diff(_safe_div(rnd, sgna.abs() + 1.0), 4), 4), 4))
def cg_f020_sga_rnd_mix_core134_3rd_v135_signal(sgna, rnd, opex):
    return _clean(_diff(_diff(_diff(_safe_div(rnd, opex), 4), 4), 4))
def cg_f020_sga_rnd_mix_core135_3rd_v136_signal(sgna, rnd, opex):
    return _clean(_diff(_diff(_diff(_safe_div(sgna, opex), 4), 4), 4))
def cg_f020_sga_rnd_mix_core136_3rd_v137_signal(sgna, rnd, opex):
    return _clean(_diff(_diff(_diff(sgna + rnd, 4), 4), 4))
def cg_f020_sga_rnd_mix_core137_3rd_v138_signal(sgna, rnd, opex):
    return _clean(_diff(_diff(_diff(_safe_div(sgna + rnd, opex), 4), 4), 4))
def cg_f020_sga_rnd_mix_core138_3rd_v139_signal(sgna, rnd, opex):
    return _clean(_diff(_diff(_diff(_log(sgna.abs() + 1.0), 4), 4), 4))
def cg_f020_sga_rnd_mix_core139_3rd_v140_signal(sgna, rnd, opex):
    return _clean(_diff(_diff(_diff(_log(rnd.abs() + 1.0), 4), 4), 4))
def cg_f020_sga_rnd_mix_core140_3rd_v141_signal(sgna, rnd, opex):
    return _clean(_z(_slope(_diff(_diff(sgna, 4), 4), 4), 8))
def cg_f020_sga_rnd_mix_core141_3rd_v142_signal(sgna, rnd, opex):
    return _clean(_z(_slope(_diff(_diff(rnd, 4), 4), 4), 8))
def cg_f020_sga_rnd_mix_core142_3rd_v143_signal(sgna, rnd, opex):
    return _clean(_z(_slope(_diff(_diff(opex, 4), 4), 4), 8))
def cg_f020_sga_rnd_mix_core143_3rd_v144_signal(sgna, rnd, opex):
    return _clean(_z(_slope(_diff(_diff(_safe_div(rnd, sgna.abs() + 1.0), 4), 4), 4), 8))
def cg_f020_sga_rnd_mix_core144_3rd_v145_signal(sgna, rnd, opex):
    return _clean(_z(_slope(_diff(_diff(_safe_div(rnd, opex), 4), 4), 4), 8))
def cg_f020_sga_rnd_mix_core145_3rd_v146_signal(sgna, rnd, opex):
    return _clean(_z(_slope(_diff(_diff(_safe_div(sgna, opex), 4), 4), 4), 8))
def cg_f020_sga_rnd_mix_core146_3rd_v147_signal(sgna, rnd, opex):
    return _clean(_z(_slope(_diff(_diff(sgna + rnd, 4), 4), 4), 8))
def cg_f020_sga_rnd_mix_core147_3rd_v148_signal(sgna, rnd, opex):
    return _clean(_z(_slope(_diff(_diff(_safe_div(sgna + rnd, opex), 4), 4), 4), 8))
def cg_f020_sga_rnd_mix_core148_3rd_v149_signal(sgna, rnd, opex):
    return _clean(_z(_slope(_diff(_diff(_log(sgna.abs() + 1.0), 4), 4), 4), 8))
def cg_f020_sga_rnd_mix_core149_3rd_v150_signal(sgna, rnd, opex):
    return _clean(_z(_slope(_diff(_diff(_log(rnd.abs() + 1.0), 4), 4), 4), 8))