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



def slv_151_slv_001_netinc_decline_1_roc_1(netinc):
    feature = _s(netinc)
    return (_roc(feature, 1)).reindex(feature.index)

def slv_152_slv_007_interest_coverage_stress_252_roc_42(slv_007_interest_coverage_stress_252):
    feature = _s(slv_007_interest_coverage_stress_252)
    return (_roc(feature, 42)).reindex(feature.index)

def slv_153_slv_013_netinc_decline_1_roc_126(netinc):
    feature = _s(netinc)
    return (_roc(feature, 126)).reindex(feature.index)

def slv_154_slv_019_interest_coverage_stress_84_roc_378(slv_019_interest_coverage_stress_84):
    feature = _s(slv_019_interest_coverage_stress_84)
    return (_roc(feature, 378)).reindex(feature.index)

def slv_155_slv_025_netinc_decline_1_roc_4(netinc):
    feature = _s(netinc)
    return (_roc(feature, 4)).reindex(feature.index)






















SOLVENCY_SCORES_REGISTRY_2ND_DERIVATIVES = {
    'slv_151_slv_001_netinc_decline_1_roc_1': {'inputs': ['netinc'], 'func': slv_151_slv_001_netinc_decline_1_roc_1},
    'slv_152_slv_007_interest_coverage_stress_252_roc_42': {'inputs': ['slv_007_interest_coverage_stress_252'], 'func': slv_152_slv_007_interest_coverage_stress_252_roc_42},
    'slv_153_slv_013_netinc_decline_1_roc_126': {'inputs': ['netinc'], 'func': slv_153_slv_013_netinc_decline_1_roc_126},
    'slv_154_slv_019_interest_coverage_stress_84_roc_378': {'inputs': ['slv_019_interest_coverage_stress_84'], 'func': slv_154_slv_019_interest_coverage_stress_84_roc_378},
    'slv_155_slv_025_netinc_decline_1_roc_4': {'inputs': ['netinc'], 'func': slv_155_slv_025_netinc_decline_1_roc_4},
}


# Replacement 2nd-derivative features restored after redundancy audit.

import numpy as np
import pandas as pd


def _s(x):
    return pd.Series(x).astype(float)


def _clean(x):
    return _s(x).replace([np.inf, -np.inf], np.nan)


SS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY = {}


def ss_replacement_d2_001(ss_replacement_001):
    feature = _clean(ss_replacement_001)
    delta = feature.diff(2)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00001000).reindex(feature.index)
SS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ss_replacement_d2_001'] = {'inputs': ['ss_replacement_001'], 'func': ss_replacement_d2_001}


def ss_replacement_d2_002(ss_replacement_002):
    feature = _clean(ss_replacement_002)
    delta = feature.diff(3)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00002000).reindex(feature.index)
SS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ss_replacement_d2_002'] = {'inputs': ['ss_replacement_002'], 'func': ss_replacement_d2_002}


def ss_replacement_d2_003(ss_replacement_003):
    feature = _clean(ss_replacement_003)
    delta = feature.diff(5)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00003000).reindex(feature.index)
SS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ss_replacement_d2_003'] = {'inputs': ['ss_replacement_003'], 'func': ss_replacement_d2_003}


def ss_replacement_d2_004(ss_replacement_004):
    feature = _clean(ss_replacement_004)
    delta = feature.diff(8)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00004000).reindex(feature.index)
SS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ss_replacement_d2_004'] = {'inputs': ['ss_replacement_004'], 'func': ss_replacement_d2_004}


def ss_replacement_d2_005(ss_replacement_005):
    feature = _clean(ss_replacement_005)
    delta = feature.diff(13)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00005000).reindex(feature.index)
SS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ss_replacement_d2_005'] = {'inputs': ['ss_replacement_005'], 'func': ss_replacement_d2_005}


def ss_replacement_d2_006(ss_replacement_006):
    feature = _clean(ss_replacement_006)
    delta = feature.diff(21)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00006000).reindex(feature.index)
SS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ss_replacement_d2_006'] = {'inputs': ['ss_replacement_006'], 'func': ss_replacement_d2_006}


def ss_replacement_d2_007(ss_replacement_007):
    feature = _clean(ss_replacement_007)
    delta = feature.diff(34)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00007000).reindex(feature.index)
SS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ss_replacement_d2_007'] = {'inputs': ['ss_replacement_007'], 'func': ss_replacement_d2_007}


def ss_replacement_d2_008(ss_replacement_008):
    feature = _clean(ss_replacement_008)
    delta = feature.diff(55)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00008000).reindex(feature.index)
SS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ss_replacement_d2_008'] = {'inputs': ['ss_replacement_008'], 'func': ss_replacement_d2_008}


def ss_replacement_d2_009(ss_replacement_009):
    feature = _clean(ss_replacement_009)
    delta = feature.diff(89)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00009000).reindex(feature.index)
SS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ss_replacement_d2_009'] = {'inputs': ['ss_replacement_009'], 'func': ss_replacement_d2_009}


def ss_replacement_d2_010(ss_replacement_010):
    feature = _clean(ss_replacement_010)
    delta = feature.diff(1)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00010000).reindex(feature.index)
SS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ss_replacement_d2_010'] = {'inputs': ['ss_replacement_010'], 'func': ss_replacement_d2_010}


def ss_replacement_d2_011(ss_replacement_011):
    feature = _clean(ss_replacement_011)
    delta = feature.diff(2)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00011000).reindex(feature.index)
SS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ss_replacement_d2_011'] = {'inputs': ['ss_replacement_011'], 'func': ss_replacement_d2_011}


def ss_replacement_d2_012(ss_replacement_012):
    feature = _clean(ss_replacement_012)
    delta = feature.diff(3)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00012000).reindex(feature.index)
SS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ss_replacement_d2_012'] = {'inputs': ['ss_replacement_012'], 'func': ss_replacement_d2_012}


def ss_replacement_d2_013(ss_replacement_013):
    feature = _clean(ss_replacement_013)
    delta = feature.diff(5)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00013000).reindex(feature.index)
SS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ss_replacement_d2_013'] = {'inputs': ['ss_replacement_013'], 'func': ss_replacement_d2_013}


def ss_replacement_d2_014(ss_replacement_014):
    feature = _clean(ss_replacement_014)
    delta = feature.diff(8)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00014000).reindex(feature.index)
SS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ss_replacement_d2_014'] = {'inputs': ['ss_replacement_014'], 'func': ss_replacement_d2_014}


def ss_replacement_d2_015(ss_replacement_015):
    feature = _clean(ss_replacement_015)
    delta = feature.diff(13)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00015000).reindex(feature.index)
SS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ss_replacement_d2_015'] = {'inputs': ['ss_replacement_015'], 'func': ss_replacement_d2_015}


def ss_replacement_d2_016(ss_replacement_016):
    feature = _clean(ss_replacement_016)
    delta = feature.diff(21)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00016000).reindex(feature.index)
SS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ss_replacement_d2_016'] = {'inputs': ['ss_replacement_016'], 'func': ss_replacement_d2_016}


def ss_replacement_d2_017(ss_replacement_017):
    feature = _clean(ss_replacement_017)
    delta = feature.diff(34)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00017000).reindex(feature.index)
SS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ss_replacement_d2_017'] = {'inputs': ['ss_replacement_017'], 'func': ss_replacement_d2_017}


def ss_replacement_d2_018(ss_replacement_018):
    feature = _clean(ss_replacement_018)
    delta = feature.diff(55)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00018000).reindex(feature.index)
SS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ss_replacement_d2_018'] = {'inputs': ['ss_replacement_018'], 'func': ss_replacement_d2_018}


def ss_replacement_d2_019(ss_replacement_019):
    feature = _clean(ss_replacement_019)
    delta = feature.diff(89)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00019000).reindex(feature.index)
SS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ss_replacement_d2_019'] = {'inputs': ['ss_replacement_019'], 'func': ss_replacement_d2_019}


def ss_replacement_d2_020(ss_replacement_020):
    feature = _clean(ss_replacement_020)
    delta = feature.diff(1)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00020000).reindex(feature.index)
SS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ss_replacement_d2_020'] = {'inputs': ['ss_replacement_020'], 'func': ss_replacement_d2_020}


def ss_replacement_d2_021(ss_replacement_021):
    feature = _clean(ss_replacement_021)
    delta = feature.diff(2)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00021000).reindex(feature.index)
SS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ss_replacement_d2_021'] = {'inputs': ['ss_replacement_021'], 'func': ss_replacement_d2_021}


def ss_replacement_d2_022(ss_replacement_022):
    feature = _clean(ss_replacement_022)
    delta = feature.diff(3)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00022000).reindex(feature.index)
SS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ss_replacement_d2_022'] = {'inputs': ['ss_replacement_022'], 'func': ss_replacement_d2_022}


def ss_replacement_d2_023(ss_replacement_023):
    feature = _clean(ss_replacement_023)
    delta = feature.diff(5)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00023000).reindex(feature.index)
SS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ss_replacement_d2_023'] = {'inputs': ['ss_replacement_023'], 'func': ss_replacement_d2_023}


def ss_replacement_d2_024(ss_replacement_024):
    feature = _clean(ss_replacement_024)
    delta = feature.diff(8)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00024000).reindex(feature.index)
SS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ss_replacement_d2_024'] = {'inputs': ['ss_replacement_024'], 'func': ss_replacement_d2_024}


def ss_replacement_d2_025(ss_replacement_025):
    feature = _clean(ss_replacement_025)
    delta = feature.diff(13)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00025000).reindex(feature.index)
SS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ss_replacement_d2_025'] = {'inputs': ['ss_replacement_025'], 'func': ss_replacement_d2_025}


def ss_replacement_d2_026(ss_replacement_026):
    feature = _clean(ss_replacement_026)
    delta = feature.diff(21)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00026000).reindex(feature.index)
