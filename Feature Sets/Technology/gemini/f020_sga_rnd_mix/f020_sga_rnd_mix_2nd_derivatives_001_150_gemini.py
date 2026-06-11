import numpy as np
import pandas as pd
from technology_helpers import _to_num, _clean, _safe_div, _log, _mean, _std, _sum, _min, _max, _z, _pct_change, _diff, _rank, _skew, _kurt, _autocorr, _corr, _slope, _ewm, _event_flag, _event_count, _event_rate, _clip_z

def cg_f020_sga_rnd_mix_core00_2nd_v001_signal(sgna, rnd, opex):
    return _clean(_slope(sgna, 4))
def cg_f020_sga_rnd_mix_core01_2nd_v002_signal(sgna, rnd, opex):
    return _clean(_slope(rnd, 4))
def cg_f020_sga_rnd_mix_core02_2nd_v003_signal(sgna, rnd, opex):
    return _clean(_slope(opex, 4))
def cg_f020_sga_rnd_mix_core03_2nd_v004_signal(sgna, rnd, opex):
    return _clean(_slope(_safe_div(rnd, sgna.abs() + 1.0), 4))
def cg_f020_sga_rnd_mix_core04_2nd_v005_signal(sgna, rnd, opex):
    return _clean(_slope(_safe_div(rnd, opex), 4))
def cg_f020_sga_rnd_mix_core05_2nd_v006_signal(sgna, rnd, opex):
    return _clean(_slope(_safe_div(sgna, opex), 4))
def cg_f020_sga_rnd_mix_core06_2nd_v007_signal(sgna, rnd, opex):
    return _clean(_slope(sgna + rnd, 4))
def cg_f020_sga_rnd_mix_core07_2nd_v008_signal(sgna, rnd, opex):
    return _clean(_slope(_safe_div(sgna + rnd, opex), 4))
def cg_f020_sga_rnd_mix_core08_2nd_v009_signal(sgna, rnd, opex):
    return _clean(_slope(_log(sgna.abs() + 1.0), 4))
def cg_f020_sga_rnd_mix_core09_2nd_v010_signal(sgna, rnd, opex):
    return _clean(_slope(_log(rnd.abs() + 1.0), 4))
def cg_f020_sga_rnd_mix_core10_2nd_v011_signal(sgna, rnd, opex):
    return _clean(_slope(sgna, 8))
def cg_f020_sga_rnd_mix_core11_2nd_v012_signal(sgna, rnd, opex):
    return _clean(_slope(rnd, 8))
def cg_f020_sga_rnd_mix_core12_2nd_v013_signal(sgna, rnd, opex):
    return _clean(_slope(opex, 8))
def cg_f020_sga_rnd_mix_core13_2nd_v014_signal(sgna, rnd, opex):
    return _clean(_slope(_safe_div(rnd, sgna.abs() + 1.0), 8))
def cg_f020_sga_rnd_mix_core14_2nd_v015_signal(sgna, rnd, opex):
    return _clean(_slope(_safe_div(rnd, opex), 8))
def cg_f020_sga_rnd_mix_core15_2nd_v016_signal(sgna, rnd, opex):
    return _clean(_slope(_safe_div(sgna, opex), 8))
def cg_f020_sga_rnd_mix_core16_2nd_v017_signal(sgna, rnd, opex):
    return _clean(_slope(sgna + rnd, 8))
def cg_f020_sga_rnd_mix_core17_2nd_v018_signal(sgna, rnd, opex):
    return _clean(_slope(_safe_div(sgna + rnd, opex), 8))
def cg_f020_sga_rnd_mix_core18_2nd_v019_signal(sgna, rnd, opex):
    return _clean(_slope(_log(sgna.abs() + 1.0), 8))
def cg_f020_sga_rnd_mix_core19_2nd_v020_signal(sgna, rnd, opex):
    return _clean(_slope(_log(rnd.abs() + 1.0), 8))
def cg_f020_sga_rnd_mix_core20_2nd_v021_signal(sgna, rnd, opex):
    return _clean(_diff(sgna, 4))
