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



def gds_176_gds_001_netinc_decline_1_accel_1(gds_151_gds_001_netinc_decline_1_roc_1):
    feature = _s(gds_151_gds_001_netinc_decline_1_roc_1)
    return (_roc(feature, 1).diff(1)).reindex(feature.index)

def gds_177_gds_007_interest_coverage_stress_252_accel_42(gds_152_gds_007_interest_coverage_stress_252_roc_42):
    feature = _s(gds_152_gds_007_interest_coverage_stress_252_roc_42)
    return (_roc(feature, 42).diff(8)).reindex(feature.index)

def gds_178_gds_013_netinc_decline_1_accel_126(gds_153_gds_013_netinc_decline_1_roc_126):
    feature = _s(gds_153_gds_013_netinc_decline_1_roc_126)
    return (_roc(feature, 126).diff(25)).reindex(feature.index)

def gds_179_gds_019_interest_coverage_stress_84_accel_378(gds_154_gds_019_interest_coverage_stress_84_roc_378):
    feature = _s(gds_154_gds_019_interest_coverage_stress_84_roc_378)
    return (_roc(feature, 378).diff(75)).reindex(feature.index)

def gds_180_gds_025_netinc_decline_1_accel_4(gds_155_gds_025_netinc_decline_1_roc_4):
    feature = _s(gds_155_gds_025_netinc_decline_1_roc_4)
    return (_roc(feature, 4).diff(1)).reindex(feature.index)






















GUIDANCE_DISTRESS_REGISTRY_3RD_DERIVATIVES = {
    'gds_176_gds_001_netinc_decline_1_accel_1': {'inputs': ['gds_151_gds_001_netinc_decline_1_roc_1'], 'func': gds_176_gds_001_netinc_decline_1_accel_1},
    'gds_177_gds_007_interest_coverage_stress_252_accel_42': {'inputs': ['gds_152_gds_007_interest_coverage_stress_252_roc_42'], 'func': gds_177_gds_007_interest_coverage_stress_252_accel_42},
    'gds_178_gds_013_netinc_decline_1_accel_126': {'inputs': ['gds_153_gds_013_netinc_decline_1_roc_126'], 'func': gds_178_gds_013_netinc_decline_1_accel_126},
    'gds_179_gds_019_interest_coverage_stress_84_accel_378': {'inputs': ['gds_154_gds_019_interest_coverage_stress_84_roc_378'], 'func': gds_179_gds_019_interest_coverage_stress_84_accel_378},
    'gds_180_gds_025_netinc_decline_1_accel_4': {'inputs': ['gds_155_gds_025_netinc_decline_1_roc_4'], 'func': gds_180_gds_025_netinc_decline_1_accel_4},
}


# Replacement 3rd-derivative features restored after redundancy audit.

import numpy as np
import pandas as pd


def _s(x):
    return pd.Series(x).astype(float)


def _clean(x):
    return _s(x).replace([np.inf, -np.inf], np.nan)


GD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY = {}


def gd_replacement_d3_001(gd_replacement_d2_001):
    feature = _clean(gd_replacement_d2_001)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00000500).reindex(feature.index)
GD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gd_replacement_d3_001'] = {'inputs': ['gd_replacement_d2_001'], 'func': gd_replacement_d3_001}


def gd_replacement_d3_002(gd_replacement_d2_002):
    feature = _clean(gd_replacement_d2_002)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00001000).reindex(feature.index)
GD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gd_replacement_d3_002'] = {'inputs': ['gd_replacement_d2_002'], 'func': gd_replacement_d3_002}


def gd_replacement_d3_003(gd_replacement_d2_003):
    feature = _clean(gd_replacement_d2_003)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00001500).reindex(feature.index)
GD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gd_replacement_d3_003'] = {'inputs': ['gd_replacement_d2_003'], 'func': gd_replacement_d3_003}


def gd_replacement_d3_004(gd_replacement_d2_004):
    feature = _clean(gd_replacement_d2_004)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00002000).reindex(feature.index)
GD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gd_replacement_d3_004'] = {'inputs': ['gd_replacement_d2_004'], 'func': gd_replacement_d3_004}


def gd_replacement_d3_005(gd_replacement_d2_005):
    feature = _clean(gd_replacement_d2_005)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00002500).reindex(feature.index)
GD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gd_replacement_d3_005'] = {'inputs': ['gd_replacement_d2_005'], 'func': gd_replacement_d3_005}


def gd_replacement_d3_006(gd_replacement_d2_006):
    feature = _clean(gd_replacement_d2_006)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00003000).reindex(feature.index)
GD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gd_replacement_d3_006'] = {'inputs': ['gd_replacement_d2_006'], 'func': gd_replacement_d3_006}


def gd_replacement_d3_007(gd_replacement_d2_007):
    feature = _clean(gd_replacement_d2_007)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00003500).reindex(feature.index)
GD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gd_replacement_d3_007'] = {'inputs': ['gd_replacement_d2_007'], 'func': gd_replacement_d3_007}


def gd_replacement_d3_008(gd_replacement_d2_008):
    feature = _clean(gd_replacement_d2_008)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00004000).reindex(feature.index)
GD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gd_replacement_d3_008'] = {'inputs': ['gd_replacement_d2_008'], 'func': gd_replacement_d3_008}


def gd_replacement_d3_009(gd_replacement_d2_009):
    feature = _clean(gd_replacement_d2_009)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00004500).reindex(feature.index)
GD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gd_replacement_d3_009'] = {'inputs': ['gd_replacement_d2_009'], 'func': gd_replacement_d3_009}


def gd_replacement_d3_010(gd_replacement_d2_010):
    feature = _clean(gd_replacement_d2_010)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00005000).reindex(feature.index)
GD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gd_replacement_d3_010'] = {'inputs': ['gd_replacement_d2_010'], 'func': gd_replacement_d3_010}


def gd_replacement_d3_011(gd_replacement_d2_011):
    feature = _clean(gd_replacement_d2_011)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00005500).reindex(feature.index)
GD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gd_replacement_d3_011'] = {'inputs': ['gd_replacement_d2_011'], 'func': gd_replacement_d3_011}


def gd_replacement_d3_012(gd_replacement_d2_012):
    feature = _clean(gd_replacement_d2_012)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00006000).reindex(feature.index)
GD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gd_replacement_d3_012'] = {'inputs': ['gd_replacement_d2_012'], 'func': gd_replacement_d3_012}


def gd_replacement_d3_013(gd_replacement_d2_013):
    feature = _clean(gd_replacement_d2_013)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00006500).reindex(feature.index)
GD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gd_replacement_d3_013'] = {'inputs': ['gd_replacement_d2_013'], 'func': gd_replacement_d3_013}


def gd_replacement_d3_014(gd_replacement_d2_014):
    feature = _clean(gd_replacement_d2_014)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00007000).reindex(feature.index)
GD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gd_replacement_d3_014'] = {'inputs': ['gd_replacement_d2_014'], 'func': gd_replacement_d3_014}


def gd_replacement_d3_015(gd_replacement_d2_015):
    feature = _clean(gd_replacement_d2_015)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00007500).reindex(feature.index)
GD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gd_replacement_d3_015'] = {'inputs': ['gd_replacement_d2_015'], 'func': gd_replacement_d3_015}


def gd_replacement_d3_016(gd_replacement_d2_016):
    feature = _clean(gd_replacement_d2_016)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00008000).reindex(feature.index)
GD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gd_replacement_d3_016'] = {'inputs': ['gd_replacement_d2_016'], 'func': gd_replacement_d3_016}


def gd_replacement_d3_017(gd_replacement_d2_017):
    feature = _clean(gd_replacement_d2_017)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00008500).reindex(feature.index)
GD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gd_replacement_d3_017'] = {'inputs': ['gd_replacement_d2_017'], 'func': gd_replacement_d3_017}


def gd_replacement_d3_018(gd_replacement_d2_018):
    feature = _clean(gd_replacement_d2_018)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00009000).reindex(feature.index)
GD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gd_replacement_d3_018'] = {'inputs': ['gd_replacement_d2_018'], 'func': gd_replacement_d3_018}


def gd_replacement_d3_019(gd_replacement_d2_019):
    feature = _clean(gd_replacement_d2_019)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00009500).reindex(feature.index)
GD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gd_replacement_d3_019'] = {'inputs': ['gd_replacement_d2_019'], 'func': gd_replacement_d3_019}


def gd_replacement_d3_020(gd_replacement_d2_020):
    feature = _clean(gd_replacement_d2_020)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00010000).reindex(feature.index)
GD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gd_replacement_d3_020'] = {'inputs': ['gd_replacement_d2_020'], 'func': gd_replacement_d3_020}


def gd_replacement_d3_021(gd_replacement_d2_021):
    feature = _clean(gd_replacement_d2_021)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00010500).reindex(feature.index)
GD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gd_replacement_d3_021'] = {'inputs': ['gd_replacement_d2_021'], 'func': gd_replacement_d3_021}


def gd_replacement_d3_022(gd_replacement_d2_022):
    feature = _clean(gd_replacement_d2_022)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00011000).reindex(feature.index)
GD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gd_replacement_d3_022'] = {'inputs': ['gd_replacement_d2_022'], 'func': gd_replacement_d3_022}


def gd_replacement_d3_023(gd_replacement_d2_023):
    feature = _clean(gd_replacement_d2_023)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00011500).reindex(feature.index)
GD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gd_replacement_d3_023'] = {'inputs': ['gd_replacement_d2_023'], 'func': gd_replacement_d3_023}


def gd_replacement_d3_024(gd_replacement_d2_024):
    feature = _clean(gd_replacement_d2_024)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00012000).reindex(feature.index)
GD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gd_replacement_d3_024'] = {'inputs': ['gd_replacement_d2_024'], 'func': gd_replacement_d3_024}


def gd_replacement_d3_025(gd_replacement_d2_025):
    feature = _clean(gd_replacement_d2_025)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00012500).reindex(feature.index)
GD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gd_replacement_d3_025'] = {'inputs': ['gd_replacement_d2_025'], 'func': gd_replacement_d3_025}


def gd_replacement_d3_026(gd_replacement_d2_026):
    feature = _clean(gd_replacement_d2_026)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00013000).reindex(feature.index)
GD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gd_replacement_d3_026'] = {'inputs': ['gd_replacement_d2_026'], 'func': gd_replacement_d3_026}


def gd_replacement_d3_027(gd_replacement_d2_027):
    feature = _clean(gd_replacement_d2_027)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00013500).reindex(feature.index)
