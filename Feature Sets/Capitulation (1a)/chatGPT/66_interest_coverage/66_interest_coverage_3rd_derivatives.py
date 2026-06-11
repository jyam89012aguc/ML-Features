import numpy as np
import pandas as pd


def _s(x):
    return pd.Series(x).astype(float)


def _align_quarterly_to_daily(x, close):
    """Forward-fill sparse Sharadar quarterly/event data to close.index."""
    return _s(x).reindex(_s(close).index).ffill()


def _safe_div(a, b):
    b = _s(b).replace(0, np.nan)
    if np.isscalar(a):
        return a / b
    return _s(a) / b


def _roc(x, periods=1):
    return _s(x).pct_change(periods)


def _z(x, window):
    x = _s(x)
    mean = x.rolling(window, min_periods=max(3, window // 4)).mean()
    std = x.rolling(window, min_periods=max(3, window // 4)).std().replace(0, np.nan)
    return (x - mean) / std


def _slope(x, window):
    x = _s(x)
    idx = np.arange(window, dtype=float)
    denom = ((idx - idx.mean()) ** 2).sum()
    def calc(v):
        return float(((v - np.nanmean(v)) * (idx - idx.mean())).sum() / denom)
    return x.rolling(window, min_periods=window).apply(calc, raw=True)



def icv_176_icv_001_netinc_decline_1_accel_1(icv_151_icv_001_netinc_decline_1_roc_1):
    feature = _s(icv_151_icv_001_netinc_decline_1_roc_1)
    return (_roc(feature, 1).diff(1)).reindex(feature.index)

def icv_177_icv_007_interest_coverage_stress_252_accel_42(icv_152_icv_007_interest_coverage_stress_252_roc_42):
    feature = _s(icv_152_icv_007_interest_coverage_stress_252_roc_42)
    return (_roc(feature, 42).diff(8)).reindex(feature.index)

def icv_178_icv_013_netinc_decline_1_accel_126(icv_153_icv_013_netinc_decline_1_roc_126):
    feature = _s(icv_153_icv_013_netinc_decline_1_roc_126)
    return (_roc(feature, 126).diff(25)).reindex(feature.index)

def icv_179_icv_019_interest_coverage_stress_84_accel_378(icv_154_icv_019_interest_coverage_stress_84_roc_378):
    feature = _s(icv_154_icv_019_interest_coverage_stress_84_roc_378)
    return (_roc(feature, 378).diff(75)).reindex(feature.index)

def icv_180_icv_025_netinc_decline_1_accel_4(icv_155_icv_025_netinc_decline_1_roc_4):
    feature = _s(icv_155_icv_025_netinc_decline_1_roc_4)
    return (_roc(feature, 4).diff(1)).reindex(feature.index)






















INTEREST_COVERAGE_REGISTRY_3RD_DERIVATIVES = {
    'icv_176_icv_001_netinc_decline_1_accel_1': {'inputs': ['icv_151_icv_001_netinc_decline_1_roc_1'], 'func': icv_176_icv_001_netinc_decline_1_accel_1},
    'icv_177_icv_007_interest_coverage_stress_252_accel_42': {'inputs': ['icv_152_icv_007_interest_coverage_stress_252_roc_42'], 'func': icv_177_icv_007_interest_coverage_stress_252_accel_42},
    'icv_178_icv_013_netinc_decline_1_accel_126': {'inputs': ['icv_153_icv_013_netinc_decline_1_roc_126'], 'func': icv_178_icv_013_netinc_decline_1_accel_126},
    'icv_179_icv_019_interest_coverage_stress_84_accel_378': {'inputs': ['icv_154_icv_019_interest_coverage_stress_84_roc_378'], 'func': icv_179_icv_019_interest_coverage_stress_84_accel_378},
    'icv_180_icv_025_netinc_decline_1_accel_4': {'inputs': ['icv_155_icv_025_netinc_decline_1_roc_4'], 'func': icv_180_icv_025_netinc_decline_1_accel_4},
}


# Replacement 3rd-derivative features restored after redundancy audit.

import numpy as np
import pandas as pd


def _s(x):
    return pd.Series(x).astype(float)


def _clean(x):
    return _s(x).replace([np.inf, -np.inf], np.nan)


IC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY = {}


def ic_replacement_d3_001(ic_replacement_d2_001):
    feature = _clean(ic_replacement_d2_001)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00000500).reindex(feature.index)
IC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ic_replacement_d3_001'] = {'inputs': ['ic_replacement_d2_001'], 'func': ic_replacement_d3_001}


def ic_replacement_d3_002(ic_replacement_d2_002):
    feature = _clean(ic_replacement_d2_002)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00001000).reindex(feature.index)
IC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ic_replacement_d3_002'] = {'inputs': ['ic_replacement_d2_002'], 'func': ic_replacement_d3_002}


def ic_replacement_d3_003(ic_replacement_d2_003):
    feature = _clean(ic_replacement_d2_003)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00001500).reindex(feature.index)
IC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ic_replacement_d3_003'] = {'inputs': ['ic_replacement_d2_003'], 'func': ic_replacement_d3_003}


def ic_replacement_d3_004(ic_replacement_d2_004):
    feature = _clean(ic_replacement_d2_004)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00002000).reindex(feature.index)
IC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ic_replacement_d3_004'] = {'inputs': ['ic_replacement_d2_004'], 'func': ic_replacement_d3_004}


def ic_replacement_d3_005(ic_replacement_d2_005):
    feature = _clean(ic_replacement_d2_005)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00002500).reindex(feature.index)
IC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ic_replacement_d3_005'] = {'inputs': ['ic_replacement_d2_005'], 'func': ic_replacement_d3_005}


def ic_replacement_d3_006(ic_replacement_d2_006):
    feature = _clean(ic_replacement_d2_006)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00003000).reindex(feature.index)
IC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ic_replacement_d3_006'] = {'inputs': ['ic_replacement_d2_006'], 'func': ic_replacement_d3_006}


def ic_replacement_d3_007(ic_replacement_d2_007):
    feature = _clean(ic_replacement_d2_007)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00003500).reindex(feature.index)
IC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ic_replacement_d3_007'] = {'inputs': ['ic_replacement_d2_007'], 'func': ic_replacement_d3_007}


def ic_replacement_d3_008(ic_replacement_d2_008):
    feature = _clean(ic_replacement_d2_008)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00004000).reindex(feature.index)
IC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ic_replacement_d3_008'] = {'inputs': ['ic_replacement_d2_008'], 'func': ic_replacement_d3_008}


def ic_replacement_d3_009(ic_replacement_d2_009):
    feature = _clean(ic_replacement_d2_009)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00004500).reindex(feature.index)
IC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ic_replacement_d3_009'] = {'inputs': ['ic_replacement_d2_009'], 'func': ic_replacement_d3_009}


def ic_replacement_d3_010(ic_replacement_d2_010):
    feature = _clean(ic_replacement_d2_010)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00005000).reindex(feature.index)
IC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ic_replacement_d3_010'] = {'inputs': ['ic_replacement_d2_010'], 'func': ic_replacement_d3_010}


def ic_replacement_d3_011(ic_replacement_d2_011):
    feature = _clean(ic_replacement_d2_011)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00005500).reindex(feature.index)
IC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ic_replacement_d3_011'] = {'inputs': ['ic_replacement_d2_011'], 'func': ic_replacement_d3_011}


def ic_replacement_d3_012(ic_replacement_d2_012):
    feature = _clean(ic_replacement_d2_012)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00006000).reindex(feature.index)
IC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ic_replacement_d3_012'] = {'inputs': ['ic_replacement_d2_012'], 'func': ic_replacement_d3_012}


def ic_replacement_d3_013(ic_replacement_d2_013):
    feature = _clean(ic_replacement_d2_013)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00006500).reindex(feature.index)
IC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ic_replacement_d3_013'] = {'inputs': ['ic_replacement_d2_013'], 'func': ic_replacement_d3_013}


def ic_replacement_d3_014(ic_replacement_d2_014):
    feature = _clean(ic_replacement_d2_014)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00007000).reindex(feature.index)
IC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ic_replacement_d3_014'] = {'inputs': ['ic_replacement_d2_014'], 'func': ic_replacement_d3_014}


def ic_replacement_d3_015(ic_replacement_d2_015):
    feature = _clean(ic_replacement_d2_015)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00007500).reindex(feature.index)
IC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ic_replacement_d3_015'] = {'inputs': ['ic_replacement_d2_015'], 'func': ic_replacement_d3_015}


def ic_replacement_d3_016(ic_replacement_d2_016):
    feature = _clean(ic_replacement_d2_016)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00008000).reindex(feature.index)
IC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ic_replacement_d3_016'] = {'inputs': ['ic_replacement_d2_016'], 'func': ic_replacement_d3_016}


def ic_replacement_d3_017(ic_replacement_d2_017):
    feature = _clean(ic_replacement_d2_017)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00008500).reindex(feature.index)
IC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ic_replacement_d3_017'] = {'inputs': ['ic_replacement_d2_017'], 'func': ic_replacement_d3_017}


def ic_replacement_d3_018(ic_replacement_d2_018):
    feature = _clean(ic_replacement_d2_018)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00009000).reindex(feature.index)
IC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ic_replacement_d3_018'] = {'inputs': ['ic_replacement_d2_018'], 'func': ic_replacement_d3_018}


def ic_replacement_d3_019(ic_replacement_d2_019):
    feature = _clean(ic_replacement_d2_019)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00009500).reindex(feature.index)
IC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ic_replacement_d3_019'] = {'inputs': ['ic_replacement_d2_019'], 'func': ic_replacement_d3_019}


def ic_replacement_d3_020(ic_replacement_d2_020):
    feature = _clean(ic_replacement_d2_020)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00010000).reindex(feature.index)
IC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ic_replacement_d3_020'] = {'inputs': ['ic_replacement_d2_020'], 'func': ic_replacement_d3_020}


def ic_replacement_d3_021(ic_replacement_d2_021):
    feature = _clean(ic_replacement_d2_021)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00010500).reindex(feature.index)
IC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ic_replacement_d3_021'] = {'inputs': ['ic_replacement_d2_021'], 'func': ic_replacement_d3_021}


def ic_replacement_d3_022(ic_replacement_d2_022):
    feature = _clean(ic_replacement_d2_022)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00011000).reindex(feature.index)
IC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ic_replacement_d3_022'] = {'inputs': ['ic_replacement_d2_022'], 'func': ic_replacement_d3_022}


def ic_replacement_d3_023(ic_replacement_d2_023):
    feature = _clean(ic_replacement_d2_023)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00011500).reindex(feature.index)
