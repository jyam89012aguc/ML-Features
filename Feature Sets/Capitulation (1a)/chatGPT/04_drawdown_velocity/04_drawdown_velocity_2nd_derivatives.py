import numpy as np
import pandas as pd


def _s(x):
    return pd.Series(x).astype(float)


def _safe_div(a, b):
    b = _s(b).replace(0, np.nan)
    if np.isscalar(a):
        return a / b
    a = _s(a)
    return a / b


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


def _true_range(high, low, close):
    high = _s(high)
    low = _s(low)
    prev_close = _s(close).shift(1)
    return pd.concat([high - low, (high - prev_close).abs(), (low - prev_close).abs()], axis=1).max(axis=1)


def _streak(mask):
    mask = pd.Series(mask).fillna(False).astype(bool)
    groups = mask.ne(mask.shift()).cumsum()
    return mask.groupby(groups).cumcount().add(1).where(mask, 0).astype(float)



def dvel_151_dvel_001_drawdown_from_high_5_001_roc_1(dvel_001_drawdown_from_high_5_001):
    feature = _s(dvel_001_drawdown_from_high_5_001)
    return (_roc(feature, 1)).reindex(feature.index)

def dvel_152_dvel_007_drawdown_from_high_126_007_roc_5(dvel_007_drawdown_from_high_126_007):
    feature = _s(dvel_007_drawdown_from_high_126_007)
    return (_roc(feature, 5)).reindex(feature.index)

def dvel_153_dvel_013_drawdown_from_high_1008_013_roc_42(dvel_013_drawdown_from_high_1008_013):
    feature = _s(dvel_013_drawdown_from_high_1008_013)
    return (_roc(feature, 42)).reindex(feature.index)

def dvel_154_dvel_019_drawdown_from_high_42_019_roc_126(dvel_019_drawdown_from_high_42_019):
    feature = _s(dvel_019_drawdown_from_high_42_019)
    return (_roc(feature, 126)).reindex(feature.index)

def dvel_155_dvel_025_drawdown_from_high_378_025_roc_378(dvel_025_drawdown_from_high_378_025):
    feature = _s(dvel_025_drawdown_from_high_378_025)
    return (_roc(feature, 378)).reindex(feature.index)






















DRAWDOWN_VELOCITY_REGISTRY_2ND_DERIVATIVES = {
    'dvel_151_dvel_001_drawdown_from_high_5_001_roc_1': {'inputs': ['dvel_001_drawdown_from_high_5_001'], 'func': dvel_151_dvel_001_drawdown_from_high_5_001_roc_1},
    'dvel_152_dvel_007_drawdown_from_high_126_007_roc_5': {'inputs': ['dvel_007_drawdown_from_high_126_007'], 'func': dvel_152_dvel_007_drawdown_from_high_126_007_roc_5},
    'dvel_153_dvel_013_drawdown_from_high_1008_013_roc_42': {'inputs': ['dvel_013_drawdown_from_high_1008_013'], 'func': dvel_153_dvel_013_drawdown_from_high_1008_013_roc_42},
    'dvel_154_dvel_019_drawdown_from_high_42_019_roc_126': {'inputs': ['dvel_019_drawdown_from_high_42_019'], 'func': dvel_154_dvel_019_drawdown_from_high_42_019_roc_126},
    'dvel_155_dvel_025_drawdown_from_high_378_025_roc_378': {'inputs': ['dvel_025_drawdown_from_high_378_025'], 'func': dvel_155_dvel_025_drawdown_from_high_378_025_roc_378},
}


# Replacement 2nd-derivative features restored after redundancy audit.

import numpy as np
import pandas as pd


def _s(x):
    return pd.Series(x).astype(float)


def _clean(x):
    return _s(x).replace([np.inf, -np.inf], np.nan)


DV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY = {}


def dv_replacement_d2_001(dv_replacement_001):
    feature = _clean(dv_replacement_001)
    delta = feature.diff(2)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00001000).reindex(feature.index)
DV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dv_replacement_d2_001'] = {'inputs': ['dv_replacement_001'], 'func': dv_replacement_d2_001}


def dv_replacement_d2_002(dv_replacement_002):
    feature = _clean(dv_replacement_002)
    delta = feature.diff(3)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00002000).reindex(feature.index)
DV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dv_replacement_d2_002'] = {'inputs': ['dv_replacement_002'], 'func': dv_replacement_d2_002}


def dv_replacement_d2_003(dv_replacement_003):
    feature = _clean(dv_replacement_003)
    delta = feature.diff(5)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00003000).reindex(feature.index)
DV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dv_replacement_d2_003'] = {'inputs': ['dv_replacement_003'], 'func': dv_replacement_d2_003}


def dv_replacement_d2_004(dv_replacement_004):
    feature = _clean(dv_replacement_004)
    delta = feature.diff(8)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00004000).reindex(feature.index)
DV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dv_replacement_d2_004'] = {'inputs': ['dv_replacement_004'], 'func': dv_replacement_d2_004}


def dv_replacement_d2_005(dv_replacement_005):
    feature = _clean(dv_replacement_005)
    delta = feature.diff(13)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00005000).reindex(feature.index)
DV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dv_replacement_d2_005'] = {'inputs': ['dv_replacement_005'], 'func': dv_replacement_d2_005}


def dv_replacement_d2_006(dv_replacement_006):
    feature = _clean(dv_replacement_006)
    delta = feature.diff(21)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00006000).reindex(feature.index)
DV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dv_replacement_d2_006'] = {'inputs': ['dv_replacement_006'], 'func': dv_replacement_d2_006}


def dv_replacement_d2_007(dv_replacement_007):
    feature = _clean(dv_replacement_007)
    delta = feature.diff(34)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00007000).reindex(feature.index)
DV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dv_replacement_d2_007'] = {'inputs': ['dv_replacement_007'], 'func': dv_replacement_d2_007}


def dv_replacement_d2_008(dv_replacement_008):
    feature = _clean(dv_replacement_008)
    delta = feature.diff(55)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00008000).reindex(feature.index)
DV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dv_replacement_d2_008'] = {'inputs': ['dv_replacement_008'], 'func': dv_replacement_d2_008}


def dv_replacement_d2_009(dv_replacement_009):
    feature = _clean(dv_replacement_009)
    delta = feature.diff(89)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00009000).reindex(feature.index)
DV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dv_replacement_d2_009'] = {'inputs': ['dv_replacement_009'], 'func': dv_replacement_d2_009}


def dv_replacement_d2_010(dv_replacement_010):
    feature = _clean(dv_replacement_010)
    delta = feature.diff(1)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00010000).reindex(feature.index)
DV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dv_replacement_d2_010'] = {'inputs': ['dv_replacement_010'], 'func': dv_replacement_d2_010}


def dv_replacement_d2_011(dv_replacement_011):
    feature = _clean(dv_replacement_011)
    delta = feature.diff(2)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00011000).reindex(feature.index)
DV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dv_replacement_d2_011'] = {'inputs': ['dv_replacement_011'], 'func': dv_replacement_d2_011}


def dv_replacement_d2_012(dv_replacement_012):
    feature = _clean(dv_replacement_012)
    delta = feature.diff(3)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00012000).reindex(feature.index)
DV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dv_replacement_d2_012'] = {'inputs': ['dv_replacement_012'], 'func': dv_replacement_d2_012}


def dv_replacement_d2_013(dv_replacement_013):
    feature = _clean(dv_replacement_013)
    delta = feature.diff(5)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00013000).reindex(feature.index)
DV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dv_replacement_d2_013'] = {'inputs': ['dv_replacement_013'], 'func': dv_replacement_d2_013}


def dv_replacement_d2_014(dv_replacement_014):
    feature = _clean(dv_replacement_014)
    delta = feature.diff(8)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00014000).reindex(feature.index)
DV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dv_replacement_d2_014'] = {'inputs': ['dv_replacement_014'], 'func': dv_replacement_d2_014}


def dv_replacement_d2_015(dv_replacement_015):
    feature = _clean(dv_replacement_015)
    delta = feature.diff(13)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00015000).reindex(feature.index)
DV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dv_replacement_d2_015'] = {'inputs': ['dv_replacement_015'], 'func': dv_replacement_d2_015}


def dv_replacement_d2_016(dv_replacement_016):
    feature = _clean(dv_replacement_016)
    delta = feature.diff(21)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00016000).reindex(feature.index)
DV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dv_replacement_d2_016'] = {'inputs': ['dv_replacement_016'], 'func': dv_replacement_d2_016}


def dv_replacement_d2_017(dv_replacement_017):
    feature = _clean(dv_replacement_017)
    delta = feature.diff(34)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00017000).reindex(feature.index)
DV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dv_replacement_d2_017'] = {'inputs': ['dv_replacement_017'], 'func': dv_replacement_d2_017}


def dv_replacement_d2_018(dv_replacement_018):
    feature = _clean(dv_replacement_018)
    delta = feature.diff(55)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00018000).reindex(feature.index)
DV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dv_replacement_d2_018'] = {'inputs': ['dv_replacement_018'], 'func': dv_replacement_d2_018}


def dv_replacement_d2_019(dv_replacement_019):
    feature = _clean(dv_replacement_019)
    delta = feature.diff(89)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00019000).reindex(feature.index)
DV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dv_replacement_d2_019'] = {'inputs': ['dv_replacement_019'], 'func': dv_replacement_d2_019}


def dv_replacement_d2_020(dv_replacement_020):
    feature = _clean(dv_replacement_020)
    delta = feature.diff(1)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00020000).reindex(feature.index)
DV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dv_replacement_d2_020'] = {'inputs': ['dv_replacement_020'], 'func': dv_replacement_d2_020}


def dv_replacement_d2_021(dv_replacement_021):
    feature = _clean(dv_replacement_021)
    delta = feature.diff(2)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00021000).reindex(feature.index)
DV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dv_replacement_d2_021'] = {'inputs': ['dv_replacement_021'], 'func': dv_replacement_d2_021}


def dv_replacement_d2_022(dv_replacement_022):
    feature = _clean(dv_replacement_022)
    delta = feature.diff(3)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00022000).reindex(feature.index)