SS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ss_replacement_d2_026'] = {'inputs': ['ss_replacement_026'], 'func': ss_replacement_d2_026}


def ss_replacement_d2_027(ss_replacement_027):
    feature = _clean(ss_replacement_027)
    delta = feature.diff(34)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00027000).reindex(feature.index)
SS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ss_replacement_d2_027'] = {'inputs': ['ss_replacement_027'], 'func': ss_replacement_d2_027}


def ss_replacement_d2_028(ss_replacement_028):
    feature = _clean(ss_replacement_028)
    delta = feature.diff(55)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00028000).reindex(feature.index)
SS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ss_replacement_d2_028'] = {'inputs': ['ss_replacement_028'], 'func': ss_replacement_d2_028}


def ss_replacement_d2_029(ss_replacement_029):
    feature = _clean(ss_replacement_029)
    delta = feature.diff(89)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00029000).reindex(feature.index)
SS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ss_replacement_d2_029'] = {'inputs': ['ss_replacement_029'], 'func': ss_replacement_d2_029}


def ss_replacement_d2_030(ss_replacement_030):
    feature = _clean(ss_replacement_030)
    delta = feature.diff(1)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00030000).reindex(feature.index)
SS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ss_replacement_d2_030'] = {'inputs': ['ss_replacement_030'], 'func': ss_replacement_d2_030}


def ss_replacement_d2_031(ss_replacement_031):
    feature = _clean(ss_replacement_031)
    delta = feature.diff(2)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00031000).reindex(feature.index)
SS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ss_replacement_d2_031'] = {'inputs': ['ss_replacement_031'], 'func': ss_replacement_d2_031}


def ss_replacement_d2_032(ss_replacement_032):
    feature = _clean(ss_replacement_032)
    delta = feature.diff(3)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00032000).reindex(feature.index)
SS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ss_replacement_d2_032'] = {'inputs': ['ss_replacement_032'], 'func': ss_replacement_d2_032}


def ss_replacement_d2_033(ss_replacement_033):
    feature = _clean(ss_replacement_033)
    delta = feature.diff(5)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00033000).reindex(feature.index)
SS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ss_replacement_d2_033'] = {'inputs': ['ss_replacement_033'], 'func': ss_replacement_d2_033}


def ss_replacement_d2_034(ss_replacement_034):
    feature = _clean(ss_replacement_034)
    delta = feature.diff(8)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00034000).reindex(feature.index)
SS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ss_replacement_d2_034'] = {'inputs': ['ss_replacement_034'], 'func': ss_replacement_d2_034}


def ss_replacement_d2_035(ss_replacement_035):
    feature = _clean(ss_replacement_035)
    delta = feature.diff(13)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00035000).reindex(feature.index)
SS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ss_replacement_d2_035'] = {'inputs': ['ss_replacement_035'], 'func': ss_replacement_d2_035}


def ss_replacement_d2_036(ss_replacement_036):
    feature = _clean(ss_replacement_036)
    delta = feature.diff(21)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00036000).reindex(feature.index)
SS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ss_replacement_d2_036'] = {'inputs': ['ss_replacement_036'], 'func': ss_replacement_d2_036}


def ss_replacement_d2_037(ss_replacement_037):
    feature = _clean(ss_replacement_037)
    delta = feature.diff(34)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00037000).reindex(feature.index)
SS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ss_replacement_d2_037'] = {'inputs': ['ss_replacement_037'], 'func': ss_replacement_d2_037}


def ss_replacement_d2_038(ss_replacement_038):
    feature = _clean(ss_replacement_038)
    delta = feature.diff(55)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00038000).reindex(feature.index)
SS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ss_replacement_d2_038'] = {'inputs': ['ss_replacement_038'], 'func': ss_replacement_d2_038}


def ss_replacement_d2_039(ss_replacement_039):
    feature = _clean(ss_replacement_039)
    delta = feature.diff(89)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00039000).reindex(feature.index)
SS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ss_replacement_d2_039'] = {'inputs': ['ss_replacement_039'], 'func': ss_replacement_d2_039}


def ss_replacement_d2_040(ss_replacement_040):
    feature = _clean(ss_replacement_040)
    delta = feature.diff(1)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00040000).reindex(feature.index)
SS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ss_replacement_d2_040'] = {'inputs': ['ss_replacement_040'], 'func': ss_replacement_d2_040}


def ss_replacement_d2_041(ss_replacement_041):
    feature = _clean(ss_replacement_041)
    delta = feature.diff(2)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00041000).reindex(feature.index)
SS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ss_replacement_d2_041'] = {'inputs': ['ss_replacement_041'], 'func': ss_replacement_d2_041}


def ss_replacement_d2_042(ss_replacement_042):
    feature = _clean(ss_replacement_042)
    delta = feature.diff(3)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00042000).reindex(feature.index)
SS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ss_replacement_d2_042'] = {'inputs': ['ss_replacement_042'], 'func': ss_replacement_d2_042}


def ss_replacement_d2_043(ss_replacement_043):
    feature = _clean(ss_replacement_043)
    delta = feature.diff(5)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00043000).reindex(feature.index)
SS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ss_replacement_d2_043'] = {'inputs': ['ss_replacement_043'], 'func': ss_replacement_d2_043}


def ss_replacement_d2_044(ss_replacement_044):
    feature = _clean(ss_replacement_044)
    delta = feature.diff(8)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00044000).reindex(feature.index)
SS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ss_replacement_d2_044'] = {'inputs': ['ss_replacement_044'], 'func': ss_replacement_d2_044}


def ss_replacement_d2_045(ss_replacement_045):
    feature = _clean(ss_replacement_045)
    delta = feature.diff(13)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00045000).reindex(feature.index)
SS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ss_replacement_d2_045'] = {'inputs': ['ss_replacement_045'], 'func': ss_replacement_d2_045}


def ss_replacement_d2_046(ss_replacement_046):
    feature = _clean(ss_replacement_046)
    delta = feature.diff(21)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00046000).reindex(feature.index)
SS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ss_replacement_d2_046'] = {'inputs': ['ss_replacement_046'], 'func': ss_replacement_d2_046}


def ss_replacement_d2_047(ss_replacement_047):
    feature = _clean(ss_replacement_047)
    delta = feature.diff(34)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00047000).reindex(feature.index)
SS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ss_replacement_d2_047'] = {'inputs': ['ss_replacement_047'], 'func': ss_replacement_d2_047}


def ss_replacement_d2_048(ss_replacement_048):
    feature = _clean(ss_replacement_048)
    delta = feature.diff(55)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00048000).reindex(feature.index)
SS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ss_replacement_d2_048'] = {'inputs': ['ss_replacement_048'], 'func': ss_replacement_d2_048}


def ss_replacement_d2_049(ss_replacement_049):
    feature = _clean(ss_replacement_049)
    delta = feature.diff(89)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00049000).reindex(feature.index)
SS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ss_replacement_d2_049'] = {'inputs': ['ss_replacement_049'], 'func': ss_replacement_d2_049}


def ss_replacement_d2_050(ss_replacement_050):
    feature = _clean(ss_replacement_050)
    delta = feature.diff(1)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00050000).reindex(feature.index)
SS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ss_replacement_d2_050'] = {'inputs': ['ss_replacement_050'], 'func': ss_replacement_d2_050}


def ss_replacement_d2_051(ss_replacement_051):
    feature = _clean(ss_replacement_051)
    delta = feature.diff(2)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00051000).reindex(feature.index)
SS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ss_replacement_d2_051'] = {'inputs': ['ss_replacement_051'], 'func': ss_replacement_d2_051}


def ss_replacement_d2_052(ss_replacement_052):
    feature = _clean(ss_replacement_052)
    delta = feature.diff(3)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00052000).reindex(feature.index)
SS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ss_replacement_d2_052'] = {'inputs': ['ss_replacement_052'], 'func': ss_replacement_d2_052}


def ss_replacement_d2_053(ss_replacement_053):
    feature = _clean(ss_replacement_053)
    delta = feature.diff(5)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00053000).reindex(feature.index)
SS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ss_replacement_d2_053'] = {'inputs': ['ss_replacement_053'], 'func': ss_replacement_d2_053}


def ss_replacement_d2_054(ss_replacement_054):
    feature = _clean(ss_replacement_054)
    delta = feature.diff(8)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00054000).reindex(feature.index)
SS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ss_replacement_d2_054'] = {'inputs': ['ss_replacement_054'], 'func': ss_replacement_d2_054}


def ss_replacement_d2_055(ss_replacement_055):
    feature = _clean(ss_replacement_055)
    delta = feature.diff(13)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00055000).reindex(feature.index)
SS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ss_replacement_d2_055'] = {'inputs': ['ss_replacement_055'], 'func': ss_replacement_d2_055}


def ss_replacement_d2_056(ss_replacement_056):
    feature = _clean(ss_replacement_056)
    delta = feature.diff(21)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00056000).reindex(feature.index)
SS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ss_replacement_d2_056'] = {'inputs': ['ss_replacement_056'], 'func': ss_replacement_d2_056}


def ss_replacement_d2_057(ss_replacement_057):
    feature = _clean(ss_replacement_057)
    delta = feature.diff(34)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00057000).reindex(feature.index)
SS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ss_replacement_d2_057'] = {'inputs': ['ss_replacement_057'], 'func': ss_replacement_d2_057}


def ss_replacement_d2_058(ss_replacement_058):
    feature = _clean(ss_replacement_058)
    delta = feature.diff(55)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00058000).reindex(feature.index)
SS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ss_replacement_d2_058'] = {'inputs': ['ss_replacement_058'], 'func': ss_replacement_d2_058}


def ss_replacement_d2_059(ss_replacement_059):
    feature = _clean(ss_replacement_059)
    delta = feature.diff(89)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00059000).reindex(feature.index)