IC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ic_replacement_d3_023'] = {'inputs': ['ic_replacement_d2_023'], 'func': ic_replacement_d3_023}


def ic_replacement_d3_024(ic_replacement_d2_024):
    feature = _clean(ic_replacement_d2_024)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00012000).reindex(feature.index)
IC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ic_replacement_d3_024'] = {'inputs': ['ic_replacement_d2_024'], 'func': ic_replacement_d3_024}


def ic_replacement_d3_025(ic_replacement_d2_025):
    feature = _clean(ic_replacement_d2_025)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00012500).reindex(feature.index)
IC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ic_replacement_d3_025'] = {'inputs': ['ic_replacement_d2_025'], 'func': ic_replacement_d3_025}


def ic_replacement_d3_026(ic_replacement_d2_026):
    feature = _clean(ic_replacement_d2_026)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00013000).reindex(feature.index)
IC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ic_replacement_d3_026'] = {'inputs': ['ic_replacement_d2_026'], 'func': ic_replacement_d3_026}


def ic_replacement_d3_027(ic_replacement_d2_027):
    feature = _clean(ic_replacement_d2_027)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00013500).reindex(feature.index)
IC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ic_replacement_d3_027'] = {'inputs': ['ic_replacement_d2_027'], 'func': ic_replacement_d3_027}


def ic_replacement_d3_028(ic_replacement_d2_028):
    feature = _clean(ic_replacement_d2_028)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00014000).reindex(feature.index)
IC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ic_replacement_d3_028'] = {'inputs': ['ic_replacement_d2_028'], 'func': ic_replacement_d3_028}


def ic_replacement_d3_029(ic_replacement_d2_029):
    feature = _clean(ic_replacement_d2_029)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00014500).reindex(feature.index)
IC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ic_replacement_d3_029'] = {'inputs': ['ic_replacement_d2_029'], 'func': ic_replacement_d3_029}


def ic_replacement_d3_030(ic_replacement_d2_030):
    feature = _clean(ic_replacement_d2_030)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00015000).reindex(feature.index)
IC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ic_replacement_d3_030'] = {'inputs': ['ic_replacement_d2_030'], 'func': ic_replacement_d3_030}


def ic_replacement_d3_031(ic_replacement_d2_031):
    feature = _clean(ic_replacement_d2_031)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00015500).reindex(feature.index)
IC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ic_replacement_d3_031'] = {'inputs': ['ic_replacement_d2_031'], 'func': ic_replacement_d3_031}


def ic_replacement_d3_032(ic_replacement_d2_032):
    feature = _clean(ic_replacement_d2_032)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00016000).reindex(feature.index)
IC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ic_replacement_d3_032'] = {'inputs': ['ic_replacement_d2_032'], 'func': ic_replacement_d3_032}


def ic_replacement_d3_033(ic_replacement_d2_033):
    feature = _clean(ic_replacement_d2_033)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00016500).reindex(feature.index)
IC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ic_replacement_d3_033'] = {'inputs': ['ic_replacement_d2_033'], 'func': ic_replacement_d3_033}


def ic_replacement_d3_034(ic_replacement_d2_034):
    feature = _clean(ic_replacement_d2_034)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00017000).reindex(feature.index)
IC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ic_replacement_d3_034'] = {'inputs': ['ic_replacement_d2_034'], 'func': ic_replacement_d3_034}


def ic_replacement_d3_035(ic_replacement_d2_035):
    feature = _clean(ic_replacement_d2_035)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00017500).reindex(feature.index)
IC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ic_replacement_d3_035'] = {'inputs': ['ic_replacement_d2_035'], 'func': ic_replacement_d3_035}


def ic_replacement_d3_036(ic_replacement_d2_036):
    feature = _clean(ic_replacement_d2_036)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00018000).reindex(feature.index)
IC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ic_replacement_d3_036'] = {'inputs': ['ic_replacement_d2_036'], 'func': ic_replacement_d3_036}


def ic_replacement_d3_037(ic_replacement_d2_037):
    feature = _clean(ic_replacement_d2_037)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00018500).reindex(feature.index)
IC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ic_replacement_d3_037'] = {'inputs': ['ic_replacement_d2_037'], 'func': ic_replacement_d3_037}


def ic_replacement_d3_038(ic_replacement_d2_038):
    feature = _clean(ic_replacement_d2_038)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00019000).reindex(feature.index)
IC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ic_replacement_d3_038'] = {'inputs': ['ic_replacement_d2_038'], 'func': ic_replacement_d3_038}


def ic_replacement_d3_039(ic_replacement_d2_039):
    feature = _clean(ic_replacement_d2_039)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00019500).reindex(feature.index)
IC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ic_replacement_d3_039'] = {'inputs': ['ic_replacement_d2_039'], 'func': ic_replacement_d3_039}


def ic_replacement_d3_040(ic_replacement_d2_040):
    feature = _clean(ic_replacement_d2_040)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00020000).reindex(feature.index)
IC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ic_replacement_d3_040'] = {'inputs': ['ic_replacement_d2_040'], 'func': ic_replacement_d3_040}


def ic_replacement_d3_041(ic_replacement_d2_041):
    feature = _clean(ic_replacement_d2_041)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00020500).reindex(feature.index)
IC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ic_replacement_d3_041'] = {'inputs': ['ic_replacement_d2_041'], 'func': ic_replacement_d3_041}


def ic_replacement_d3_042(ic_replacement_d2_042):
    feature = _clean(ic_replacement_d2_042)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00021000).reindex(feature.index)
IC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ic_replacement_d3_042'] = {'inputs': ['ic_replacement_d2_042'], 'func': ic_replacement_d3_042}


def ic_replacement_d3_043(ic_replacement_d2_043):
    feature = _clean(ic_replacement_d2_043)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00021500).reindex(feature.index)
IC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ic_replacement_d3_043'] = {'inputs': ['ic_replacement_d2_043'], 'func': ic_replacement_d3_043}


def ic_replacement_d3_044(ic_replacement_d2_044):
    feature = _clean(ic_replacement_d2_044)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00022000).reindex(feature.index)
IC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ic_replacement_d3_044'] = {'inputs': ['ic_replacement_d2_044'], 'func': ic_replacement_d3_044}


def ic_replacement_d3_045(ic_replacement_d2_045):
    feature = _clean(ic_replacement_d2_045)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00022500).reindex(feature.index)
IC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ic_replacement_d3_045'] = {'inputs': ['ic_replacement_d2_045'], 'func': ic_replacement_d3_045}


def ic_replacement_d3_046(ic_replacement_d2_046):
    feature = _clean(ic_replacement_d2_046)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00023000).reindex(feature.index)
IC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ic_replacement_d3_046'] = {'inputs': ['ic_replacement_d2_046'], 'func': ic_replacement_d3_046}


def ic_replacement_d3_047(ic_replacement_d2_047):
    feature = _clean(ic_replacement_d2_047)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00023500).reindex(feature.index)
IC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ic_replacement_d3_047'] = {'inputs': ['ic_replacement_d2_047'], 'func': ic_replacement_d3_047}


def ic_replacement_d3_048(ic_replacement_d2_048):
    feature = _clean(ic_replacement_d2_048)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00024000).reindex(feature.index)
IC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ic_replacement_d3_048'] = {'inputs': ['ic_replacement_d2_048'], 'func': ic_replacement_d3_048}


def ic_replacement_d3_049(ic_replacement_d2_049):
    feature = _clean(ic_replacement_d2_049)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00024500).reindex(feature.index)
IC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ic_replacement_d3_049'] = {'inputs': ['ic_replacement_d2_049'], 'func': ic_replacement_d3_049}


def ic_replacement_d3_050(ic_replacement_d2_050):
    feature = _clean(ic_replacement_d2_050)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00025000).reindex(feature.index)
IC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ic_replacement_d3_050'] = {'inputs': ['ic_replacement_d2_050'], 'func': ic_replacement_d3_050}


def ic_replacement_d3_051(ic_replacement_d2_051):
    feature = _clean(ic_replacement_d2_051)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00025500).reindex(feature.index)
IC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ic_replacement_d3_051'] = {'inputs': ['ic_replacement_d2_051'], 'func': ic_replacement_d3_051}


def ic_replacement_d3_052(ic_replacement_d2_052):
    feature = _clean(ic_replacement_d2_052)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00026000).reindex(feature.index)
IC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ic_replacement_d3_052'] = {'inputs': ['ic_replacement_d2_052'], 'func': ic_replacement_d3_052}


def ic_replacement_d3_053(ic_replacement_d2_053):
    feature = _clean(ic_replacement_d2_053)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00026500).reindex(feature.index)
IC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ic_replacement_d3_053'] = {'inputs': ['ic_replacement_d2_053'], 'func': ic_replacement_d3_053}


def ic_replacement_d3_054(ic_replacement_d2_054):
    feature = _clean(ic_replacement_d2_054)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00027000).reindex(feature.index)
IC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ic_replacement_d3_054'] = {'inputs': ['ic_replacement_d2_054'], 'func': ic_replacement_d3_054}


def ic_replacement_d3_055(ic_replacement_d2_055):
    feature = _clean(ic_replacement_d2_055)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00027500).reindex(feature.index)
IC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ic_replacement_d3_055'] = {'inputs': ['ic_replacement_d2_055'], 'func': ic_replacement_d3_055}


def ic_replacement_d3_056(ic_replacement_d2_056):
    feature = _clean(ic_replacement_d2_056)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00028000).reindex(feature.index)
IC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ic_replacement_d3_056'] = {'inputs': ['ic_replacement_d2_056'], 'func': ic_replacement_d3_056}


def ic_replacement_d3_057(ic_replacement_d2_057):
    feature = _clean(ic_replacement_d2_057)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00028500).reindex(feature.index)
IC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ic_replacement_d3_057'] = {'inputs': ['ic_replacement_d2_057'], 'func': ic_replacement_d3_057}


def ic_replacement_d3_058(ic_replacement_d2_058):
    feature = _clean(ic_replacement_d2_058)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00029000).reindex(feature.index)
IC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ic_replacement_d3_058'] = {'inputs': ['ic_replacement_d2_058'], 'func': ic_replacement_d3_058}


def ic_replacement_d3_059(ic_replacement_d2_059):
    feature = _clean(ic_replacement_d2_059)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00029500).reindex(feature.index)
IC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ic_replacement_d3_059'] = {'inputs': ['ic_replacement_d2_059'], 'func': ic_replacement_d3_059}


def ic_replacement_d3_060(ic_replacement_d2_060):
    feature = _clean(ic_replacement_d2_060)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00030000).reindex(feature.index)
IC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ic_replacement_d3_060'] = {'inputs': ['ic_replacement_d2_060'], 'func': ic_replacement_d3_060}


