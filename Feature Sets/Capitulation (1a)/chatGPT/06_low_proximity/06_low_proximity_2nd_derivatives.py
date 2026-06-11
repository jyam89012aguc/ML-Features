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



def lp_151_lp_001_drawdown_from_high_5_001_roc_1(lp_001_drawdown_from_high_5_001):
    feature = _s(lp_001_drawdown_from_high_5_001)
    return (_roc(feature, 1)).reindex(feature.index)

def lp_152_lp_007_drawdown_from_high_126_007_roc_5(lp_007_drawdown_from_high_126_007):
    feature = _s(lp_007_drawdown_from_high_126_007)
    return (_roc(feature, 5)).reindex(feature.index)

def lp_153_lp_013_drawdown_from_high_1008_013_roc_42(lp_013_drawdown_from_high_1008_013):
    feature = _s(lp_013_drawdown_from_high_1008_013)
    return (_roc(feature, 42)).reindex(feature.index)

def lp_154_lp_019_drawdown_from_high_42_019_roc_126(lp_019_drawdown_from_high_42_019):
    feature = _s(lp_019_drawdown_from_high_42_019)
    return (_roc(feature, 126)).reindex(feature.index)

def lp_155_lp_025_drawdown_from_high_378_025_roc_378(lp_025_drawdown_from_high_378_025):
    feature = _s(lp_025_drawdown_from_high_378_025)
    return (_roc(feature, 378)).reindex(feature.index)






















LOW_PROXIMITY_REGISTRY_2ND_DERIVATIVES = {
    'lp_151_lp_001_drawdown_from_high_5_001_roc_1': {'inputs': ['lp_001_drawdown_from_high_5_001'], 'func': lp_151_lp_001_drawdown_from_high_5_001_roc_1},
    'lp_152_lp_007_drawdown_from_high_126_007_roc_5': {'inputs': ['lp_007_drawdown_from_high_126_007'], 'func': lp_152_lp_007_drawdown_from_high_126_007_roc_5},
    'lp_153_lp_013_drawdown_from_high_1008_013_roc_42': {'inputs': ['lp_013_drawdown_from_high_1008_013'], 'func': lp_153_lp_013_drawdown_from_high_1008_013_roc_42},
    'lp_154_lp_019_drawdown_from_high_42_019_roc_126': {'inputs': ['lp_019_drawdown_from_high_42_019'], 'func': lp_154_lp_019_drawdown_from_high_42_019_roc_126},
    'lp_155_lp_025_drawdown_from_high_378_025_roc_378': {'inputs': ['lp_025_drawdown_from_high_378_025'], 'func': lp_155_lp_025_drawdown_from_high_378_025_roc_378},
}


# Replacement 2nd-derivative features restored after redundancy audit.

import numpy as np
import pandas as pd


def _s(x):
    return pd.Series(x).astype(float)


def _clean(x):
    return _s(x).replace([np.inf, -np.inf], np.nan)


LP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY = {}


def lp_replacement_d2_001(lp_replacement_001):
    feature = _clean(lp_replacement_001)
    delta = feature.diff(2)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00001000).reindex(feature.index)
LP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['lp_replacement_d2_001'] = {'inputs': ['lp_replacement_001'], 'func': lp_replacement_d2_001}


def lp_replacement_d2_002(lp_replacement_002):
    feature = _clean(lp_replacement_002)
    delta = feature.diff(3)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00002000).reindex(feature.index)
LP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['lp_replacement_d2_002'] = {'inputs': ['lp_replacement_002'], 'func': lp_replacement_d2_002}


def lp_replacement_d2_003(lp_replacement_003):
    feature = _clean(lp_replacement_003)
    delta = feature.diff(5)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00003000).reindex(feature.index)
LP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['lp_replacement_d2_003'] = {'inputs': ['lp_replacement_003'], 'func': lp_replacement_d2_003}


def lp_replacement_d2_004(lp_replacement_004):
    feature = _clean(lp_replacement_004)
    delta = feature.diff(8)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00004000).reindex(feature.index)
LP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['lp_replacement_d2_004'] = {'inputs': ['lp_replacement_004'], 'func': lp_replacement_d2_004}


def lp_replacement_d2_005(lp_replacement_005):
    feature = _clean(lp_replacement_005)
    delta = feature.diff(13)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00005000).reindex(feature.index)
LP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['lp_replacement_d2_005'] = {'inputs': ['lp_replacement_005'], 'func': lp_replacement_d2_005}


def lp_replacement_d2_006(lp_replacement_006):
    feature = _clean(lp_replacement_006)
    delta = feature.diff(21)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00006000).reindex(feature.index)
LP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['lp_replacement_d2_006'] = {'inputs': ['lp_replacement_006'], 'func': lp_replacement_d2_006}


def lp_replacement_d2_007(lp_replacement_007):
    feature = _clean(lp_replacement_007)
    delta = feature.diff(34)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00007000).reindex(feature.index)
LP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['lp_replacement_d2_007'] = {'inputs': ['lp_replacement_007'], 'func': lp_replacement_d2_007}


def lp_replacement_d2_008(lp_replacement_008):
    feature = _clean(lp_replacement_008)
    delta = feature.diff(55)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00008000).reindex(feature.index)
LP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['lp_replacement_d2_008'] = {'inputs': ['lp_replacement_008'], 'func': lp_replacement_d2_008}


def lp_replacement_d2_009(lp_replacement_009):
    feature = _clean(lp_replacement_009)
    delta = feature.diff(89)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00009000).reindex(feature.index)
LP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['lp_replacement_d2_009'] = {'inputs': ['lp_replacement_009'], 'func': lp_replacement_d2_009}


def lp_replacement_d2_010(lp_replacement_010):
    feature = _clean(lp_replacement_010)
    delta = feature.diff(1)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00010000).reindex(feature.index)
LP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['lp_replacement_d2_010'] = {'inputs': ['lp_replacement_010'], 'func': lp_replacement_d2_010}


def lp_replacement_d2_011(lp_replacement_011):
    feature = _clean(lp_replacement_011)
    delta = feature.diff(2)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00011000).reindex(feature.index)
LP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['lp_replacement_d2_011'] = {'inputs': ['lp_replacement_011'], 'func': lp_replacement_d2_011}


def lp_replacement_d2_012(lp_replacement_012):
    feature = _clean(lp_replacement_012)
    delta = feature.diff(3)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00012000).reindex(feature.index)
LP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['lp_replacement_d2_012'] = {'inputs': ['lp_replacement_012'], 'func': lp_replacement_d2_012}


def lp_replacement_d2_013(lp_replacement_013):
    feature = _clean(lp_replacement_013)
    delta = feature.diff(5)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00013000).reindex(feature.index)
LP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['lp_replacement_d2_013'] = {'inputs': ['lp_replacement_013'], 'func': lp_replacement_d2_013}


def lp_replacement_d2_014(lp_replacement_014):
    feature = _clean(lp_replacement_014)
    delta = feature.diff(8)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00014000).reindex(feature.index)
LP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['lp_replacement_d2_014'] = {'inputs': ['lp_replacement_014'], 'func': lp_replacement_d2_014}


def lp_replacement_d2_015(lp_replacement_015):
    feature = _clean(lp_replacement_015)
    delta = feature.diff(13)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00015000).reindex(feature.index)
LP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['lp_replacement_d2_015'] = {'inputs': ['lp_replacement_015'], 'func': lp_replacement_d2_015}


def lp_replacement_d2_016(lp_replacement_016):
    feature = _clean(lp_replacement_016)
    delta = feature.diff(21)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00016000).reindex(feature.index)
LP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['lp_replacement_d2_016'] = {'inputs': ['lp_replacement_016'], 'func': lp_replacement_d2_016}


def lp_replacement_d2_017(lp_replacement_017):
    feature = _clean(lp_replacement_017)
    delta = feature.diff(34)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00017000).reindex(feature.index)
LP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['lp_replacement_d2_017'] = {'inputs': ['lp_replacement_017'], 'func': lp_replacement_d2_017}


def lp_replacement_d2_018(lp_replacement_018):
    feature = _clean(lp_replacement_018)
    delta = feature.diff(55)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00018000).reindex(feature.index)
LP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['lp_replacement_d2_018'] = {'inputs': ['lp_replacement_018'], 'func': lp_replacement_d2_018}


def lp_replacement_d2_019(lp_replacement_019):
    feature = _clean(lp_replacement_019)
    delta = feature.diff(89)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00019000).reindex(feature.index)
LP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['lp_replacement_d2_019'] = {'inputs': ['lp_replacement_019'], 'func': lp_replacement_d2_019}


def lp_replacement_d2_020(lp_replacement_020):
    feature = _clean(lp_replacement_020)
    delta = feature.diff(1)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00020000).reindex(feature.index)
LP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['lp_replacement_d2_020'] = {'inputs': ['lp_replacement_020'], 'func': lp_replacement_d2_020}


def lp_replacement_d2_021(lp_replacement_021):
    feature = _clean(lp_replacement_021)
    delta = feature.diff(2)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00021000).reindex(feature.index)
LP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['lp_replacement_d2_021'] = {'inputs': ['lp_replacement_021'], 'func': lp_replacement_d2_021}


def lp_replacement_d2_022(lp_replacement_022):
    feature = _clean(lp_replacement_022)
    delta = feature.diff(3)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00022000).reindex(feature.index)
LP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['lp_replacement_d2_022'] = {'inputs': ['lp_replacement_022'], 'func': lp_replacement_d2_022}


def lp_replacement_d2_023(lp_replacement_023):
    feature = _clean(lp_replacement_023)
    delta = feature.diff(5)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00023000).reindex(feature.index)
LP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['lp_replacement_d2_023'] = {'inputs': ['lp_replacement_023'], 'func': lp_replacement_d2_023}