def cg_f020_sga_rnd_mix_core21_2nd_v022_signal(sgna, rnd, opex):
    return _clean(_diff(rnd, 4))
def cg_f020_sga_rnd_mix_core22_2nd_v023_signal(sgna, rnd, opex):
    return _clean(_diff(opex, 4))
def cg_f020_sga_rnd_mix_core23_2nd_v024_signal(sgna, rnd, opex):
    return _clean(_diff(_safe_div(rnd, sgna.abs() + 1.0), 4))
def cg_f020_sga_rnd_mix_core24_2nd_v025_signal(sgna, rnd, opex):
    return _clean(_diff(_safe_div(rnd, opex), 4))
def cg_f020_sga_rnd_mix_core25_2nd_v026_signal(sgna, rnd, opex):
    return _clean(_diff(_safe_div(sgna, opex), 4))
def cg_f020_sga_rnd_mix_core26_2nd_v027_signal(sgna, rnd, opex):
    return _clean(_diff(sgna + rnd, 4))
def cg_f020_sga_rnd_mix_core27_2nd_v028_signal(sgna, rnd, opex):
    return _clean(_diff(_safe_div(sgna + rnd, opex), 4))
def cg_f020_sga_rnd_mix_core28_2nd_v029_signal(sgna, rnd, opex):
    return _clean(_diff(_log(sgna.abs() + 1.0), 4))
def cg_f020_sga_rnd_mix_core29_2nd_v030_signal(sgna, rnd, opex):
    return _clean(_diff(_log(rnd.abs() + 1.0), 4))
def cg_f020_sga_rnd_mix_core30_2nd_v031_signal(sgna, rnd, opex):
    return _clean(_z(_slope(sgna, 4), 8))
def cg_f020_sga_rnd_mix_core31_2nd_v032_signal(sgna, rnd, opex):
    return _clean(_z(_slope(rnd, 4), 8))
def cg_f020_sga_rnd_mix_core32_2nd_v033_signal(sgna, rnd, opex):
    return _clean(_z(_slope(opex, 4), 8))
def cg_f020_sga_rnd_mix_core33_2nd_v034_signal(sgna, rnd, opex):
    return _clean(_z(_slope(_safe_div(rnd, sgna.abs() + 1.0), 4), 8))
def cg_f020_sga_rnd_mix_core34_2nd_v035_signal(sgna, rnd, opex):
    return _clean(_z(_slope(_safe_div(rnd, opex), 4), 8))
def cg_f020_sga_rnd_mix_core35_2nd_v036_signal(sgna, rnd, opex):
    return _clean(_z(_slope(_safe_div(sgna, opex), 4), 8))
def cg_f020_sga_rnd_mix_core36_2nd_v037_signal(sgna, rnd, opex):
    return _clean(_z(_slope(sgna + rnd, 4), 8))
def cg_f020_sga_rnd_mix_core37_2nd_v038_signal(sgna, rnd, opex):
    return _clean(_z(_slope(_safe_div(sgna + rnd, opex), 4), 8))
def cg_f020_sga_rnd_mix_core38_2nd_v039_signal(sgna, rnd, opex):
    return _clean(_z(_slope(_log(sgna.abs() + 1.0), 4), 8))
def cg_f020_sga_rnd_mix_core39_2nd_v040_signal(sgna, rnd, opex):
    return _clean(_z(_slope(_log(rnd.abs() + 1.0), 4), 8))
def cg_f020_sga_rnd_mix_core40_2nd_v041_signal(sgna, rnd, opex):
    return _clean(_z(_slope(sgna, 8), 12))
def cg_f020_sga_rnd_mix_core41_2nd_v042_signal(sgna, rnd, opex):
    return _clean(_z(_slope(rnd, 8), 12))
def cg_f020_sga_rnd_mix_core42_2nd_v043_signal(sgna, rnd, opex):
    return _clean(_z(_slope(opex, 8), 12))
def cg_f020_sga_rnd_mix_core43_2nd_v044_signal(sgna, rnd, opex):
    return _clean(_z(_slope(_safe_div(rnd, sgna.abs() + 1.0), 8), 12))