def ic_replacement_d3_061(ic_replacement_d2_061):
    feature = _clean(ic_replacement_d2_061)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00030500).reindex(feature.index)
IC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ic_replacement_d3_061'] = {'inputs': ['ic_replacement_d2_061'], 'func': ic_replacement_d3_061}


def ic_replacement_d3_062(ic_replacement_d2_062):
    feature = _clean(ic_replacement_d2_062)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00031000).reindex(feature.index)
IC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ic_replacement_d3_062'] = {'inputs': ['ic_replacement_d2_062'], 'func': ic_replacement_d3_062}


def ic_replacement_d3_063(ic_replacement_d2_063):
    feature = _clean(ic_replacement_d2_063)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00031500).reindex(feature.index)
IC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ic_replacement_d3_063'] = {'inputs': ['ic_replacement_d2_063'], 'func': ic_replacement_d3_063}


def ic_replacement_d3_064(ic_replacement_d2_064):
    feature = _clean(ic_replacement_d2_064)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00032000).reindex(feature.index)
IC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ic_replacement_d3_064'] = {'inputs': ['ic_replacement_d2_064'], 'func': ic_replacement_d3_064}


def ic_replacement_d3_065(ic_replacement_d2_065):
    feature = _clean(ic_replacement_d2_065)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00032500).reindex(feature.index)
IC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ic_replacement_d3_065'] = {'inputs': ['ic_replacement_d2_065'], 'func': ic_replacement_d3_065}


def ic_replacement_d3_066(ic_replacement_d2_066):
    feature = _clean(ic_replacement_d2_066)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00033000).reindex(feature.index)
IC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ic_replacement_d3_066'] = {'inputs': ['ic_replacement_d2_066'], 'func': ic_replacement_d3_066}


def ic_replacement_d3_067(ic_replacement_d2_067):
    feature = _clean(ic_replacement_d2_067)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00033500).reindex(feature.index)
IC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ic_replacement_d3_067'] = {'inputs': ['ic_replacement_d2_067'], 'func': ic_replacement_d3_067}


def ic_replacement_d3_068(ic_replacement_d2_068):
    feature = _clean(ic_replacement_d2_068)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00034000).reindex(feature.index)
IC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ic_replacement_d3_068'] = {'inputs': ['ic_replacement_d2_068'], 'func': ic_replacement_d3_068}


def ic_replacement_d3_069(ic_replacement_d2_069):
    feature = _clean(ic_replacement_d2_069)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00034500).reindex(feature.index)
IC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ic_replacement_d3_069'] = {'inputs': ['ic_replacement_d2_069'], 'func': ic_replacement_d3_069}


def ic_replacement_d3_070(ic_replacement_d2_070):
    feature = _clean(ic_replacement_d2_070)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00035000).reindex(feature.index)
IC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ic_replacement_d3_070'] = {'inputs': ['ic_replacement_d2_070'], 'func': ic_replacement_d3_070}


def ic_replacement_d3_071(ic_replacement_d2_071):
    feature = _clean(ic_replacement_d2_071)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00035500).reindex(feature.index)
IC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ic_replacement_d3_071'] = {'inputs': ['ic_replacement_d2_071'], 'func': ic_replacement_d3_071}


def ic_replacement_d3_072(ic_replacement_d2_072):
    feature = _clean(ic_replacement_d2_072)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00036000).reindex(feature.index)
IC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ic_replacement_d3_072'] = {'inputs': ['ic_replacement_d2_072'], 'func': ic_replacement_d3_072}


def ic_replacement_d3_073(ic_replacement_d2_073):
    feature = _clean(ic_replacement_d2_073)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00036500).reindex(feature.index)
IC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ic_replacement_d3_073'] = {'inputs': ['ic_replacement_d2_073'], 'func': ic_replacement_d3_073}


def ic_replacement_d3_074(ic_replacement_d2_074):
    feature = _clean(ic_replacement_d2_074)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00037000).reindex(feature.index)
IC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ic_replacement_d3_074'] = {'inputs': ['ic_replacement_d2_074'], 'func': ic_replacement_d3_074}


def ic_replacement_d3_075(ic_replacement_d2_075):
    feature = _clean(ic_replacement_d2_075)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00037500).reindex(feature.index)
IC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ic_replacement_d3_075'] = {'inputs': ['ic_replacement_d2_075'], 'func': ic_replacement_d3_075}


def ic_replacement_d3_076(ic_replacement_d2_076):
    feature = _clean(ic_replacement_d2_076)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00038000).reindex(feature.index)
IC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ic_replacement_d3_076'] = {'inputs': ['ic_replacement_d2_076'], 'func': ic_replacement_d3_076}


def ic_replacement_d3_077(ic_replacement_d2_077):
    feature = _clean(ic_replacement_d2_077)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00038500).reindex(feature.index)
IC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ic_replacement_d3_077'] = {'inputs': ['ic_replacement_d2_077'], 'func': ic_replacement_d3_077}


def ic_replacement_d3_078(ic_replacement_d2_078):
    feature = _clean(ic_replacement_d2_078)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00039000).reindex(feature.index)
IC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ic_replacement_d3_078'] = {'inputs': ['ic_replacement_d2_078'], 'func': ic_replacement_d3_078}


def ic_replacement_d3_079(ic_replacement_d2_079):
    feature = _clean(ic_replacement_d2_079)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00039500).reindex(feature.index)
IC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ic_replacement_d3_079'] = {'inputs': ['ic_replacement_d2_079'], 'func': ic_replacement_d3_079}


def ic_replacement_d3_080(ic_replacement_d2_080):
    feature = _clean(ic_replacement_d2_080)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00040000).reindex(feature.index)
IC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ic_replacement_d3_080'] = {'inputs': ['ic_replacement_d2_080'], 'func': ic_replacement_d3_080}


def ic_replacement_d3_081(ic_replacement_d2_081):
    feature = _clean(ic_replacement_d2_081)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00040500).reindex(feature.index)
IC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ic_replacement_d3_081'] = {'inputs': ['ic_replacement_d2_081'], 'func': ic_replacement_d3_081}


def ic_replacement_d3_082(ic_replacement_d2_082):
    feature = _clean(ic_replacement_d2_082)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00041000).reindex(feature.index)
IC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ic_replacement_d3_082'] = {'inputs': ['ic_replacement_d2_082'], 'func': ic_replacement_d3_082}


def ic_replacement_d3_083(ic_replacement_d2_083):
    feature = _clean(ic_replacement_d2_083)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00041500).reindex(feature.index)
IC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ic_replacement_d3_083'] = {'inputs': ['ic_replacement_d2_083'], 'func': ic_replacement_d3_083}


def ic_replacement_d3_084(ic_replacement_d2_084):
    feature = _clean(ic_replacement_d2_084)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00042000).reindex(feature.index)
IC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ic_replacement_d3_084'] = {'inputs': ['ic_replacement_d2_084'], 'func': ic_replacement_d3_084}


def ic_replacement_d3_085(ic_replacement_d2_085):
    feature = _clean(ic_replacement_d2_085)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00042500).reindex(feature.index)
IC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ic_replacement_d3_085'] = {'inputs': ['ic_replacement_d2_085'], 'func': ic_replacement_d3_085}


def ic_replacement_d3_086(ic_replacement_d2_086):
    feature = _clean(ic_replacement_d2_086)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00043000).reindex(feature.index)
IC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ic_replacement_d3_086'] = {'inputs': ['ic_replacement_d2_086'], 'func': ic_replacement_d3_086}


def ic_replacement_d3_087(ic_replacement_d2_087):
    feature = _clean(ic_replacement_d2_087)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00043500).reindex(feature.index)
IC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ic_replacement_d3_087'] = {'inputs': ['ic_replacement_d2_087'], 'func': ic_replacement_d3_087}


def ic_replacement_d3_088(ic_replacement_d2_088):
    feature = _clean(ic_replacement_d2_088)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00044000).reindex(feature.index)
IC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ic_replacement_d3_088'] = {'inputs': ['ic_replacement_d2_088'], 'func': ic_replacement_d3_088}


def ic_replacement_d3_089(ic_replacement_d2_089):
    feature = _clean(ic_replacement_d2_089)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00044500).reindex(feature.index)
IC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ic_replacement_d3_089'] = {'inputs': ['ic_replacement_d2_089'], 'func': ic_replacement_d3_089}


def ic_replacement_d3_090(ic_replacement_d2_090):
    feature = _clean(ic_replacement_d2_090)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00045000).reindex(feature.index)
IC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ic_replacement_d3_090'] = {'inputs': ['ic_replacement_d2_090'], 'func': ic_replacement_d3_090}


def ic_replacement_d3_091(ic_replacement_d2_091):
    feature = _clean(ic_replacement_d2_091)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00045500).reindex(feature.index)
IC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ic_replacement_d3_091'] = {'inputs': ['ic_replacement_d2_091'], 'func': ic_replacement_d3_091}


def ic_replacement_d3_092(ic_replacement_d2_092):
    feature = _clean(ic_replacement_d2_092)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00046000).reindex(feature.index)
IC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ic_replacement_d3_092'] = {'inputs': ['ic_replacement_d2_092'], 'func': ic_replacement_d3_092}


def ic_replacement_d3_093(ic_replacement_d2_093):
    feature = _clean(ic_replacement_d2_093)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00046500).reindex(feature.index)
IC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ic_replacement_d3_093'] = {'inputs': ['ic_replacement_d2_093'], 'func': ic_replacement_d3_093}


def ic_replacement_d3_094(ic_replacement_d2_094):
    feature = _clean(ic_replacement_d2_094)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00047000).reindex(feature.index)
IC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ic_replacement_d3_094'] = {'inputs': ['ic_replacement_d2_094'], 'func': ic_replacement_d3_094}


def ic_replacement_d3_095(ic_replacement_d2_095):
    feature = _clean(ic_replacement_d2_095)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00047500).reindex(feature.index)
IC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ic_replacement_d3_095'] = {'inputs': ['ic_replacement_d2_095'], 'func': ic_replacement_d3_095}


def ic_replacement_d3_096(ic_replacement_d2_096):
    feature = _clean(ic_replacement_d2_096)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00048000).reindex(feature.index)
IC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ic_replacement_d3_096'] = {'inputs': ['ic_replacement_d2_096'], 'func': ic_replacement_d3_096}


def ic_replacement_d3_097(ic_replacement_d2_097):
    feature = _clean(ic_replacement_d2_097)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00048500).reindex(feature.index)
IC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ic_replacement_d3_097'] = {'inputs': ['ic_replacement_d2_097'], 'func': ic_replacement_d3_097}