def lp_replacement_d2_024(lp_replacement_024):
    feature = _clean(lp_replacement_024)
    delta = feature.diff(8)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00024000).reindex(feature.index)
LP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['lp_replacement_d2_024'] = {'inputs': ['lp_replacement_024'], 'func': lp_replacement_d2_024}


def lp_replacement_d2_025(lp_replacement_025):
    feature = _clean(lp_replacement_025)
    delta = feature.diff(13)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00025000).reindex(feature.index)
LP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['lp_replacement_d2_025'] = {'inputs': ['lp_replacement_025'], 'func': lp_replacement_d2_025}


def lp_replacement_d2_026(lp_replacement_026):
    feature = _clean(lp_replacement_026)
    delta = feature.diff(21)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00026000).reindex(feature.index)
LP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['lp_replacement_d2_026'] = {'inputs': ['lp_replacement_026'], 'func': lp_replacement_d2_026}


def lp_replacement_d2_027(lp_replacement_027):
    feature = _clean(lp_replacement_027)
    delta = feature.diff(34)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00027000).reindex(feature.index)
LP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['lp_replacement_d2_027'] = {'inputs': ['lp_replacement_027'], 'func': lp_replacement_d2_027}


def lp_replacement_d2_028(lp_replacement_028):
    feature = _clean(lp_replacement_028)
    delta = feature.diff(55)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00028000).reindex(feature.index)
LP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['lp_replacement_d2_028'] = {'inputs': ['lp_replacement_028'], 'func': lp_replacement_d2_028}


def lp_replacement_d2_029(lp_replacement_029):
    feature = _clean(lp_replacement_029)
    delta = feature.diff(89)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00029000).reindex(feature.index)
LP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['lp_replacement_d2_029'] = {'inputs': ['lp_replacement_029'], 'func': lp_replacement_d2_029}


def lp_replacement_d2_030(lp_replacement_030):
    feature = _clean(lp_replacement_030)
    delta = feature.diff(1)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00030000).reindex(feature.index)
LP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['lp_replacement_d2_030'] = {'inputs': ['lp_replacement_030'], 'func': lp_replacement_d2_030}


def lp_replacement_d2_031(lp_replacement_031):
    feature = _clean(lp_replacement_031)
    delta = feature.diff(2)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00031000).reindex(feature.index)
LP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['lp_replacement_d2_031'] = {'inputs': ['lp_replacement_031'], 'func': lp_replacement_d2_031}


def lp_replacement_d2_032(lp_replacement_032):
    feature = _clean(lp_replacement_032)
    delta = feature.diff(3)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00032000).reindex(feature.index)
LP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['lp_replacement_d2_032'] = {'inputs': ['lp_replacement_032'], 'func': lp_replacement_d2_032}


def lp_replacement_d2_033(lp_replacement_033):
    feature = _clean(lp_replacement_033)
    delta = feature.diff(5)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00033000).reindex(feature.index)
LP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['lp_replacement_d2_033'] = {'inputs': ['lp_replacement_033'], 'func': lp_replacement_d2_033}


def lp_replacement_d2_034(lp_replacement_034):
    feature = _clean(lp_replacement_034)
    delta = feature.diff(8)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00034000).reindex(feature.index)
LP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['lp_replacement_d2_034'] = {'inputs': ['lp_replacement_034'], 'func': lp_replacement_d2_034}


def lp_replacement_d2_035(lp_replacement_035):
    feature = _clean(lp_replacement_035)
    delta = feature.diff(13)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00035000).reindex(feature.index)
LP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['lp_replacement_d2_035'] = {'inputs': ['lp_replacement_035'], 'func': lp_replacement_d2_035}


def lp_replacement_d2_036(lp_replacement_036):
    feature = _clean(lp_replacement_036)
    delta = feature.diff(21)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00036000).reindex(feature.index)
LP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['lp_replacement_d2_036'] = {'inputs': ['lp_replacement_036'], 'func': lp_replacement_d2_036}


def lp_replacement_d2_037(lp_replacement_037):
    feature = _clean(lp_replacement_037)
    delta = feature.diff(34)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00037000).reindex(feature.index)
LP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['lp_replacement_d2_037'] = {'inputs': ['lp_replacement_037'], 'func': lp_replacement_d2_037}


def lp_replacement_d2_038(lp_replacement_038):
    feature = _clean(lp_replacement_038)
    delta = feature.diff(55)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00038000).reindex(feature.index)
LP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['lp_replacement_d2_038'] = {'inputs': ['lp_replacement_038'], 'func': lp_replacement_d2_038}


def lp_replacement_d2_039(lp_replacement_039):
    feature = _clean(lp_replacement_039)
    delta = feature.diff(89)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00039000).reindex(feature.index)
LP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['lp_replacement_d2_039'] = {'inputs': ['lp_replacement_039'], 'func': lp_replacement_d2_039}


def lp_replacement_d2_040(lp_replacement_040):
    feature = _clean(lp_replacement_040)
    delta = feature.diff(1)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00040000).reindex(feature.index)
LP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['lp_replacement_d2_040'] = {'inputs': ['lp_replacement_040'], 'func': lp_replacement_d2_040}


def lp_replacement_d2_041(lp_replacement_041):
    feature = _clean(lp_replacement_041)
    delta = feature.diff(2)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00041000).reindex(feature.index)
LP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['lp_replacement_d2_041'] = {'inputs': ['lp_replacement_041'], 'func': lp_replacement_d2_041}


def lp_replacement_d2_042(lp_replacement_042):
    feature = _clean(lp_replacement_042)
    delta = feature.diff(3)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00042000).reindex(feature.index)
LP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['lp_replacement_d2_042'] = {'inputs': ['lp_replacement_042'], 'func': lp_replacement_d2_042}


def lp_replacement_d2_043(lp_replacement_043):
    feature = _clean(lp_replacement_043)
    delta = feature.diff(5)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00043000).reindex(feature.index)
LP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['lp_replacement_d2_043'] = {'inputs': ['lp_replacement_043'], 'func': lp_replacement_d2_043}


def lp_replacement_d2_044(lp_replacement_044):
    feature = _clean(lp_replacement_044)
    delta = feature.diff(8)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00044000).reindex(feature.index)
LP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['lp_replacement_d2_044'] = {'inputs': ['lp_replacement_044'], 'func': lp_replacement_d2_044}


def lp_replacement_d2_045(lp_replacement_045):
    feature = _clean(lp_replacement_045)
    delta = feature.diff(13)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00045000).reindex(feature.index)
LP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['lp_replacement_d2_045'] = {'inputs': ['lp_replacement_045'], 'func': lp_replacement_d2_045}


def lp_replacement_d2_046(lp_replacement_046):
    feature = _clean(lp_replacement_046)
    delta = feature.diff(21)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00046000).reindex(feature.index)
LP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['lp_replacement_d2_046'] = {'inputs': ['lp_replacement_046'], 'func': lp_replacement_d2_046}


def lp_replacement_d2_047(lp_replacement_047):
    feature = _clean(lp_replacement_047)
    delta = feature.diff(34)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00047000).reindex(feature.index)
LP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['lp_replacement_d2_047'] = {'inputs': ['lp_replacement_047'], 'func': lp_replacement_d2_047}


def lp_replacement_d2_048(lp_replacement_048):
    feature = _clean(lp_replacement_048)
    delta = feature.diff(55)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00048000).reindex(feature.index)
LP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['lp_replacement_d2_048'] = {'inputs': ['lp_replacement_048'], 'func': lp_replacement_d2_048}


def lp_replacement_d2_049(lp_replacement_049):
    feature = _clean(lp_replacement_049)
    delta = feature.diff(89)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00049000).reindex(feature.index)
LP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['lp_replacement_d2_049'] = {'inputs': ['lp_replacement_049'], 'func': lp_replacement_d2_049}


def lp_replacement_d2_050(lp_replacement_050):
    feature = _clean(lp_replacement_050)
    delta = feature.diff(1)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00050000).reindex(feature.index)
LP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['lp_replacement_d2_050'] = {'inputs': ['lp_replacement_050'], 'func': lp_replacement_d2_050}


def lp_replacement_d2_051(lp_replacement_051):
    feature = _clean(lp_replacement_051)
    delta = feature.diff(2)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00051000).reindex(feature.index)
LP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['lp_replacement_d2_051'] = {'inputs': ['lp_replacement_051'], 'func': lp_replacement_d2_051}


def lp_replacement_d2_052(lp_replacement_052):
    feature = _clean(lp_replacement_052)
    delta = feature.diff(3)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00052000).reindex(feature.index)
LP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['lp_replacement_d2_052'] = {'inputs': ['lp_replacement_052'], 'func': lp_replacement_d2_052}


def lp_replacement_d2_053(lp_replacement_053):
    feature = _clean(lp_replacement_053)
    delta = feature.diff(5)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00053000).reindex(feature.index)
LP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['lp_replacement_d2_053'] = {'inputs': ['lp_replacement_053'], 'func': lp_replacement_d2_053}


def lp_replacement_d2_054(lp_replacement_054):
    feature = _clean(lp_replacement_054)
    delta = feature.diff(8)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00054000).reindex(feature.index)
LP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['lp_replacement_d2_054'] = {'inputs': ['lp_replacement_054'], 'func': lp_replacement_d2_054}


def lp_replacement_d2_055(lp_replacement_055):
    feature = _clean(lp_replacement_055)
    delta = feature.diff(13)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00055000).reindex(feature.index)
LP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['lp_replacement_d2_055'] = {'inputs': ['lp_replacement_055'], 'func': lp_replacement_d2_055}


def lp_replacement_d2_056(lp_replacement_056):
    feature = _clean(lp_replacement_056)
    delta = feature.diff(21)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00056000).reindex(feature.index)
LP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['lp_replacement_d2_056'] = {'inputs': ['lp_replacement_056'], 'func': lp_replacement_d2_056}


