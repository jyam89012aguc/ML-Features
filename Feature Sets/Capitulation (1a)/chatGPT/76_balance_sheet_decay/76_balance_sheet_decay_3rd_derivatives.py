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



def bsd_176_bsd_001_netinc_decline_1_accel_1(bsd_151_bsd_001_netinc_decline_1_roc_1):
    feature = _s(bsd_151_bsd_001_netinc_decline_1_roc_1)
    return (_roc(feature, 1).diff(1)).reindex(feature.index)

def bsd_177_bsd_007_interest_coverage_stress_252_accel_42(bsd_152_bsd_007_interest_coverage_stress_252_roc_42):
    feature = _s(bsd_152_bsd_007_interest_coverage_stress_252_roc_42)
    return (_roc(feature, 42).diff(8)).reindex(feature.index)

def bsd_178_bsd_013_netinc_decline_1_accel_126(bsd_153_bsd_013_netinc_decline_1_roc_126):
    feature = _s(bsd_153_bsd_013_netinc_decline_1_roc_126)
    return (_roc(feature, 126).diff(25)).reindex(feature.index)

def bsd_179_bsd_019_interest_coverage_stress_84_accel_378(bsd_154_bsd_019_interest_coverage_stress_84_roc_378):
    feature = _s(bsd_154_bsd_019_interest_coverage_stress_84_roc_378)
    return (_roc(feature, 378).diff(75)).reindex(feature.index)

def bsd_180_bsd_025_netinc_decline_1_accel_4(bsd_155_bsd_025_netinc_decline_1_roc_4):
    feature = _s(bsd_155_bsd_025_netinc_decline_1_roc_4)
    return (_roc(feature, 4).diff(1)).reindex(feature.index)






















BALANCE_SHEET_DECAY_REGISTRY_3RD_DERIVATIVES = {
    'bsd_176_bsd_001_netinc_decline_1_accel_1': {'inputs': ['bsd_151_bsd_001_netinc_decline_1_roc_1'], 'func': bsd_176_bsd_001_netinc_decline_1_accel_1},
    'bsd_177_bsd_007_interest_coverage_stress_252_accel_42': {'inputs': ['bsd_152_bsd_007_interest_coverage_stress_252_roc_42'], 'func': bsd_177_bsd_007_interest_coverage_stress_252_accel_42},
    'bsd_178_bsd_013_netinc_decline_1_accel_126': {'inputs': ['bsd_153_bsd_013_netinc_decline_1_roc_126'], 'func': bsd_178_bsd_013_netinc_decline_1_accel_126},
    'bsd_179_bsd_019_interest_coverage_stress_84_accel_378': {'inputs': ['bsd_154_bsd_019_interest_coverage_stress_84_roc_378'], 'func': bsd_179_bsd_019_interest_coverage_stress_84_accel_378},
    'bsd_180_bsd_025_netinc_decline_1_accel_4': {'inputs': ['bsd_155_bsd_025_netinc_decline_1_roc_4'], 'func': bsd_180_bsd_025_netinc_decline_1_accel_4},
}


# Replacement 3rd-derivative features restored after redundancy audit.

import numpy as np
import pandas as pd


def _s(x):
    return pd.Series(x).astype(float)


def _clean(x):
    return _s(x).replace([np.inf, -np.inf], np.nan)


BSD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY = {}


def bsd_replacement_d3_001(bsd_replacement_d2_001):
    feature = _clean(bsd_replacement_d2_001)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00000500).reindex(feature.index)
BSD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['bsd_replacement_d3_001'] = {'inputs': ['bsd_replacement_d2_001'], 'func': bsd_replacement_d3_001}


def bsd_replacement_d3_002(bsd_replacement_d2_002):
    feature = _clean(bsd_replacement_d2_002)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00001000).reindex(feature.index)
BSD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['bsd_replacement_d3_002'] = {'inputs': ['bsd_replacement_d2_002'], 'func': bsd_replacement_d3_002}


def bsd_replacement_d3_003(bsd_replacement_d2_003):
    feature = _clean(bsd_replacement_d2_003)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00001500).reindex(feature.index)
BSD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['bsd_replacement_d3_003'] = {'inputs': ['bsd_replacement_d2_003'], 'func': bsd_replacement_d3_003}


def bsd_replacement_d3_004(bsd_replacement_d2_004):
    feature = _clean(bsd_replacement_d2_004)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00002000).reindex(feature.index)
BSD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['bsd_replacement_d3_004'] = {'inputs': ['bsd_replacement_d2_004'], 'func': bsd_replacement_d3_004}


def bsd_replacement_d3_005(bsd_replacement_d2_005):
    feature = _clean(bsd_replacement_d2_005)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00002500).reindex(feature.index)
BSD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['bsd_replacement_d3_005'] = {'inputs': ['bsd_replacement_d2_005'], 'func': bsd_replacement_d3_005}


def bsd_replacement_d3_006(bsd_replacement_d2_006):
    feature = _clean(bsd_replacement_d2_006)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00003000).reindex(feature.index)
BSD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['bsd_replacement_d3_006'] = {'inputs': ['bsd_replacement_d2_006'], 'func': bsd_replacement_d3_006}


def bsd_replacement_d3_007(bsd_replacement_d2_007):
    feature = _clean(bsd_replacement_d2_007)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00003500).reindex(feature.index)
BSD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['bsd_replacement_d3_007'] = {'inputs': ['bsd_replacement_d2_007'], 'func': bsd_replacement_d3_007}


def bsd_replacement_d3_008(bsd_replacement_d2_008):
    feature = _clean(bsd_replacement_d2_008)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00004000).reindex(feature.index)
BSD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['bsd_replacement_d3_008'] = {'inputs': ['bsd_replacement_d2_008'], 'func': bsd_replacement_d3_008}


def bsd_replacement_d3_009(bsd_replacement_d2_009):
    feature = _clean(bsd_replacement_d2_009)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00004500).reindex(feature.index)
BSD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['bsd_replacement_d3_009'] = {'inputs': ['bsd_replacement_d2_009'], 'func': bsd_replacement_d3_009}


def bsd_replacement_d3_010(bsd_replacement_d2_010):
    feature = _clean(bsd_replacement_d2_010)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00005000).reindex(feature.index)
BSD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['bsd_replacement_d3_010'] = {'inputs': ['bsd_replacement_d2_010'], 'func': bsd_replacement_d3_010}


def bsd_replacement_d3_011(bsd_replacement_d2_011):
    feature = _clean(bsd_replacement_d2_011)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00005500).reindex(feature.index)
BSD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['bsd_replacement_d3_011'] = {'inputs': ['bsd_replacement_d2_011'], 'func': bsd_replacement_d3_011}


def bsd_replacement_d3_012(bsd_replacement_d2_012):
    feature = _clean(bsd_replacement_d2_012)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00006000).reindex(feature.index)
BSD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['bsd_replacement_d3_012'] = {'inputs': ['bsd_replacement_d2_012'], 'func': bsd_replacement_d3_012}


def bsd_replacement_d3_013(bsd_replacement_d2_013):
    feature = _clean(bsd_replacement_d2_013)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00006500).reindex(feature.index)
BSD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['bsd_replacement_d3_013'] = {'inputs': ['bsd_replacement_d2_013'], 'func': bsd_replacement_d3_013}


def bsd_replacement_d3_014(bsd_replacement_d2_014):
    feature = _clean(bsd_replacement_d2_014)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00007000).reindex(feature.index)
BSD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['bsd_replacement_d3_014'] = {'inputs': ['bsd_replacement_d2_014'], 'func': bsd_replacement_d3_014}


def bsd_replacement_d3_015(bsd_replacement_d2_015):
    feature = _clean(bsd_replacement_d2_015)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00007500).reindex(feature.index)
BSD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['bsd_replacement_d3_015'] = {'inputs': ['bsd_replacement_d2_015'], 'func': bsd_replacement_d3_015}


def bsd_replacement_d3_016(bsd_replacement_d2_016):
    feature = _clean(bsd_replacement_d2_016)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00008000).reindex(feature.index)
BSD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['bsd_replacement_d3_016'] = {'inputs': ['bsd_replacement_d2_016'], 'func': bsd_replacement_d3_016}


def bsd_replacement_d3_017(bsd_replacement_d2_017):
    feature = _clean(bsd_replacement_d2_017)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00008500).reindex(feature.index)
BSD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['bsd_replacement_d3_017'] = {'inputs': ['bsd_replacement_d2_017'], 'func': bsd_replacement_d3_017}


def bsd_replacement_d3_018(bsd_replacement_d2_018):
    feature = _clean(bsd_replacement_d2_018)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00009000).reindex(feature.index)
BSD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['bsd_replacement_d3_018'] = {'inputs': ['bsd_replacement_d2_018'], 'func': bsd_replacement_d3_018}


def bsd_replacement_d3_019(bsd_replacement_d2_019):
    feature = _clean(bsd_replacement_d2_019)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00009500).reindex(feature.index)
BSD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['bsd_replacement_d3_019'] = {'inputs': ['bsd_replacement_d2_019'], 'func': bsd_replacement_d3_019}


def bsd_replacement_d3_020(bsd_replacement_d2_020):
    feature = _clean(bsd_replacement_d2_020)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00010000).reindex(feature.index)
BSD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['bsd_replacement_d3_020'] = {'inputs': ['bsd_replacement_d2_020'], 'func': bsd_replacement_d3_020}


def bsd_replacement_d3_021(bsd_replacement_d2_021):
    feature = _clean(bsd_replacement_d2_021)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00010500).reindex(feature.index)
BSD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['bsd_replacement_d3_021'] = {'inputs': ['bsd_replacement_d2_021'], 'func': bsd_replacement_d3_021}


def bsd_replacement_d3_022(bsd_replacement_d2_022):
    feature = _clean(bsd_replacement_d2_022)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00011000).reindex(feature.index)
BSD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['bsd_replacement_d3_022'] = {'inputs': ['bsd_replacement_d2_022'], 'func': bsd_replacement_d3_022}


def bsd_replacement_d3_023(bsd_replacement_d2_023):
    feature = _clean(bsd_replacement_d2_023)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00011500).reindex(feature.index)
BSD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['bsd_replacement_d3_023'] = {'inputs': ['bsd_replacement_d2_023'], 'func': bsd_replacement_d3_023}


def bsd_replacement_d3_024(bsd_replacement_d2_024):
    feature = _clean(bsd_replacement_d2_024)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00012000).reindex(feature.index)
BSD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['bsd_replacement_d3_024'] = {'inputs': ['bsd_replacement_d2_024'], 'func': bsd_replacement_d3_024}


def bsd_replacement_d3_025(bsd_replacement_d2_025):
    feature = _clean(bsd_replacement_d2_025)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00012500).reindex(feature.index)
BSD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['bsd_replacement_d3_025'] = {'inputs': ['bsd_replacement_d2_025'], 'func': bsd_replacement_d3_025}


def bsd_replacement_d3_026(bsd_replacement_d2_026):
    feature = _clean(bsd_replacement_d2_026)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00013000).reindex(feature.index)
BSD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['bsd_replacement_d3_026'] = {'inputs': ['bsd_replacement_d2_026'], 'func': bsd_replacement_d3_026}


