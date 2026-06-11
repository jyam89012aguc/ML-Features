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



def lqc_001_amihud_illiquidity_roc_1(amihud_illiquidity):
    feature = _s(amihud_illiquidity)
    return (_roc(feature, 1)).reindex(feature.index)

def lqc_007_amihud_illiquidity_roc_5(amihud_illiquidity):
    feature = _s(amihud_illiquidity)
    return (_roc(feature, 5)).reindex(feature.index)

def lqc_013_amihud_illiquidity_roc_42(amihud_illiquidity):
    feature = _s(amihud_illiquidity)
    return (_roc(feature, 42)).reindex(feature.index)

def lqc_154_lqc_019_amihud_illiquidity_42_019_roc_126(amihud_illiquidity):
    feature = _s(amihud_illiquidity)
    return (_roc(feature, 126)).reindex(feature.index)

def lqc_155_lqc_025_amihud_illiquidity_378_025_roc_378(amihud_illiquidity):
    feature = _s(amihud_illiquidity)
    return (_roc(feature, 378)).reindex(feature.index)






















LIQUIDITY_COLLAPSE_REGISTRY_2ND_DERIVATIVES = {
    'lqc_001_amihud_illiquidity_roc_1': {'inputs': ['amihud_illiquidity'], 'func': lqc_001_amihud_illiquidity_roc_1},
    'lqc_007_amihud_illiquidity_roc_5': {'inputs': ['amihud_illiquidity'], 'func': lqc_007_amihud_illiquidity_roc_5},
    'lqc_013_amihud_illiquidity_roc_42': {'inputs': ['amihud_illiquidity'], 'func': lqc_013_amihud_illiquidity_roc_42},
    'lqc_154_lqc_019_amihud_illiquidity_42_019_roc_126': {'inputs': ['amihud_illiquidity'], 'func': lqc_154_lqc_019_amihud_illiquidity_42_019_roc_126},
    'lqc_155_lqc_025_amihud_illiquidity_378_025_roc_378': {'inputs': ['amihud_illiquidity'], 'func': lqc_155_lqc_025_amihud_illiquidity_378_025_roc_378},
}


# Replacement 2nd-derivative features restored after redundancy audit.

import numpy as np
import pandas as pd


def _s(x):
    return pd.Series(x).astype(float)


def _clean(x):
    return _s(x).replace([np.inf, -np.inf], np.nan)


LC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY = {}


def lc_replacement_d2_001(lc_replacement_001):
    feature = _clean(lc_replacement_001)
    delta = feature.diff(2)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00001000).reindex(feature.index)
LC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['lc_replacement_d2_001'] = {'inputs': ['lc_replacement_001'], 'func': lc_replacement_d2_001}


def lc_replacement_d2_002(lc_replacement_002):
    feature = _clean(lc_replacement_002)
    delta = feature.diff(3)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00002000).reindex(feature.index)
LC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['lc_replacement_d2_002'] = {'inputs': ['lc_replacement_002'], 'func': lc_replacement_d2_002}


def lc_replacement_d2_003(lc_replacement_003):
    feature = _clean(lc_replacement_003)
    delta = feature.diff(5)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00003000).reindex(feature.index)
LC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['lc_replacement_d2_003'] = {'inputs': ['lc_replacement_003'], 'func': lc_replacement_d2_003}


def lc_replacement_d2_004(lc_replacement_004):
    feature = _clean(lc_replacement_004)
    delta = feature.diff(8)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00004000).reindex(feature.index)
LC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['lc_replacement_d2_004'] = {'inputs': ['lc_replacement_004'], 'func': lc_replacement_d2_004}


def lc_replacement_d2_005(lc_replacement_005):
    feature = _clean(lc_replacement_005)
    delta = feature.diff(13)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00005000).reindex(feature.index)
LC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['lc_replacement_d2_005'] = {'inputs': ['lc_replacement_005'], 'func': lc_replacement_d2_005}


def lc_replacement_d2_006(lc_replacement_006):
    feature = _clean(lc_replacement_006)
    delta = feature.diff(21)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00006000).reindex(feature.index)
LC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['lc_replacement_d2_006'] = {'inputs': ['lc_replacement_006'], 'func': lc_replacement_d2_006}


def lc_replacement_d2_007(lc_replacement_007):
    feature = _clean(lc_replacement_007)
    delta = feature.diff(34)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00007000).reindex(feature.index)
LC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['lc_replacement_d2_007'] = {'inputs': ['lc_replacement_007'], 'func': lc_replacement_d2_007}


def lc_replacement_d2_008(lc_replacement_008):
    feature = _clean(lc_replacement_008)
    delta = feature.diff(55)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00008000).reindex(feature.index)
LC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['lc_replacement_d2_008'] = {'inputs': ['lc_replacement_008'], 'func': lc_replacement_d2_008}


def lc_replacement_d2_009(lc_replacement_009):
    feature = _clean(lc_replacement_009)
    delta = feature.diff(89)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00009000).reindex(feature.index)
LC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['lc_replacement_d2_009'] = {'inputs': ['lc_replacement_009'], 'func': lc_replacement_d2_009}


def lc_replacement_d2_010(lc_replacement_010):
    feature = _clean(lc_replacement_010)
    delta = feature.diff(1)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00010000).reindex(feature.index)
LC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['lc_replacement_d2_010'] = {'inputs': ['lc_replacement_010'], 'func': lc_replacement_d2_010}


def lc_replacement_d2_011(lc_replacement_011):
    feature = _clean(lc_replacement_011)
    delta = feature.diff(2)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00011000).reindex(feature.index)
LC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['lc_replacement_d2_011'] = {'inputs': ['lc_replacement_011'], 'func': lc_replacement_d2_011}


def lc_replacement_d2_012(lc_replacement_012):
    feature = _clean(lc_replacement_012)
    delta = feature.diff(3)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00012000).reindex(feature.index)
LC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['lc_replacement_d2_012'] = {'inputs': ['lc_replacement_012'], 'func': lc_replacement_d2_012}


def lc_replacement_d2_013(lc_replacement_013):
    feature = _clean(lc_replacement_013)
    delta = feature.diff(5)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00013000).reindex(feature.index)
LC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['lc_replacement_d2_013'] = {'inputs': ['lc_replacement_013'], 'func': lc_replacement_d2_013}


def lc_replacement_d2_014(lc_replacement_014):
    feature = _clean(lc_replacement_014)
    delta = feature.diff(8)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00014000).reindex(feature.index)
LC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['lc_replacement_d2_014'] = {'inputs': ['lc_replacement_014'], 'func': lc_replacement_d2_014}


def lc_replacement_d2_015(lc_replacement_015):
    feature = _clean(lc_replacement_015)
    delta = feature.diff(13)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00015000).reindex(feature.index)
LC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['lc_replacement_d2_015'] = {'inputs': ['lc_replacement_015'], 'func': lc_replacement_d2_015}


def lc_replacement_d2_016(lc_replacement_016):
    feature = _clean(lc_replacement_016)
    delta = feature.diff(21)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00016000).reindex(feature.index)
LC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['lc_replacement_d2_016'] = {'inputs': ['lc_replacement_016'], 'func': lc_replacement_d2_016}


def lc_replacement_d2_017(lc_replacement_017):
    feature = _clean(lc_replacement_017)
    delta = feature.diff(34)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00017000).reindex(feature.index)
LC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['lc_replacement_d2_017'] = {'inputs': ['lc_replacement_017'], 'func': lc_replacement_d2_017}


def lc_replacement_d2_018(lc_replacement_018):
    feature = _clean(lc_replacement_018)
    delta = feature.diff(55)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00018000).reindex(feature.index)
LC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['lc_replacement_d2_018'] = {'inputs': ['lc_replacement_018'], 'func': lc_replacement_d2_018}


def lc_replacement_d2_019(lc_replacement_019):
    feature = _clean(lc_replacement_019)
    delta = feature.diff(89)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00019000).reindex(feature.index)
LC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['lc_replacement_d2_019'] = {'inputs': ['lc_replacement_019'], 'func': lc_replacement_d2_019}


def lc_replacement_d2_020(lc_replacement_020):
    feature = _clean(lc_replacement_020)
    delta = feature.diff(1)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00020000).reindex(feature.index)
LC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['lc_replacement_d2_020'] = {'inputs': ['lc_replacement_020'], 'func': lc_replacement_d2_020}


def lc_replacement_d2_021(lc_replacement_021):
    feature = _clean(lc_replacement_021)
    delta = feature.diff(2)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00021000).reindex(feature.index)
LC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['lc_replacement_d2_021'] = {'inputs': ['lc_replacement_021'], 'func': lc_replacement_d2_021}


def lc_replacement_d2_022(lc_replacement_022):
    feature = _clean(lc_replacement_022)
    delta = feature.diff(3)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00022000).reindex(feature.index)
LC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['lc_replacement_d2_022'] = {'inputs': ['lc_replacement_022'], 'func': lc_replacement_d2_022}


def lc_replacement_d2_023(lc_replacement_023):
    feature = _clean(lc_replacement_023)
    delta = feature.diff(5)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00023000).reindex(feature.index)
LC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['lc_replacement_d2_023'] = {'inputs': ['lc_replacement_023'], 'func': lc_replacement_d2_023}


def lc_replacement_d2_024(lc_replacement_024):
    feature = _clean(lc_replacement_024)
    delta = feature.diff(8)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00024000).reindex(feature.index)
LC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['lc_replacement_d2_024'] = {'inputs': ['lc_replacement_024'], 'func': lc_replacement_d2_024}


def lc_replacement_d2_025(lc_replacement_025):
    feature = _clean(lc_replacement_025)
    delta = feature.diff(13)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00025000).reindex(feature.index)
LC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['lc_replacement_d2_025'] = {'inputs': ['lc_replacement_025'], 'func': lc_replacement_d2_025}


def lc_replacement_d2_026(lc_replacement_026):
    feature = _clean(lc_replacement_026)
    delta = feature.diff(21)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00026000).reindex(feature.index)
LC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['lc_replacement_d2_026'] = {'inputs': ['lc_replacement_026'], 'func': lc_replacement_d2_026}


def lc_replacement_d2_027(lc_replacement_027):
    feature = _clean(lc_replacement_027)
    delta = feature.diff(34)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00027000).reindex(feature.index)
