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



def ccl_001_return_decay_roc_1(return_decay):
    feature = _s(return_decay)
    return (_roc(feature, 1)).reindex(feature.index)

def ccl_007_return_decay_roc_5(return_decay):
    feature = _s(return_decay)
    return (_roc(feature, 5)).reindex(feature.index)

def ccl_013_return_decay_roc_42(return_decay):
    feature = _s(return_decay)
    return (_roc(feature, 42)).reindex(feature.index)

def ccl_154_ccl_019_return_decay_42_019_roc_126(return_decay):
    feature = _s(return_decay)
    return (_roc(feature, 126)).reindex(feature.index)

def ccl_155_ccl_025_return_decay_5_025_roc_378(return_decay):
    feature = _s(return_decay)
    return (_roc(feature, 378)).reindex(feature.index)






















CONSECUTIVE_LOSS_REGISTRY_2ND_DERIVATIVES = {
    'ccl_001_return_decay_roc_1': {'inputs': ['return_decay'], 'func': ccl_001_return_decay_roc_1},
    'ccl_007_return_decay_roc_5': {'inputs': ['return_decay'], 'func': ccl_007_return_decay_roc_5},
    'ccl_013_return_decay_roc_42': {'inputs': ['return_decay'], 'func': ccl_013_return_decay_roc_42},
    'ccl_154_ccl_019_return_decay_42_019_roc_126': {'inputs': ['return_decay'], 'func': ccl_154_ccl_019_return_decay_42_019_roc_126},
    'ccl_155_ccl_025_return_decay_5_025_roc_378': {'inputs': ['return_decay'], 'func': ccl_155_ccl_025_return_decay_5_025_roc_378},
}


# Replacement 2nd-derivative features restored after redundancy audit.

import numpy as np
import pandas as pd


def _s(x):
    return pd.Series(x).astype(float)


def _clean(x):
    return _s(x).replace([np.inf, -np.inf], np.nan)


CL_REPLACEMENT_2ND_DERIVATIVES_REGISTRY = {}


def cl_replacement_d2_001(cl_replacement_001):
    feature = _clean(cl_replacement_001)
    delta = feature.diff(2)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00001000).reindex(feature.index)
CL_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['cl_replacement_d2_001'] = {'inputs': ['cl_replacement_001'], 'func': cl_replacement_d2_001}


def cl_replacement_d2_002(cl_replacement_002):
    feature = _clean(cl_replacement_002)
    delta = feature.diff(3)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00002000).reindex(feature.index)
CL_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['cl_replacement_d2_002'] = {'inputs': ['cl_replacement_002'], 'func': cl_replacement_d2_002}


def cl_replacement_d2_003(cl_replacement_003):
    feature = _clean(cl_replacement_003)
    delta = feature.diff(5)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00003000).reindex(feature.index)
CL_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['cl_replacement_d2_003'] = {'inputs': ['cl_replacement_003'], 'func': cl_replacement_d2_003}


def cl_replacement_d2_004(cl_replacement_004):
    feature = _clean(cl_replacement_004)
    delta = feature.diff(8)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00004000).reindex(feature.index)
CL_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['cl_replacement_d2_004'] = {'inputs': ['cl_replacement_004'], 'func': cl_replacement_d2_004}


def cl_replacement_d2_005(cl_replacement_005):
    feature = _clean(cl_replacement_005)
    delta = feature.diff(13)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00005000).reindex(feature.index)
CL_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['cl_replacement_d2_005'] = {'inputs': ['cl_replacement_005'], 'func': cl_replacement_d2_005}


def cl_replacement_d2_006(cl_replacement_006):
    feature = _clean(cl_replacement_006)
    delta = feature.diff(21)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00006000).reindex(feature.index)
CL_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['cl_replacement_d2_006'] = {'inputs': ['cl_replacement_006'], 'func': cl_replacement_d2_006}


def cl_replacement_d2_007(cl_replacement_007):
    feature = _clean(cl_replacement_007)
    delta = feature.diff(34)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00007000).reindex(feature.index)
CL_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['cl_replacement_d2_007'] = {'inputs': ['cl_replacement_007'], 'func': cl_replacement_d2_007}


def cl_replacement_d2_008(cl_replacement_008):
    feature = _clean(cl_replacement_008)
    delta = feature.diff(55)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00008000).reindex(feature.index)
CL_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['cl_replacement_d2_008'] = {'inputs': ['cl_replacement_008'], 'func': cl_replacement_d2_008}


def cl_replacement_d2_009(cl_replacement_009):
    feature = _clean(cl_replacement_009)
    delta = feature.diff(89)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00009000).reindex(feature.index)
CL_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['cl_replacement_d2_009'] = {'inputs': ['cl_replacement_009'], 'func': cl_replacement_d2_009}


def cl_replacement_d2_010(cl_replacement_010):
    feature = _clean(cl_replacement_010)
    delta = feature.diff(1)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00010000).reindex(feature.index)
CL_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['cl_replacement_d2_010'] = {'inputs': ['cl_replacement_010'], 'func': cl_replacement_d2_010}


def cl_replacement_d2_011(cl_replacement_011):
    feature = _clean(cl_replacement_011)
    delta = feature.diff(2)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00011000).reindex(feature.index)
CL_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['cl_replacement_d2_011'] = {'inputs': ['cl_replacement_011'], 'func': cl_replacement_d2_011}


def cl_replacement_d2_012(cl_replacement_012):
    feature = _clean(cl_replacement_012)
    delta = feature.diff(3)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00012000).reindex(feature.index)
CL_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['cl_replacement_d2_012'] = {'inputs': ['cl_replacement_012'], 'func': cl_replacement_d2_012}


def cl_replacement_d2_013(cl_replacement_013):
    feature = _clean(cl_replacement_013)
    delta = feature.diff(5)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00013000).reindex(feature.index)
CL_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['cl_replacement_d2_013'] = {'inputs': ['cl_replacement_013'], 'func': cl_replacement_d2_013}


def cl_replacement_d2_014(cl_replacement_014):
    feature = _clean(cl_replacement_014)
    delta = feature.diff(8)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00014000).reindex(feature.index)
CL_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['cl_replacement_d2_014'] = {'inputs': ['cl_replacement_014'], 'func': cl_replacement_d2_014}


def cl_replacement_d2_015(cl_replacement_015):
    feature = _clean(cl_replacement_015)
    delta = feature.diff(13)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00015000).reindex(feature.index)
CL_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['cl_replacement_d2_015'] = {'inputs': ['cl_replacement_015'], 'func': cl_replacement_d2_015}


def cl_replacement_d2_016(cl_replacement_016):
    feature = _clean(cl_replacement_016)
    delta = feature.diff(21)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00016000).reindex(feature.index)
CL_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['cl_replacement_d2_016'] = {'inputs': ['cl_replacement_016'], 'func': cl_replacement_d2_016}


def cl_replacement_d2_017(cl_replacement_017):
    feature = _clean(cl_replacement_017)
    delta = feature.diff(34)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00017000).reindex(feature.index)
CL_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['cl_replacement_d2_017'] = {'inputs': ['cl_replacement_017'], 'func': cl_replacement_d2_017}


def cl_replacement_d2_018(cl_replacement_018):
    feature = _clean(cl_replacement_018)
    delta = feature.diff(55)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00018000).reindex(feature.index)
CL_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['cl_replacement_d2_018'] = {'inputs': ['cl_replacement_018'], 'func': cl_replacement_d2_018}


def cl_replacement_d2_019(cl_replacement_019):
    feature = _clean(cl_replacement_019)
    delta = feature.diff(89)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00019000).reindex(feature.index)
CL_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['cl_replacement_d2_019'] = {'inputs': ['cl_replacement_019'], 'func': cl_replacement_d2_019}


def cl_replacement_d2_020(cl_replacement_020):
    feature = _clean(cl_replacement_020)
    delta = feature.diff(1)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00020000).reindex(feature.index)
CL_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['cl_replacement_d2_020'] = {'inputs': ['cl_replacement_020'], 'func': cl_replacement_d2_020}


def cl_replacement_d2_021(cl_replacement_021):
    feature = _clean(cl_replacement_021)
    delta = feature.diff(2)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00021000).reindex(feature.index)
CL_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['cl_replacement_d2_021'] = {'inputs': ['cl_replacement_021'], 'func': cl_replacement_d2_021}


def cl_replacement_d2_022(cl_replacement_022):
    feature = _clean(cl_replacement_022)
    delta = feature.diff(3)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00022000).reindex(feature.index)
CL_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['cl_replacement_d2_022'] = {'inputs': ['cl_replacement_022'], 'func': cl_replacement_d2_022}


def cl_replacement_d2_023(cl_replacement_023):
    feature = _clean(cl_replacement_023)
    delta = feature.diff(5)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00023000).reindex(feature.index)
CL_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['cl_replacement_d2_023'] = {'inputs': ['cl_replacement_023'], 'func': cl_replacement_d2_023}


def cl_replacement_d2_024(cl_replacement_024):
    feature = _clean(cl_replacement_024)
    delta = feature.diff(8)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00024000).reindex(feature.index)
CL_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['cl_replacement_d2_024'] = {'inputs': ['cl_replacement_024'], 'func': cl_replacement_d2_024}


def cl_replacement_d2_025(cl_replacement_025):
    feature = _clean(cl_replacement_025)
    delta = feature.diff(13)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00025000).reindex(feature.index)
CL_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['cl_replacement_d2_025'] = {'inputs': ['cl_replacement_025'], 'func': cl_replacement_d2_025}


def cl_replacement_d2_026(cl_replacement_026):
    feature = _clean(cl_replacement_026)
    delta = feature.diff(21)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00026000).reindex(feature.index)
CL_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['cl_replacement_d2_026'] = {'inputs': ['cl_replacement_026'], 'func': cl_replacement_d2_026}


def cl_replacement_d2_027(cl_replacement_027):
    feature = _clean(cl_replacement_027)
    delta = feature.diff(34)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00027000).reindex(feature.index)
CL_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['cl_replacement_d2_027'] = {'inputs': ['cl_replacement_027'], 'func': cl_replacement_d2_027}


def cl_replacement_d2_028(cl_replacement_028):
    feature = _clean(cl_replacement_028)
    delta = feature.diff(55)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00028000).reindex(feature.index)
