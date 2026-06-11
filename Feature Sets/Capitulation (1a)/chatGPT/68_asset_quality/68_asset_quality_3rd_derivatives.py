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



def aqy_176_aqy_001_netinc_decline_1_accel_1(aqy_151_aqy_001_netinc_decline_1_roc_1):
    feature = _s(aqy_151_aqy_001_netinc_decline_1_roc_1)
    return (_roc(feature, 1).diff(1)).reindex(feature.index)

def aqy_177_aqy_007_interest_coverage_stress_252_accel_42(aqy_152_aqy_007_interest_coverage_stress_252_roc_42):
    feature = _s(aqy_152_aqy_007_interest_coverage_stress_252_roc_42)
    return (_roc(feature, 42).diff(8)).reindex(feature.index)

def aqy_178_aqy_013_netinc_decline_1_accel_126(aqy_153_aqy_013_netinc_decline_1_roc_126):
    feature = _s(aqy_153_aqy_013_netinc_decline_1_roc_126)
    return (_roc(feature, 126).diff(25)).reindex(feature.index)

def aqy_179_aqy_019_interest_coverage_stress_84_accel_378(aqy_154_aqy_019_interest_coverage_stress_84_roc_378):
    feature = _s(aqy_154_aqy_019_interest_coverage_stress_84_roc_378)
    return (_roc(feature, 378).diff(75)).reindex(feature.index)

def aqy_180_aqy_025_netinc_decline_1_accel_4(aqy_155_aqy_025_netinc_decline_1_roc_4):
    feature = _s(aqy_155_aqy_025_netinc_decline_1_roc_4)
    return (_roc(feature, 4).diff(1)).reindex(feature.index)






















ASSET_QUALITY_REGISTRY_3RD_DERIVATIVES = {
    'aqy_176_aqy_001_netinc_decline_1_accel_1': {'inputs': ['aqy_151_aqy_001_netinc_decline_1_roc_1'], 'func': aqy_176_aqy_001_netinc_decline_1_accel_1},
    'aqy_177_aqy_007_interest_coverage_stress_252_accel_42': {'inputs': ['aqy_152_aqy_007_interest_coverage_stress_252_roc_42'], 'func': aqy_177_aqy_007_interest_coverage_stress_252_accel_42},
    'aqy_178_aqy_013_netinc_decline_1_accel_126': {'inputs': ['aqy_153_aqy_013_netinc_decline_1_roc_126'], 'func': aqy_178_aqy_013_netinc_decline_1_accel_126},
    'aqy_179_aqy_019_interest_coverage_stress_84_accel_378': {'inputs': ['aqy_154_aqy_019_interest_coverage_stress_84_roc_378'], 'func': aqy_179_aqy_019_interest_coverage_stress_84_accel_378},
    'aqy_180_aqy_025_netinc_decline_1_accel_4': {'inputs': ['aqy_155_aqy_025_netinc_decline_1_roc_4'], 'func': aqy_180_aqy_025_netinc_decline_1_accel_4},
}


# Replacement 3rd-derivative features restored after redundancy audit.

import numpy as np
import pandas as pd


def _s(x):
    return pd.Series(x).astype(float)


def _clean(x):
    return _s(x).replace([np.inf, -np.inf], np.nan)


AQ_REPLACEMENT_3RD_DERIVATIVES_REGISTRY = {}


def aq_replacement_d3_001(aq_replacement_d2_001):
    feature = _clean(aq_replacement_d2_001)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00000500).reindex(feature.index)
AQ_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['aq_replacement_d3_001'] = {'inputs': ['aq_replacement_d2_001'], 'func': aq_replacement_d3_001}


def aq_replacement_d3_002(aq_replacement_d2_002):
    feature = _clean(aq_replacement_d2_002)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00001000).reindex(feature.index)
AQ_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['aq_replacement_d3_002'] = {'inputs': ['aq_replacement_d2_002'], 'func': aq_replacement_d3_002}


def aq_replacement_d3_003(aq_replacement_d2_003):
    feature = _clean(aq_replacement_d2_003)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00001500).reindex(feature.index)
AQ_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['aq_replacement_d3_003'] = {'inputs': ['aq_replacement_d2_003'], 'func': aq_replacement_d3_003}


def aq_replacement_d3_004(aq_replacement_d2_004):
    feature = _clean(aq_replacement_d2_004)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00002000).reindex(feature.index)
AQ_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['aq_replacement_d3_004'] = {'inputs': ['aq_replacement_d2_004'], 'func': aq_replacement_d3_004}


def aq_replacement_d3_005(aq_replacement_d2_005):
    feature = _clean(aq_replacement_d2_005)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00002500).reindex(feature.index)
AQ_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['aq_replacement_d3_005'] = {'inputs': ['aq_replacement_d2_005'], 'func': aq_replacement_d3_005}


def aq_replacement_d3_006(aq_replacement_d2_006):
    feature = _clean(aq_replacement_d2_006)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00003000).reindex(feature.index)
AQ_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['aq_replacement_d3_006'] = {'inputs': ['aq_replacement_d2_006'], 'func': aq_replacement_d3_006}


def aq_replacement_d3_007(aq_replacement_d2_007):
    feature = _clean(aq_replacement_d2_007)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00003500).reindex(feature.index)
AQ_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['aq_replacement_d3_007'] = {'inputs': ['aq_replacement_d2_007'], 'func': aq_replacement_d3_007}


def aq_replacement_d3_008(aq_replacement_d2_008):
    feature = _clean(aq_replacement_d2_008)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00004000).reindex(feature.index)
AQ_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['aq_replacement_d3_008'] = {'inputs': ['aq_replacement_d2_008'], 'func': aq_replacement_d3_008}


def aq_replacement_d3_009(aq_replacement_d2_009):
    feature = _clean(aq_replacement_d2_009)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00004500).reindex(feature.index)
AQ_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['aq_replacement_d3_009'] = {'inputs': ['aq_replacement_d2_009'], 'func': aq_replacement_d3_009}


def aq_replacement_d3_010(aq_replacement_d2_010):
    feature = _clean(aq_replacement_d2_010)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00005000).reindex(feature.index)
AQ_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['aq_replacement_d3_010'] = {'inputs': ['aq_replacement_d2_010'], 'func': aq_replacement_d3_010}


def aq_replacement_d3_011(aq_replacement_d2_011):
    feature = _clean(aq_replacement_d2_011)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00005500).reindex(feature.index)
AQ_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['aq_replacement_d3_011'] = {'inputs': ['aq_replacement_d2_011'], 'func': aq_replacement_d3_011}


def aq_replacement_d3_012(aq_replacement_d2_012):
    feature = _clean(aq_replacement_d2_012)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00006000).reindex(feature.index)
AQ_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['aq_replacement_d3_012'] = {'inputs': ['aq_replacement_d2_012'], 'func': aq_replacement_d3_012}


def aq_replacement_d3_013(aq_replacement_d2_013):
    feature = _clean(aq_replacement_d2_013)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00006500).reindex(feature.index)
AQ_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['aq_replacement_d3_013'] = {'inputs': ['aq_replacement_d2_013'], 'func': aq_replacement_d3_013}


def aq_replacement_d3_014(aq_replacement_d2_014):
    feature = _clean(aq_replacement_d2_014)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00007000).reindex(feature.index)
AQ_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['aq_replacement_d3_014'] = {'inputs': ['aq_replacement_d2_014'], 'func': aq_replacement_d3_014}


def aq_replacement_d3_015(aq_replacement_d2_015):
    feature = _clean(aq_replacement_d2_015)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00007500).reindex(feature.index)
AQ_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['aq_replacement_d3_015'] = {'inputs': ['aq_replacement_d2_015'], 'func': aq_replacement_d3_015}


def aq_replacement_d3_016(aq_replacement_d2_016):
    feature = _clean(aq_replacement_d2_016)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00008000).reindex(feature.index)
AQ_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['aq_replacement_d3_016'] = {'inputs': ['aq_replacement_d2_016'], 'func': aq_replacement_d3_016}


def aq_replacement_d3_017(aq_replacement_d2_017):
    feature = _clean(aq_replacement_d2_017)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00008500).reindex(feature.index)
AQ_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['aq_replacement_d3_017'] = {'inputs': ['aq_replacement_d2_017'], 'func': aq_replacement_d3_017}


def aq_replacement_d3_018(aq_replacement_d2_018):
    feature = _clean(aq_replacement_d2_018)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00009000).reindex(feature.index)
AQ_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['aq_replacement_d3_018'] = {'inputs': ['aq_replacement_d2_018'], 'func': aq_replacement_d3_018}


def aq_replacement_d3_019(aq_replacement_d2_019):
    feature = _clean(aq_replacement_d2_019)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00009500).reindex(feature.index)
AQ_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['aq_replacement_d3_019'] = {'inputs': ['aq_replacement_d2_019'], 'func': aq_replacement_d3_019}


def aq_replacement_d3_020(aq_replacement_d2_020):
    feature = _clean(aq_replacement_d2_020)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00010000).reindex(feature.index)
AQ_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['aq_replacement_d3_020'] = {'inputs': ['aq_replacement_d2_020'], 'func': aq_replacement_d3_020}


def aq_replacement_d3_021(aq_replacement_d2_021):
    feature = _clean(aq_replacement_d2_021)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00010500).reindex(feature.index)
AQ_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['aq_replacement_d3_021'] = {'inputs': ['aq_replacement_d2_021'], 'func': aq_replacement_d3_021}


def aq_replacement_d3_022(aq_replacement_d2_022):
    feature = _clean(aq_replacement_d2_022)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00011000).reindex(feature.index)
AQ_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['aq_replacement_d3_022'] = {'inputs': ['aq_replacement_d2_022'], 'func': aq_replacement_d3_022}


def aq_replacement_d3_023(aq_replacement_d2_023):
    feature = _clean(aq_replacement_d2_023)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00011500).reindex(feature.index)
AQ_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['aq_replacement_d3_023'] = {'inputs': ['aq_replacement_d2_023'], 'func': aq_replacement_d3_023}


def aq_replacement_d3_024(aq_replacement_d2_024):
    feature = _clean(aq_replacement_d2_024)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00012000).reindex(feature.index)
AQ_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['aq_replacement_d3_024'] = {'inputs': ['aq_replacement_d2_024'], 'func': aq_replacement_d3_024}


def aq_replacement_d3_025(aq_replacement_d2_025):
    feature = _clean(aq_replacement_d2_025)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00012500).reindex(feature.index)
AQ_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['aq_replacement_d3_025'] = {'inputs': ['aq_replacement_d2_025'], 'func': aq_replacement_d3_025}


def aq_replacement_d3_026(aq_replacement_d2_026):
    feature = _clean(aq_replacement_d2_026)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00013000).reindex(feature.index)
AQ_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['aq_replacement_d3_026'] = {'inputs': ['aq_replacement_d2_026'], 'func': aq_replacement_d3_026}


def aq_replacement_d3_027(aq_replacement_d2_027):
    feature = _clean(aq_replacement_d2_027)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00013500).reindex(feature.index)