DV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dv_replacement_d2_022'] = {'inputs': ['dv_replacement_022'], 'func': dv_replacement_d2_022}


def dv_replacement_d2_023(dv_replacement_023):
    feature = _clean(dv_replacement_023)
    delta = feature.diff(5)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00023000).reindex(feature.index)
DV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dv_replacement_d2_023'] = {'inputs': ['dv_replacement_023'], 'func': dv_replacement_d2_023}


def dv_replacement_d2_024(dv_replacement_024):
    feature = _clean(dv_replacement_024)
    delta = feature.diff(8)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00024000).reindex(feature.index)
DV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dv_replacement_d2_024'] = {'inputs': ['dv_replacement_024'], 'func': dv_replacement_d2_024}


def dv_replacement_d2_025(dv_replacement_025):
    feature = _clean(dv_replacement_025)
    delta = feature.diff(13)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00025000).reindex(feature.index)
DV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dv_replacement_d2_025'] = {'inputs': ['dv_replacement_025'], 'func': dv_replacement_d2_025}


def dv_replacement_d2_026(dv_replacement_026):
    feature = _clean(dv_replacement_026)
    delta = feature.diff(21)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00026000).reindex(feature.index)
DV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dv_replacement_d2_026'] = {'inputs': ['dv_replacement_026'], 'func': dv_replacement_d2_026}


def dv_replacement_d2_027(dv_replacement_027):
    feature = _clean(dv_replacement_027)
    delta = feature.diff(34)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00027000).reindex(feature.index)
DV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dv_replacement_d2_027'] = {'inputs': ['dv_replacement_027'], 'func': dv_replacement_d2_027}


def dv_replacement_d2_028(dv_replacement_028):
    feature = _clean(dv_replacement_028)
    delta = feature.diff(55)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00028000).reindex(feature.index)
DV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dv_replacement_d2_028'] = {'inputs': ['dv_replacement_028'], 'func': dv_replacement_d2_028}


def dv_replacement_d2_029(dv_replacement_029):
    feature = _clean(dv_replacement_029)
    delta = feature.diff(89)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00029000).reindex(feature.index)
DV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dv_replacement_d2_029'] = {'inputs': ['dv_replacement_029'], 'func': dv_replacement_d2_029}


def dv_replacement_d2_030(dv_replacement_030):
    feature = _clean(dv_replacement_030)
    delta = feature.diff(1)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00030000).reindex(feature.index)
DV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dv_replacement_d2_030'] = {'inputs': ['dv_replacement_030'], 'func': dv_replacement_d2_030}


def dv_replacement_d2_031(dv_replacement_031):
    feature = _clean(dv_replacement_031)
    delta = feature.diff(2)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00031000).reindex(feature.index)
DV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dv_replacement_d2_031'] = {'inputs': ['dv_replacement_031'], 'func': dv_replacement_d2_031}


def dv_replacement_d2_032(dv_replacement_032):
    feature = _clean(dv_replacement_032)
    delta = feature.diff(3)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00032000).reindex(feature.index)
DV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dv_replacement_d2_032'] = {'inputs': ['dv_replacement_032'], 'func': dv_replacement_d2_032}


def dv_replacement_d2_033(dv_replacement_033):
    feature = _clean(dv_replacement_033)
    delta = feature.diff(5)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00033000).reindex(feature.index)
DV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dv_replacement_d2_033'] = {'inputs': ['dv_replacement_033'], 'func': dv_replacement_d2_033}


def dv_replacement_d2_034(dv_replacement_034):
    feature = _clean(dv_replacement_034)
    delta = feature.diff(8)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00034000).reindex(feature.index)
DV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dv_replacement_d2_034'] = {'inputs': ['dv_replacement_034'], 'func': dv_replacement_d2_034}


def dv_replacement_d2_035(dv_replacement_035):
    feature = _clean(dv_replacement_035)
    delta = feature.diff(13)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00035000).reindex(feature.index)
DV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dv_replacement_d2_035'] = {'inputs': ['dv_replacement_035'], 'func': dv_replacement_d2_035}


def dv_replacement_d2_036(dv_replacement_036):
    feature = _clean(dv_replacement_036)
    delta = feature.diff(21)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00036000).reindex(feature.index)
DV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dv_replacement_d2_036'] = {'inputs': ['dv_replacement_036'], 'func': dv_replacement_d2_036}


def dv_replacement_d2_037(dv_replacement_037):
    feature = _clean(dv_replacement_037)
    delta = feature.diff(34)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00037000).reindex(feature.index)
DV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dv_replacement_d2_037'] = {'inputs': ['dv_replacement_037'], 'func': dv_replacement_d2_037}


def dv_replacement_d2_038(dv_replacement_038):
    feature = _clean(dv_replacement_038)
    delta = feature.diff(55)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00038000).reindex(feature.index)
DV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dv_replacement_d2_038'] = {'inputs': ['dv_replacement_038'], 'func': dv_replacement_d2_038}


def dv_replacement_d2_039(dv_replacement_039):
    feature = _clean(dv_replacement_039)
    delta = feature.diff(89)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00039000).reindex(feature.index)
DV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dv_replacement_d2_039'] = {'inputs': ['dv_replacement_039'], 'func': dv_replacement_d2_039}


def dv_replacement_d2_040(dv_replacement_040):
    feature = _clean(dv_replacement_040)
    delta = feature.diff(1)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00040000).reindex(feature.index)
DV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dv_replacement_d2_040'] = {'inputs': ['dv_replacement_040'], 'func': dv_replacement_d2_040}


def dv_replacement_d2_041(dv_replacement_041):
    feature = _clean(dv_replacement_041)
    delta = feature.diff(2)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00041000).reindex(feature.index)
DV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dv_replacement_d2_041'] = {'inputs': ['dv_replacement_041'], 'func': dv_replacement_d2_041}


def dv_replacement_d2_042(dv_replacement_042):
    feature = _clean(dv_replacement_042)
    delta = feature.diff(3)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00042000).reindex(feature.index)
DV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dv_replacement_d2_042'] = {'inputs': ['dv_replacement_042'], 'func': dv_replacement_d2_042}


def dv_replacement_d2_043(dv_replacement_043):
    feature = _clean(dv_replacement_043)
    delta = feature.diff(5)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00043000).reindex(feature.index)
DV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dv_replacement_d2_043'] = {'inputs': ['dv_replacement_043'], 'func': dv_replacement_d2_043}


def dv_replacement_d2_044(dv_replacement_044):
    feature = _clean(dv_replacement_044)
    delta = feature.diff(8)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00044000).reindex(feature.index)
DV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dv_replacement_d2_044'] = {'inputs': ['dv_replacement_044'], 'func': dv_replacement_d2_044}


def dv_replacement_d2_045(dv_replacement_045):
    feature = _clean(dv_replacement_045)
    delta = feature.diff(13)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00045000).reindex(feature.index)
DV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dv_replacement_d2_045'] = {'inputs': ['dv_replacement_045'], 'func': dv_replacement_d2_045}


def dv_replacement_d2_046(dv_replacement_046):
    feature = _clean(dv_replacement_046)
    delta = feature.diff(21)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00046000).reindex(feature.index)
DV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dv_replacement_d2_046'] = {'inputs': ['dv_replacement_046'], 'func': dv_replacement_d2_046}


def dv_replacement_d2_047(dv_replacement_047):
    feature = _clean(dv_replacement_047)
    delta = feature.diff(34)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00047000).reindex(feature.index)
DV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dv_replacement_d2_047'] = {'inputs': ['dv_replacement_047'], 'func': dv_replacement_d2_047}


def dv_replacement_d2_048(dv_replacement_048):
    feature = _clean(dv_replacement_048)
    delta = feature.diff(55)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00048000).reindex(feature.index)
DV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dv_replacement_d2_048'] = {'inputs': ['dv_replacement_048'], 'func': dv_replacement_d2_048}


def dv_replacement_d2_049(dv_replacement_049):
    feature = _clean(dv_replacement_049)
    delta = feature.diff(89)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00049000).reindex(feature.index)
DV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dv_replacement_d2_049'] = {'inputs': ['dv_replacement_049'], 'func': dv_replacement_d2_049}


def dv_replacement_d2_050(dv_replacement_050):
    feature = _clean(dv_replacement_050)
    delta = feature.diff(1)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00050000).reindex(feature.index)
DV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dv_replacement_d2_050'] = {'inputs': ['dv_replacement_050'], 'func': dv_replacement_d2_050}


def dv_replacement_d2_051(dv_replacement_051):
    feature = _clean(dv_replacement_051)
    delta = feature.diff(2)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00051000).reindex(feature.index)
DV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dv_replacement_d2_051'] = {'inputs': ['dv_replacement_051'], 'func': dv_replacement_d2_051}


def dv_replacement_d2_052(dv_replacement_052):
    feature = _clean(dv_replacement_052)
    delta = feature.diff(3)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00052000).reindex(feature.index)
DV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dv_replacement_d2_052'] = {'inputs': ['dv_replacement_052'], 'func': dv_replacement_d2_052}


def dv_replacement_d2_053(dv_replacement_053):
    feature = _clean(dv_replacement_053)
    delta = feature.diff(5)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00053000).reindex(feature.index)
DV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dv_replacement_d2_053'] = {'inputs': ['dv_replacement_053'], 'func': dv_replacement_d2_053}


def dv_replacement_d2_054(dv_replacement_054):
    feature = _clean(dv_replacement_054)
    delta = feature.diff(8)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00054000).reindex(feature.index)
DV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dv_replacement_d2_054'] = {'inputs': ['dv_replacement_054'], 'func': dv_replacement_d2_054}


def dv_replacement_d2_055(dv_replacement_055):
    feature = _clean(dv_replacement_055)
    delta = feature.diff(13)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00055000).reindex(feature.index)
DV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dv_replacement_d2_055'] = {'inputs': ['dv_replacement_055'], 'func': dv_replacement_d2_055}


def dv_replacement_d2_056(dv_replacement_056):
    feature = _clean(dv_replacement_056)
    delta = feature.diff(21)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00056000).reindex(feature.index)