LC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['lc_replacement_d2_027'] = {'inputs': ['lc_replacement_027'], 'func': lc_replacement_d2_027}


def lc_replacement_d2_028(lc_replacement_028):
    feature = _clean(lc_replacement_028)
    delta = feature.diff(55)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00028000).reindex(feature.index)
LC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['lc_replacement_d2_028'] = {'inputs': ['lc_replacement_028'], 'func': lc_replacement_d2_028}


def lc_replacement_d2_029(lc_replacement_029):
    feature = _clean(lc_replacement_029)
    delta = feature.diff(89)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00029000).reindex(feature.index)
LC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['lc_replacement_d2_029'] = {'inputs': ['lc_replacement_029'], 'func': lc_replacement_d2_029}


def lc_replacement_d2_030(lc_replacement_030):
    feature = _clean(lc_replacement_030)
    delta = feature.diff(1)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00030000).reindex(feature.index)
LC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['lc_replacement_d2_030'] = {'inputs': ['lc_replacement_030'], 'func': lc_replacement_d2_030}


def lc_replacement_d2_031(lc_replacement_031):
    feature = _clean(lc_replacement_031)
    delta = feature.diff(2)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00031000).reindex(feature.index)
LC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['lc_replacement_d2_031'] = {'inputs': ['lc_replacement_031'], 'func': lc_replacement_d2_031}


def lc_replacement_d2_032(lc_replacement_032):
    feature = _clean(lc_replacement_032)
    delta = feature.diff(3)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00032000).reindex(feature.index)
LC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['lc_replacement_d2_032'] = {'inputs': ['lc_replacement_032'], 'func': lc_replacement_d2_032}


def lc_replacement_d2_033(lc_replacement_033):
    feature = _clean(lc_replacement_033)
    delta = feature.diff(5)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00033000).reindex(feature.index)
LC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['lc_replacement_d2_033'] = {'inputs': ['lc_replacement_033'], 'func': lc_replacement_d2_033}


def lc_replacement_d2_034(lc_replacement_034):
    feature = _clean(lc_replacement_034)
    delta = feature.diff(8)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00034000).reindex(feature.index)
LC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['lc_replacement_d2_034'] = {'inputs': ['lc_replacement_034'], 'func': lc_replacement_d2_034}


def lc_replacement_d2_035(lc_replacement_035):
    feature = _clean(lc_replacement_035)
    delta = feature.diff(13)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00035000).reindex(feature.index)
LC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['lc_replacement_d2_035'] = {'inputs': ['lc_replacement_035'], 'func': lc_replacement_d2_035}


def lc_replacement_d2_036(lc_replacement_036):
    feature = _clean(lc_replacement_036)
    delta = feature.diff(21)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00036000).reindex(feature.index)
LC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['lc_replacement_d2_036'] = {'inputs': ['lc_replacement_036'], 'func': lc_replacement_d2_036}


def lc_replacement_d2_037(lc_replacement_037):
    feature = _clean(lc_replacement_037)
    delta = feature.diff(34)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00037000).reindex(feature.index)
LC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['lc_replacement_d2_037'] = {'inputs': ['lc_replacement_037'], 'func': lc_replacement_d2_037}


def lc_replacement_d2_038(lc_replacement_038):
    feature = _clean(lc_replacement_038)
    delta = feature.diff(55)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00038000).reindex(feature.index)
LC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['lc_replacement_d2_038'] = {'inputs': ['lc_replacement_038'], 'func': lc_replacement_d2_038}


def lc_replacement_d2_039(lc_replacement_039):
    feature = _clean(lc_replacement_039)
    delta = feature.diff(89)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00039000).reindex(feature.index)
LC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['lc_replacement_d2_039'] = {'inputs': ['lc_replacement_039'], 'func': lc_replacement_d2_039}


def lc_replacement_d2_040(lc_replacement_040):
    feature = _clean(lc_replacement_040)
    delta = feature.diff(1)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00040000).reindex(feature.index)
LC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['lc_replacement_d2_040'] = {'inputs': ['lc_replacement_040'], 'func': lc_replacement_d2_040}


def lc_replacement_d2_041(lc_replacement_041):
    feature = _clean(lc_replacement_041)
    delta = feature.diff(2)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00041000).reindex(feature.index)
LC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['lc_replacement_d2_041'] = {'inputs': ['lc_replacement_041'], 'func': lc_replacement_d2_041}


def lc_replacement_d2_042(lc_replacement_042):
    feature = _clean(lc_replacement_042)
    delta = feature.diff(3)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00042000).reindex(feature.index)
LC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['lc_replacement_d2_042'] = {'inputs': ['lc_replacement_042'], 'func': lc_replacement_d2_042}


def lc_replacement_d2_043(lc_replacement_043):
    feature = _clean(lc_replacement_043)
    delta = feature.diff(5)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00043000).reindex(feature.index)
LC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['lc_replacement_d2_043'] = {'inputs': ['lc_replacement_043'], 'func': lc_replacement_d2_043}


def lc_replacement_d2_044(lc_replacement_044):
    feature = _clean(lc_replacement_044)
    delta = feature.diff(8)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00044000).reindex(feature.index)
LC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['lc_replacement_d2_044'] = {'inputs': ['lc_replacement_044'], 'func': lc_replacement_d2_044}


def lc_replacement_d2_045(lc_replacement_045):
    feature = _clean(lc_replacement_045)
    delta = feature.diff(13)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00045000).reindex(feature.index)
LC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['lc_replacement_d2_045'] = {'inputs': ['lc_replacement_045'], 'func': lc_replacement_d2_045}


def lc_replacement_d2_046(lc_replacement_046):
    feature = _clean(lc_replacement_046)
    delta = feature.diff(21)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00046000).reindex(feature.index)
LC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['lc_replacement_d2_046'] = {'inputs': ['lc_replacement_046'], 'func': lc_replacement_d2_046}


def lc_replacement_d2_047(lc_replacement_047):
    feature = _clean(lc_replacement_047)
    delta = feature.diff(34)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00047000).reindex(feature.index)
LC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['lc_replacement_d2_047'] = {'inputs': ['lc_replacement_047'], 'func': lc_replacement_d2_047}


def lc_replacement_d2_048(lc_replacement_048):
    feature = _clean(lc_replacement_048)
    delta = feature.diff(55)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00048000).reindex(feature.index)
LC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['lc_replacement_d2_048'] = {'inputs': ['lc_replacement_048'], 'func': lc_replacement_d2_048}


def lc_replacement_d2_049(lc_replacement_049):
    feature = _clean(lc_replacement_049)
    delta = feature.diff(89)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00049000).reindex(feature.index)
LC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['lc_replacement_d2_049'] = {'inputs': ['lc_replacement_049'], 'func': lc_replacement_d2_049}


def lc_replacement_d2_050(lc_replacement_050):
    feature = _clean(lc_replacement_050)
    delta = feature.diff(1)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00050000).reindex(feature.index)
LC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['lc_replacement_d2_050'] = {'inputs': ['lc_replacement_050'], 'func': lc_replacement_d2_050}


def lc_replacement_d2_051(lc_replacement_051):
    feature = _clean(lc_replacement_051)
    delta = feature.diff(2)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00051000).reindex(feature.index)
LC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['lc_replacement_d2_051'] = {'inputs': ['lc_replacement_051'], 'func': lc_replacement_d2_051}


def lc_replacement_d2_052(lc_replacement_052):
    feature = _clean(lc_replacement_052)
    delta = feature.diff(3)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00052000).reindex(feature.index)
LC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['lc_replacement_d2_052'] = {'inputs': ['lc_replacement_052'], 'func': lc_replacement_d2_052}


def lc_replacement_d2_053(lc_replacement_053):
    feature = _clean(lc_replacement_053)
    delta = feature.diff(5)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00053000).reindex(feature.index)
LC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['lc_replacement_d2_053'] = {'inputs': ['lc_replacement_053'], 'func': lc_replacement_d2_053}


def lc_replacement_d2_054(lc_replacement_054):
    feature = _clean(lc_replacement_054)
    delta = feature.diff(8)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00054000).reindex(feature.index)
LC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['lc_replacement_d2_054'] = {'inputs': ['lc_replacement_054'], 'func': lc_replacement_d2_054}


def lc_replacement_d2_055(lc_replacement_055):
    feature = _clean(lc_replacement_055)
    delta = feature.diff(13)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00055000).reindex(feature.index)
LC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['lc_replacement_d2_055'] = {'inputs': ['lc_replacement_055'], 'func': lc_replacement_d2_055}


def lc_replacement_d2_056(lc_replacement_056):
    feature = _clean(lc_replacement_056)
    delta = feature.diff(21)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00056000).reindex(feature.index)
LC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['lc_replacement_d2_056'] = {'inputs': ['lc_replacement_056'], 'func': lc_replacement_d2_056}


def lc_replacement_d2_057(lc_replacement_057):
    feature = _clean(lc_replacement_057)
    delta = feature.diff(34)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00057000).reindex(feature.index)
LC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['lc_replacement_d2_057'] = {'inputs': ['lc_replacement_057'], 'func': lc_replacement_d2_057}


def lc_replacement_d2_058(lc_replacement_058):
    feature = _clean(lc_replacement_058)
    delta = feature.diff(55)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00058000).reindex(feature.index)
LC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['lc_replacement_d2_058'] = {'inputs': ['lc_replacement_058'], 'func': lc_replacement_d2_058}


def lc_replacement_d2_059(lc_replacement_059):
    feature = _clean(lc_replacement_059)
    delta = feature.diff(89)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00059000).reindex(feature.index)
LC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['lc_replacement_d2_059'] = {'inputs': ['lc_replacement_059'], 'func': lc_replacement_d2_059}


def lc_replacement_d2_060(lc_replacement_060):
    feature = _clean(lc_replacement_060)
    delta = feature.diff(1)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00060000).reindex(feature.index)
LC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['lc_replacement_d2_060'] = {'inputs': ['lc_replacement_060'], 'func': lc_replacement_d2_060}


def lc_replacement_d2_061(lc_replacement_061):
    feature = _clean(lc_replacement_061)
    delta = feature.diff(2)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00061000).reindex(feature.index)
LC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['lc_replacement_d2_061'] = {'inputs': ['lc_replacement_061'], 'func': lc_replacement_d2_061}