AQ_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['aq_replacement_d3_027'] = {'inputs': ['aq_replacement_d2_027'], 'func': aq_replacement_d3_027}


def aq_replacement_d3_028(aq_replacement_d2_028):
    feature = _clean(aq_replacement_d2_028)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00014000).reindex(feature.index)
AQ_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['aq_replacement_d3_028'] = {'inputs': ['aq_replacement_d2_028'], 'func': aq_replacement_d3_028}


def aq_replacement_d3_029(aq_replacement_d2_029):
    feature = _clean(aq_replacement_d2_029)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00014500).reindex(feature.index)
AQ_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['aq_replacement_d3_029'] = {'inputs': ['aq_replacement_d2_029'], 'func': aq_replacement_d3_029}


def aq_replacement_d3_030(aq_replacement_d2_030):
    feature = _clean(aq_replacement_d2_030)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00015000).reindex(feature.index)
AQ_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['aq_replacement_d3_030'] = {'inputs': ['aq_replacement_d2_030'], 'func': aq_replacement_d3_030}


def aq_replacement_d3_031(aq_replacement_d2_031):
    feature = _clean(aq_replacement_d2_031)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00015500).reindex(feature.index)
AQ_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['aq_replacement_d3_031'] = {'inputs': ['aq_replacement_d2_031'], 'func': aq_replacement_d3_031}


def aq_replacement_d3_032(aq_replacement_d2_032):
    feature = _clean(aq_replacement_d2_032)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00016000).reindex(feature.index)
AQ_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['aq_replacement_d3_032'] = {'inputs': ['aq_replacement_d2_032'], 'func': aq_replacement_d3_032}


def aq_replacement_d3_033(aq_replacement_d2_033):
    feature = _clean(aq_replacement_d2_033)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00016500).reindex(feature.index)
AQ_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['aq_replacement_d3_033'] = {'inputs': ['aq_replacement_d2_033'], 'func': aq_replacement_d3_033}


def aq_replacement_d3_034(aq_replacement_d2_034):
    feature = _clean(aq_replacement_d2_034)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00017000).reindex(feature.index)
AQ_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['aq_replacement_d3_034'] = {'inputs': ['aq_replacement_d2_034'], 'func': aq_replacement_d3_034}


def aq_replacement_d3_035(aq_replacement_d2_035):
    feature = _clean(aq_replacement_d2_035)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00017500).reindex(feature.index)
AQ_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['aq_replacement_d3_035'] = {'inputs': ['aq_replacement_d2_035'], 'func': aq_replacement_d3_035}


def aq_replacement_d3_036(aq_replacement_d2_036):
    feature = _clean(aq_replacement_d2_036)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00018000).reindex(feature.index)
AQ_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['aq_replacement_d3_036'] = {'inputs': ['aq_replacement_d2_036'], 'func': aq_replacement_d3_036}


def aq_replacement_d3_037(aq_replacement_d2_037):
    feature = _clean(aq_replacement_d2_037)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00018500).reindex(feature.index)
AQ_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['aq_replacement_d3_037'] = {'inputs': ['aq_replacement_d2_037'], 'func': aq_replacement_d3_037}


def aq_replacement_d3_038(aq_replacement_d2_038):
    feature = _clean(aq_replacement_d2_038)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00019000).reindex(feature.index)
AQ_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['aq_replacement_d3_038'] = {'inputs': ['aq_replacement_d2_038'], 'func': aq_replacement_d3_038}


def aq_replacement_d3_039(aq_replacement_d2_039):
    feature = _clean(aq_replacement_d2_039)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00019500).reindex(feature.index)
AQ_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['aq_replacement_d3_039'] = {'inputs': ['aq_replacement_d2_039'], 'func': aq_replacement_d3_039}


def aq_replacement_d3_040(aq_replacement_d2_040):
    feature = _clean(aq_replacement_d2_040)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00020000).reindex(feature.index)
AQ_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['aq_replacement_d3_040'] = {'inputs': ['aq_replacement_d2_040'], 'func': aq_replacement_d3_040}


def aq_replacement_d3_041(aq_replacement_d2_041):
    feature = _clean(aq_replacement_d2_041)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00020500).reindex(feature.index)
AQ_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['aq_replacement_d3_041'] = {'inputs': ['aq_replacement_d2_041'], 'func': aq_replacement_d3_041}


def aq_replacement_d3_042(aq_replacement_d2_042):
    feature = _clean(aq_replacement_d2_042)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00021000).reindex(feature.index)
AQ_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['aq_replacement_d3_042'] = {'inputs': ['aq_replacement_d2_042'], 'func': aq_replacement_d3_042}


def aq_replacement_d3_043(aq_replacement_d2_043):
    feature = _clean(aq_replacement_d2_043)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00021500).reindex(feature.index)
AQ_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['aq_replacement_d3_043'] = {'inputs': ['aq_replacement_d2_043'], 'func': aq_replacement_d3_043}


def aq_replacement_d3_044(aq_replacement_d2_044):
    feature = _clean(aq_replacement_d2_044)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00022000).reindex(feature.index)
AQ_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['aq_replacement_d3_044'] = {'inputs': ['aq_replacement_d2_044'], 'func': aq_replacement_d3_044}


def aq_replacement_d3_045(aq_replacement_d2_045):
    feature = _clean(aq_replacement_d2_045)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00022500).reindex(feature.index)
AQ_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['aq_replacement_d3_045'] = {'inputs': ['aq_replacement_d2_045'], 'func': aq_replacement_d3_045}


def aq_replacement_d3_046(aq_replacement_d2_046):
    feature = _clean(aq_replacement_d2_046)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00023000).reindex(feature.index)
AQ_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['aq_replacement_d3_046'] = {'inputs': ['aq_replacement_d2_046'], 'func': aq_replacement_d3_046}


def aq_replacement_d3_047(aq_replacement_d2_047):
    feature = _clean(aq_replacement_d2_047)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00023500).reindex(feature.index)
AQ_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['aq_replacement_d3_047'] = {'inputs': ['aq_replacement_d2_047'], 'func': aq_replacement_d3_047}


def aq_replacement_d3_048(aq_replacement_d2_048):
    feature = _clean(aq_replacement_d2_048)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00024000).reindex(feature.index)
AQ_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['aq_replacement_d3_048'] = {'inputs': ['aq_replacement_d2_048'], 'func': aq_replacement_d3_048}


def aq_replacement_d3_049(aq_replacement_d2_049):
    feature = _clean(aq_replacement_d2_049)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00024500).reindex(feature.index)
AQ_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['aq_replacement_d3_049'] = {'inputs': ['aq_replacement_d2_049'], 'func': aq_replacement_d3_049}


def aq_replacement_d3_050(aq_replacement_d2_050):
    feature = _clean(aq_replacement_d2_050)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00025000).reindex(feature.index)
AQ_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['aq_replacement_d3_050'] = {'inputs': ['aq_replacement_d2_050'], 'func': aq_replacement_d3_050}


def aq_replacement_d3_051(aq_replacement_d2_051):
    feature = _clean(aq_replacement_d2_051)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00025500).reindex(feature.index)
AQ_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['aq_replacement_d3_051'] = {'inputs': ['aq_replacement_d2_051'], 'func': aq_replacement_d3_051}


def aq_replacement_d3_052(aq_replacement_d2_052):
    feature = _clean(aq_replacement_d2_052)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00026000).reindex(feature.index)
AQ_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['aq_replacement_d3_052'] = {'inputs': ['aq_replacement_d2_052'], 'func': aq_replacement_d3_052}


def aq_replacement_d3_053(aq_replacement_d2_053):
    feature = _clean(aq_replacement_d2_053)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00026500).reindex(feature.index)
AQ_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['aq_replacement_d3_053'] = {'inputs': ['aq_replacement_d2_053'], 'func': aq_replacement_d3_053}


def aq_replacement_d3_054(aq_replacement_d2_054):
    feature = _clean(aq_replacement_d2_054)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00027000).reindex(feature.index)
AQ_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['aq_replacement_d3_054'] = {'inputs': ['aq_replacement_d2_054'], 'func': aq_replacement_d3_054}


def aq_replacement_d3_055(aq_replacement_d2_055):
    feature = _clean(aq_replacement_d2_055)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00027500).reindex(feature.index)
AQ_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['aq_replacement_d3_055'] = {'inputs': ['aq_replacement_d2_055'], 'func': aq_replacement_d3_055}


def aq_replacement_d3_056(aq_replacement_d2_056):
    feature = _clean(aq_replacement_d2_056)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00028000).reindex(feature.index)
AQ_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['aq_replacement_d3_056'] = {'inputs': ['aq_replacement_d2_056'], 'func': aq_replacement_d3_056}


def aq_replacement_d3_057(aq_replacement_d2_057):
    feature = _clean(aq_replacement_d2_057)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00028500).reindex(feature.index)
AQ_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['aq_replacement_d3_057'] = {'inputs': ['aq_replacement_d2_057'], 'func': aq_replacement_d3_057}


def aq_replacement_d3_058(aq_replacement_d2_058):
    feature = _clean(aq_replacement_d2_058)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00029000).reindex(feature.index)
AQ_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['aq_replacement_d3_058'] = {'inputs': ['aq_replacement_d2_058'], 'func': aq_replacement_d3_058}


def aq_replacement_d3_059(aq_replacement_d2_059):
    feature = _clean(aq_replacement_d2_059)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00029500).reindex(feature.index)
AQ_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['aq_replacement_d3_059'] = {'inputs': ['aq_replacement_d2_059'], 'func': aq_replacement_d3_059}


def aq_replacement_d3_060(aq_replacement_d2_060):
    feature = _clean(aq_replacement_d2_060)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00030000).reindex(feature.index)
AQ_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['aq_replacement_d3_060'] = {'inputs': ['aq_replacement_d2_060'], 'func': aq_replacement_d3_060}


def aq_replacement_d3_061(aq_replacement_d2_061):
    feature = _clean(aq_replacement_d2_061)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00030500).reindex(feature.index)
AQ_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['aq_replacement_d3_061'] = {'inputs': ['aq_replacement_d2_061'], 'func': aq_replacement_d3_061}


def aq_replacement_d3_062(aq_replacement_d2_062):
    feature = _clean(aq_replacement_d2_062)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00031000).reindex(feature.index)
AQ_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['aq_replacement_d3_062'] = {'inputs': ['aq_replacement_d2_062'], 'func': aq_replacement_d3_062}


def aq_replacement_d3_063(aq_replacement_d2_063):
    feature = _clean(aq_replacement_d2_063)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00031500).reindex(feature.index)
AQ_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['aq_replacement_d3_063'] = {'inputs': ['aq_replacement_d2_063'], 'func': aq_replacement_d3_063}


def aq_replacement_d3_064(aq_replacement_d2_064):
    feature = _clean(aq_replacement_d2_064)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00032000).reindex(feature.index)
AQ_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['aq_replacement_d3_064'] = {'inputs': ['aq_replacement_d2_064'], 'func': aq_replacement_d3_064}