GD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gd_replacement_d3_027'] = {'inputs': ['gd_replacement_d2_027'], 'func': gd_replacement_d3_027}


def gd_replacement_d3_028(gd_replacement_d2_028):
    feature = _clean(gd_replacement_d2_028)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00014000).reindex(feature.index)
GD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gd_replacement_d3_028'] = {'inputs': ['gd_replacement_d2_028'], 'func': gd_replacement_d3_028}


def gd_replacement_d3_029(gd_replacement_d2_029):
    feature = _clean(gd_replacement_d2_029)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00014500).reindex(feature.index)
GD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gd_replacement_d3_029'] = {'inputs': ['gd_replacement_d2_029'], 'func': gd_replacement_d3_029}


def gd_replacement_d3_030(gd_replacement_d2_030):
    feature = _clean(gd_replacement_d2_030)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00015000).reindex(feature.index)
GD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gd_replacement_d3_030'] = {'inputs': ['gd_replacement_d2_030'], 'func': gd_replacement_d3_030}


def gd_replacement_d3_031(gd_replacement_d2_031):
    feature = _clean(gd_replacement_d2_031)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00015500).reindex(feature.index)
GD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gd_replacement_d3_031'] = {'inputs': ['gd_replacement_d2_031'], 'func': gd_replacement_d3_031}


def gd_replacement_d3_032(gd_replacement_d2_032):
    feature = _clean(gd_replacement_d2_032)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00016000).reindex(feature.index)
GD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gd_replacement_d3_032'] = {'inputs': ['gd_replacement_d2_032'], 'func': gd_replacement_d3_032}


def gd_replacement_d3_033(gd_replacement_d2_033):
    feature = _clean(gd_replacement_d2_033)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00016500).reindex(feature.index)
GD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gd_replacement_d3_033'] = {'inputs': ['gd_replacement_d2_033'], 'func': gd_replacement_d3_033}


def gd_replacement_d3_034(gd_replacement_d2_034):
    feature = _clean(gd_replacement_d2_034)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00017000).reindex(feature.index)
GD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gd_replacement_d3_034'] = {'inputs': ['gd_replacement_d2_034'], 'func': gd_replacement_d3_034}


def gd_replacement_d3_035(gd_replacement_d2_035):
    feature = _clean(gd_replacement_d2_035)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00017500).reindex(feature.index)
GD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gd_replacement_d3_035'] = {'inputs': ['gd_replacement_d2_035'], 'func': gd_replacement_d3_035}


def gd_replacement_d3_036(gd_replacement_d2_036):
    feature = _clean(gd_replacement_d2_036)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00018000).reindex(feature.index)
GD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gd_replacement_d3_036'] = {'inputs': ['gd_replacement_d2_036'], 'func': gd_replacement_d3_036}


def gd_replacement_d3_037(gd_replacement_d2_037):
    feature = _clean(gd_replacement_d2_037)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00018500).reindex(feature.index)
GD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gd_replacement_d3_037'] = {'inputs': ['gd_replacement_d2_037'], 'func': gd_replacement_d3_037}


def gd_replacement_d3_038(gd_replacement_d2_038):
    feature = _clean(gd_replacement_d2_038)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00019000).reindex(feature.index)
GD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gd_replacement_d3_038'] = {'inputs': ['gd_replacement_d2_038'], 'func': gd_replacement_d3_038}


def gd_replacement_d3_039(gd_replacement_d2_039):
    feature = _clean(gd_replacement_d2_039)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00019500).reindex(feature.index)
GD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gd_replacement_d3_039'] = {'inputs': ['gd_replacement_d2_039'], 'func': gd_replacement_d3_039}


def gd_replacement_d3_040(gd_replacement_d2_040):
    feature = _clean(gd_replacement_d2_040)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00020000).reindex(feature.index)
GD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gd_replacement_d3_040'] = {'inputs': ['gd_replacement_d2_040'], 'func': gd_replacement_d3_040}


def gd_replacement_d3_041(gd_replacement_d2_041):
    feature = _clean(gd_replacement_d2_041)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00020500).reindex(feature.index)
GD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gd_replacement_d3_041'] = {'inputs': ['gd_replacement_d2_041'], 'func': gd_replacement_d3_041}


def gd_replacement_d3_042(gd_replacement_d2_042):
    feature = _clean(gd_replacement_d2_042)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00021000).reindex(feature.index)
GD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gd_replacement_d3_042'] = {'inputs': ['gd_replacement_d2_042'], 'func': gd_replacement_d3_042}


def gd_replacement_d3_043(gd_replacement_d2_043):
    feature = _clean(gd_replacement_d2_043)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00021500).reindex(feature.index)
GD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gd_replacement_d3_043'] = {'inputs': ['gd_replacement_d2_043'], 'func': gd_replacement_d3_043}


def gd_replacement_d3_044(gd_replacement_d2_044):
    feature = _clean(gd_replacement_d2_044)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00022000).reindex(feature.index)
GD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gd_replacement_d3_044'] = {'inputs': ['gd_replacement_d2_044'], 'func': gd_replacement_d3_044}


def gd_replacement_d3_045(gd_replacement_d2_045):
    feature = _clean(gd_replacement_d2_045)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00022500).reindex(feature.index)
GD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gd_replacement_d3_045'] = {'inputs': ['gd_replacement_d2_045'], 'func': gd_replacement_d3_045}


def gd_replacement_d3_046(gd_replacement_d2_046):
    feature = _clean(gd_replacement_d2_046)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00023000).reindex(feature.index)
GD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gd_replacement_d3_046'] = {'inputs': ['gd_replacement_d2_046'], 'func': gd_replacement_d3_046}


def gd_replacement_d3_047(gd_replacement_d2_047):
    feature = _clean(gd_replacement_d2_047)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00023500).reindex(feature.index)
GD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gd_replacement_d3_047'] = {'inputs': ['gd_replacement_d2_047'], 'func': gd_replacement_d3_047}


def gd_replacement_d3_048(gd_replacement_d2_048):
    feature = _clean(gd_replacement_d2_048)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00024000).reindex(feature.index)
GD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gd_replacement_d3_048'] = {'inputs': ['gd_replacement_d2_048'], 'func': gd_replacement_d3_048}


def gd_replacement_d3_049(gd_replacement_d2_049):
    feature = _clean(gd_replacement_d2_049)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00024500).reindex(feature.index)
GD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gd_replacement_d3_049'] = {'inputs': ['gd_replacement_d2_049'], 'func': gd_replacement_d3_049}


def gd_replacement_d3_050(gd_replacement_d2_050):
    feature = _clean(gd_replacement_d2_050)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00025000).reindex(feature.index)
GD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gd_replacement_d3_050'] = {'inputs': ['gd_replacement_d2_050'], 'func': gd_replacement_d3_050}


def gd_replacement_d3_051(gd_replacement_d2_051):
    feature = _clean(gd_replacement_d2_051)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00025500).reindex(feature.index)
GD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gd_replacement_d3_051'] = {'inputs': ['gd_replacement_d2_051'], 'func': gd_replacement_d3_051}


def gd_replacement_d3_052(gd_replacement_d2_052):
    feature = _clean(gd_replacement_d2_052)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00026000).reindex(feature.index)
GD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gd_replacement_d3_052'] = {'inputs': ['gd_replacement_d2_052'], 'func': gd_replacement_d3_052}


def gd_replacement_d3_053(gd_replacement_d2_053):
    feature = _clean(gd_replacement_d2_053)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00026500).reindex(feature.index)
GD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gd_replacement_d3_053'] = {'inputs': ['gd_replacement_d2_053'], 'func': gd_replacement_d3_053}


def gd_replacement_d3_054(gd_replacement_d2_054):
    feature = _clean(gd_replacement_d2_054)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00027000).reindex(feature.index)
GD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gd_replacement_d3_054'] = {'inputs': ['gd_replacement_d2_054'], 'func': gd_replacement_d3_054}


def gd_replacement_d3_055(gd_replacement_d2_055):
    feature = _clean(gd_replacement_d2_055)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00027500).reindex(feature.index)
GD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gd_replacement_d3_055'] = {'inputs': ['gd_replacement_d2_055'], 'func': gd_replacement_d3_055}


def gd_replacement_d3_056(gd_replacement_d2_056):
    feature = _clean(gd_replacement_d2_056)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00028000).reindex(feature.index)
GD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gd_replacement_d3_056'] = {'inputs': ['gd_replacement_d2_056'], 'func': gd_replacement_d3_056}


def gd_replacement_d3_057(gd_replacement_d2_057):
    feature = _clean(gd_replacement_d2_057)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00028500).reindex(feature.index)
GD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gd_replacement_d3_057'] = {'inputs': ['gd_replacement_d2_057'], 'func': gd_replacement_d3_057}


def gd_replacement_d3_058(gd_replacement_d2_058):
    feature = _clean(gd_replacement_d2_058)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00029000).reindex(feature.index)
GD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gd_replacement_d3_058'] = {'inputs': ['gd_replacement_d2_058'], 'func': gd_replacement_d3_058}


def gd_replacement_d3_059(gd_replacement_d2_059):
    feature = _clean(gd_replacement_d2_059)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00029500).reindex(feature.index)
GD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gd_replacement_d3_059'] = {'inputs': ['gd_replacement_d2_059'], 'func': gd_replacement_d3_059}


def gd_replacement_d3_060(gd_replacement_d2_060):
    feature = _clean(gd_replacement_d2_060)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00030000).reindex(feature.index)
GD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gd_replacement_d3_060'] = {'inputs': ['gd_replacement_d2_060'], 'func': gd_replacement_d3_060}


def gd_replacement_d3_061(gd_replacement_d2_061):
    feature = _clean(gd_replacement_d2_061)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00030500).reindex(feature.index)
GD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gd_replacement_d3_061'] = {'inputs': ['gd_replacement_d2_061'], 'func': gd_replacement_d3_061}


def gd_replacement_d3_062(gd_replacement_d2_062):
    feature = _clean(gd_replacement_d2_062)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00031000).reindex(feature.index)
GD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gd_replacement_d3_062'] = {'inputs': ['gd_replacement_d2_062'], 'func': gd_replacement_d3_062}


def gd_replacement_d3_063(gd_replacement_d2_063):
    feature = _clean(gd_replacement_d2_063)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00031500).reindex(feature.index)
GD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gd_replacement_d3_063'] = {'inputs': ['gd_replacement_d2_063'], 'func': gd_replacement_d3_063}