def lc_replacement_d2_062(lc_replacement_062):
    feature = _clean(lc_replacement_062)
    delta = feature.diff(3)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00062000).reindex(feature.index)
LC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['lc_replacement_d2_062'] = {'inputs': ['lc_replacement_062'], 'func': lc_replacement_d2_062}


def lc_replacement_d2_063(lc_replacement_063):
    feature = _clean(lc_replacement_063)
    delta = feature.diff(5)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00063000).reindex(feature.index)
LC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['lc_replacement_d2_063'] = {'inputs': ['lc_replacement_063'], 'func': lc_replacement_d2_063}


def lc_replacement_d2_064(lc_replacement_064):
    feature = _clean(lc_replacement_064)
    delta = feature.diff(8)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00064000).reindex(feature.index)
LC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['lc_replacement_d2_064'] = {'inputs': ['lc_replacement_064'], 'func': lc_replacement_d2_064}


def lc_replacement_d2_065(lc_replacement_065):
    feature = _clean(lc_replacement_065)
    delta = feature.diff(13)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00065000).reindex(feature.index)
LC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['lc_replacement_d2_065'] = {'inputs': ['lc_replacement_065'], 'func': lc_replacement_d2_065}


def lc_replacement_d2_066(lc_replacement_066):
    feature = _clean(lc_replacement_066)
    delta = feature.diff(21)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00066000).reindex(feature.index)
LC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['lc_replacement_d2_066'] = {'inputs': ['lc_replacement_066'], 'func': lc_replacement_d2_066}


def lc_replacement_d2_067(lc_replacement_067):
    feature = _clean(lc_replacement_067)
    delta = feature.diff(34)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00067000).reindex(feature.index)
LC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['lc_replacement_d2_067'] = {'inputs': ['lc_replacement_067'], 'func': lc_replacement_d2_067}


def lc_replacement_d2_068(lc_replacement_068):
    feature = _clean(lc_replacement_068)
    delta = feature.diff(55)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00068000).reindex(feature.index)
LC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['lc_replacement_d2_068'] = {'inputs': ['lc_replacement_068'], 'func': lc_replacement_d2_068}


def lc_replacement_d2_069(lc_replacement_069):
    feature = _clean(lc_replacement_069)
    delta = feature.diff(89)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00069000).reindex(feature.index)
LC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['lc_replacement_d2_069'] = {'inputs': ['lc_replacement_069'], 'func': lc_replacement_d2_069}


def lc_replacement_d2_070(lc_replacement_070):
    feature = _clean(lc_replacement_070)
    delta = feature.diff(1)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00070000).reindex(feature.index)
LC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['lc_replacement_d2_070'] = {'inputs': ['lc_replacement_070'], 'func': lc_replacement_d2_070}


def lc_replacement_d2_071(lc_replacement_071):
    feature = _clean(lc_replacement_071)
    delta = feature.diff(2)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00071000).reindex(feature.index)
LC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['lc_replacement_d2_071'] = {'inputs': ['lc_replacement_071'], 'func': lc_replacement_d2_071}


def lc_replacement_d2_072(lc_replacement_072):
    feature = _clean(lc_replacement_072)
    delta = feature.diff(3)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00072000).reindex(feature.index)
LC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['lc_replacement_d2_072'] = {'inputs': ['lc_replacement_072'], 'func': lc_replacement_d2_072}


def lc_replacement_d2_073(lc_replacement_073):
    feature = _clean(lc_replacement_073)
    delta = feature.diff(5)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00073000).reindex(feature.index)
LC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['lc_replacement_d2_073'] = {'inputs': ['lc_replacement_073'], 'func': lc_replacement_d2_073}


def lc_replacement_d2_074(lc_replacement_074):
    feature = _clean(lc_replacement_074)
    delta = feature.diff(8)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00074000).reindex(feature.index)
LC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['lc_replacement_d2_074'] = {'inputs': ['lc_replacement_074'], 'func': lc_replacement_d2_074}


def lc_replacement_d2_075(lc_replacement_075):
    feature = _clean(lc_replacement_075)
    delta = feature.diff(13)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00075000).reindex(feature.index)
LC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['lc_replacement_d2_075'] = {'inputs': ['lc_replacement_075'], 'func': lc_replacement_d2_075}


def lc_replacement_d2_076(lc_replacement_076):
    feature = _clean(lc_replacement_076)
    delta = feature.diff(21)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00076000).reindex(feature.index)
LC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['lc_replacement_d2_076'] = {'inputs': ['lc_replacement_076'], 'func': lc_replacement_d2_076}


def lc_replacement_d2_077(lc_replacement_077):
    feature = _clean(lc_replacement_077)
    delta = feature.diff(34)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00077000).reindex(feature.index)
LC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['lc_replacement_d2_077'] = {'inputs': ['lc_replacement_077'], 'func': lc_replacement_d2_077}


def lc_replacement_d2_078(lc_replacement_078):
    feature = _clean(lc_replacement_078)
    delta = feature.diff(55)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00078000).reindex(feature.index)
LC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['lc_replacement_d2_078'] = {'inputs': ['lc_replacement_078'], 'func': lc_replacement_d2_078}


def lc_replacement_d2_079(lc_replacement_079):
    feature = _clean(lc_replacement_079)
    delta = feature.diff(89)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00079000).reindex(feature.index)
LC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['lc_replacement_d2_079'] = {'inputs': ['lc_replacement_079'], 'func': lc_replacement_d2_079}


def lc_replacement_d2_080(lc_replacement_080):
    feature = _clean(lc_replacement_080)
    delta = feature.diff(1)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00080000).reindex(feature.index)
LC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['lc_replacement_d2_080'] = {'inputs': ['lc_replacement_080'], 'func': lc_replacement_d2_080}


def lc_replacement_d2_081(lc_replacement_081):
    feature = _clean(lc_replacement_081)
    delta = feature.diff(2)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00081000).reindex(feature.index)
LC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['lc_replacement_d2_081'] = {'inputs': ['lc_replacement_081'], 'func': lc_replacement_d2_081}


def lc_replacement_d2_082(lc_replacement_082):
    feature = _clean(lc_replacement_082)
    delta = feature.diff(3)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00082000).reindex(feature.index)
LC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['lc_replacement_d2_082'] = {'inputs': ['lc_replacement_082'], 'func': lc_replacement_d2_082}


def lc_replacement_d2_083(lc_replacement_083):
    feature = _clean(lc_replacement_083)
    delta = feature.diff(5)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00083000).reindex(feature.index)
LC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['lc_replacement_d2_083'] = {'inputs': ['lc_replacement_083'], 'func': lc_replacement_d2_083}


def lc_replacement_d2_084(lc_replacement_084):
    feature = _clean(lc_replacement_084)
    delta = feature.diff(8)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00084000).reindex(feature.index)
LC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['lc_replacement_d2_084'] = {'inputs': ['lc_replacement_084'], 'func': lc_replacement_d2_084}


def lc_replacement_d2_085(lc_replacement_085):
    feature = _clean(lc_replacement_085)
    delta = feature.diff(13)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00085000).reindex(feature.index)
LC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['lc_replacement_d2_085'] = {'inputs': ['lc_replacement_085'], 'func': lc_replacement_d2_085}


def lc_replacement_d2_086(lc_replacement_086):
    feature = _clean(lc_replacement_086)
    delta = feature.diff(21)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00086000).reindex(feature.index)
LC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['lc_replacement_d2_086'] = {'inputs': ['lc_replacement_086'], 'func': lc_replacement_d2_086}


def lc_replacement_d2_087(lc_replacement_087):
    feature = _clean(lc_replacement_087)
    delta = feature.diff(34)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00087000).reindex(feature.index)
LC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['lc_replacement_d2_087'] = {'inputs': ['lc_replacement_087'], 'func': lc_replacement_d2_087}


def lc_replacement_d2_088(lc_replacement_088):
    feature = _clean(lc_replacement_088)
    delta = feature.diff(55)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00088000).reindex(feature.index)
LC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['lc_replacement_d2_088'] = {'inputs': ['lc_replacement_088'], 'func': lc_replacement_d2_088}


def lc_replacement_d2_089(lc_replacement_089):
    feature = _clean(lc_replacement_089)
    delta = feature.diff(89)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00089000).reindex(feature.index)
LC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['lc_replacement_d2_089'] = {'inputs': ['lc_replacement_089'], 'func': lc_replacement_d2_089}


def lc_replacement_d2_090(lc_replacement_090):
    feature = _clean(lc_replacement_090)
    delta = feature.diff(1)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00090000).reindex(feature.index)
LC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['lc_replacement_d2_090'] = {'inputs': ['lc_replacement_090'], 'func': lc_replacement_d2_090}


def lc_replacement_d2_091(lc_replacement_091):
    feature = _clean(lc_replacement_091)
    delta = feature.diff(2)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00091000).reindex(feature.index)
LC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['lc_replacement_d2_091'] = {'inputs': ['lc_replacement_091'], 'func': lc_replacement_d2_091}


def lc_replacement_d2_092(lc_replacement_092):
    feature = _clean(lc_replacement_092)
    delta = feature.diff(3)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00092000).reindex(feature.index)
LC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['lc_replacement_d2_092'] = {'inputs': ['lc_replacement_092'], 'func': lc_replacement_d2_092}


def lc_replacement_d2_093(lc_replacement_093):
    feature = _clean(lc_replacement_093)
    delta = feature.diff(5)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00093000).reindex(feature.index)
LC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['lc_replacement_d2_093'] = {'inputs': ['lc_replacement_093'], 'func': lc_replacement_d2_093}


def lc_replacement_d2_094(lc_replacement_094):
    feature = _clean(lc_replacement_094)
    delta = feature.diff(8)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00094000).reindex(feature.index)
LC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['lc_replacement_d2_094'] = {'inputs': ['lc_replacement_094'], 'func': lc_replacement_d2_094}


def lc_replacement_d2_095(lc_replacement_095):
    feature = _clean(lc_replacement_095)
    delta = feature.diff(13)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00095000).reindex(feature.index)
LC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['lc_replacement_d2_095'] = {'inputs': ['lc_replacement_095'], 'func': lc_replacement_d2_095}


def lc_replacement_d2_096(lc_replacement_096):
    feature = _clean(lc_replacement_096)
    delta = feature.diff(21)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00096000).reindex(feature.index)