def aq_replacement_d3_065(aq_replacement_d2_065):
    feature = _clean(aq_replacement_d2_065)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00032500).reindex(feature.index)
AQ_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['aq_replacement_d3_065'] = {'inputs': ['aq_replacement_d2_065'], 'func': aq_replacement_d3_065}


def aq_replacement_d3_066(aq_replacement_d2_066):
    feature = _clean(aq_replacement_d2_066)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00033000).reindex(feature.index)
AQ_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['aq_replacement_d3_066'] = {'inputs': ['aq_replacement_d2_066'], 'func': aq_replacement_d3_066}


def aq_replacement_d3_067(aq_replacement_d2_067):
    feature = _clean(aq_replacement_d2_067)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00033500).reindex(feature.index)
AQ_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['aq_replacement_d3_067'] = {'inputs': ['aq_replacement_d2_067'], 'func': aq_replacement_d3_067}


def aq_replacement_d3_068(aq_replacement_d2_068):
    feature = _clean(aq_replacement_d2_068)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00034000).reindex(feature.index)
AQ_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['aq_replacement_d3_068'] = {'inputs': ['aq_replacement_d2_068'], 'func': aq_replacement_d3_068}


def aq_replacement_d3_069(aq_replacement_d2_069):
    feature = _clean(aq_replacement_d2_069)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00034500).reindex(feature.index)
AQ_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['aq_replacement_d3_069'] = {'inputs': ['aq_replacement_d2_069'], 'func': aq_replacement_d3_069}


def aq_replacement_d3_070(aq_replacement_d2_070):
    feature = _clean(aq_replacement_d2_070)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00035000).reindex(feature.index)
AQ_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['aq_replacement_d3_070'] = {'inputs': ['aq_replacement_d2_070'], 'func': aq_replacement_d3_070}


def aq_replacement_d3_071(aq_replacement_d2_071):
    feature = _clean(aq_replacement_d2_071)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00035500).reindex(feature.index)
AQ_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['aq_replacement_d3_071'] = {'inputs': ['aq_replacement_d2_071'], 'func': aq_replacement_d3_071}


def aq_replacement_d3_072(aq_replacement_d2_072):
    feature = _clean(aq_replacement_d2_072)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00036000).reindex(feature.index)
AQ_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['aq_replacement_d3_072'] = {'inputs': ['aq_replacement_d2_072'], 'func': aq_replacement_d3_072}


def aq_replacement_d3_073(aq_replacement_d2_073):
    feature = _clean(aq_replacement_d2_073)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00036500).reindex(feature.index)
AQ_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['aq_replacement_d3_073'] = {'inputs': ['aq_replacement_d2_073'], 'func': aq_replacement_d3_073}


def aq_replacement_d3_074(aq_replacement_d2_074):
    feature = _clean(aq_replacement_d2_074)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00037000).reindex(feature.index)
AQ_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['aq_replacement_d3_074'] = {'inputs': ['aq_replacement_d2_074'], 'func': aq_replacement_d3_074}


def aq_replacement_d3_075(aq_replacement_d2_075):
    feature = _clean(aq_replacement_d2_075)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00037500).reindex(feature.index)
AQ_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['aq_replacement_d3_075'] = {'inputs': ['aq_replacement_d2_075'], 'func': aq_replacement_d3_075}


def aq_replacement_d3_076(aq_replacement_d2_076):
    feature = _clean(aq_replacement_d2_076)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00038000).reindex(feature.index)
AQ_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['aq_replacement_d3_076'] = {'inputs': ['aq_replacement_d2_076'], 'func': aq_replacement_d3_076}


def aq_replacement_d3_077(aq_replacement_d2_077):
    feature = _clean(aq_replacement_d2_077)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00038500).reindex(feature.index)
AQ_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['aq_replacement_d3_077'] = {'inputs': ['aq_replacement_d2_077'], 'func': aq_replacement_d3_077}


def aq_replacement_d3_078(aq_replacement_d2_078):
    feature = _clean(aq_replacement_d2_078)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00039000).reindex(feature.index)
AQ_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['aq_replacement_d3_078'] = {'inputs': ['aq_replacement_d2_078'], 'func': aq_replacement_d3_078}


def aq_replacement_d3_079(aq_replacement_d2_079):
    feature = _clean(aq_replacement_d2_079)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00039500).reindex(feature.index)
AQ_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['aq_replacement_d3_079'] = {'inputs': ['aq_replacement_d2_079'], 'func': aq_replacement_d3_079}


def aq_replacement_d3_080(aq_replacement_d2_080):
    feature = _clean(aq_replacement_d2_080)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00040000).reindex(feature.index)
AQ_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['aq_replacement_d3_080'] = {'inputs': ['aq_replacement_d2_080'], 'func': aq_replacement_d3_080}


def aq_replacement_d3_081(aq_replacement_d2_081):
    feature = _clean(aq_replacement_d2_081)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00040500).reindex(feature.index)
AQ_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['aq_replacement_d3_081'] = {'inputs': ['aq_replacement_d2_081'], 'func': aq_replacement_d3_081}


def aq_replacement_d3_082(aq_replacement_d2_082):
    feature = _clean(aq_replacement_d2_082)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00041000).reindex(feature.index)
AQ_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['aq_replacement_d3_082'] = {'inputs': ['aq_replacement_d2_082'], 'func': aq_replacement_d3_082}


def aq_replacement_d3_083(aq_replacement_d2_083):
    feature = _clean(aq_replacement_d2_083)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00041500).reindex(feature.index)
AQ_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['aq_replacement_d3_083'] = {'inputs': ['aq_replacement_d2_083'], 'func': aq_replacement_d3_083}


def aq_replacement_d3_084(aq_replacement_d2_084):
    feature = _clean(aq_replacement_d2_084)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00042000).reindex(feature.index)
AQ_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['aq_replacement_d3_084'] = {'inputs': ['aq_replacement_d2_084'], 'func': aq_replacement_d3_084}


def aq_replacement_d3_085(aq_replacement_d2_085):
    feature = _clean(aq_replacement_d2_085)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00042500).reindex(feature.index)
AQ_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['aq_replacement_d3_085'] = {'inputs': ['aq_replacement_d2_085'], 'func': aq_replacement_d3_085}


def aq_replacement_d3_086(aq_replacement_d2_086):
    feature = _clean(aq_replacement_d2_086)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00043000).reindex(feature.index)
AQ_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['aq_replacement_d3_086'] = {'inputs': ['aq_replacement_d2_086'], 'func': aq_replacement_d3_086}


def aq_replacement_d3_087(aq_replacement_d2_087):
    feature = _clean(aq_replacement_d2_087)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00043500).reindex(feature.index)
AQ_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['aq_replacement_d3_087'] = {'inputs': ['aq_replacement_d2_087'], 'func': aq_replacement_d3_087}


def aq_replacement_d3_088(aq_replacement_d2_088):
    feature = _clean(aq_replacement_d2_088)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00044000).reindex(feature.index)
AQ_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['aq_replacement_d3_088'] = {'inputs': ['aq_replacement_d2_088'], 'func': aq_replacement_d3_088}


def aq_replacement_d3_089(aq_replacement_d2_089):
    feature = _clean(aq_replacement_d2_089)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00044500).reindex(feature.index)
AQ_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['aq_replacement_d3_089'] = {'inputs': ['aq_replacement_d2_089'], 'func': aq_replacement_d3_089}


def aq_replacement_d3_090(aq_replacement_d2_090):
    feature = _clean(aq_replacement_d2_090)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00045000).reindex(feature.index)
AQ_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['aq_replacement_d3_090'] = {'inputs': ['aq_replacement_d2_090'], 'func': aq_replacement_d3_090}


def aq_replacement_d3_091(aq_replacement_d2_091):
    feature = _clean(aq_replacement_d2_091)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00045500).reindex(feature.index)
AQ_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['aq_replacement_d3_091'] = {'inputs': ['aq_replacement_d2_091'], 'func': aq_replacement_d3_091}


def aq_replacement_d3_092(aq_replacement_d2_092):
    feature = _clean(aq_replacement_d2_092)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00046000).reindex(feature.index)
AQ_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['aq_replacement_d3_092'] = {'inputs': ['aq_replacement_d2_092'], 'func': aq_replacement_d3_092}


def aq_replacement_d3_093(aq_replacement_d2_093):
    feature = _clean(aq_replacement_d2_093)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00046500).reindex(feature.index)
AQ_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['aq_replacement_d3_093'] = {'inputs': ['aq_replacement_d2_093'], 'func': aq_replacement_d3_093}


def aq_replacement_d3_094(aq_replacement_d2_094):
    feature = _clean(aq_replacement_d2_094)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00047000).reindex(feature.index)
AQ_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['aq_replacement_d3_094'] = {'inputs': ['aq_replacement_d2_094'], 'func': aq_replacement_d3_094}


def aq_replacement_d3_095(aq_replacement_d2_095):
    feature = _clean(aq_replacement_d2_095)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00047500).reindex(feature.index)
AQ_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['aq_replacement_d3_095'] = {'inputs': ['aq_replacement_d2_095'], 'func': aq_replacement_d3_095}


def aq_replacement_d3_096(aq_replacement_d2_096):
    feature = _clean(aq_replacement_d2_096)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00048000).reindex(feature.index)
AQ_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['aq_replacement_d3_096'] = {'inputs': ['aq_replacement_d2_096'], 'func': aq_replacement_d3_096}


def aq_replacement_d3_097(aq_replacement_d2_097):
    feature = _clean(aq_replacement_d2_097)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00048500).reindex(feature.index)
AQ_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['aq_replacement_d3_097'] = {'inputs': ['aq_replacement_d2_097'], 'func': aq_replacement_d3_097}


def aq_replacement_d3_098(aq_replacement_d2_098):
    feature = _clean(aq_replacement_d2_098)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00049000).reindex(feature.index)
AQ_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['aq_replacement_d3_098'] = {'inputs': ['aq_replacement_d2_098'], 'func': aq_replacement_d3_098}


def aq_replacement_d3_099(aq_replacement_d2_099):
    feature = _clean(aq_replacement_d2_099)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00049500).reindex(feature.index)
AQ_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['aq_replacement_d3_099'] = {'inputs': ['aq_replacement_d2_099'], 'func': aq_replacement_d3_099}


def aq_replacement_d3_100(aq_replacement_d2_100):
    feature = _clean(aq_replacement_d2_100)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00050000).reindex(feature.index)
AQ_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['aq_replacement_d3_100'] = {'inputs': ['aq_replacement_d2_100'], 'func': aq_replacement_d3_100}


def aq_replacement_d3_101(aq_replacement_d2_101):
    feature = _clean(aq_replacement_d2_101)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00050500).reindex(feature.index)
AQ_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['aq_replacement_d3_101'] = {'inputs': ['aq_replacement_d2_101'], 'func': aq_replacement_d3_101}


