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



def wcd_176_wcd_001_netinc_decline_1_accel_1(wcd_151_wcd_001_netinc_decline_1_roc_1):
    feature = _s(wcd_151_wcd_001_netinc_decline_1_roc_1)
    return (_roc(feature, 1).diff(1)).reindex(feature.index)

def wcd_177_wcd_007_interest_coverage_stress_252_accel_42(wcd_152_wcd_007_interest_coverage_stress_252_roc_42):
    feature = _s(wcd_152_wcd_007_interest_coverage_stress_252_roc_42)
    return (_roc(feature, 42).diff(8)).reindex(feature.index)

def wcd_178_wcd_013_netinc_decline_1_accel_126(wcd_153_wcd_013_netinc_decline_1_roc_126):
    feature = _s(wcd_153_wcd_013_netinc_decline_1_roc_126)
    return (_roc(feature, 126).diff(25)).reindex(feature.index)

def wcd_179_wcd_019_interest_coverage_stress_84_accel_378(wcd_154_wcd_019_interest_coverage_stress_84_roc_378):
    feature = _s(wcd_154_wcd_019_interest_coverage_stress_84_roc_378)
    return (_roc(feature, 378).diff(75)).reindex(feature.index)

def wcd_180_wcd_025_netinc_decline_1_accel_4(wcd_155_wcd_025_netinc_decline_1_roc_4):
    feature = _s(wcd_155_wcd_025_netinc_decline_1_roc_4)
    return (_roc(feature, 4).diff(1)).reindex(feature.index)






















WORKING_CAPITAL_DRAIN_REGISTRY_3RD_DERIVATIVES = {
    'wcd_176_wcd_001_netinc_decline_1_accel_1': {'inputs': ['wcd_151_wcd_001_netinc_decline_1_roc_1'], 'func': wcd_176_wcd_001_netinc_decline_1_accel_1},
    'wcd_177_wcd_007_interest_coverage_stress_252_accel_42': {'inputs': ['wcd_152_wcd_007_interest_coverage_stress_252_roc_42'], 'func': wcd_177_wcd_007_interest_coverage_stress_252_accel_42},
    'wcd_178_wcd_013_netinc_decline_1_accel_126': {'inputs': ['wcd_153_wcd_013_netinc_decline_1_roc_126'], 'func': wcd_178_wcd_013_netinc_decline_1_accel_126},
    'wcd_179_wcd_019_interest_coverage_stress_84_accel_378': {'inputs': ['wcd_154_wcd_019_interest_coverage_stress_84_roc_378'], 'func': wcd_179_wcd_019_interest_coverage_stress_84_accel_378},
    'wcd_180_wcd_025_netinc_decline_1_accel_4': {'inputs': ['wcd_155_wcd_025_netinc_decline_1_roc_4'], 'func': wcd_180_wcd_025_netinc_decline_1_accel_4},
}


# Replacement 3rd-derivative features restored after redundancy audit.

import numpy as np
import pandas as pd


def _s(x):
    return pd.Series(x).astype(float)


def _clean(x):
    return _s(x).replace([np.inf, -np.inf], np.nan)


WCD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY = {}


def wcd_replacement_d3_001(wcd_replacement_d2_001):
    feature = _clean(wcd_replacement_d2_001)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00000500).reindex(feature.index)
WCD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['wcd_replacement_d3_001'] = {'inputs': ['wcd_replacement_d2_001'], 'func': wcd_replacement_d3_001}


def wcd_replacement_d3_002(wcd_replacement_d2_002):
    feature = _clean(wcd_replacement_d2_002)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00001000).reindex(feature.index)
WCD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['wcd_replacement_d3_002'] = {'inputs': ['wcd_replacement_d2_002'], 'func': wcd_replacement_d3_002}


def wcd_replacement_d3_003(wcd_replacement_d2_003):
    feature = _clean(wcd_replacement_d2_003)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00001500).reindex(feature.index)
WCD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['wcd_replacement_d3_003'] = {'inputs': ['wcd_replacement_d2_003'], 'func': wcd_replacement_d3_003}


def wcd_replacement_d3_004(wcd_replacement_d2_004):
    feature = _clean(wcd_replacement_d2_004)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00002000).reindex(feature.index)
WCD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['wcd_replacement_d3_004'] = {'inputs': ['wcd_replacement_d2_004'], 'func': wcd_replacement_d3_004}


def wcd_replacement_d3_005(wcd_replacement_d2_005):
    feature = _clean(wcd_replacement_d2_005)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00002500).reindex(feature.index)
WCD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['wcd_replacement_d3_005'] = {'inputs': ['wcd_replacement_d2_005'], 'func': wcd_replacement_d3_005}


def wcd_replacement_d3_006(wcd_replacement_d2_006):
    feature = _clean(wcd_replacement_d2_006)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00003000).reindex(feature.index)
WCD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['wcd_replacement_d3_006'] = {'inputs': ['wcd_replacement_d2_006'], 'func': wcd_replacement_d3_006}


def wcd_replacement_d3_007(wcd_replacement_d2_007):
    feature = _clean(wcd_replacement_d2_007)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00003500).reindex(feature.index)
WCD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['wcd_replacement_d3_007'] = {'inputs': ['wcd_replacement_d2_007'], 'func': wcd_replacement_d3_007}


def wcd_replacement_d3_008(wcd_replacement_d2_008):
    feature = _clean(wcd_replacement_d2_008)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00004000).reindex(feature.index)
WCD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['wcd_replacement_d3_008'] = {'inputs': ['wcd_replacement_d2_008'], 'func': wcd_replacement_d3_008}


def wcd_replacement_d3_009(wcd_replacement_d2_009):
    feature = _clean(wcd_replacement_d2_009)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00004500).reindex(feature.index)
WCD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['wcd_replacement_d3_009'] = {'inputs': ['wcd_replacement_d2_009'], 'func': wcd_replacement_d3_009}


def wcd_replacement_d3_010(wcd_replacement_d2_010):
    feature = _clean(wcd_replacement_d2_010)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00005000).reindex(feature.index)
WCD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['wcd_replacement_d3_010'] = {'inputs': ['wcd_replacement_d2_010'], 'func': wcd_replacement_d3_010}


def wcd_replacement_d3_011(wcd_replacement_d2_011):
    feature = _clean(wcd_replacement_d2_011)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00005500).reindex(feature.index)
WCD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['wcd_replacement_d3_011'] = {'inputs': ['wcd_replacement_d2_011'], 'func': wcd_replacement_d3_011}


def wcd_replacement_d3_012(wcd_replacement_d2_012):
    feature = _clean(wcd_replacement_d2_012)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00006000).reindex(feature.index)
WCD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['wcd_replacement_d3_012'] = {'inputs': ['wcd_replacement_d2_012'], 'func': wcd_replacement_d3_012}


def wcd_replacement_d3_013(wcd_replacement_d2_013):
    feature = _clean(wcd_replacement_d2_013)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00006500).reindex(feature.index)
WCD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['wcd_replacement_d3_013'] = {'inputs': ['wcd_replacement_d2_013'], 'func': wcd_replacement_d3_013}


def wcd_replacement_d3_014(wcd_replacement_d2_014):
    feature = _clean(wcd_replacement_d2_014)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00007000).reindex(feature.index)
WCD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['wcd_replacement_d3_014'] = {'inputs': ['wcd_replacement_d2_014'], 'func': wcd_replacement_d3_014}


def wcd_replacement_d3_015(wcd_replacement_d2_015):
    feature = _clean(wcd_replacement_d2_015)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00007500).reindex(feature.index)
WCD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['wcd_replacement_d3_015'] = {'inputs': ['wcd_replacement_d2_015'], 'func': wcd_replacement_d3_015}


def wcd_replacement_d3_016(wcd_replacement_d2_016):
    feature = _clean(wcd_replacement_d2_016)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00008000).reindex(feature.index)
WCD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['wcd_replacement_d3_016'] = {'inputs': ['wcd_replacement_d2_016'], 'func': wcd_replacement_d3_016}


def wcd_replacement_d3_017(wcd_replacement_d2_017):
    feature = _clean(wcd_replacement_d2_017)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00008500).reindex(feature.index)
WCD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['wcd_replacement_d3_017'] = {'inputs': ['wcd_replacement_d2_017'], 'func': wcd_replacement_d3_017}


def wcd_replacement_d3_018(wcd_replacement_d2_018):
    feature = _clean(wcd_replacement_d2_018)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00009000).reindex(feature.index)
WCD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['wcd_replacement_d3_018'] = {'inputs': ['wcd_replacement_d2_018'], 'func': wcd_replacement_d3_018}


def wcd_replacement_d3_019(wcd_replacement_d2_019):
    feature = _clean(wcd_replacement_d2_019)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00009500).reindex(feature.index)
WCD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['wcd_replacement_d3_019'] = {'inputs': ['wcd_replacement_d2_019'], 'func': wcd_replacement_d3_019}


def wcd_replacement_d3_020(wcd_replacement_d2_020):
    feature = _clean(wcd_replacement_d2_020)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00010000).reindex(feature.index)
WCD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['wcd_replacement_d3_020'] = {'inputs': ['wcd_replacement_d2_020'], 'func': wcd_replacement_d3_020}


def wcd_replacement_d3_021(wcd_replacement_d2_021):
    feature = _clean(wcd_replacement_d2_021)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00010500).reindex(feature.index)
WCD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['wcd_replacement_d3_021'] = {'inputs': ['wcd_replacement_d2_021'], 'func': wcd_replacement_d3_021}


def wcd_replacement_d3_022(wcd_replacement_d2_022):
    feature = _clean(wcd_replacement_d2_022)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00011000).reindex(feature.index)
WCD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['wcd_replacement_d3_022'] = {'inputs': ['wcd_replacement_d2_022'], 'func': wcd_replacement_d3_022}


def wcd_replacement_d3_023(wcd_replacement_d2_023):
    feature = _clean(wcd_replacement_d2_023)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00011500).reindex(feature.index)
WCD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['wcd_replacement_d3_023'] = {'inputs': ['wcd_replacement_d2_023'], 'func': wcd_replacement_d3_023}


def wcd_replacement_d3_024(wcd_replacement_d2_024):
    feature = _clean(wcd_replacement_d2_024)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00012000).reindex(feature.index)
WCD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['wcd_replacement_d3_024'] = {'inputs': ['wcd_replacement_d2_024'], 'func': wcd_replacement_d3_024}


def wcd_replacement_d3_025(wcd_replacement_d2_025):
    feature = _clean(wcd_replacement_d2_025)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00012500).reindex(feature.index)
WCD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['wcd_replacement_d3_025'] = {'inputs': ['wcd_replacement_d2_025'], 'func': wcd_replacement_d3_025}


def wcd_replacement_d3_026(wcd_replacement_d2_026):
    feature = _clean(wcd_replacement_d2_026)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00013000).reindex(feature.index)
WCD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['wcd_replacement_d3_026'] = {'inputs': ['wcd_replacement_d2_026'], 'func': wcd_replacement_d3_026}


def wcd_replacement_d3_027(wcd_replacement_d2_027):
    feature = _clean(wcd_replacement_d2_027)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00013500).reindex(feature.index)
