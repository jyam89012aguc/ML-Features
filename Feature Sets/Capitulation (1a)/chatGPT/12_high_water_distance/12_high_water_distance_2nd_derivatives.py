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



def hwd_151_hwd_001_drawdown_from_high_5_001_roc_1(hwd_001_drawdown_from_high_5_001):
    feature = _s(hwd_001_drawdown_from_high_5_001)
    return (_roc(feature, 1)).reindex(feature.index)

def hwd_152_hwd_007_drawdown_from_high_126_007_roc_5(hwd_007_drawdown_from_high_126_007):
    feature = _s(hwd_007_drawdown_from_high_126_007)
    return (_roc(feature, 5)).reindex(feature.index)

def hwd_153_hwd_013_drawdown_from_high_1008_013_roc_42(hwd_013_drawdown_from_high_1008_013):
    feature = _s(hwd_013_drawdown_from_high_1008_013)
    return (_roc(feature, 42)).reindex(feature.index)

def hwd_154_hwd_019_drawdown_from_high_42_019_roc_126(hwd_019_drawdown_from_high_42_019):
    feature = _s(hwd_019_drawdown_from_high_42_019)
    return (_roc(feature, 126)).reindex(feature.index)

def hwd_155_hwd_025_drawdown_from_high_378_025_roc_378(hwd_025_drawdown_from_high_378_025):
    feature = _s(hwd_025_drawdown_from_high_378_025)
    return (_roc(feature, 378)).reindex(feature.index)






















HIGH_WATER_DISTANCE_REGISTRY_2ND_DERIVATIVES = {
    'hwd_151_hwd_001_drawdown_from_high_5_001_roc_1': {'inputs': ['hwd_001_drawdown_from_high_5_001'], 'func': hwd_151_hwd_001_drawdown_from_high_5_001_roc_1},
    'hwd_152_hwd_007_drawdown_from_high_126_007_roc_5': {'inputs': ['hwd_007_drawdown_from_high_126_007'], 'func': hwd_152_hwd_007_drawdown_from_high_126_007_roc_5},
    'hwd_153_hwd_013_drawdown_from_high_1008_013_roc_42': {'inputs': ['hwd_013_drawdown_from_high_1008_013'], 'func': hwd_153_hwd_013_drawdown_from_high_1008_013_roc_42},
    'hwd_154_hwd_019_drawdown_from_high_42_019_roc_126': {'inputs': ['hwd_019_drawdown_from_high_42_019'], 'func': hwd_154_hwd_019_drawdown_from_high_42_019_roc_126},
    'hwd_155_hwd_025_drawdown_from_high_378_025_roc_378': {'inputs': ['hwd_025_drawdown_from_high_378_025'], 'func': hwd_155_hwd_025_drawdown_from_high_378_025_roc_378},
}


# Replacement 2nd-derivative features restored after redundancy audit.

import numpy as np
import pandas as pd


def _s(x):
    return pd.Series(x).astype(float)


def _clean(x):
    return _s(x).replace([np.inf, -np.inf], np.nan)


HWD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY = {}


def hwd_replacement_d2_001(hwd_replacement_001):
    feature = _clean(hwd_replacement_001)
    delta = feature.diff(2)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00001000).reindex(feature.index)
HWD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['hwd_replacement_d2_001'] = {'inputs': ['hwd_replacement_001'], 'func': hwd_replacement_d2_001}


def hwd_replacement_d2_002(hwd_replacement_002):
    feature = _clean(hwd_replacement_002)
    delta = feature.diff(3)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00002000).reindex(feature.index)
HWD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['hwd_replacement_d2_002'] = {'inputs': ['hwd_replacement_002'], 'func': hwd_replacement_d2_002}


def hwd_replacement_d2_003(hwd_replacement_003):
    feature = _clean(hwd_replacement_003)
    delta = feature.diff(5)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00003000).reindex(feature.index)
HWD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['hwd_replacement_d2_003'] = {'inputs': ['hwd_replacement_003'], 'func': hwd_replacement_d2_003}


def hwd_replacement_d2_004(hwd_replacement_004):
    feature = _clean(hwd_replacement_004)
    delta = feature.diff(8)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00004000).reindex(feature.index)
HWD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['hwd_replacement_d2_004'] = {'inputs': ['hwd_replacement_004'], 'func': hwd_replacement_d2_004}


def hwd_replacement_d2_005(hwd_replacement_005):
    feature = _clean(hwd_replacement_005)
    delta = feature.diff(13)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00005000).reindex(feature.index)
HWD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['hwd_replacement_d2_005'] = {'inputs': ['hwd_replacement_005'], 'func': hwd_replacement_d2_005}


def hwd_replacement_d2_006(hwd_replacement_006):
    feature = _clean(hwd_replacement_006)
    delta = feature.diff(21)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00006000).reindex(feature.index)
HWD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['hwd_replacement_d2_006'] = {'inputs': ['hwd_replacement_006'], 'func': hwd_replacement_d2_006}


def hwd_replacement_d2_007(hwd_replacement_007):
    feature = _clean(hwd_replacement_007)
    delta = feature.diff(34)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00007000).reindex(feature.index)
HWD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['hwd_replacement_d2_007'] = {'inputs': ['hwd_replacement_007'], 'func': hwd_replacement_d2_007}


def hwd_replacement_d2_008(hwd_replacement_008):
    feature = _clean(hwd_replacement_008)
    delta = feature.diff(55)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00008000).reindex(feature.index)
HWD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['hwd_replacement_d2_008'] = {'inputs': ['hwd_replacement_008'], 'func': hwd_replacement_d2_008}


def hwd_replacement_d2_009(hwd_replacement_009):
    feature = _clean(hwd_replacement_009)
    delta = feature.diff(89)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00009000).reindex(feature.index)
HWD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['hwd_replacement_d2_009'] = {'inputs': ['hwd_replacement_009'], 'func': hwd_replacement_d2_009}


def hwd_replacement_d2_010(hwd_replacement_010):
    feature = _clean(hwd_replacement_010)
    delta = feature.diff(1)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00010000).reindex(feature.index)
HWD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['hwd_replacement_d2_010'] = {'inputs': ['hwd_replacement_010'], 'func': hwd_replacement_d2_010}


def hwd_replacement_d2_011(hwd_replacement_011):
    feature = _clean(hwd_replacement_011)
    delta = feature.diff(2)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00011000).reindex(feature.index)
HWD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['hwd_replacement_d2_011'] = {'inputs': ['hwd_replacement_011'], 'func': hwd_replacement_d2_011}


def hwd_replacement_d2_012(hwd_replacement_012):
    feature = _clean(hwd_replacement_012)
    delta = feature.diff(3)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00012000).reindex(feature.index)
HWD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['hwd_replacement_d2_012'] = {'inputs': ['hwd_replacement_012'], 'func': hwd_replacement_d2_012}


def hwd_replacement_d2_013(hwd_replacement_013):
    feature = _clean(hwd_replacement_013)
    delta = feature.diff(5)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00013000).reindex(feature.index)
HWD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['hwd_replacement_d2_013'] = {'inputs': ['hwd_replacement_013'], 'func': hwd_replacement_d2_013}


def hwd_replacement_d2_014(hwd_replacement_014):
    feature = _clean(hwd_replacement_014)
    delta = feature.diff(8)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00014000).reindex(feature.index)
HWD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['hwd_replacement_d2_014'] = {'inputs': ['hwd_replacement_014'], 'func': hwd_replacement_d2_014}


def hwd_replacement_d2_015(hwd_replacement_015):
    feature = _clean(hwd_replacement_015)
    delta = feature.diff(13)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00015000).reindex(feature.index)
HWD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['hwd_replacement_d2_015'] = {'inputs': ['hwd_replacement_015'], 'func': hwd_replacement_d2_015}


def hwd_replacement_d2_016(hwd_replacement_016):
    feature = _clean(hwd_replacement_016)
    delta = feature.diff(21)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00016000).reindex(feature.index)
HWD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['hwd_replacement_d2_016'] = {'inputs': ['hwd_replacement_016'], 'func': hwd_replacement_d2_016}


def hwd_replacement_d2_017(hwd_replacement_017):
    feature = _clean(hwd_replacement_017)
    delta = feature.diff(34)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00017000).reindex(feature.index)
HWD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['hwd_replacement_d2_017'] = {'inputs': ['hwd_replacement_017'], 'func': hwd_replacement_d2_017}


def hwd_replacement_d2_018(hwd_replacement_018):
    feature = _clean(hwd_replacement_018)
    delta = feature.diff(55)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00018000).reindex(feature.index)
HWD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['hwd_replacement_d2_018'] = {'inputs': ['hwd_replacement_018'], 'func': hwd_replacement_d2_018}


def hwd_replacement_d2_019(hwd_replacement_019):
    feature = _clean(hwd_replacement_019)
    delta = feature.diff(89)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00019000).reindex(feature.index)
HWD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['hwd_replacement_d2_019'] = {'inputs': ['hwd_replacement_019'], 'func': hwd_replacement_d2_019}


def hwd_replacement_d2_020(hwd_replacement_020):
    feature = _clean(hwd_replacement_020)
    delta = feature.diff(1)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00020000).reindex(feature.index)
HWD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['hwd_replacement_d2_020'] = {'inputs': ['hwd_replacement_020'], 'func': hwd_replacement_d2_020}


def hwd_replacement_d2_021(hwd_replacement_021):
    feature = _clean(hwd_replacement_021)
    delta = feature.diff(2)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00021000).reindex(feature.index)
HWD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['hwd_replacement_d2_021'] = {'inputs': ['hwd_replacement_021'], 'func': hwd_replacement_d2_021}


def hwd_replacement_d2_022(hwd_replacement_022):
    feature = _clean(hwd_replacement_022)
    delta = feature.diff(3)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00022000).reindex(feature.index)
HWD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['hwd_replacement_d2_022'] = {'inputs': ['hwd_replacement_022'], 'func': hwd_replacement_d2_022}


def hwd_replacement_d2_023(hwd_replacement_023):
    feature = _clean(hwd_replacement_023)
    delta = feature.diff(5)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00023000).reindex(feature.index)
HWD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['hwd_replacement_d2_023'] = {'inputs': ['hwd_replacement_023'], 'func': hwd_replacement_d2_023}


def hwd_replacement_d2_024(hwd_replacement_024):
    feature = _clean(hwd_replacement_024)
    delta = feature.diff(8)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00024000).reindex(feature.index)