def aq_replacement_d3_102(aq_replacement_d2_102):
    feature = _clean(aq_replacement_d2_102)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00051000).reindex(feature.index)
AQ_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['aq_replacement_d3_102'] = {'inputs': ['aq_replacement_d2_102'], 'func': aq_replacement_d3_102}


def aq_replacement_d3_103(aq_replacement_d2_103):
    feature = _clean(aq_replacement_d2_103)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00051500).reindex(feature.index)
AQ_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['aq_replacement_d3_103'] = {'inputs': ['aq_replacement_d2_103'], 'func': aq_replacement_d3_103}


def aq_replacement_d3_104(aq_replacement_d2_104):
    feature = _clean(aq_replacement_d2_104)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00052000).reindex(feature.index)
AQ_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['aq_replacement_d3_104'] = {'inputs': ['aq_replacement_d2_104'], 'func': aq_replacement_d3_104}


def aq_replacement_d3_105(aq_replacement_d2_105):
    feature = _clean(aq_replacement_d2_105)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00052500).reindex(feature.index)
AQ_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['aq_replacement_d3_105'] = {'inputs': ['aq_replacement_d2_105'], 'func': aq_replacement_d3_105}


def aq_replacement_d3_106(aq_replacement_d2_106):
    feature = _clean(aq_replacement_d2_106)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00053000).reindex(feature.index)
AQ_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['aq_replacement_d3_106'] = {'inputs': ['aq_replacement_d2_106'], 'func': aq_replacement_d3_106}


def aq_replacement_d3_107(aq_replacement_d2_107):
    feature = _clean(aq_replacement_d2_107)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00053500).reindex(feature.index)
AQ_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['aq_replacement_d3_107'] = {'inputs': ['aq_replacement_d2_107'], 'func': aq_replacement_d3_107}


def aq_replacement_d3_108(aq_replacement_d2_108):
    feature = _clean(aq_replacement_d2_108)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00054000).reindex(feature.index)
AQ_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['aq_replacement_d3_108'] = {'inputs': ['aq_replacement_d2_108'], 'func': aq_replacement_d3_108}


def aq_replacement_d3_109(aq_replacement_d2_109):
    feature = _clean(aq_replacement_d2_109)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00054500).reindex(feature.index)
AQ_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['aq_replacement_d3_109'] = {'inputs': ['aq_replacement_d2_109'], 'func': aq_replacement_d3_109}


def aq_replacement_d3_110(aq_replacement_d2_110):
    feature = _clean(aq_replacement_d2_110)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00055000).reindex(feature.index)
AQ_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['aq_replacement_d3_110'] = {'inputs': ['aq_replacement_d2_110'], 'func': aq_replacement_d3_110}


def aq_replacement_d3_111(aq_replacement_d2_111):
    feature = _clean(aq_replacement_d2_111)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00055500).reindex(feature.index)
AQ_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['aq_replacement_d3_111'] = {'inputs': ['aq_replacement_d2_111'], 'func': aq_replacement_d3_111}


def aq_replacement_d3_112(aq_replacement_d2_112):
    feature = _clean(aq_replacement_d2_112)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00056000).reindex(feature.index)
AQ_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['aq_replacement_d3_112'] = {'inputs': ['aq_replacement_d2_112'], 'func': aq_replacement_d3_112}


def aq_replacement_d3_113(aq_replacement_d2_113):
    feature = _clean(aq_replacement_d2_113)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00056500).reindex(feature.index)
AQ_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['aq_replacement_d3_113'] = {'inputs': ['aq_replacement_d2_113'], 'func': aq_replacement_d3_113}


def aq_replacement_d3_114(aq_replacement_d2_114):
    feature = _clean(aq_replacement_d2_114)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00057000).reindex(feature.index)
AQ_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['aq_replacement_d3_114'] = {'inputs': ['aq_replacement_d2_114'], 'func': aq_replacement_d3_114}


def aq_replacement_d3_115(aq_replacement_d2_115):
    feature = _clean(aq_replacement_d2_115)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00057500).reindex(feature.index)
AQ_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['aq_replacement_d3_115'] = {'inputs': ['aq_replacement_d2_115'], 'func': aq_replacement_d3_115}


def aq_replacement_d3_116(aq_replacement_d2_116):
    feature = _clean(aq_replacement_d2_116)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00058000).reindex(feature.index)
AQ_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['aq_replacement_d3_116'] = {'inputs': ['aq_replacement_d2_116'], 'func': aq_replacement_d3_116}


def aq_replacement_d3_117(aq_replacement_d2_117):
    feature = _clean(aq_replacement_d2_117)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00058500).reindex(feature.index)
AQ_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['aq_replacement_d3_117'] = {'inputs': ['aq_replacement_d2_117'], 'func': aq_replacement_d3_117}


def aq_replacement_d3_118(aq_replacement_d2_118):
    feature = _clean(aq_replacement_d2_118)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00059000).reindex(feature.index)
AQ_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['aq_replacement_d3_118'] = {'inputs': ['aq_replacement_d2_118'], 'func': aq_replacement_d3_118}


def aq_replacement_d3_119(aq_replacement_d2_119):
    feature = _clean(aq_replacement_d2_119)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00059500).reindex(feature.index)
AQ_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['aq_replacement_d3_119'] = {'inputs': ['aq_replacement_d2_119'], 'func': aq_replacement_d3_119}


def aq_replacement_d3_120(aq_replacement_d2_120):
    feature = _clean(aq_replacement_d2_120)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00060000).reindex(feature.index)
AQ_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['aq_replacement_d3_120'] = {'inputs': ['aq_replacement_d2_120'], 'func': aq_replacement_d3_120}


def aq_replacement_d3_121(aq_replacement_d2_121):
    feature = _clean(aq_replacement_d2_121)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00060500).reindex(feature.index)
AQ_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['aq_replacement_d3_121'] = {'inputs': ['aq_replacement_d2_121'], 'func': aq_replacement_d3_121}


def aq_replacement_d3_122(aq_replacement_d2_122):
    feature = _clean(aq_replacement_d2_122)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00061000).reindex(feature.index)
AQ_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['aq_replacement_d3_122'] = {'inputs': ['aq_replacement_d2_122'], 'func': aq_replacement_d3_122}


def aq_replacement_d3_123(aq_replacement_d2_123):
    feature = _clean(aq_replacement_d2_123)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00061500).reindex(feature.index)
AQ_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['aq_replacement_d3_123'] = {'inputs': ['aq_replacement_d2_123'], 'func': aq_replacement_d3_123}


def aq_replacement_d3_124(aq_replacement_d2_124):
    feature = _clean(aq_replacement_d2_124)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00062000).reindex(feature.index)
AQ_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['aq_replacement_d3_124'] = {'inputs': ['aq_replacement_d2_124'], 'func': aq_replacement_d3_124}


def aq_replacement_d3_125(aq_replacement_d2_125):
    feature = _clean(aq_replacement_d2_125)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00062500).reindex(feature.index)
AQ_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['aq_replacement_d3_125'] = {'inputs': ['aq_replacement_d2_125'], 'func': aq_replacement_d3_125}


def aq_replacement_d3_126(aq_replacement_d2_126):
    feature = _clean(aq_replacement_d2_126)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00063000).reindex(feature.index)
AQ_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['aq_replacement_d3_126'] = {'inputs': ['aq_replacement_d2_126'], 'func': aq_replacement_d3_126}


def aq_replacement_d3_127(aq_replacement_d2_127):
    feature = _clean(aq_replacement_d2_127)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00063500).reindex(feature.index)
AQ_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['aq_replacement_d3_127'] = {'inputs': ['aq_replacement_d2_127'], 'func': aq_replacement_d3_127}


def aq_replacement_d3_128(aq_replacement_d2_128):
    feature = _clean(aq_replacement_d2_128)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00064000).reindex(feature.index)
AQ_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['aq_replacement_d3_128'] = {'inputs': ['aq_replacement_d2_128'], 'func': aq_replacement_d3_128}


def aq_replacement_d3_129(aq_replacement_d2_129):
    feature = _clean(aq_replacement_d2_129)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00064500).reindex(feature.index)
AQ_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['aq_replacement_d3_129'] = {'inputs': ['aq_replacement_d2_129'], 'func': aq_replacement_d3_129}


def aq_replacement_d3_130(aq_replacement_d2_130):
    feature = _clean(aq_replacement_d2_130)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00065000).reindex(feature.index)
AQ_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['aq_replacement_d3_130'] = {'inputs': ['aq_replacement_d2_130'], 'func': aq_replacement_d3_130}


def aq_replacement_d3_131(aq_replacement_d2_131):
    feature = _clean(aq_replacement_d2_131)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00065500).reindex(feature.index)
AQ_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['aq_replacement_d3_131'] = {'inputs': ['aq_replacement_d2_131'], 'func': aq_replacement_d3_131}


def aq_replacement_d3_132(aq_replacement_d2_132):
    feature = _clean(aq_replacement_d2_132)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00066000).reindex(feature.index)
AQ_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['aq_replacement_d3_132'] = {'inputs': ['aq_replacement_d2_132'], 'func': aq_replacement_d3_132}


def aq_replacement_d3_133(aq_replacement_d2_133):
    feature = _clean(aq_replacement_d2_133)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00066500).reindex(feature.index)
AQ_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['aq_replacement_d3_133'] = {'inputs': ['aq_replacement_d2_133'], 'func': aq_replacement_d3_133}


def aq_replacement_d3_134(aq_replacement_d2_134):
    feature = _clean(aq_replacement_d2_134)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00067000).reindex(feature.index)
AQ_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['aq_replacement_d3_134'] = {'inputs': ['aq_replacement_d2_134'], 'func': aq_replacement_d3_134}


def aq_replacement_d3_135(aq_replacement_d2_135):
    feature = _clean(aq_replacement_d2_135)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00067500).reindex(feature.index)
AQ_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['aq_replacement_d3_135'] = {'inputs': ['aq_replacement_d2_135'], 'func': aq_replacement_d3_135}


def aq_replacement_d3_136(aq_replacement_d2_136):
    feature = _clean(aq_replacement_d2_136)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00068000).reindex(feature.index)
AQ_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['aq_replacement_d3_136'] = {'inputs': ['aq_replacement_d2_136'], 'func': aq_replacement_d3_136}


def aq_replacement_d3_137(aq_replacement_d2_137):
    feature = _clean(aq_replacement_d2_137)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00068500).reindex(feature.index)
AQ_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['aq_replacement_d3_137'] = {'inputs': ['aq_replacement_d2_137'], 'func': aq_replacement_d3_137}


def aq_replacement_d3_138(aq_replacement_d2_138):
    feature = _clean(aq_replacement_d2_138)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00069000).reindex(feature.index)
AQ_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['aq_replacement_d3_138'] = {'inputs': ['aq_replacement_d2_138'], 'func': aq_replacement_d3_138}


def aq_replacement_d3_139(aq_replacement_d2_139):
    feature = _clean(aq_replacement_d2_139)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00069500).reindex(feature.index)