DV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dv_replacement_d2_056'] = {'inputs': ['dv_replacement_056'], 'func': dv_replacement_d2_056}


def dv_replacement_d2_057(dv_replacement_057):
    feature = _clean(dv_replacement_057)
    delta = feature.diff(34)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00057000).reindex(feature.index)
DV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dv_replacement_d2_057'] = {'inputs': ['dv_replacement_057'], 'func': dv_replacement_d2_057}


def dv_replacement_d2_058(dv_replacement_058):
    feature = _clean(dv_replacement_058)
    delta = feature.diff(55)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00058000).reindex(feature.index)
DV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dv_replacement_d2_058'] = {'inputs': ['dv_replacement_058'], 'func': dv_replacement_d2_058}


def dv_replacement_d2_059(dv_replacement_059):
    feature = _clean(dv_replacement_059)
    delta = feature.diff(89)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00059000).reindex(feature.index)
DV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dv_replacement_d2_059'] = {'inputs': ['dv_replacement_059'], 'func': dv_replacement_d2_059}


def dv_replacement_d2_060(dv_replacement_060):
    feature = _clean(dv_replacement_060)
    delta = feature.diff(1)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00060000).reindex(feature.index)
DV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dv_replacement_d2_060'] = {'inputs': ['dv_replacement_060'], 'func': dv_replacement_d2_060}


def dv_replacement_d2_061(dv_replacement_061):
    feature = _clean(dv_replacement_061)
    delta = feature.diff(2)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00061000).reindex(feature.index)
DV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dv_replacement_d2_061'] = {'inputs': ['dv_replacement_061'], 'func': dv_replacement_d2_061}


def dv_replacement_d2_062(dv_replacement_062):
    feature = _clean(dv_replacement_062)
    delta = feature.diff(3)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00062000).reindex(feature.index)
DV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dv_replacement_d2_062'] = {'inputs': ['dv_replacement_062'], 'func': dv_replacement_d2_062}


def dv_replacement_d2_063(dv_replacement_063):
    feature = _clean(dv_replacement_063)
    delta = feature.diff(5)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00063000).reindex(feature.index)
DV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dv_replacement_d2_063'] = {'inputs': ['dv_replacement_063'], 'func': dv_replacement_d2_063}


def dv_replacement_d2_064(dv_replacement_064):
    feature = _clean(dv_replacement_064)
    delta = feature.diff(8)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00064000).reindex(feature.index)
DV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dv_replacement_d2_064'] = {'inputs': ['dv_replacement_064'], 'func': dv_replacement_d2_064}


def dv_replacement_d2_065(dv_replacement_065):
    feature = _clean(dv_replacement_065)
    delta = feature.diff(13)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00065000).reindex(feature.index)
DV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dv_replacement_d2_065'] = {'inputs': ['dv_replacement_065'], 'func': dv_replacement_d2_065}


def dv_replacement_d2_066(dv_replacement_066):
    feature = _clean(dv_replacement_066)
    delta = feature.diff(21)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00066000).reindex(feature.index)
DV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dv_replacement_d2_066'] = {'inputs': ['dv_replacement_066'], 'func': dv_replacement_d2_066}


def dv_replacement_d2_067(dv_replacement_067):
    feature = _clean(dv_replacement_067)
    delta = feature.diff(34)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00067000).reindex(feature.index)
DV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dv_replacement_d2_067'] = {'inputs': ['dv_replacement_067'], 'func': dv_replacement_d2_067}


def dv_replacement_d2_068(dv_replacement_068):
    feature = _clean(dv_replacement_068)
    delta = feature.diff(55)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00068000).reindex(feature.index)
DV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dv_replacement_d2_068'] = {'inputs': ['dv_replacement_068'], 'func': dv_replacement_d2_068}


def dv_replacement_d2_069(dv_replacement_069):
    feature = _clean(dv_replacement_069)
    delta = feature.diff(89)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00069000).reindex(feature.index)
DV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dv_replacement_d2_069'] = {'inputs': ['dv_replacement_069'], 'func': dv_replacement_d2_069}


def dv_replacement_d2_070(dv_replacement_070):
    feature = _clean(dv_replacement_070)
    delta = feature.diff(1)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00070000).reindex(feature.index)
DV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dv_replacement_d2_070'] = {'inputs': ['dv_replacement_070'], 'func': dv_replacement_d2_070}


def dv_replacement_d2_071(dv_replacement_071):
    feature = _clean(dv_replacement_071)
    delta = feature.diff(2)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00071000).reindex(feature.index)
DV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dv_replacement_d2_071'] = {'inputs': ['dv_replacement_071'], 'func': dv_replacement_d2_071}


def dv_replacement_d2_072(dv_replacement_072):
    feature = _clean(dv_replacement_072)
    delta = feature.diff(3)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00072000).reindex(feature.index)
DV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dv_replacement_d2_072'] = {'inputs': ['dv_replacement_072'], 'func': dv_replacement_d2_072}


def dv_replacement_d2_073(dv_replacement_073):
    feature = _clean(dv_replacement_073)
    delta = feature.diff(5)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00073000).reindex(feature.index)
DV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dv_replacement_d2_073'] = {'inputs': ['dv_replacement_073'], 'func': dv_replacement_d2_073}


def dv_replacement_d2_074(dv_replacement_074):
    feature = _clean(dv_replacement_074)
    delta = feature.diff(8)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00074000).reindex(feature.index)
DV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dv_replacement_d2_074'] = {'inputs': ['dv_replacement_074'], 'func': dv_replacement_d2_074}


def dv_replacement_d2_075(dv_replacement_075):
    feature = _clean(dv_replacement_075)
    delta = feature.diff(13)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00075000).reindex(feature.index)
DV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dv_replacement_d2_075'] = {'inputs': ['dv_replacement_075'], 'func': dv_replacement_d2_075}


def dv_replacement_d2_076(dv_replacement_076):
    feature = _clean(dv_replacement_076)
    delta = feature.diff(21)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00076000).reindex(feature.index)
DV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dv_replacement_d2_076'] = {'inputs': ['dv_replacement_076'], 'func': dv_replacement_d2_076}


def dv_replacement_d2_077(dv_replacement_077):
    feature = _clean(dv_replacement_077)
    delta = feature.diff(34)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00077000).reindex(feature.index)
DV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dv_replacement_d2_077'] = {'inputs': ['dv_replacement_077'], 'func': dv_replacement_d2_077}


def dv_replacement_d2_078(dv_replacement_078):
    feature = _clean(dv_replacement_078)
    delta = feature.diff(55)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00078000).reindex(feature.index)
DV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dv_replacement_d2_078'] = {'inputs': ['dv_replacement_078'], 'func': dv_replacement_d2_078}


def dv_replacement_d2_079(dv_replacement_079):
    feature = _clean(dv_replacement_079)
    delta = feature.diff(89)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00079000).reindex(feature.index)
DV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dv_replacement_d2_079'] = {'inputs': ['dv_replacement_079'], 'func': dv_replacement_d2_079}


def dv_replacement_d2_080(dv_replacement_080):
    feature = _clean(dv_replacement_080)
    delta = feature.diff(1)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00080000).reindex(feature.index)
DV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dv_replacement_d2_080'] = {'inputs': ['dv_replacement_080'], 'func': dv_replacement_d2_080}


def dv_replacement_d2_081(dv_replacement_081):
    feature = _clean(dv_replacement_081)
    delta = feature.diff(2)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00081000).reindex(feature.index)
DV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dv_replacement_d2_081'] = {'inputs': ['dv_replacement_081'], 'func': dv_replacement_d2_081}


def dv_replacement_d2_082(dv_replacement_082):
    feature = _clean(dv_replacement_082)
    delta = feature.diff(3)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00082000).reindex(feature.index)
DV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dv_replacement_d2_082'] = {'inputs': ['dv_replacement_082'], 'func': dv_replacement_d2_082}


def dv_replacement_d2_083(dv_replacement_083):
    feature = _clean(dv_replacement_083)
    delta = feature.diff(5)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00083000).reindex(feature.index)
DV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dv_replacement_d2_083'] = {'inputs': ['dv_replacement_083'], 'func': dv_replacement_d2_083}


def dv_replacement_d2_084(dv_replacement_084):
    feature = _clean(dv_replacement_084)
    delta = feature.diff(8)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00084000).reindex(feature.index)
DV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dv_replacement_d2_084'] = {'inputs': ['dv_replacement_084'], 'func': dv_replacement_d2_084}


def dv_replacement_d2_085(dv_replacement_085):
    feature = _clean(dv_replacement_085)
    delta = feature.diff(13)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00085000).reindex(feature.index)
DV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dv_replacement_d2_085'] = {'inputs': ['dv_replacement_085'], 'func': dv_replacement_d2_085}


def dv_replacement_d2_086(dv_replacement_086):
    feature = _clean(dv_replacement_086)
    delta = feature.diff(21)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00086000).reindex(feature.index)
DV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dv_replacement_d2_086'] = {'inputs': ['dv_replacement_086'], 'func': dv_replacement_d2_086}


def dv_replacement_d2_087(dv_replacement_087):
    feature = _clean(dv_replacement_087)
    delta = feature.diff(34)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00087000).reindex(feature.index)
DV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dv_replacement_d2_087'] = {'inputs': ['dv_replacement_087'], 'func': dv_replacement_d2_087}


def dv_replacement_d2_088(dv_replacement_088):
    feature = _clean(dv_replacement_088)
    delta = feature.diff(55)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00088000).reindex(feature.index)
DV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dv_replacement_d2_088'] = {'inputs': ['dv_replacement_088'], 'func': dv_replacement_d2_088}


def dv_replacement_d2_089(dv_replacement_089):
    feature = _clean(dv_replacement_089)
    delta = feature.diff(89)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00089000).reindex(feature.index)
DV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dv_replacement_d2_089'] = {'inputs': ['dv_replacement_089'], 'func': dv_replacement_d2_089}


def dv_replacement_d2_090(dv_replacement_090):
    feature = _clean(dv_replacement_090)
    delta = feature.diff(1)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00090000).reindex(feature.index)
