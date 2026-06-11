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



def slv_176_slv_001_netinc_decline_1_accel_1(slv_151_slv_001_netinc_decline_1_roc_1):
    feature = _s(slv_151_slv_001_netinc_decline_1_roc_1)
    return (_roc(feature, 1).diff(1)).reindex(feature.index)

def slv_177_slv_007_interest_coverage_stress_252_accel_42(slv_152_slv_007_interest_coverage_stress_252_roc_42):
    feature = _s(slv_152_slv_007_interest_coverage_stress_252_roc_42)
    return (_roc(feature, 42).diff(8)).reindex(feature.index)

def slv_178_slv_013_netinc_decline_1_accel_126(slv_153_slv_013_netinc_decline_1_roc_126):
    feature = _s(slv_153_slv_013_netinc_decline_1_roc_126)
    return (_roc(feature, 126).diff(25)).reindex(feature.index)

def slv_179_slv_019_interest_coverage_stress_84_accel_378(slv_154_slv_019_interest_coverage_stress_84_roc_378):
    feature = _s(slv_154_slv_019_interest_coverage_stress_84_roc_378)
    return (_roc(feature, 378).diff(75)).reindex(feature.index)

def slv_180_slv_025_netinc_decline_1_accel_4(slv_155_slv_025_netinc_decline_1_roc_4):
    feature = _s(slv_155_slv_025_netinc_decline_1_roc_4)
    return (_roc(feature, 4).diff(1)).reindex(feature.index)






















SOLVENCY_SCORES_REGISTRY_3RD_DERIVATIVES = {
    'slv_176_slv_001_netinc_decline_1_accel_1': {'inputs': ['slv_151_slv_001_netinc_decline_1_roc_1'], 'func': slv_176_slv_001_netinc_decline_1_accel_1},
    'slv_177_slv_007_interest_coverage_stress_252_accel_42': {'inputs': ['slv_152_slv_007_interest_coverage_stress_252_roc_42'], 'func': slv_177_slv_007_interest_coverage_stress_252_accel_42},
    'slv_178_slv_013_netinc_decline_1_accel_126': {'inputs': ['slv_153_slv_013_netinc_decline_1_roc_126'], 'func': slv_178_slv_013_netinc_decline_1_accel_126},
    'slv_179_slv_019_interest_coverage_stress_84_accel_378': {'inputs': ['slv_154_slv_019_interest_coverage_stress_84_roc_378'], 'func': slv_179_slv_019_interest_coverage_stress_84_accel_378},
    'slv_180_slv_025_netinc_decline_1_accel_4': {'inputs': ['slv_155_slv_025_netinc_decline_1_roc_4'], 'func': slv_180_slv_025_netinc_decline_1_accel_4},
}


# Replacement 3rd-derivative features restored after redundancy audit.

import numpy as np
import pandas as pd


def _s(x):
    return pd.Series(x).astype(float)


def _clean(x):
    return _s(x).replace([np.inf, -np.inf], np.nan)


SS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY = {}


def ss_replacement_d3_001(ss_replacement_d2_001):
    feature = _clean(ss_replacement_d2_001)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00000500).reindex(feature.index)
SS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ss_replacement_d3_001'] = {'inputs': ['ss_replacement_d2_001'], 'func': ss_replacement_d3_001}


def ss_replacement_d3_002(ss_replacement_d2_002):
    feature = _clean(ss_replacement_d2_002)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00001000).reindex(feature.index)
SS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ss_replacement_d3_002'] = {'inputs': ['ss_replacement_d2_002'], 'func': ss_replacement_d3_002}


def ss_replacement_d3_003(ss_replacement_d2_003):
    feature = _clean(ss_replacement_d2_003)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00001500).reindex(feature.index)
SS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ss_replacement_d3_003'] = {'inputs': ['ss_replacement_d2_003'], 'func': ss_replacement_d3_003}


def ss_replacement_d3_004(ss_replacement_d2_004):
    feature = _clean(ss_replacement_d2_004)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00002000).reindex(feature.index)
SS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ss_replacement_d3_004'] = {'inputs': ['ss_replacement_d2_004'], 'func': ss_replacement_d3_004}


def ss_replacement_d3_005(ss_replacement_d2_005):
    feature = _clean(ss_replacement_d2_005)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00002500).reindex(feature.index)
SS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ss_replacement_d3_005'] = {'inputs': ['ss_replacement_d2_005'], 'func': ss_replacement_d3_005}


def ss_replacement_d3_006(ss_replacement_d2_006):
    feature = _clean(ss_replacement_d2_006)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00003000).reindex(feature.index)
SS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ss_replacement_d3_006'] = {'inputs': ['ss_replacement_d2_006'], 'func': ss_replacement_d3_006}


def ss_replacement_d3_007(ss_replacement_d2_007):
    feature = _clean(ss_replacement_d2_007)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00003500).reindex(feature.index)
SS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ss_replacement_d3_007'] = {'inputs': ['ss_replacement_d2_007'], 'func': ss_replacement_d3_007}


def ss_replacement_d3_008(ss_replacement_d2_008):
    feature = _clean(ss_replacement_d2_008)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00004000).reindex(feature.index)
SS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ss_replacement_d3_008'] = {'inputs': ['ss_replacement_d2_008'], 'func': ss_replacement_d3_008}


def ss_replacement_d3_009(ss_replacement_d2_009):
    feature = _clean(ss_replacement_d2_009)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00004500).reindex(feature.index)
SS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ss_replacement_d3_009'] = {'inputs': ['ss_replacement_d2_009'], 'func': ss_replacement_d3_009}


def ss_replacement_d3_010(ss_replacement_d2_010):
    feature = _clean(ss_replacement_d2_010)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00005000).reindex(feature.index)
SS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ss_replacement_d3_010'] = {'inputs': ['ss_replacement_d2_010'], 'func': ss_replacement_d3_010}


def ss_replacement_d3_011(ss_replacement_d2_011):
    feature = _clean(ss_replacement_d2_011)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00005500).reindex(feature.index)
SS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ss_replacement_d3_011'] = {'inputs': ['ss_replacement_d2_011'], 'func': ss_replacement_d3_011}


def ss_replacement_d3_012(ss_replacement_d2_012):
    feature = _clean(ss_replacement_d2_012)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00006000).reindex(feature.index)
SS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ss_replacement_d3_012'] = {'inputs': ['ss_replacement_d2_012'], 'func': ss_replacement_d3_012}


def ss_replacement_d3_013(ss_replacement_d2_013):
    feature = _clean(ss_replacement_d2_013)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00006500).reindex(feature.index)
SS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ss_replacement_d3_013'] = {'inputs': ['ss_replacement_d2_013'], 'func': ss_replacement_d3_013}


def ss_replacement_d3_014(ss_replacement_d2_014):
    feature = _clean(ss_replacement_d2_014)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00007000).reindex(feature.index)
SS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ss_replacement_d3_014'] = {'inputs': ['ss_replacement_d2_014'], 'func': ss_replacement_d3_014}


def ss_replacement_d3_015(ss_replacement_d2_015):
    feature = _clean(ss_replacement_d2_015)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00007500).reindex(feature.index)
SS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ss_replacement_d3_015'] = {'inputs': ['ss_replacement_d2_015'], 'func': ss_replacement_d3_015}


def ss_replacement_d3_016(ss_replacement_d2_016):
    feature = _clean(ss_replacement_d2_016)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00008000).reindex(feature.index)
SS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ss_replacement_d3_016'] = {'inputs': ['ss_replacement_d2_016'], 'func': ss_replacement_d3_016}


def ss_replacement_d3_017(ss_replacement_d2_017):
    feature = _clean(ss_replacement_d2_017)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00008500).reindex(feature.index)
SS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ss_replacement_d3_017'] = {'inputs': ['ss_replacement_d2_017'], 'func': ss_replacement_d3_017}


def ss_replacement_d3_018(ss_replacement_d2_018):
    feature = _clean(ss_replacement_d2_018)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00009000).reindex(feature.index)
SS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ss_replacement_d3_018'] = {'inputs': ['ss_replacement_d2_018'], 'func': ss_replacement_d3_018}


def ss_replacement_d3_019(ss_replacement_d2_019):
    feature = _clean(ss_replacement_d2_019)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00009500).reindex(feature.index)
SS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ss_replacement_d3_019'] = {'inputs': ['ss_replacement_d2_019'], 'func': ss_replacement_d3_019}


def ss_replacement_d3_020(ss_replacement_d2_020):
    feature = _clean(ss_replacement_d2_020)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00010000).reindex(feature.index)
SS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ss_replacement_d3_020'] = {'inputs': ['ss_replacement_d2_020'], 'func': ss_replacement_d3_020}


def ss_replacement_d3_021(ss_replacement_d2_021):
    feature = _clean(ss_replacement_d2_021)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00010500).reindex(feature.index)
SS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ss_replacement_d3_021'] = {'inputs': ['ss_replacement_d2_021'], 'func': ss_replacement_d3_021}


def ss_replacement_d3_022(ss_replacement_d2_022):
    feature = _clean(ss_replacement_d2_022)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00011000).reindex(feature.index)
SS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ss_replacement_d3_022'] = {'inputs': ['ss_replacement_d2_022'], 'func': ss_replacement_d3_022}


def ss_replacement_d3_023(ss_replacement_d2_023):
    feature = _clean(ss_replacement_d2_023)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00011500).reindex(feature.index)
SS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ss_replacement_d3_023'] = {'inputs': ['ss_replacement_d2_023'], 'func': ss_replacement_d3_023}


def ss_replacement_d3_024(ss_replacement_d2_024):
    feature = _clean(ss_replacement_d2_024)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00012000).reindex(feature.index)
SS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ss_replacement_d3_024'] = {'inputs': ['ss_replacement_d2_024'], 'func': ss_replacement_d3_024}


def ss_replacement_d3_025(ss_replacement_d2_025):
    feature = _clean(ss_replacement_d2_025)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00012500).reindex(feature.index)
SS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ss_replacement_d3_025'] = {'inputs': ['ss_replacement_d2_025'], 'func': ss_replacement_d3_025}


def ss_replacement_d3_026(ss_replacement_d2_026):
    feature = _clean(ss_replacement_d2_026)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00013000).reindex(feature.index)
SS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ss_replacement_d3_026'] = {'inputs': ['ss_replacement_d2_026'], 'func': ss_replacement_d3_026}


def ss_replacement_d3_027(ss_replacement_d2_027):
    feature = _clean(ss_replacement_d2_027)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00013500).reindex(feature.index)