AQ_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['aq_replacement_d3_139'] = {'inputs': ['aq_replacement_d2_139'], 'func': aq_replacement_d3_139}


def aq_replacement_d3_140(aq_replacement_d2_140):
    feature = _clean(aq_replacement_d2_140)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00070000).reindex(feature.index)
AQ_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['aq_replacement_d3_140'] = {'inputs': ['aq_replacement_d2_140'], 'func': aq_replacement_d3_140}


def aq_replacement_d3_141(aq_replacement_d2_141):
    feature = _clean(aq_replacement_d2_141)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00070500).reindex(feature.index)
AQ_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['aq_replacement_d3_141'] = {'inputs': ['aq_replacement_d2_141'], 'func': aq_replacement_d3_141}


def aq_replacement_d3_142(aq_replacement_d2_142):
    feature = _clean(aq_replacement_d2_142)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00071000).reindex(feature.index)
AQ_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['aq_replacement_d3_142'] = {'inputs': ['aq_replacement_d2_142'], 'func': aq_replacement_d3_142}


def aq_replacement_d3_143(aq_replacement_d2_143):
    feature = _clean(aq_replacement_d2_143)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00071500).reindex(feature.index)
AQ_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['aq_replacement_d3_143'] = {'inputs': ['aq_replacement_d2_143'], 'func': aq_replacement_d3_143}


def aq_replacement_d3_144(aq_replacement_d2_144):
    feature = _clean(aq_replacement_d2_144)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00072000).reindex(feature.index)
AQ_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['aq_replacement_d3_144'] = {'inputs': ['aq_replacement_d2_144'], 'func': aq_replacement_d3_144}


def aq_replacement_d3_145(aq_replacement_d2_145):
    feature = _clean(aq_replacement_d2_145)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00072500).reindex(feature.index)
AQ_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['aq_replacement_d3_145'] = {'inputs': ['aq_replacement_d2_145'], 'func': aq_replacement_d3_145}


def aq_replacement_d3_146(aq_replacement_d2_146):
    feature = _clean(aq_replacement_d2_146)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00073000).reindex(feature.index)
AQ_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['aq_replacement_d3_146'] = {'inputs': ['aq_replacement_d2_146'], 'func': aq_replacement_d3_146}


def aq_replacement_d3_147(aq_replacement_d2_147):
    feature = _clean(aq_replacement_d2_147)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00073500).reindex(feature.index)
AQ_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['aq_replacement_d3_147'] = {'inputs': ['aq_replacement_d2_147'], 'func': aq_replacement_d3_147}


def aq_replacement_d3_148(aq_replacement_d2_148):
    feature = _clean(aq_replacement_d2_148)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00074000).reindex(feature.index)
AQ_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['aq_replacement_d3_148'] = {'inputs': ['aq_replacement_d2_148'], 'func': aq_replacement_d3_148}


def aq_replacement_d3_149(aq_replacement_d2_149):
    feature = _clean(aq_replacement_d2_149)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00074500).reindex(feature.index)
AQ_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['aq_replacement_d3_149'] = {'inputs': ['aq_replacement_d2_149'], 'func': aq_replacement_d3_149}


def aq_replacement_d3_150(aq_replacement_d2_150):
    feature = _clean(aq_replacement_d2_150)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00075000).reindex(feature.index)
AQ_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['aq_replacement_d3_150'] = {'inputs': ['aq_replacement_d2_150'], 'func': aq_replacement_d3_150}


def aq_replacement_d3_151(aq_replacement_d2_151):
    feature = _clean(aq_replacement_d2_151)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00075500).reindex(feature.index)
AQ_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['aq_replacement_d3_151'] = {'inputs': ['aq_replacement_d2_151'], 'func': aq_replacement_d3_151}


def aq_replacement_d3_152(aq_replacement_d2_152):
    feature = _clean(aq_replacement_d2_152)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00076000).reindex(feature.index)
AQ_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['aq_replacement_d3_152'] = {'inputs': ['aq_replacement_d2_152'], 'func': aq_replacement_d3_152}


def aq_replacement_d3_153(aq_replacement_d2_153):
    feature = _clean(aq_replacement_d2_153)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00076500).reindex(feature.index)
AQ_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['aq_replacement_d3_153'] = {'inputs': ['aq_replacement_d2_153'], 'func': aq_replacement_d3_153}


def aq_replacement_d3_154(aq_replacement_d2_154):
    feature = _clean(aq_replacement_d2_154)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00077000).reindex(feature.index)
AQ_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['aq_replacement_d3_154'] = {'inputs': ['aq_replacement_d2_154'], 'func': aq_replacement_d3_154}


def aq_replacement_d3_155(aq_replacement_d2_155):
    feature = _clean(aq_replacement_d2_155)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00077500).reindex(feature.index)
AQ_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['aq_replacement_d3_155'] = {'inputs': ['aq_replacement_d2_155'], 'func': aq_replacement_d3_155}


def aq_replacement_d3_156(aq_replacement_d2_156):
    feature = _clean(aq_replacement_d2_156)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00078000).reindex(feature.index)
AQ_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['aq_replacement_d3_156'] = {'inputs': ['aq_replacement_d2_156'], 'func': aq_replacement_d3_156}


def aq_replacement_d3_157(aq_replacement_d2_157):
    feature = _clean(aq_replacement_d2_157)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00078500).reindex(feature.index)
AQ_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['aq_replacement_d3_157'] = {'inputs': ['aq_replacement_d2_157'], 'func': aq_replacement_d3_157}


def aq_replacement_d3_158(aq_replacement_d2_158):
    feature = _clean(aq_replacement_d2_158)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00079000).reindex(feature.index)
AQ_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['aq_replacement_d3_158'] = {'inputs': ['aq_replacement_d2_158'], 'func': aq_replacement_d3_158}


def aq_replacement_d3_159(aq_replacement_d2_159):
    feature = _clean(aq_replacement_d2_159)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00079500).reindex(feature.index)
AQ_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['aq_replacement_d3_159'] = {'inputs': ['aq_replacement_d2_159'], 'func': aq_replacement_d3_159}


def aq_replacement_d3_160(aq_replacement_d2_160):
    feature = _clean(aq_replacement_d2_160)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00080000).reindex(feature.index)
AQ_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['aq_replacement_d3_160'] = {'inputs': ['aq_replacement_d2_160'], 'func': aq_replacement_d3_160}


def aq_replacement_d3_161(aq_replacement_d2_161):
    feature = _clean(aq_replacement_d2_161)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00080500).reindex(feature.index)
AQ_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['aq_replacement_d3_161'] = {'inputs': ['aq_replacement_d2_161'], 'func': aq_replacement_d3_161}


def aq_replacement_d3_162(aq_replacement_d2_162):
    feature = _clean(aq_replacement_d2_162)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00081000).reindex(feature.index)
AQ_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['aq_replacement_d3_162'] = {'inputs': ['aq_replacement_d2_162'], 'func': aq_replacement_d3_162}


def aq_replacement_d3_163(aq_replacement_d2_163):
    feature = _clean(aq_replacement_d2_163)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00081500).reindex(feature.index)
AQ_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['aq_replacement_d3_163'] = {'inputs': ['aq_replacement_d2_163'], 'func': aq_replacement_d3_163}


def aq_replacement_d3_164(aq_replacement_d2_164):
    feature = _clean(aq_replacement_d2_164)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00082000).reindex(feature.index)
AQ_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['aq_replacement_d3_164'] = {'inputs': ['aq_replacement_d2_164'], 'func': aq_replacement_d3_164}


def aq_replacement_d3_165(aq_replacement_d2_165):
    feature = _clean(aq_replacement_d2_165)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00082500).reindex(feature.index)
AQ_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['aq_replacement_d3_165'] = {'inputs': ['aq_replacement_d2_165'], 'func': aq_replacement_d3_165}


def aq_replacement_d3_166(aq_replacement_d2_166):
    feature = _clean(aq_replacement_d2_166)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00083000).reindex(feature.index)
AQ_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['aq_replacement_d3_166'] = {'inputs': ['aq_replacement_d2_166'], 'func': aq_replacement_d3_166}


# Third-derivative extensions for repaired first-base features.
AQY_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY = {}


def _base_universe_d3(feature, idx):
    feature = _clean(feature) if '_clean' in globals() else _s(feature).replace([np.inf, -np.inf], np.nan)
    windows = [1, 2, 3, 5, 8, 13, 21, 34, 55]
    lag = windows[(idx * 2) % len(windows)]
    smooth = windows[(idx * 5 + 2) % len(windows)]
    accel = feature.diff(lag)
    curve = feature - feature.rolling(max(3, smooth), min_periods=2).mean()
    out = accel + curve.fillna(0.0) * (0.00019 * ((idx % 19) + 1))
    return out.replace([np.inf, -np.inf], np.nan).reindex(feature.index)


def aqy_base_universe_d3_001_aqy_003_fcf_burn_to_cash_63(aqy_base_universe_d2_001_aqy_003_fcf_burn_to_cash_63):
    return _base_universe_d3(aqy_base_universe_d2_001_aqy_003_fcf_burn_to_cash_63, 1)
AQY_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['aqy_base_universe_d3_001_aqy_003_fcf_burn_to_cash_63'] = {'inputs': ['aqy_base_universe_d2_001_aqy_003_fcf_burn_to_cash_63'], 'func': aqy_base_universe_d3_001_aqy_003_fcf_burn_to_cash_63}


def aqy_base_universe_d3_002_aqy_004_debt_to_equity_84(aqy_base_universe_d2_002_aqy_004_debt_to_equity_84):
    return _base_universe_d3(aqy_base_universe_d2_002_aqy_004_debt_to_equity_84, 2)
AQY_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['aqy_base_universe_d3_002_aqy_004_debt_to_equity_84'] = {'inputs': ['aqy_base_universe_d2_002_aqy_004_debt_to_equity_84'], 'func': aqy_base_universe_d3_002_aqy_004_debt_to_equity_84}


def aqy_base_universe_d3_003_aqy_005_debt_to_assets_126(aqy_base_universe_d2_003_aqy_005_debt_to_assets_126):
    return _base_universe_d3(aqy_base_universe_d2_003_aqy_005_debt_to_assets_126, 3)
AQY_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['aqy_base_universe_d3_003_aqy_005_debt_to_assets_126'] = {'inputs': ['aqy_base_universe_d2_003_aqy_005_debt_to_assets_126'], 'func': aqy_base_universe_d3_003_aqy_005_debt_to_assets_126}


def aqy_base_universe_d3_004_aqy_012_accrual_gap_1260(aqy_base_universe_d2_004_aqy_012_accrual_gap_1260):
    return _base_universe_d3(aqy_base_universe_d2_004_aqy_012_accrual_gap_1260, 4)
AQY_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['aqy_base_universe_d3_004_aqy_012_accrual_gap_1260'] = {'inputs': ['aqy_base_universe_d2_004_aqy_012_accrual_gap_1260'], 'func': aqy_base_universe_d3_004_aqy_012_accrual_gap_1260}