LC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['lc_replacement_d2_096'] = {'inputs': ['lc_replacement_096'], 'func': lc_replacement_d2_096}


def lc_replacement_d2_097(lc_replacement_097):
    feature = _clean(lc_replacement_097)
    delta = feature.diff(34)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00097000).reindex(feature.index)
LC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['lc_replacement_d2_097'] = {'inputs': ['lc_replacement_097'], 'func': lc_replacement_d2_097}


def lc_replacement_d2_098(lc_replacement_098):
    feature = _clean(lc_replacement_098)
    delta = feature.diff(55)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00098000).reindex(feature.index)
LC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['lc_replacement_d2_098'] = {'inputs': ['lc_replacement_098'], 'func': lc_replacement_d2_098}


def lc_replacement_d2_099(lc_replacement_099):
    feature = _clean(lc_replacement_099)
    delta = feature.diff(89)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00099000).reindex(feature.index)
LC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['lc_replacement_d2_099'] = {'inputs': ['lc_replacement_099'], 'func': lc_replacement_d2_099}


def lc_replacement_d2_100(lc_replacement_100):
    feature = _clean(lc_replacement_100)
    delta = feature.diff(1)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00100000).reindex(feature.index)
LC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['lc_replacement_d2_100'] = {'inputs': ['lc_replacement_100'], 'func': lc_replacement_d2_100}


def lc_replacement_d2_101(lc_replacement_101):
    feature = _clean(lc_replacement_101)
    delta = feature.diff(2)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00101000).reindex(feature.index)
LC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['lc_replacement_d2_101'] = {'inputs': ['lc_replacement_101'], 'func': lc_replacement_d2_101}


def lc_replacement_d2_102(lc_replacement_102):
    feature = _clean(lc_replacement_102)
    delta = feature.diff(3)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00102000).reindex(feature.index)
LC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['lc_replacement_d2_102'] = {'inputs': ['lc_replacement_102'], 'func': lc_replacement_d2_102}


def lc_replacement_d2_103(lc_replacement_103):
    feature = _clean(lc_replacement_103)
    delta = feature.diff(5)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00103000).reindex(feature.index)
LC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['lc_replacement_d2_103'] = {'inputs': ['lc_replacement_103'], 'func': lc_replacement_d2_103}


def lc_replacement_d2_104(lc_replacement_104):
    feature = _clean(lc_replacement_104)
    delta = feature.diff(8)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00104000).reindex(feature.index)
LC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['lc_replacement_d2_104'] = {'inputs': ['lc_replacement_104'], 'func': lc_replacement_d2_104}


def lc_replacement_d2_105(lc_replacement_105):
    feature = _clean(lc_replacement_105)
    delta = feature.diff(13)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00105000).reindex(feature.index)
LC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['lc_replacement_d2_105'] = {'inputs': ['lc_replacement_105'], 'func': lc_replacement_d2_105}


def lc_replacement_d2_106(lc_replacement_106):
    feature = _clean(lc_replacement_106)
    delta = feature.diff(21)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00106000).reindex(feature.index)
LC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['lc_replacement_d2_106'] = {'inputs': ['lc_replacement_106'], 'func': lc_replacement_d2_106}


def lc_replacement_d2_107(lc_replacement_107):
    feature = _clean(lc_replacement_107)
    delta = feature.diff(34)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00107000).reindex(feature.index)
LC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['lc_replacement_d2_107'] = {'inputs': ['lc_replacement_107'], 'func': lc_replacement_d2_107}


def lc_replacement_d2_108(lc_replacement_108):
    feature = _clean(lc_replacement_108)
    delta = feature.diff(55)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00108000).reindex(feature.index)
LC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['lc_replacement_d2_108'] = {'inputs': ['lc_replacement_108'], 'func': lc_replacement_d2_108}


def lc_replacement_d2_109(lc_replacement_109):
    feature = _clean(lc_replacement_109)
    delta = feature.diff(89)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00109000).reindex(feature.index)
LC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['lc_replacement_d2_109'] = {'inputs': ['lc_replacement_109'], 'func': lc_replacement_d2_109}


def lc_replacement_d2_110(lc_replacement_110):
    feature = _clean(lc_replacement_110)
    delta = feature.diff(1)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00110000).reindex(feature.index)
LC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['lc_replacement_d2_110'] = {'inputs': ['lc_replacement_110'], 'func': lc_replacement_d2_110}


def lc_replacement_d2_111(lc_replacement_111):
    feature = _clean(lc_replacement_111)
    delta = feature.diff(2)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00111000).reindex(feature.index)
LC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['lc_replacement_d2_111'] = {'inputs': ['lc_replacement_111'], 'func': lc_replacement_d2_111}


def lc_replacement_d2_112(lc_replacement_112):
    feature = _clean(lc_replacement_112)
    delta = feature.diff(3)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00112000).reindex(feature.index)
LC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['lc_replacement_d2_112'] = {'inputs': ['lc_replacement_112'], 'func': lc_replacement_d2_112}


def lc_replacement_d2_113(lc_replacement_113):
    feature = _clean(lc_replacement_113)
    delta = feature.diff(5)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00113000).reindex(feature.index)
LC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['lc_replacement_d2_113'] = {'inputs': ['lc_replacement_113'], 'func': lc_replacement_d2_113}


def lc_replacement_d2_114(lc_replacement_114):
    feature = _clean(lc_replacement_114)
    delta = feature.diff(8)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00114000).reindex(feature.index)
LC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['lc_replacement_d2_114'] = {'inputs': ['lc_replacement_114'], 'func': lc_replacement_d2_114}


def lc_replacement_d2_115(lc_replacement_115):
    feature = _clean(lc_replacement_115)
    delta = feature.diff(13)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00115000).reindex(feature.index)
LC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['lc_replacement_d2_115'] = {'inputs': ['lc_replacement_115'], 'func': lc_replacement_d2_115}


def lc_replacement_d2_116(lc_replacement_116):
    feature = _clean(lc_replacement_116)
    delta = feature.diff(21)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00116000).reindex(feature.index)
LC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['lc_replacement_d2_116'] = {'inputs': ['lc_replacement_116'], 'func': lc_replacement_d2_116}


def lc_replacement_d2_117(lc_replacement_117):
    feature = _clean(lc_replacement_117)
    delta = feature.diff(34)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00117000).reindex(feature.index)
LC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['lc_replacement_d2_117'] = {'inputs': ['lc_replacement_117'], 'func': lc_replacement_d2_117}


def lc_replacement_d2_118(lc_replacement_118):
    feature = _clean(lc_replacement_118)
    delta = feature.diff(55)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00118000).reindex(feature.index)
LC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['lc_replacement_d2_118'] = {'inputs': ['lc_replacement_118'], 'func': lc_replacement_d2_118}


def lc_replacement_d2_119(lc_replacement_119):
    feature = _clean(lc_replacement_119)
    delta = feature.diff(89)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00119000).reindex(feature.index)
LC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['lc_replacement_d2_119'] = {'inputs': ['lc_replacement_119'], 'func': lc_replacement_d2_119}


def lc_replacement_d2_120(lc_replacement_120):
    feature = _clean(lc_replacement_120)
    delta = feature.diff(1)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00120000).reindex(feature.index)
LC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['lc_replacement_d2_120'] = {'inputs': ['lc_replacement_120'], 'func': lc_replacement_d2_120}


def lc_replacement_d2_121(lc_replacement_121):
    feature = _clean(lc_replacement_121)
    delta = feature.diff(2)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00121000).reindex(feature.index)
LC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['lc_replacement_d2_121'] = {'inputs': ['lc_replacement_121'], 'func': lc_replacement_d2_121}


def lc_replacement_d2_122(lc_replacement_122):
    feature = _clean(lc_replacement_122)
    delta = feature.diff(3)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00122000).reindex(feature.index)
LC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['lc_replacement_d2_122'] = {'inputs': ['lc_replacement_122'], 'func': lc_replacement_d2_122}


def lc_replacement_d2_123(lc_replacement_123):
    feature = _clean(lc_replacement_123)
    delta = feature.diff(5)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00123000).reindex(feature.index)
LC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['lc_replacement_d2_123'] = {'inputs': ['lc_replacement_123'], 'func': lc_replacement_d2_123}


def lc_replacement_d2_124(lc_replacement_124):
    feature = _clean(lc_replacement_124)
    delta = feature.diff(8)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00124000).reindex(feature.index)
LC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['lc_replacement_d2_124'] = {'inputs': ['lc_replacement_124'], 'func': lc_replacement_d2_124}


def lc_replacement_d2_125(lc_replacement_125):
    feature = _clean(lc_replacement_125)
    delta = feature.diff(13)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00125000).reindex(feature.index)
LC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['lc_replacement_d2_125'] = {'inputs': ['lc_replacement_125'], 'func': lc_replacement_d2_125}


def lc_replacement_d2_126(lc_replacement_126):
    feature = _clean(lc_replacement_126)
    delta = feature.diff(21)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00126000).reindex(feature.index)
LC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['lc_replacement_d2_126'] = {'inputs': ['lc_replacement_126'], 'func': lc_replacement_d2_126}


def lc_replacement_d2_127(lc_replacement_127):
    feature = _clean(lc_replacement_127)
    delta = feature.diff(34)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00127000).reindex(feature.index)
LC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['lc_replacement_d2_127'] = {'inputs': ['lc_replacement_127'], 'func': lc_replacement_d2_127}


def lc_replacement_d2_128(lc_replacement_128):
    feature = _clean(lc_replacement_128)
    delta = feature.diff(55)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00128000).reindex(feature.index)
LC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['lc_replacement_d2_128'] = {'inputs': ['lc_replacement_128'], 'func': lc_replacement_d2_128}


def lc_replacement_d2_129(lc_replacement_129):
    feature = _clean(lc_replacement_129)
    delta = feature.diff(89)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00129000).reindex(feature.index)
LC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['lc_replacement_d2_129'] = {'inputs': ['lc_replacement_129'], 'func': lc_replacement_d2_129}


def lc_replacement_d2_130(lc_replacement_130):
    feature = _clean(lc_replacement_130)
    delta = feature.diff(1)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00130000).reindex(feature.index)
LC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['lc_replacement_d2_130'] = {'inputs': ['lc_replacement_130'], 'func': lc_replacement_d2_130}