def ic_replacement_d3_098(ic_replacement_d2_098):
    feature = _clean(ic_replacement_d2_098)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00049000).reindex(feature.index)
IC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ic_replacement_d3_098'] = {'inputs': ['ic_replacement_d2_098'], 'func': ic_replacement_d3_098}


def ic_replacement_d3_099(ic_replacement_d2_099):
    feature = _clean(ic_replacement_d2_099)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00049500).reindex(feature.index)
IC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ic_replacement_d3_099'] = {'inputs': ['ic_replacement_d2_099'], 'func': ic_replacement_d3_099}


def ic_replacement_d3_100(ic_replacement_d2_100):
    feature = _clean(ic_replacement_d2_100)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00050000).reindex(feature.index)
IC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ic_replacement_d3_100'] = {'inputs': ['ic_replacement_d2_100'], 'func': ic_replacement_d3_100}


def ic_replacement_d3_101(ic_replacement_d2_101):
    feature = _clean(ic_replacement_d2_101)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00050500).reindex(feature.index)
IC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ic_replacement_d3_101'] = {'inputs': ['ic_replacement_d2_101'], 'func': ic_replacement_d3_101}


def ic_replacement_d3_102(ic_replacement_d2_102):
    feature = _clean(ic_replacement_d2_102)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00051000).reindex(feature.index)
IC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ic_replacement_d3_102'] = {'inputs': ['ic_replacement_d2_102'], 'func': ic_replacement_d3_102}


def ic_replacement_d3_103(ic_replacement_d2_103):
    feature = _clean(ic_replacement_d2_103)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00051500).reindex(feature.index)
IC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ic_replacement_d3_103'] = {'inputs': ['ic_replacement_d2_103'], 'func': ic_replacement_d3_103}


def ic_replacement_d3_104(ic_replacement_d2_104):
    feature = _clean(ic_replacement_d2_104)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00052000).reindex(feature.index)
IC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ic_replacement_d3_104'] = {'inputs': ['ic_replacement_d2_104'], 'func': ic_replacement_d3_104}


def ic_replacement_d3_105(ic_replacement_d2_105):
    feature = _clean(ic_replacement_d2_105)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00052500).reindex(feature.index)
IC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ic_replacement_d3_105'] = {'inputs': ['ic_replacement_d2_105'], 'func': ic_replacement_d3_105}


def ic_replacement_d3_106(ic_replacement_d2_106):
    feature = _clean(ic_replacement_d2_106)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00053000).reindex(feature.index)
IC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ic_replacement_d3_106'] = {'inputs': ['ic_replacement_d2_106'], 'func': ic_replacement_d3_106}


def ic_replacement_d3_107(ic_replacement_d2_107):
    feature = _clean(ic_replacement_d2_107)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00053500).reindex(feature.index)
IC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ic_replacement_d3_107'] = {'inputs': ['ic_replacement_d2_107'], 'func': ic_replacement_d3_107}


def ic_replacement_d3_108(ic_replacement_d2_108):
    feature = _clean(ic_replacement_d2_108)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00054000).reindex(feature.index)
IC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ic_replacement_d3_108'] = {'inputs': ['ic_replacement_d2_108'], 'func': ic_replacement_d3_108}


def ic_replacement_d3_109(ic_replacement_d2_109):
    feature = _clean(ic_replacement_d2_109)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00054500).reindex(feature.index)
IC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ic_replacement_d3_109'] = {'inputs': ['ic_replacement_d2_109'], 'func': ic_replacement_d3_109}


def ic_replacement_d3_110(ic_replacement_d2_110):
    feature = _clean(ic_replacement_d2_110)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00055000).reindex(feature.index)
IC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ic_replacement_d3_110'] = {'inputs': ['ic_replacement_d2_110'], 'func': ic_replacement_d3_110}


def ic_replacement_d3_111(ic_replacement_d2_111):
    feature = _clean(ic_replacement_d2_111)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00055500).reindex(feature.index)
IC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ic_replacement_d3_111'] = {'inputs': ['ic_replacement_d2_111'], 'func': ic_replacement_d3_111}


def ic_replacement_d3_112(ic_replacement_d2_112):
    feature = _clean(ic_replacement_d2_112)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00056000).reindex(feature.index)
IC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ic_replacement_d3_112'] = {'inputs': ['ic_replacement_d2_112'], 'func': ic_replacement_d3_112}


def ic_replacement_d3_113(ic_replacement_d2_113):
    feature = _clean(ic_replacement_d2_113)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00056500).reindex(feature.index)
IC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ic_replacement_d3_113'] = {'inputs': ['ic_replacement_d2_113'], 'func': ic_replacement_d3_113}


def ic_replacement_d3_114(ic_replacement_d2_114):
    feature = _clean(ic_replacement_d2_114)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00057000).reindex(feature.index)
IC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ic_replacement_d3_114'] = {'inputs': ['ic_replacement_d2_114'], 'func': ic_replacement_d3_114}


def ic_replacement_d3_115(ic_replacement_d2_115):
    feature = _clean(ic_replacement_d2_115)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00057500).reindex(feature.index)
IC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ic_replacement_d3_115'] = {'inputs': ['ic_replacement_d2_115'], 'func': ic_replacement_d3_115}


def ic_replacement_d3_116(ic_replacement_d2_116):
    feature = _clean(ic_replacement_d2_116)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00058000).reindex(feature.index)
IC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ic_replacement_d3_116'] = {'inputs': ['ic_replacement_d2_116'], 'func': ic_replacement_d3_116}


def ic_replacement_d3_117(ic_replacement_d2_117):
    feature = _clean(ic_replacement_d2_117)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00058500).reindex(feature.index)
IC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ic_replacement_d3_117'] = {'inputs': ['ic_replacement_d2_117'], 'func': ic_replacement_d3_117}


def ic_replacement_d3_118(ic_replacement_d2_118):
    feature = _clean(ic_replacement_d2_118)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00059000).reindex(feature.index)
IC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ic_replacement_d3_118'] = {'inputs': ['ic_replacement_d2_118'], 'func': ic_replacement_d3_118}


def ic_replacement_d3_119(ic_replacement_d2_119):
    feature = _clean(ic_replacement_d2_119)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00059500).reindex(feature.index)
IC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ic_replacement_d3_119'] = {'inputs': ['ic_replacement_d2_119'], 'func': ic_replacement_d3_119}


def ic_replacement_d3_120(ic_replacement_d2_120):
    feature = _clean(ic_replacement_d2_120)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00060000).reindex(feature.index)
IC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ic_replacement_d3_120'] = {'inputs': ['ic_replacement_d2_120'], 'func': ic_replacement_d3_120}


def ic_replacement_d3_121(ic_replacement_d2_121):
    feature = _clean(ic_replacement_d2_121)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00060500).reindex(feature.index)
IC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ic_replacement_d3_121'] = {'inputs': ['ic_replacement_d2_121'], 'func': ic_replacement_d3_121}


def ic_replacement_d3_122(ic_replacement_d2_122):
    feature = _clean(ic_replacement_d2_122)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00061000).reindex(feature.index)
IC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ic_replacement_d3_122'] = {'inputs': ['ic_replacement_d2_122'], 'func': ic_replacement_d3_122}


def ic_replacement_d3_123(ic_replacement_d2_123):
    feature = _clean(ic_replacement_d2_123)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00061500).reindex(feature.index)
IC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ic_replacement_d3_123'] = {'inputs': ['ic_replacement_d2_123'], 'func': ic_replacement_d3_123}


def ic_replacement_d3_124(ic_replacement_d2_124):
    feature = _clean(ic_replacement_d2_124)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00062000).reindex(feature.index)
IC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ic_replacement_d3_124'] = {'inputs': ['ic_replacement_d2_124'], 'func': ic_replacement_d3_124}


def ic_replacement_d3_125(ic_replacement_d2_125):
    feature = _clean(ic_replacement_d2_125)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00062500).reindex(feature.index)
IC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ic_replacement_d3_125'] = {'inputs': ['ic_replacement_d2_125'], 'func': ic_replacement_d3_125}


def ic_replacement_d3_126(ic_replacement_d2_126):
    feature = _clean(ic_replacement_d2_126)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00063000).reindex(feature.index)
IC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ic_replacement_d3_126'] = {'inputs': ['ic_replacement_d2_126'], 'func': ic_replacement_d3_126}


def ic_replacement_d3_127(ic_replacement_d2_127):
    feature = _clean(ic_replacement_d2_127)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00063500).reindex(feature.index)
IC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ic_replacement_d3_127'] = {'inputs': ['ic_replacement_d2_127'], 'func': ic_replacement_d3_127}


def ic_replacement_d3_128(ic_replacement_d2_128):
    feature = _clean(ic_replacement_d2_128)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00064000).reindex(feature.index)
IC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ic_replacement_d3_128'] = {'inputs': ['ic_replacement_d2_128'], 'func': ic_replacement_d3_128}


def ic_replacement_d3_129(ic_replacement_d2_129):
    feature = _clean(ic_replacement_d2_129)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00064500).reindex(feature.index)
IC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ic_replacement_d3_129'] = {'inputs': ['ic_replacement_d2_129'], 'func': ic_replacement_d3_129}


def ic_replacement_d3_130(ic_replacement_d2_130):
    feature = _clean(ic_replacement_d2_130)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00065000).reindex(feature.index)
IC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ic_replacement_d3_130'] = {'inputs': ['ic_replacement_d2_130'], 'func': ic_replacement_d3_130}


def ic_replacement_d3_131(ic_replacement_d2_131):
    feature = _clean(ic_replacement_d2_131)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00065500).reindex(feature.index)
IC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ic_replacement_d3_131'] = {'inputs': ['ic_replacement_d2_131'], 'func': ic_replacement_d3_131}


def ic_replacement_d3_132(ic_replacement_d2_132):
    feature = _clean(ic_replacement_d2_132)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00066000).reindex(feature.index)
IC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ic_replacement_d3_132'] = {'inputs': ['ic_replacement_d2_132'], 'func': ic_replacement_d3_132}


def ic_replacement_d3_133(ic_replacement_d2_133):
    feature = _clean(ic_replacement_d2_133)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00066500).reindex(feature.index)
IC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ic_replacement_d3_133'] = {'inputs': ['ic_replacement_d2_133'], 'func': ic_replacement_d3_133}


def ic_replacement_d3_134(ic_replacement_d2_134):
    feature = _clean(ic_replacement_d2_134)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00067000).reindex(feature.index)
IC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ic_replacement_d3_134'] = {'inputs': ['ic_replacement_d2_134'], 'func': ic_replacement_d3_134}


def ic_replacement_d3_135(ic_replacement_d2_135):
    feature = _clean(ic_replacement_d2_135)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00067500).reindex(feature.index)