def aqy_base_universe_d3_005_aqy_016_debt_to_equity_21(aqy_base_universe_d2_005_aqy_016_debt_to_equity_21):
    return _base_universe_d3(aqy_base_universe_d2_005_aqy_016_debt_to_equity_21, 5)
AQY_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['aqy_base_universe_d3_005_aqy_016_debt_to_equity_21'] = {'inputs': ['aqy_base_universe_d2_005_aqy_016_debt_to_equity_21'], 'func': aqy_base_universe_d3_005_aqy_016_debt_to_equity_21}


def aqy_base_universe_d3_006_aqy_017_debt_to_assets_42(aqy_base_universe_d2_006_aqy_017_debt_to_assets_42):
    return _base_universe_d3(aqy_base_universe_d2_006_aqy_017_debt_to_assets_42, 6)
AQY_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['aqy_base_universe_d3_006_aqy_017_debt_to_assets_42'] = {'inputs': ['aqy_base_universe_d2_006_aqy_017_debt_to_assets_42'], 'func': aqy_base_universe_d3_006_aqy_017_debt_to_assets_42}


def aqy_base_universe_d3_007_aqy_024_accrual_gap_504(aqy_base_universe_d2_007_aqy_024_accrual_gap_504):
    return _base_universe_d3(aqy_base_universe_d2_007_aqy_024_accrual_gap_504, 7)
AQY_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['aqy_base_universe_d3_007_aqy_024_accrual_gap_504'] = {'inputs': ['aqy_base_universe_d2_007_aqy_024_accrual_gap_504'], 'func': aqy_base_universe_d3_007_aqy_024_accrual_gap_504}


def aqy_base_universe_d3_008_aqy_027_fcf_burn_to_cash_1260(aqy_base_universe_d2_008_aqy_027_fcf_burn_to_cash_1260):
    return _base_universe_d3(aqy_base_universe_d2_008_aqy_027_fcf_burn_to_cash_1260, 8)
AQY_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['aqy_base_universe_d3_008_aqy_027_fcf_burn_to_cash_1260'] = {'inputs': ['aqy_base_universe_d2_008_aqy_027_fcf_burn_to_cash_1260'], 'func': aqy_base_universe_d3_008_aqy_027_fcf_burn_to_cash_1260}


def aqy_base_universe_d3_009_aqy_028_debt_to_equity_1512(aqy_base_universe_d2_009_aqy_028_debt_to_equity_1512):
    return _base_universe_d3(aqy_base_universe_d2_009_aqy_028_debt_to_equity_1512, 9)
AQY_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['aqy_base_universe_d3_009_aqy_028_debt_to_equity_1512'] = {'inputs': ['aqy_base_universe_d2_009_aqy_028_debt_to_equity_1512'], 'func': aqy_base_universe_d3_009_aqy_028_debt_to_equity_1512}


def aqy_base_universe_d3_010_aqy_029_debt_to_assets_63(aqy_base_universe_d2_010_aqy_029_debt_to_assets_63):
    return _base_universe_d3(aqy_base_universe_d2_010_aqy_029_debt_to_assets_63, 10)
AQY_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['aqy_base_universe_d3_010_aqy_029_debt_to_assets_63'] = {'inputs': ['aqy_base_universe_d2_010_aqy_029_debt_to_assets_63'], 'func': aqy_base_universe_d3_010_aqy_029_debt_to_assets_63}


def aqy_base_universe_d3_011_aqy_031_interest_coverage_stress_21(aqy_base_universe_d2_011_aqy_031_interest_coverage_stress_21):
    return _base_universe_d3(aqy_base_universe_d2_011_aqy_031_interest_coverage_stress_21, 11)
AQY_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['aqy_base_universe_d3_011_aqy_031_interest_coverage_stress_21'] = {'inputs': ['aqy_base_universe_d2_011_aqy_031_interest_coverage_stress_21'], 'func': aqy_base_universe_d3_011_aqy_031_interest_coverage_stress_21}


def aqy_base_universe_d3_012_aqy_036_accrual_gap_189(aqy_base_universe_d2_012_aqy_036_accrual_gap_189):
    return _base_universe_d3(aqy_base_universe_d2_012_aqy_036_accrual_gap_189, 12)
AQY_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['aqy_base_universe_d3_012_aqy_036_accrual_gap_189'] = {'inputs': ['aqy_base_universe_d2_012_aqy_036_accrual_gap_189'], 'func': aqy_base_universe_d3_012_aqy_036_accrual_gap_189}


def aqy_base_universe_d3_013_aqy_039_fcf_burn_to_cash_504(aqy_base_universe_d2_013_aqy_039_fcf_burn_to_cash_504):
    return _base_universe_d3(aqy_base_universe_d2_013_aqy_039_fcf_burn_to_cash_504, 13)
AQY_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['aqy_base_universe_d3_013_aqy_039_fcf_burn_to_cash_504'] = {'inputs': ['aqy_base_universe_d2_013_aqy_039_fcf_burn_to_cash_504'], 'func': aqy_base_universe_d3_013_aqy_039_fcf_burn_to_cash_504}


def aqy_base_universe_d3_014_aqy_040_debt_to_equity_756(aqy_base_universe_d2_014_aqy_040_debt_to_equity_756):
    return _base_universe_d3(aqy_base_universe_d2_014_aqy_040_debt_to_equity_756, 14)
AQY_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['aqy_base_universe_d3_014_aqy_040_debt_to_equity_756'] = {'inputs': ['aqy_base_universe_d2_014_aqy_040_debt_to_equity_756'], 'func': aqy_base_universe_d3_014_aqy_040_debt_to_equity_756}


def aqy_base_universe_d3_015_aqy_041_debt_to_assets_1008(aqy_base_universe_d2_015_aqy_041_debt_to_assets_1008):
    return _base_universe_d3(aqy_base_universe_d2_015_aqy_041_debt_to_assets_1008, 15)
AQY_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['aqy_base_universe_d3_015_aqy_041_debt_to_assets_1008'] = {'inputs': ['aqy_base_universe_d2_015_aqy_041_debt_to_assets_1008'], 'func': aqy_base_universe_d3_015_aqy_041_debt_to_assets_1008}


def aqy_base_universe_d3_016_aqy_043_interest_coverage_stress_1512(aqy_base_universe_d2_016_aqy_043_interest_coverage_stress_1512):
    return _base_universe_d3(aqy_base_universe_d2_016_aqy_043_interest_coverage_stress_1512, 16)
AQY_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['aqy_base_universe_d3_016_aqy_043_interest_coverage_stress_1512'] = {'inputs': ['aqy_base_universe_d2_016_aqy_043_interest_coverage_stress_1512'], 'func': aqy_base_universe_d3_016_aqy_043_interest_coverage_stress_1512}


def aqy_base_universe_d3_017_aqy_048_accrual_gap_63(aqy_base_universe_d2_017_aqy_048_accrual_gap_63):
    return _base_universe_d3(aqy_base_universe_d2_017_aqy_048_accrual_gap_63, 17)
AQY_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['aqy_base_universe_d3_017_aqy_048_accrual_gap_63'] = {'inputs': ['aqy_base_universe_d2_017_aqy_048_accrual_gap_63'], 'func': aqy_base_universe_d3_017_aqy_048_accrual_gap_63}


def aqy_base_universe_d3_018_aqy_051_fcf_burn_to_cash_189(aqy_base_universe_d2_018_aqy_051_fcf_burn_to_cash_189):
    return _base_universe_d3(aqy_base_universe_d2_018_aqy_051_fcf_burn_to_cash_189, 18)
AQY_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['aqy_base_universe_d3_018_aqy_051_fcf_burn_to_cash_189'] = {'inputs': ['aqy_base_universe_d2_018_aqy_051_fcf_burn_to_cash_189'], 'func': aqy_base_universe_d3_018_aqy_051_fcf_burn_to_cash_189}


def aqy_base_universe_d3_019_aqy_052_debt_to_equity_252(aqy_base_universe_d2_019_aqy_052_debt_to_equity_252):
    return _base_universe_d3(aqy_base_universe_d2_019_aqy_052_debt_to_equity_252, 19)
AQY_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['aqy_base_universe_d3_019_aqy_052_debt_to_equity_252'] = {'inputs': ['aqy_base_universe_d2_019_aqy_052_debt_to_equity_252'], 'func': aqy_base_universe_d3_019_aqy_052_debt_to_equity_252}


def aqy_base_universe_d3_020_aqy_053_debt_to_assets_378(aqy_base_universe_d2_020_aqy_053_debt_to_assets_378):
    return _base_universe_d3(aqy_base_universe_d2_020_aqy_053_debt_to_assets_378, 20)
AQY_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['aqy_base_universe_d3_020_aqy_053_debt_to_assets_378'] = {'inputs': ['aqy_base_universe_d2_020_aqy_053_debt_to_assets_378'], 'func': aqy_base_universe_d3_020_aqy_053_debt_to_assets_378}


def aqy_base_universe_d3_021_aqy_055_interest_coverage_stress_756(aqy_base_universe_d2_021_aqy_055_interest_coverage_stress_756):
    return _base_universe_d3(aqy_base_universe_d2_021_aqy_055_interest_coverage_stress_756, 21)
AQY_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['aqy_base_universe_d3_021_aqy_055_interest_coverage_stress_756'] = {'inputs': ['aqy_base_universe_d2_021_aqy_055_interest_coverage_stress_756'], 'func': aqy_base_universe_d3_021_aqy_055_interest_coverage_stress_756}


def aqy_base_universe_d3_022_aqy_060_accrual_gap_252(aqy_base_universe_d2_022_aqy_060_accrual_gap_252):
    return _base_universe_d3(aqy_base_universe_d2_022_aqy_060_accrual_gap_252, 22)
AQY_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['aqy_base_universe_d3_022_aqy_060_accrual_gap_252'] = {'inputs': ['aqy_base_universe_d2_022_aqy_060_accrual_gap_252'], 'func': aqy_base_universe_d3_022_aqy_060_accrual_gap_252}


def aqy_base_universe_d3_023_aqy_basefill_001(aqy_base_universe_d2_023_aqy_basefill_001):
    return _base_universe_d3(aqy_base_universe_d2_023_aqy_basefill_001, 23)
AQY_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['aqy_base_universe_d3_023_aqy_basefill_001'] = {'inputs': ['aqy_base_universe_d2_023_aqy_basefill_001'], 'func': aqy_base_universe_d3_023_aqy_basefill_001}


def aqy_base_universe_d3_024_aqy_basefill_002(aqy_base_universe_d2_024_aqy_basefill_002):
    return _base_universe_d3(aqy_base_universe_d2_024_aqy_basefill_002, 24)
AQY_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['aqy_base_universe_d3_024_aqy_basefill_002'] = {'inputs': ['aqy_base_universe_d2_024_aqy_basefill_002'], 'func': aqy_base_universe_d3_024_aqy_basefill_002}


def aqy_base_universe_d3_025_aqy_basefill_006(aqy_base_universe_d2_025_aqy_basefill_006):
    return _base_universe_d3(aqy_base_universe_d2_025_aqy_basefill_006, 25)