def cg_f020_sga_rnd_mix_core44_2nd_v045_signal(sgna, rnd, opex):
    return _clean(_z(_slope(_safe_div(rnd, opex), 8), 12))
def cg_f020_sga_rnd_mix_core45_2nd_v046_signal(sgna, rnd, opex):
    return _clean(_z(_slope(_safe_div(sgna, opex), 8), 12))
def cg_f020_sga_rnd_mix_core46_2nd_v047_signal(sgna, rnd, opex):
    return _clean(_z(_slope(sgna + rnd, 8), 12))
def cg_f020_sga_rnd_mix_core47_2nd_v048_signal(sgna, rnd, opex):
    return _clean(_z(_slope(_safe_div(sgna + rnd, opex), 8), 12))
def cg_f020_sga_rnd_mix_core48_2nd_v049_signal(sgna, rnd, opex):
    return _clean(_z(_slope(_log(sgna.abs() + 1.0), 8), 12))
def cg_f020_sga_rnd_mix_core49_2nd_v050_signal(sgna, rnd, opex):
    return _clean(_z(_slope(_log(rnd.abs() + 1.0), 8), 12))
def cg_f020_sga_rnd_mix_core50_2nd_v051_signal(sgna, rnd, opex):
    return _clean(_z(_diff(sgna, 4), 8))
def cg_f020_sga_rnd_mix_core51_2nd_v052_signal(sgna, rnd, opex):
    return _clean(_z(_diff(rnd, 4), 8))
def cg_f020_sga_rnd_mix_core52_2nd_v053_signal(sgna, rnd, opex):
    return _clean(_z(_diff(opex, 4), 8))
def cg_f020_sga_rnd_mix_core53_2nd_v054_signal(sgna, rnd, opex):
    return _clean(_z(_diff(_safe_div(rnd, sgna.abs() + 1.0), 4), 8))
def cg_f020_sga_rnd_mix_core54_2nd_v055_signal(sgna, rnd, opex):
    return _clean(_z(_diff(_safe_div(rnd, opex), 4), 8))
def cg_f020_sga_rnd_mix_core55_2nd_v056_signal(sgna, rnd, opex):
    return _clean(_z(_diff(_safe_div(sgna, opex), 4), 8))
def cg_f020_sga_rnd_mix_core56_2nd_v057_signal(sgna, rnd, opex):
    return _clean(_z(_diff(sgna + rnd, 4), 8))
def cg_f020_sga_rnd_mix_core57_2nd_v058_signal(sgna, rnd, opex):
    return _clean(_z(_diff(_safe_div(sgna + rnd, opex), 4), 8))
def cg_f020_sga_rnd_mix_core58_2nd_v059_signal(sgna, rnd, opex):
    return _clean(_z(_diff(_log(sgna.abs() + 1.0), 4), 8))
def cg_f020_sga_rnd_mix_core59_2nd_v060_signal(sgna, rnd, opex):
    return _clean(_z(_diff(_log(rnd.abs() + 1.0), 4), 8))
def cg_f020_sga_rnd_mix_core60_2nd_v061_signal(sgna, rnd, opex):
    return _clean(_rank(_slope(sgna, 4), 12))
def cg_f020_sga_rnd_mix_core61_2nd_v062_signal(sgna, rnd, opex):
    return _clean(_rank(_slope(rnd, 4), 12))
def cg_f020_sga_rnd_mix_core62_2nd_v063_signal(sgna, rnd, opex):
    return _clean(_rank(_slope(opex, 4), 12))
def cg_f020_sga_rnd_mix_core63_2nd_v064_signal(sgna, rnd, opex):
    return _clean(_rank(_slope(_safe_div(rnd, sgna.abs() + 1.0), 4), 12))
def cg_f020_sga_rnd_mix_core64_2nd_v065_signal(sgna, rnd, opex):
    return _clean(_rank(_slope(_safe_div(rnd, opex), 4), 12))