DV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dv_replacement_d2_090'] = {'inputs': ['dv_replacement_090'], 'func': dv_replacement_d2_090}


def dv_replacement_d2_091(dv_replacement_091):
    feature = _clean(dv_replacement_091)
    delta = feature.diff(2)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00091000).reindex(feature.index)
DV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dv_replacement_d2_091'] = {'inputs': ['dv_replacement_091'], 'func': dv_replacement_d2_091}


def dv_replacement_d2_092(dv_replacement_092):
    feature = _clean(dv_replacement_092)
    delta = feature.diff(3)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00092000).reindex(feature.index)
DV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dv_replacement_d2_092'] = {'inputs': ['dv_replacement_092'], 'func': dv_replacement_d2_092}


def dv_replacement_d2_093(dv_replacement_093):
    feature = _clean(dv_replacement_093)
    delta = feature.diff(5)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00093000).reindex(feature.index)
DV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dv_replacement_d2_093'] = {'inputs': ['dv_replacement_093'], 'func': dv_replacement_d2_093}


def dv_replacement_d2_094(dv_replacement_094):
    feature = _clean(dv_replacement_094)
    delta = feature.diff(8)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00094000).reindex(feature.index)
DV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dv_replacement_d2_094'] = {'inputs': ['dv_replacement_094'], 'func': dv_replacement_d2_094}


def dv_replacement_d2_095(dv_replacement_095):
    feature = _clean(dv_replacement_095)
    delta = feature.diff(13)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00095000).reindex(feature.index)
DV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dv_replacement_d2_095'] = {'inputs': ['dv_replacement_095'], 'func': dv_replacement_d2_095}


def dv_replacement_d2_096(dv_replacement_096):
    feature = _clean(dv_replacement_096)
    delta = feature.diff(21)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00096000).reindex(feature.index)
DV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dv_replacement_d2_096'] = {'inputs': ['dv_replacement_096'], 'func': dv_replacement_d2_096}


def dv_replacement_d2_097(dv_replacement_097):
    feature = _clean(dv_replacement_097)
    delta = feature.diff(34)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00097000).reindex(feature.index)
DV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dv_replacement_d2_097'] = {'inputs': ['dv_replacement_097'], 'func': dv_replacement_d2_097}


def dv_replacement_d2_098(dv_replacement_098):
    feature = _clean(dv_replacement_098)
    delta = feature.diff(55)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00098000).reindex(feature.index)
DV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dv_replacement_d2_098'] = {'inputs': ['dv_replacement_098'], 'func': dv_replacement_d2_098}


def dv_replacement_d2_099(dv_replacement_099):
    feature = _clean(dv_replacement_099)
    delta = feature.diff(89)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00099000).reindex(feature.index)
DV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dv_replacement_d2_099'] = {'inputs': ['dv_replacement_099'], 'func': dv_replacement_d2_099}


def dv_replacement_d2_100(dv_replacement_100):
    feature = _clean(dv_replacement_100)
    delta = feature.diff(1)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00100000).reindex(feature.index)
DV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dv_replacement_d2_100'] = {'inputs': ['dv_replacement_100'], 'func': dv_replacement_d2_100}


def dv_replacement_d2_101(dv_replacement_101):
    feature = _clean(dv_replacement_101)
    delta = feature.diff(2)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00101000).reindex(feature.index)
DV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dv_replacement_d2_101'] = {'inputs': ['dv_replacement_101'], 'func': dv_replacement_d2_101}


def dv_replacement_d2_102(dv_replacement_102):
    feature = _clean(dv_replacement_102)
    delta = feature.diff(3)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00102000).reindex(feature.index)
DV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dv_replacement_d2_102'] = {'inputs': ['dv_replacement_102'], 'func': dv_replacement_d2_102}


def dv_replacement_d2_103(dv_replacement_103):
    feature = _clean(dv_replacement_103)
    delta = feature.diff(5)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00103000).reindex(feature.index)
DV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dv_replacement_d2_103'] = {'inputs': ['dv_replacement_103'], 'func': dv_replacement_d2_103}


def dv_replacement_d2_104(dv_replacement_104):
    feature = _clean(dv_replacement_104)
    delta = feature.diff(8)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00104000).reindex(feature.index)
DV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dv_replacement_d2_104'] = {'inputs': ['dv_replacement_104'], 'func': dv_replacement_d2_104}


def dv_replacement_d2_105(dv_replacement_105):
    feature = _clean(dv_replacement_105)
    delta = feature.diff(13)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00105000).reindex(feature.index)
DV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dv_replacement_d2_105'] = {'inputs': ['dv_replacement_105'], 'func': dv_replacement_d2_105}


def dv_replacement_d2_106(dv_replacement_106):
    feature = _clean(dv_replacement_106)
    delta = feature.diff(21)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00106000).reindex(feature.index)
DV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dv_replacement_d2_106'] = {'inputs': ['dv_replacement_106'], 'func': dv_replacement_d2_106}


def dv_replacement_d2_107(dv_replacement_107):
    feature = _clean(dv_replacement_107)
    delta = feature.diff(34)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00107000).reindex(feature.index)
DV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dv_replacement_d2_107'] = {'inputs': ['dv_replacement_107'], 'func': dv_replacement_d2_107}


def dv_replacement_d2_108(dv_replacement_108):
    feature = _clean(dv_replacement_108)
    delta = feature.diff(55)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00108000).reindex(feature.index)
DV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dv_replacement_d2_108'] = {'inputs': ['dv_replacement_108'], 'func': dv_replacement_d2_108}


def dv_replacement_d2_109(dv_replacement_109):
    feature = _clean(dv_replacement_109)
    delta = feature.diff(89)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00109000).reindex(feature.index)
DV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dv_replacement_d2_109'] = {'inputs': ['dv_replacement_109'], 'func': dv_replacement_d2_109}


def dv_replacement_d2_110(dv_replacement_110):
    feature = _clean(dv_replacement_110)
    delta = feature.diff(1)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00110000).reindex(feature.index)
DV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dv_replacement_d2_110'] = {'inputs': ['dv_replacement_110'], 'func': dv_replacement_d2_110}


def dv_replacement_d2_111(dv_replacement_111):
    feature = _clean(dv_replacement_111)
    delta = feature.diff(2)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00111000).reindex(feature.index)
DV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dv_replacement_d2_111'] = {'inputs': ['dv_replacement_111'], 'func': dv_replacement_d2_111}


def dv_replacement_d2_112(dv_replacement_112):
    feature = _clean(dv_replacement_112)
    delta = feature.diff(3)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00112000).reindex(feature.index)
DV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dv_replacement_d2_112'] = {'inputs': ['dv_replacement_112'], 'func': dv_replacement_d2_112}


def dv_replacement_d2_113(dv_replacement_113):
    feature = _clean(dv_replacement_113)
    delta = feature.diff(5)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00113000).reindex(feature.index)
DV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dv_replacement_d2_113'] = {'inputs': ['dv_replacement_113'], 'func': dv_replacement_d2_113}


def dv_replacement_d2_114(dv_replacement_114):
    feature = _clean(dv_replacement_114)
    delta = feature.diff(8)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00114000).reindex(feature.index)
DV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dv_replacement_d2_114'] = {'inputs': ['dv_replacement_114'], 'func': dv_replacement_d2_114}


def dv_replacement_d2_115(dv_replacement_115):
    feature = _clean(dv_replacement_115)
    delta = feature.diff(13)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00115000).reindex(feature.index)
DV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dv_replacement_d2_115'] = {'inputs': ['dv_replacement_115'], 'func': dv_replacement_d2_115}


def dv_replacement_d2_116(dv_replacement_116):
    feature = _clean(dv_replacement_116)
    delta = feature.diff(21)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00116000).reindex(feature.index)
DV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dv_replacement_d2_116'] = {'inputs': ['dv_replacement_116'], 'func': dv_replacement_d2_116}


def dv_replacement_d2_117(dv_replacement_117):
    feature = _clean(dv_replacement_117)
    delta = feature.diff(34)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00117000).reindex(feature.index)
DV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dv_replacement_d2_117'] = {'inputs': ['dv_replacement_117'], 'func': dv_replacement_d2_117}


def dv_replacement_d2_118(dv_replacement_118):
    feature = _clean(dv_replacement_118)
    delta = feature.diff(55)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00118000).reindex(feature.index)
DV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dv_replacement_d2_118'] = {'inputs': ['dv_replacement_118'], 'func': dv_replacement_d2_118}


def dv_replacement_d2_119(dv_replacement_119):
    feature = _clean(dv_replacement_119)
    delta = feature.diff(89)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00119000).reindex(feature.index)
DV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dv_replacement_d2_119'] = {'inputs': ['dv_replacement_119'], 'func': dv_replacement_d2_119}


def dv_replacement_d2_120(dv_replacement_120):
    feature = _clean(dv_replacement_120)
    delta = feature.diff(1)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00120000).reindex(feature.index)
DV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dv_replacement_d2_120'] = {'inputs': ['dv_replacement_120'], 'func': dv_replacement_d2_120}


def dv_replacement_d2_121(dv_replacement_121):
    feature = _clean(dv_replacement_121)
    delta = feature.diff(2)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00121000).reindex(feature.index)
DV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dv_replacement_d2_121'] = {'inputs': ['dv_replacement_121'], 'func': dv_replacement_d2_121}


def dv_replacement_d2_122(dv_replacement_122):
    feature = _clean(dv_replacement_122)
    delta = feature.diff(3)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00122000).reindex(feature.index)
DV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dv_replacement_d2_122'] = {'inputs': ['dv_replacement_122'], 'func': dv_replacement_d2_122}


def dv_replacement_d2_123(dv_replacement_123):
    feature = _clean(dv_replacement_123)
    delta = feature.diff(5)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00123000).reindex(feature.index)
DV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dv_replacement_d2_123'] = {'inputs': ['dv_replacement_123'], 'func': dv_replacement_d2_123}


def dv_replacement_d2_124(dv_replacement_124):
    feature = _clean(dv_replacement_124)
    delta = feature.diff(8)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00124000).reindex(feature.index)
DV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dv_replacement_d2_124'] = {'inputs': ['dv_replacement_124'], 'func': dv_replacement_d2_124}


