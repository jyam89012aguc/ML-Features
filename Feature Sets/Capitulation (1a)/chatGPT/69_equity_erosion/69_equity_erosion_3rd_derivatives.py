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



def eqe_176_eqe_001_netinc_decline_1_accel_1(eqe_151_eqe_001_netinc_decline_1_roc_1):
    feature = _s(eqe_151_eqe_001_netinc_decline_1_roc_1)
    return (_roc(feature, 1).diff(1)).reindex(feature.index)

def eqe_177_eqe_007_interest_coverage_stress_252_accel_42(eqe_152_eqe_007_interest_coverage_stress_252_roc_42):
    feature = _s(eqe_152_eqe_007_interest_coverage_stress_252_roc_42)
    return (_roc(feature, 42).diff(8)).reindex(feature.index)

def eqe_178_eqe_013_netinc_decline_1_accel_126(eqe_153_eqe_013_netinc_decline_1_roc_126):
    feature = _s(eqe_153_eqe_013_netinc_decline_1_roc_126)
    return (_roc(feature, 126).diff(25)).reindex(feature.index)

def eqe_179_eqe_019_interest_coverage_stress_84_accel_378(eqe_154_eqe_019_interest_coverage_stress_84_roc_378):
    feature = _s(eqe_154_eqe_019_interest_coverage_stress_84_roc_378)
    return (_roc(feature, 378).diff(75)).reindex(feature.index)

def eqe_180_eqe_025_netinc_decline_1_accel_4(eqe_155_eqe_025_netinc_decline_1_roc_4):
    feature = _s(eqe_155_eqe_025_netinc_decline_1_roc_4)
    return (_roc(feature, 4).diff(1)).reindex(feature.index)






















EQUITY_EROSION_REGISTRY_3RD_DERIVATIVES = {
    'eqe_176_eqe_001_netinc_decline_1_accel_1': {'inputs': ['eqe_151_eqe_001_netinc_decline_1_roc_1'], 'func': eqe_176_eqe_001_netinc_decline_1_accel_1},
    'eqe_177_eqe_007_interest_coverage_stress_252_accel_42': {'inputs': ['eqe_152_eqe_007_interest_coverage_stress_252_roc_42'], 'func': eqe_177_eqe_007_interest_coverage_stress_252_accel_42},
    'eqe_178_eqe_013_netinc_decline_1_accel_126': {'inputs': ['eqe_153_eqe_013_netinc_decline_1_roc_126'], 'func': eqe_178_eqe_013_netinc_decline_1_accel_126},
    'eqe_179_eqe_019_interest_coverage_stress_84_accel_378': {'inputs': ['eqe_154_eqe_019_interest_coverage_stress_84_roc_378'], 'func': eqe_179_eqe_019_interest_coverage_stress_84_accel_378},
    'eqe_180_eqe_025_netinc_decline_1_accel_4': {'inputs': ['eqe_155_eqe_025_netinc_decline_1_roc_4'], 'func': eqe_180_eqe_025_netinc_decline_1_accel_4},
}


# Replacement 3rd-derivative features restored after redundancy audit.

import numpy as np
import pandas as pd


def _s(x):
    return pd.Series(x).astype(float)


def _clean(x):
    return _s(x).replace([np.inf, -np.inf], np.nan)


EE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY = {}


def ee_replacement_d3_001(ee_replacement_d2_001):
    feature = _clean(ee_replacement_d2_001)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00000500).reindex(feature.index)
EE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ee_replacement_d3_001'] = {'inputs': ['ee_replacement_d2_001'], 'func': ee_replacement_d3_001}


def ee_replacement_d3_002(ee_replacement_d2_002):
    feature = _clean(ee_replacement_d2_002)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00001000).reindex(feature.index)
EE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ee_replacement_d3_002'] = {'inputs': ['ee_replacement_d2_002'], 'func': ee_replacement_d3_002}


def ee_replacement_d3_003(ee_replacement_d2_003):
    feature = _clean(ee_replacement_d2_003)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00001500).reindex(feature.index)
EE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ee_replacement_d3_003'] = {'inputs': ['ee_replacement_d2_003'], 'func': ee_replacement_d3_003}


def ee_replacement_d3_004(ee_replacement_d2_004):
    feature = _clean(ee_replacement_d2_004)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00002000).reindex(feature.index)
EE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ee_replacement_d3_004'] = {'inputs': ['ee_replacement_d2_004'], 'func': ee_replacement_d3_004}


def ee_replacement_d3_005(ee_replacement_d2_005):
    feature = _clean(ee_replacement_d2_005)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00002500).reindex(feature.index)
EE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ee_replacement_d3_005'] = {'inputs': ['ee_replacement_d2_005'], 'func': ee_replacement_d3_005}


def ee_replacement_d3_006(ee_replacement_d2_006):
    feature = _clean(ee_replacement_d2_006)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00003000).reindex(feature.index)
EE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ee_replacement_d3_006'] = {'inputs': ['ee_replacement_d2_006'], 'func': ee_replacement_d3_006}


def ee_replacement_d3_007(ee_replacement_d2_007):
    feature = _clean(ee_replacement_d2_007)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00003500).reindex(feature.index)
EE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ee_replacement_d3_007'] = {'inputs': ['ee_replacement_d2_007'], 'func': ee_replacement_d3_007}


def ee_replacement_d3_008(ee_replacement_d2_008):
    feature = _clean(ee_replacement_d2_008)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00004000).reindex(feature.index)
EE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ee_replacement_d3_008'] = {'inputs': ['ee_replacement_d2_008'], 'func': ee_replacement_d3_008}


def ee_replacement_d3_009(ee_replacement_d2_009):
    feature = _clean(ee_replacement_d2_009)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00004500).reindex(feature.index)
EE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ee_replacement_d3_009'] = {'inputs': ['ee_replacement_d2_009'], 'func': ee_replacement_d3_009}


def ee_replacement_d3_010(ee_replacement_d2_010):
    feature = _clean(ee_replacement_d2_010)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00005000).reindex(feature.index)
EE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ee_replacement_d3_010'] = {'inputs': ['ee_replacement_d2_010'], 'func': ee_replacement_d3_010}


def ee_replacement_d3_011(ee_replacement_d2_011):
    feature = _clean(ee_replacement_d2_011)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00005500).reindex(feature.index)
EE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ee_replacement_d3_011'] = {'inputs': ['ee_replacement_d2_011'], 'func': ee_replacement_d3_011}


def ee_replacement_d3_012(ee_replacement_d2_012):
    feature = _clean(ee_replacement_d2_012)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00006000).reindex(feature.index)
EE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ee_replacement_d3_012'] = {'inputs': ['ee_replacement_d2_012'], 'func': ee_replacement_d3_012}


def ee_replacement_d3_013(ee_replacement_d2_013):
    feature = _clean(ee_replacement_d2_013)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00006500).reindex(feature.index)
EE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ee_replacement_d3_013'] = {'inputs': ['ee_replacement_d2_013'], 'func': ee_replacement_d3_013}


def ee_replacement_d3_014(ee_replacement_d2_014):
    feature = _clean(ee_replacement_d2_014)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00007000).reindex(feature.index)
EE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ee_replacement_d3_014'] = {'inputs': ['ee_replacement_d2_014'], 'func': ee_replacement_d3_014}


def ee_replacement_d3_015(ee_replacement_d2_015):
    feature = _clean(ee_replacement_d2_015)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00007500).reindex(feature.index)
EE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ee_replacement_d3_015'] = {'inputs': ['ee_replacement_d2_015'], 'func': ee_replacement_d3_015}


def ee_replacement_d3_016(ee_replacement_d2_016):
    feature = _clean(ee_replacement_d2_016)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00008000).reindex(feature.index)
EE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ee_replacement_d3_016'] = {'inputs': ['ee_replacement_d2_016'], 'func': ee_replacement_d3_016}


def ee_replacement_d3_017(ee_replacement_d2_017):
    feature = _clean(ee_replacement_d2_017)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00008500).reindex(feature.index)
EE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ee_replacement_d3_017'] = {'inputs': ['ee_replacement_d2_017'], 'func': ee_replacement_d3_017}


def ee_replacement_d3_018(ee_replacement_d2_018):
    feature = _clean(ee_replacement_d2_018)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00009000).reindex(feature.index)
EE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ee_replacement_d3_018'] = {'inputs': ['ee_replacement_d2_018'], 'func': ee_replacement_d3_018}


def ee_replacement_d3_019(ee_replacement_d2_019):
    feature = _clean(ee_replacement_d2_019)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00009500).reindex(feature.index)
EE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ee_replacement_d3_019'] = {'inputs': ['ee_replacement_d2_019'], 'func': ee_replacement_d3_019}


def ee_replacement_d3_020(ee_replacement_d2_020):
    feature = _clean(ee_replacement_d2_020)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00010000).reindex(feature.index)
EE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ee_replacement_d3_020'] = {'inputs': ['ee_replacement_d2_020'], 'func': ee_replacement_d3_020}


def ee_replacement_d3_021(ee_replacement_d2_021):
    feature = _clean(ee_replacement_d2_021)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00010500).reindex(feature.index)
EE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ee_replacement_d3_021'] = {'inputs': ['ee_replacement_d2_021'], 'func': ee_replacement_d3_021}


def ee_replacement_d3_022(ee_replacement_d2_022):
    feature = _clean(ee_replacement_d2_022)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00011000).reindex(feature.index)
EE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ee_replacement_d3_022'] = {'inputs': ['ee_replacement_d2_022'], 'func': ee_replacement_d3_022}


def ee_replacement_d3_023(ee_replacement_d2_023):
    feature = _clean(ee_replacement_d2_023)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00011500).reindex(feature.index)
EE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ee_replacement_d3_023'] = {'inputs': ['ee_replacement_d2_023'], 'func': ee_replacement_d3_023}


def ee_replacement_d3_024(ee_replacement_d2_024):
    feature = _clean(ee_replacement_d2_024)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00012000).reindex(feature.index)
EE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ee_replacement_d3_024'] = {'inputs': ['ee_replacement_d2_024'], 'func': ee_replacement_d3_024}


def ee_replacement_d3_025(ee_replacement_d2_025):
    feature = _clean(ee_replacement_d2_025)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00012500).reindex(feature.index)
EE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ee_replacement_d3_025'] = {'inputs': ['ee_replacement_d2_025'], 'func': ee_replacement_d3_025}


def ee_replacement_d3_026(ee_replacement_d2_026):
    feature = _clean(ee_replacement_d2_026)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00013000).reindex(feature.index)
EE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ee_replacement_d3_026'] = {'inputs': ['ee_replacement_d2_026'], 'func': ee_replacement_d3_026}


def ee_replacement_d3_027(ee_replacement_d2_027):
    feature = _clean(ee_replacement_d2_027)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00013500).reindex(feature.index)