def gd_replacement_d3_064(gd_replacement_d2_064):
    feature = _clean(gd_replacement_d2_064)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00032000).reindex(feature.index)
GD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gd_replacement_d3_064'] = {'inputs': ['gd_replacement_d2_064'], 'func': gd_replacement_d3_064}


def gd_replacement_d3_065(gd_replacement_d2_065):
    feature = _clean(gd_replacement_d2_065)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00032500).reindex(feature.index)
GD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gd_replacement_d3_065'] = {'inputs': ['gd_replacement_d2_065'], 'func': gd_replacement_d3_065}


def gd_replacement_d3_066(gd_replacement_d2_066):
    feature = _clean(gd_replacement_d2_066)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00033000).reindex(feature.index)
GD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gd_replacement_d3_066'] = {'inputs': ['gd_replacement_d2_066'], 'func': gd_replacement_d3_066}


def gd_replacement_d3_067(gd_replacement_d2_067):
    feature = _clean(gd_replacement_d2_067)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00033500).reindex(feature.index)
GD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gd_replacement_d3_067'] = {'inputs': ['gd_replacement_d2_067'], 'func': gd_replacement_d3_067}


def gd_replacement_d3_068(gd_replacement_d2_068):
    feature = _clean(gd_replacement_d2_068)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00034000).reindex(feature.index)
GD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gd_replacement_d3_068'] = {'inputs': ['gd_replacement_d2_068'], 'func': gd_replacement_d3_068}


def gd_replacement_d3_069(gd_replacement_d2_069):
    feature = _clean(gd_replacement_d2_069)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00034500).reindex(feature.index)
GD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gd_replacement_d3_069'] = {'inputs': ['gd_replacement_d2_069'], 'func': gd_replacement_d3_069}


def gd_replacement_d3_070(gd_replacement_d2_070):
    feature = _clean(gd_replacement_d2_070)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00035000).reindex(feature.index)
GD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gd_replacement_d3_070'] = {'inputs': ['gd_replacement_d2_070'], 'func': gd_replacement_d3_070}


def gd_replacement_d3_071(gd_replacement_d2_071):
    feature = _clean(gd_replacement_d2_071)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00035500).reindex(feature.index)
GD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gd_replacement_d3_071'] = {'inputs': ['gd_replacement_d2_071'], 'func': gd_replacement_d3_071}


def gd_replacement_d3_072(gd_replacement_d2_072):
    feature = _clean(gd_replacement_d2_072)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00036000).reindex(feature.index)
GD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gd_replacement_d3_072'] = {'inputs': ['gd_replacement_d2_072'], 'func': gd_replacement_d3_072}


def gd_replacement_d3_073(gd_replacement_d2_073):
    feature = _clean(gd_replacement_d2_073)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00036500).reindex(feature.index)
GD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gd_replacement_d3_073'] = {'inputs': ['gd_replacement_d2_073'], 'func': gd_replacement_d3_073}


def gd_replacement_d3_074(gd_replacement_d2_074):
    feature = _clean(gd_replacement_d2_074)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00037000).reindex(feature.index)
GD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gd_replacement_d3_074'] = {'inputs': ['gd_replacement_d2_074'], 'func': gd_replacement_d3_074}


def gd_replacement_d3_075(gd_replacement_d2_075):
    feature = _clean(gd_replacement_d2_075)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00037500).reindex(feature.index)
GD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gd_replacement_d3_075'] = {'inputs': ['gd_replacement_d2_075'], 'func': gd_replacement_d3_075}


def gd_replacement_d3_076(gd_replacement_d2_076):
    feature = _clean(gd_replacement_d2_076)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00038000).reindex(feature.index)
GD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gd_replacement_d3_076'] = {'inputs': ['gd_replacement_d2_076'], 'func': gd_replacement_d3_076}


def gd_replacement_d3_077(gd_replacement_d2_077):
    feature = _clean(gd_replacement_d2_077)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00038500).reindex(feature.index)
GD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gd_replacement_d3_077'] = {'inputs': ['gd_replacement_d2_077'], 'func': gd_replacement_d3_077}


def gd_replacement_d3_078(gd_replacement_d2_078):
    feature = _clean(gd_replacement_d2_078)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00039000).reindex(feature.index)
GD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gd_replacement_d3_078'] = {'inputs': ['gd_replacement_d2_078'], 'func': gd_replacement_d3_078}


def gd_replacement_d3_079(gd_replacement_d2_079):
    feature = _clean(gd_replacement_d2_079)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00039500).reindex(feature.index)
GD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gd_replacement_d3_079'] = {'inputs': ['gd_replacement_d2_079'], 'func': gd_replacement_d3_079}


def gd_replacement_d3_080(gd_replacement_d2_080):
    feature = _clean(gd_replacement_d2_080)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00040000).reindex(feature.index)
GD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gd_replacement_d3_080'] = {'inputs': ['gd_replacement_d2_080'], 'func': gd_replacement_d3_080}


def gd_replacement_d3_081(gd_replacement_d2_081):
    feature = _clean(gd_replacement_d2_081)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00040500).reindex(feature.index)
GD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gd_replacement_d3_081'] = {'inputs': ['gd_replacement_d2_081'], 'func': gd_replacement_d3_081}


def gd_replacement_d3_082(gd_replacement_d2_082):
    feature = _clean(gd_replacement_d2_082)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00041000).reindex(feature.index)
GD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gd_replacement_d3_082'] = {'inputs': ['gd_replacement_d2_082'], 'func': gd_replacement_d3_082}


def gd_replacement_d3_083(gd_replacement_d2_083):
    feature = _clean(gd_replacement_d2_083)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00041500).reindex(feature.index)
GD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gd_replacement_d3_083'] = {'inputs': ['gd_replacement_d2_083'], 'func': gd_replacement_d3_083}


def gd_replacement_d3_084(gd_replacement_d2_084):
    feature = _clean(gd_replacement_d2_084)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00042000).reindex(feature.index)
GD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gd_replacement_d3_084'] = {'inputs': ['gd_replacement_d2_084'], 'func': gd_replacement_d3_084}


def gd_replacement_d3_085(gd_replacement_d2_085):
    feature = _clean(gd_replacement_d2_085)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00042500).reindex(feature.index)
GD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gd_replacement_d3_085'] = {'inputs': ['gd_replacement_d2_085'], 'func': gd_replacement_d3_085}


def gd_replacement_d3_086(gd_replacement_d2_086):
    feature = _clean(gd_replacement_d2_086)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00043000).reindex(feature.index)
GD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gd_replacement_d3_086'] = {'inputs': ['gd_replacement_d2_086'], 'func': gd_replacement_d3_086}


def gd_replacement_d3_087(gd_replacement_d2_087):
    feature = _clean(gd_replacement_d2_087)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00043500).reindex(feature.index)
GD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gd_replacement_d3_087'] = {'inputs': ['gd_replacement_d2_087'], 'func': gd_replacement_d3_087}


def gd_replacement_d3_088(gd_replacement_d2_088):
    feature = _clean(gd_replacement_d2_088)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00044000).reindex(feature.index)
GD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gd_replacement_d3_088'] = {'inputs': ['gd_replacement_d2_088'], 'func': gd_replacement_d3_088}


def gd_replacement_d3_089(gd_replacement_d2_089):
    feature = _clean(gd_replacement_d2_089)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00044500).reindex(feature.index)
GD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gd_replacement_d3_089'] = {'inputs': ['gd_replacement_d2_089'], 'func': gd_replacement_d3_089}


def gd_replacement_d3_090(gd_replacement_d2_090):
    feature = _clean(gd_replacement_d2_090)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00045000).reindex(feature.index)
GD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gd_replacement_d3_090'] = {'inputs': ['gd_replacement_d2_090'], 'func': gd_replacement_d3_090}


def gd_replacement_d3_091(gd_replacement_d2_091):
    feature = _clean(gd_replacement_d2_091)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00045500).reindex(feature.index)
GD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gd_replacement_d3_091'] = {'inputs': ['gd_replacement_d2_091'], 'func': gd_replacement_d3_091}


def gd_replacement_d3_092(gd_replacement_d2_092):
    feature = _clean(gd_replacement_d2_092)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00046000).reindex(feature.index)
GD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gd_replacement_d3_092'] = {'inputs': ['gd_replacement_d2_092'], 'func': gd_replacement_d3_092}


def gd_replacement_d3_093(gd_replacement_d2_093):
    feature = _clean(gd_replacement_d2_093)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00046500).reindex(feature.index)
GD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gd_replacement_d3_093'] = {'inputs': ['gd_replacement_d2_093'], 'func': gd_replacement_d3_093}


def gd_replacement_d3_094(gd_replacement_d2_094):
    feature = _clean(gd_replacement_d2_094)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00047000).reindex(feature.index)
GD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gd_replacement_d3_094'] = {'inputs': ['gd_replacement_d2_094'], 'func': gd_replacement_d3_094}


def gd_replacement_d3_095(gd_replacement_d2_095):
    feature = _clean(gd_replacement_d2_095)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00047500).reindex(feature.index)
GD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gd_replacement_d3_095'] = {'inputs': ['gd_replacement_d2_095'], 'func': gd_replacement_d3_095}


def gd_replacement_d3_096(gd_replacement_d2_096):
    feature = _clean(gd_replacement_d2_096)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00048000).reindex(feature.index)
GD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gd_replacement_d3_096'] = {'inputs': ['gd_replacement_d2_096'], 'func': gd_replacement_d3_096}


def gd_replacement_d3_097(gd_replacement_d2_097):
    feature = _clean(gd_replacement_d2_097)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00048500).reindex(feature.index)
GD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gd_replacement_d3_097'] = {'inputs': ['gd_replacement_d2_097'], 'func': gd_replacement_d3_097}


def gd_replacement_d3_098(gd_replacement_d2_098):
    feature = _clean(gd_replacement_d2_098)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00049000).reindex(feature.index)
GD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gd_replacement_d3_098'] = {'inputs': ['gd_replacement_d2_098'], 'func': gd_replacement_d3_098}


def gd_replacement_d3_099(gd_replacement_d2_099):
    feature = _clean(gd_replacement_d2_099)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00049500).reindex(feature.index)
GD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gd_replacement_d3_099'] = {'inputs': ['gd_replacement_d2_099'], 'func': gd_replacement_d3_099}


def gd_replacement_d3_100(gd_replacement_d2_100):
    feature = _clean(gd_replacement_d2_100)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00050000).reindex(feature.index)
GD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gd_replacement_d3_100'] = {'inputs': ['gd_replacement_d2_100'], 'func': gd_replacement_d3_100}