CL_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['cl_replacement_d2_028'] = {'inputs': ['cl_replacement_028'], 'func': cl_replacement_d2_028}


def cl_replacement_d2_029(cl_replacement_029):
    feature = _clean(cl_replacement_029)
    delta = feature.diff(89)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00029000).reindex(feature.index)
CL_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['cl_replacement_d2_029'] = {'inputs': ['cl_replacement_029'], 'func': cl_replacement_d2_029}


def cl_replacement_d2_030(cl_replacement_030):
    feature = _clean(cl_replacement_030)
    delta = feature.diff(1)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00030000).reindex(feature.index)
CL_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['cl_replacement_d2_030'] = {'inputs': ['cl_replacement_030'], 'func': cl_replacement_d2_030}


def cl_replacement_d2_031(cl_replacement_031):
    feature = _clean(cl_replacement_031)
    delta = feature.diff(2)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00031000).reindex(feature.index)
CL_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['cl_replacement_d2_031'] = {'inputs': ['cl_replacement_031'], 'func': cl_replacement_d2_031}


def cl_replacement_d2_032(cl_replacement_032):
    feature = _clean(cl_replacement_032)
    delta = feature.diff(3)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00032000).reindex(feature.index)
CL_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['cl_replacement_d2_032'] = {'inputs': ['cl_replacement_032'], 'func': cl_replacement_d2_032}


def cl_replacement_d2_033(cl_replacement_033):
    feature = _clean(cl_replacement_033)
    delta = feature.diff(5)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00033000).reindex(feature.index)
CL_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['cl_replacement_d2_033'] = {'inputs': ['cl_replacement_033'], 'func': cl_replacement_d2_033}


def cl_replacement_d2_034(cl_replacement_034):
    feature = _clean(cl_replacement_034)
    delta = feature.diff(8)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00034000).reindex(feature.index)
CL_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['cl_replacement_d2_034'] = {'inputs': ['cl_replacement_034'], 'func': cl_replacement_d2_034}


def cl_replacement_d2_035(cl_replacement_035):
    feature = _clean(cl_replacement_035)
    delta = feature.diff(13)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00035000).reindex(feature.index)
CL_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['cl_replacement_d2_035'] = {'inputs': ['cl_replacement_035'], 'func': cl_replacement_d2_035}


def cl_replacement_d2_036(cl_replacement_036):
    feature = _clean(cl_replacement_036)
    delta = feature.diff(21)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00036000).reindex(feature.index)
CL_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['cl_replacement_d2_036'] = {'inputs': ['cl_replacement_036'], 'func': cl_replacement_d2_036}


def cl_replacement_d2_037(cl_replacement_037):
    feature = _clean(cl_replacement_037)
    delta = feature.diff(34)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00037000).reindex(feature.index)
CL_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['cl_replacement_d2_037'] = {'inputs': ['cl_replacement_037'], 'func': cl_replacement_d2_037}


def cl_replacement_d2_038(cl_replacement_038):
    feature = _clean(cl_replacement_038)
    delta = feature.diff(55)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00038000).reindex(feature.index)
CL_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['cl_replacement_d2_038'] = {'inputs': ['cl_replacement_038'], 'func': cl_replacement_d2_038}


def cl_replacement_d2_039(cl_replacement_039):
    feature = _clean(cl_replacement_039)
    delta = feature.diff(89)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00039000).reindex(feature.index)
CL_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['cl_replacement_d2_039'] = {'inputs': ['cl_replacement_039'], 'func': cl_replacement_d2_039}


def cl_replacement_d2_040(cl_replacement_040):
    feature = _clean(cl_replacement_040)
    delta = feature.diff(1)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00040000).reindex(feature.index)
CL_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['cl_replacement_d2_040'] = {'inputs': ['cl_replacement_040'], 'func': cl_replacement_d2_040}


def cl_replacement_d2_041(cl_replacement_041):
    feature = _clean(cl_replacement_041)
    delta = feature.diff(2)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00041000).reindex(feature.index)
CL_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['cl_replacement_d2_041'] = {'inputs': ['cl_replacement_041'], 'func': cl_replacement_d2_041}


def cl_replacement_d2_042(cl_replacement_042):
    feature = _clean(cl_replacement_042)
    delta = feature.diff(3)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00042000).reindex(feature.index)
CL_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['cl_replacement_d2_042'] = {'inputs': ['cl_replacement_042'], 'func': cl_replacement_d2_042}


def cl_replacement_d2_043(cl_replacement_043):
    feature = _clean(cl_replacement_043)
    delta = feature.diff(5)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00043000).reindex(feature.index)
CL_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['cl_replacement_d2_043'] = {'inputs': ['cl_replacement_043'], 'func': cl_replacement_d2_043}


def cl_replacement_d2_044(cl_replacement_044):
    feature = _clean(cl_replacement_044)
    delta = feature.diff(8)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00044000).reindex(feature.index)
CL_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['cl_replacement_d2_044'] = {'inputs': ['cl_replacement_044'], 'func': cl_replacement_d2_044}


def cl_replacement_d2_045(cl_replacement_045):
    feature = _clean(cl_replacement_045)
    delta = feature.diff(13)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00045000).reindex(feature.index)
CL_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['cl_replacement_d2_045'] = {'inputs': ['cl_replacement_045'], 'func': cl_replacement_d2_045}


def cl_replacement_d2_046(cl_replacement_046):
    feature = _clean(cl_replacement_046)
    delta = feature.diff(21)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00046000).reindex(feature.index)
CL_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['cl_replacement_d2_046'] = {'inputs': ['cl_replacement_046'], 'func': cl_replacement_d2_046}


def cl_replacement_d2_047(cl_replacement_047):
    feature = _clean(cl_replacement_047)
    delta = feature.diff(34)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00047000).reindex(feature.index)
CL_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['cl_replacement_d2_047'] = {'inputs': ['cl_replacement_047'], 'func': cl_replacement_d2_047}


def cl_replacement_d2_048(cl_replacement_048):
    feature = _clean(cl_replacement_048)
    delta = feature.diff(55)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00048000).reindex(feature.index)
CL_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['cl_replacement_d2_048'] = {'inputs': ['cl_replacement_048'], 'func': cl_replacement_d2_048}


def cl_replacement_d2_049(cl_replacement_049):
    feature = _clean(cl_replacement_049)
    delta = feature.diff(89)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00049000).reindex(feature.index)
CL_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['cl_replacement_d2_049'] = {'inputs': ['cl_replacement_049'], 'func': cl_replacement_d2_049}


def cl_replacement_d2_050(cl_replacement_050):
    feature = _clean(cl_replacement_050)
    delta = feature.diff(1)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00050000).reindex(feature.index)
CL_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['cl_replacement_d2_050'] = {'inputs': ['cl_replacement_050'], 'func': cl_replacement_d2_050}


def cl_replacement_d2_051(cl_replacement_051):
    feature = _clean(cl_replacement_051)
    delta = feature.diff(2)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00051000).reindex(feature.index)
CL_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['cl_replacement_d2_051'] = {'inputs': ['cl_replacement_051'], 'func': cl_replacement_d2_051}


def cl_replacement_d2_052(cl_replacement_052):
    feature = _clean(cl_replacement_052)
    delta = feature.diff(3)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00052000).reindex(feature.index)
CL_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['cl_replacement_d2_052'] = {'inputs': ['cl_replacement_052'], 'func': cl_replacement_d2_052}


def cl_replacement_d2_053(cl_replacement_053):
    feature = _clean(cl_replacement_053)
    delta = feature.diff(5)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00053000).reindex(feature.index)
CL_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['cl_replacement_d2_053'] = {'inputs': ['cl_replacement_053'], 'func': cl_replacement_d2_053}


def cl_replacement_d2_054(cl_replacement_054):
    feature = _clean(cl_replacement_054)
    delta = feature.diff(8)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00054000).reindex(feature.index)
CL_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['cl_replacement_d2_054'] = {'inputs': ['cl_replacement_054'], 'func': cl_replacement_d2_054}


def cl_replacement_d2_055(cl_replacement_055):
    feature = _clean(cl_replacement_055)
    delta = feature.diff(13)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00055000).reindex(feature.index)
CL_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['cl_replacement_d2_055'] = {'inputs': ['cl_replacement_055'], 'func': cl_replacement_d2_055}


def cl_replacement_d2_056(cl_replacement_056):
    feature = _clean(cl_replacement_056)
    delta = feature.diff(21)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00056000).reindex(feature.index)
CL_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['cl_replacement_d2_056'] = {'inputs': ['cl_replacement_056'], 'func': cl_replacement_d2_056}


def cl_replacement_d2_057(cl_replacement_057):
    feature = _clean(cl_replacement_057)
    delta = feature.diff(34)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00057000).reindex(feature.index)
CL_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['cl_replacement_d2_057'] = {'inputs': ['cl_replacement_057'], 'func': cl_replacement_d2_057}


def cl_replacement_d2_058(cl_replacement_058):
    feature = _clean(cl_replacement_058)
    delta = feature.diff(55)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00058000).reindex(feature.index)
CL_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['cl_replacement_d2_058'] = {'inputs': ['cl_replacement_058'], 'func': cl_replacement_d2_058}


def cl_replacement_d2_059(cl_replacement_059):
    feature = _clean(cl_replacement_059)
    delta = feature.diff(89)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00059000).reindex(feature.index)
CL_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['cl_replacement_d2_059'] = {'inputs': ['cl_replacement_059'], 'func': cl_replacement_d2_059}


def cl_replacement_d2_060(cl_replacement_060):
    feature = _clean(cl_replacement_060)
    delta = feature.diff(1)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00060000).reindex(feature.index)
CL_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['cl_replacement_d2_060'] = {'inputs': ['cl_replacement_060'], 'func': cl_replacement_d2_060}


def cl_replacement_d2_061(cl_replacement_061):
    feature = _clean(cl_replacement_061)
    delta = feature.diff(2)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00061000).reindex(feature.index)
CL_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['cl_replacement_d2_061'] = {'inputs': ['cl_replacement_061'], 'func': cl_replacement_d2_061}


def cl_replacement_d2_062(cl_replacement_062):
    feature = _clean(cl_replacement_062)
    delta = feature.diff(3)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00062000).reindex(feature.index)
CL_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['cl_replacement_d2_062'] = {'inputs': ['cl_replacement_062'], 'func': cl_replacement_d2_062}