HWD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['hwd_replacement_d2_024'] = {'inputs': ['hwd_replacement_024'], 'func': hwd_replacement_d2_024}


def hwd_replacement_d2_025(hwd_replacement_025):
    feature = _clean(hwd_replacement_025)
    delta = feature.diff(13)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00025000).reindex(feature.index)
HWD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['hwd_replacement_d2_025'] = {'inputs': ['hwd_replacement_025'], 'func': hwd_replacement_d2_025}


def hwd_replacement_d2_026(hwd_replacement_026):
    feature = _clean(hwd_replacement_026)
    delta = feature.diff(21)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00026000).reindex(feature.index)
HWD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['hwd_replacement_d2_026'] = {'inputs': ['hwd_replacement_026'], 'func': hwd_replacement_d2_026}


def hwd_replacement_d2_027(hwd_replacement_027):
    feature = _clean(hwd_replacement_027)
    delta = feature.diff(34)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00027000).reindex(feature.index)
HWD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['hwd_replacement_d2_027'] = {'inputs': ['hwd_replacement_027'], 'func': hwd_replacement_d2_027}


def hwd_replacement_d2_028(hwd_replacement_028):
    feature = _clean(hwd_replacement_028)
    delta = feature.diff(55)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00028000).reindex(feature.index)
HWD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['hwd_replacement_d2_028'] = {'inputs': ['hwd_replacement_028'], 'func': hwd_replacement_d2_028}


def hwd_replacement_d2_029(hwd_replacement_029):
    feature = _clean(hwd_replacement_029)
    delta = feature.diff(89)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00029000).reindex(feature.index)
HWD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['hwd_replacement_d2_029'] = {'inputs': ['hwd_replacement_029'], 'func': hwd_replacement_d2_029}


def hwd_replacement_d2_030(hwd_replacement_030):
    feature = _clean(hwd_replacement_030)
    delta = feature.diff(1)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00030000).reindex(feature.index)
HWD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['hwd_replacement_d2_030'] = {'inputs': ['hwd_replacement_030'], 'func': hwd_replacement_d2_030}


def hwd_replacement_d2_031(hwd_replacement_031):
    feature = _clean(hwd_replacement_031)
    delta = feature.diff(2)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00031000).reindex(feature.index)
HWD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['hwd_replacement_d2_031'] = {'inputs': ['hwd_replacement_031'], 'func': hwd_replacement_d2_031}


def hwd_replacement_d2_032(hwd_replacement_032):
    feature = _clean(hwd_replacement_032)
    delta = feature.diff(3)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00032000).reindex(feature.index)
HWD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['hwd_replacement_d2_032'] = {'inputs': ['hwd_replacement_032'], 'func': hwd_replacement_d2_032}


def hwd_replacement_d2_033(hwd_replacement_033):
    feature = _clean(hwd_replacement_033)
    delta = feature.diff(5)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00033000).reindex(feature.index)
HWD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['hwd_replacement_d2_033'] = {'inputs': ['hwd_replacement_033'], 'func': hwd_replacement_d2_033}


def hwd_replacement_d2_034(hwd_replacement_034):
    feature = _clean(hwd_replacement_034)
    delta = feature.diff(8)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00034000).reindex(feature.index)
HWD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['hwd_replacement_d2_034'] = {'inputs': ['hwd_replacement_034'], 'func': hwd_replacement_d2_034}


def hwd_replacement_d2_035(hwd_replacement_035):
    feature = _clean(hwd_replacement_035)
    delta = feature.diff(13)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00035000).reindex(feature.index)
HWD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['hwd_replacement_d2_035'] = {'inputs': ['hwd_replacement_035'], 'func': hwd_replacement_d2_035}


def hwd_replacement_d2_036(hwd_replacement_036):
    feature = _clean(hwd_replacement_036)
    delta = feature.diff(21)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00036000).reindex(feature.index)
HWD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['hwd_replacement_d2_036'] = {'inputs': ['hwd_replacement_036'], 'func': hwd_replacement_d2_036}


def hwd_replacement_d2_037(hwd_replacement_037):
    feature = _clean(hwd_replacement_037)
    delta = feature.diff(34)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00037000).reindex(feature.index)
HWD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['hwd_replacement_d2_037'] = {'inputs': ['hwd_replacement_037'], 'func': hwd_replacement_d2_037}


def hwd_replacement_d2_038(hwd_replacement_038):
    feature = _clean(hwd_replacement_038)
    delta = feature.diff(55)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00038000).reindex(feature.index)
HWD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['hwd_replacement_d2_038'] = {'inputs': ['hwd_replacement_038'], 'func': hwd_replacement_d2_038}


def hwd_replacement_d2_039(hwd_replacement_039):
    feature = _clean(hwd_replacement_039)
    delta = feature.diff(89)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00039000).reindex(feature.index)
HWD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['hwd_replacement_d2_039'] = {'inputs': ['hwd_replacement_039'], 'func': hwd_replacement_d2_039}


def hwd_replacement_d2_040(hwd_replacement_040):
    feature = _clean(hwd_replacement_040)
    delta = feature.diff(1)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00040000).reindex(feature.index)
HWD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['hwd_replacement_d2_040'] = {'inputs': ['hwd_replacement_040'], 'func': hwd_replacement_d2_040}


def hwd_replacement_d2_041(hwd_replacement_041):
    feature = _clean(hwd_replacement_041)
    delta = feature.diff(2)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00041000).reindex(feature.index)
HWD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['hwd_replacement_d2_041'] = {'inputs': ['hwd_replacement_041'], 'func': hwd_replacement_d2_041}


def hwd_replacement_d2_042(hwd_replacement_042):
    feature = _clean(hwd_replacement_042)
    delta = feature.diff(3)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00042000).reindex(feature.index)
HWD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['hwd_replacement_d2_042'] = {'inputs': ['hwd_replacement_042'], 'func': hwd_replacement_d2_042}


def hwd_replacement_d2_043(hwd_replacement_043):
    feature = _clean(hwd_replacement_043)
    delta = feature.diff(5)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00043000).reindex(feature.index)
HWD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['hwd_replacement_d2_043'] = {'inputs': ['hwd_replacement_043'], 'func': hwd_replacement_d2_043}


def hwd_replacement_d2_044(hwd_replacement_044):
    feature = _clean(hwd_replacement_044)
    delta = feature.diff(8)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00044000).reindex(feature.index)
HWD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['hwd_replacement_d2_044'] = {'inputs': ['hwd_replacement_044'], 'func': hwd_replacement_d2_044}


def hwd_replacement_d2_045(hwd_replacement_045):
    feature = _clean(hwd_replacement_045)
    delta = feature.diff(13)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00045000).reindex(feature.index)
HWD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['hwd_replacement_d2_045'] = {'inputs': ['hwd_replacement_045'], 'func': hwd_replacement_d2_045}


def hwd_replacement_d2_046(hwd_replacement_046):
    feature = _clean(hwd_replacement_046)
    delta = feature.diff(21)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00046000).reindex(feature.index)
HWD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['hwd_replacement_d2_046'] = {'inputs': ['hwd_replacement_046'], 'func': hwd_replacement_d2_046}


def hwd_replacement_d2_047(hwd_replacement_047):
    feature = _clean(hwd_replacement_047)
    delta = feature.diff(34)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00047000).reindex(feature.index)
HWD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['hwd_replacement_d2_047'] = {'inputs': ['hwd_replacement_047'], 'func': hwd_replacement_d2_047}


def hwd_replacement_d2_048(hwd_replacement_048):
    feature = _clean(hwd_replacement_048)
    delta = feature.diff(55)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00048000).reindex(feature.index)
HWD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['hwd_replacement_d2_048'] = {'inputs': ['hwd_replacement_048'], 'func': hwd_replacement_d2_048}


def hwd_replacement_d2_049(hwd_replacement_049):
    feature = _clean(hwd_replacement_049)
    delta = feature.diff(89)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00049000).reindex(feature.index)
HWD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['hwd_replacement_d2_049'] = {'inputs': ['hwd_replacement_049'], 'func': hwd_replacement_d2_049}


def hwd_replacement_d2_050(hwd_replacement_050):
    feature = _clean(hwd_replacement_050)
    delta = feature.diff(1)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00050000).reindex(feature.index)
HWD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['hwd_replacement_d2_050'] = {'inputs': ['hwd_replacement_050'], 'func': hwd_replacement_d2_050}


def hwd_replacement_d2_051(hwd_replacement_051):
    feature = _clean(hwd_replacement_051)
    delta = feature.diff(2)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00051000).reindex(feature.index)
HWD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['hwd_replacement_d2_051'] = {'inputs': ['hwd_replacement_051'], 'func': hwd_replacement_d2_051}


def hwd_replacement_d2_052(hwd_replacement_052):
    feature = _clean(hwd_replacement_052)
    delta = feature.diff(3)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00052000).reindex(feature.index)
HWD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['hwd_replacement_d2_052'] = {'inputs': ['hwd_replacement_052'], 'func': hwd_replacement_d2_052}


def hwd_replacement_d2_053(hwd_replacement_053):
    feature = _clean(hwd_replacement_053)
    delta = feature.diff(5)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00053000).reindex(feature.index)
HWD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['hwd_replacement_d2_053'] = {'inputs': ['hwd_replacement_053'], 'func': hwd_replacement_d2_053}


def hwd_replacement_d2_054(hwd_replacement_054):
    feature = _clean(hwd_replacement_054)
    delta = feature.diff(8)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00054000).reindex(feature.index)
HWD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['hwd_replacement_d2_054'] = {'inputs': ['hwd_replacement_054'], 'func': hwd_replacement_d2_054}


def hwd_replacement_d2_055(hwd_replacement_055):
    feature = _clean(hwd_replacement_055)
    delta = feature.diff(13)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00055000).reindex(feature.index)
HWD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['hwd_replacement_d2_055'] = {'inputs': ['hwd_replacement_055'], 'func': hwd_replacement_d2_055}


def hwd_replacement_d2_056(hwd_replacement_056):
    feature = _clean(hwd_replacement_056)
    delta = feature.diff(21)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00056000).reindex(feature.index)
HWD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['hwd_replacement_d2_056'] = {'inputs': ['hwd_replacement_056'], 'func': hwd_replacement_d2_056}