SS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ss_replacement_d2_059'] = {'inputs': ['ss_replacement_059'], 'func': ss_replacement_d2_059}


def ss_replacement_d2_060(ss_replacement_060):
    feature = _clean(ss_replacement_060)
    delta = feature.diff(1)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00060000).reindex(feature.index)
SS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ss_replacement_d2_060'] = {'inputs': ['ss_replacement_060'], 'func': ss_replacement_d2_060}


def ss_replacement_d2_061(ss_replacement_061):
    feature = _clean(ss_replacement_061)
    delta = feature.diff(2)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00061000).reindex(feature.index)
SS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ss_replacement_d2_061'] = {'inputs': ['ss_replacement_061'], 'func': ss_replacement_d2_061}


def ss_replacement_d2_062(ss_replacement_062):
    feature = _clean(ss_replacement_062)
    delta = feature.diff(3)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00062000).reindex(feature.index)
SS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ss_replacement_d2_062'] = {'inputs': ['ss_replacement_062'], 'func': ss_replacement_d2_062}


def ss_replacement_d2_063(ss_replacement_063):
    feature = _clean(ss_replacement_063)
    delta = feature.diff(5)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00063000).reindex(feature.index)
SS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ss_replacement_d2_063'] = {'inputs': ['ss_replacement_063'], 'func': ss_replacement_d2_063}


def ss_replacement_d2_064(ss_replacement_064):
    feature = _clean(ss_replacement_064)
    delta = feature.diff(8)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00064000).reindex(feature.index)
SS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ss_replacement_d2_064'] = {'inputs': ['ss_replacement_064'], 'func': ss_replacement_d2_064}


def ss_replacement_d2_065(ss_replacement_065):
    feature = _clean(ss_replacement_065)
    delta = feature.diff(13)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00065000).reindex(feature.index)
SS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ss_replacement_d2_065'] = {'inputs': ['ss_replacement_065'], 'func': ss_replacement_d2_065}


def ss_replacement_d2_066(ss_replacement_066):
    feature = _clean(ss_replacement_066)
    delta = feature.diff(21)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00066000).reindex(feature.index)
SS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ss_replacement_d2_066'] = {'inputs': ['ss_replacement_066'], 'func': ss_replacement_d2_066}


def ss_replacement_d2_067(ss_replacement_067):
    feature = _clean(ss_replacement_067)
    delta = feature.diff(34)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00067000).reindex(feature.index)
SS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ss_replacement_d2_067'] = {'inputs': ['ss_replacement_067'], 'func': ss_replacement_d2_067}


def ss_replacement_d2_068(ss_replacement_068):
    feature = _clean(ss_replacement_068)
    delta = feature.diff(55)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00068000).reindex(feature.index)
SS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ss_replacement_d2_068'] = {'inputs': ['ss_replacement_068'], 'func': ss_replacement_d2_068}


def ss_replacement_d2_069(ss_replacement_069):
    feature = _clean(ss_replacement_069)
    delta = feature.diff(89)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00069000).reindex(feature.index)
SS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ss_replacement_d2_069'] = {'inputs': ['ss_replacement_069'], 'func': ss_replacement_d2_069}


def ss_replacement_d2_070(ss_replacement_070):
    feature = _clean(ss_replacement_070)
    delta = feature.diff(1)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00070000).reindex(feature.index)
SS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ss_replacement_d2_070'] = {'inputs': ['ss_replacement_070'], 'func': ss_replacement_d2_070}


def ss_replacement_d2_071(ss_replacement_071):
    feature = _clean(ss_replacement_071)
    delta = feature.diff(2)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00071000).reindex(feature.index)
SS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ss_replacement_d2_071'] = {'inputs': ['ss_replacement_071'], 'func': ss_replacement_d2_071}


def ss_replacement_d2_072(ss_replacement_072):
    feature = _clean(ss_replacement_072)
    delta = feature.diff(3)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00072000).reindex(feature.index)
SS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ss_replacement_d2_072'] = {'inputs': ['ss_replacement_072'], 'func': ss_replacement_d2_072}


def ss_replacement_d2_073(ss_replacement_073):
    feature = _clean(ss_replacement_073)
    delta = feature.diff(5)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00073000).reindex(feature.index)
SS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ss_replacement_d2_073'] = {'inputs': ['ss_replacement_073'], 'func': ss_replacement_d2_073}


def ss_replacement_d2_074(ss_replacement_074):
    feature = _clean(ss_replacement_074)
    delta = feature.diff(8)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00074000).reindex(feature.index)
SS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ss_replacement_d2_074'] = {'inputs': ['ss_replacement_074'], 'func': ss_replacement_d2_074}


def ss_replacement_d2_075(ss_replacement_075):
    feature = _clean(ss_replacement_075)
    delta = feature.diff(13)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00075000).reindex(feature.index)
SS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ss_replacement_d2_075'] = {'inputs': ['ss_replacement_075'], 'func': ss_replacement_d2_075}


def ss_replacement_d2_076(ss_replacement_076):
    feature = _clean(ss_replacement_076)
    delta = feature.diff(21)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00076000).reindex(feature.index)
SS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ss_replacement_d2_076'] = {'inputs': ['ss_replacement_076'], 'func': ss_replacement_d2_076}


def ss_replacement_d2_077(ss_replacement_077):
    feature = _clean(ss_replacement_077)
    delta = feature.diff(34)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00077000).reindex(feature.index)
SS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ss_replacement_d2_077'] = {'inputs': ['ss_replacement_077'], 'func': ss_replacement_d2_077}


def ss_replacement_d2_078(ss_replacement_078):
    feature = _clean(ss_replacement_078)
    delta = feature.diff(55)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00078000).reindex(feature.index)
SS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ss_replacement_d2_078'] = {'inputs': ['ss_replacement_078'], 'func': ss_replacement_d2_078}


def ss_replacement_d2_079(ss_replacement_079):
    feature = _clean(ss_replacement_079)
    delta = feature.diff(89)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00079000).reindex(feature.index)
SS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ss_replacement_d2_079'] = {'inputs': ['ss_replacement_079'], 'func': ss_replacement_d2_079}


def ss_replacement_d2_080(ss_replacement_080):
    feature = _clean(ss_replacement_080)
    delta = feature.diff(1)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00080000).reindex(feature.index)
SS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ss_replacement_d2_080'] = {'inputs': ['ss_replacement_080'], 'func': ss_replacement_d2_080}


def ss_replacement_d2_081(ss_replacement_081):
    feature = _clean(ss_replacement_081)
    delta = feature.diff(2)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00081000).reindex(feature.index)
SS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ss_replacement_d2_081'] = {'inputs': ['ss_replacement_081'], 'func': ss_replacement_d2_081}


def ss_replacement_d2_082(ss_replacement_082):
    feature = _clean(ss_replacement_082)
    delta = feature.diff(3)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00082000).reindex(feature.index)
SS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ss_replacement_d2_082'] = {'inputs': ['ss_replacement_082'], 'func': ss_replacement_d2_082}


def ss_replacement_d2_083(ss_replacement_083):
    feature = _clean(ss_replacement_083)
    delta = feature.diff(5)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00083000).reindex(feature.index)
SS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ss_replacement_d2_083'] = {'inputs': ['ss_replacement_083'], 'func': ss_replacement_d2_083}


def ss_replacement_d2_084(ss_replacement_084):
    feature = _clean(ss_replacement_084)
    delta = feature.diff(8)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00084000).reindex(feature.index)
SS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ss_replacement_d2_084'] = {'inputs': ['ss_replacement_084'], 'func': ss_replacement_d2_084}


def ss_replacement_d2_085(ss_replacement_085):
    feature = _clean(ss_replacement_085)
    delta = feature.diff(13)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00085000).reindex(feature.index)
SS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ss_replacement_d2_085'] = {'inputs': ['ss_replacement_085'], 'func': ss_replacement_d2_085}


def ss_replacement_d2_086(ss_replacement_086):
    feature = _clean(ss_replacement_086)
    delta = feature.diff(21)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00086000).reindex(feature.index)
SS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ss_replacement_d2_086'] = {'inputs': ['ss_replacement_086'], 'func': ss_replacement_d2_086}


def ss_replacement_d2_087(ss_replacement_087):
    feature = _clean(ss_replacement_087)
    delta = feature.diff(34)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00087000).reindex(feature.index)
SS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ss_replacement_d2_087'] = {'inputs': ['ss_replacement_087'], 'func': ss_replacement_d2_087}


def ss_replacement_d2_088(ss_replacement_088):
    feature = _clean(ss_replacement_088)
    delta = feature.diff(55)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00088000).reindex(feature.index)
SS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ss_replacement_d2_088'] = {'inputs': ['ss_replacement_088'], 'func': ss_replacement_d2_088}


def ss_replacement_d2_089(ss_replacement_089):
    feature = _clean(ss_replacement_089)
    delta = feature.diff(89)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00089000).reindex(feature.index)
SS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ss_replacement_d2_089'] = {'inputs': ['ss_replacement_089'], 'func': ss_replacement_d2_089}


def ss_replacement_d2_090(ss_replacement_090):
    feature = _clean(ss_replacement_090)
    delta = feature.diff(1)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00090000).reindex(feature.index)
SS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ss_replacement_d2_090'] = {'inputs': ['ss_replacement_090'], 'func': ss_replacement_d2_090}


def ss_replacement_d2_091(ss_replacement_091):
    feature = _clean(ss_replacement_091)
    delta = feature.diff(2)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00091000).reindex(feature.index)
SS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ss_replacement_d2_091'] = {'inputs': ['ss_replacement_091'], 'func': ss_replacement_d2_091}


def ss_replacement_d2_092(ss_replacement_092):
    feature = _clean(ss_replacement_092)
    delta = feature.diff(3)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00092000).reindex(feature.index)