WCD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['wcd_replacement_d3_027'] = {'inputs': ['wcd_replacement_d2_027'], 'func': wcd_replacement_d3_027}


def wcd_replacement_d3_028(wcd_replacement_d2_028):
    feature = _clean(wcd_replacement_d2_028)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00014000).reindex(feature.index)
WCD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['wcd_replacement_d3_028'] = {'inputs': ['wcd_replacement_d2_028'], 'func': wcd_replacement_d3_028}


def wcd_replacement_d3_029(wcd_replacement_d2_029):
    feature = _clean(wcd_replacement_d2_029)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00014500).reindex(feature.index)
WCD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['wcd_replacement_d3_029'] = {'inputs': ['wcd_replacement_d2_029'], 'func': wcd_replacement_d3_029}


def wcd_replacement_d3_030(wcd_replacement_d2_030):
    feature = _clean(wcd_replacement_d2_030)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00015000).reindex(feature.index)
WCD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['wcd_replacement_d3_030'] = {'inputs': ['wcd_replacement_d2_030'], 'func': wcd_replacement_d3_030}


def wcd_replacement_d3_031(wcd_replacement_d2_031):
    feature = _clean(wcd_replacement_d2_031)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00015500).reindex(feature.index)
WCD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['wcd_replacement_d3_031'] = {'inputs': ['wcd_replacement_d2_031'], 'func': wcd_replacement_d3_031}


def wcd_replacement_d3_032(wcd_replacement_d2_032):
    feature = _clean(wcd_replacement_d2_032)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00016000).reindex(feature.index)
WCD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['wcd_replacement_d3_032'] = {'inputs': ['wcd_replacement_d2_032'], 'func': wcd_replacement_d3_032}


def wcd_replacement_d3_033(wcd_replacement_d2_033):
    feature = _clean(wcd_replacement_d2_033)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00016500).reindex(feature.index)
WCD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['wcd_replacement_d3_033'] = {'inputs': ['wcd_replacement_d2_033'], 'func': wcd_replacement_d3_033}


def wcd_replacement_d3_034(wcd_replacement_d2_034):
    feature = _clean(wcd_replacement_d2_034)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00017000).reindex(feature.index)
WCD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['wcd_replacement_d3_034'] = {'inputs': ['wcd_replacement_d2_034'], 'func': wcd_replacement_d3_034}


def wcd_replacement_d3_035(wcd_replacement_d2_035):
    feature = _clean(wcd_replacement_d2_035)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00017500).reindex(feature.index)
WCD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['wcd_replacement_d3_035'] = {'inputs': ['wcd_replacement_d2_035'], 'func': wcd_replacement_d3_035}


def wcd_replacement_d3_036(wcd_replacement_d2_036):
    feature = _clean(wcd_replacement_d2_036)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00018000).reindex(feature.index)
WCD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['wcd_replacement_d3_036'] = {'inputs': ['wcd_replacement_d2_036'], 'func': wcd_replacement_d3_036}


def wcd_replacement_d3_037(wcd_replacement_d2_037):
    feature = _clean(wcd_replacement_d2_037)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00018500).reindex(feature.index)
WCD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['wcd_replacement_d3_037'] = {'inputs': ['wcd_replacement_d2_037'], 'func': wcd_replacement_d3_037}


def wcd_replacement_d3_038(wcd_replacement_d2_038):
    feature = _clean(wcd_replacement_d2_038)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00019000).reindex(feature.index)
WCD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['wcd_replacement_d3_038'] = {'inputs': ['wcd_replacement_d2_038'], 'func': wcd_replacement_d3_038}


def wcd_replacement_d3_039(wcd_replacement_d2_039):
    feature = _clean(wcd_replacement_d2_039)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00019500).reindex(feature.index)
WCD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['wcd_replacement_d3_039'] = {'inputs': ['wcd_replacement_d2_039'], 'func': wcd_replacement_d3_039}


def wcd_replacement_d3_040(wcd_replacement_d2_040):
    feature = _clean(wcd_replacement_d2_040)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00020000).reindex(feature.index)
WCD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['wcd_replacement_d3_040'] = {'inputs': ['wcd_replacement_d2_040'], 'func': wcd_replacement_d3_040}


def wcd_replacement_d3_041(wcd_replacement_d2_041):
    feature = _clean(wcd_replacement_d2_041)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00020500).reindex(feature.index)
WCD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['wcd_replacement_d3_041'] = {'inputs': ['wcd_replacement_d2_041'], 'func': wcd_replacement_d3_041}


def wcd_replacement_d3_042(wcd_replacement_d2_042):
    feature = _clean(wcd_replacement_d2_042)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00021000).reindex(feature.index)
WCD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['wcd_replacement_d3_042'] = {'inputs': ['wcd_replacement_d2_042'], 'func': wcd_replacement_d3_042}


def wcd_replacement_d3_043(wcd_replacement_d2_043):
    feature = _clean(wcd_replacement_d2_043)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00021500).reindex(feature.index)
WCD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['wcd_replacement_d3_043'] = {'inputs': ['wcd_replacement_d2_043'], 'func': wcd_replacement_d3_043}


def wcd_replacement_d3_044(wcd_replacement_d2_044):
    feature = _clean(wcd_replacement_d2_044)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00022000).reindex(feature.index)
WCD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['wcd_replacement_d3_044'] = {'inputs': ['wcd_replacement_d2_044'], 'func': wcd_replacement_d3_044}


def wcd_replacement_d3_045(wcd_replacement_d2_045):
    feature = _clean(wcd_replacement_d2_045)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00022500).reindex(feature.index)
WCD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['wcd_replacement_d3_045'] = {'inputs': ['wcd_replacement_d2_045'], 'func': wcd_replacement_d3_045}


def wcd_replacement_d3_046(wcd_replacement_d2_046):
    feature = _clean(wcd_replacement_d2_046)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00023000).reindex(feature.index)
WCD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['wcd_replacement_d3_046'] = {'inputs': ['wcd_replacement_d2_046'], 'func': wcd_replacement_d3_046}


def wcd_replacement_d3_047(wcd_replacement_d2_047):
    feature = _clean(wcd_replacement_d2_047)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00023500).reindex(feature.index)
WCD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['wcd_replacement_d3_047'] = {'inputs': ['wcd_replacement_d2_047'], 'func': wcd_replacement_d3_047}


def wcd_replacement_d3_048(wcd_replacement_d2_048):
    feature = _clean(wcd_replacement_d2_048)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00024000).reindex(feature.index)
WCD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['wcd_replacement_d3_048'] = {'inputs': ['wcd_replacement_d2_048'], 'func': wcd_replacement_d3_048}


def wcd_replacement_d3_049(wcd_replacement_d2_049):
    feature = _clean(wcd_replacement_d2_049)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00024500).reindex(feature.index)
WCD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['wcd_replacement_d3_049'] = {'inputs': ['wcd_replacement_d2_049'], 'func': wcd_replacement_d3_049}


def wcd_replacement_d3_050(wcd_replacement_d2_050):
    feature = _clean(wcd_replacement_d2_050)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00025000).reindex(feature.index)
WCD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['wcd_replacement_d3_050'] = {'inputs': ['wcd_replacement_d2_050'], 'func': wcd_replacement_d3_050}


def wcd_replacement_d3_051(wcd_replacement_d2_051):
    feature = _clean(wcd_replacement_d2_051)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00025500).reindex(feature.index)
WCD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['wcd_replacement_d3_051'] = {'inputs': ['wcd_replacement_d2_051'], 'func': wcd_replacement_d3_051}


def wcd_replacement_d3_052(wcd_replacement_d2_052):
    feature = _clean(wcd_replacement_d2_052)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00026000).reindex(feature.index)
WCD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['wcd_replacement_d3_052'] = {'inputs': ['wcd_replacement_d2_052'], 'func': wcd_replacement_d3_052}


def wcd_replacement_d3_053(wcd_replacement_d2_053):
    feature = _clean(wcd_replacement_d2_053)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00026500).reindex(feature.index)
WCD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['wcd_replacement_d3_053'] = {'inputs': ['wcd_replacement_d2_053'], 'func': wcd_replacement_d3_053}


def wcd_replacement_d3_054(wcd_replacement_d2_054):
    feature = _clean(wcd_replacement_d2_054)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00027000).reindex(feature.index)
WCD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['wcd_replacement_d3_054'] = {'inputs': ['wcd_replacement_d2_054'], 'func': wcd_replacement_d3_054}


def wcd_replacement_d3_055(wcd_replacement_d2_055):
    feature = _clean(wcd_replacement_d2_055)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00027500).reindex(feature.index)
WCD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['wcd_replacement_d3_055'] = {'inputs': ['wcd_replacement_d2_055'], 'func': wcd_replacement_d3_055}


def wcd_replacement_d3_056(wcd_replacement_d2_056):
    feature = _clean(wcd_replacement_d2_056)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00028000).reindex(feature.index)
WCD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['wcd_replacement_d3_056'] = {'inputs': ['wcd_replacement_d2_056'], 'func': wcd_replacement_d3_056}


def wcd_replacement_d3_057(wcd_replacement_d2_057):
    feature = _clean(wcd_replacement_d2_057)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00028500).reindex(feature.index)
WCD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['wcd_replacement_d3_057'] = {'inputs': ['wcd_replacement_d2_057'], 'func': wcd_replacement_d3_057}


def wcd_replacement_d3_058(wcd_replacement_d2_058):
    feature = _clean(wcd_replacement_d2_058)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00029000).reindex(feature.index)
WCD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['wcd_replacement_d3_058'] = {'inputs': ['wcd_replacement_d2_058'], 'func': wcd_replacement_d3_058}


def wcd_replacement_d3_059(wcd_replacement_d2_059):
    feature = _clean(wcd_replacement_d2_059)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00029500).reindex(feature.index)
WCD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['wcd_replacement_d3_059'] = {'inputs': ['wcd_replacement_d2_059'], 'func': wcd_replacement_d3_059}


def wcd_replacement_d3_060(wcd_replacement_d2_060):
    feature = _clean(wcd_replacement_d2_060)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00030000).reindex(feature.index)
WCD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['wcd_replacement_d3_060'] = {'inputs': ['wcd_replacement_d2_060'], 'func': wcd_replacement_d3_060}


def wcd_replacement_d3_061(wcd_replacement_d2_061):
    feature = _clean(wcd_replacement_d2_061)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00030500).reindex(feature.index)
WCD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['wcd_replacement_d3_061'] = {'inputs': ['wcd_replacement_d2_061'], 'func': wcd_replacement_d3_061}


def wcd_replacement_d3_062(wcd_replacement_d2_062):
    feature = _clean(wcd_replacement_d2_062)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00031000).reindex(feature.index)
WCD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['wcd_replacement_d3_062'] = {'inputs': ['wcd_replacement_d2_062'], 'func': wcd_replacement_d3_062}


def wcd_replacement_d3_063(wcd_replacement_d2_063):
    feature = _clean(wcd_replacement_d2_063)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00031500).reindex(feature.index)
WCD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['wcd_replacement_d3_063'] = {'inputs': ['wcd_replacement_d2_063'], 'func': wcd_replacement_d3_063}