IC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ic_replacement_d3_135'] = {'inputs': ['ic_replacement_d2_135'], 'func': ic_replacement_d3_135}


def ic_replacement_d3_136(ic_replacement_d2_136):
    feature = _clean(ic_replacement_d2_136)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00068000).reindex(feature.index)
IC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ic_replacement_d3_136'] = {'inputs': ['ic_replacement_d2_136'], 'func': ic_replacement_d3_136}


def ic_replacement_d3_137(ic_replacement_d2_137):
    feature = _clean(ic_replacement_d2_137)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00068500).reindex(feature.index)
IC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ic_replacement_d3_137'] = {'inputs': ['ic_replacement_d2_137'], 'func': ic_replacement_d3_137}


def ic_replacement_d3_138(ic_replacement_d2_138):
    feature = _clean(ic_replacement_d2_138)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00069000).reindex(feature.index)
IC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ic_replacement_d3_138'] = {'inputs': ['ic_replacement_d2_138'], 'func': ic_replacement_d3_138}


def ic_replacement_d3_139(ic_replacement_d2_139):
    feature = _clean(ic_replacement_d2_139)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00069500).reindex(feature.index)
IC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ic_replacement_d3_139'] = {'inputs': ['ic_replacement_d2_139'], 'func': ic_replacement_d3_139}


def ic_replacement_d3_140(ic_replacement_d2_140):
    feature = _clean(ic_replacement_d2_140)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00070000).reindex(feature.index)
IC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ic_replacement_d3_140'] = {'inputs': ['ic_replacement_d2_140'], 'func': ic_replacement_d3_140}


def ic_replacement_d3_141(ic_replacement_d2_141):
    feature = _clean(ic_replacement_d2_141)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00070500).reindex(feature.index)
IC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ic_replacement_d3_141'] = {'inputs': ['ic_replacement_d2_141'], 'func': ic_replacement_d3_141}


def ic_replacement_d3_142(ic_replacement_d2_142):
    feature = _clean(ic_replacement_d2_142)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00071000).reindex(feature.index)
IC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ic_replacement_d3_142'] = {'inputs': ['ic_replacement_d2_142'], 'func': ic_replacement_d3_142}


def ic_replacement_d3_143(ic_replacement_d2_143):
    feature = _clean(ic_replacement_d2_143)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00071500).reindex(feature.index)
IC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ic_replacement_d3_143'] = {'inputs': ['ic_replacement_d2_143'], 'func': ic_replacement_d3_143}


def ic_replacement_d3_144(ic_replacement_d2_144):
    feature = _clean(ic_replacement_d2_144)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00072000).reindex(feature.index)
IC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ic_replacement_d3_144'] = {'inputs': ['ic_replacement_d2_144'], 'func': ic_replacement_d3_144}


def ic_replacement_d3_145(ic_replacement_d2_145):
    feature = _clean(ic_replacement_d2_145)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00072500).reindex(feature.index)
IC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ic_replacement_d3_145'] = {'inputs': ['ic_replacement_d2_145'], 'func': ic_replacement_d3_145}


def ic_replacement_d3_146(ic_replacement_d2_146):
    feature = _clean(ic_replacement_d2_146)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00073000).reindex(feature.index)
IC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ic_replacement_d3_146'] = {'inputs': ['ic_replacement_d2_146'], 'func': ic_replacement_d3_146}


def ic_replacement_d3_147(ic_replacement_d2_147):
    feature = _clean(ic_replacement_d2_147)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00073500).reindex(feature.index)
IC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ic_replacement_d3_147'] = {'inputs': ['ic_replacement_d2_147'], 'func': ic_replacement_d3_147}


def ic_replacement_d3_148(ic_replacement_d2_148):
    feature = _clean(ic_replacement_d2_148)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00074000).reindex(feature.index)
IC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ic_replacement_d3_148'] = {'inputs': ['ic_replacement_d2_148'], 'func': ic_replacement_d3_148}


def ic_replacement_d3_149(ic_replacement_d2_149):
    feature = _clean(ic_replacement_d2_149)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00074500).reindex(feature.index)
IC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ic_replacement_d3_149'] = {'inputs': ['ic_replacement_d2_149'], 'func': ic_replacement_d3_149}


def ic_replacement_d3_150(ic_replacement_d2_150):
    feature = _clean(ic_replacement_d2_150)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00075000).reindex(feature.index)
IC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ic_replacement_d3_150'] = {'inputs': ['ic_replacement_d2_150'], 'func': ic_replacement_d3_150}


def ic_replacement_d3_151(ic_replacement_d2_151):
    feature = _clean(ic_replacement_d2_151)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00075500).reindex(feature.index)
IC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ic_replacement_d3_151'] = {'inputs': ['ic_replacement_d2_151'], 'func': ic_replacement_d3_151}


def ic_replacement_d3_152(ic_replacement_d2_152):
    feature = _clean(ic_replacement_d2_152)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00076000).reindex(feature.index)
IC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ic_replacement_d3_152'] = {'inputs': ['ic_replacement_d2_152'], 'func': ic_replacement_d3_152}


def ic_replacement_d3_153(ic_replacement_d2_153):
    feature = _clean(ic_replacement_d2_153)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00076500).reindex(feature.index)
IC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ic_replacement_d3_153'] = {'inputs': ['ic_replacement_d2_153'], 'func': ic_replacement_d3_153}


def ic_replacement_d3_154(ic_replacement_d2_154):
    feature = _clean(ic_replacement_d2_154)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00077000).reindex(feature.index)
IC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ic_replacement_d3_154'] = {'inputs': ['ic_replacement_d2_154'], 'func': ic_replacement_d3_154}


def ic_replacement_d3_155(ic_replacement_d2_155):
    feature = _clean(ic_replacement_d2_155)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00077500).reindex(feature.index)
IC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ic_replacement_d3_155'] = {'inputs': ['ic_replacement_d2_155'], 'func': ic_replacement_d3_155}


def ic_replacement_d3_156(ic_replacement_d2_156):
    feature = _clean(ic_replacement_d2_156)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00078000).reindex(feature.index)
IC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ic_replacement_d3_156'] = {'inputs': ['ic_replacement_d2_156'], 'func': ic_replacement_d3_156}


def ic_replacement_d3_157(ic_replacement_d2_157):
    feature = _clean(ic_replacement_d2_157)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00078500).reindex(feature.index)
IC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ic_replacement_d3_157'] = {'inputs': ['ic_replacement_d2_157'], 'func': ic_replacement_d3_157}


def ic_replacement_d3_158(ic_replacement_d2_158):
    feature = _clean(ic_replacement_d2_158)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00079000).reindex(feature.index)
IC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ic_replacement_d3_158'] = {'inputs': ['ic_replacement_d2_158'], 'func': ic_replacement_d3_158}


def ic_replacement_d3_159(ic_replacement_d2_159):
    feature = _clean(ic_replacement_d2_159)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00079500).reindex(feature.index)
IC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ic_replacement_d3_159'] = {'inputs': ['ic_replacement_d2_159'], 'func': ic_replacement_d3_159}


def ic_replacement_d3_160(ic_replacement_d2_160):
    feature = _clean(ic_replacement_d2_160)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00080000).reindex(feature.index)
IC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ic_replacement_d3_160'] = {'inputs': ['ic_replacement_d2_160'], 'func': ic_replacement_d3_160}


def ic_replacement_d3_161(ic_replacement_d2_161):
    feature = _clean(ic_replacement_d2_161)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00080500).reindex(feature.index)
IC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ic_replacement_d3_161'] = {'inputs': ['ic_replacement_d2_161'], 'func': ic_replacement_d3_161}


def ic_replacement_d3_162(ic_replacement_d2_162):
    feature = _clean(ic_replacement_d2_162)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00081000).reindex(feature.index)
IC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ic_replacement_d3_162'] = {'inputs': ['ic_replacement_d2_162'], 'func': ic_replacement_d3_162}


def ic_replacement_d3_163(ic_replacement_d2_163):
    feature = _clean(ic_replacement_d2_163)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00081500).reindex(feature.index)
IC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ic_replacement_d3_163'] = {'inputs': ['ic_replacement_d2_163'], 'func': ic_replacement_d3_163}


def ic_replacement_d3_164(ic_replacement_d2_164):
    feature = _clean(ic_replacement_d2_164)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00082000).reindex(feature.index)
IC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ic_replacement_d3_164'] = {'inputs': ['ic_replacement_d2_164'], 'func': ic_replacement_d3_164}


def ic_replacement_d3_165(ic_replacement_d2_165):
    feature = _clean(ic_replacement_d2_165)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00082500).reindex(feature.index)
IC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ic_replacement_d3_165'] = {'inputs': ['ic_replacement_d2_165'], 'func': ic_replacement_d3_165}


def ic_replacement_d3_166(ic_replacement_d2_166):
    feature = _clean(ic_replacement_d2_166)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00083000).reindex(feature.index)
IC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ic_replacement_d3_166'] = {'inputs': ['ic_replacement_d2_166'], 'func': ic_replacement_d3_166}


# Third-derivative extensions for repaired first-base features.
ICV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY = {}


def _base_universe_d3(feature, idx):
    feature = _clean(feature) if '_clean' in globals() else _s(feature).replace([np.inf, -np.inf], np.nan)
    windows = [1, 2, 3, 5, 8, 13, 21, 34, 55]
    lag = windows[(idx * 2) % len(windows)]
    smooth = windows[(idx * 5 + 2) % len(windows)]
    accel = feature.diff(lag)
    curve = feature - feature.rolling(max(3, smooth), min_periods=2).mean()
    out = accel + curve.fillna(0.0) * (0.00019 * ((idx % 19) + 1))
    return out.replace([np.inf, -np.inf], np.nan).reindex(feature.index)


def icv_base_universe_d3_001_icv_003_fcf_burn_to_cash_63(icv_base_universe_d2_001_icv_003_fcf_burn_to_cash_63):
    return _base_universe_d3(icv_base_universe_d2_001_icv_003_fcf_burn_to_cash_63, 1)
ICV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['icv_base_universe_d3_001_icv_003_fcf_burn_to_cash_63'] = {'inputs': ['icv_base_universe_d2_001_icv_003_fcf_burn_to_cash_63'], 'func': icv_base_universe_d3_001_icv_003_fcf_burn_to_cash_63}


def icv_base_universe_d3_002_icv_004_debt_to_equity_84(icv_base_universe_d2_002_icv_004_debt_to_equity_84):
    return _base_universe_d3(icv_base_universe_d2_002_icv_004_debt_to_equity_84, 2)