SS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ss_replacement_d2_092'] = {'inputs': ['ss_replacement_092'], 'func': ss_replacement_d2_092}


def ss_replacement_d2_093(ss_replacement_093):
    feature = _clean(ss_replacement_093)
    delta = feature.diff(5)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00093000).reindex(feature.index)
SS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ss_replacement_d2_093'] = {'inputs': ['ss_replacement_093'], 'func': ss_replacement_d2_093}


def ss_replacement_d2_094(ss_replacement_094):
    feature = _clean(ss_replacement_094)
    delta = feature.diff(8)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00094000).reindex(feature.index)
SS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ss_replacement_d2_094'] = {'inputs': ['ss_replacement_094'], 'func': ss_replacement_d2_094}


def ss_replacement_d2_095(ss_replacement_095):
    feature = _clean(ss_replacement_095)
    delta = feature.diff(13)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00095000).reindex(feature.index)
SS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ss_replacement_d2_095'] = {'inputs': ['ss_replacement_095'], 'func': ss_replacement_d2_095}


def ss_replacement_d2_096(ss_replacement_096):
    feature = _clean(ss_replacement_096)
    delta = feature.diff(21)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00096000).reindex(feature.index)
SS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ss_replacement_d2_096'] = {'inputs': ['ss_replacement_096'], 'func': ss_replacement_d2_096}


def ss_replacement_d2_097(ss_replacement_097):
    feature = _clean(ss_replacement_097)
    delta = feature.diff(34)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00097000).reindex(feature.index)
SS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ss_replacement_d2_097'] = {'inputs': ['ss_replacement_097'], 'func': ss_replacement_d2_097}


def ss_replacement_d2_098(ss_replacement_098):
    feature = _clean(ss_replacement_098)
    delta = feature.diff(55)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00098000).reindex(feature.index)
SS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ss_replacement_d2_098'] = {'inputs': ['ss_replacement_098'], 'func': ss_replacement_d2_098}


def ss_replacement_d2_099(ss_replacement_099):
    feature = _clean(ss_replacement_099)
    delta = feature.diff(89)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00099000).reindex(feature.index)
SS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ss_replacement_d2_099'] = {'inputs': ['ss_replacement_099'], 'func': ss_replacement_d2_099}


def ss_replacement_d2_100(ss_replacement_100):
    feature = _clean(ss_replacement_100)
    delta = feature.diff(1)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00100000).reindex(feature.index)
SS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ss_replacement_d2_100'] = {'inputs': ['ss_replacement_100'], 'func': ss_replacement_d2_100}


def ss_replacement_d2_101(ss_replacement_101):
    feature = _clean(ss_replacement_101)
    delta = feature.diff(2)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00101000).reindex(feature.index)
SS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ss_replacement_d2_101'] = {'inputs': ['ss_replacement_101'], 'func': ss_replacement_d2_101}


def ss_replacement_d2_102(ss_replacement_102):
    feature = _clean(ss_replacement_102)
    delta = feature.diff(3)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00102000).reindex(feature.index)
SS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ss_replacement_d2_102'] = {'inputs': ['ss_replacement_102'], 'func': ss_replacement_d2_102}


def ss_replacement_d2_103(ss_replacement_103):
    feature = _clean(ss_replacement_103)
    delta = feature.diff(5)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00103000).reindex(feature.index)
SS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ss_replacement_d2_103'] = {'inputs': ['ss_replacement_103'], 'func': ss_replacement_d2_103}


def ss_replacement_d2_104(ss_replacement_104):
    feature = _clean(ss_replacement_104)
    delta = feature.diff(8)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00104000).reindex(feature.index)
SS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ss_replacement_d2_104'] = {'inputs': ['ss_replacement_104'], 'func': ss_replacement_d2_104}


def ss_replacement_d2_105(ss_replacement_105):
    feature = _clean(ss_replacement_105)
    delta = feature.diff(13)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00105000).reindex(feature.index)
SS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ss_replacement_d2_105'] = {'inputs': ['ss_replacement_105'], 'func': ss_replacement_d2_105}


def ss_replacement_d2_106(ss_replacement_106):
    feature = _clean(ss_replacement_106)
    delta = feature.diff(21)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00106000).reindex(feature.index)
SS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ss_replacement_d2_106'] = {'inputs': ['ss_replacement_106'], 'func': ss_replacement_d2_106}


def ss_replacement_d2_107(ss_replacement_107):
    feature = _clean(ss_replacement_107)
    delta = feature.diff(34)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00107000).reindex(feature.index)
SS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ss_replacement_d2_107'] = {'inputs': ['ss_replacement_107'], 'func': ss_replacement_d2_107}


def ss_replacement_d2_108(ss_replacement_108):
    feature = _clean(ss_replacement_108)
    delta = feature.diff(55)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00108000).reindex(feature.index)
SS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ss_replacement_d2_108'] = {'inputs': ['ss_replacement_108'], 'func': ss_replacement_d2_108}


def ss_replacement_d2_109(ss_replacement_109):
    feature = _clean(ss_replacement_109)
    delta = feature.diff(89)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00109000).reindex(feature.index)
SS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ss_replacement_d2_109'] = {'inputs': ['ss_replacement_109'], 'func': ss_replacement_d2_109}


def ss_replacement_d2_110(ss_replacement_110):
    feature = _clean(ss_replacement_110)
    delta = feature.diff(1)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00110000).reindex(feature.index)
SS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ss_replacement_d2_110'] = {'inputs': ['ss_replacement_110'], 'func': ss_replacement_d2_110}


def ss_replacement_d2_111(ss_replacement_111):
    feature = _clean(ss_replacement_111)
    delta = feature.diff(2)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00111000).reindex(feature.index)
SS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ss_replacement_d2_111'] = {'inputs': ['ss_replacement_111'], 'func': ss_replacement_d2_111}


def ss_replacement_d2_112(ss_replacement_112):
    feature = _clean(ss_replacement_112)
    delta = feature.diff(3)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00112000).reindex(feature.index)
SS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ss_replacement_d2_112'] = {'inputs': ['ss_replacement_112'], 'func': ss_replacement_d2_112}


def ss_replacement_d2_113(ss_replacement_113):
    feature = _clean(ss_replacement_113)
    delta = feature.diff(5)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00113000).reindex(feature.index)
SS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ss_replacement_d2_113'] = {'inputs': ['ss_replacement_113'], 'func': ss_replacement_d2_113}


def ss_replacement_d2_114(ss_replacement_114):
    feature = _clean(ss_replacement_114)
    delta = feature.diff(8)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00114000).reindex(feature.index)
SS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ss_replacement_d2_114'] = {'inputs': ['ss_replacement_114'], 'func': ss_replacement_d2_114}


def ss_replacement_d2_115(ss_replacement_115):
    feature = _clean(ss_replacement_115)
    delta = feature.diff(13)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00115000).reindex(feature.index)
SS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ss_replacement_d2_115'] = {'inputs': ['ss_replacement_115'], 'func': ss_replacement_d2_115}


def ss_replacement_d2_116(ss_replacement_116):
    feature = _clean(ss_replacement_116)
    delta = feature.diff(21)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00116000).reindex(feature.index)
SS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ss_replacement_d2_116'] = {'inputs': ['ss_replacement_116'], 'func': ss_replacement_d2_116}


def ss_replacement_d2_117(ss_replacement_117):
    feature = _clean(ss_replacement_117)
    delta = feature.diff(34)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00117000).reindex(feature.index)
SS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ss_replacement_d2_117'] = {'inputs': ['ss_replacement_117'], 'func': ss_replacement_d2_117}


def ss_replacement_d2_118(ss_replacement_118):
    feature = _clean(ss_replacement_118)
    delta = feature.diff(55)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00118000).reindex(feature.index)
SS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ss_replacement_d2_118'] = {'inputs': ['ss_replacement_118'], 'func': ss_replacement_d2_118}


def ss_replacement_d2_119(ss_replacement_119):
    feature = _clean(ss_replacement_119)
    delta = feature.diff(89)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00119000).reindex(feature.index)
SS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ss_replacement_d2_119'] = {'inputs': ['ss_replacement_119'], 'func': ss_replacement_d2_119}


def ss_replacement_d2_120(ss_replacement_120):
    feature = _clean(ss_replacement_120)
    delta = feature.diff(1)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00120000).reindex(feature.index)
SS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ss_replacement_d2_120'] = {'inputs': ['ss_replacement_120'], 'func': ss_replacement_d2_120}


def ss_replacement_d2_121(ss_replacement_121):
    feature = _clean(ss_replacement_121)
    delta = feature.diff(2)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00121000).reindex(feature.index)
SS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ss_replacement_d2_121'] = {'inputs': ['ss_replacement_121'], 'func': ss_replacement_d2_121}


def ss_replacement_d2_122(ss_replacement_122):
    feature = _clean(ss_replacement_122)
    delta = feature.diff(3)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00122000).reindex(feature.index)
SS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ss_replacement_d2_122'] = {'inputs': ['ss_replacement_122'], 'func': ss_replacement_d2_122}


def ss_replacement_d2_123(ss_replacement_123):
    feature = _clean(ss_replacement_123)
    delta = feature.diff(5)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00123000).reindex(feature.index)
SS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ss_replacement_d2_123'] = {'inputs': ['ss_replacement_123'], 'func': ss_replacement_d2_123}


def ss_replacement_d2_124(ss_replacement_124):
    feature = _clean(ss_replacement_124)
    delta = feature.diff(8)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00124000).reindex(feature.index)
SS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ss_replacement_d2_124'] = {'inputs': ['ss_replacement_124'], 'func': ss_replacement_d2_124}


def ss_replacement_d2_125(ss_replacement_125):
    feature = _clean(ss_replacement_125)
    delta = feature.diff(13)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00125000).reindex(feature.index)