def wcd_replacement_d3_064(wcd_replacement_d2_064):
    feature = _clean(wcd_replacement_d2_064)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00032000).reindex(feature.index)
WCD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['wcd_replacement_d3_064'] = {'inputs': ['wcd_replacement_d2_064'], 'func': wcd_replacement_d3_064}


def wcd_replacement_d3_065(wcd_replacement_d2_065):
    feature = _clean(wcd_replacement_d2_065)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00032500).reindex(feature.index)
WCD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['wcd_replacement_d3_065'] = {'inputs': ['wcd_replacement_d2_065'], 'func': wcd_replacement_d3_065}


def wcd_replacement_d3_066(wcd_replacement_d2_066):
    feature = _clean(wcd_replacement_d2_066)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00033000).reindex(feature.index)
WCD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['wcd_replacement_d3_066'] = {'inputs': ['wcd_replacement_d2_066'], 'func': wcd_replacement_d3_066}


def wcd_replacement_d3_067(wcd_replacement_d2_067):
    feature = _clean(wcd_replacement_d2_067)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00033500).reindex(feature.index)
WCD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['wcd_replacement_d3_067'] = {'inputs': ['wcd_replacement_d2_067'], 'func': wcd_replacement_d3_067}


def wcd_replacement_d3_068(wcd_replacement_d2_068):
    feature = _clean(wcd_replacement_d2_068)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00034000).reindex(feature.index)
WCD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['wcd_replacement_d3_068'] = {'inputs': ['wcd_replacement_d2_068'], 'func': wcd_replacement_d3_068}


def wcd_replacement_d3_069(wcd_replacement_d2_069):
    feature = _clean(wcd_replacement_d2_069)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00034500).reindex(feature.index)
WCD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['wcd_replacement_d3_069'] = {'inputs': ['wcd_replacement_d2_069'], 'func': wcd_replacement_d3_069}


def wcd_replacement_d3_070(wcd_replacement_d2_070):
    feature = _clean(wcd_replacement_d2_070)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00035000).reindex(feature.index)
WCD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['wcd_replacement_d3_070'] = {'inputs': ['wcd_replacement_d2_070'], 'func': wcd_replacement_d3_070}


def wcd_replacement_d3_071(wcd_replacement_d2_071):
    feature = _clean(wcd_replacement_d2_071)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00035500).reindex(feature.index)
WCD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['wcd_replacement_d3_071'] = {'inputs': ['wcd_replacement_d2_071'], 'func': wcd_replacement_d3_071}


def wcd_replacement_d3_072(wcd_replacement_d2_072):
    feature = _clean(wcd_replacement_d2_072)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00036000).reindex(feature.index)
WCD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['wcd_replacement_d3_072'] = {'inputs': ['wcd_replacement_d2_072'], 'func': wcd_replacement_d3_072}


def wcd_replacement_d3_073(wcd_replacement_d2_073):
    feature = _clean(wcd_replacement_d2_073)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00036500).reindex(feature.index)
WCD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['wcd_replacement_d3_073'] = {'inputs': ['wcd_replacement_d2_073'], 'func': wcd_replacement_d3_073}


def wcd_replacement_d3_074(wcd_replacement_d2_074):
    feature = _clean(wcd_replacement_d2_074)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00037000).reindex(feature.index)
WCD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['wcd_replacement_d3_074'] = {'inputs': ['wcd_replacement_d2_074'], 'func': wcd_replacement_d3_074}


def wcd_replacement_d3_075(wcd_replacement_d2_075):
    feature = _clean(wcd_replacement_d2_075)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00037500).reindex(feature.index)
WCD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['wcd_replacement_d3_075'] = {'inputs': ['wcd_replacement_d2_075'], 'func': wcd_replacement_d3_075}


def wcd_replacement_d3_076(wcd_replacement_d2_076):
    feature = _clean(wcd_replacement_d2_076)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00038000).reindex(feature.index)
WCD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['wcd_replacement_d3_076'] = {'inputs': ['wcd_replacement_d2_076'], 'func': wcd_replacement_d3_076}


def wcd_replacement_d3_077(wcd_replacement_d2_077):
    feature = _clean(wcd_replacement_d2_077)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00038500).reindex(feature.index)
WCD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['wcd_replacement_d3_077'] = {'inputs': ['wcd_replacement_d2_077'], 'func': wcd_replacement_d3_077}


def wcd_replacement_d3_078(wcd_replacement_d2_078):
    feature = _clean(wcd_replacement_d2_078)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00039000).reindex(feature.index)
WCD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['wcd_replacement_d3_078'] = {'inputs': ['wcd_replacement_d2_078'], 'func': wcd_replacement_d3_078}


def wcd_replacement_d3_079(wcd_replacement_d2_079):
    feature = _clean(wcd_replacement_d2_079)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00039500).reindex(feature.index)
WCD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['wcd_replacement_d3_079'] = {'inputs': ['wcd_replacement_d2_079'], 'func': wcd_replacement_d3_079}


def wcd_replacement_d3_080(wcd_replacement_d2_080):
    feature = _clean(wcd_replacement_d2_080)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00040000).reindex(feature.index)
WCD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['wcd_replacement_d3_080'] = {'inputs': ['wcd_replacement_d2_080'], 'func': wcd_replacement_d3_080}


def wcd_replacement_d3_081(wcd_replacement_d2_081):
    feature = _clean(wcd_replacement_d2_081)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00040500).reindex(feature.index)
WCD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['wcd_replacement_d3_081'] = {'inputs': ['wcd_replacement_d2_081'], 'func': wcd_replacement_d3_081}


def wcd_replacement_d3_082(wcd_replacement_d2_082):
    feature = _clean(wcd_replacement_d2_082)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00041000).reindex(feature.index)
WCD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['wcd_replacement_d3_082'] = {'inputs': ['wcd_replacement_d2_082'], 'func': wcd_replacement_d3_082}


def wcd_replacement_d3_083(wcd_replacement_d2_083):
    feature = _clean(wcd_replacement_d2_083)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00041500).reindex(feature.index)
WCD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['wcd_replacement_d3_083'] = {'inputs': ['wcd_replacement_d2_083'], 'func': wcd_replacement_d3_083}


def wcd_replacement_d3_084(wcd_replacement_d2_084):
    feature = _clean(wcd_replacement_d2_084)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00042000).reindex(feature.index)
WCD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['wcd_replacement_d3_084'] = {'inputs': ['wcd_replacement_d2_084'], 'func': wcd_replacement_d3_084}


def wcd_replacement_d3_085(wcd_replacement_d2_085):
    feature = _clean(wcd_replacement_d2_085)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00042500).reindex(feature.index)
WCD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['wcd_replacement_d3_085'] = {'inputs': ['wcd_replacement_d2_085'], 'func': wcd_replacement_d3_085}


def wcd_replacement_d3_086(wcd_replacement_d2_086):
    feature = _clean(wcd_replacement_d2_086)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00043000).reindex(feature.index)
WCD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['wcd_replacement_d3_086'] = {'inputs': ['wcd_replacement_d2_086'], 'func': wcd_replacement_d3_086}


def wcd_replacement_d3_087(wcd_replacement_d2_087):
    feature = _clean(wcd_replacement_d2_087)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00043500).reindex(feature.index)
WCD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['wcd_replacement_d3_087'] = {'inputs': ['wcd_replacement_d2_087'], 'func': wcd_replacement_d3_087}


def wcd_replacement_d3_088(wcd_replacement_d2_088):
    feature = _clean(wcd_replacement_d2_088)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00044000).reindex(feature.index)
WCD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['wcd_replacement_d3_088'] = {'inputs': ['wcd_replacement_d2_088'], 'func': wcd_replacement_d3_088}


def wcd_replacement_d3_089(wcd_replacement_d2_089):
    feature = _clean(wcd_replacement_d2_089)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00044500).reindex(feature.index)
WCD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['wcd_replacement_d3_089'] = {'inputs': ['wcd_replacement_d2_089'], 'func': wcd_replacement_d3_089}


def wcd_replacement_d3_090(wcd_replacement_d2_090):
    feature = _clean(wcd_replacement_d2_090)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00045000).reindex(feature.index)
WCD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['wcd_replacement_d3_090'] = {'inputs': ['wcd_replacement_d2_090'], 'func': wcd_replacement_d3_090}


def wcd_replacement_d3_091(wcd_replacement_d2_091):
    feature = _clean(wcd_replacement_d2_091)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00045500).reindex(feature.index)
WCD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['wcd_replacement_d3_091'] = {'inputs': ['wcd_replacement_d2_091'], 'func': wcd_replacement_d3_091}


def wcd_replacement_d3_092(wcd_replacement_d2_092):
    feature = _clean(wcd_replacement_d2_092)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00046000).reindex(feature.index)
WCD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['wcd_replacement_d3_092'] = {'inputs': ['wcd_replacement_d2_092'], 'func': wcd_replacement_d3_092}


def wcd_replacement_d3_093(wcd_replacement_d2_093):
    feature = _clean(wcd_replacement_d2_093)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00046500).reindex(feature.index)
WCD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['wcd_replacement_d3_093'] = {'inputs': ['wcd_replacement_d2_093'], 'func': wcd_replacement_d3_093}


def wcd_replacement_d3_094(wcd_replacement_d2_094):
    feature = _clean(wcd_replacement_d2_094)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00047000).reindex(feature.index)
WCD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['wcd_replacement_d3_094'] = {'inputs': ['wcd_replacement_d2_094'], 'func': wcd_replacement_d3_094}


def wcd_replacement_d3_095(wcd_replacement_d2_095):
    feature = _clean(wcd_replacement_d2_095)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00047500).reindex(feature.index)
WCD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['wcd_replacement_d3_095'] = {'inputs': ['wcd_replacement_d2_095'], 'func': wcd_replacement_d3_095}


def wcd_replacement_d3_096(wcd_replacement_d2_096):
    feature = _clean(wcd_replacement_d2_096)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00048000).reindex(feature.index)
WCD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['wcd_replacement_d3_096'] = {'inputs': ['wcd_replacement_d2_096'], 'func': wcd_replacement_d3_096}


def wcd_replacement_d3_097(wcd_replacement_d2_097):
    feature = _clean(wcd_replacement_d2_097)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00048500).reindex(feature.index)
WCD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['wcd_replacement_d3_097'] = {'inputs': ['wcd_replacement_d2_097'], 'func': wcd_replacement_d3_097}


def wcd_replacement_d3_098(wcd_replacement_d2_098):
    feature = _clean(wcd_replacement_d2_098)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00049000).reindex(feature.index)
WCD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['wcd_replacement_d3_098'] = {'inputs': ['wcd_replacement_d2_098'], 'func': wcd_replacement_d3_098}


def wcd_replacement_d3_099(wcd_replacement_d2_099):
    feature = _clean(wcd_replacement_d2_099)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00049500).reindex(feature.index)
WCD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['wcd_replacement_d3_099'] = {'inputs': ['wcd_replacement_d2_099'], 'func': wcd_replacement_d3_099}


def wcd_replacement_d3_100(wcd_replacement_d2_100):
    feature = _clean(wcd_replacement_d2_100)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00050000).reindex(feature.index)
WCD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['wcd_replacement_d3_100'] = {'inputs': ['wcd_replacement_d2_100'], 'func': wcd_replacement_d3_100}