def cg_f020_sga_rnd_mix_core65_2nd_v066_signal(sgna, rnd, opex):
    return _clean(_rank(_slope(_safe_div(sgna, opex), 4), 12))
def cg_f020_sga_rnd_mix_core66_2nd_v067_signal(sgna, rnd, opex):
    return _clean(_rank(_slope(sgna + rnd, 4), 12))
def cg_f020_sga_rnd_mix_core67_2nd_v068_signal(sgna, rnd, opex):
    return _clean(_rank(_slope(_safe_div(sgna + rnd, opex), 4), 12))
def cg_f020_sga_rnd_mix_core68_2nd_v069_signal(sgna, rnd, opex):
    return _clean(_rank(_slope(_log(sgna.abs() + 1.0), 4), 12))
def cg_f020_sga_rnd_mix_core69_2nd_v070_signal(sgna, rnd, opex):
    return _clean(_rank(_slope(_log(rnd.abs() + 1.0), 4), 12))
def cg_f020_sga_rnd_mix_core70_2nd_v071_signal(sgna, rnd, opex):
    return _clean(_rank(_diff(sgna, 4), 12))
def cg_f020_sga_rnd_mix_core71_2nd_v072_signal(sgna, rnd, opex):
    return _clean(_rank(_diff(rnd, 4), 12))
def cg_f020_sga_rnd_mix_core72_2nd_v073_signal(sgna, rnd, opex):
    return _clean(_rank(_diff(opex, 4), 12))
def cg_f020_sga_rnd_mix_core73_2nd_v074_signal(sgna, rnd, opex):
    return _clean(_rank(_diff(_safe_div(rnd, sgna.abs() + 1.0), 4), 12))
def cg_f020_sga_rnd_mix_core74_2nd_v075_signal(sgna, rnd, opex):
    return _clean(_rank(_diff(_safe_div(rnd, opex), 4), 12))
def cg_f020_sga_rnd_mix_core75_2nd_v076_signal(sgna, rnd, opex):
    return _clean(_rank(_diff(_safe_div(sgna, opex), 4), 12))
def cg_f020_sga_rnd_mix_core76_2nd_v077_signal(sgna, rnd, opex):
    return _clean(_rank(_diff(sgna + rnd, 4), 12))
def cg_f020_sga_rnd_mix_core77_2nd_v078_signal(sgna, rnd, opex):
    return _clean(_rank(_diff(_safe_div(sgna + rnd, opex), 4), 12))
def cg_f020_sga_rnd_mix_core78_2nd_v079_signal(sgna, rnd, opex):
    return _clean(_rank(_diff(_log(sgna.abs() + 1.0), 4), 12))
def cg_f020_sga_rnd_mix_core79_2nd_v080_signal(sgna, rnd, opex):
    return _clean(_rank(_diff(_log(rnd.abs() + 1.0), 4), 12))
def cg_f020_sga_rnd_mix_core80_2nd_v081_signal(sgna, rnd, opex):
    return _clean(_mean(_slope(sgna, 4), 4))
def cg_f020_sga_rnd_mix_core81_2nd_v082_signal(sgna, rnd, opex):
    return _clean(_mean(_slope(rnd, 4), 4))
def cg_f020_sga_rnd_mix_core82_2nd_v083_signal(sgna, rnd, opex):
    return _clean(_mean(_slope(opex, 4), 4))
def cg_f020_sga_rnd_mix_core83_2nd_v084_signal(sgna, rnd, opex):
    return _clean(_mean(_slope(_safe_div(rnd, sgna.abs() + 1.0), 4), 4))
def cg_f020_sga_rnd_mix_core84_2nd_v085_signal(sgna, rnd, opex):
    return _clean(_mean(_slope(_safe_div(rnd, opex), 4), 4))
def cg_f020_sga_rnd_mix_core85_2nd_v086_signal(sgna, rnd, opex):
    return _clean(_mean(_slope(_safe_div(sgna, opex), 4), 4))
def cg_f020_sga_rnd_mix_core86_2nd_v087_signal(sgna, rnd, opex):
    return _clean(_mean(_slope(sgna + rnd, 4), 4))
