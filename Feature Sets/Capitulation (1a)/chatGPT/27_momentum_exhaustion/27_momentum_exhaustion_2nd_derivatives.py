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



def mex_001_return_decay_roc_1(return_decay):
    feature = _s(return_decay)
    return (_roc(feature, 1)).reindex(feature.index)

def mex_007_return_decay_roc_5(return_decay):
    feature = _s(return_decay)
    return (_roc(feature, 5)).reindex(feature.index)

def mex_013_return_decay_roc_42(return_decay):
    feature = _s(return_decay)
    return (_roc(feature, 42)).reindex(feature.index)

def mex_154_mex_019_return_decay_42_019_roc_126(return_decay):
    feature = _s(return_decay)
    return (_roc(feature, 126)).reindex(feature.index)

def mex_155_mex_025_return_decay_5_025_roc_378(return_decay):
    feature = _s(return_decay)
    return (_roc(feature, 378)).reindex(feature.index)






















MOMENTUM_EXHAUSTION_REGISTRY_2ND_DERIVATIVES = {
    'mex_001_return_decay_roc_1': {'inputs': ['return_decay'], 'func': mex_001_return_decay_roc_1},
    'mex_007_return_decay_roc_5': {'inputs': ['return_decay'], 'func': mex_007_return_decay_roc_5},
    'mex_013_return_decay_roc_42': {'inputs': ['return_decay'], 'func': mex_013_return_decay_roc_42},
    'mex_154_mex_019_return_decay_42_019_roc_126': {'inputs': ['return_decay'], 'func': mex_154_mex_019_return_decay_42_019_roc_126},
    'mex_155_mex_025_return_decay_5_025_roc_378': {'inputs': ['return_decay'], 'func': mex_155_mex_025_return_decay_5_025_roc_378},
}


# Replacement 2nd-derivative features restored after redundancy audit.

import numpy as np
import pandas as pd


def _s(x):
    return pd.Series(x).astype(float)


def _clean(x):
    return _s(x).replace([np.inf, -np.inf], np.nan)


ME_REPLACEMENT_2ND_DERIVATIVES_REGISTRY = {}


def me_replacement_d2_001(me_replacement_001):
    feature = _clean(me_replacement_001)
    delta = feature.diff(2)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00001000).reindex(feature.index)
ME_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['me_replacement_d2_001'] = {'inputs': ['me_replacement_001'], 'func': me_replacement_d2_001}


def me_replacement_d2_002(me_replacement_002):
    feature = _clean(me_replacement_002)
    delta = feature.diff(3)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00002000).reindex(feature.index)
ME_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['me_replacement_d2_002'] = {'inputs': ['me_replacement_002'], 'func': me_replacement_d2_002}


def me_replacement_d2_003(me_replacement_003):
    feature = _clean(me_replacement_003)
    delta = feature.diff(5)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00003000).reindex(feature.index)
ME_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['me_replacement_d2_003'] = {'inputs': ['me_replacement_003'], 'func': me_replacement_d2_003}


def me_replacement_d2_004(me_replacement_004):
    feature = _clean(me_replacement_004)
    delta = feature.diff(8)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00004000).reindex(feature.index)
ME_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['me_replacement_d2_004'] = {'inputs': ['me_replacement_004'], 'func': me_replacement_d2_004}


def me_replacement_d2_005(me_replacement_005):
    feature = _clean(me_replacement_005)
    delta = feature.diff(13)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00005000).reindex(feature.index)
ME_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['me_replacement_d2_005'] = {'inputs': ['me_replacement_005'], 'func': me_replacement_d2_005}


def me_replacement_d2_006(me_replacement_006):
    feature = _clean(me_replacement_006)
    delta = feature.diff(21)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00006000).reindex(feature.index)
ME_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['me_replacement_d2_006'] = {'inputs': ['me_replacement_006'], 'func': me_replacement_d2_006}


def me_replacement_d2_007(me_replacement_007):
    feature = _clean(me_replacement_007)
    delta = feature.diff(34)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00007000).reindex(feature.index)
ME_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['me_replacement_d2_007'] = {'inputs': ['me_replacement_007'], 'func': me_replacement_d2_007}


def me_replacement_d2_008(me_replacement_008):
    feature = _clean(me_replacement_008)
    delta = feature.diff(55)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00008000).reindex(feature.index)
ME_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['me_replacement_d2_008'] = {'inputs': ['me_replacement_008'], 'func': me_replacement_d2_008}


def me_replacement_d2_009(me_replacement_009):
    feature = _clean(me_replacement_009)
    delta = feature.diff(89)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00009000).reindex(feature.index)
ME_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['me_replacement_d2_009'] = {'inputs': ['me_replacement_009'], 'func': me_replacement_d2_009}


def me_replacement_d2_010(me_replacement_010):
    feature = _clean(me_replacement_010)
    delta = feature.diff(1)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00010000).reindex(feature.index)
ME_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['me_replacement_d2_010'] = {'inputs': ['me_replacement_010'], 'func': me_replacement_d2_010}


def me_replacement_d2_011(me_replacement_011):
    feature = _clean(me_replacement_011)
    delta = feature.diff(2)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00011000).reindex(feature.index)
ME_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['me_replacement_d2_011'] = {'inputs': ['me_replacement_011'], 'func': me_replacement_d2_011}


def me_replacement_d2_012(me_replacement_012):
    feature = _clean(me_replacement_012)
    delta = feature.diff(3)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00012000).reindex(feature.index)
ME_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['me_replacement_d2_012'] = {'inputs': ['me_replacement_012'], 'func': me_replacement_d2_012}


def me_replacement_d2_013(me_replacement_013):
    feature = _clean(me_replacement_013)
    delta = feature.diff(5)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00013000).reindex(feature.index)
ME_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['me_replacement_d2_013'] = {'inputs': ['me_replacement_013'], 'func': me_replacement_d2_013}


def me_replacement_d2_014(me_replacement_014):
    feature = _clean(me_replacement_014)
    delta = feature.diff(8)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00014000).reindex(feature.index)
ME_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['me_replacement_d2_014'] = {'inputs': ['me_replacement_014'], 'func': me_replacement_d2_014}


def me_replacement_d2_015(me_replacement_015):
    feature = _clean(me_replacement_015)
    delta = feature.diff(13)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00015000).reindex(feature.index)
ME_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['me_replacement_d2_015'] = {'inputs': ['me_replacement_015'], 'func': me_replacement_d2_015}


def me_replacement_d2_016(me_replacement_016):
    feature = _clean(me_replacement_016)
    delta = feature.diff(21)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00016000).reindex(feature.index)
ME_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['me_replacement_d2_016'] = {'inputs': ['me_replacement_016'], 'func': me_replacement_d2_016}


def me_replacement_d2_017(me_replacement_017):
    feature = _clean(me_replacement_017)
    delta = feature.diff(34)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00017000).reindex(feature.index)
ME_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['me_replacement_d2_017'] = {'inputs': ['me_replacement_017'], 'func': me_replacement_d2_017}


def me_replacement_d2_018(me_replacement_018):
    feature = _clean(me_replacement_018)
    delta = feature.diff(55)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00018000).reindex(feature.index)
ME_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['me_replacement_d2_018'] = {'inputs': ['me_replacement_018'], 'func': me_replacement_d2_018}


def me_replacement_d2_019(me_replacement_019):
    feature = _clean(me_replacement_019)
    delta = feature.diff(89)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00019000).reindex(feature.index)
ME_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['me_replacement_d2_019'] = {'inputs': ['me_replacement_019'], 'func': me_replacement_d2_019}


def me_replacement_d2_020(me_replacement_020):
    feature = _clean(me_replacement_020)
    delta = feature.diff(1)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00020000).reindex(feature.index)
ME_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['me_replacement_d2_020'] = {'inputs': ['me_replacement_020'], 'func': me_replacement_d2_020}


def me_replacement_d2_021(me_replacement_021):
    feature = _clean(me_replacement_021)
    delta = feature.diff(2)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00021000).reindex(feature.index)
ME_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['me_replacement_d2_021'] = {'inputs': ['me_replacement_021'], 'func': me_replacement_d2_021}


def me_replacement_d2_022(me_replacement_022):
    feature = _clean(me_replacement_022)
    delta = feature.diff(3)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00022000).reindex(feature.index)
ME_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['me_replacement_d2_022'] = {'inputs': ['me_replacement_022'], 'func': me_replacement_d2_022}


def me_replacement_d2_023(me_replacement_023):
    feature = _clean(me_replacement_023)
    delta = feature.diff(5)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00023000).reindex(feature.index)
ME_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['me_replacement_d2_023'] = {'inputs': ['me_replacement_023'], 'func': me_replacement_d2_023}


def me_replacement_d2_024(me_replacement_024):
    feature = _clean(me_replacement_024)
    delta = feature.diff(8)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00024000).reindex(feature.index)
ME_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['me_replacement_d2_024'] = {'inputs': ['me_replacement_024'], 'func': me_replacement_d2_024}


def me_replacement_d2_025(me_replacement_025):
    feature = _clean(me_replacement_025)
    delta = feature.diff(13)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00025000).reindex(feature.index)
ME_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['me_replacement_d2_025'] = {'inputs': ['me_replacement_025'], 'func': me_replacement_d2_025}


def me_replacement_d2_026(me_replacement_026):
    feature = _clean(me_replacement_026)
    delta = feature.diff(21)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00026000).reindex(feature.index)
ME_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['me_replacement_d2_026'] = {'inputs': ['me_replacement_026'], 'func': me_replacement_d2_026}


def me_replacement_d2_027(me_replacement_027):
    feature = _clean(me_replacement_027)
    delta = feature.diff(34)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00027000).reindex(feature.index)
ME_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['me_replacement_d2_027'] = {'inputs': ['me_replacement_027'], 'func': me_replacement_d2_027}