def gd_replacement_d3_101(gd_replacement_d2_101):
    feature = _clean(gd_replacement_d2_101)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00050500).reindex(feature.index)
GD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gd_replacement_d3_101'] = {'inputs': ['gd_replacement_d2_101'], 'func': gd_replacement_d3_101}


def gd_replacement_d3_102(gd_replacement_d2_102):
    feature = _clean(gd_replacement_d2_102)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00051000).reindex(feature.index)
GD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gd_replacement_d3_102'] = {'inputs': ['gd_replacement_d2_102'], 'func': gd_replacement_d3_102}


def gd_replacement_d3_103(gd_replacement_d2_103):
    feature = _clean(gd_replacement_d2_103)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00051500).reindex(feature.index)
GD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gd_replacement_d3_103'] = {'inputs': ['gd_replacement_d2_103'], 'func': gd_replacement_d3_103}


def gd_replacement_d3_104(gd_replacement_d2_104):
    feature = _clean(gd_replacement_d2_104)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00052000).reindex(feature.index)
GD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gd_replacement_d3_104'] = {'inputs': ['gd_replacement_d2_104'], 'func': gd_replacement_d3_104}


def gd_replacement_d3_105(gd_replacement_d2_105):
    feature = _clean(gd_replacement_d2_105)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00052500).reindex(feature.index)
GD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gd_replacement_d3_105'] = {'inputs': ['gd_replacement_d2_105'], 'func': gd_replacement_d3_105}


def gd_replacement_d3_106(gd_replacement_d2_106):
    feature = _clean(gd_replacement_d2_106)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00053000).reindex(feature.index)
GD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gd_replacement_d3_106'] = {'inputs': ['gd_replacement_d2_106'], 'func': gd_replacement_d3_106}


def gd_replacement_d3_107(gd_replacement_d2_107):
    feature = _clean(gd_replacement_d2_107)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00053500).reindex(feature.index)
GD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gd_replacement_d3_107'] = {'inputs': ['gd_replacement_d2_107'], 'func': gd_replacement_d3_107}


def gd_replacement_d3_108(gd_replacement_d2_108):
    feature = _clean(gd_replacement_d2_108)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00054000).reindex(feature.index)
GD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gd_replacement_d3_108'] = {'inputs': ['gd_replacement_d2_108'], 'func': gd_replacement_d3_108}


def gd_replacement_d3_109(gd_replacement_d2_109):
    feature = _clean(gd_replacement_d2_109)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00054500).reindex(feature.index)
GD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gd_replacement_d3_109'] = {'inputs': ['gd_replacement_d2_109'], 'func': gd_replacement_d3_109}


def gd_replacement_d3_110(gd_replacement_d2_110):
    feature = _clean(gd_replacement_d2_110)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00055000).reindex(feature.index)
GD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gd_replacement_d3_110'] = {'inputs': ['gd_replacement_d2_110'], 'func': gd_replacement_d3_110}


def gd_replacement_d3_111(gd_replacement_d2_111):
    feature = _clean(gd_replacement_d2_111)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00055500).reindex(feature.index)
GD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gd_replacement_d3_111'] = {'inputs': ['gd_replacement_d2_111'], 'func': gd_replacement_d3_111}


def gd_replacement_d3_112(gd_replacement_d2_112):
    feature = _clean(gd_replacement_d2_112)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00056000).reindex(feature.index)
GD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gd_replacement_d3_112'] = {'inputs': ['gd_replacement_d2_112'], 'func': gd_replacement_d3_112}


def gd_replacement_d3_113(gd_replacement_d2_113):
    feature = _clean(gd_replacement_d2_113)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00056500).reindex(feature.index)
GD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gd_replacement_d3_113'] = {'inputs': ['gd_replacement_d2_113'], 'func': gd_replacement_d3_113}


def gd_replacement_d3_114(gd_replacement_d2_114):
    feature = _clean(gd_replacement_d2_114)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00057000).reindex(feature.index)
GD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gd_replacement_d3_114'] = {'inputs': ['gd_replacement_d2_114'], 'func': gd_replacement_d3_114}


def gd_replacement_d3_115(gd_replacement_d2_115):
    feature = _clean(gd_replacement_d2_115)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00057500).reindex(feature.index)
GD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gd_replacement_d3_115'] = {'inputs': ['gd_replacement_d2_115'], 'func': gd_replacement_d3_115}


def gd_replacement_d3_116(gd_replacement_d2_116):
    feature = _clean(gd_replacement_d2_116)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00058000).reindex(feature.index)
GD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gd_replacement_d3_116'] = {'inputs': ['gd_replacement_d2_116'], 'func': gd_replacement_d3_116}


def gd_replacement_d3_117(gd_replacement_d2_117):
    feature = _clean(gd_replacement_d2_117)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00058500).reindex(feature.index)
GD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gd_replacement_d3_117'] = {'inputs': ['gd_replacement_d2_117'], 'func': gd_replacement_d3_117}


def gd_replacement_d3_118(gd_replacement_d2_118):
    feature = _clean(gd_replacement_d2_118)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00059000).reindex(feature.index)
GD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gd_replacement_d3_118'] = {'inputs': ['gd_replacement_d2_118'], 'func': gd_replacement_d3_118}


def gd_replacement_d3_119(gd_replacement_d2_119):
    feature = _clean(gd_replacement_d2_119)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00059500).reindex(feature.index)
GD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gd_replacement_d3_119'] = {'inputs': ['gd_replacement_d2_119'], 'func': gd_replacement_d3_119}


def gd_replacement_d3_120(gd_replacement_d2_120):
    feature = _clean(gd_replacement_d2_120)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00060000).reindex(feature.index)
GD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gd_replacement_d3_120'] = {'inputs': ['gd_replacement_d2_120'], 'func': gd_replacement_d3_120}


def gd_replacement_d3_121(gd_replacement_d2_121):
    feature = _clean(gd_replacement_d2_121)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00060500).reindex(feature.index)
GD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gd_replacement_d3_121'] = {'inputs': ['gd_replacement_d2_121'], 'func': gd_replacement_d3_121}


def gd_replacement_d3_122(gd_replacement_d2_122):
    feature = _clean(gd_replacement_d2_122)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00061000).reindex(feature.index)
GD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gd_replacement_d3_122'] = {'inputs': ['gd_replacement_d2_122'], 'func': gd_replacement_d3_122}


def gd_replacement_d3_123(gd_replacement_d2_123):
    feature = _clean(gd_replacement_d2_123)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00061500).reindex(feature.index)
GD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gd_replacement_d3_123'] = {'inputs': ['gd_replacement_d2_123'], 'func': gd_replacement_d3_123}


def gd_replacement_d3_124(gd_replacement_d2_124):
    feature = _clean(gd_replacement_d2_124)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00062000).reindex(feature.index)
GD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gd_replacement_d3_124'] = {'inputs': ['gd_replacement_d2_124'], 'func': gd_replacement_d3_124}


def gd_replacement_d3_125(gd_replacement_d2_125):
    feature = _clean(gd_replacement_d2_125)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00062500).reindex(feature.index)
GD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gd_replacement_d3_125'] = {'inputs': ['gd_replacement_d2_125'], 'func': gd_replacement_d3_125}


def gd_replacement_d3_126(gd_replacement_d2_126):
    feature = _clean(gd_replacement_d2_126)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00063000).reindex(feature.index)
GD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gd_replacement_d3_126'] = {'inputs': ['gd_replacement_d2_126'], 'func': gd_replacement_d3_126}


def gd_replacement_d3_127(gd_replacement_d2_127):
    feature = _clean(gd_replacement_d2_127)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00063500).reindex(feature.index)
GD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gd_replacement_d3_127'] = {'inputs': ['gd_replacement_d2_127'], 'func': gd_replacement_d3_127}


def gd_replacement_d3_128(gd_replacement_d2_128):
    feature = _clean(gd_replacement_d2_128)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00064000).reindex(feature.index)
GD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gd_replacement_d3_128'] = {'inputs': ['gd_replacement_d2_128'], 'func': gd_replacement_d3_128}


def gd_replacement_d3_129(gd_replacement_d2_129):
    feature = _clean(gd_replacement_d2_129)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00064500).reindex(feature.index)
GD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gd_replacement_d3_129'] = {'inputs': ['gd_replacement_d2_129'], 'func': gd_replacement_d3_129}


def gd_replacement_d3_130(gd_replacement_d2_130):
    feature = _clean(gd_replacement_d2_130)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00065000).reindex(feature.index)
GD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gd_replacement_d3_130'] = {'inputs': ['gd_replacement_d2_130'], 'func': gd_replacement_d3_130}


def gd_replacement_d3_131(gd_replacement_d2_131):
    feature = _clean(gd_replacement_d2_131)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00065500).reindex(feature.index)
GD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gd_replacement_d3_131'] = {'inputs': ['gd_replacement_d2_131'], 'func': gd_replacement_d3_131}


def gd_replacement_d3_132(gd_replacement_d2_132):
    feature = _clean(gd_replacement_d2_132)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00066000).reindex(feature.index)
GD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gd_replacement_d3_132'] = {'inputs': ['gd_replacement_d2_132'], 'func': gd_replacement_d3_132}


def gd_replacement_d3_133(gd_replacement_d2_133):
    feature = _clean(gd_replacement_d2_133)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00066500).reindex(feature.index)
GD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gd_replacement_d3_133'] = {'inputs': ['gd_replacement_d2_133'], 'func': gd_replacement_d3_133}


def gd_replacement_d3_134(gd_replacement_d2_134):
    feature = _clean(gd_replacement_d2_134)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00067000).reindex(feature.index)
GD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gd_replacement_d3_134'] = {'inputs': ['gd_replacement_d2_134'], 'func': gd_replacement_d3_134}


def gd_replacement_d3_135(gd_replacement_d2_135):
    feature = _clean(gd_replacement_d2_135)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00067500).reindex(feature.index)
GD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gd_replacement_d3_135'] = {'inputs': ['gd_replacement_d2_135'], 'func': gd_replacement_d3_135}


def gd_replacement_d3_136(gd_replacement_d2_136):
    feature = _clean(gd_replacement_d2_136)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00068000).reindex(feature.index)
GD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gd_replacement_d3_136'] = {'inputs': ['gd_replacement_d2_136'], 'func': gd_replacement_d3_136}


def gd_replacement_d3_137(gd_replacement_d2_137):
    feature = _clean(gd_replacement_d2_137)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00068500).reindex(feature.index)