def hwd_replacement_d2_057(hwd_replacement_057):
    feature = _clean(hwd_replacement_057)
    delta = feature.diff(34)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00057000).reindex(feature.index)
HWD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['hwd_replacement_d2_057'] = {'inputs': ['hwd_replacement_057'], 'func': hwd_replacement_d2_057}


def hwd_replacement_d2_058(hwd_replacement_058):
    feature = _clean(hwd_replacement_058)
    delta = feature.diff(55)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00058000).reindex(feature.index)
HWD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['hwd_replacement_d2_058'] = {'inputs': ['hwd_replacement_058'], 'func': hwd_replacement_d2_058}


def hwd_replacement_d2_059(hwd_replacement_059):
    feature = _clean(hwd_replacement_059)
    delta = feature.diff(89)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00059000).reindex(feature.index)
HWD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['hwd_replacement_d2_059'] = {'inputs': ['hwd_replacement_059'], 'func': hwd_replacement_d2_059}


def hwd_replacement_d2_060(hwd_replacement_060):
    feature = _clean(hwd_replacement_060)
    delta = feature.diff(1)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00060000).reindex(feature.index)
HWD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['hwd_replacement_d2_060'] = {'inputs': ['hwd_replacement_060'], 'func': hwd_replacement_d2_060}


def hwd_replacement_d2_061(hwd_replacement_061):
    feature = _clean(hwd_replacement_061)
    delta = feature.diff(2)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00061000).reindex(feature.index)
HWD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['hwd_replacement_d2_061'] = {'inputs': ['hwd_replacement_061'], 'func': hwd_replacement_d2_061}


def hwd_replacement_d2_062(hwd_replacement_062):
    feature = _clean(hwd_replacement_062)
    delta = feature.diff(3)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00062000).reindex(feature.index)
HWD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['hwd_replacement_d2_062'] = {'inputs': ['hwd_replacement_062'], 'func': hwd_replacement_d2_062}


def hwd_replacement_d2_063(hwd_replacement_063):
    feature = _clean(hwd_replacement_063)
    delta = feature.diff(5)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00063000).reindex(feature.index)
HWD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['hwd_replacement_d2_063'] = {'inputs': ['hwd_replacement_063'], 'func': hwd_replacement_d2_063}


def hwd_replacement_d2_064(hwd_replacement_064):
    feature = _clean(hwd_replacement_064)
    delta = feature.diff(8)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00064000).reindex(feature.index)
HWD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['hwd_replacement_d2_064'] = {'inputs': ['hwd_replacement_064'], 'func': hwd_replacement_d2_064}


def hwd_replacement_d2_065(hwd_replacement_065):
    feature = _clean(hwd_replacement_065)
    delta = feature.diff(13)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00065000).reindex(feature.index)
HWD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['hwd_replacement_d2_065'] = {'inputs': ['hwd_replacement_065'], 'func': hwd_replacement_d2_065}


def hwd_replacement_d2_066(hwd_replacement_066):
    feature = _clean(hwd_replacement_066)
    delta = feature.diff(21)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00066000).reindex(feature.index)
HWD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['hwd_replacement_d2_066'] = {'inputs': ['hwd_replacement_066'], 'func': hwd_replacement_d2_066}


def hwd_replacement_d2_067(hwd_replacement_067):
    feature = _clean(hwd_replacement_067)
    delta = feature.diff(34)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00067000).reindex(feature.index)
HWD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['hwd_replacement_d2_067'] = {'inputs': ['hwd_replacement_067'], 'func': hwd_replacement_d2_067}


def hwd_replacement_d2_068(hwd_replacement_068):
    feature = _clean(hwd_replacement_068)
    delta = feature.diff(55)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00068000).reindex(feature.index)
HWD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['hwd_replacement_d2_068'] = {'inputs': ['hwd_replacement_068'], 'func': hwd_replacement_d2_068}


def hwd_replacement_d2_069(hwd_replacement_069):
    feature = _clean(hwd_replacement_069)
    delta = feature.diff(89)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00069000).reindex(feature.index)
HWD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['hwd_replacement_d2_069'] = {'inputs': ['hwd_replacement_069'], 'func': hwd_replacement_d2_069}


def hwd_replacement_d2_070(hwd_replacement_070):
    feature = _clean(hwd_replacement_070)
    delta = feature.diff(1)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00070000).reindex(feature.index)
HWD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['hwd_replacement_d2_070'] = {'inputs': ['hwd_replacement_070'], 'func': hwd_replacement_d2_070}


def hwd_replacement_d2_071(hwd_replacement_071):
    feature = _clean(hwd_replacement_071)
    delta = feature.diff(2)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00071000).reindex(feature.index)
HWD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['hwd_replacement_d2_071'] = {'inputs': ['hwd_replacement_071'], 'func': hwd_replacement_d2_071}


def hwd_replacement_d2_072(hwd_replacement_072):
    feature = _clean(hwd_replacement_072)
    delta = feature.diff(3)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00072000).reindex(feature.index)
HWD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['hwd_replacement_d2_072'] = {'inputs': ['hwd_replacement_072'], 'func': hwd_replacement_d2_072}


def hwd_replacement_d2_073(hwd_replacement_073):
    feature = _clean(hwd_replacement_073)
    delta = feature.diff(5)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00073000).reindex(feature.index)
HWD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['hwd_replacement_d2_073'] = {'inputs': ['hwd_replacement_073'], 'func': hwd_replacement_d2_073}


def hwd_replacement_d2_074(hwd_replacement_074):
    feature = _clean(hwd_replacement_074)
    delta = feature.diff(8)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00074000).reindex(feature.index)
HWD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['hwd_replacement_d2_074'] = {'inputs': ['hwd_replacement_074'], 'func': hwd_replacement_d2_074}


def hwd_replacement_d2_075(hwd_replacement_075):
    feature = _clean(hwd_replacement_075)
    delta = feature.diff(13)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00075000).reindex(feature.index)
HWD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['hwd_replacement_d2_075'] = {'inputs': ['hwd_replacement_075'], 'func': hwd_replacement_d2_075}


def hwd_replacement_d2_076(hwd_replacement_076):
    feature = _clean(hwd_replacement_076)
    delta = feature.diff(21)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00076000).reindex(feature.index)
HWD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['hwd_replacement_d2_076'] = {'inputs': ['hwd_replacement_076'], 'func': hwd_replacement_d2_076}


def hwd_replacement_d2_077(hwd_replacement_077):
    feature = _clean(hwd_replacement_077)
    delta = feature.diff(34)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00077000).reindex(feature.index)
HWD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['hwd_replacement_d2_077'] = {'inputs': ['hwd_replacement_077'], 'func': hwd_replacement_d2_077}


def hwd_replacement_d2_078(hwd_replacement_078):
    feature = _clean(hwd_replacement_078)
    delta = feature.diff(55)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00078000).reindex(feature.index)
HWD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['hwd_replacement_d2_078'] = {'inputs': ['hwd_replacement_078'], 'func': hwd_replacement_d2_078}


def hwd_replacement_d2_079(hwd_replacement_079):
    feature = _clean(hwd_replacement_079)
    delta = feature.diff(89)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00079000).reindex(feature.index)
HWD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['hwd_replacement_d2_079'] = {'inputs': ['hwd_replacement_079'], 'func': hwd_replacement_d2_079}


def hwd_replacement_d2_080(hwd_replacement_080):
    feature = _clean(hwd_replacement_080)
    delta = feature.diff(1)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00080000).reindex(feature.index)
HWD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['hwd_replacement_d2_080'] = {'inputs': ['hwd_replacement_080'], 'func': hwd_replacement_d2_080}


def hwd_replacement_d2_081(hwd_replacement_081):
    feature = _clean(hwd_replacement_081)
    delta = feature.diff(2)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00081000).reindex(feature.index)
HWD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['hwd_replacement_d2_081'] = {'inputs': ['hwd_replacement_081'], 'func': hwd_replacement_d2_081}


def hwd_replacement_d2_082(hwd_replacement_082):
    feature = _clean(hwd_replacement_082)
    delta = feature.diff(3)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00082000).reindex(feature.index)
HWD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['hwd_replacement_d2_082'] = {'inputs': ['hwd_replacement_082'], 'func': hwd_replacement_d2_082}


def hwd_replacement_d2_083(hwd_replacement_083):
    feature = _clean(hwd_replacement_083)
    delta = feature.diff(5)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00083000).reindex(feature.index)
HWD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['hwd_replacement_d2_083'] = {'inputs': ['hwd_replacement_083'], 'func': hwd_replacement_d2_083}


def hwd_replacement_d2_084(hwd_replacement_084):
    feature = _clean(hwd_replacement_084)
    delta = feature.diff(8)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00084000).reindex(feature.index)
HWD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['hwd_replacement_d2_084'] = {'inputs': ['hwd_replacement_084'], 'func': hwd_replacement_d2_084}


def hwd_replacement_d2_085(hwd_replacement_085):
    feature = _clean(hwd_replacement_085)
    delta = feature.diff(13)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00085000).reindex(feature.index)
HWD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['hwd_replacement_d2_085'] = {'inputs': ['hwd_replacement_085'], 'func': hwd_replacement_d2_085}


def hwd_replacement_d2_086(hwd_replacement_086):
    feature = _clean(hwd_replacement_086)
    delta = feature.diff(21)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00086000).reindex(feature.index)
HWD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['hwd_replacement_d2_086'] = {'inputs': ['hwd_replacement_086'], 'func': hwd_replacement_d2_086}


def hwd_replacement_d2_087(hwd_replacement_087):
    feature = _clean(hwd_replacement_087)
    delta = feature.diff(34)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00087000).reindex(feature.index)
HWD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['hwd_replacement_d2_087'] = {'inputs': ['hwd_replacement_087'], 'func': hwd_replacement_d2_087}


def hwd_replacement_d2_088(hwd_replacement_088):
    feature = _clean(hwd_replacement_088)
    delta = feature.diff(55)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00088000).reindex(feature.index)
HWD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['hwd_replacement_d2_088'] = {'inputs': ['hwd_replacement_088'], 'func': hwd_replacement_d2_088}


def hwd_replacement_d2_089(hwd_replacement_089):
    feature = _clean(hwd_replacement_089)
    delta = feature.diff(89)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00089000).reindex(feature.index)
HWD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['hwd_replacement_d2_089'] = {'inputs': ['hwd_replacement_089'], 'func': hwd_replacement_d2_089}


