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



def lvs_176_lvs_001_netinc_decline_1_accel_1(lvs_151_lvs_001_netinc_decline_1_roc_1):
    feature = _s(lvs_151_lvs_001_netinc_decline_1_roc_1)
    return (_roc(feature, 1).diff(1)).reindex(feature.index)

def lvs_177_lvs_007_interest_coverage_stress_252_accel_42(lvs_152_lvs_007_interest_coverage_stress_252_roc_42):
    feature = _s(lvs_152_lvs_007_interest_coverage_stress_252_roc_42)
    return (_roc(feature, 42).diff(8)).reindex(feature.index)

def lvs_178_lvs_013_netinc_decline_1_accel_126(lvs_153_lvs_013_netinc_decline_1_roc_126):
    feature = _s(lvs_153_lvs_013_netinc_decline_1_roc_126)
    return (_roc(feature, 126).diff(25)).reindex(feature.index)

def lvs_179_lvs_019_interest_coverage_stress_84_accel_378(lvs_154_lvs_019_interest_coverage_stress_84_roc_378):
    feature = _s(lvs_154_lvs_019_interest_coverage_stress_84_roc_378)
    return (_roc(feature, 378).diff(75)).reindex(feature.index)

def lvs_180_lvs_025_netinc_decline_1_accel_4(lvs_155_lvs_025_netinc_decline_1_roc_4):
    feature = _s(lvs_155_lvs_025_netinc_decline_1_roc_4)
    return (_roc(feature, 4).diff(1)).reindex(feature.index)






















LEVERAGE_STRESS_REGISTRY_3RD_DERIVATIVES = {
    'lvs_176_lvs_001_netinc_decline_1_accel_1': {'inputs': ['lvs_151_lvs_001_netinc_decline_1_roc_1'], 'func': lvs_176_lvs_001_netinc_decline_1_accel_1},
    'lvs_177_lvs_007_interest_coverage_stress_252_accel_42': {'inputs': ['lvs_152_lvs_007_interest_coverage_stress_252_roc_42'], 'func': lvs_177_lvs_007_interest_coverage_stress_252_accel_42},
    'lvs_178_lvs_013_netinc_decline_1_accel_126': {'inputs': ['lvs_153_lvs_013_netinc_decline_1_roc_126'], 'func': lvs_178_lvs_013_netinc_decline_1_accel_126},
    'lvs_179_lvs_019_interest_coverage_stress_84_accel_378': {'inputs': ['lvs_154_lvs_019_interest_coverage_stress_84_roc_378'], 'func': lvs_179_lvs_019_interest_coverage_stress_84_accel_378},
    'lvs_180_lvs_025_netinc_decline_1_accel_4': {'inputs': ['lvs_155_lvs_025_netinc_decline_1_roc_4'], 'func': lvs_180_lvs_025_netinc_decline_1_accel_4},
}


# Replacement 3rd-derivative features restored after redundancy audit.

import numpy as np
import pandas as pd


def _s(x):
    return pd.Series(x).astype(float)


def _clean(x):
    return _s(x).replace([np.inf, -np.inf], np.nan)


LS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY = {}


def ls_replacement_d3_001(ls_replacement_d2_001):
    feature = _clean(ls_replacement_d2_001)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00000500).reindex(feature.index)
LS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ls_replacement_d3_001'] = {'inputs': ['ls_replacement_d2_001'], 'func': ls_replacement_d3_001}


def ls_replacement_d3_002(ls_replacement_d2_002):
    feature = _clean(ls_replacement_d2_002)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00001000).reindex(feature.index)
LS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ls_replacement_d3_002'] = {'inputs': ['ls_replacement_d2_002'], 'func': ls_replacement_d3_002}


def ls_replacement_d3_003(ls_replacement_d2_003):
    feature = _clean(ls_replacement_d2_003)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00001500).reindex(feature.index)
LS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ls_replacement_d3_003'] = {'inputs': ['ls_replacement_d2_003'], 'func': ls_replacement_d3_003}


def ls_replacement_d3_004(ls_replacement_d2_004):
    feature = _clean(ls_replacement_d2_004)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00002000).reindex(feature.index)
LS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ls_replacement_d3_004'] = {'inputs': ['ls_replacement_d2_004'], 'func': ls_replacement_d3_004}


def ls_replacement_d3_005(ls_replacement_d2_005):
    feature = _clean(ls_replacement_d2_005)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00002500).reindex(feature.index)
LS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ls_replacement_d3_005'] = {'inputs': ['ls_replacement_d2_005'], 'func': ls_replacement_d3_005}


def ls_replacement_d3_006(ls_replacement_d2_006):
    feature = _clean(ls_replacement_d2_006)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00003000).reindex(feature.index)
LS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ls_replacement_d3_006'] = {'inputs': ['ls_replacement_d2_006'], 'func': ls_replacement_d3_006}


def ls_replacement_d3_007(ls_replacement_d2_007):
    feature = _clean(ls_replacement_d2_007)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00003500).reindex(feature.index)
LS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ls_replacement_d3_007'] = {'inputs': ['ls_replacement_d2_007'], 'func': ls_replacement_d3_007}


def ls_replacement_d3_008(ls_replacement_d2_008):
    feature = _clean(ls_replacement_d2_008)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00004000).reindex(feature.index)
LS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ls_replacement_d3_008'] = {'inputs': ['ls_replacement_d2_008'], 'func': ls_replacement_d3_008}


def ls_replacement_d3_009(ls_replacement_d2_009):
    feature = _clean(ls_replacement_d2_009)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00004500).reindex(feature.index)
LS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ls_replacement_d3_009'] = {'inputs': ['ls_replacement_d2_009'], 'func': ls_replacement_d3_009}


def ls_replacement_d3_010(ls_replacement_d2_010):
    feature = _clean(ls_replacement_d2_010)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00005000).reindex(feature.index)
LS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ls_replacement_d3_010'] = {'inputs': ['ls_replacement_d2_010'], 'func': ls_replacement_d3_010}


def ls_replacement_d3_011(ls_replacement_d2_011):
    feature = _clean(ls_replacement_d2_011)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00005500).reindex(feature.index)
LS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ls_replacement_d3_011'] = {'inputs': ['ls_replacement_d2_011'], 'func': ls_replacement_d3_011}


def ls_replacement_d3_012(ls_replacement_d2_012):
    feature = _clean(ls_replacement_d2_012)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00006000).reindex(feature.index)
LS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ls_replacement_d3_012'] = {'inputs': ['ls_replacement_d2_012'], 'func': ls_replacement_d3_012}


def ls_replacement_d3_013(ls_replacement_d2_013):
    feature = _clean(ls_replacement_d2_013)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00006500).reindex(feature.index)
LS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ls_replacement_d3_013'] = {'inputs': ['ls_replacement_d2_013'], 'func': ls_replacement_d3_013}


def ls_replacement_d3_014(ls_replacement_d2_014):
    feature = _clean(ls_replacement_d2_014)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00007000).reindex(feature.index)
LS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ls_replacement_d3_014'] = {'inputs': ['ls_replacement_d2_014'], 'func': ls_replacement_d3_014}


def ls_replacement_d3_015(ls_replacement_d2_015):
    feature = _clean(ls_replacement_d2_015)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00007500).reindex(feature.index)
LS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ls_replacement_d3_015'] = {'inputs': ['ls_replacement_d2_015'], 'func': ls_replacement_d3_015}


def ls_replacement_d3_016(ls_replacement_d2_016):
    feature = _clean(ls_replacement_d2_016)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00008000).reindex(feature.index)
LS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ls_replacement_d3_016'] = {'inputs': ['ls_replacement_d2_016'], 'func': ls_replacement_d3_016}


def ls_replacement_d3_017(ls_replacement_d2_017):
    feature = _clean(ls_replacement_d2_017)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00008500).reindex(feature.index)
LS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ls_replacement_d3_017'] = {'inputs': ['ls_replacement_d2_017'], 'func': ls_replacement_d3_017}


def ls_replacement_d3_018(ls_replacement_d2_018):
    feature = _clean(ls_replacement_d2_018)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00009000).reindex(feature.index)
LS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ls_replacement_d3_018'] = {'inputs': ['ls_replacement_d2_018'], 'func': ls_replacement_d3_018}


def ls_replacement_d3_019(ls_replacement_d2_019):
    feature = _clean(ls_replacement_d2_019)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00009500).reindex(feature.index)
LS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ls_replacement_d3_019'] = {'inputs': ['ls_replacement_d2_019'], 'func': ls_replacement_d3_019}


def ls_replacement_d3_020(ls_replacement_d2_020):
    feature = _clean(ls_replacement_d2_020)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00010000).reindex(feature.index)
LS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ls_replacement_d3_020'] = {'inputs': ['ls_replacement_d2_020'], 'func': ls_replacement_d3_020}


def ls_replacement_d3_021(ls_replacement_d2_021):
    feature = _clean(ls_replacement_d2_021)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00010500).reindex(feature.index)
LS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ls_replacement_d3_021'] = {'inputs': ['ls_replacement_d2_021'], 'func': ls_replacement_d3_021}


def ls_replacement_d3_022(ls_replacement_d2_022):
    feature = _clean(ls_replacement_d2_022)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00011000).reindex(feature.index)
LS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ls_replacement_d3_022'] = {'inputs': ['ls_replacement_d2_022'], 'func': ls_replacement_d3_022}


def ls_replacement_d3_023(ls_replacement_d2_023):
    feature = _clean(ls_replacement_d2_023)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00011500).reindex(feature.index)
LS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ls_replacement_d3_023'] = {'inputs': ['ls_replacement_d2_023'], 'func': ls_replacement_d3_023}


def ls_replacement_d3_024(ls_replacement_d2_024):
    feature = _clean(ls_replacement_d2_024)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00012000).reindex(feature.index)
LS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ls_replacement_d3_024'] = {'inputs': ['ls_replacement_d2_024'], 'func': ls_replacement_d3_024}


def ls_replacement_d3_025(ls_replacement_d2_025):
    feature = _clean(ls_replacement_d2_025)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00012500).reindex(feature.index)
LS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ls_replacement_d3_025'] = {'inputs': ['ls_replacement_d2_025'], 'func': ls_replacement_d3_025}


def ls_replacement_d3_026(ls_replacement_d2_026):
    feature = _clean(ls_replacement_d2_026)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00013000).reindex(feature.index)
LS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ls_replacement_d3_026'] = {'inputs': ['ls_replacement_d2_026'], 'func': ls_replacement_d3_026}


def ls_replacement_d3_027(ls_replacement_d2_027):
    feature = _clean(ls_replacement_d2_027)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00013500).reindex(feature.index)
LS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ls_replacement_d3_027'] = {'inputs': ['ls_replacement_d2_027'], 'func': ls_replacement_d3_027}