def me_replacement_d2_028(me_replacement_028):
    feature = _clean(me_replacement_028)
    delta = feature.diff(55)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00028000).reindex(feature.index)
ME_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['me_replacement_d2_028'] = {'inputs': ['me_replacement_028'], 'func': me_replacement_d2_028}


def me_replacement_d2_029(me_replacement_029):
    feature = _clean(me_replacement_029)
    delta = feature.diff(89)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00029000).reindex(feature.index)
ME_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['me_replacement_d2_029'] = {'inputs': ['me_replacement_029'], 'func': me_replacement_d2_029}


def me_replacement_d2_030(me_replacement_030):
    feature = _clean(me_replacement_030)
    delta = feature.diff(1)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00030000).reindex(feature.index)
ME_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['me_replacement_d2_030'] = {'inputs': ['me_replacement_030'], 'func': me_replacement_d2_030}


def me_replacement_d2_031(me_replacement_031):
    feature = _clean(me_replacement_031)
    delta = feature.diff(2)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00031000).reindex(feature.index)
ME_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['me_replacement_d2_031'] = {'inputs': ['me_replacement_031'], 'func': me_replacement_d2_031}


def me_replacement_d2_032(me_replacement_032):
    feature = _clean(me_replacement_032)
    delta = feature.diff(3)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00032000).reindex(feature.index)
ME_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['me_replacement_d2_032'] = {'inputs': ['me_replacement_032'], 'func': me_replacement_d2_032}


def me_replacement_d2_033(me_replacement_033):
    feature = _clean(me_replacement_033)
    delta = feature.diff(5)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00033000).reindex(feature.index)
ME_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['me_replacement_d2_033'] = {'inputs': ['me_replacement_033'], 'func': me_replacement_d2_033}


def me_replacement_d2_034(me_replacement_034):
    feature = _clean(me_replacement_034)
    delta = feature.diff(8)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00034000).reindex(feature.index)
ME_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['me_replacement_d2_034'] = {'inputs': ['me_replacement_034'], 'func': me_replacement_d2_034}


def me_replacement_d2_035(me_replacement_035):
    feature = _clean(me_replacement_035)
    delta = feature.diff(13)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00035000).reindex(feature.index)
ME_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['me_replacement_d2_035'] = {'inputs': ['me_replacement_035'], 'func': me_replacement_d2_035}


def me_replacement_d2_036(me_replacement_036):
    feature = _clean(me_replacement_036)
    delta = feature.diff(21)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00036000).reindex(feature.index)
ME_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['me_replacement_d2_036'] = {'inputs': ['me_replacement_036'], 'func': me_replacement_d2_036}


def me_replacement_d2_037(me_replacement_037):
    feature = _clean(me_replacement_037)
    delta = feature.diff(34)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00037000).reindex(feature.index)
ME_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['me_replacement_d2_037'] = {'inputs': ['me_replacement_037'], 'func': me_replacement_d2_037}


def me_replacement_d2_038(me_replacement_038):
    feature = _clean(me_replacement_038)
    delta = feature.diff(55)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00038000).reindex(feature.index)
ME_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['me_replacement_d2_038'] = {'inputs': ['me_replacement_038'], 'func': me_replacement_d2_038}


def me_replacement_d2_039(me_replacement_039):
    feature = _clean(me_replacement_039)
    delta = feature.diff(89)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00039000).reindex(feature.index)
ME_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['me_replacement_d2_039'] = {'inputs': ['me_replacement_039'], 'func': me_replacement_d2_039}


def me_replacement_d2_040(me_replacement_040):
    feature = _clean(me_replacement_040)
    delta = feature.diff(1)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00040000).reindex(feature.index)
ME_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['me_replacement_d2_040'] = {'inputs': ['me_replacement_040'], 'func': me_replacement_d2_040}


def me_replacement_d2_041(me_replacement_041):
    feature = _clean(me_replacement_041)
    delta = feature.diff(2)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00041000).reindex(feature.index)
ME_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['me_replacement_d2_041'] = {'inputs': ['me_replacement_041'], 'func': me_replacement_d2_041}


def me_replacement_d2_042(me_replacement_042):
    feature = _clean(me_replacement_042)
    delta = feature.diff(3)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00042000).reindex(feature.index)
ME_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['me_replacement_d2_042'] = {'inputs': ['me_replacement_042'], 'func': me_replacement_d2_042}


def me_replacement_d2_043(me_replacement_043):
    feature = _clean(me_replacement_043)
    delta = feature.diff(5)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00043000).reindex(feature.index)
ME_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['me_replacement_d2_043'] = {'inputs': ['me_replacement_043'], 'func': me_replacement_d2_043}


def me_replacement_d2_044(me_replacement_044):
    feature = _clean(me_replacement_044)
    delta = feature.diff(8)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00044000).reindex(feature.index)
ME_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['me_replacement_d2_044'] = {'inputs': ['me_replacement_044'], 'func': me_replacement_d2_044}


def me_replacement_d2_045(me_replacement_045):
    feature = _clean(me_replacement_045)
    delta = feature.diff(13)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00045000).reindex(feature.index)
ME_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['me_replacement_d2_045'] = {'inputs': ['me_replacement_045'], 'func': me_replacement_d2_045}


def me_replacement_d2_046(me_replacement_046):
    feature = _clean(me_replacement_046)
    delta = feature.diff(21)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00046000).reindex(feature.index)
ME_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['me_replacement_d2_046'] = {'inputs': ['me_replacement_046'], 'func': me_replacement_d2_046}


def me_replacement_d2_047(me_replacement_047):
    feature = _clean(me_replacement_047)
    delta = feature.diff(34)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00047000).reindex(feature.index)
ME_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['me_replacement_d2_047'] = {'inputs': ['me_replacement_047'], 'func': me_replacement_d2_047}


def me_replacement_d2_048(me_replacement_048):
    feature = _clean(me_replacement_048)
    delta = feature.diff(55)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00048000).reindex(feature.index)
ME_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['me_replacement_d2_048'] = {'inputs': ['me_replacement_048'], 'func': me_replacement_d2_048}


def me_replacement_d2_049(me_replacement_049):
    feature = _clean(me_replacement_049)
    delta = feature.diff(89)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00049000).reindex(feature.index)
ME_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['me_replacement_d2_049'] = {'inputs': ['me_replacement_049'], 'func': me_replacement_d2_049}


def me_replacement_d2_050(me_replacement_050):
    feature = _clean(me_replacement_050)
    delta = feature.diff(1)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00050000).reindex(feature.index)
ME_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['me_replacement_d2_050'] = {'inputs': ['me_replacement_050'], 'func': me_replacement_d2_050}


def me_replacement_d2_051(me_replacement_051):
    feature = _clean(me_replacement_051)
    delta = feature.diff(2)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00051000).reindex(feature.index)
ME_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['me_replacement_d2_051'] = {'inputs': ['me_replacement_051'], 'func': me_replacement_d2_051}


def me_replacement_d2_052(me_replacement_052):
    feature = _clean(me_replacement_052)
    delta = feature.diff(3)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00052000).reindex(feature.index)
ME_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['me_replacement_d2_052'] = {'inputs': ['me_replacement_052'], 'func': me_replacement_d2_052}


def me_replacement_d2_053(me_replacement_053):
    feature = _clean(me_replacement_053)
    delta = feature.diff(5)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00053000).reindex(feature.index)
ME_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['me_replacement_d2_053'] = {'inputs': ['me_replacement_053'], 'func': me_replacement_d2_053}


def me_replacement_d2_054(me_replacement_054):
    feature = _clean(me_replacement_054)
    delta = feature.diff(8)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00054000).reindex(feature.index)
ME_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['me_replacement_d2_054'] = {'inputs': ['me_replacement_054'], 'func': me_replacement_d2_054}


def me_replacement_d2_055(me_replacement_055):
    feature = _clean(me_replacement_055)
    delta = feature.diff(13)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00055000).reindex(feature.index)
ME_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['me_replacement_d2_055'] = {'inputs': ['me_replacement_055'], 'func': me_replacement_d2_055}


def me_replacement_d2_056(me_replacement_056):
    feature = _clean(me_replacement_056)
    delta = feature.diff(21)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00056000).reindex(feature.index)
ME_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['me_replacement_d2_056'] = {'inputs': ['me_replacement_056'], 'func': me_replacement_d2_056}


def me_replacement_d2_057(me_replacement_057):
    feature = _clean(me_replacement_057)
    delta = feature.diff(34)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00057000).reindex(feature.index)
ME_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['me_replacement_d2_057'] = {'inputs': ['me_replacement_057'], 'func': me_replacement_d2_057}


def me_replacement_d2_058(me_replacement_058):
    feature = _clean(me_replacement_058)
    delta = feature.diff(55)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00058000).reindex(feature.index)
ME_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['me_replacement_d2_058'] = {'inputs': ['me_replacement_058'], 'func': me_replacement_d2_058}


def me_replacement_d2_059(me_replacement_059):
    feature = _clean(me_replacement_059)
    delta = feature.diff(89)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00059000).reindex(feature.index)
ME_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['me_replacement_d2_059'] = {'inputs': ['me_replacement_059'], 'func': me_replacement_d2_059}


def me_replacement_d2_060(me_replacement_060):
    feature = _clean(me_replacement_060)
    delta = feature.diff(1)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00060000).reindex(feature.index)
ME_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['me_replacement_d2_060'] = {'inputs': ['me_replacement_060'], 'func': me_replacement_d2_060}


def me_replacement_d2_061(me_replacement_061):
    feature = _clean(me_replacement_061)
    delta = feature.diff(2)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00061000).reindex(feature.index)
ME_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['me_replacement_d2_061'] = {'inputs': ['me_replacement_061'], 'func': me_replacement_d2_061}


def me_replacement_d2_062(me_replacement_062):
    feature = _clean(me_replacement_062)
    delta = feature.diff(3)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00062000).reindex(feature.index)