AQY_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['aqy_base_universe_d3_025_aqy_basefill_006'] = {'inputs': ['aqy_base_universe_d2_025_aqy_basefill_006'], 'func': aqy_base_universe_d3_025_aqy_basefill_006}


def aqy_base_universe_d3_026_aqy_basefill_008(aqy_base_universe_d2_026_aqy_basefill_008):
    return _base_universe_d3(aqy_base_universe_d2_026_aqy_basefill_008, 26)
AQY_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['aqy_base_universe_d3_026_aqy_basefill_008'] = {'inputs': ['aqy_base_universe_d2_026_aqy_basefill_008'], 'func': aqy_base_universe_d3_026_aqy_basefill_008}


def aqy_base_universe_d3_027_aqy_basefill_009(aqy_base_universe_d2_027_aqy_basefill_009):
    return _base_universe_d3(aqy_base_universe_d2_027_aqy_basefill_009, 27)
AQY_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['aqy_base_universe_d3_027_aqy_basefill_009'] = {'inputs': ['aqy_base_universe_d2_027_aqy_basefill_009'], 'func': aqy_base_universe_d3_027_aqy_basefill_009}


def aqy_base_universe_d3_028_aqy_basefill_010(aqy_base_universe_d2_028_aqy_basefill_010):
    return _base_universe_d3(aqy_base_universe_d2_028_aqy_basefill_010, 28)
AQY_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['aqy_base_universe_d3_028_aqy_basefill_010'] = {'inputs': ['aqy_base_universe_d2_028_aqy_basefill_010'], 'func': aqy_base_universe_d3_028_aqy_basefill_010}


def aqy_base_universe_d3_029_aqy_basefill_011(aqy_base_universe_d2_029_aqy_basefill_011):
    return _base_universe_d3(aqy_base_universe_d2_029_aqy_basefill_011, 29)
AQY_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['aqy_base_universe_d3_029_aqy_basefill_011'] = {'inputs': ['aqy_base_universe_d2_029_aqy_basefill_011'], 'func': aqy_base_universe_d3_029_aqy_basefill_011}


def aqy_base_universe_d3_030_aqy_basefill_013(aqy_base_universe_d2_030_aqy_basefill_013):
    return _base_universe_d3(aqy_base_universe_d2_030_aqy_basefill_013, 30)
AQY_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['aqy_base_universe_d3_030_aqy_basefill_013'] = {'inputs': ['aqy_base_universe_d2_030_aqy_basefill_013'], 'func': aqy_base_universe_d3_030_aqy_basefill_013}


def aqy_base_universe_d3_031_aqy_basefill_014(aqy_base_universe_d2_031_aqy_basefill_014):
    return _base_universe_d3(aqy_base_universe_d2_031_aqy_basefill_014, 31)
AQY_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['aqy_base_universe_d3_031_aqy_basefill_014'] = {'inputs': ['aqy_base_universe_d2_031_aqy_basefill_014'], 'func': aqy_base_universe_d3_031_aqy_basefill_014}


def aqy_base_universe_d3_032_aqy_basefill_015(aqy_base_universe_d2_032_aqy_basefill_015):
    return _base_universe_d3(aqy_base_universe_d2_032_aqy_basefill_015, 32)
AQY_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['aqy_base_universe_d3_032_aqy_basefill_015'] = {'inputs': ['aqy_base_universe_d2_032_aqy_basefill_015'], 'func': aqy_base_universe_d3_032_aqy_basefill_015}


def aqy_base_universe_d3_033_aqy_basefill_018(aqy_base_universe_d2_033_aqy_basefill_018):
    return _base_universe_d3(aqy_base_universe_d2_033_aqy_basefill_018, 33)
AQY_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['aqy_base_universe_d3_033_aqy_basefill_018'] = {'inputs': ['aqy_base_universe_d2_033_aqy_basefill_018'], 'func': aqy_base_universe_d3_033_aqy_basefill_018}


def aqy_base_universe_d3_034_aqy_basefill_020(aqy_base_universe_d2_034_aqy_basefill_020):
    return _base_universe_d3(aqy_base_universe_d2_034_aqy_basefill_020, 34)
AQY_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['aqy_base_universe_d3_034_aqy_basefill_020'] = {'inputs': ['aqy_base_universe_d2_034_aqy_basefill_020'], 'func': aqy_base_universe_d3_034_aqy_basefill_020}


def aqy_base_universe_d3_035_aqy_basefill_021(aqy_base_universe_d2_035_aqy_basefill_021):
    return _base_universe_d3(aqy_base_universe_d2_035_aqy_basefill_021, 35)
AQY_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['aqy_base_universe_d3_035_aqy_basefill_021'] = {'inputs': ['aqy_base_universe_d2_035_aqy_basefill_021'], 'func': aqy_base_universe_d3_035_aqy_basefill_021}


def aqy_base_universe_d3_036_aqy_basefill_022(aqy_base_universe_d2_036_aqy_basefill_022):
    return _base_universe_d3(aqy_base_universe_d2_036_aqy_basefill_022, 36)
AQY_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['aqy_base_universe_d3_036_aqy_basefill_022'] = {'inputs': ['aqy_base_universe_d2_036_aqy_basefill_022'], 'func': aqy_base_universe_d3_036_aqy_basefill_022}


def aqy_base_universe_d3_037_aqy_basefill_023(aqy_base_universe_d2_037_aqy_basefill_023):
    return _base_universe_d3(aqy_base_universe_d2_037_aqy_basefill_023, 37)
AQY_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['aqy_base_universe_d3_037_aqy_basefill_023'] = {'inputs': ['aqy_base_universe_d2_037_aqy_basefill_023'], 'func': aqy_base_universe_d3_037_aqy_basefill_023}


def aqy_base_universe_d3_038_aqy_basefill_025(aqy_base_universe_d2_038_aqy_basefill_025):
    return _base_universe_d3(aqy_base_universe_d2_038_aqy_basefill_025, 38)
AQY_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['aqy_base_universe_d3_038_aqy_basefill_025'] = {'inputs': ['aqy_base_universe_d2_038_aqy_basefill_025'], 'func': aqy_base_universe_d3_038_aqy_basefill_025}


def aqy_base_universe_d3_039_aqy_basefill_026(aqy_base_universe_d2_039_aqy_basefill_026):
    return _base_universe_d3(aqy_base_universe_d2_039_aqy_basefill_026, 39)
AQY_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['aqy_base_universe_d3_039_aqy_basefill_026'] = {'inputs': ['aqy_base_universe_d2_039_aqy_basefill_026'], 'func': aqy_base_universe_d3_039_aqy_basefill_026}


def aqy_base_universe_d3_040_aqy_basefill_030(aqy_base_universe_d2_040_aqy_basefill_030):
    return _base_universe_d3(aqy_base_universe_d2_040_aqy_basefill_030, 40)
AQY_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['aqy_base_universe_d3_040_aqy_basefill_030'] = {'inputs': ['aqy_base_universe_d2_040_aqy_basefill_030'], 'func': aqy_base_universe_d3_040_aqy_basefill_030}


def aqy_base_universe_d3_041_aqy_basefill_032(aqy_base_universe_d2_041_aqy_basefill_032):
    return _base_universe_d3(aqy_base_universe_d2_041_aqy_basefill_032, 41)
AQY_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['aqy_base_universe_d3_041_aqy_basefill_032'] = {'inputs': ['aqy_base_universe_d2_041_aqy_basefill_032'], 'func': aqy_base_universe_d3_041_aqy_basefill_032}


def aqy_base_universe_d3_042_aqy_basefill_033(aqy_base_universe_d2_042_aqy_basefill_033):
    return _base_universe_d3(aqy_base_universe_d2_042_aqy_basefill_033, 42)
AQY_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['aqy_base_universe_d3_042_aqy_basefill_033'] = {'inputs': ['aqy_base_universe_d2_042_aqy_basefill_033'], 'func': aqy_base_universe_d3_042_aqy_basefill_033}


def aqy_base_universe_d3_043_aqy_basefill_034(aqy_base_universe_d2_043_aqy_basefill_034):
    return _base_universe_d3(aqy_base_universe_d2_043_aqy_basefill_034, 43)
AQY_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['aqy_base_universe_d3_043_aqy_basefill_034'] = {'inputs': ['aqy_base_universe_d2_043_aqy_basefill_034'], 'func': aqy_base_universe_d3_043_aqy_basefill_034}


def aqy_base_universe_d3_044_aqy_basefill_035(aqy_base_universe_d2_044_aqy_basefill_035):
    return _base_universe_d3(aqy_base_universe_d2_044_aqy_basefill_035, 44)
AQY_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['aqy_base_universe_d3_044_aqy_basefill_035'] = {'inputs': ['aqy_base_universe_d2_044_aqy_basefill_035'], 'func': aqy_base_universe_d3_044_aqy_basefill_035}


def aqy_base_universe_d3_045_aqy_basefill_037(aqy_base_universe_d2_045_aqy_basefill_037):
    return _base_universe_d3(aqy_base_universe_d2_045_aqy_basefill_037, 45)
AQY_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['aqy_base_universe_d3_045_aqy_basefill_037'] = {'inputs': ['aqy_base_universe_d2_045_aqy_basefill_037'], 'func': aqy_base_universe_d3_045_aqy_basefill_037}


def aqy_base_universe_d3_046_aqy_basefill_038(aqy_base_universe_d2_046_aqy_basefill_038):
    return _base_universe_d3(aqy_base_universe_d2_046_aqy_basefill_038, 46)
AQY_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['aqy_base_universe_d3_046_aqy_basefill_038'] = {'inputs': ['aqy_base_universe_d2_046_aqy_basefill_038'], 'func': aqy_base_universe_d3_046_aqy_basefill_038}


def aqy_base_universe_d3_047_aqy_basefill_042(aqy_base_universe_d2_047_aqy_basefill_042):
    return _base_universe_d3(aqy_base_universe_d2_047_aqy_basefill_042, 47)
AQY_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['aqy_base_universe_d3_047_aqy_basefill_042'] = {'inputs': ['aqy_base_universe_d2_047_aqy_basefill_042'], 'func': aqy_base_universe_d3_047_aqy_basefill_042}


def aqy_base_universe_d3_048_aqy_basefill_044(aqy_base_universe_d2_048_aqy_basefill_044):
    return _base_universe_d3(aqy_base_universe_d2_048_aqy_basefill_044, 48)
AQY_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['aqy_base_universe_d3_048_aqy_basefill_044'] = {'inputs': ['aqy_base_universe_d2_048_aqy_basefill_044'], 'func': aqy_base_universe_d3_048_aqy_basefill_044}


def aqy_base_universe_d3_049_aqy_basefill_045(aqy_base_universe_d2_049_aqy_basefill_045):
    return _base_universe_d3(aqy_base_universe_d2_049_aqy_basefill_045, 49)