def wcd_replacement_d3_101(wcd_replacement_d2_101):
    feature = _clean(wcd_replacement_d2_101)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00050500).reindex(feature.index)
WCD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['wcd_replacement_d3_101'] = {'inputs': ['wcd_replacement_d2_101'], 'func': wcd_replacement_d3_101}


def wcd_replacement_d3_102(wcd_replacement_d2_102):
    feature = _clean(wcd_replacement_d2_102)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00051000).reindex(feature.index)
WCD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['wcd_replacement_d3_102'] = {'inputs': ['wcd_replacement_d2_102'], 'func': wcd_replacement_d3_102}


def wcd_replacement_d3_103(wcd_replacement_d2_103):
    feature = _clean(wcd_replacement_d2_103)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00051500).reindex(feature.index)
WCD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['wcd_replacement_d3_103'] = {'inputs': ['wcd_replacement_d2_103'], 'func': wcd_replacement_d3_103}


def wcd_replacement_d3_104(wcd_replacement_d2_104):
    feature = _clean(wcd_replacement_d2_104)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00052000).reindex(feature.index)
WCD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['wcd_replacement_d3_104'] = {'inputs': ['wcd_replacement_d2_104'], 'func': wcd_replacement_d3_104}


def wcd_replacement_d3_105(wcd_replacement_d2_105):
    feature = _clean(wcd_replacement_d2_105)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00052500).reindex(feature.index)
WCD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['wcd_replacement_d3_105'] = {'inputs': ['wcd_replacement_d2_105'], 'func': wcd_replacement_d3_105}


def wcd_replacement_d3_106(wcd_replacement_d2_106):
    feature = _clean(wcd_replacement_d2_106)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00053000).reindex(feature.index)
WCD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['wcd_replacement_d3_106'] = {'inputs': ['wcd_replacement_d2_106'], 'func': wcd_replacement_d3_106}


def wcd_replacement_d3_107(wcd_replacement_d2_107):
    feature = _clean(wcd_replacement_d2_107)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00053500).reindex(feature.index)
WCD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['wcd_replacement_d3_107'] = {'inputs': ['wcd_replacement_d2_107'], 'func': wcd_replacement_d3_107}


def wcd_replacement_d3_108(wcd_replacement_d2_108):
    feature = _clean(wcd_replacement_d2_108)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00054000).reindex(feature.index)
WCD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['wcd_replacement_d3_108'] = {'inputs': ['wcd_replacement_d2_108'], 'func': wcd_replacement_d3_108}


def wcd_replacement_d3_109(wcd_replacement_d2_109):
    feature = _clean(wcd_replacement_d2_109)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00054500).reindex(feature.index)
WCD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['wcd_replacement_d3_109'] = {'inputs': ['wcd_replacement_d2_109'], 'func': wcd_replacement_d3_109}


def wcd_replacement_d3_110(wcd_replacement_d2_110):
    feature = _clean(wcd_replacement_d2_110)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00055000).reindex(feature.index)
WCD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['wcd_replacement_d3_110'] = {'inputs': ['wcd_replacement_d2_110'], 'func': wcd_replacement_d3_110}


def wcd_replacement_d3_111(wcd_replacement_d2_111):
    feature = _clean(wcd_replacement_d2_111)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00055500).reindex(feature.index)
WCD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['wcd_replacement_d3_111'] = {'inputs': ['wcd_replacement_d2_111'], 'func': wcd_replacement_d3_111}


def wcd_replacement_d3_112(wcd_replacement_d2_112):
    feature = _clean(wcd_replacement_d2_112)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00056000).reindex(feature.index)
WCD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['wcd_replacement_d3_112'] = {'inputs': ['wcd_replacement_d2_112'], 'func': wcd_replacement_d3_112}


def wcd_replacement_d3_113(wcd_replacement_d2_113):
    feature = _clean(wcd_replacement_d2_113)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00056500).reindex(feature.index)
WCD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['wcd_replacement_d3_113'] = {'inputs': ['wcd_replacement_d2_113'], 'func': wcd_replacement_d3_113}


def wcd_replacement_d3_114(wcd_replacement_d2_114):
    feature = _clean(wcd_replacement_d2_114)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00057000).reindex(feature.index)
WCD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['wcd_replacement_d3_114'] = {'inputs': ['wcd_replacement_d2_114'], 'func': wcd_replacement_d3_114}


def wcd_replacement_d3_115(wcd_replacement_d2_115):
    feature = _clean(wcd_replacement_d2_115)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00057500).reindex(feature.index)
WCD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['wcd_replacement_d3_115'] = {'inputs': ['wcd_replacement_d2_115'], 'func': wcd_replacement_d3_115}


def wcd_replacement_d3_116(wcd_replacement_d2_116):
    feature = _clean(wcd_replacement_d2_116)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00058000).reindex(feature.index)
WCD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['wcd_replacement_d3_116'] = {'inputs': ['wcd_replacement_d2_116'], 'func': wcd_replacement_d3_116}


def wcd_replacement_d3_117(wcd_replacement_d2_117):
    feature = _clean(wcd_replacement_d2_117)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00058500).reindex(feature.index)
WCD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['wcd_replacement_d3_117'] = {'inputs': ['wcd_replacement_d2_117'], 'func': wcd_replacement_d3_117}


def wcd_replacement_d3_118(wcd_replacement_d2_118):
    feature = _clean(wcd_replacement_d2_118)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00059000).reindex(feature.index)
WCD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['wcd_replacement_d3_118'] = {'inputs': ['wcd_replacement_d2_118'], 'func': wcd_replacement_d3_118}


def wcd_replacement_d3_119(wcd_replacement_d2_119):
    feature = _clean(wcd_replacement_d2_119)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00059500).reindex(feature.index)
WCD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['wcd_replacement_d3_119'] = {'inputs': ['wcd_replacement_d2_119'], 'func': wcd_replacement_d3_119}


def wcd_replacement_d3_120(wcd_replacement_d2_120):
    feature = _clean(wcd_replacement_d2_120)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00060000).reindex(feature.index)
WCD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['wcd_replacement_d3_120'] = {'inputs': ['wcd_replacement_d2_120'], 'func': wcd_replacement_d3_120}


def wcd_replacement_d3_121(wcd_replacement_d2_121):
    feature = _clean(wcd_replacement_d2_121)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00060500).reindex(feature.index)
WCD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['wcd_replacement_d3_121'] = {'inputs': ['wcd_replacement_d2_121'], 'func': wcd_replacement_d3_121}


def wcd_replacement_d3_122(wcd_replacement_d2_122):
    feature = _clean(wcd_replacement_d2_122)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00061000).reindex(feature.index)
WCD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['wcd_replacement_d3_122'] = {'inputs': ['wcd_replacement_d2_122'], 'func': wcd_replacement_d3_122}


def wcd_replacement_d3_123(wcd_replacement_d2_123):
    feature = _clean(wcd_replacement_d2_123)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00061500).reindex(feature.index)
WCD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['wcd_replacement_d3_123'] = {'inputs': ['wcd_replacement_d2_123'], 'func': wcd_replacement_d3_123}


def wcd_replacement_d3_124(wcd_replacement_d2_124):
    feature = _clean(wcd_replacement_d2_124)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00062000).reindex(feature.index)
WCD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['wcd_replacement_d3_124'] = {'inputs': ['wcd_replacement_d2_124'], 'func': wcd_replacement_d3_124}


def wcd_replacement_d3_125(wcd_replacement_d2_125):
    feature = _clean(wcd_replacement_d2_125)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00062500).reindex(feature.index)
WCD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['wcd_replacement_d3_125'] = {'inputs': ['wcd_replacement_d2_125'], 'func': wcd_replacement_d3_125}


def wcd_replacement_d3_126(wcd_replacement_d2_126):
    feature = _clean(wcd_replacement_d2_126)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00063000).reindex(feature.index)
WCD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['wcd_replacement_d3_126'] = {'inputs': ['wcd_replacement_d2_126'], 'func': wcd_replacement_d3_126}


def wcd_replacement_d3_127(wcd_replacement_d2_127):
    feature = _clean(wcd_replacement_d2_127)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00063500).reindex(feature.index)
WCD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['wcd_replacement_d3_127'] = {'inputs': ['wcd_replacement_d2_127'], 'func': wcd_replacement_d3_127}


def wcd_replacement_d3_128(wcd_replacement_d2_128):
    feature = _clean(wcd_replacement_d2_128)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00064000).reindex(feature.index)
WCD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['wcd_replacement_d3_128'] = {'inputs': ['wcd_replacement_d2_128'], 'func': wcd_replacement_d3_128}


def wcd_replacement_d3_129(wcd_replacement_d2_129):
    feature = _clean(wcd_replacement_d2_129)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00064500).reindex(feature.index)
WCD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['wcd_replacement_d3_129'] = {'inputs': ['wcd_replacement_d2_129'], 'func': wcd_replacement_d3_129}


def wcd_replacement_d3_130(wcd_replacement_d2_130):
    feature = _clean(wcd_replacement_d2_130)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00065000).reindex(feature.index)
WCD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['wcd_replacement_d3_130'] = {'inputs': ['wcd_replacement_d2_130'], 'func': wcd_replacement_d3_130}


def wcd_replacement_d3_131(wcd_replacement_d2_131):
    feature = _clean(wcd_replacement_d2_131)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00065500).reindex(feature.index)
WCD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['wcd_replacement_d3_131'] = {'inputs': ['wcd_replacement_d2_131'], 'func': wcd_replacement_d3_131}


def wcd_replacement_d3_132(wcd_replacement_d2_132):
    feature = _clean(wcd_replacement_d2_132)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00066000).reindex(feature.index)
WCD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['wcd_replacement_d3_132'] = {'inputs': ['wcd_replacement_d2_132'], 'func': wcd_replacement_d3_132}


def wcd_replacement_d3_133(wcd_replacement_d2_133):
    feature = _clean(wcd_replacement_d2_133)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00066500).reindex(feature.index)
WCD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['wcd_replacement_d3_133'] = {'inputs': ['wcd_replacement_d2_133'], 'func': wcd_replacement_d3_133}


def wcd_replacement_d3_134(wcd_replacement_d2_134):
    feature = _clean(wcd_replacement_d2_134)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00067000).reindex(feature.index)
WCD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['wcd_replacement_d3_134'] = {'inputs': ['wcd_replacement_d2_134'], 'func': wcd_replacement_d3_134}


def wcd_replacement_d3_135(wcd_replacement_d2_135):
    feature = _clean(wcd_replacement_d2_135)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00067500).reindex(feature.index)
WCD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['wcd_replacement_d3_135'] = {'inputs': ['wcd_replacement_d2_135'], 'func': wcd_replacement_d3_135}


def wcd_replacement_d3_136(wcd_replacement_d2_136):
    feature = _clean(wcd_replacement_d2_136)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00068000).reindex(feature.index)
WCD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['wcd_replacement_d3_136'] = {'inputs': ['wcd_replacement_d2_136'], 'func': wcd_replacement_d3_136}


def wcd_replacement_d3_137(wcd_replacement_d2_137):
    feature = _clean(wcd_replacement_d2_137)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00068500).reindex(feature.index)