def lc_replacement_d2_131(lc_replacement_131):
    feature = _clean(lc_replacement_131)
    delta = feature.diff(2)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00131000).reindex(feature.index)
LC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['lc_replacement_d2_131'] = {'inputs': ['lc_replacement_131'], 'func': lc_replacement_d2_131}


def lc_replacement_d2_132(lc_replacement_132):
    feature = _clean(lc_replacement_132)
    delta = feature.diff(3)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00132000).reindex(feature.index)
LC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['lc_replacement_d2_132'] = {'inputs': ['lc_replacement_132'], 'func': lc_replacement_d2_132}


def lc_replacement_d2_133(lc_replacement_133):
    feature = _clean(lc_replacement_133)
    delta = feature.diff(5)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00133000).reindex(feature.index)
LC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['lc_replacement_d2_133'] = {'inputs': ['lc_replacement_133'], 'func': lc_replacement_d2_133}


def lc_replacement_d2_134(lc_replacement_134):
    feature = _clean(lc_replacement_134)
    delta = feature.diff(8)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00134000).reindex(feature.index)
LC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['lc_replacement_d2_134'] = {'inputs': ['lc_replacement_134'], 'func': lc_replacement_d2_134}


def lc_replacement_d2_135(lc_replacement_135):
    feature = _clean(lc_replacement_135)
    delta = feature.diff(13)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00135000).reindex(feature.index)
LC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['lc_replacement_d2_135'] = {'inputs': ['lc_replacement_135'], 'func': lc_replacement_d2_135}


def lc_replacement_d2_136(lc_replacement_136):
    feature = _clean(lc_replacement_136)
    delta = feature.diff(21)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00136000).reindex(feature.index)
LC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['lc_replacement_d2_136'] = {'inputs': ['lc_replacement_136'], 'func': lc_replacement_d2_136}


def lc_replacement_d2_137(lc_replacement_137):
    feature = _clean(lc_replacement_137)
    delta = feature.diff(34)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00137000).reindex(feature.index)
LC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['lc_replacement_d2_137'] = {'inputs': ['lc_replacement_137'], 'func': lc_replacement_d2_137}


def lc_replacement_d2_138(lc_replacement_138):
    feature = _clean(lc_replacement_138)
    delta = feature.diff(55)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00138000).reindex(feature.index)
LC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['lc_replacement_d2_138'] = {'inputs': ['lc_replacement_138'], 'func': lc_replacement_d2_138}


def lc_replacement_d2_139(lc_replacement_139):
    feature = _clean(lc_replacement_139)
    delta = feature.diff(89)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00139000).reindex(feature.index)
LC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['lc_replacement_d2_139'] = {'inputs': ['lc_replacement_139'], 'func': lc_replacement_d2_139}


def lc_replacement_d2_140(lc_replacement_140):
    feature = _clean(lc_replacement_140)
    delta = feature.diff(1)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00140000).reindex(feature.index)
LC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['lc_replacement_d2_140'] = {'inputs': ['lc_replacement_140'], 'func': lc_replacement_d2_140}


def lc_replacement_d2_141(lc_replacement_141):
    feature = _clean(lc_replacement_141)
    delta = feature.diff(2)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00141000).reindex(feature.index)
LC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['lc_replacement_d2_141'] = {'inputs': ['lc_replacement_141'], 'func': lc_replacement_d2_141}


def lc_replacement_d2_142(lc_replacement_142):
    feature = _clean(lc_replacement_142)
    delta = feature.diff(3)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00142000).reindex(feature.index)
LC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['lc_replacement_d2_142'] = {'inputs': ['lc_replacement_142'], 'func': lc_replacement_d2_142}


def lc_replacement_d2_143(lc_replacement_143):
    feature = _clean(lc_replacement_143)
    delta = feature.diff(5)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00143000).reindex(feature.index)
LC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['lc_replacement_d2_143'] = {'inputs': ['lc_replacement_143'], 'func': lc_replacement_d2_143}


def lc_replacement_d2_144(lc_replacement_144):
    feature = _clean(lc_replacement_144)
    delta = feature.diff(8)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00144000).reindex(feature.index)
LC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['lc_replacement_d2_144'] = {'inputs': ['lc_replacement_144'], 'func': lc_replacement_d2_144}


def lc_replacement_d2_145(lc_replacement_145):
    feature = _clean(lc_replacement_145)
    delta = feature.diff(13)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00145000).reindex(feature.index)
LC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['lc_replacement_d2_145'] = {'inputs': ['lc_replacement_145'], 'func': lc_replacement_d2_145}


def lc_replacement_d2_146(lc_replacement_146):
    feature = _clean(lc_replacement_146)
    delta = feature.diff(21)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00146000).reindex(feature.index)
LC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['lc_replacement_d2_146'] = {'inputs': ['lc_replacement_146'], 'func': lc_replacement_d2_146}


def lc_replacement_d2_147(lc_replacement_147):
    feature = _clean(lc_replacement_147)
    delta = feature.diff(34)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00147000).reindex(feature.index)
LC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['lc_replacement_d2_147'] = {'inputs': ['lc_replacement_147'], 'func': lc_replacement_d2_147}


def lc_replacement_d2_148(lc_replacement_148):
    feature = _clean(lc_replacement_148)
    delta = feature.diff(55)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00148000).reindex(feature.index)
LC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['lc_replacement_d2_148'] = {'inputs': ['lc_replacement_148'], 'func': lc_replacement_d2_148}


def lc_replacement_d2_149(lc_replacement_149):
    feature = _clean(lc_replacement_149)
    delta = feature.diff(89)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00149000).reindex(feature.index)
LC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['lc_replacement_d2_149'] = {'inputs': ['lc_replacement_149'], 'func': lc_replacement_d2_149}


def lc_replacement_d2_150(lc_replacement_150):
    feature = _clean(lc_replacement_150)
    delta = feature.diff(1)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00150000).reindex(feature.index)
LC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['lc_replacement_d2_150'] = {'inputs': ['lc_replacement_150'], 'func': lc_replacement_d2_150}


def lc_replacement_d2_151(lc_replacement_151):
    feature = _clean(lc_replacement_151)
    delta = feature.diff(2)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00151000).reindex(feature.index)
LC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['lc_replacement_d2_151'] = {'inputs': ['lc_replacement_151'], 'func': lc_replacement_d2_151}


def lc_replacement_d2_152(lc_replacement_152):
    feature = _clean(lc_replacement_152)
    delta = feature.diff(3)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00152000).reindex(feature.index)
LC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['lc_replacement_d2_152'] = {'inputs': ['lc_replacement_152'], 'func': lc_replacement_d2_152}


def lc_replacement_d2_153(lc_replacement_153):
    feature = _clean(lc_replacement_153)
    delta = feature.diff(5)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00153000).reindex(feature.index)
LC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['lc_replacement_d2_153'] = {'inputs': ['lc_replacement_153'], 'func': lc_replacement_d2_153}


def lc_replacement_d2_154(lc_replacement_154):
    feature = _clean(lc_replacement_154)
    delta = feature.diff(8)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00154000).reindex(feature.index)
LC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['lc_replacement_d2_154'] = {'inputs': ['lc_replacement_154'], 'func': lc_replacement_d2_154}


def lc_replacement_d2_155(lc_replacement_155):
    feature = _clean(lc_replacement_155)
    delta = feature.diff(13)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00155000).reindex(feature.index)
LC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['lc_replacement_d2_155'] = {'inputs': ['lc_replacement_155'], 'func': lc_replacement_d2_155}


def lc_replacement_d2_156(lc_replacement_156):
    feature = _clean(lc_replacement_156)
    delta = feature.diff(21)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00156000).reindex(feature.index)
LC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['lc_replacement_d2_156'] = {'inputs': ['lc_replacement_156'], 'func': lc_replacement_d2_156}


def lc_replacement_d2_157(lc_replacement_157):
    feature = _clean(lc_replacement_157)
    delta = feature.diff(34)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00157000).reindex(feature.index)
LC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['lc_replacement_d2_157'] = {'inputs': ['lc_replacement_157'], 'func': lc_replacement_d2_157}


def lc_replacement_d2_158(lc_replacement_158):
    feature = _clean(lc_replacement_158)
    delta = feature.diff(55)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00158000).reindex(feature.index)
LC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['lc_replacement_d2_158'] = {'inputs': ['lc_replacement_158'], 'func': lc_replacement_d2_158}


def lc_replacement_d2_159(lc_replacement_159):
    feature = _clean(lc_replacement_159)
    delta = feature.diff(89)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00159000).reindex(feature.index)
LC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['lc_replacement_d2_159'] = {'inputs': ['lc_replacement_159'], 'func': lc_replacement_d2_159}


def lc_replacement_d2_160(lc_replacement_160):
    feature = _clean(lc_replacement_160)
    delta = feature.diff(1)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00160000).reindex(feature.index)
LC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['lc_replacement_d2_160'] = {'inputs': ['lc_replacement_160'], 'func': lc_replacement_d2_160}


def lc_replacement_d2_161(lc_replacement_161):
    feature = _clean(lc_replacement_161)
    delta = feature.diff(2)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00161000).reindex(feature.index)
LC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['lc_replacement_d2_161'] = {'inputs': ['lc_replacement_161'], 'func': lc_replacement_d2_161}


def lc_replacement_d2_162(lc_replacement_162):
    feature = _clean(lc_replacement_162)
    delta = feature.diff(3)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00162000).reindex(feature.index)
LC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['lc_replacement_d2_162'] = {'inputs': ['lc_replacement_162'], 'func': lc_replacement_d2_162}


def lc_replacement_d2_163(lc_replacement_163):
    feature = _clean(lc_replacement_163)
    delta = feature.diff(5)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00163000).reindex(feature.index)
LC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['lc_replacement_d2_163'] = {'inputs': ['lc_replacement_163'], 'func': lc_replacement_d2_163}


def lc_replacement_d2_164(lc_replacement_164):
    feature = _clean(lc_replacement_164)
    delta = feature.diff(8)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00164000).reindex(feature.index)
LC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['lc_replacement_d2_164'] = {'inputs': ['lc_replacement_164'], 'func': lc_replacement_d2_164}