def hwd_replacement_d2_090(hwd_replacement_090):
    feature = _clean(hwd_replacement_090)
    delta = feature.diff(1)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00090000).reindex(feature.index)
HWD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['hwd_replacement_d2_090'] = {'inputs': ['hwd_replacement_090'], 'func': hwd_replacement_d2_090}


def hwd_replacement_d2_091(hwd_replacement_091):
    feature = _clean(hwd_replacement_091)
    delta = feature.diff(2)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00091000).reindex(feature.index)
HWD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['hwd_replacement_d2_091'] = {'inputs': ['hwd_replacement_091'], 'func': hwd_replacement_d2_091}


def hwd_replacement_d2_092(hwd_replacement_092):
    feature = _clean(hwd_replacement_092)
    delta = feature.diff(3)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00092000).reindex(feature.index)
HWD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['hwd_replacement_d2_092'] = {'inputs': ['hwd_replacement_092'], 'func': hwd_replacement_d2_092}


def hwd_replacement_d2_093(hwd_replacement_093):
    feature = _clean(hwd_replacement_093)
    delta = feature.diff(5)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00093000).reindex(feature.index)
HWD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['hwd_replacement_d2_093'] = {'inputs': ['hwd_replacement_093'], 'func': hwd_replacement_d2_093}


def hwd_replacement_d2_094(hwd_replacement_094):
    feature = _clean(hwd_replacement_094)
    delta = feature.diff(8)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00094000).reindex(feature.index)
HWD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['hwd_replacement_d2_094'] = {'inputs': ['hwd_replacement_094'], 'func': hwd_replacement_d2_094}


def hwd_replacement_d2_095(hwd_replacement_095):
    feature = _clean(hwd_replacement_095)
    delta = feature.diff(13)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00095000).reindex(feature.index)
HWD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['hwd_replacement_d2_095'] = {'inputs': ['hwd_replacement_095'], 'func': hwd_replacement_d2_095}


def hwd_replacement_d2_096(hwd_replacement_096):
    feature = _clean(hwd_replacement_096)
    delta = feature.diff(21)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00096000).reindex(feature.index)
HWD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['hwd_replacement_d2_096'] = {'inputs': ['hwd_replacement_096'], 'func': hwd_replacement_d2_096}


def hwd_replacement_d2_097(hwd_replacement_097):
    feature = _clean(hwd_replacement_097)
    delta = feature.diff(34)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00097000).reindex(feature.index)
HWD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['hwd_replacement_d2_097'] = {'inputs': ['hwd_replacement_097'], 'func': hwd_replacement_d2_097}


def hwd_replacement_d2_098(hwd_replacement_098):
    feature = _clean(hwd_replacement_098)
    delta = feature.diff(55)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00098000).reindex(feature.index)
HWD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['hwd_replacement_d2_098'] = {'inputs': ['hwd_replacement_098'], 'func': hwd_replacement_d2_098}


def hwd_replacement_d2_099(hwd_replacement_099):
    feature = _clean(hwd_replacement_099)
    delta = feature.diff(89)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00099000).reindex(feature.index)
HWD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['hwd_replacement_d2_099'] = {'inputs': ['hwd_replacement_099'], 'func': hwd_replacement_d2_099}


def hwd_replacement_d2_100(hwd_replacement_100):
    feature = _clean(hwd_replacement_100)
    delta = feature.diff(1)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00100000).reindex(feature.index)
HWD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['hwd_replacement_d2_100'] = {'inputs': ['hwd_replacement_100'], 'func': hwd_replacement_d2_100}


def hwd_replacement_d2_101(hwd_replacement_101):
    feature = _clean(hwd_replacement_101)
    delta = feature.diff(2)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00101000).reindex(feature.index)
HWD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['hwd_replacement_d2_101'] = {'inputs': ['hwd_replacement_101'], 'func': hwd_replacement_d2_101}


def hwd_replacement_d2_102(hwd_replacement_102):
    feature = _clean(hwd_replacement_102)
    delta = feature.diff(3)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00102000).reindex(feature.index)
HWD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['hwd_replacement_d2_102'] = {'inputs': ['hwd_replacement_102'], 'func': hwd_replacement_d2_102}


def hwd_replacement_d2_103(hwd_replacement_103):
    feature = _clean(hwd_replacement_103)
    delta = feature.diff(5)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00103000).reindex(feature.index)
HWD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['hwd_replacement_d2_103'] = {'inputs': ['hwd_replacement_103'], 'func': hwd_replacement_d2_103}


def hwd_replacement_d2_104(hwd_replacement_104):
    feature = _clean(hwd_replacement_104)
    delta = feature.diff(8)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00104000).reindex(feature.index)
HWD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['hwd_replacement_d2_104'] = {'inputs': ['hwd_replacement_104'], 'func': hwd_replacement_d2_104}


def hwd_replacement_d2_105(hwd_replacement_105):
    feature = _clean(hwd_replacement_105)
    delta = feature.diff(13)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00105000).reindex(feature.index)
HWD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['hwd_replacement_d2_105'] = {'inputs': ['hwd_replacement_105'], 'func': hwd_replacement_d2_105}


def hwd_replacement_d2_106(hwd_replacement_106):
    feature = _clean(hwd_replacement_106)
    delta = feature.diff(21)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00106000).reindex(feature.index)
HWD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['hwd_replacement_d2_106'] = {'inputs': ['hwd_replacement_106'], 'func': hwd_replacement_d2_106}


def hwd_replacement_d2_107(hwd_replacement_107):
    feature = _clean(hwd_replacement_107)
    delta = feature.diff(34)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00107000).reindex(feature.index)
HWD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['hwd_replacement_d2_107'] = {'inputs': ['hwd_replacement_107'], 'func': hwd_replacement_d2_107}


def hwd_replacement_d2_108(hwd_replacement_108):
    feature = _clean(hwd_replacement_108)
    delta = feature.diff(55)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00108000).reindex(feature.index)
HWD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['hwd_replacement_d2_108'] = {'inputs': ['hwd_replacement_108'], 'func': hwd_replacement_d2_108}


def hwd_replacement_d2_109(hwd_replacement_109):
    feature = _clean(hwd_replacement_109)
    delta = feature.diff(89)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00109000).reindex(feature.index)
HWD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['hwd_replacement_d2_109'] = {'inputs': ['hwd_replacement_109'], 'func': hwd_replacement_d2_109}


def hwd_replacement_d2_110(hwd_replacement_110):
    feature = _clean(hwd_replacement_110)
    delta = feature.diff(1)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00110000).reindex(feature.index)
HWD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['hwd_replacement_d2_110'] = {'inputs': ['hwd_replacement_110'], 'func': hwd_replacement_d2_110}


def hwd_replacement_d2_111(hwd_replacement_111):
    feature = _clean(hwd_replacement_111)
    delta = feature.diff(2)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00111000).reindex(feature.index)
HWD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['hwd_replacement_d2_111'] = {'inputs': ['hwd_replacement_111'], 'func': hwd_replacement_d2_111}


def hwd_replacement_d2_112(hwd_replacement_112):
    feature = _clean(hwd_replacement_112)
    delta = feature.diff(3)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00112000).reindex(feature.index)
HWD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['hwd_replacement_d2_112'] = {'inputs': ['hwd_replacement_112'], 'func': hwd_replacement_d2_112}


def hwd_replacement_d2_113(hwd_replacement_113):
    feature = _clean(hwd_replacement_113)
    delta = feature.diff(5)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00113000).reindex(feature.index)
HWD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['hwd_replacement_d2_113'] = {'inputs': ['hwd_replacement_113'], 'func': hwd_replacement_d2_113}


def hwd_replacement_d2_114(hwd_replacement_114):
    feature = _clean(hwd_replacement_114)
    delta = feature.diff(8)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00114000).reindex(feature.index)
HWD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['hwd_replacement_d2_114'] = {'inputs': ['hwd_replacement_114'], 'func': hwd_replacement_d2_114}


def hwd_replacement_d2_115(hwd_replacement_115):
    feature = _clean(hwd_replacement_115)
    delta = feature.diff(13)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00115000).reindex(feature.index)
HWD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['hwd_replacement_d2_115'] = {'inputs': ['hwd_replacement_115'], 'func': hwd_replacement_d2_115}


def hwd_replacement_d2_116(hwd_replacement_116):
    feature = _clean(hwd_replacement_116)
    delta = feature.diff(21)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00116000).reindex(feature.index)
HWD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['hwd_replacement_d2_116'] = {'inputs': ['hwd_replacement_116'], 'func': hwd_replacement_d2_116}


def hwd_replacement_d2_117(hwd_replacement_117):
    feature = _clean(hwd_replacement_117)
    delta = feature.diff(34)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00117000).reindex(feature.index)
HWD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['hwd_replacement_d2_117'] = {'inputs': ['hwd_replacement_117'], 'func': hwd_replacement_d2_117}


def hwd_replacement_d2_118(hwd_replacement_118):
    feature = _clean(hwd_replacement_118)
    delta = feature.diff(55)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00118000).reindex(feature.index)
HWD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['hwd_replacement_d2_118'] = {'inputs': ['hwd_replacement_118'], 'func': hwd_replacement_d2_118}


def hwd_replacement_d2_119(hwd_replacement_119):
    feature = _clean(hwd_replacement_119)
    delta = feature.diff(89)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00119000).reindex(feature.index)
HWD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['hwd_replacement_d2_119'] = {'inputs': ['hwd_replacement_119'], 'func': hwd_replacement_d2_119}


def hwd_replacement_d2_120(hwd_replacement_120):
    feature = _clean(hwd_replacement_120)
    delta = feature.diff(1)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00120000).reindex(feature.index)
HWD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['hwd_replacement_d2_120'] = {'inputs': ['hwd_replacement_120'], 'func': hwd_replacement_d2_120}


def hwd_replacement_d2_121(hwd_replacement_121):
    feature = _clean(hwd_replacement_121)
    delta = feature.diff(2)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00121000).reindex(feature.index)
HWD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['hwd_replacement_d2_121'] = {'inputs': ['hwd_replacement_121'], 'func': hwd_replacement_d2_121}


def hwd_replacement_d2_122(hwd_replacement_122):
    feature = _clean(hwd_replacement_122)
    delta = feature.diff(3)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00122000).reindex(feature.index)
HWD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['hwd_replacement_d2_122'] = {'inputs': ['hwd_replacement_122'], 'func': hwd_replacement_d2_122}