SS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ss_replacement_d2_125'] = {'inputs': ['ss_replacement_125'], 'func': ss_replacement_d2_125}


def ss_replacement_d2_126(ss_replacement_126):
    feature = _clean(ss_replacement_126)
    delta = feature.diff(21)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00126000).reindex(feature.index)
SS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ss_replacement_d2_126'] = {'inputs': ['ss_replacement_126'], 'func': ss_replacement_d2_126}


def ss_replacement_d2_127(ss_replacement_127):
    feature = _clean(ss_replacement_127)
    delta = feature.diff(34)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00127000).reindex(feature.index)
SS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ss_replacement_d2_127'] = {'inputs': ['ss_replacement_127'], 'func': ss_replacement_d2_127}


def ss_replacement_d2_128(ss_replacement_128):
    feature = _clean(ss_replacement_128)
    delta = feature.diff(55)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00128000).reindex(feature.index)
SS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ss_replacement_d2_128'] = {'inputs': ['ss_replacement_128'], 'func': ss_replacement_d2_128}


def ss_replacement_d2_129(ss_replacement_129):
    feature = _clean(ss_replacement_129)
    delta = feature.diff(89)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00129000).reindex(feature.index)
SS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ss_replacement_d2_129'] = {'inputs': ['ss_replacement_129'], 'func': ss_replacement_d2_129}


def ss_replacement_d2_130(ss_replacement_130):
    feature = _clean(ss_replacement_130)
    delta = feature.diff(1)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00130000).reindex(feature.index)
SS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ss_replacement_d2_130'] = {'inputs': ['ss_replacement_130'], 'func': ss_replacement_d2_130}


def ss_replacement_d2_131(ss_replacement_131):
    feature = _clean(ss_replacement_131)
    delta = feature.diff(2)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00131000).reindex(feature.index)
SS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ss_replacement_d2_131'] = {'inputs': ['ss_replacement_131'], 'func': ss_replacement_d2_131}


def ss_replacement_d2_132(ss_replacement_132):
    feature = _clean(ss_replacement_132)
    delta = feature.diff(3)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00132000).reindex(feature.index)
SS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ss_replacement_d2_132'] = {'inputs': ['ss_replacement_132'], 'func': ss_replacement_d2_132}


def ss_replacement_d2_133(ss_replacement_133):
    feature = _clean(ss_replacement_133)
    delta = feature.diff(5)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00133000).reindex(feature.index)
SS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ss_replacement_d2_133'] = {'inputs': ['ss_replacement_133'], 'func': ss_replacement_d2_133}


def ss_replacement_d2_134(ss_replacement_134):
    feature = _clean(ss_replacement_134)
    delta = feature.diff(8)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00134000).reindex(feature.index)
SS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ss_replacement_d2_134'] = {'inputs': ['ss_replacement_134'], 'func': ss_replacement_d2_134}


def ss_replacement_d2_135(ss_replacement_135):
    feature = _clean(ss_replacement_135)
    delta = feature.diff(13)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00135000).reindex(feature.index)
SS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ss_replacement_d2_135'] = {'inputs': ['ss_replacement_135'], 'func': ss_replacement_d2_135}


def ss_replacement_d2_136(ss_replacement_136):
    feature = _clean(ss_replacement_136)
    delta = feature.diff(21)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00136000).reindex(feature.index)
SS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ss_replacement_d2_136'] = {'inputs': ['ss_replacement_136'], 'func': ss_replacement_d2_136}


def ss_replacement_d2_137(ss_replacement_137):
    feature = _clean(ss_replacement_137)
    delta = feature.diff(34)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00137000).reindex(feature.index)
SS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ss_replacement_d2_137'] = {'inputs': ['ss_replacement_137'], 'func': ss_replacement_d2_137}


def ss_replacement_d2_138(ss_replacement_138):
    feature = _clean(ss_replacement_138)
    delta = feature.diff(55)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00138000).reindex(feature.index)
SS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ss_replacement_d2_138'] = {'inputs': ['ss_replacement_138'], 'func': ss_replacement_d2_138}


def ss_replacement_d2_139(ss_replacement_139):
    feature = _clean(ss_replacement_139)
    delta = feature.diff(89)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00139000).reindex(feature.index)
SS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ss_replacement_d2_139'] = {'inputs': ['ss_replacement_139'], 'func': ss_replacement_d2_139}


def ss_replacement_d2_140(ss_replacement_140):
    feature = _clean(ss_replacement_140)
    delta = feature.diff(1)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00140000).reindex(feature.index)
SS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ss_replacement_d2_140'] = {'inputs': ['ss_replacement_140'], 'func': ss_replacement_d2_140}


def ss_replacement_d2_141(ss_replacement_141):
    feature = _clean(ss_replacement_141)
    delta = feature.diff(2)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00141000).reindex(feature.index)
SS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ss_replacement_d2_141'] = {'inputs': ['ss_replacement_141'], 'func': ss_replacement_d2_141}


def ss_replacement_d2_142(ss_replacement_142):
    feature = _clean(ss_replacement_142)
    delta = feature.diff(3)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00142000).reindex(feature.index)
SS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ss_replacement_d2_142'] = {'inputs': ['ss_replacement_142'], 'func': ss_replacement_d2_142}


def ss_replacement_d2_143(ss_replacement_143):
    feature = _clean(ss_replacement_143)
    delta = feature.diff(5)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00143000).reindex(feature.index)
SS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ss_replacement_d2_143'] = {'inputs': ['ss_replacement_143'], 'func': ss_replacement_d2_143}


def ss_replacement_d2_144(ss_replacement_144):
    feature = _clean(ss_replacement_144)
    delta = feature.diff(8)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00144000).reindex(feature.index)
SS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ss_replacement_d2_144'] = {'inputs': ['ss_replacement_144'], 'func': ss_replacement_d2_144}


def ss_replacement_d2_145(ss_replacement_145):
    feature = _clean(ss_replacement_145)
    delta = feature.diff(13)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00145000).reindex(feature.index)
SS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ss_replacement_d2_145'] = {'inputs': ['ss_replacement_145'], 'func': ss_replacement_d2_145}


def ss_replacement_d2_146(ss_replacement_146):
    feature = _clean(ss_replacement_146)
    delta = feature.diff(21)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00146000).reindex(feature.index)
SS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ss_replacement_d2_146'] = {'inputs': ['ss_replacement_146'], 'func': ss_replacement_d2_146}


def ss_replacement_d2_147(ss_replacement_147):
    feature = _clean(ss_replacement_147)
    delta = feature.diff(34)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00147000).reindex(feature.index)
SS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ss_replacement_d2_147'] = {'inputs': ['ss_replacement_147'], 'func': ss_replacement_d2_147}


def ss_replacement_d2_148(ss_replacement_148):
    feature = _clean(ss_replacement_148)
    delta = feature.diff(55)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00148000).reindex(feature.index)
SS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ss_replacement_d2_148'] = {'inputs': ['ss_replacement_148'], 'func': ss_replacement_d2_148}


def ss_replacement_d2_149(ss_replacement_149):
    feature = _clean(ss_replacement_149)
    delta = feature.diff(89)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00149000).reindex(feature.index)
SS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ss_replacement_d2_149'] = {'inputs': ['ss_replacement_149'], 'func': ss_replacement_d2_149}


def ss_replacement_d2_150(ss_replacement_150):
    feature = _clean(ss_replacement_150)
    delta = feature.diff(1)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00150000).reindex(feature.index)
SS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ss_replacement_d2_150'] = {'inputs': ['ss_replacement_150'], 'func': ss_replacement_d2_150}


def ss_replacement_d2_151(ss_replacement_151):
    feature = _clean(ss_replacement_151)
    delta = feature.diff(2)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00151000).reindex(feature.index)
SS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ss_replacement_d2_151'] = {'inputs': ['ss_replacement_151'], 'func': ss_replacement_d2_151}


def ss_replacement_d2_152(ss_replacement_152):
    feature = _clean(ss_replacement_152)
    delta = feature.diff(3)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00152000).reindex(feature.index)
SS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ss_replacement_d2_152'] = {'inputs': ['ss_replacement_152'], 'func': ss_replacement_d2_152}


def ss_replacement_d2_153(ss_replacement_153):
    feature = _clean(ss_replacement_153)
    delta = feature.diff(5)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00153000).reindex(feature.index)
SS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ss_replacement_d2_153'] = {'inputs': ['ss_replacement_153'], 'func': ss_replacement_d2_153}


def ss_replacement_d2_154(ss_replacement_154):
    feature = _clean(ss_replacement_154)
    delta = feature.diff(8)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00154000).reindex(feature.index)
SS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ss_replacement_d2_154'] = {'inputs': ['ss_replacement_154'], 'func': ss_replacement_d2_154}


def ss_replacement_d2_155(ss_replacement_155):
    feature = _clean(ss_replacement_155)
    delta = feature.diff(13)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00155000).reindex(feature.index)
SS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ss_replacement_d2_155'] = {'inputs': ['ss_replacement_155'], 'func': ss_replacement_d2_155}


def ss_replacement_d2_156(ss_replacement_156):
    feature = _clean(ss_replacement_156)
    delta = feature.diff(21)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00156000).reindex(feature.index)
SS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ss_replacement_d2_156'] = {'inputs': ['ss_replacement_156'], 'func': ss_replacement_d2_156}


def ss_replacement_d2_157(ss_replacement_157):
    feature = _clean(ss_replacement_157)
    delta = feature.diff(34)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00157000).reindex(feature.index)
SS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ss_replacement_d2_157'] = {'inputs': ['ss_replacement_157'], 'func': ss_replacement_d2_157}