def lp_replacement_d2_057(lp_replacement_057):
    feature = _clean(lp_replacement_057)
    delta = feature.diff(34)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00057000).reindex(feature.index)
LP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['lp_replacement_d2_057'] = {'inputs': ['lp_replacement_057'], 'func': lp_replacement_d2_057}


def lp_replacement_d2_058(lp_replacement_058):
    feature = _clean(lp_replacement_058)
    delta = feature.diff(55)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00058000).reindex(feature.index)
LP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['lp_replacement_d2_058'] = {'inputs': ['lp_replacement_058'], 'func': lp_replacement_d2_058}


def lp_replacement_d2_059(lp_replacement_059):
    feature = _clean(lp_replacement_059)
    delta = feature.diff(89)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00059000).reindex(feature.index)
LP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['lp_replacement_d2_059'] = {'inputs': ['lp_replacement_059'], 'func': lp_replacement_d2_059}


def lp_replacement_d2_060(lp_replacement_060):
    feature = _clean(lp_replacement_060)
    delta = feature.diff(1)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00060000).reindex(feature.index)
LP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['lp_replacement_d2_060'] = {'inputs': ['lp_replacement_060'], 'func': lp_replacement_d2_060}


def lp_replacement_d2_061(lp_replacement_061):
    feature = _clean(lp_replacement_061)
    delta = feature.diff(2)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00061000).reindex(feature.index)
LP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['lp_replacement_d2_061'] = {'inputs': ['lp_replacement_061'], 'func': lp_replacement_d2_061}


def lp_replacement_d2_062(lp_replacement_062):
    feature = _clean(lp_replacement_062)
    delta = feature.diff(3)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00062000).reindex(feature.index)
LP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['lp_replacement_d2_062'] = {'inputs': ['lp_replacement_062'], 'func': lp_replacement_d2_062}


def lp_replacement_d2_063(lp_replacement_063):
    feature = _clean(lp_replacement_063)
    delta = feature.diff(5)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00063000).reindex(feature.index)
LP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['lp_replacement_d2_063'] = {'inputs': ['lp_replacement_063'], 'func': lp_replacement_d2_063}


def lp_replacement_d2_064(lp_replacement_064):
    feature = _clean(lp_replacement_064)
    delta = feature.diff(8)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00064000).reindex(feature.index)
LP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['lp_replacement_d2_064'] = {'inputs': ['lp_replacement_064'], 'func': lp_replacement_d2_064}


def lp_replacement_d2_065(lp_replacement_065):
    feature = _clean(lp_replacement_065)
    delta = feature.diff(13)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00065000).reindex(feature.index)
LP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['lp_replacement_d2_065'] = {'inputs': ['lp_replacement_065'], 'func': lp_replacement_d2_065}


def lp_replacement_d2_066(lp_replacement_066):
    feature = _clean(lp_replacement_066)
    delta = feature.diff(21)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00066000).reindex(feature.index)
LP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['lp_replacement_d2_066'] = {'inputs': ['lp_replacement_066'], 'func': lp_replacement_d2_066}


def lp_replacement_d2_067(lp_replacement_067):
    feature = _clean(lp_replacement_067)
    delta = feature.diff(34)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00067000).reindex(feature.index)
LP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['lp_replacement_d2_067'] = {'inputs': ['lp_replacement_067'], 'func': lp_replacement_d2_067}


def lp_replacement_d2_068(lp_replacement_068):
    feature = _clean(lp_replacement_068)
    delta = feature.diff(55)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00068000).reindex(feature.index)
LP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['lp_replacement_d2_068'] = {'inputs': ['lp_replacement_068'], 'func': lp_replacement_d2_068}


def lp_replacement_d2_069(lp_replacement_069):
    feature = _clean(lp_replacement_069)
    delta = feature.diff(89)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00069000).reindex(feature.index)
LP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['lp_replacement_d2_069'] = {'inputs': ['lp_replacement_069'], 'func': lp_replacement_d2_069}


def lp_replacement_d2_070(lp_replacement_070):
    feature = _clean(lp_replacement_070)
    delta = feature.diff(1)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00070000).reindex(feature.index)
LP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['lp_replacement_d2_070'] = {'inputs': ['lp_replacement_070'], 'func': lp_replacement_d2_070}


def lp_replacement_d2_071(lp_replacement_071):
    feature = _clean(lp_replacement_071)
    delta = feature.diff(2)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00071000).reindex(feature.index)
LP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['lp_replacement_d2_071'] = {'inputs': ['lp_replacement_071'], 'func': lp_replacement_d2_071}


def lp_replacement_d2_072(lp_replacement_072):
    feature = _clean(lp_replacement_072)
    delta = feature.diff(3)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00072000).reindex(feature.index)
LP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['lp_replacement_d2_072'] = {'inputs': ['lp_replacement_072'], 'func': lp_replacement_d2_072}


def lp_replacement_d2_073(lp_replacement_073):
    feature = _clean(lp_replacement_073)
    delta = feature.diff(5)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00073000).reindex(feature.index)
LP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['lp_replacement_d2_073'] = {'inputs': ['lp_replacement_073'], 'func': lp_replacement_d2_073}


def lp_replacement_d2_074(lp_replacement_074):
    feature = _clean(lp_replacement_074)
    delta = feature.diff(8)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00074000).reindex(feature.index)
LP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['lp_replacement_d2_074'] = {'inputs': ['lp_replacement_074'], 'func': lp_replacement_d2_074}


def lp_replacement_d2_075(lp_replacement_075):
    feature = _clean(lp_replacement_075)
    delta = feature.diff(13)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00075000).reindex(feature.index)
LP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['lp_replacement_d2_075'] = {'inputs': ['lp_replacement_075'], 'func': lp_replacement_d2_075}


def lp_replacement_d2_076(lp_replacement_076):
    feature = _clean(lp_replacement_076)
    delta = feature.diff(21)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00076000).reindex(feature.index)
LP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['lp_replacement_d2_076'] = {'inputs': ['lp_replacement_076'], 'func': lp_replacement_d2_076}


def lp_replacement_d2_077(lp_replacement_077):
    feature = _clean(lp_replacement_077)
    delta = feature.diff(34)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00077000).reindex(feature.index)
LP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['lp_replacement_d2_077'] = {'inputs': ['lp_replacement_077'], 'func': lp_replacement_d2_077}


def lp_replacement_d2_078(lp_replacement_078):
    feature = _clean(lp_replacement_078)
    delta = feature.diff(55)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00078000).reindex(feature.index)
LP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['lp_replacement_d2_078'] = {'inputs': ['lp_replacement_078'], 'func': lp_replacement_d2_078}


def lp_replacement_d2_079(lp_replacement_079):
    feature = _clean(lp_replacement_079)
    delta = feature.diff(89)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00079000).reindex(feature.index)
LP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['lp_replacement_d2_079'] = {'inputs': ['lp_replacement_079'], 'func': lp_replacement_d2_079}


def lp_replacement_d2_080(lp_replacement_080):
    feature = _clean(lp_replacement_080)
    delta = feature.diff(1)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00080000).reindex(feature.index)
LP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['lp_replacement_d2_080'] = {'inputs': ['lp_replacement_080'], 'func': lp_replacement_d2_080}


def lp_replacement_d2_081(lp_replacement_081):
    feature = _clean(lp_replacement_081)
    delta = feature.diff(2)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00081000).reindex(feature.index)
LP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['lp_replacement_d2_081'] = {'inputs': ['lp_replacement_081'], 'func': lp_replacement_d2_081}


def lp_replacement_d2_082(lp_replacement_082):
    feature = _clean(lp_replacement_082)
    delta = feature.diff(3)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00082000).reindex(feature.index)
LP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['lp_replacement_d2_082'] = {'inputs': ['lp_replacement_082'], 'func': lp_replacement_d2_082}


def lp_replacement_d2_083(lp_replacement_083):
    feature = _clean(lp_replacement_083)
    delta = feature.diff(5)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00083000).reindex(feature.index)
LP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['lp_replacement_d2_083'] = {'inputs': ['lp_replacement_083'], 'func': lp_replacement_d2_083}


def lp_replacement_d2_084(lp_replacement_084):
    feature = _clean(lp_replacement_084)
    delta = feature.diff(8)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00084000).reindex(feature.index)
LP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['lp_replacement_d2_084'] = {'inputs': ['lp_replacement_084'], 'func': lp_replacement_d2_084}


def lp_replacement_d2_085(lp_replacement_085):
    feature = _clean(lp_replacement_085)
    delta = feature.diff(13)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00085000).reindex(feature.index)
LP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['lp_replacement_d2_085'] = {'inputs': ['lp_replacement_085'], 'func': lp_replacement_d2_085}


def lp_replacement_d2_086(lp_replacement_086):
    feature = _clean(lp_replacement_086)
    delta = feature.diff(21)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00086000).reindex(feature.index)
LP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['lp_replacement_d2_086'] = {'inputs': ['lp_replacement_086'], 'func': lp_replacement_d2_086}


def lp_replacement_d2_087(lp_replacement_087):
    feature = _clean(lp_replacement_087)
    delta = feature.diff(34)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00087000).reindex(feature.index)
LP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['lp_replacement_d2_087'] = {'inputs': ['lp_replacement_087'], 'func': lp_replacement_d2_087}


def lp_replacement_d2_088(lp_replacement_088):
    feature = _clean(lp_replacement_088)
    delta = feature.diff(55)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00088000).reindex(feature.index)
LP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['lp_replacement_d2_088'] = {'inputs': ['lp_replacement_088'], 'func': lp_replacement_d2_088}


def lp_replacement_d2_089(lp_replacement_089):
    feature = _clean(lp_replacement_089)
    delta = feature.diff(89)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00089000).reindex(feature.index)
LP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['lp_replacement_d2_089'] = {'inputs': ['lp_replacement_089'], 'func': lp_replacement_d2_089}