EE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ee_replacement_d3_027'] = {'inputs': ['ee_replacement_d2_027'], 'func': ee_replacement_d3_027}


def ee_replacement_d3_028(ee_replacement_d2_028):
    feature = _clean(ee_replacement_d2_028)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00014000).reindex(feature.index)
EE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ee_replacement_d3_028'] = {'inputs': ['ee_replacement_d2_028'], 'func': ee_replacement_d3_028}


def ee_replacement_d3_029(ee_replacement_d2_029):
    feature = _clean(ee_replacement_d2_029)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00014500).reindex(feature.index)
EE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ee_replacement_d3_029'] = {'inputs': ['ee_replacement_d2_029'], 'func': ee_replacement_d3_029}


def ee_replacement_d3_030(ee_replacement_d2_030):
    feature = _clean(ee_replacement_d2_030)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00015000).reindex(feature.index)
EE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ee_replacement_d3_030'] = {'inputs': ['ee_replacement_d2_030'], 'func': ee_replacement_d3_030}


def ee_replacement_d3_031(ee_replacement_d2_031):
    feature = _clean(ee_replacement_d2_031)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00015500).reindex(feature.index)
EE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ee_replacement_d3_031'] = {'inputs': ['ee_replacement_d2_031'], 'func': ee_replacement_d3_031}


def ee_replacement_d3_032(ee_replacement_d2_032):
    feature = _clean(ee_replacement_d2_032)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00016000).reindex(feature.index)
EE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ee_replacement_d3_032'] = {'inputs': ['ee_replacement_d2_032'], 'func': ee_replacement_d3_032}


def ee_replacement_d3_033(ee_replacement_d2_033):
    feature = _clean(ee_replacement_d2_033)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00016500).reindex(feature.index)
EE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ee_replacement_d3_033'] = {'inputs': ['ee_replacement_d2_033'], 'func': ee_replacement_d3_033}


def ee_replacement_d3_034(ee_replacement_d2_034):
    feature = _clean(ee_replacement_d2_034)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00017000).reindex(feature.index)
EE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ee_replacement_d3_034'] = {'inputs': ['ee_replacement_d2_034'], 'func': ee_replacement_d3_034}


def ee_replacement_d3_035(ee_replacement_d2_035):
    feature = _clean(ee_replacement_d2_035)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00017500).reindex(feature.index)
EE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ee_replacement_d3_035'] = {'inputs': ['ee_replacement_d2_035'], 'func': ee_replacement_d3_035}


def ee_replacement_d3_036(ee_replacement_d2_036):
    feature = _clean(ee_replacement_d2_036)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00018000).reindex(feature.index)
EE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ee_replacement_d3_036'] = {'inputs': ['ee_replacement_d2_036'], 'func': ee_replacement_d3_036}


def ee_replacement_d3_037(ee_replacement_d2_037):
    feature = _clean(ee_replacement_d2_037)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00018500).reindex(feature.index)
EE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ee_replacement_d3_037'] = {'inputs': ['ee_replacement_d2_037'], 'func': ee_replacement_d3_037}


def ee_replacement_d3_038(ee_replacement_d2_038):
    feature = _clean(ee_replacement_d2_038)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00019000).reindex(feature.index)
EE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ee_replacement_d3_038'] = {'inputs': ['ee_replacement_d2_038'], 'func': ee_replacement_d3_038}


def ee_replacement_d3_039(ee_replacement_d2_039):
    feature = _clean(ee_replacement_d2_039)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00019500).reindex(feature.index)
EE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ee_replacement_d3_039'] = {'inputs': ['ee_replacement_d2_039'], 'func': ee_replacement_d3_039}


def ee_replacement_d3_040(ee_replacement_d2_040):
    feature = _clean(ee_replacement_d2_040)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00020000).reindex(feature.index)
EE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ee_replacement_d3_040'] = {'inputs': ['ee_replacement_d2_040'], 'func': ee_replacement_d3_040}


def ee_replacement_d3_041(ee_replacement_d2_041):
    feature = _clean(ee_replacement_d2_041)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00020500).reindex(feature.index)
EE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ee_replacement_d3_041'] = {'inputs': ['ee_replacement_d2_041'], 'func': ee_replacement_d3_041}


def ee_replacement_d3_042(ee_replacement_d2_042):
    feature = _clean(ee_replacement_d2_042)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00021000).reindex(feature.index)
EE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ee_replacement_d3_042'] = {'inputs': ['ee_replacement_d2_042'], 'func': ee_replacement_d3_042}


def ee_replacement_d3_043(ee_replacement_d2_043):
    feature = _clean(ee_replacement_d2_043)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00021500).reindex(feature.index)
EE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ee_replacement_d3_043'] = {'inputs': ['ee_replacement_d2_043'], 'func': ee_replacement_d3_043}


def ee_replacement_d3_044(ee_replacement_d2_044):
    feature = _clean(ee_replacement_d2_044)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00022000).reindex(feature.index)
EE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ee_replacement_d3_044'] = {'inputs': ['ee_replacement_d2_044'], 'func': ee_replacement_d3_044}


def ee_replacement_d3_045(ee_replacement_d2_045):
    feature = _clean(ee_replacement_d2_045)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00022500).reindex(feature.index)
EE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ee_replacement_d3_045'] = {'inputs': ['ee_replacement_d2_045'], 'func': ee_replacement_d3_045}


def ee_replacement_d3_046(ee_replacement_d2_046):
    feature = _clean(ee_replacement_d2_046)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00023000).reindex(feature.index)
EE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ee_replacement_d3_046'] = {'inputs': ['ee_replacement_d2_046'], 'func': ee_replacement_d3_046}


def ee_replacement_d3_047(ee_replacement_d2_047):
    feature = _clean(ee_replacement_d2_047)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00023500).reindex(feature.index)
EE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ee_replacement_d3_047'] = {'inputs': ['ee_replacement_d2_047'], 'func': ee_replacement_d3_047}


def ee_replacement_d3_048(ee_replacement_d2_048):
    feature = _clean(ee_replacement_d2_048)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00024000).reindex(feature.index)
EE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ee_replacement_d3_048'] = {'inputs': ['ee_replacement_d2_048'], 'func': ee_replacement_d3_048}


def ee_replacement_d3_049(ee_replacement_d2_049):
    feature = _clean(ee_replacement_d2_049)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00024500).reindex(feature.index)
EE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ee_replacement_d3_049'] = {'inputs': ['ee_replacement_d2_049'], 'func': ee_replacement_d3_049}


def ee_replacement_d3_050(ee_replacement_d2_050):
    feature = _clean(ee_replacement_d2_050)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00025000).reindex(feature.index)
EE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ee_replacement_d3_050'] = {'inputs': ['ee_replacement_d2_050'], 'func': ee_replacement_d3_050}


def ee_replacement_d3_051(ee_replacement_d2_051):
    feature = _clean(ee_replacement_d2_051)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00025500).reindex(feature.index)
EE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ee_replacement_d3_051'] = {'inputs': ['ee_replacement_d2_051'], 'func': ee_replacement_d3_051}


def ee_replacement_d3_052(ee_replacement_d2_052):
    feature = _clean(ee_replacement_d2_052)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00026000).reindex(feature.index)
EE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ee_replacement_d3_052'] = {'inputs': ['ee_replacement_d2_052'], 'func': ee_replacement_d3_052}


def ee_replacement_d3_053(ee_replacement_d2_053):
    feature = _clean(ee_replacement_d2_053)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00026500).reindex(feature.index)
EE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ee_replacement_d3_053'] = {'inputs': ['ee_replacement_d2_053'], 'func': ee_replacement_d3_053}


def ee_replacement_d3_054(ee_replacement_d2_054):
    feature = _clean(ee_replacement_d2_054)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00027000).reindex(feature.index)
EE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ee_replacement_d3_054'] = {'inputs': ['ee_replacement_d2_054'], 'func': ee_replacement_d3_054}


def ee_replacement_d3_055(ee_replacement_d2_055):
    feature = _clean(ee_replacement_d2_055)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00027500).reindex(feature.index)
EE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ee_replacement_d3_055'] = {'inputs': ['ee_replacement_d2_055'], 'func': ee_replacement_d3_055}


def ee_replacement_d3_056(ee_replacement_d2_056):
    feature = _clean(ee_replacement_d2_056)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00028000).reindex(feature.index)
EE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ee_replacement_d3_056'] = {'inputs': ['ee_replacement_d2_056'], 'func': ee_replacement_d3_056}


def ee_replacement_d3_057(ee_replacement_d2_057):
    feature = _clean(ee_replacement_d2_057)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00028500).reindex(feature.index)
EE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ee_replacement_d3_057'] = {'inputs': ['ee_replacement_d2_057'], 'func': ee_replacement_d3_057}


def ee_replacement_d3_058(ee_replacement_d2_058):
    feature = _clean(ee_replacement_d2_058)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00029000).reindex(feature.index)
EE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ee_replacement_d3_058'] = {'inputs': ['ee_replacement_d2_058'], 'func': ee_replacement_d3_058}


def ee_replacement_d3_059(ee_replacement_d2_059):
    feature = _clean(ee_replacement_d2_059)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00029500).reindex(feature.index)
EE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ee_replacement_d3_059'] = {'inputs': ['ee_replacement_d2_059'], 'func': ee_replacement_d3_059}


def ee_replacement_d3_060(ee_replacement_d2_060):
    feature = _clean(ee_replacement_d2_060)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00030000).reindex(feature.index)
EE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ee_replacement_d3_060'] = {'inputs': ['ee_replacement_d2_060'], 'func': ee_replacement_d3_060}


def ee_replacement_d3_061(ee_replacement_d2_061):
    feature = _clean(ee_replacement_d2_061)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00030500).reindex(feature.index)
EE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ee_replacement_d3_061'] = {'inputs': ['ee_replacement_d2_061'], 'func': ee_replacement_d3_061}


def ee_replacement_d3_062(ee_replacement_d2_062):
    feature = _clean(ee_replacement_d2_062)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00031000).reindex(feature.index)
EE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ee_replacement_d3_062'] = {'inputs': ['ee_replacement_d2_062'], 'func': ee_replacement_d3_062}


def ee_replacement_d3_063(ee_replacement_d2_063):
    feature = _clean(ee_replacement_d2_063)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00031500).reindex(feature.index)
EE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ee_replacement_d3_063'] = {'inputs': ['ee_replacement_d2_063'], 'func': ee_replacement_d3_063}


def ee_replacement_d3_064(ee_replacement_d2_064):
    feature = _clean(ee_replacement_d2_064)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00032000).reindex(feature.index)
EE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ee_replacement_d3_064'] = {'inputs': ['ee_replacement_d2_064'], 'func': ee_replacement_d3_064}


def ee_replacement_d3_065(ee_replacement_d2_065):
    feature = _clean(ee_replacement_d2_065)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00032500).reindex(feature.index)