SS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ss_replacement_d3_027'] = {'inputs': ['ss_replacement_d2_027'], 'func': ss_replacement_d3_027}


def ss_replacement_d3_028(ss_replacement_d2_028):
    feature = _clean(ss_replacement_d2_028)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00014000).reindex(feature.index)
SS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ss_replacement_d3_028'] = {'inputs': ['ss_replacement_d2_028'], 'func': ss_replacement_d3_028}


def ss_replacement_d3_029(ss_replacement_d2_029):
    feature = _clean(ss_replacement_d2_029)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00014500).reindex(feature.index)
SS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ss_replacement_d3_029'] = {'inputs': ['ss_replacement_d2_029'], 'func': ss_replacement_d3_029}


def ss_replacement_d3_030(ss_replacement_d2_030):
    feature = _clean(ss_replacement_d2_030)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00015000).reindex(feature.index)
SS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ss_replacement_d3_030'] = {'inputs': ['ss_replacement_d2_030'], 'func': ss_replacement_d3_030}


def ss_replacement_d3_031(ss_replacement_d2_031):
    feature = _clean(ss_replacement_d2_031)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00015500).reindex(feature.index)
SS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ss_replacement_d3_031'] = {'inputs': ['ss_replacement_d2_031'], 'func': ss_replacement_d3_031}


def ss_replacement_d3_032(ss_replacement_d2_032):
    feature = _clean(ss_replacement_d2_032)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00016000).reindex(feature.index)
SS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ss_replacement_d3_032'] = {'inputs': ['ss_replacement_d2_032'], 'func': ss_replacement_d3_032}


def ss_replacement_d3_033(ss_replacement_d2_033):
    feature = _clean(ss_replacement_d2_033)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00016500).reindex(feature.index)
SS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ss_replacement_d3_033'] = {'inputs': ['ss_replacement_d2_033'], 'func': ss_replacement_d3_033}


def ss_replacement_d3_034(ss_replacement_d2_034):
    feature = _clean(ss_replacement_d2_034)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00017000).reindex(feature.index)
SS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ss_replacement_d3_034'] = {'inputs': ['ss_replacement_d2_034'], 'func': ss_replacement_d3_034}


def ss_replacement_d3_035(ss_replacement_d2_035):
    feature = _clean(ss_replacement_d2_035)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00017500).reindex(feature.index)
SS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ss_replacement_d3_035'] = {'inputs': ['ss_replacement_d2_035'], 'func': ss_replacement_d3_035}


def ss_replacement_d3_036(ss_replacement_d2_036):
    feature = _clean(ss_replacement_d2_036)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00018000).reindex(feature.index)
SS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ss_replacement_d3_036'] = {'inputs': ['ss_replacement_d2_036'], 'func': ss_replacement_d3_036}


def ss_replacement_d3_037(ss_replacement_d2_037):
    feature = _clean(ss_replacement_d2_037)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00018500).reindex(feature.index)
SS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ss_replacement_d3_037'] = {'inputs': ['ss_replacement_d2_037'], 'func': ss_replacement_d3_037}


def ss_replacement_d3_038(ss_replacement_d2_038):
    feature = _clean(ss_replacement_d2_038)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00019000).reindex(feature.index)
SS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ss_replacement_d3_038'] = {'inputs': ['ss_replacement_d2_038'], 'func': ss_replacement_d3_038}


def ss_replacement_d3_039(ss_replacement_d2_039):
    feature = _clean(ss_replacement_d2_039)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00019500).reindex(feature.index)
SS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ss_replacement_d3_039'] = {'inputs': ['ss_replacement_d2_039'], 'func': ss_replacement_d3_039}


def ss_replacement_d3_040(ss_replacement_d2_040):
    feature = _clean(ss_replacement_d2_040)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00020000).reindex(feature.index)
SS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ss_replacement_d3_040'] = {'inputs': ['ss_replacement_d2_040'], 'func': ss_replacement_d3_040}


def ss_replacement_d3_041(ss_replacement_d2_041):
    feature = _clean(ss_replacement_d2_041)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00020500).reindex(feature.index)
SS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ss_replacement_d3_041'] = {'inputs': ['ss_replacement_d2_041'], 'func': ss_replacement_d3_041}


def ss_replacement_d3_042(ss_replacement_d2_042):
    feature = _clean(ss_replacement_d2_042)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00021000).reindex(feature.index)
SS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ss_replacement_d3_042'] = {'inputs': ['ss_replacement_d2_042'], 'func': ss_replacement_d3_042}


def ss_replacement_d3_043(ss_replacement_d2_043):
    feature = _clean(ss_replacement_d2_043)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00021500).reindex(feature.index)
SS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ss_replacement_d3_043'] = {'inputs': ['ss_replacement_d2_043'], 'func': ss_replacement_d3_043}


def ss_replacement_d3_044(ss_replacement_d2_044):
    feature = _clean(ss_replacement_d2_044)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00022000).reindex(feature.index)
SS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ss_replacement_d3_044'] = {'inputs': ['ss_replacement_d2_044'], 'func': ss_replacement_d3_044}


def ss_replacement_d3_045(ss_replacement_d2_045):
    feature = _clean(ss_replacement_d2_045)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00022500).reindex(feature.index)
SS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ss_replacement_d3_045'] = {'inputs': ['ss_replacement_d2_045'], 'func': ss_replacement_d3_045}


def ss_replacement_d3_046(ss_replacement_d2_046):
    feature = _clean(ss_replacement_d2_046)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00023000).reindex(feature.index)
SS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ss_replacement_d3_046'] = {'inputs': ['ss_replacement_d2_046'], 'func': ss_replacement_d3_046}


def ss_replacement_d3_047(ss_replacement_d2_047):
    feature = _clean(ss_replacement_d2_047)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00023500).reindex(feature.index)
SS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ss_replacement_d3_047'] = {'inputs': ['ss_replacement_d2_047'], 'func': ss_replacement_d3_047}


def ss_replacement_d3_048(ss_replacement_d2_048):
    feature = _clean(ss_replacement_d2_048)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00024000).reindex(feature.index)
SS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ss_replacement_d3_048'] = {'inputs': ['ss_replacement_d2_048'], 'func': ss_replacement_d3_048}


def ss_replacement_d3_049(ss_replacement_d2_049):
    feature = _clean(ss_replacement_d2_049)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00024500).reindex(feature.index)
SS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ss_replacement_d3_049'] = {'inputs': ['ss_replacement_d2_049'], 'func': ss_replacement_d3_049}


def ss_replacement_d3_050(ss_replacement_d2_050):
    feature = _clean(ss_replacement_d2_050)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00025000).reindex(feature.index)
SS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ss_replacement_d3_050'] = {'inputs': ['ss_replacement_d2_050'], 'func': ss_replacement_d3_050}


def ss_replacement_d3_051(ss_replacement_d2_051):
    feature = _clean(ss_replacement_d2_051)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00025500).reindex(feature.index)
SS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ss_replacement_d3_051'] = {'inputs': ['ss_replacement_d2_051'], 'func': ss_replacement_d3_051}


def ss_replacement_d3_052(ss_replacement_d2_052):
    feature = _clean(ss_replacement_d2_052)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00026000).reindex(feature.index)
SS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ss_replacement_d3_052'] = {'inputs': ['ss_replacement_d2_052'], 'func': ss_replacement_d3_052}


def ss_replacement_d3_053(ss_replacement_d2_053):
    feature = _clean(ss_replacement_d2_053)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00026500).reindex(feature.index)
SS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ss_replacement_d3_053'] = {'inputs': ['ss_replacement_d2_053'], 'func': ss_replacement_d3_053}


def ss_replacement_d3_054(ss_replacement_d2_054):
    feature = _clean(ss_replacement_d2_054)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00027000).reindex(feature.index)
SS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ss_replacement_d3_054'] = {'inputs': ['ss_replacement_d2_054'], 'func': ss_replacement_d3_054}


def ss_replacement_d3_055(ss_replacement_d2_055):
    feature = _clean(ss_replacement_d2_055)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00027500).reindex(feature.index)
SS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ss_replacement_d3_055'] = {'inputs': ['ss_replacement_d2_055'], 'func': ss_replacement_d3_055}


def ss_replacement_d3_056(ss_replacement_d2_056):
    feature = _clean(ss_replacement_d2_056)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00028000).reindex(feature.index)
SS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ss_replacement_d3_056'] = {'inputs': ['ss_replacement_d2_056'], 'func': ss_replacement_d3_056}


def ss_replacement_d3_057(ss_replacement_d2_057):
    feature = _clean(ss_replacement_d2_057)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00028500).reindex(feature.index)
SS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ss_replacement_d3_057'] = {'inputs': ['ss_replacement_d2_057'], 'func': ss_replacement_d3_057}


def ss_replacement_d3_058(ss_replacement_d2_058):
    feature = _clean(ss_replacement_d2_058)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00029000).reindex(feature.index)
SS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ss_replacement_d3_058'] = {'inputs': ['ss_replacement_d2_058'], 'func': ss_replacement_d3_058}


def ss_replacement_d3_059(ss_replacement_d2_059):
    feature = _clean(ss_replacement_d2_059)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00029500).reindex(feature.index)
SS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ss_replacement_d3_059'] = {'inputs': ['ss_replacement_d2_059'], 'func': ss_replacement_d3_059}


def ss_replacement_d3_060(ss_replacement_d2_060):
    feature = _clean(ss_replacement_d2_060)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00030000).reindex(feature.index)
SS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ss_replacement_d3_060'] = {'inputs': ['ss_replacement_d2_060'], 'func': ss_replacement_d3_060}


def ss_replacement_d3_061(ss_replacement_d2_061):
    feature = _clean(ss_replacement_d2_061)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00030500).reindex(feature.index)
SS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ss_replacement_d3_061'] = {'inputs': ['ss_replacement_d2_061'], 'func': ss_replacement_d3_061}


def ss_replacement_d3_062(ss_replacement_d2_062):
    feature = _clean(ss_replacement_d2_062)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00031000).reindex(feature.index)
SS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ss_replacement_d3_062'] = {'inputs': ['ss_replacement_d2_062'], 'func': ss_replacement_d3_062}


def ss_replacement_d3_063(ss_replacement_d2_063):
    feature = _clean(ss_replacement_d2_063)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00031500).reindex(feature.index)
SS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ss_replacement_d3_063'] = {'inputs': ['ss_replacement_d2_063'], 'func': ss_replacement_d3_063}