ME_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['me_replacement_d2_062'] = {'inputs': ['me_replacement_062'], 'func': me_replacement_d2_062}


def me_replacement_d2_063(me_replacement_063):
    feature = _clean(me_replacement_063)
    delta = feature.diff(5)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00063000).reindex(feature.index)
ME_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['me_replacement_d2_063'] = {'inputs': ['me_replacement_063'], 'func': me_replacement_d2_063}


def me_replacement_d2_064(me_replacement_064):
    feature = _clean(me_replacement_064)
    delta = feature.diff(8)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00064000).reindex(feature.index)
ME_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['me_replacement_d2_064'] = {'inputs': ['me_replacement_064'], 'func': me_replacement_d2_064}


def me_replacement_d2_065(me_replacement_065):
    feature = _clean(me_replacement_065)
    delta = feature.diff(13)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00065000).reindex(feature.index)
ME_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['me_replacement_d2_065'] = {'inputs': ['me_replacement_065'], 'func': me_replacement_d2_065}


def me_replacement_d2_066(me_replacement_066):
    feature = _clean(me_replacement_066)
    delta = feature.diff(21)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00066000).reindex(feature.index)
ME_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['me_replacement_d2_066'] = {'inputs': ['me_replacement_066'], 'func': me_replacement_d2_066}


def me_replacement_d2_067(me_replacement_067):
    feature = _clean(me_replacement_067)
    delta = feature.diff(34)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00067000).reindex(feature.index)
ME_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['me_replacement_d2_067'] = {'inputs': ['me_replacement_067'], 'func': me_replacement_d2_067}


def me_replacement_d2_068(me_replacement_068):
    feature = _clean(me_replacement_068)
    delta = feature.diff(55)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00068000).reindex(feature.index)
ME_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['me_replacement_d2_068'] = {'inputs': ['me_replacement_068'], 'func': me_replacement_d2_068}


def me_replacement_d2_069(me_replacement_069):
    feature = _clean(me_replacement_069)
    delta = feature.diff(89)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00069000).reindex(feature.index)
ME_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['me_replacement_d2_069'] = {'inputs': ['me_replacement_069'], 'func': me_replacement_d2_069}


def me_replacement_d2_070(me_replacement_070):
    feature = _clean(me_replacement_070)
    delta = feature.diff(1)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00070000).reindex(feature.index)
ME_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['me_replacement_d2_070'] = {'inputs': ['me_replacement_070'], 'func': me_replacement_d2_070}


def me_replacement_d2_071(me_replacement_071):
    feature = _clean(me_replacement_071)
    delta = feature.diff(2)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00071000).reindex(feature.index)
ME_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['me_replacement_d2_071'] = {'inputs': ['me_replacement_071'], 'func': me_replacement_d2_071}


def me_replacement_d2_072(me_replacement_072):
    feature = _clean(me_replacement_072)
    delta = feature.diff(3)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00072000).reindex(feature.index)
ME_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['me_replacement_d2_072'] = {'inputs': ['me_replacement_072'], 'func': me_replacement_d2_072}


def me_replacement_d2_073(me_replacement_073):
    feature = _clean(me_replacement_073)
    delta = feature.diff(5)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00073000).reindex(feature.index)
ME_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['me_replacement_d2_073'] = {'inputs': ['me_replacement_073'], 'func': me_replacement_d2_073}


def me_replacement_d2_074(me_replacement_074):
    feature = _clean(me_replacement_074)
    delta = feature.diff(8)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00074000).reindex(feature.index)
ME_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['me_replacement_d2_074'] = {'inputs': ['me_replacement_074'], 'func': me_replacement_d2_074}


def me_replacement_d2_075(me_replacement_075):
    feature = _clean(me_replacement_075)
    delta = feature.diff(13)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00075000).reindex(feature.index)
ME_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['me_replacement_d2_075'] = {'inputs': ['me_replacement_075'], 'func': me_replacement_d2_075}


def me_replacement_d2_076(me_replacement_076):
    feature = _clean(me_replacement_076)
    delta = feature.diff(21)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00076000).reindex(feature.index)
ME_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['me_replacement_d2_076'] = {'inputs': ['me_replacement_076'], 'func': me_replacement_d2_076}


def me_replacement_d2_077(me_replacement_077):
    feature = _clean(me_replacement_077)
    delta = feature.diff(34)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00077000).reindex(feature.index)
ME_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['me_replacement_d2_077'] = {'inputs': ['me_replacement_077'], 'func': me_replacement_d2_077}


def me_replacement_d2_078(me_replacement_078):
    feature = _clean(me_replacement_078)
    delta = feature.diff(55)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00078000).reindex(feature.index)
ME_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['me_replacement_d2_078'] = {'inputs': ['me_replacement_078'], 'func': me_replacement_d2_078}


def me_replacement_d2_079(me_replacement_079):
    feature = _clean(me_replacement_079)
    delta = feature.diff(89)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00079000).reindex(feature.index)
ME_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['me_replacement_d2_079'] = {'inputs': ['me_replacement_079'], 'func': me_replacement_d2_079}


def me_replacement_d2_080(me_replacement_080):
    feature = _clean(me_replacement_080)
    delta = feature.diff(1)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00080000).reindex(feature.index)
ME_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['me_replacement_d2_080'] = {'inputs': ['me_replacement_080'], 'func': me_replacement_d2_080}


def me_replacement_d2_081(me_replacement_081):
    feature = _clean(me_replacement_081)
    delta = feature.diff(2)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00081000).reindex(feature.index)
ME_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['me_replacement_d2_081'] = {'inputs': ['me_replacement_081'], 'func': me_replacement_d2_081}


def me_replacement_d2_082(me_replacement_082):
    feature = _clean(me_replacement_082)
    delta = feature.diff(3)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00082000).reindex(feature.index)
ME_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['me_replacement_d2_082'] = {'inputs': ['me_replacement_082'], 'func': me_replacement_d2_082}


def me_replacement_d2_083(me_replacement_083):
    feature = _clean(me_replacement_083)
    delta = feature.diff(5)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00083000).reindex(feature.index)
ME_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['me_replacement_d2_083'] = {'inputs': ['me_replacement_083'], 'func': me_replacement_d2_083}


def me_replacement_d2_084(me_replacement_084):
    feature = _clean(me_replacement_084)
    delta = feature.diff(8)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00084000).reindex(feature.index)
ME_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['me_replacement_d2_084'] = {'inputs': ['me_replacement_084'], 'func': me_replacement_d2_084}


def me_replacement_d2_085(me_replacement_085):
    feature = _clean(me_replacement_085)
    delta = feature.diff(13)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00085000).reindex(feature.index)
ME_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['me_replacement_d2_085'] = {'inputs': ['me_replacement_085'], 'func': me_replacement_d2_085}


def me_replacement_d2_086(me_replacement_086):
    feature = _clean(me_replacement_086)
    delta = feature.diff(21)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00086000).reindex(feature.index)
ME_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['me_replacement_d2_086'] = {'inputs': ['me_replacement_086'], 'func': me_replacement_d2_086}


def me_replacement_d2_087(me_replacement_087):
    feature = _clean(me_replacement_087)
    delta = feature.diff(34)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00087000).reindex(feature.index)
ME_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['me_replacement_d2_087'] = {'inputs': ['me_replacement_087'], 'func': me_replacement_d2_087}


def me_replacement_d2_088(me_replacement_088):
    feature = _clean(me_replacement_088)
    delta = feature.diff(55)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00088000).reindex(feature.index)
ME_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['me_replacement_d2_088'] = {'inputs': ['me_replacement_088'], 'func': me_replacement_d2_088}


def me_replacement_d2_089(me_replacement_089):
    feature = _clean(me_replacement_089)
    delta = feature.diff(89)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00089000).reindex(feature.index)
ME_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['me_replacement_d2_089'] = {'inputs': ['me_replacement_089'], 'func': me_replacement_d2_089}


def me_replacement_d2_090(me_replacement_090):
    feature = _clean(me_replacement_090)
    delta = feature.diff(1)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00090000).reindex(feature.index)
ME_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['me_replacement_d2_090'] = {'inputs': ['me_replacement_090'], 'func': me_replacement_d2_090}


def me_replacement_d2_091(me_replacement_091):
    feature = _clean(me_replacement_091)
    delta = feature.diff(2)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00091000).reindex(feature.index)
ME_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['me_replacement_d2_091'] = {'inputs': ['me_replacement_091'], 'func': me_replacement_d2_091}


def me_replacement_d2_092(me_replacement_092):
    feature = _clean(me_replacement_092)
    delta = feature.diff(3)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00092000).reindex(feature.index)
ME_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['me_replacement_d2_092'] = {'inputs': ['me_replacement_092'], 'func': me_replacement_d2_092}


def me_replacement_d2_093(me_replacement_093):
    feature = _clean(me_replacement_093)
    delta = feature.diff(5)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00093000).reindex(feature.index)
ME_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['me_replacement_d2_093'] = {'inputs': ['me_replacement_093'], 'func': me_replacement_d2_093}


def me_replacement_d2_094(me_replacement_094):
    feature = _clean(me_replacement_094)
    delta = feature.diff(8)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00094000).reindex(feature.index)
ME_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['me_replacement_d2_094'] = {'inputs': ['me_replacement_094'], 'func': me_replacement_d2_094}


def me_replacement_d2_095(me_replacement_095):
    feature = _clean(me_replacement_095)
    delta = feature.diff(13)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00095000).reindex(feature.index)
ME_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['me_replacement_d2_095'] = {'inputs': ['me_replacement_095'], 'func': me_replacement_d2_095}


def me_replacement_d2_096(me_replacement_096):
    feature = _clean(me_replacement_096)
    delta = feature.diff(21)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00096000).reindex(feature.index)
ME_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['me_replacement_d2_096'] = {'inputs': ['me_replacement_096'], 'func': me_replacement_d2_096}