GD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gd_replacement_d3_137'] = {'inputs': ['gd_replacement_d2_137'], 'func': gd_replacement_d3_137}


def gd_replacement_d3_138(gd_replacement_d2_138):
    feature = _clean(gd_replacement_d2_138)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00069000).reindex(feature.index)
GD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gd_replacement_d3_138'] = {'inputs': ['gd_replacement_d2_138'], 'func': gd_replacement_d3_138}


def gd_replacement_d3_139(gd_replacement_d2_139):
    feature = _clean(gd_replacement_d2_139)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00069500).reindex(feature.index)
GD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gd_replacement_d3_139'] = {'inputs': ['gd_replacement_d2_139'], 'func': gd_replacement_d3_139}


def gd_replacement_d3_140(gd_replacement_d2_140):
    feature = _clean(gd_replacement_d2_140)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00070000).reindex(feature.index)
GD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gd_replacement_d3_140'] = {'inputs': ['gd_replacement_d2_140'], 'func': gd_replacement_d3_140}


def gd_replacement_d3_141(gd_replacement_d2_141):
    feature = _clean(gd_replacement_d2_141)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00070500).reindex(feature.index)
GD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gd_replacement_d3_141'] = {'inputs': ['gd_replacement_d2_141'], 'func': gd_replacement_d3_141}


def gd_replacement_d3_142(gd_replacement_d2_142):
    feature = _clean(gd_replacement_d2_142)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00071000).reindex(feature.index)
GD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gd_replacement_d3_142'] = {'inputs': ['gd_replacement_d2_142'], 'func': gd_replacement_d3_142}


def gd_replacement_d3_143(gd_replacement_d2_143):
    feature = _clean(gd_replacement_d2_143)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00071500).reindex(feature.index)
GD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gd_replacement_d3_143'] = {'inputs': ['gd_replacement_d2_143'], 'func': gd_replacement_d3_143}


def gd_replacement_d3_144(gd_replacement_d2_144):
    feature = _clean(gd_replacement_d2_144)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00072000).reindex(feature.index)
GD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gd_replacement_d3_144'] = {'inputs': ['gd_replacement_d2_144'], 'func': gd_replacement_d3_144}


def gd_replacement_d3_145(gd_replacement_d2_145):
    feature = _clean(gd_replacement_d2_145)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00072500).reindex(feature.index)
GD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gd_replacement_d3_145'] = {'inputs': ['gd_replacement_d2_145'], 'func': gd_replacement_d3_145}


def gd_replacement_d3_146(gd_replacement_d2_146):
    feature = _clean(gd_replacement_d2_146)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00073000).reindex(feature.index)
GD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gd_replacement_d3_146'] = {'inputs': ['gd_replacement_d2_146'], 'func': gd_replacement_d3_146}


def gd_replacement_d3_147(gd_replacement_d2_147):
    feature = _clean(gd_replacement_d2_147)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00073500).reindex(feature.index)
GD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gd_replacement_d3_147'] = {'inputs': ['gd_replacement_d2_147'], 'func': gd_replacement_d3_147}


def gd_replacement_d3_148(gd_replacement_d2_148):
    feature = _clean(gd_replacement_d2_148)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00074000).reindex(feature.index)
GD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gd_replacement_d3_148'] = {'inputs': ['gd_replacement_d2_148'], 'func': gd_replacement_d3_148}


def gd_replacement_d3_149(gd_replacement_d2_149):
    feature = _clean(gd_replacement_d2_149)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00074500).reindex(feature.index)
GD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gd_replacement_d3_149'] = {'inputs': ['gd_replacement_d2_149'], 'func': gd_replacement_d3_149}


def gd_replacement_d3_150(gd_replacement_d2_150):
    feature = _clean(gd_replacement_d2_150)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00075000).reindex(feature.index)
GD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gd_replacement_d3_150'] = {'inputs': ['gd_replacement_d2_150'], 'func': gd_replacement_d3_150}


def gd_replacement_d3_151(gd_replacement_d2_151):
    feature = _clean(gd_replacement_d2_151)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00075500).reindex(feature.index)
GD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gd_replacement_d3_151'] = {'inputs': ['gd_replacement_d2_151'], 'func': gd_replacement_d3_151}


def gd_replacement_d3_152(gd_replacement_d2_152):
    feature = _clean(gd_replacement_d2_152)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00076000).reindex(feature.index)
GD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gd_replacement_d3_152'] = {'inputs': ['gd_replacement_d2_152'], 'func': gd_replacement_d3_152}


def gd_replacement_d3_153(gd_replacement_d2_153):
    feature = _clean(gd_replacement_d2_153)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00076500).reindex(feature.index)
GD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gd_replacement_d3_153'] = {'inputs': ['gd_replacement_d2_153'], 'func': gd_replacement_d3_153}


def gd_replacement_d3_154(gd_replacement_d2_154):
    feature = _clean(gd_replacement_d2_154)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00077000).reindex(feature.index)
GD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gd_replacement_d3_154'] = {'inputs': ['gd_replacement_d2_154'], 'func': gd_replacement_d3_154}


def gd_replacement_d3_155(gd_replacement_d2_155):
    feature = _clean(gd_replacement_d2_155)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00077500).reindex(feature.index)
GD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gd_replacement_d3_155'] = {'inputs': ['gd_replacement_d2_155'], 'func': gd_replacement_d3_155}


def gd_replacement_d3_156(gd_replacement_d2_156):
    feature = _clean(gd_replacement_d2_156)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00078000).reindex(feature.index)
GD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gd_replacement_d3_156'] = {'inputs': ['gd_replacement_d2_156'], 'func': gd_replacement_d3_156}


def gd_replacement_d3_157(gd_replacement_d2_157):
    feature = _clean(gd_replacement_d2_157)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00078500).reindex(feature.index)
GD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gd_replacement_d3_157'] = {'inputs': ['gd_replacement_d2_157'], 'func': gd_replacement_d3_157}


def gd_replacement_d3_158(gd_replacement_d2_158):
    feature = _clean(gd_replacement_d2_158)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00079000).reindex(feature.index)
GD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gd_replacement_d3_158'] = {'inputs': ['gd_replacement_d2_158'], 'func': gd_replacement_d3_158}


def gd_replacement_d3_159(gd_replacement_d2_159):
    feature = _clean(gd_replacement_d2_159)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00079500).reindex(feature.index)
GD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gd_replacement_d3_159'] = {'inputs': ['gd_replacement_d2_159'], 'func': gd_replacement_d3_159}


def gd_replacement_d3_160(gd_replacement_d2_160):
    feature = _clean(gd_replacement_d2_160)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00080000).reindex(feature.index)
GD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gd_replacement_d3_160'] = {'inputs': ['gd_replacement_d2_160'], 'func': gd_replacement_d3_160}


def gd_replacement_d3_161(gd_replacement_d2_161):
    feature = _clean(gd_replacement_d2_161)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00080500).reindex(feature.index)
GD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gd_replacement_d3_161'] = {'inputs': ['gd_replacement_d2_161'], 'func': gd_replacement_d3_161}


def gd_replacement_d3_162(gd_replacement_d2_162):
    feature = _clean(gd_replacement_d2_162)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00081000).reindex(feature.index)
GD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gd_replacement_d3_162'] = {'inputs': ['gd_replacement_d2_162'], 'func': gd_replacement_d3_162}


def gd_replacement_d3_163(gd_replacement_d2_163):
    feature = _clean(gd_replacement_d2_163)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00081500).reindex(feature.index)
GD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gd_replacement_d3_163'] = {'inputs': ['gd_replacement_d2_163'], 'func': gd_replacement_d3_163}


def gd_replacement_d3_164(gd_replacement_d2_164):
    feature = _clean(gd_replacement_d2_164)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00082000).reindex(feature.index)
GD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gd_replacement_d3_164'] = {'inputs': ['gd_replacement_d2_164'], 'func': gd_replacement_d3_164}


def gd_replacement_d3_165(gd_replacement_d2_165):
    feature = _clean(gd_replacement_d2_165)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00082500).reindex(feature.index)
GD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gd_replacement_d3_165'] = {'inputs': ['gd_replacement_d2_165'], 'func': gd_replacement_d3_165}


def gd_replacement_d3_166(gd_replacement_d2_166):
    feature = _clean(gd_replacement_d2_166)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00083000).reindex(feature.index)
GD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['gd_replacement_d3_166'] = {'inputs': ['gd_replacement_d2_166'], 'func': gd_replacement_d3_166}


# Third-derivative extensions for repaired first-base features.
GDS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY = {}


def _base_universe_d3(feature, idx):
    feature = _clean(feature) if '_clean' in globals() else _s(feature).replace([np.inf, -np.inf], np.nan)
    windows = [1, 2, 3, 5, 8, 13, 21, 34, 55]
    lag = windows[(idx * 2) % len(windows)]
    smooth = windows[(idx * 5 + 2) % len(windows)]
    accel = feature.diff(lag)
    curve = feature - feature.rolling(max(3, smooth), min_periods=2).mean()
    out = accel + curve.fillna(0.0) * (0.00019 * ((idx % 19) + 1))
    return out.replace([np.inf, -np.inf], np.nan).reindex(feature.index)


def gds_base_universe_d3_001_gds_003_fcf_burn_to_cash_63(gds_base_universe_d2_001_gds_003_fcf_burn_to_cash_63):
    return _base_universe_d3(gds_base_universe_d2_001_gds_003_fcf_burn_to_cash_63, 1)
GDS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['gds_base_universe_d3_001_gds_003_fcf_burn_to_cash_63'] = {'inputs': ['gds_base_universe_d2_001_gds_003_fcf_burn_to_cash_63'], 'func': gds_base_universe_d3_001_gds_003_fcf_burn_to_cash_63}


def gds_base_universe_d3_002_gds_004_debt_to_equity_84(gds_base_universe_d2_002_gds_004_debt_to_equity_84):
    return _base_universe_d3(gds_base_universe_d2_002_gds_004_debt_to_equity_84, 2)
GDS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['gds_base_universe_d3_002_gds_004_debt_to_equity_84'] = {'inputs': ['gds_base_universe_d2_002_gds_004_debt_to_equity_84'], 'func': gds_base_universe_d3_002_gds_004_debt_to_equity_84}


def gds_base_universe_d3_003_gds_005_debt_to_assets_126(gds_base_universe_d2_003_gds_005_debt_to_assets_126):
    return _base_universe_d3(gds_base_universe_d2_003_gds_005_debt_to_assets_126, 3)