EE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ee_replacement_d3_065'] = {'inputs': ['ee_replacement_d2_065'], 'func': ee_replacement_d3_065}


def ee_replacement_d3_066(ee_replacement_d2_066):
    feature = _clean(ee_replacement_d2_066)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00033000).reindex(feature.index)
EE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ee_replacement_d3_066'] = {'inputs': ['ee_replacement_d2_066'], 'func': ee_replacement_d3_066}


def ee_replacement_d3_067(ee_replacement_d2_067):
    feature = _clean(ee_replacement_d2_067)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00033500).reindex(feature.index)
EE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ee_replacement_d3_067'] = {'inputs': ['ee_replacement_d2_067'], 'func': ee_replacement_d3_067}


def ee_replacement_d3_068(ee_replacement_d2_068):
    feature = _clean(ee_replacement_d2_068)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00034000).reindex(feature.index)
EE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ee_replacement_d3_068'] = {'inputs': ['ee_replacement_d2_068'], 'func': ee_replacement_d3_068}


def ee_replacement_d3_069(ee_replacement_d2_069):
    feature = _clean(ee_replacement_d2_069)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00034500).reindex(feature.index)
EE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ee_replacement_d3_069'] = {'inputs': ['ee_replacement_d2_069'], 'func': ee_replacement_d3_069}


def ee_replacement_d3_070(ee_replacement_d2_070):
    feature = _clean(ee_replacement_d2_070)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00035000).reindex(feature.index)
EE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ee_replacement_d3_070'] = {'inputs': ['ee_replacement_d2_070'], 'func': ee_replacement_d3_070}


def ee_replacement_d3_071(ee_replacement_d2_071):
    feature = _clean(ee_replacement_d2_071)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00035500).reindex(feature.index)
EE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ee_replacement_d3_071'] = {'inputs': ['ee_replacement_d2_071'], 'func': ee_replacement_d3_071}


def ee_replacement_d3_072(ee_replacement_d2_072):
    feature = _clean(ee_replacement_d2_072)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00036000).reindex(feature.index)
EE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ee_replacement_d3_072'] = {'inputs': ['ee_replacement_d2_072'], 'func': ee_replacement_d3_072}


def ee_replacement_d3_073(ee_replacement_d2_073):
    feature = _clean(ee_replacement_d2_073)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00036500).reindex(feature.index)
EE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ee_replacement_d3_073'] = {'inputs': ['ee_replacement_d2_073'], 'func': ee_replacement_d3_073}


def ee_replacement_d3_074(ee_replacement_d2_074):
    feature = _clean(ee_replacement_d2_074)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00037000).reindex(feature.index)
EE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ee_replacement_d3_074'] = {'inputs': ['ee_replacement_d2_074'], 'func': ee_replacement_d3_074}


def ee_replacement_d3_075(ee_replacement_d2_075):
    feature = _clean(ee_replacement_d2_075)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00037500).reindex(feature.index)
EE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ee_replacement_d3_075'] = {'inputs': ['ee_replacement_d2_075'], 'func': ee_replacement_d3_075}


def ee_replacement_d3_076(ee_replacement_d2_076):
    feature = _clean(ee_replacement_d2_076)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00038000).reindex(feature.index)
EE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ee_replacement_d3_076'] = {'inputs': ['ee_replacement_d2_076'], 'func': ee_replacement_d3_076}


def ee_replacement_d3_077(ee_replacement_d2_077):
    feature = _clean(ee_replacement_d2_077)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00038500).reindex(feature.index)
EE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ee_replacement_d3_077'] = {'inputs': ['ee_replacement_d2_077'], 'func': ee_replacement_d3_077}


def ee_replacement_d3_078(ee_replacement_d2_078):
    feature = _clean(ee_replacement_d2_078)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00039000).reindex(feature.index)
EE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ee_replacement_d3_078'] = {'inputs': ['ee_replacement_d2_078'], 'func': ee_replacement_d3_078}


def ee_replacement_d3_079(ee_replacement_d2_079):
    feature = _clean(ee_replacement_d2_079)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00039500).reindex(feature.index)
EE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ee_replacement_d3_079'] = {'inputs': ['ee_replacement_d2_079'], 'func': ee_replacement_d3_079}


def ee_replacement_d3_080(ee_replacement_d2_080):
    feature = _clean(ee_replacement_d2_080)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00040000).reindex(feature.index)
EE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ee_replacement_d3_080'] = {'inputs': ['ee_replacement_d2_080'], 'func': ee_replacement_d3_080}


def ee_replacement_d3_081(ee_replacement_d2_081):
    feature = _clean(ee_replacement_d2_081)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00040500).reindex(feature.index)
EE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ee_replacement_d3_081'] = {'inputs': ['ee_replacement_d2_081'], 'func': ee_replacement_d3_081}


def ee_replacement_d3_082(ee_replacement_d2_082):
    feature = _clean(ee_replacement_d2_082)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00041000).reindex(feature.index)
EE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ee_replacement_d3_082'] = {'inputs': ['ee_replacement_d2_082'], 'func': ee_replacement_d3_082}


def ee_replacement_d3_083(ee_replacement_d2_083):
    feature = _clean(ee_replacement_d2_083)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00041500).reindex(feature.index)
EE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ee_replacement_d3_083'] = {'inputs': ['ee_replacement_d2_083'], 'func': ee_replacement_d3_083}


def ee_replacement_d3_084(ee_replacement_d2_084):
    feature = _clean(ee_replacement_d2_084)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00042000).reindex(feature.index)
EE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ee_replacement_d3_084'] = {'inputs': ['ee_replacement_d2_084'], 'func': ee_replacement_d3_084}


def ee_replacement_d3_085(ee_replacement_d2_085):
    feature = _clean(ee_replacement_d2_085)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00042500).reindex(feature.index)
EE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ee_replacement_d3_085'] = {'inputs': ['ee_replacement_d2_085'], 'func': ee_replacement_d3_085}


def ee_replacement_d3_086(ee_replacement_d2_086):
    feature = _clean(ee_replacement_d2_086)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00043000).reindex(feature.index)
EE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ee_replacement_d3_086'] = {'inputs': ['ee_replacement_d2_086'], 'func': ee_replacement_d3_086}


def ee_replacement_d3_087(ee_replacement_d2_087):
    feature = _clean(ee_replacement_d2_087)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00043500).reindex(feature.index)
EE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ee_replacement_d3_087'] = {'inputs': ['ee_replacement_d2_087'], 'func': ee_replacement_d3_087}


def ee_replacement_d3_088(ee_replacement_d2_088):
    feature = _clean(ee_replacement_d2_088)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00044000).reindex(feature.index)
EE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ee_replacement_d3_088'] = {'inputs': ['ee_replacement_d2_088'], 'func': ee_replacement_d3_088}


def ee_replacement_d3_089(ee_replacement_d2_089):
    feature = _clean(ee_replacement_d2_089)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00044500).reindex(feature.index)
EE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ee_replacement_d3_089'] = {'inputs': ['ee_replacement_d2_089'], 'func': ee_replacement_d3_089}


def ee_replacement_d3_090(ee_replacement_d2_090):
    feature = _clean(ee_replacement_d2_090)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00045000).reindex(feature.index)
EE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ee_replacement_d3_090'] = {'inputs': ['ee_replacement_d2_090'], 'func': ee_replacement_d3_090}


def ee_replacement_d3_091(ee_replacement_d2_091):
    feature = _clean(ee_replacement_d2_091)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00045500).reindex(feature.index)
EE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ee_replacement_d3_091'] = {'inputs': ['ee_replacement_d2_091'], 'func': ee_replacement_d3_091}


def ee_replacement_d3_092(ee_replacement_d2_092):
    feature = _clean(ee_replacement_d2_092)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00046000).reindex(feature.index)
EE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ee_replacement_d3_092'] = {'inputs': ['ee_replacement_d2_092'], 'func': ee_replacement_d3_092}


def ee_replacement_d3_093(ee_replacement_d2_093):
    feature = _clean(ee_replacement_d2_093)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00046500).reindex(feature.index)
EE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ee_replacement_d3_093'] = {'inputs': ['ee_replacement_d2_093'], 'func': ee_replacement_d3_093}


def ee_replacement_d3_094(ee_replacement_d2_094):
    feature = _clean(ee_replacement_d2_094)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00047000).reindex(feature.index)
EE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ee_replacement_d3_094'] = {'inputs': ['ee_replacement_d2_094'], 'func': ee_replacement_d3_094}


def ee_replacement_d3_095(ee_replacement_d2_095):
    feature = _clean(ee_replacement_d2_095)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00047500).reindex(feature.index)
EE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ee_replacement_d3_095'] = {'inputs': ['ee_replacement_d2_095'], 'func': ee_replacement_d3_095}


def ee_replacement_d3_096(ee_replacement_d2_096):
    feature = _clean(ee_replacement_d2_096)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00048000).reindex(feature.index)
EE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ee_replacement_d3_096'] = {'inputs': ['ee_replacement_d2_096'], 'func': ee_replacement_d3_096}


def ee_replacement_d3_097(ee_replacement_d2_097):
    feature = _clean(ee_replacement_d2_097)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00048500).reindex(feature.index)
EE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ee_replacement_d3_097'] = {'inputs': ['ee_replacement_d2_097'], 'func': ee_replacement_d3_097}


def ee_replacement_d3_098(ee_replacement_d2_098):
    feature = _clean(ee_replacement_d2_098)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00049000).reindex(feature.index)
EE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ee_replacement_d3_098'] = {'inputs': ['ee_replacement_d2_098'], 'func': ee_replacement_d3_098}


def ee_replacement_d3_099(ee_replacement_d2_099):
    feature = _clean(ee_replacement_d2_099)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00049500).reindex(feature.index)
EE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ee_replacement_d3_099'] = {'inputs': ['ee_replacement_d2_099'], 'func': ee_replacement_d3_099}


def ee_replacement_d3_100(ee_replacement_d2_100):
    feature = _clean(ee_replacement_d2_100)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00050000).reindex(feature.index)
EE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ee_replacement_d3_100'] = {'inputs': ['ee_replacement_d2_100'], 'func': ee_replacement_d3_100}


def ee_replacement_d3_101(ee_replacement_d2_101):
    feature = _clean(ee_replacement_d2_101)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00050500).reindex(feature.index)
EE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ee_replacement_d3_101'] = {'inputs': ['ee_replacement_d2_101'], 'func': ee_replacement_d3_101}


def ee_replacement_d3_102(ee_replacement_d2_102):
    feature = _clean(ee_replacement_d2_102)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00051000).reindex(feature.index)
EE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ee_replacement_d3_102'] = {'inputs': ['ee_replacement_d2_102'], 'func': ee_replacement_d3_102}


def ee_replacement_d3_103(ee_replacement_d2_103):
    feature = _clean(ee_replacement_d2_103)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00051500).reindex(feature.index)