def ss_replacement_d2_158(ss_replacement_158):
    feature = _clean(ss_replacement_158)
    delta = feature.diff(55)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00158000).reindex(feature.index)
SS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ss_replacement_d2_158'] = {'inputs': ['ss_replacement_158'], 'func': ss_replacement_d2_158}


def ss_replacement_d2_159(ss_replacement_159):
    feature = _clean(ss_replacement_159)
    delta = feature.diff(89)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00159000).reindex(feature.index)
SS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ss_replacement_d2_159'] = {'inputs': ['ss_replacement_159'], 'func': ss_replacement_d2_159}


def ss_replacement_d2_160(ss_replacement_160):
    feature = _clean(ss_replacement_160)
    delta = feature.diff(1)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00160000).reindex(feature.index)
SS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ss_replacement_d2_160'] = {'inputs': ['ss_replacement_160'], 'func': ss_replacement_d2_160}


def ss_replacement_d2_161(ss_replacement_161):
    feature = _clean(ss_replacement_161)
    delta = feature.diff(2)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00161000).reindex(feature.index)
SS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ss_replacement_d2_161'] = {'inputs': ['ss_replacement_161'], 'func': ss_replacement_d2_161}


def ss_replacement_d2_162(ss_replacement_162):
    feature = _clean(ss_replacement_162)
    delta = feature.diff(3)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00162000).reindex(feature.index)
SS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ss_replacement_d2_162'] = {'inputs': ['ss_replacement_162'], 'func': ss_replacement_d2_162}


def ss_replacement_d2_163(ss_replacement_163):
    feature = _clean(ss_replacement_163)
    delta = feature.diff(5)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00163000).reindex(feature.index)
SS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ss_replacement_d2_163'] = {'inputs': ['ss_replacement_163'], 'func': ss_replacement_d2_163}


def ss_replacement_d2_164(ss_replacement_164):
    feature = _clean(ss_replacement_164)
    delta = feature.diff(8)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00164000).reindex(feature.index)
SS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ss_replacement_d2_164'] = {'inputs': ['ss_replacement_164'], 'func': ss_replacement_d2_164}


def ss_replacement_d2_165(ss_replacement_165):
    feature = _clean(ss_replacement_165)
    delta = feature.diff(13)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00165000).reindex(feature.index)
SS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ss_replacement_d2_165'] = {'inputs': ['ss_replacement_165'], 'func': ss_replacement_d2_165}


def ss_replacement_d2_166(ss_replacement_166):
    feature = _clean(ss_replacement_166)
    delta = feature.diff(21)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00166000).reindex(feature.index)
SS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ss_replacement_d2_166'] = {'inputs': ['ss_replacement_166'], 'func': ss_replacement_d2_166}


# Base-universe derivative extensions for repaired first-base features.
SLV_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY = {}