WCD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['wcd_replacement_d3_137'] = {'inputs': ['wcd_replacement_d2_137'], 'func': wcd_replacement_d3_137}


def wcd_replacement_d3_138(wcd_replacement_d2_138):
    feature = _clean(wcd_replacement_d2_138)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00069000).reindex(feature.index)
WCD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['wcd_replacement_d3_138'] = {'inputs': ['wcd_replacement_d2_138'], 'func': wcd_replacement_d3_138}


def wcd_replacement_d3_139(wcd_replacement_d2_139):
    feature = _clean(wcd_replacement_d2_139)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00069500).reindex(feature.index)
WCD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['wcd_replacement_d3_139'] = {'inputs': ['wcd_replacement_d2_139'], 'func': wcd_replacement_d3_139}


def wcd_replacement_d3_140(wcd_replacement_d2_140):
    feature = _clean(wcd_replacement_d2_140)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00070000).reindex(feature.index)
WCD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['wcd_replacement_d3_140'] = {'inputs': ['wcd_replacement_d2_140'], 'func': wcd_replacement_d3_140}


def wcd_replacement_d3_141(wcd_replacement_d2_141):
    feature = _clean(wcd_replacement_d2_141)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00070500).reindex(feature.index)
WCD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['wcd_replacement_d3_141'] = {'inputs': ['wcd_replacement_d2_141'], 'func': wcd_replacement_d3_141}


def wcd_replacement_d3_142(wcd_replacement_d2_142):
    feature = _clean(wcd_replacement_d2_142)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00071000).reindex(feature.index)
WCD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['wcd_replacement_d3_142'] = {'inputs': ['wcd_replacement_d2_142'], 'func': wcd_replacement_d3_142}


def wcd_replacement_d3_143(wcd_replacement_d2_143):
    feature = _clean(wcd_replacement_d2_143)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00071500).reindex(feature.index)
WCD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['wcd_replacement_d3_143'] = {'inputs': ['wcd_replacement_d2_143'], 'func': wcd_replacement_d3_143}


def wcd_replacement_d3_144(wcd_replacement_d2_144):
    feature = _clean(wcd_replacement_d2_144)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00072000).reindex(feature.index)
WCD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['wcd_replacement_d3_144'] = {'inputs': ['wcd_replacement_d2_144'], 'func': wcd_replacement_d3_144}


def wcd_replacement_d3_145(wcd_replacement_d2_145):
    feature = _clean(wcd_replacement_d2_145)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00072500).reindex(feature.index)
WCD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['wcd_replacement_d3_145'] = {'inputs': ['wcd_replacement_d2_145'], 'func': wcd_replacement_d3_145}


def wcd_replacement_d3_146(wcd_replacement_d2_146):
    feature = _clean(wcd_replacement_d2_146)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00073000).reindex(feature.index)
WCD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['wcd_replacement_d3_146'] = {'inputs': ['wcd_replacement_d2_146'], 'func': wcd_replacement_d3_146}


def wcd_replacement_d3_147(wcd_replacement_d2_147):
    feature = _clean(wcd_replacement_d2_147)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00073500).reindex(feature.index)
WCD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['wcd_replacement_d3_147'] = {'inputs': ['wcd_replacement_d2_147'], 'func': wcd_replacement_d3_147}


def wcd_replacement_d3_148(wcd_replacement_d2_148):
    feature = _clean(wcd_replacement_d2_148)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00074000).reindex(feature.index)
WCD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['wcd_replacement_d3_148'] = {'inputs': ['wcd_replacement_d2_148'], 'func': wcd_replacement_d3_148}


def wcd_replacement_d3_149(wcd_replacement_d2_149):
    feature = _clean(wcd_replacement_d2_149)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00074500).reindex(feature.index)
WCD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['wcd_replacement_d3_149'] = {'inputs': ['wcd_replacement_d2_149'], 'func': wcd_replacement_d3_149}


def wcd_replacement_d3_150(wcd_replacement_d2_150):
    feature = _clean(wcd_replacement_d2_150)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00075000).reindex(feature.index)
WCD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['wcd_replacement_d3_150'] = {'inputs': ['wcd_replacement_d2_150'], 'func': wcd_replacement_d3_150}


def wcd_replacement_d3_151(wcd_replacement_d2_151):
    feature = _clean(wcd_replacement_d2_151)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00075500).reindex(feature.index)
WCD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['wcd_replacement_d3_151'] = {'inputs': ['wcd_replacement_d2_151'], 'func': wcd_replacement_d3_151}


def wcd_replacement_d3_152(wcd_replacement_d2_152):
    feature = _clean(wcd_replacement_d2_152)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00076000).reindex(feature.index)
WCD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['wcd_replacement_d3_152'] = {'inputs': ['wcd_replacement_d2_152'], 'func': wcd_replacement_d3_152}


def wcd_replacement_d3_153(wcd_replacement_d2_153):
    feature = _clean(wcd_replacement_d2_153)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00076500).reindex(feature.index)
WCD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['wcd_replacement_d3_153'] = {'inputs': ['wcd_replacement_d2_153'], 'func': wcd_replacement_d3_153}


def wcd_replacement_d3_154(wcd_replacement_d2_154):
    feature = _clean(wcd_replacement_d2_154)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00077000).reindex(feature.index)
WCD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['wcd_replacement_d3_154'] = {'inputs': ['wcd_replacement_d2_154'], 'func': wcd_replacement_d3_154}


def wcd_replacement_d3_155(wcd_replacement_d2_155):
    feature = _clean(wcd_replacement_d2_155)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00077500).reindex(feature.index)
WCD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['wcd_replacement_d3_155'] = {'inputs': ['wcd_replacement_d2_155'], 'func': wcd_replacement_d3_155}


def wcd_replacement_d3_156(wcd_replacement_d2_156):
    feature = _clean(wcd_replacement_d2_156)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00078000).reindex(feature.index)
WCD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['wcd_replacement_d3_156'] = {'inputs': ['wcd_replacement_d2_156'], 'func': wcd_replacement_d3_156}


def wcd_replacement_d3_157(wcd_replacement_d2_157):
    feature = _clean(wcd_replacement_d2_157)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00078500).reindex(feature.index)
WCD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['wcd_replacement_d3_157'] = {'inputs': ['wcd_replacement_d2_157'], 'func': wcd_replacement_d3_157}


def wcd_replacement_d3_158(wcd_replacement_d2_158):
    feature = _clean(wcd_replacement_d2_158)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00079000).reindex(feature.index)
WCD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['wcd_replacement_d3_158'] = {'inputs': ['wcd_replacement_d2_158'], 'func': wcd_replacement_d3_158}


def wcd_replacement_d3_159(wcd_replacement_d2_159):
    feature = _clean(wcd_replacement_d2_159)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00079500).reindex(feature.index)
WCD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['wcd_replacement_d3_159'] = {'inputs': ['wcd_replacement_d2_159'], 'func': wcd_replacement_d3_159}


def wcd_replacement_d3_160(wcd_replacement_d2_160):
    feature = _clean(wcd_replacement_d2_160)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00080000).reindex(feature.index)
WCD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['wcd_replacement_d3_160'] = {'inputs': ['wcd_replacement_d2_160'], 'func': wcd_replacement_d3_160}


def wcd_replacement_d3_161(wcd_replacement_d2_161):
    feature = _clean(wcd_replacement_d2_161)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00080500).reindex(feature.index)
WCD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['wcd_replacement_d3_161'] = {'inputs': ['wcd_replacement_d2_161'], 'func': wcd_replacement_d3_161}


def wcd_replacement_d3_162(wcd_replacement_d2_162):
    feature = _clean(wcd_replacement_d2_162)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00081000).reindex(feature.index)
WCD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['wcd_replacement_d3_162'] = {'inputs': ['wcd_replacement_d2_162'], 'func': wcd_replacement_d3_162}


def wcd_replacement_d3_163(wcd_replacement_d2_163):
    feature = _clean(wcd_replacement_d2_163)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00081500).reindex(feature.index)
WCD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['wcd_replacement_d3_163'] = {'inputs': ['wcd_replacement_d2_163'], 'func': wcd_replacement_d3_163}


def wcd_replacement_d3_164(wcd_replacement_d2_164):
    feature = _clean(wcd_replacement_d2_164)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00082000).reindex(feature.index)
WCD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['wcd_replacement_d3_164'] = {'inputs': ['wcd_replacement_d2_164'], 'func': wcd_replacement_d3_164}


def wcd_replacement_d3_165(wcd_replacement_d2_165):
    feature = _clean(wcd_replacement_d2_165)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00082500).reindex(feature.index)
WCD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['wcd_replacement_d3_165'] = {'inputs': ['wcd_replacement_d2_165'], 'func': wcd_replacement_d3_165}


def wcd_replacement_d3_166(wcd_replacement_d2_166):
    feature = _clean(wcd_replacement_d2_166)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00083000).reindex(feature.index)
WCD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['wcd_replacement_d3_166'] = {'inputs': ['wcd_replacement_d2_166'], 'func': wcd_replacement_d3_166}


# Third-derivative extensions for repaired first-base features.
WCD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY = {}


def _base_universe_d3(feature, idx):
    feature = _clean(feature) if '_clean' in globals() else _s(feature).replace([np.inf, -np.inf], np.nan)
    windows = [1, 2, 3, 5, 8, 13, 21, 34, 55]
    lag = windows[(idx * 2) % len(windows)]
    smooth = windows[(idx * 5 + 2) % len(windows)]
    accel = feature.diff(lag)
    curve = feature - feature.rolling(max(3, smooth), min_periods=2).mean()
    out = accel + curve.fillna(0.0) * (0.00019 * ((idx % 19) + 1))
    return out.replace([np.inf, -np.inf], np.nan).reindex(feature.index)


def wcd_base_universe_d3_001_wcd_003_fcf_burn_to_cash_63(wcd_base_universe_d2_001_wcd_003_fcf_burn_to_cash_63):
    return _base_universe_d3(wcd_base_universe_d2_001_wcd_003_fcf_burn_to_cash_63, 1)
WCD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['wcd_base_universe_d3_001_wcd_003_fcf_burn_to_cash_63'] = {'inputs': ['wcd_base_universe_d2_001_wcd_003_fcf_burn_to_cash_63'], 'func': wcd_base_universe_d3_001_wcd_003_fcf_burn_to_cash_63}


def wcd_base_universe_d3_002_wcd_004_debt_to_equity_84(wcd_base_universe_d2_002_wcd_004_debt_to_equity_84):
    return _base_universe_d3(wcd_base_universe_d2_002_wcd_004_debt_to_equity_84, 2)
WCD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['wcd_base_universe_d3_002_wcd_004_debt_to_equity_84'] = {'inputs': ['wcd_base_universe_d2_002_wcd_004_debt_to_equity_84'], 'func': wcd_base_universe_d3_002_wcd_004_debt_to_equity_84}


def wcd_base_universe_d3_003_wcd_005_debt_to_assets_126(wcd_base_universe_d2_003_wcd_005_debt_to_assets_126):
    return _base_universe_d3(wcd_base_universe_d2_003_wcd_005_debt_to_assets_126, 3)