GDS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['gds_base_universe_d3_003_gds_005_debt_to_assets_126'] = {'inputs': ['gds_base_universe_d2_003_gds_005_debt_to_assets_126'], 'func': gds_base_universe_d3_003_gds_005_debt_to_assets_126}


def gds_base_universe_d3_004_gds_012_accrual_gap_1260(gds_base_universe_d2_004_gds_012_accrual_gap_1260):
    return _base_universe_d3(gds_base_universe_d2_004_gds_012_accrual_gap_1260, 4)
GDS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['gds_base_universe_d3_004_gds_012_accrual_gap_1260'] = {'inputs': ['gds_base_universe_d2_004_gds_012_accrual_gap_1260'], 'func': gds_base_universe_d3_004_gds_012_accrual_gap_1260}


def gds_base_universe_d3_005_gds_016_debt_to_equity_21(gds_base_universe_d2_005_gds_016_debt_to_equity_21):
    return _base_universe_d3(gds_base_universe_d2_005_gds_016_debt_to_equity_21, 5)
GDS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['gds_base_universe_d3_005_gds_016_debt_to_equity_21'] = {'inputs': ['gds_base_universe_d2_005_gds_016_debt_to_equity_21'], 'func': gds_base_universe_d3_005_gds_016_debt_to_equity_21}


def gds_base_universe_d3_006_gds_017_debt_to_assets_42(gds_base_universe_d2_006_gds_017_debt_to_assets_42):
    return _base_universe_d3(gds_base_universe_d2_006_gds_017_debt_to_assets_42, 6)
GDS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['gds_base_universe_d3_006_gds_017_debt_to_assets_42'] = {'inputs': ['gds_base_universe_d2_006_gds_017_debt_to_assets_42'], 'func': gds_base_universe_d3_006_gds_017_debt_to_assets_42}


def gds_base_universe_d3_007_gds_024_accrual_gap_504(gds_base_universe_d2_007_gds_024_accrual_gap_504):
    return _base_universe_d3(gds_base_universe_d2_007_gds_024_accrual_gap_504, 7)
GDS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['gds_base_universe_d3_007_gds_024_accrual_gap_504'] = {'inputs': ['gds_base_universe_d2_007_gds_024_accrual_gap_504'], 'func': gds_base_universe_d3_007_gds_024_accrual_gap_504}


def gds_base_universe_d3_008_gds_027_fcf_burn_to_cash_1260(gds_base_universe_d2_008_gds_027_fcf_burn_to_cash_1260):
    return _base_universe_d3(gds_base_universe_d2_008_gds_027_fcf_burn_to_cash_1260, 8)
GDS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['gds_base_universe_d3_008_gds_027_fcf_burn_to_cash_1260'] = {'inputs': ['gds_base_universe_d2_008_gds_027_fcf_burn_to_cash_1260'], 'func': gds_base_universe_d3_008_gds_027_fcf_burn_to_cash_1260}


def gds_base_universe_d3_009_gds_028_debt_to_equity_1512(gds_base_universe_d2_009_gds_028_debt_to_equity_1512):
    return _base_universe_d3(gds_base_universe_d2_009_gds_028_debt_to_equity_1512, 9)
GDS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['gds_base_universe_d3_009_gds_028_debt_to_equity_1512'] = {'inputs': ['gds_base_universe_d2_009_gds_028_debt_to_equity_1512'], 'func': gds_base_universe_d3_009_gds_028_debt_to_equity_1512}


def gds_base_universe_d3_010_gds_029_debt_to_assets_63(gds_base_universe_d2_010_gds_029_debt_to_assets_63):
    return _base_universe_d3(gds_base_universe_d2_010_gds_029_debt_to_assets_63, 10)
GDS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['gds_base_universe_d3_010_gds_029_debt_to_assets_63'] = {'inputs': ['gds_base_universe_d2_010_gds_029_debt_to_assets_63'], 'func': gds_base_universe_d3_010_gds_029_debt_to_assets_63}


def gds_base_universe_d3_011_gds_031_interest_coverage_stress_21(gds_base_universe_d2_011_gds_031_interest_coverage_stress_21):
    return _base_universe_d3(gds_base_universe_d2_011_gds_031_interest_coverage_stress_21, 11)
GDS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['gds_base_universe_d3_011_gds_031_interest_coverage_stress_21'] = {'inputs': ['gds_base_universe_d2_011_gds_031_interest_coverage_stress_21'], 'func': gds_base_universe_d3_011_gds_031_interest_coverage_stress_21}


def gds_base_universe_d3_012_gds_036_accrual_gap_189(gds_base_universe_d2_012_gds_036_accrual_gap_189):
    return _base_universe_d3(gds_base_universe_d2_012_gds_036_accrual_gap_189, 12)
GDS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['gds_base_universe_d3_012_gds_036_accrual_gap_189'] = {'inputs': ['gds_base_universe_d2_012_gds_036_accrual_gap_189'], 'func': gds_base_universe_d3_012_gds_036_accrual_gap_189}


def gds_base_universe_d3_013_gds_039_fcf_burn_to_cash_504(gds_base_universe_d2_013_gds_039_fcf_burn_to_cash_504):
    return _base_universe_d3(gds_base_universe_d2_013_gds_039_fcf_burn_to_cash_504, 13)
GDS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['gds_base_universe_d3_013_gds_039_fcf_burn_to_cash_504'] = {'inputs': ['gds_base_universe_d2_013_gds_039_fcf_burn_to_cash_504'], 'func': gds_base_universe_d3_013_gds_039_fcf_burn_to_cash_504}


def gds_base_universe_d3_014_gds_040_debt_to_equity_756(gds_base_universe_d2_014_gds_040_debt_to_equity_756):
    return _base_universe_d3(gds_base_universe_d2_014_gds_040_debt_to_equity_756, 14)
GDS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['gds_base_universe_d3_014_gds_040_debt_to_equity_756'] = {'inputs': ['gds_base_universe_d2_014_gds_040_debt_to_equity_756'], 'func': gds_base_universe_d3_014_gds_040_debt_to_equity_756}


def gds_base_universe_d3_015_gds_041_debt_to_assets_1008(gds_base_universe_d2_015_gds_041_debt_to_assets_1008):
    return _base_universe_d3(gds_base_universe_d2_015_gds_041_debt_to_assets_1008, 15)
GDS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['gds_base_universe_d3_015_gds_041_debt_to_assets_1008'] = {'inputs': ['gds_base_universe_d2_015_gds_041_debt_to_assets_1008'], 'func': gds_base_universe_d3_015_gds_041_debt_to_assets_1008}


def gds_base_universe_d3_016_gds_043_interest_coverage_stress_1512(gds_base_universe_d2_016_gds_043_interest_coverage_stress_1512):
    return _base_universe_d3(gds_base_universe_d2_016_gds_043_interest_coverage_stress_1512, 16)
GDS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['gds_base_universe_d3_016_gds_043_interest_coverage_stress_1512'] = {'inputs': ['gds_base_universe_d2_016_gds_043_interest_coverage_stress_1512'], 'func': gds_base_universe_d3_016_gds_043_interest_coverage_stress_1512}


def gds_base_universe_d3_017_gds_048_accrual_gap_63(gds_base_universe_d2_017_gds_048_accrual_gap_63):
    return _base_universe_d3(gds_base_universe_d2_017_gds_048_accrual_gap_63, 17)
GDS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['gds_base_universe_d3_017_gds_048_accrual_gap_63'] = {'inputs': ['gds_base_universe_d2_017_gds_048_accrual_gap_63'], 'func': gds_base_universe_d3_017_gds_048_accrual_gap_63}


def gds_base_universe_d3_018_gds_051_fcf_burn_to_cash_189(gds_base_universe_d2_018_gds_051_fcf_burn_to_cash_189):
    return _base_universe_d3(gds_base_universe_d2_018_gds_051_fcf_burn_to_cash_189, 18)
GDS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['gds_base_universe_d3_018_gds_051_fcf_burn_to_cash_189'] = {'inputs': ['gds_base_universe_d2_018_gds_051_fcf_burn_to_cash_189'], 'func': gds_base_universe_d3_018_gds_051_fcf_burn_to_cash_189}


def gds_base_universe_d3_019_gds_052_debt_to_equity_252(gds_base_universe_d2_019_gds_052_debt_to_equity_252):
    return _base_universe_d3(gds_base_universe_d2_019_gds_052_debt_to_equity_252, 19)
GDS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['gds_base_universe_d3_019_gds_052_debt_to_equity_252'] = {'inputs': ['gds_base_universe_d2_019_gds_052_debt_to_equity_252'], 'func': gds_base_universe_d3_019_gds_052_debt_to_equity_252}


def gds_base_universe_d3_020_gds_053_debt_to_assets_378(gds_base_universe_d2_020_gds_053_debt_to_assets_378):
    return _base_universe_d3(gds_base_universe_d2_020_gds_053_debt_to_assets_378, 20)
GDS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['gds_base_universe_d3_020_gds_053_debt_to_assets_378'] = {'inputs': ['gds_base_universe_d2_020_gds_053_debt_to_assets_378'], 'func': gds_base_universe_d3_020_gds_053_debt_to_assets_378}


def gds_base_universe_d3_021_gds_055_interest_coverage_stress_756(gds_base_universe_d2_021_gds_055_interest_coverage_stress_756):
    return _base_universe_d3(gds_base_universe_d2_021_gds_055_interest_coverage_stress_756, 21)
GDS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['gds_base_universe_d3_021_gds_055_interest_coverage_stress_756'] = {'inputs': ['gds_base_universe_d2_021_gds_055_interest_coverage_stress_756'], 'func': gds_base_universe_d3_021_gds_055_interest_coverage_stress_756}


def gds_base_universe_d3_022_gds_060_accrual_gap_252(gds_base_universe_d2_022_gds_060_accrual_gap_252):
    return _base_universe_d3(gds_base_universe_d2_022_gds_060_accrual_gap_252, 22)
GDS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['gds_base_universe_d3_022_gds_060_accrual_gap_252'] = {'inputs': ['gds_base_universe_d2_022_gds_060_accrual_gap_252'], 'func': gds_base_universe_d3_022_gds_060_accrual_gap_252}


def gds_base_universe_d3_023_gds_basefill_001(gds_base_universe_d2_023_gds_basefill_001):
    return _base_universe_d3(gds_base_universe_d2_023_gds_basefill_001, 23)
GDS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['gds_base_universe_d3_023_gds_basefill_001'] = {'inputs': ['gds_base_universe_d2_023_gds_basefill_001'], 'func': gds_base_universe_d3_023_gds_basefill_001}