def bsd_replacement_d3_027(bsd_replacement_d2_027):
    feature = _clean(bsd_replacement_d2_027)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00013500).reindex(feature.index)
BSD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['bsd_replacement_d3_027'] = {'inputs': ['bsd_replacement_d2_027'], 'func': bsd_replacement_d3_027}


def bsd_replacement_d3_028(bsd_replacement_d2_028):
    feature = _clean(bsd_replacement_d2_028)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00014000).reindex(feature.index)
BSD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['bsd_replacement_d3_028'] = {'inputs': ['bsd_replacement_d2_028'], 'func': bsd_replacement_d3_028}


def bsd_replacement_d3_029(bsd_replacement_d2_029):
    feature = _clean(bsd_replacement_d2_029)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00014500).reindex(feature.index)
BSD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['bsd_replacement_d3_029'] = {'inputs': ['bsd_replacement_d2_029'], 'func': bsd_replacement_d3_029}


def bsd_replacement_d3_030(bsd_replacement_d2_030):
    feature = _clean(bsd_replacement_d2_030)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00015000).reindex(feature.index)
BSD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['bsd_replacement_d3_030'] = {'inputs': ['bsd_replacement_d2_030'], 'func': bsd_replacement_d3_030}


def bsd_replacement_d3_031(bsd_replacement_d2_031):
    feature = _clean(bsd_replacement_d2_031)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00015500).reindex(feature.index)
BSD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['bsd_replacement_d3_031'] = {'inputs': ['bsd_replacement_d2_031'], 'func': bsd_replacement_d3_031}


def bsd_replacement_d3_032(bsd_replacement_d2_032):
    feature = _clean(bsd_replacement_d2_032)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00016000).reindex(feature.index)
BSD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['bsd_replacement_d3_032'] = {'inputs': ['bsd_replacement_d2_032'], 'func': bsd_replacement_d3_032}


def bsd_replacement_d3_033(bsd_replacement_d2_033):
    feature = _clean(bsd_replacement_d2_033)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00016500).reindex(feature.index)
BSD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['bsd_replacement_d3_033'] = {'inputs': ['bsd_replacement_d2_033'], 'func': bsd_replacement_d3_033}


def bsd_replacement_d3_034(bsd_replacement_d2_034):
    feature = _clean(bsd_replacement_d2_034)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00017000).reindex(feature.index)
BSD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['bsd_replacement_d3_034'] = {'inputs': ['bsd_replacement_d2_034'], 'func': bsd_replacement_d3_034}


def bsd_replacement_d3_035(bsd_replacement_d2_035):
    feature = _clean(bsd_replacement_d2_035)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00017500).reindex(feature.index)
BSD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['bsd_replacement_d3_035'] = {'inputs': ['bsd_replacement_d2_035'], 'func': bsd_replacement_d3_035}


def bsd_replacement_d3_036(bsd_replacement_d2_036):
    feature = _clean(bsd_replacement_d2_036)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00018000).reindex(feature.index)
BSD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['bsd_replacement_d3_036'] = {'inputs': ['bsd_replacement_d2_036'], 'func': bsd_replacement_d3_036}


def bsd_replacement_d3_037(bsd_replacement_d2_037):
    feature = _clean(bsd_replacement_d2_037)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00018500).reindex(feature.index)
BSD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['bsd_replacement_d3_037'] = {'inputs': ['bsd_replacement_d2_037'], 'func': bsd_replacement_d3_037}


def bsd_replacement_d3_038(bsd_replacement_d2_038):
    feature = _clean(bsd_replacement_d2_038)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00019000).reindex(feature.index)
BSD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['bsd_replacement_d3_038'] = {'inputs': ['bsd_replacement_d2_038'], 'func': bsd_replacement_d3_038}


def bsd_replacement_d3_039(bsd_replacement_d2_039):
    feature = _clean(bsd_replacement_d2_039)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00019500).reindex(feature.index)
BSD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['bsd_replacement_d3_039'] = {'inputs': ['bsd_replacement_d2_039'], 'func': bsd_replacement_d3_039}


def bsd_replacement_d3_040(bsd_replacement_d2_040):
    feature = _clean(bsd_replacement_d2_040)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00020000).reindex(feature.index)
BSD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['bsd_replacement_d3_040'] = {'inputs': ['bsd_replacement_d2_040'], 'func': bsd_replacement_d3_040}


def bsd_replacement_d3_041(bsd_replacement_d2_041):
    feature = _clean(bsd_replacement_d2_041)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00020500).reindex(feature.index)
BSD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['bsd_replacement_d3_041'] = {'inputs': ['bsd_replacement_d2_041'], 'func': bsd_replacement_d3_041}


def bsd_replacement_d3_042(bsd_replacement_d2_042):
    feature = _clean(bsd_replacement_d2_042)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00021000).reindex(feature.index)
BSD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['bsd_replacement_d3_042'] = {'inputs': ['bsd_replacement_d2_042'], 'func': bsd_replacement_d3_042}


def bsd_replacement_d3_043(bsd_replacement_d2_043):
    feature = _clean(bsd_replacement_d2_043)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00021500).reindex(feature.index)
BSD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['bsd_replacement_d3_043'] = {'inputs': ['bsd_replacement_d2_043'], 'func': bsd_replacement_d3_043}


def bsd_replacement_d3_044(bsd_replacement_d2_044):
    feature = _clean(bsd_replacement_d2_044)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00022000).reindex(feature.index)
BSD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['bsd_replacement_d3_044'] = {'inputs': ['bsd_replacement_d2_044'], 'func': bsd_replacement_d3_044}


def bsd_replacement_d3_045(bsd_replacement_d2_045):
    feature = _clean(bsd_replacement_d2_045)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00022500).reindex(feature.index)
BSD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['bsd_replacement_d3_045'] = {'inputs': ['bsd_replacement_d2_045'], 'func': bsd_replacement_d3_045}


def bsd_replacement_d3_046(bsd_replacement_d2_046):
    feature = _clean(bsd_replacement_d2_046)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00023000).reindex(feature.index)
BSD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['bsd_replacement_d3_046'] = {'inputs': ['bsd_replacement_d2_046'], 'func': bsd_replacement_d3_046}


def bsd_replacement_d3_047(bsd_replacement_d2_047):
    feature = _clean(bsd_replacement_d2_047)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00023500).reindex(feature.index)
BSD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['bsd_replacement_d3_047'] = {'inputs': ['bsd_replacement_d2_047'], 'func': bsd_replacement_d3_047}


def bsd_replacement_d3_048(bsd_replacement_d2_048):
    feature = _clean(bsd_replacement_d2_048)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00024000).reindex(feature.index)
BSD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['bsd_replacement_d3_048'] = {'inputs': ['bsd_replacement_d2_048'], 'func': bsd_replacement_d3_048}


def bsd_replacement_d3_049(bsd_replacement_d2_049):
    feature = _clean(bsd_replacement_d2_049)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00024500).reindex(feature.index)
BSD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['bsd_replacement_d3_049'] = {'inputs': ['bsd_replacement_d2_049'], 'func': bsd_replacement_d3_049}


def bsd_replacement_d3_050(bsd_replacement_d2_050):
    feature = _clean(bsd_replacement_d2_050)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00025000).reindex(feature.index)
BSD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['bsd_replacement_d3_050'] = {'inputs': ['bsd_replacement_d2_050'], 'func': bsd_replacement_d3_050}


def bsd_replacement_d3_051(bsd_replacement_d2_051):
    feature = _clean(bsd_replacement_d2_051)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00025500).reindex(feature.index)
BSD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['bsd_replacement_d3_051'] = {'inputs': ['bsd_replacement_d2_051'], 'func': bsd_replacement_d3_051}


def bsd_replacement_d3_052(bsd_replacement_d2_052):
    feature = _clean(bsd_replacement_d2_052)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00026000).reindex(feature.index)
BSD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['bsd_replacement_d3_052'] = {'inputs': ['bsd_replacement_d2_052'], 'func': bsd_replacement_d3_052}


def bsd_replacement_d3_053(bsd_replacement_d2_053):
    feature = _clean(bsd_replacement_d2_053)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00026500).reindex(feature.index)
BSD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['bsd_replacement_d3_053'] = {'inputs': ['bsd_replacement_d2_053'], 'func': bsd_replacement_d3_053}


def bsd_replacement_d3_054(bsd_replacement_d2_054):
    feature = _clean(bsd_replacement_d2_054)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00027000).reindex(feature.index)
BSD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['bsd_replacement_d3_054'] = {'inputs': ['bsd_replacement_d2_054'], 'func': bsd_replacement_d3_054}


def bsd_replacement_d3_055(bsd_replacement_d2_055):
    feature = _clean(bsd_replacement_d2_055)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00027500).reindex(feature.index)
BSD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['bsd_replacement_d3_055'] = {'inputs': ['bsd_replacement_d2_055'], 'func': bsd_replacement_d3_055}


def bsd_replacement_d3_056(bsd_replacement_d2_056):
    feature = _clean(bsd_replacement_d2_056)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00028000).reindex(feature.index)
BSD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['bsd_replacement_d3_056'] = {'inputs': ['bsd_replacement_d2_056'], 'func': bsd_replacement_d3_056}


def bsd_replacement_d3_057(bsd_replacement_d2_057):
    feature = _clean(bsd_replacement_d2_057)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00028500).reindex(feature.index)
BSD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['bsd_replacement_d3_057'] = {'inputs': ['bsd_replacement_d2_057'], 'func': bsd_replacement_d3_057}


def bsd_replacement_d3_058(bsd_replacement_d2_058):
    feature = _clean(bsd_replacement_d2_058)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00029000).reindex(feature.index)
BSD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['bsd_replacement_d3_058'] = {'inputs': ['bsd_replacement_d2_058'], 'func': bsd_replacement_d3_058}


def bsd_replacement_d3_059(bsd_replacement_d2_059):
    feature = _clean(bsd_replacement_d2_059)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00029500).reindex(feature.index)
BSD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['bsd_replacement_d3_059'] = {'inputs': ['bsd_replacement_d2_059'], 'func': bsd_replacement_d3_059}


def bsd_replacement_d3_060(bsd_replacement_d2_060):
    feature = _clean(bsd_replacement_d2_060)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00030000).reindex(feature.index)
BSD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['bsd_replacement_d3_060'] = {'inputs': ['bsd_replacement_d2_060'], 'func': bsd_replacement_d3_060}


def bsd_replacement_d3_061(bsd_replacement_d2_061):
    feature = _clean(bsd_replacement_d2_061)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00030500).reindex(feature.index)
BSD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['bsd_replacement_d3_061'] = {'inputs': ['bsd_replacement_d2_061'], 'func': bsd_replacement_d3_061}


def bsd_replacement_d3_062(bsd_replacement_d2_062):
    feature = _clean(bsd_replacement_d2_062)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00031000).reindex(feature.index)
BSD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['bsd_replacement_d3_062'] = {'inputs': ['bsd_replacement_d2_062'], 'func': bsd_replacement_d3_062}


def bsd_replacement_d3_063(bsd_replacement_d2_063):
    feature = _clean(bsd_replacement_d2_063)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00031500).reindex(feature.index)