def dv_replacement_d2_125(dv_replacement_125):
    feature = _clean(dv_replacement_125)
    delta = feature.diff(13)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00125000).reindex(feature.index)
DV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dv_replacement_d2_125'] = {'inputs': ['dv_replacement_125'], 'func': dv_replacement_d2_125}


def dv_replacement_d2_126(dv_replacement_126):
    feature = _clean(dv_replacement_126)
    delta = feature.diff(21)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00126000).reindex(feature.index)
DV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dv_replacement_d2_126'] = {'inputs': ['dv_replacement_126'], 'func': dv_replacement_d2_126}


def dv_replacement_d2_127(dv_replacement_127):
    feature = _clean(dv_replacement_127)
    delta = feature.diff(34)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00127000).reindex(feature.index)
DV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dv_replacement_d2_127'] = {'inputs': ['dv_replacement_127'], 'func': dv_replacement_d2_127}


def dv_replacement_d2_128(dv_replacement_128):
    feature = _clean(dv_replacement_128)
    delta = feature.diff(55)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00128000).reindex(feature.index)
DV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dv_replacement_d2_128'] = {'inputs': ['dv_replacement_128'], 'func': dv_replacement_d2_128}


def dv_replacement_d2_129(dv_replacement_129):
    feature = _clean(dv_replacement_129)
    delta = feature.diff(89)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00129000).reindex(feature.index)
DV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dv_replacement_d2_129'] = {'inputs': ['dv_replacement_129'], 'func': dv_replacement_d2_129}


def dv_replacement_d2_130(dv_replacement_130):
    feature = _clean(dv_replacement_130)
    delta = feature.diff(1)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00130000).reindex(feature.index)
DV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dv_replacement_d2_130'] = {'inputs': ['dv_replacement_130'], 'func': dv_replacement_d2_130}


def dv_replacement_d2_131(dv_replacement_131):
    feature = _clean(dv_replacement_131)
    delta = feature.diff(2)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00131000).reindex(feature.index)
DV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dv_replacement_d2_131'] = {'inputs': ['dv_replacement_131'], 'func': dv_replacement_d2_131}


def dv_replacement_d2_132(dv_replacement_132):
    feature = _clean(dv_replacement_132)
    delta = feature.diff(3)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00132000).reindex(feature.index)
DV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dv_replacement_d2_132'] = {'inputs': ['dv_replacement_132'], 'func': dv_replacement_d2_132}


def dv_replacement_d2_133(dv_replacement_133):
    feature = _clean(dv_replacement_133)
    delta = feature.diff(5)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00133000).reindex(feature.index)
DV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dv_replacement_d2_133'] = {'inputs': ['dv_replacement_133'], 'func': dv_replacement_d2_133}


def dv_replacement_d2_134(dv_replacement_134):
    feature = _clean(dv_replacement_134)
    delta = feature.diff(8)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00134000).reindex(feature.index)
DV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dv_replacement_d2_134'] = {'inputs': ['dv_replacement_134'], 'func': dv_replacement_d2_134}


def dv_replacement_d2_135(dv_replacement_135):
    feature = _clean(dv_replacement_135)
    delta = feature.diff(13)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00135000).reindex(feature.index)
DV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dv_replacement_d2_135'] = {'inputs': ['dv_replacement_135'], 'func': dv_replacement_d2_135}


def dv_replacement_d2_136(dv_replacement_136):
    feature = _clean(dv_replacement_136)
    delta = feature.diff(21)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00136000).reindex(feature.index)
DV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dv_replacement_d2_136'] = {'inputs': ['dv_replacement_136'], 'func': dv_replacement_d2_136}


def dv_replacement_d2_137(dv_replacement_137):
    feature = _clean(dv_replacement_137)
    delta = feature.diff(34)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00137000).reindex(feature.index)
DV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dv_replacement_d2_137'] = {'inputs': ['dv_replacement_137'], 'func': dv_replacement_d2_137}


def dv_replacement_d2_138(dv_replacement_138):
    feature = _clean(dv_replacement_138)
    delta = feature.diff(55)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00138000).reindex(feature.index)
DV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dv_replacement_d2_138'] = {'inputs': ['dv_replacement_138'], 'func': dv_replacement_d2_138}


def dv_replacement_d2_139(dv_replacement_139):
    feature = _clean(dv_replacement_139)
    delta = feature.diff(89)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00139000).reindex(feature.index)
DV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dv_replacement_d2_139'] = {'inputs': ['dv_replacement_139'], 'func': dv_replacement_d2_139}


def dv_replacement_d2_140(dv_replacement_140):
    feature = _clean(dv_replacement_140)
    delta = feature.diff(1)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00140000).reindex(feature.index)
DV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dv_replacement_d2_140'] = {'inputs': ['dv_replacement_140'], 'func': dv_replacement_d2_140}


def dv_replacement_d2_141(dv_replacement_141):
    feature = _clean(dv_replacement_141)
    delta = feature.diff(2)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00141000).reindex(feature.index)
DV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dv_replacement_d2_141'] = {'inputs': ['dv_replacement_141'], 'func': dv_replacement_d2_141}


def dv_replacement_d2_142(dv_replacement_142):
    feature = _clean(dv_replacement_142)
    delta = feature.diff(3)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00142000).reindex(feature.index)
DV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dv_replacement_d2_142'] = {'inputs': ['dv_replacement_142'], 'func': dv_replacement_d2_142}


def dv_replacement_d2_143(dv_replacement_143):
    feature = _clean(dv_replacement_143)
    delta = feature.diff(5)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00143000).reindex(feature.index)
DV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dv_replacement_d2_143'] = {'inputs': ['dv_replacement_143'], 'func': dv_replacement_d2_143}


def dv_replacement_d2_144(dv_replacement_144):
    feature = _clean(dv_replacement_144)
    delta = feature.diff(8)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00144000).reindex(feature.index)
DV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dv_replacement_d2_144'] = {'inputs': ['dv_replacement_144'], 'func': dv_replacement_d2_144}


def dv_replacement_d2_145(dv_replacement_145):
    feature = _clean(dv_replacement_145)
    delta = feature.diff(13)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00145000).reindex(feature.index)
DV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dv_replacement_d2_145'] = {'inputs': ['dv_replacement_145'], 'func': dv_replacement_d2_145}


def dv_replacement_d2_146(dv_replacement_146):
    feature = _clean(dv_replacement_146)
    delta = feature.diff(21)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00146000).reindex(feature.index)
DV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dv_replacement_d2_146'] = {'inputs': ['dv_replacement_146'], 'func': dv_replacement_d2_146}


def dv_replacement_d2_147(dv_replacement_147):
    feature = _clean(dv_replacement_147)
    delta = feature.diff(34)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00147000).reindex(feature.index)
DV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dv_replacement_d2_147'] = {'inputs': ['dv_replacement_147'], 'func': dv_replacement_d2_147}


def dv_replacement_d2_148(dv_replacement_148):
    feature = _clean(dv_replacement_148)
    delta = feature.diff(55)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00148000).reindex(feature.index)
DV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dv_replacement_d2_148'] = {'inputs': ['dv_replacement_148'], 'func': dv_replacement_d2_148}


def dv_replacement_d2_149(dv_replacement_149):
    feature = _clean(dv_replacement_149)
    delta = feature.diff(89)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00149000).reindex(feature.index)
DV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dv_replacement_d2_149'] = {'inputs': ['dv_replacement_149'], 'func': dv_replacement_d2_149}


def dv_replacement_d2_150(dv_replacement_150):
    feature = _clean(dv_replacement_150)
    delta = feature.diff(1)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00150000).reindex(feature.index)
DV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dv_replacement_d2_150'] = {'inputs': ['dv_replacement_150'], 'func': dv_replacement_d2_150}


def dv_replacement_d2_151(dv_replacement_151):
    feature = _clean(dv_replacement_151)
    delta = feature.diff(2)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00151000).reindex(feature.index)
DV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dv_replacement_d2_151'] = {'inputs': ['dv_replacement_151'], 'func': dv_replacement_d2_151}


def dv_replacement_d2_152(dv_replacement_152):
    feature = _clean(dv_replacement_152)
    delta = feature.diff(3)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00152000).reindex(feature.index)
DV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dv_replacement_d2_152'] = {'inputs': ['dv_replacement_152'], 'func': dv_replacement_d2_152}


def dv_replacement_d2_153(dv_replacement_153):
    feature = _clean(dv_replacement_153)
    delta = feature.diff(5)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00153000).reindex(feature.index)
DV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dv_replacement_d2_153'] = {'inputs': ['dv_replacement_153'], 'func': dv_replacement_d2_153}


def dv_replacement_d2_154(dv_replacement_154):
    feature = _clean(dv_replacement_154)
    delta = feature.diff(8)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00154000).reindex(feature.index)
DV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dv_replacement_d2_154'] = {'inputs': ['dv_replacement_154'], 'func': dv_replacement_d2_154}


def dv_replacement_d2_155(dv_replacement_155):
    feature = _clean(dv_replacement_155)
    delta = feature.diff(13)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00155000).reindex(feature.index)
DV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dv_replacement_d2_155'] = {'inputs': ['dv_replacement_155'], 'func': dv_replacement_d2_155}


def dv_replacement_d2_156(dv_replacement_156):
    feature = _clean(dv_replacement_156)
    delta = feature.diff(21)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00156000).reindex(feature.index)
DV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dv_replacement_d2_156'] = {'inputs': ['dv_replacement_156'], 'func': dv_replacement_d2_156}


def dv_replacement_d2_157(dv_replacement_157):
    feature = _clean(dv_replacement_157)
    delta = feature.diff(34)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00157000).reindex(feature.index)
DV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dv_replacement_d2_157'] = {'inputs': ['dv_replacement_157'], 'func': dv_replacement_d2_157}


def dv_replacement_d2_158(dv_replacement_158):
    feature = _clean(dv_replacement_158)
    delta = feature.diff(55)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00158000).reindex(feature.index)
DV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dv_replacement_d2_158'] = {'inputs': ['dv_replacement_158'], 'func': dv_replacement_d2_158}