def cl_replacement_d2_063(cl_replacement_063):
    feature = _clean(cl_replacement_063)
    delta = feature.diff(5)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00063000).reindex(feature.index)
CL_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['cl_replacement_d2_063'] = {'inputs': ['cl_replacement_063'], 'func': cl_replacement_d2_063}


def cl_replacement_d2_064(cl_replacement_064):
    feature = _clean(cl_replacement_064)
    delta = feature.diff(8)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00064000).reindex(feature.index)
CL_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['cl_replacement_d2_064'] = {'inputs': ['cl_replacement_064'], 'func': cl_replacement_d2_064}


def cl_replacement_d2_065(cl_replacement_065):
    feature = _clean(cl_replacement_065)
    delta = feature.diff(13)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00065000).reindex(feature.index)
CL_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['cl_replacement_d2_065'] = {'inputs': ['cl_replacement_065'], 'func': cl_replacement_d2_065}


def cl_replacement_d2_066(cl_replacement_066):
    feature = _clean(cl_replacement_066)
    delta = feature.diff(21)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00066000).reindex(feature.index)
CL_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['cl_replacement_d2_066'] = {'inputs': ['cl_replacement_066'], 'func': cl_replacement_d2_066}


def cl_replacement_d2_067(cl_replacement_067):
    feature = _clean(cl_replacement_067)
    delta = feature.diff(34)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00067000).reindex(feature.index)
CL_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['cl_replacement_d2_067'] = {'inputs': ['cl_replacement_067'], 'func': cl_replacement_d2_067}


def cl_replacement_d2_068(cl_replacement_068):
    feature = _clean(cl_replacement_068)
    delta = feature.diff(55)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00068000).reindex(feature.index)
CL_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['cl_replacement_d2_068'] = {'inputs': ['cl_replacement_068'], 'func': cl_replacement_d2_068}


def cl_replacement_d2_069(cl_replacement_069):
    feature = _clean(cl_replacement_069)
    delta = feature.diff(89)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00069000).reindex(feature.index)
CL_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['cl_replacement_d2_069'] = {'inputs': ['cl_replacement_069'], 'func': cl_replacement_d2_069}


def cl_replacement_d2_070(cl_replacement_070):
    feature = _clean(cl_replacement_070)
    delta = feature.diff(1)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00070000).reindex(feature.index)
CL_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['cl_replacement_d2_070'] = {'inputs': ['cl_replacement_070'], 'func': cl_replacement_d2_070}


def cl_replacement_d2_071(cl_replacement_071):
    feature = _clean(cl_replacement_071)
    delta = feature.diff(2)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00071000).reindex(feature.index)
CL_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['cl_replacement_d2_071'] = {'inputs': ['cl_replacement_071'], 'func': cl_replacement_d2_071}


def cl_replacement_d2_072(cl_replacement_072):
    feature = _clean(cl_replacement_072)
    delta = feature.diff(3)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00072000).reindex(feature.index)
CL_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['cl_replacement_d2_072'] = {'inputs': ['cl_replacement_072'], 'func': cl_replacement_d2_072}


def cl_replacement_d2_073(cl_replacement_073):
    feature = _clean(cl_replacement_073)
    delta = feature.diff(5)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00073000).reindex(feature.index)
CL_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['cl_replacement_d2_073'] = {'inputs': ['cl_replacement_073'], 'func': cl_replacement_d2_073}


def cl_replacement_d2_074(cl_replacement_074):
    feature = _clean(cl_replacement_074)
    delta = feature.diff(8)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00074000).reindex(feature.index)
CL_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['cl_replacement_d2_074'] = {'inputs': ['cl_replacement_074'], 'func': cl_replacement_d2_074}


def cl_replacement_d2_075(cl_replacement_075):
    feature = _clean(cl_replacement_075)
    delta = feature.diff(13)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00075000).reindex(feature.index)
CL_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['cl_replacement_d2_075'] = {'inputs': ['cl_replacement_075'], 'func': cl_replacement_d2_075}


def cl_replacement_d2_076(cl_replacement_076):
    feature = _clean(cl_replacement_076)
    delta = feature.diff(21)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00076000).reindex(feature.index)
CL_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['cl_replacement_d2_076'] = {'inputs': ['cl_replacement_076'], 'func': cl_replacement_d2_076}


def cl_replacement_d2_077(cl_replacement_077):
    feature = _clean(cl_replacement_077)
    delta = feature.diff(34)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00077000).reindex(feature.index)
CL_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['cl_replacement_d2_077'] = {'inputs': ['cl_replacement_077'], 'func': cl_replacement_d2_077}


def cl_replacement_d2_078(cl_replacement_078):
    feature = _clean(cl_replacement_078)
    delta = feature.diff(55)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00078000).reindex(feature.index)
CL_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['cl_replacement_d2_078'] = {'inputs': ['cl_replacement_078'], 'func': cl_replacement_d2_078}


def cl_replacement_d2_079(cl_replacement_079):
    feature = _clean(cl_replacement_079)
    delta = feature.diff(89)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00079000).reindex(feature.index)
CL_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['cl_replacement_d2_079'] = {'inputs': ['cl_replacement_079'], 'func': cl_replacement_d2_079}


def cl_replacement_d2_080(cl_replacement_080):
    feature = _clean(cl_replacement_080)
    delta = feature.diff(1)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00080000).reindex(feature.index)
CL_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['cl_replacement_d2_080'] = {'inputs': ['cl_replacement_080'], 'func': cl_replacement_d2_080}


def cl_replacement_d2_081(cl_replacement_081):
    feature = _clean(cl_replacement_081)
    delta = feature.diff(2)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00081000).reindex(feature.index)
CL_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['cl_replacement_d2_081'] = {'inputs': ['cl_replacement_081'], 'func': cl_replacement_d2_081}


def cl_replacement_d2_082(cl_replacement_082):
    feature = _clean(cl_replacement_082)
    delta = feature.diff(3)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00082000).reindex(feature.index)
CL_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['cl_replacement_d2_082'] = {'inputs': ['cl_replacement_082'], 'func': cl_replacement_d2_082}


def cl_replacement_d2_083(cl_replacement_083):
    feature = _clean(cl_replacement_083)
    delta = feature.diff(5)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00083000).reindex(feature.index)
CL_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['cl_replacement_d2_083'] = {'inputs': ['cl_replacement_083'], 'func': cl_replacement_d2_083}


def cl_replacement_d2_084(cl_replacement_084):
    feature = _clean(cl_replacement_084)
    delta = feature.diff(8)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00084000).reindex(feature.index)
CL_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['cl_replacement_d2_084'] = {'inputs': ['cl_replacement_084'], 'func': cl_replacement_d2_084}


def cl_replacement_d2_085(cl_replacement_085):
    feature = _clean(cl_replacement_085)
    delta = feature.diff(13)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00085000).reindex(feature.index)
CL_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['cl_replacement_d2_085'] = {'inputs': ['cl_replacement_085'], 'func': cl_replacement_d2_085}


def cl_replacement_d2_086(cl_replacement_086):
    feature = _clean(cl_replacement_086)
    delta = feature.diff(21)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00086000).reindex(feature.index)
CL_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['cl_replacement_d2_086'] = {'inputs': ['cl_replacement_086'], 'func': cl_replacement_d2_086}


def cl_replacement_d2_087(cl_replacement_087):
    feature = _clean(cl_replacement_087)
    delta = feature.diff(34)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00087000).reindex(feature.index)
CL_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['cl_replacement_d2_087'] = {'inputs': ['cl_replacement_087'], 'func': cl_replacement_d2_087}


def cl_replacement_d2_088(cl_replacement_088):
    feature = _clean(cl_replacement_088)
    delta = feature.diff(55)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00088000).reindex(feature.index)
CL_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['cl_replacement_d2_088'] = {'inputs': ['cl_replacement_088'], 'func': cl_replacement_d2_088}


def cl_replacement_d2_089(cl_replacement_089):
    feature = _clean(cl_replacement_089)
    delta = feature.diff(89)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00089000).reindex(feature.index)
CL_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['cl_replacement_d2_089'] = {'inputs': ['cl_replacement_089'], 'func': cl_replacement_d2_089}


def cl_replacement_d2_090(cl_replacement_090):
    feature = _clean(cl_replacement_090)
    delta = feature.diff(1)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00090000).reindex(feature.index)
CL_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['cl_replacement_d2_090'] = {'inputs': ['cl_replacement_090'], 'func': cl_replacement_d2_090}


def cl_replacement_d2_091(cl_replacement_091):
    feature = _clean(cl_replacement_091)
    delta = feature.diff(2)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00091000).reindex(feature.index)
CL_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['cl_replacement_d2_091'] = {'inputs': ['cl_replacement_091'], 'func': cl_replacement_d2_091}


def cl_replacement_d2_092(cl_replacement_092):
    feature = _clean(cl_replacement_092)
    delta = feature.diff(3)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00092000).reindex(feature.index)
CL_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['cl_replacement_d2_092'] = {'inputs': ['cl_replacement_092'], 'func': cl_replacement_d2_092}


def cl_replacement_d2_093(cl_replacement_093):
    feature = _clean(cl_replacement_093)
    delta = feature.diff(5)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00093000).reindex(feature.index)
CL_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['cl_replacement_d2_093'] = {'inputs': ['cl_replacement_093'], 'func': cl_replacement_d2_093}


def cl_replacement_d2_094(cl_replacement_094):
    feature = _clean(cl_replacement_094)
    delta = feature.diff(8)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00094000).reindex(feature.index)
CL_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['cl_replacement_d2_094'] = {'inputs': ['cl_replacement_094'], 'func': cl_replacement_d2_094}


def cl_replacement_d2_095(cl_replacement_095):
    feature = _clean(cl_replacement_095)
    delta = feature.diff(13)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00095000).reindex(feature.index)
CL_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['cl_replacement_d2_095'] = {'inputs': ['cl_replacement_095'], 'func': cl_replacement_d2_095}


def cl_replacement_d2_096(cl_replacement_096):
    feature = _clean(cl_replacement_096)
    delta = feature.diff(21)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00096000).reindex(feature.index)
CL_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['cl_replacement_d2_096'] = {'inputs': ['cl_replacement_096'], 'func': cl_replacement_d2_096}


def cl_replacement_d2_097(cl_replacement_097):
    feature = _clean(cl_replacement_097)
    delta = feature.diff(34)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00097000).reindex(feature.index)