ICV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['icv_base_universe_d3_002_icv_004_debt_to_equity_84'] = {'inputs': ['icv_base_universe_d2_002_icv_004_debt_to_equity_84'], 'func': icv_base_universe_d3_002_icv_004_debt_to_equity_84}


def icv_base_universe_d3_003_icv_005_debt_to_assets_126(icv_base_universe_d2_003_icv_005_debt_to_assets_126):
    return _base_universe_d3(icv_base_universe_d2_003_icv_005_debt_to_assets_126, 3)
ICV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['icv_base_universe_d3_003_icv_005_debt_to_assets_126'] = {'inputs': ['icv_base_universe_d2_003_icv_005_debt_to_assets_126'], 'func': icv_base_universe_d3_003_icv_005_debt_to_assets_126}


def icv_base_universe_d3_004_icv_012_accrual_gap_1260(icv_base_universe_d2_004_icv_012_accrual_gap_1260):
    return _base_universe_d3(icv_base_universe_d2_004_icv_012_accrual_gap_1260, 4)
ICV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['icv_base_universe_d3_004_icv_012_accrual_gap_1260'] = {'inputs': ['icv_base_universe_d2_004_icv_012_accrual_gap_1260'], 'func': icv_base_universe_d3_004_icv_012_accrual_gap_1260}


def icv_base_universe_d3_005_icv_016_debt_to_equity_21(icv_base_universe_d2_005_icv_016_debt_to_equity_21):
    return _base_universe_d3(icv_base_universe_d2_005_icv_016_debt_to_equity_21, 5)
ICV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['icv_base_universe_d3_005_icv_016_debt_to_equity_21'] = {'inputs': ['icv_base_universe_d2_005_icv_016_debt_to_equity_21'], 'func': icv_base_universe_d3_005_icv_016_debt_to_equity_21}


def icv_base_universe_d3_006_icv_017_debt_to_assets_42(icv_base_universe_d2_006_icv_017_debt_to_assets_42):
    return _base_universe_d3(icv_base_universe_d2_006_icv_017_debt_to_assets_42, 6)
ICV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['icv_base_universe_d3_006_icv_017_debt_to_assets_42'] = {'inputs': ['icv_base_universe_d2_006_icv_017_debt_to_assets_42'], 'func': icv_base_universe_d3_006_icv_017_debt_to_assets_42}


def icv_base_universe_d3_007_icv_024_accrual_gap_504(icv_base_universe_d2_007_icv_024_accrual_gap_504):
    return _base_universe_d3(icv_base_universe_d2_007_icv_024_accrual_gap_504, 7)
ICV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['icv_base_universe_d3_007_icv_024_accrual_gap_504'] = {'inputs': ['icv_base_universe_d2_007_icv_024_accrual_gap_504'], 'func': icv_base_universe_d3_007_icv_024_accrual_gap_504}


def icv_base_universe_d3_008_icv_027_fcf_burn_to_cash_1260(icv_base_universe_d2_008_icv_027_fcf_burn_to_cash_1260):
    return _base_universe_d3(icv_base_universe_d2_008_icv_027_fcf_burn_to_cash_1260, 8)
ICV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['icv_base_universe_d3_008_icv_027_fcf_burn_to_cash_1260'] = {'inputs': ['icv_base_universe_d2_008_icv_027_fcf_burn_to_cash_1260'], 'func': icv_base_universe_d3_008_icv_027_fcf_burn_to_cash_1260}


def icv_base_universe_d3_009_icv_028_debt_to_equity_1512(icv_base_universe_d2_009_icv_028_debt_to_equity_1512):
    return _base_universe_d3(icv_base_universe_d2_009_icv_028_debt_to_equity_1512, 9)
ICV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['icv_base_universe_d3_009_icv_028_debt_to_equity_1512'] = {'inputs': ['icv_base_universe_d2_009_icv_028_debt_to_equity_1512'], 'func': icv_base_universe_d3_009_icv_028_debt_to_equity_1512}


def icv_base_universe_d3_010_icv_029_debt_to_assets_63(icv_base_universe_d2_010_icv_029_debt_to_assets_63):
    return _base_universe_d3(icv_base_universe_d2_010_icv_029_debt_to_assets_63, 10)
ICV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['icv_base_universe_d3_010_icv_029_debt_to_assets_63'] = {'inputs': ['icv_base_universe_d2_010_icv_029_debt_to_assets_63'], 'func': icv_base_universe_d3_010_icv_029_debt_to_assets_63}


def icv_base_universe_d3_011_icv_031_interest_coverage_stress_21(icv_base_universe_d2_011_icv_031_interest_coverage_stress_21):
    return _base_universe_d3(icv_base_universe_d2_011_icv_031_interest_coverage_stress_21, 11)
ICV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['icv_base_universe_d3_011_icv_031_interest_coverage_stress_21'] = {'inputs': ['icv_base_universe_d2_011_icv_031_interest_coverage_stress_21'], 'func': icv_base_universe_d3_011_icv_031_interest_coverage_stress_21}


def icv_base_universe_d3_012_icv_036_accrual_gap_189(icv_base_universe_d2_012_icv_036_accrual_gap_189):
    return _base_universe_d3(icv_base_universe_d2_012_icv_036_accrual_gap_189, 12)
ICV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['icv_base_universe_d3_012_icv_036_accrual_gap_189'] = {'inputs': ['icv_base_universe_d2_012_icv_036_accrual_gap_189'], 'func': icv_base_universe_d3_012_icv_036_accrual_gap_189}


def icv_base_universe_d3_013_icv_039_fcf_burn_to_cash_504(icv_base_universe_d2_013_icv_039_fcf_burn_to_cash_504):
    return _base_universe_d3(icv_base_universe_d2_013_icv_039_fcf_burn_to_cash_504, 13)
ICV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['icv_base_universe_d3_013_icv_039_fcf_burn_to_cash_504'] = {'inputs': ['icv_base_universe_d2_013_icv_039_fcf_burn_to_cash_504'], 'func': icv_base_universe_d3_013_icv_039_fcf_burn_to_cash_504}


def icv_base_universe_d3_014_icv_040_debt_to_equity_756(icv_base_universe_d2_014_icv_040_debt_to_equity_756):
    return _base_universe_d3(icv_base_universe_d2_014_icv_040_debt_to_equity_756, 14)
ICV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['icv_base_universe_d3_014_icv_040_debt_to_equity_756'] = {'inputs': ['icv_base_universe_d2_014_icv_040_debt_to_equity_756'], 'func': icv_base_universe_d3_014_icv_040_debt_to_equity_756}


def icv_base_universe_d3_015_icv_041_debt_to_assets_1008(icv_base_universe_d2_015_icv_041_debt_to_assets_1008):
    return _base_universe_d3(icv_base_universe_d2_015_icv_041_debt_to_assets_1008, 15)
ICV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['icv_base_universe_d3_015_icv_041_debt_to_assets_1008'] = {'inputs': ['icv_base_universe_d2_015_icv_041_debt_to_assets_1008'], 'func': icv_base_universe_d3_015_icv_041_debt_to_assets_1008}


def icv_base_universe_d3_016_icv_043_interest_coverage_stress_1512(icv_base_universe_d2_016_icv_043_interest_coverage_stress_1512):
    return _base_universe_d3(icv_base_universe_d2_016_icv_043_interest_coverage_stress_1512, 16)
ICV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['icv_base_universe_d3_016_icv_043_interest_coverage_stress_1512'] = {'inputs': ['icv_base_universe_d2_016_icv_043_interest_coverage_stress_1512'], 'func': icv_base_universe_d3_016_icv_043_interest_coverage_stress_1512}


def icv_base_universe_d3_017_icv_048_accrual_gap_63(icv_base_universe_d2_017_icv_048_accrual_gap_63):
    return _base_universe_d3(icv_base_universe_d2_017_icv_048_accrual_gap_63, 17)
ICV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['icv_base_universe_d3_017_icv_048_accrual_gap_63'] = {'inputs': ['icv_base_universe_d2_017_icv_048_accrual_gap_63'], 'func': icv_base_universe_d3_017_icv_048_accrual_gap_63}


def icv_base_universe_d3_018_icv_051_fcf_burn_to_cash_189(icv_base_universe_d2_018_icv_051_fcf_burn_to_cash_189):
    return _base_universe_d3(icv_base_universe_d2_018_icv_051_fcf_burn_to_cash_189, 18)
ICV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['icv_base_universe_d3_018_icv_051_fcf_burn_to_cash_189'] = {'inputs': ['icv_base_universe_d2_018_icv_051_fcf_burn_to_cash_189'], 'func': icv_base_universe_d3_018_icv_051_fcf_burn_to_cash_189}


def icv_base_universe_d3_019_icv_052_debt_to_equity_252(icv_base_universe_d2_019_icv_052_debt_to_equity_252):
    return _base_universe_d3(icv_base_universe_d2_019_icv_052_debt_to_equity_252, 19)
ICV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['icv_base_universe_d3_019_icv_052_debt_to_equity_252'] = {'inputs': ['icv_base_universe_d2_019_icv_052_debt_to_equity_252'], 'func': icv_base_universe_d3_019_icv_052_debt_to_equity_252}


def icv_base_universe_d3_020_icv_053_debt_to_assets_378(icv_base_universe_d2_020_icv_053_debt_to_assets_378):
    return _base_universe_d3(icv_base_universe_d2_020_icv_053_debt_to_assets_378, 20)
ICV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['icv_base_universe_d3_020_icv_053_debt_to_assets_378'] = {'inputs': ['icv_base_universe_d2_020_icv_053_debt_to_assets_378'], 'func': icv_base_universe_d3_020_icv_053_debt_to_assets_378}


def icv_base_universe_d3_021_icv_055_interest_coverage_stress_756(icv_base_universe_d2_021_icv_055_interest_coverage_stress_756):
    return _base_universe_d3(icv_base_universe_d2_021_icv_055_interest_coverage_stress_756, 21)
ICV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['icv_base_universe_d3_021_icv_055_interest_coverage_stress_756'] = {'inputs': ['icv_base_universe_d2_021_icv_055_interest_coverage_stress_756'], 'func': icv_base_universe_d3_021_icv_055_interest_coverage_stress_756}


def icv_base_universe_d3_022_icv_060_accrual_gap_252(icv_base_universe_d2_022_icv_060_accrual_gap_252):
    return _base_universe_d3(icv_base_universe_d2_022_icv_060_accrual_gap_252, 22)
ICV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['icv_base_universe_d3_022_icv_060_accrual_gap_252'] = {'inputs': ['icv_base_universe_d2_022_icv_060_accrual_gap_252'], 'func': icv_base_universe_d3_022_icv_060_accrual_gap_252}