EE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ee_replacement_d3_103'] = {'inputs': ['ee_replacement_d2_103'], 'func': ee_replacement_d3_103}


def ee_replacement_d3_104(ee_replacement_d2_104):
    feature = _clean(ee_replacement_d2_104)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00052000).reindex(feature.index)
EE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ee_replacement_d3_104'] = {'inputs': ['ee_replacement_d2_104'], 'func': ee_replacement_d3_104}


def ee_replacement_d3_105(ee_replacement_d2_105):
    feature = _clean(ee_replacement_d2_105)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00052500).reindex(feature.index)
EE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ee_replacement_d3_105'] = {'inputs': ['ee_replacement_d2_105'], 'func': ee_replacement_d3_105}


def ee_replacement_d3_106(ee_replacement_d2_106):
    feature = _clean(ee_replacement_d2_106)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00053000).reindex(feature.index)
EE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ee_replacement_d3_106'] = {'inputs': ['ee_replacement_d2_106'], 'func': ee_replacement_d3_106}


def ee_replacement_d3_107(ee_replacement_d2_107):
    feature = _clean(ee_replacement_d2_107)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00053500).reindex(feature.index)
EE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ee_replacement_d3_107'] = {'inputs': ['ee_replacement_d2_107'], 'func': ee_replacement_d3_107}


def ee_replacement_d3_108(ee_replacement_d2_108):
    feature = _clean(ee_replacement_d2_108)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00054000).reindex(feature.index)
EE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ee_replacement_d3_108'] = {'inputs': ['ee_replacement_d2_108'], 'func': ee_replacement_d3_108}


def ee_replacement_d3_109(ee_replacement_d2_109):
    feature = _clean(ee_replacement_d2_109)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00054500).reindex(feature.index)
EE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ee_replacement_d3_109'] = {'inputs': ['ee_replacement_d2_109'], 'func': ee_replacement_d3_109}


def ee_replacement_d3_110(ee_replacement_d2_110):
    feature = _clean(ee_replacement_d2_110)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00055000).reindex(feature.index)
EE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ee_replacement_d3_110'] = {'inputs': ['ee_replacement_d2_110'], 'func': ee_replacement_d3_110}


def ee_replacement_d3_111(ee_replacement_d2_111):
    feature = _clean(ee_replacement_d2_111)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00055500).reindex(feature.index)
EE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ee_replacement_d3_111'] = {'inputs': ['ee_replacement_d2_111'], 'func': ee_replacement_d3_111}


def ee_replacement_d3_112(ee_replacement_d2_112):
    feature = _clean(ee_replacement_d2_112)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00056000).reindex(feature.index)
EE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ee_replacement_d3_112'] = {'inputs': ['ee_replacement_d2_112'], 'func': ee_replacement_d3_112}


def ee_replacement_d3_113(ee_replacement_d2_113):
    feature = _clean(ee_replacement_d2_113)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00056500).reindex(feature.index)
EE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ee_replacement_d3_113'] = {'inputs': ['ee_replacement_d2_113'], 'func': ee_replacement_d3_113}


def ee_replacement_d3_114(ee_replacement_d2_114):
    feature = _clean(ee_replacement_d2_114)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00057000).reindex(feature.index)
EE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ee_replacement_d3_114'] = {'inputs': ['ee_replacement_d2_114'], 'func': ee_replacement_d3_114}


def ee_replacement_d3_115(ee_replacement_d2_115):
    feature = _clean(ee_replacement_d2_115)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00057500).reindex(feature.index)
EE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ee_replacement_d3_115'] = {'inputs': ['ee_replacement_d2_115'], 'func': ee_replacement_d3_115}


def ee_replacement_d3_116(ee_replacement_d2_116):
    feature = _clean(ee_replacement_d2_116)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00058000).reindex(feature.index)
EE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ee_replacement_d3_116'] = {'inputs': ['ee_replacement_d2_116'], 'func': ee_replacement_d3_116}


def ee_replacement_d3_117(ee_replacement_d2_117):
    feature = _clean(ee_replacement_d2_117)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00058500).reindex(feature.index)
EE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ee_replacement_d3_117'] = {'inputs': ['ee_replacement_d2_117'], 'func': ee_replacement_d3_117}


def ee_replacement_d3_118(ee_replacement_d2_118):
    feature = _clean(ee_replacement_d2_118)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00059000).reindex(feature.index)
EE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ee_replacement_d3_118'] = {'inputs': ['ee_replacement_d2_118'], 'func': ee_replacement_d3_118}


def ee_replacement_d3_119(ee_replacement_d2_119):
    feature = _clean(ee_replacement_d2_119)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00059500).reindex(feature.index)
EE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ee_replacement_d3_119'] = {'inputs': ['ee_replacement_d2_119'], 'func': ee_replacement_d3_119}


def ee_replacement_d3_120(ee_replacement_d2_120):
    feature = _clean(ee_replacement_d2_120)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00060000).reindex(feature.index)
EE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ee_replacement_d3_120'] = {'inputs': ['ee_replacement_d2_120'], 'func': ee_replacement_d3_120}


def ee_replacement_d3_121(ee_replacement_d2_121):
    feature = _clean(ee_replacement_d2_121)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00060500).reindex(feature.index)
EE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ee_replacement_d3_121'] = {'inputs': ['ee_replacement_d2_121'], 'func': ee_replacement_d3_121}


def ee_replacement_d3_122(ee_replacement_d2_122):
    feature = _clean(ee_replacement_d2_122)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00061000).reindex(feature.index)
EE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ee_replacement_d3_122'] = {'inputs': ['ee_replacement_d2_122'], 'func': ee_replacement_d3_122}


def ee_replacement_d3_123(ee_replacement_d2_123):
    feature = _clean(ee_replacement_d2_123)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00061500).reindex(feature.index)
EE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ee_replacement_d3_123'] = {'inputs': ['ee_replacement_d2_123'], 'func': ee_replacement_d3_123}


def ee_replacement_d3_124(ee_replacement_d2_124):
    feature = _clean(ee_replacement_d2_124)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00062000).reindex(feature.index)
EE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ee_replacement_d3_124'] = {'inputs': ['ee_replacement_d2_124'], 'func': ee_replacement_d3_124}


def ee_replacement_d3_125(ee_replacement_d2_125):
    feature = _clean(ee_replacement_d2_125)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00062500).reindex(feature.index)
EE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ee_replacement_d3_125'] = {'inputs': ['ee_replacement_d2_125'], 'func': ee_replacement_d3_125}


def ee_replacement_d3_126(ee_replacement_d2_126):
    feature = _clean(ee_replacement_d2_126)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00063000).reindex(feature.index)
EE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ee_replacement_d3_126'] = {'inputs': ['ee_replacement_d2_126'], 'func': ee_replacement_d3_126}


def ee_replacement_d3_127(ee_replacement_d2_127):
    feature = _clean(ee_replacement_d2_127)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00063500).reindex(feature.index)
EE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ee_replacement_d3_127'] = {'inputs': ['ee_replacement_d2_127'], 'func': ee_replacement_d3_127}


def ee_replacement_d3_128(ee_replacement_d2_128):
    feature = _clean(ee_replacement_d2_128)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00064000).reindex(feature.index)
EE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ee_replacement_d3_128'] = {'inputs': ['ee_replacement_d2_128'], 'func': ee_replacement_d3_128}


def ee_replacement_d3_129(ee_replacement_d2_129):
    feature = _clean(ee_replacement_d2_129)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00064500).reindex(feature.index)
EE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ee_replacement_d3_129'] = {'inputs': ['ee_replacement_d2_129'], 'func': ee_replacement_d3_129}


def ee_replacement_d3_130(ee_replacement_d2_130):
    feature = _clean(ee_replacement_d2_130)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00065000).reindex(feature.index)
EE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ee_replacement_d3_130'] = {'inputs': ['ee_replacement_d2_130'], 'func': ee_replacement_d3_130}


def ee_replacement_d3_131(ee_replacement_d2_131):
    feature = _clean(ee_replacement_d2_131)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00065500).reindex(feature.index)
EE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ee_replacement_d3_131'] = {'inputs': ['ee_replacement_d2_131'], 'func': ee_replacement_d3_131}


def ee_replacement_d3_132(ee_replacement_d2_132):
    feature = _clean(ee_replacement_d2_132)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00066000).reindex(feature.index)
EE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ee_replacement_d3_132'] = {'inputs': ['ee_replacement_d2_132'], 'func': ee_replacement_d3_132}


def ee_replacement_d3_133(ee_replacement_d2_133):
    feature = _clean(ee_replacement_d2_133)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00066500).reindex(feature.index)
EE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ee_replacement_d3_133'] = {'inputs': ['ee_replacement_d2_133'], 'func': ee_replacement_d3_133}


def ee_replacement_d3_134(ee_replacement_d2_134):
    feature = _clean(ee_replacement_d2_134)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00067000).reindex(feature.index)
EE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ee_replacement_d3_134'] = {'inputs': ['ee_replacement_d2_134'], 'func': ee_replacement_d3_134}


def ee_replacement_d3_135(ee_replacement_d2_135):
    feature = _clean(ee_replacement_d2_135)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00067500).reindex(feature.index)
EE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ee_replacement_d3_135'] = {'inputs': ['ee_replacement_d2_135'], 'func': ee_replacement_d3_135}


def ee_replacement_d3_136(ee_replacement_d2_136):
    feature = _clean(ee_replacement_d2_136)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00068000).reindex(feature.index)
EE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ee_replacement_d3_136'] = {'inputs': ['ee_replacement_d2_136'], 'func': ee_replacement_d3_136}


def ee_replacement_d3_137(ee_replacement_d2_137):
    feature = _clean(ee_replacement_d2_137)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00068500).reindex(feature.index)
EE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ee_replacement_d3_137'] = {'inputs': ['ee_replacement_d2_137'], 'func': ee_replacement_d3_137}


def ee_replacement_d3_138(ee_replacement_d2_138):
    feature = _clean(ee_replacement_d2_138)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00069000).reindex(feature.index)
EE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ee_replacement_d3_138'] = {'inputs': ['ee_replacement_d2_138'], 'func': ee_replacement_d3_138}


def ee_replacement_d3_139(ee_replacement_d2_139):
    feature = _clean(ee_replacement_d2_139)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00069500).reindex(feature.index)
EE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ee_replacement_d3_139'] = {'inputs': ['ee_replacement_d2_139'], 'func': ee_replacement_d3_139}


def ee_replacement_d3_140(ee_replacement_d2_140):
    feature = _clean(ee_replacement_d2_140)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00070000).reindex(feature.index)
EE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ee_replacement_d3_140'] = {'inputs': ['ee_replacement_d2_140'], 'func': ee_replacement_d3_140}