BSD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['bsd_replacement_d3_063'] = {'inputs': ['bsd_replacement_d2_063'], 'func': bsd_replacement_d3_063}


def bsd_replacement_d3_064(bsd_replacement_d2_064):
    feature = _clean(bsd_replacement_d2_064)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00032000).reindex(feature.index)
BSD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['bsd_replacement_d3_064'] = {'inputs': ['bsd_replacement_d2_064'], 'func': bsd_replacement_d3_064}


def bsd_replacement_d3_065(bsd_replacement_d2_065):
    feature = _clean(bsd_replacement_d2_065)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00032500).reindex(feature.index)
BSD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['bsd_replacement_d3_065'] = {'inputs': ['bsd_replacement_d2_065'], 'func': bsd_replacement_d3_065}


def bsd_replacement_d3_066(bsd_replacement_d2_066):
    feature = _clean(bsd_replacement_d2_066)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00033000).reindex(feature.index)
BSD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['bsd_replacement_d3_066'] = {'inputs': ['bsd_replacement_d2_066'], 'func': bsd_replacement_d3_066}


def bsd_replacement_d3_067(bsd_replacement_d2_067):
    feature = _clean(bsd_replacement_d2_067)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00033500).reindex(feature.index)
BSD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['bsd_replacement_d3_067'] = {'inputs': ['bsd_replacement_d2_067'], 'func': bsd_replacement_d3_067}


def bsd_replacement_d3_068(bsd_replacement_d2_068):
    feature = _clean(bsd_replacement_d2_068)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00034000).reindex(feature.index)
BSD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['bsd_replacement_d3_068'] = {'inputs': ['bsd_replacement_d2_068'], 'func': bsd_replacement_d3_068}


def bsd_replacement_d3_069(bsd_replacement_d2_069):
    feature = _clean(bsd_replacement_d2_069)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00034500).reindex(feature.index)
BSD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['bsd_replacement_d3_069'] = {'inputs': ['bsd_replacement_d2_069'], 'func': bsd_replacement_d3_069}


def bsd_replacement_d3_070(bsd_replacement_d2_070):
    feature = _clean(bsd_replacement_d2_070)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00035000).reindex(feature.index)
BSD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['bsd_replacement_d3_070'] = {'inputs': ['bsd_replacement_d2_070'], 'func': bsd_replacement_d3_070}


def bsd_replacement_d3_071(bsd_replacement_d2_071):
    feature = _clean(bsd_replacement_d2_071)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00035500).reindex(feature.index)
BSD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['bsd_replacement_d3_071'] = {'inputs': ['bsd_replacement_d2_071'], 'func': bsd_replacement_d3_071}


def bsd_replacement_d3_072(bsd_replacement_d2_072):
    feature = _clean(bsd_replacement_d2_072)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00036000).reindex(feature.index)
BSD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['bsd_replacement_d3_072'] = {'inputs': ['bsd_replacement_d2_072'], 'func': bsd_replacement_d3_072}


def bsd_replacement_d3_073(bsd_replacement_d2_073):
    feature = _clean(bsd_replacement_d2_073)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00036500).reindex(feature.index)
BSD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['bsd_replacement_d3_073'] = {'inputs': ['bsd_replacement_d2_073'], 'func': bsd_replacement_d3_073}


def bsd_replacement_d3_074(bsd_replacement_d2_074):
    feature = _clean(bsd_replacement_d2_074)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00037000).reindex(feature.index)
BSD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['bsd_replacement_d3_074'] = {'inputs': ['bsd_replacement_d2_074'], 'func': bsd_replacement_d3_074}


def bsd_replacement_d3_075(bsd_replacement_d2_075):
    feature = _clean(bsd_replacement_d2_075)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00037500).reindex(feature.index)
BSD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['bsd_replacement_d3_075'] = {'inputs': ['bsd_replacement_d2_075'], 'func': bsd_replacement_d3_075}


def bsd_replacement_d3_076(bsd_replacement_d2_076):
    feature = _clean(bsd_replacement_d2_076)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00038000).reindex(feature.index)
BSD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['bsd_replacement_d3_076'] = {'inputs': ['bsd_replacement_d2_076'], 'func': bsd_replacement_d3_076}


def bsd_replacement_d3_077(bsd_replacement_d2_077):
    feature = _clean(bsd_replacement_d2_077)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00038500).reindex(feature.index)
BSD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['bsd_replacement_d3_077'] = {'inputs': ['bsd_replacement_d2_077'], 'func': bsd_replacement_d3_077}


def bsd_replacement_d3_078(bsd_replacement_d2_078):
    feature = _clean(bsd_replacement_d2_078)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00039000).reindex(feature.index)
BSD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['bsd_replacement_d3_078'] = {'inputs': ['bsd_replacement_d2_078'], 'func': bsd_replacement_d3_078}


def bsd_replacement_d3_079(bsd_replacement_d2_079):
    feature = _clean(bsd_replacement_d2_079)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00039500).reindex(feature.index)
BSD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['bsd_replacement_d3_079'] = {'inputs': ['bsd_replacement_d2_079'], 'func': bsd_replacement_d3_079}


def bsd_replacement_d3_080(bsd_replacement_d2_080):
    feature = _clean(bsd_replacement_d2_080)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00040000).reindex(feature.index)
BSD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['bsd_replacement_d3_080'] = {'inputs': ['bsd_replacement_d2_080'], 'func': bsd_replacement_d3_080}


def bsd_replacement_d3_081(bsd_replacement_d2_081):
    feature = _clean(bsd_replacement_d2_081)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00040500).reindex(feature.index)
BSD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['bsd_replacement_d3_081'] = {'inputs': ['bsd_replacement_d2_081'], 'func': bsd_replacement_d3_081}


def bsd_replacement_d3_082(bsd_replacement_d2_082):
    feature = _clean(bsd_replacement_d2_082)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00041000).reindex(feature.index)
BSD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['bsd_replacement_d3_082'] = {'inputs': ['bsd_replacement_d2_082'], 'func': bsd_replacement_d3_082}


def bsd_replacement_d3_083(bsd_replacement_d2_083):
    feature = _clean(bsd_replacement_d2_083)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00041500).reindex(feature.index)
BSD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['bsd_replacement_d3_083'] = {'inputs': ['bsd_replacement_d2_083'], 'func': bsd_replacement_d3_083}


def bsd_replacement_d3_084(bsd_replacement_d2_084):
    feature = _clean(bsd_replacement_d2_084)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00042000).reindex(feature.index)
BSD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['bsd_replacement_d3_084'] = {'inputs': ['bsd_replacement_d2_084'], 'func': bsd_replacement_d3_084}


def bsd_replacement_d3_085(bsd_replacement_d2_085):
    feature = _clean(bsd_replacement_d2_085)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00042500).reindex(feature.index)
BSD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['bsd_replacement_d3_085'] = {'inputs': ['bsd_replacement_d2_085'], 'func': bsd_replacement_d3_085}


def bsd_replacement_d3_086(bsd_replacement_d2_086):
    feature = _clean(bsd_replacement_d2_086)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00043000).reindex(feature.index)
BSD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['bsd_replacement_d3_086'] = {'inputs': ['bsd_replacement_d2_086'], 'func': bsd_replacement_d3_086}


def bsd_replacement_d3_087(bsd_replacement_d2_087):
    feature = _clean(bsd_replacement_d2_087)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00043500).reindex(feature.index)
BSD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['bsd_replacement_d3_087'] = {'inputs': ['bsd_replacement_d2_087'], 'func': bsd_replacement_d3_087}


def bsd_replacement_d3_088(bsd_replacement_d2_088):
    feature = _clean(bsd_replacement_d2_088)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00044000).reindex(feature.index)
BSD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['bsd_replacement_d3_088'] = {'inputs': ['bsd_replacement_d2_088'], 'func': bsd_replacement_d3_088}


def bsd_replacement_d3_089(bsd_replacement_d2_089):
    feature = _clean(bsd_replacement_d2_089)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00044500).reindex(feature.index)
BSD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['bsd_replacement_d3_089'] = {'inputs': ['bsd_replacement_d2_089'], 'func': bsd_replacement_d3_089}


def bsd_replacement_d3_090(bsd_replacement_d2_090):
    feature = _clean(bsd_replacement_d2_090)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00045000).reindex(feature.index)
BSD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['bsd_replacement_d3_090'] = {'inputs': ['bsd_replacement_d2_090'], 'func': bsd_replacement_d3_090}


def bsd_replacement_d3_091(bsd_replacement_d2_091):
    feature = _clean(bsd_replacement_d2_091)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00045500).reindex(feature.index)
BSD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['bsd_replacement_d3_091'] = {'inputs': ['bsd_replacement_d2_091'], 'func': bsd_replacement_d3_091}


def bsd_replacement_d3_092(bsd_replacement_d2_092):
    feature = _clean(bsd_replacement_d2_092)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00046000).reindex(feature.index)
BSD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['bsd_replacement_d3_092'] = {'inputs': ['bsd_replacement_d2_092'], 'func': bsd_replacement_d3_092}


def bsd_replacement_d3_093(bsd_replacement_d2_093):
    feature = _clean(bsd_replacement_d2_093)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00046500).reindex(feature.index)
BSD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['bsd_replacement_d3_093'] = {'inputs': ['bsd_replacement_d2_093'], 'func': bsd_replacement_d3_093}


def bsd_replacement_d3_094(bsd_replacement_d2_094):
    feature = _clean(bsd_replacement_d2_094)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00047000).reindex(feature.index)
BSD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['bsd_replacement_d3_094'] = {'inputs': ['bsd_replacement_d2_094'], 'func': bsd_replacement_d3_094}


def bsd_replacement_d3_095(bsd_replacement_d2_095):
    feature = _clean(bsd_replacement_d2_095)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00047500).reindex(feature.index)
BSD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['bsd_replacement_d3_095'] = {'inputs': ['bsd_replacement_d2_095'], 'func': bsd_replacement_d3_095}


def bsd_replacement_d3_096(bsd_replacement_d2_096):
    feature = _clean(bsd_replacement_d2_096)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00048000).reindex(feature.index)
BSD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['bsd_replacement_d3_096'] = {'inputs': ['bsd_replacement_d2_096'], 'func': bsd_replacement_d3_096}


def bsd_replacement_d3_097(bsd_replacement_d2_097):
    feature = _clean(bsd_replacement_d2_097)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00048500).reindex(feature.index)
BSD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['bsd_replacement_d3_097'] = {'inputs': ['bsd_replacement_d2_097'], 'func': bsd_replacement_d3_097}


def bsd_replacement_d3_098(bsd_replacement_d2_098):
    feature = _clean(bsd_replacement_d2_098)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00049000).reindex(feature.index)
BSD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['bsd_replacement_d3_098'] = {'inputs': ['bsd_replacement_d2_098'], 'func': bsd_replacement_d3_098}


def bsd_replacement_d3_099(bsd_replacement_d2_099):
    feature = _clean(bsd_replacement_d2_099)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00049500).reindex(feature.index)
BSD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['bsd_replacement_d3_099'] = {'inputs': ['bsd_replacement_d2_099'], 'func': bsd_replacement_d3_099}


def bsd_replacement_d3_100(bsd_replacement_d2_100):
    feature = _clean(bsd_replacement_d2_100)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00050000).reindex(feature.index)