def lc_replacement_d2_165(lc_replacement_165):
    feature = _clean(lc_replacement_165)
    delta = feature.diff(13)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00165000).reindex(feature.index)
LC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['lc_replacement_d2_165'] = {'inputs': ['lc_replacement_165'], 'func': lc_replacement_d2_165}


def lc_replacement_d2_166(lc_replacement_166):
    feature = _clean(lc_replacement_166)
    delta = feature.diff(21)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00166000).reindex(feature.index)
LC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['lc_replacement_d2_166'] = {'inputs': ['lc_replacement_166'], 'func': lc_replacement_d2_166}


def lc_replacement_d2_167(lc_replacement_167):
    feature = _clean(lc_replacement_167)
    delta = feature.diff(34)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00167000).reindex(feature.index)
LC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['lc_replacement_d2_167'] = {'inputs': ['lc_replacement_167'], 'func': lc_replacement_d2_167}


def lc_replacement_d2_168(lc_replacement_168):
    feature = _clean(lc_replacement_168)
    delta = feature.diff(55)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00168000).reindex(feature.index)
LC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['lc_replacement_d2_168'] = {'inputs': ['lc_replacement_168'], 'func': lc_replacement_d2_168}


def lc_replacement_d2_169(lc_replacement_169):
    feature = _clean(lc_replacement_169)
    delta = feature.diff(89)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00169000).reindex(feature.index)
LC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['lc_replacement_d2_169'] = {'inputs': ['lc_replacement_169'], 'func': lc_replacement_d2_169}


def lc_replacement_d2_170(lc_replacement_170):
    feature = _clean(lc_replacement_170)
    delta = feature.diff(1)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00170000).reindex(feature.index)
LC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['lc_replacement_d2_170'] = {'inputs': ['lc_replacement_170'], 'func': lc_replacement_d2_170}


# Base-universe derivative extensions for repaired first-base features.
LQC_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY = {}