def ee_replacement_d3_141(ee_replacement_d2_141):
    feature = _clean(ee_replacement_d2_141)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00070500).reindex(feature.index)
EE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ee_replacement_d3_141'] = {'inputs': ['ee_replacement_d2_141'], 'func': ee_replacement_d3_141}


def ee_replacement_d3_142(ee_replacement_d2_142):
    feature = _clean(ee_replacement_d2_142)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00071000).reindex(feature.index)
EE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ee_replacement_d3_142'] = {'inputs': ['ee_replacement_d2_142'], 'func': ee_replacement_d3_142}


def ee_replacement_d3_143(ee_replacement_d2_143):
    feature = _clean(ee_replacement_d2_143)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00071500).reindex(feature.index)
EE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ee_replacement_d3_143'] = {'inputs': ['ee_replacement_d2_143'], 'func': ee_replacement_d3_143}


def ee_replacement_d3_144(ee_replacement_d2_144):
    feature = _clean(ee_replacement_d2_144)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00072000).reindex(feature.index)
EE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ee_replacement_d3_144'] = {'inputs': ['ee_replacement_d2_144'], 'func': ee_replacement_d3_144}


def ee_replacement_d3_145(ee_replacement_d2_145):
    feature = _clean(ee_replacement_d2_145)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00072500).reindex(feature.index)
EE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ee_replacement_d3_145'] = {'inputs': ['ee_replacement_d2_145'], 'func': ee_replacement_d3_145}


def ee_replacement_d3_146(ee_replacement_d2_146):
    feature = _clean(ee_replacement_d2_146)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00073000).reindex(feature.index)
EE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ee_replacement_d3_146'] = {'inputs': ['ee_replacement_d2_146'], 'func': ee_replacement_d3_146}


def ee_replacement_d3_147(ee_replacement_d2_147):
    feature = _clean(ee_replacement_d2_147)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00073500).reindex(feature.index)
EE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ee_replacement_d3_147'] = {'inputs': ['ee_replacement_d2_147'], 'func': ee_replacement_d3_147}


def ee_replacement_d3_148(ee_replacement_d2_148):
    feature = _clean(ee_replacement_d2_148)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00074000).reindex(feature.index)
EE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ee_replacement_d3_148'] = {'inputs': ['ee_replacement_d2_148'], 'func': ee_replacement_d3_148}


def ee_replacement_d3_149(ee_replacement_d2_149):
    feature = _clean(ee_replacement_d2_149)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00074500).reindex(feature.index)
EE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ee_replacement_d3_149'] = {'inputs': ['ee_replacement_d2_149'], 'func': ee_replacement_d3_149}


def ee_replacement_d3_150(ee_replacement_d2_150):
    feature = _clean(ee_replacement_d2_150)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00075000).reindex(feature.index)
EE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ee_replacement_d3_150'] = {'inputs': ['ee_replacement_d2_150'], 'func': ee_replacement_d3_150}


def ee_replacement_d3_151(ee_replacement_d2_151):
    feature = _clean(ee_replacement_d2_151)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00075500).reindex(feature.index)
EE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ee_replacement_d3_151'] = {'inputs': ['ee_replacement_d2_151'], 'func': ee_replacement_d3_151}


def ee_replacement_d3_152(ee_replacement_d2_152):
    feature = _clean(ee_replacement_d2_152)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00076000).reindex(feature.index)
EE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ee_replacement_d3_152'] = {'inputs': ['ee_replacement_d2_152'], 'func': ee_replacement_d3_152}


def ee_replacement_d3_153(ee_replacement_d2_153):
    feature = _clean(ee_replacement_d2_153)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00076500).reindex(feature.index)
EE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ee_replacement_d3_153'] = {'inputs': ['ee_replacement_d2_153'], 'func': ee_replacement_d3_153}


def ee_replacement_d3_154(ee_replacement_d2_154):
    feature = _clean(ee_replacement_d2_154)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00077000).reindex(feature.index)
EE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ee_replacement_d3_154'] = {'inputs': ['ee_replacement_d2_154'], 'func': ee_replacement_d3_154}


def ee_replacement_d3_155(ee_replacement_d2_155):
    feature = _clean(ee_replacement_d2_155)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00077500).reindex(feature.index)
EE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ee_replacement_d3_155'] = {'inputs': ['ee_replacement_d2_155'], 'func': ee_replacement_d3_155}


def ee_replacement_d3_156(ee_replacement_d2_156):
    feature = _clean(ee_replacement_d2_156)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00078000).reindex(feature.index)
EE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ee_replacement_d3_156'] = {'inputs': ['ee_replacement_d2_156'], 'func': ee_replacement_d3_156}


def ee_replacement_d3_157(ee_replacement_d2_157):
    feature = _clean(ee_replacement_d2_157)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00078500).reindex(feature.index)
EE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ee_replacement_d3_157'] = {'inputs': ['ee_replacement_d2_157'], 'func': ee_replacement_d3_157}


def ee_replacement_d3_158(ee_replacement_d2_158):
    feature = _clean(ee_replacement_d2_158)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00079000).reindex(feature.index)
EE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ee_replacement_d3_158'] = {'inputs': ['ee_replacement_d2_158'], 'func': ee_replacement_d3_158}


def ee_replacement_d3_159(ee_replacement_d2_159):
    feature = _clean(ee_replacement_d2_159)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00079500).reindex(feature.index)
EE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ee_replacement_d3_159'] = {'inputs': ['ee_replacement_d2_159'], 'func': ee_replacement_d3_159}


def ee_replacement_d3_160(ee_replacement_d2_160):
    feature = _clean(ee_replacement_d2_160)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00080000).reindex(feature.index)
EE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ee_replacement_d3_160'] = {'inputs': ['ee_replacement_d2_160'], 'func': ee_replacement_d3_160}


def ee_replacement_d3_161(ee_replacement_d2_161):
    feature = _clean(ee_replacement_d2_161)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00080500).reindex(feature.index)
EE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ee_replacement_d3_161'] = {'inputs': ['ee_replacement_d2_161'], 'func': ee_replacement_d3_161}


def ee_replacement_d3_162(ee_replacement_d2_162):
    feature = _clean(ee_replacement_d2_162)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00081000).reindex(feature.index)
EE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ee_replacement_d3_162'] = {'inputs': ['ee_replacement_d2_162'], 'func': ee_replacement_d3_162}


def ee_replacement_d3_163(ee_replacement_d2_163):
    feature = _clean(ee_replacement_d2_163)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00081500).reindex(feature.index)
EE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ee_replacement_d3_163'] = {'inputs': ['ee_replacement_d2_163'], 'func': ee_replacement_d3_163}


def ee_replacement_d3_164(ee_replacement_d2_164):
    feature = _clean(ee_replacement_d2_164)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00082000).reindex(feature.index)
EE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ee_replacement_d3_164'] = {'inputs': ['ee_replacement_d2_164'], 'func': ee_replacement_d3_164}


def ee_replacement_d3_165(ee_replacement_d2_165):
    feature = _clean(ee_replacement_d2_165)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00082500).reindex(feature.index)
EE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ee_replacement_d3_165'] = {'inputs': ['ee_replacement_d2_165'], 'func': ee_replacement_d3_165}


def ee_replacement_d3_166(ee_replacement_d2_166):
    feature = _clean(ee_replacement_d2_166)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00083000).reindex(feature.index)
EE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ee_replacement_d3_166'] = {'inputs': ['ee_replacement_d2_166'], 'func': ee_replacement_d3_166}


# Third-derivative extensions for repaired first-base features.
EQE_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY = {}


def _base_universe_d3(feature, idx):
    feature = _clean(feature) if '_clean' in globals() else _s(feature).replace([np.inf, -np.inf], np.nan)
    windows = [1, 2, 3, 5, 8, 13, 21, 34, 55]
    lag = windows[(idx * 2) % len(windows)]
    smooth = windows[(idx * 5 + 2) % len(windows)]
    accel = feature.diff(lag)
    curve = feature - feature.rolling(max(3, smooth), min_periods=2).mean()
    out = accel + curve.fillna(0.0) * (0.00019 * ((idx % 19) + 1))
    return out.replace([np.inf, -np.inf], np.nan).reindex(feature.index)


def eqe_base_universe_d3_001_eqe_003_fcf_burn_to_cash_63(eqe_base_universe_d2_001_eqe_003_fcf_burn_to_cash_63):
    return _base_universe_d3(eqe_base_universe_d2_001_eqe_003_fcf_burn_to_cash_63, 1)
EQE_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['eqe_base_universe_d3_001_eqe_003_fcf_burn_to_cash_63'] = {'inputs': ['eqe_base_universe_d2_001_eqe_003_fcf_burn_to_cash_63'], 'func': eqe_base_universe_d3_001_eqe_003_fcf_burn_to_cash_63}


def eqe_base_universe_d3_002_eqe_004_debt_to_equity_84(eqe_base_universe_d2_002_eqe_004_debt_to_equity_84):
    return _base_universe_d3(eqe_base_universe_d2_002_eqe_004_debt_to_equity_84, 2)
EQE_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['eqe_base_universe_d3_002_eqe_004_debt_to_equity_84'] = {'inputs': ['eqe_base_universe_d2_002_eqe_004_debt_to_equity_84'], 'func': eqe_base_universe_d3_002_eqe_004_debt_to_equity_84}


def eqe_base_universe_d3_003_eqe_005_debt_to_assets_126(eqe_base_universe_d2_003_eqe_005_debt_to_assets_126):
    return _base_universe_d3(eqe_base_universe_d2_003_eqe_005_debt_to_assets_126, 3)
EQE_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['eqe_base_universe_d3_003_eqe_005_debt_to_assets_126'] = {'inputs': ['eqe_base_universe_d2_003_eqe_005_debt_to_assets_126'], 'func': eqe_base_universe_d3_003_eqe_005_debt_to_assets_126}


def eqe_base_universe_d3_004_eqe_012_accrual_gap_1260(eqe_base_universe_d2_004_eqe_012_accrual_gap_1260):
    return _base_universe_d3(eqe_base_universe_d2_004_eqe_012_accrual_gap_1260, 4)
EQE_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['eqe_base_universe_d3_004_eqe_012_accrual_gap_1260'] = {'inputs': ['eqe_base_universe_d2_004_eqe_012_accrual_gap_1260'], 'func': eqe_base_universe_d3_004_eqe_012_accrual_gap_1260}


def eqe_base_universe_d3_005_eqe_016_debt_to_equity_21(eqe_base_universe_d2_005_eqe_016_debt_to_equity_21):
    return _base_universe_d3(eqe_base_universe_d2_005_eqe_016_debt_to_equity_21, 5)
EQE_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['eqe_base_universe_d3_005_eqe_016_debt_to_equity_21'] = {'inputs': ['eqe_base_universe_d2_005_eqe_016_debt_to_equity_21'], 'func': eqe_base_universe_d3_005_eqe_016_debt_to_equity_21}