BSD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['bsd_replacement_d3_100'] = {'inputs': ['bsd_replacement_d2_100'], 'func': bsd_replacement_d3_100}


def bsd_replacement_d3_101(bsd_replacement_d2_101):
    feature = _clean(bsd_replacement_d2_101)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00050500).reindex(feature.index)
BSD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['bsd_replacement_d3_101'] = {'inputs': ['bsd_replacement_d2_101'], 'func': bsd_replacement_d3_101}


def bsd_replacement_d3_102(bsd_replacement_d2_102):
    feature = _clean(bsd_replacement_d2_102)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00051000).reindex(feature.index)
BSD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['bsd_replacement_d3_102'] = {'inputs': ['bsd_replacement_d2_102'], 'func': bsd_replacement_d3_102}


def bsd_replacement_d3_103(bsd_replacement_d2_103):
    feature = _clean(bsd_replacement_d2_103)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00051500).reindex(feature.index)
BSD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['bsd_replacement_d3_103'] = {'inputs': ['bsd_replacement_d2_103'], 'func': bsd_replacement_d3_103}


def bsd_replacement_d3_104(bsd_replacement_d2_104):
    feature = _clean(bsd_replacement_d2_104)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00052000).reindex(feature.index)
BSD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['bsd_replacement_d3_104'] = {'inputs': ['bsd_replacement_d2_104'], 'func': bsd_replacement_d3_104}


def bsd_replacement_d3_105(bsd_replacement_d2_105):
    feature = _clean(bsd_replacement_d2_105)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00052500).reindex(feature.index)
BSD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['bsd_replacement_d3_105'] = {'inputs': ['bsd_replacement_d2_105'], 'func': bsd_replacement_d3_105}


def bsd_replacement_d3_106(bsd_replacement_d2_106):
    feature = _clean(bsd_replacement_d2_106)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00053000).reindex(feature.index)
BSD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['bsd_replacement_d3_106'] = {'inputs': ['bsd_replacement_d2_106'], 'func': bsd_replacement_d3_106}


def bsd_replacement_d3_107(bsd_replacement_d2_107):
    feature = _clean(bsd_replacement_d2_107)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00053500).reindex(feature.index)
BSD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['bsd_replacement_d3_107'] = {'inputs': ['bsd_replacement_d2_107'], 'func': bsd_replacement_d3_107}


def bsd_replacement_d3_108(bsd_replacement_d2_108):
    feature = _clean(bsd_replacement_d2_108)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00054000).reindex(feature.index)
BSD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['bsd_replacement_d3_108'] = {'inputs': ['bsd_replacement_d2_108'], 'func': bsd_replacement_d3_108}


def bsd_replacement_d3_109(bsd_replacement_d2_109):
    feature = _clean(bsd_replacement_d2_109)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00054500).reindex(feature.index)
BSD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['bsd_replacement_d3_109'] = {'inputs': ['bsd_replacement_d2_109'], 'func': bsd_replacement_d3_109}


def bsd_replacement_d3_110(bsd_replacement_d2_110):
    feature = _clean(bsd_replacement_d2_110)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00055000).reindex(feature.index)
BSD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['bsd_replacement_d3_110'] = {'inputs': ['bsd_replacement_d2_110'], 'func': bsd_replacement_d3_110}


def bsd_replacement_d3_111(bsd_replacement_d2_111):
    feature = _clean(bsd_replacement_d2_111)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00055500).reindex(feature.index)
BSD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['bsd_replacement_d3_111'] = {'inputs': ['bsd_replacement_d2_111'], 'func': bsd_replacement_d3_111}


def bsd_replacement_d3_112(bsd_replacement_d2_112):
    feature = _clean(bsd_replacement_d2_112)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00056000).reindex(feature.index)
BSD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['bsd_replacement_d3_112'] = {'inputs': ['bsd_replacement_d2_112'], 'func': bsd_replacement_d3_112}


def bsd_replacement_d3_113(bsd_replacement_d2_113):
    feature = _clean(bsd_replacement_d2_113)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00056500).reindex(feature.index)
BSD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['bsd_replacement_d3_113'] = {'inputs': ['bsd_replacement_d2_113'], 'func': bsd_replacement_d3_113}


def bsd_replacement_d3_114(bsd_replacement_d2_114):
    feature = _clean(bsd_replacement_d2_114)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00057000).reindex(feature.index)
BSD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['bsd_replacement_d3_114'] = {'inputs': ['bsd_replacement_d2_114'], 'func': bsd_replacement_d3_114}


def bsd_replacement_d3_115(bsd_replacement_d2_115):
    feature = _clean(bsd_replacement_d2_115)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00057500).reindex(feature.index)
BSD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['bsd_replacement_d3_115'] = {'inputs': ['bsd_replacement_d2_115'], 'func': bsd_replacement_d3_115}


def bsd_replacement_d3_116(bsd_replacement_d2_116):
    feature = _clean(bsd_replacement_d2_116)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00058000).reindex(feature.index)
BSD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['bsd_replacement_d3_116'] = {'inputs': ['bsd_replacement_d2_116'], 'func': bsd_replacement_d3_116}


def bsd_replacement_d3_117(bsd_replacement_d2_117):
    feature = _clean(bsd_replacement_d2_117)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00058500).reindex(feature.index)
BSD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['bsd_replacement_d3_117'] = {'inputs': ['bsd_replacement_d2_117'], 'func': bsd_replacement_d3_117}


def bsd_replacement_d3_118(bsd_replacement_d2_118):
    feature = _clean(bsd_replacement_d2_118)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00059000).reindex(feature.index)
BSD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['bsd_replacement_d3_118'] = {'inputs': ['bsd_replacement_d2_118'], 'func': bsd_replacement_d3_118}


def bsd_replacement_d3_119(bsd_replacement_d2_119):
    feature = _clean(bsd_replacement_d2_119)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00059500).reindex(feature.index)
BSD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['bsd_replacement_d3_119'] = {'inputs': ['bsd_replacement_d2_119'], 'func': bsd_replacement_d3_119}


def bsd_replacement_d3_120(bsd_replacement_d2_120):
    feature = _clean(bsd_replacement_d2_120)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00060000).reindex(feature.index)
BSD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['bsd_replacement_d3_120'] = {'inputs': ['bsd_replacement_d2_120'], 'func': bsd_replacement_d3_120}


def bsd_replacement_d3_121(bsd_replacement_d2_121):
    feature = _clean(bsd_replacement_d2_121)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00060500).reindex(feature.index)
BSD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['bsd_replacement_d3_121'] = {'inputs': ['bsd_replacement_d2_121'], 'func': bsd_replacement_d3_121}


def bsd_replacement_d3_122(bsd_replacement_d2_122):
    feature = _clean(bsd_replacement_d2_122)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00061000).reindex(feature.index)
BSD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['bsd_replacement_d3_122'] = {'inputs': ['bsd_replacement_d2_122'], 'func': bsd_replacement_d3_122}


def bsd_replacement_d3_123(bsd_replacement_d2_123):
    feature = _clean(bsd_replacement_d2_123)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00061500).reindex(feature.index)
BSD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['bsd_replacement_d3_123'] = {'inputs': ['bsd_replacement_d2_123'], 'func': bsd_replacement_d3_123}


def bsd_replacement_d3_124(bsd_replacement_d2_124):
    feature = _clean(bsd_replacement_d2_124)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00062000).reindex(feature.index)
BSD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['bsd_replacement_d3_124'] = {'inputs': ['bsd_replacement_d2_124'], 'func': bsd_replacement_d3_124}


def bsd_replacement_d3_125(bsd_replacement_d2_125):
    feature = _clean(bsd_replacement_d2_125)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00062500).reindex(feature.index)
BSD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['bsd_replacement_d3_125'] = {'inputs': ['bsd_replacement_d2_125'], 'func': bsd_replacement_d3_125}


def bsd_replacement_d3_126(bsd_replacement_d2_126):
    feature = _clean(bsd_replacement_d2_126)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00063000).reindex(feature.index)
BSD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['bsd_replacement_d3_126'] = {'inputs': ['bsd_replacement_d2_126'], 'func': bsd_replacement_d3_126}


def bsd_replacement_d3_127(bsd_replacement_d2_127):
    feature = _clean(bsd_replacement_d2_127)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00063500).reindex(feature.index)
BSD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['bsd_replacement_d3_127'] = {'inputs': ['bsd_replacement_d2_127'], 'func': bsd_replacement_d3_127}


def bsd_replacement_d3_128(bsd_replacement_d2_128):
    feature = _clean(bsd_replacement_d2_128)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00064000).reindex(feature.index)
BSD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['bsd_replacement_d3_128'] = {'inputs': ['bsd_replacement_d2_128'], 'func': bsd_replacement_d3_128}


def bsd_replacement_d3_129(bsd_replacement_d2_129):
    feature = _clean(bsd_replacement_d2_129)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00064500).reindex(feature.index)
BSD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['bsd_replacement_d3_129'] = {'inputs': ['bsd_replacement_d2_129'], 'func': bsd_replacement_d3_129}


def bsd_replacement_d3_130(bsd_replacement_d2_130):
    feature = _clean(bsd_replacement_d2_130)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00065000).reindex(feature.index)
BSD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['bsd_replacement_d3_130'] = {'inputs': ['bsd_replacement_d2_130'], 'func': bsd_replacement_d3_130}


def bsd_replacement_d3_131(bsd_replacement_d2_131):
    feature = _clean(bsd_replacement_d2_131)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00065500).reindex(feature.index)
BSD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['bsd_replacement_d3_131'] = {'inputs': ['bsd_replacement_d2_131'], 'func': bsd_replacement_d3_131}


def bsd_replacement_d3_132(bsd_replacement_d2_132):
    feature = _clean(bsd_replacement_d2_132)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00066000).reindex(feature.index)
BSD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['bsd_replacement_d3_132'] = {'inputs': ['bsd_replacement_d2_132'], 'func': bsd_replacement_d3_132}


def bsd_replacement_d3_133(bsd_replacement_d2_133):
    feature = _clean(bsd_replacement_d2_133)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00066500).reindex(feature.index)
BSD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['bsd_replacement_d3_133'] = {'inputs': ['bsd_replacement_d2_133'], 'func': bsd_replacement_d3_133}


def bsd_replacement_d3_134(bsd_replacement_d2_134):
    feature = _clean(bsd_replacement_d2_134)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00067000).reindex(feature.index)
BSD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['bsd_replacement_d3_134'] = {'inputs': ['bsd_replacement_d2_134'], 'func': bsd_replacement_d3_134}


def bsd_replacement_d3_135(bsd_replacement_d2_135):
    feature = _clean(bsd_replacement_d2_135)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00067500).reindex(feature.index)
BSD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['bsd_replacement_d3_135'] = {'inputs': ['bsd_replacement_d2_135'], 'func': bsd_replacement_d3_135}


def bsd_replacement_d3_136(bsd_replacement_d2_136):
    feature = _clean(bsd_replacement_d2_136)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00068000).reindex(feature.index)
BSD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['bsd_replacement_d3_136'] = {'inputs': ['bsd_replacement_d2_136'], 'func': bsd_replacement_d3_136}