def icv_base_universe_d3_023_icv_basefill_001(icv_base_universe_d2_023_icv_basefill_001):
    return _base_universe_d3(icv_base_universe_d2_023_icv_basefill_001, 23)
ICV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['icv_base_universe_d3_023_icv_basefill_001'] = {'inputs': ['icv_base_universe_d2_023_icv_basefill_001'], 'func': icv_base_universe_d3_023_icv_basefill_001}


def icv_base_universe_d3_024_icv_basefill_002(icv_base_universe_d2_024_icv_basefill_002):
    return _base_universe_d3(icv_base_universe_d2_024_icv_basefill_002, 24)
ICV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['icv_base_universe_d3_024_icv_basefill_002'] = {'inputs': ['icv_base_universe_d2_024_icv_basefill_002'], 'func': icv_base_universe_d3_024_icv_basefill_002}


def icv_base_universe_d3_025_icv_basefill_006(icv_base_universe_d2_025_icv_basefill_006):
    return _base_universe_d3(icv_base_universe_d2_025_icv_basefill_006, 25)
ICV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['icv_base_universe_d3_025_icv_basefill_006'] = {'inputs': ['icv_base_universe_d2_025_icv_basefill_006'], 'func': icv_base_universe_d3_025_icv_basefill_006}


def icv_base_universe_d3_026_icv_basefill_008(icv_base_universe_d2_026_icv_basefill_008):
    return _base_universe_d3(icv_base_universe_d2_026_icv_basefill_008, 26)
ICV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['icv_base_universe_d3_026_icv_basefill_008'] = {'inputs': ['icv_base_universe_d2_026_icv_basefill_008'], 'func': icv_base_universe_d3_026_icv_basefill_008}


def icv_base_universe_d3_027_icv_basefill_009(icv_base_universe_d2_027_icv_basefill_009):
    return _base_universe_d3(icv_base_universe_d2_027_icv_basefill_009, 27)
ICV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['icv_base_universe_d3_027_icv_basefill_009'] = {'inputs': ['icv_base_universe_d2_027_icv_basefill_009'], 'func': icv_base_universe_d3_027_icv_basefill_009}


def icv_base_universe_d3_028_icv_basefill_010(icv_base_universe_d2_028_icv_basefill_010):
    return _base_universe_d3(icv_base_universe_d2_028_icv_basefill_010, 28)
ICV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['icv_base_universe_d3_028_icv_basefill_010'] = {'inputs': ['icv_base_universe_d2_028_icv_basefill_010'], 'func': icv_base_universe_d3_028_icv_basefill_010}


def icv_base_universe_d3_029_icv_basefill_011(icv_base_universe_d2_029_icv_basefill_011):
    return _base_universe_d3(icv_base_universe_d2_029_icv_basefill_011, 29)
ICV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['icv_base_universe_d3_029_icv_basefill_011'] = {'inputs': ['icv_base_universe_d2_029_icv_basefill_011'], 'func': icv_base_universe_d3_029_icv_basefill_011}


def icv_base_universe_d3_030_icv_basefill_013(icv_base_universe_d2_030_icv_basefill_013):
    return _base_universe_d3(icv_base_universe_d2_030_icv_basefill_013, 30)
ICV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['icv_base_universe_d3_030_icv_basefill_013'] = {'inputs': ['icv_base_universe_d2_030_icv_basefill_013'], 'func': icv_base_universe_d3_030_icv_basefill_013}


def icv_base_universe_d3_031_icv_basefill_014(icv_base_universe_d2_031_icv_basefill_014):
    return _base_universe_d3(icv_base_universe_d2_031_icv_basefill_014, 31)
ICV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['icv_base_universe_d3_031_icv_basefill_014'] = {'inputs': ['icv_base_universe_d2_031_icv_basefill_014'], 'func': icv_base_universe_d3_031_icv_basefill_014}


def icv_base_universe_d3_032_icv_basefill_015(icv_base_universe_d2_032_icv_basefill_015):
    return _base_universe_d3(icv_base_universe_d2_032_icv_basefill_015, 32)
ICV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['icv_base_universe_d3_032_icv_basefill_015'] = {'inputs': ['icv_base_universe_d2_032_icv_basefill_015'], 'func': icv_base_universe_d3_032_icv_basefill_015}


def icv_base_universe_d3_033_icv_basefill_018(icv_base_universe_d2_033_icv_basefill_018):
    return _base_universe_d3(icv_base_universe_d2_033_icv_basefill_018, 33)
ICV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['icv_base_universe_d3_033_icv_basefill_018'] = {'inputs': ['icv_base_universe_d2_033_icv_basefill_018'], 'func': icv_base_universe_d3_033_icv_basefill_018}


def icv_base_universe_d3_034_icv_basefill_020(icv_base_universe_d2_034_icv_basefill_020):
    return _base_universe_d3(icv_base_universe_d2_034_icv_basefill_020, 34)
ICV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['icv_base_universe_d3_034_icv_basefill_020'] = {'inputs': ['icv_base_universe_d2_034_icv_basefill_020'], 'func': icv_base_universe_d3_034_icv_basefill_020}


def icv_base_universe_d3_035_icv_basefill_021(icv_base_universe_d2_035_icv_basefill_021):
    return _base_universe_d3(icv_base_universe_d2_035_icv_basefill_021, 35)
ICV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['icv_base_universe_d3_035_icv_basefill_021'] = {'inputs': ['icv_base_universe_d2_035_icv_basefill_021'], 'func': icv_base_universe_d3_035_icv_basefill_021}


def icv_base_universe_d3_036_icv_basefill_022(icv_base_universe_d2_036_icv_basefill_022):
    return _base_universe_d3(icv_base_universe_d2_036_icv_basefill_022, 36)
ICV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['icv_base_universe_d3_036_icv_basefill_022'] = {'inputs': ['icv_base_universe_d2_036_icv_basefill_022'], 'func': icv_base_universe_d3_036_icv_basefill_022}


def icv_base_universe_d3_037_icv_basefill_023(icv_base_universe_d2_037_icv_basefill_023):
    return _base_universe_d3(icv_base_universe_d2_037_icv_basefill_023, 37)
ICV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['icv_base_universe_d3_037_icv_basefill_023'] = {'inputs': ['icv_base_universe_d2_037_icv_basefill_023'], 'func': icv_base_universe_d3_037_icv_basefill_023}


def icv_base_universe_d3_038_icv_basefill_025(icv_base_universe_d2_038_icv_basefill_025):
    return _base_universe_d3(icv_base_universe_d2_038_icv_basefill_025, 38)
ICV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['icv_base_universe_d3_038_icv_basefill_025'] = {'inputs': ['icv_base_universe_d2_038_icv_basefill_025'], 'func': icv_base_universe_d3_038_icv_basefill_025}


def icv_base_universe_d3_039_icv_basefill_026(icv_base_universe_d2_039_icv_basefill_026):
    return _base_universe_d3(icv_base_universe_d2_039_icv_basefill_026, 39)
ICV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['icv_base_universe_d3_039_icv_basefill_026'] = {'inputs': ['icv_base_universe_d2_039_icv_basefill_026'], 'func': icv_base_universe_d3_039_icv_basefill_026}


def icv_base_universe_d3_040_icv_basefill_030(icv_base_universe_d2_040_icv_basefill_030):
    return _base_universe_d3(icv_base_universe_d2_040_icv_basefill_030, 40)
ICV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['icv_base_universe_d3_040_icv_basefill_030'] = {'inputs': ['icv_base_universe_d2_040_icv_basefill_030'], 'func': icv_base_universe_d3_040_icv_basefill_030}


def icv_base_universe_d3_041_icv_basefill_032(icv_base_universe_d2_041_icv_basefill_032):
    return _base_universe_d3(icv_base_universe_d2_041_icv_basefill_032, 41)
ICV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['icv_base_universe_d3_041_icv_basefill_032'] = {'inputs': ['icv_base_universe_d2_041_icv_basefill_032'], 'func': icv_base_universe_d3_041_icv_basefill_032}


def icv_base_universe_d3_042_icv_basefill_033(icv_base_universe_d2_042_icv_basefill_033):
    return _base_universe_d3(icv_base_universe_d2_042_icv_basefill_033, 42)
ICV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['icv_base_universe_d3_042_icv_basefill_033'] = {'inputs': ['icv_base_universe_d2_042_icv_basefill_033'], 'func': icv_base_universe_d3_042_icv_basefill_033}


def icv_base_universe_d3_043_icv_basefill_034(icv_base_universe_d2_043_icv_basefill_034):
    return _base_universe_d3(icv_base_universe_d2_043_icv_basefill_034, 43)
ICV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['icv_base_universe_d3_043_icv_basefill_034'] = {'inputs': ['icv_base_universe_d2_043_icv_basefill_034'], 'func': icv_base_universe_d3_043_icv_basefill_034}


def icv_base_universe_d3_044_icv_basefill_035(icv_base_universe_d2_044_icv_basefill_035):
    return _base_universe_d3(icv_base_universe_d2_044_icv_basefill_035, 44)
ICV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['icv_base_universe_d3_044_icv_basefill_035'] = {'inputs': ['icv_base_universe_d2_044_icv_basefill_035'], 'func': icv_base_universe_d3_044_icv_basefill_035}


def icv_base_universe_d3_045_icv_basefill_037(icv_base_universe_d2_045_icv_basefill_037):
    return _base_universe_d3(icv_base_universe_d2_045_icv_basefill_037, 45)
ICV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['icv_base_universe_d3_045_icv_basefill_037'] = {'inputs': ['icv_base_universe_d2_045_icv_basefill_037'], 'func': icv_base_universe_d3_045_icv_basefill_037}


def icv_base_universe_d3_046_icv_basefill_038(icv_base_universe_d2_046_icv_basefill_038):
    return _base_universe_d3(icv_base_universe_d2_046_icv_basefill_038, 46)
ICV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['icv_base_universe_d3_046_icv_basefill_038'] = {'inputs': ['icv_base_universe_d2_046_icv_basefill_038'], 'func': icv_base_universe_d3_046_icv_basefill_038}


def icv_base_universe_d3_047_icv_basefill_042(icv_base_universe_d2_047_icv_basefill_042):
    return _base_universe_d3(icv_base_universe_d2_047_icv_basefill_042, 47)
ICV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['icv_base_universe_d3_047_icv_basefill_042'] = {'inputs': ['icv_base_universe_d2_047_icv_basefill_042'], 'func': icv_base_universe_d3_047_icv_basefill_042}


def icv_base_universe_d3_048_icv_basefill_044(icv_base_universe_d2_048_icv_basefill_044):
    return _base_universe_d3(icv_base_universe_d2_048_icv_basefill_044, 48)