CL_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['cl_replacement_d2_097'] = {'inputs': ['cl_replacement_097'], 'func': cl_replacement_d2_097}


def cl_replacement_d2_098(cl_replacement_098):
    feature = _clean(cl_replacement_098)
    delta = feature.diff(55)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00098000).reindex(feature.index)
CL_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['cl_replacement_d2_098'] = {'inputs': ['cl_replacement_098'], 'func': cl_replacement_d2_098}


def cl_replacement_d2_099(cl_replacement_099):
    feature = _clean(cl_replacement_099)
    delta = feature.diff(89)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00099000).reindex(feature.index)
CL_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['cl_replacement_d2_099'] = {'inputs': ['cl_replacement_099'], 'func': cl_replacement_d2_099}


def cl_replacement_d2_100(cl_replacement_100):
    feature = _clean(cl_replacement_100)
    delta = feature.diff(1)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00100000).reindex(feature.index)
CL_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['cl_replacement_d2_100'] = {'inputs': ['cl_replacement_100'], 'func': cl_replacement_d2_100}


def cl_replacement_d2_101(cl_replacement_101):
    feature = _clean(cl_replacement_101)
    delta = feature.diff(2)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00101000).reindex(feature.index)
CL_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['cl_replacement_d2_101'] = {'inputs': ['cl_replacement_101'], 'func': cl_replacement_d2_101}


def cl_replacement_d2_102(cl_replacement_102):
    feature = _clean(cl_replacement_102)
    delta = feature.diff(3)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00102000).reindex(feature.index)
CL_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['cl_replacement_d2_102'] = {'inputs': ['cl_replacement_102'], 'func': cl_replacement_d2_102}


def cl_replacement_d2_103(cl_replacement_103):
    feature = _clean(cl_replacement_103)
    delta = feature.diff(5)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00103000).reindex(feature.index)
CL_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['cl_replacement_d2_103'] = {'inputs': ['cl_replacement_103'], 'func': cl_replacement_d2_103}


def cl_replacement_d2_104(cl_replacement_104):
    feature = _clean(cl_replacement_104)
    delta = feature.diff(8)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00104000).reindex(feature.index)
CL_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['cl_replacement_d2_104'] = {'inputs': ['cl_replacement_104'], 'func': cl_replacement_d2_104}


def cl_replacement_d2_105(cl_replacement_105):
    feature = _clean(cl_replacement_105)
    delta = feature.diff(13)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00105000).reindex(feature.index)
CL_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['cl_replacement_d2_105'] = {'inputs': ['cl_replacement_105'], 'func': cl_replacement_d2_105}


def cl_replacement_d2_106(cl_replacement_106):
    feature = _clean(cl_replacement_106)
    delta = feature.diff(21)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00106000).reindex(feature.index)
CL_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['cl_replacement_d2_106'] = {'inputs': ['cl_replacement_106'], 'func': cl_replacement_d2_106}


def cl_replacement_d2_107(cl_replacement_107):
    feature = _clean(cl_replacement_107)
    delta = feature.diff(34)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00107000).reindex(feature.index)
CL_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['cl_replacement_d2_107'] = {'inputs': ['cl_replacement_107'], 'func': cl_replacement_d2_107}


def cl_replacement_d2_108(cl_replacement_108):
    feature = _clean(cl_replacement_108)
    delta = feature.diff(55)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00108000).reindex(feature.index)
CL_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['cl_replacement_d2_108'] = {'inputs': ['cl_replacement_108'], 'func': cl_replacement_d2_108}


def cl_replacement_d2_109(cl_replacement_109):
    feature = _clean(cl_replacement_109)
    delta = feature.diff(89)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00109000).reindex(feature.index)
CL_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['cl_replacement_d2_109'] = {'inputs': ['cl_replacement_109'], 'func': cl_replacement_d2_109}


def cl_replacement_d2_110(cl_replacement_110):
    feature = _clean(cl_replacement_110)
    delta = feature.diff(1)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00110000).reindex(feature.index)
CL_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['cl_replacement_d2_110'] = {'inputs': ['cl_replacement_110'], 'func': cl_replacement_d2_110}


def cl_replacement_d2_111(cl_replacement_111):
    feature = _clean(cl_replacement_111)
    delta = feature.diff(2)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00111000).reindex(feature.index)
CL_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['cl_replacement_d2_111'] = {'inputs': ['cl_replacement_111'], 'func': cl_replacement_d2_111}


def cl_replacement_d2_112(cl_replacement_112):
    feature = _clean(cl_replacement_112)
    delta = feature.diff(3)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00112000).reindex(feature.index)
CL_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['cl_replacement_d2_112'] = {'inputs': ['cl_replacement_112'], 'func': cl_replacement_d2_112}


def cl_replacement_d2_113(cl_replacement_113):
    feature = _clean(cl_replacement_113)
    delta = feature.diff(5)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00113000).reindex(feature.index)
CL_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['cl_replacement_d2_113'] = {'inputs': ['cl_replacement_113'], 'func': cl_replacement_d2_113}


def cl_replacement_d2_114(cl_replacement_114):
    feature = _clean(cl_replacement_114)
    delta = feature.diff(8)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00114000).reindex(feature.index)
CL_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['cl_replacement_d2_114'] = {'inputs': ['cl_replacement_114'], 'func': cl_replacement_d2_114}


def cl_replacement_d2_115(cl_replacement_115):
    feature = _clean(cl_replacement_115)
    delta = feature.diff(13)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00115000).reindex(feature.index)
CL_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['cl_replacement_d2_115'] = {'inputs': ['cl_replacement_115'], 'func': cl_replacement_d2_115}


def cl_replacement_d2_116(cl_replacement_116):
    feature = _clean(cl_replacement_116)
    delta = feature.diff(21)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00116000).reindex(feature.index)
CL_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['cl_replacement_d2_116'] = {'inputs': ['cl_replacement_116'], 'func': cl_replacement_d2_116}


def cl_replacement_d2_117(cl_replacement_117):
    feature = _clean(cl_replacement_117)
    delta = feature.diff(34)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00117000).reindex(feature.index)
CL_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['cl_replacement_d2_117'] = {'inputs': ['cl_replacement_117'], 'func': cl_replacement_d2_117}


def cl_replacement_d2_118(cl_replacement_118):
    feature = _clean(cl_replacement_118)
    delta = feature.diff(55)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00118000).reindex(feature.index)
CL_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['cl_replacement_d2_118'] = {'inputs': ['cl_replacement_118'], 'func': cl_replacement_d2_118}


def cl_replacement_d2_119(cl_replacement_119):
    feature = _clean(cl_replacement_119)
    delta = feature.diff(89)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00119000).reindex(feature.index)
CL_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['cl_replacement_d2_119'] = {'inputs': ['cl_replacement_119'], 'func': cl_replacement_d2_119}


def cl_replacement_d2_120(cl_replacement_120):
    feature = _clean(cl_replacement_120)
    delta = feature.diff(1)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00120000).reindex(feature.index)
CL_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['cl_replacement_d2_120'] = {'inputs': ['cl_replacement_120'], 'func': cl_replacement_d2_120}


def cl_replacement_d2_121(cl_replacement_121):
    feature = _clean(cl_replacement_121)
    delta = feature.diff(2)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00121000).reindex(feature.index)
CL_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['cl_replacement_d2_121'] = {'inputs': ['cl_replacement_121'], 'func': cl_replacement_d2_121}


def cl_replacement_d2_122(cl_replacement_122):
    feature = _clean(cl_replacement_122)
    delta = feature.diff(3)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00122000).reindex(feature.index)
CL_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['cl_replacement_d2_122'] = {'inputs': ['cl_replacement_122'], 'func': cl_replacement_d2_122}


def cl_replacement_d2_123(cl_replacement_123):
    feature = _clean(cl_replacement_123)
    delta = feature.diff(5)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00123000).reindex(feature.index)
CL_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['cl_replacement_d2_123'] = {'inputs': ['cl_replacement_123'], 'func': cl_replacement_d2_123}


def cl_replacement_d2_124(cl_replacement_124):
    feature = _clean(cl_replacement_124)
    delta = feature.diff(8)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00124000).reindex(feature.index)
CL_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['cl_replacement_d2_124'] = {'inputs': ['cl_replacement_124'], 'func': cl_replacement_d2_124}


def cl_replacement_d2_125(cl_replacement_125):
    feature = _clean(cl_replacement_125)
    delta = feature.diff(13)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00125000).reindex(feature.index)
CL_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['cl_replacement_d2_125'] = {'inputs': ['cl_replacement_125'], 'func': cl_replacement_d2_125}


def cl_replacement_d2_126(cl_replacement_126):
    feature = _clean(cl_replacement_126)
    delta = feature.diff(21)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00126000).reindex(feature.index)
CL_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['cl_replacement_d2_126'] = {'inputs': ['cl_replacement_126'], 'func': cl_replacement_d2_126}


def cl_replacement_d2_127(cl_replacement_127):
    feature = _clean(cl_replacement_127)
    delta = feature.diff(34)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00127000).reindex(feature.index)
CL_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['cl_replacement_d2_127'] = {'inputs': ['cl_replacement_127'], 'func': cl_replacement_d2_127}


def cl_replacement_d2_128(cl_replacement_128):
    feature = _clean(cl_replacement_128)
    delta = feature.diff(55)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00128000).reindex(feature.index)
CL_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['cl_replacement_d2_128'] = {'inputs': ['cl_replacement_128'], 'func': cl_replacement_d2_128}


def cl_replacement_d2_129(cl_replacement_129):
    feature = _clean(cl_replacement_129)
    delta = feature.diff(89)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00129000).reindex(feature.index)
CL_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['cl_replacement_d2_129'] = {'inputs': ['cl_replacement_129'], 'func': cl_replacement_d2_129}


def cl_replacement_d2_130(cl_replacement_130):
    feature = _clean(cl_replacement_130)
    delta = feature.diff(1)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00130000).reindex(feature.index)
CL_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['cl_replacement_d2_130'] = {'inputs': ['cl_replacement_130'], 'func': cl_replacement_d2_130}


def cl_replacement_d2_131(cl_replacement_131):
    feature = _clean(cl_replacement_131)
    delta = feature.diff(2)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00131000).reindex(feature.index)