def bsd_replacement_d3_137(bsd_replacement_d2_137):
    feature = _clean(bsd_replacement_d2_137)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00068500).reindex(feature.index)
BSD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['bsd_replacement_d3_137'] = {'inputs': ['bsd_replacement_d2_137'], 'func': bsd_replacement_d3_137}


def bsd_replacement_d3_138(bsd_replacement_d2_138):
    feature = _clean(bsd_replacement_d2_138)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00069000).reindex(feature.index)
BSD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['bsd_replacement_d3_138'] = {'inputs': ['bsd_replacement_d2_138'], 'func': bsd_replacement_d3_138}


def bsd_replacement_d3_139(bsd_replacement_d2_139):
    feature = _clean(bsd_replacement_d2_139)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00069500).reindex(feature.index)
BSD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['bsd_replacement_d3_139'] = {'inputs': ['bsd_replacement_d2_139'], 'func': bsd_replacement_d3_139}


def bsd_replacement_d3_140(bsd_replacement_d2_140):
    feature = _clean(bsd_replacement_d2_140)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00070000).reindex(feature.index)
BSD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['bsd_replacement_d3_140'] = {'inputs': ['bsd_replacement_d2_140'], 'func': bsd_replacement_d3_140}


def bsd_replacement_d3_141(bsd_replacement_d2_141):
    feature = _clean(bsd_replacement_d2_141)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00070500).reindex(feature.index)
BSD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['bsd_replacement_d3_141'] = {'inputs': ['bsd_replacement_d2_141'], 'func': bsd_replacement_d3_141}


def bsd_replacement_d3_142(bsd_replacement_d2_142):
    feature = _clean(bsd_replacement_d2_142)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00071000).reindex(feature.index)
BSD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['bsd_replacement_d3_142'] = {'inputs': ['bsd_replacement_d2_142'], 'func': bsd_replacement_d3_142}


def bsd_replacement_d3_143(bsd_replacement_d2_143):
    feature = _clean(bsd_replacement_d2_143)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00071500).reindex(feature.index)
BSD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['bsd_replacement_d3_143'] = {'inputs': ['bsd_replacement_d2_143'], 'func': bsd_replacement_d3_143}


def bsd_replacement_d3_144(bsd_replacement_d2_144):
    feature = _clean(bsd_replacement_d2_144)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00072000).reindex(feature.index)
BSD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['bsd_replacement_d3_144'] = {'inputs': ['bsd_replacement_d2_144'], 'func': bsd_replacement_d3_144}


def bsd_replacement_d3_145(bsd_replacement_d2_145):
    feature = _clean(bsd_replacement_d2_145)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00072500).reindex(feature.index)
BSD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['bsd_replacement_d3_145'] = {'inputs': ['bsd_replacement_d2_145'], 'func': bsd_replacement_d3_145}


def bsd_replacement_d3_146(bsd_replacement_d2_146):
    feature = _clean(bsd_replacement_d2_146)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00073000).reindex(feature.index)
BSD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['bsd_replacement_d3_146'] = {'inputs': ['bsd_replacement_d2_146'], 'func': bsd_replacement_d3_146}


def bsd_replacement_d3_147(bsd_replacement_d2_147):
    feature = _clean(bsd_replacement_d2_147)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00073500).reindex(feature.index)
BSD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['bsd_replacement_d3_147'] = {'inputs': ['bsd_replacement_d2_147'], 'func': bsd_replacement_d3_147}


def bsd_replacement_d3_148(bsd_replacement_d2_148):
    feature = _clean(bsd_replacement_d2_148)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00074000).reindex(feature.index)
BSD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['bsd_replacement_d3_148'] = {'inputs': ['bsd_replacement_d2_148'], 'func': bsd_replacement_d3_148}


def bsd_replacement_d3_149(bsd_replacement_d2_149):
    feature = _clean(bsd_replacement_d2_149)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00074500).reindex(feature.index)
BSD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['bsd_replacement_d3_149'] = {'inputs': ['bsd_replacement_d2_149'], 'func': bsd_replacement_d3_149}


def bsd_replacement_d3_150(bsd_replacement_d2_150):
    feature = _clean(bsd_replacement_d2_150)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00075000).reindex(feature.index)
BSD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['bsd_replacement_d3_150'] = {'inputs': ['bsd_replacement_d2_150'], 'func': bsd_replacement_d3_150}


def bsd_replacement_d3_151(bsd_replacement_d2_151):
    feature = _clean(bsd_replacement_d2_151)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00075500).reindex(feature.index)
BSD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['bsd_replacement_d3_151'] = {'inputs': ['bsd_replacement_d2_151'], 'func': bsd_replacement_d3_151}


def bsd_replacement_d3_152(bsd_replacement_d2_152):
    feature = _clean(bsd_replacement_d2_152)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00076000).reindex(feature.index)
BSD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['bsd_replacement_d3_152'] = {'inputs': ['bsd_replacement_d2_152'], 'func': bsd_replacement_d3_152}


def bsd_replacement_d3_153(bsd_replacement_d2_153):
    feature = _clean(bsd_replacement_d2_153)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00076500).reindex(feature.index)
BSD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['bsd_replacement_d3_153'] = {'inputs': ['bsd_replacement_d2_153'], 'func': bsd_replacement_d3_153}


def bsd_replacement_d3_154(bsd_replacement_d2_154):
    feature = _clean(bsd_replacement_d2_154)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00077000).reindex(feature.index)
BSD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['bsd_replacement_d3_154'] = {'inputs': ['bsd_replacement_d2_154'], 'func': bsd_replacement_d3_154}


def bsd_replacement_d3_155(bsd_replacement_d2_155):
    feature = _clean(bsd_replacement_d2_155)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00077500).reindex(feature.index)
BSD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['bsd_replacement_d3_155'] = {'inputs': ['bsd_replacement_d2_155'], 'func': bsd_replacement_d3_155}


def bsd_replacement_d3_156(bsd_replacement_d2_156):
    feature = _clean(bsd_replacement_d2_156)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00078000).reindex(feature.index)
BSD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['bsd_replacement_d3_156'] = {'inputs': ['bsd_replacement_d2_156'], 'func': bsd_replacement_d3_156}


def bsd_replacement_d3_157(bsd_replacement_d2_157):
    feature = _clean(bsd_replacement_d2_157)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00078500).reindex(feature.index)
BSD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['bsd_replacement_d3_157'] = {'inputs': ['bsd_replacement_d2_157'], 'func': bsd_replacement_d3_157}


def bsd_replacement_d3_158(bsd_replacement_d2_158):
    feature = _clean(bsd_replacement_d2_158)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00079000).reindex(feature.index)
BSD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['bsd_replacement_d3_158'] = {'inputs': ['bsd_replacement_d2_158'], 'func': bsd_replacement_d3_158}


def bsd_replacement_d3_159(bsd_replacement_d2_159):
    feature = _clean(bsd_replacement_d2_159)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00079500).reindex(feature.index)
BSD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['bsd_replacement_d3_159'] = {'inputs': ['bsd_replacement_d2_159'], 'func': bsd_replacement_d3_159}


def bsd_replacement_d3_160(bsd_replacement_d2_160):
    feature = _clean(bsd_replacement_d2_160)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00080000).reindex(feature.index)
BSD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['bsd_replacement_d3_160'] = {'inputs': ['bsd_replacement_d2_160'], 'func': bsd_replacement_d3_160}


def bsd_replacement_d3_161(bsd_replacement_d2_161):
    feature = _clean(bsd_replacement_d2_161)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00080500).reindex(feature.index)
BSD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['bsd_replacement_d3_161'] = {'inputs': ['bsd_replacement_d2_161'], 'func': bsd_replacement_d3_161}


def bsd_replacement_d3_162(bsd_replacement_d2_162):
    feature = _clean(bsd_replacement_d2_162)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00081000).reindex(feature.index)
BSD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['bsd_replacement_d3_162'] = {'inputs': ['bsd_replacement_d2_162'], 'func': bsd_replacement_d3_162}


def bsd_replacement_d3_163(bsd_replacement_d2_163):
    feature = _clean(bsd_replacement_d2_163)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00081500).reindex(feature.index)
BSD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['bsd_replacement_d3_163'] = {'inputs': ['bsd_replacement_d2_163'], 'func': bsd_replacement_d3_163}


def bsd_replacement_d3_164(bsd_replacement_d2_164):
    feature = _clean(bsd_replacement_d2_164)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00082000).reindex(feature.index)
BSD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['bsd_replacement_d3_164'] = {'inputs': ['bsd_replacement_d2_164'], 'func': bsd_replacement_d3_164}


def bsd_replacement_d3_165(bsd_replacement_d2_165):
    feature = _clean(bsd_replacement_d2_165)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00082500).reindex(feature.index)
BSD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['bsd_replacement_d3_165'] = {'inputs': ['bsd_replacement_d2_165'], 'func': bsd_replacement_d3_165}


def bsd_replacement_d3_166(bsd_replacement_d2_166):
    feature = _clean(bsd_replacement_d2_166)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00083000).reindex(feature.index)
BSD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['bsd_replacement_d3_166'] = {'inputs': ['bsd_replacement_d2_166'], 'func': bsd_replacement_d3_166}


# Third-derivative extensions for repaired first-base features.
BSD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY = {}


def _base_universe_d3(feature, idx):
    feature = _clean(feature) if '_clean' in globals() else _s(feature).replace([np.inf, -np.inf], np.nan)
    windows = [1, 2, 3, 5, 8, 13, 21, 34, 55]
    lag = windows[(idx * 2) % len(windows)]
    smooth = windows[(idx * 5 + 2) % len(windows)]
    accel = feature.diff(lag)
    curve = feature - feature.rolling(max(3, smooth), min_periods=2).mean()
    out = accel + curve.fillna(0.0) * (0.00019 * ((idx % 19) + 1))
    return out.replace([np.inf, -np.inf], np.nan).reindex(feature.index)


def bsd_base_universe_d3_001_bsd_003_fcf_burn_to_cash_63(bsd_base_universe_d2_001_bsd_003_fcf_burn_to_cash_63):
    return _base_universe_d3(bsd_base_universe_d2_001_bsd_003_fcf_burn_to_cash_63, 1)
BSD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['bsd_base_universe_d3_001_bsd_003_fcf_burn_to_cash_63'] = {'inputs': ['bsd_base_universe_d2_001_bsd_003_fcf_burn_to_cash_63'], 'func': bsd_base_universe_d3_001_bsd_003_fcf_burn_to_cash_63}


def bsd_base_universe_d3_002_bsd_004_debt_to_equity_84(bsd_base_universe_d2_002_bsd_004_debt_to_equity_84):
    return _base_universe_d3(bsd_base_universe_d2_002_bsd_004_debt_to_equity_84, 2)
BSD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['bsd_base_universe_d3_002_bsd_004_debt_to_equity_84'] = {'inputs': ['bsd_base_universe_d2_002_bsd_004_debt_to_equity_84'], 'func': bsd_base_universe_d3_002_bsd_004_debt_to_equity_84}


def bsd_base_universe_d3_003_bsd_005_debt_to_assets_126(bsd_base_universe_d2_003_bsd_005_debt_to_assets_126):
    return _base_universe_d3(bsd_base_universe_d2_003_bsd_005_debt_to_assets_126, 3)