def me_replacement_d2_097(me_replacement_097):
    feature = _clean(me_replacement_097)
    delta = feature.diff(34)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00097000).reindex(feature.index)
ME_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['me_replacement_d2_097'] = {'inputs': ['me_replacement_097'], 'func': me_replacement_d2_097}


def me_replacement_d2_098(me_replacement_098):
    feature = _clean(me_replacement_098)
    delta = feature.diff(55)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00098000).reindex(feature.index)
ME_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['me_replacement_d2_098'] = {'inputs': ['me_replacement_098'], 'func': me_replacement_d2_098}


def me_replacement_d2_099(me_replacement_099):
    feature = _clean(me_replacement_099)
    delta = feature.diff(89)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00099000).reindex(feature.index)
ME_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['me_replacement_d2_099'] = {'inputs': ['me_replacement_099'], 'func': me_replacement_d2_099}


def me_replacement_d2_100(me_replacement_100):
    feature = _clean(me_replacement_100)
    delta = feature.diff(1)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00100000).reindex(feature.index)
ME_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['me_replacement_d2_100'] = {'inputs': ['me_replacement_100'], 'func': me_replacement_d2_100}


def me_replacement_d2_101(me_replacement_101):
    feature = _clean(me_replacement_101)
    delta = feature.diff(2)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00101000).reindex(feature.index)
ME_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['me_replacement_d2_101'] = {'inputs': ['me_replacement_101'], 'func': me_replacement_d2_101}


def me_replacement_d2_102(me_replacement_102):
    feature = _clean(me_replacement_102)
    delta = feature.diff(3)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00102000).reindex(feature.index)
ME_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['me_replacement_d2_102'] = {'inputs': ['me_replacement_102'], 'func': me_replacement_d2_102}


def me_replacement_d2_103(me_replacement_103):
    feature = _clean(me_replacement_103)
    delta = feature.diff(5)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00103000).reindex(feature.index)
ME_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['me_replacement_d2_103'] = {'inputs': ['me_replacement_103'], 'func': me_replacement_d2_103}


def me_replacement_d2_104(me_replacement_104):
    feature = _clean(me_replacement_104)
    delta = feature.diff(8)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00104000).reindex(feature.index)
ME_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['me_replacement_d2_104'] = {'inputs': ['me_replacement_104'], 'func': me_replacement_d2_104}


def me_replacement_d2_105(me_replacement_105):
    feature = _clean(me_replacement_105)
    delta = feature.diff(13)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00105000).reindex(feature.index)
ME_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['me_replacement_d2_105'] = {'inputs': ['me_replacement_105'], 'func': me_replacement_d2_105}


def me_replacement_d2_106(me_replacement_106):
    feature = _clean(me_replacement_106)
    delta = feature.diff(21)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00106000).reindex(feature.index)
ME_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['me_replacement_d2_106'] = {'inputs': ['me_replacement_106'], 'func': me_replacement_d2_106}


def me_replacement_d2_107(me_replacement_107):
    feature = _clean(me_replacement_107)
    delta = feature.diff(34)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00107000).reindex(feature.index)
ME_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['me_replacement_d2_107'] = {'inputs': ['me_replacement_107'], 'func': me_replacement_d2_107}


def me_replacement_d2_108(me_replacement_108):
    feature = _clean(me_replacement_108)
    delta = feature.diff(55)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00108000).reindex(feature.index)
ME_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['me_replacement_d2_108'] = {'inputs': ['me_replacement_108'], 'func': me_replacement_d2_108}


def me_replacement_d2_109(me_replacement_109):
    feature = _clean(me_replacement_109)
    delta = feature.diff(89)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00109000).reindex(feature.index)
ME_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['me_replacement_d2_109'] = {'inputs': ['me_replacement_109'], 'func': me_replacement_d2_109}


def me_replacement_d2_110(me_replacement_110):
    feature = _clean(me_replacement_110)
    delta = feature.diff(1)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00110000).reindex(feature.index)
ME_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['me_replacement_d2_110'] = {'inputs': ['me_replacement_110'], 'func': me_replacement_d2_110}


def me_replacement_d2_111(me_replacement_111):
    feature = _clean(me_replacement_111)
    delta = feature.diff(2)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00111000).reindex(feature.index)
ME_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['me_replacement_d2_111'] = {'inputs': ['me_replacement_111'], 'func': me_replacement_d2_111}


def me_replacement_d2_112(me_replacement_112):
    feature = _clean(me_replacement_112)
    delta = feature.diff(3)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00112000).reindex(feature.index)
ME_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['me_replacement_d2_112'] = {'inputs': ['me_replacement_112'], 'func': me_replacement_d2_112}


def me_replacement_d2_113(me_replacement_113):
    feature = _clean(me_replacement_113)
    delta = feature.diff(5)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00113000).reindex(feature.index)
ME_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['me_replacement_d2_113'] = {'inputs': ['me_replacement_113'], 'func': me_replacement_d2_113}


def me_replacement_d2_114(me_replacement_114):
    feature = _clean(me_replacement_114)
    delta = feature.diff(8)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00114000).reindex(feature.index)
ME_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['me_replacement_d2_114'] = {'inputs': ['me_replacement_114'], 'func': me_replacement_d2_114}


def me_replacement_d2_115(me_replacement_115):
    feature = _clean(me_replacement_115)
    delta = feature.diff(13)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00115000).reindex(feature.index)
ME_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['me_replacement_d2_115'] = {'inputs': ['me_replacement_115'], 'func': me_replacement_d2_115}


def me_replacement_d2_116(me_replacement_116):
    feature = _clean(me_replacement_116)
    delta = feature.diff(21)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00116000).reindex(feature.index)
ME_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['me_replacement_d2_116'] = {'inputs': ['me_replacement_116'], 'func': me_replacement_d2_116}


def me_replacement_d2_117(me_replacement_117):
    feature = _clean(me_replacement_117)
    delta = feature.diff(34)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00117000).reindex(feature.index)
ME_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['me_replacement_d2_117'] = {'inputs': ['me_replacement_117'], 'func': me_replacement_d2_117}


def me_replacement_d2_118(me_replacement_118):
    feature = _clean(me_replacement_118)
    delta = feature.diff(55)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00118000).reindex(feature.index)
ME_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['me_replacement_d2_118'] = {'inputs': ['me_replacement_118'], 'func': me_replacement_d2_118}


def me_replacement_d2_119(me_replacement_119):
    feature = _clean(me_replacement_119)
    delta = feature.diff(89)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00119000).reindex(feature.index)
ME_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['me_replacement_d2_119'] = {'inputs': ['me_replacement_119'], 'func': me_replacement_d2_119}


def me_replacement_d2_120(me_replacement_120):
    feature = _clean(me_replacement_120)
    delta = feature.diff(1)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00120000).reindex(feature.index)
ME_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['me_replacement_d2_120'] = {'inputs': ['me_replacement_120'], 'func': me_replacement_d2_120}


def me_replacement_d2_121(me_replacement_121):
    feature = _clean(me_replacement_121)
    delta = feature.diff(2)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00121000).reindex(feature.index)
ME_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['me_replacement_d2_121'] = {'inputs': ['me_replacement_121'], 'func': me_replacement_d2_121}


def me_replacement_d2_122(me_replacement_122):
    feature = _clean(me_replacement_122)
    delta = feature.diff(3)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00122000).reindex(feature.index)
ME_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['me_replacement_d2_122'] = {'inputs': ['me_replacement_122'], 'func': me_replacement_d2_122}


def me_replacement_d2_123(me_replacement_123):
    feature = _clean(me_replacement_123)
    delta = feature.diff(5)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00123000).reindex(feature.index)
ME_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['me_replacement_d2_123'] = {'inputs': ['me_replacement_123'], 'func': me_replacement_d2_123}


def me_replacement_d2_124(me_replacement_124):
    feature = _clean(me_replacement_124)
    delta = feature.diff(8)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00124000).reindex(feature.index)
ME_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['me_replacement_d2_124'] = {'inputs': ['me_replacement_124'], 'func': me_replacement_d2_124}


def me_replacement_d2_125(me_replacement_125):
    feature = _clean(me_replacement_125)
    delta = feature.diff(13)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00125000).reindex(feature.index)
ME_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['me_replacement_d2_125'] = {'inputs': ['me_replacement_125'], 'func': me_replacement_d2_125}


def me_replacement_d2_126(me_replacement_126):
    feature = _clean(me_replacement_126)
    delta = feature.diff(21)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00126000).reindex(feature.index)
ME_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['me_replacement_d2_126'] = {'inputs': ['me_replacement_126'], 'func': me_replacement_d2_126}


def me_replacement_d2_127(me_replacement_127):
    feature = _clean(me_replacement_127)
    delta = feature.diff(34)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00127000).reindex(feature.index)
ME_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['me_replacement_d2_127'] = {'inputs': ['me_replacement_127'], 'func': me_replacement_d2_127}


def me_replacement_d2_128(me_replacement_128):
    feature = _clean(me_replacement_128)
    delta = feature.diff(55)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00128000).reindex(feature.index)
ME_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['me_replacement_d2_128'] = {'inputs': ['me_replacement_128'], 'func': me_replacement_d2_128}


def me_replacement_d2_129(me_replacement_129):
    feature = _clean(me_replacement_129)
    delta = feature.diff(89)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00129000).reindex(feature.index)
ME_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['me_replacement_d2_129'] = {'inputs': ['me_replacement_129'], 'func': me_replacement_d2_129}


def me_replacement_d2_130(me_replacement_130):
    feature = _clean(me_replacement_130)
    delta = feature.diff(1)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00130000).reindex(feature.index)
ME_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['me_replacement_d2_130'] = {'inputs': ['me_replacement_130'], 'func': me_replacement_d2_130}