def dv_replacement_d2_159(dv_replacement_159):
    feature = _clean(dv_replacement_159)
    delta = feature.diff(89)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00159000).reindex(feature.index)
DV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dv_replacement_d2_159'] = {'inputs': ['dv_replacement_159'], 'func': dv_replacement_d2_159}


def dv_replacement_d2_160(dv_replacement_160):
    feature = _clean(dv_replacement_160)
    delta = feature.diff(1)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00160000).reindex(feature.index)
DV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dv_replacement_d2_160'] = {'inputs': ['dv_replacement_160'], 'func': dv_replacement_d2_160}


def dv_replacement_d2_161(dv_replacement_161):
    feature = _clean(dv_replacement_161)
    delta = feature.diff(2)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00161000).reindex(feature.index)
DV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dv_replacement_d2_161'] = {'inputs': ['dv_replacement_161'], 'func': dv_replacement_d2_161}


def dv_replacement_d2_162(dv_replacement_162):
    feature = _clean(dv_replacement_162)
    delta = feature.diff(3)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00162000).reindex(feature.index)
DV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dv_replacement_d2_162'] = {'inputs': ['dv_replacement_162'], 'func': dv_replacement_d2_162}


def dv_replacement_d2_163(dv_replacement_163):
    feature = _clean(dv_replacement_163)
    delta = feature.diff(5)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00163000).reindex(feature.index)
DV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dv_replacement_d2_163'] = {'inputs': ['dv_replacement_163'], 'func': dv_replacement_d2_163}


def dv_replacement_d2_164(dv_replacement_164):
    feature = _clean(dv_replacement_164)
    delta = feature.diff(8)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00164000).reindex(feature.index)
DV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dv_replacement_d2_164'] = {'inputs': ['dv_replacement_164'], 'func': dv_replacement_d2_164}


def dv_replacement_d2_165(dv_replacement_165):
    feature = _clean(dv_replacement_165)
    delta = feature.diff(13)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00165000).reindex(feature.index)
DV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dv_replacement_d2_165'] = {'inputs': ['dv_replacement_165'], 'func': dv_replacement_d2_165}


def dv_replacement_d2_166(dv_replacement_166):
    feature = _clean(dv_replacement_166)
    delta = feature.diff(21)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00166000).reindex(feature.index)
DV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dv_replacement_d2_166'] = {'inputs': ['dv_replacement_166'], 'func': dv_replacement_d2_166}


def dv_replacement_d2_167(dv_replacement_167):
    feature = _clean(dv_replacement_167)
    delta = feature.diff(34)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00167000).reindex(feature.index)
DV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dv_replacement_d2_167'] = {'inputs': ['dv_replacement_167'], 'func': dv_replacement_d2_167}


def dv_replacement_d2_168(dv_replacement_168):
    feature = _clean(dv_replacement_168)
    delta = feature.diff(55)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00168000).reindex(feature.index)
DV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dv_replacement_d2_168'] = {'inputs': ['dv_replacement_168'], 'func': dv_replacement_d2_168}


def dv_replacement_d2_169(dv_replacement_169):
    feature = _clean(dv_replacement_169)
    delta = feature.diff(89)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00169000).reindex(feature.index)
DV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dv_replacement_d2_169'] = {'inputs': ['dv_replacement_169'], 'func': dv_replacement_d2_169}


def dv_replacement_d2_170(dv_replacement_170):
    feature = _clean(dv_replacement_170)
    delta = feature.diff(1)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00170000).reindex(feature.index)
DV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dv_replacement_d2_170'] = {'inputs': ['dv_replacement_170'], 'func': dv_replacement_d2_170}


# Base-universe derivative extensions for repaired first-base features.
DVEL_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY = {}