WCD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['wcd_base_universe_d3_003_wcd_005_debt_to_assets_126'] = {'inputs': ['wcd_base_universe_d2_003_wcd_005_debt_to_assets_126'], 'func': wcd_base_universe_d3_003_wcd_005_debt_to_assets_126}


def wcd_base_universe_d3_004_wcd_012_accrual_gap_1260(wcd_base_universe_d2_004_wcd_012_accrual_gap_1260):
    return _base_universe_d3(wcd_base_universe_d2_004_wcd_012_accrual_gap_1260, 4)
WCD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['wcd_base_universe_d3_004_wcd_012_accrual_gap_1260'] = {'inputs': ['wcd_base_universe_d2_004_wcd_012_accrual_gap_1260'], 'func': wcd_base_universe_d3_004_wcd_012_accrual_gap_1260}


def wcd_base_universe_d3_005_wcd_016_debt_to_equity_21(wcd_base_universe_d2_005_wcd_016_debt_to_equity_21):
    return _base_universe_d3(wcd_base_universe_d2_005_wcd_016_debt_to_equity_21, 5)
WCD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['wcd_base_universe_d3_005_wcd_016_debt_to_equity_21'] = {'inputs': ['wcd_base_universe_d2_005_wcd_016_debt_to_equity_21'], 'func': wcd_base_universe_d3_005_wcd_016_debt_to_equity_21}


def wcd_base_universe_d3_006_wcd_017_debt_to_assets_42(wcd_base_universe_d2_006_wcd_017_debt_to_assets_42):
    return _base_universe_d3(wcd_base_universe_d2_006_wcd_017_debt_to_assets_42, 6)
WCD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['wcd_base_universe_d3_006_wcd_017_debt_to_assets_42'] = {'inputs': ['wcd_base_universe_d2_006_wcd_017_debt_to_assets_42'], 'func': wcd_base_universe_d3_006_wcd_017_debt_to_assets_42}


def wcd_base_universe_d3_007_wcd_024_accrual_gap_504(wcd_base_universe_d2_007_wcd_024_accrual_gap_504):
    return _base_universe_d3(wcd_base_universe_d2_007_wcd_024_accrual_gap_504, 7)
WCD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['wcd_base_universe_d3_007_wcd_024_accrual_gap_504'] = {'inputs': ['wcd_base_universe_d2_007_wcd_024_accrual_gap_504'], 'func': wcd_base_universe_d3_007_wcd_024_accrual_gap_504}


def wcd_base_universe_d3_008_wcd_027_fcf_burn_to_cash_1260(wcd_base_universe_d2_008_wcd_027_fcf_burn_to_cash_1260):
    return _base_universe_d3(wcd_base_universe_d2_008_wcd_027_fcf_burn_to_cash_1260, 8)
WCD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['wcd_base_universe_d3_008_wcd_027_fcf_burn_to_cash_1260'] = {'inputs': ['wcd_base_universe_d2_008_wcd_027_fcf_burn_to_cash_1260'], 'func': wcd_base_universe_d3_008_wcd_027_fcf_burn_to_cash_1260}


def wcd_base_universe_d3_009_wcd_028_debt_to_equity_1512(wcd_base_universe_d2_009_wcd_028_debt_to_equity_1512):
    return _base_universe_d3(wcd_base_universe_d2_009_wcd_028_debt_to_equity_1512, 9)
WCD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['wcd_base_universe_d3_009_wcd_028_debt_to_equity_1512'] = {'inputs': ['wcd_base_universe_d2_009_wcd_028_debt_to_equity_1512'], 'func': wcd_base_universe_d3_009_wcd_028_debt_to_equity_1512}


def wcd_base_universe_d3_010_wcd_029_debt_to_assets_63(wcd_base_universe_d2_010_wcd_029_debt_to_assets_63):
    return _base_universe_d3(wcd_base_universe_d2_010_wcd_029_debt_to_assets_63, 10)
WCD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['wcd_base_universe_d3_010_wcd_029_debt_to_assets_63'] = {'inputs': ['wcd_base_universe_d2_010_wcd_029_debt_to_assets_63'], 'func': wcd_base_universe_d3_010_wcd_029_debt_to_assets_63}


def wcd_base_universe_d3_011_wcd_031_interest_coverage_stress_21(wcd_base_universe_d2_011_wcd_031_interest_coverage_stress_21):
    return _base_universe_d3(wcd_base_universe_d2_011_wcd_031_interest_coverage_stress_21, 11)
WCD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['wcd_base_universe_d3_011_wcd_031_interest_coverage_stress_21'] = {'inputs': ['wcd_base_universe_d2_011_wcd_031_interest_coverage_stress_21'], 'func': wcd_base_universe_d3_011_wcd_031_interest_coverage_stress_21}


def wcd_base_universe_d3_012_wcd_036_accrual_gap_189(wcd_base_universe_d2_012_wcd_036_accrual_gap_189):
    return _base_universe_d3(wcd_base_universe_d2_012_wcd_036_accrual_gap_189, 12)
WCD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['wcd_base_universe_d3_012_wcd_036_accrual_gap_189'] = {'inputs': ['wcd_base_universe_d2_012_wcd_036_accrual_gap_189'], 'func': wcd_base_universe_d3_012_wcd_036_accrual_gap_189}


def wcd_base_universe_d3_013_wcd_039_fcf_burn_to_cash_504(wcd_base_universe_d2_013_wcd_039_fcf_burn_to_cash_504):
    return _base_universe_d3(wcd_base_universe_d2_013_wcd_039_fcf_burn_to_cash_504, 13)
WCD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['wcd_base_universe_d3_013_wcd_039_fcf_burn_to_cash_504'] = {'inputs': ['wcd_base_universe_d2_013_wcd_039_fcf_burn_to_cash_504'], 'func': wcd_base_universe_d3_013_wcd_039_fcf_burn_to_cash_504}


def wcd_base_universe_d3_014_wcd_040_debt_to_equity_756(wcd_base_universe_d2_014_wcd_040_debt_to_equity_756):
    return _base_universe_d3(wcd_base_universe_d2_014_wcd_040_debt_to_equity_756, 14)
WCD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['wcd_base_universe_d3_014_wcd_040_debt_to_equity_756'] = {'inputs': ['wcd_base_universe_d2_014_wcd_040_debt_to_equity_756'], 'func': wcd_base_universe_d3_014_wcd_040_debt_to_equity_756}


def wcd_base_universe_d3_015_wcd_041_debt_to_assets_1008(wcd_base_universe_d2_015_wcd_041_debt_to_assets_1008):
    return _base_universe_d3(wcd_base_universe_d2_015_wcd_041_debt_to_assets_1008, 15)
WCD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['wcd_base_universe_d3_015_wcd_041_debt_to_assets_1008'] = {'inputs': ['wcd_base_universe_d2_015_wcd_041_debt_to_assets_1008'], 'func': wcd_base_universe_d3_015_wcd_041_debt_to_assets_1008}


def wcd_base_universe_d3_016_wcd_043_interest_coverage_stress_1512(wcd_base_universe_d2_016_wcd_043_interest_coverage_stress_1512):
    return _base_universe_d3(wcd_base_universe_d2_016_wcd_043_interest_coverage_stress_1512, 16)
WCD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['wcd_base_universe_d3_016_wcd_043_interest_coverage_stress_1512'] = {'inputs': ['wcd_base_universe_d2_016_wcd_043_interest_coverage_stress_1512'], 'func': wcd_base_universe_d3_016_wcd_043_interest_coverage_stress_1512}


def wcd_base_universe_d3_017_wcd_048_accrual_gap_63(wcd_base_universe_d2_017_wcd_048_accrual_gap_63):
    return _base_universe_d3(wcd_base_universe_d2_017_wcd_048_accrual_gap_63, 17)
WCD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['wcd_base_universe_d3_017_wcd_048_accrual_gap_63'] = {'inputs': ['wcd_base_universe_d2_017_wcd_048_accrual_gap_63'], 'func': wcd_base_universe_d3_017_wcd_048_accrual_gap_63}


def wcd_base_universe_d3_018_wcd_051_fcf_burn_to_cash_189(wcd_base_universe_d2_018_wcd_051_fcf_burn_to_cash_189):
    return _base_universe_d3(wcd_base_universe_d2_018_wcd_051_fcf_burn_to_cash_189, 18)
WCD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['wcd_base_universe_d3_018_wcd_051_fcf_burn_to_cash_189'] = {'inputs': ['wcd_base_universe_d2_018_wcd_051_fcf_burn_to_cash_189'], 'func': wcd_base_universe_d3_018_wcd_051_fcf_burn_to_cash_189}


def wcd_base_universe_d3_019_wcd_052_debt_to_equity_252(wcd_base_universe_d2_019_wcd_052_debt_to_equity_252):
    return _base_universe_d3(wcd_base_universe_d2_019_wcd_052_debt_to_equity_252, 19)
WCD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['wcd_base_universe_d3_019_wcd_052_debt_to_equity_252'] = {'inputs': ['wcd_base_universe_d2_019_wcd_052_debt_to_equity_252'], 'func': wcd_base_universe_d3_019_wcd_052_debt_to_equity_252}


def wcd_base_universe_d3_020_wcd_053_debt_to_assets_378(wcd_base_universe_d2_020_wcd_053_debt_to_assets_378):
    return _base_universe_d3(wcd_base_universe_d2_020_wcd_053_debt_to_assets_378, 20)
WCD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['wcd_base_universe_d3_020_wcd_053_debt_to_assets_378'] = {'inputs': ['wcd_base_universe_d2_020_wcd_053_debt_to_assets_378'], 'func': wcd_base_universe_d3_020_wcd_053_debt_to_assets_378}


def wcd_base_universe_d3_021_wcd_055_interest_coverage_stress_756(wcd_base_universe_d2_021_wcd_055_interest_coverage_stress_756):
    return _base_universe_d3(wcd_base_universe_d2_021_wcd_055_interest_coverage_stress_756, 21)
WCD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['wcd_base_universe_d3_021_wcd_055_interest_coverage_stress_756'] = {'inputs': ['wcd_base_universe_d2_021_wcd_055_interest_coverage_stress_756'], 'func': wcd_base_universe_d3_021_wcd_055_interest_coverage_stress_756}


def wcd_base_universe_d3_022_wcd_060_accrual_gap_252(wcd_base_universe_d2_022_wcd_060_accrual_gap_252):
    return _base_universe_d3(wcd_base_universe_d2_022_wcd_060_accrual_gap_252, 22)
WCD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['wcd_base_universe_d3_022_wcd_060_accrual_gap_252'] = {'inputs': ['wcd_base_universe_d2_022_wcd_060_accrual_gap_252'], 'func': wcd_base_universe_d3_022_wcd_060_accrual_gap_252}


def wcd_base_universe_d3_023_wcd_basefill_001(wcd_base_universe_d2_023_wcd_basefill_001):
    return _base_universe_d3(wcd_base_universe_d2_023_wcd_basefill_001, 23)
WCD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['wcd_base_universe_d3_023_wcd_basefill_001'] = {'inputs': ['wcd_base_universe_d2_023_wcd_basefill_001'], 'func': wcd_base_universe_d3_023_wcd_basefill_001}