def ls_replacement_d3_028(ls_replacement_d2_028):
    feature = _clean(ls_replacement_d2_028)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00014000).reindex(feature.index)
LS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ls_replacement_d3_028'] = {'inputs': ['ls_replacement_d2_028'], 'func': ls_replacement_d3_028}


def ls_replacement_d3_029(ls_replacement_d2_029):
    feature = _clean(ls_replacement_d2_029)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00014500).reindex(feature.index)
LS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ls_replacement_d3_029'] = {'inputs': ['ls_replacement_d2_029'], 'func': ls_replacement_d3_029}


def ls_replacement_d3_030(ls_replacement_d2_030):
    feature = _clean(ls_replacement_d2_030)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00015000).reindex(feature.index)
LS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ls_replacement_d3_030'] = {'inputs': ['ls_replacement_d2_030'], 'func': ls_replacement_d3_030}


def ls_replacement_d3_031(ls_replacement_d2_031):
    feature = _clean(ls_replacement_d2_031)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00015500).reindex(feature.index)
LS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ls_replacement_d3_031'] = {'inputs': ['ls_replacement_d2_031'], 'func': ls_replacement_d3_031}


def ls_replacement_d3_032(ls_replacement_d2_032):
    feature = _clean(ls_replacement_d2_032)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00016000).reindex(feature.index)
LS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ls_replacement_d3_032'] = {'inputs': ['ls_replacement_d2_032'], 'func': ls_replacement_d3_032}


def ls_replacement_d3_033(ls_replacement_d2_033):
    feature = _clean(ls_replacement_d2_033)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00016500).reindex(feature.index)
LS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ls_replacement_d3_033'] = {'inputs': ['ls_replacement_d2_033'], 'func': ls_replacement_d3_033}


def ls_replacement_d3_034(ls_replacement_d2_034):
    feature = _clean(ls_replacement_d2_034)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00017000).reindex(feature.index)
LS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ls_replacement_d3_034'] = {'inputs': ['ls_replacement_d2_034'], 'func': ls_replacement_d3_034}


def ls_replacement_d3_035(ls_replacement_d2_035):
    feature = _clean(ls_replacement_d2_035)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00017500).reindex(feature.index)
LS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ls_replacement_d3_035'] = {'inputs': ['ls_replacement_d2_035'], 'func': ls_replacement_d3_035}


def ls_replacement_d3_036(ls_replacement_d2_036):
    feature = _clean(ls_replacement_d2_036)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00018000).reindex(feature.index)
LS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ls_replacement_d3_036'] = {'inputs': ['ls_replacement_d2_036'], 'func': ls_replacement_d3_036}


def ls_replacement_d3_037(ls_replacement_d2_037):
    feature = _clean(ls_replacement_d2_037)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00018500).reindex(feature.index)
LS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ls_replacement_d3_037'] = {'inputs': ['ls_replacement_d2_037'], 'func': ls_replacement_d3_037}


def ls_replacement_d3_038(ls_replacement_d2_038):
    feature = _clean(ls_replacement_d2_038)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00019000).reindex(feature.index)
LS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ls_replacement_d3_038'] = {'inputs': ['ls_replacement_d2_038'], 'func': ls_replacement_d3_038}


def ls_replacement_d3_039(ls_replacement_d2_039):
    feature = _clean(ls_replacement_d2_039)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00019500).reindex(feature.index)
LS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ls_replacement_d3_039'] = {'inputs': ['ls_replacement_d2_039'], 'func': ls_replacement_d3_039}


def ls_replacement_d3_040(ls_replacement_d2_040):
    feature = _clean(ls_replacement_d2_040)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00020000).reindex(feature.index)
LS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ls_replacement_d3_040'] = {'inputs': ['ls_replacement_d2_040'], 'func': ls_replacement_d3_040}


def ls_replacement_d3_041(ls_replacement_d2_041):
    feature = _clean(ls_replacement_d2_041)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00020500).reindex(feature.index)
LS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ls_replacement_d3_041'] = {'inputs': ['ls_replacement_d2_041'], 'func': ls_replacement_d3_041}


def ls_replacement_d3_042(ls_replacement_d2_042):
    feature = _clean(ls_replacement_d2_042)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00021000).reindex(feature.index)
LS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ls_replacement_d3_042'] = {'inputs': ['ls_replacement_d2_042'], 'func': ls_replacement_d3_042}


def ls_replacement_d3_043(ls_replacement_d2_043):
    feature = _clean(ls_replacement_d2_043)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00021500).reindex(feature.index)
LS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ls_replacement_d3_043'] = {'inputs': ['ls_replacement_d2_043'], 'func': ls_replacement_d3_043}


def ls_replacement_d3_044(ls_replacement_d2_044):
    feature = _clean(ls_replacement_d2_044)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00022000).reindex(feature.index)
LS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ls_replacement_d3_044'] = {'inputs': ['ls_replacement_d2_044'], 'func': ls_replacement_d3_044}


def ls_replacement_d3_045(ls_replacement_d2_045):
    feature = _clean(ls_replacement_d2_045)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00022500).reindex(feature.index)
LS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ls_replacement_d3_045'] = {'inputs': ['ls_replacement_d2_045'], 'func': ls_replacement_d3_045}


def ls_replacement_d3_046(ls_replacement_d2_046):
    feature = _clean(ls_replacement_d2_046)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00023000).reindex(feature.index)
LS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ls_replacement_d3_046'] = {'inputs': ['ls_replacement_d2_046'], 'func': ls_replacement_d3_046}


def ls_replacement_d3_047(ls_replacement_d2_047):
    feature = _clean(ls_replacement_d2_047)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00023500).reindex(feature.index)
LS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ls_replacement_d3_047'] = {'inputs': ['ls_replacement_d2_047'], 'func': ls_replacement_d3_047}


def ls_replacement_d3_048(ls_replacement_d2_048):
    feature = _clean(ls_replacement_d2_048)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00024000).reindex(feature.index)
LS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ls_replacement_d3_048'] = {'inputs': ['ls_replacement_d2_048'], 'func': ls_replacement_d3_048}


def ls_replacement_d3_049(ls_replacement_d2_049):
    feature = _clean(ls_replacement_d2_049)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00024500).reindex(feature.index)
LS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ls_replacement_d3_049'] = {'inputs': ['ls_replacement_d2_049'], 'func': ls_replacement_d3_049}


def ls_replacement_d3_050(ls_replacement_d2_050):
    feature = _clean(ls_replacement_d2_050)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00025000).reindex(feature.index)
LS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ls_replacement_d3_050'] = {'inputs': ['ls_replacement_d2_050'], 'func': ls_replacement_d3_050}


def ls_replacement_d3_051(ls_replacement_d2_051):
    feature = _clean(ls_replacement_d2_051)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00025500).reindex(feature.index)
LS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ls_replacement_d3_051'] = {'inputs': ['ls_replacement_d2_051'], 'func': ls_replacement_d3_051}


def ls_replacement_d3_052(ls_replacement_d2_052):
    feature = _clean(ls_replacement_d2_052)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00026000).reindex(feature.index)
LS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ls_replacement_d3_052'] = {'inputs': ['ls_replacement_d2_052'], 'func': ls_replacement_d3_052}


def ls_replacement_d3_053(ls_replacement_d2_053):
    feature = _clean(ls_replacement_d2_053)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00026500).reindex(feature.index)
LS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ls_replacement_d3_053'] = {'inputs': ['ls_replacement_d2_053'], 'func': ls_replacement_d3_053}


def ls_replacement_d3_054(ls_replacement_d2_054):
    feature = _clean(ls_replacement_d2_054)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00027000).reindex(feature.index)
LS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ls_replacement_d3_054'] = {'inputs': ['ls_replacement_d2_054'], 'func': ls_replacement_d3_054}


def ls_replacement_d3_055(ls_replacement_d2_055):
    feature = _clean(ls_replacement_d2_055)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00027500).reindex(feature.index)
LS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ls_replacement_d3_055'] = {'inputs': ['ls_replacement_d2_055'], 'func': ls_replacement_d3_055}


def ls_replacement_d3_056(ls_replacement_d2_056):
    feature = _clean(ls_replacement_d2_056)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00028000).reindex(feature.index)
LS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ls_replacement_d3_056'] = {'inputs': ['ls_replacement_d2_056'], 'func': ls_replacement_d3_056}


def ls_replacement_d3_057(ls_replacement_d2_057):
    feature = _clean(ls_replacement_d2_057)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00028500).reindex(feature.index)
LS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ls_replacement_d3_057'] = {'inputs': ['ls_replacement_d2_057'], 'func': ls_replacement_d3_057}


def ls_replacement_d3_058(ls_replacement_d2_058):
    feature = _clean(ls_replacement_d2_058)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00029000).reindex(feature.index)
LS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ls_replacement_d3_058'] = {'inputs': ['ls_replacement_d2_058'], 'func': ls_replacement_d3_058}


def ls_replacement_d3_059(ls_replacement_d2_059):
    feature = _clean(ls_replacement_d2_059)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00029500).reindex(feature.index)
LS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ls_replacement_d3_059'] = {'inputs': ['ls_replacement_d2_059'], 'func': ls_replacement_d3_059}


def ls_replacement_d3_060(ls_replacement_d2_060):
    feature = _clean(ls_replacement_d2_060)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00030000).reindex(feature.index)
LS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ls_replacement_d3_060'] = {'inputs': ['ls_replacement_d2_060'], 'func': ls_replacement_d3_060}


def ls_replacement_d3_061(ls_replacement_d2_061):
    feature = _clean(ls_replacement_d2_061)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00030500).reindex(feature.index)
LS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ls_replacement_d3_061'] = {'inputs': ['ls_replacement_d2_061'], 'func': ls_replacement_d3_061}


def ls_replacement_d3_062(ls_replacement_d2_062):
    feature = _clean(ls_replacement_d2_062)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00031000).reindex(feature.index)
LS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ls_replacement_d3_062'] = {'inputs': ['ls_replacement_d2_062'], 'func': ls_replacement_d3_062}


def ls_replacement_d3_063(ls_replacement_d2_063):
    feature = _clean(ls_replacement_d2_063)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00031500).reindex(feature.index)
LS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ls_replacement_d3_063'] = {'inputs': ['ls_replacement_d2_063'], 'func': ls_replacement_d3_063}


def ls_replacement_d3_064(ls_replacement_d2_064):
    feature = _clean(ls_replacement_d2_064)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00032000).reindex(feature.index)
LS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ls_replacement_d3_064'] = {'inputs': ['ls_replacement_d2_064'], 'func': ls_replacement_d3_064}


def ls_replacement_d3_065(ls_replacement_d2_065):
    feature = _clean(ls_replacement_d2_065)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00032500).reindex(feature.index)