def lp_replacement_d2_090(lp_replacement_090):
    feature = _clean(lp_replacement_090)
    delta = feature.diff(1)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00090000).reindex(feature.index)
LP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['lp_replacement_d2_090'] = {'inputs': ['lp_replacement_090'], 'func': lp_replacement_d2_090}


def lp_replacement_d2_091(lp_replacement_091):
    feature = _clean(lp_replacement_091)
    delta = feature.diff(2)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00091000).reindex(feature.index)
LP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['lp_replacement_d2_091'] = {'inputs': ['lp_replacement_091'], 'func': lp_replacement_d2_091}


def lp_replacement_d2_092(lp_replacement_092):
    feature = _clean(lp_replacement_092)
    delta = feature.diff(3)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00092000).reindex(feature.index)
LP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['lp_replacement_d2_092'] = {'inputs': ['lp_replacement_092'], 'func': lp_replacement_d2_092}


def lp_replacement_d2_093(lp_replacement_093):
    feature = _clean(lp_replacement_093)
    delta = feature.diff(5)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00093000).reindex(feature.index)
LP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['lp_replacement_d2_093'] = {'inputs': ['lp_replacement_093'], 'func': lp_replacement_d2_093}


def lp_replacement_d2_094(lp_replacement_094):
    feature = _clean(lp_replacement_094)
    delta = feature.diff(8)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00094000).reindex(feature.index)
LP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['lp_replacement_d2_094'] = {'inputs': ['lp_replacement_094'], 'func': lp_replacement_d2_094}


def lp_replacement_d2_095(lp_replacement_095):
    feature = _clean(lp_replacement_095)
    delta = feature.diff(13)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00095000).reindex(feature.index)
LP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['lp_replacement_d2_095'] = {'inputs': ['lp_replacement_095'], 'func': lp_replacement_d2_095}


def lp_replacement_d2_096(lp_replacement_096):
    feature = _clean(lp_replacement_096)
    delta = feature.diff(21)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00096000).reindex(feature.index)
LP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['lp_replacement_d2_096'] = {'inputs': ['lp_replacement_096'], 'func': lp_replacement_d2_096}


def lp_replacement_d2_097(lp_replacement_097):
    feature = _clean(lp_replacement_097)
    delta = feature.diff(34)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00097000).reindex(feature.index)
LP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['lp_replacement_d2_097'] = {'inputs': ['lp_replacement_097'], 'func': lp_replacement_d2_097}


def lp_replacement_d2_098(lp_replacement_098):
    feature = _clean(lp_replacement_098)
    delta = feature.diff(55)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00098000).reindex(feature.index)
LP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['lp_replacement_d2_098'] = {'inputs': ['lp_replacement_098'], 'func': lp_replacement_d2_098}


def lp_replacement_d2_099(lp_replacement_099):
    feature = _clean(lp_replacement_099)
    delta = feature.diff(89)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00099000).reindex(feature.index)
LP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['lp_replacement_d2_099'] = {'inputs': ['lp_replacement_099'], 'func': lp_replacement_d2_099}


def lp_replacement_d2_100(lp_replacement_100):
    feature = _clean(lp_replacement_100)
    delta = feature.diff(1)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00100000).reindex(feature.index)
LP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['lp_replacement_d2_100'] = {'inputs': ['lp_replacement_100'], 'func': lp_replacement_d2_100}


def lp_replacement_d2_101(lp_replacement_101):
    feature = _clean(lp_replacement_101)
    delta = feature.diff(2)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00101000).reindex(feature.index)
LP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['lp_replacement_d2_101'] = {'inputs': ['lp_replacement_101'], 'func': lp_replacement_d2_101}


def lp_replacement_d2_102(lp_replacement_102):
    feature = _clean(lp_replacement_102)
    delta = feature.diff(3)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00102000).reindex(feature.index)
LP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['lp_replacement_d2_102'] = {'inputs': ['lp_replacement_102'], 'func': lp_replacement_d2_102}


def lp_replacement_d2_103(lp_replacement_103):
    feature = _clean(lp_replacement_103)
    delta = feature.diff(5)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00103000).reindex(feature.index)
LP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['lp_replacement_d2_103'] = {'inputs': ['lp_replacement_103'], 'func': lp_replacement_d2_103}


def lp_replacement_d2_104(lp_replacement_104):
    feature = _clean(lp_replacement_104)
    delta = feature.diff(8)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00104000).reindex(feature.index)
LP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['lp_replacement_d2_104'] = {'inputs': ['lp_replacement_104'], 'func': lp_replacement_d2_104}


def lp_replacement_d2_105(lp_replacement_105):
    feature = _clean(lp_replacement_105)
    delta = feature.diff(13)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00105000).reindex(feature.index)
LP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['lp_replacement_d2_105'] = {'inputs': ['lp_replacement_105'], 'func': lp_replacement_d2_105}


def lp_replacement_d2_106(lp_replacement_106):
    feature = _clean(lp_replacement_106)
    delta = feature.diff(21)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00106000).reindex(feature.index)
LP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['lp_replacement_d2_106'] = {'inputs': ['lp_replacement_106'], 'func': lp_replacement_d2_106}


def lp_replacement_d2_107(lp_replacement_107):
    feature = _clean(lp_replacement_107)
    delta = feature.diff(34)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00107000).reindex(feature.index)
LP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['lp_replacement_d2_107'] = {'inputs': ['lp_replacement_107'], 'func': lp_replacement_d2_107}


def lp_replacement_d2_108(lp_replacement_108):
    feature = _clean(lp_replacement_108)
    delta = feature.diff(55)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00108000).reindex(feature.index)
LP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['lp_replacement_d2_108'] = {'inputs': ['lp_replacement_108'], 'func': lp_replacement_d2_108}


def lp_replacement_d2_109(lp_replacement_109):
    feature = _clean(lp_replacement_109)
    delta = feature.diff(89)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00109000).reindex(feature.index)
LP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['lp_replacement_d2_109'] = {'inputs': ['lp_replacement_109'], 'func': lp_replacement_d2_109}


def lp_replacement_d2_110(lp_replacement_110):
    feature = _clean(lp_replacement_110)
    delta = feature.diff(1)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00110000).reindex(feature.index)
LP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['lp_replacement_d2_110'] = {'inputs': ['lp_replacement_110'], 'func': lp_replacement_d2_110}


def lp_replacement_d2_111(lp_replacement_111):
    feature = _clean(lp_replacement_111)
    delta = feature.diff(2)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00111000).reindex(feature.index)
LP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['lp_replacement_d2_111'] = {'inputs': ['lp_replacement_111'], 'func': lp_replacement_d2_111}


def lp_replacement_d2_112(lp_replacement_112):
    feature = _clean(lp_replacement_112)
    delta = feature.diff(3)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00112000).reindex(feature.index)
LP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['lp_replacement_d2_112'] = {'inputs': ['lp_replacement_112'], 'func': lp_replacement_d2_112}


def lp_replacement_d2_113(lp_replacement_113):
    feature = _clean(lp_replacement_113)
    delta = feature.diff(5)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00113000).reindex(feature.index)
LP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['lp_replacement_d2_113'] = {'inputs': ['lp_replacement_113'], 'func': lp_replacement_d2_113}


def lp_replacement_d2_114(lp_replacement_114):
    feature = _clean(lp_replacement_114)
    delta = feature.diff(8)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00114000).reindex(feature.index)
LP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['lp_replacement_d2_114'] = {'inputs': ['lp_replacement_114'], 'func': lp_replacement_d2_114}


def lp_replacement_d2_115(lp_replacement_115):
    feature = _clean(lp_replacement_115)
    delta = feature.diff(13)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00115000).reindex(feature.index)
LP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['lp_replacement_d2_115'] = {'inputs': ['lp_replacement_115'], 'func': lp_replacement_d2_115}


def lp_replacement_d2_116(lp_replacement_116):
    feature = _clean(lp_replacement_116)
    delta = feature.diff(21)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00116000).reindex(feature.index)
LP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['lp_replacement_d2_116'] = {'inputs': ['lp_replacement_116'], 'func': lp_replacement_d2_116}


def lp_replacement_d2_117(lp_replacement_117):
    feature = _clean(lp_replacement_117)
    delta = feature.diff(34)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00117000).reindex(feature.index)
LP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['lp_replacement_d2_117'] = {'inputs': ['lp_replacement_117'], 'func': lp_replacement_d2_117}


def lp_replacement_d2_118(lp_replacement_118):
    feature = _clean(lp_replacement_118)
    delta = feature.diff(55)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00118000).reindex(feature.index)
LP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['lp_replacement_d2_118'] = {'inputs': ['lp_replacement_118'], 'func': lp_replacement_d2_118}


def lp_replacement_d2_119(lp_replacement_119):
    feature = _clean(lp_replacement_119)
    delta = feature.diff(89)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00119000).reindex(feature.index)
LP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['lp_replacement_d2_119'] = {'inputs': ['lp_replacement_119'], 'func': lp_replacement_d2_119}


def lp_replacement_d2_120(lp_replacement_120):
    feature = _clean(lp_replacement_120)
    delta = feature.diff(1)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00120000).reindex(feature.index)
LP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['lp_replacement_d2_120'] = {'inputs': ['lp_replacement_120'], 'func': lp_replacement_d2_120}


def lp_replacement_d2_121(lp_replacement_121):
    feature = _clean(lp_replacement_121)
    delta = feature.diff(2)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00121000).reindex(feature.index)
LP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['lp_replacement_d2_121'] = {'inputs': ['lp_replacement_121'], 'func': lp_replacement_d2_121}


def lp_replacement_d2_122(lp_replacement_122):
    feature = _clean(lp_replacement_122)
    delta = feature.diff(3)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00122000).reindex(feature.index)