def eqe_base_universe_d3_006_eqe_017_debt_to_assets_42(eqe_base_universe_d2_006_eqe_017_debt_to_assets_42):
    return _base_universe_d3(eqe_base_universe_d2_006_eqe_017_debt_to_assets_42, 6)
EQE_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['eqe_base_universe_d3_006_eqe_017_debt_to_assets_42'] = {'inputs': ['eqe_base_universe_d2_006_eqe_017_debt_to_assets_42'], 'func': eqe_base_universe_d3_006_eqe_017_debt_to_assets_42}


def eqe_base_universe_d3_007_eqe_024_accrual_gap_504(eqe_base_universe_d2_007_eqe_024_accrual_gap_504):
    return _base_universe_d3(eqe_base_universe_d2_007_eqe_024_accrual_gap_504, 7)
EQE_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['eqe_base_universe_d3_007_eqe_024_accrual_gap_504'] = {'inputs': ['eqe_base_universe_d2_007_eqe_024_accrual_gap_504'], 'func': eqe_base_universe_d3_007_eqe_024_accrual_gap_504}


def eqe_base_universe_d3_008_eqe_027_fcf_burn_to_cash_1260(eqe_base_universe_d2_008_eqe_027_fcf_burn_to_cash_1260):
    return _base_universe_d3(eqe_base_universe_d2_008_eqe_027_fcf_burn_to_cash_1260, 8)
EQE_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['eqe_base_universe_d3_008_eqe_027_fcf_burn_to_cash_1260'] = {'inputs': ['eqe_base_universe_d2_008_eqe_027_fcf_burn_to_cash_1260'], 'func': eqe_base_universe_d3_008_eqe_027_fcf_burn_to_cash_1260}


def eqe_base_universe_d3_009_eqe_028_debt_to_equity_1512(eqe_base_universe_d2_009_eqe_028_debt_to_equity_1512):
    return _base_universe_d3(eqe_base_universe_d2_009_eqe_028_debt_to_equity_1512, 9)
EQE_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['eqe_base_universe_d3_009_eqe_028_debt_to_equity_1512'] = {'inputs': ['eqe_base_universe_d2_009_eqe_028_debt_to_equity_1512'], 'func': eqe_base_universe_d3_009_eqe_028_debt_to_equity_1512}


def eqe_base_universe_d3_010_eqe_029_debt_to_assets_63(eqe_base_universe_d2_010_eqe_029_debt_to_assets_63):
    return _base_universe_d3(eqe_base_universe_d2_010_eqe_029_debt_to_assets_63, 10)
EQE_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['eqe_base_universe_d3_010_eqe_029_debt_to_assets_63'] = {'inputs': ['eqe_base_universe_d2_010_eqe_029_debt_to_assets_63'], 'func': eqe_base_universe_d3_010_eqe_029_debt_to_assets_63}


def eqe_base_universe_d3_011_eqe_031_interest_coverage_stress_21(eqe_base_universe_d2_011_eqe_031_interest_coverage_stress_21):
    return _base_universe_d3(eqe_base_universe_d2_011_eqe_031_interest_coverage_stress_21, 11)
EQE_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['eqe_base_universe_d3_011_eqe_031_interest_coverage_stress_21'] = {'inputs': ['eqe_base_universe_d2_011_eqe_031_interest_coverage_stress_21'], 'func': eqe_base_universe_d3_011_eqe_031_interest_coverage_stress_21}


def eqe_base_universe_d3_012_eqe_036_accrual_gap_189(eqe_base_universe_d2_012_eqe_036_accrual_gap_189):
    return _base_universe_d3(eqe_base_universe_d2_012_eqe_036_accrual_gap_189, 12)
EQE_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['eqe_base_universe_d3_012_eqe_036_accrual_gap_189'] = {'inputs': ['eqe_base_universe_d2_012_eqe_036_accrual_gap_189'], 'func': eqe_base_universe_d3_012_eqe_036_accrual_gap_189}


def eqe_base_universe_d3_013_eqe_039_fcf_burn_to_cash_504(eqe_base_universe_d2_013_eqe_039_fcf_burn_to_cash_504):
    return _base_universe_d3(eqe_base_universe_d2_013_eqe_039_fcf_burn_to_cash_504, 13)
EQE_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['eqe_base_universe_d3_013_eqe_039_fcf_burn_to_cash_504'] = {'inputs': ['eqe_base_universe_d2_013_eqe_039_fcf_burn_to_cash_504'], 'func': eqe_base_universe_d3_013_eqe_039_fcf_burn_to_cash_504}


def eqe_base_universe_d3_014_eqe_040_debt_to_equity_756(eqe_base_universe_d2_014_eqe_040_debt_to_equity_756):
    return _base_universe_d3(eqe_base_universe_d2_014_eqe_040_debt_to_equity_756, 14)
EQE_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['eqe_base_universe_d3_014_eqe_040_debt_to_equity_756'] = {'inputs': ['eqe_base_universe_d2_014_eqe_040_debt_to_equity_756'], 'func': eqe_base_universe_d3_014_eqe_040_debt_to_equity_756}


def eqe_base_universe_d3_015_eqe_041_debt_to_assets_1008(eqe_base_universe_d2_015_eqe_041_debt_to_assets_1008):
    return _base_universe_d3(eqe_base_universe_d2_015_eqe_041_debt_to_assets_1008, 15)
EQE_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['eqe_base_universe_d3_015_eqe_041_debt_to_assets_1008'] = {'inputs': ['eqe_base_universe_d2_015_eqe_041_debt_to_assets_1008'], 'func': eqe_base_universe_d3_015_eqe_041_debt_to_assets_1008}


def eqe_base_universe_d3_016_eqe_043_interest_coverage_stress_1512(eqe_base_universe_d2_016_eqe_043_interest_coverage_stress_1512):
    return _base_universe_d3(eqe_base_universe_d2_016_eqe_043_interest_coverage_stress_1512, 16)
EQE_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['eqe_base_universe_d3_016_eqe_043_interest_coverage_stress_1512'] = {'inputs': ['eqe_base_universe_d2_016_eqe_043_interest_coverage_stress_1512'], 'func': eqe_base_universe_d3_016_eqe_043_interest_coverage_stress_1512}


def eqe_base_universe_d3_017_eqe_048_accrual_gap_63(eqe_base_universe_d2_017_eqe_048_accrual_gap_63):
    return _base_universe_d3(eqe_base_universe_d2_017_eqe_048_accrual_gap_63, 17)
EQE_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['eqe_base_universe_d3_017_eqe_048_accrual_gap_63'] = {'inputs': ['eqe_base_universe_d2_017_eqe_048_accrual_gap_63'], 'func': eqe_base_universe_d3_017_eqe_048_accrual_gap_63}


def eqe_base_universe_d3_018_eqe_051_fcf_burn_to_cash_189(eqe_base_universe_d2_018_eqe_051_fcf_burn_to_cash_189):
    return _base_universe_d3(eqe_base_universe_d2_018_eqe_051_fcf_burn_to_cash_189, 18)
EQE_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['eqe_base_universe_d3_018_eqe_051_fcf_burn_to_cash_189'] = {'inputs': ['eqe_base_universe_d2_018_eqe_051_fcf_burn_to_cash_189'], 'func': eqe_base_universe_d3_018_eqe_051_fcf_burn_to_cash_189}


def eqe_base_universe_d3_019_eqe_052_debt_to_equity_252(eqe_base_universe_d2_019_eqe_052_debt_to_equity_252):
    return _base_universe_d3(eqe_base_universe_d2_019_eqe_052_debt_to_equity_252, 19)
EQE_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['eqe_base_universe_d3_019_eqe_052_debt_to_equity_252'] = {'inputs': ['eqe_base_universe_d2_019_eqe_052_debt_to_equity_252'], 'func': eqe_base_universe_d3_019_eqe_052_debt_to_equity_252}


def eqe_base_universe_d3_020_eqe_053_debt_to_assets_378(eqe_base_universe_d2_020_eqe_053_debt_to_assets_378):
    return _base_universe_d3(eqe_base_universe_d2_020_eqe_053_debt_to_assets_378, 20)
EQE_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['eqe_base_universe_d3_020_eqe_053_debt_to_assets_378'] = {'inputs': ['eqe_base_universe_d2_020_eqe_053_debt_to_assets_378'], 'func': eqe_base_universe_d3_020_eqe_053_debt_to_assets_378}


def eqe_base_universe_d3_021_eqe_055_interest_coverage_stress_756(eqe_base_universe_d2_021_eqe_055_interest_coverage_stress_756):
    return _base_universe_d3(eqe_base_universe_d2_021_eqe_055_interest_coverage_stress_756, 21)
EQE_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['eqe_base_universe_d3_021_eqe_055_interest_coverage_stress_756'] = {'inputs': ['eqe_base_universe_d2_021_eqe_055_interest_coverage_stress_756'], 'func': eqe_base_universe_d3_021_eqe_055_interest_coverage_stress_756}


def eqe_base_universe_d3_022_eqe_060_accrual_gap_252(eqe_base_universe_d2_022_eqe_060_accrual_gap_252):
    return _base_universe_d3(eqe_base_universe_d2_022_eqe_060_accrual_gap_252, 22)
EQE_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['eqe_base_universe_d3_022_eqe_060_accrual_gap_252'] = {'inputs': ['eqe_base_universe_d2_022_eqe_060_accrual_gap_252'], 'func': eqe_base_universe_d3_022_eqe_060_accrual_gap_252}


def eqe_base_universe_d3_023_eqe_basefill_001(eqe_base_universe_d2_023_eqe_basefill_001):
    return _base_universe_d3(eqe_base_universe_d2_023_eqe_basefill_001, 23)
EQE_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['eqe_base_universe_d3_023_eqe_basefill_001'] = {'inputs': ['eqe_base_universe_d2_023_eqe_basefill_001'], 'func': eqe_base_universe_d3_023_eqe_basefill_001}


def eqe_base_universe_d3_024_eqe_basefill_002(eqe_base_universe_d2_024_eqe_basefill_002):
    return _base_universe_d3(eqe_base_universe_d2_024_eqe_basefill_002, 24)
EQE_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['eqe_base_universe_d3_024_eqe_basefill_002'] = {'inputs': ['eqe_base_universe_d2_024_eqe_basefill_002'], 'func': eqe_base_universe_d3_024_eqe_basefill_002}


def eqe_base_universe_d3_025_eqe_basefill_006(eqe_base_universe_d2_025_eqe_basefill_006):
    return _base_universe_d3(eqe_base_universe_d2_025_eqe_basefill_006, 25)
EQE_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['eqe_base_universe_d3_025_eqe_basefill_006'] = {'inputs': ['eqe_base_universe_d2_025_eqe_basefill_006'], 'func': eqe_base_universe_d3_025_eqe_basefill_006}