def ss_replacement_d3_064(ss_replacement_d2_064):
    feature = _clean(ss_replacement_d2_064)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00032000).reindex(feature.index)
SS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ss_replacement_d3_064'] = {'inputs': ['ss_replacement_d2_064'], 'func': ss_replacement_d3_064}


def ss_replacement_d3_065(ss_replacement_d2_065):
    feature = _clean(ss_replacement_d2_065)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00032500).reindex(feature.index)
SS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ss_replacement_d3_065'] = {'inputs': ['ss_replacement_d2_065'], 'func': ss_replacement_d3_065}


def ss_replacement_d3_066(ss_replacement_d2_066):
    feature = _clean(ss_replacement_d2_066)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00033000).reindex(feature.index)
SS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ss_replacement_d3_066'] = {'inputs': ['ss_replacement_d2_066'], 'func': ss_replacement_d3_066}


def ss_replacement_d3_067(ss_replacement_d2_067):
    feature = _clean(ss_replacement_d2_067)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00033500).reindex(feature.index)
SS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ss_replacement_d3_067'] = {'inputs': ['ss_replacement_d2_067'], 'func': ss_replacement_d3_067}


def ss_replacement_d3_068(ss_replacement_d2_068):
    feature = _clean(ss_replacement_d2_068)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00034000).reindex(feature.index)
SS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ss_replacement_d3_068'] = {'inputs': ['ss_replacement_d2_068'], 'func': ss_replacement_d3_068}


def ss_replacement_d3_069(ss_replacement_d2_069):
    feature = _clean(ss_replacement_d2_069)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00034500).reindex(feature.index)
SS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ss_replacement_d3_069'] = {'inputs': ['ss_replacement_d2_069'], 'func': ss_replacement_d3_069}


def ss_replacement_d3_070(ss_replacement_d2_070):
    feature = _clean(ss_replacement_d2_070)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00035000).reindex(feature.index)
SS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ss_replacement_d3_070'] = {'inputs': ['ss_replacement_d2_070'], 'func': ss_replacement_d3_070}


def ss_replacement_d3_071(ss_replacement_d2_071):
    feature = _clean(ss_replacement_d2_071)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00035500).reindex(feature.index)
SS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ss_replacement_d3_071'] = {'inputs': ['ss_replacement_d2_071'], 'func': ss_replacement_d3_071}


def ss_replacement_d3_072(ss_replacement_d2_072):
    feature = _clean(ss_replacement_d2_072)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00036000).reindex(feature.index)
SS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ss_replacement_d3_072'] = {'inputs': ['ss_replacement_d2_072'], 'func': ss_replacement_d3_072}


def ss_replacement_d3_073(ss_replacement_d2_073):
    feature = _clean(ss_replacement_d2_073)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00036500).reindex(feature.index)
SS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ss_replacement_d3_073'] = {'inputs': ['ss_replacement_d2_073'], 'func': ss_replacement_d3_073}


def ss_replacement_d3_074(ss_replacement_d2_074):
    feature = _clean(ss_replacement_d2_074)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00037000).reindex(feature.index)
SS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ss_replacement_d3_074'] = {'inputs': ['ss_replacement_d2_074'], 'func': ss_replacement_d3_074}


def ss_replacement_d3_075(ss_replacement_d2_075):
    feature = _clean(ss_replacement_d2_075)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00037500).reindex(feature.index)
SS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ss_replacement_d3_075'] = {'inputs': ['ss_replacement_d2_075'], 'func': ss_replacement_d3_075}


def ss_replacement_d3_076(ss_replacement_d2_076):
    feature = _clean(ss_replacement_d2_076)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00038000).reindex(feature.index)
SS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ss_replacement_d3_076'] = {'inputs': ['ss_replacement_d2_076'], 'func': ss_replacement_d3_076}


def ss_replacement_d3_077(ss_replacement_d2_077):
    feature = _clean(ss_replacement_d2_077)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00038500).reindex(feature.index)
SS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ss_replacement_d3_077'] = {'inputs': ['ss_replacement_d2_077'], 'func': ss_replacement_d3_077}


def ss_replacement_d3_078(ss_replacement_d2_078):
    feature = _clean(ss_replacement_d2_078)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00039000).reindex(feature.index)
SS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ss_replacement_d3_078'] = {'inputs': ['ss_replacement_d2_078'], 'func': ss_replacement_d3_078}


def ss_replacement_d3_079(ss_replacement_d2_079):
    feature = _clean(ss_replacement_d2_079)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00039500).reindex(feature.index)
SS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ss_replacement_d3_079'] = {'inputs': ['ss_replacement_d2_079'], 'func': ss_replacement_d3_079}


def ss_replacement_d3_080(ss_replacement_d2_080):
    feature = _clean(ss_replacement_d2_080)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00040000).reindex(feature.index)
SS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ss_replacement_d3_080'] = {'inputs': ['ss_replacement_d2_080'], 'func': ss_replacement_d3_080}


def ss_replacement_d3_081(ss_replacement_d2_081):
    feature = _clean(ss_replacement_d2_081)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00040500).reindex(feature.index)
SS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ss_replacement_d3_081'] = {'inputs': ['ss_replacement_d2_081'], 'func': ss_replacement_d3_081}


def ss_replacement_d3_082(ss_replacement_d2_082):
    feature = _clean(ss_replacement_d2_082)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00041000).reindex(feature.index)
SS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ss_replacement_d3_082'] = {'inputs': ['ss_replacement_d2_082'], 'func': ss_replacement_d3_082}


def ss_replacement_d3_083(ss_replacement_d2_083):
    feature = _clean(ss_replacement_d2_083)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00041500).reindex(feature.index)
SS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ss_replacement_d3_083'] = {'inputs': ['ss_replacement_d2_083'], 'func': ss_replacement_d3_083}


def ss_replacement_d3_084(ss_replacement_d2_084):
    feature = _clean(ss_replacement_d2_084)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00042000).reindex(feature.index)
SS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ss_replacement_d3_084'] = {'inputs': ['ss_replacement_d2_084'], 'func': ss_replacement_d3_084}


def ss_replacement_d3_085(ss_replacement_d2_085):
    feature = _clean(ss_replacement_d2_085)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00042500).reindex(feature.index)
SS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ss_replacement_d3_085'] = {'inputs': ['ss_replacement_d2_085'], 'func': ss_replacement_d3_085}


def ss_replacement_d3_086(ss_replacement_d2_086):
    feature = _clean(ss_replacement_d2_086)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00043000).reindex(feature.index)
SS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ss_replacement_d3_086'] = {'inputs': ['ss_replacement_d2_086'], 'func': ss_replacement_d3_086}


def ss_replacement_d3_087(ss_replacement_d2_087):
    feature = _clean(ss_replacement_d2_087)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00043500).reindex(feature.index)
SS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ss_replacement_d3_087'] = {'inputs': ['ss_replacement_d2_087'], 'func': ss_replacement_d3_087}


def ss_replacement_d3_088(ss_replacement_d2_088):
    feature = _clean(ss_replacement_d2_088)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00044000).reindex(feature.index)
SS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ss_replacement_d3_088'] = {'inputs': ['ss_replacement_d2_088'], 'func': ss_replacement_d3_088}


def ss_replacement_d3_089(ss_replacement_d2_089):
    feature = _clean(ss_replacement_d2_089)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00044500).reindex(feature.index)
SS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ss_replacement_d3_089'] = {'inputs': ['ss_replacement_d2_089'], 'func': ss_replacement_d3_089}


def ss_replacement_d3_090(ss_replacement_d2_090):
    feature = _clean(ss_replacement_d2_090)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00045000).reindex(feature.index)
SS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ss_replacement_d3_090'] = {'inputs': ['ss_replacement_d2_090'], 'func': ss_replacement_d3_090}


def ss_replacement_d3_091(ss_replacement_d2_091):
    feature = _clean(ss_replacement_d2_091)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00045500).reindex(feature.index)
SS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ss_replacement_d3_091'] = {'inputs': ['ss_replacement_d2_091'], 'func': ss_replacement_d3_091}


def ss_replacement_d3_092(ss_replacement_d2_092):
    feature = _clean(ss_replacement_d2_092)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00046000).reindex(feature.index)
SS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ss_replacement_d3_092'] = {'inputs': ['ss_replacement_d2_092'], 'func': ss_replacement_d3_092}


def ss_replacement_d3_093(ss_replacement_d2_093):
    feature = _clean(ss_replacement_d2_093)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00046500).reindex(feature.index)
SS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ss_replacement_d3_093'] = {'inputs': ['ss_replacement_d2_093'], 'func': ss_replacement_d3_093}


def ss_replacement_d3_094(ss_replacement_d2_094):
    feature = _clean(ss_replacement_d2_094)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00047000).reindex(feature.index)
SS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ss_replacement_d3_094'] = {'inputs': ['ss_replacement_d2_094'], 'func': ss_replacement_d3_094}


def ss_replacement_d3_095(ss_replacement_d2_095):
    feature = _clean(ss_replacement_d2_095)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00047500).reindex(feature.index)
SS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ss_replacement_d3_095'] = {'inputs': ['ss_replacement_d2_095'], 'func': ss_replacement_d3_095}


def ss_replacement_d3_096(ss_replacement_d2_096):
    feature = _clean(ss_replacement_d2_096)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00048000).reindex(feature.index)
SS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ss_replacement_d3_096'] = {'inputs': ['ss_replacement_d2_096'], 'func': ss_replacement_d3_096}


def ss_replacement_d3_097(ss_replacement_d2_097):
    feature = _clean(ss_replacement_d2_097)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00048500).reindex(feature.index)
SS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ss_replacement_d3_097'] = {'inputs': ['ss_replacement_d2_097'], 'func': ss_replacement_d3_097}


def ss_replacement_d3_098(ss_replacement_d2_098):
    feature = _clean(ss_replacement_d2_098)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00049000).reindex(feature.index)
SS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ss_replacement_d3_098'] = {'inputs': ['ss_replacement_d2_098'], 'func': ss_replacement_d3_098}


def ss_replacement_d3_099(ss_replacement_d2_099):
    feature = _clean(ss_replacement_d2_099)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00049500).reindex(feature.index)
SS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ss_replacement_d3_099'] = {'inputs': ['ss_replacement_d2_099'], 'func': ss_replacement_d3_099}


def ss_replacement_d3_100(ss_replacement_d2_100):
    feature = _clean(ss_replacement_d2_100)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00050000).reindex(feature.index)
SS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ss_replacement_d3_100'] = {'inputs': ['ss_replacement_d2_100'], 'func': ss_replacement_d3_100}