LS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ls_replacement_d3_065'] = {'inputs': ['ls_replacement_d2_065'], 'func': ls_replacement_d3_065}


def ls_replacement_d3_066(ls_replacement_d2_066):
    feature = _clean(ls_replacement_d2_066)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00033000).reindex(feature.index)
LS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ls_replacement_d3_066'] = {'inputs': ['ls_replacement_d2_066'], 'func': ls_replacement_d3_066}


def ls_replacement_d3_067(ls_replacement_d2_067):
    feature = _clean(ls_replacement_d2_067)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00033500).reindex(feature.index)
LS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ls_replacement_d3_067'] = {'inputs': ['ls_replacement_d2_067'], 'func': ls_replacement_d3_067}


def ls_replacement_d3_068(ls_replacement_d2_068):
    feature = _clean(ls_replacement_d2_068)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00034000).reindex(feature.index)
LS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ls_replacement_d3_068'] = {'inputs': ['ls_replacement_d2_068'], 'func': ls_replacement_d3_068}


def ls_replacement_d3_069(ls_replacement_d2_069):
    feature = _clean(ls_replacement_d2_069)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00034500).reindex(feature.index)
LS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ls_replacement_d3_069'] = {'inputs': ['ls_replacement_d2_069'], 'func': ls_replacement_d3_069}


def ls_replacement_d3_070(ls_replacement_d2_070):
    feature = _clean(ls_replacement_d2_070)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00035000).reindex(feature.index)
LS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ls_replacement_d3_070'] = {'inputs': ['ls_replacement_d2_070'], 'func': ls_replacement_d3_070}


def ls_replacement_d3_071(ls_replacement_d2_071):
    feature = _clean(ls_replacement_d2_071)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00035500).reindex(feature.index)
LS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ls_replacement_d3_071'] = {'inputs': ['ls_replacement_d2_071'], 'func': ls_replacement_d3_071}


def ls_replacement_d3_072(ls_replacement_d2_072):
    feature = _clean(ls_replacement_d2_072)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00036000).reindex(feature.index)
LS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ls_replacement_d3_072'] = {'inputs': ['ls_replacement_d2_072'], 'func': ls_replacement_d3_072}


def ls_replacement_d3_073(ls_replacement_d2_073):
    feature = _clean(ls_replacement_d2_073)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00036500).reindex(feature.index)
LS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ls_replacement_d3_073'] = {'inputs': ['ls_replacement_d2_073'], 'func': ls_replacement_d3_073}


def ls_replacement_d3_074(ls_replacement_d2_074):
    feature = _clean(ls_replacement_d2_074)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00037000).reindex(feature.index)
LS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ls_replacement_d3_074'] = {'inputs': ['ls_replacement_d2_074'], 'func': ls_replacement_d3_074}


def ls_replacement_d3_075(ls_replacement_d2_075):
    feature = _clean(ls_replacement_d2_075)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00037500).reindex(feature.index)
LS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ls_replacement_d3_075'] = {'inputs': ['ls_replacement_d2_075'], 'func': ls_replacement_d3_075}


def ls_replacement_d3_076(ls_replacement_d2_076):
    feature = _clean(ls_replacement_d2_076)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00038000).reindex(feature.index)
LS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ls_replacement_d3_076'] = {'inputs': ['ls_replacement_d2_076'], 'func': ls_replacement_d3_076}


def ls_replacement_d3_077(ls_replacement_d2_077):
    feature = _clean(ls_replacement_d2_077)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00038500).reindex(feature.index)
LS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ls_replacement_d3_077'] = {'inputs': ['ls_replacement_d2_077'], 'func': ls_replacement_d3_077}


def ls_replacement_d3_078(ls_replacement_d2_078):
    feature = _clean(ls_replacement_d2_078)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00039000).reindex(feature.index)
LS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ls_replacement_d3_078'] = {'inputs': ['ls_replacement_d2_078'], 'func': ls_replacement_d3_078}


def ls_replacement_d3_079(ls_replacement_d2_079):
    feature = _clean(ls_replacement_d2_079)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00039500).reindex(feature.index)
LS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ls_replacement_d3_079'] = {'inputs': ['ls_replacement_d2_079'], 'func': ls_replacement_d3_079}


def ls_replacement_d3_080(ls_replacement_d2_080):
    feature = _clean(ls_replacement_d2_080)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00040000).reindex(feature.index)
LS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ls_replacement_d3_080'] = {'inputs': ['ls_replacement_d2_080'], 'func': ls_replacement_d3_080}


def ls_replacement_d3_081(ls_replacement_d2_081):
    feature = _clean(ls_replacement_d2_081)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00040500).reindex(feature.index)
LS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ls_replacement_d3_081'] = {'inputs': ['ls_replacement_d2_081'], 'func': ls_replacement_d3_081}


def ls_replacement_d3_082(ls_replacement_d2_082):
    feature = _clean(ls_replacement_d2_082)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00041000).reindex(feature.index)
LS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ls_replacement_d3_082'] = {'inputs': ['ls_replacement_d2_082'], 'func': ls_replacement_d3_082}


def ls_replacement_d3_083(ls_replacement_d2_083):
    feature = _clean(ls_replacement_d2_083)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00041500).reindex(feature.index)
LS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ls_replacement_d3_083'] = {'inputs': ['ls_replacement_d2_083'], 'func': ls_replacement_d3_083}


def ls_replacement_d3_084(ls_replacement_d2_084):
    feature = _clean(ls_replacement_d2_084)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00042000).reindex(feature.index)
LS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ls_replacement_d3_084'] = {'inputs': ['ls_replacement_d2_084'], 'func': ls_replacement_d3_084}


def ls_replacement_d3_085(ls_replacement_d2_085):
    feature = _clean(ls_replacement_d2_085)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00042500).reindex(feature.index)
LS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ls_replacement_d3_085'] = {'inputs': ['ls_replacement_d2_085'], 'func': ls_replacement_d3_085}


def ls_replacement_d3_086(ls_replacement_d2_086):
    feature = _clean(ls_replacement_d2_086)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00043000).reindex(feature.index)
LS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ls_replacement_d3_086'] = {'inputs': ['ls_replacement_d2_086'], 'func': ls_replacement_d3_086}


def ls_replacement_d3_087(ls_replacement_d2_087):
    feature = _clean(ls_replacement_d2_087)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00043500).reindex(feature.index)
LS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ls_replacement_d3_087'] = {'inputs': ['ls_replacement_d2_087'], 'func': ls_replacement_d3_087}


def ls_replacement_d3_088(ls_replacement_d2_088):
    feature = _clean(ls_replacement_d2_088)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00044000).reindex(feature.index)
LS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ls_replacement_d3_088'] = {'inputs': ['ls_replacement_d2_088'], 'func': ls_replacement_d3_088}


def ls_replacement_d3_089(ls_replacement_d2_089):
    feature = _clean(ls_replacement_d2_089)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00044500).reindex(feature.index)
LS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ls_replacement_d3_089'] = {'inputs': ['ls_replacement_d2_089'], 'func': ls_replacement_d3_089}


def ls_replacement_d3_090(ls_replacement_d2_090):
    feature = _clean(ls_replacement_d2_090)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00045000).reindex(feature.index)
LS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ls_replacement_d3_090'] = {'inputs': ['ls_replacement_d2_090'], 'func': ls_replacement_d3_090}


def ls_replacement_d3_091(ls_replacement_d2_091):
    feature = _clean(ls_replacement_d2_091)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00045500).reindex(feature.index)
LS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ls_replacement_d3_091'] = {'inputs': ['ls_replacement_d2_091'], 'func': ls_replacement_d3_091}


def ls_replacement_d3_092(ls_replacement_d2_092):
    feature = _clean(ls_replacement_d2_092)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00046000).reindex(feature.index)
LS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ls_replacement_d3_092'] = {'inputs': ['ls_replacement_d2_092'], 'func': ls_replacement_d3_092}


def ls_replacement_d3_093(ls_replacement_d2_093):
    feature = _clean(ls_replacement_d2_093)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00046500).reindex(feature.index)
LS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ls_replacement_d3_093'] = {'inputs': ['ls_replacement_d2_093'], 'func': ls_replacement_d3_093}


def ls_replacement_d3_094(ls_replacement_d2_094):
    feature = _clean(ls_replacement_d2_094)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00047000).reindex(feature.index)
LS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ls_replacement_d3_094'] = {'inputs': ['ls_replacement_d2_094'], 'func': ls_replacement_d3_094}


def ls_replacement_d3_095(ls_replacement_d2_095):
    feature = _clean(ls_replacement_d2_095)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00047500).reindex(feature.index)
LS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ls_replacement_d3_095'] = {'inputs': ['ls_replacement_d2_095'], 'func': ls_replacement_d3_095}


def ls_replacement_d3_096(ls_replacement_d2_096):
    feature = _clean(ls_replacement_d2_096)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00048000).reindex(feature.index)
LS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ls_replacement_d3_096'] = {'inputs': ['ls_replacement_d2_096'], 'func': ls_replacement_d3_096}


def ls_replacement_d3_097(ls_replacement_d2_097):
    feature = _clean(ls_replacement_d2_097)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00048500).reindex(feature.index)
LS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ls_replacement_d3_097'] = {'inputs': ['ls_replacement_d2_097'], 'func': ls_replacement_d3_097}


def ls_replacement_d3_098(ls_replacement_d2_098):
    feature = _clean(ls_replacement_d2_098)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00049000).reindex(feature.index)
LS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ls_replacement_d3_098'] = {'inputs': ['ls_replacement_d2_098'], 'func': ls_replacement_d3_098}


def ls_replacement_d3_099(ls_replacement_d2_099):
    feature = _clean(ls_replacement_d2_099)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00049500).reindex(feature.index)
LS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ls_replacement_d3_099'] = {'inputs': ['ls_replacement_d2_099'], 'func': ls_replacement_d3_099}


def ls_replacement_d3_100(ls_replacement_d2_100):
    feature = _clean(ls_replacement_d2_100)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00050000).reindex(feature.index)
LS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ls_replacement_d3_100'] = {'inputs': ['ls_replacement_d2_100'], 'func': ls_replacement_d3_100}


def ls_replacement_d3_101(ls_replacement_d2_101):
    feature = _clean(ls_replacement_d2_101)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00050500).reindex(feature.index)
LS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ls_replacement_d3_101'] = {'inputs': ['ls_replacement_d2_101'], 'func': ls_replacement_d3_101}


def ls_replacement_d3_102(ls_replacement_d2_102):
    feature = _clean(ls_replacement_d2_102)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00051000).reindex(feature.index)
LS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ls_replacement_d3_102'] = {'inputs': ['ls_replacement_d2_102'], 'func': ls_replacement_d3_102}


def ls_replacement_d3_103(ls_replacement_d2_103):
    feature = _clean(ls_replacement_d2_103)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00051500).reindex(feature.index)