def hwd_replacement_d2_123(hwd_replacement_123):
    feature = _clean(hwd_replacement_123)
    delta = feature.diff(5)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00123000).reindex(feature.index)
HWD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['hwd_replacement_d2_123'] = {'inputs': ['hwd_replacement_123'], 'func': hwd_replacement_d2_123}


def hwd_replacement_d2_124(hwd_replacement_124):
    feature = _clean(hwd_replacement_124)
    delta = feature.diff(8)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00124000).reindex(feature.index)
HWD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['hwd_replacement_d2_124'] = {'inputs': ['hwd_replacement_124'], 'func': hwd_replacement_d2_124}


def hwd_replacement_d2_125(hwd_replacement_125):
    feature = _clean(hwd_replacement_125)
    delta = feature.diff(13)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00125000).reindex(feature.index)
HWD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['hwd_replacement_d2_125'] = {'inputs': ['hwd_replacement_125'], 'func': hwd_replacement_d2_125}


def hwd_replacement_d2_126(hwd_replacement_126):
    feature = _clean(hwd_replacement_126)
    delta = feature.diff(21)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00126000).reindex(feature.index)
HWD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['hwd_replacement_d2_126'] = {'inputs': ['hwd_replacement_126'], 'func': hwd_replacement_d2_126}


def hwd_replacement_d2_127(hwd_replacement_127):
    feature = _clean(hwd_replacement_127)
    delta = feature.diff(34)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00127000).reindex(feature.index)
HWD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['hwd_replacement_d2_127'] = {'inputs': ['hwd_replacement_127'], 'func': hwd_replacement_d2_127}


def hwd_replacement_d2_128(hwd_replacement_128):
    feature = _clean(hwd_replacement_128)
    delta = feature.diff(55)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00128000).reindex(feature.index)
HWD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['hwd_replacement_d2_128'] = {'inputs': ['hwd_replacement_128'], 'func': hwd_replacement_d2_128}


def hwd_replacement_d2_129(hwd_replacement_129):
    feature = _clean(hwd_replacement_129)
    delta = feature.diff(89)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00129000).reindex(feature.index)
HWD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['hwd_replacement_d2_129'] = {'inputs': ['hwd_replacement_129'], 'func': hwd_replacement_d2_129}


def hwd_replacement_d2_130(hwd_replacement_130):
    feature = _clean(hwd_replacement_130)
    delta = feature.diff(1)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00130000).reindex(feature.index)
HWD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['hwd_replacement_d2_130'] = {'inputs': ['hwd_replacement_130'], 'func': hwd_replacement_d2_130}


def hwd_replacement_d2_131(hwd_replacement_131):
    feature = _clean(hwd_replacement_131)
    delta = feature.diff(2)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00131000).reindex(feature.index)
HWD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['hwd_replacement_d2_131'] = {'inputs': ['hwd_replacement_131'], 'func': hwd_replacement_d2_131}


def hwd_replacement_d2_132(hwd_replacement_132):
    feature = _clean(hwd_replacement_132)
    delta = feature.diff(3)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00132000).reindex(feature.index)
HWD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['hwd_replacement_d2_132'] = {'inputs': ['hwd_replacement_132'], 'func': hwd_replacement_d2_132}


def hwd_replacement_d2_133(hwd_replacement_133):
    feature = _clean(hwd_replacement_133)
    delta = feature.diff(5)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00133000).reindex(feature.index)
HWD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['hwd_replacement_d2_133'] = {'inputs': ['hwd_replacement_133'], 'func': hwd_replacement_d2_133}


def hwd_replacement_d2_134(hwd_replacement_134):
    feature = _clean(hwd_replacement_134)
    delta = feature.diff(8)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00134000).reindex(feature.index)
HWD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['hwd_replacement_d2_134'] = {'inputs': ['hwd_replacement_134'], 'func': hwd_replacement_d2_134}


def hwd_replacement_d2_135(hwd_replacement_135):
    feature = _clean(hwd_replacement_135)
    delta = feature.diff(13)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00135000).reindex(feature.index)
HWD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['hwd_replacement_d2_135'] = {'inputs': ['hwd_replacement_135'], 'func': hwd_replacement_d2_135}


def hwd_replacement_d2_136(hwd_replacement_136):
    feature = _clean(hwd_replacement_136)
    delta = feature.diff(21)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00136000).reindex(feature.index)
HWD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['hwd_replacement_d2_136'] = {'inputs': ['hwd_replacement_136'], 'func': hwd_replacement_d2_136}


def hwd_replacement_d2_137(hwd_replacement_137):
    feature = _clean(hwd_replacement_137)
    delta = feature.diff(34)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00137000).reindex(feature.index)
HWD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['hwd_replacement_d2_137'] = {'inputs': ['hwd_replacement_137'], 'func': hwd_replacement_d2_137}


def hwd_replacement_d2_138(hwd_replacement_138):
    feature = _clean(hwd_replacement_138)
    delta = feature.diff(55)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00138000).reindex(feature.index)
HWD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['hwd_replacement_d2_138'] = {'inputs': ['hwd_replacement_138'], 'func': hwd_replacement_d2_138}


def hwd_replacement_d2_139(hwd_replacement_139):
    feature = _clean(hwd_replacement_139)
    delta = feature.diff(89)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00139000).reindex(feature.index)
HWD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['hwd_replacement_d2_139'] = {'inputs': ['hwd_replacement_139'], 'func': hwd_replacement_d2_139}


def hwd_replacement_d2_140(hwd_replacement_140):
    feature = _clean(hwd_replacement_140)
    delta = feature.diff(1)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00140000).reindex(feature.index)
HWD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['hwd_replacement_d2_140'] = {'inputs': ['hwd_replacement_140'], 'func': hwd_replacement_d2_140}


def hwd_replacement_d2_141(hwd_replacement_141):
    feature = _clean(hwd_replacement_141)
    delta = feature.diff(2)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00141000).reindex(feature.index)
HWD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['hwd_replacement_d2_141'] = {'inputs': ['hwd_replacement_141'], 'func': hwd_replacement_d2_141}


def hwd_replacement_d2_142(hwd_replacement_142):
    feature = _clean(hwd_replacement_142)
    delta = feature.diff(3)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00142000).reindex(feature.index)
HWD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['hwd_replacement_d2_142'] = {'inputs': ['hwd_replacement_142'], 'func': hwd_replacement_d2_142}


def hwd_replacement_d2_143(hwd_replacement_143):
    feature = _clean(hwd_replacement_143)
    delta = feature.diff(5)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00143000).reindex(feature.index)
HWD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['hwd_replacement_d2_143'] = {'inputs': ['hwd_replacement_143'], 'func': hwd_replacement_d2_143}


def hwd_replacement_d2_144(hwd_replacement_144):
    feature = _clean(hwd_replacement_144)
    delta = feature.diff(8)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00144000).reindex(feature.index)
HWD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['hwd_replacement_d2_144'] = {'inputs': ['hwd_replacement_144'], 'func': hwd_replacement_d2_144}


def hwd_replacement_d2_145(hwd_replacement_145):
    feature = _clean(hwd_replacement_145)
    delta = feature.diff(13)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00145000).reindex(feature.index)
HWD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['hwd_replacement_d2_145'] = {'inputs': ['hwd_replacement_145'], 'func': hwd_replacement_d2_145}


def hwd_replacement_d2_146(hwd_replacement_146):
    feature = _clean(hwd_replacement_146)
    delta = feature.diff(21)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00146000).reindex(feature.index)
HWD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['hwd_replacement_d2_146'] = {'inputs': ['hwd_replacement_146'], 'func': hwd_replacement_d2_146}


def hwd_replacement_d2_147(hwd_replacement_147):
    feature = _clean(hwd_replacement_147)
    delta = feature.diff(34)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00147000).reindex(feature.index)
HWD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['hwd_replacement_d2_147'] = {'inputs': ['hwd_replacement_147'], 'func': hwd_replacement_d2_147}


def hwd_replacement_d2_148(hwd_replacement_148):
    feature = _clean(hwd_replacement_148)
    delta = feature.diff(55)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00148000).reindex(feature.index)
HWD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['hwd_replacement_d2_148'] = {'inputs': ['hwd_replacement_148'], 'func': hwd_replacement_d2_148}


def hwd_replacement_d2_149(hwd_replacement_149):
    feature = _clean(hwd_replacement_149)
    delta = feature.diff(89)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00149000).reindex(feature.index)
HWD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['hwd_replacement_d2_149'] = {'inputs': ['hwd_replacement_149'], 'func': hwd_replacement_d2_149}


def hwd_replacement_d2_150(hwd_replacement_150):
    feature = _clean(hwd_replacement_150)
    delta = feature.diff(1)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00150000).reindex(feature.index)
HWD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['hwd_replacement_d2_150'] = {'inputs': ['hwd_replacement_150'], 'func': hwd_replacement_d2_150}


def hwd_replacement_d2_151(hwd_replacement_151):
    feature = _clean(hwd_replacement_151)
    delta = feature.diff(2)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00151000).reindex(feature.index)
HWD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['hwd_replacement_d2_151'] = {'inputs': ['hwd_replacement_151'], 'func': hwd_replacement_d2_151}


def hwd_replacement_d2_152(hwd_replacement_152):
    feature = _clean(hwd_replacement_152)
    delta = feature.diff(3)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00152000).reindex(feature.index)
HWD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['hwd_replacement_d2_152'] = {'inputs': ['hwd_replacement_152'], 'func': hwd_replacement_d2_152}


def hwd_replacement_d2_153(hwd_replacement_153):
    feature = _clean(hwd_replacement_153)
    delta = feature.diff(5)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00153000).reindex(feature.index)
HWD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['hwd_replacement_d2_153'] = {'inputs': ['hwd_replacement_153'], 'func': hwd_replacement_d2_153}


def hwd_replacement_d2_154(hwd_replacement_154):
    feature = _clean(hwd_replacement_154)
    delta = feature.diff(8)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00154000).reindex(feature.index)
HWD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['hwd_replacement_d2_154'] = {'inputs': ['hwd_replacement_154'], 'func': hwd_replacement_d2_154}


def hwd_replacement_d2_155(hwd_replacement_155):
    feature = _clean(hwd_replacement_155)
    delta = feature.diff(13)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00155000).reindex(feature.index)
HWD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['hwd_replacement_d2_155'] = {'inputs': ['hwd_replacement_155'], 'func': hwd_replacement_d2_155}