def cg_f020_sga_rnd_mix_core87_2nd_v088_signal(sgna, rnd, opex):
    return _clean(_mean(_slope(_safe_div(sgna + rnd, opex), 4), 4))
def cg_f020_sga_rnd_mix_core88_2nd_v089_signal(sgna, rnd, opex):
    return _clean(_mean(_slope(_log(sgna.abs() + 1.0), 4), 4))
def cg_f020_sga_rnd_mix_core89_2nd_v090_signal(sgna, rnd, opex):
    return _clean(_mean(_slope(_log(rnd.abs() + 1.0), 4), 4))
def cg_f020_sga_rnd_mix_core90_2nd_v091_signal(sgna, rnd, opex):
    return _clean(_mean(_diff(sgna, 4), 4))
def cg_f020_sga_rnd_mix_core91_2nd_v092_signal(sgna, rnd, opex):
    return _clean(_mean(_diff(rnd, 4), 4))
def cg_f020_sga_rnd_mix_core92_2nd_v093_signal(sgna, rnd, opex):
    return _clean(_mean(_diff(opex, 4), 4))
def cg_f020_sga_rnd_mix_core93_2nd_v094_signal(sgna, rnd, opex):
    return _clean(_mean(_diff(_safe_div(rnd, sgna.abs() + 1.0), 4), 4))
def cg_f020_sga_rnd_mix_core94_2nd_v095_signal(sgna, rnd, opex):
    return _clean(_mean(_diff(_safe_div(rnd, opex), 4), 4))
def cg_f020_sga_rnd_mix_core95_2nd_v096_signal(sgna, rnd, opex):
    return _clean(_mean(_diff(_safe_div(sgna, opex), 4), 4))
def cg_f020_sga_rnd_mix_core96_2nd_v097_signal(sgna, rnd, opex):
    return _clean(_mean(_diff(sgna + rnd, 4), 4))
def cg_f020_sga_rnd_mix_core97_2nd_v098_signal(sgna, rnd, opex):
    return _clean(_mean(_diff(_safe_div(sgna + rnd, opex), 4), 4))
def cg_f020_sga_rnd_mix_core98_2nd_v099_signal(sgna, rnd, opex):
    return _clean(_mean(_diff(_log(sgna.abs() + 1.0), 4), 4))
def cg_f020_sga_rnd_mix_core99_2nd_v100_signal(sgna, rnd, opex):
    return _clean(_mean(_diff(_log(rnd.abs() + 1.0), 4), 4))
def cg_f020_sga_rnd_mix_core100_2nd_v101_signal(sgna, rnd, opex):
    return _clean(_slope(_mean(sgna, 4), 4))
def cg_f020_sga_rnd_mix_core101_2nd_v102_signal(sgna, rnd, opex):
    return _clean(_slope(_mean(rnd, 4), 4))
def cg_f020_sga_rnd_mix_core102_2nd_v103_signal(sgna, rnd, opex):
    return _clean(_slope(_mean(opex, 4), 4))
def cg_f020_sga_rnd_mix_core103_2nd_v104_signal(sgna, rnd, opex):
    return _clean(_slope(_mean(_safe_div(rnd, sgna.abs() + 1.0), 4), 4))
def cg_f020_sga_rnd_mix_core104_2nd_v105_signal(sgna, rnd, opex):
    return _clean(_slope(_mean(_safe_div(rnd, opex), 4), 4))
def cg_f020_sga_rnd_mix_core105_2nd_v106_signal(sgna, rnd, opex):
    return _clean(_slope(_mean(_safe_div(sgna, opex), 4), 4))
def cg_f020_sga_rnd_mix_core106_2nd_v107_signal(sgna, rnd, opex):
    return _clean(_slope(_mean(sgna + rnd, 4), 4))
def cg_f020_sga_rnd_mix_core107_2nd_v108_signal(sgna, rnd, opex):
    return _clean(_slope(_mean(_safe_div(sgna + rnd, opex), 4), 4))
def cg_f020_sga_rnd_mix_core108_2nd_v109_signal(sgna, rnd, opex):
    return _clean(_slope(_mean(_log(sgna.abs() + 1.0), 4), 4))