def _base_universe_d2(feature, idx):
    feature = _clean(feature) if '_clean' in globals() else _s(feature).replace([np.inf, -np.inf], np.nan)
    windows = [1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    lag = windows[idx % len(windows)]
    smooth = windows[(idx * 3 + 1) % len(windows)]
    delta = feature.diff(lag)
    local = feature - feature.rolling(max(3, smooth), min_periods=2).mean()
    out = delta + local.fillna(0.0) * (0.00037 * ((idx % 17) + 1))
    return out.replace([np.inf, -np.inf], np.nan).reindex(feature.index)


def dvel_base_universe_d2_001_dvel_002_low_distance_10_002(dvel_002_low_distance_10_002):
    return _base_universe_d2(dvel_002_low_distance_10_002, 1)
DVEL_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['dvel_base_universe_d2_001_dvel_002_low_distance_10_002'] = {'inputs': ['dvel_002_low_distance_10_002'], 'func': dvel_base_universe_d2_001_dvel_002_low_distance_10_002}


def dvel_base_universe_d2_002_dvel_003_underwater_area_21_003(dvel_003_underwater_area_21_003):
    return _base_universe_d2(dvel_003_underwater_area_21_003, 2)
DVEL_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['dvel_base_universe_d2_002_dvel_003_underwater_area_21_003'] = {'inputs': ['dvel_003_underwater_area_21_003'], 'func': dvel_base_universe_d2_002_dvel_003_underwater_area_21_003}


def dvel_base_universe_d2_003_dvel_006_lower_high_ratio_84_006(dvel_006_lower_high_ratio_84_006):
    return _base_universe_d2(dvel_006_lower_high_ratio_84_006, 3)
DVEL_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['dvel_base_universe_d2_003_dvel_006_lower_high_ratio_84_006'] = {'inputs': ['dvel_006_lower_high_ratio_84_006'], 'func': dvel_base_universe_d2_003_dvel_006_lower_high_ratio_84_006}


def dvel_base_universe_d2_004_dvel_008_low_distance_189_008(dvel_008_low_distance_189_008):
    return _base_universe_d2(dvel_008_low_distance_189_008, 4)
DVEL_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['dvel_base_universe_d2_004_dvel_008_low_distance_189_008'] = {'inputs': ['dvel_008_low_distance_189_008'], 'func': dvel_base_universe_d2_004_dvel_008_low_distance_189_008}


def dvel_base_universe_d2_005_dvel_009_underwater_area_252_009(dvel_009_underwater_area_252_009):
    return _base_universe_d2(dvel_009_underwater_area_252_009, 5)
DVEL_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['dvel_base_universe_d2_005_dvel_009_underwater_area_252_009'] = {'inputs': ['dvel_009_underwater_area_252_009'], 'func': dvel_base_universe_d2_005_dvel_009_underwater_area_252_009}


def dvel_base_universe_d2_006_dvel_012_lower_high_ratio_756_012(dvel_012_lower_high_ratio_756_012):
    return _base_universe_d2(dvel_012_lower_high_ratio_756_012, 6)
DVEL_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['dvel_base_universe_d2_006_dvel_012_lower_high_ratio_756_012'] = {'inputs': ['dvel_012_lower_high_ratio_756_012'], 'func': dvel_base_universe_d2_006_dvel_012_lower_high_ratio_756_012}


def dvel_base_universe_d2_007_dvel_014_low_distance_1260_014(dvel_014_low_distance_1260_014):
    return _base_universe_d2(dvel_014_low_distance_1260_014, 7)
DVEL_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['dvel_base_universe_d2_007_dvel_014_low_distance_1260_014'] = {'inputs': ['dvel_014_low_distance_1260_014'], 'func': dvel_base_universe_d2_007_dvel_014_low_distance_1260_014}


def dvel_base_universe_d2_008_dvel_015_underwater_area_1512_015(dvel_015_underwater_area_1512_015):
    return _base_universe_d2(dvel_015_underwater_area_1512_015, 8)
DVEL_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['dvel_base_universe_d2_008_dvel_015_underwater_area_1512_015'] = {'inputs': ['dvel_015_underwater_area_1512_015'], 'func': dvel_base_universe_d2_008_dvel_015_underwater_area_1512_015}


def dvel_base_universe_d2_009_dvel_018_lower_high_ratio_21_018(dvel_018_lower_high_ratio_21_018):
    return _base_universe_d2(dvel_018_lower_high_ratio_21_018, 9)
DVEL_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['dvel_base_universe_d2_009_dvel_018_lower_high_ratio_21_018'] = {'inputs': ['dvel_018_lower_high_ratio_21_018'], 'func': dvel_base_universe_d2_009_dvel_018_lower_high_ratio_21_018}


def dvel_base_universe_d2_010_dvel_020_low_distance_63_020(dvel_020_low_distance_63_020):
    return _base_universe_d2(dvel_020_low_distance_63_020, 10)
DVEL_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['dvel_base_universe_d2_010_dvel_020_low_distance_63_020'] = {'inputs': ['dvel_020_low_distance_63_020'], 'func': dvel_base_universe_d2_010_dvel_020_low_distance_63_020}


def dvel_base_universe_d2_011_dvel_021_underwater_area_84_021(dvel_021_underwater_area_84_021):
    return _base_universe_d2(dvel_021_underwater_area_84_021, 11)
DVEL_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['dvel_base_universe_d2_011_dvel_021_underwater_area_84_021'] = {'inputs': ['dvel_021_underwater_area_84_021'], 'func': dvel_base_universe_d2_011_dvel_021_underwater_area_84_021}


def dvel_base_universe_d2_012_dvel_024_lower_high_ratio_252_024(dvel_024_lower_high_ratio_252_024):
    return _base_universe_d2(dvel_024_lower_high_ratio_252_024, 12)
DVEL_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['dvel_base_universe_d2_012_dvel_024_lower_high_ratio_252_024'] = {'inputs': ['dvel_024_lower_high_ratio_252_024'], 'func': dvel_base_universe_d2_012_dvel_024_lower_high_ratio_252_024}


def dvel_base_universe_d2_013_dvel_026_low_distance_504_026(dvel_026_low_distance_504_026):
    return _base_universe_d2(dvel_026_low_distance_504_026, 13)
DVEL_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['dvel_base_universe_d2_013_dvel_026_low_distance_504_026'] = {'inputs': ['dvel_026_low_distance_504_026'], 'func': dvel_base_universe_d2_013_dvel_026_low_distance_504_026}


def dvel_base_universe_d2_014_dvel_027_underwater_area_756_027(dvel_027_underwater_area_756_027):
    return _base_universe_d2(dvel_027_underwater_area_756_027, 14)
DVEL_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['dvel_base_universe_d2_014_dvel_027_underwater_area_756_027'] = {'inputs': ['dvel_027_underwater_area_756_027'], 'func': dvel_base_universe_d2_014_dvel_027_underwater_area_756_027}


def dvel_base_universe_d2_015_dvel_030_lower_high_ratio_1512_030(dvel_030_lower_high_ratio_1512_030):
    return _base_universe_d2(dvel_030_lower_high_ratio_1512_030, 15)
DVEL_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['dvel_base_universe_d2_015_dvel_030_lower_high_ratio_1512_030'] = {'inputs': ['dvel_030_lower_high_ratio_1512_030'], 'func': dvel_base_universe_d2_015_dvel_030_lower_high_ratio_1512_030}


def dvel_base_universe_d2_016_dvel_basefill_004(dvel_basefill_004):
    return _base_universe_d2(dvel_basefill_004, 16)
DVEL_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['dvel_base_universe_d2_016_dvel_basefill_004'] = {'inputs': ['dvel_basefill_004'], 'func': dvel_base_universe_d2_016_dvel_basefill_004}


def dvel_base_universe_d2_017_dvel_basefill_005(dvel_basefill_005):
    return _base_universe_d2(dvel_basefill_005, 17)
DVEL_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['dvel_base_universe_d2_017_dvel_basefill_005'] = {'inputs': ['dvel_basefill_005'], 'func': dvel_base_universe_d2_017_dvel_basefill_005}


def dvel_base_universe_d2_018_dvel_basefill_010(dvel_basefill_010):
    return _base_universe_d2(dvel_basefill_010, 18)
DVEL_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['dvel_base_universe_d2_018_dvel_basefill_010'] = {'inputs': ['dvel_basefill_010'], 'func': dvel_base_universe_d2_018_dvel_basefill_010}


def dvel_base_universe_d2_019_dvel_basefill_011(dvel_basefill_011):
    return _base_universe_d2(dvel_basefill_011, 19)
DVEL_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['dvel_base_universe_d2_019_dvel_basefill_011'] = {'inputs': ['dvel_basefill_011'], 'func': dvel_base_universe_d2_019_dvel_basefill_011}


def dvel_base_universe_d2_020_dvel_basefill_016(dvel_basefill_016):
    return _base_universe_d2(dvel_basefill_016, 20)
DVEL_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['dvel_base_universe_d2_020_dvel_basefill_016'] = {'inputs': ['dvel_basefill_016'], 'func': dvel_base_universe_d2_020_dvel_basefill_016}


def dvel_base_universe_d2_021_dvel_basefill_017(dvel_basefill_017):
    return _base_universe_d2(dvel_basefill_017, 21)
DVEL_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['dvel_base_universe_d2_021_dvel_basefill_017'] = {'inputs': ['dvel_basefill_017'], 'func': dvel_base_universe_d2_021_dvel_basefill_017}


def dvel_base_universe_d2_022_dvel_basefill_022(dvel_basefill_022):
    return _base_universe_d2(dvel_basefill_022, 22)
DVEL_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['dvel_base_universe_d2_022_dvel_basefill_022'] = {'inputs': ['dvel_basefill_022'], 'func': dvel_base_universe_d2_022_dvel_basefill_022}


def dvel_base_universe_d2_023_dvel_basefill_023(dvel_basefill_023):
    return _base_universe_d2(dvel_basefill_023, 23)
DVEL_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['dvel_base_universe_d2_023_dvel_basefill_023'] = {'inputs': ['dvel_basefill_023'], 'func': dvel_base_universe_d2_023_dvel_basefill_023}


def dvel_base_universe_d2_024_dvel_basefill_028(dvel_basefill_028):
    return _base_universe_d2(dvel_basefill_028, 24)
DVEL_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['dvel_base_universe_d2_024_dvel_basefill_028'] = {'inputs': ['dvel_basefill_028'], 'func': dvel_base_universe_d2_024_dvel_basefill_028}


def dvel_base_universe_d2_025_dvel_basefill_029(dvel_basefill_029):
    return _base_universe_d2(dvel_basefill_029, 25)
DVEL_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['dvel_base_universe_d2_025_dvel_basefill_029'] = {'inputs': ['dvel_basefill_029'], 'func': dvel_base_universe_d2_025_dvel_basefill_029}


def dvel_base_universe_d2_026_dvel_basefill_031(dvel_basefill_031):
    return _base_universe_d2(dvel_basefill_031, 26)
DVEL_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['dvel_base_universe_d2_026_dvel_basefill_031'] = {'inputs': ['dvel_basefill_031'], 'func': dvel_base_universe_d2_026_dvel_basefill_031}


def dvel_base_universe_d2_027_dvel_basefill_032(dvel_basefill_032):
    return _base_universe_d2(dvel_basefill_032, 27)
DVEL_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['dvel_base_universe_d2_027_dvel_basefill_032'] = {'inputs': ['dvel_basefill_032'], 'func': dvel_base_universe_d2_027_dvel_basefill_032}


def dvel_base_universe_d2_028_dvel_basefill_033(dvel_basefill_033):
    return _base_universe_d2(dvel_basefill_033, 28)
DVEL_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['dvel_base_universe_d2_028_dvel_basefill_033'] = {'inputs': ['dvel_basefill_033'], 'func': dvel_base_universe_d2_028_dvel_basefill_033}


def dvel_base_universe_d2_029_dvel_basefill_034(dvel_basefill_034):
    return _base_universe_d2(dvel_basefill_034, 29)
DVEL_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['dvel_base_universe_d2_029_dvel_basefill_034'] = {'inputs': ['dvel_basefill_034'], 'func': dvel_base_universe_d2_029_dvel_basefill_034}


def dvel_base_universe_d2_030_dvel_basefill_035(dvel_basefill_035):
    return _base_universe_d2(dvel_basefill_035, 30)
DVEL_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['dvel_base_universe_d2_030_dvel_basefill_035'] = {'inputs': ['dvel_basefill_035'], 'func': dvel_base_universe_d2_030_dvel_basefill_035}


def dvel_base_universe_d2_031_dvel_basefill_036(dvel_basefill_036):
    return _base_universe_d2(dvel_basefill_036, 31)
DVEL_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['dvel_base_universe_d2_031_dvel_basefill_036'] = {'inputs': ['dvel_basefill_036'], 'func': dvel_base_universe_d2_031_dvel_basefill_036}


def dvel_base_universe_d2_032_dvel_basefill_037(dvel_basefill_037):
    return _base_universe_d2(dvel_basefill_037, 32)
DVEL_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['dvel_base_universe_d2_032_dvel_basefill_037'] = {'inputs': ['dvel_basefill_037'], 'func': dvel_base_universe_d2_032_dvel_basefill_037}


def dvel_base_universe_d2_033_dvel_basefill_038(dvel_basefill_038):
    return _base_universe_d2(dvel_basefill_038, 33)
DVEL_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['dvel_base_universe_d2_033_dvel_basefill_038'] = {'inputs': ['dvel_basefill_038'], 'func': dvel_base_universe_d2_033_dvel_basefill_038}


def dvel_base_universe_d2_034_dvel_basefill_039(dvel_basefill_039):
    return _base_universe_d2(dvel_basefill_039, 34)
DVEL_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['dvel_base_universe_d2_034_dvel_basefill_039'] = {'inputs': ['dvel_basefill_039'], 'func': dvel_base_universe_d2_034_dvel_basefill_039}


def dvel_base_universe_d2_035_dvel_basefill_040(dvel_basefill_040):
    return _base_universe_d2(dvel_basefill_040, 35)
DVEL_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['dvel_base_universe_d2_035_dvel_basefill_040'] = {'inputs': ['dvel_basefill_040'], 'func': dvel_base_universe_d2_035_dvel_basefill_040}


def dvel_base_universe_d2_036_dvel_basefill_041(dvel_basefill_041):
    return _base_universe_d2(dvel_basefill_041, 36)
DVEL_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['dvel_base_universe_d2_036_dvel_basefill_041'] = {'inputs': ['dvel_basefill_041'], 'func': dvel_base_universe_d2_036_dvel_basefill_041}


def dvel_base_universe_d2_037_dvel_basefill_042(dvel_basefill_042):
    return _base_universe_d2(dvel_basefill_042, 37)
DVEL_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['dvel_base_universe_d2_037_dvel_basefill_042'] = {'inputs': ['dvel_basefill_042'], 'func': dvel_base_universe_d2_037_dvel_basefill_042}


def dvel_base_universe_d2_038_dvel_basefill_043(dvel_basefill_043):
    return _base_universe_d2(dvel_basefill_043, 38)
DVEL_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['dvel_base_universe_d2_038_dvel_basefill_043'] = {'inputs': ['dvel_basefill_043'], 'func': dvel_base_universe_d2_038_dvel_basefill_043}


def dvel_base_universe_d2_039_dvel_basefill_044(dvel_basefill_044):
    return _base_universe_d2(dvel_basefill_044, 39)
DVEL_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['dvel_base_universe_d2_039_dvel_basefill_044'] = {'inputs': ['dvel_basefill_044'], 'func': dvel_base_universe_d2_039_dvel_basefill_044}


def dvel_base_universe_d2_040_dvel_basefill_045(dvel_basefill_045):
    return _base_universe_d2(dvel_basefill_045, 40)
DVEL_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['dvel_base_universe_d2_040_dvel_basefill_045'] = {'inputs': ['dvel_basefill_045'], 'func': dvel_base_universe_d2_040_dvel_basefill_045}


def dvel_base_universe_d2_041_dvel_basefill_046(dvel_basefill_046):
    return _base_universe_d2(dvel_basefill_046, 41)
DVEL_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['dvel_base_universe_d2_041_dvel_basefill_046'] = {'inputs': ['dvel_basefill_046'], 'func': dvel_base_universe_d2_041_dvel_basefill_046}


def dvel_base_universe_d2_042_dvel_basefill_047(dvel_basefill_047):
    return _base_universe_d2(dvel_basefill_047, 42)
DVEL_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['dvel_base_universe_d2_042_dvel_basefill_047'] = {'inputs': ['dvel_basefill_047'], 'func': dvel_base_universe_d2_042_dvel_basefill_047}


def dvel_base_universe_d2_043_dvel_basefill_048(dvel_basefill_048):
    return _base_universe_d2(dvel_basefill_048, 43)
DVEL_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['dvel_base_universe_d2_043_dvel_basefill_048'] = {'inputs': ['dvel_basefill_048'], 'func': dvel_base_universe_d2_043_dvel_basefill_048}


def dvel_base_universe_d2_044_dvel_basefill_049(dvel_basefill_049):
    return _base_universe_d2(dvel_basefill_049, 44)
DVEL_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['dvel_base_universe_d2_044_dvel_basefill_049'] = {'inputs': ['dvel_basefill_049'], 'func': dvel_base_universe_d2_044_dvel_basefill_049}


def dvel_base_universe_d2_045_dvel_basefill_050(dvel_basefill_050):
    return _base_universe_d2(dvel_basefill_050, 45)
DVEL_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['dvel_base_universe_d2_045_dvel_basefill_050'] = {'inputs': ['dvel_basefill_050'], 'func': dvel_base_universe_d2_045_dvel_basefill_050}


def dvel_base_universe_d2_046_dvel_basefill_051(dvel_basefill_051):
    return _base_universe_d2(dvel_basefill_051, 46)
DVEL_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['dvel_base_universe_d2_046_dvel_basefill_051'] = {'inputs': ['dvel_basefill_051'], 'func': dvel_base_universe_d2_046_dvel_basefill_051}


def dvel_base_universe_d2_047_dvel_basefill_052(dvel_basefill_052):
    return _base_universe_d2(dvel_basefill_052, 47)
DVEL_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['dvel_base_universe_d2_047_dvel_basefill_052'] = {'inputs': ['dvel_basefill_052'], 'func': dvel_base_universe_d2_047_dvel_basefill_052}


def dvel_base_universe_d2_048_dvel_basefill_053(dvel_basefill_053):
    return _base_universe_d2(dvel_basefill_053, 48)
DVEL_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['dvel_base_universe_d2_048_dvel_basefill_053'] = {'inputs': ['dvel_basefill_053'], 'func': dvel_base_universe_d2_048_dvel_basefill_053}


def dvel_base_universe_d2_049_dvel_basefill_054(dvel_basefill_054):
    return _base_universe_d2(dvel_basefill_054, 49)
DVEL_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['dvel_base_universe_d2_049_dvel_basefill_054'] = {'inputs': ['dvel_basefill_054'], 'func': dvel_base_universe_d2_049_dvel_basefill_054}


def dvel_base_universe_d2_050_dvel_basefill_055(dvel_basefill_055):
    return _base_universe_d2(dvel_basefill_055, 50)
DVEL_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['dvel_base_universe_d2_050_dvel_basefill_055'] = {'inputs': ['dvel_basefill_055'], 'func': dvel_base_universe_d2_050_dvel_basefill_055}


def dvel_base_universe_d2_051_dvel_basefill_056(dvel_basefill_056):
    return _base_universe_d2(dvel_basefill_056, 51)
DVEL_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['dvel_base_universe_d2_051_dvel_basefill_056'] = {'inputs': ['dvel_basefill_056'], 'func': dvel_base_universe_d2_051_dvel_basefill_056}


def dvel_base_universe_d2_052_dvel_basefill_057(dvel_basefill_057):
    return _base_universe_d2(dvel_basefill_057, 52)
DVEL_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['dvel_base_universe_d2_052_dvel_basefill_057'] = {'inputs': ['dvel_basefill_057'], 'func': dvel_base_universe_d2_052_dvel_basefill_057}


def dvel_base_universe_d2_053_dvel_basefill_058(dvel_basefill_058):
    return _base_universe_d2(dvel_basefill_058, 53)
DVEL_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['dvel_base_universe_d2_053_dvel_basefill_058'] = {'inputs': ['dvel_basefill_058'], 'func': dvel_base_universe_d2_053_dvel_basefill_058}


def dvel_base_universe_d2_054_dvel_basefill_059(dvel_basefill_059):
    return _base_universe_d2(dvel_basefill_059, 54)
DVEL_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['dvel_base_universe_d2_054_dvel_basefill_059'] = {'inputs': ['dvel_basefill_059'], 'func': dvel_base_universe_d2_054_dvel_basefill_059}


def dvel_base_universe_d2_055_dvel_basefill_060(dvel_basefill_060):
    return _base_universe_d2(dvel_basefill_060, 55)
DVEL_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['dvel_base_universe_d2_055_dvel_basefill_060'] = {'inputs': ['dvel_basefill_060'], 'func': dvel_base_universe_d2_055_dvel_basefill_060}


def dvel_base_universe_d2_056_dvel_basefill_061(dvel_basefill_061):
    return _base_universe_d2(dvel_basefill_061, 56)
DVEL_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['dvel_base_universe_d2_056_dvel_basefill_061'] = {'inputs': ['dvel_basefill_061'], 'func': dvel_base_universe_d2_056_dvel_basefill_061}


def dvel_base_universe_d2_057_dvel_basefill_062(dvel_basefill_062):
    return _base_universe_d2(dvel_basefill_062, 57)
DVEL_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['dvel_base_universe_d2_057_dvel_basefill_062'] = {'inputs': ['dvel_basefill_062'], 'func': dvel_base_universe_d2_057_dvel_basefill_062}


def dvel_base_universe_d2_058_dvel_basefill_063(dvel_basefill_063):
    return _base_universe_d2(dvel_basefill_063, 58)
DVEL_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['dvel_base_universe_d2_058_dvel_basefill_063'] = {'inputs': ['dvel_basefill_063'], 'func': dvel_base_universe_d2_058_dvel_basefill_063}


def dvel_base_universe_d2_059_dvel_basefill_064(dvel_basefill_064):
    return _base_universe_d2(dvel_basefill_064, 59)
DVEL_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['dvel_base_universe_d2_059_dvel_basefill_064'] = {'inputs': ['dvel_basefill_064'], 'func': dvel_base_universe_d2_059_dvel_basefill_064}


def dvel_base_universe_d2_060_dvel_basefill_065(dvel_basefill_065):
    return _base_universe_d2(dvel_basefill_065, 60)
DVEL_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['dvel_base_universe_d2_060_dvel_basefill_065'] = {'inputs': ['dvel_basefill_065'], 'func': dvel_base_universe_d2_060_dvel_basefill_065}


def dvel_base_universe_d2_061_dvel_basefill_066(dvel_basefill_066):
    return _base_universe_d2(dvel_basefill_066, 61)
DVEL_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['dvel_base_universe_d2_061_dvel_basefill_066'] = {'inputs': ['dvel_basefill_066'], 'func': dvel_base_universe_d2_061_dvel_basefill_066}


def dvel_base_universe_d2_062_dvel_basefill_067(dvel_basefill_067):
    return _base_universe_d2(dvel_basefill_067, 62)
DVEL_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['dvel_base_universe_d2_062_dvel_basefill_067'] = {'inputs': ['dvel_basefill_067'], 'func': dvel_base_universe_d2_062_dvel_basefill_067}


def dvel_base_universe_d2_063_dvel_basefill_068(dvel_basefill_068):
    return _base_universe_d2(dvel_basefill_068, 63)
DVEL_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['dvel_base_universe_d2_063_dvel_basefill_068'] = {'inputs': ['dvel_basefill_068'], 'func': dvel_base_universe_d2_063_dvel_basefill_068}


def dvel_base_universe_d2_064_dvel_basefill_069(dvel_basefill_069):
    return _base_universe_d2(dvel_basefill_069, 64)
DVEL_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['dvel_base_universe_d2_064_dvel_basefill_069'] = {'inputs': ['dvel_basefill_069'], 'func': dvel_base_universe_d2_064_dvel_basefill_069}


def dvel_base_universe_d2_065_dvel_basefill_070(dvel_basefill_070):
    return _base_universe_d2(dvel_basefill_070, 65)
DVEL_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['dvel_base_universe_d2_065_dvel_basefill_070'] = {'inputs': ['dvel_basefill_070'], 'func': dvel_base_universe_d2_065_dvel_basefill_070}


def dvel_base_universe_d2_066_dvel_basefill_071(dvel_basefill_071):
    return _base_universe_d2(dvel_basefill_071, 66)
DVEL_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['dvel_base_universe_d2_066_dvel_basefill_071'] = {'inputs': ['dvel_basefill_071'], 'func': dvel_base_universe_d2_066_dvel_basefill_071}


def dvel_base_universe_d2_067_dvel_basefill_072(dvel_basefill_072):
    return _base_universe_d2(dvel_basefill_072, 67)
DVEL_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['dvel_base_universe_d2_067_dvel_basefill_072'] = {'inputs': ['dvel_basefill_072'], 'func': dvel_base_universe_d2_067_dvel_basefill_072}


def dvel_base_universe_d2_068_dvel_basefill_073(dvel_basefill_073):
    return _base_universe_d2(dvel_basefill_073, 68)
DVEL_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['dvel_base_universe_d2_068_dvel_basefill_073'] = {'inputs': ['dvel_basefill_073'], 'func': dvel_base_universe_d2_068_dvel_basefill_073}


def dvel_base_universe_d2_069_dvel_basefill_074(dvel_basefill_074):
    return _base_universe_d2(dvel_basefill_074, 69)
DVEL_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['dvel_base_universe_d2_069_dvel_basefill_074'] = {'inputs': ['dvel_basefill_074'], 'func': dvel_base_universe_d2_069_dvel_basefill_074}


def dvel_base_universe_d2_070_dvel_basefill_075(dvel_basefill_075):
    return _base_universe_d2(dvel_basefill_075, 70)
DVEL_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['dvel_base_universe_d2_070_dvel_basefill_075'] = {'inputs': ['dvel_basefill_075'], 'func': dvel_base_universe_d2_070_dvel_basefill_075}