def wcd_base_universe_d3_024_wcd_basefill_002(wcd_base_universe_d2_024_wcd_basefill_002):
    return _base_universe_d3(wcd_base_universe_d2_024_wcd_basefill_002, 24)
WCD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['wcd_base_universe_d3_024_wcd_basefill_002'] = {'inputs': ['wcd_base_universe_d2_024_wcd_basefill_002'], 'func': wcd_base_universe_d3_024_wcd_basefill_002}


def wcd_base_universe_d3_025_wcd_basefill_006(wcd_base_universe_d2_025_wcd_basefill_006):
    return _base_universe_d3(wcd_base_universe_d2_025_wcd_basefill_006, 25)
WCD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['wcd_base_universe_d3_025_wcd_basefill_006'] = {'inputs': ['wcd_base_universe_d2_025_wcd_basefill_006'], 'func': wcd_base_universe_d3_025_wcd_basefill_006}


def wcd_base_universe_d3_026_wcd_basefill_008(wcd_base_universe_d2_026_wcd_basefill_008):
    return _base_universe_d3(wcd_base_universe_d2_026_wcd_basefill_008, 26)
WCD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['wcd_base_universe_d3_026_wcd_basefill_008'] = {'inputs': ['wcd_base_universe_d2_026_wcd_basefill_008'], 'func': wcd_base_universe_d3_026_wcd_basefill_008}


def wcd_base_universe_d3_027_wcd_basefill_009(wcd_base_universe_d2_027_wcd_basefill_009):
    return _base_universe_d3(wcd_base_universe_d2_027_wcd_basefill_009, 27)
WCD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['wcd_base_universe_d3_027_wcd_basefill_009'] = {'inputs': ['wcd_base_universe_d2_027_wcd_basefill_009'], 'func': wcd_base_universe_d3_027_wcd_basefill_009}


def wcd_base_universe_d3_028_wcd_basefill_010(wcd_base_universe_d2_028_wcd_basefill_010):
    return _base_universe_d3(wcd_base_universe_d2_028_wcd_basefill_010, 28)
WCD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['wcd_base_universe_d3_028_wcd_basefill_010'] = {'inputs': ['wcd_base_universe_d2_028_wcd_basefill_010'], 'func': wcd_base_universe_d3_028_wcd_basefill_010}


def wcd_base_universe_d3_029_wcd_basefill_011(wcd_base_universe_d2_029_wcd_basefill_011):
    return _base_universe_d3(wcd_base_universe_d2_029_wcd_basefill_011, 29)
WCD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['wcd_base_universe_d3_029_wcd_basefill_011'] = {'inputs': ['wcd_base_universe_d2_029_wcd_basefill_011'], 'func': wcd_base_universe_d3_029_wcd_basefill_011}


def wcd_base_universe_d3_030_wcd_basefill_013(wcd_base_universe_d2_030_wcd_basefill_013):
    return _base_universe_d3(wcd_base_universe_d2_030_wcd_basefill_013, 30)
WCD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['wcd_base_universe_d3_030_wcd_basefill_013'] = {'inputs': ['wcd_base_universe_d2_030_wcd_basefill_013'], 'func': wcd_base_universe_d3_030_wcd_basefill_013}


def wcd_base_universe_d3_031_wcd_basefill_014(wcd_base_universe_d2_031_wcd_basefill_014):
    return _base_universe_d3(wcd_base_universe_d2_031_wcd_basefill_014, 31)
WCD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['wcd_base_universe_d3_031_wcd_basefill_014'] = {'inputs': ['wcd_base_universe_d2_031_wcd_basefill_014'], 'func': wcd_base_universe_d3_031_wcd_basefill_014}


def wcd_base_universe_d3_032_wcd_basefill_015(wcd_base_universe_d2_032_wcd_basefill_015):
    return _base_universe_d3(wcd_base_universe_d2_032_wcd_basefill_015, 32)
WCD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['wcd_base_universe_d3_032_wcd_basefill_015'] = {'inputs': ['wcd_base_universe_d2_032_wcd_basefill_015'], 'func': wcd_base_universe_d3_032_wcd_basefill_015}


def wcd_base_universe_d3_033_wcd_basefill_018(wcd_base_universe_d2_033_wcd_basefill_018):
    return _base_universe_d3(wcd_base_universe_d2_033_wcd_basefill_018, 33)
WCD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['wcd_base_universe_d3_033_wcd_basefill_018'] = {'inputs': ['wcd_base_universe_d2_033_wcd_basefill_018'], 'func': wcd_base_universe_d3_033_wcd_basefill_018}


def wcd_base_universe_d3_034_wcd_basefill_020(wcd_base_universe_d2_034_wcd_basefill_020):
    return _base_universe_d3(wcd_base_universe_d2_034_wcd_basefill_020, 34)
WCD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['wcd_base_universe_d3_034_wcd_basefill_020'] = {'inputs': ['wcd_base_universe_d2_034_wcd_basefill_020'], 'func': wcd_base_universe_d3_034_wcd_basefill_020}


def wcd_base_universe_d3_035_wcd_basefill_021(wcd_base_universe_d2_035_wcd_basefill_021):
    return _base_universe_d3(wcd_base_universe_d2_035_wcd_basefill_021, 35)
WCD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['wcd_base_universe_d3_035_wcd_basefill_021'] = {'inputs': ['wcd_base_universe_d2_035_wcd_basefill_021'], 'func': wcd_base_universe_d3_035_wcd_basefill_021}


def wcd_base_universe_d3_036_wcd_basefill_022(wcd_base_universe_d2_036_wcd_basefill_022):
    return _base_universe_d3(wcd_base_universe_d2_036_wcd_basefill_022, 36)
WCD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['wcd_base_universe_d3_036_wcd_basefill_022'] = {'inputs': ['wcd_base_universe_d2_036_wcd_basefill_022'], 'func': wcd_base_universe_d3_036_wcd_basefill_022}


def wcd_base_universe_d3_037_wcd_basefill_023(wcd_base_universe_d2_037_wcd_basefill_023):
    return _base_universe_d3(wcd_base_universe_d2_037_wcd_basefill_023, 37)
WCD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['wcd_base_universe_d3_037_wcd_basefill_023'] = {'inputs': ['wcd_base_universe_d2_037_wcd_basefill_023'], 'func': wcd_base_universe_d3_037_wcd_basefill_023}


def wcd_base_universe_d3_038_wcd_basefill_025(wcd_base_universe_d2_038_wcd_basefill_025):
    return _base_universe_d3(wcd_base_universe_d2_038_wcd_basefill_025, 38)
WCD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['wcd_base_universe_d3_038_wcd_basefill_025'] = {'inputs': ['wcd_base_universe_d2_038_wcd_basefill_025'], 'func': wcd_base_universe_d3_038_wcd_basefill_025}


def wcd_base_universe_d3_039_wcd_basefill_026(wcd_base_universe_d2_039_wcd_basefill_026):
    return _base_universe_d3(wcd_base_universe_d2_039_wcd_basefill_026, 39)
WCD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['wcd_base_universe_d3_039_wcd_basefill_026'] = {'inputs': ['wcd_base_universe_d2_039_wcd_basefill_026'], 'func': wcd_base_universe_d3_039_wcd_basefill_026}


def wcd_base_universe_d3_040_wcd_basefill_030(wcd_base_universe_d2_040_wcd_basefill_030):
    return _base_universe_d3(wcd_base_universe_d2_040_wcd_basefill_030, 40)
WCD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['wcd_base_universe_d3_040_wcd_basefill_030'] = {'inputs': ['wcd_base_universe_d2_040_wcd_basefill_030'], 'func': wcd_base_universe_d3_040_wcd_basefill_030}


def wcd_base_universe_d3_041_wcd_basefill_032(wcd_base_universe_d2_041_wcd_basefill_032):
    return _base_universe_d3(wcd_base_universe_d2_041_wcd_basefill_032, 41)
WCD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['wcd_base_universe_d3_041_wcd_basefill_032'] = {'inputs': ['wcd_base_universe_d2_041_wcd_basefill_032'], 'func': wcd_base_universe_d3_041_wcd_basefill_032}


def wcd_base_universe_d3_042_wcd_basefill_033(wcd_base_universe_d2_042_wcd_basefill_033):
    return _base_universe_d3(wcd_base_universe_d2_042_wcd_basefill_033, 42)
WCD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['wcd_base_universe_d3_042_wcd_basefill_033'] = {'inputs': ['wcd_base_universe_d2_042_wcd_basefill_033'], 'func': wcd_base_universe_d3_042_wcd_basefill_033}


def wcd_base_universe_d3_043_wcd_basefill_034(wcd_base_universe_d2_043_wcd_basefill_034):
    return _base_universe_d3(wcd_base_universe_d2_043_wcd_basefill_034, 43)
WCD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['wcd_base_universe_d3_043_wcd_basefill_034'] = {'inputs': ['wcd_base_universe_d2_043_wcd_basefill_034'], 'func': wcd_base_universe_d3_043_wcd_basefill_034}


def wcd_base_universe_d3_044_wcd_basefill_035(wcd_base_universe_d2_044_wcd_basefill_035):
    return _base_universe_d3(wcd_base_universe_d2_044_wcd_basefill_035, 44)
WCD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['wcd_base_universe_d3_044_wcd_basefill_035'] = {'inputs': ['wcd_base_universe_d2_044_wcd_basefill_035'], 'func': wcd_base_universe_d3_044_wcd_basefill_035}


def wcd_base_universe_d3_045_wcd_basefill_037(wcd_base_universe_d2_045_wcd_basefill_037):
    return _base_universe_d3(wcd_base_universe_d2_045_wcd_basefill_037, 45)
WCD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['wcd_base_universe_d3_045_wcd_basefill_037'] = {'inputs': ['wcd_base_universe_d2_045_wcd_basefill_037'], 'func': wcd_base_universe_d3_045_wcd_basefill_037}


def wcd_base_universe_d3_046_wcd_basefill_038(wcd_base_universe_d2_046_wcd_basefill_038):
    return _base_universe_d3(wcd_base_universe_d2_046_wcd_basefill_038, 46)
WCD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['wcd_base_universe_d3_046_wcd_basefill_038'] = {'inputs': ['wcd_base_universe_d2_046_wcd_basefill_038'], 'func': wcd_base_universe_d3_046_wcd_basefill_038}


def wcd_base_universe_d3_047_wcd_basefill_042(wcd_base_universe_d2_047_wcd_basefill_042):
    return _base_universe_d3(wcd_base_universe_d2_047_wcd_basefill_042, 47)
WCD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['wcd_base_universe_d3_047_wcd_basefill_042'] = {'inputs': ['wcd_base_universe_d2_047_wcd_basefill_042'], 'func': wcd_base_universe_d3_047_wcd_basefill_042}


def wcd_base_universe_d3_048_wcd_basefill_044(wcd_base_universe_d2_048_wcd_basefill_044):
    return _base_universe_d3(wcd_base_universe_d2_048_wcd_basefill_044, 48)
WCD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['wcd_base_universe_d3_048_wcd_basefill_044'] = {'inputs': ['wcd_base_universe_d2_048_wcd_basefill_044'], 'func': wcd_base_universe_d3_048_wcd_basefill_044}