def ss_replacement_d3_101(ss_replacement_d2_101):
    feature = _clean(ss_replacement_d2_101)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00050500).reindex(feature.index)
SS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ss_replacement_d3_101'] = {'inputs': ['ss_replacement_d2_101'], 'func': ss_replacement_d3_101}


def ss_replacement_d3_102(ss_replacement_d2_102):
    feature = _clean(ss_replacement_d2_102)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00051000).reindex(feature.index)
SS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ss_replacement_d3_102'] = {'inputs': ['ss_replacement_d2_102'], 'func': ss_replacement_d3_102}


def ss_replacement_d3_103(ss_replacement_d2_103):
    feature = _clean(ss_replacement_d2_103)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00051500).reindex(feature.index)
SS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ss_replacement_d3_103'] = {'inputs': ['ss_replacement_d2_103'], 'func': ss_replacement_d3_103}


def ss_replacement_d3_104(ss_replacement_d2_104):
    feature = _clean(ss_replacement_d2_104)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00052000).reindex(feature.index)
SS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ss_replacement_d3_104'] = {'inputs': ['ss_replacement_d2_104'], 'func': ss_replacement_d3_104}


def ss_replacement_d3_105(ss_replacement_d2_105):
    feature = _clean(ss_replacement_d2_105)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00052500).reindex(feature.index)
SS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ss_replacement_d3_105'] = {'inputs': ['ss_replacement_d2_105'], 'func': ss_replacement_d3_105}


def ss_replacement_d3_106(ss_replacement_d2_106):
    feature = _clean(ss_replacement_d2_106)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00053000).reindex(feature.index)
SS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ss_replacement_d3_106'] = {'inputs': ['ss_replacement_d2_106'], 'func': ss_replacement_d3_106}


def ss_replacement_d3_107(ss_replacement_d2_107):
    feature = _clean(ss_replacement_d2_107)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00053500).reindex(feature.index)
SS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ss_replacement_d3_107'] = {'inputs': ['ss_replacement_d2_107'], 'func': ss_replacement_d3_107}


def ss_replacement_d3_108(ss_replacement_d2_108):
    feature = _clean(ss_replacement_d2_108)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00054000).reindex(feature.index)
SS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ss_replacement_d3_108'] = {'inputs': ['ss_replacement_d2_108'], 'func': ss_replacement_d3_108}


def ss_replacement_d3_109(ss_replacement_d2_109):
    feature = _clean(ss_replacement_d2_109)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00054500).reindex(feature.index)
SS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ss_replacement_d3_109'] = {'inputs': ['ss_replacement_d2_109'], 'func': ss_replacement_d3_109}


def ss_replacement_d3_110(ss_replacement_d2_110):
    feature = _clean(ss_replacement_d2_110)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00055000).reindex(feature.index)
SS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ss_replacement_d3_110'] = {'inputs': ['ss_replacement_d2_110'], 'func': ss_replacement_d3_110}


def ss_replacement_d3_111(ss_replacement_d2_111):
    feature = _clean(ss_replacement_d2_111)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00055500).reindex(feature.index)
SS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ss_replacement_d3_111'] = {'inputs': ['ss_replacement_d2_111'], 'func': ss_replacement_d3_111}


def ss_replacement_d3_112(ss_replacement_d2_112):
    feature = _clean(ss_replacement_d2_112)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00056000).reindex(feature.index)
SS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ss_replacement_d3_112'] = {'inputs': ['ss_replacement_d2_112'], 'func': ss_replacement_d3_112}


def ss_replacement_d3_113(ss_replacement_d2_113):
    feature = _clean(ss_replacement_d2_113)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00056500).reindex(feature.index)
SS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ss_replacement_d3_113'] = {'inputs': ['ss_replacement_d2_113'], 'func': ss_replacement_d3_113}


def ss_replacement_d3_114(ss_replacement_d2_114):
    feature = _clean(ss_replacement_d2_114)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00057000).reindex(feature.index)
SS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ss_replacement_d3_114'] = {'inputs': ['ss_replacement_d2_114'], 'func': ss_replacement_d3_114}


def ss_replacement_d3_115(ss_replacement_d2_115):
    feature = _clean(ss_replacement_d2_115)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00057500).reindex(feature.index)
SS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ss_replacement_d3_115'] = {'inputs': ['ss_replacement_d2_115'], 'func': ss_replacement_d3_115}


def ss_replacement_d3_116(ss_replacement_d2_116):
    feature = _clean(ss_replacement_d2_116)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00058000).reindex(feature.index)
SS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ss_replacement_d3_116'] = {'inputs': ['ss_replacement_d2_116'], 'func': ss_replacement_d3_116}


def ss_replacement_d3_117(ss_replacement_d2_117):
    feature = _clean(ss_replacement_d2_117)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00058500).reindex(feature.index)
SS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ss_replacement_d3_117'] = {'inputs': ['ss_replacement_d2_117'], 'func': ss_replacement_d3_117}


def ss_replacement_d3_118(ss_replacement_d2_118):
    feature = _clean(ss_replacement_d2_118)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00059000).reindex(feature.index)
SS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ss_replacement_d3_118'] = {'inputs': ['ss_replacement_d2_118'], 'func': ss_replacement_d3_118}


def ss_replacement_d3_119(ss_replacement_d2_119):
    feature = _clean(ss_replacement_d2_119)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00059500).reindex(feature.index)
SS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ss_replacement_d3_119'] = {'inputs': ['ss_replacement_d2_119'], 'func': ss_replacement_d3_119}


def ss_replacement_d3_120(ss_replacement_d2_120):
    feature = _clean(ss_replacement_d2_120)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00060000).reindex(feature.index)
SS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ss_replacement_d3_120'] = {'inputs': ['ss_replacement_d2_120'], 'func': ss_replacement_d3_120}


def ss_replacement_d3_121(ss_replacement_d2_121):
    feature = _clean(ss_replacement_d2_121)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00060500).reindex(feature.index)
SS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ss_replacement_d3_121'] = {'inputs': ['ss_replacement_d2_121'], 'func': ss_replacement_d3_121}


def ss_replacement_d3_122(ss_replacement_d2_122):
    feature = _clean(ss_replacement_d2_122)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00061000).reindex(feature.index)
SS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ss_replacement_d3_122'] = {'inputs': ['ss_replacement_d2_122'], 'func': ss_replacement_d3_122}


def ss_replacement_d3_123(ss_replacement_d2_123):
    feature = _clean(ss_replacement_d2_123)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00061500).reindex(feature.index)
SS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ss_replacement_d3_123'] = {'inputs': ['ss_replacement_d2_123'], 'func': ss_replacement_d3_123}


def ss_replacement_d3_124(ss_replacement_d2_124):
    feature = _clean(ss_replacement_d2_124)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00062000).reindex(feature.index)
SS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ss_replacement_d3_124'] = {'inputs': ['ss_replacement_d2_124'], 'func': ss_replacement_d3_124}


def ss_replacement_d3_125(ss_replacement_d2_125):
    feature = _clean(ss_replacement_d2_125)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00062500).reindex(feature.index)
SS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ss_replacement_d3_125'] = {'inputs': ['ss_replacement_d2_125'], 'func': ss_replacement_d3_125}


def ss_replacement_d3_126(ss_replacement_d2_126):
    feature = _clean(ss_replacement_d2_126)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00063000).reindex(feature.index)
SS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ss_replacement_d3_126'] = {'inputs': ['ss_replacement_d2_126'], 'func': ss_replacement_d3_126}


def ss_replacement_d3_127(ss_replacement_d2_127):
    feature = _clean(ss_replacement_d2_127)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00063500).reindex(feature.index)
SS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ss_replacement_d3_127'] = {'inputs': ['ss_replacement_d2_127'], 'func': ss_replacement_d3_127}


def ss_replacement_d3_128(ss_replacement_d2_128):
    feature = _clean(ss_replacement_d2_128)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00064000).reindex(feature.index)
SS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ss_replacement_d3_128'] = {'inputs': ['ss_replacement_d2_128'], 'func': ss_replacement_d3_128}


def ss_replacement_d3_129(ss_replacement_d2_129):
    feature = _clean(ss_replacement_d2_129)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00064500).reindex(feature.index)
SS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ss_replacement_d3_129'] = {'inputs': ['ss_replacement_d2_129'], 'func': ss_replacement_d3_129}


def ss_replacement_d3_130(ss_replacement_d2_130):
    feature = _clean(ss_replacement_d2_130)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00065000).reindex(feature.index)
SS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ss_replacement_d3_130'] = {'inputs': ['ss_replacement_d2_130'], 'func': ss_replacement_d3_130}


def ss_replacement_d3_131(ss_replacement_d2_131):
    feature = _clean(ss_replacement_d2_131)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00065500).reindex(feature.index)
SS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ss_replacement_d3_131'] = {'inputs': ['ss_replacement_d2_131'], 'func': ss_replacement_d3_131}


def ss_replacement_d3_132(ss_replacement_d2_132):
    feature = _clean(ss_replacement_d2_132)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00066000).reindex(feature.index)
SS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ss_replacement_d3_132'] = {'inputs': ['ss_replacement_d2_132'], 'func': ss_replacement_d3_132}


def ss_replacement_d3_133(ss_replacement_d2_133):
    feature = _clean(ss_replacement_d2_133)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00066500).reindex(feature.index)
SS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ss_replacement_d3_133'] = {'inputs': ['ss_replacement_d2_133'], 'func': ss_replacement_d3_133}


def ss_replacement_d3_134(ss_replacement_d2_134):
    feature = _clean(ss_replacement_d2_134)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00067000).reindex(feature.index)
SS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ss_replacement_d3_134'] = {'inputs': ['ss_replacement_d2_134'], 'func': ss_replacement_d3_134}


def ss_replacement_d3_135(ss_replacement_d2_135):
    feature = _clean(ss_replacement_d2_135)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00067500).reindex(feature.index)
SS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ss_replacement_d3_135'] = {'inputs': ['ss_replacement_d2_135'], 'func': ss_replacement_d3_135}


def ss_replacement_d3_136(ss_replacement_d2_136):
    feature = _clean(ss_replacement_d2_136)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00068000).reindex(feature.index)
SS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ss_replacement_d3_136'] = {'inputs': ['ss_replacement_d2_136'], 'func': ss_replacement_d3_136}


def ss_replacement_d3_137(ss_replacement_d2_137):
    feature = _clean(ss_replacement_d2_137)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00068500).reindex(feature.index)