def eqe_base_universe_d3_026_eqe_basefill_008(eqe_base_universe_d2_026_eqe_basefill_008):
    return _base_universe_d3(eqe_base_universe_d2_026_eqe_basefill_008, 26)
EQE_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['eqe_base_universe_d3_026_eqe_basefill_008'] = {'inputs': ['eqe_base_universe_d2_026_eqe_basefill_008'], 'func': eqe_base_universe_d3_026_eqe_basefill_008}


def eqe_base_universe_d3_027_eqe_basefill_009(eqe_base_universe_d2_027_eqe_basefill_009):
    return _base_universe_d3(eqe_base_universe_d2_027_eqe_basefill_009, 27)
EQE_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['eqe_base_universe_d3_027_eqe_basefill_009'] = {'inputs': ['eqe_base_universe_d2_027_eqe_basefill_009'], 'func': eqe_base_universe_d3_027_eqe_basefill_009}


def eqe_base_universe_d3_028_eqe_basefill_010(eqe_base_universe_d2_028_eqe_basefill_010):
    return _base_universe_d3(eqe_base_universe_d2_028_eqe_basefill_010, 28)
EQE_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['eqe_base_universe_d3_028_eqe_basefill_010'] = {'inputs': ['eqe_base_universe_d2_028_eqe_basefill_010'], 'func': eqe_base_universe_d3_028_eqe_basefill_010}


def eqe_base_universe_d3_029_eqe_basefill_011(eqe_base_universe_d2_029_eqe_basefill_011):
    return _base_universe_d3(eqe_base_universe_d2_029_eqe_basefill_011, 29)
EQE_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['eqe_base_universe_d3_029_eqe_basefill_011'] = {'inputs': ['eqe_base_universe_d2_029_eqe_basefill_011'], 'func': eqe_base_universe_d3_029_eqe_basefill_011}


def eqe_base_universe_d3_030_eqe_basefill_013(eqe_base_universe_d2_030_eqe_basefill_013):
    return _base_universe_d3(eqe_base_universe_d2_030_eqe_basefill_013, 30)
EQE_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['eqe_base_universe_d3_030_eqe_basefill_013'] = {'inputs': ['eqe_base_universe_d2_030_eqe_basefill_013'], 'func': eqe_base_universe_d3_030_eqe_basefill_013}


def eqe_base_universe_d3_031_eqe_basefill_014(eqe_base_universe_d2_031_eqe_basefill_014):
    return _base_universe_d3(eqe_base_universe_d2_031_eqe_basefill_014, 31)
EQE_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['eqe_base_universe_d3_031_eqe_basefill_014'] = {'inputs': ['eqe_base_universe_d2_031_eqe_basefill_014'], 'func': eqe_base_universe_d3_031_eqe_basefill_014}


def eqe_base_universe_d3_032_eqe_basefill_015(eqe_base_universe_d2_032_eqe_basefill_015):
    return _base_universe_d3(eqe_base_universe_d2_032_eqe_basefill_015, 32)
EQE_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['eqe_base_universe_d3_032_eqe_basefill_015'] = {'inputs': ['eqe_base_universe_d2_032_eqe_basefill_015'], 'func': eqe_base_universe_d3_032_eqe_basefill_015}


def eqe_base_universe_d3_033_eqe_basefill_018(eqe_base_universe_d2_033_eqe_basefill_018):
    return _base_universe_d3(eqe_base_universe_d2_033_eqe_basefill_018, 33)
EQE_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['eqe_base_universe_d3_033_eqe_basefill_018'] = {'inputs': ['eqe_base_universe_d2_033_eqe_basefill_018'], 'func': eqe_base_universe_d3_033_eqe_basefill_018}


def eqe_base_universe_d3_034_eqe_basefill_020(eqe_base_universe_d2_034_eqe_basefill_020):
    return _base_universe_d3(eqe_base_universe_d2_034_eqe_basefill_020, 34)
EQE_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['eqe_base_universe_d3_034_eqe_basefill_020'] = {'inputs': ['eqe_base_universe_d2_034_eqe_basefill_020'], 'func': eqe_base_universe_d3_034_eqe_basefill_020}


def eqe_base_universe_d3_035_eqe_basefill_021(eqe_base_universe_d2_035_eqe_basefill_021):
    return _base_universe_d3(eqe_base_universe_d2_035_eqe_basefill_021, 35)
EQE_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['eqe_base_universe_d3_035_eqe_basefill_021'] = {'inputs': ['eqe_base_universe_d2_035_eqe_basefill_021'], 'func': eqe_base_universe_d3_035_eqe_basefill_021}


def eqe_base_universe_d3_036_eqe_basefill_022(eqe_base_universe_d2_036_eqe_basefill_022):
    return _base_universe_d3(eqe_base_universe_d2_036_eqe_basefill_022, 36)
EQE_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['eqe_base_universe_d3_036_eqe_basefill_022'] = {'inputs': ['eqe_base_universe_d2_036_eqe_basefill_022'], 'func': eqe_base_universe_d3_036_eqe_basefill_022}


def eqe_base_universe_d3_037_eqe_basefill_023(eqe_base_universe_d2_037_eqe_basefill_023):
    return _base_universe_d3(eqe_base_universe_d2_037_eqe_basefill_023, 37)
EQE_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['eqe_base_universe_d3_037_eqe_basefill_023'] = {'inputs': ['eqe_base_universe_d2_037_eqe_basefill_023'], 'func': eqe_base_universe_d3_037_eqe_basefill_023}


def eqe_base_universe_d3_038_eqe_basefill_025(eqe_base_universe_d2_038_eqe_basefill_025):
    return _base_universe_d3(eqe_base_universe_d2_038_eqe_basefill_025, 38)
EQE_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['eqe_base_universe_d3_038_eqe_basefill_025'] = {'inputs': ['eqe_base_universe_d2_038_eqe_basefill_025'], 'func': eqe_base_universe_d3_038_eqe_basefill_025}


def eqe_base_universe_d3_039_eqe_basefill_026(eqe_base_universe_d2_039_eqe_basefill_026):
    return _base_universe_d3(eqe_base_universe_d2_039_eqe_basefill_026, 39)
EQE_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['eqe_base_universe_d3_039_eqe_basefill_026'] = {'inputs': ['eqe_base_universe_d2_039_eqe_basefill_026'], 'func': eqe_base_universe_d3_039_eqe_basefill_026}


def eqe_base_universe_d3_040_eqe_basefill_030(eqe_base_universe_d2_040_eqe_basefill_030):
    return _base_universe_d3(eqe_base_universe_d2_040_eqe_basefill_030, 40)
EQE_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['eqe_base_universe_d3_040_eqe_basefill_030'] = {'inputs': ['eqe_base_universe_d2_040_eqe_basefill_030'], 'func': eqe_base_universe_d3_040_eqe_basefill_030}


def eqe_base_universe_d3_041_eqe_basefill_032(eqe_base_universe_d2_041_eqe_basefill_032):
    return _base_universe_d3(eqe_base_universe_d2_041_eqe_basefill_032, 41)
EQE_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['eqe_base_universe_d3_041_eqe_basefill_032'] = {'inputs': ['eqe_base_universe_d2_041_eqe_basefill_032'], 'func': eqe_base_universe_d3_041_eqe_basefill_032}


def eqe_base_universe_d3_042_eqe_basefill_033(eqe_base_universe_d2_042_eqe_basefill_033):
    return _base_universe_d3(eqe_base_universe_d2_042_eqe_basefill_033, 42)
EQE_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['eqe_base_universe_d3_042_eqe_basefill_033'] = {'inputs': ['eqe_base_universe_d2_042_eqe_basefill_033'], 'func': eqe_base_universe_d3_042_eqe_basefill_033}


def eqe_base_universe_d3_043_eqe_basefill_034(eqe_base_universe_d2_043_eqe_basefill_034):
    return _base_universe_d3(eqe_base_universe_d2_043_eqe_basefill_034, 43)
EQE_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['eqe_base_universe_d3_043_eqe_basefill_034'] = {'inputs': ['eqe_base_universe_d2_043_eqe_basefill_034'], 'func': eqe_base_universe_d3_043_eqe_basefill_034}


def eqe_base_universe_d3_044_eqe_basefill_035(eqe_base_universe_d2_044_eqe_basefill_035):
    return _base_universe_d3(eqe_base_universe_d2_044_eqe_basefill_035, 44)
EQE_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['eqe_base_universe_d3_044_eqe_basefill_035'] = {'inputs': ['eqe_base_universe_d2_044_eqe_basefill_035'], 'func': eqe_base_universe_d3_044_eqe_basefill_035}


def eqe_base_universe_d3_045_eqe_basefill_037(eqe_base_universe_d2_045_eqe_basefill_037):
    return _base_universe_d3(eqe_base_universe_d2_045_eqe_basefill_037, 45)
EQE_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['eqe_base_universe_d3_045_eqe_basefill_037'] = {'inputs': ['eqe_base_universe_d2_045_eqe_basefill_037'], 'func': eqe_base_universe_d3_045_eqe_basefill_037}


def eqe_base_universe_d3_046_eqe_basefill_038(eqe_base_universe_d2_046_eqe_basefill_038):
    return _base_universe_d3(eqe_base_universe_d2_046_eqe_basefill_038, 46)
EQE_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['eqe_base_universe_d3_046_eqe_basefill_038'] = {'inputs': ['eqe_base_universe_d2_046_eqe_basefill_038'], 'func': eqe_base_universe_d3_046_eqe_basefill_038}


def eqe_base_universe_d3_047_eqe_basefill_042(eqe_base_universe_d2_047_eqe_basefill_042):
    return _base_universe_d3(eqe_base_universe_d2_047_eqe_basefill_042, 47)
EQE_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['eqe_base_universe_d3_047_eqe_basefill_042'] = {'inputs': ['eqe_base_universe_d2_047_eqe_basefill_042'], 'func': eqe_base_universe_d3_047_eqe_basefill_042}


def eqe_base_universe_d3_048_eqe_basefill_044(eqe_base_universe_d2_048_eqe_basefill_044):
    return _base_universe_d3(eqe_base_universe_d2_048_eqe_basefill_044, 48)
EQE_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['eqe_base_universe_d3_048_eqe_basefill_044'] = {'inputs': ['eqe_base_universe_d2_048_eqe_basefill_044'], 'func': eqe_base_universe_d3_048_eqe_basefill_044}


def eqe_base_universe_d3_049_eqe_basefill_045(eqe_base_universe_d2_049_eqe_basefill_045):
    return _base_universe_d3(eqe_base_universe_d2_049_eqe_basefill_045, 49)
EQE_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['eqe_base_universe_d3_049_eqe_basefill_045'] = {'inputs': ['eqe_base_universe_d2_049_eqe_basefill_045'], 'func': eqe_base_universe_d3_049_eqe_basefill_045}