BSD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['bsd_base_universe_d3_003_bsd_005_debt_to_assets_126'] = {'inputs': ['bsd_base_universe_d2_003_bsd_005_debt_to_assets_126'], 'func': bsd_base_universe_d3_003_bsd_005_debt_to_assets_126}


def bsd_base_universe_d3_004_bsd_012_accrual_gap_1260(bsd_base_universe_d2_004_bsd_012_accrual_gap_1260):
    return _base_universe_d3(bsd_base_universe_d2_004_bsd_012_accrual_gap_1260, 4)
BSD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['bsd_base_universe_d3_004_bsd_012_accrual_gap_1260'] = {'inputs': ['bsd_base_universe_d2_004_bsd_012_accrual_gap_1260'], 'func': bsd_base_universe_d3_004_bsd_012_accrual_gap_1260}


def bsd_base_universe_d3_005_bsd_016_debt_to_equity_21(bsd_base_universe_d2_005_bsd_016_debt_to_equity_21):
    return _base_universe_d3(bsd_base_universe_d2_005_bsd_016_debt_to_equity_21, 5)
BSD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['bsd_base_universe_d3_005_bsd_016_debt_to_equity_21'] = {'inputs': ['bsd_base_universe_d2_005_bsd_016_debt_to_equity_21'], 'func': bsd_base_universe_d3_005_bsd_016_debt_to_equity_21}


def bsd_base_universe_d3_006_bsd_017_debt_to_assets_42(bsd_base_universe_d2_006_bsd_017_debt_to_assets_42):
    return _base_universe_d3(bsd_base_universe_d2_006_bsd_017_debt_to_assets_42, 6)
BSD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['bsd_base_universe_d3_006_bsd_017_debt_to_assets_42'] = {'inputs': ['bsd_base_universe_d2_006_bsd_017_debt_to_assets_42'], 'func': bsd_base_universe_d3_006_bsd_017_debt_to_assets_42}


def bsd_base_universe_d3_007_bsd_024_accrual_gap_504(bsd_base_universe_d2_007_bsd_024_accrual_gap_504):
    return _base_universe_d3(bsd_base_universe_d2_007_bsd_024_accrual_gap_504, 7)
BSD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['bsd_base_universe_d3_007_bsd_024_accrual_gap_504'] = {'inputs': ['bsd_base_universe_d2_007_bsd_024_accrual_gap_504'], 'func': bsd_base_universe_d3_007_bsd_024_accrual_gap_504}


def bsd_base_universe_d3_008_bsd_027_fcf_burn_to_cash_1260(bsd_base_universe_d2_008_bsd_027_fcf_burn_to_cash_1260):
    return _base_universe_d3(bsd_base_universe_d2_008_bsd_027_fcf_burn_to_cash_1260, 8)
BSD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['bsd_base_universe_d3_008_bsd_027_fcf_burn_to_cash_1260'] = {'inputs': ['bsd_base_universe_d2_008_bsd_027_fcf_burn_to_cash_1260'], 'func': bsd_base_universe_d3_008_bsd_027_fcf_burn_to_cash_1260}


def bsd_base_universe_d3_009_bsd_028_debt_to_equity_1512(bsd_base_universe_d2_009_bsd_028_debt_to_equity_1512):
    return _base_universe_d3(bsd_base_universe_d2_009_bsd_028_debt_to_equity_1512, 9)
BSD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['bsd_base_universe_d3_009_bsd_028_debt_to_equity_1512'] = {'inputs': ['bsd_base_universe_d2_009_bsd_028_debt_to_equity_1512'], 'func': bsd_base_universe_d3_009_bsd_028_debt_to_equity_1512}


def bsd_base_universe_d3_010_bsd_029_debt_to_assets_63(bsd_base_universe_d2_010_bsd_029_debt_to_assets_63):
    return _base_universe_d3(bsd_base_universe_d2_010_bsd_029_debt_to_assets_63, 10)
BSD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['bsd_base_universe_d3_010_bsd_029_debt_to_assets_63'] = {'inputs': ['bsd_base_universe_d2_010_bsd_029_debt_to_assets_63'], 'func': bsd_base_universe_d3_010_bsd_029_debt_to_assets_63}


def bsd_base_universe_d3_011_bsd_031_interest_coverage_stress_21(bsd_base_universe_d2_011_bsd_031_interest_coverage_stress_21):
    return _base_universe_d3(bsd_base_universe_d2_011_bsd_031_interest_coverage_stress_21, 11)
BSD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['bsd_base_universe_d3_011_bsd_031_interest_coverage_stress_21'] = {'inputs': ['bsd_base_universe_d2_011_bsd_031_interest_coverage_stress_21'], 'func': bsd_base_universe_d3_011_bsd_031_interest_coverage_stress_21}


def bsd_base_universe_d3_012_bsd_036_accrual_gap_189(bsd_base_universe_d2_012_bsd_036_accrual_gap_189):
    return _base_universe_d3(bsd_base_universe_d2_012_bsd_036_accrual_gap_189, 12)
BSD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['bsd_base_universe_d3_012_bsd_036_accrual_gap_189'] = {'inputs': ['bsd_base_universe_d2_012_bsd_036_accrual_gap_189'], 'func': bsd_base_universe_d3_012_bsd_036_accrual_gap_189}


def bsd_base_universe_d3_013_bsd_039_fcf_burn_to_cash_504(bsd_base_universe_d2_013_bsd_039_fcf_burn_to_cash_504):
    return _base_universe_d3(bsd_base_universe_d2_013_bsd_039_fcf_burn_to_cash_504, 13)
BSD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['bsd_base_universe_d3_013_bsd_039_fcf_burn_to_cash_504'] = {'inputs': ['bsd_base_universe_d2_013_bsd_039_fcf_burn_to_cash_504'], 'func': bsd_base_universe_d3_013_bsd_039_fcf_burn_to_cash_504}


def bsd_base_universe_d3_014_bsd_040_debt_to_equity_756(bsd_base_universe_d2_014_bsd_040_debt_to_equity_756):
    return _base_universe_d3(bsd_base_universe_d2_014_bsd_040_debt_to_equity_756, 14)
BSD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['bsd_base_universe_d3_014_bsd_040_debt_to_equity_756'] = {'inputs': ['bsd_base_universe_d2_014_bsd_040_debt_to_equity_756'], 'func': bsd_base_universe_d3_014_bsd_040_debt_to_equity_756}


def bsd_base_universe_d3_015_bsd_041_debt_to_assets_1008(bsd_base_universe_d2_015_bsd_041_debt_to_assets_1008):
    return _base_universe_d3(bsd_base_universe_d2_015_bsd_041_debt_to_assets_1008, 15)
BSD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['bsd_base_universe_d3_015_bsd_041_debt_to_assets_1008'] = {'inputs': ['bsd_base_universe_d2_015_bsd_041_debt_to_assets_1008'], 'func': bsd_base_universe_d3_015_bsd_041_debt_to_assets_1008}


def bsd_base_universe_d3_016_bsd_043_interest_coverage_stress_1512(bsd_base_universe_d2_016_bsd_043_interest_coverage_stress_1512):
    return _base_universe_d3(bsd_base_universe_d2_016_bsd_043_interest_coverage_stress_1512, 16)
BSD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['bsd_base_universe_d3_016_bsd_043_interest_coverage_stress_1512'] = {'inputs': ['bsd_base_universe_d2_016_bsd_043_interest_coverage_stress_1512'], 'func': bsd_base_universe_d3_016_bsd_043_interest_coverage_stress_1512}


def bsd_base_universe_d3_017_bsd_048_accrual_gap_63(bsd_base_universe_d2_017_bsd_048_accrual_gap_63):
    return _base_universe_d3(bsd_base_universe_d2_017_bsd_048_accrual_gap_63, 17)
BSD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['bsd_base_universe_d3_017_bsd_048_accrual_gap_63'] = {'inputs': ['bsd_base_universe_d2_017_bsd_048_accrual_gap_63'], 'func': bsd_base_universe_d3_017_bsd_048_accrual_gap_63}


def bsd_base_universe_d3_018_bsd_051_fcf_burn_to_cash_189(bsd_base_universe_d2_018_bsd_051_fcf_burn_to_cash_189):
    return _base_universe_d3(bsd_base_universe_d2_018_bsd_051_fcf_burn_to_cash_189, 18)
BSD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['bsd_base_universe_d3_018_bsd_051_fcf_burn_to_cash_189'] = {'inputs': ['bsd_base_universe_d2_018_bsd_051_fcf_burn_to_cash_189'], 'func': bsd_base_universe_d3_018_bsd_051_fcf_burn_to_cash_189}


def bsd_base_universe_d3_019_bsd_052_debt_to_equity_252(bsd_base_universe_d2_019_bsd_052_debt_to_equity_252):
    return _base_universe_d3(bsd_base_universe_d2_019_bsd_052_debt_to_equity_252, 19)
BSD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['bsd_base_universe_d3_019_bsd_052_debt_to_equity_252'] = {'inputs': ['bsd_base_universe_d2_019_bsd_052_debt_to_equity_252'], 'func': bsd_base_universe_d3_019_bsd_052_debt_to_equity_252}


def bsd_base_universe_d3_020_bsd_053_debt_to_assets_378(bsd_base_universe_d2_020_bsd_053_debt_to_assets_378):
    return _base_universe_d3(bsd_base_universe_d2_020_bsd_053_debt_to_assets_378, 20)
BSD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['bsd_base_universe_d3_020_bsd_053_debt_to_assets_378'] = {'inputs': ['bsd_base_universe_d2_020_bsd_053_debt_to_assets_378'], 'func': bsd_base_universe_d3_020_bsd_053_debt_to_assets_378}


def bsd_base_universe_d3_021_bsd_055_interest_coverage_stress_756(bsd_base_universe_d2_021_bsd_055_interest_coverage_stress_756):
    return _base_universe_d3(bsd_base_universe_d2_021_bsd_055_interest_coverage_stress_756, 21)
BSD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['bsd_base_universe_d3_021_bsd_055_interest_coverage_stress_756'] = {'inputs': ['bsd_base_universe_d2_021_bsd_055_interest_coverage_stress_756'], 'func': bsd_base_universe_d3_021_bsd_055_interest_coverage_stress_756}


def bsd_base_universe_d3_022_bsd_060_accrual_gap_252(bsd_base_universe_d2_022_bsd_060_accrual_gap_252):
    return _base_universe_d3(bsd_base_universe_d2_022_bsd_060_accrual_gap_252, 22)
BSD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['bsd_base_universe_d3_022_bsd_060_accrual_gap_252'] = {'inputs': ['bsd_base_universe_d2_022_bsd_060_accrual_gap_252'], 'func': bsd_base_universe_d3_022_bsd_060_accrual_gap_252}


def bsd_base_universe_d3_023_bsd_basefill_001(bsd_base_universe_d2_023_bsd_basefill_001):
    return _base_universe_d3(bsd_base_universe_d2_023_bsd_basefill_001, 23)
BSD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['bsd_base_universe_d3_023_bsd_basefill_001'] = {'inputs': ['bsd_base_universe_d2_023_bsd_basefill_001'], 'func': bsd_base_universe_d3_023_bsd_basefill_001}