def me_replacement_d2_131(me_replacement_131):
    feature = _clean(me_replacement_131)
    delta = feature.diff(2)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00131000).reindex(feature.index)
ME_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['me_replacement_d2_131'] = {'inputs': ['me_replacement_131'], 'func': me_replacement_d2_131}


def me_replacement_d2_132(me_replacement_132):
    feature = _clean(me_replacement_132)
    delta = feature.diff(3)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00132000).reindex(feature.index)
ME_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['me_replacement_d2_132'] = {'inputs': ['me_replacement_132'], 'func': me_replacement_d2_132}


def me_replacement_d2_133(me_replacement_133):
    feature = _clean(me_replacement_133)
    delta = feature.diff(5)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00133000).reindex(feature.index)
ME_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['me_replacement_d2_133'] = {'inputs': ['me_replacement_133'], 'func': me_replacement_d2_133}


def me_replacement_d2_134(me_replacement_134):
    feature = _clean(me_replacement_134)
    delta = feature.diff(8)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00134000).reindex(feature.index)
ME_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['me_replacement_d2_134'] = {'inputs': ['me_replacement_134'], 'func': me_replacement_d2_134}


def me_replacement_d2_135(me_replacement_135):
    feature = _clean(me_replacement_135)
    delta = feature.diff(13)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00135000).reindex(feature.index)
ME_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['me_replacement_d2_135'] = {'inputs': ['me_replacement_135'], 'func': me_replacement_d2_135}


def me_replacement_d2_136(me_replacement_136):
    feature = _clean(me_replacement_136)
    delta = feature.diff(21)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00136000).reindex(feature.index)
ME_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['me_replacement_d2_136'] = {'inputs': ['me_replacement_136'], 'func': me_replacement_d2_136}


def me_replacement_d2_137(me_replacement_137):
    feature = _clean(me_replacement_137)
    delta = feature.diff(34)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00137000).reindex(feature.index)
ME_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['me_replacement_d2_137'] = {'inputs': ['me_replacement_137'], 'func': me_replacement_d2_137}


def me_replacement_d2_138(me_replacement_138):
    feature = _clean(me_replacement_138)
    delta = feature.diff(55)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00138000).reindex(feature.index)
ME_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['me_replacement_d2_138'] = {'inputs': ['me_replacement_138'], 'func': me_replacement_d2_138}


def me_replacement_d2_139(me_replacement_139):
    feature = _clean(me_replacement_139)
    delta = feature.diff(89)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00139000).reindex(feature.index)
ME_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['me_replacement_d2_139'] = {'inputs': ['me_replacement_139'], 'func': me_replacement_d2_139}


def me_replacement_d2_140(me_replacement_140):
    feature = _clean(me_replacement_140)
    delta = feature.diff(1)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00140000).reindex(feature.index)
ME_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['me_replacement_d2_140'] = {'inputs': ['me_replacement_140'], 'func': me_replacement_d2_140}


def me_replacement_d2_141(me_replacement_141):
    feature = _clean(me_replacement_141)
    delta = feature.diff(2)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00141000).reindex(feature.index)
ME_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['me_replacement_d2_141'] = {'inputs': ['me_replacement_141'], 'func': me_replacement_d2_141}


def me_replacement_d2_142(me_replacement_142):
    feature = _clean(me_replacement_142)
    delta = feature.diff(3)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00142000).reindex(feature.index)
ME_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['me_replacement_d2_142'] = {'inputs': ['me_replacement_142'], 'func': me_replacement_d2_142}


def me_replacement_d2_143(me_replacement_143):
    feature = _clean(me_replacement_143)
    delta = feature.diff(5)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00143000).reindex(feature.index)
ME_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['me_replacement_d2_143'] = {'inputs': ['me_replacement_143'], 'func': me_replacement_d2_143}


def me_replacement_d2_144(me_replacement_144):
    feature = _clean(me_replacement_144)
    delta = feature.diff(8)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00144000).reindex(feature.index)
ME_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['me_replacement_d2_144'] = {'inputs': ['me_replacement_144'], 'func': me_replacement_d2_144}


def me_replacement_d2_145(me_replacement_145):
    feature = _clean(me_replacement_145)
    delta = feature.diff(13)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00145000).reindex(feature.index)
ME_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['me_replacement_d2_145'] = {'inputs': ['me_replacement_145'], 'func': me_replacement_d2_145}


def me_replacement_d2_146(me_replacement_146):
    feature = _clean(me_replacement_146)
    delta = feature.diff(21)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00146000).reindex(feature.index)
ME_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['me_replacement_d2_146'] = {'inputs': ['me_replacement_146'], 'func': me_replacement_d2_146}


def me_replacement_d2_147(me_replacement_147):
    feature = _clean(me_replacement_147)
    delta = feature.diff(34)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00147000).reindex(feature.index)
ME_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['me_replacement_d2_147'] = {'inputs': ['me_replacement_147'], 'func': me_replacement_d2_147}


def me_replacement_d2_148(me_replacement_148):
    feature = _clean(me_replacement_148)
    delta = feature.diff(55)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00148000).reindex(feature.index)
ME_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['me_replacement_d2_148'] = {'inputs': ['me_replacement_148'], 'func': me_replacement_d2_148}


def me_replacement_d2_149(me_replacement_149):
    feature = _clean(me_replacement_149)
    delta = feature.diff(89)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00149000).reindex(feature.index)
ME_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['me_replacement_d2_149'] = {'inputs': ['me_replacement_149'], 'func': me_replacement_d2_149}


def me_replacement_d2_150(me_replacement_150):
    feature = _clean(me_replacement_150)
    delta = feature.diff(1)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00150000).reindex(feature.index)
ME_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['me_replacement_d2_150'] = {'inputs': ['me_replacement_150'], 'func': me_replacement_d2_150}


def me_replacement_d2_151(me_replacement_151):
    feature = _clean(me_replacement_151)
    delta = feature.diff(2)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00151000).reindex(feature.index)
ME_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['me_replacement_d2_151'] = {'inputs': ['me_replacement_151'], 'func': me_replacement_d2_151}


def me_replacement_d2_152(me_replacement_152):
    feature = _clean(me_replacement_152)
    delta = feature.diff(3)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00152000).reindex(feature.index)
ME_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['me_replacement_d2_152'] = {'inputs': ['me_replacement_152'], 'func': me_replacement_d2_152}


def me_replacement_d2_153(me_replacement_153):
    feature = _clean(me_replacement_153)
    delta = feature.diff(5)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00153000).reindex(feature.index)
ME_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['me_replacement_d2_153'] = {'inputs': ['me_replacement_153'], 'func': me_replacement_d2_153}


def me_replacement_d2_154(me_replacement_154):
    feature = _clean(me_replacement_154)
    delta = feature.diff(8)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00154000).reindex(feature.index)
ME_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['me_replacement_d2_154'] = {'inputs': ['me_replacement_154'], 'func': me_replacement_d2_154}


def me_replacement_d2_155(me_replacement_155):
    feature = _clean(me_replacement_155)
    delta = feature.diff(13)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00155000).reindex(feature.index)
ME_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['me_replacement_d2_155'] = {'inputs': ['me_replacement_155'], 'func': me_replacement_d2_155}


def me_replacement_d2_156(me_replacement_156):
    feature = _clean(me_replacement_156)
    delta = feature.diff(21)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00156000).reindex(feature.index)
ME_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['me_replacement_d2_156'] = {'inputs': ['me_replacement_156'], 'func': me_replacement_d2_156}


def me_replacement_d2_157(me_replacement_157):
    feature = _clean(me_replacement_157)
    delta = feature.diff(34)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00157000).reindex(feature.index)
ME_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['me_replacement_d2_157'] = {'inputs': ['me_replacement_157'], 'func': me_replacement_d2_157}


def me_replacement_d2_158(me_replacement_158):
    feature = _clean(me_replacement_158)
    delta = feature.diff(55)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00158000).reindex(feature.index)
ME_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['me_replacement_d2_158'] = {'inputs': ['me_replacement_158'], 'func': me_replacement_d2_158}


def me_replacement_d2_159(me_replacement_159):
    feature = _clean(me_replacement_159)
    delta = feature.diff(89)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00159000).reindex(feature.index)
ME_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['me_replacement_d2_159'] = {'inputs': ['me_replacement_159'], 'func': me_replacement_d2_159}


def me_replacement_d2_160(me_replacement_160):
    feature = _clean(me_replacement_160)
    delta = feature.diff(1)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00160000).reindex(feature.index)
ME_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['me_replacement_d2_160'] = {'inputs': ['me_replacement_160'], 'func': me_replacement_d2_160}


def me_replacement_d2_161(me_replacement_161):
    feature = _clean(me_replacement_161)
    delta = feature.diff(2)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00161000).reindex(feature.index)
ME_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['me_replacement_d2_161'] = {'inputs': ['me_replacement_161'], 'func': me_replacement_d2_161}


def me_replacement_d2_162(me_replacement_162):
    feature = _clean(me_replacement_162)
    delta = feature.diff(3)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00162000).reindex(feature.index)
ME_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['me_replacement_d2_162'] = {'inputs': ['me_replacement_162'], 'func': me_replacement_d2_162}


def me_replacement_d2_163(me_replacement_163):
    feature = _clean(me_replacement_163)
    delta = feature.diff(5)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00163000).reindex(feature.index)
ME_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['me_replacement_d2_163'] = {'inputs': ['me_replacement_163'], 'func': me_replacement_d2_163}


def me_replacement_d2_164(me_replacement_164):
    feature = _clean(me_replacement_164)
    delta = feature.diff(8)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00164000).reindex(feature.index)
ME_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['me_replacement_d2_164'] = {'inputs': ['me_replacement_164'], 'func': me_replacement_d2_164}


def me_replacement_d2_165(me_replacement_165):
    feature = _clean(me_replacement_165)
    delta = feature.diff(13)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00165000).reindex(feature.index)