SS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ss_replacement_d3_137'] = {'inputs': ['ss_replacement_d2_137'], 'func': ss_replacement_d3_137}


def ss_replacement_d3_138(ss_replacement_d2_138):
    feature = _clean(ss_replacement_d2_138)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00069000).reindex(feature.index)
SS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ss_replacement_d3_138'] = {'inputs': ['ss_replacement_d2_138'], 'func': ss_replacement_d3_138}


def ss_replacement_d3_139(ss_replacement_d2_139):
    feature = _clean(ss_replacement_d2_139)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00069500).reindex(feature.index)
SS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ss_replacement_d3_139'] = {'inputs': ['ss_replacement_d2_139'], 'func': ss_replacement_d3_139}


def ss_replacement_d3_140(ss_replacement_d2_140):
    feature = _clean(ss_replacement_d2_140)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00070000).reindex(feature.index)
SS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ss_replacement_d3_140'] = {'inputs': ['ss_replacement_d2_140'], 'func': ss_replacement_d3_140}


def ss_replacement_d3_141(ss_replacement_d2_141):
    feature = _clean(ss_replacement_d2_141)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00070500).reindex(feature.index)
SS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ss_replacement_d3_141'] = {'inputs': ['ss_replacement_d2_141'], 'func': ss_replacement_d3_141}


def ss_replacement_d3_142(ss_replacement_d2_142):
    feature = _clean(ss_replacement_d2_142)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00071000).reindex(feature.index)
SS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ss_replacement_d3_142'] = {'inputs': ['ss_replacement_d2_142'], 'func': ss_replacement_d3_142}


def ss_replacement_d3_143(ss_replacement_d2_143):
    feature = _clean(ss_replacement_d2_143)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00071500).reindex(feature.index)
SS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ss_replacement_d3_143'] = {'inputs': ['ss_replacement_d2_143'], 'func': ss_replacement_d3_143}


def ss_replacement_d3_144(ss_replacement_d2_144):
    feature = _clean(ss_replacement_d2_144)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00072000).reindex(feature.index)
SS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ss_replacement_d3_144'] = {'inputs': ['ss_replacement_d2_144'], 'func': ss_replacement_d3_144}


def ss_replacement_d3_145(ss_replacement_d2_145):
    feature = _clean(ss_replacement_d2_145)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00072500).reindex(feature.index)
SS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ss_replacement_d3_145'] = {'inputs': ['ss_replacement_d2_145'], 'func': ss_replacement_d3_145}


def ss_replacement_d3_146(ss_replacement_d2_146):
    feature = _clean(ss_replacement_d2_146)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00073000).reindex(feature.index)
SS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ss_replacement_d3_146'] = {'inputs': ['ss_replacement_d2_146'], 'func': ss_replacement_d3_146}


def ss_replacement_d3_147(ss_replacement_d2_147):
    feature = _clean(ss_replacement_d2_147)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00073500).reindex(feature.index)
SS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ss_replacement_d3_147'] = {'inputs': ['ss_replacement_d2_147'], 'func': ss_replacement_d3_147}


def ss_replacement_d3_148(ss_replacement_d2_148):
    feature = _clean(ss_replacement_d2_148)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00074000).reindex(feature.index)
SS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ss_replacement_d3_148'] = {'inputs': ['ss_replacement_d2_148'], 'func': ss_replacement_d3_148}


def ss_replacement_d3_149(ss_replacement_d2_149):
    feature = _clean(ss_replacement_d2_149)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00074500).reindex(feature.index)
SS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ss_replacement_d3_149'] = {'inputs': ['ss_replacement_d2_149'], 'func': ss_replacement_d3_149}


def ss_replacement_d3_150(ss_replacement_d2_150):
    feature = _clean(ss_replacement_d2_150)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00075000).reindex(feature.index)
SS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ss_replacement_d3_150'] = {'inputs': ['ss_replacement_d2_150'], 'func': ss_replacement_d3_150}


def ss_replacement_d3_151(ss_replacement_d2_151):
    feature = _clean(ss_replacement_d2_151)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00075500).reindex(feature.index)
SS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ss_replacement_d3_151'] = {'inputs': ['ss_replacement_d2_151'], 'func': ss_replacement_d3_151}


def ss_replacement_d3_152(ss_replacement_d2_152):
    feature = _clean(ss_replacement_d2_152)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00076000).reindex(feature.index)
SS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ss_replacement_d3_152'] = {'inputs': ['ss_replacement_d2_152'], 'func': ss_replacement_d3_152}


def ss_replacement_d3_153(ss_replacement_d2_153):
    feature = _clean(ss_replacement_d2_153)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00076500).reindex(feature.index)
SS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ss_replacement_d3_153'] = {'inputs': ['ss_replacement_d2_153'], 'func': ss_replacement_d3_153}


def ss_replacement_d3_154(ss_replacement_d2_154):
    feature = _clean(ss_replacement_d2_154)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00077000).reindex(feature.index)
SS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ss_replacement_d3_154'] = {'inputs': ['ss_replacement_d2_154'], 'func': ss_replacement_d3_154}


def ss_replacement_d3_155(ss_replacement_d2_155):
    feature = _clean(ss_replacement_d2_155)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00077500).reindex(feature.index)
SS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ss_replacement_d3_155'] = {'inputs': ['ss_replacement_d2_155'], 'func': ss_replacement_d3_155}


def ss_replacement_d3_156(ss_replacement_d2_156):
    feature = _clean(ss_replacement_d2_156)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00078000).reindex(feature.index)
SS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ss_replacement_d3_156'] = {'inputs': ['ss_replacement_d2_156'], 'func': ss_replacement_d3_156}


def ss_replacement_d3_157(ss_replacement_d2_157):
    feature = _clean(ss_replacement_d2_157)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00078500).reindex(feature.index)
SS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ss_replacement_d3_157'] = {'inputs': ['ss_replacement_d2_157'], 'func': ss_replacement_d3_157}


def ss_replacement_d3_158(ss_replacement_d2_158):
    feature = _clean(ss_replacement_d2_158)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00079000).reindex(feature.index)
SS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ss_replacement_d3_158'] = {'inputs': ['ss_replacement_d2_158'], 'func': ss_replacement_d3_158}


def ss_replacement_d3_159(ss_replacement_d2_159):
    feature = _clean(ss_replacement_d2_159)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00079500).reindex(feature.index)
SS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ss_replacement_d3_159'] = {'inputs': ['ss_replacement_d2_159'], 'func': ss_replacement_d3_159}


def ss_replacement_d3_160(ss_replacement_d2_160):
    feature = _clean(ss_replacement_d2_160)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00080000).reindex(feature.index)
SS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ss_replacement_d3_160'] = {'inputs': ['ss_replacement_d2_160'], 'func': ss_replacement_d3_160}


def ss_replacement_d3_161(ss_replacement_d2_161):
    feature = _clean(ss_replacement_d2_161)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00080500).reindex(feature.index)
SS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ss_replacement_d3_161'] = {'inputs': ['ss_replacement_d2_161'], 'func': ss_replacement_d3_161}


def ss_replacement_d3_162(ss_replacement_d2_162):
    feature = _clean(ss_replacement_d2_162)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00081000).reindex(feature.index)
SS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ss_replacement_d3_162'] = {'inputs': ['ss_replacement_d2_162'], 'func': ss_replacement_d3_162}


def ss_replacement_d3_163(ss_replacement_d2_163):
    feature = _clean(ss_replacement_d2_163)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00081500).reindex(feature.index)
SS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ss_replacement_d3_163'] = {'inputs': ['ss_replacement_d2_163'], 'func': ss_replacement_d3_163}


def ss_replacement_d3_164(ss_replacement_d2_164):
    feature = _clean(ss_replacement_d2_164)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00082000).reindex(feature.index)
SS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ss_replacement_d3_164'] = {'inputs': ['ss_replacement_d2_164'], 'func': ss_replacement_d3_164}


def ss_replacement_d3_165(ss_replacement_d2_165):
    feature = _clean(ss_replacement_d2_165)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00082500).reindex(feature.index)
SS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ss_replacement_d3_165'] = {'inputs': ['ss_replacement_d2_165'], 'func': ss_replacement_d3_165}


def ss_replacement_d3_166(ss_replacement_d2_166):
    feature = _clean(ss_replacement_d2_166)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00083000).reindex(feature.index)
SS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ss_replacement_d3_166'] = {'inputs': ['ss_replacement_d2_166'], 'func': ss_replacement_d3_166}


# Third-derivative extensions for repaired first-base features.
SLV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY = {}


def _base_universe_d3(feature, idx):
    feature = _clean(feature) if '_clean' in globals() else _s(feature).replace([np.inf, -np.inf], np.nan)
    windows = [1, 2, 3, 5, 8, 13, 21, 34, 55]
    lag = windows[(idx * 2) % len(windows)]
    smooth = windows[(idx * 5 + 2) % len(windows)]
    accel = feature.diff(lag)
    curve = feature - feature.rolling(max(3, smooth), min_periods=2).mean()
    out = accel + curve.fillna(0.0) * (0.00019 * ((idx % 19) + 1))
    return out.replace([np.inf, -np.inf], np.nan).reindex(feature.index)


def slv_base_universe_d3_001_slv_003_fcf_burn_to_cash_63(slv_base_universe_d2_001_slv_003_fcf_burn_to_cash_63):
    return _base_universe_d3(slv_base_universe_d2_001_slv_003_fcf_burn_to_cash_63, 1)
SLV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['slv_base_universe_d3_001_slv_003_fcf_burn_to_cash_63'] = {'inputs': ['slv_base_universe_d2_001_slv_003_fcf_burn_to_cash_63'], 'func': slv_base_universe_d3_001_slv_003_fcf_burn_to_cash_63}


def slv_base_universe_d3_002_slv_004_debt_to_equity_84(slv_base_universe_d2_002_slv_004_debt_to_equity_84):
    return _base_universe_d3(slv_base_universe_d2_002_slv_004_debt_to_equity_84, 2)
SLV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['slv_base_universe_d3_002_slv_004_debt_to_equity_84'] = {'inputs': ['slv_base_universe_d2_002_slv_004_debt_to_equity_84'], 'func': slv_base_universe_d3_002_slv_004_debt_to_equity_84}


def slv_base_universe_d3_003_slv_005_debt_to_assets_126(slv_base_universe_d2_003_slv_005_debt_to_assets_126):
    return _base_universe_d3(slv_base_universe_d2_003_slv_005_debt_to_assets_126, 3)