ICV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['icv_base_universe_d3_048_icv_basefill_044'] = {'inputs': ['icv_base_universe_d2_048_icv_basefill_044'], 'func': icv_base_universe_d3_048_icv_basefill_044}


def icv_base_universe_d3_049_icv_basefill_045(icv_base_universe_d2_049_icv_basefill_045):
    return _base_universe_d3(icv_base_universe_d2_049_icv_basefill_045, 49)
ICV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['icv_base_universe_d3_049_icv_basefill_045'] = {'inputs': ['icv_base_universe_d2_049_icv_basefill_045'], 'func': icv_base_universe_d3_049_icv_basefill_045}


def icv_base_universe_d3_050_icv_basefill_046(icv_base_universe_d2_050_icv_basefill_046):
    return _base_universe_d3(icv_base_universe_d2_050_icv_basefill_046, 50)
ICV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['icv_base_universe_d3_050_icv_basefill_046'] = {'inputs': ['icv_base_universe_d2_050_icv_basefill_046'], 'func': icv_base_universe_d3_050_icv_basefill_046}


def icv_base_universe_d3_051_icv_basefill_047(icv_base_universe_d2_051_icv_basefill_047):
    return _base_universe_d3(icv_base_universe_d2_051_icv_basefill_047, 51)
ICV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['icv_base_universe_d3_051_icv_basefill_047'] = {'inputs': ['icv_base_universe_d2_051_icv_basefill_047'], 'func': icv_base_universe_d3_051_icv_basefill_047}


def icv_base_universe_d3_052_icv_basefill_049(icv_base_universe_d2_052_icv_basefill_049):
    return _base_universe_d3(icv_base_universe_d2_052_icv_basefill_049, 52)
ICV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['icv_base_universe_d3_052_icv_basefill_049'] = {'inputs': ['icv_base_universe_d2_052_icv_basefill_049'], 'func': icv_base_universe_d3_052_icv_basefill_049}


def icv_base_universe_d3_053_icv_basefill_050(icv_base_universe_d2_053_icv_basefill_050):
    return _base_universe_d3(icv_base_universe_d2_053_icv_basefill_050, 53)
ICV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['icv_base_universe_d3_053_icv_basefill_050'] = {'inputs': ['icv_base_universe_d2_053_icv_basefill_050'], 'func': icv_base_universe_d3_053_icv_basefill_050}


def icv_base_universe_d3_054_icv_basefill_054(icv_base_universe_d2_054_icv_basefill_054):
    return _base_universe_d3(icv_base_universe_d2_054_icv_basefill_054, 54)
ICV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['icv_base_universe_d3_054_icv_basefill_054'] = {'inputs': ['icv_base_universe_d2_054_icv_basefill_054'], 'func': icv_base_universe_d3_054_icv_basefill_054}


def icv_base_universe_d3_055_icv_basefill_056(icv_base_universe_d2_055_icv_basefill_056):
    return _base_universe_d3(icv_base_universe_d2_055_icv_basefill_056, 55)
ICV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['icv_base_universe_d3_055_icv_basefill_056'] = {'inputs': ['icv_base_universe_d2_055_icv_basefill_056'], 'func': icv_base_universe_d3_055_icv_basefill_056}


def icv_base_universe_d3_056_icv_basefill_057(icv_base_universe_d2_056_icv_basefill_057):
    return _base_universe_d3(icv_base_universe_d2_056_icv_basefill_057, 56)
ICV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['icv_base_universe_d3_056_icv_basefill_057'] = {'inputs': ['icv_base_universe_d2_056_icv_basefill_057'], 'func': icv_base_universe_d3_056_icv_basefill_057}


def icv_base_universe_d3_057_icv_basefill_058(icv_base_universe_d2_057_icv_basefill_058):
    return _base_universe_d3(icv_base_universe_d2_057_icv_basefill_058, 57)
ICV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['icv_base_universe_d3_057_icv_basefill_058'] = {'inputs': ['icv_base_universe_d2_057_icv_basefill_058'], 'func': icv_base_universe_d3_057_icv_basefill_058}


def icv_base_universe_d3_058_icv_basefill_059(icv_base_universe_d2_058_icv_basefill_059):
    return _base_universe_d3(icv_base_universe_d2_058_icv_basefill_059, 58)
ICV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['icv_base_universe_d3_058_icv_basefill_059'] = {'inputs': ['icv_base_universe_d2_058_icv_basefill_059'], 'func': icv_base_universe_d3_058_icv_basefill_059}


def icv_base_universe_d3_059_icv_basefill_061(icv_base_universe_d2_059_icv_basefill_061):
    return _base_universe_d3(icv_base_universe_d2_059_icv_basefill_061, 59)
ICV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['icv_base_universe_d3_059_icv_basefill_061'] = {'inputs': ['icv_base_universe_d2_059_icv_basefill_061'], 'func': icv_base_universe_d3_059_icv_basefill_061}


def icv_base_universe_d3_060_icv_basefill_062(icv_base_universe_d2_060_icv_basefill_062):
    return _base_universe_d3(icv_base_universe_d2_060_icv_basefill_062, 60)
ICV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['icv_base_universe_d3_060_icv_basefill_062'] = {'inputs': ['icv_base_universe_d2_060_icv_basefill_062'], 'func': icv_base_universe_d3_060_icv_basefill_062}


def icv_base_universe_d3_061_icv_basefill_063(icv_base_universe_d2_061_icv_basefill_063):
    return _base_universe_d3(icv_base_universe_d2_061_icv_basefill_063, 61)
ICV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['icv_base_universe_d3_061_icv_basefill_063'] = {'inputs': ['icv_base_universe_d2_061_icv_basefill_063'], 'func': icv_base_universe_d3_061_icv_basefill_063}


def icv_base_universe_d3_062_icv_basefill_064(icv_base_universe_d2_062_icv_basefill_064):
    return _base_universe_d3(icv_base_universe_d2_062_icv_basefill_064, 62)
ICV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['icv_base_universe_d3_062_icv_basefill_064'] = {'inputs': ['icv_base_universe_d2_062_icv_basefill_064'], 'func': icv_base_universe_d3_062_icv_basefill_064}


def icv_base_universe_d3_063_icv_basefill_065(icv_base_universe_d2_063_icv_basefill_065):
    return _base_universe_d3(icv_base_universe_d2_063_icv_basefill_065, 63)
ICV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['icv_base_universe_d3_063_icv_basefill_065'] = {'inputs': ['icv_base_universe_d2_063_icv_basefill_065'], 'func': icv_base_universe_d3_063_icv_basefill_065}


def icv_base_universe_d3_064_icv_basefill_066(icv_base_universe_d2_064_icv_basefill_066):
    return _base_universe_d3(icv_base_universe_d2_064_icv_basefill_066, 64)
ICV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['icv_base_universe_d3_064_icv_basefill_066'] = {'inputs': ['icv_base_universe_d2_064_icv_basefill_066'], 'func': icv_base_universe_d3_064_icv_basefill_066}


def icv_base_universe_d3_065_icv_basefill_067(icv_base_universe_d2_065_icv_basefill_067):
    return _base_universe_d3(icv_base_universe_d2_065_icv_basefill_067, 65)
ICV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['icv_base_universe_d3_065_icv_basefill_067'] = {'inputs': ['icv_base_universe_d2_065_icv_basefill_067'], 'func': icv_base_universe_d3_065_icv_basefill_067}


def icv_base_universe_d3_066_icv_basefill_068(icv_base_universe_d2_066_icv_basefill_068):
    return _base_universe_d3(icv_base_universe_d2_066_icv_basefill_068, 66)
ICV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['icv_base_universe_d3_066_icv_basefill_068'] = {'inputs': ['icv_base_universe_d2_066_icv_basefill_068'], 'func': icv_base_universe_d3_066_icv_basefill_068}


def icv_base_universe_d3_067_icv_basefill_069(icv_base_universe_d2_067_icv_basefill_069):
    return _base_universe_d3(icv_base_universe_d2_067_icv_basefill_069, 67)
ICV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['icv_base_universe_d3_067_icv_basefill_069'] = {'inputs': ['icv_base_universe_d2_067_icv_basefill_069'], 'func': icv_base_universe_d3_067_icv_basefill_069}


def icv_base_universe_d3_068_icv_basefill_070(icv_base_universe_d2_068_icv_basefill_070):
    return _base_universe_d3(icv_base_universe_d2_068_icv_basefill_070, 68)
ICV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['icv_base_universe_d3_068_icv_basefill_070'] = {'inputs': ['icv_base_universe_d2_068_icv_basefill_070'], 'func': icv_base_universe_d3_068_icv_basefill_070}


def icv_base_universe_d3_069_icv_basefill_071(icv_base_universe_d2_069_icv_basefill_071):
    return _base_universe_d3(icv_base_universe_d2_069_icv_basefill_071, 69)
ICV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['icv_base_universe_d3_069_icv_basefill_071'] = {'inputs': ['icv_base_universe_d2_069_icv_basefill_071'], 'func': icv_base_universe_d3_069_icv_basefill_071}


def icv_base_universe_d3_070_icv_basefill_072(icv_base_universe_d2_070_icv_basefill_072):
    return _base_universe_d3(icv_base_universe_d2_070_icv_basefill_072, 70)
ICV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['icv_base_universe_d3_070_icv_basefill_072'] = {'inputs': ['icv_base_universe_d2_070_icv_basefill_072'], 'func': icv_base_universe_d3_070_icv_basefill_072}


def icv_base_universe_d3_071_icv_basefill_073(icv_base_universe_d2_071_icv_basefill_073):
    return _base_universe_d3(icv_base_universe_d2_071_icv_basefill_073, 71)
ICV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['icv_base_universe_d3_071_icv_basefill_073'] = {'inputs': ['icv_base_universe_d2_071_icv_basefill_073'], 'func': icv_base_universe_d3_071_icv_basefill_073}


def icv_base_universe_d3_072_icv_basefill_074(icv_base_universe_d2_072_icv_basefill_074):
    return _base_universe_d3(icv_base_universe_d2_072_icv_basefill_074, 72)
ICV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['icv_base_universe_d3_072_icv_basefill_074'] = {'inputs': ['icv_base_universe_d2_072_icv_basefill_074'], 'func': icv_base_universe_d3_072_icv_basefill_074}


def icv_base_universe_d3_073_icv_basefill_075(icv_base_universe_d2_073_icv_basefill_075):
    return _base_universe_d3(icv_base_universe_d2_073_icv_basefill_075, 73)
ICV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['icv_base_universe_d3_073_icv_basefill_075'] = {'inputs': ['icv_base_universe_d2_073_icv_basefill_075'], 'func': icv_base_universe_d3_073_icv_basefill_075}