def hwd_replacement_d2_156(hwd_replacement_156):
    feature = _clean(hwd_replacement_156)
    delta = feature.diff(21)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00156000).reindex(feature.index)
HWD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['hwd_replacement_d2_156'] = {'inputs': ['hwd_replacement_156'], 'func': hwd_replacement_d2_156}


def hwd_replacement_d2_157(hwd_replacement_157):
    feature = _clean(hwd_replacement_157)
    delta = feature.diff(34)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00157000).reindex(feature.index)
HWD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['hwd_replacement_d2_157'] = {'inputs': ['hwd_replacement_157'], 'func': hwd_replacement_d2_157}


def hwd_replacement_d2_158(hwd_replacement_158):
    feature = _clean(hwd_replacement_158)
    delta = feature.diff(55)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00158000).reindex(feature.index)
HWD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['hwd_replacement_d2_158'] = {'inputs': ['hwd_replacement_158'], 'func': hwd_replacement_d2_158}


def hwd_replacement_d2_159(hwd_replacement_159):
    feature = _clean(hwd_replacement_159)
    delta = feature.diff(89)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00159000).reindex(feature.index)
HWD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['hwd_replacement_d2_159'] = {'inputs': ['hwd_replacement_159'], 'func': hwd_replacement_d2_159}


def hwd_replacement_d2_160(hwd_replacement_160):
    feature = _clean(hwd_replacement_160)
    delta = feature.diff(1)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00160000).reindex(feature.index)
HWD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['hwd_replacement_d2_160'] = {'inputs': ['hwd_replacement_160'], 'func': hwd_replacement_d2_160}


def hwd_replacement_d2_161(hwd_replacement_161):
    feature = _clean(hwd_replacement_161)
    delta = feature.diff(2)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00161000).reindex(feature.index)
HWD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['hwd_replacement_d2_161'] = {'inputs': ['hwd_replacement_161'], 'func': hwd_replacement_d2_161}


def hwd_replacement_d2_162(hwd_replacement_162):
    feature = _clean(hwd_replacement_162)
    delta = feature.diff(3)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00162000).reindex(feature.index)
HWD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['hwd_replacement_d2_162'] = {'inputs': ['hwd_replacement_162'], 'func': hwd_replacement_d2_162}


def hwd_replacement_d2_163(hwd_replacement_163):
    feature = _clean(hwd_replacement_163)
    delta = feature.diff(5)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00163000).reindex(feature.index)
HWD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['hwd_replacement_d2_163'] = {'inputs': ['hwd_replacement_163'], 'func': hwd_replacement_d2_163}


def hwd_replacement_d2_164(hwd_replacement_164):
    feature = _clean(hwd_replacement_164)
    delta = feature.diff(8)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00164000).reindex(feature.index)
HWD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['hwd_replacement_d2_164'] = {'inputs': ['hwd_replacement_164'], 'func': hwd_replacement_d2_164}


def hwd_replacement_d2_165(hwd_replacement_165):
    feature = _clean(hwd_replacement_165)
    delta = feature.diff(13)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00165000).reindex(feature.index)
HWD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['hwd_replacement_d2_165'] = {'inputs': ['hwd_replacement_165'], 'func': hwd_replacement_d2_165}


def hwd_replacement_d2_166(hwd_replacement_166):
    feature = _clean(hwd_replacement_166)
    delta = feature.diff(21)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00166000).reindex(feature.index)
HWD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['hwd_replacement_d2_166'] = {'inputs': ['hwd_replacement_166'], 'func': hwd_replacement_d2_166}


def hwd_replacement_d2_167(hwd_replacement_167):
    feature = _clean(hwd_replacement_167)
    delta = feature.diff(34)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00167000).reindex(feature.index)
HWD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['hwd_replacement_d2_167'] = {'inputs': ['hwd_replacement_167'], 'func': hwd_replacement_d2_167}


def hwd_replacement_d2_168(hwd_replacement_168):
    feature = _clean(hwd_replacement_168)
    delta = feature.diff(55)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00168000).reindex(feature.index)
HWD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['hwd_replacement_d2_168'] = {'inputs': ['hwd_replacement_168'], 'func': hwd_replacement_d2_168}


def hwd_replacement_d2_169(hwd_replacement_169):
    feature = _clean(hwd_replacement_169)
    delta = feature.diff(89)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00169000).reindex(feature.index)
HWD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['hwd_replacement_d2_169'] = {'inputs': ['hwd_replacement_169'], 'func': hwd_replacement_d2_169}


def hwd_replacement_d2_170(hwd_replacement_170):
    feature = _clean(hwd_replacement_170)
    delta = feature.diff(1)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00170000).reindex(feature.index)
HWD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['hwd_replacement_d2_170'] = {'inputs': ['hwd_replacement_170'], 'func': hwd_replacement_d2_170}


# Base-universe derivative extensions for repaired first-base features.
HWD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY = {}