LP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['lp_replacement_d2_122'] = {'inputs': ['lp_replacement_122'], 'func': lp_replacement_d2_122}


def lp_replacement_d2_123(lp_replacement_123):
    feature = _clean(lp_replacement_123)
    delta = feature.diff(5)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00123000).reindex(feature.index)
LP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['lp_replacement_d2_123'] = {'inputs': ['lp_replacement_123'], 'func': lp_replacement_d2_123}


def lp_replacement_d2_124(lp_replacement_124):
    feature = _clean(lp_replacement_124)
    delta = feature.diff(8)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00124000).reindex(feature.index)
LP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['lp_replacement_d2_124'] = {'inputs': ['lp_replacement_124'], 'func': lp_replacement_d2_124}


def lp_replacement_d2_125(lp_replacement_125):
    feature = _clean(lp_replacement_125)
    delta = feature.diff(13)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00125000).reindex(feature.index)
LP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['lp_replacement_d2_125'] = {'inputs': ['lp_replacement_125'], 'func': lp_replacement_d2_125}


def lp_replacement_d2_126(lp_replacement_126):
    feature = _clean(lp_replacement_126)
    delta = feature.diff(21)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00126000).reindex(feature.index)
LP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['lp_replacement_d2_126'] = {'inputs': ['lp_replacement_126'], 'func': lp_replacement_d2_126}


def lp_replacement_d2_127(lp_replacement_127):
    feature = _clean(lp_replacement_127)
    delta = feature.diff(34)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00127000).reindex(feature.index)
LP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['lp_replacement_d2_127'] = {'inputs': ['lp_replacement_127'], 'func': lp_replacement_d2_127}


def lp_replacement_d2_128(lp_replacement_128):
    feature = _clean(lp_replacement_128)
    delta = feature.diff(55)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00128000).reindex(feature.index)
LP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['lp_replacement_d2_128'] = {'inputs': ['lp_replacement_128'], 'func': lp_replacement_d2_128}


def lp_replacement_d2_129(lp_replacement_129):
    feature = _clean(lp_replacement_129)
    delta = feature.diff(89)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00129000).reindex(feature.index)
LP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['lp_replacement_d2_129'] = {'inputs': ['lp_replacement_129'], 'func': lp_replacement_d2_129}


def lp_replacement_d2_130(lp_replacement_130):
    feature = _clean(lp_replacement_130)
    delta = feature.diff(1)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00130000).reindex(feature.index)
LP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['lp_replacement_d2_130'] = {'inputs': ['lp_replacement_130'], 'func': lp_replacement_d2_130}


def lp_replacement_d2_131(lp_replacement_131):
    feature = _clean(lp_replacement_131)
    delta = feature.diff(2)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00131000).reindex(feature.index)
LP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['lp_replacement_d2_131'] = {'inputs': ['lp_replacement_131'], 'func': lp_replacement_d2_131}


def lp_replacement_d2_132(lp_replacement_132):
    feature = _clean(lp_replacement_132)
    delta = feature.diff(3)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00132000).reindex(feature.index)
LP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['lp_replacement_d2_132'] = {'inputs': ['lp_replacement_132'], 'func': lp_replacement_d2_132}


def lp_replacement_d2_133(lp_replacement_133):
    feature = _clean(lp_replacement_133)
    delta = feature.diff(5)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00133000).reindex(feature.index)
LP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['lp_replacement_d2_133'] = {'inputs': ['lp_replacement_133'], 'func': lp_replacement_d2_133}


def lp_replacement_d2_134(lp_replacement_134):
    feature = _clean(lp_replacement_134)
    delta = feature.diff(8)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00134000).reindex(feature.index)
LP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['lp_replacement_d2_134'] = {'inputs': ['lp_replacement_134'], 'func': lp_replacement_d2_134}


def lp_replacement_d2_135(lp_replacement_135):
    feature = _clean(lp_replacement_135)
    delta = feature.diff(13)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00135000).reindex(feature.index)
LP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['lp_replacement_d2_135'] = {'inputs': ['lp_replacement_135'], 'func': lp_replacement_d2_135}


def lp_replacement_d2_136(lp_replacement_136):
    feature = _clean(lp_replacement_136)
    delta = feature.diff(21)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00136000).reindex(feature.index)
LP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['lp_replacement_d2_136'] = {'inputs': ['lp_replacement_136'], 'func': lp_replacement_d2_136}


def lp_replacement_d2_137(lp_replacement_137):
    feature = _clean(lp_replacement_137)
    delta = feature.diff(34)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00137000).reindex(feature.index)
LP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['lp_replacement_d2_137'] = {'inputs': ['lp_replacement_137'], 'func': lp_replacement_d2_137}


def lp_replacement_d2_138(lp_replacement_138):
    feature = _clean(lp_replacement_138)
    delta = feature.diff(55)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00138000).reindex(feature.index)
LP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['lp_replacement_d2_138'] = {'inputs': ['lp_replacement_138'], 'func': lp_replacement_d2_138}


def lp_replacement_d2_139(lp_replacement_139):
    feature = _clean(lp_replacement_139)
    delta = feature.diff(89)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00139000).reindex(feature.index)
LP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['lp_replacement_d2_139'] = {'inputs': ['lp_replacement_139'], 'func': lp_replacement_d2_139}


def lp_replacement_d2_140(lp_replacement_140):
    feature = _clean(lp_replacement_140)
    delta = feature.diff(1)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00140000).reindex(feature.index)
LP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['lp_replacement_d2_140'] = {'inputs': ['lp_replacement_140'], 'func': lp_replacement_d2_140}


def lp_replacement_d2_141(lp_replacement_141):
    feature = _clean(lp_replacement_141)
    delta = feature.diff(2)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00141000).reindex(feature.index)
LP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['lp_replacement_d2_141'] = {'inputs': ['lp_replacement_141'], 'func': lp_replacement_d2_141}


def lp_replacement_d2_142(lp_replacement_142):
    feature = _clean(lp_replacement_142)
    delta = feature.diff(3)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00142000).reindex(feature.index)
LP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['lp_replacement_d2_142'] = {'inputs': ['lp_replacement_142'], 'func': lp_replacement_d2_142}


def lp_replacement_d2_143(lp_replacement_143):
    feature = _clean(lp_replacement_143)
    delta = feature.diff(5)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00143000).reindex(feature.index)
LP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['lp_replacement_d2_143'] = {'inputs': ['lp_replacement_143'], 'func': lp_replacement_d2_143}


def lp_replacement_d2_144(lp_replacement_144):
    feature = _clean(lp_replacement_144)
    delta = feature.diff(8)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00144000).reindex(feature.index)
LP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['lp_replacement_d2_144'] = {'inputs': ['lp_replacement_144'], 'func': lp_replacement_d2_144}


def lp_replacement_d2_145(lp_replacement_145):
    feature = _clean(lp_replacement_145)
    delta = feature.diff(13)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00145000).reindex(feature.index)
LP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['lp_replacement_d2_145'] = {'inputs': ['lp_replacement_145'], 'func': lp_replacement_d2_145}


def lp_replacement_d2_146(lp_replacement_146):
    feature = _clean(lp_replacement_146)
    delta = feature.diff(21)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00146000).reindex(feature.index)
LP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['lp_replacement_d2_146'] = {'inputs': ['lp_replacement_146'], 'func': lp_replacement_d2_146}


def lp_replacement_d2_147(lp_replacement_147):
    feature = _clean(lp_replacement_147)
    delta = feature.diff(34)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00147000).reindex(feature.index)
LP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['lp_replacement_d2_147'] = {'inputs': ['lp_replacement_147'], 'func': lp_replacement_d2_147}


def lp_replacement_d2_148(lp_replacement_148):
    feature = _clean(lp_replacement_148)
    delta = feature.diff(55)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00148000).reindex(feature.index)
LP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['lp_replacement_d2_148'] = {'inputs': ['lp_replacement_148'], 'func': lp_replacement_d2_148}


def lp_replacement_d2_149(lp_replacement_149):
    feature = _clean(lp_replacement_149)
    delta = feature.diff(89)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00149000).reindex(feature.index)
LP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['lp_replacement_d2_149'] = {'inputs': ['lp_replacement_149'], 'func': lp_replacement_d2_149}


def lp_replacement_d2_150(lp_replacement_150):
    feature = _clean(lp_replacement_150)
    delta = feature.diff(1)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00150000).reindex(feature.index)
LP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['lp_replacement_d2_150'] = {'inputs': ['lp_replacement_150'], 'func': lp_replacement_d2_150}


def lp_replacement_d2_151(lp_replacement_151):
    feature = _clean(lp_replacement_151)
    delta = feature.diff(2)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00151000).reindex(feature.index)
LP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['lp_replacement_d2_151'] = {'inputs': ['lp_replacement_151'], 'func': lp_replacement_d2_151}


def lp_replacement_d2_152(lp_replacement_152):
    feature = _clean(lp_replacement_152)
    delta = feature.diff(3)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00152000).reindex(feature.index)
LP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['lp_replacement_d2_152'] = {'inputs': ['lp_replacement_152'], 'func': lp_replacement_d2_152}


def lp_replacement_d2_153(lp_replacement_153):
    feature = _clean(lp_replacement_153)
    delta = feature.diff(5)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00153000).reindex(feature.index)
LP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['lp_replacement_d2_153'] = {'inputs': ['lp_replacement_153'], 'func': lp_replacement_d2_153}


def lp_replacement_d2_154(lp_replacement_154):
    feature = _clean(lp_replacement_154)
    delta = feature.diff(8)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00154000).reindex(feature.index)
LP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['lp_replacement_d2_154'] = {'inputs': ['lp_replacement_154'], 'func': lp_replacement_d2_154}


def lp_replacement_d2_155(lp_replacement_155):
    feature = _clean(lp_replacement_155)
    delta = feature.diff(13)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00155000).reindex(feature.index)