def cg_f020_sga_rnd_mix_core109_2nd_v110_signal(sgna, rnd, opex):
    return _clean(_slope(_mean(_log(rnd.abs() + 1.0), 4), 4))
def cg_f020_sga_rnd_mix_core110_2nd_v111_signal(sgna, rnd, opex):
    return _clean(_slope(_mean(sgna, 8), 8))
def cg_f020_sga_rnd_mix_core111_2nd_v112_signal(sgna, rnd, opex):
    return _clean(_slope(_mean(rnd, 8), 8))
def cg_f020_sga_rnd_mix_core112_2nd_v113_signal(sgna, rnd, opex):
    return _clean(_slope(_mean(opex, 8), 8))
def cg_f020_sga_rnd_mix_core113_2nd_v114_signal(sgna, rnd, opex):
    return _clean(_slope(_mean(_safe_div(rnd, sgna.abs() + 1.0), 8), 8))
def cg_f020_sga_rnd_mix_core114_2nd_v115_signal(sgna, rnd, opex):
    return _clean(_slope(_mean(_safe_div(rnd, opex), 8), 8))
def cg_f020_sga_rnd_mix_core115_2nd_v116_signal(sgna, rnd, opex):
    return _clean(_slope(_mean(_safe_div(sgna, opex), 8), 8))
def cg_f020_sga_rnd_mix_core116_2nd_v117_signal(sgna, rnd, opex):
    return _clean(_slope(_mean(sgna + rnd, 8), 8))
def cg_f020_sga_rnd_mix_core117_2nd_v118_signal(sgna, rnd, opex):
    return _clean(_slope(_mean(_safe_div(sgna + rnd, opex), 8), 8))
def cg_f020_sga_rnd_mix_core118_2nd_v119_signal(sgna, rnd, opex):
    return _clean(_slope(_mean(_log(sgna.abs() + 1.0), 8), 8))
def cg_f020_sga_rnd_mix_core119_2nd_v120_signal(sgna, rnd, opex):
    return _clean(_slope(_mean(_log(rnd.abs() + 1.0), 8), 8))
def cg_f020_sga_rnd_mix_core120_2nd_v121_signal(sgna, rnd, opex):
    return _clean(_diff(_mean(sgna, 4), 4))
def cg_f020_sga_rnd_mix_core121_2nd_v122_signal(sgna, rnd, opex):
    return _clean(_diff(_mean(rnd, 4), 4))
def cg_f020_sga_rnd_mix_core122_2nd_v123_signal(sgna, rnd, opex):
    return _clean(_diff(_mean(opex, 4), 4))
def cg_f020_sga_rnd_mix_core123_2nd_v124_signal(sgna, rnd, opex):
    return _clean(_diff(_mean(_safe_div(rnd, sgna.abs() + 1.0), 4), 4))
def cg_f020_sga_rnd_mix_core124_2nd_v125_signal(sgna, rnd, opex):
    return _clean(_diff(_mean(_safe_div(rnd, opex), 4), 4))
def cg_f020_sga_rnd_mix_core125_2nd_v126_signal(sgna, rnd, opex):
    return _clean(_diff(_mean(_safe_div(sgna, opex), 4), 4))
def cg_f020_sga_rnd_mix_core126_2nd_v127_signal(sgna, rnd, opex):
    return _clean(_diff(_mean(sgna + rnd, 4), 4))
def cg_f020_sga_rnd_mix_core127_2nd_v128_signal(sgna, rnd, opex):
    return _clean(_diff(_mean(_safe_div(sgna + rnd, opex), 4), 4))
def cg_f020_sga_rnd_mix_core128_2nd_v129_signal(sgna, rnd, opex):
    return _clean(_diff(_mean(_log(sgna.abs() + 1.0), 4), 4))
def cg_f020_sga_rnd_mix_core129_2nd_v130_signal(sgna, rnd, opex):
    return _clean(_diff(_mean(_log(rnd.abs() + 1.0), 4), 4))