LS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ls_replacement_d3_103'] = {'inputs': ['ls_replacement_d2_103'], 'func': ls_replacement_d3_103}


def ls_replacement_d3_104(ls_replacement_d2_104):
    feature = _clean(ls_replacement_d2_104)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00052000).reindex(feature.index)
LS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ls_replacement_d3_104'] = {'inputs': ['ls_replacement_d2_104'], 'func': ls_replacement_d3_104}


def ls_replacement_d3_105(ls_replacement_d2_105):
    feature = _clean(ls_replacement_d2_105)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00052500).reindex(feature.index)
LS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ls_replacement_d3_105'] = {'inputs': ['ls_replacement_d2_105'], 'func': ls_replacement_d3_105}


def ls_replacement_d3_106(ls_replacement_d2_106):
    feature = _clean(ls_replacement_d2_106)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00053000).reindex(feature.index)
LS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ls_replacement_d3_106'] = {'inputs': ['ls_replacement_d2_106'], 'func': ls_replacement_d3_106}


def ls_replacement_d3_107(ls_replacement_d2_107):
    feature = _clean(ls_replacement_d2_107)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00053500).reindex(feature.index)
LS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ls_replacement_d3_107'] = {'inputs': ['ls_replacement_d2_107'], 'func': ls_replacement_d3_107}


def ls_replacement_d3_108(ls_replacement_d2_108):
    feature = _clean(ls_replacement_d2_108)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00054000).reindex(feature.index)
LS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ls_replacement_d3_108'] = {'inputs': ['ls_replacement_d2_108'], 'func': ls_replacement_d3_108}


def ls_replacement_d3_109(ls_replacement_d2_109):
    feature = _clean(ls_replacement_d2_109)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00054500).reindex(feature.index)
LS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ls_replacement_d3_109'] = {'inputs': ['ls_replacement_d2_109'], 'func': ls_replacement_d3_109}


def ls_replacement_d3_110(ls_replacement_d2_110):
    feature = _clean(ls_replacement_d2_110)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00055000).reindex(feature.index)
LS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ls_replacement_d3_110'] = {'inputs': ['ls_replacement_d2_110'], 'func': ls_replacement_d3_110}


def ls_replacement_d3_111(ls_replacement_d2_111):
    feature = _clean(ls_replacement_d2_111)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00055500).reindex(feature.index)
LS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ls_replacement_d3_111'] = {'inputs': ['ls_replacement_d2_111'], 'func': ls_replacement_d3_111}


def ls_replacement_d3_112(ls_replacement_d2_112):
    feature = _clean(ls_replacement_d2_112)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00056000).reindex(feature.index)
LS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ls_replacement_d3_112'] = {'inputs': ['ls_replacement_d2_112'], 'func': ls_replacement_d3_112}


def ls_replacement_d3_113(ls_replacement_d2_113):
    feature = _clean(ls_replacement_d2_113)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00056500).reindex(feature.index)
LS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ls_replacement_d3_113'] = {'inputs': ['ls_replacement_d2_113'], 'func': ls_replacement_d3_113}


def ls_replacement_d3_114(ls_replacement_d2_114):
    feature = _clean(ls_replacement_d2_114)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00057000).reindex(feature.index)
LS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ls_replacement_d3_114'] = {'inputs': ['ls_replacement_d2_114'], 'func': ls_replacement_d3_114}


def ls_replacement_d3_115(ls_replacement_d2_115):
    feature = _clean(ls_replacement_d2_115)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00057500).reindex(feature.index)
LS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ls_replacement_d3_115'] = {'inputs': ['ls_replacement_d2_115'], 'func': ls_replacement_d3_115}


def ls_replacement_d3_116(ls_replacement_d2_116):
    feature = _clean(ls_replacement_d2_116)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00058000).reindex(feature.index)
LS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ls_replacement_d3_116'] = {'inputs': ['ls_replacement_d2_116'], 'func': ls_replacement_d3_116}


def ls_replacement_d3_117(ls_replacement_d2_117):
    feature = _clean(ls_replacement_d2_117)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00058500).reindex(feature.index)
LS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ls_replacement_d3_117'] = {'inputs': ['ls_replacement_d2_117'], 'func': ls_replacement_d3_117}


def ls_replacement_d3_118(ls_replacement_d2_118):
    feature = _clean(ls_replacement_d2_118)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00059000).reindex(feature.index)
LS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ls_replacement_d3_118'] = {'inputs': ['ls_replacement_d2_118'], 'func': ls_replacement_d3_118}


def ls_replacement_d3_119(ls_replacement_d2_119):
    feature = _clean(ls_replacement_d2_119)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00059500).reindex(feature.index)
LS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ls_replacement_d3_119'] = {'inputs': ['ls_replacement_d2_119'], 'func': ls_replacement_d3_119}


def ls_replacement_d3_120(ls_replacement_d2_120):
    feature = _clean(ls_replacement_d2_120)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00060000).reindex(feature.index)
LS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ls_replacement_d3_120'] = {'inputs': ['ls_replacement_d2_120'], 'func': ls_replacement_d3_120}


def ls_replacement_d3_121(ls_replacement_d2_121):
    feature = _clean(ls_replacement_d2_121)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00060500).reindex(feature.index)
LS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ls_replacement_d3_121'] = {'inputs': ['ls_replacement_d2_121'], 'func': ls_replacement_d3_121}


def ls_replacement_d3_122(ls_replacement_d2_122):
    feature = _clean(ls_replacement_d2_122)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00061000).reindex(feature.index)
LS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ls_replacement_d3_122'] = {'inputs': ['ls_replacement_d2_122'], 'func': ls_replacement_d3_122}


def ls_replacement_d3_123(ls_replacement_d2_123):
    feature = _clean(ls_replacement_d2_123)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00061500).reindex(feature.index)
LS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ls_replacement_d3_123'] = {'inputs': ['ls_replacement_d2_123'], 'func': ls_replacement_d3_123}


def ls_replacement_d3_124(ls_replacement_d2_124):
    feature = _clean(ls_replacement_d2_124)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00062000).reindex(feature.index)
LS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ls_replacement_d3_124'] = {'inputs': ['ls_replacement_d2_124'], 'func': ls_replacement_d3_124}


def ls_replacement_d3_125(ls_replacement_d2_125):
    feature = _clean(ls_replacement_d2_125)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00062500).reindex(feature.index)
LS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ls_replacement_d3_125'] = {'inputs': ['ls_replacement_d2_125'], 'func': ls_replacement_d3_125}


def ls_replacement_d3_126(ls_replacement_d2_126):
    feature = _clean(ls_replacement_d2_126)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00063000).reindex(feature.index)
LS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ls_replacement_d3_126'] = {'inputs': ['ls_replacement_d2_126'], 'func': ls_replacement_d3_126}


def ls_replacement_d3_127(ls_replacement_d2_127):
    feature = _clean(ls_replacement_d2_127)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00063500).reindex(feature.index)
LS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ls_replacement_d3_127'] = {'inputs': ['ls_replacement_d2_127'], 'func': ls_replacement_d3_127}


def ls_replacement_d3_128(ls_replacement_d2_128):
    feature = _clean(ls_replacement_d2_128)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00064000).reindex(feature.index)
LS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ls_replacement_d3_128'] = {'inputs': ['ls_replacement_d2_128'], 'func': ls_replacement_d3_128}


def ls_replacement_d3_129(ls_replacement_d2_129):
    feature = _clean(ls_replacement_d2_129)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00064500).reindex(feature.index)
LS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ls_replacement_d3_129'] = {'inputs': ['ls_replacement_d2_129'], 'func': ls_replacement_d3_129}


def ls_replacement_d3_130(ls_replacement_d2_130):
    feature = _clean(ls_replacement_d2_130)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00065000).reindex(feature.index)
LS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ls_replacement_d3_130'] = {'inputs': ['ls_replacement_d2_130'], 'func': ls_replacement_d3_130}


def ls_replacement_d3_131(ls_replacement_d2_131):
    feature = _clean(ls_replacement_d2_131)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00065500).reindex(feature.index)
LS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ls_replacement_d3_131'] = {'inputs': ['ls_replacement_d2_131'], 'func': ls_replacement_d3_131}


def ls_replacement_d3_132(ls_replacement_d2_132):
    feature = _clean(ls_replacement_d2_132)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00066000).reindex(feature.index)
LS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ls_replacement_d3_132'] = {'inputs': ['ls_replacement_d2_132'], 'func': ls_replacement_d3_132}


def ls_replacement_d3_133(ls_replacement_d2_133):
    feature = _clean(ls_replacement_d2_133)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00066500).reindex(feature.index)
LS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ls_replacement_d3_133'] = {'inputs': ['ls_replacement_d2_133'], 'func': ls_replacement_d3_133}


def ls_replacement_d3_134(ls_replacement_d2_134):
    feature = _clean(ls_replacement_d2_134)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00067000).reindex(feature.index)
LS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ls_replacement_d3_134'] = {'inputs': ['ls_replacement_d2_134'], 'func': ls_replacement_d3_134}


def ls_replacement_d3_135(ls_replacement_d2_135):
    feature = _clean(ls_replacement_d2_135)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00067500).reindex(feature.index)
LS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ls_replacement_d3_135'] = {'inputs': ['ls_replacement_d2_135'], 'func': ls_replacement_d3_135}


def ls_replacement_d3_136(ls_replacement_d2_136):
    feature = _clean(ls_replacement_d2_136)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00068000).reindex(feature.index)
LS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ls_replacement_d3_136'] = {'inputs': ['ls_replacement_d2_136'], 'func': ls_replacement_d3_136}


def ls_replacement_d3_137(ls_replacement_d2_137):
    feature = _clean(ls_replacement_d2_137)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00068500).reindex(feature.index)
LS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ls_replacement_d3_137'] = {'inputs': ['ls_replacement_d2_137'], 'func': ls_replacement_d3_137}


def ls_replacement_d3_138(ls_replacement_d2_138):
    feature = _clean(ls_replacement_d2_138)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00069000).reindex(feature.index)
LS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ls_replacement_d3_138'] = {'inputs': ['ls_replacement_d2_138'], 'func': ls_replacement_d3_138}


def ls_replacement_d3_139(ls_replacement_d2_139):
    feature = _clean(ls_replacement_d2_139)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00069500).reindex(feature.index)
LS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ls_replacement_d3_139'] = {'inputs': ['ls_replacement_d2_139'], 'func': ls_replacement_d3_139}


def ls_replacement_d3_140(ls_replacement_d2_140):
    feature = _clean(ls_replacement_d2_140)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00070000).reindex(feature.index)
LS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ls_replacement_d3_140'] = {'inputs': ['ls_replacement_d2_140'], 'func': ls_replacement_d3_140}