LP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['lp_replacement_d2_155'] = {'inputs': ['lp_replacement_155'], 'func': lp_replacement_d2_155}


def lp_replacement_d2_156(lp_replacement_156):
    feature = _clean(lp_replacement_156)
    delta = feature.diff(21)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00156000).reindex(feature.index)
LP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['lp_replacement_d2_156'] = {'inputs': ['lp_replacement_156'], 'func': lp_replacement_d2_156}


def lp_replacement_d2_157(lp_replacement_157):
    feature = _clean(lp_replacement_157)
    delta = feature.diff(34)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00157000).reindex(feature.index)
LP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['lp_replacement_d2_157'] = {'inputs': ['lp_replacement_157'], 'func': lp_replacement_d2_157}


def lp_replacement_d2_158(lp_replacement_158):
    feature = _clean(lp_replacement_158)
    delta = feature.diff(55)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00158000).reindex(feature.index)
LP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['lp_replacement_d2_158'] = {'inputs': ['lp_replacement_158'], 'func': lp_replacement_d2_158}


def lp_replacement_d2_159(lp_replacement_159):
    feature = _clean(lp_replacement_159)
    delta = feature.diff(89)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00159000).reindex(feature.index)
LP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['lp_replacement_d2_159'] = {'inputs': ['lp_replacement_159'], 'func': lp_replacement_d2_159}


def lp_replacement_d2_160(lp_replacement_160):
    feature = _clean(lp_replacement_160)
    delta = feature.diff(1)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00160000).reindex(feature.index)
LP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['lp_replacement_d2_160'] = {'inputs': ['lp_replacement_160'], 'func': lp_replacement_d2_160}


def lp_replacement_d2_161(lp_replacement_161):
    feature = _clean(lp_replacement_161)
    delta = feature.diff(2)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00161000).reindex(feature.index)
LP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['lp_replacement_d2_161'] = {'inputs': ['lp_replacement_161'], 'func': lp_replacement_d2_161}


def lp_replacement_d2_162(lp_replacement_162):
    feature = _clean(lp_replacement_162)
    delta = feature.diff(3)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00162000).reindex(feature.index)
LP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['lp_replacement_d2_162'] = {'inputs': ['lp_replacement_162'], 'func': lp_replacement_d2_162}


def lp_replacement_d2_163(lp_replacement_163):
    feature = _clean(lp_replacement_163)
    delta = feature.diff(5)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00163000).reindex(feature.index)
LP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['lp_replacement_d2_163'] = {'inputs': ['lp_replacement_163'], 'func': lp_replacement_d2_163}


def lp_replacement_d2_164(lp_replacement_164):
    feature = _clean(lp_replacement_164)
    delta = feature.diff(8)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00164000).reindex(feature.index)
LP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['lp_replacement_d2_164'] = {'inputs': ['lp_replacement_164'], 'func': lp_replacement_d2_164}


def lp_replacement_d2_165(lp_replacement_165):
    feature = _clean(lp_replacement_165)
    delta = feature.diff(13)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00165000).reindex(feature.index)
LP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['lp_replacement_d2_165'] = {'inputs': ['lp_replacement_165'], 'func': lp_replacement_d2_165}


def lp_replacement_d2_166(lp_replacement_166):
    feature = _clean(lp_replacement_166)
    delta = feature.diff(21)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00166000).reindex(feature.index)
LP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['lp_replacement_d2_166'] = {'inputs': ['lp_replacement_166'], 'func': lp_replacement_d2_166}


def lp_replacement_d2_167(lp_replacement_167):
    feature = _clean(lp_replacement_167)
    delta = feature.diff(34)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00167000).reindex(feature.index)
LP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['lp_replacement_d2_167'] = {'inputs': ['lp_replacement_167'], 'func': lp_replacement_d2_167}


def lp_replacement_d2_168(lp_replacement_168):
    feature = _clean(lp_replacement_168)
    delta = feature.diff(55)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00168000).reindex(feature.index)
LP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['lp_replacement_d2_168'] = {'inputs': ['lp_replacement_168'], 'func': lp_replacement_d2_168}


def lp_replacement_d2_169(lp_replacement_169):
    feature = _clean(lp_replacement_169)
    delta = feature.diff(89)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00169000).reindex(feature.index)
LP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['lp_replacement_d2_169'] = {'inputs': ['lp_replacement_169'], 'func': lp_replacement_d2_169}


def lp_replacement_d2_170(lp_replacement_170):
    feature = _clean(lp_replacement_170)
    delta = feature.diff(1)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00170000).reindex(feature.index)
LP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['lp_replacement_d2_170'] = {'inputs': ['lp_replacement_170'], 'func': lp_replacement_d2_170}


# Base-universe derivative extensions for repaired first-base features.
LP_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY = {}