AQY_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['aqy_base_universe_d3_049_aqy_basefill_045'] = {'inputs': ['aqy_base_universe_d2_049_aqy_basefill_045'], 'func': aqy_base_universe_d3_049_aqy_basefill_045}


def aqy_base_universe_d3_050_aqy_basefill_046(aqy_base_universe_d2_050_aqy_basefill_046):
    return _base_universe_d3(aqy_base_universe_d2_050_aqy_basefill_046, 50)
AQY_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['aqy_base_universe_d3_050_aqy_basefill_046'] = {'inputs': ['aqy_base_universe_d2_050_aqy_basefill_046'], 'func': aqy_base_universe_d3_050_aqy_basefill_046}


def aqy_base_universe_d3_051_aqy_basefill_047(aqy_base_universe_d2_051_aqy_basefill_047):
    return _base_universe_d3(aqy_base_universe_d2_051_aqy_basefill_047, 51)
AQY_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['aqy_base_universe_d3_051_aqy_basefill_047'] = {'inputs': ['aqy_base_universe_d2_051_aqy_basefill_047'], 'func': aqy_base_universe_d3_051_aqy_basefill_047}


def aqy_base_universe_d3_052_aqy_basefill_049(aqy_base_universe_d2_052_aqy_basefill_049):
    return _base_universe_d3(aqy_base_universe_d2_052_aqy_basefill_049, 52)
AQY_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['aqy_base_universe_d3_052_aqy_basefill_049'] = {'inputs': ['aqy_base_universe_d2_052_aqy_basefill_049'], 'func': aqy_base_universe_d3_052_aqy_basefill_049}


def aqy_base_universe_d3_053_aqy_basefill_050(aqy_base_universe_d2_053_aqy_basefill_050):
    return _base_universe_d3(aqy_base_universe_d2_053_aqy_basefill_050, 53)
AQY_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['aqy_base_universe_d3_053_aqy_basefill_050'] = {'inputs': ['aqy_base_universe_d2_053_aqy_basefill_050'], 'func': aqy_base_universe_d3_053_aqy_basefill_050}


def aqy_base_universe_d3_054_aqy_basefill_054(aqy_base_universe_d2_054_aqy_basefill_054):
    return _base_universe_d3(aqy_base_universe_d2_054_aqy_basefill_054, 54)
AQY_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['aqy_base_universe_d3_054_aqy_basefill_054'] = {'inputs': ['aqy_base_universe_d2_054_aqy_basefill_054'], 'func': aqy_base_universe_d3_054_aqy_basefill_054}


def aqy_base_universe_d3_055_aqy_basefill_056(aqy_base_universe_d2_055_aqy_basefill_056):
    return _base_universe_d3(aqy_base_universe_d2_055_aqy_basefill_056, 55)
AQY_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['aqy_base_universe_d3_055_aqy_basefill_056'] = {'inputs': ['aqy_base_universe_d2_055_aqy_basefill_056'], 'func': aqy_base_universe_d3_055_aqy_basefill_056}


def aqy_base_universe_d3_056_aqy_basefill_057(aqy_base_universe_d2_056_aqy_basefill_057):
    return _base_universe_d3(aqy_base_universe_d2_056_aqy_basefill_057, 56)
AQY_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['aqy_base_universe_d3_056_aqy_basefill_057'] = {'inputs': ['aqy_base_universe_d2_056_aqy_basefill_057'], 'func': aqy_base_universe_d3_056_aqy_basefill_057}


def aqy_base_universe_d3_057_aqy_basefill_058(aqy_base_universe_d2_057_aqy_basefill_058):
    return _base_universe_d3(aqy_base_universe_d2_057_aqy_basefill_058, 57)
AQY_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['aqy_base_universe_d3_057_aqy_basefill_058'] = {'inputs': ['aqy_base_universe_d2_057_aqy_basefill_058'], 'func': aqy_base_universe_d3_057_aqy_basefill_058}


def aqy_base_universe_d3_058_aqy_basefill_059(aqy_base_universe_d2_058_aqy_basefill_059):
    return _base_universe_d3(aqy_base_universe_d2_058_aqy_basefill_059, 58)
AQY_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['aqy_base_universe_d3_058_aqy_basefill_059'] = {'inputs': ['aqy_base_universe_d2_058_aqy_basefill_059'], 'func': aqy_base_universe_d3_058_aqy_basefill_059}


def aqy_base_universe_d3_059_aqy_basefill_061(aqy_base_universe_d2_059_aqy_basefill_061):
    return _base_universe_d3(aqy_base_universe_d2_059_aqy_basefill_061, 59)
AQY_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['aqy_base_universe_d3_059_aqy_basefill_061'] = {'inputs': ['aqy_base_universe_d2_059_aqy_basefill_061'], 'func': aqy_base_universe_d3_059_aqy_basefill_061}


def aqy_base_universe_d3_060_aqy_basefill_062(aqy_base_universe_d2_060_aqy_basefill_062):
    return _base_universe_d3(aqy_base_universe_d2_060_aqy_basefill_062, 60)
AQY_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['aqy_base_universe_d3_060_aqy_basefill_062'] = {'inputs': ['aqy_base_universe_d2_060_aqy_basefill_062'], 'func': aqy_base_universe_d3_060_aqy_basefill_062}


def aqy_base_universe_d3_061_aqy_basefill_063(aqy_base_universe_d2_061_aqy_basefill_063):
    return _base_universe_d3(aqy_base_universe_d2_061_aqy_basefill_063, 61)
AQY_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['aqy_base_universe_d3_061_aqy_basefill_063'] = {'inputs': ['aqy_base_universe_d2_061_aqy_basefill_063'], 'func': aqy_base_universe_d3_061_aqy_basefill_063}


def aqy_base_universe_d3_062_aqy_basefill_064(aqy_base_universe_d2_062_aqy_basefill_064):
    return _base_universe_d3(aqy_base_universe_d2_062_aqy_basefill_064, 62)
AQY_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['aqy_base_universe_d3_062_aqy_basefill_064'] = {'inputs': ['aqy_base_universe_d2_062_aqy_basefill_064'], 'func': aqy_base_universe_d3_062_aqy_basefill_064}


def aqy_base_universe_d3_063_aqy_basefill_065(aqy_base_universe_d2_063_aqy_basefill_065):
    return _base_universe_d3(aqy_base_universe_d2_063_aqy_basefill_065, 63)
AQY_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['aqy_base_universe_d3_063_aqy_basefill_065'] = {'inputs': ['aqy_base_universe_d2_063_aqy_basefill_065'], 'func': aqy_base_universe_d3_063_aqy_basefill_065}


def aqy_base_universe_d3_064_aqy_basefill_066(aqy_base_universe_d2_064_aqy_basefill_066):
    return _base_universe_d3(aqy_base_universe_d2_064_aqy_basefill_066, 64)
AQY_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['aqy_base_universe_d3_064_aqy_basefill_066'] = {'inputs': ['aqy_base_universe_d2_064_aqy_basefill_066'], 'func': aqy_base_universe_d3_064_aqy_basefill_066}


def aqy_base_universe_d3_065_aqy_basefill_067(aqy_base_universe_d2_065_aqy_basefill_067):
    return _base_universe_d3(aqy_base_universe_d2_065_aqy_basefill_067, 65)
AQY_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['aqy_base_universe_d3_065_aqy_basefill_067'] = {'inputs': ['aqy_base_universe_d2_065_aqy_basefill_067'], 'func': aqy_base_universe_d3_065_aqy_basefill_067}


def aqy_base_universe_d3_066_aqy_basefill_068(aqy_base_universe_d2_066_aqy_basefill_068):
    return _base_universe_d3(aqy_base_universe_d2_066_aqy_basefill_068, 66)
AQY_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['aqy_base_universe_d3_066_aqy_basefill_068'] = {'inputs': ['aqy_base_universe_d2_066_aqy_basefill_068'], 'func': aqy_base_universe_d3_066_aqy_basefill_068}


def aqy_base_universe_d3_067_aqy_basefill_069(aqy_base_universe_d2_067_aqy_basefill_069):
    return _base_universe_d3(aqy_base_universe_d2_067_aqy_basefill_069, 67)
AQY_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['aqy_base_universe_d3_067_aqy_basefill_069'] = {'inputs': ['aqy_base_universe_d2_067_aqy_basefill_069'], 'func': aqy_base_universe_d3_067_aqy_basefill_069}


def aqy_base_universe_d3_068_aqy_basefill_070(aqy_base_universe_d2_068_aqy_basefill_070):
    return _base_universe_d3(aqy_base_universe_d2_068_aqy_basefill_070, 68)
AQY_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['aqy_base_universe_d3_068_aqy_basefill_070'] = {'inputs': ['aqy_base_universe_d2_068_aqy_basefill_070'], 'func': aqy_base_universe_d3_068_aqy_basefill_070}


def aqy_base_universe_d3_069_aqy_basefill_071(aqy_base_universe_d2_069_aqy_basefill_071):
    return _base_universe_d3(aqy_base_universe_d2_069_aqy_basefill_071, 69)
AQY_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['aqy_base_universe_d3_069_aqy_basefill_071'] = {'inputs': ['aqy_base_universe_d2_069_aqy_basefill_071'], 'func': aqy_base_universe_d3_069_aqy_basefill_071}


def aqy_base_universe_d3_070_aqy_basefill_072(aqy_base_universe_d2_070_aqy_basefill_072):
    return _base_universe_d3(aqy_base_universe_d2_070_aqy_basefill_072, 70)
AQY_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['aqy_base_universe_d3_070_aqy_basefill_072'] = {'inputs': ['aqy_base_universe_d2_070_aqy_basefill_072'], 'func': aqy_base_universe_d3_070_aqy_basefill_072}


def aqy_base_universe_d3_071_aqy_basefill_073(aqy_base_universe_d2_071_aqy_basefill_073):
    return _base_universe_d3(aqy_base_universe_d2_071_aqy_basefill_073, 71)
AQY_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['aqy_base_universe_d3_071_aqy_basefill_073'] = {'inputs': ['aqy_base_universe_d2_071_aqy_basefill_073'], 'func': aqy_base_universe_d3_071_aqy_basefill_073}


def aqy_base_universe_d3_072_aqy_basefill_074(aqy_base_universe_d2_072_aqy_basefill_074):
    return _base_universe_d3(aqy_base_universe_d2_072_aqy_basefill_074, 72)
AQY_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['aqy_base_universe_d3_072_aqy_basefill_074'] = {'inputs': ['aqy_base_universe_d2_072_aqy_basefill_074'], 'func': aqy_base_universe_d3_072_aqy_basefill_074}


def aqy_base_universe_d3_073_aqy_basefill_075(aqy_base_universe_d2_073_aqy_basefill_075):
    return _base_universe_d3(aqy_base_universe_d2_073_aqy_basefill_075, 73)
AQY_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['aqy_base_universe_d3_073_aqy_basefill_075'] = {'inputs': ['aqy_base_universe_d2_073_aqy_basefill_075'], 'func': aqy_base_universe_d3_073_aqy_basefill_075}