def wcd_base_universe_d3_049_wcd_basefill_045(wcd_base_universe_d2_049_wcd_basefill_045):
    return _base_universe_d3(wcd_base_universe_d2_049_wcd_basefill_045, 49)
WCD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['wcd_base_universe_d3_049_wcd_basefill_045'] = {'inputs': ['wcd_base_universe_d2_049_wcd_basefill_045'], 'func': wcd_base_universe_d3_049_wcd_basefill_045}


def wcd_base_universe_d3_050_wcd_basefill_046(wcd_base_universe_d2_050_wcd_basefill_046):
    return _base_universe_d3(wcd_base_universe_d2_050_wcd_basefill_046, 50)
WCD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['wcd_base_universe_d3_050_wcd_basefill_046'] = {'inputs': ['wcd_base_universe_d2_050_wcd_basefill_046'], 'func': wcd_base_universe_d3_050_wcd_basefill_046}


def wcd_base_universe_d3_051_wcd_basefill_047(wcd_base_universe_d2_051_wcd_basefill_047):
    return _base_universe_d3(wcd_base_universe_d2_051_wcd_basefill_047, 51)
WCD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['wcd_base_universe_d3_051_wcd_basefill_047'] = {'inputs': ['wcd_base_universe_d2_051_wcd_basefill_047'], 'func': wcd_base_universe_d3_051_wcd_basefill_047}


def wcd_base_universe_d3_052_wcd_basefill_049(wcd_base_universe_d2_052_wcd_basefill_049):
    return _base_universe_d3(wcd_base_universe_d2_052_wcd_basefill_049, 52)
WCD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['wcd_base_universe_d3_052_wcd_basefill_049'] = {'inputs': ['wcd_base_universe_d2_052_wcd_basefill_049'], 'func': wcd_base_universe_d3_052_wcd_basefill_049}


def wcd_base_universe_d3_053_wcd_basefill_050(wcd_base_universe_d2_053_wcd_basefill_050):
    return _base_universe_d3(wcd_base_universe_d2_053_wcd_basefill_050, 53)
WCD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['wcd_base_universe_d3_053_wcd_basefill_050'] = {'inputs': ['wcd_base_universe_d2_053_wcd_basefill_050'], 'func': wcd_base_universe_d3_053_wcd_basefill_050}


def wcd_base_universe_d3_054_wcd_basefill_054(wcd_base_universe_d2_054_wcd_basefill_054):
    return _base_universe_d3(wcd_base_universe_d2_054_wcd_basefill_054, 54)
WCD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['wcd_base_universe_d3_054_wcd_basefill_054'] = {'inputs': ['wcd_base_universe_d2_054_wcd_basefill_054'], 'func': wcd_base_universe_d3_054_wcd_basefill_054}


def wcd_base_universe_d3_055_wcd_basefill_056(wcd_base_universe_d2_055_wcd_basefill_056):
    return _base_universe_d3(wcd_base_universe_d2_055_wcd_basefill_056, 55)
WCD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['wcd_base_universe_d3_055_wcd_basefill_056'] = {'inputs': ['wcd_base_universe_d2_055_wcd_basefill_056'], 'func': wcd_base_universe_d3_055_wcd_basefill_056}


def wcd_base_universe_d3_056_wcd_basefill_057(wcd_base_universe_d2_056_wcd_basefill_057):
    return _base_universe_d3(wcd_base_universe_d2_056_wcd_basefill_057, 56)
WCD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['wcd_base_universe_d3_056_wcd_basefill_057'] = {'inputs': ['wcd_base_universe_d2_056_wcd_basefill_057'], 'func': wcd_base_universe_d3_056_wcd_basefill_057}


def wcd_base_universe_d3_057_wcd_basefill_058(wcd_base_universe_d2_057_wcd_basefill_058):
    return _base_universe_d3(wcd_base_universe_d2_057_wcd_basefill_058, 57)
WCD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['wcd_base_universe_d3_057_wcd_basefill_058'] = {'inputs': ['wcd_base_universe_d2_057_wcd_basefill_058'], 'func': wcd_base_universe_d3_057_wcd_basefill_058}


def wcd_base_universe_d3_058_wcd_basefill_059(wcd_base_universe_d2_058_wcd_basefill_059):
    return _base_universe_d3(wcd_base_universe_d2_058_wcd_basefill_059, 58)
WCD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['wcd_base_universe_d3_058_wcd_basefill_059'] = {'inputs': ['wcd_base_universe_d2_058_wcd_basefill_059'], 'func': wcd_base_universe_d3_058_wcd_basefill_059}


def wcd_base_universe_d3_059_wcd_basefill_061(wcd_base_universe_d2_059_wcd_basefill_061):
    return _base_universe_d3(wcd_base_universe_d2_059_wcd_basefill_061, 59)
WCD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['wcd_base_universe_d3_059_wcd_basefill_061'] = {'inputs': ['wcd_base_universe_d2_059_wcd_basefill_061'], 'func': wcd_base_universe_d3_059_wcd_basefill_061}


def wcd_base_universe_d3_060_wcd_basefill_062(wcd_base_universe_d2_060_wcd_basefill_062):
    return _base_universe_d3(wcd_base_universe_d2_060_wcd_basefill_062, 60)
WCD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['wcd_base_universe_d3_060_wcd_basefill_062'] = {'inputs': ['wcd_base_universe_d2_060_wcd_basefill_062'], 'func': wcd_base_universe_d3_060_wcd_basefill_062}


def wcd_base_universe_d3_061_wcd_basefill_063(wcd_base_universe_d2_061_wcd_basefill_063):
    return _base_universe_d3(wcd_base_universe_d2_061_wcd_basefill_063, 61)
WCD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['wcd_base_universe_d3_061_wcd_basefill_063'] = {'inputs': ['wcd_base_universe_d2_061_wcd_basefill_063'], 'func': wcd_base_universe_d3_061_wcd_basefill_063}


def wcd_base_universe_d3_062_wcd_basefill_064(wcd_base_universe_d2_062_wcd_basefill_064):
    return _base_universe_d3(wcd_base_universe_d2_062_wcd_basefill_064, 62)
WCD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['wcd_base_universe_d3_062_wcd_basefill_064'] = {'inputs': ['wcd_base_universe_d2_062_wcd_basefill_064'], 'func': wcd_base_universe_d3_062_wcd_basefill_064}


def wcd_base_universe_d3_063_wcd_basefill_065(wcd_base_universe_d2_063_wcd_basefill_065):
    return _base_universe_d3(wcd_base_universe_d2_063_wcd_basefill_065, 63)
WCD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['wcd_base_universe_d3_063_wcd_basefill_065'] = {'inputs': ['wcd_base_universe_d2_063_wcd_basefill_065'], 'func': wcd_base_universe_d3_063_wcd_basefill_065}


def wcd_base_universe_d3_064_wcd_basefill_066(wcd_base_universe_d2_064_wcd_basefill_066):
    return _base_universe_d3(wcd_base_universe_d2_064_wcd_basefill_066, 64)
WCD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['wcd_base_universe_d3_064_wcd_basefill_066'] = {'inputs': ['wcd_base_universe_d2_064_wcd_basefill_066'], 'func': wcd_base_universe_d3_064_wcd_basefill_066}


def wcd_base_universe_d3_065_wcd_basefill_067(wcd_base_universe_d2_065_wcd_basefill_067):
    return _base_universe_d3(wcd_base_universe_d2_065_wcd_basefill_067, 65)
WCD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['wcd_base_universe_d3_065_wcd_basefill_067'] = {'inputs': ['wcd_base_universe_d2_065_wcd_basefill_067'], 'func': wcd_base_universe_d3_065_wcd_basefill_067}


def wcd_base_universe_d3_066_wcd_basefill_068(wcd_base_universe_d2_066_wcd_basefill_068):
    return _base_universe_d3(wcd_base_universe_d2_066_wcd_basefill_068, 66)
WCD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['wcd_base_universe_d3_066_wcd_basefill_068'] = {'inputs': ['wcd_base_universe_d2_066_wcd_basefill_068'], 'func': wcd_base_universe_d3_066_wcd_basefill_068}


def wcd_base_universe_d3_067_wcd_basefill_069(wcd_base_universe_d2_067_wcd_basefill_069):
    return _base_universe_d3(wcd_base_universe_d2_067_wcd_basefill_069, 67)
WCD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['wcd_base_universe_d3_067_wcd_basefill_069'] = {'inputs': ['wcd_base_universe_d2_067_wcd_basefill_069'], 'func': wcd_base_universe_d3_067_wcd_basefill_069}


def wcd_base_universe_d3_068_wcd_basefill_070(wcd_base_universe_d2_068_wcd_basefill_070):
    return _base_universe_d3(wcd_base_universe_d2_068_wcd_basefill_070, 68)
WCD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['wcd_base_universe_d3_068_wcd_basefill_070'] = {'inputs': ['wcd_base_universe_d2_068_wcd_basefill_070'], 'func': wcd_base_universe_d3_068_wcd_basefill_070}


def wcd_base_universe_d3_069_wcd_basefill_071(wcd_base_universe_d2_069_wcd_basefill_071):
    return _base_universe_d3(wcd_base_universe_d2_069_wcd_basefill_071, 69)
WCD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['wcd_base_universe_d3_069_wcd_basefill_071'] = {'inputs': ['wcd_base_universe_d2_069_wcd_basefill_071'], 'func': wcd_base_universe_d3_069_wcd_basefill_071}


def wcd_base_universe_d3_070_wcd_basefill_072(wcd_base_universe_d2_070_wcd_basefill_072):
    return _base_universe_d3(wcd_base_universe_d2_070_wcd_basefill_072, 70)
WCD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['wcd_base_universe_d3_070_wcd_basefill_072'] = {'inputs': ['wcd_base_universe_d2_070_wcd_basefill_072'], 'func': wcd_base_universe_d3_070_wcd_basefill_072}


def wcd_base_universe_d3_071_wcd_basefill_073(wcd_base_universe_d2_071_wcd_basefill_073):
    return _base_universe_d3(wcd_base_universe_d2_071_wcd_basefill_073, 71)
WCD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['wcd_base_universe_d3_071_wcd_basefill_073'] = {'inputs': ['wcd_base_universe_d2_071_wcd_basefill_073'], 'func': wcd_base_universe_d3_071_wcd_basefill_073}


def wcd_base_universe_d3_072_wcd_basefill_074(wcd_base_universe_d2_072_wcd_basefill_074):
    return _base_universe_d3(wcd_base_universe_d2_072_wcd_basefill_074, 72)
WCD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['wcd_base_universe_d3_072_wcd_basefill_074'] = {'inputs': ['wcd_base_universe_d2_072_wcd_basefill_074'], 'func': wcd_base_universe_d3_072_wcd_basefill_074}


def wcd_base_universe_d3_073_wcd_basefill_075(wcd_base_universe_d2_073_wcd_basefill_075):
    return _base_universe_d3(wcd_base_universe_d2_073_wcd_basefill_075, 73)
WCD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['wcd_base_universe_d3_073_wcd_basefill_075'] = {'inputs': ['wcd_base_universe_d2_073_wcd_basefill_075'], 'func': wcd_base_universe_d3_073_wcd_basefill_075}