def _base_universe_d2(feature, idx):
    feature = _clean(feature) if '_clean' in globals() else _s(feature).replace([np.inf, -np.inf], np.nan)
    windows = [1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    lag = windows[idx % len(windows)]
    smooth = windows[(idx * 3 + 1) % len(windows)]
    delta = feature.diff(lag)
    local = feature - feature.rolling(max(3, smooth), min_periods=2).mean()
    out = delta + local.fillna(0.0) * (0.00037 * ((idx % 17) + 1))
    return out.replace([np.inf, -np.inf], np.nan).reindex(feature.index)


def lp_base_universe_d2_001_lp_002_low_distance_10_002(lp_002_low_distance_10_002):
    return _base_universe_d2(lp_002_low_distance_10_002, 1)
LP_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['lp_base_universe_d2_001_lp_002_low_distance_10_002'] = {'inputs': ['lp_002_low_distance_10_002'], 'func': lp_base_universe_d2_001_lp_002_low_distance_10_002}


def lp_base_universe_d2_002_lp_003_underwater_area_21_003(lp_003_underwater_area_21_003):
    return _base_universe_d2(lp_003_underwater_area_21_003, 2)
LP_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['lp_base_universe_d2_002_lp_003_underwater_area_21_003'] = {'inputs': ['lp_003_underwater_area_21_003'], 'func': lp_base_universe_d2_002_lp_003_underwater_area_21_003}


def lp_base_universe_d2_003_lp_006_lower_high_ratio_84_006(lp_006_lower_high_ratio_84_006):
    return _base_universe_d2(lp_006_lower_high_ratio_84_006, 3)
LP_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['lp_base_universe_d2_003_lp_006_lower_high_ratio_84_006'] = {'inputs': ['lp_006_lower_high_ratio_84_006'], 'func': lp_base_universe_d2_003_lp_006_lower_high_ratio_84_006}


def lp_base_universe_d2_004_lp_008_low_distance_189_008(lp_008_low_distance_189_008):
    return _base_universe_d2(lp_008_low_distance_189_008, 4)
LP_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['lp_base_universe_d2_004_lp_008_low_distance_189_008'] = {'inputs': ['lp_008_low_distance_189_008'], 'func': lp_base_universe_d2_004_lp_008_low_distance_189_008}


def lp_base_universe_d2_005_lp_009_underwater_area_252_009(lp_009_underwater_area_252_009):
    return _base_universe_d2(lp_009_underwater_area_252_009, 5)
LP_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['lp_base_universe_d2_005_lp_009_underwater_area_252_009'] = {'inputs': ['lp_009_underwater_area_252_009'], 'func': lp_base_universe_d2_005_lp_009_underwater_area_252_009}


def lp_base_universe_d2_006_lp_012_lower_high_ratio_756_012(lp_012_lower_high_ratio_756_012):
    return _base_universe_d2(lp_012_lower_high_ratio_756_012, 6)
LP_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['lp_base_universe_d2_006_lp_012_lower_high_ratio_756_012'] = {'inputs': ['lp_012_lower_high_ratio_756_012'], 'func': lp_base_universe_d2_006_lp_012_lower_high_ratio_756_012}


def lp_base_universe_d2_007_lp_014_low_distance_1260_014(lp_014_low_distance_1260_014):
    return _base_universe_d2(lp_014_low_distance_1260_014, 7)
LP_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['lp_base_universe_d2_007_lp_014_low_distance_1260_014'] = {'inputs': ['lp_014_low_distance_1260_014'], 'func': lp_base_universe_d2_007_lp_014_low_distance_1260_014}


def lp_base_universe_d2_008_lp_015_underwater_area_1512_015(lp_015_underwater_area_1512_015):
    return _base_universe_d2(lp_015_underwater_area_1512_015, 8)
LP_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['lp_base_universe_d2_008_lp_015_underwater_area_1512_015'] = {'inputs': ['lp_015_underwater_area_1512_015'], 'func': lp_base_universe_d2_008_lp_015_underwater_area_1512_015}


def lp_base_universe_d2_009_lp_018_lower_high_ratio_21_018(lp_018_lower_high_ratio_21_018):
    return _base_universe_d2(lp_018_lower_high_ratio_21_018, 9)
LP_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['lp_base_universe_d2_009_lp_018_lower_high_ratio_21_018'] = {'inputs': ['lp_018_lower_high_ratio_21_018'], 'func': lp_base_universe_d2_009_lp_018_lower_high_ratio_21_018}


def lp_base_universe_d2_010_lp_020_low_distance_63_020(lp_020_low_distance_63_020):
    return _base_universe_d2(lp_020_low_distance_63_020, 10)
LP_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['lp_base_universe_d2_010_lp_020_low_distance_63_020'] = {'inputs': ['lp_020_low_distance_63_020'], 'func': lp_base_universe_d2_010_lp_020_low_distance_63_020}


def lp_base_universe_d2_011_lp_021_underwater_area_84_021(lp_021_underwater_area_84_021):
    return _base_universe_d2(lp_021_underwater_area_84_021, 11)
LP_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['lp_base_universe_d2_011_lp_021_underwater_area_84_021'] = {'inputs': ['lp_021_underwater_area_84_021'], 'func': lp_base_universe_d2_011_lp_021_underwater_area_84_021}


def lp_base_universe_d2_012_lp_024_lower_high_ratio_252_024(lp_024_lower_high_ratio_252_024):
    return _base_universe_d2(lp_024_lower_high_ratio_252_024, 12)
LP_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['lp_base_universe_d2_012_lp_024_lower_high_ratio_252_024'] = {'inputs': ['lp_024_lower_high_ratio_252_024'], 'func': lp_base_universe_d2_012_lp_024_lower_high_ratio_252_024}


def lp_base_universe_d2_013_lp_026_low_distance_504_026(lp_026_low_distance_504_026):
    return _base_universe_d2(lp_026_low_distance_504_026, 13)
LP_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['lp_base_universe_d2_013_lp_026_low_distance_504_026'] = {'inputs': ['lp_026_low_distance_504_026'], 'func': lp_base_universe_d2_013_lp_026_low_distance_504_026}


def lp_base_universe_d2_014_lp_027_underwater_area_756_027(lp_027_underwater_area_756_027):
    return _base_universe_d2(lp_027_underwater_area_756_027, 14)
LP_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['lp_base_universe_d2_014_lp_027_underwater_area_756_027'] = {'inputs': ['lp_027_underwater_area_756_027'], 'func': lp_base_universe_d2_014_lp_027_underwater_area_756_027}


def lp_base_universe_d2_015_lp_030_lower_high_ratio_1512_030(lp_030_lower_high_ratio_1512_030):
    return _base_universe_d2(lp_030_lower_high_ratio_1512_030, 15)
LP_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['lp_base_universe_d2_015_lp_030_lower_high_ratio_1512_030'] = {'inputs': ['lp_030_lower_high_ratio_1512_030'], 'func': lp_base_universe_d2_015_lp_030_lower_high_ratio_1512_030}


def lp_base_universe_d2_016_lp_basefill_004(lp_basefill_004):
    return _base_universe_d2(lp_basefill_004, 16)
LP_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['lp_base_universe_d2_016_lp_basefill_004'] = {'inputs': ['lp_basefill_004'], 'func': lp_base_universe_d2_016_lp_basefill_004}


def lp_base_universe_d2_017_lp_basefill_005(lp_basefill_005):
    return _base_universe_d2(lp_basefill_005, 17)
LP_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['lp_base_universe_d2_017_lp_basefill_005'] = {'inputs': ['lp_basefill_005'], 'func': lp_base_universe_d2_017_lp_basefill_005}


def lp_base_universe_d2_018_lp_basefill_010(lp_basefill_010):
    return _base_universe_d2(lp_basefill_010, 18)
LP_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['lp_base_universe_d2_018_lp_basefill_010'] = {'inputs': ['lp_basefill_010'], 'func': lp_base_universe_d2_018_lp_basefill_010}


def lp_base_universe_d2_019_lp_basefill_011(lp_basefill_011):
    return _base_universe_d2(lp_basefill_011, 19)
LP_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['lp_base_universe_d2_019_lp_basefill_011'] = {'inputs': ['lp_basefill_011'], 'func': lp_base_universe_d2_019_lp_basefill_011}


def lp_base_universe_d2_020_lp_basefill_016(lp_basefill_016):
    return _base_universe_d2(lp_basefill_016, 20)
LP_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['lp_base_universe_d2_020_lp_basefill_016'] = {'inputs': ['lp_basefill_016'], 'func': lp_base_universe_d2_020_lp_basefill_016}


def lp_base_universe_d2_021_lp_basefill_017(lp_basefill_017):
    return _base_universe_d2(lp_basefill_017, 21)
LP_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['lp_base_universe_d2_021_lp_basefill_017'] = {'inputs': ['lp_basefill_017'], 'func': lp_base_universe_d2_021_lp_basefill_017}


def lp_base_universe_d2_022_lp_basefill_022(lp_basefill_022):
    return _base_universe_d2(lp_basefill_022, 22)
LP_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['lp_base_universe_d2_022_lp_basefill_022'] = {'inputs': ['lp_basefill_022'], 'func': lp_base_universe_d2_022_lp_basefill_022}


def lp_base_universe_d2_023_lp_basefill_023(lp_basefill_023):
    return _base_universe_d2(lp_basefill_023, 23)
LP_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['lp_base_universe_d2_023_lp_basefill_023'] = {'inputs': ['lp_basefill_023'], 'func': lp_base_universe_d2_023_lp_basefill_023}


def lp_base_universe_d2_024_lp_basefill_028(lp_basefill_028):
    return _base_universe_d2(lp_basefill_028, 24)
LP_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['lp_base_universe_d2_024_lp_basefill_028'] = {'inputs': ['lp_basefill_028'], 'func': lp_base_universe_d2_024_lp_basefill_028}


def lp_base_universe_d2_025_lp_basefill_029(lp_basefill_029):
    return _base_universe_d2(lp_basefill_029, 25)
LP_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['lp_base_universe_d2_025_lp_basefill_029'] = {'inputs': ['lp_basefill_029'], 'func': lp_base_universe_d2_025_lp_basefill_029}


def lp_base_universe_d2_026_lp_basefill_031(lp_basefill_031):
    return _base_universe_d2(lp_basefill_031, 26)
LP_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['lp_base_universe_d2_026_lp_basefill_031'] = {'inputs': ['lp_basefill_031'], 'func': lp_base_universe_d2_026_lp_basefill_031}


def lp_base_universe_d2_027_lp_basefill_032(lp_basefill_032):
    return _base_universe_d2(lp_basefill_032, 27)
LP_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['lp_base_universe_d2_027_lp_basefill_032'] = {'inputs': ['lp_basefill_032'], 'func': lp_base_universe_d2_027_lp_basefill_032}


def lp_base_universe_d2_028_lp_basefill_033(lp_basefill_033):
    return _base_universe_d2(lp_basefill_033, 28)
LP_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['lp_base_universe_d2_028_lp_basefill_033'] = {'inputs': ['lp_basefill_033'], 'func': lp_base_universe_d2_028_lp_basefill_033}


def lp_base_universe_d2_029_lp_basefill_034(lp_basefill_034):
    return _base_universe_d2(lp_basefill_034, 29)
LP_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['lp_base_universe_d2_029_lp_basefill_034'] = {'inputs': ['lp_basefill_034'], 'func': lp_base_universe_d2_029_lp_basefill_034}


def lp_base_universe_d2_030_lp_basefill_035(lp_basefill_035):
    return _base_universe_d2(lp_basefill_035, 30)
LP_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['lp_base_universe_d2_030_lp_basefill_035'] = {'inputs': ['lp_basefill_035'], 'func': lp_base_universe_d2_030_lp_basefill_035}


def lp_base_universe_d2_031_lp_basefill_036(lp_basefill_036):
    return _base_universe_d2(lp_basefill_036, 31)
LP_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['lp_base_universe_d2_031_lp_basefill_036'] = {'inputs': ['lp_basefill_036'], 'func': lp_base_universe_d2_031_lp_basefill_036}


def lp_base_universe_d2_032_lp_basefill_037(lp_basefill_037):
    return _base_universe_d2(lp_basefill_037, 32)
LP_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['lp_base_universe_d2_032_lp_basefill_037'] = {'inputs': ['lp_basefill_037'], 'func': lp_base_universe_d2_032_lp_basefill_037}


def lp_base_universe_d2_033_lp_basefill_038(lp_basefill_038):
    return _base_universe_d2(lp_basefill_038, 33)
LP_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['lp_base_universe_d2_033_lp_basefill_038'] = {'inputs': ['lp_basefill_038'], 'func': lp_base_universe_d2_033_lp_basefill_038}


def lp_base_universe_d2_034_lp_basefill_039(lp_basefill_039):
    return _base_universe_d2(lp_basefill_039, 34)
LP_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['lp_base_universe_d2_034_lp_basefill_039'] = {'inputs': ['lp_basefill_039'], 'func': lp_base_universe_d2_034_lp_basefill_039}


def lp_base_universe_d2_035_lp_basefill_040(lp_basefill_040):
    return _base_universe_d2(lp_basefill_040, 35)
LP_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['lp_base_universe_d2_035_lp_basefill_040'] = {'inputs': ['lp_basefill_040'], 'func': lp_base_universe_d2_035_lp_basefill_040}


def lp_base_universe_d2_036_lp_basefill_041(lp_basefill_041):
    return _base_universe_d2(lp_basefill_041, 36)
LP_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['lp_base_universe_d2_036_lp_basefill_041'] = {'inputs': ['lp_basefill_041'], 'func': lp_base_universe_d2_036_lp_basefill_041}


def lp_base_universe_d2_037_lp_basefill_042(lp_basefill_042):
    return _base_universe_d2(lp_basefill_042, 37)
LP_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['lp_base_universe_d2_037_lp_basefill_042'] = {'inputs': ['lp_basefill_042'], 'func': lp_base_universe_d2_037_lp_basefill_042}


def lp_base_universe_d2_038_lp_basefill_043(lp_basefill_043):
    return _base_universe_d2(lp_basefill_043, 38)
LP_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['lp_base_universe_d2_038_lp_basefill_043'] = {'inputs': ['lp_basefill_043'], 'func': lp_base_universe_d2_038_lp_basefill_043}


def lp_base_universe_d2_039_lp_basefill_044(lp_basefill_044):
    return _base_universe_d2(lp_basefill_044, 39)
LP_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['lp_base_universe_d2_039_lp_basefill_044'] = {'inputs': ['lp_basefill_044'], 'func': lp_base_universe_d2_039_lp_basefill_044}


def lp_base_universe_d2_040_lp_basefill_045(lp_basefill_045):
    return _base_universe_d2(lp_basefill_045, 40)
LP_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['lp_base_universe_d2_040_lp_basefill_045'] = {'inputs': ['lp_basefill_045'], 'func': lp_base_universe_d2_040_lp_basefill_045}


def lp_base_universe_d2_041_lp_basefill_046(lp_basefill_046):
    return _base_universe_d2(lp_basefill_046, 41)
LP_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['lp_base_universe_d2_041_lp_basefill_046'] = {'inputs': ['lp_basefill_046'], 'func': lp_base_universe_d2_041_lp_basefill_046}


def lp_base_universe_d2_042_lp_basefill_047(lp_basefill_047):
    return _base_universe_d2(lp_basefill_047, 42)
LP_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['lp_base_universe_d2_042_lp_basefill_047'] = {'inputs': ['lp_basefill_047'], 'func': lp_base_universe_d2_042_lp_basefill_047}


def lp_base_universe_d2_043_lp_basefill_048(lp_basefill_048):
    return _base_universe_d2(lp_basefill_048, 43)
LP_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['lp_base_universe_d2_043_lp_basefill_048'] = {'inputs': ['lp_basefill_048'], 'func': lp_base_universe_d2_043_lp_basefill_048}


def lp_base_universe_d2_044_lp_basefill_049(lp_basefill_049):
    return _base_universe_d2(lp_basefill_049, 44)
LP_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['lp_base_universe_d2_044_lp_basefill_049'] = {'inputs': ['lp_basefill_049'], 'func': lp_base_universe_d2_044_lp_basefill_049}


def lp_base_universe_d2_045_lp_basefill_050(lp_basefill_050):
    return _base_universe_d2(lp_basefill_050, 45)
LP_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['lp_base_universe_d2_045_lp_basefill_050'] = {'inputs': ['lp_basefill_050'], 'func': lp_base_universe_d2_045_lp_basefill_050}


def lp_base_universe_d2_046_lp_basefill_051(lp_basefill_051):
    return _base_universe_d2(lp_basefill_051, 46)
LP_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['lp_base_universe_d2_046_lp_basefill_051'] = {'inputs': ['lp_basefill_051'], 'func': lp_base_universe_d2_046_lp_basefill_051}


def lp_base_universe_d2_047_lp_basefill_052(lp_basefill_052):
    return _base_universe_d2(lp_basefill_052, 47)
LP_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['lp_base_universe_d2_047_lp_basefill_052'] = {'inputs': ['lp_basefill_052'], 'func': lp_base_universe_d2_047_lp_basefill_052}


def lp_base_universe_d2_048_lp_basefill_053(lp_basefill_053):
    return _base_universe_d2(lp_basefill_053, 48)
LP_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['lp_base_universe_d2_048_lp_basefill_053'] = {'inputs': ['lp_basefill_053'], 'func': lp_base_universe_d2_048_lp_basefill_053}


def lp_base_universe_d2_049_lp_basefill_054(lp_basefill_054):
    return _base_universe_d2(lp_basefill_054, 49)
LP_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['lp_base_universe_d2_049_lp_basefill_054'] = {'inputs': ['lp_basefill_054'], 'func': lp_base_universe_d2_049_lp_basefill_054}


def lp_base_universe_d2_050_lp_basefill_055(lp_basefill_055):
    return _base_universe_d2(lp_basefill_055, 50)
LP_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['lp_base_universe_d2_050_lp_basefill_055'] = {'inputs': ['lp_basefill_055'], 'func': lp_base_universe_d2_050_lp_basefill_055}


def lp_base_universe_d2_051_lp_basefill_056(lp_basefill_056):
    return _base_universe_d2(lp_basefill_056, 51)
LP_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['lp_base_universe_d2_051_lp_basefill_056'] = {'inputs': ['lp_basefill_056'], 'func': lp_base_universe_d2_051_lp_basefill_056}


def lp_base_universe_d2_052_lp_basefill_057(lp_basefill_057):
    return _base_universe_d2(lp_basefill_057, 52)
LP_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['lp_base_universe_d2_052_lp_basefill_057'] = {'inputs': ['lp_basefill_057'], 'func': lp_base_universe_d2_052_lp_basefill_057}


def lp_base_universe_d2_053_lp_basefill_058(lp_basefill_058):
    return _base_universe_d2(lp_basefill_058, 53)
LP_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['lp_base_universe_d2_053_lp_basefill_058'] = {'inputs': ['lp_basefill_058'], 'func': lp_base_universe_d2_053_lp_basefill_058}


def lp_base_universe_d2_054_lp_basefill_059(lp_basefill_059):
    return _base_universe_d2(lp_basefill_059, 54)
LP_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['lp_base_universe_d2_054_lp_basefill_059'] = {'inputs': ['lp_basefill_059'], 'func': lp_base_universe_d2_054_lp_basefill_059}


def lp_base_universe_d2_055_lp_basefill_060(lp_basefill_060):
    return _base_universe_d2(lp_basefill_060, 55)
LP_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['lp_base_universe_d2_055_lp_basefill_060'] = {'inputs': ['lp_basefill_060'], 'func': lp_base_universe_d2_055_lp_basefill_060}


def lp_base_universe_d2_056_lp_basefill_061(lp_basefill_061):
    return _base_universe_d2(lp_basefill_061, 56)
LP_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['lp_base_universe_d2_056_lp_basefill_061'] = {'inputs': ['lp_basefill_061'], 'func': lp_base_universe_d2_056_lp_basefill_061}


def lp_base_universe_d2_057_lp_basefill_062(lp_basefill_062):
    return _base_universe_d2(lp_basefill_062, 57)
LP_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['lp_base_universe_d2_057_lp_basefill_062'] = {'inputs': ['lp_basefill_062'], 'func': lp_base_universe_d2_057_lp_basefill_062}


def lp_base_universe_d2_058_lp_basefill_063(lp_basefill_063):
    return _base_universe_d2(lp_basefill_063, 58)
LP_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['lp_base_universe_d2_058_lp_basefill_063'] = {'inputs': ['lp_basefill_063'], 'func': lp_base_universe_d2_058_lp_basefill_063}


def lp_base_universe_d2_059_lp_basefill_064(lp_basefill_064):
    return _base_universe_d2(lp_basefill_064, 59)
LP_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['lp_base_universe_d2_059_lp_basefill_064'] = {'inputs': ['lp_basefill_064'], 'func': lp_base_universe_d2_059_lp_basefill_064}


def lp_base_universe_d2_060_lp_basefill_065(lp_basefill_065):
    return _base_universe_d2(lp_basefill_065, 60)
LP_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['lp_base_universe_d2_060_lp_basefill_065'] = {'inputs': ['lp_basefill_065'], 'func': lp_base_universe_d2_060_lp_basefill_065}


def lp_base_universe_d2_061_lp_basefill_066(lp_basefill_066):
    return _base_universe_d2(lp_basefill_066, 61)
LP_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['lp_base_universe_d2_061_lp_basefill_066'] = {'inputs': ['lp_basefill_066'], 'func': lp_base_universe_d2_061_lp_basefill_066}


def lp_base_universe_d2_062_lp_basefill_067(lp_basefill_067):
    return _base_universe_d2(lp_basefill_067, 62)
LP_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['lp_base_universe_d2_062_lp_basefill_067'] = {'inputs': ['lp_basefill_067'], 'func': lp_base_universe_d2_062_lp_basefill_067}


def lp_base_universe_d2_063_lp_basefill_068(lp_basefill_068):
    return _base_universe_d2(lp_basefill_068, 63)
LP_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['lp_base_universe_d2_063_lp_basefill_068'] = {'inputs': ['lp_basefill_068'], 'func': lp_base_universe_d2_063_lp_basefill_068}


def lp_base_universe_d2_064_lp_basefill_069(lp_basefill_069):
    return _base_universe_d2(lp_basefill_069, 64)
LP_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['lp_base_universe_d2_064_lp_basefill_069'] = {'inputs': ['lp_basefill_069'], 'func': lp_base_universe_d2_064_lp_basefill_069}


def lp_base_universe_d2_065_lp_basefill_070(lp_basefill_070):
    return _base_universe_d2(lp_basefill_070, 65)
LP_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['lp_base_universe_d2_065_lp_basefill_070'] = {'inputs': ['lp_basefill_070'], 'func': lp_base_universe_d2_065_lp_basefill_070}


def lp_base_universe_d2_066_lp_basefill_071(lp_basefill_071):
    return _base_universe_d2(lp_basefill_071, 66)
LP_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['lp_base_universe_d2_066_lp_basefill_071'] = {'inputs': ['lp_basefill_071'], 'func': lp_base_universe_d2_066_lp_basefill_071}


def lp_base_universe_d2_067_lp_basefill_072(lp_basefill_072):
    return _base_universe_d2(lp_basefill_072, 67)
LP_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['lp_base_universe_d2_067_lp_basefill_072'] = {'inputs': ['lp_basefill_072'], 'func': lp_base_universe_d2_067_lp_basefill_072}


def lp_base_universe_d2_068_lp_basefill_073(lp_basefill_073):
    return _base_universe_d2(lp_basefill_073, 68)
LP_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['lp_base_universe_d2_068_lp_basefill_073'] = {'inputs': ['lp_basefill_073'], 'func': lp_base_universe_d2_068_lp_basefill_073}


def lp_base_universe_d2_069_lp_basefill_074(lp_basefill_074):
    return _base_universe_d2(lp_basefill_074, 69)
LP_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['lp_base_universe_d2_069_lp_basefill_074'] = {'inputs': ['lp_basefill_074'], 'func': lp_base_universe_d2_069_lp_basefill_074}


def lp_base_universe_d2_070_lp_basefill_075(lp_basefill_075):
    return _base_universe_d2(lp_basefill_075, 70)
LP_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['lp_base_universe_d2_070_lp_basefill_075'] = {'inputs': ['lp_basefill_075'], 'func': lp_base_universe_d2_070_lp_basefill_075}