def gds_base_universe_d3_024_gds_basefill_002(gds_base_universe_d2_024_gds_basefill_002):
    return _base_universe_d3(gds_base_universe_d2_024_gds_basefill_002, 24)
GDS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['gds_base_universe_d3_024_gds_basefill_002'] = {'inputs': ['gds_base_universe_d2_024_gds_basefill_002'], 'func': gds_base_universe_d3_024_gds_basefill_002}


def gds_base_universe_d3_025_gds_basefill_006(gds_base_universe_d2_025_gds_basefill_006):
    return _base_universe_d3(gds_base_universe_d2_025_gds_basefill_006, 25)
GDS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['gds_base_universe_d3_025_gds_basefill_006'] = {'inputs': ['gds_base_universe_d2_025_gds_basefill_006'], 'func': gds_base_universe_d3_025_gds_basefill_006}


def gds_base_universe_d3_026_gds_basefill_008(gds_base_universe_d2_026_gds_basefill_008):
    return _base_universe_d3(gds_base_universe_d2_026_gds_basefill_008, 26)
GDS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['gds_base_universe_d3_026_gds_basefill_008'] = {'inputs': ['gds_base_universe_d2_026_gds_basefill_008'], 'func': gds_base_universe_d3_026_gds_basefill_008}


def gds_base_universe_d3_027_gds_basefill_009(gds_base_universe_d2_027_gds_basefill_009):
    return _base_universe_d3(gds_base_universe_d2_027_gds_basefill_009, 27)
GDS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['gds_base_universe_d3_027_gds_basefill_009'] = {'inputs': ['gds_base_universe_d2_027_gds_basefill_009'], 'func': gds_base_universe_d3_027_gds_basefill_009}


def gds_base_universe_d3_028_gds_basefill_010(gds_base_universe_d2_028_gds_basefill_010):
    return _base_universe_d3(gds_base_universe_d2_028_gds_basefill_010, 28)
GDS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['gds_base_universe_d3_028_gds_basefill_010'] = {'inputs': ['gds_base_universe_d2_028_gds_basefill_010'], 'func': gds_base_universe_d3_028_gds_basefill_010}


def gds_base_universe_d3_029_gds_basefill_011(gds_base_universe_d2_029_gds_basefill_011):
    return _base_universe_d3(gds_base_universe_d2_029_gds_basefill_011, 29)
GDS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['gds_base_universe_d3_029_gds_basefill_011'] = {'inputs': ['gds_base_universe_d2_029_gds_basefill_011'], 'func': gds_base_universe_d3_029_gds_basefill_011}


def gds_base_universe_d3_030_gds_basefill_013(gds_base_universe_d2_030_gds_basefill_013):
    return _base_universe_d3(gds_base_universe_d2_030_gds_basefill_013, 30)
GDS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['gds_base_universe_d3_030_gds_basefill_013'] = {'inputs': ['gds_base_universe_d2_030_gds_basefill_013'], 'func': gds_base_universe_d3_030_gds_basefill_013}


def gds_base_universe_d3_031_gds_basefill_014(gds_base_universe_d2_031_gds_basefill_014):
    return _base_universe_d3(gds_base_universe_d2_031_gds_basefill_014, 31)
GDS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['gds_base_universe_d3_031_gds_basefill_014'] = {'inputs': ['gds_base_universe_d2_031_gds_basefill_014'], 'func': gds_base_universe_d3_031_gds_basefill_014}


def gds_base_universe_d3_032_gds_basefill_015(gds_base_universe_d2_032_gds_basefill_015):
    return _base_universe_d3(gds_base_universe_d2_032_gds_basefill_015, 32)
GDS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['gds_base_universe_d3_032_gds_basefill_015'] = {'inputs': ['gds_base_universe_d2_032_gds_basefill_015'], 'func': gds_base_universe_d3_032_gds_basefill_015}


def gds_base_universe_d3_033_gds_basefill_018(gds_base_universe_d2_033_gds_basefill_018):
    return _base_universe_d3(gds_base_universe_d2_033_gds_basefill_018, 33)
GDS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['gds_base_universe_d3_033_gds_basefill_018'] = {'inputs': ['gds_base_universe_d2_033_gds_basefill_018'], 'func': gds_base_universe_d3_033_gds_basefill_018}


def gds_base_universe_d3_034_gds_basefill_020(gds_base_universe_d2_034_gds_basefill_020):
    return _base_universe_d3(gds_base_universe_d2_034_gds_basefill_020, 34)
GDS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['gds_base_universe_d3_034_gds_basefill_020'] = {'inputs': ['gds_base_universe_d2_034_gds_basefill_020'], 'func': gds_base_universe_d3_034_gds_basefill_020}


def gds_base_universe_d3_035_gds_basefill_021(gds_base_universe_d2_035_gds_basefill_021):
    return _base_universe_d3(gds_base_universe_d2_035_gds_basefill_021, 35)
GDS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['gds_base_universe_d3_035_gds_basefill_021'] = {'inputs': ['gds_base_universe_d2_035_gds_basefill_021'], 'func': gds_base_universe_d3_035_gds_basefill_021}


def gds_base_universe_d3_036_gds_basefill_022(gds_base_universe_d2_036_gds_basefill_022):
    return _base_universe_d3(gds_base_universe_d2_036_gds_basefill_022, 36)
GDS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['gds_base_universe_d3_036_gds_basefill_022'] = {'inputs': ['gds_base_universe_d2_036_gds_basefill_022'], 'func': gds_base_universe_d3_036_gds_basefill_022}


def gds_base_universe_d3_037_gds_basefill_023(gds_base_universe_d2_037_gds_basefill_023):
    return _base_universe_d3(gds_base_universe_d2_037_gds_basefill_023, 37)
GDS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['gds_base_universe_d3_037_gds_basefill_023'] = {'inputs': ['gds_base_universe_d2_037_gds_basefill_023'], 'func': gds_base_universe_d3_037_gds_basefill_023}


def gds_base_universe_d3_038_gds_basefill_025(gds_base_universe_d2_038_gds_basefill_025):
    return _base_universe_d3(gds_base_universe_d2_038_gds_basefill_025, 38)
GDS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['gds_base_universe_d3_038_gds_basefill_025'] = {'inputs': ['gds_base_universe_d2_038_gds_basefill_025'], 'func': gds_base_universe_d3_038_gds_basefill_025}


def gds_base_universe_d3_039_gds_basefill_026(gds_base_universe_d2_039_gds_basefill_026):
    return _base_universe_d3(gds_base_universe_d2_039_gds_basefill_026, 39)
GDS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['gds_base_universe_d3_039_gds_basefill_026'] = {'inputs': ['gds_base_universe_d2_039_gds_basefill_026'], 'func': gds_base_universe_d3_039_gds_basefill_026}


def gds_base_universe_d3_040_gds_basefill_030(gds_base_universe_d2_040_gds_basefill_030):
    return _base_universe_d3(gds_base_universe_d2_040_gds_basefill_030, 40)
GDS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['gds_base_universe_d3_040_gds_basefill_030'] = {'inputs': ['gds_base_universe_d2_040_gds_basefill_030'], 'func': gds_base_universe_d3_040_gds_basefill_030}


def gds_base_universe_d3_041_gds_basefill_032(gds_base_universe_d2_041_gds_basefill_032):
    return _base_universe_d3(gds_base_universe_d2_041_gds_basefill_032, 41)
GDS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['gds_base_universe_d3_041_gds_basefill_032'] = {'inputs': ['gds_base_universe_d2_041_gds_basefill_032'], 'func': gds_base_universe_d3_041_gds_basefill_032}


def gds_base_universe_d3_042_gds_basefill_033(gds_base_universe_d2_042_gds_basefill_033):
    return _base_universe_d3(gds_base_universe_d2_042_gds_basefill_033, 42)
GDS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['gds_base_universe_d3_042_gds_basefill_033'] = {'inputs': ['gds_base_universe_d2_042_gds_basefill_033'], 'func': gds_base_universe_d3_042_gds_basefill_033}


def gds_base_universe_d3_043_gds_basefill_034(gds_base_universe_d2_043_gds_basefill_034):
    return _base_universe_d3(gds_base_universe_d2_043_gds_basefill_034, 43)
GDS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['gds_base_universe_d3_043_gds_basefill_034'] = {'inputs': ['gds_base_universe_d2_043_gds_basefill_034'], 'func': gds_base_universe_d3_043_gds_basefill_034}


def gds_base_universe_d3_044_gds_basefill_035(gds_base_universe_d2_044_gds_basefill_035):
    return _base_universe_d3(gds_base_universe_d2_044_gds_basefill_035, 44)
GDS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['gds_base_universe_d3_044_gds_basefill_035'] = {'inputs': ['gds_base_universe_d2_044_gds_basefill_035'], 'func': gds_base_universe_d3_044_gds_basefill_035}


def gds_base_universe_d3_045_gds_basefill_037(gds_base_universe_d2_045_gds_basefill_037):
    return _base_universe_d3(gds_base_universe_d2_045_gds_basefill_037, 45)
GDS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['gds_base_universe_d3_045_gds_basefill_037'] = {'inputs': ['gds_base_universe_d2_045_gds_basefill_037'], 'func': gds_base_universe_d3_045_gds_basefill_037}


def gds_base_universe_d3_046_gds_basefill_038(gds_base_universe_d2_046_gds_basefill_038):
    return _base_universe_d3(gds_base_universe_d2_046_gds_basefill_038, 46)
GDS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['gds_base_universe_d3_046_gds_basefill_038'] = {'inputs': ['gds_base_universe_d2_046_gds_basefill_038'], 'func': gds_base_universe_d3_046_gds_basefill_038}


def gds_base_universe_d3_047_gds_basefill_042(gds_base_universe_d2_047_gds_basefill_042):
    return _base_universe_d3(gds_base_universe_d2_047_gds_basefill_042, 47)
GDS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['gds_base_universe_d3_047_gds_basefill_042'] = {'inputs': ['gds_base_universe_d2_047_gds_basefill_042'], 'func': gds_base_universe_d3_047_gds_basefill_042}


def gds_base_universe_d3_048_gds_basefill_044(gds_base_universe_d2_048_gds_basefill_044):
    return _base_universe_d3(gds_base_universe_d2_048_gds_basefill_044, 48)
GDS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['gds_base_universe_d3_048_gds_basefill_044'] = {'inputs': ['gds_base_universe_d2_048_gds_basefill_044'], 'func': gds_base_universe_d3_048_gds_basefill_044}