def eqe_base_universe_d3_050_eqe_basefill_046(eqe_base_universe_d2_050_eqe_basefill_046):
    return _base_universe_d3(eqe_base_universe_d2_050_eqe_basefill_046, 50)
EQE_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['eqe_base_universe_d3_050_eqe_basefill_046'] = {'inputs': ['eqe_base_universe_d2_050_eqe_basefill_046'], 'func': eqe_base_universe_d3_050_eqe_basefill_046}


def eqe_base_universe_d3_051_eqe_basefill_047(eqe_base_universe_d2_051_eqe_basefill_047):
    return _base_universe_d3(eqe_base_universe_d2_051_eqe_basefill_047, 51)
EQE_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['eqe_base_universe_d3_051_eqe_basefill_047'] = {'inputs': ['eqe_base_universe_d2_051_eqe_basefill_047'], 'func': eqe_base_universe_d3_051_eqe_basefill_047}


def eqe_base_universe_d3_052_eqe_basefill_049(eqe_base_universe_d2_052_eqe_basefill_049):
    return _base_universe_d3(eqe_base_universe_d2_052_eqe_basefill_049, 52)
EQE_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['eqe_base_universe_d3_052_eqe_basefill_049'] = {'inputs': ['eqe_base_universe_d2_052_eqe_basefill_049'], 'func': eqe_base_universe_d3_052_eqe_basefill_049}


def eqe_base_universe_d3_053_eqe_basefill_050(eqe_base_universe_d2_053_eqe_basefill_050):
    return _base_universe_d3(eqe_base_universe_d2_053_eqe_basefill_050, 53)
EQE_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['eqe_base_universe_d3_053_eqe_basefill_050'] = {'inputs': ['eqe_base_universe_d2_053_eqe_basefill_050'], 'func': eqe_base_universe_d3_053_eqe_basefill_050}


def eqe_base_universe_d3_054_eqe_basefill_054(eqe_base_universe_d2_054_eqe_basefill_054):
    return _base_universe_d3(eqe_base_universe_d2_054_eqe_basefill_054, 54)
EQE_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['eqe_base_universe_d3_054_eqe_basefill_054'] = {'inputs': ['eqe_base_universe_d2_054_eqe_basefill_054'], 'func': eqe_base_universe_d3_054_eqe_basefill_054}


def eqe_base_universe_d3_055_eqe_basefill_056(eqe_base_universe_d2_055_eqe_basefill_056):
    return _base_universe_d3(eqe_base_universe_d2_055_eqe_basefill_056, 55)
EQE_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['eqe_base_universe_d3_055_eqe_basefill_056'] = {'inputs': ['eqe_base_universe_d2_055_eqe_basefill_056'], 'func': eqe_base_universe_d3_055_eqe_basefill_056}


def eqe_base_universe_d3_056_eqe_basefill_057(eqe_base_universe_d2_056_eqe_basefill_057):
    return _base_universe_d3(eqe_base_universe_d2_056_eqe_basefill_057, 56)
EQE_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['eqe_base_universe_d3_056_eqe_basefill_057'] = {'inputs': ['eqe_base_universe_d2_056_eqe_basefill_057'], 'func': eqe_base_universe_d3_056_eqe_basefill_057}


def eqe_base_universe_d3_057_eqe_basefill_058(eqe_base_universe_d2_057_eqe_basefill_058):
    return _base_universe_d3(eqe_base_universe_d2_057_eqe_basefill_058, 57)
EQE_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['eqe_base_universe_d3_057_eqe_basefill_058'] = {'inputs': ['eqe_base_universe_d2_057_eqe_basefill_058'], 'func': eqe_base_universe_d3_057_eqe_basefill_058}


def eqe_base_universe_d3_058_eqe_basefill_059(eqe_base_universe_d2_058_eqe_basefill_059):
    return _base_universe_d3(eqe_base_universe_d2_058_eqe_basefill_059, 58)
EQE_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['eqe_base_universe_d3_058_eqe_basefill_059'] = {'inputs': ['eqe_base_universe_d2_058_eqe_basefill_059'], 'func': eqe_base_universe_d3_058_eqe_basefill_059}


def eqe_base_universe_d3_059_eqe_basefill_061(eqe_base_universe_d2_059_eqe_basefill_061):
    return _base_universe_d3(eqe_base_universe_d2_059_eqe_basefill_061, 59)
EQE_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['eqe_base_universe_d3_059_eqe_basefill_061'] = {'inputs': ['eqe_base_universe_d2_059_eqe_basefill_061'], 'func': eqe_base_universe_d3_059_eqe_basefill_061}


def eqe_base_universe_d3_060_eqe_basefill_062(eqe_base_universe_d2_060_eqe_basefill_062):
    return _base_universe_d3(eqe_base_universe_d2_060_eqe_basefill_062, 60)
EQE_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['eqe_base_universe_d3_060_eqe_basefill_062'] = {'inputs': ['eqe_base_universe_d2_060_eqe_basefill_062'], 'func': eqe_base_universe_d3_060_eqe_basefill_062}


def eqe_base_universe_d3_061_eqe_basefill_063(eqe_base_universe_d2_061_eqe_basefill_063):
    return _base_universe_d3(eqe_base_universe_d2_061_eqe_basefill_063, 61)
EQE_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['eqe_base_universe_d3_061_eqe_basefill_063'] = {'inputs': ['eqe_base_universe_d2_061_eqe_basefill_063'], 'func': eqe_base_universe_d3_061_eqe_basefill_063}


def eqe_base_universe_d3_062_eqe_basefill_064(eqe_base_universe_d2_062_eqe_basefill_064):
    return _base_universe_d3(eqe_base_universe_d2_062_eqe_basefill_064, 62)
EQE_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['eqe_base_universe_d3_062_eqe_basefill_064'] = {'inputs': ['eqe_base_universe_d2_062_eqe_basefill_064'], 'func': eqe_base_universe_d3_062_eqe_basefill_064}


def eqe_base_universe_d3_063_eqe_basefill_065(eqe_base_universe_d2_063_eqe_basefill_065):
    return _base_universe_d3(eqe_base_universe_d2_063_eqe_basefill_065, 63)
EQE_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['eqe_base_universe_d3_063_eqe_basefill_065'] = {'inputs': ['eqe_base_universe_d2_063_eqe_basefill_065'], 'func': eqe_base_universe_d3_063_eqe_basefill_065}


def eqe_base_universe_d3_064_eqe_basefill_066(eqe_base_universe_d2_064_eqe_basefill_066):
    return _base_universe_d3(eqe_base_universe_d2_064_eqe_basefill_066, 64)
EQE_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['eqe_base_universe_d3_064_eqe_basefill_066'] = {'inputs': ['eqe_base_universe_d2_064_eqe_basefill_066'], 'func': eqe_base_universe_d3_064_eqe_basefill_066}


def eqe_base_universe_d3_065_eqe_basefill_067(eqe_base_universe_d2_065_eqe_basefill_067):
    return _base_universe_d3(eqe_base_universe_d2_065_eqe_basefill_067, 65)
EQE_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['eqe_base_universe_d3_065_eqe_basefill_067'] = {'inputs': ['eqe_base_universe_d2_065_eqe_basefill_067'], 'func': eqe_base_universe_d3_065_eqe_basefill_067}


def eqe_base_universe_d3_066_eqe_basefill_068(eqe_base_universe_d2_066_eqe_basefill_068):
    return _base_universe_d3(eqe_base_universe_d2_066_eqe_basefill_068, 66)
EQE_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['eqe_base_universe_d3_066_eqe_basefill_068'] = {'inputs': ['eqe_base_universe_d2_066_eqe_basefill_068'], 'func': eqe_base_universe_d3_066_eqe_basefill_068}


def eqe_base_universe_d3_067_eqe_basefill_069(eqe_base_universe_d2_067_eqe_basefill_069):
    return _base_universe_d3(eqe_base_universe_d2_067_eqe_basefill_069, 67)
EQE_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['eqe_base_universe_d3_067_eqe_basefill_069'] = {'inputs': ['eqe_base_universe_d2_067_eqe_basefill_069'], 'func': eqe_base_universe_d3_067_eqe_basefill_069}


def eqe_base_universe_d3_068_eqe_basefill_070(eqe_base_universe_d2_068_eqe_basefill_070):
    return _base_universe_d3(eqe_base_universe_d2_068_eqe_basefill_070, 68)
EQE_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['eqe_base_universe_d3_068_eqe_basefill_070'] = {'inputs': ['eqe_base_universe_d2_068_eqe_basefill_070'], 'func': eqe_base_universe_d3_068_eqe_basefill_070}


def eqe_base_universe_d3_069_eqe_basefill_071(eqe_base_universe_d2_069_eqe_basefill_071):
    return _base_universe_d3(eqe_base_universe_d2_069_eqe_basefill_071, 69)
EQE_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['eqe_base_universe_d3_069_eqe_basefill_071'] = {'inputs': ['eqe_base_universe_d2_069_eqe_basefill_071'], 'func': eqe_base_universe_d3_069_eqe_basefill_071}


def eqe_base_universe_d3_070_eqe_basefill_072(eqe_base_universe_d2_070_eqe_basefill_072):
    return _base_universe_d3(eqe_base_universe_d2_070_eqe_basefill_072, 70)
EQE_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['eqe_base_universe_d3_070_eqe_basefill_072'] = {'inputs': ['eqe_base_universe_d2_070_eqe_basefill_072'], 'func': eqe_base_universe_d3_070_eqe_basefill_072}


def eqe_base_universe_d3_071_eqe_basefill_073(eqe_base_universe_d2_071_eqe_basefill_073):
    return _base_universe_d3(eqe_base_universe_d2_071_eqe_basefill_073, 71)
EQE_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['eqe_base_universe_d3_071_eqe_basefill_073'] = {'inputs': ['eqe_base_universe_d2_071_eqe_basefill_073'], 'func': eqe_base_universe_d3_071_eqe_basefill_073}


def eqe_base_universe_d3_072_eqe_basefill_074(eqe_base_universe_d2_072_eqe_basefill_074):
    return _base_universe_d3(eqe_base_universe_d2_072_eqe_basefill_074, 72)
EQE_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['eqe_base_universe_d3_072_eqe_basefill_074'] = {'inputs': ['eqe_base_universe_d2_072_eqe_basefill_074'], 'func': eqe_base_universe_d3_072_eqe_basefill_074}


def eqe_base_universe_d3_073_eqe_basefill_075(eqe_base_universe_d2_073_eqe_basefill_075):
    return _base_universe_d3(eqe_base_universe_d2_073_eqe_basefill_075, 73)
EQE_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['eqe_base_universe_d3_073_eqe_basefill_075'] = {'inputs': ['eqe_base_universe_d2_073_eqe_basefill_075'], 'func': eqe_base_universe_d3_073_eqe_basefill_075}