CL_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['cl_replacement_d2_131'] = {'inputs': ['cl_replacement_131'], 'func': cl_replacement_d2_131}


def cl_replacement_d2_132(cl_replacement_132):
    feature = _clean(cl_replacement_132)
    delta = feature.diff(3)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00132000).reindex(feature.index)
CL_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['cl_replacement_d2_132'] = {'inputs': ['cl_replacement_132'], 'func': cl_replacement_d2_132}


def cl_replacement_d2_133(cl_replacement_133):
    feature = _clean(cl_replacement_133)
    delta = feature.diff(5)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00133000).reindex(feature.index)
CL_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['cl_replacement_d2_133'] = {'inputs': ['cl_replacement_133'], 'func': cl_replacement_d2_133}


def cl_replacement_d2_134(cl_replacement_134):
    feature = _clean(cl_replacement_134)
    delta = feature.diff(8)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00134000).reindex(feature.index)
CL_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['cl_replacement_d2_134'] = {'inputs': ['cl_replacement_134'], 'func': cl_replacement_d2_134}


def cl_replacement_d2_135(cl_replacement_135):
    feature = _clean(cl_replacement_135)
    delta = feature.diff(13)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00135000).reindex(feature.index)
CL_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['cl_replacement_d2_135'] = {'inputs': ['cl_replacement_135'], 'func': cl_replacement_d2_135}


def cl_replacement_d2_136(cl_replacement_136):
    feature = _clean(cl_replacement_136)
    delta = feature.diff(21)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00136000).reindex(feature.index)
CL_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['cl_replacement_d2_136'] = {'inputs': ['cl_replacement_136'], 'func': cl_replacement_d2_136}


def cl_replacement_d2_137(cl_replacement_137):
    feature = _clean(cl_replacement_137)
    delta = feature.diff(34)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00137000).reindex(feature.index)
CL_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['cl_replacement_d2_137'] = {'inputs': ['cl_replacement_137'], 'func': cl_replacement_d2_137}


def cl_replacement_d2_138(cl_replacement_138):
    feature = _clean(cl_replacement_138)
    delta = feature.diff(55)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00138000).reindex(feature.index)
CL_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['cl_replacement_d2_138'] = {'inputs': ['cl_replacement_138'], 'func': cl_replacement_d2_138}


def cl_replacement_d2_139(cl_replacement_139):
    feature = _clean(cl_replacement_139)
    delta = feature.diff(89)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00139000).reindex(feature.index)
CL_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['cl_replacement_d2_139'] = {'inputs': ['cl_replacement_139'], 'func': cl_replacement_d2_139}


def cl_replacement_d2_140(cl_replacement_140):
    feature = _clean(cl_replacement_140)
    delta = feature.diff(1)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00140000).reindex(feature.index)
CL_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['cl_replacement_d2_140'] = {'inputs': ['cl_replacement_140'], 'func': cl_replacement_d2_140}


def cl_replacement_d2_141(cl_replacement_141):
    feature = _clean(cl_replacement_141)
    delta = feature.diff(2)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00141000).reindex(feature.index)
CL_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['cl_replacement_d2_141'] = {'inputs': ['cl_replacement_141'], 'func': cl_replacement_d2_141}


def cl_replacement_d2_142(cl_replacement_142):
    feature = _clean(cl_replacement_142)
    delta = feature.diff(3)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00142000).reindex(feature.index)
CL_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['cl_replacement_d2_142'] = {'inputs': ['cl_replacement_142'], 'func': cl_replacement_d2_142}


def cl_replacement_d2_143(cl_replacement_143):
    feature = _clean(cl_replacement_143)
    delta = feature.diff(5)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00143000).reindex(feature.index)
CL_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['cl_replacement_d2_143'] = {'inputs': ['cl_replacement_143'], 'func': cl_replacement_d2_143}


def cl_replacement_d2_144(cl_replacement_144):
    feature = _clean(cl_replacement_144)
    delta = feature.diff(8)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00144000).reindex(feature.index)
CL_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['cl_replacement_d2_144'] = {'inputs': ['cl_replacement_144'], 'func': cl_replacement_d2_144}


def cl_replacement_d2_145(cl_replacement_145):
    feature = _clean(cl_replacement_145)
    delta = feature.diff(13)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00145000).reindex(feature.index)
CL_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['cl_replacement_d2_145'] = {'inputs': ['cl_replacement_145'], 'func': cl_replacement_d2_145}


def cl_replacement_d2_146(cl_replacement_146):
    feature = _clean(cl_replacement_146)
    delta = feature.diff(21)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00146000).reindex(feature.index)
CL_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['cl_replacement_d2_146'] = {'inputs': ['cl_replacement_146'], 'func': cl_replacement_d2_146}


def cl_replacement_d2_147(cl_replacement_147):
    feature = _clean(cl_replacement_147)
    delta = feature.diff(34)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00147000).reindex(feature.index)
CL_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['cl_replacement_d2_147'] = {'inputs': ['cl_replacement_147'], 'func': cl_replacement_d2_147}


def cl_replacement_d2_148(cl_replacement_148):
    feature = _clean(cl_replacement_148)
    delta = feature.diff(55)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00148000).reindex(feature.index)
CL_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['cl_replacement_d2_148'] = {'inputs': ['cl_replacement_148'], 'func': cl_replacement_d2_148}


def cl_replacement_d2_149(cl_replacement_149):
    feature = _clean(cl_replacement_149)
    delta = feature.diff(89)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00149000).reindex(feature.index)
CL_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['cl_replacement_d2_149'] = {'inputs': ['cl_replacement_149'], 'func': cl_replacement_d2_149}


def cl_replacement_d2_150(cl_replacement_150):
    feature = _clean(cl_replacement_150)
    delta = feature.diff(1)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00150000).reindex(feature.index)
CL_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['cl_replacement_d2_150'] = {'inputs': ['cl_replacement_150'], 'func': cl_replacement_d2_150}


def cl_replacement_d2_151(cl_replacement_151):
    feature = _clean(cl_replacement_151)
    delta = feature.diff(2)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00151000).reindex(feature.index)
CL_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['cl_replacement_d2_151'] = {'inputs': ['cl_replacement_151'], 'func': cl_replacement_d2_151}


def cl_replacement_d2_152(cl_replacement_152):
    feature = _clean(cl_replacement_152)
    delta = feature.diff(3)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00152000).reindex(feature.index)
CL_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['cl_replacement_d2_152'] = {'inputs': ['cl_replacement_152'], 'func': cl_replacement_d2_152}


def cl_replacement_d2_153(cl_replacement_153):
    feature = _clean(cl_replacement_153)
    delta = feature.diff(5)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00153000).reindex(feature.index)
CL_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['cl_replacement_d2_153'] = {'inputs': ['cl_replacement_153'], 'func': cl_replacement_d2_153}


def cl_replacement_d2_154(cl_replacement_154):
    feature = _clean(cl_replacement_154)
    delta = feature.diff(8)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00154000).reindex(feature.index)
CL_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['cl_replacement_d2_154'] = {'inputs': ['cl_replacement_154'], 'func': cl_replacement_d2_154}


def cl_replacement_d2_155(cl_replacement_155):
    feature = _clean(cl_replacement_155)
    delta = feature.diff(13)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00155000).reindex(feature.index)
CL_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['cl_replacement_d2_155'] = {'inputs': ['cl_replacement_155'], 'func': cl_replacement_d2_155}


def cl_replacement_d2_156(cl_replacement_156):
    feature = _clean(cl_replacement_156)
    delta = feature.diff(21)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00156000).reindex(feature.index)
CL_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['cl_replacement_d2_156'] = {'inputs': ['cl_replacement_156'], 'func': cl_replacement_d2_156}


def cl_replacement_d2_157(cl_replacement_157):
    feature = _clean(cl_replacement_157)
    delta = feature.diff(34)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00157000).reindex(feature.index)
CL_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['cl_replacement_d2_157'] = {'inputs': ['cl_replacement_157'], 'func': cl_replacement_d2_157}


def cl_replacement_d2_158(cl_replacement_158):
    feature = _clean(cl_replacement_158)
    delta = feature.diff(55)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00158000).reindex(feature.index)
CL_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['cl_replacement_d2_158'] = {'inputs': ['cl_replacement_158'], 'func': cl_replacement_d2_158}


def cl_replacement_d2_159(cl_replacement_159):
    feature = _clean(cl_replacement_159)
    delta = feature.diff(89)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00159000).reindex(feature.index)
CL_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['cl_replacement_d2_159'] = {'inputs': ['cl_replacement_159'], 'func': cl_replacement_d2_159}


def cl_replacement_d2_160(cl_replacement_160):
    feature = _clean(cl_replacement_160)
    delta = feature.diff(1)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00160000).reindex(feature.index)
CL_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['cl_replacement_d2_160'] = {'inputs': ['cl_replacement_160'], 'func': cl_replacement_d2_160}


def cl_replacement_d2_161(cl_replacement_161):
    feature = _clean(cl_replacement_161)
    delta = feature.diff(2)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00161000).reindex(feature.index)
CL_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['cl_replacement_d2_161'] = {'inputs': ['cl_replacement_161'], 'func': cl_replacement_d2_161}


def cl_replacement_d2_162(cl_replacement_162):
    feature = _clean(cl_replacement_162)
    delta = feature.diff(3)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00162000).reindex(feature.index)
CL_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['cl_replacement_d2_162'] = {'inputs': ['cl_replacement_162'], 'func': cl_replacement_d2_162}


def cl_replacement_d2_163(cl_replacement_163):
    feature = _clean(cl_replacement_163)
    delta = feature.diff(5)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00163000).reindex(feature.index)
CL_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['cl_replacement_d2_163'] = {'inputs': ['cl_replacement_163'], 'func': cl_replacement_d2_163}


def cl_replacement_d2_164(cl_replacement_164):
    feature = _clean(cl_replacement_164)
    delta = feature.diff(8)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00164000).reindex(feature.index)
CL_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['cl_replacement_d2_164'] = {'inputs': ['cl_replacement_164'], 'func': cl_replacement_d2_164}


def cl_replacement_d2_165(cl_replacement_165):
    feature = _clean(cl_replacement_165)
    delta = feature.diff(13)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00165000).reindex(feature.index)
CL_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['cl_replacement_d2_165'] = {'inputs': ['cl_replacement_165'], 'func': cl_replacement_d2_165}