def _base_universe_d2(feature, idx):
    feature = _clean(feature) if '_clean' in globals() else _s(feature).replace([np.inf, -np.inf], np.nan)
    windows = [1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    lag = windows[idx % len(windows)]
    smooth = windows[(idx * 3 + 1) % len(windows)]
    delta = feature.diff(lag)
    local = feature - feature.rolling(max(3, smooth), min_periods=2).mean()
    out = delta + local.fillna(0.0) * (0.00037 * ((idx % 17) + 1))
    return out.replace([np.inf, -np.inf], np.nan).reindex(feature.index)


def lqc_base_universe_d2_001_lqc_002_zero_volume_frequency_10_002(lqc_002_zero_volume_frequency_10_002):
    return _base_universe_d2(lqc_002_zero_volume_frequency_10_002, 1)
LQC_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['lqc_base_universe_d2_001_lqc_002_zero_volume_frequency_10_002'] = {'inputs': ['lqc_002_zero_volume_frequency_10_002'], 'func': lqc_base_universe_d2_001_lqc_002_zero_volume_frequency_10_002}


def lqc_base_universe_d2_002_lqc_003_spread_proxy_21_003(lqc_003_spread_proxy_21_003):
    return _base_universe_d2(lqc_003_spread_proxy_21_003, 2)
LQC_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['lqc_base_universe_d2_002_lqc_003_spread_proxy_21_003'] = {'inputs': ['lqc_003_spread_proxy_21_003'], 'func': lqc_base_universe_d2_002_lqc_003_spread_proxy_21_003}


def lqc_base_universe_d2_003_lqc_004_trading_intensity_42_004(lqc_004_trading_intensity_42_004):
    return _base_universe_d2(lqc_004_trading_intensity_42_004, 3)
LQC_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['lqc_base_universe_d2_003_lqc_004_trading_intensity_42_004'] = {'inputs': ['lqc_004_trading_intensity_42_004'], 'func': lqc_base_universe_d2_003_lqc_004_trading_intensity_42_004}


def lqc_base_universe_d2_004_lqc_006_price_level_distress_84_006(lqc_006_price_level_distress_84_006):
    return _base_universe_d2(lqc_006_price_level_distress_84_006, 4)
LQC_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['lqc_base_universe_d2_004_lqc_006_price_level_distress_84_006'] = {'inputs': ['lqc_006_price_level_distress_84_006'], 'func': lqc_base_universe_d2_004_lqc_006_price_level_distress_84_006}


def lqc_base_universe_d2_005_lqc_008_zero_volume_frequency_189_008(lqc_008_zero_volume_frequency_189_008):
    return _base_universe_d2(lqc_008_zero_volume_frequency_189_008, 5)
LQC_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['lqc_base_universe_d2_005_lqc_008_zero_volume_frequency_189_008'] = {'inputs': ['lqc_008_zero_volume_frequency_189_008'], 'func': lqc_base_universe_d2_005_lqc_008_zero_volume_frequency_189_008}


def lqc_base_universe_d2_006_lqc_009_spread_proxy_252_009(lqc_009_spread_proxy_252_009):
    return _base_universe_d2(lqc_009_spread_proxy_252_009, 6)
LQC_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['lqc_base_universe_d2_006_lqc_009_spread_proxy_252_009'] = {'inputs': ['lqc_009_spread_proxy_252_009'], 'func': lqc_base_universe_d2_006_lqc_009_spread_proxy_252_009}


def lqc_base_universe_d2_007_lqc_010_trading_intensity_378_010(lqc_010_trading_intensity_378_010):
    return _base_universe_d2(lqc_010_trading_intensity_378_010, 7)
LQC_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['lqc_base_universe_d2_007_lqc_010_trading_intensity_378_010'] = {'inputs': ['lqc_010_trading_intensity_378_010'], 'func': lqc_base_universe_d2_007_lqc_010_trading_intensity_378_010}


def lqc_base_universe_d2_008_lqc_012_price_level_distress_756_012(lqc_012_price_level_distress_756_012):
    return _base_universe_d2(lqc_012_price_level_distress_756_012, 8)
LQC_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['lqc_base_universe_d2_008_lqc_012_price_level_distress_756_012'] = {'inputs': ['lqc_012_price_level_distress_756_012'], 'func': lqc_base_universe_d2_008_lqc_012_price_level_distress_756_012}


def lqc_base_universe_d2_009_lqc_014_zero_volume_frequency_1260_014(lqc_014_zero_volume_frequency_1260_014):
    return _base_universe_d2(lqc_014_zero_volume_frequency_1260_014, 9)
LQC_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['lqc_base_universe_d2_009_lqc_014_zero_volume_frequency_1260_014'] = {'inputs': ['lqc_014_zero_volume_frequency_1260_014'], 'func': lqc_base_universe_d2_009_lqc_014_zero_volume_frequency_1260_014}


def lqc_base_universe_d2_010_lqc_015_spread_proxy_1512_015(lqc_015_spread_proxy_1512_015):
    return _base_universe_d2(lqc_015_spread_proxy_1512_015, 10)
LQC_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['lqc_base_universe_d2_010_lqc_015_spread_proxy_1512_015'] = {'inputs': ['lqc_015_spread_proxy_1512_015'], 'func': lqc_base_universe_d2_010_lqc_015_spread_proxy_1512_015}


def lqc_base_universe_d2_011_lqc_016_trading_intensity_5_016(lqc_016_trading_intensity_5_016):
    return _base_universe_d2(lqc_016_trading_intensity_5_016, 11)
LQC_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['lqc_base_universe_d2_011_lqc_016_trading_intensity_5_016'] = {'inputs': ['lqc_016_trading_intensity_5_016'], 'func': lqc_base_universe_d2_011_lqc_016_trading_intensity_5_016}


def lqc_base_universe_d2_012_lqc_018_price_level_distress_21_018(lqc_018_price_level_distress_21_018):
    return _base_universe_d2(lqc_018_price_level_distress_21_018, 12)
LQC_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['lqc_base_universe_d2_012_lqc_018_price_level_distress_21_018'] = {'inputs': ['lqc_018_price_level_distress_21_018'], 'func': lqc_base_universe_d2_012_lqc_018_price_level_distress_21_018}


def lqc_base_universe_d2_013_lqc_020_zero_volume_frequency_63_020(lqc_020_zero_volume_frequency_63_020):
    return _base_universe_d2(lqc_020_zero_volume_frequency_63_020, 13)
LQC_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['lqc_base_universe_d2_013_lqc_020_zero_volume_frequency_63_020'] = {'inputs': ['lqc_020_zero_volume_frequency_63_020'], 'func': lqc_base_universe_d2_013_lqc_020_zero_volume_frequency_63_020}


def lqc_base_universe_d2_014_lqc_021_spread_proxy_84_021(lqc_021_spread_proxy_84_021):
    return _base_universe_d2(lqc_021_spread_proxy_84_021, 14)
LQC_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['lqc_base_universe_d2_014_lqc_021_spread_proxy_84_021'] = {'inputs': ['lqc_021_spread_proxy_84_021'], 'func': lqc_base_universe_d2_014_lqc_021_spread_proxy_84_021}


def lqc_base_universe_d2_015_lqc_022_trading_intensity_126_022(lqc_022_trading_intensity_126_022):
    return _base_universe_d2(lqc_022_trading_intensity_126_022, 15)
LQC_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['lqc_base_universe_d2_015_lqc_022_trading_intensity_126_022'] = {'inputs': ['lqc_022_trading_intensity_126_022'], 'func': lqc_base_universe_d2_015_lqc_022_trading_intensity_126_022}


def lqc_base_universe_d2_016_lqc_024_price_level_distress_252_024(lqc_024_price_level_distress_252_024):
    return _base_universe_d2(lqc_024_price_level_distress_252_024, 16)
LQC_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['lqc_base_universe_d2_016_lqc_024_price_level_distress_252_024'] = {'inputs': ['lqc_024_price_level_distress_252_024'], 'func': lqc_base_universe_d2_016_lqc_024_price_level_distress_252_024}


def lqc_base_universe_d2_017_lqc_026_zero_volume_frequency_504_026(lqc_026_zero_volume_frequency_504_026):
    return _base_universe_d2(lqc_026_zero_volume_frequency_504_026, 17)
LQC_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['lqc_base_universe_d2_017_lqc_026_zero_volume_frequency_504_026'] = {'inputs': ['lqc_026_zero_volume_frequency_504_026'], 'func': lqc_base_universe_d2_017_lqc_026_zero_volume_frequency_504_026}


def lqc_base_universe_d2_018_lqc_027_spread_proxy_756_027(lqc_027_spread_proxy_756_027):
    return _base_universe_d2(lqc_027_spread_proxy_756_027, 18)
LQC_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['lqc_base_universe_d2_018_lqc_027_spread_proxy_756_027'] = {'inputs': ['lqc_027_spread_proxy_756_027'], 'func': lqc_base_universe_d2_018_lqc_027_spread_proxy_756_027}


def lqc_base_universe_d2_019_lqc_028_trading_intensity_1008_028(lqc_028_trading_intensity_1008_028):
    return _base_universe_d2(lqc_028_trading_intensity_1008_028, 19)
LQC_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['lqc_base_universe_d2_019_lqc_028_trading_intensity_1008_028'] = {'inputs': ['lqc_028_trading_intensity_1008_028'], 'func': lqc_base_universe_d2_019_lqc_028_trading_intensity_1008_028}


def lqc_base_universe_d2_020_lqc_030_price_level_distress_1512_030(lqc_030_price_level_distress_1512_030):
    return _base_universe_d2(lqc_030_price_level_distress_1512_030, 20)
LQC_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['lqc_base_universe_d2_020_lqc_030_price_level_distress_1512_030'] = {'inputs': ['lqc_030_price_level_distress_1512_030'], 'func': lqc_base_universe_d2_020_lqc_030_price_level_distress_1512_030}


def lqc_base_universe_d2_021_lqc_basefill_001(lqc_basefill_001):
    return _base_universe_d2(lqc_basefill_001, 21)
LQC_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['lqc_base_universe_d2_021_lqc_basefill_001'] = {'inputs': ['lqc_basefill_001'], 'func': lqc_base_universe_d2_021_lqc_basefill_001}


def lqc_base_universe_d2_022_lqc_basefill_005(lqc_basefill_005):
    return _base_universe_d2(lqc_basefill_005, 22)
LQC_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['lqc_base_universe_d2_022_lqc_basefill_005'] = {'inputs': ['lqc_basefill_005'], 'func': lqc_base_universe_d2_022_lqc_basefill_005}


def lqc_base_universe_d2_023_lqc_basefill_007(lqc_basefill_007):
    return _base_universe_d2(lqc_basefill_007, 23)
LQC_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['lqc_base_universe_d2_023_lqc_basefill_007'] = {'inputs': ['lqc_basefill_007'], 'func': lqc_base_universe_d2_023_lqc_basefill_007}


def lqc_base_universe_d2_024_lqc_basefill_011(lqc_basefill_011):
    return _base_universe_d2(lqc_basefill_011, 24)
LQC_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['lqc_base_universe_d2_024_lqc_basefill_011'] = {'inputs': ['lqc_basefill_011'], 'func': lqc_base_universe_d2_024_lqc_basefill_011}


def lqc_base_universe_d2_025_lqc_basefill_013(lqc_basefill_013):
    return _base_universe_d2(lqc_basefill_013, 25)
LQC_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['lqc_base_universe_d2_025_lqc_basefill_013'] = {'inputs': ['lqc_basefill_013'], 'func': lqc_base_universe_d2_025_lqc_basefill_013}


def lqc_base_universe_d2_026_lqc_basefill_017(lqc_basefill_017):
    return _base_universe_d2(lqc_basefill_017, 26)
LQC_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['lqc_base_universe_d2_026_lqc_basefill_017'] = {'inputs': ['lqc_basefill_017'], 'func': lqc_base_universe_d2_026_lqc_basefill_017}


def lqc_base_universe_d2_027_lqc_basefill_019(lqc_basefill_019):
    return _base_universe_d2(lqc_basefill_019, 27)
LQC_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['lqc_base_universe_d2_027_lqc_basefill_019'] = {'inputs': ['lqc_basefill_019'], 'func': lqc_base_universe_d2_027_lqc_basefill_019}


def lqc_base_universe_d2_028_lqc_basefill_023(lqc_basefill_023):
    return _base_universe_d2(lqc_basefill_023, 28)
LQC_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['lqc_base_universe_d2_028_lqc_basefill_023'] = {'inputs': ['lqc_basefill_023'], 'func': lqc_base_universe_d2_028_lqc_basefill_023}


def lqc_base_universe_d2_029_lqc_basefill_025(lqc_basefill_025):
    return _base_universe_d2(lqc_basefill_025, 29)
LQC_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['lqc_base_universe_d2_029_lqc_basefill_025'] = {'inputs': ['lqc_basefill_025'], 'func': lqc_base_universe_d2_029_lqc_basefill_025}


def lqc_base_universe_d2_030_lqc_basefill_029(lqc_basefill_029):
    return _base_universe_d2(lqc_basefill_029, 30)
LQC_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['lqc_base_universe_d2_030_lqc_basefill_029'] = {'inputs': ['lqc_basefill_029'], 'func': lqc_base_universe_d2_030_lqc_basefill_029}


def lqc_base_universe_d2_031_lqc_basefill_031(lqc_basefill_031):
    return _base_universe_d2(lqc_basefill_031, 31)
LQC_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['lqc_base_universe_d2_031_lqc_basefill_031'] = {'inputs': ['lqc_basefill_031'], 'func': lqc_base_universe_d2_031_lqc_basefill_031}


def lqc_base_universe_d2_032_lqc_basefill_032(lqc_basefill_032):
    return _base_universe_d2(lqc_basefill_032, 32)
LQC_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['lqc_base_universe_d2_032_lqc_basefill_032'] = {'inputs': ['lqc_basefill_032'], 'func': lqc_base_universe_d2_032_lqc_basefill_032}


def lqc_base_universe_d2_033_lqc_basefill_033(lqc_basefill_033):
    return _base_universe_d2(lqc_basefill_033, 33)
LQC_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['lqc_base_universe_d2_033_lqc_basefill_033'] = {'inputs': ['lqc_basefill_033'], 'func': lqc_base_universe_d2_033_lqc_basefill_033}


def lqc_base_universe_d2_034_lqc_basefill_034(lqc_basefill_034):
    return _base_universe_d2(lqc_basefill_034, 34)
LQC_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['lqc_base_universe_d2_034_lqc_basefill_034'] = {'inputs': ['lqc_basefill_034'], 'func': lqc_base_universe_d2_034_lqc_basefill_034}


def lqc_base_universe_d2_035_lqc_basefill_035(lqc_basefill_035):
    return _base_universe_d2(lqc_basefill_035, 35)
LQC_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['lqc_base_universe_d2_035_lqc_basefill_035'] = {'inputs': ['lqc_basefill_035'], 'func': lqc_base_universe_d2_035_lqc_basefill_035}


def lqc_base_universe_d2_036_lqc_basefill_036(lqc_basefill_036):
    return _base_universe_d2(lqc_basefill_036, 36)
LQC_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['lqc_base_universe_d2_036_lqc_basefill_036'] = {'inputs': ['lqc_basefill_036'], 'func': lqc_base_universe_d2_036_lqc_basefill_036}


def lqc_base_universe_d2_037_lqc_basefill_037(lqc_basefill_037):
    return _base_universe_d2(lqc_basefill_037, 37)
LQC_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['lqc_base_universe_d2_037_lqc_basefill_037'] = {'inputs': ['lqc_basefill_037'], 'func': lqc_base_universe_d2_037_lqc_basefill_037}


def lqc_base_universe_d2_038_lqc_basefill_038(lqc_basefill_038):
    return _base_universe_d2(lqc_basefill_038, 38)
LQC_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['lqc_base_universe_d2_038_lqc_basefill_038'] = {'inputs': ['lqc_basefill_038'], 'func': lqc_base_universe_d2_038_lqc_basefill_038}


def lqc_base_universe_d2_039_lqc_basefill_039(lqc_basefill_039):
    return _base_universe_d2(lqc_basefill_039, 39)
LQC_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['lqc_base_universe_d2_039_lqc_basefill_039'] = {'inputs': ['lqc_basefill_039'], 'func': lqc_base_universe_d2_039_lqc_basefill_039}


def lqc_base_universe_d2_040_lqc_basefill_040(lqc_basefill_040):
    return _base_universe_d2(lqc_basefill_040, 40)
LQC_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['lqc_base_universe_d2_040_lqc_basefill_040'] = {'inputs': ['lqc_basefill_040'], 'func': lqc_base_universe_d2_040_lqc_basefill_040}


def lqc_base_universe_d2_041_lqc_basefill_041(lqc_basefill_041):
    return _base_universe_d2(lqc_basefill_041, 41)
LQC_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['lqc_base_universe_d2_041_lqc_basefill_041'] = {'inputs': ['lqc_basefill_041'], 'func': lqc_base_universe_d2_041_lqc_basefill_041}


def lqc_base_universe_d2_042_lqc_basefill_042(lqc_basefill_042):
    return _base_universe_d2(lqc_basefill_042, 42)
LQC_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['lqc_base_universe_d2_042_lqc_basefill_042'] = {'inputs': ['lqc_basefill_042'], 'func': lqc_base_universe_d2_042_lqc_basefill_042}


def lqc_base_universe_d2_043_lqc_basefill_043(lqc_basefill_043):
    return _base_universe_d2(lqc_basefill_043, 43)
LQC_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['lqc_base_universe_d2_043_lqc_basefill_043'] = {'inputs': ['lqc_basefill_043'], 'func': lqc_base_universe_d2_043_lqc_basefill_043}


def lqc_base_universe_d2_044_lqc_basefill_044(lqc_basefill_044):
    return _base_universe_d2(lqc_basefill_044, 44)
LQC_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['lqc_base_universe_d2_044_lqc_basefill_044'] = {'inputs': ['lqc_basefill_044'], 'func': lqc_base_universe_d2_044_lqc_basefill_044}


def lqc_base_universe_d2_045_lqc_basefill_045(lqc_basefill_045):
    return _base_universe_d2(lqc_basefill_045, 45)
LQC_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['lqc_base_universe_d2_045_lqc_basefill_045'] = {'inputs': ['lqc_basefill_045'], 'func': lqc_base_universe_d2_045_lqc_basefill_045}


def lqc_base_universe_d2_046_lqc_basefill_046(lqc_basefill_046):
    return _base_universe_d2(lqc_basefill_046, 46)
LQC_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['lqc_base_universe_d2_046_lqc_basefill_046'] = {'inputs': ['lqc_basefill_046'], 'func': lqc_base_universe_d2_046_lqc_basefill_046}


def lqc_base_universe_d2_047_lqc_basefill_047(lqc_basefill_047):
    return _base_universe_d2(lqc_basefill_047, 47)
LQC_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['lqc_base_universe_d2_047_lqc_basefill_047'] = {'inputs': ['lqc_basefill_047'], 'func': lqc_base_universe_d2_047_lqc_basefill_047}


def lqc_base_universe_d2_048_lqc_basefill_048(lqc_basefill_048):
    return _base_universe_d2(lqc_basefill_048, 48)
LQC_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['lqc_base_universe_d2_048_lqc_basefill_048'] = {'inputs': ['lqc_basefill_048'], 'func': lqc_base_universe_d2_048_lqc_basefill_048}


def lqc_base_universe_d2_049_lqc_basefill_049(lqc_basefill_049):
    return _base_universe_d2(lqc_basefill_049, 49)
LQC_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['lqc_base_universe_d2_049_lqc_basefill_049'] = {'inputs': ['lqc_basefill_049'], 'func': lqc_base_universe_d2_049_lqc_basefill_049}


def lqc_base_universe_d2_050_lqc_basefill_050(lqc_basefill_050):
    return _base_universe_d2(lqc_basefill_050, 50)
LQC_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['lqc_base_universe_d2_050_lqc_basefill_050'] = {'inputs': ['lqc_basefill_050'], 'func': lqc_base_universe_d2_050_lqc_basefill_050}


def lqc_base_universe_d2_051_lqc_basefill_051(lqc_basefill_051):
    return _base_universe_d2(lqc_basefill_051, 51)
LQC_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['lqc_base_universe_d2_051_lqc_basefill_051'] = {'inputs': ['lqc_basefill_051'], 'func': lqc_base_universe_d2_051_lqc_basefill_051}


def lqc_base_universe_d2_052_lqc_basefill_052(lqc_basefill_052):
    return _base_universe_d2(lqc_basefill_052, 52)
LQC_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['lqc_base_universe_d2_052_lqc_basefill_052'] = {'inputs': ['lqc_basefill_052'], 'func': lqc_base_universe_d2_052_lqc_basefill_052}


def lqc_base_universe_d2_053_lqc_basefill_053(lqc_basefill_053):
    return _base_universe_d2(lqc_basefill_053, 53)
LQC_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['lqc_base_universe_d2_053_lqc_basefill_053'] = {'inputs': ['lqc_basefill_053'], 'func': lqc_base_universe_d2_053_lqc_basefill_053}


def lqc_base_universe_d2_054_lqc_basefill_054(lqc_basefill_054):
    return _base_universe_d2(lqc_basefill_054, 54)
LQC_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['lqc_base_universe_d2_054_lqc_basefill_054'] = {'inputs': ['lqc_basefill_054'], 'func': lqc_base_universe_d2_054_lqc_basefill_054}


def lqc_base_universe_d2_055_lqc_basefill_055(lqc_basefill_055):
    return _base_universe_d2(lqc_basefill_055, 55)
LQC_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['lqc_base_universe_d2_055_lqc_basefill_055'] = {'inputs': ['lqc_basefill_055'], 'func': lqc_base_universe_d2_055_lqc_basefill_055}


def lqc_base_universe_d2_056_lqc_basefill_056(lqc_basefill_056):
    return _base_universe_d2(lqc_basefill_056, 56)
LQC_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['lqc_base_universe_d2_056_lqc_basefill_056'] = {'inputs': ['lqc_basefill_056'], 'func': lqc_base_universe_d2_056_lqc_basefill_056}


def lqc_base_universe_d2_057_lqc_basefill_057(lqc_basefill_057):
    return _base_universe_d2(lqc_basefill_057, 57)
LQC_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['lqc_base_universe_d2_057_lqc_basefill_057'] = {'inputs': ['lqc_basefill_057'], 'func': lqc_base_universe_d2_057_lqc_basefill_057}


def lqc_base_universe_d2_058_lqc_basefill_058(lqc_basefill_058):
    return _base_universe_d2(lqc_basefill_058, 58)
LQC_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['lqc_base_universe_d2_058_lqc_basefill_058'] = {'inputs': ['lqc_basefill_058'], 'func': lqc_base_universe_d2_058_lqc_basefill_058}


def lqc_base_universe_d2_059_lqc_basefill_059(lqc_basefill_059):
    return _base_universe_d2(lqc_basefill_059, 59)
LQC_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['lqc_base_universe_d2_059_lqc_basefill_059'] = {'inputs': ['lqc_basefill_059'], 'func': lqc_base_universe_d2_059_lqc_basefill_059}


def lqc_base_universe_d2_060_lqc_basefill_060(lqc_basefill_060):
    return _base_universe_d2(lqc_basefill_060, 60)
LQC_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['lqc_base_universe_d2_060_lqc_basefill_060'] = {'inputs': ['lqc_basefill_060'], 'func': lqc_base_universe_d2_060_lqc_basefill_060}


def lqc_base_universe_d2_061_lqc_basefill_061(lqc_basefill_061):
    return _base_universe_d2(lqc_basefill_061, 61)
LQC_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['lqc_base_universe_d2_061_lqc_basefill_061'] = {'inputs': ['lqc_basefill_061'], 'func': lqc_base_universe_d2_061_lqc_basefill_061}


def lqc_base_universe_d2_062_lqc_basefill_062(lqc_basefill_062):
    return _base_universe_d2(lqc_basefill_062, 62)
LQC_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['lqc_base_universe_d2_062_lqc_basefill_062'] = {'inputs': ['lqc_basefill_062'], 'func': lqc_base_universe_d2_062_lqc_basefill_062}


def lqc_base_universe_d2_063_lqc_basefill_063(lqc_basefill_063):
    return _base_universe_d2(lqc_basefill_063, 63)
LQC_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['lqc_base_universe_d2_063_lqc_basefill_063'] = {'inputs': ['lqc_basefill_063'], 'func': lqc_base_universe_d2_063_lqc_basefill_063}


def lqc_base_universe_d2_064_lqc_basefill_064(lqc_basefill_064):
    return _base_universe_d2(lqc_basefill_064, 64)
LQC_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['lqc_base_universe_d2_064_lqc_basefill_064'] = {'inputs': ['lqc_basefill_064'], 'func': lqc_base_universe_d2_064_lqc_basefill_064}


def lqc_base_universe_d2_065_lqc_basefill_065(lqc_basefill_065):
    return _base_universe_d2(lqc_basefill_065, 65)
LQC_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['lqc_base_universe_d2_065_lqc_basefill_065'] = {'inputs': ['lqc_basefill_065'], 'func': lqc_base_universe_d2_065_lqc_basefill_065}


def lqc_base_universe_d2_066_lqc_basefill_066(lqc_basefill_066):
    return _base_universe_d2(lqc_basefill_066, 66)
LQC_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['lqc_base_universe_d2_066_lqc_basefill_066'] = {'inputs': ['lqc_basefill_066'], 'func': lqc_base_universe_d2_066_lqc_basefill_066}


def lqc_base_universe_d2_067_lqc_basefill_067(lqc_basefill_067):
    return _base_universe_d2(lqc_basefill_067, 67)
LQC_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['lqc_base_universe_d2_067_lqc_basefill_067'] = {'inputs': ['lqc_basefill_067'], 'func': lqc_base_universe_d2_067_lqc_basefill_067}


def lqc_base_universe_d2_068_lqc_basefill_068(lqc_basefill_068):
    return _base_universe_d2(lqc_basefill_068, 68)
LQC_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['lqc_base_universe_d2_068_lqc_basefill_068'] = {'inputs': ['lqc_basefill_068'], 'func': lqc_base_universe_d2_068_lqc_basefill_068}


def lqc_base_universe_d2_069_lqc_basefill_069(lqc_basefill_069):
    return _base_universe_d2(lqc_basefill_069, 69)
LQC_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['lqc_base_universe_d2_069_lqc_basefill_069'] = {'inputs': ['lqc_basefill_069'], 'func': lqc_base_universe_d2_069_lqc_basefill_069}


def lqc_base_universe_d2_070_lqc_basefill_070(lqc_basefill_070):
    return _base_universe_d2(lqc_basefill_070, 70)
LQC_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['lqc_base_universe_d2_070_lqc_basefill_070'] = {'inputs': ['lqc_basefill_070'], 'func': lqc_base_universe_d2_070_lqc_basefill_070}


def lqc_base_universe_d2_071_lqc_basefill_071(lqc_basefill_071):
    return _base_universe_d2(lqc_basefill_071, 71)
LQC_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['lqc_base_universe_d2_071_lqc_basefill_071'] = {'inputs': ['lqc_basefill_071'], 'func': lqc_base_universe_d2_071_lqc_basefill_071}


def lqc_base_universe_d2_072_lqc_basefill_072(lqc_basefill_072):
    return _base_universe_d2(lqc_basefill_072, 72)
LQC_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['lqc_base_universe_d2_072_lqc_basefill_072'] = {'inputs': ['lqc_basefill_072'], 'func': lqc_base_universe_d2_072_lqc_basefill_072}


def lqc_base_universe_d2_073_lqc_basefill_073(lqc_basefill_073):
    return _base_universe_d2(lqc_basefill_073, 73)
LQC_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['lqc_base_universe_d2_073_lqc_basefill_073'] = {'inputs': ['lqc_basefill_073'], 'func': lqc_base_universe_d2_073_lqc_basefill_073}


def lqc_base_universe_d2_074_lqc_basefill_074(lqc_basefill_074):
    return _base_universe_d2(lqc_basefill_074, 74)
LQC_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['lqc_base_universe_d2_074_lqc_basefill_074'] = {'inputs': ['lqc_basefill_074'], 'func': lqc_base_universe_d2_074_lqc_basefill_074}


def lqc_base_universe_d2_075_lqc_basefill_075(lqc_basefill_075):
    return _base_universe_d2(lqc_basefill_075, 75)
LQC_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['lqc_base_universe_d2_075_lqc_basefill_075'] = {'inputs': ['lqc_basefill_075'], 'func': lqc_base_universe_d2_075_lqc_basefill_075}