ME_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['me_replacement_d2_165'] = {'inputs': ['me_replacement_165'], 'func': me_replacement_d2_165}


def me_replacement_d2_166(me_replacement_166):
    feature = _clean(me_replacement_166)
    delta = feature.diff(21)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00166000).reindex(feature.index)
ME_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['me_replacement_d2_166'] = {'inputs': ['me_replacement_166'], 'func': me_replacement_d2_166}


def me_replacement_d2_167(me_replacement_167):
    feature = _clean(me_replacement_167)
    delta = feature.diff(34)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00167000).reindex(feature.index)
ME_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['me_replacement_d2_167'] = {'inputs': ['me_replacement_167'], 'func': me_replacement_d2_167}


def me_replacement_d2_168(me_replacement_168):
    feature = _clean(me_replacement_168)
    delta = feature.diff(55)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00168000).reindex(feature.index)
ME_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['me_replacement_d2_168'] = {'inputs': ['me_replacement_168'], 'func': me_replacement_d2_168}


def me_replacement_d2_169(me_replacement_169):
    feature = _clean(me_replacement_169)
    delta = feature.diff(89)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00169000).reindex(feature.index)
ME_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['me_replacement_d2_169'] = {'inputs': ['me_replacement_169'], 'func': me_replacement_d2_169}


def me_replacement_d2_170(me_replacement_170):
    feature = _clean(me_replacement_170)
    delta = feature.diff(1)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00170000).reindex(feature.index)
ME_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['me_replacement_d2_170'] = {'inputs': ['me_replacement_170'], 'func': me_replacement_d2_170}


def me_replacement_d2_171(me_replacement_171):
    feature = _clean(me_replacement_171)
    delta = feature.diff(2)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00171000).reindex(feature.index)
ME_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['me_replacement_d2_171'] = {'inputs': ['me_replacement_171'], 'func': me_replacement_d2_171}


def me_replacement_d2_172(me_replacement_172):
    feature = _clean(me_replacement_172)
    delta = feature.diff(3)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00172000).reindex(feature.index)
ME_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['me_replacement_d2_172'] = {'inputs': ['me_replacement_172'], 'func': me_replacement_d2_172}


def me_replacement_d2_173(me_replacement_173):
    feature = _clean(me_replacement_173)
    delta = feature.diff(5)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00173000).reindex(feature.index)
ME_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['me_replacement_d2_173'] = {'inputs': ['me_replacement_173'], 'func': me_replacement_d2_173}


def me_replacement_d2_174(me_replacement_174):
    feature = _clean(me_replacement_174)
    delta = feature.diff(8)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00174000).reindex(feature.index)
ME_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['me_replacement_d2_174'] = {'inputs': ['me_replacement_174'], 'func': me_replacement_d2_174}


def me_replacement_d2_175(me_replacement_175):
    feature = _clean(me_replacement_175)
    delta = feature.diff(13)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00175000).reindex(feature.index)
ME_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['me_replacement_d2_175'] = {'inputs': ['me_replacement_175'], 'func': me_replacement_d2_175}


# Base-universe derivative extensions for repaired first-base features.
MEX_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY = {}