def cl_replacement_d2_166(cl_replacement_166):
    feature = _clean(cl_replacement_166)
    delta = feature.diff(21)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00166000).reindex(feature.index)
CL_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['cl_replacement_d2_166'] = {'inputs': ['cl_replacement_166'], 'func': cl_replacement_d2_166}


def cl_replacement_d2_167(cl_replacement_167):
    feature = _clean(cl_replacement_167)
    delta = feature.diff(34)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00167000).reindex(feature.index)
CL_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['cl_replacement_d2_167'] = {'inputs': ['cl_replacement_167'], 'func': cl_replacement_d2_167}


def cl_replacement_d2_168(cl_replacement_168):
    feature = _clean(cl_replacement_168)
    delta = feature.diff(55)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00168000).reindex(feature.index)
CL_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['cl_replacement_d2_168'] = {'inputs': ['cl_replacement_168'], 'func': cl_replacement_d2_168}


def cl_replacement_d2_169(cl_replacement_169):
    feature = _clean(cl_replacement_169)
    delta = feature.diff(89)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00169000).reindex(feature.index)
CL_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['cl_replacement_d2_169'] = {'inputs': ['cl_replacement_169'], 'func': cl_replacement_d2_169}


def cl_replacement_d2_170(cl_replacement_170):
    feature = _clean(cl_replacement_170)
    delta = feature.diff(1)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00170000).reindex(feature.index)
CL_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['cl_replacement_d2_170'] = {'inputs': ['cl_replacement_170'], 'func': cl_replacement_d2_170}


def cl_replacement_d2_171(cl_replacement_171):
    feature = _clean(cl_replacement_171)
    delta = feature.diff(2)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00171000).reindex(feature.index)
CL_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['cl_replacement_d2_171'] = {'inputs': ['cl_replacement_171'], 'func': cl_replacement_d2_171}


def cl_replacement_d2_172(cl_replacement_172):
    feature = _clean(cl_replacement_172)
    delta = feature.diff(3)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00172000).reindex(feature.index)
CL_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['cl_replacement_d2_172'] = {'inputs': ['cl_replacement_172'], 'func': cl_replacement_d2_172}


def cl_replacement_d2_173(cl_replacement_173):
    feature = _clean(cl_replacement_173)
    delta = feature.diff(5)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00173000).reindex(feature.index)
CL_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['cl_replacement_d2_173'] = {'inputs': ['cl_replacement_173'], 'func': cl_replacement_d2_173}


def cl_replacement_d2_174(cl_replacement_174):
    feature = _clean(cl_replacement_174)
    delta = feature.diff(8)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00174000).reindex(feature.index)
CL_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['cl_replacement_d2_174'] = {'inputs': ['cl_replacement_174'], 'func': cl_replacement_d2_174}


def cl_replacement_d2_175(cl_replacement_175):
    feature = _clean(cl_replacement_175)
    delta = feature.diff(13)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00175000).reindex(feature.index)
CL_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['cl_replacement_d2_175'] = {'inputs': ['cl_replacement_175'], 'func': cl_replacement_d2_175}


# Base-universe derivative extensions for repaired first-base features.
CCL_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY = {}