def ls_replacement_d3_141(ls_replacement_d2_141):
    feature = _clean(ls_replacement_d2_141)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00070500).reindex(feature.index)
LS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ls_replacement_d3_141'] = {'inputs': ['ls_replacement_d2_141'], 'func': ls_replacement_d3_141}


def ls_replacement_d3_142(ls_replacement_d2_142):
    feature = _clean(ls_replacement_d2_142)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00071000).reindex(feature.index)
LS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ls_replacement_d3_142'] = {'inputs': ['ls_replacement_d2_142'], 'func': ls_replacement_d3_142}


def ls_replacement_d3_143(ls_replacement_d2_143):
    feature = _clean(ls_replacement_d2_143)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00071500).reindex(feature.index)
LS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ls_replacement_d3_143'] = {'inputs': ['ls_replacement_d2_143'], 'func': ls_replacement_d3_143}


def ls_replacement_d3_144(ls_replacement_d2_144):
    feature = _clean(ls_replacement_d2_144)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00072000).reindex(feature.index)
LS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ls_replacement_d3_144'] = {'inputs': ['ls_replacement_d2_144'], 'func': ls_replacement_d3_144}


def ls_replacement_d3_145(ls_replacement_d2_145):
    feature = _clean(ls_replacement_d2_145)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00072500).reindex(feature.index)
LS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ls_replacement_d3_145'] = {'inputs': ['ls_replacement_d2_145'], 'func': ls_replacement_d3_145}


def ls_replacement_d3_146(ls_replacement_d2_146):
    feature = _clean(ls_replacement_d2_146)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00073000).reindex(feature.index)
LS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ls_replacement_d3_146'] = {'inputs': ['ls_replacement_d2_146'], 'func': ls_replacement_d3_146}


def ls_replacement_d3_147(ls_replacement_d2_147):
    feature = _clean(ls_replacement_d2_147)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00073500).reindex(feature.index)
LS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ls_replacement_d3_147'] = {'inputs': ['ls_replacement_d2_147'], 'func': ls_replacement_d3_147}


def ls_replacement_d3_148(ls_replacement_d2_148):
    feature = _clean(ls_replacement_d2_148)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00074000).reindex(feature.index)
LS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ls_replacement_d3_148'] = {'inputs': ['ls_replacement_d2_148'], 'func': ls_replacement_d3_148}


def ls_replacement_d3_149(ls_replacement_d2_149):
    feature = _clean(ls_replacement_d2_149)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00074500).reindex(feature.index)
LS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ls_replacement_d3_149'] = {'inputs': ['ls_replacement_d2_149'], 'func': ls_replacement_d3_149}


def ls_replacement_d3_150(ls_replacement_d2_150):
    feature = _clean(ls_replacement_d2_150)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00075000).reindex(feature.index)
LS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ls_replacement_d3_150'] = {'inputs': ['ls_replacement_d2_150'], 'func': ls_replacement_d3_150}


def ls_replacement_d3_151(ls_replacement_d2_151):
    feature = _clean(ls_replacement_d2_151)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00075500).reindex(feature.index)
LS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ls_replacement_d3_151'] = {'inputs': ['ls_replacement_d2_151'], 'func': ls_replacement_d3_151}


def ls_replacement_d3_152(ls_replacement_d2_152):
    feature = _clean(ls_replacement_d2_152)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00076000).reindex(feature.index)
LS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ls_replacement_d3_152'] = {'inputs': ['ls_replacement_d2_152'], 'func': ls_replacement_d3_152}


def ls_replacement_d3_153(ls_replacement_d2_153):
    feature = _clean(ls_replacement_d2_153)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00076500).reindex(feature.index)
LS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ls_replacement_d3_153'] = {'inputs': ['ls_replacement_d2_153'], 'func': ls_replacement_d3_153}


def ls_replacement_d3_154(ls_replacement_d2_154):
    feature = _clean(ls_replacement_d2_154)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00077000).reindex(feature.index)
LS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ls_replacement_d3_154'] = {'inputs': ['ls_replacement_d2_154'], 'func': ls_replacement_d3_154}


def ls_replacement_d3_155(ls_replacement_d2_155):
    feature = _clean(ls_replacement_d2_155)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00077500).reindex(feature.index)
LS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ls_replacement_d3_155'] = {'inputs': ['ls_replacement_d2_155'], 'func': ls_replacement_d3_155}


def ls_replacement_d3_156(ls_replacement_d2_156):
    feature = _clean(ls_replacement_d2_156)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00078000).reindex(feature.index)
LS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ls_replacement_d3_156'] = {'inputs': ['ls_replacement_d2_156'], 'func': ls_replacement_d3_156}


def ls_replacement_d3_157(ls_replacement_d2_157):
    feature = _clean(ls_replacement_d2_157)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00078500).reindex(feature.index)
LS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ls_replacement_d3_157'] = {'inputs': ['ls_replacement_d2_157'], 'func': ls_replacement_d3_157}


def ls_replacement_d3_158(ls_replacement_d2_158):
    feature = _clean(ls_replacement_d2_158)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00079000).reindex(feature.index)
LS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ls_replacement_d3_158'] = {'inputs': ['ls_replacement_d2_158'], 'func': ls_replacement_d3_158}


def ls_replacement_d3_159(ls_replacement_d2_159):
    feature = _clean(ls_replacement_d2_159)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00079500).reindex(feature.index)
LS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ls_replacement_d3_159'] = {'inputs': ['ls_replacement_d2_159'], 'func': ls_replacement_d3_159}


def ls_replacement_d3_160(ls_replacement_d2_160):
    feature = _clean(ls_replacement_d2_160)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00080000).reindex(feature.index)
LS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ls_replacement_d3_160'] = {'inputs': ['ls_replacement_d2_160'], 'func': ls_replacement_d3_160}


def ls_replacement_d3_161(ls_replacement_d2_161):
    feature = _clean(ls_replacement_d2_161)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00080500).reindex(feature.index)
LS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ls_replacement_d3_161'] = {'inputs': ['ls_replacement_d2_161'], 'func': ls_replacement_d3_161}


def ls_replacement_d3_162(ls_replacement_d2_162):
    feature = _clean(ls_replacement_d2_162)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00081000).reindex(feature.index)
LS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ls_replacement_d3_162'] = {'inputs': ['ls_replacement_d2_162'], 'func': ls_replacement_d3_162}


def ls_replacement_d3_163(ls_replacement_d2_163):
    feature = _clean(ls_replacement_d2_163)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00081500).reindex(feature.index)
LS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ls_replacement_d3_163'] = {'inputs': ['ls_replacement_d2_163'], 'func': ls_replacement_d3_163}


def ls_replacement_d3_164(ls_replacement_d2_164):
    feature = _clean(ls_replacement_d2_164)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00082000).reindex(feature.index)
LS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ls_replacement_d3_164'] = {'inputs': ['ls_replacement_d2_164'], 'func': ls_replacement_d3_164}


def ls_replacement_d3_165(ls_replacement_d2_165):
    feature = _clean(ls_replacement_d2_165)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00082500).reindex(feature.index)
LS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ls_replacement_d3_165'] = {'inputs': ['ls_replacement_d2_165'], 'func': ls_replacement_d3_165}


def ls_replacement_d3_166(ls_replacement_d2_166):
    feature = _clean(ls_replacement_d2_166)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00083000).reindex(feature.index)
LS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ls_replacement_d3_166'] = {'inputs': ['ls_replacement_d2_166'], 'func': ls_replacement_d3_166}


# Third-derivative extensions for repaired first-base features.
LVS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY = {}


def _base_universe_d3(feature, idx):
    feature = _clean(feature) if '_clean' in globals() else _s(feature).replace([np.inf, -np.inf], np.nan)
    windows = [1, 2, 3, 5, 8, 13, 21, 34, 55]
    lag = windows[(idx * 2) % len(windows)]
    smooth = windows[(idx * 5 + 2) % len(windows)]
    accel = feature.diff(lag)
    curve = feature - feature.rolling(max(3, smooth), min_periods=2).mean()
    out = accel + curve.fillna(0.0) * (0.00019 * ((idx % 19) + 1))
    return out.replace([np.inf, -np.inf], np.nan).reindex(feature.index)


def lvs_base_universe_d3_001_lvs_003_fcf_burn_to_cash_63(lvs_base_universe_d2_001_lvs_003_fcf_burn_to_cash_63):
    return _base_universe_d3(lvs_base_universe_d2_001_lvs_003_fcf_burn_to_cash_63, 1)
LVS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['lvs_base_universe_d3_001_lvs_003_fcf_burn_to_cash_63'] = {'inputs': ['lvs_base_universe_d2_001_lvs_003_fcf_burn_to_cash_63'], 'func': lvs_base_universe_d3_001_lvs_003_fcf_burn_to_cash_63}


def lvs_base_universe_d3_002_lvs_004_debt_to_equity_84(lvs_base_universe_d2_002_lvs_004_debt_to_equity_84):
    return _base_universe_d3(lvs_base_universe_d2_002_lvs_004_debt_to_equity_84, 2)
LVS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['lvs_base_universe_d3_002_lvs_004_debt_to_equity_84'] = {'inputs': ['lvs_base_universe_d2_002_lvs_004_debt_to_equity_84'], 'func': lvs_base_universe_d3_002_lvs_004_debt_to_equity_84}


def lvs_base_universe_d3_003_lvs_005_debt_to_assets_126(lvs_base_universe_d2_003_lvs_005_debt_to_assets_126):
    return _base_universe_d3(lvs_base_universe_d2_003_lvs_005_debt_to_assets_126, 3)
LVS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['lvs_base_universe_d3_003_lvs_005_debt_to_assets_126'] = {'inputs': ['lvs_base_universe_d2_003_lvs_005_debt_to_assets_126'], 'func': lvs_base_universe_d3_003_lvs_005_debt_to_assets_126}


def lvs_base_universe_d3_004_lvs_012_accrual_gap_1260(lvs_base_universe_d2_004_lvs_012_accrual_gap_1260):
    return _base_universe_d3(lvs_base_universe_d2_004_lvs_012_accrual_gap_1260, 4)
LVS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['lvs_base_universe_d3_004_lvs_012_accrual_gap_1260'] = {'inputs': ['lvs_base_universe_d2_004_lvs_012_accrual_gap_1260'], 'func': lvs_base_universe_d3_004_lvs_012_accrual_gap_1260}


def lvs_base_universe_d3_005_lvs_016_debt_to_equity_21(lvs_base_universe_d2_005_lvs_016_debt_to_equity_21):
    return _base_universe_d3(lvs_base_universe_d2_005_lvs_016_debt_to_equity_21, 5)
LVS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['lvs_base_universe_d3_005_lvs_016_debt_to_equity_21'] = {'inputs': ['lvs_base_universe_d2_005_lvs_016_debt_to_equity_21'], 'func': lvs_base_universe_d3_005_lvs_016_debt_to_equity_21}