def bsd_base_universe_d3_024_bsd_basefill_002(bsd_base_universe_d2_024_bsd_basefill_002):
    return _base_universe_d3(bsd_base_universe_d2_024_bsd_basefill_002, 24)
BSD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['bsd_base_universe_d3_024_bsd_basefill_002'] = {'inputs': ['bsd_base_universe_d2_024_bsd_basefill_002'], 'func': bsd_base_universe_d3_024_bsd_basefill_002}


def bsd_base_universe_d3_025_bsd_basefill_006(bsd_base_universe_d2_025_bsd_basefill_006):
    return _base_universe_d3(bsd_base_universe_d2_025_bsd_basefill_006, 25)
BSD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['bsd_base_universe_d3_025_bsd_basefill_006'] = {'inputs': ['bsd_base_universe_d2_025_bsd_basefill_006'], 'func': bsd_base_universe_d3_025_bsd_basefill_006}


def bsd_base_universe_d3_026_bsd_basefill_008(bsd_base_universe_d2_026_bsd_basefill_008):
    return _base_universe_d3(bsd_base_universe_d2_026_bsd_basefill_008, 26)
BSD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['bsd_base_universe_d3_026_bsd_basefill_008'] = {'inputs': ['bsd_base_universe_d2_026_bsd_basefill_008'], 'func': bsd_base_universe_d3_026_bsd_basefill_008}


def bsd_base_universe_d3_027_bsd_basefill_009(bsd_base_universe_d2_027_bsd_basefill_009):
    return _base_universe_d3(bsd_base_universe_d2_027_bsd_basefill_009, 27)
BSD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['bsd_base_universe_d3_027_bsd_basefill_009'] = {'inputs': ['bsd_base_universe_d2_027_bsd_basefill_009'], 'func': bsd_base_universe_d3_027_bsd_basefill_009}


def bsd_base_universe_d3_028_bsd_basefill_010(bsd_base_universe_d2_028_bsd_basefill_010):
    return _base_universe_d3(bsd_base_universe_d2_028_bsd_basefill_010, 28)
BSD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['bsd_base_universe_d3_028_bsd_basefill_010'] = {'inputs': ['bsd_base_universe_d2_028_bsd_basefill_010'], 'func': bsd_base_universe_d3_028_bsd_basefill_010}


def bsd_base_universe_d3_029_bsd_basefill_011(bsd_base_universe_d2_029_bsd_basefill_011):
    return _base_universe_d3(bsd_base_universe_d2_029_bsd_basefill_011, 29)
BSD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['bsd_base_universe_d3_029_bsd_basefill_011'] = {'inputs': ['bsd_base_universe_d2_029_bsd_basefill_011'], 'func': bsd_base_universe_d3_029_bsd_basefill_011}


def bsd_base_universe_d3_030_bsd_basefill_013(bsd_base_universe_d2_030_bsd_basefill_013):
    return _base_universe_d3(bsd_base_universe_d2_030_bsd_basefill_013, 30)
BSD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['bsd_base_universe_d3_030_bsd_basefill_013'] = {'inputs': ['bsd_base_universe_d2_030_bsd_basefill_013'], 'func': bsd_base_universe_d3_030_bsd_basefill_013}


def bsd_base_universe_d3_031_bsd_basefill_014(bsd_base_universe_d2_031_bsd_basefill_014):
    return _base_universe_d3(bsd_base_universe_d2_031_bsd_basefill_014, 31)
BSD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['bsd_base_universe_d3_031_bsd_basefill_014'] = {'inputs': ['bsd_base_universe_d2_031_bsd_basefill_014'], 'func': bsd_base_universe_d3_031_bsd_basefill_014}


def bsd_base_universe_d3_032_bsd_basefill_015(bsd_base_universe_d2_032_bsd_basefill_015):
    return _base_universe_d3(bsd_base_universe_d2_032_bsd_basefill_015, 32)
BSD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['bsd_base_universe_d3_032_bsd_basefill_015'] = {'inputs': ['bsd_base_universe_d2_032_bsd_basefill_015'], 'func': bsd_base_universe_d3_032_bsd_basefill_015}


def bsd_base_universe_d3_033_bsd_basefill_018(bsd_base_universe_d2_033_bsd_basefill_018):
    return _base_universe_d3(bsd_base_universe_d2_033_bsd_basefill_018, 33)
BSD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['bsd_base_universe_d3_033_bsd_basefill_018'] = {'inputs': ['bsd_base_universe_d2_033_bsd_basefill_018'], 'func': bsd_base_universe_d3_033_bsd_basefill_018}


def bsd_base_universe_d3_034_bsd_basefill_020(bsd_base_universe_d2_034_bsd_basefill_020):
    return _base_universe_d3(bsd_base_universe_d2_034_bsd_basefill_020, 34)
BSD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['bsd_base_universe_d3_034_bsd_basefill_020'] = {'inputs': ['bsd_base_universe_d2_034_bsd_basefill_020'], 'func': bsd_base_universe_d3_034_bsd_basefill_020}


def bsd_base_universe_d3_035_bsd_basefill_021(bsd_base_universe_d2_035_bsd_basefill_021):
    return _base_universe_d3(bsd_base_universe_d2_035_bsd_basefill_021, 35)
BSD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['bsd_base_universe_d3_035_bsd_basefill_021'] = {'inputs': ['bsd_base_universe_d2_035_bsd_basefill_021'], 'func': bsd_base_universe_d3_035_bsd_basefill_021}


def bsd_base_universe_d3_036_bsd_basefill_022(bsd_base_universe_d2_036_bsd_basefill_022):
    return _base_universe_d3(bsd_base_universe_d2_036_bsd_basefill_022, 36)
BSD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['bsd_base_universe_d3_036_bsd_basefill_022'] = {'inputs': ['bsd_base_universe_d2_036_bsd_basefill_022'], 'func': bsd_base_universe_d3_036_bsd_basefill_022}


def bsd_base_universe_d3_037_bsd_basefill_023(bsd_base_universe_d2_037_bsd_basefill_023):
    return _base_universe_d3(bsd_base_universe_d2_037_bsd_basefill_023, 37)
BSD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['bsd_base_universe_d3_037_bsd_basefill_023'] = {'inputs': ['bsd_base_universe_d2_037_bsd_basefill_023'], 'func': bsd_base_universe_d3_037_bsd_basefill_023}


def bsd_base_universe_d3_038_bsd_basefill_025(bsd_base_universe_d2_038_bsd_basefill_025):
    return _base_universe_d3(bsd_base_universe_d2_038_bsd_basefill_025, 38)
BSD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['bsd_base_universe_d3_038_bsd_basefill_025'] = {'inputs': ['bsd_base_universe_d2_038_bsd_basefill_025'], 'func': bsd_base_universe_d3_038_bsd_basefill_025}


def bsd_base_universe_d3_039_bsd_basefill_026(bsd_base_universe_d2_039_bsd_basefill_026):
    return _base_universe_d3(bsd_base_universe_d2_039_bsd_basefill_026, 39)
BSD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['bsd_base_universe_d3_039_bsd_basefill_026'] = {'inputs': ['bsd_base_universe_d2_039_bsd_basefill_026'], 'func': bsd_base_universe_d3_039_bsd_basefill_026}


def bsd_base_universe_d3_040_bsd_basefill_030(bsd_base_universe_d2_040_bsd_basefill_030):
    return _base_universe_d3(bsd_base_universe_d2_040_bsd_basefill_030, 40)
BSD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['bsd_base_universe_d3_040_bsd_basefill_030'] = {'inputs': ['bsd_base_universe_d2_040_bsd_basefill_030'], 'func': bsd_base_universe_d3_040_bsd_basefill_030}


def bsd_base_universe_d3_041_bsd_basefill_032(bsd_base_universe_d2_041_bsd_basefill_032):
    return _base_universe_d3(bsd_base_universe_d2_041_bsd_basefill_032, 41)
BSD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['bsd_base_universe_d3_041_bsd_basefill_032'] = {'inputs': ['bsd_base_universe_d2_041_bsd_basefill_032'], 'func': bsd_base_universe_d3_041_bsd_basefill_032}


def bsd_base_universe_d3_042_bsd_basefill_033(bsd_base_universe_d2_042_bsd_basefill_033):
    return _base_universe_d3(bsd_base_universe_d2_042_bsd_basefill_033, 42)
BSD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['bsd_base_universe_d3_042_bsd_basefill_033'] = {'inputs': ['bsd_base_universe_d2_042_bsd_basefill_033'], 'func': bsd_base_universe_d3_042_bsd_basefill_033}


def bsd_base_universe_d3_043_bsd_basefill_034(bsd_base_universe_d2_043_bsd_basefill_034):
    return _base_universe_d3(bsd_base_universe_d2_043_bsd_basefill_034, 43)
BSD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['bsd_base_universe_d3_043_bsd_basefill_034'] = {'inputs': ['bsd_base_universe_d2_043_bsd_basefill_034'], 'func': bsd_base_universe_d3_043_bsd_basefill_034}


def bsd_base_universe_d3_044_bsd_basefill_035(bsd_base_universe_d2_044_bsd_basefill_035):
    return _base_universe_d3(bsd_base_universe_d2_044_bsd_basefill_035, 44)
BSD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['bsd_base_universe_d3_044_bsd_basefill_035'] = {'inputs': ['bsd_base_universe_d2_044_bsd_basefill_035'], 'func': bsd_base_universe_d3_044_bsd_basefill_035}


def bsd_base_universe_d3_045_bsd_basefill_037(bsd_base_universe_d2_045_bsd_basefill_037):
    return _base_universe_d3(bsd_base_universe_d2_045_bsd_basefill_037, 45)
BSD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['bsd_base_universe_d3_045_bsd_basefill_037'] = {'inputs': ['bsd_base_universe_d2_045_bsd_basefill_037'], 'func': bsd_base_universe_d3_045_bsd_basefill_037}


def bsd_base_universe_d3_046_bsd_basefill_038(bsd_base_universe_d2_046_bsd_basefill_038):
    return _base_universe_d3(bsd_base_universe_d2_046_bsd_basefill_038, 46)
BSD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['bsd_base_universe_d3_046_bsd_basefill_038'] = {'inputs': ['bsd_base_universe_d2_046_bsd_basefill_038'], 'func': bsd_base_universe_d3_046_bsd_basefill_038}


def bsd_base_universe_d3_047_bsd_basefill_042(bsd_base_universe_d2_047_bsd_basefill_042):
    return _base_universe_d3(bsd_base_universe_d2_047_bsd_basefill_042, 47)
BSD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['bsd_base_universe_d3_047_bsd_basefill_042'] = {'inputs': ['bsd_base_universe_d2_047_bsd_basefill_042'], 'func': bsd_base_universe_d3_047_bsd_basefill_042}


def bsd_base_universe_d3_048_bsd_basefill_044(bsd_base_universe_d2_048_bsd_basefill_044):
    return _base_universe_d3(bsd_base_universe_d2_048_bsd_basefill_044, 48)
BSD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['bsd_base_universe_d3_048_bsd_basefill_044'] = {'inputs': ['bsd_base_universe_d2_048_bsd_basefill_044'], 'func': bsd_base_universe_d3_048_bsd_basefill_044}