def _base_universe_d2(feature, idx):
    feature = _clean(feature) if '_clean' in globals() else _s(feature).replace([np.inf, -np.inf], np.nan)
    windows = [1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    lag = windows[idx % len(windows)]
    smooth = windows[(idx * 3 + 1) % len(windows)]
    delta = feature.diff(lag)
    local = feature - feature.rolling(max(3, smooth), min_periods=2).mean()
    out = delta + local.fillna(0.0) * (0.00037 * ((idx % 17) + 1))
    return out.replace([np.inf, -np.inf], np.nan).reindex(feature.index)


def hwd_base_universe_d2_001_hwd_002_low_distance_10_002(hwd_002_low_distance_10_002):
    return _base_universe_d2(hwd_002_low_distance_10_002, 1)
HWD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['hwd_base_universe_d2_001_hwd_002_low_distance_10_002'] = {'inputs': ['hwd_002_low_distance_10_002'], 'func': hwd_base_universe_d2_001_hwd_002_low_distance_10_002}


def hwd_base_universe_d2_002_hwd_003_underwater_area_21_003(hwd_003_underwater_area_21_003):
    return _base_universe_d2(hwd_003_underwater_area_21_003, 2)
HWD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['hwd_base_universe_d2_002_hwd_003_underwater_area_21_003'] = {'inputs': ['hwd_003_underwater_area_21_003'], 'func': hwd_base_universe_d2_002_hwd_003_underwater_area_21_003}


def hwd_base_universe_d2_003_hwd_006_lower_high_ratio_84_006(hwd_006_lower_high_ratio_84_006):
    return _base_universe_d2(hwd_006_lower_high_ratio_84_006, 3)
HWD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['hwd_base_universe_d2_003_hwd_006_lower_high_ratio_84_006'] = {'inputs': ['hwd_006_lower_high_ratio_84_006'], 'func': hwd_base_universe_d2_003_hwd_006_lower_high_ratio_84_006}


def hwd_base_universe_d2_004_hwd_008_low_distance_189_008(hwd_008_low_distance_189_008):
    return _base_universe_d2(hwd_008_low_distance_189_008, 4)
HWD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['hwd_base_universe_d2_004_hwd_008_low_distance_189_008'] = {'inputs': ['hwd_008_low_distance_189_008'], 'func': hwd_base_universe_d2_004_hwd_008_low_distance_189_008}


def hwd_base_universe_d2_005_hwd_009_underwater_area_252_009(hwd_009_underwater_area_252_009):
    return _base_universe_d2(hwd_009_underwater_area_252_009, 5)
HWD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['hwd_base_universe_d2_005_hwd_009_underwater_area_252_009'] = {'inputs': ['hwd_009_underwater_area_252_009'], 'func': hwd_base_universe_d2_005_hwd_009_underwater_area_252_009}


def hwd_base_universe_d2_006_hwd_012_lower_high_ratio_756_012(hwd_012_lower_high_ratio_756_012):
    return _base_universe_d2(hwd_012_lower_high_ratio_756_012, 6)
HWD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['hwd_base_universe_d2_006_hwd_012_lower_high_ratio_756_012'] = {'inputs': ['hwd_012_lower_high_ratio_756_012'], 'func': hwd_base_universe_d2_006_hwd_012_lower_high_ratio_756_012}


def hwd_base_universe_d2_007_hwd_014_low_distance_1260_014(hwd_014_low_distance_1260_014):
    return _base_universe_d2(hwd_014_low_distance_1260_014, 7)
HWD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['hwd_base_universe_d2_007_hwd_014_low_distance_1260_014'] = {'inputs': ['hwd_014_low_distance_1260_014'], 'func': hwd_base_universe_d2_007_hwd_014_low_distance_1260_014}


def hwd_base_universe_d2_008_hwd_015_underwater_area_1512_015(hwd_015_underwater_area_1512_015):
    return _base_universe_d2(hwd_015_underwater_area_1512_015, 8)
HWD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['hwd_base_universe_d2_008_hwd_015_underwater_area_1512_015'] = {'inputs': ['hwd_015_underwater_area_1512_015'], 'func': hwd_base_universe_d2_008_hwd_015_underwater_area_1512_015}


def hwd_base_universe_d2_009_hwd_018_lower_high_ratio_21_018(hwd_018_lower_high_ratio_21_018):
    return _base_universe_d2(hwd_018_lower_high_ratio_21_018, 9)
HWD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['hwd_base_universe_d2_009_hwd_018_lower_high_ratio_21_018'] = {'inputs': ['hwd_018_lower_high_ratio_21_018'], 'func': hwd_base_universe_d2_009_hwd_018_lower_high_ratio_21_018}


def hwd_base_universe_d2_010_hwd_020_low_distance_63_020(hwd_020_low_distance_63_020):
    return _base_universe_d2(hwd_020_low_distance_63_020, 10)
HWD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['hwd_base_universe_d2_010_hwd_020_low_distance_63_020'] = {'inputs': ['hwd_020_low_distance_63_020'], 'func': hwd_base_universe_d2_010_hwd_020_low_distance_63_020}


def hwd_base_universe_d2_011_hwd_021_underwater_area_84_021(hwd_021_underwater_area_84_021):
    return _base_universe_d2(hwd_021_underwater_area_84_021, 11)
HWD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['hwd_base_universe_d2_011_hwd_021_underwater_area_84_021'] = {'inputs': ['hwd_021_underwater_area_84_021'], 'func': hwd_base_universe_d2_011_hwd_021_underwater_area_84_021}


def hwd_base_universe_d2_012_hwd_024_lower_high_ratio_252_024(hwd_024_lower_high_ratio_252_024):
    return _base_universe_d2(hwd_024_lower_high_ratio_252_024, 12)
HWD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['hwd_base_universe_d2_012_hwd_024_lower_high_ratio_252_024'] = {'inputs': ['hwd_024_lower_high_ratio_252_024'], 'func': hwd_base_universe_d2_012_hwd_024_lower_high_ratio_252_024}


def hwd_base_universe_d2_013_hwd_026_low_distance_504_026(hwd_026_low_distance_504_026):
    return _base_universe_d2(hwd_026_low_distance_504_026, 13)
HWD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['hwd_base_universe_d2_013_hwd_026_low_distance_504_026'] = {'inputs': ['hwd_026_low_distance_504_026'], 'func': hwd_base_universe_d2_013_hwd_026_low_distance_504_026}


def hwd_base_universe_d2_014_hwd_027_underwater_area_756_027(hwd_027_underwater_area_756_027):
    return _base_universe_d2(hwd_027_underwater_area_756_027, 14)
HWD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['hwd_base_universe_d2_014_hwd_027_underwater_area_756_027'] = {'inputs': ['hwd_027_underwater_area_756_027'], 'func': hwd_base_universe_d2_014_hwd_027_underwater_area_756_027}


def hwd_base_universe_d2_015_hwd_030_lower_high_ratio_1512_030(hwd_030_lower_high_ratio_1512_030):
    return _base_universe_d2(hwd_030_lower_high_ratio_1512_030, 15)
HWD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['hwd_base_universe_d2_015_hwd_030_lower_high_ratio_1512_030'] = {'inputs': ['hwd_030_lower_high_ratio_1512_030'], 'func': hwd_base_universe_d2_015_hwd_030_lower_high_ratio_1512_030}


def hwd_base_universe_d2_016_hwd_basefill_004(hwd_basefill_004):
    return _base_universe_d2(hwd_basefill_004, 16)
HWD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['hwd_base_universe_d2_016_hwd_basefill_004'] = {'inputs': ['hwd_basefill_004'], 'func': hwd_base_universe_d2_016_hwd_basefill_004}


def hwd_base_universe_d2_017_hwd_basefill_005(hwd_basefill_005):
    return _base_universe_d2(hwd_basefill_005, 17)
HWD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['hwd_base_universe_d2_017_hwd_basefill_005'] = {'inputs': ['hwd_basefill_005'], 'func': hwd_base_universe_d2_017_hwd_basefill_005}


def hwd_base_universe_d2_018_hwd_basefill_010(hwd_basefill_010):
    return _base_universe_d2(hwd_basefill_010, 18)
HWD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['hwd_base_universe_d2_018_hwd_basefill_010'] = {'inputs': ['hwd_basefill_010'], 'func': hwd_base_universe_d2_018_hwd_basefill_010}


def hwd_base_universe_d2_019_hwd_basefill_011(hwd_basefill_011):
    return _base_universe_d2(hwd_basefill_011, 19)
HWD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['hwd_base_universe_d2_019_hwd_basefill_011'] = {'inputs': ['hwd_basefill_011'], 'func': hwd_base_universe_d2_019_hwd_basefill_011}


def hwd_base_universe_d2_020_hwd_basefill_016(hwd_basefill_016):
    return _base_universe_d2(hwd_basefill_016, 20)
HWD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['hwd_base_universe_d2_020_hwd_basefill_016'] = {'inputs': ['hwd_basefill_016'], 'func': hwd_base_universe_d2_020_hwd_basefill_016}


def hwd_base_universe_d2_021_hwd_basefill_017(hwd_basefill_017):
    return _base_universe_d2(hwd_basefill_017, 21)
HWD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['hwd_base_universe_d2_021_hwd_basefill_017'] = {'inputs': ['hwd_basefill_017'], 'func': hwd_base_universe_d2_021_hwd_basefill_017}


def hwd_base_universe_d2_022_hwd_basefill_022(hwd_basefill_022):
    return _base_universe_d2(hwd_basefill_022, 22)
HWD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['hwd_base_universe_d2_022_hwd_basefill_022'] = {'inputs': ['hwd_basefill_022'], 'func': hwd_base_universe_d2_022_hwd_basefill_022}


def hwd_base_universe_d2_023_hwd_basefill_023(hwd_basefill_023):
    return _base_universe_d2(hwd_basefill_023, 23)
HWD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['hwd_base_universe_d2_023_hwd_basefill_023'] = {'inputs': ['hwd_basefill_023'], 'func': hwd_base_universe_d2_023_hwd_basefill_023}


def hwd_base_universe_d2_024_hwd_basefill_028(hwd_basefill_028):
    return _base_universe_d2(hwd_basefill_028, 24)
HWD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['hwd_base_universe_d2_024_hwd_basefill_028'] = {'inputs': ['hwd_basefill_028'], 'func': hwd_base_universe_d2_024_hwd_basefill_028}


def hwd_base_universe_d2_025_hwd_basefill_029(hwd_basefill_029):
    return _base_universe_d2(hwd_basefill_029, 25)
HWD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['hwd_base_universe_d2_025_hwd_basefill_029'] = {'inputs': ['hwd_basefill_029'], 'func': hwd_base_universe_d2_025_hwd_basefill_029}


def hwd_base_universe_d2_026_hwd_basefill_031(hwd_basefill_031):
    return _base_universe_d2(hwd_basefill_031, 26)
HWD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['hwd_base_universe_d2_026_hwd_basefill_031'] = {'inputs': ['hwd_basefill_031'], 'func': hwd_base_universe_d2_026_hwd_basefill_031}


def hwd_base_universe_d2_027_hwd_basefill_032(hwd_basefill_032):
    return _base_universe_d2(hwd_basefill_032, 27)
HWD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['hwd_base_universe_d2_027_hwd_basefill_032'] = {'inputs': ['hwd_basefill_032'], 'func': hwd_base_universe_d2_027_hwd_basefill_032}


def hwd_base_universe_d2_028_hwd_basefill_033(hwd_basefill_033):
    return _base_universe_d2(hwd_basefill_033, 28)
HWD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['hwd_base_universe_d2_028_hwd_basefill_033'] = {'inputs': ['hwd_basefill_033'], 'func': hwd_base_universe_d2_028_hwd_basefill_033}


def hwd_base_universe_d2_029_hwd_basefill_034(hwd_basefill_034):
    return _base_universe_d2(hwd_basefill_034, 29)
HWD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['hwd_base_universe_d2_029_hwd_basefill_034'] = {'inputs': ['hwd_basefill_034'], 'func': hwd_base_universe_d2_029_hwd_basefill_034}


def hwd_base_universe_d2_030_hwd_basefill_035(hwd_basefill_035):
    return _base_universe_d2(hwd_basefill_035, 30)
HWD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['hwd_base_universe_d2_030_hwd_basefill_035'] = {'inputs': ['hwd_basefill_035'], 'func': hwd_base_universe_d2_030_hwd_basefill_035}


def hwd_base_universe_d2_031_hwd_basefill_036(hwd_basefill_036):
    return _base_universe_d2(hwd_basefill_036, 31)
HWD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['hwd_base_universe_d2_031_hwd_basefill_036'] = {'inputs': ['hwd_basefill_036'], 'func': hwd_base_universe_d2_031_hwd_basefill_036}


def hwd_base_universe_d2_032_hwd_basefill_037(hwd_basefill_037):
    return _base_universe_d2(hwd_basefill_037, 32)
HWD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['hwd_base_universe_d2_032_hwd_basefill_037'] = {'inputs': ['hwd_basefill_037'], 'func': hwd_base_universe_d2_032_hwd_basefill_037}


def hwd_base_universe_d2_033_hwd_basefill_038(hwd_basefill_038):
    return _base_universe_d2(hwd_basefill_038, 33)
HWD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['hwd_base_universe_d2_033_hwd_basefill_038'] = {'inputs': ['hwd_basefill_038'], 'func': hwd_base_universe_d2_033_hwd_basefill_038}


def hwd_base_universe_d2_034_hwd_basefill_039(hwd_basefill_039):
    return _base_universe_d2(hwd_basefill_039, 34)
HWD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['hwd_base_universe_d2_034_hwd_basefill_039'] = {'inputs': ['hwd_basefill_039'], 'func': hwd_base_universe_d2_034_hwd_basefill_039}


def hwd_base_universe_d2_035_hwd_basefill_040(hwd_basefill_040):
    return _base_universe_d2(hwd_basefill_040, 35)
HWD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['hwd_base_universe_d2_035_hwd_basefill_040'] = {'inputs': ['hwd_basefill_040'], 'func': hwd_base_universe_d2_035_hwd_basefill_040}


def hwd_base_universe_d2_036_hwd_basefill_041(hwd_basefill_041):
    return _base_universe_d2(hwd_basefill_041, 36)
HWD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['hwd_base_universe_d2_036_hwd_basefill_041'] = {'inputs': ['hwd_basefill_041'], 'func': hwd_base_universe_d2_036_hwd_basefill_041}


def hwd_base_universe_d2_037_hwd_basefill_042(hwd_basefill_042):
    return _base_universe_d2(hwd_basefill_042, 37)
HWD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['hwd_base_universe_d2_037_hwd_basefill_042'] = {'inputs': ['hwd_basefill_042'], 'func': hwd_base_universe_d2_037_hwd_basefill_042}


def hwd_base_universe_d2_038_hwd_basefill_043(hwd_basefill_043):
    return _base_universe_d2(hwd_basefill_043, 38)
HWD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['hwd_base_universe_d2_038_hwd_basefill_043'] = {'inputs': ['hwd_basefill_043'], 'func': hwd_base_universe_d2_038_hwd_basefill_043}


def hwd_base_universe_d2_039_hwd_basefill_044(hwd_basefill_044):
    return _base_universe_d2(hwd_basefill_044, 39)
HWD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['hwd_base_universe_d2_039_hwd_basefill_044'] = {'inputs': ['hwd_basefill_044'], 'func': hwd_base_universe_d2_039_hwd_basefill_044}


def hwd_base_universe_d2_040_hwd_basefill_045(hwd_basefill_045):
    return _base_universe_d2(hwd_basefill_045, 40)
HWD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['hwd_base_universe_d2_040_hwd_basefill_045'] = {'inputs': ['hwd_basefill_045'], 'func': hwd_base_universe_d2_040_hwd_basefill_045}


def hwd_base_universe_d2_041_hwd_basefill_046(hwd_basefill_046):
    return _base_universe_d2(hwd_basefill_046, 41)
HWD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['hwd_base_universe_d2_041_hwd_basefill_046'] = {'inputs': ['hwd_basefill_046'], 'func': hwd_base_universe_d2_041_hwd_basefill_046}


def hwd_base_universe_d2_042_hwd_basefill_047(hwd_basefill_047):
    return _base_universe_d2(hwd_basefill_047, 42)
HWD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['hwd_base_universe_d2_042_hwd_basefill_047'] = {'inputs': ['hwd_basefill_047'], 'func': hwd_base_universe_d2_042_hwd_basefill_047}


def hwd_base_universe_d2_043_hwd_basefill_048(hwd_basefill_048):
    return _base_universe_d2(hwd_basefill_048, 43)
HWD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['hwd_base_universe_d2_043_hwd_basefill_048'] = {'inputs': ['hwd_basefill_048'], 'func': hwd_base_universe_d2_043_hwd_basefill_048}


def hwd_base_universe_d2_044_hwd_basefill_049(hwd_basefill_049):
    return _base_universe_d2(hwd_basefill_049, 44)
HWD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['hwd_base_universe_d2_044_hwd_basefill_049'] = {'inputs': ['hwd_basefill_049'], 'func': hwd_base_universe_d2_044_hwd_basefill_049}


def hwd_base_universe_d2_045_hwd_basefill_050(hwd_basefill_050):
    return _base_universe_d2(hwd_basefill_050, 45)
HWD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['hwd_base_universe_d2_045_hwd_basefill_050'] = {'inputs': ['hwd_basefill_050'], 'func': hwd_base_universe_d2_045_hwd_basefill_050}


def hwd_base_universe_d2_046_hwd_basefill_051(hwd_basefill_051):
    return _base_universe_d2(hwd_basefill_051, 46)
HWD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['hwd_base_universe_d2_046_hwd_basefill_051'] = {'inputs': ['hwd_basefill_051'], 'func': hwd_base_universe_d2_046_hwd_basefill_051}


def hwd_base_universe_d2_047_hwd_basefill_052(hwd_basefill_052):
    return _base_universe_d2(hwd_basefill_052, 47)
HWD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['hwd_base_universe_d2_047_hwd_basefill_052'] = {'inputs': ['hwd_basefill_052'], 'func': hwd_base_universe_d2_047_hwd_basefill_052}


def hwd_base_universe_d2_048_hwd_basefill_053(hwd_basefill_053):
    return _base_universe_d2(hwd_basefill_053, 48)
HWD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['hwd_base_universe_d2_048_hwd_basefill_053'] = {'inputs': ['hwd_basefill_053'], 'func': hwd_base_universe_d2_048_hwd_basefill_053}


def hwd_base_universe_d2_049_hwd_basefill_054(hwd_basefill_054):
    return _base_universe_d2(hwd_basefill_054, 49)
HWD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['hwd_base_universe_d2_049_hwd_basefill_054'] = {'inputs': ['hwd_basefill_054'], 'func': hwd_base_universe_d2_049_hwd_basefill_054}


def hwd_base_universe_d2_050_hwd_basefill_055(hwd_basefill_055):
    return _base_universe_d2(hwd_basefill_055, 50)
HWD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['hwd_base_universe_d2_050_hwd_basefill_055'] = {'inputs': ['hwd_basefill_055'], 'func': hwd_base_universe_d2_050_hwd_basefill_055}


def hwd_base_universe_d2_051_hwd_basefill_056(hwd_basefill_056):
    return _base_universe_d2(hwd_basefill_056, 51)
HWD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['hwd_base_universe_d2_051_hwd_basefill_056'] = {'inputs': ['hwd_basefill_056'], 'func': hwd_base_universe_d2_051_hwd_basefill_056}


def hwd_base_universe_d2_052_hwd_basefill_057(hwd_basefill_057):
    return _base_universe_d2(hwd_basefill_057, 52)
HWD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['hwd_base_universe_d2_052_hwd_basefill_057'] = {'inputs': ['hwd_basefill_057'], 'func': hwd_base_universe_d2_052_hwd_basefill_057}


def hwd_base_universe_d2_053_hwd_basefill_058(hwd_basefill_058):
    return _base_universe_d2(hwd_basefill_058, 53)
HWD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['hwd_base_universe_d2_053_hwd_basefill_058'] = {'inputs': ['hwd_basefill_058'], 'func': hwd_base_universe_d2_053_hwd_basefill_058}


def hwd_base_universe_d2_054_hwd_basefill_059(hwd_basefill_059):
    return _base_universe_d2(hwd_basefill_059, 54)
HWD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['hwd_base_universe_d2_054_hwd_basefill_059'] = {'inputs': ['hwd_basefill_059'], 'func': hwd_base_universe_d2_054_hwd_basefill_059}


def hwd_base_universe_d2_055_hwd_basefill_060(hwd_basefill_060):
    return _base_universe_d2(hwd_basefill_060, 55)
HWD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['hwd_base_universe_d2_055_hwd_basefill_060'] = {'inputs': ['hwd_basefill_060'], 'func': hwd_base_universe_d2_055_hwd_basefill_060}


def hwd_base_universe_d2_056_hwd_basefill_061(hwd_basefill_061):
    return _base_universe_d2(hwd_basefill_061, 56)
HWD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['hwd_base_universe_d2_056_hwd_basefill_061'] = {'inputs': ['hwd_basefill_061'], 'func': hwd_base_universe_d2_056_hwd_basefill_061}


def hwd_base_universe_d2_057_hwd_basefill_062(hwd_basefill_062):
    return _base_universe_d2(hwd_basefill_062, 57)
HWD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['hwd_base_universe_d2_057_hwd_basefill_062'] = {'inputs': ['hwd_basefill_062'], 'func': hwd_base_universe_d2_057_hwd_basefill_062}


def hwd_base_universe_d2_058_hwd_basefill_063(hwd_basefill_063):
    return _base_universe_d2(hwd_basefill_063, 58)
HWD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['hwd_base_universe_d2_058_hwd_basefill_063'] = {'inputs': ['hwd_basefill_063'], 'func': hwd_base_universe_d2_058_hwd_basefill_063}


def hwd_base_universe_d2_059_hwd_basefill_064(hwd_basefill_064):
    return _base_universe_d2(hwd_basefill_064, 59)
HWD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['hwd_base_universe_d2_059_hwd_basefill_064'] = {'inputs': ['hwd_basefill_064'], 'func': hwd_base_universe_d2_059_hwd_basefill_064}


def hwd_base_universe_d2_060_hwd_basefill_065(hwd_basefill_065):
    return _base_universe_d2(hwd_basefill_065, 60)
HWD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['hwd_base_universe_d2_060_hwd_basefill_065'] = {'inputs': ['hwd_basefill_065'], 'func': hwd_base_universe_d2_060_hwd_basefill_065}


def hwd_base_universe_d2_061_hwd_basefill_066(hwd_basefill_066):
    return _base_universe_d2(hwd_basefill_066, 61)
HWD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['hwd_base_universe_d2_061_hwd_basefill_066'] = {'inputs': ['hwd_basefill_066'], 'func': hwd_base_universe_d2_061_hwd_basefill_066}


def hwd_base_universe_d2_062_hwd_basefill_067(hwd_basefill_067):
    return _base_universe_d2(hwd_basefill_067, 62)
HWD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['hwd_base_universe_d2_062_hwd_basefill_067'] = {'inputs': ['hwd_basefill_067'], 'func': hwd_base_universe_d2_062_hwd_basefill_067}


def hwd_base_universe_d2_063_hwd_basefill_068(hwd_basefill_068):
    return _base_universe_d2(hwd_basefill_068, 63)
HWD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['hwd_base_universe_d2_063_hwd_basefill_068'] = {'inputs': ['hwd_basefill_068'], 'func': hwd_base_universe_d2_063_hwd_basefill_068}


def hwd_base_universe_d2_064_hwd_basefill_069(hwd_basefill_069):
    return _base_universe_d2(hwd_basefill_069, 64)
HWD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['hwd_base_universe_d2_064_hwd_basefill_069'] = {'inputs': ['hwd_basefill_069'], 'func': hwd_base_universe_d2_064_hwd_basefill_069}


def hwd_base_universe_d2_065_hwd_basefill_070(hwd_basefill_070):
    return _base_universe_d2(hwd_basefill_070, 65)
HWD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['hwd_base_universe_d2_065_hwd_basefill_070'] = {'inputs': ['hwd_basefill_070'], 'func': hwd_base_universe_d2_065_hwd_basefill_070}


def hwd_base_universe_d2_066_hwd_basefill_071(hwd_basefill_071):
    return _base_universe_d2(hwd_basefill_071, 66)
HWD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['hwd_base_universe_d2_066_hwd_basefill_071'] = {'inputs': ['hwd_basefill_071'], 'func': hwd_base_universe_d2_066_hwd_basefill_071}


def hwd_base_universe_d2_067_hwd_basefill_072(hwd_basefill_072):
    return _base_universe_d2(hwd_basefill_072, 67)
HWD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['hwd_base_universe_d2_067_hwd_basefill_072'] = {'inputs': ['hwd_basefill_072'], 'func': hwd_base_universe_d2_067_hwd_basefill_072}


def hwd_base_universe_d2_068_hwd_basefill_073(hwd_basefill_073):
    return _base_universe_d2(hwd_basefill_073, 68)
HWD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['hwd_base_universe_d2_068_hwd_basefill_073'] = {'inputs': ['hwd_basefill_073'], 'func': hwd_base_universe_d2_068_hwd_basefill_073}


def hwd_base_universe_d2_069_hwd_basefill_074(hwd_basefill_074):
    return _base_universe_d2(hwd_basefill_074, 69)
HWD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['hwd_base_universe_d2_069_hwd_basefill_074'] = {'inputs': ['hwd_basefill_074'], 'func': hwd_base_universe_d2_069_hwd_basefill_074}


def hwd_base_universe_d2_070_hwd_basefill_075(hwd_basefill_075):
    return _base_universe_d2(hwd_basefill_075, 70)
HWD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['hwd_base_universe_d2_070_hwd_basefill_075'] = {'inputs': ['hwd_basefill_075'], 'func': hwd_base_universe_d2_070_hwd_basefill_075}