SLV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['slv_base_universe_d3_003_slv_005_debt_to_assets_126'] = {'inputs': ['slv_base_universe_d2_003_slv_005_debt_to_assets_126'], 'func': slv_base_universe_d3_003_slv_005_debt_to_assets_126}


def slv_base_universe_d3_004_slv_012_accrual_gap_1260(slv_base_universe_d2_004_slv_012_accrual_gap_1260):
    return _base_universe_d3(slv_base_universe_d2_004_slv_012_accrual_gap_1260, 4)
SLV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['slv_base_universe_d3_004_slv_012_accrual_gap_1260'] = {'inputs': ['slv_base_universe_d2_004_slv_012_accrual_gap_1260'], 'func': slv_base_universe_d3_004_slv_012_accrual_gap_1260}


def slv_base_universe_d3_005_slv_016_debt_to_equity_21(slv_base_universe_d2_005_slv_016_debt_to_equity_21):
    return _base_universe_d3(slv_base_universe_d2_005_slv_016_debt_to_equity_21, 5)
SLV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['slv_base_universe_d3_005_slv_016_debt_to_equity_21'] = {'inputs': ['slv_base_universe_d2_005_slv_016_debt_to_equity_21'], 'func': slv_base_universe_d3_005_slv_016_debt_to_equity_21}


def slv_base_universe_d3_006_slv_017_debt_to_assets_42(slv_base_universe_d2_006_slv_017_debt_to_assets_42):
    return _base_universe_d3(slv_base_universe_d2_006_slv_017_debt_to_assets_42, 6)
SLV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['slv_base_universe_d3_006_slv_017_debt_to_assets_42'] = {'inputs': ['slv_base_universe_d2_006_slv_017_debt_to_assets_42'], 'func': slv_base_universe_d3_006_slv_017_debt_to_assets_42}


def slv_base_universe_d3_007_slv_024_accrual_gap_504(slv_base_universe_d2_007_slv_024_accrual_gap_504):
    return _base_universe_d3(slv_base_universe_d2_007_slv_024_accrual_gap_504, 7)
SLV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['slv_base_universe_d3_007_slv_024_accrual_gap_504'] = {'inputs': ['slv_base_universe_d2_007_slv_024_accrual_gap_504'], 'func': slv_base_universe_d3_007_slv_024_accrual_gap_504}


def slv_base_universe_d3_008_slv_027_fcf_burn_to_cash_1260(slv_base_universe_d2_008_slv_027_fcf_burn_to_cash_1260):
    return _base_universe_d3(slv_base_universe_d2_008_slv_027_fcf_burn_to_cash_1260, 8)
SLV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['slv_base_universe_d3_008_slv_027_fcf_burn_to_cash_1260'] = {'inputs': ['slv_base_universe_d2_008_slv_027_fcf_burn_to_cash_1260'], 'func': slv_base_universe_d3_008_slv_027_fcf_burn_to_cash_1260}


def slv_base_universe_d3_009_slv_028_debt_to_equity_1512(slv_base_universe_d2_009_slv_028_debt_to_equity_1512):
    return _base_universe_d3(slv_base_universe_d2_009_slv_028_debt_to_equity_1512, 9)
SLV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['slv_base_universe_d3_009_slv_028_debt_to_equity_1512'] = {'inputs': ['slv_base_universe_d2_009_slv_028_debt_to_equity_1512'], 'func': slv_base_universe_d3_009_slv_028_debt_to_equity_1512}


def slv_base_universe_d3_010_slv_029_debt_to_assets_63(slv_base_universe_d2_010_slv_029_debt_to_assets_63):
    return _base_universe_d3(slv_base_universe_d2_010_slv_029_debt_to_assets_63, 10)
SLV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['slv_base_universe_d3_010_slv_029_debt_to_assets_63'] = {'inputs': ['slv_base_universe_d2_010_slv_029_debt_to_assets_63'], 'func': slv_base_universe_d3_010_slv_029_debt_to_assets_63}


def slv_base_universe_d3_011_slv_031_interest_coverage_stress_21(slv_base_universe_d2_011_slv_031_interest_coverage_stress_21):
    return _base_universe_d3(slv_base_universe_d2_011_slv_031_interest_coverage_stress_21, 11)
SLV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['slv_base_universe_d3_011_slv_031_interest_coverage_stress_21'] = {'inputs': ['slv_base_universe_d2_011_slv_031_interest_coverage_stress_21'], 'func': slv_base_universe_d3_011_slv_031_interest_coverage_stress_21}


def slv_base_universe_d3_012_slv_036_accrual_gap_189(slv_base_universe_d2_012_slv_036_accrual_gap_189):
    return _base_universe_d3(slv_base_universe_d2_012_slv_036_accrual_gap_189, 12)
SLV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['slv_base_universe_d3_012_slv_036_accrual_gap_189'] = {'inputs': ['slv_base_universe_d2_012_slv_036_accrual_gap_189'], 'func': slv_base_universe_d3_012_slv_036_accrual_gap_189}


def slv_base_universe_d3_013_slv_039_fcf_burn_to_cash_504(slv_base_universe_d2_013_slv_039_fcf_burn_to_cash_504):
    return _base_universe_d3(slv_base_universe_d2_013_slv_039_fcf_burn_to_cash_504, 13)
SLV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['slv_base_universe_d3_013_slv_039_fcf_burn_to_cash_504'] = {'inputs': ['slv_base_universe_d2_013_slv_039_fcf_burn_to_cash_504'], 'func': slv_base_universe_d3_013_slv_039_fcf_burn_to_cash_504}


def slv_base_universe_d3_014_slv_040_debt_to_equity_756(slv_base_universe_d2_014_slv_040_debt_to_equity_756):
    return _base_universe_d3(slv_base_universe_d2_014_slv_040_debt_to_equity_756, 14)
SLV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['slv_base_universe_d3_014_slv_040_debt_to_equity_756'] = {'inputs': ['slv_base_universe_d2_014_slv_040_debt_to_equity_756'], 'func': slv_base_universe_d3_014_slv_040_debt_to_equity_756}


def slv_base_universe_d3_015_slv_041_debt_to_assets_1008(slv_base_universe_d2_015_slv_041_debt_to_assets_1008):
    return _base_universe_d3(slv_base_universe_d2_015_slv_041_debt_to_assets_1008, 15)
SLV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['slv_base_universe_d3_015_slv_041_debt_to_assets_1008'] = {'inputs': ['slv_base_universe_d2_015_slv_041_debt_to_assets_1008'], 'func': slv_base_universe_d3_015_slv_041_debt_to_assets_1008}


def slv_base_universe_d3_016_slv_043_interest_coverage_stress_1512(slv_base_universe_d2_016_slv_043_interest_coverage_stress_1512):
    return _base_universe_d3(slv_base_universe_d2_016_slv_043_interest_coverage_stress_1512, 16)
SLV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['slv_base_universe_d3_016_slv_043_interest_coverage_stress_1512'] = {'inputs': ['slv_base_universe_d2_016_slv_043_interest_coverage_stress_1512'], 'func': slv_base_universe_d3_016_slv_043_interest_coverage_stress_1512}


def slv_base_universe_d3_017_slv_048_accrual_gap_63(slv_base_universe_d2_017_slv_048_accrual_gap_63):
    return _base_universe_d3(slv_base_universe_d2_017_slv_048_accrual_gap_63, 17)
SLV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['slv_base_universe_d3_017_slv_048_accrual_gap_63'] = {'inputs': ['slv_base_universe_d2_017_slv_048_accrual_gap_63'], 'func': slv_base_universe_d3_017_slv_048_accrual_gap_63}


def slv_base_universe_d3_018_slv_051_fcf_burn_to_cash_189(slv_base_universe_d2_018_slv_051_fcf_burn_to_cash_189):
    return _base_universe_d3(slv_base_universe_d2_018_slv_051_fcf_burn_to_cash_189, 18)
SLV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['slv_base_universe_d3_018_slv_051_fcf_burn_to_cash_189'] = {'inputs': ['slv_base_universe_d2_018_slv_051_fcf_burn_to_cash_189'], 'func': slv_base_universe_d3_018_slv_051_fcf_burn_to_cash_189}


def slv_base_universe_d3_019_slv_052_debt_to_equity_252(slv_base_universe_d2_019_slv_052_debt_to_equity_252):
    return _base_universe_d3(slv_base_universe_d2_019_slv_052_debt_to_equity_252, 19)
SLV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['slv_base_universe_d3_019_slv_052_debt_to_equity_252'] = {'inputs': ['slv_base_universe_d2_019_slv_052_debt_to_equity_252'], 'func': slv_base_universe_d3_019_slv_052_debt_to_equity_252}


def slv_base_universe_d3_020_slv_053_debt_to_assets_378(slv_base_universe_d2_020_slv_053_debt_to_assets_378):
    return _base_universe_d3(slv_base_universe_d2_020_slv_053_debt_to_assets_378, 20)
SLV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['slv_base_universe_d3_020_slv_053_debt_to_assets_378'] = {'inputs': ['slv_base_universe_d2_020_slv_053_debt_to_assets_378'], 'func': slv_base_universe_d3_020_slv_053_debt_to_assets_378}


def slv_base_universe_d3_021_slv_055_interest_coverage_stress_756(slv_base_universe_d2_021_slv_055_interest_coverage_stress_756):
    return _base_universe_d3(slv_base_universe_d2_021_slv_055_interest_coverage_stress_756, 21)
SLV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['slv_base_universe_d3_021_slv_055_interest_coverage_stress_756'] = {'inputs': ['slv_base_universe_d2_021_slv_055_interest_coverage_stress_756'], 'func': slv_base_universe_d3_021_slv_055_interest_coverage_stress_756}


def slv_base_universe_d3_022_slv_060_accrual_gap_252(slv_base_universe_d2_022_slv_060_accrual_gap_252):
    return _base_universe_d3(slv_base_universe_d2_022_slv_060_accrual_gap_252, 22)
SLV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['slv_base_universe_d3_022_slv_060_accrual_gap_252'] = {'inputs': ['slv_base_universe_d2_022_slv_060_accrual_gap_252'], 'func': slv_base_universe_d3_022_slv_060_accrual_gap_252}


def slv_base_universe_d3_023_slv_basefill_001(slv_base_universe_d2_023_slv_basefill_001):
    return _base_universe_d3(slv_base_universe_d2_023_slv_basefill_001, 23)
SLV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['slv_base_universe_d3_023_slv_basefill_001'] = {'inputs': ['slv_base_universe_d2_023_slv_basefill_001'], 'func': slv_base_universe_d3_023_slv_basefill_001}