def bsd_base_universe_d3_049_bsd_basefill_045(bsd_base_universe_d2_049_bsd_basefill_045):
    return _base_universe_d3(bsd_base_universe_d2_049_bsd_basefill_045, 49)
BSD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['bsd_base_universe_d3_049_bsd_basefill_045'] = {'inputs': ['bsd_base_universe_d2_049_bsd_basefill_045'], 'func': bsd_base_universe_d3_049_bsd_basefill_045}


def bsd_base_universe_d3_050_bsd_basefill_046(bsd_base_universe_d2_050_bsd_basefill_046):
    return _base_universe_d3(bsd_base_universe_d2_050_bsd_basefill_046, 50)
BSD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['bsd_base_universe_d3_050_bsd_basefill_046'] = {'inputs': ['bsd_base_universe_d2_050_bsd_basefill_046'], 'func': bsd_base_universe_d3_050_bsd_basefill_046}


def bsd_base_universe_d3_051_bsd_basefill_047(bsd_base_universe_d2_051_bsd_basefill_047):
    return _base_universe_d3(bsd_base_universe_d2_051_bsd_basefill_047, 51)
BSD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['bsd_base_universe_d3_051_bsd_basefill_047'] = {'inputs': ['bsd_base_universe_d2_051_bsd_basefill_047'], 'func': bsd_base_universe_d3_051_bsd_basefill_047}


def bsd_base_universe_d3_052_bsd_basefill_049(bsd_base_universe_d2_052_bsd_basefill_049):
    return _base_universe_d3(bsd_base_universe_d2_052_bsd_basefill_049, 52)
BSD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['bsd_base_universe_d3_052_bsd_basefill_049'] = {'inputs': ['bsd_base_universe_d2_052_bsd_basefill_049'], 'func': bsd_base_universe_d3_052_bsd_basefill_049}


def bsd_base_universe_d3_053_bsd_basefill_050(bsd_base_universe_d2_053_bsd_basefill_050):
    return _base_universe_d3(bsd_base_universe_d2_053_bsd_basefill_050, 53)
BSD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['bsd_base_universe_d3_053_bsd_basefill_050'] = {'inputs': ['bsd_base_universe_d2_053_bsd_basefill_050'], 'func': bsd_base_universe_d3_053_bsd_basefill_050}


def bsd_base_universe_d3_054_bsd_basefill_054(bsd_base_universe_d2_054_bsd_basefill_054):
    return _base_universe_d3(bsd_base_universe_d2_054_bsd_basefill_054, 54)
BSD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['bsd_base_universe_d3_054_bsd_basefill_054'] = {'inputs': ['bsd_base_universe_d2_054_bsd_basefill_054'], 'func': bsd_base_universe_d3_054_bsd_basefill_054}


def bsd_base_universe_d3_055_bsd_basefill_056(bsd_base_universe_d2_055_bsd_basefill_056):
    return _base_universe_d3(bsd_base_universe_d2_055_bsd_basefill_056, 55)
BSD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['bsd_base_universe_d3_055_bsd_basefill_056'] = {'inputs': ['bsd_base_universe_d2_055_bsd_basefill_056'], 'func': bsd_base_universe_d3_055_bsd_basefill_056}


def bsd_base_universe_d3_056_bsd_basefill_057(bsd_base_universe_d2_056_bsd_basefill_057):
    return _base_universe_d3(bsd_base_universe_d2_056_bsd_basefill_057, 56)
BSD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['bsd_base_universe_d3_056_bsd_basefill_057'] = {'inputs': ['bsd_base_universe_d2_056_bsd_basefill_057'], 'func': bsd_base_universe_d3_056_bsd_basefill_057}


def bsd_base_universe_d3_057_bsd_basefill_058(bsd_base_universe_d2_057_bsd_basefill_058):
    return _base_universe_d3(bsd_base_universe_d2_057_bsd_basefill_058, 57)
BSD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['bsd_base_universe_d3_057_bsd_basefill_058'] = {'inputs': ['bsd_base_universe_d2_057_bsd_basefill_058'], 'func': bsd_base_universe_d3_057_bsd_basefill_058}


def bsd_base_universe_d3_058_bsd_basefill_059(bsd_base_universe_d2_058_bsd_basefill_059):
    return _base_universe_d3(bsd_base_universe_d2_058_bsd_basefill_059, 58)
BSD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['bsd_base_universe_d3_058_bsd_basefill_059'] = {'inputs': ['bsd_base_universe_d2_058_bsd_basefill_059'], 'func': bsd_base_universe_d3_058_bsd_basefill_059}


def bsd_base_universe_d3_059_bsd_basefill_061(bsd_base_universe_d2_059_bsd_basefill_061):
    return _base_universe_d3(bsd_base_universe_d2_059_bsd_basefill_061, 59)
BSD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['bsd_base_universe_d3_059_bsd_basefill_061'] = {'inputs': ['bsd_base_universe_d2_059_bsd_basefill_061'], 'func': bsd_base_universe_d3_059_bsd_basefill_061}


def bsd_base_universe_d3_060_bsd_basefill_062(bsd_base_universe_d2_060_bsd_basefill_062):
    return _base_universe_d3(bsd_base_universe_d2_060_bsd_basefill_062, 60)
BSD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['bsd_base_universe_d3_060_bsd_basefill_062'] = {'inputs': ['bsd_base_universe_d2_060_bsd_basefill_062'], 'func': bsd_base_universe_d3_060_bsd_basefill_062}


def bsd_base_universe_d3_061_bsd_basefill_063(bsd_base_universe_d2_061_bsd_basefill_063):
    return _base_universe_d3(bsd_base_universe_d2_061_bsd_basefill_063, 61)
BSD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['bsd_base_universe_d3_061_bsd_basefill_063'] = {'inputs': ['bsd_base_universe_d2_061_bsd_basefill_063'], 'func': bsd_base_universe_d3_061_bsd_basefill_063}


def bsd_base_universe_d3_062_bsd_basefill_064(bsd_base_universe_d2_062_bsd_basefill_064):
    return _base_universe_d3(bsd_base_universe_d2_062_bsd_basefill_064, 62)
BSD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['bsd_base_universe_d3_062_bsd_basefill_064'] = {'inputs': ['bsd_base_universe_d2_062_bsd_basefill_064'], 'func': bsd_base_universe_d3_062_bsd_basefill_064}


def bsd_base_universe_d3_063_bsd_basefill_065(bsd_base_universe_d2_063_bsd_basefill_065):
    return _base_universe_d3(bsd_base_universe_d2_063_bsd_basefill_065, 63)
BSD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['bsd_base_universe_d3_063_bsd_basefill_065'] = {'inputs': ['bsd_base_universe_d2_063_bsd_basefill_065'], 'func': bsd_base_universe_d3_063_bsd_basefill_065}


def bsd_base_universe_d3_064_bsd_basefill_066(bsd_base_universe_d2_064_bsd_basefill_066):
    return _base_universe_d3(bsd_base_universe_d2_064_bsd_basefill_066, 64)
BSD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['bsd_base_universe_d3_064_bsd_basefill_066'] = {'inputs': ['bsd_base_universe_d2_064_bsd_basefill_066'], 'func': bsd_base_universe_d3_064_bsd_basefill_066}


def bsd_base_universe_d3_065_bsd_basefill_067(bsd_base_universe_d2_065_bsd_basefill_067):
    return _base_universe_d3(bsd_base_universe_d2_065_bsd_basefill_067, 65)
BSD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['bsd_base_universe_d3_065_bsd_basefill_067'] = {'inputs': ['bsd_base_universe_d2_065_bsd_basefill_067'], 'func': bsd_base_universe_d3_065_bsd_basefill_067}


def bsd_base_universe_d3_066_bsd_basefill_068(bsd_base_universe_d2_066_bsd_basefill_068):
    return _base_universe_d3(bsd_base_universe_d2_066_bsd_basefill_068, 66)
BSD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['bsd_base_universe_d3_066_bsd_basefill_068'] = {'inputs': ['bsd_base_universe_d2_066_bsd_basefill_068'], 'func': bsd_base_universe_d3_066_bsd_basefill_068}


def bsd_base_universe_d3_067_bsd_basefill_069(bsd_base_universe_d2_067_bsd_basefill_069):
    return _base_universe_d3(bsd_base_universe_d2_067_bsd_basefill_069, 67)
BSD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['bsd_base_universe_d3_067_bsd_basefill_069'] = {'inputs': ['bsd_base_universe_d2_067_bsd_basefill_069'], 'func': bsd_base_universe_d3_067_bsd_basefill_069}


def bsd_base_universe_d3_068_bsd_basefill_070(bsd_base_universe_d2_068_bsd_basefill_070):
    return _base_universe_d3(bsd_base_universe_d2_068_bsd_basefill_070, 68)
BSD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['bsd_base_universe_d3_068_bsd_basefill_070'] = {'inputs': ['bsd_base_universe_d2_068_bsd_basefill_070'], 'func': bsd_base_universe_d3_068_bsd_basefill_070}


def bsd_base_universe_d3_069_bsd_basefill_071(bsd_base_universe_d2_069_bsd_basefill_071):
    return _base_universe_d3(bsd_base_universe_d2_069_bsd_basefill_071, 69)
BSD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['bsd_base_universe_d3_069_bsd_basefill_071'] = {'inputs': ['bsd_base_universe_d2_069_bsd_basefill_071'], 'func': bsd_base_universe_d3_069_bsd_basefill_071}


def bsd_base_universe_d3_070_bsd_basefill_072(bsd_base_universe_d2_070_bsd_basefill_072):
    return _base_universe_d3(bsd_base_universe_d2_070_bsd_basefill_072, 70)
BSD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['bsd_base_universe_d3_070_bsd_basefill_072'] = {'inputs': ['bsd_base_universe_d2_070_bsd_basefill_072'], 'func': bsd_base_universe_d3_070_bsd_basefill_072}


def bsd_base_universe_d3_071_bsd_basefill_073(bsd_base_universe_d2_071_bsd_basefill_073):
    return _base_universe_d3(bsd_base_universe_d2_071_bsd_basefill_073, 71)
BSD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['bsd_base_universe_d3_071_bsd_basefill_073'] = {'inputs': ['bsd_base_universe_d2_071_bsd_basefill_073'], 'func': bsd_base_universe_d3_071_bsd_basefill_073}


def bsd_base_universe_d3_072_bsd_basefill_074(bsd_base_universe_d2_072_bsd_basefill_074):
    return _base_universe_d3(bsd_base_universe_d2_072_bsd_basefill_074, 72)
BSD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['bsd_base_universe_d3_072_bsd_basefill_074'] = {'inputs': ['bsd_base_universe_d2_072_bsd_basefill_074'], 'func': bsd_base_universe_d3_072_bsd_basefill_074}


def bsd_base_universe_d3_073_bsd_basefill_075(bsd_base_universe_d2_073_bsd_basefill_075):
    return _base_universe_d3(bsd_base_universe_d2_073_bsd_basefill_075, 73)
BSD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['bsd_base_universe_d3_073_bsd_basefill_075'] = {'inputs': ['bsd_base_universe_d2_073_bsd_basefill_075'], 'func': bsd_base_universe_d3_073_bsd_basefill_075}