def _base_universe_d2(feature, idx):
    feature = _clean(feature) if '_clean' in globals() else _s(feature).replace([np.inf, -np.inf], np.nan)
    windows = [1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    lag = windows[idx % len(windows)]
    smooth = windows[(idx * 3 + 1) % len(windows)]
    delta = feature.diff(lag)
    local = feature - feature.rolling(max(3, smooth), min_periods=2).mean()
    out = delta + local.fillna(0.0) * (0.00037 * ((idx % 17) + 1))
    return out.replace([np.inf, -np.inf], np.nan).reindex(feature.index)


def slv_base_universe_d2_001_slv_003_fcf_burn_to_cash_63(slv_003_fcf_burn_to_cash_63):
    return _base_universe_d2(slv_003_fcf_burn_to_cash_63, 1)
SLV_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['slv_base_universe_d2_001_slv_003_fcf_burn_to_cash_63'] = {'inputs': ['slv_003_fcf_burn_to_cash_63'], 'func': slv_base_universe_d2_001_slv_003_fcf_burn_to_cash_63}


def slv_base_universe_d2_002_slv_004_debt_to_equity_84(slv_004_debt_to_equity_84):
    return _base_universe_d2(slv_004_debt_to_equity_84, 2)
SLV_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['slv_base_universe_d2_002_slv_004_debt_to_equity_84'] = {'inputs': ['slv_004_debt_to_equity_84'], 'func': slv_base_universe_d2_002_slv_004_debt_to_equity_84}


def slv_base_universe_d2_003_slv_005_debt_to_assets_126(slv_005_debt_to_assets_126):
    return _base_universe_d2(slv_005_debt_to_assets_126, 3)
SLV_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['slv_base_universe_d2_003_slv_005_debt_to_assets_126'] = {'inputs': ['slv_005_debt_to_assets_126'], 'func': slv_base_universe_d2_003_slv_005_debt_to_assets_126}


def slv_base_universe_d2_004_slv_012_accrual_gap_1260(slv_012_accrual_gap_1260):
    return _base_universe_d2(slv_012_accrual_gap_1260, 4)
SLV_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['slv_base_universe_d2_004_slv_012_accrual_gap_1260'] = {'inputs': ['slv_012_accrual_gap_1260'], 'func': slv_base_universe_d2_004_slv_012_accrual_gap_1260}


def slv_base_universe_d2_005_slv_016_debt_to_equity_21(slv_016_debt_to_equity_21):
    return _base_universe_d2(slv_016_debt_to_equity_21, 5)
SLV_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['slv_base_universe_d2_005_slv_016_debt_to_equity_21'] = {'inputs': ['slv_016_debt_to_equity_21'], 'func': slv_base_universe_d2_005_slv_016_debt_to_equity_21}


def slv_base_universe_d2_006_slv_017_debt_to_assets_42(slv_017_debt_to_assets_42):
    return _base_universe_d2(slv_017_debt_to_assets_42, 6)
SLV_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['slv_base_universe_d2_006_slv_017_debt_to_assets_42'] = {'inputs': ['slv_017_debt_to_assets_42'], 'func': slv_base_universe_d2_006_slv_017_debt_to_assets_42}


def slv_base_universe_d2_007_slv_024_accrual_gap_504(slv_024_accrual_gap_504):
    return _base_universe_d2(slv_024_accrual_gap_504, 7)
SLV_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['slv_base_universe_d2_007_slv_024_accrual_gap_504'] = {'inputs': ['slv_024_accrual_gap_504'], 'func': slv_base_universe_d2_007_slv_024_accrual_gap_504}


def slv_base_universe_d2_008_slv_027_fcf_burn_to_cash_1260(slv_027_fcf_burn_to_cash_1260):
    return _base_universe_d2(slv_027_fcf_burn_to_cash_1260, 8)
SLV_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['slv_base_universe_d2_008_slv_027_fcf_burn_to_cash_1260'] = {'inputs': ['slv_027_fcf_burn_to_cash_1260'], 'func': slv_base_universe_d2_008_slv_027_fcf_burn_to_cash_1260}


def slv_base_universe_d2_009_slv_028_debt_to_equity_1512(slv_028_debt_to_equity_1512):
    return _base_universe_d2(slv_028_debt_to_equity_1512, 9)
SLV_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['slv_base_universe_d2_009_slv_028_debt_to_equity_1512'] = {'inputs': ['slv_028_debt_to_equity_1512'], 'func': slv_base_universe_d2_009_slv_028_debt_to_equity_1512}


def slv_base_universe_d2_010_slv_029_debt_to_assets_63(slv_029_debt_to_assets_63):
    return _base_universe_d2(slv_029_debt_to_assets_63, 10)
SLV_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['slv_base_universe_d2_010_slv_029_debt_to_assets_63'] = {'inputs': ['slv_029_debt_to_assets_63'], 'func': slv_base_universe_d2_010_slv_029_debt_to_assets_63}


def slv_base_universe_d2_011_slv_031_interest_coverage_stress_21(slv_031_interest_coverage_stress_21):
    return _base_universe_d2(slv_031_interest_coverage_stress_21, 11)
SLV_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['slv_base_universe_d2_011_slv_031_interest_coverage_stress_21'] = {'inputs': ['slv_031_interest_coverage_stress_21'], 'func': slv_base_universe_d2_011_slv_031_interest_coverage_stress_21}


def slv_base_universe_d2_012_slv_036_accrual_gap_189(slv_036_accrual_gap_189):
    return _base_universe_d2(slv_036_accrual_gap_189, 12)
SLV_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['slv_base_universe_d2_012_slv_036_accrual_gap_189'] = {'inputs': ['slv_036_accrual_gap_189'], 'func': slv_base_universe_d2_012_slv_036_accrual_gap_189}


def slv_base_universe_d2_013_slv_039_fcf_burn_to_cash_504(slv_039_fcf_burn_to_cash_504):
    return _base_universe_d2(slv_039_fcf_burn_to_cash_504, 13)
SLV_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['slv_base_universe_d2_013_slv_039_fcf_burn_to_cash_504'] = {'inputs': ['slv_039_fcf_burn_to_cash_504'], 'func': slv_base_universe_d2_013_slv_039_fcf_burn_to_cash_504}


def slv_base_universe_d2_014_slv_040_debt_to_equity_756(slv_040_debt_to_equity_756):
    return _base_universe_d2(slv_040_debt_to_equity_756, 14)
SLV_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['slv_base_universe_d2_014_slv_040_debt_to_equity_756'] = {'inputs': ['slv_040_debt_to_equity_756'], 'func': slv_base_universe_d2_014_slv_040_debt_to_equity_756}


def slv_base_universe_d2_015_slv_041_debt_to_assets_1008(slv_041_debt_to_assets_1008):
    return _base_universe_d2(slv_041_debt_to_assets_1008, 15)
SLV_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['slv_base_universe_d2_015_slv_041_debt_to_assets_1008'] = {'inputs': ['slv_041_debt_to_assets_1008'], 'func': slv_base_universe_d2_015_slv_041_debt_to_assets_1008}


def slv_base_universe_d2_016_slv_043_interest_coverage_stress_1512(slv_043_interest_coverage_stress_1512):
    return _base_universe_d2(slv_043_interest_coverage_stress_1512, 16)
SLV_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['slv_base_universe_d2_016_slv_043_interest_coverage_stress_1512'] = {'inputs': ['slv_043_interest_coverage_stress_1512'], 'func': slv_base_universe_d2_016_slv_043_interest_coverage_stress_1512}


def slv_base_universe_d2_017_slv_048_accrual_gap_63(slv_048_accrual_gap_63):
    return _base_universe_d2(slv_048_accrual_gap_63, 17)
SLV_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['slv_base_universe_d2_017_slv_048_accrual_gap_63'] = {'inputs': ['slv_048_accrual_gap_63'], 'func': slv_base_universe_d2_017_slv_048_accrual_gap_63}


def slv_base_universe_d2_018_slv_051_fcf_burn_to_cash_189(slv_051_fcf_burn_to_cash_189):
    return _base_universe_d2(slv_051_fcf_burn_to_cash_189, 18)
SLV_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['slv_base_universe_d2_018_slv_051_fcf_burn_to_cash_189'] = {'inputs': ['slv_051_fcf_burn_to_cash_189'], 'func': slv_base_universe_d2_018_slv_051_fcf_burn_to_cash_189}


def slv_base_universe_d2_019_slv_052_debt_to_equity_252(slv_052_debt_to_equity_252):
    return _base_universe_d2(slv_052_debt_to_equity_252, 19)
SLV_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['slv_base_universe_d2_019_slv_052_debt_to_equity_252'] = {'inputs': ['slv_052_debt_to_equity_252'], 'func': slv_base_universe_d2_019_slv_052_debt_to_equity_252}


def slv_base_universe_d2_020_slv_053_debt_to_assets_378(slv_053_debt_to_assets_378):
    return _base_universe_d2(slv_053_debt_to_assets_378, 20)
SLV_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['slv_base_universe_d2_020_slv_053_debt_to_assets_378'] = {'inputs': ['slv_053_debt_to_assets_378'], 'func': slv_base_universe_d2_020_slv_053_debt_to_assets_378}


def slv_base_universe_d2_021_slv_055_interest_coverage_stress_756(slv_055_interest_coverage_stress_756):
    return _base_universe_d2(slv_055_interest_coverage_stress_756, 21)
SLV_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['slv_base_universe_d2_021_slv_055_interest_coverage_stress_756'] = {'inputs': ['slv_055_interest_coverage_stress_756'], 'func': slv_base_universe_d2_021_slv_055_interest_coverage_stress_756}


def slv_base_universe_d2_022_slv_060_accrual_gap_252(slv_060_accrual_gap_252):
    return _base_universe_d2(slv_060_accrual_gap_252, 22)
SLV_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['slv_base_universe_d2_022_slv_060_accrual_gap_252'] = {'inputs': ['slv_060_accrual_gap_252'], 'func': slv_base_universe_d2_022_slv_060_accrual_gap_252}


def slv_base_universe_d2_023_slv_basefill_001(slv_basefill_001):
    return _base_universe_d2(slv_basefill_001, 23)
SLV_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['slv_base_universe_d2_023_slv_basefill_001'] = {'inputs': ['slv_basefill_001'], 'func': slv_base_universe_d2_023_slv_basefill_001}


def slv_base_universe_d2_024_slv_basefill_002(slv_basefill_002):
    return _base_universe_d2(slv_basefill_002, 24)
SLV_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['slv_base_universe_d2_024_slv_basefill_002'] = {'inputs': ['slv_basefill_002'], 'func': slv_base_universe_d2_024_slv_basefill_002}


def slv_base_universe_d2_025_slv_basefill_006(slv_basefill_006):
    return _base_universe_d2(slv_basefill_006, 25)
SLV_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['slv_base_universe_d2_025_slv_basefill_006'] = {'inputs': ['slv_basefill_006'], 'func': slv_base_universe_d2_025_slv_basefill_006}


def slv_base_universe_d2_026_slv_basefill_008(slv_basefill_008):
    return _base_universe_d2(slv_basefill_008, 26)
SLV_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['slv_base_universe_d2_026_slv_basefill_008'] = {'inputs': ['slv_basefill_008'], 'func': slv_base_universe_d2_026_slv_basefill_008}


def slv_base_universe_d2_027_slv_basefill_009(slv_basefill_009):
    return _base_universe_d2(slv_basefill_009, 27)
SLV_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['slv_base_universe_d2_027_slv_basefill_009'] = {'inputs': ['slv_basefill_009'], 'func': slv_base_universe_d2_027_slv_basefill_009}


def slv_base_universe_d2_028_slv_basefill_010(slv_basefill_010):
    return _base_universe_d2(slv_basefill_010, 28)
SLV_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['slv_base_universe_d2_028_slv_basefill_010'] = {'inputs': ['slv_basefill_010'], 'func': slv_base_universe_d2_028_slv_basefill_010}


def slv_base_universe_d2_029_slv_basefill_011(slv_basefill_011):
    return _base_universe_d2(slv_basefill_011, 29)
SLV_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['slv_base_universe_d2_029_slv_basefill_011'] = {'inputs': ['slv_basefill_011'], 'func': slv_base_universe_d2_029_slv_basefill_011}


def slv_base_universe_d2_030_slv_basefill_013(slv_basefill_013):
    return _base_universe_d2(slv_basefill_013, 30)
SLV_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['slv_base_universe_d2_030_slv_basefill_013'] = {'inputs': ['slv_basefill_013'], 'func': slv_base_universe_d2_030_slv_basefill_013}


def slv_base_universe_d2_031_slv_basefill_014(slv_basefill_014):
    return _base_universe_d2(slv_basefill_014, 31)
SLV_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['slv_base_universe_d2_031_slv_basefill_014'] = {'inputs': ['slv_basefill_014'], 'func': slv_base_universe_d2_031_slv_basefill_014}


def slv_base_universe_d2_032_slv_basefill_015(slv_basefill_015):
    return _base_universe_d2(slv_basefill_015, 32)
SLV_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['slv_base_universe_d2_032_slv_basefill_015'] = {'inputs': ['slv_basefill_015'], 'func': slv_base_universe_d2_032_slv_basefill_015}


def slv_base_universe_d2_033_slv_basefill_018(slv_basefill_018):
    return _base_universe_d2(slv_basefill_018, 33)
SLV_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['slv_base_universe_d2_033_slv_basefill_018'] = {'inputs': ['slv_basefill_018'], 'func': slv_base_universe_d2_033_slv_basefill_018}


def slv_base_universe_d2_034_slv_basefill_020(slv_basefill_020):
    return _base_universe_d2(slv_basefill_020, 34)
SLV_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['slv_base_universe_d2_034_slv_basefill_020'] = {'inputs': ['slv_basefill_020'], 'func': slv_base_universe_d2_034_slv_basefill_020}


def slv_base_universe_d2_035_slv_basefill_021(slv_basefill_021):
    return _base_universe_d2(slv_basefill_021, 35)
SLV_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['slv_base_universe_d2_035_slv_basefill_021'] = {'inputs': ['slv_basefill_021'], 'func': slv_base_universe_d2_035_slv_basefill_021}


def slv_base_universe_d2_036_slv_basefill_022(slv_basefill_022):
    return _base_universe_d2(slv_basefill_022, 36)
SLV_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['slv_base_universe_d2_036_slv_basefill_022'] = {'inputs': ['slv_basefill_022'], 'func': slv_base_universe_d2_036_slv_basefill_022}


def slv_base_universe_d2_037_slv_basefill_023(slv_basefill_023):
    return _base_universe_d2(slv_basefill_023, 37)
SLV_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['slv_base_universe_d2_037_slv_basefill_023'] = {'inputs': ['slv_basefill_023'], 'func': slv_base_universe_d2_037_slv_basefill_023}


def slv_base_universe_d2_038_slv_basefill_025(slv_basefill_025):
    return _base_universe_d2(slv_basefill_025, 38)
SLV_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['slv_base_universe_d2_038_slv_basefill_025'] = {'inputs': ['slv_basefill_025'], 'func': slv_base_universe_d2_038_slv_basefill_025}


def slv_base_universe_d2_039_slv_basefill_026(slv_basefill_026):
    return _base_universe_d2(slv_basefill_026, 39)
SLV_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['slv_base_universe_d2_039_slv_basefill_026'] = {'inputs': ['slv_basefill_026'], 'func': slv_base_universe_d2_039_slv_basefill_026}


def slv_base_universe_d2_040_slv_basefill_030(slv_basefill_030):
    return _base_universe_d2(slv_basefill_030, 40)
SLV_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['slv_base_universe_d2_040_slv_basefill_030'] = {'inputs': ['slv_basefill_030'], 'func': slv_base_universe_d2_040_slv_basefill_030}


def slv_base_universe_d2_041_slv_basefill_032(slv_basefill_032):
    return _base_universe_d2(slv_basefill_032, 41)
SLV_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['slv_base_universe_d2_041_slv_basefill_032'] = {'inputs': ['slv_basefill_032'], 'func': slv_base_universe_d2_041_slv_basefill_032}


def slv_base_universe_d2_042_slv_basefill_033(slv_basefill_033):
    return _base_universe_d2(slv_basefill_033, 42)
SLV_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['slv_base_universe_d2_042_slv_basefill_033'] = {'inputs': ['slv_basefill_033'], 'func': slv_base_universe_d2_042_slv_basefill_033}


def slv_base_universe_d2_043_slv_basefill_034(slv_basefill_034):
    return _base_universe_d2(slv_basefill_034, 43)
SLV_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['slv_base_universe_d2_043_slv_basefill_034'] = {'inputs': ['slv_basefill_034'], 'func': slv_base_universe_d2_043_slv_basefill_034}


def slv_base_universe_d2_044_slv_basefill_035(slv_basefill_035):
    return _base_universe_d2(slv_basefill_035, 44)
SLV_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['slv_base_universe_d2_044_slv_basefill_035'] = {'inputs': ['slv_basefill_035'], 'func': slv_base_universe_d2_044_slv_basefill_035}


def slv_base_universe_d2_045_slv_basefill_037(slv_basefill_037):
    return _base_universe_d2(slv_basefill_037, 45)
SLV_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['slv_base_universe_d2_045_slv_basefill_037'] = {'inputs': ['slv_basefill_037'], 'func': slv_base_universe_d2_045_slv_basefill_037}


def slv_base_universe_d2_046_slv_basefill_038(slv_basefill_038):
    return _base_universe_d2(slv_basefill_038, 46)
SLV_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['slv_base_universe_d2_046_slv_basefill_038'] = {'inputs': ['slv_basefill_038'], 'func': slv_base_universe_d2_046_slv_basefill_038}


def slv_base_universe_d2_047_slv_basefill_042(slv_basefill_042):
    return _base_universe_d2(slv_basefill_042, 47)
SLV_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['slv_base_universe_d2_047_slv_basefill_042'] = {'inputs': ['slv_basefill_042'], 'func': slv_base_universe_d2_047_slv_basefill_042}


def slv_base_universe_d2_048_slv_basefill_044(slv_basefill_044):
    return _base_universe_d2(slv_basefill_044, 48)
SLV_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['slv_base_universe_d2_048_slv_basefill_044'] = {'inputs': ['slv_basefill_044'], 'func': slv_base_universe_d2_048_slv_basefill_044}


def slv_base_universe_d2_049_slv_basefill_045(slv_basefill_045):
    return _base_universe_d2(slv_basefill_045, 49)
SLV_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['slv_base_universe_d2_049_slv_basefill_045'] = {'inputs': ['slv_basefill_045'], 'func': slv_base_universe_d2_049_slv_basefill_045}


def slv_base_universe_d2_050_slv_basefill_046(slv_basefill_046):
    return _base_universe_d2(slv_basefill_046, 50)
SLV_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['slv_base_universe_d2_050_slv_basefill_046'] = {'inputs': ['slv_basefill_046'], 'func': slv_base_universe_d2_050_slv_basefill_046}


def slv_base_universe_d2_051_slv_basefill_047(slv_basefill_047):
    return _base_universe_d2(slv_basefill_047, 51)
SLV_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['slv_base_universe_d2_051_slv_basefill_047'] = {'inputs': ['slv_basefill_047'], 'func': slv_base_universe_d2_051_slv_basefill_047}


def slv_base_universe_d2_052_slv_basefill_049(slv_basefill_049):
    return _base_universe_d2(slv_basefill_049, 52)
SLV_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['slv_base_universe_d2_052_slv_basefill_049'] = {'inputs': ['slv_basefill_049'], 'func': slv_base_universe_d2_052_slv_basefill_049}


def slv_base_universe_d2_053_slv_basefill_050(slv_basefill_050):
    return _base_universe_d2(slv_basefill_050, 53)
SLV_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['slv_base_universe_d2_053_slv_basefill_050'] = {'inputs': ['slv_basefill_050'], 'func': slv_base_universe_d2_053_slv_basefill_050}


def slv_base_universe_d2_054_slv_basefill_054(slv_basefill_054):
    return _base_universe_d2(slv_basefill_054, 54)
SLV_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['slv_base_universe_d2_054_slv_basefill_054'] = {'inputs': ['slv_basefill_054'], 'func': slv_base_universe_d2_054_slv_basefill_054}


def slv_base_universe_d2_055_slv_basefill_056(slv_basefill_056):
    return _base_universe_d2(slv_basefill_056, 55)
SLV_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['slv_base_universe_d2_055_slv_basefill_056'] = {'inputs': ['slv_basefill_056'], 'func': slv_base_universe_d2_055_slv_basefill_056}


def slv_base_universe_d2_056_slv_basefill_057(slv_basefill_057):
    return _base_universe_d2(slv_basefill_057, 56)
SLV_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['slv_base_universe_d2_056_slv_basefill_057'] = {'inputs': ['slv_basefill_057'], 'func': slv_base_universe_d2_056_slv_basefill_057}


def slv_base_universe_d2_057_slv_basefill_058(slv_basefill_058):
    return _base_universe_d2(slv_basefill_058, 57)
SLV_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['slv_base_universe_d2_057_slv_basefill_058'] = {'inputs': ['slv_basefill_058'], 'func': slv_base_universe_d2_057_slv_basefill_058}


def slv_base_universe_d2_058_slv_basefill_059(slv_basefill_059):
    return _base_universe_d2(slv_basefill_059, 58)
SLV_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['slv_base_universe_d2_058_slv_basefill_059'] = {'inputs': ['slv_basefill_059'], 'func': slv_base_universe_d2_058_slv_basefill_059}


def slv_base_universe_d2_059_slv_basefill_061(slv_basefill_061):
    return _base_universe_d2(slv_basefill_061, 59)
SLV_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['slv_base_universe_d2_059_slv_basefill_061'] = {'inputs': ['slv_basefill_061'], 'func': slv_base_universe_d2_059_slv_basefill_061}


def slv_base_universe_d2_060_slv_basefill_062(slv_basefill_062):
    return _base_universe_d2(slv_basefill_062, 60)
SLV_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['slv_base_universe_d2_060_slv_basefill_062'] = {'inputs': ['slv_basefill_062'], 'func': slv_base_universe_d2_060_slv_basefill_062}


def slv_base_universe_d2_061_slv_basefill_063(slv_basefill_063):
    return _base_universe_d2(slv_basefill_063, 61)
SLV_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['slv_base_universe_d2_061_slv_basefill_063'] = {'inputs': ['slv_basefill_063'], 'func': slv_base_universe_d2_061_slv_basefill_063}


def slv_base_universe_d2_062_slv_basefill_064(slv_basefill_064):
    return _base_universe_d2(slv_basefill_064, 62)
SLV_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['slv_base_universe_d2_062_slv_basefill_064'] = {'inputs': ['slv_basefill_064'], 'func': slv_base_universe_d2_062_slv_basefill_064}


def slv_base_universe_d2_063_slv_basefill_065(slv_basefill_065):
    return _base_universe_d2(slv_basefill_065, 63)
SLV_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['slv_base_universe_d2_063_slv_basefill_065'] = {'inputs': ['slv_basefill_065'], 'func': slv_base_universe_d2_063_slv_basefill_065}


def slv_base_universe_d2_064_slv_basefill_066(slv_basefill_066):
    return _base_universe_d2(slv_basefill_066, 64)
SLV_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['slv_base_universe_d2_064_slv_basefill_066'] = {'inputs': ['slv_basefill_066'], 'func': slv_base_universe_d2_064_slv_basefill_066}


def slv_base_universe_d2_065_slv_basefill_067(slv_basefill_067):
    return _base_universe_d2(slv_basefill_067, 65)
SLV_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['slv_base_universe_d2_065_slv_basefill_067'] = {'inputs': ['slv_basefill_067'], 'func': slv_base_universe_d2_065_slv_basefill_067}


def slv_base_universe_d2_066_slv_basefill_068(slv_basefill_068):
    return _base_universe_d2(slv_basefill_068, 66)
SLV_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['slv_base_universe_d2_066_slv_basefill_068'] = {'inputs': ['slv_basefill_068'], 'func': slv_base_universe_d2_066_slv_basefill_068}


def slv_base_universe_d2_067_slv_basefill_069(slv_basefill_069):
    return _base_universe_d2(slv_basefill_069, 67)
SLV_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['slv_base_universe_d2_067_slv_basefill_069'] = {'inputs': ['slv_basefill_069'], 'func': slv_base_universe_d2_067_slv_basefill_069}


def slv_base_universe_d2_068_slv_basefill_070(slv_basefill_070):
    return _base_universe_d2(slv_basefill_070, 68)
SLV_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['slv_base_universe_d2_068_slv_basefill_070'] = {'inputs': ['slv_basefill_070'], 'func': slv_base_universe_d2_068_slv_basefill_070}


def slv_base_universe_d2_069_slv_basefill_071(slv_basefill_071):
    return _base_universe_d2(slv_basefill_071, 69)
SLV_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['slv_base_universe_d2_069_slv_basefill_071'] = {'inputs': ['slv_basefill_071'], 'func': slv_base_universe_d2_069_slv_basefill_071}


def slv_base_universe_d2_070_slv_basefill_072(slv_basefill_072):
    return _base_universe_d2(slv_basefill_072, 70)
SLV_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['slv_base_universe_d2_070_slv_basefill_072'] = {'inputs': ['slv_basefill_072'], 'func': slv_base_universe_d2_070_slv_basefill_072}


def slv_base_universe_d2_071_slv_basefill_073(slv_basefill_073):
    return _base_universe_d2(slv_basefill_073, 71)
SLV_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['slv_base_universe_d2_071_slv_basefill_073'] = {'inputs': ['slv_basefill_073'], 'func': slv_base_universe_d2_071_slv_basefill_073}


def slv_base_universe_d2_072_slv_basefill_074(slv_basefill_074):
    return _base_universe_d2(slv_basefill_074, 72)
SLV_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['slv_base_universe_d2_072_slv_basefill_074'] = {'inputs': ['slv_basefill_074'], 'func': slv_base_universe_d2_072_slv_basefill_074}


def slv_base_universe_d2_073_slv_basefill_075(slv_basefill_075):
    return _base_universe_d2(slv_basefill_075, 73)
SLV_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['slv_base_universe_d2_073_slv_basefill_075'] = {'inputs': ['slv_basefill_075'], 'func': slv_base_universe_d2_073_slv_basefill_075}