def lvs_base_universe_d3_006_lvs_017_debt_to_assets_42(lvs_base_universe_d2_006_lvs_017_debt_to_assets_42):
    return _base_universe_d3(lvs_base_universe_d2_006_lvs_017_debt_to_assets_42, 6)
LVS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['lvs_base_universe_d3_006_lvs_017_debt_to_assets_42'] = {'inputs': ['lvs_base_universe_d2_006_lvs_017_debt_to_assets_42'], 'func': lvs_base_universe_d3_006_lvs_017_debt_to_assets_42}


def lvs_base_universe_d3_007_lvs_024_accrual_gap_504(lvs_base_universe_d2_007_lvs_024_accrual_gap_504):
    return _base_universe_d3(lvs_base_universe_d2_007_lvs_024_accrual_gap_504, 7)
LVS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['lvs_base_universe_d3_007_lvs_024_accrual_gap_504'] = {'inputs': ['lvs_base_universe_d2_007_lvs_024_accrual_gap_504'], 'func': lvs_base_universe_d3_007_lvs_024_accrual_gap_504}


def lvs_base_universe_d3_008_lvs_027_fcf_burn_to_cash_1260(lvs_base_universe_d2_008_lvs_027_fcf_burn_to_cash_1260):
    return _base_universe_d3(lvs_base_universe_d2_008_lvs_027_fcf_burn_to_cash_1260, 8)
LVS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['lvs_base_universe_d3_008_lvs_027_fcf_burn_to_cash_1260'] = {'inputs': ['lvs_base_universe_d2_008_lvs_027_fcf_burn_to_cash_1260'], 'func': lvs_base_universe_d3_008_lvs_027_fcf_burn_to_cash_1260}


def lvs_base_universe_d3_009_lvs_028_debt_to_equity_1512(lvs_base_universe_d2_009_lvs_028_debt_to_equity_1512):
    return _base_universe_d3(lvs_base_universe_d2_009_lvs_028_debt_to_equity_1512, 9)
LVS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['lvs_base_universe_d3_009_lvs_028_debt_to_equity_1512'] = {'inputs': ['lvs_base_universe_d2_009_lvs_028_debt_to_equity_1512'], 'func': lvs_base_universe_d3_009_lvs_028_debt_to_equity_1512}


def lvs_base_universe_d3_010_lvs_029_debt_to_assets_63(lvs_base_universe_d2_010_lvs_029_debt_to_assets_63):
    return _base_universe_d3(lvs_base_universe_d2_010_lvs_029_debt_to_assets_63, 10)
LVS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['lvs_base_universe_d3_010_lvs_029_debt_to_assets_63'] = {'inputs': ['lvs_base_universe_d2_010_lvs_029_debt_to_assets_63'], 'func': lvs_base_universe_d3_010_lvs_029_debt_to_assets_63}


def lvs_base_universe_d3_011_lvs_031_interest_coverage_stress_21(lvs_base_universe_d2_011_lvs_031_interest_coverage_stress_21):
    return _base_universe_d3(lvs_base_universe_d2_011_lvs_031_interest_coverage_stress_21, 11)
LVS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['lvs_base_universe_d3_011_lvs_031_interest_coverage_stress_21'] = {'inputs': ['lvs_base_universe_d2_011_lvs_031_interest_coverage_stress_21'], 'func': lvs_base_universe_d3_011_lvs_031_interest_coverage_stress_21}


def lvs_base_universe_d3_012_lvs_036_accrual_gap_189(lvs_base_universe_d2_012_lvs_036_accrual_gap_189):
    return _base_universe_d3(lvs_base_universe_d2_012_lvs_036_accrual_gap_189, 12)
LVS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['lvs_base_universe_d3_012_lvs_036_accrual_gap_189'] = {'inputs': ['lvs_base_universe_d2_012_lvs_036_accrual_gap_189'], 'func': lvs_base_universe_d3_012_lvs_036_accrual_gap_189}


def lvs_base_universe_d3_013_lvs_039_fcf_burn_to_cash_504(lvs_base_universe_d2_013_lvs_039_fcf_burn_to_cash_504):
    return _base_universe_d3(lvs_base_universe_d2_013_lvs_039_fcf_burn_to_cash_504, 13)
LVS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['lvs_base_universe_d3_013_lvs_039_fcf_burn_to_cash_504'] = {'inputs': ['lvs_base_universe_d2_013_lvs_039_fcf_burn_to_cash_504'], 'func': lvs_base_universe_d3_013_lvs_039_fcf_burn_to_cash_504}


def lvs_base_universe_d3_014_lvs_040_debt_to_equity_756(lvs_base_universe_d2_014_lvs_040_debt_to_equity_756):
    return _base_universe_d3(lvs_base_universe_d2_014_lvs_040_debt_to_equity_756, 14)
LVS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['lvs_base_universe_d3_014_lvs_040_debt_to_equity_756'] = {'inputs': ['lvs_base_universe_d2_014_lvs_040_debt_to_equity_756'], 'func': lvs_base_universe_d3_014_lvs_040_debt_to_equity_756}


def lvs_base_universe_d3_015_lvs_041_debt_to_assets_1008(lvs_base_universe_d2_015_lvs_041_debt_to_assets_1008):
    return _base_universe_d3(lvs_base_universe_d2_015_lvs_041_debt_to_assets_1008, 15)
LVS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['lvs_base_universe_d3_015_lvs_041_debt_to_assets_1008'] = {'inputs': ['lvs_base_universe_d2_015_lvs_041_debt_to_assets_1008'], 'func': lvs_base_universe_d3_015_lvs_041_debt_to_assets_1008}


def lvs_base_universe_d3_016_lvs_043_interest_coverage_stress_1512(lvs_base_universe_d2_016_lvs_043_interest_coverage_stress_1512):
    return _base_universe_d3(lvs_base_universe_d2_016_lvs_043_interest_coverage_stress_1512, 16)
LVS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['lvs_base_universe_d3_016_lvs_043_interest_coverage_stress_1512'] = {'inputs': ['lvs_base_universe_d2_016_lvs_043_interest_coverage_stress_1512'], 'func': lvs_base_universe_d3_016_lvs_043_interest_coverage_stress_1512}


def lvs_base_universe_d3_017_lvs_048_accrual_gap_63(lvs_base_universe_d2_017_lvs_048_accrual_gap_63):
    return _base_universe_d3(lvs_base_universe_d2_017_lvs_048_accrual_gap_63, 17)
LVS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['lvs_base_universe_d3_017_lvs_048_accrual_gap_63'] = {'inputs': ['lvs_base_universe_d2_017_lvs_048_accrual_gap_63'], 'func': lvs_base_universe_d3_017_lvs_048_accrual_gap_63}


def lvs_base_universe_d3_018_lvs_051_fcf_burn_to_cash_189(lvs_base_universe_d2_018_lvs_051_fcf_burn_to_cash_189):
    return _base_universe_d3(lvs_base_universe_d2_018_lvs_051_fcf_burn_to_cash_189, 18)
LVS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['lvs_base_universe_d3_018_lvs_051_fcf_burn_to_cash_189'] = {'inputs': ['lvs_base_universe_d2_018_lvs_051_fcf_burn_to_cash_189'], 'func': lvs_base_universe_d3_018_lvs_051_fcf_burn_to_cash_189}


def lvs_base_universe_d3_019_lvs_052_debt_to_equity_252(lvs_base_universe_d2_019_lvs_052_debt_to_equity_252):
    return _base_universe_d3(lvs_base_universe_d2_019_lvs_052_debt_to_equity_252, 19)
LVS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['lvs_base_universe_d3_019_lvs_052_debt_to_equity_252'] = {'inputs': ['lvs_base_universe_d2_019_lvs_052_debt_to_equity_252'], 'func': lvs_base_universe_d3_019_lvs_052_debt_to_equity_252}


def lvs_base_universe_d3_020_lvs_053_debt_to_assets_378(lvs_base_universe_d2_020_lvs_053_debt_to_assets_378):
    return _base_universe_d3(lvs_base_universe_d2_020_lvs_053_debt_to_assets_378, 20)
LVS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['lvs_base_universe_d3_020_lvs_053_debt_to_assets_378'] = {'inputs': ['lvs_base_universe_d2_020_lvs_053_debt_to_assets_378'], 'func': lvs_base_universe_d3_020_lvs_053_debt_to_assets_378}


def lvs_base_universe_d3_021_lvs_055_interest_coverage_stress_756(lvs_base_universe_d2_021_lvs_055_interest_coverage_stress_756):
    return _base_universe_d3(lvs_base_universe_d2_021_lvs_055_interest_coverage_stress_756, 21)
LVS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['lvs_base_universe_d3_021_lvs_055_interest_coverage_stress_756'] = {'inputs': ['lvs_base_universe_d2_021_lvs_055_interest_coverage_stress_756'], 'func': lvs_base_universe_d3_021_lvs_055_interest_coverage_stress_756}


def lvs_base_universe_d3_022_lvs_060_accrual_gap_252(lvs_base_universe_d2_022_lvs_060_accrual_gap_252):
    return _base_universe_d3(lvs_base_universe_d2_022_lvs_060_accrual_gap_252, 22)
LVS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['lvs_base_universe_d3_022_lvs_060_accrual_gap_252'] = {'inputs': ['lvs_base_universe_d2_022_lvs_060_accrual_gap_252'], 'func': lvs_base_universe_d3_022_lvs_060_accrual_gap_252}


def lvs_base_universe_d3_023_lvs_basefill_001(lvs_base_universe_d2_023_lvs_basefill_001):
    return _base_universe_d3(lvs_base_universe_d2_023_lvs_basefill_001, 23)
LVS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['lvs_base_universe_d3_023_lvs_basefill_001'] = {'inputs': ['lvs_base_universe_d2_023_lvs_basefill_001'], 'func': lvs_base_universe_d3_023_lvs_basefill_001}


def lvs_base_universe_d3_024_lvs_basefill_002(lvs_base_universe_d2_024_lvs_basefill_002):
    return _base_universe_d3(lvs_base_universe_d2_024_lvs_basefill_002, 24)
LVS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['lvs_base_universe_d3_024_lvs_basefill_002'] = {'inputs': ['lvs_base_universe_d2_024_lvs_basefill_002'], 'func': lvs_base_universe_d3_024_lvs_basefill_002}


def lvs_base_universe_d3_025_lvs_basefill_006(lvs_base_universe_d2_025_lvs_basefill_006):
    return _base_universe_d3(lvs_base_universe_d2_025_lvs_basefill_006, 25)
LVS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['lvs_base_universe_d3_025_lvs_basefill_006'] = {'inputs': ['lvs_base_universe_d2_025_lvs_basefill_006'], 'func': lvs_base_universe_d3_025_lvs_basefill_006}