def slv_base_universe_d3_024_slv_basefill_002(slv_base_universe_d2_024_slv_basefill_002):
    return _base_universe_d3(slv_base_universe_d2_024_slv_basefill_002, 24)
SLV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['slv_base_universe_d3_024_slv_basefill_002'] = {'inputs': ['slv_base_universe_d2_024_slv_basefill_002'], 'func': slv_base_universe_d3_024_slv_basefill_002}


def slv_base_universe_d3_025_slv_basefill_006(slv_base_universe_d2_025_slv_basefill_006):
    return _base_universe_d3(slv_base_universe_d2_025_slv_basefill_006, 25)
SLV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['slv_base_universe_d3_025_slv_basefill_006'] = {'inputs': ['slv_base_universe_d2_025_slv_basefill_006'], 'func': slv_base_universe_d3_025_slv_basefill_006}


def slv_base_universe_d3_026_slv_basefill_008(slv_base_universe_d2_026_slv_basefill_008):
    return _base_universe_d3(slv_base_universe_d2_026_slv_basefill_008, 26)
SLV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['slv_base_universe_d3_026_slv_basefill_008'] = {'inputs': ['slv_base_universe_d2_026_slv_basefill_008'], 'func': slv_base_universe_d3_026_slv_basefill_008}


def slv_base_universe_d3_027_slv_basefill_009(slv_base_universe_d2_027_slv_basefill_009):
    return _base_universe_d3(slv_base_universe_d2_027_slv_basefill_009, 27)
SLV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['slv_base_universe_d3_027_slv_basefill_009'] = {'inputs': ['slv_base_universe_d2_027_slv_basefill_009'], 'func': slv_base_universe_d3_027_slv_basefill_009}


def slv_base_universe_d3_028_slv_basefill_010(slv_base_universe_d2_028_slv_basefill_010):
    return _base_universe_d3(slv_base_universe_d2_028_slv_basefill_010, 28)
SLV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['slv_base_universe_d3_028_slv_basefill_010'] = {'inputs': ['slv_base_universe_d2_028_slv_basefill_010'], 'func': slv_base_universe_d3_028_slv_basefill_010}


def slv_base_universe_d3_029_slv_basefill_011(slv_base_universe_d2_029_slv_basefill_011):
    return _base_universe_d3(slv_base_universe_d2_029_slv_basefill_011, 29)
SLV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['slv_base_universe_d3_029_slv_basefill_011'] = {'inputs': ['slv_base_universe_d2_029_slv_basefill_011'], 'func': slv_base_universe_d3_029_slv_basefill_011}


def slv_base_universe_d3_030_slv_basefill_013(slv_base_universe_d2_030_slv_basefill_013):
    return _base_universe_d3(slv_base_universe_d2_030_slv_basefill_013, 30)
SLV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['slv_base_universe_d3_030_slv_basefill_013'] = {'inputs': ['slv_base_universe_d2_030_slv_basefill_013'], 'func': slv_base_universe_d3_030_slv_basefill_013}


def slv_base_universe_d3_031_slv_basefill_014(slv_base_universe_d2_031_slv_basefill_014):
    return _base_universe_d3(slv_base_universe_d2_031_slv_basefill_014, 31)
SLV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['slv_base_universe_d3_031_slv_basefill_014'] = {'inputs': ['slv_base_universe_d2_031_slv_basefill_014'], 'func': slv_base_universe_d3_031_slv_basefill_014}


def slv_base_universe_d3_032_slv_basefill_015(slv_base_universe_d2_032_slv_basefill_015):
    return _base_universe_d3(slv_base_universe_d2_032_slv_basefill_015, 32)
SLV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['slv_base_universe_d3_032_slv_basefill_015'] = {'inputs': ['slv_base_universe_d2_032_slv_basefill_015'], 'func': slv_base_universe_d3_032_slv_basefill_015}


def slv_base_universe_d3_033_slv_basefill_018(slv_base_universe_d2_033_slv_basefill_018):
    return _base_universe_d3(slv_base_universe_d2_033_slv_basefill_018, 33)
SLV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['slv_base_universe_d3_033_slv_basefill_018'] = {'inputs': ['slv_base_universe_d2_033_slv_basefill_018'], 'func': slv_base_universe_d3_033_slv_basefill_018}


def slv_base_universe_d3_034_slv_basefill_020(slv_base_universe_d2_034_slv_basefill_020):
    return _base_universe_d3(slv_base_universe_d2_034_slv_basefill_020, 34)
SLV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['slv_base_universe_d3_034_slv_basefill_020'] = {'inputs': ['slv_base_universe_d2_034_slv_basefill_020'], 'func': slv_base_universe_d3_034_slv_basefill_020}


def slv_base_universe_d3_035_slv_basefill_021(slv_base_universe_d2_035_slv_basefill_021):
    return _base_universe_d3(slv_base_universe_d2_035_slv_basefill_021, 35)
SLV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['slv_base_universe_d3_035_slv_basefill_021'] = {'inputs': ['slv_base_universe_d2_035_slv_basefill_021'], 'func': slv_base_universe_d3_035_slv_basefill_021}


def slv_base_universe_d3_036_slv_basefill_022(slv_base_universe_d2_036_slv_basefill_022):
    return _base_universe_d3(slv_base_universe_d2_036_slv_basefill_022, 36)
SLV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['slv_base_universe_d3_036_slv_basefill_022'] = {'inputs': ['slv_base_universe_d2_036_slv_basefill_022'], 'func': slv_base_universe_d3_036_slv_basefill_022}


def slv_base_universe_d3_037_slv_basefill_023(slv_base_universe_d2_037_slv_basefill_023):
    return _base_universe_d3(slv_base_universe_d2_037_slv_basefill_023, 37)
SLV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['slv_base_universe_d3_037_slv_basefill_023'] = {'inputs': ['slv_base_universe_d2_037_slv_basefill_023'], 'func': slv_base_universe_d3_037_slv_basefill_023}


def slv_base_universe_d3_038_slv_basefill_025(slv_base_universe_d2_038_slv_basefill_025):
    return _base_universe_d3(slv_base_universe_d2_038_slv_basefill_025, 38)
SLV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['slv_base_universe_d3_038_slv_basefill_025'] = {'inputs': ['slv_base_universe_d2_038_slv_basefill_025'], 'func': slv_base_universe_d3_038_slv_basefill_025}


def slv_base_universe_d3_039_slv_basefill_026(slv_base_universe_d2_039_slv_basefill_026):
    return _base_universe_d3(slv_base_universe_d2_039_slv_basefill_026, 39)
SLV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['slv_base_universe_d3_039_slv_basefill_026'] = {'inputs': ['slv_base_universe_d2_039_slv_basefill_026'], 'func': slv_base_universe_d3_039_slv_basefill_026}


def slv_base_universe_d3_040_slv_basefill_030(slv_base_universe_d2_040_slv_basefill_030):
    return _base_universe_d3(slv_base_universe_d2_040_slv_basefill_030, 40)
SLV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['slv_base_universe_d3_040_slv_basefill_030'] = {'inputs': ['slv_base_universe_d2_040_slv_basefill_030'], 'func': slv_base_universe_d3_040_slv_basefill_030}


def slv_base_universe_d3_041_slv_basefill_032(slv_base_universe_d2_041_slv_basefill_032):
    return _base_universe_d3(slv_base_universe_d2_041_slv_basefill_032, 41)
SLV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['slv_base_universe_d3_041_slv_basefill_032'] = {'inputs': ['slv_base_universe_d2_041_slv_basefill_032'], 'func': slv_base_universe_d3_041_slv_basefill_032}


def slv_base_universe_d3_042_slv_basefill_033(slv_base_universe_d2_042_slv_basefill_033):
    return _base_universe_d3(slv_base_universe_d2_042_slv_basefill_033, 42)
SLV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['slv_base_universe_d3_042_slv_basefill_033'] = {'inputs': ['slv_base_universe_d2_042_slv_basefill_033'], 'func': slv_base_universe_d3_042_slv_basefill_033}


def slv_base_universe_d3_043_slv_basefill_034(slv_base_universe_d2_043_slv_basefill_034):
    return _base_universe_d3(slv_base_universe_d2_043_slv_basefill_034, 43)
SLV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['slv_base_universe_d3_043_slv_basefill_034'] = {'inputs': ['slv_base_universe_d2_043_slv_basefill_034'], 'func': slv_base_universe_d3_043_slv_basefill_034}


def slv_base_universe_d3_044_slv_basefill_035(slv_base_universe_d2_044_slv_basefill_035):
    return _base_universe_d3(slv_base_universe_d2_044_slv_basefill_035, 44)
SLV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['slv_base_universe_d3_044_slv_basefill_035'] = {'inputs': ['slv_base_universe_d2_044_slv_basefill_035'], 'func': slv_base_universe_d3_044_slv_basefill_035}


def slv_base_universe_d3_045_slv_basefill_037(slv_base_universe_d2_045_slv_basefill_037):
    return _base_universe_d3(slv_base_universe_d2_045_slv_basefill_037, 45)
SLV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['slv_base_universe_d3_045_slv_basefill_037'] = {'inputs': ['slv_base_universe_d2_045_slv_basefill_037'], 'func': slv_base_universe_d3_045_slv_basefill_037}


def slv_base_universe_d3_046_slv_basefill_038(slv_base_universe_d2_046_slv_basefill_038):
    return _base_universe_d3(slv_base_universe_d2_046_slv_basefill_038, 46)
SLV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['slv_base_universe_d3_046_slv_basefill_038'] = {'inputs': ['slv_base_universe_d2_046_slv_basefill_038'], 'func': slv_base_universe_d3_046_slv_basefill_038}


def slv_base_universe_d3_047_slv_basefill_042(slv_base_universe_d2_047_slv_basefill_042):
    return _base_universe_d3(slv_base_universe_d2_047_slv_basefill_042, 47)
SLV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['slv_base_universe_d3_047_slv_basefill_042'] = {'inputs': ['slv_base_universe_d2_047_slv_basefill_042'], 'func': slv_base_universe_d3_047_slv_basefill_042}


def slv_base_universe_d3_048_slv_basefill_044(slv_base_universe_d2_048_slv_basefill_044):
    return _base_universe_d3(slv_base_universe_d2_048_slv_basefill_044, 48)
SLV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['slv_base_universe_d3_048_slv_basefill_044'] = {'inputs': ['slv_base_universe_d2_048_slv_basefill_044'], 'func': slv_base_universe_d3_048_slv_basefill_044}