def cg_f020_sga_rnd_mix_core130_2nd_v131_signal(sgna, rnd, opex):
    return _clean(_z(_diff(_mean(sgna, 4), 4), 8))
def cg_f020_sga_rnd_mix_core131_2nd_v132_signal(sgna, rnd, opex):
    return _clean(_z(_diff(_mean(rnd, 4), 4), 8))
def cg_f020_sga_rnd_mix_core132_2nd_v133_signal(sgna, rnd, opex):
    return _clean(_z(_diff(_mean(opex, 4), 4), 8))
def cg_f020_sga_rnd_mix_core133_2nd_v134_signal(sgna, rnd, opex):
    return _clean(_z(_diff(_mean(_safe_div(rnd, sgna.abs() + 1.0), 4), 4), 8))
def cg_f020_sga_rnd_mix_core134_2nd_v135_signal(sgna, rnd, opex):
    return _clean(_z(_diff(_mean(_safe_div(rnd, opex), 4), 4), 8))
def cg_f020_sga_rnd_mix_core135_2nd_v136_signal(sgna, rnd, opex):
    return _clean(_z(_diff(_mean(_safe_div(sgna, opex), 4), 4), 8))
def cg_f020_sga_rnd_mix_core136_2nd_v137_signal(sgna, rnd, opex):
    return _clean(_z(_diff(_mean(sgna + rnd, 4), 4), 8))
def cg_f020_sga_rnd_mix_core137_2nd_v138_signal(sgna, rnd, opex):
    return _clean(_z(_diff(_mean(_safe_div(sgna + rnd, opex), 4), 4), 8))
def cg_f020_sga_rnd_mix_core138_2nd_v139_signal(sgna, rnd, opex):
    return _clean(_z(_diff(_mean(_log(sgna.abs() + 1.0), 4), 4), 8))
def cg_f020_sga_rnd_mix_core139_2nd_v140_signal(sgna, rnd, opex):
    return _clean(_z(_diff(_mean(_log(rnd.abs() + 1.0), 4), 4), 8))
def cg_f020_sga_rnd_mix_core140_2nd_v141_signal(sgna, rnd, opex):
    return _clean(_rank(_slope(_mean(sgna, 4), 4), 12))
def cg_f020_sga_rnd_mix_core141_2nd_v142_signal(sgna, rnd, opex):
    return _clean(_rank(_slope(_mean(rnd, 4), 4), 12))
def cg_f020_sga_rnd_mix_core142_2nd_v143_signal(sgna, rnd, opex):
    return _clean(_rank(_slope(_mean(opex, 4), 4), 12))
def cg_f020_sga_rnd_mix_core143_2nd_v144_signal(sgna, rnd, opex):
    return _clean(_rank(_slope(_mean(_safe_div(rnd, sgna.abs() + 1.0), 4), 4), 12))
def cg_f020_sga_rnd_mix_core144_2nd_v145_signal(sgna, rnd, opex):
    return _clean(_rank(_slope(_mean(_safe_div(rnd, opex), 4), 4), 12))
def cg_f020_sga_rnd_mix_core145_2nd_v146_signal(sgna, rnd, opex):
    return _clean(_rank(_slope(_mean(_safe_div(sgna, opex), 4), 4), 12))
def cg_f020_sga_rnd_mix_core146_2nd_v147_signal(sgna, rnd, opex):
    return _clean(_rank(_slope(_mean(sgna + rnd, 4), 4), 12))
def cg_f020_sga_rnd_mix_core147_2nd_v148_signal(sgna, rnd, opex):
    return _clean(_rank(_slope(_mean(_safe_div(sgna + rnd, opex), 4), 4), 12))
def cg_f020_sga_rnd_mix_core148_2nd_v149_signal(sgna, rnd, opex):
    return _clean(_rank(_slope(_mean(_log(sgna.abs() + 1.0), 4), 4), 12))
def cg_f020_sga_rnd_mix_core149_2nd_v150_signal(sgna, rnd, opex):
    return _clean(_rank(_slope(_mean(_log(rnd.abs() + 1.0), 4), 4), 12))