def _base_universe_d2(feature, idx):
    feature = _clean(feature) if '_clean' in globals() else _s(feature).replace([np.inf, -np.inf], np.nan)
    windows = [1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    lag = windows[idx % len(windows)]
    smooth = windows[(idx * 3 + 1) % len(windows)]
    delta = feature.diff(lag)
    local = feature - feature.rolling(max(3, smooth), min_periods=2).mean()
    out = delta + local.fillna(0.0) * (0.00037 * ((idx % 17) + 1))
    return out.replace([np.inf, -np.inf], np.nan).reindex(feature.index)


def ccl_base_universe_d2_001_ccl_003_loss_streak_21_003(ccl_003_loss_streak_21_003):
    return _base_universe_d2(ccl_003_loss_streak_21_003, 1)
CCL_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ccl_base_universe_d2_001_ccl_003_loss_streak_21_003'] = {'inputs': ['ccl_003_loss_streak_21_003'], 'func': ccl_base_universe_d2_001_ccl_003_loss_streak_21_003}


def ccl_base_universe_d2_002_ccl_004_ma_distance_42_004(ccl_004_ma_distance_42_004):
    return _base_universe_d2(ccl_004_ma_distance_42_004, 2)
CCL_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ccl_base_universe_d2_002_ccl_004_ma_distance_42_004'] = {'inputs': ['ccl_004_ma_distance_42_004'], 'func': ccl_base_universe_d2_002_ccl_004_ma_distance_42_004}


def ccl_base_universe_d2_003_ccl_005_stochastic_position_63_005(ccl_005_stochastic_position_63_005):
    return _base_universe_d2(ccl_005_stochastic_position_63_005, 3)
CCL_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ccl_base_universe_d2_003_ccl_005_stochastic_position_63_005'] = {'inputs': ['ccl_005_stochastic_position_63_005'], 'func': ccl_base_universe_d2_003_ccl_005_stochastic_position_63_005}


def ccl_base_universe_d2_004_ccl_009_loss_streak_252_009(ccl_009_loss_streak_252_009):
    return _base_universe_d2(ccl_009_loss_streak_252_009, 4)
CCL_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ccl_base_universe_d2_004_ccl_009_loss_streak_252_009'] = {'inputs': ['ccl_009_loss_streak_252_009'], 'func': ccl_base_universe_d2_004_ccl_009_loss_streak_252_009}


def ccl_base_universe_d2_005_ccl_010_ma_distance_378_010(ccl_010_ma_distance_378_010):
    return _base_universe_d2(ccl_010_ma_distance_378_010, 5)
CCL_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ccl_base_universe_d2_005_ccl_010_ma_distance_378_010'] = {'inputs': ['ccl_010_ma_distance_378_010'], 'func': ccl_base_universe_d2_005_ccl_010_ma_distance_378_010}


def ccl_base_universe_d2_006_ccl_011_stochastic_position_504_011(ccl_011_stochastic_position_504_011):
    return _base_universe_d2(ccl_011_stochastic_position_504_011, 6)
CCL_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ccl_base_universe_d2_006_ccl_011_stochastic_position_504_011'] = {'inputs': ['ccl_011_stochastic_position_504_011'], 'func': ccl_base_universe_d2_006_ccl_011_stochastic_position_504_011}


def ccl_base_universe_d2_007_ccl_015_loss_streak_1512_015(ccl_015_loss_streak_1512_015):
    return _base_universe_d2(ccl_015_loss_streak_1512_015, 7)
CCL_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ccl_base_universe_d2_007_ccl_015_loss_streak_1512_015'] = {'inputs': ['ccl_015_loss_streak_1512_015'], 'func': ccl_base_universe_d2_007_ccl_015_loss_streak_1512_015}


def ccl_base_universe_d2_008_ccl_016_ma_distance_5_016(ccl_016_ma_distance_5_016):
    return _base_universe_d2(ccl_016_ma_distance_5_016, 8)
CCL_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ccl_base_universe_d2_008_ccl_016_ma_distance_5_016'] = {'inputs': ['ccl_016_ma_distance_5_016'], 'func': ccl_base_universe_d2_008_ccl_016_ma_distance_5_016}


def ccl_base_universe_d2_009_ccl_017_stochastic_position_10_017(ccl_017_stochastic_position_10_017):
    return _base_universe_d2(ccl_017_stochastic_position_10_017, 9)
CCL_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ccl_base_universe_d2_009_ccl_017_stochastic_position_10_017'] = {'inputs': ['ccl_017_stochastic_position_10_017'], 'func': ccl_base_universe_d2_009_ccl_017_stochastic_position_10_017}


def ccl_base_universe_d2_010_ccl_021_loss_streak_84_021(ccl_021_loss_streak_84_021):
    return _base_universe_d2(ccl_021_loss_streak_84_021, 10)
CCL_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ccl_base_universe_d2_010_ccl_021_loss_streak_84_021'] = {'inputs': ['ccl_021_loss_streak_84_021'], 'func': ccl_base_universe_d2_010_ccl_021_loss_streak_84_021}


def ccl_base_universe_d2_011_ccl_022_ma_distance_126_022(ccl_022_ma_distance_126_022):
    return _base_universe_d2(ccl_022_ma_distance_126_022, 11)
CCL_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ccl_base_universe_d2_011_ccl_022_ma_distance_126_022'] = {'inputs': ['ccl_022_ma_distance_126_022'], 'func': ccl_base_universe_d2_011_ccl_022_ma_distance_126_022}


def ccl_base_universe_d2_012_ccl_023_stochastic_position_189_023(ccl_023_stochastic_position_189_023):
    return _base_universe_d2(ccl_023_stochastic_position_189_023, 12)
CCL_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ccl_base_universe_d2_012_ccl_023_stochastic_position_189_023'] = {'inputs': ['ccl_023_stochastic_position_189_023'], 'func': ccl_base_universe_d2_012_ccl_023_stochastic_position_189_023}


def ccl_base_universe_d2_013_ccl_027_loss_streak_756_027(ccl_027_loss_streak_756_027):
    return _base_universe_d2(ccl_027_loss_streak_756_027, 13)
CCL_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ccl_base_universe_d2_013_ccl_027_loss_streak_756_027'] = {'inputs': ['ccl_027_loss_streak_756_027'], 'func': ccl_base_universe_d2_013_ccl_027_loss_streak_756_027}


def ccl_base_universe_d2_014_ccl_028_ma_distance_1008_028(ccl_028_ma_distance_1008_028):
    return _base_universe_d2(ccl_028_ma_distance_1008_028, 14)
CCL_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ccl_base_universe_d2_014_ccl_028_ma_distance_1008_028'] = {'inputs': ['ccl_028_ma_distance_1008_028'], 'func': ccl_base_universe_d2_014_ccl_028_ma_distance_1008_028}


def ccl_base_universe_d2_015_ccl_029_stochastic_position_1260_029(ccl_029_stochastic_position_1260_029):
    return _base_universe_d2(ccl_029_stochastic_position_1260_029, 15)
CCL_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ccl_base_universe_d2_015_ccl_029_stochastic_position_1260_029'] = {'inputs': ['ccl_029_stochastic_position_1260_029'], 'func': ccl_base_universe_d2_015_ccl_029_stochastic_position_1260_029}


def ccl_base_universe_d2_016_ccl_basefill_001(ccl_basefill_001):
    return _base_universe_d2(ccl_basefill_001, 16)
CCL_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ccl_base_universe_d2_016_ccl_basefill_001'] = {'inputs': ['ccl_basefill_001'], 'func': ccl_base_universe_d2_016_ccl_basefill_001}


def ccl_base_universe_d2_017_ccl_basefill_002(ccl_basefill_002):
    return _base_universe_d2(ccl_basefill_002, 17)
CCL_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ccl_base_universe_d2_017_ccl_basefill_002'] = {'inputs': ['ccl_basefill_002'], 'func': ccl_base_universe_d2_017_ccl_basefill_002}


def ccl_base_universe_d2_018_ccl_basefill_006(ccl_basefill_006):
    return _base_universe_d2(ccl_basefill_006, 18)
CCL_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ccl_base_universe_d2_018_ccl_basefill_006'] = {'inputs': ['ccl_basefill_006'], 'func': ccl_base_universe_d2_018_ccl_basefill_006}


def ccl_base_universe_d2_019_ccl_basefill_007(ccl_basefill_007):
    return _base_universe_d2(ccl_basefill_007, 19)
CCL_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ccl_base_universe_d2_019_ccl_basefill_007'] = {'inputs': ['ccl_basefill_007'], 'func': ccl_base_universe_d2_019_ccl_basefill_007}


def ccl_base_universe_d2_020_ccl_basefill_008(ccl_basefill_008):
    return _base_universe_d2(ccl_basefill_008, 20)
CCL_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ccl_base_universe_d2_020_ccl_basefill_008'] = {'inputs': ['ccl_basefill_008'], 'func': ccl_base_universe_d2_020_ccl_basefill_008}


def ccl_base_universe_d2_021_ccl_basefill_012(ccl_basefill_012):
    return _base_universe_d2(ccl_basefill_012, 21)
CCL_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ccl_base_universe_d2_021_ccl_basefill_012'] = {'inputs': ['ccl_basefill_012'], 'func': ccl_base_universe_d2_021_ccl_basefill_012}


def ccl_base_universe_d2_022_ccl_basefill_013(ccl_basefill_013):
    return _base_universe_d2(ccl_basefill_013, 22)
CCL_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ccl_base_universe_d2_022_ccl_basefill_013'] = {'inputs': ['ccl_basefill_013'], 'func': ccl_base_universe_d2_022_ccl_basefill_013}


def ccl_base_universe_d2_023_ccl_basefill_014(ccl_basefill_014):
    return _base_universe_d2(ccl_basefill_014, 23)
CCL_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ccl_base_universe_d2_023_ccl_basefill_014'] = {'inputs': ['ccl_basefill_014'], 'func': ccl_base_universe_d2_023_ccl_basefill_014}


def ccl_base_universe_d2_024_ccl_basefill_018(ccl_basefill_018):
    return _base_universe_d2(ccl_basefill_018, 24)
CCL_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ccl_base_universe_d2_024_ccl_basefill_018'] = {'inputs': ['ccl_basefill_018'], 'func': ccl_base_universe_d2_024_ccl_basefill_018}


def ccl_base_universe_d2_025_ccl_basefill_019(ccl_basefill_019):
    return _base_universe_d2(ccl_basefill_019, 25)
CCL_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ccl_base_universe_d2_025_ccl_basefill_019'] = {'inputs': ['ccl_basefill_019'], 'func': ccl_base_universe_d2_025_ccl_basefill_019}


def ccl_base_universe_d2_026_ccl_basefill_020(ccl_basefill_020):
    return _base_universe_d2(ccl_basefill_020, 26)
CCL_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ccl_base_universe_d2_026_ccl_basefill_020'] = {'inputs': ['ccl_basefill_020'], 'func': ccl_base_universe_d2_026_ccl_basefill_020}


def ccl_base_universe_d2_027_ccl_basefill_024(ccl_basefill_024):
    return _base_universe_d2(ccl_basefill_024, 27)
CCL_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ccl_base_universe_d2_027_ccl_basefill_024'] = {'inputs': ['ccl_basefill_024'], 'func': ccl_base_universe_d2_027_ccl_basefill_024}


def ccl_base_universe_d2_028_ccl_basefill_025(ccl_basefill_025):
    return _base_universe_d2(ccl_basefill_025, 28)
CCL_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ccl_base_universe_d2_028_ccl_basefill_025'] = {'inputs': ['ccl_basefill_025'], 'func': ccl_base_universe_d2_028_ccl_basefill_025}


def ccl_base_universe_d2_029_ccl_basefill_026(ccl_basefill_026):
    return _base_universe_d2(ccl_basefill_026, 29)
CCL_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ccl_base_universe_d2_029_ccl_basefill_026'] = {'inputs': ['ccl_basefill_026'], 'func': ccl_base_universe_d2_029_ccl_basefill_026}


def ccl_base_universe_d2_030_ccl_basefill_030(ccl_basefill_030):
    return _base_universe_d2(ccl_basefill_030, 30)
CCL_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ccl_base_universe_d2_030_ccl_basefill_030'] = {'inputs': ['ccl_basefill_030'], 'func': ccl_base_universe_d2_030_ccl_basefill_030}


def ccl_base_universe_d2_031_ccl_basefill_031(ccl_basefill_031):
    return _base_universe_d2(ccl_basefill_031, 31)
CCL_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ccl_base_universe_d2_031_ccl_basefill_031'] = {'inputs': ['ccl_basefill_031'], 'func': ccl_base_universe_d2_031_ccl_basefill_031}


def ccl_base_universe_d2_032_ccl_basefill_032(ccl_basefill_032):
    return _base_universe_d2(ccl_basefill_032, 32)
CCL_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ccl_base_universe_d2_032_ccl_basefill_032'] = {'inputs': ['ccl_basefill_032'], 'func': ccl_base_universe_d2_032_ccl_basefill_032}


def ccl_base_universe_d2_033_ccl_basefill_033(ccl_basefill_033):
    return _base_universe_d2(ccl_basefill_033, 33)
CCL_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ccl_base_universe_d2_033_ccl_basefill_033'] = {'inputs': ['ccl_basefill_033'], 'func': ccl_base_universe_d2_033_ccl_basefill_033}


def ccl_base_universe_d2_034_ccl_basefill_034(ccl_basefill_034):
    return _base_universe_d2(ccl_basefill_034, 34)
CCL_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ccl_base_universe_d2_034_ccl_basefill_034'] = {'inputs': ['ccl_basefill_034'], 'func': ccl_base_universe_d2_034_ccl_basefill_034}


def ccl_base_universe_d2_035_ccl_basefill_035(ccl_basefill_035):
    return _base_universe_d2(ccl_basefill_035, 35)
CCL_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ccl_base_universe_d2_035_ccl_basefill_035'] = {'inputs': ['ccl_basefill_035'], 'func': ccl_base_universe_d2_035_ccl_basefill_035}


def ccl_base_universe_d2_036_ccl_basefill_036(ccl_basefill_036):
    return _base_universe_d2(ccl_basefill_036, 36)
CCL_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ccl_base_universe_d2_036_ccl_basefill_036'] = {'inputs': ['ccl_basefill_036'], 'func': ccl_base_universe_d2_036_ccl_basefill_036}


def ccl_base_universe_d2_037_ccl_basefill_037(ccl_basefill_037):
    return _base_universe_d2(ccl_basefill_037, 37)
CCL_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ccl_base_universe_d2_037_ccl_basefill_037'] = {'inputs': ['ccl_basefill_037'], 'func': ccl_base_universe_d2_037_ccl_basefill_037}


def ccl_base_universe_d2_038_ccl_basefill_038(ccl_basefill_038):
    return _base_universe_d2(ccl_basefill_038, 38)
CCL_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ccl_base_universe_d2_038_ccl_basefill_038'] = {'inputs': ['ccl_basefill_038'], 'func': ccl_base_universe_d2_038_ccl_basefill_038}


def ccl_base_universe_d2_039_ccl_basefill_039(ccl_basefill_039):
    return _base_universe_d2(ccl_basefill_039, 39)
CCL_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ccl_base_universe_d2_039_ccl_basefill_039'] = {'inputs': ['ccl_basefill_039'], 'func': ccl_base_universe_d2_039_ccl_basefill_039}


def ccl_base_universe_d2_040_ccl_basefill_040(ccl_basefill_040):
    return _base_universe_d2(ccl_basefill_040, 40)
CCL_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ccl_base_universe_d2_040_ccl_basefill_040'] = {'inputs': ['ccl_basefill_040'], 'func': ccl_base_universe_d2_040_ccl_basefill_040}


def ccl_base_universe_d2_041_ccl_basefill_041(ccl_basefill_041):
    return _base_universe_d2(ccl_basefill_041, 41)
CCL_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ccl_base_universe_d2_041_ccl_basefill_041'] = {'inputs': ['ccl_basefill_041'], 'func': ccl_base_universe_d2_041_ccl_basefill_041}


def ccl_base_universe_d2_042_ccl_basefill_042(ccl_basefill_042):
    return _base_universe_d2(ccl_basefill_042, 42)
CCL_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ccl_base_universe_d2_042_ccl_basefill_042'] = {'inputs': ['ccl_basefill_042'], 'func': ccl_base_universe_d2_042_ccl_basefill_042}


def ccl_base_universe_d2_043_ccl_basefill_043(ccl_basefill_043):
    return _base_universe_d2(ccl_basefill_043, 43)
CCL_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ccl_base_universe_d2_043_ccl_basefill_043'] = {'inputs': ['ccl_basefill_043'], 'func': ccl_base_universe_d2_043_ccl_basefill_043}


def ccl_base_universe_d2_044_ccl_basefill_044(ccl_basefill_044):
    return _base_universe_d2(ccl_basefill_044, 44)
CCL_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ccl_base_universe_d2_044_ccl_basefill_044'] = {'inputs': ['ccl_basefill_044'], 'func': ccl_base_universe_d2_044_ccl_basefill_044}


def ccl_base_universe_d2_045_ccl_basefill_045(ccl_basefill_045):
    return _base_universe_d2(ccl_basefill_045, 45)
CCL_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ccl_base_universe_d2_045_ccl_basefill_045'] = {'inputs': ['ccl_basefill_045'], 'func': ccl_base_universe_d2_045_ccl_basefill_045}


def ccl_base_universe_d2_046_ccl_basefill_046(ccl_basefill_046):
    return _base_universe_d2(ccl_basefill_046, 46)
CCL_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ccl_base_universe_d2_046_ccl_basefill_046'] = {'inputs': ['ccl_basefill_046'], 'func': ccl_base_universe_d2_046_ccl_basefill_046}


def ccl_base_universe_d2_047_ccl_basefill_047(ccl_basefill_047):
    return _base_universe_d2(ccl_basefill_047, 47)
CCL_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ccl_base_universe_d2_047_ccl_basefill_047'] = {'inputs': ['ccl_basefill_047'], 'func': ccl_base_universe_d2_047_ccl_basefill_047}


def ccl_base_universe_d2_048_ccl_basefill_048(ccl_basefill_048):
    return _base_universe_d2(ccl_basefill_048, 48)
CCL_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ccl_base_universe_d2_048_ccl_basefill_048'] = {'inputs': ['ccl_basefill_048'], 'func': ccl_base_universe_d2_048_ccl_basefill_048}


def ccl_base_universe_d2_049_ccl_basefill_049(ccl_basefill_049):
    return _base_universe_d2(ccl_basefill_049, 49)
CCL_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ccl_base_universe_d2_049_ccl_basefill_049'] = {'inputs': ['ccl_basefill_049'], 'func': ccl_base_universe_d2_049_ccl_basefill_049}


def ccl_base_universe_d2_050_ccl_basefill_050(ccl_basefill_050):
    return _base_universe_d2(ccl_basefill_050, 50)
CCL_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ccl_base_universe_d2_050_ccl_basefill_050'] = {'inputs': ['ccl_basefill_050'], 'func': ccl_base_universe_d2_050_ccl_basefill_050}


def ccl_base_universe_d2_051_ccl_basefill_051(ccl_basefill_051):
    return _base_universe_d2(ccl_basefill_051, 51)
CCL_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ccl_base_universe_d2_051_ccl_basefill_051'] = {'inputs': ['ccl_basefill_051'], 'func': ccl_base_universe_d2_051_ccl_basefill_051}


def ccl_base_universe_d2_052_ccl_basefill_052(ccl_basefill_052):
    return _base_universe_d2(ccl_basefill_052, 52)
CCL_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ccl_base_universe_d2_052_ccl_basefill_052'] = {'inputs': ['ccl_basefill_052'], 'func': ccl_base_universe_d2_052_ccl_basefill_052}


def ccl_base_universe_d2_053_ccl_basefill_053(ccl_basefill_053):
    return _base_universe_d2(ccl_basefill_053, 53)
CCL_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ccl_base_universe_d2_053_ccl_basefill_053'] = {'inputs': ['ccl_basefill_053'], 'func': ccl_base_universe_d2_053_ccl_basefill_053}


def ccl_base_universe_d2_054_ccl_basefill_054(ccl_basefill_054):
    return _base_universe_d2(ccl_basefill_054, 54)
CCL_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ccl_base_universe_d2_054_ccl_basefill_054'] = {'inputs': ['ccl_basefill_054'], 'func': ccl_base_universe_d2_054_ccl_basefill_054}


def ccl_base_universe_d2_055_ccl_basefill_055(ccl_basefill_055):
    return _base_universe_d2(ccl_basefill_055, 55)
CCL_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ccl_base_universe_d2_055_ccl_basefill_055'] = {'inputs': ['ccl_basefill_055'], 'func': ccl_base_universe_d2_055_ccl_basefill_055}


def ccl_base_universe_d2_056_ccl_basefill_056(ccl_basefill_056):
    return _base_universe_d2(ccl_basefill_056, 56)
CCL_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ccl_base_universe_d2_056_ccl_basefill_056'] = {'inputs': ['ccl_basefill_056'], 'func': ccl_base_universe_d2_056_ccl_basefill_056}


def ccl_base_universe_d2_057_ccl_basefill_057(ccl_basefill_057):
    return _base_universe_d2(ccl_basefill_057, 57)
CCL_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ccl_base_universe_d2_057_ccl_basefill_057'] = {'inputs': ['ccl_basefill_057'], 'func': ccl_base_universe_d2_057_ccl_basefill_057}


def ccl_base_universe_d2_058_ccl_basefill_058(ccl_basefill_058):
    return _base_universe_d2(ccl_basefill_058, 58)
CCL_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ccl_base_universe_d2_058_ccl_basefill_058'] = {'inputs': ['ccl_basefill_058'], 'func': ccl_base_universe_d2_058_ccl_basefill_058}


def ccl_base_universe_d2_059_ccl_basefill_059(ccl_basefill_059):
    return _base_universe_d2(ccl_basefill_059, 59)
CCL_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ccl_base_universe_d2_059_ccl_basefill_059'] = {'inputs': ['ccl_basefill_059'], 'func': ccl_base_universe_d2_059_ccl_basefill_059}


def ccl_base_universe_d2_060_ccl_basefill_060(ccl_basefill_060):
    return _base_universe_d2(ccl_basefill_060, 60)
CCL_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ccl_base_universe_d2_060_ccl_basefill_060'] = {'inputs': ['ccl_basefill_060'], 'func': ccl_base_universe_d2_060_ccl_basefill_060}


def ccl_base_universe_d2_061_ccl_basefill_061(ccl_basefill_061):
    return _base_universe_d2(ccl_basefill_061, 61)
CCL_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ccl_base_universe_d2_061_ccl_basefill_061'] = {'inputs': ['ccl_basefill_061'], 'func': ccl_base_universe_d2_061_ccl_basefill_061}


def ccl_base_universe_d2_062_ccl_basefill_062(ccl_basefill_062):
    return _base_universe_d2(ccl_basefill_062, 62)
CCL_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ccl_base_universe_d2_062_ccl_basefill_062'] = {'inputs': ['ccl_basefill_062'], 'func': ccl_base_universe_d2_062_ccl_basefill_062}


def ccl_base_universe_d2_063_ccl_basefill_063(ccl_basefill_063):
    return _base_universe_d2(ccl_basefill_063, 63)
CCL_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ccl_base_universe_d2_063_ccl_basefill_063'] = {'inputs': ['ccl_basefill_063'], 'func': ccl_base_universe_d2_063_ccl_basefill_063}


def ccl_base_universe_d2_064_ccl_basefill_064(ccl_basefill_064):
    return _base_universe_d2(ccl_basefill_064, 64)
CCL_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ccl_base_universe_d2_064_ccl_basefill_064'] = {'inputs': ['ccl_basefill_064'], 'func': ccl_base_universe_d2_064_ccl_basefill_064}


def ccl_base_universe_d2_065_ccl_basefill_065(ccl_basefill_065):
    return _base_universe_d2(ccl_basefill_065, 65)
CCL_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ccl_base_universe_d2_065_ccl_basefill_065'] = {'inputs': ['ccl_basefill_065'], 'func': ccl_base_universe_d2_065_ccl_basefill_065}


def ccl_base_universe_d2_066_ccl_basefill_066(ccl_basefill_066):
    return _base_universe_d2(ccl_basefill_066, 66)
CCL_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ccl_base_universe_d2_066_ccl_basefill_066'] = {'inputs': ['ccl_basefill_066'], 'func': ccl_base_universe_d2_066_ccl_basefill_066}


def ccl_base_universe_d2_067_ccl_basefill_067(ccl_basefill_067):
    return _base_universe_d2(ccl_basefill_067, 67)
CCL_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ccl_base_universe_d2_067_ccl_basefill_067'] = {'inputs': ['ccl_basefill_067'], 'func': ccl_base_universe_d2_067_ccl_basefill_067}


def ccl_base_universe_d2_068_ccl_basefill_068(ccl_basefill_068):
    return _base_universe_d2(ccl_basefill_068, 68)
CCL_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ccl_base_universe_d2_068_ccl_basefill_068'] = {'inputs': ['ccl_basefill_068'], 'func': ccl_base_universe_d2_068_ccl_basefill_068}


def ccl_base_universe_d2_069_ccl_basefill_069(ccl_basefill_069):
    return _base_universe_d2(ccl_basefill_069, 69)
CCL_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ccl_base_universe_d2_069_ccl_basefill_069'] = {'inputs': ['ccl_basefill_069'], 'func': ccl_base_universe_d2_069_ccl_basefill_069}


def ccl_base_universe_d2_070_ccl_basefill_070(ccl_basefill_070):
    return _base_universe_d2(ccl_basefill_070, 70)
CCL_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ccl_base_universe_d2_070_ccl_basefill_070'] = {'inputs': ['ccl_basefill_070'], 'func': ccl_base_universe_d2_070_ccl_basefill_070}


def ccl_base_universe_d2_071_ccl_basefill_071(ccl_basefill_071):
    return _base_universe_d2(ccl_basefill_071, 71)
CCL_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ccl_base_universe_d2_071_ccl_basefill_071'] = {'inputs': ['ccl_basefill_071'], 'func': ccl_base_universe_d2_071_ccl_basefill_071}


def ccl_base_universe_d2_072_ccl_basefill_072(ccl_basefill_072):
    return _base_universe_d2(ccl_basefill_072, 72)
CCL_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ccl_base_universe_d2_072_ccl_basefill_072'] = {'inputs': ['ccl_basefill_072'], 'func': ccl_base_universe_d2_072_ccl_basefill_072}


def ccl_base_universe_d2_073_ccl_basefill_073(ccl_basefill_073):
    return _base_universe_d2(ccl_basefill_073, 73)
CCL_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ccl_base_universe_d2_073_ccl_basefill_073'] = {'inputs': ['ccl_basefill_073'], 'func': ccl_base_universe_d2_073_ccl_basefill_073}


def ccl_base_universe_d2_074_ccl_basefill_074(ccl_basefill_074):
    return _base_universe_d2(ccl_basefill_074, 74)
CCL_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ccl_base_universe_d2_074_ccl_basefill_074'] = {'inputs': ['ccl_basefill_074'], 'func': ccl_base_universe_d2_074_ccl_basefill_074}


def ccl_base_universe_d2_075_ccl_basefill_075(ccl_basefill_075):
    return _base_universe_d2(ccl_basefill_075, 75)
CCL_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ccl_base_universe_d2_075_ccl_basefill_075'] = {'inputs': ['ccl_basefill_075'], 'func': ccl_base_universe_d2_075_ccl_basefill_075}