def _base_universe_d2(feature, idx):
    feature = _clean(feature) if '_clean' in globals() else _s(feature).replace([np.inf, -np.inf], np.nan)
    windows = [1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    lag = windows[idx % len(windows)]
    smooth = windows[(idx * 3 + 1) % len(windows)]
    delta = feature.diff(lag)
    local = feature - feature.rolling(max(3, smooth), min_periods=2).mean()
    out = delta + local.fillna(0.0) * (0.00037 * ((idx % 17) + 1))
    return out.replace([np.inf, -np.inf], np.nan).reindex(feature.index)


def mex_base_universe_d2_001_mex_003_loss_streak_21_003(mex_003_loss_streak_21_003):
    return _base_universe_d2(mex_003_loss_streak_21_003, 1)
MEX_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['mex_base_universe_d2_001_mex_003_loss_streak_21_003'] = {'inputs': ['mex_003_loss_streak_21_003'], 'func': mex_base_universe_d2_001_mex_003_loss_streak_21_003}


def mex_base_universe_d2_002_mex_004_ma_distance_42_004(mex_004_ma_distance_42_004):
    return _base_universe_d2(mex_004_ma_distance_42_004, 2)
MEX_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['mex_base_universe_d2_002_mex_004_ma_distance_42_004'] = {'inputs': ['mex_004_ma_distance_42_004'], 'func': mex_base_universe_d2_002_mex_004_ma_distance_42_004}


def mex_base_universe_d2_003_mex_005_stochastic_position_63_005(mex_005_stochastic_position_63_005):
    return _base_universe_d2(mex_005_stochastic_position_63_005, 3)
MEX_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['mex_base_universe_d2_003_mex_005_stochastic_position_63_005'] = {'inputs': ['mex_005_stochastic_position_63_005'], 'func': mex_base_universe_d2_003_mex_005_stochastic_position_63_005}


def mex_base_universe_d2_004_mex_009_loss_streak_252_009(mex_009_loss_streak_252_009):
    return _base_universe_d2(mex_009_loss_streak_252_009, 4)
MEX_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['mex_base_universe_d2_004_mex_009_loss_streak_252_009'] = {'inputs': ['mex_009_loss_streak_252_009'], 'func': mex_base_universe_d2_004_mex_009_loss_streak_252_009}


def mex_base_universe_d2_005_mex_010_ma_distance_378_010(mex_010_ma_distance_378_010):
    return _base_universe_d2(mex_010_ma_distance_378_010, 5)
MEX_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['mex_base_universe_d2_005_mex_010_ma_distance_378_010'] = {'inputs': ['mex_010_ma_distance_378_010'], 'func': mex_base_universe_d2_005_mex_010_ma_distance_378_010}


def mex_base_universe_d2_006_mex_011_stochastic_position_504_011(mex_011_stochastic_position_504_011):
    return _base_universe_d2(mex_011_stochastic_position_504_011, 6)
MEX_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['mex_base_universe_d2_006_mex_011_stochastic_position_504_011'] = {'inputs': ['mex_011_stochastic_position_504_011'], 'func': mex_base_universe_d2_006_mex_011_stochastic_position_504_011}


def mex_base_universe_d2_007_mex_015_loss_streak_1512_015(mex_015_loss_streak_1512_015):
    return _base_universe_d2(mex_015_loss_streak_1512_015, 7)
MEX_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['mex_base_universe_d2_007_mex_015_loss_streak_1512_015'] = {'inputs': ['mex_015_loss_streak_1512_015'], 'func': mex_base_universe_d2_007_mex_015_loss_streak_1512_015}


def mex_base_universe_d2_008_mex_016_ma_distance_5_016(mex_016_ma_distance_5_016):
    return _base_universe_d2(mex_016_ma_distance_5_016, 8)
MEX_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['mex_base_universe_d2_008_mex_016_ma_distance_5_016'] = {'inputs': ['mex_016_ma_distance_5_016'], 'func': mex_base_universe_d2_008_mex_016_ma_distance_5_016}


def mex_base_universe_d2_009_mex_017_stochastic_position_10_017(mex_017_stochastic_position_10_017):
    return _base_universe_d2(mex_017_stochastic_position_10_017, 9)
MEX_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['mex_base_universe_d2_009_mex_017_stochastic_position_10_017'] = {'inputs': ['mex_017_stochastic_position_10_017'], 'func': mex_base_universe_d2_009_mex_017_stochastic_position_10_017}


def mex_base_universe_d2_010_mex_021_loss_streak_84_021(mex_021_loss_streak_84_021):
    return _base_universe_d2(mex_021_loss_streak_84_021, 10)
MEX_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['mex_base_universe_d2_010_mex_021_loss_streak_84_021'] = {'inputs': ['mex_021_loss_streak_84_021'], 'func': mex_base_universe_d2_010_mex_021_loss_streak_84_021}


def mex_base_universe_d2_011_mex_022_ma_distance_126_022(mex_022_ma_distance_126_022):
    return _base_universe_d2(mex_022_ma_distance_126_022, 11)
MEX_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['mex_base_universe_d2_011_mex_022_ma_distance_126_022'] = {'inputs': ['mex_022_ma_distance_126_022'], 'func': mex_base_universe_d2_011_mex_022_ma_distance_126_022}


def mex_base_universe_d2_012_mex_023_stochastic_position_189_023(mex_023_stochastic_position_189_023):
    return _base_universe_d2(mex_023_stochastic_position_189_023, 12)
MEX_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['mex_base_universe_d2_012_mex_023_stochastic_position_189_023'] = {'inputs': ['mex_023_stochastic_position_189_023'], 'func': mex_base_universe_d2_012_mex_023_stochastic_position_189_023}


def mex_base_universe_d2_013_mex_027_loss_streak_756_027(mex_027_loss_streak_756_027):
    return _base_universe_d2(mex_027_loss_streak_756_027, 13)
MEX_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['mex_base_universe_d2_013_mex_027_loss_streak_756_027'] = {'inputs': ['mex_027_loss_streak_756_027'], 'func': mex_base_universe_d2_013_mex_027_loss_streak_756_027}


def mex_base_universe_d2_014_mex_028_ma_distance_1008_028(mex_028_ma_distance_1008_028):
    return _base_universe_d2(mex_028_ma_distance_1008_028, 14)
MEX_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['mex_base_universe_d2_014_mex_028_ma_distance_1008_028'] = {'inputs': ['mex_028_ma_distance_1008_028'], 'func': mex_base_universe_d2_014_mex_028_ma_distance_1008_028}


def mex_base_universe_d2_015_mex_029_stochastic_position_1260_029(mex_029_stochastic_position_1260_029):
    return _base_universe_d2(mex_029_stochastic_position_1260_029, 15)
MEX_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['mex_base_universe_d2_015_mex_029_stochastic_position_1260_029'] = {'inputs': ['mex_029_stochastic_position_1260_029'], 'func': mex_base_universe_d2_015_mex_029_stochastic_position_1260_029}


def mex_base_universe_d2_016_mex_basefill_001(mex_basefill_001):
    return _base_universe_d2(mex_basefill_001, 16)
MEX_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['mex_base_universe_d2_016_mex_basefill_001'] = {'inputs': ['mex_basefill_001'], 'func': mex_base_universe_d2_016_mex_basefill_001}


def mex_base_universe_d2_017_mex_basefill_002(mex_basefill_002):
    return _base_universe_d2(mex_basefill_002, 17)
MEX_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['mex_base_universe_d2_017_mex_basefill_002'] = {'inputs': ['mex_basefill_002'], 'func': mex_base_universe_d2_017_mex_basefill_002}


def mex_base_universe_d2_018_mex_basefill_006(mex_basefill_006):
    return _base_universe_d2(mex_basefill_006, 18)
MEX_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['mex_base_universe_d2_018_mex_basefill_006'] = {'inputs': ['mex_basefill_006'], 'func': mex_base_universe_d2_018_mex_basefill_006}


def mex_base_universe_d2_019_mex_basefill_007(mex_basefill_007):
    return _base_universe_d2(mex_basefill_007, 19)
MEX_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['mex_base_universe_d2_019_mex_basefill_007'] = {'inputs': ['mex_basefill_007'], 'func': mex_base_universe_d2_019_mex_basefill_007}


def mex_base_universe_d2_020_mex_basefill_008(mex_basefill_008):
    return _base_universe_d2(mex_basefill_008, 20)
MEX_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['mex_base_universe_d2_020_mex_basefill_008'] = {'inputs': ['mex_basefill_008'], 'func': mex_base_universe_d2_020_mex_basefill_008}


def mex_base_universe_d2_021_mex_basefill_012(mex_basefill_012):
    return _base_universe_d2(mex_basefill_012, 21)
MEX_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['mex_base_universe_d2_021_mex_basefill_012'] = {'inputs': ['mex_basefill_012'], 'func': mex_base_universe_d2_021_mex_basefill_012}


def mex_base_universe_d2_022_mex_basefill_013(mex_basefill_013):
    return _base_universe_d2(mex_basefill_013, 22)
MEX_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['mex_base_universe_d2_022_mex_basefill_013'] = {'inputs': ['mex_basefill_013'], 'func': mex_base_universe_d2_022_mex_basefill_013}


def mex_base_universe_d2_023_mex_basefill_014(mex_basefill_014):
    return _base_universe_d2(mex_basefill_014, 23)
MEX_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['mex_base_universe_d2_023_mex_basefill_014'] = {'inputs': ['mex_basefill_014'], 'func': mex_base_universe_d2_023_mex_basefill_014}


def mex_base_universe_d2_024_mex_basefill_018(mex_basefill_018):
    return _base_universe_d2(mex_basefill_018, 24)
MEX_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['mex_base_universe_d2_024_mex_basefill_018'] = {'inputs': ['mex_basefill_018'], 'func': mex_base_universe_d2_024_mex_basefill_018}


def mex_base_universe_d2_025_mex_basefill_019(mex_basefill_019):
    return _base_universe_d2(mex_basefill_019, 25)
MEX_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['mex_base_universe_d2_025_mex_basefill_019'] = {'inputs': ['mex_basefill_019'], 'func': mex_base_universe_d2_025_mex_basefill_019}


def mex_base_universe_d2_026_mex_basefill_020(mex_basefill_020):
    return _base_universe_d2(mex_basefill_020, 26)
MEX_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['mex_base_universe_d2_026_mex_basefill_020'] = {'inputs': ['mex_basefill_020'], 'func': mex_base_universe_d2_026_mex_basefill_020}


def mex_base_universe_d2_027_mex_basefill_024(mex_basefill_024):
    return _base_universe_d2(mex_basefill_024, 27)
MEX_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['mex_base_universe_d2_027_mex_basefill_024'] = {'inputs': ['mex_basefill_024'], 'func': mex_base_universe_d2_027_mex_basefill_024}


def mex_base_universe_d2_028_mex_basefill_025(mex_basefill_025):
    return _base_universe_d2(mex_basefill_025, 28)
MEX_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['mex_base_universe_d2_028_mex_basefill_025'] = {'inputs': ['mex_basefill_025'], 'func': mex_base_universe_d2_028_mex_basefill_025}


def mex_base_universe_d2_029_mex_basefill_026(mex_basefill_026):
    return _base_universe_d2(mex_basefill_026, 29)
MEX_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['mex_base_universe_d2_029_mex_basefill_026'] = {'inputs': ['mex_basefill_026'], 'func': mex_base_universe_d2_029_mex_basefill_026}


def mex_base_universe_d2_030_mex_basefill_030(mex_basefill_030):
    return _base_universe_d2(mex_basefill_030, 30)
MEX_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['mex_base_universe_d2_030_mex_basefill_030'] = {'inputs': ['mex_basefill_030'], 'func': mex_base_universe_d2_030_mex_basefill_030}


def mex_base_universe_d2_031_mex_basefill_031(mex_basefill_031):
    return _base_universe_d2(mex_basefill_031, 31)
MEX_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['mex_base_universe_d2_031_mex_basefill_031'] = {'inputs': ['mex_basefill_031'], 'func': mex_base_universe_d2_031_mex_basefill_031}


def mex_base_universe_d2_032_mex_basefill_032(mex_basefill_032):
    return _base_universe_d2(mex_basefill_032, 32)
MEX_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['mex_base_universe_d2_032_mex_basefill_032'] = {'inputs': ['mex_basefill_032'], 'func': mex_base_universe_d2_032_mex_basefill_032}


def mex_base_universe_d2_033_mex_basefill_033(mex_basefill_033):
    return _base_universe_d2(mex_basefill_033, 33)
MEX_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['mex_base_universe_d2_033_mex_basefill_033'] = {'inputs': ['mex_basefill_033'], 'func': mex_base_universe_d2_033_mex_basefill_033}


def mex_base_universe_d2_034_mex_basefill_034(mex_basefill_034):
    return _base_universe_d2(mex_basefill_034, 34)
MEX_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['mex_base_universe_d2_034_mex_basefill_034'] = {'inputs': ['mex_basefill_034'], 'func': mex_base_universe_d2_034_mex_basefill_034}


def mex_base_universe_d2_035_mex_basefill_035(mex_basefill_035):
    return _base_universe_d2(mex_basefill_035, 35)
MEX_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['mex_base_universe_d2_035_mex_basefill_035'] = {'inputs': ['mex_basefill_035'], 'func': mex_base_universe_d2_035_mex_basefill_035}


def mex_base_universe_d2_036_mex_basefill_036(mex_basefill_036):
    return _base_universe_d2(mex_basefill_036, 36)
MEX_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['mex_base_universe_d2_036_mex_basefill_036'] = {'inputs': ['mex_basefill_036'], 'func': mex_base_universe_d2_036_mex_basefill_036}


def mex_base_universe_d2_037_mex_basefill_037(mex_basefill_037):
    return _base_universe_d2(mex_basefill_037, 37)
MEX_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['mex_base_universe_d2_037_mex_basefill_037'] = {'inputs': ['mex_basefill_037'], 'func': mex_base_universe_d2_037_mex_basefill_037}


def mex_base_universe_d2_038_mex_basefill_038(mex_basefill_038):
    return _base_universe_d2(mex_basefill_038, 38)
MEX_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['mex_base_universe_d2_038_mex_basefill_038'] = {'inputs': ['mex_basefill_038'], 'func': mex_base_universe_d2_038_mex_basefill_038}


def mex_base_universe_d2_039_mex_basefill_039(mex_basefill_039):
    return _base_universe_d2(mex_basefill_039, 39)
MEX_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['mex_base_universe_d2_039_mex_basefill_039'] = {'inputs': ['mex_basefill_039'], 'func': mex_base_universe_d2_039_mex_basefill_039}


def mex_base_universe_d2_040_mex_basefill_040(mex_basefill_040):
    return _base_universe_d2(mex_basefill_040, 40)
MEX_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['mex_base_universe_d2_040_mex_basefill_040'] = {'inputs': ['mex_basefill_040'], 'func': mex_base_universe_d2_040_mex_basefill_040}


def mex_base_universe_d2_041_mex_basefill_041(mex_basefill_041):
    return _base_universe_d2(mex_basefill_041, 41)
MEX_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['mex_base_universe_d2_041_mex_basefill_041'] = {'inputs': ['mex_basefill_041'], 'func': mex_base_universe_d2_041_mex_basefill_041}


def mex_base_universe_d2_042_mex_basefill_042(mex_basefill_042):
    return _base_universe_d2(mex_basefill_042, 42)
MEX_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['mex_base_universe_d2_042_mex_basefill_042'] = {'inputs': ['mex_basefill_042'], 'func': mex_base_universe_d2_042_mex_basefill_042}


def mex_base_universe_d2_043_mex_basefill_043(mex_basefill_043):
    return _base_universe_d2(mex_basefill_043, 43)
MEX_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['mex_base_universe_d2_043_mex_basefill_043'] = {'inputs': ['mex_basefill_043'], 'func': mex_base_universe_d2_043_mex_basefill_043}


def mex_base_universe_d2_044_mex_basefill_044(mex_basefill_044):
    return _base_universe_d2(mex_basefill_044, 44)
MEX_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['mex_base_universe_d2_044_mex_basefill_044'] = {'inputs': ['mex_basefill_044'], 'func': mex_base_universe_d2_044_mex_basefill_044}


def mex_base_universe_d2_045_mex_basefill_045(mex_basefill_045):
    return _base_universe_d2(mex_basefill_045, 45)
MEX_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['mex_base_universe_d2_045_mex_basefill_045'] = {'inputs': ['mex_basefill_045'], 'func': mex_base_universe_d2_045_mex_basefill_045}


def mex_base_universe_d2_046_mex_basefill_046(mex_basefill_046):
    return _base_universe_d2(mex_basefill_046, 46)
MEX_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['mex_base_universe_d2_046_mex_basefill_046'] = {'inputs': ['mex_basefill_046'], 'func': mex_base_universe_d2_046_mex_basefill_046}


def mex_base_universe_d2_047_mex_basefill_047(mex_basefill_047):
    return _base_universe_d2(mex_basefill_047, 47)
MEX_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['mex_base_universe_d2_047_mex_basefill_047'] = {'inputs': ['mex_basefill_047'], 'func': mex_base_universe_d2_047_mex_basefill_047}


def mex_base_universe_d2_048_mex_basefill_048(mex_basefill_048):
    return _base_universe_d2(mex_basefill_048, 48)
MEX_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['mex_base_universe_d2_048_mex_basefill_048'] = {'inputs': ['mex_basefill_048'], 'func': mex_base_universe_d2_048_mex_basefill_048}


def mex_base_universe_d2_049_mex_basefill_049(mex_basefill_049):
    return _base_universe_d2(mex_basefill_049, 49)
MEX_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['mex_base_universe_d2_049_mex_basefill_049'] = {'inputs': ['mex_basefill_049'], 'func': mex_base_universe_d2_049_mex_basefill_049}


def mex_base_universe_d2_050_mex_basefill_050(mex_basefill_050):
    return _base_universe_d2(mex_basefill_050, 50)
MEX_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['mex_base_universe_d2_050_mex_basefill_050'] = {'inputs': ['mex_basefill_050'], 'func': mex_base_universe_d2_050_mex_basefill_050}


def mex_base_universe_d2_051_mex_basefill_051(mex_basefill_051):
    return _base_universe_d2(mex_basefill_051, 51)
MEX_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['mex_base_universe_d2_051_mex_basefill_051'] = {'inputs': ['mex_basefill_051'], 'func': mex_base_universe_d2_051_mex_basefill_051}


def mex_base_universe_d2_052_mex_basefill_052(mex_basefill_052):
    return _base_universe_d2(mex_basefill_052, 52)
MEX_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['mex_base_universe_d2_052_mex_basefill_052'] = {'inputs': ['mex_basefill_052'], 'func': mex_base_universe_d2_052_mex_basefill_052}


def mex_base_universe_d2_053_mex_basefill_053(mex_basefill_053):
    return _base_universe_d2(mex_basefill_053, 53)
MEX_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['mex_base_universe_d2_053_mex_basefill_053'] = {'inputs': ['mex_basefill_053'], 'func': mex_base_universe_d2_053_mex_basefill_053}


def mex_base_universe_d2_054_mex_basefill_054(mex_basefill_054):
    return _base_universe_d2(mex_basefill_054, 54)
MEX_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['mex_base_universe_d2_054_mex_basefill_054'] = {'inputs': ['mex_basefill_054'], 'func': mex_base_universe_d2_054_mex_basefill_054}


def mex_base_universe_d2_055_mex_basefill_055(mex_basefill_055):
    return _base_universe_d2(mex_basefill_055, 55)
MEX_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['mex_base_universe_d2_055_mex_basefill_055'] = {'inputs': ['mex_basefill_055'], 'func': mex_base_universe_d2_055_mex_basefill_055}


def mex_base_universe_d2_056_mex_basefill_056(mex_basefill_056):
    return _base_universe_d2(mex_basefill_056, 56)
MEX_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['mex_base_universe_d2_056_mex_basefill_056'] = {'inputs': ['mex_basefill_056'], 'func': mex_base_universe_d2_056_mex_basefill_056}


def mex_base_universe_d2_057_mex_basefill_057(mex_basefill_057):
    return _base_universe_d2(mex_basefill_057, 57)
MEX_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['mex_base_universe_d2_057_mex_basefill_057'] = {'inputs': ['mex_basefill_057'], 'func': mex_base_universe_d2_057_mex_basefill_057}


def mex_base_universe_d2_058_mex_basefill_058(mex_basefill_058):
    return _base_universe_d2(mex_basefill_058, 58)
MEX_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['mex_base_universe_d2_058_mex_basefill_058'] = {'inputs': ['mex_basefill_058'], 'func': mex_base_universe_d2_058_mex_basefill_058}


def mex_base_universe_d2_059_mex_basefill_059(mex_basefill_059):
    return _base_universe_d2(mex_basefill_059, 59)
MEX_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['mex_base_universe_d2_059_mex_basefill_059'] = {'inputs': ['mex_basefill_059'], 'func': mex_base_universe_d2_059_mex_basefill_059}


def mex_base_universe_d2_060_mex_basefill_060(mex_basefill_060):
    return _base_universe_d2(mex_basefill_060, 60)
MEX_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['mex_base_universe_d2_060_mex_basefill_060'] = {'inputs': ['mex_basefill_060'], 'func': mex_base_universe_d2_060_mex_basefill_060}


def mex_base_universe_d2_061_mex_basefill_061(mex_basefill_061):
    return _base_universe_d2(mex_basefill_061, 61)
MEX_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['mex_base_universe_d2_061_mex_basefill_061'] = {'inputs': ['mex_basefill_061'], 'func': mex_base_universe_d2_061_mex_basefill_061}


def mex_base_universe_d2_062_mex_basefill_062(mex_basefill_062):
    return _base_universe_d2(mex_basefill_062, 62)
MEX_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['mex_base_universe_d2_062_mex_basefill_062'] = {'inputs': ['mex_basefill_062'], 'func': mex_base_universe_d2_062_mex_basefill_062}


def mex_base_universe_d2_063_mex_basefill_063(mex_basefill_063):
    return _base_universe_d2(mex_basefill_063, 63)
MEX_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['mex_base_universe_d2_063_mex_basefill_063'] = {'inputs': ['mex_basefill_063'], 'func': mex_base_universe_d2_063_mex_basefill_063}


def mex_base_universe_d2_064_mex_basefill_064(mex_basefill_064):
    return _base_universe_d2(mex_basefill_064, 64)
MEX_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['mex_base_universe_d2_064_mex_basefill_064'] = {'inputs': ['mex_basefill_064'], 'func': mex_base_universe_d2_064_mex_basefill_064}


def mex_base_universe_d2_065_mex_basefill_065(mex_basefill_065):
    return _base_universe_d2(mex_basefill_065, 65)
MEX_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['mex_base_universe_d2_065_mex_basefill_065'] = {'inputs': ['mex_basefill_065'], 'func': mex_base_universe_d2_065_mex_basefill_065}


def mex_base_universe_d2_066_mex_basefill_066(mex_basefill_066):
    return _base_universe_d2(mex_basefill_066, 66)
MEX_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['mex_base_universe_d2_066_mex_basefill_066'] = {'inputs': ['mex_basefill_066'], 'func': mex_base_universe_d2_066_mex_basefill_066}


def mex_base_universe_d2_067_mex_basefill_067(mex_basefill_067):
    return _base_universe_d2(mex_basefill_067, 67)
MEX_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['mex_base_universe_d2_067_mex_basefill_067'] = {'inputs': ['mex_basefill_067'], 'func': mex_base_universe_d2_067_mex_basefill_067}


def mex_base_universe_d2_068_mex_basefill_068(mex_basefill_068):
    return _base_universe_d2(mex_basefill_068, 68)
MEX_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['mex_base_universe_d2_068_mex_basefill_068'] = {'inputs': ['mex_basefill_068'], 'func': mex_base_universe_d2_068_mex_basefill_068}


def mex_base_universe_d2_069_mex_basefill_069(mex_basefill_069):
    return _base_universe_d2(mex_basefill_069, 69)
MEX_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['mex_base_universe_d2_069_mex_basefill_069'] = {'inputs': ['mex_basefill_069'], 'func': mex_base_universe_d2_069_mex_basefill_069}


def mex_base_universe_d2_070_mex_basefill_070(mex_basefill_070):
    return _base_universe_d2(mex_basefill_070, 70)
MEX_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['mex_base_universe_d2_070_mex_basefill_070'] = {'inputs': ['mex_basefill_070'], 'func': mex_base_universe_d2_070_mex_basefill_070}


def mex_base_universe_d2_071_mex_basefill_071(mex_basefill_071):
    return _base_universe_d2(mex_basefill_071, 71)
MEX_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['mex_base_universe_d2_071_mex_basefill_071'] = {'inputs': ['mex_basefill_071'], 'func': mex_base_universe_d2_071_mex_basefill_071}


def mex_base_universe_d2_072_mex_basefill_072(mex_basefill_072):
    return _base_universe_d2(mex_basefill_072, 72)
MEX_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['mex_base_universe_d2_072_mex_basefill_072'] = {'inputs': ['mex_basefill_072'], 'func': mex_base_universe_d2_072_mex_basefill_072}


def mex_base_universe_d2_073_mex_basefill_073(mex_basefill_073):
    return _base_universe_d2(mex_basefill_073, 73)
MEX_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['mex_base_universe_d2_073_mex_basefill_073'] = {'inputs': ['mex_basefill_073'], 'func': mex_base_universe_d2_073_mex_basefill_073}


def mex_base_universe_d2_074_mex_basefill_074(mex_basefill_074):
    return _base_universe_d2(mex_basefill_074, 74)
MEX_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['mex_base_universe_d2_074_mex_basefill_074'] = {'inputs': ['mex_basefill_074'], 'func': mex_base_universe_d2_074_mex_basefill_074}


def mex_base_universe_d2_075_mex_basefill_075(mex_basefill_075):
    return _base_universe_d2(mex_basefill_075, 75)
MEX_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['mex_base_universe_d2_075_mex_basefill_075'] = {'inputs': ['mex_basefill_075'], 'func': mex_base_universe_d2_075_mex_basefill_075}