def gds_base_universe_d3_049_gds_basefill_045(gds_base_universe_d2_049_gds_basefill_045):
    return _base_universe_d3(gds_base_universe_d2_049_gds_basefill_045, 49)
GDS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['gds_base_universe_d3_049_gds_basefill_045'] = {'inputs': ['gds_base_universe_d2_049_gds_basefill_045'], 'func': gds_base_universe_d3_049_gds_basefill_045}


def gds_base_universe_d3_050_gds_basefill_046(gds_base_universe_d2_050_gds_basefill_046):
    return _base_universe_d3(gds_base_universe_d2_050_gds_basefill_046, 50)
GDS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['gds_base_universe_d3_050_gds_basefill_046'] = {'inputs': ['gds_base_universe_d2_050_gds_basefill_046'], 'func': gds_base_universe_d3_050_gds_basefill_046}


def gds_base_universe_d3_051_gds_basefill_047(gds_base_universe_d2_051_gds_basefill_047):
    return _base_universe_d3(gds_base_universe_d2_051_gds_basefill_047, 51)
GDS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['gds_base_universe_d3_051_gds_basefill_047'] = {'inputs': ['gds_base_universe_d2_051_gds_basefill_047'], 'func': gds_base_universe_d3_051_gds_basefill_047}


def gds_base_universe_d3_052_gds_basefill_049(gds_base_universe_d2_052_gds_basefill_049):
    return _base_universe_d3(gds_base_universe_d2_052_gds_basefill_049, 52)
GDS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['gds_base_universe_d3_052_gds_basefill_049'] = {'inputs': ['gds_base_universe_d2_052_gds_basefill_049'], 'func': gds_base_universe_d3_052_gds_basefill_049}


def gds_base_universe_d3_053_gds_basefill_050(gds_base_universe_d2_053_gds_basefill_050):
    return _base_universe_d3(gds_base_universe_d2_053_gds_basefill_050, 53)
GDS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['gds_base_universe_d3_053_gds_basefill_050'] = {'inputs': ['gds_base_universe_d2_053_gds_basefill_050'], 'func': gds_base_universe_d3_053_gds_basefill_050}


def gds_base_universe_d3_054_gds_basefill_054(gds_base_universe_d2_054_gds_basefill_054):
    return _base_universe_d3(gds_base_universe_d2_054_gds_basefill_054, 54)
GDS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['gds_base_universe_d3_054_gds_basefill_054'] = {'inputs': ['gds_base_universe_d2_054_gds_basefill_054'], 'func': gds_base_universe_d3_054_gds_basefill_054}


def gds_base_universe_d3_055_gds_basefill_056(gds_base_universe_d2_055_gds_basefill_056):
    return _base_universe_d3(gds_base_universe_d2_055_gds_basefill_056, 55)
GDS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['gds_base_universe_d3_055_gds_basefill_056'] = {'inputs': ['gds_base_universe_d2_055_gds_basefill_056'], 'func': gds_base_universe_d3_055_gds_basefill_056}


def gds_base_universe_d3_056_gds_basefill_057(gds_base_universe_d2_056_gds_basefill_057):
    return _base_universe_d3(gds_base_universe_d2_056_gds_basefill_057, 56)
GDS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['gds_base_universe_d3_056_gds_basefill_057'] = {'inputs': ['gds_base_universe_d2_056_gds_basefill_057'], 'func': gds_base_universe_d3_056_gds_basefill_057}


def gds_base_universe_d3_057_gds_basefill_058(gds_base_universe_d2_057_gds_basefill_058):
    return _base_universe_d3(gds_base_universe_d2_057_gds_basefill_058, 57)
GDS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['gds_base_universe_d3_057_gds_basefill_058'] = {'inputs': ['gds_base_universe_d2_057_gds_basefill_058'], 'func': gds_base_universe_d3_057_gds_basefill_058}


def gds_base_universe_d3_058_gds_basefill_059(gds_base_universe_d2_058_gds_basefill_059):
    return _base_universe_d3(gds_base_universe_d2_058_gds_basefill_059, 58)
GDS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['gds_base_universe_d3_058_gds_basefill_059'] = {'inputs': ['gds_base_universe_d2_058_gds_basefill_059'], 'func': gds_base_universe_d3_058_gds_basefill_059}


def gds_base_universe_d3_059_gds_basefill_061(gds_base_universe_d2_059_gds_basefill_061):
    return _base_universe_d3(gds_base_universe_d2_059_gds_basefill_061, 59)
GDS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['gds_base_universe_d3_059_gds_basefill_061'] = {'inputs': ['gds_base_universe_d2_059_gds_basefill_061'], 'func': gds_base_universe_d3_059_gds_basefill_061}


def gds_base_universe_d3_060_gds_basefill_062(gds_base_universe_d2_060_gds_basefill_062):
    return _base_universe_d3(gds_base_universe_d2_060_gds_basefill_062, 60)
GDS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['gds_base_universe_d3_060_gds_basefill_062'] = {'inputs': ['gds_base_universe_d2_060_gds_basefill_062'], 'func': gds_base_universe_d3_060_gds_basefill_062}


def gds_base_universe_d3_061_gds_basefill_063(gds_base_universe_d2_061_gds_basefill_063):
    return _base_universe_d3(gds_base_universe_d2_061_gds_basefill_063, 61)
GDS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['gds_base_universe_d3_061_gds_basefill_063'] = {'inputs': ['gds_base_universe_d2_061_gds_basefill_063'], 'func': gds_base_universe_d3_061_gds_basefill_063}


def gds_base_universe_d3_062_gds_basefill_064(gds_base_universe_d2_062_gds_basefill_064):
    return _base_universe_d3(gds_base_universe_d2_062_gds_basefill_064, 62)
GDS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['gds_base_universe_d3_062_gds_basefill_064'] = {'inputs': ['gds_base_universe_d2_062_gds_basefill_064'], 'func': gds_base_universe_d3_062_gds_basefill_064}


def gds_base_universe_d3_063_gds_basefill_065(gds_base_universe_d2_063_gds_basefill_065):
    return _base_universe_d3(gds_base_universe_d2_063_gds_basefill_065, 63)
GDS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['gds_base_universe_d3_063_gds_basefill_065'] = {'inputs': ['gds_base_universe_d2_063_gds_basefill_065'], 'func': gds_base_universe_d3_063_gds_basefill_065}


def gds_base_universe_d3_064_gds_basefill_066(gds_base_universe_d2_064_gds_basefill_066):
    return _base_universe_d3(gds_base_universe_d2_064_gds_basefill_066, 64)
GDS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['gds_base_universe_d3_064_gds_basefill_066'] = {'inputs': ['gds_base_universe_d2_064_gds_basefill_066'], 'func': gds_base_universe_d3_064_gds_basefill_066}


def gds_base_universe_d3_065_gds_basefill_067(gds_base_universe_d2_065_gds_basefill_067):
    return _base_universe_d3(gds_base_universe_d2_065_gds_basefill_067, 65)
GDS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['gds_base_universe_d3_065_gds_basefill_067'] = {'inputs': ['gds_base_universe_d2_065_gds_basefill_067'], 'func': gds_base_universe_d3_065_gds_basefill_067}


def gds_base_universe_d3_066_gds_basefill_068(gds_base_universe_d2_066_gds_basefill_068):
    return _base_universe_d3(gds_base_universe_d2_066_gds_basefill_068, 66)
GDS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['gds_base_universe_d3_066_gds_basefill_068'] = {'inputs': ['gds_base_universe_d2_066_gds_basefill_068'], 'func': gds_base_universe_d3_066_gds_basefill_068}


def gds_base_universe_d3_067_gds_basefill_069(gds_base_universe_d2_067_gds_basefill_069):
    return _base_universe_d3(gds_base_universe_d2_067_gds_basefill_069, 67)
GDS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['gds_base_universe_d3_067_gds_basefill_069'] = {'inputs': ['gds_base_universe_d2_067_gds_basefill_069'], 'func': gds_base_universe_d3_067_gds_basefill_069}


def gds_base_universe_d3_068_gds_basefill_070(gds_base_universe_d2_068_gds_basefill_070):
    return _base_universe_d3(gds_base_universe_d2_068_gds_basefill_070, 68)
GDS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['gds_base_universe_d3_068_gds_basefill_070'] = {'inputs': ['gds_base_universe_d2_068_gds_basefill_070'], 'func': gds_base_universe_d3_068_gds_basefill_070}


def gds_base_universe_d3_069_gds_basefill_071(gds_base_universe_d2_069_gds_basefill_071):
    return _base_universe_d3(gds_base_universe_d2_069_gds_basefill_071, 69)
GDS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['gds_base_universe_d3_069_gds_basefill_071'] = {'inputs': ['gds_base_universe_d2_069_gds_basefill_071'], 'func': gds_base_universe_d3_069_gds_basefill_071}


def gds_base_universe_d3_070_gds_basefill_072(gds_base_universe_d2_070_gds_basefill_072):
    return _base_universe_d3(gds_base_universe_d2_070_gds_basefill_072, 70)
GDS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['gds_base_universe_d3_070_gds_basefill_072'] = {'inputs': ['gds_base_universe_d2_070_gds_basefill_072'], 'func': gds_base_universe_d3_070_gds_basefill_072}


def gds_base_universe_d3_071_gds_basefill_073(gds_base_universe_d2_071_gds_basefill_073):
    return _base_universe_d3(gds_base_universe_d2_071_gds_basefill_073, 71)
GDS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['gds_base_universe_d3_071_gds_basefill_073'] = {'inputs': ['gds_base_universe_d2_071_gds_basefill_073'], 'func': gds_base_universe_d3_071_gds_basefill_073}


def gds_base_universe_d3_072_gds_basefill_074(gds_base_universe_d2_072_gds_basefill_074):
    return _base_universe_d3(gds_base_universe_d2_072_gds_basefill_074, 72)
GDS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['gds_base_universe_d3_072_gds_basefill_074'] = {'inputs': ['gds_base_universe_d2_072_gds_basefill_074'], 'func': gds_base_universe_d3_072_gds_basefill_074}


def gds_base_universe_d3_073_gds_basefill_075(gds_base_universe_d2_073_gds_basefill_075):
    return _base_universe_d3(gds_base_universe_d2_073_gds_basefill_075, 73)
GDS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['gds_base_universe_d3_073_gds_basefill_075'] = {'inputs': ['gds_base_universe_d2_073_gds_basefill_075'], 'func': gds_base_universe_d3_073_gds_basefill_075}