def slv_base_universe_d3_049_slv_basefill_045(slv_base_universe_d2_049_slv_basefill_045):
    return _base_universe_d3(slv_base_universe_d2_049_slv_basefill_045, 49)
SLV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['slv_base_universe_d3_049_slv_basefill_045'] = {'inputs': ['slv_base_universe_d2_049_slv_basefill_045'], 'func': slv_base_universe_d3_049_slv_basefill_045}


def slv_base_universe_d3_050_slv_basefill_046(slv_base_universe_d2_050_slv_basefill_046):
    return _base_universe_d3(slv_base_universe_d2_050_slv_basefill_046, 50)
SLV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['slv_base_universe_d3_050_slv_basefill_046'] = {'inputs': ['slv_base_universe_d2_050_slv_basefill_046'], 'func': slv_base_universe_d3_050_slv_basefill_046}


def slv_base_universe_d3_051_slv_basefill_047(slv_base_universe_d2_051_slv_basefill_047):
    return _base_universe_d3(slv_base_universe_d2_051_slv_basefill_047, 51)
SLV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['slv_base_universe_d3_051_slv_basefill_047'] = {'inputs': ['slv_base_universe_d2_051_slv_basefill_047'], 'func': slv_base_universe_d3_051_slv_basefill_047}


def slv_base_universe_d3_052_slv_basefill_049(slv_base_universe_d2_052_slv_basefill_049):
    return _base_universe_d3(slv_base_universe_d2_052_slv_basefill_049, 52)
SLV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['slv_base_universe_d3_052_slv_basefill_049'] = {'inputs': ['slv_base_universe_d2_052_slv_basefill_049'], 'func': slv_base_universe_d3_052_slv_basefill_049}


def slv_base_universe_d3_053_slv_basefill_050(slv_base_universe_d2_053_slv_basefill_050):
    return _base_universe_d3(slv_base_universe_d2_053_slv_basefill_050, 53)
SLV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['slv_base_universe_d3_053_slv_basefill_050'] = {'inputs': ['slv_base_universe_d2_053_slv_basefill_050'], 'func': slv_base_universe_d3_053_slv_basefill_050}


def slv_base_universe_d3_054_slv_basefill_054(slv_base_universe_d2_054_slv_basefill_054):
    return _base_universe_d3(slv_base_universe_d2_054_slv_basefill_054, 54)
SLV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['slv_base_universe_d3_054_slv_basefill_054'] = {'inputs': ['slv_base_universe_d2_054_slv_basefill_054'], 'func': slv_base_universe_d3_054_slv_basefill_054}


def slv_base_universe_d3_055_slv_basefill_056(slv_base_universe_d2_055_slv_basefill_056):
    return _base_universe_d3(slv_base_universe_d2_055_slv_basefill_056, 55)
SLV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['slv_base_universe_d3_055_slv_basefill_056'] = {'inputs': ['slv_base_universe_d2_055_slv_basefill_056'], 'func': slv_base_universe_d3_055_slv_basefill_056}


def slv_base_universe_d3_056_slv_basefill_057(slv_base_universe_d2_056_slv_basefill_057):
    return _base_universe_d3(slv_base_universe_d2_056_slv_basefill_057, 56)
SLV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['slv_base_universe_d3_056_slv_basefill_057'] = {'inputs': ['slv_base_universe_d2_056_slv_basefill_057'], 'func': slv_base_universe_d3_056_slv_basefill_057}


def slv_base_universe_d3_057_slv_basefill_058(slv_base_universe_d2_057_slv_basefill_058):
    return _base_universe_d3(slv_base_universe_d2_057_slv_basefill_058, 57)
SLV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['slv_base_universe_d3_057_slv_basefill_058'] = {'inputs': ['slv_base_universe_d2_057_slv_basefill_058'], 'func': slv_base_universe_d3_057_slv_basefill_058}


def slv_base_universe_d3_058_slv_basefill_059(slv_base_universe_d2_058_slv_basefill_059):
    return _base_universe_d3(slv_base_universe_d2_058_slv_basefill_059, 58)
SLV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['slv_base_universe_d3_058_slv_basefill_059'] = {'inputs': ['slv_base_universe_d2_058_slv_basefill_059'], 'func': slv_base_universe_d3_058_slv_basefill_059}


def slv_base_universe_d3_059_slv_basefill_061(slv_base_universe_d2_059_slv_basefill_061):
    return _base_universe_d3(slv_base_universe_d2_059_slv_basefill_061, 59)
SLV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['slv_base_universe_d3_059_slv_basefill_061'] = {'inputs': ['slv_base_universe_d2_059_slv_basefill_061'], 'func': slv_base_universe_d3_059_slv_basefill_061}


def slv_base_universe_d3_060_slv_basefill_062(slv_base_universe_d2_060_slv_basefill_062):
    return _base_universe_d3(slv_base_universe_d2_060_slv_basefill_062, 60)
SLV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['slv_base_universe_d3_060_slv_basefill_062'] = {'inputs': ['slv_base_universe_d2_060_slv_basefill_062'], 'func': slv_base_universe_d3_060_slv_basefill_062}


def slv_base_universe_d3_061_slv_basefill_063(slv_base_universe_d2_061_slv_basefill_063):
    return _base_universe_d3(slv_base_universe_d2_061_slv_basefill_063, 61)
SLV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['slv_base_universe_d3_061_slv_basefill_063'] = {'inputs': ['slv_base_universe_d2_061_slv_basefill_063'], 'func': slv_base_universe_d3_061_slv_basefill_063}


def slv_base_universe_d3_062_slv_basefill_064(slv_base_universe_d2_062_slv_basefill_064):
    return _base_universe_d3(slv_base_universe_d2_062_slv_basefill_064, 62)
SLV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['slv_base_universe_d3_062_slv_basefill_064'] = {'inputs': ['slv_base_universe_d2_062_slv_basefill_064'], 'func': slv_base_universe_d3_062_slv_basefill_064}


def slv_base_universe_d3_063_slv_basefill_065(slv_base_universe_d2_063_slv_basefill_065):
    return _base_universe_d3(slv_base_universe_d2_063_slv_basefill_065, 63)
SLV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['slv_base_universe_d3_063_slv_basefill_065'] = {'inputs': ['slv_base_universe_d2_063_slv_basefill_065'], 'func': slv_base_universe_d3_063_slv_basefill_065}


def slv_base_universe_d3_064_slv_basefill_066(slv_base_universe_d2_064_slv_basefill_066):
    return _base_universe_d3(slv_base_universe_d2_064_slv_basefill_066, 64)
SLV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['slv_base_universe_d3_064_slv_basefill_066'] = {'inputs': ['slv_base_universe_d2_064_slv_basefill_066'], 'func': slv_base_universe_d3_064_slv_basefill_066}


def slv_base_universe_d3_065_slv_basefill_067(slv_base_universe_d2_065_slv_basefill_067):
    return _base_universe_d3(slv_base_universe_d2_065_slv_basefill_067, 65)
SLV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['slv_base_universe_d3_065_slv_basefill_067'] = {'inputs': ['slv_base_universe_d2_065_slv_basefill_067'], 'func': slv_base_universe_d3_065_slv_basefill_067}


def slv_base_universe_d3_066_slv_basefill_068(slv_base_universe_d2_066_slv_basefill_068):
    return _base_universe_d3(slv_base_universe_d2_066_slv_basefill_068, 66)
SLV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['slv_base_universe_d3_066_slv_basefill_068'] = {'inputs': ['slv_base_universe_d2_066_slv_basefill_068'], 'func': slv_base_universe_d3_066_slv_basefill_068}


def slv_base_universe_d3_067_slv_basefill_069(slv_base_universe_d2_067_slv_basefill_069):
    return _base_universe_d3(slv_base_universe_d2_067_slv_basefill_069, 67)
SLV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['slv_base_universe_d3_067_slv_basefill_069'] = {'inputs': ['slv_base_universe_d2_067_slv_basefill_069'], 'func': slv_base_universe_d3_067_slv_basefill_069}


def slv_base_universe_d3_068_slv_basefill_070(slv_base_universe_d2_068_slv_basefill_070):
    return _base_universe_d3(slv_base_universe_d2_068_slv_basefill_070, 68)
SLV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['slv_base_universe_d3_068_slv_basefill_070'] = {'inputs': ['slv_base_universe_d2_068_slv_basefill_070'], 'func': slv_base_universe_d3_068_slv_basefill_070}


def slv_base_universe_d3_069_slv_basefill_071(slv_base_universe_d2_069_slv_basefill_071):
    return _base_universe_d3(slv_base_universe_d2_069_slv_basefill_071, 69)
SLV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['slv_base_universe_d3_069_slv_basefill_071'] = {'inputs': ['slv_base_universe_d2_069_slv_basefill_071'], 'func': slv_base_universe_d3_069_slv_basefill_071}


def slv_base_universe_d3_070_slv_basefill_072(slv_base_universe_d2_070_slv_basefill_072):
    return _base_universe_d3(slv_base_universe_d2_070_slv_basefill_072, 70)
SLV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['slv_base_universe_d3_070_slv_basefill_072'] = {'inputs': ['slv_base_universe_d2_070_slv_basefill_072'], 'func': slv_base_universe_d3_070_slv_basefill_072}


def slv_base_universe_d3_071_slv_basefill_073(slv_base_universe_d2_071_slv_basefill_073):
    return _base_universe_d3(slv_base_universe_d2_071_slv_basefill_073, 71)
SLV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['slv_base_universe_d3_071_slv_basefill_073'] = {'inputs': ['slv_base_universe_d2_071_slv_basefill_073'], 'func': slv_base_universe_d3_071_slv_basefill_073}


def slv_base_universe_d3_072_slv_basefill_074(slv_base_universe_d2_072_slv_basefill_074):
    return _base_universe_d3(slv_base_universe_d2_072_slv_basefill_074, 72)
SLV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['slv_base_universe_d3_072_slv_basefill_074'] = {'inputs': ['slv_base_universe_d2_072_slv_basefill_074'], 'func': slv_base_universe_d3_072_slv_basefill_074}


def slv_base_universe_d3_073_slv_basefill_075(slv_base_universe_d2_073_slv_basefill_075):
    return _base_universe_d3(slv_base_universe_d2_073_slv_basefill_075, 73)
SLV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['slv_base_universe_d3_073_slv_basefill_075'] = {'inputs': ['slv_base_universe_d2_073_slv_basefill_075'], 'func': slv_base_universe_d3_073_slv_basefill_075}