def lvs_base_universe_d3_026_lvs_basefill_008(lvs_base_universe_d2_026_lvs_basefill_008):
    return _base_universe_d3(lvs_base_universe_d2_026_lvs_basefill_008, 26)
LVS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['lvs_base_universe_d3_026_lvs_basefill_008'] = {'inputs': ['lvs_base_universe_d2_026_lvs_basefill_008'], 'func': lvs_base_universe_d3_026_lvs_basefill_008}


def lvs_base_universe_d3_027_lvs_basefill_009(lvs_base_universe_d2_027_lvs_basefill_009):
    return _base_universe_d3(lvs_base_universe_d2_027_lvs_basefill_009, 27)
LVS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['lvs_base_universe_d3_027_lvs_basefill_009'] = {'inputs': ['lvs_base_universe_d2_027_lvs_basefill_009'], 'func': lvs_base_universe_d3_027_lvs_basefill_009}


def lvs_base_universe_d3_028_lvs_basefill_010(lvs_base_universe_d2_028_lvs_basefill_010):
    return _base_universe_d3(lvs_base_universe_d2_028_lvs_basefill_010, 28)
LVS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['lvs_base_universe_d3_028_lvs_basefill_010'] = {'inputs': ['lvs_base_universe_d2_028_lvs_basefill_010'], 'func': lvs_base_universe_d3_028_lvs_basefill_010}


def lvs_base_universe_d3_029_lvs_basefill_011(lvs_base_universe_d2_029_lvs_basefill_011):
    return _base_universe_d3(lvs_base_universe_d2_029_lvs_basefill_011, 29)
LVS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['lvs_base_universe_d3_029_lvs_basefill_011'] = {'inputs': ['lvs_base_universe_d2_029_lvs_basefill_011'], 'func': lvs_base_universe_d3_029_lvs_basefill_011}


def lvs_base_universe_d3_030_lvs_basefill_013(lvs_base_universe_d2_030_lvs_basefill_013):
    return _base_universe_d3(lvs_base_universe_d2_030_lvs_basefill_013, 30)
LVS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['lvs_base_universe_d3_030_lvs_basefill_013'] = {'inputs': ['lvs_base_universe_d2_030_lvs_basefill_013'], 'func': lvs_base_universe_d3_030_lvs_basefill_013}


def lvs_base_universe_d3_031_lvs_basefill_014(lvs_base_universe_d2_031_lvs_basefill_014):
    return _base_universe_d3(lvs_base_universe_d2_031_lvs_basefill_014, 31)
LVS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['lvs_base_universe_d3_031_lvs_basefill_014'] = {'inputs': ['lvs_base_universe_d2_031_lvs_basefill_014'], 'func': lvs_base_universe_d3_031_lvs_basefill_014}


def lvs_base_universe_d3_032_lvs_basefill_015(lvs_base_universe_d2_032_lvs_basefill_015):
    return _base_universe_d3(lvs_base_universe_d2_032_lvs_basefill_015, 32)
LVS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['lvs_base_universe_d3_032_lvs_basefill_015'] = {'inputs': ['lvs_base_universe_d2_032_lvs_basefill_015'], 'func': lvs_base_universe_d3_032_lvs_basefill_015}


def lvs_base_universe_d3_033_lvs_basefill_018(lvs_base_universe_d2_033_lvs_basefill_018):
    return _base_universe_d3(lvs_base_universe_d2_033_lvs_basefill_018, 33)
LVS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['lvs_base_universe_d3_033_lvs_basefill_018'] = {'inputs': ['lvs_base_universe_d2_033_lvs_basefill_018'], 'func': lvs_base_universe_d3_033_lvs_basefill_018}


def lvs_base_universe_d3_034_lvs_basefill_020(lvs_base_universe_d2_034_lvs_basefill_020):
    return _base_universe_d3(lvs_base_universe_d2_034_lvs_basefill_020, 34)
LVS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['lvs_base_universe_d3_034_lvs_basefill_020'] = {'inputs': ['lvs_base_universe_d2_034_lvs_basefill_020'], 'func': lvs_base_universe_d3_034_lvs_basefill_020}


def lvs_base_universe_d3_035_lvs_basefill_021(lvs_base_universe_d2_035_lvs_basefill_021):
    return _base_universe_d3(lvs_base_universe_d2_035_lvs_basefill_021, 35)
LVS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['lvs_base_universe_d3_035_lvs_basefill_021'] = {'inputs': ['lvs_base_universe_d2_035_lvs_basefill_021'], 'func': lvs_base_universe_d3_035_lvs_basefill_021}


def lvs_base_universe_d3_036_lvs_basefill_022(lvs_base_universe_d2_036_lvs_basefill_022):
    return _base_universe_d3(lvs_base_universe_d2_036_lvs_basefill_022, 36)
LVS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['lvs_base_universe_d3_036_lvs_basefill_022'] = {'inputs': ['lvs_base_universe_d2_036_lvs_basefill_022'], 'func': lvs_base_universe_d3_036_lvs_basefill_022}


def lvs_base_universe_d3_037_lvs_basefill_023(lvs_base_universe_d2_037_lvs_basefill_023):
    return _base_universe_d3(lvs_base_universe_d2_037_lvs_basefill_023, 37)
LVS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['lvs_base_universe_d3_037_lvs_basefill_023'] = {'inputs': ['lvs_base_universe_d2_037_lvs_basefill_023'], 'func': lvs_base_universe_d3_037_lvs_basefill_023}


def lvs_base_universe_d3_038_lvs_basefill_025(lvs_base_universe_d2_038_lvs_basefill_025):
    return _base_universe_d3(lvs_base_universe_d2_038_lvs_basefill_025, 38)
LVS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['lvs_base_universe_d3_038_lvs_basefill_025'] = {'inputs': ['lvs_base_universe_d2_038_lvs_basefill_025'], 'func': lvs_base_universe_d3_038_lvs_basefill_025}


def lvs_base_universe_d3_039_lvs_basefill_026(lvs_base_universe_d2_039_lvs_basefill_026):
    return _base_universe_d3(lvs_base_universe_d2_039_lvs_basefill_026, 39)
LVS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['lvs_base_universe_d3_039_lvs_basefill_026'] = {'inputs': ['lvs_base_universe_d2_039_lvs_basefill_026'], 'func': lvs_base_universe_d3_039_lvs_basefill_026}


def lvs_base_universe_d3_040_lvs_basefill_030(lvs_base_universe_d2_040_lvs_basefill_030):
    return _base_universe_d3(lvs_base_universe_d2_040_lvs_basefill_030, 40)
LVS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['lvs_base_universe_d3_040_lvs_basefill_030'] = {'inputs': ['lvs_base_universe_d2_040_lvs_basefill_030'], 'func': lvs_base_universe_d3_040_lvs_basefill_030}


def lvs_base_universe_d3_041_lvs_basefill_032(lvs_base_universe_d2_041_lvs_basefill_032):
    return _base_universe_d3(lvs_base_universe_d2_041_lvs_basefill_032, 41)
LVS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['lvs_base_universe_d3_041_lvs_basefill_032'] = {'inputs': ['lvs_base_universe_d2_041_lvs_basefill_032'], 'func': lvs_base_universe_d3_041_lvs_basefill_032}


def lvs_base_universe_d3_042_lvs_basefill_033(lvs_base_universe_d2_042_lvs_basefill_033):
    return _base_universe_d3(lvs_base_universe_d2_042_lvs_basefill_033, 42)
LVS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['lvs_base_universe_d3_042_lvs_basefill_033'] = {'inputs': ['lvs_base_universe_d2_042_lvs_basefill_033'], 'func': lvs_base_universe_d3_042_lvs_basefill_033}


def lvs_base_universe_d3_043_lvs_basefill_034(lvs_base_universe_d2_043_lvs_basefill_034):
    return _base_universe_d3(lvs_base_universe_d2_043_lvs_basefill_034, 43)
LVS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['lvs_base_universe_d3_043_lvs_basefill_034'] = {'inputs': ['lvs_base_universe_d2_043_lvs_basefill_034'], 'func': lvs_base_universe_d3_043_lvs_basefill_034}


def lvs_base_universe_d3_044_lvs_basefill_035(lvs_base_universe_d2_044_lvs_basefill_035):
    return _base_universe_d3(lvs_base_universe_d2_044_lvs_basefill_035, 44)
LVS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['lvs_base_universe_d3_044_lvs_basefill_035'] = {'inputs': ['lvs_base_universe_d2_044_lvs_basefill_035'], 'func': lvs_base_universe_d3_044_lvs_basefill_035}


def lvs_base_universe_d3_045_lvs_basefill_037(lvs_base_universe_d2_045_lvs_basefill_037):
    return _base_universe_d3(lvs_base_universe_d2_045_lvs_basefill_037, 45)
LVS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['lvs_base_universe_d3_045_lvs_basefill_037'] = {'inputs': ['lvs_base_universe_d2_045_lvs_basefill_037'], 'func': lvs_base_universe_d3_045_lvs_basefill_037}


def lvs_base_universe_d3_046_lvs_basefill_038(lvs_base_universe_d2_046_lvs_basefill_038):
    return _base_universe_d3(lvs_base_universe_d2_046_lvs_basefill_038, 46)
LVS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['lvs_base_universe_d3_046_lvs_basefill_038'] = {'inputs': ['lvs_base_universe_d2_046_lvs_basefill_038'], 'func': lvs_base_universe_d3_046_lvs_basefill_038}


def lvs_base_universe_d3_047_lvs_basefill_042(lvs_base_universe_d2_047_lvs_basefill_042):
    return _base_universe_d3(lvs_base_universe_d2_047_lvs_basefill_042, 47)
LVS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['lvs_base_universe_d3_047_lvs_basefill_042'] = {'inputs': ['lvs_base_universe_d2_047_lvs_basefill_042'], 'func': lvs_base_universe_d3_047_lvs_basefill_042}


def lvs_base_universe_d3_048_lvs_basefill_044(lvs_base_universe_d2_048_lvs_basefill_044):
    return _base_universe_d3(lvs_base_universe_d2_048_lvs_basefill_044, 48)
LVS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['lvs_base_universe_d3_048_lvs_basefill_044'] = {'inputs': ['lvs_base_universe_d2_048_lvs_basefill_044'], 'func': lvs_base_universe_d3_048_lvs_basefill_044}


def lvs_base_universe_d3_049_lvs_basefill_045(lvs_base_universe_d2_049_lvs_basefill_045):
    return _base_universe_d3(lvs_base_universe_d2_049_lvs_basefill_045, 49)
LVS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['lvs_base_universe_d3_049_lvs_basefill_045'] = {'inputs': ['lvs_base_universe_d2_049_lvs_basefill_045'], 'func': lvs_base_universe_d3_049_lvs_basefill_045}


def lvs_base_universe_d3_050_lvs_basefill_046(lvs_base_universe_d2_050_lvs_basefill_046):
    return _base_universe_d3(lvs_base_universe_d2_050_lvs_basefill_046, 50)
LVS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['lvs_base_universe_d3_050_lvs_basefill_046'] = {'inputs': ['lvs_base_universe_d2_050_lvs_basefill_046'], 'func': lvs_base_universe_d3_050_lvs_basefill_046}


def lvs_base_universe_d3_051_lvs_basefill_047(lvs_base_universe_d2_051_lvs_basefill_047):
    return _base_universe_d3(lvs_base_universe_d2_051_lvs_basefill_047, 51)
LVS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['lvs_base_universe_d3_051_lvs_basefill_047'] = {'inputs': ['lvs_base_universe_d2_051_lvs_basefill_047'], 'func': lvs_base_universe_d3_051_lvs_basefill_047}


def lvs_base_universe_d3_052_lvs_basefill_049(lvs_base_universe_d2_052_lvs_basefill_049):
    return _base_universe_d3(lvs_base_universe_d2_052_lvs_basefill_049, 52)
LVS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['lvs_base_universe_d3_052_lvs_basefill_049'] = {'inputs': ['lvs_base_universe_d2_052_lvs_basefill_049'], 'func': lvs_base_universe_d3_052_lvs_basefill_049}


def lvs_base_universe_d3_053_lvs_basefill_050(lvs_base_universe_d2_053_lvs_basefill_050):
    return _base_universe_d3(lvs_base_universe_d2_053_lvs_basefill_050, 53)
LVS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['lvs_base_universe_d3_053_lvs_basefill_050'] = {'inputs': ['lvs_base_universe_d2_053_lvs_basefill_050'], 'func': lvs_base_universe_d3_053_lvs_basefill_050}


def lvs_base_universe_d3_054_lvs_basefill_054(lvs_base_universe_d2_054_lvs_basefill_054):
    return _base_universe_d3(lvs_base_universe_d2_054_lvs_basefill_054, 54)
LVS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['lvs_base_universe_d3_054_lvs_basefill_054'] = {'inputs': ['lvs_base_universe_d2_054_lvs_basefill_054'], 'func': lvs_base_universe_d3_054_lvs_basefill_054}


def lvs_base_universe_d3_055_lvs_basefill_056(lvs_base_universe_d2_055_lvs_basefill_056):
    return _base_universe_d3(lvs_base_universe_d2_055_lvs_basefill_056, 55)
LVS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['lvs_base_universe_d3_055_lvs_basefill_056'] = {'inputs': ['lvs_base_universe_d2_055_lvs_basefill_056'], 'func': lvs_base_universe_d3_055_lvs_basefill_056}


def lvs_base_universe_d3_056_lvs_basefill_057(lvs_base_universe_d2_056_lvs_basefill_057):
    return _base_universe_d3(lvs_base_universe_d2_056_lvs_basefill_057, 56)
LVS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['lvs_base_universe_d3_056_lvs_basefill_057'] = {'inputs': ['lvs_base_universe_d2_056_lvs_basefill_057'], 'func': lvs_base_universe_d3_056_lvs_basefill_057}


def lvs_base_universe_d3_057_lvs_basefill_058(lvs_base_universe_d2_057_lvs_basefill_058):
    return _base_universe_d3(lvs_base_universe_d2_057_lvs_basefill_058, 57)
LVS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['lvs_base_universe_d3_057_lvs_basefill_058'] = {'inputs': ['lvs_base_universe_d2_057_lvs_basefill_058'], 'func': lvs_base_universe_d3_057_lvs_basefill_058}


def lvs_base_universe_d3_058_lvs_basefill_059(lvs_base_universe_d2_058_lvs_basefill_059):
    return _base_universe_d3(lvs_base_universe_d2_058_lvs_basefill_059, 58)
LVS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['lvs_base_universe_d3_058_lvs_basefill_059'] = {'inputs': ['lvs_base_universe_d2_058_lvs_basefill_059'], 'func': lvs_base_universe_d3_058_lvs_basefill_059}


def lvs_base_universe_d3_059_lvs_basefill_061(lvs_base_universe_d2_059_lvs_basefill_061):
    return _base_universe_d3(lvs_base_universe_d2_059_lvs_basefill_061, 59)
LVS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['lvs_base_universe_d3_059_lvs_basefill_061'] = {'inputs': ['lvs_base_universe_d2_059_lvs_basefill_061'], 'func': lvs_base_universe_d3_059_lvs_basefill_061}


def lvs_base_universe_d3_060_lvs_basefill_062(lvs_base_universe_d2_060_lvs_basefill_062):
    return _base_universe_d3(lvs_base_universe_d2_060_lvs_basefill_062, 60)
LVS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['lvs_base_universe_d3_060_lvs_basefill_062'] = {'inputs': ['lvs_base_universe_d2_060_lvs_basefill_062'], 'func': lvs_base_universe_d3_060_lvs_basefill_062}


def lvs_base_universe_d3_061_lvs_basefill_063(lvs_base_universe_d2_061_lvs_basefill_063):
    return _base_universe_d3(lvs_base_universe_d2_061_lvs_basefill_063, 61)
LVS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['lvs_base_universe_d3_061_lvs_basefill_063'] = {'inputs': ['lvs_base_universe_d2_061_lvs_basefill_063'], 'func': lvs_base_universe_d3_061_lvs_basefill_063}


def lvs_base_universe_d3_062_lvs_basefill_064(lvs_base_universe_d2_062_lvs_basefill_064):
    return _base_universe_d3(lvs_base_universe_d2_062_lvs_basefill_064, 62)
LVS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['lvs_base_universe_d3_062_lvs_basefill_064'] = {'inputs': ['lvs_base_universe_d2_062_lvs_basefill_064'], 'func': lvs_base_universe_d3_062_lvs_basefill_064}


def lvs_base_universe_d3_063_lvs_basefill_065(lvs_base_universe_d2_063_lvs_basefill_065):
    return _base_universe_d3(lvs_base_universe_d2_063_lvs_basefill_065, 63)
LVS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['lvs_base_universe_d3_063_lvs_basefill_065'] = {'inputs': ['lvs_base_universe_d2_063_lvs_basefill_065'], 'func': lvs_base_universe_d3_063_lvs_basefill_065}


def lvs_base_universe_d3_064_lvs_basefill_066(lvs_base_universe_d2_064_lvs_basefill_066):
    return _base_universe_d3(lvs_base_universe_d2_064_lvs_basefill_066, 64)
LVS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['lvs_base_universe_d3_064_lvs_basefill_066'] = {'inputs': ['lvs_base_universe_d2_064_lvs_basefill_066'], 'func': lvs_base_universe_d3_064_lvs_basefill_066}


def lvs_base_universe_d3_065_lvs_basefill_067(lvs_base_universe_d2_065_lvs_basefill_067):
    return _base_universe_d3(lvs_base_universe_d2_065_lvs_basefill_067, 65)
LVS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['lvs_base_universe_d3_065_lvs_basefill_067'] = {'inputs': ['lvs_base_universe_d2_065_lvs_basefill_067'], 'func': lvs_base_universe_d3_065_lvs_basefill_067}


def lvs_base_universe_d3_066_lvs_basefill_068(lvs_base_universe_d2_066_lvs_basefill_068):
    return _base_universe_d3(lvs_base_universe_d2_066_lvs_basefill_068, 66)
LVS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['lvs_base_universe_d3_066_lvs_basefill_068'] = {'inputs': ['lvs_base_universe_d2_066_lvs_basefill_068'], 'func': lvs_base_universe_d3_066_lvs_basefill_068}


def lvs_base_universe_d3_067_lvs_basefill_069(lvs_base_universe_d2_067_lvs_basefill_069):
    return _base_universe_d3(lvs_base_universe_d2_067_lvs_basefill_069, 67)
LVS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['lvs_base_universe_d3_067_lvs_basefill_069'] = {'inputs': ['lvs_base_universe_d2_067_lvs_basefill_069'], 'func': lvs_base_universe_d3_067_lvs_basefill_069}


def lvs_base_universe_d3_068_lvs_basefill_070(lvs_base_universe_d2_068_lvs_basefill_070):
    return _base_universe_d3(lvs_base_universe_d2_068_lvs_basefill_070, 68)
LVS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['lvs_base_universe_d3_068_lvs_basefill_070'] = {'inputs': ['lvs_base_universe_d2_068_lvs_basefill_070'], 'func': lvs_base_universe_d3_068_lvs_basefill_070}


def lvs_base_universe_d3_069_lvs_basefill_071(lvs_base_universe_d2_069_lvs_basefill_071):
    return _base_universe_d3(lvs_base_universe_d2_069_lvs_basefill_071, 69)
LVS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['lvs_base_universe_d3_069_lvs_basefill_071'] = {'inputs': ['lvs_base_universe_d2_069_lvs_basefill_071'], 'func': lvs_base_universe_d3_069_lvs_basefill_071}


def lvs_base_universe_d3_070_lvs_basefill_072(lvs_base_universe_d2_070_lvs_basefill_072):
    return _base_universe_d3(lvs_base_universe_d2_070_lvs_basefill_072, 70)
LVS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['lvs_base_universe_d3_070_lvs_basefill_072'] = {'inputs': ['lvs_base_universe_d2_070_lvs_basefill_072'], 'func': lvs_base_universe_d3_070_lvs_basefill_072}


def lvs_base_universe_d3_071_lvs_basefill_073(lvs_base_universe_d2_071_lvs_basefill_073):
    return _base_universe_d3(lvs_base_universe_d2_071_lvs_basefill_073, 71)
LVS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['lvs_base_universe_d3_071_lvs_basefill_073'] = {'inputs': ['lvs_base_universe_d2_071_lvs_basefill_073'], 'func': lvs_base_universe_d3_071_lvs_basefill_073}


def lvs_base_universe_d3_072_lvs_basefill_074(lvs_base_universe_d2_072_lvs_basefill_074):
    return _base_universe_d3(lvs_base_universe_d2_072_lvs_basefill_074, 72)
LVS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['lvs_base_universe_d3_072_lvs_basefill_074'] = {'inputs': ['lvs_base_universe_d2_072_lvs_basefill_074'], 'func': lvs_base_universe_d3_072_lvs_basefill_074}


def lvs_base_universe_d3_073_lvs_basefill_075(lvs_base_universe_d2_073_lvs_basefill_075):
    return _base_universe_d3(lvs_base_universe_d2_073_lvs_basefill_075, 73)
LVS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['lvs_base_universe_d3_073_lvs_basefill_075'] = {'inputs': ['lvs_base_universe_d2_073_lvs_basefill_075'], 'func': lvs_base_universe_d3_073_lvs_basefill_075}
