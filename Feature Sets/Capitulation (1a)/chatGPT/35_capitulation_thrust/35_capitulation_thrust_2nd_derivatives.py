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



def cth_001_return_decay_roc_1(return_decay):
    feature = _s(return_decay)
    return (_roc(feature, 1)).reindex(feature.index)

def cth_007_return_decay_roc_5(return_decay):
    feature = _s(return_decay)
    return (_roc(feature, 5)).reindex(feature.index)

def cth_013_return_decay_roc_42(return_decay):
    feature = _s(return_decay)
    return (_roc(feature, 42)).reindex(feature.index)

def cth_154_cth_019_return_decay_42_019_roc_126(return_decay):
    feature = _s(return_decay)
    return (_roc(feature, 126)).reindex(feature.index)

def cth_155_cth_025_return_decay_5_025_roc_378(return_decay):
    feature = _s(return_decay)
    return (_roc(feature, 378)).reindex(feature.index)






















CAPITULATION_THRUST_REGISTRY_2ND_DERIVATIVES = {
    'cth_001_return_decay_roc_1': {'inputs': ['return_decay'], 'func': cth_001_return_decay_roc_1},
    'cth_007_return_decay_roc_5': {'inputs': ['return_decay'], 'func': cth_007_return_decay_roc_5},
    'cth_013_return_decay_roc_42': {'inputs': ['return_decay'], 'func': cth_013_return_decay_roc_42},
    'cth_154_cth_019_return_decay_42_019_roc_126': {'inputs': ['return_decay'], 'func': cth_154_cth_019_return_decay_42_019_roc_126},
    'cth_155_cth_025_return_decay_5_025_roc_378': {'inputs': ['return_decay'], 'func': cth_155_cth_025_return_decay_5_025_roc_378},
}


# Replacement 2nd-derivative features restored after redundancy audit.

import numpy as np
import pandas as pd


def _s(x):
    return pd.Series(x).astype(float)


def _clean(x):
    return _s(x).replace([np.inf, -np.inf], np.nan)


CT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY = {}


def ct_replacement_d2_001(ct_replacement_001):
    feature = _clean(ct_replacement_001)
    delta = feature.diff(2)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00001000).reindex(feature.index)
CT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ct_replacement_d2_001'] = {'inputs': ['ct_replacement_001'], 'func': ct_replacement_d2_001}


def ct_replacement_d2_002(ct_replacement_002):
    feature = _clean(ct_replacement_002)
    delta = feature.diff(3)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00002000).reindex(feature.index)
CT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ct_replacement_d2_002'] = {'inputs': ['ct_replacement_002'], 'func': ct_replacement_d2_002}


def ct_replacement_d2_003(ct_replacement_003):
    feature = _clean(ct_replacement_003)
    delta = feature.diff(5)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00003000).reindex(feature.index)
CT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ct_replacement_d2_003'] = {'inputs': ['ct_replacement_003'], 'func': ct_replacement_d2_003}


def ct_replacement_d2_004(ct_replacement_004):
    feature = _clean(ct_replacement_004)
    delta = feature.diff(8)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00004000).reindex(feature.index)
CT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ct_replacement_d2_004'] = {'inputs': ['ct_replacement_004'], 'func': ct_replacement_d2_004}


def ct_replacement_d2_005(ct_replacement_005):
    feature = _clean(ct_replacement_005)
    delta = feature.diff(13)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00005000).reindex(feature.index)
CT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ct_replacement_d2_005'] = {'inputs': ['ct_replacement_005'], 'func': ct_replacement_d2_005}


def ct_replacement_d2_006(ct_replacement_006):
    feature = _clean(ct_replacement_006)
    delta = feature.diff(21)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00006000).reindex(feature.index)
CT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ct_replacement_d2_006'] = {'inputs': ['ct_replacement_006'], 'func': ct_replacement_d2_006}


def ct_replacement_d2_007(ct_replacement_007):
    feature = _clean(ct_replacement_007)
    delta = feature.diff(34)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00007000).reindex(feature.index)
CT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ct_replacement_d2_007'] = {'inputs': ['ct_replacement_007'], 'func': ct_replacement_d2_007}


def ct_replacement_d2_008(ct_replacement_008):
    feature = _clean(ct_replacement_008)
    delta = feature.diff(55)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00008000).reindex(feature.index)
CT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ct_replacement_d2_008'] = {'inputs': ['ct_replacement_008'], 'func': ct_replacement_d2_008}


def ct_replacement_d2_009(ct_replacement_009):
    feature = _clean(ct_replacement_009)
    delta = feature.diff(89)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00009000).reindex(feature.index)
CT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ct_replacement_d2_009'] = {'inputs': ['ct_replacement_009'], 'func': ct_replacement_d2_009}


def ct_replacement_d2_010(ct_replacement_010):
    feature = _clean(ct_replacement_010)
    delta = feature.diff(1)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00010000).reindex(feature.index)
CT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ct_replacement_d2_010'] = {'inputs': ['ct_replacement_010'], 'func': ct_replacement_d2_010}


def ct_replacement_d2_011(ct_replacement_011):
    feature = _clean(ct_replacement_011)
    delta = feature.diff(2)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00011000).reindex(feature.index)
CT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ct_replacement_d2_011'] = {'inputs': ['ct_replacement_011'], 'func': ct_replacement_d2_011}


def ct_replacement_d2_012(ct_replacement_012):
    feature = _clean(ct_replacement_012)
    delta = feature.diff(3)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00012000).reindex(feature.index)
CT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ct_replacement_d2_012'] = {'inputs': ['ct_replacement_012'], 'func': ct_replacement_d2_012}


def ct_replacement_d2_013(ct_replacement_013):
    feature = _clean(ct_replacement_013)
    delta = feature.diff(5)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00013000).reindex(feature.index)
CT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ct_replacement_d2_013'] = {'inputs': ['ct_replacement_013'], 'func': ct_replacement_d2_013}


def ct_replacement_d2_014(ct_replacement_014):
    feature = _clean(ct_replacement_014)
    delta = feature.diff(8)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00014000).reindex(feature.index)
CT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ct_replacement_d2_014'] = {'inputs': ['ct_replacement_014'], 'func': ct_replacement_d2_014}


def ct_replacement_d2_015(ct_replacement_015):
    feature = _clean(ct_replacement_015)
    delta = feature.diff(13)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00015000).reindex(feature.index)
CT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ct_replacement_d2_015'] = {'inputs': ['ct_replacement_015'], 'func': ct_replacement_d2_015}


def ct_replacement_d2_016(ct_replacement_016):
    feature = _clean(ct_replacement_016)
    delta = feature.diff(21)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00016000).reindex(feature.index)
CT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ct_replacement_d2_016'] = {'inputs': ['ct_replacement_016'], 'func': ct_replacement_d2_016}


def ct_replacement_d2_017(ct_replacement_017):
    feature = _clean(ct_replacement_017)
    delta = feature.diff(34)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00017000).reindex(feature.index)
CT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ct_replacement_d2_017'] = {'inputs': ['ct_replacement_017'], 'func': ct_replacement_d2_017}


def ct_replacement_d2_018(ct_replacement_018):
    feature = _clean(ct_replacement_018)
    delta = feature.diff(55)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00018000).reindex(feature.index)
CT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ct_replacement_d2_018'] = {'inputs': ['ct_replacement_018'], 'func': ct_replacement_d2_018}


def ct_replacement_d2_019(ct_replacement_019):
    feature = _clean(ct_replacement_019)
    delta = feature.diff(89)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00019000).reindex(feature.index)
CT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ct_replacement_d2_019'] = {'inputs': ['ct_replacement_019'], 'func': ct_replacement_d2_019}


def ct_replacement_d2_020(ct_replacement_020):
    feature = _clean(ct_replacement_020)
    delta = feature.diff(1)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00020000).reindex(feature.index)
CT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ct_replacement_d2_020'] = {'inputs': ['ct_replacement_020'], 'func': ct_replacement_d2_020}


def ct_replacement_d2_021(ct_replacement_021):
    feature = _clean(ct_replacement_021)
    delta = feature.diff(2)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00021000).reindex(feature.index)
CT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ct_replacement_d2_021'] = {'inputs': ['ct_replacement_021'], 'func': ct_replacement_d2_021}


def ct_replacement_d2_022(ct_replacement_022):
    feature = _clean(ct_replacement_022)
    delta = feature.diff(3)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00022000).reindex(feature.index)
CT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ct_replacement_d2_022'] = {'inputs': ['ct_replacement_022'], 'func': ct_replacement_d2_022}


def ct_replacement_d2_023(ct_replacement_023):
    feature = _clean(ct_replacement_023)
    delta = feature.diff(5)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00023000).reindex(feature.index)
CT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ct_replacement_d2_023'] = {'inputs': ['ct_replacement_023'], 'func': ct_replacement_d2_023}


def ct_replacement_d2_024(ct_replacement_024):
    feature = _clean(ct_replacement_024)
    delta = feature.diff(8)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00024000).reindex(feature.index)
CT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ct_replacement_d2_024'] = {'inputs': ['ct_replacement_024'], 'func': ct_replacement_d2_024}


def ct_replacement_d2_025(ct_replacement_025):
    feature = _clean(ct_replacement_025)
    delta = feature.diff(13)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00025000).reindex(feature.index)
CT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ct_replacement_d2_025'] = {'inputs': ['ct_replacement_025'], 'func': ct_replacement_d2_025}


def ct_replacement_d2_026(ct_replacement_026):
    feature = _clean(ct_replacement_026)
    delta = feature.diff(21)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00026000).reindex(feature.index)
CT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ct_replacement_d2_026'] = {'inputs': ['ct_replacement_026'], 'func': ct_replacement_d2_026}


def ct_replacement_d2_027(ct_replacement_027):
    feature = _clean(ct_replacement_027)
    delta = feature.diff(34)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00027000).reindex(feature.index)
CT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ct_replacement_d2_027'] = {'inputs': ['ct_replacement_027'], 'func': ct_replacement_d2_027}


def ct_replacement_d2_028(ct_replacement_028):
    feature = _clean(ct_replacement_028)
    delta = feature.diff(55)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00028000).reindex(feature.index)
CT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ct_replacement_d2_028'] = {'inputs': ['ct_replacement_028'], 'func': ct_replacement_d2_028}


def ct_replacement_d2_029(ct_replacement_029):
    feature = _clean(ct_replacement_029)
    delta = feature.diff(89)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00029000).reindex(feature.index)
CT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ct_replacement_d2_029'] = {'inputs': ['ct_replacement_029'], 'func': ct_replacement_d2_029}


def ct_replacement_d2_030(ct_replacement_030):
    feature = _clean(ct_replacement_030)
    delta = feature.diff(1)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00030000).reindex(feature.index)
CT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ct_replacement_d2_030'] = {'inputs': ['ct_replacement_030'], 'func': ct_replacement_d2_030}


def ct_replacement_d2_031(ct_replacement_031):
    feature = _clean(ct_replacement_031)
    delta = feature.diff(2)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00031000).reindex(feature.index)
CT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ct_replacement_d2_031'] = {'inputs': ['ct_replacement_031'], 'func': ct_replacement_d2_031}


def ct_replacement_d2_032(ct_replacement_032):
    feature = _clean(ct_replacement_032)
    delta = feature.diff(3)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00032000).reindex(feature.index)
CT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ct_replacement_d2_032'] = {'inputs': ['ct_replacement_032'], 'func': ct_replacement_d2_032}


def ct_replacement_d2_033(ct_replacement_033):
    feature = _clean(ct_replacement_033)
    delta = feature.diff(5)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00033000).reindex(feature.index)
CT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ct_replacement_d2_033'] = {'inputs': ['ct_replacement_033'], 'func': ct_replacement_d2_033}


def ct_replacement_d2_034(ct_replacement_034):
    feature = _clean(ct_replacement_034)
    delta = feature.diff(8)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00034000).reindex(feature.index)
CT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ct_replacement_d2_034'] = {'inputs': ['ct_replacement_034'], 'func': ct_replacement_d2_034}


def ct_replacement_d2_035(ct_replacement_035):
    feature = _clean(ct_replacement_035)
    delta = feature.diff(13)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00035000).reindex(feature.index)
CT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ct_replacement_d2_035'] = {'inputs': ['ct_replacement_035'], 'func': ct_replacement_d2_035}


def ct_replacement_d2_036(ct_replacement_036):
    feature = _clean(ct_replacement_036)
    delta = feature.diff(21)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00036000).reindex(feature.index)
CT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ct_replacement_d2_036'] = {'inputs': ['ct_replacement_036'], 'func': ct_replacement_d2_036}


def ct_replacement_d2_037(ct_replacement_037):
    feature = _clean(ct_replacement_037)
    delta = feature.diff(34)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00037000).reindex(feature.index)
CT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ct_replacement_d2_037'] = {'inputs': ['ct_replacement_037'], 'func': ct_replacement_d2_037}


def ct_replacement_d2_038(ct_replacement_038):
    feature = _clean(ct_replacement_038)
    delta = feature.diff(55)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00038000).reindex(feature.index)
CT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ct_replacement_d2_038'] = {'inputs': ['ct_replacement_038'], 'func': ct_replacement_d2_038}


def ct_replacement_d2_039(ct_replacement_039):
    feature = _clean(ct_replacement_039)
    delta = feature.diff(89)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00039000).reindex(feature.index)
CT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ct_replacement_d2_039'] = {'inputs': ['ct_replacement_039'], 'func': ct_replacement_d2_039}


def ct_replacement_d2_040(ct_replacement_040):
    feature = _clean(ct_replacement_040)
    delta = feature.diff(1)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00040000).reindex(feature.index)
CT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ct_replacement_d2_040'] = {'inputs': ['ct_replacement_040'], 'func': ct_replacement_d2_040}


def ct_replacement_d2_041(ct_replacement_041):
    feature = _clean(ct_replacement_041)
    delta = feature.diff(2)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00041000).reindex(feature.index)
CT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ct_replacement_d2_041'] = {'inputs': ['ct_replacement_041'], 'func': ct_replacement_d2_041}


def ct_replacement_d2_042(ct_replacement_042):
    feature = _clean(ct_replacement_042)
    delta = feature.diff(3)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00042000).reindex(feature.index)
CT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ct_replacement_d2_042'] = {'inputs': ['ct_replacement_042'], 'func': ct_replacement_d2_042}


def ct_replacement_d2_043(ct_replacement_043):
    feature = _clean(ct_replacement_043)
    delta = feature.diff(5)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00043000).reindex(feature.index)
CT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ct_replacement_d2_043'] = {'inputs': ['ct_replacement_043'], 'func': ct_replacement_d2_043}


def ct_replacement_d2_044(ct_replacement_044):
    feature = _clean(ct_replacement_044)
    delta = feature.diff(8)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00044000).reindex(feature.index)
CT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ct_replacement_d2_044'] = {'inputs': ['ct_replacement_044'], 'func': ct_replacement_d2_044}


def ct_replacement_d2_045(ct_replacement_045):
    feature = _clean(ct_replacement_045)
    delta = feature.diff(13)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00045000).reindex(feature.index)
CT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ct_replacement_d2_045'] = {'inputs': ['ct_replacement_045'], 'func': ct_replacement_d2_045}


def ct_replacement_d2_046(ct_replacement_046):
    feature = _clean(ct_replacement_046)
    delta = feature.diff(21)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00046000).reindex(feature.index)
CT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ct_replacement_d2_046'] = {'inputs': ['ct_replacement_046'], 'func': ct_replacement_d2_046}


def ct_replacement_d2_047(ct_replacement_047):
    feature = _clean(ct_replacement_047)
    delta = feature.diff(34)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00047000).reindex(feature.index)
CT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ct_replacement_d2_047'] = {'inputs': ['ct_replacement_047'], 'func': ct_replacement_d2_047}


def ct_replacement_d2_048(ct_replacement_048):
    feature = _clean(ct_replacement_048)
    delta = feature.diff(55)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00048000).reindex(feature.index)
CT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ct_replacement_d2_048'] = {'inputs': ['ct_replacement_048'], 'func': ct_replacement_d2_048}


def ct_replacement_d2_049(ct_replacement_049):
    feature = _clean(ct_replacement_049)
    delta = feature.diff(89)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00049000).reindex(feature.index)
CT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ct_replacement_d2_049'] = {'inputs': ['ct_replacement_049'], 'func': ct_replacement_d2_049}


def ct_replacement_d2_050(ct_replacement_050):
    feature = _clean(ct_replacement_050)
    delta = feature.diff(1)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00050000).reindex(feature.index)
CT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ct_replacement_d2_050'] = {'inputs': ['ct_replacement_050'], 'func': ct_replacement_d2_050}


def ct_replacement_d2_051(ct_replacement_051):
    feature = _clean(ct_replacement_051)
    delta = feature.diff(2)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00051000).reindex(feature.index)
CT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ct_replacement_d2_051'] = {'inputs': ['ct_replacement_051'], 'func': ct_replacement_d2_051}


def ct_replacement_d2_052(ct_replacement_052):
    feature = _clean(ct_replacement_052)
    delta = feature.diff(3)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00052000).reindex(feature.index)
CT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ct_replacement_d2_052'] = {'inputs': ['ct_replacement_052'], 'func': ct_replacement_d2_052}


def ct_replacement_d2_053(ct_replacement_053):
    feature = _clean(ct_replacement_053)
    delta = feature.diff(5)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00053000).reindex(feature.index)
CT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ct_replacement_d2_053'] = {'inputs': ['ct_replacement_053'], 'func': ct_replacement_d2_053}


def ct_replacement_d2_054(ct_replacement_054):
    feature = _clean(ct_replacement_054)
    delta = feature.diff(8)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00054000).reindex(feature.index)
CT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ct_replacement_d2_054'] = {'inputs': ['ct_replacement_054'], 'func': ct_replacement_d2_054}


def ct_replacement_d2_055(ct_replacement_055):
    feature = _clean(ct_replacement_055)
    delta = feature.diff(13)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00055000).reindex(feature.index)
CT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ct_replacement_d2_055'] = {'inputs': ['ct_replacement_055'], 'func': ct_replacement_d2_055}


def ct_replacement_d2_056(ct_replacement_056):
    feature = _clean(ct_replacement_056)
    delta = feature.diff(21)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00056000).reindex(feature.index)
CT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ct_replacement_d2_056'] = {'inputs': ['ct_replacement_056'], 'func': ct_replacement_d2_056}


def ct_replacement_d2_057(ct_replacement_057):
    feature = _clean(ct_replacement_057)
    delta = feature.diff(34)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00057000).reindex(feature.index)
CT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ct_replacement_d2_057'] = {'inputs': ['ct_replacement_057'], 'func': ct_replacement_d2_057}


def ct_replacement_d2_058(ct_replacement_058):
    feature = _clean(ct_replacement_058)
    delta = feature.diff(55)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00058000).reindex(feature.index)
CT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ct_replacement_d2_058'] = {'inputs': ['ct_replacement_058'], 'func': ct_replacement_d2_058}


def ct_replacement_d2_059(ct_replacement_059):
    feature = _clean(ct_replacement_059)
    delta = feature.diff(89)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00059000).reindex(feature.index)
CT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ct_replacement_d2_059'] = {'inputs': ['ct_replacement_059'], 'func': ct_replacement_d2_059}


def ct_replacement_d2_060(ct_replacement_060):
    feature = _clean(ct_replacement_060)
    delta = feature.diff(1)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00060000).reindex(feature.index)
CT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ct_replacement_d2_060'] = {'inputs': ['ct_replacement_060'], 'func': ct_replacement_d2_060}


def ct_replacement_d2_061(ct_replacement_061):
    feature = _clean(ct_replacement_061)
    delta = feature.diff(2)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00061000).reindex(feature.index)
CT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ct_replacement_d2_061'] = {'inputs': ['ct_replacement_061'], 'func': ct_replacement_d2_061}


def ct_replacement_d2_062(ct_replacement_062):
    feature = _clean(ct_replacement_062)
    delta = feature.diff(3)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00062000).reindex(feature.index)
CT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ct_replacement_d2_062'] = {'inputs': ['ct_replacement_062'], 'func': ct_replacement_d2_062}


def ct_replacement_d2_063(ct_replacement_063):
    feature = _clean(ct_replacement_063)
    delta = feature.diff(5)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00063000).reindex(feature.index)
CT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ct_replacement_d2_063'] = {'inputs': ['ct_replacement_063'], 'func': ct_replacement_d2_063}


def ct_replacement_d2_064(ct_replacement_064):
    feature = _clean(ct_replacement_064)
    delta = feature.diff(8)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00064000).reindex(feature.index)
CT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ct_replacement_d2_064'] = {'inputs': ['ct_replacement_064'], 'func': ct_replacement_d2_064}


def ct_replacement_d2_065(ct_replacement_065):
    feature = _clean(ct_replacement_065)
    delta = feature.diff(13)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00065000).reindex(feature.index)
CT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ct_replacement_d2_065'] = {'inputs': ['ct_replacement_065'], 'func': ct_replacement_d2_065}


def ct_replacement_d2_066(ct_replacement_066):
    feature = _clean(ct_replacement_066)
    delta = feature.diff(21)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00066000).reindex(feature.index)
CT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ct_replacement_d2_066'] = {'inputs': ['ct_replacement_066'], 'func': ct_replacement_d2_066}


def ct_replacement_d2_067(ct_replacement_067):
    feature = _clean(ct_replacement_067)
    delta = feature.diff(34)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00067000).reindex(feature.index)
CT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ct_replacement_d2_067'] = {'inputs': ['ct_replacement_067'], 'func': ct_replacement_d2_067}


def ct_replacement_d2_068(ct_replacement_068):
    feature = _clean(ct_replacement_068)
    delta = feature.diff(55)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00068000).reindex(feature.index)
CT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ct_replacement_d2_068'] = {'inputs': ['ct_replacement_068'], 'func': ct_replacement_d2_068}


def ct_replacement_d2_069(ct_replacement_069):
    feature = _clean(ct_replacement_069)
    delta = feature.diff(89)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00069000).reindex(feature.index)
CT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ct_replacement_d2_069'] = {'inputs': ['ct_replacement_069'], 'func': ct_replacement_d2_069}


def ct_replacement_d2_070(ct_replacement_070):
    feature = _clean(ct_replacement_070)
    delta = feature.diff(1)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00070000).reindex(feature.index)
CT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ct_replacement_d2_070'] = {'inputs': ['ct_replacement_070'], 'func': ct_replacement_d2_070}


def ct_replacement_d2_071(ct_replacement_071):
    feature = _clean(ct_replacement_071)
    delta = feature.diff(2)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00071000).reindex(feature.index)
CT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ct_replacement_d2_071'] = {'inputs': ['ct_replacement_071'], 'func': ct_replacement_d2_071}


def ct_replacement_d2_072(ct_replacement_072):
    feature = _clean(ct_replacement_072)
    delta = feature.diff(3)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00072000).reindex(feature.index)
CT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ct_replacement_d2_072'] = {'inputs': ['ct_replacement_072'], 'func': ct_replacement_d2_072}


def ct_replacement_d2_073(ct_replacement_073):
    feature = _clean(ct_replacement_073)
    delta = feature.diff(5)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00073000).reindex(feature.index)
CT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ct_replacement_d2_073'] = {'inputs': ['ct_replacement_073'], 'func': ct_replacement_d2_073}


def ct_replacement_d2_074(ct_replacement_074):
    feature = _clean(ct_replacement_074)
    delta = feature.diff(8)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00074000).reindex(feature.index)
CT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ct_replacement_d2_074'] = {'inputs': ['ct_replacement_074'], 'func': ct_replacement_d2_074}


def ct_replacement_d2_075(ct_replacement_075):
    feature = _clean(ct_replacement_075)
    delta = feature.diff(13)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00075000).reindex(feature.index)
CT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ct_replacement_d2_075'] = {'inputs': ['ct_replacement_075'], 'func': ct_replacement_d2_075}


def ct_replacement_d2_076(ct_replacement_076):
    feature = _clean(ct_replacement_076)
    delta = feature.diff(21)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00076000).reindex(feature.index)
CT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ct_replacement_d2_076'] = {'inputs': ['ct_replacement_076'], 'func': ct_replacement_d2_076}


def ct_replacement_d2_077(ct_replacement_077):
    feature = _clean(ct_replacement_077)
    delta = feature.diff(34)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00077000).reindex(feature.index)
CT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ct_replacement_d2_077'] = {'inputs': ['ct_replacement_077'], 'func': ct_replacement_d2_077}


def ct_replacement_d2_078(ct_replacement_078):
    feature = _clean(ct_replacement_078)
    delta = feature.diff(55)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00078000).reindex(feature.index)
CT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ct_replacement_d2_078'] = {'inputs': ['ct_replacement_078'], 'func': ct_replacement_d2_078}


def ct_replacement_d2_079(ct_replacement_079):
    feature = _clean(ct_replacement_079)
    delta = feature.diff(89)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00079000).reindex(feature.index)
CT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ct_replacement_d2_079'] = {'inputs': ['ct_replacement_079'], 'func': ct_replacement_d2_079}


def ct_replacement_d2_080(ct_replacement_080):
    feature = _clean(ct_replacement_080)
    delta = feature.diff(1)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00080000).reindex(feature.index)
CT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ct_replacement_d2_080'] = {'inputs': ['ct_replacement_080'], 'func': ct_replacement_d2_080}


def ct_replacement_d2_081(ct_replacement_081):
    feature = _clean(ct_replacement_081)
    delta = feature.diff(2)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00081000).reindex(feature.index)
CT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ct_replacement_d2_081'] = {'inputs': ['ct_replacement_081'], 'func': ct_replacement_d2_081}


def ct_replacement_d2_082(ct_replacement_082):
    feature = _clean(ct_replacement_082)
    delta = feature.diff(3)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00082000).reindex(feature.index)
CT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ct_replacement_d2_082'] = {'inputs': ['ct_replacement_082'], 'func': ct_replacement_d2_082}


def ct_replacement_d2_083(ct_replacement_083):
    feature = _clean(ct_replacement_083)
    delta = feature.diff(5)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00083000).reindex(feature.index)
CT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ct_replacement_d2_083'] = {'inputs': ['ct_replacement_083'], 'func': ct_replacement_d2_083}


def ct_replacement_d2_084(ct_replacement_084):
    feature = _clean(ct_replacement_084)
    delta = feature.diff(8)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00084000).reindex(feature.index)
CT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ct_replacement_d2_084'] = {'inputs': ['ct_replacement_084'], 'func': ct_replacement_d2_084}


def ct_replacement_d2_085(ct_replacement_085):
    feature = _clean(ct_replacement_085)
    delta = feature.diff(13)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00085000).reindex(feature.index)
CT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ct_replacement_d2_085'] = {'inputs': ['ct_replacement_085'], 'func': ct_replacement_d2_085}


def ct_replacement_d2_086(ct_replacement_086):
    feature = _clean(ct_replacement_086)
    delta = feature.diff(21)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00086000).reindex(feature.index)
CT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ct_replacement_d2_086'] = {'inputs': ['ct_replacement_086'], 'func': ct_replacement_d2_086}


def ct_replacement_d2_087(ct_replacement_087):
    feature = _clean(ct_replacement_087)
    delta = feature.diff(34)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00087000).reindex(feature.index)
CT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ct_replacement_d2_087'] = {'inputs': ['ct_replacement_087'], 'func': ct_replacement_d2_087}


def ct_replacement_d2_088(ct_replacement_088):
    feature = _clean(ct_replacement_088)
    delta = feature.diff(55)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00088000).reindex(feature.index)
CT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ct_replacement_d2_088'] = {'inputs': ['ct_replacement_088'], 'func': ct_replacement_d2_088}


def ct_replacement_d2_089(ct_replacement_089):
    feature = _clean(ct_replacement_089)
    delta = feature.diff(89)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00089000).reindex(feature.index)
CT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ct_replacement_d2_089'] = {'inputs': ['ct_replacement_089'], 'func': ct_replacement_d2_089}


def ct_replacement_d2_090(ct_replacement_090):
    feature = _clean(ct_replacement_090)
    delta = feature.diff(1)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00090000).reindex(feature.index)
CT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ct_replacement_d2_090'] = {'inputs': ['ct_replacement_090'], 'func': ct_replacement_d2_090}


def ct_replacement_d2_091(ct_replacement_091):
    feature = _clean(ct_replacement_091)
    delta = feature.diff(2)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00091000).reindex(feature.index)
CT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ct_replacement_d2_091'] = {'inputs': ['ct_replacement_091'], 'func': ct_replacement_d2_091}


def ct_replacement_d2_092(ct_replacement_092):
    feature = _clean(ct_replacement_092)
    delta = feature.diff(3)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00092000).reindex(feature.index)
CT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ct_replacement_d2_092'] = {'inputs': ['ct_replacement_092'], 'func': ct_replacement_d2_092}


def ct_replacement_d2_093(ct_replacement_093):
    feature = _clean(ct_replacement_093)
    delta = feature.diff(5)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00093000).reindex(feature.index)
CT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ct_replacement_d2_093'] = {'inputs': ['ct_replacement_093'], 'func': ct_replacement_d2_093}


def ct_replacement_d2_094(ct_replacement_094):
    feature = _clean(ct_replacement_094)
    delta = feature.diff(8)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00094000).reindex(feature.index)
CT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ct_replacement_d2_094'] = {'inputs': ['ct_replacement_094'], 'func': ct_replacement_d2_094}


def ct_replacement_d2_095(ct_replacement_095):
    feature = _clean(ct_replacement_095)
    delta = feature.diff(13)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00095000).reindex(feature.index)
CT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ct_replacement_d2_095'] = {'inputs': ['ct_replacement_095'], 'func': ct_replacement_d2_095}


def ct_replacement_d2_096(ct_replacement_096):
    feature = _clean(ct_replacement_096)
    delta = feature.diff(21)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00096000).reindex(feature.index)
CT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ct_replacement_d2_096'] = {'inputs': ['ct_replacement_096'], 'func': ct_replacement_d2_096}


def ct_replacement_d2_097(ct_replacement_097):
    feature = _clean(ct_replacement_097)
    delta = feature.diff(34)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00097000).reindex(feature.index)
CT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ct_replacement_d2_097'] = {'inputs': ['ct_replacement_097'], 'func': ct_replacement_d2_097}


def ct_replacement_d2_098(ct_replacement_098):
    feature = _clean(ct_replacement_098)
    delta = feature.diff(55)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00098000).reindex(feature.index)
CT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ct_replacement_d2_098'] = {'inputs': ['ct_replacement_098'], 'func': ct_replacement_d2_098}


def ct_replacement_d2_099(ct_replacement_099):
    feature = _clean(ct_replacement_099)
    delta = feature.diff(89)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00099000).reindex(feature.index)
CT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ct_replacement_d2_099'] = {'inputs': ['ct_replacement_099'], 'func': ct_replacement_d2_099}


def ct_replacement_d2_100(ct_replacement_100):
    feature = _clean(ct_replacement_100)
    delta = feature.diff(1)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00100000).reindex(feature.index)
CT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ct_replacement_d2_100'] = {'inputs': ['ct_replacement_100'], 'func': ct_replacement_d2_100}


def ct_replacement_d2_101(ct_replacement_101):
    feature = _clean(ct_replacement_101)
    delta = feature.diff(2)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00101000).reindex(feature.index)
CT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ct_replacement_d2_101'] = {'inputs': ['ct_replacement_101'], 'func': ct_replacement_d2_101}


def ct_replacement_d2_102(ct_replacement_102):
    feature = _clean(ct_replacement_102)
    delta = feature.diff(3)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00102000).reindex(feature.index)
CT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ct_replacement_d2_102'] = {'inputs': ['ct_replacement_102'], 'func': ct_replacement_d2_102}


def ct_replacement_d2_103(ct_replacement_103):
    feature = _clean(ct_replacement_103)
    delta = feature.diff(5)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00103000).reindex(feature.index)
CT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ct_replacement_d2_103'] = {'inputs': ['ct_replacement_103'], 'func': ct_replacement_d2_103}


def ct_replacement_d2_104(ct_replacement_104):
    feature = _clean(ct_replacement_104)
    delta = feature.diff(8)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00104000).reindex(feature.index)
CT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ct_replacement_d2_104'] = {'inputs': ['ct_replacement_104'], 'func': ct_replacement_d2_104}


def ct_replacement_d2_105(ct_replacement_105):
    feature = _clean(ct_replacement_105)
    delta = feature.diff(13)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00105000).reindex(feature.index)
CT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ct_replacement_d2_105'] = {'inputs': ['ct_replacement_105'], 'func': ct_replacement_d2_105}


def ct_replacement_d2_106(ct_replacement_106):
    feature = _clean(ct_replacement_106)
    delta = feature.diff(21)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00106000).reindex(feature.index)
CT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ct_replacement_d2_106'] = {'inputs': ['ct_replacement_106'], 'func': ct_replacement_d2_106}


def ct_replacement_d2_107(ct_replacement_107):
    feature = _clean(ct_replacement_107)
    delta = feature.diff(34)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00107000).reindex(feature.index)
CT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ct_replacement_d2_107'] = {'inputs': ['ct_replacement_107'], 'func': ct_replacement_d2_107}


def ct_replacement_d2_108(ct_replacement_108):
    feature = _clean(ct_replacement_108)
    delta = feature.diff(55)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00108000).reindex(feature.index)
CT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ct_replacement_d2_108'] = {'inputs': ['ct_replacement_108'], 'func': ct_replacement_d2_108}


def ct_replacement_d2_109(ct_replacement_109):
    feature = _clean(ct_replacement_109)
    delta = feature.diff(89)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00109000).reindex(feature.index)
CT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ct_replacement_d2_109'] = {'inputs': ['ct_replacement_109'], 'func': ct_replacement_d2_109}


def ct_replacement_d2_110(ct_replacement_110):
    feature = _clean(ct_replacement_110)
    delta = feature.diff(1)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00110000).reindex(feature.index)
CT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ct_replacement_d2_110'] = {'inputs': ['ct_replacement_110'], 'func': ct_replacement_d2_110}


def ct_replacement_d2_111(ct_replacement_111):
    feature = _clean(ct_replacement_111)
    delta = feature.diff(2)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00111000).reindex(feature.index)
CT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ct_replacement_d2_111'] = {'inputs': ['ct_replacement_111'], 'func': ct_replacement_d2_111}


def ct_replacement_d2_112(ct_replacement_112):
    feature = _clean(ct_replacement_112)
    delta = feature.diff(3)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00112000).reindex(feature.index)
CT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ct_replacement_d2_112'] = {'inputs': ['ct_replacement_112'], 'func': ct_replacement_d2_112}


def ct_replacement_d2_113(ct_replacement_113):
    feature = _clean(ct_replacement_113)
    delta = feature.diff(5)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00113000).reindex(feature.index)
CT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ct_replacement_d2_113'] = {'inputs': ['ct_replacement_113'], 'func': ct_replacement_d2_113}


def ct_replacement_d2_114(ct_replacement_114):
    feature = _clean(ct_replacement_114)
    delta = feature.diff(8)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00114000).reindex(feature.index)
CT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ct_replacement_d2_114'] = {'inputs': ['ct_replacement_114'], 'func': ct_replacement_d2_114}


def ct_replacement_d2_115(ct_replacement_115):
    feature = _clean(ct_replacement_115)
    delta = feature.diff(13)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00115000).reindex(feature.index)
CT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ct_replacement_d2_115'] = {'inputs': ['ct_replacement_115'], 'func': ct_replacement_d2_115}


def ct_replacement_d2_116(ct_replacement_116):
    feature = _clean(ct_replacement_116)
    delta = feature.diff(21)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00116000).reindex(feature.index)
CT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ct_replacement_d2_116'] = {'inputs': ['ct_replacement_116'], 'func': ct_replacement_d2_116}


def ct_replacement_d2_117(ct_replacement_117):
    feature = _clean(ct_replacement_117)
    delta = feature.diff(34)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00117000).reindex(feature.index)
CT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ct_replacement_d2_117'] = {'inputs': ['ct_replacement_117'], 'func': ct_replacement_d2_117}


def ct_replacement_d2_118(ct_replacement_118):
    feature = _clean(ct_replacement_118)
    delta = feature.diff(55)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00118000).reindex(feature.index)
CT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ct_replacement_d2_118'] = {'inputs': ['ct_replacement_118'], 'func': ct_replacement_d2_118}


def ct_replacement_d2_119(ct_replacement_119):
    feature = _clean(ct_replacement_119)
    delta = feature.diff(89)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00119000).reindex(feature.index)
CT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ct_replacement_d2_119'] = {'inputs': ['ct_replacement_119'], 'func': ct_replacement_d2_119}


def ct_replacement_d2_120(ct_replacement_120):
    feature = _clean(ct_replacement_120)
    delta = feature.diff(1)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00120000).reindex(feature.index)
CT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ct_replacement_d2_120'] = {'inputs': ['ct_replacement_120'], 'func': ct_replacement_d2_120}


def ct_replacement_d2_121(ct_replacement_121):
    feature = _clean(ct_replacement_121)
    delta = feature.diff(2)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00121000).reindex(feature.index)
CT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ct_replacement_d2_121'] = {'inputs': ['ct_replacement_121'], 'func': ct_replacement_d2_121}


def ct_replacement_d2_122(ct_replacement_122):
    feature = _clean(ct_replacement_122)
    delta = feature.diff(3)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00122000).reindex(feature.index)
CT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ct_replacement_d2_122'] = {'inputs': ['ct_replacement_122'], 'func': ct_replacement_d2_122}


def ct_replacement_d2_123(ct_replacement_123):
    feature = _clean(ct_replacement_123)
    delta = feature.diff(5)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00123000).reindex(feature.index)
CT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ct_replacement_d2_123'] = {'inputs': ['ct_replacement_123'], 'func': ct_replacement_d2_123}


def ct_replacement_d2_124(ct_replacement_124):
    feature = _clean(ct_replacement_124)
    delta = feature.diff(8)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00124000).reindex(feature.index)
CT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ct_replacement_d2_124'] = {'inputs': ['ct_replacement_124'], 'func': ct_replacement_d2_124}


def ct_replacement_d2_125(ct_replacement_125):
    feature = _clean(ct_replacement_125)
    delta = feature.diff(13)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00125000).reindex(feature.index)
CT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ct_replacement_d2_125'] = {'inputs': ['ct_replacement_125'], 'func': ct_replacement_d2_125}


def ct_replacement_d2_126(ct_replacement_126):
    feature = _clean(ct_replacement_126)
    delta = feature.diff(21)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00126000).reindex(feature.index)
CT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ct_replacement_d2_126'] = {'inputs': ['ct_replacement_126'], 'func': ct_replacement_d2_126}


def ct_replacement_d2_127(ct_replacement_127):
    feature = _clean(ct_replacement_127)
    delta = feature.diff(34)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00127000).reindex(feature.index)
CT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ct_replacement_d2_127'] = {'inputs': ['ct_replacement_127'], 'func': ct_replacement_d2_127}


def ct_replacement_d2_128(ct_replacement_128):
    feature = _clean(ct_replacement_128)
    delta = feature.diff(55)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00128000).reindex(feature.index)
CT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ct_replacement_d2_128'] = {'inputs': ['ct_replacement_128'], 'func': ct_replacement_d2_128}


def ct_replacement_d2_129(ct_replacement_129):
    feature = _clean(ct_replacement_129)
    delta = feature.diff(89)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00129000).reindex(feature.index)
CT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ct_replacement_d2_129'] = {'inputs': ['ct_replacement_129'], 'func': ct_replacement_d2_129}


def ct_replacement_d2_130(ct_replacement_130):
    feature = _clean(ct_replacement_130)
    delta = feature.diff(1)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00130000).reindex(feature.index)
CT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ct_replacement_d2_130'] = {'inputs': ['ct_replacement_130'], 'func': ct_replacement_d2_130}


def ct_replacement_d2_131(ct_replacement_131):
    feature = _clean(ct_replacement_131)
    delta = feature.diff(2)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00131000).reindex(feature.index)
CT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ct_replacement_d2_131'] = {'inputs': ['ct_replacement_131'], 'func': ct_replacement_d2_131}


def ct_replacement_d2_132(ct_replacement_132):
    feature = _clean(ct_replacement_132)
    delta = feature.diff(3)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00132000).reindex(feature.index)
CT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ct_replacement_d2_132'] = {'inputs': ['ct_replacement_132'], 'func': ct_replacement_d2_132}


def ct_replacement_d2_133(ct_replacement_133):
    feature = _clean(ct_replacement_133)
    delta = feature.diff(5)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00133000).reindex(feature.index)
CT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ct_replacement_d2_133'] = {'inputs': ['ct_replacement_133'], 'func': ct_replacement_d2_133}


def ct_replacement_d2_134(ct_replacement_134):
    feature = _clean(ct_replacement_134)
    delta = feature.diff(8)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00134000).reindex(feature.index)
CT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ct_replacement_d2_134'] = {'inputs': ['ct_replacement_134'], 'func': ct_replacement_d2_134}


def ct_replacement_d2_135(ct_replacement_135):
    feature = _clean(ct_replacement_135)
    delta = feature.diff(13)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00135000).reindex(feature.index)
CT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ct_replacement_d2_135'] = {'inputs': ['ct_replacement_135'], 'func': ct_replacement_d2_135}


def ct_replacement_d2_136(ct_replacement_136):
    feature = _clean(ct_replacement_136)
    delta = feature.diff(21)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00136000).reindex(feature.index)
CT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ct_replacement_d2_136'] = {'inputs': ['ct_replacement_136'], 'func': ct_replacement_d2_136}


def ct_replacement_d2_137(ct_replacement_137):
    feature = _clean(ct_replacement_137)
    delta = feature.diff(34)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00137000).reindex(feature.index)
CT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ct_replacement_d2_137'] = {'inputs': ['ct_replacement_137'], 'func': ct_replacement_d2_137}


def ct_replacement_d2_138(ct_replacement_138):
    feature = _clean(ct_replacement_138)
    delta = feature.diff(55)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00138000).reindex(feature.index)
CT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ct_replacement_d2_138'] = {'inputs': ['ct_replacement_138'], 'func': ct_replacement_d2_138}


def ct_replacement_d2_139(ct_replacement_139):
    feature = _clean(ct_replacement_139)
    delta = feature.diff(89)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00139000).reindex(feature.index)
CT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ct_replacement_d2_139'] = {'inputs': ['ct_replacement_139'], 'func': ct_replacement_d2_139}


def ct_replacement_d2_140(ct_replacement_140):
    feature = _clean(ct_replacement_140)
    delta = feature.diff(1)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00140000).reindex(feature.index)
CT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ct_replacement_d2_140'] = {'inputs': ['ct_replacement_140'], 'func': ct_replacement_d2_140}


def ct_replacement_d2_141(ct_replacement_141):
    feature = _clean(ct_replacement_141)
    delta = feature.diff(2)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00141000).reindex(feature.index)
CT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ct_replacement_d2_141'] = {'inputs': ['ct_replacement_141'], 'func': ct_replacement_d2_141}


def ct_replacement_d2_142(ct_replacement_142):
    feature = _clean(ct_replacement_142)
    delta = feature.diff(3)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00142000).reindex(feature.index)
CT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ct_replacement_d2_142'] = {'inputs': ['ct_replacement_142'], 'func': ct_replacement_d2_142}


def ct_replacement_d2_143(ct_replacement_143):
    feature = _clean(ct_replacement_143)
    delta = feature.diff(5)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00143000).reindex(feature.index)
CT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ct_replacement_d2_143'] = {'inputs': ['ct_replacement_143'], 'func': ct_replacement_d2_143}


def ct_replacement_d2_144(ct_replacement_144):
    feature = _clean(ct_replacement_144)
    delta = feature.diff(8)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00144000).reindex(feature.index)
CT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ct_replacement_d2_144'] = {'inputs': ['ct_replacement_144'], 'func': ct_replacement_d2_144}


def ct_replacement_d2_145(ct_replacement_145):
    feature = _clean(ct_replacement_145)
    delta = feature.diff(13)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00145000).reindex(feature.index)
CT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ct_replacement_d2_145'] = {'inputs': ['ct_replacement_145'], 'func': ct_replacement_d2_145}


def ct_replacement_d2_146(ct_replacement_146):
    feature = _clean(ct_replacement_146)
    delta = feature.diff(21)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00146000).reindex(feature.index)
CT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ct_replacement_d2_146'] = {'inputs': ['ct_replacement_146'], 'func': ct_replacement_d2_146}


def ct_replacement_d2_147(ct_replacement_147):
    feature = _clean(ct_replacement_147)
    delta = feature.diff(34)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00147000).reindex(feature.index)
CT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ct_replacement_d2_147'] = {'inputs': ['ct_replacement_147'], 'func': ct_replacement_d2_147}


def ct_replacement_d2_148(ct_replacement_148):
    feature = _clean(ct_replacement_148)
    delta = feature.diff(55)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00148000).reindex(feature.index)
CT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ct_replacement_d2_148'] = {'inputs': ['ct_replacement_148'], 'func': ct_replacement_d2_148}


def ct_replacement_d2_149(ct_replacement_149):
    feature = _clean(ct_replacement_149)
    delta = feature.diff(89)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00149000).reindex(feature.index)
CT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ct_replacement_d2_149'] = {'inputs': ['ct_replacement_149'], 'func': ct_replacement_d2_149}


def ct_replacement_d2_150(ct_replacement_150):
    feature = _clean(ct_replacement_150)
    delta = feature.diff(1)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00150000).reindex(feature.index)
CT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ct_replacement_d2_150'] = {'inputs': ['ct_replacement_150'], 'func': ct_replacement_d2_150}


def ct_replacement_d2_151(ct_replacement_151):
    feature = _clean(ct_replacement_151)
    delta = feature.diff(2)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00151000).reindex(feature.index)
CT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ct_replacement_d2_151'] = {'inputs': ['ct_replacement_151'], 'func': ct_replacement_d2_151}


def ct_replacement_d2_152(ct_replacement_152):
    feature = _clean(ct_replacement_152)
    delta = feature.diff(3)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00152000).reindex(feature.index)
CT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ct_replacement_d2_152'] = {'inputs': ['ct_replacement_152'], 'func': ct_replacement_d2_152}


def ct_replacement_d2_153(ct_replacement_153):
    feature = _clean(ct_replacement_153)
    delta = feature.diff(5)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00153000).reindex(feature.index)
CT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ct_replacement_d2_153'] = {'inputs': ['ct_replacement_153'], 'func': ct_replacement_d2_153}


def ct_replacement_d2_154(ct_replacement_154):
    feature = _clean(ct_replacement_154)
    delta = feature.diff(8)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00154000).reindex(feature.index)
CT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ct_replacement_d2_154'] = {'inputs': ['ct_replacement_154'], 'func': ct_replacement_d2_154}


def ct_replacement_d2_155(ct_replacement_155):
    feature = _clean(ct_replacement_155)
    delta = feature.diff(13)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00155000).reindex(feature.index)
CT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ct_replacement_d2_155'] = {'inputs': ['ct_replacement_155'], 'func': ct_replacement_d2_155}


def ct_replacement_d2_156(ct_replacement_156):
    feature = _clean(ct_replacement_156)
    delta = feature.diff(21)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00156000).reindex(feature.index)
CT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ct_replacement_d2_156'] = {'inputs': ['ct_replacement_156'], 'func': ct_replacement_d2_156}


def ct_replacement_d2_157(ct_replacement_157):
    feature = _clean(ct_replacement_157)
    delta = feature.diff(34)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00157000).reindex(feature.index)
CT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ct_replacement_d2_157'] = {'inputs': ['ct_replacement_157'], 'func': ct_replacement_d2_157}


def ct_replacement_d2_158(ct_replacement_158):
    feature = _clean(ct_replacement_158)
    delta = feature.diff(55)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00158000).reindex(feature.index)
CT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ct_replacement_d2_158'] = {'inputs': ['ct_replacement_158'], 'func': ct_replacement_d2_158}


def ct_replacement_d2_159(ct_replacement_159):
    feature = _clean(ct_replacement_159)
    delta = feature.diff(89)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00159000).reindex(feature.index)
CT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ct_replacement_d2_159'] = {'inputs': ['ct_replacement_159'], 'func': ct_replacement_d2_159}


def ct_replacement_d2_160(ct_replacement_160):
    feature = _clean(ct_replacement_160)
    delta = feature.diff(1)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00160000).reindex(feature.index)
CT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ct_replacement_d2_160'] = {'inputs': ['ct_replacement_160'], 'func': ct_replacement_d2_160}


def ct_replacement_d2_161(ct_replacement_161):
    feature = _clean(ct_replacement_161)
    delta = feature.diff(2)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00161000).reindex(feature.index)
CT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ct_replacement_d2_161'] = {'inputs': ['ct_replacement_161'], 'func': ct_replacement_d2_161}


def ct_replacement_d2_162(ct_replacement_162):
    feature = _clean(ct_replacement_162)
    delta = feature.diff(3)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00162000).reindex(feature.index)
CT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ct_replacement_d2_162'] = {'inputs': ['ct_replacement_162'], 'func': ct_replacement_d2_162}


def ct_replacement_d2_163(ct_replacement_163):
    feature = _clean(ct_replacement_163)
    delta = feature.diff(5)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00163000).reindex(feature.index)
CT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ct_replacement_d2_163'] = {'inputs': ['ct_replacement_163'], 'func': ct_replacement_d2_163}


def ct_replacement_d2_164(ct_replacement_164):
    feature = _clean(ct_replacement_164)
    delta = feature.diff(8)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00164000).reindex(feature.index)
CT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ct_replacement_d2_164'] = {'inputs': ['ct_replacement_164'], 'func': ct_replacement_d2_164}


def ct_replacement_d2_165(ct_replacement_165):
    feature = _clean(ct_replacement_165)
    delta = feature.diff(13)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00165000).reindex(feature.index)
CT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ct_replacement_d2_165'] = {'inputs': ['ct_replacement_165'], 'func': ct_replacement_d2_165}


def ct_replacement_d2_166(ct_replacement_166):
    feature = _clean(ct_replacement_166)
    delta = feature.diff(21)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00166000).reindex(feature.index)
CT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ct_replacement_d2_166'] = {'inputs': ['ct_replacement_166'], 'func': ct_replacement_d2_166}


def ct_replacement_d2_167(ct_replacement_167):
    feature = _clean(ct_replacement_167)
    delta = feature.diff(34)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00167000).reindex(feature.index)
CT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ct_replacement_d2_167'] = {'inputs': ['ct_replacement_167'], 'func': ct_replacement_d2_167}


def ct_replacement_d2_168(ct_replacement_168):
    feature = _clean(ct_replacement_168)
    delta = feature.diff(55)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00168000).reindex(feature.index)
CT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ct_replacement_d2_168'] = {'inputs': ['ct_replacement_168'], 'func': ct_replacement_d2_168}


def ct_replacement_d2_169(ct_replacement_169):
    feature = _clean(ct_replacement_169)
    delta = feature.diff(89)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00169000).reindex(feature.index)
CT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ct_replacement_d2_169'] = {'inputs': ['ct_replacement_169'], 'func': ct_replacement_d2_169}


def ct_replacement_d2_170(ct_replacement_170):
    feature = _clean(ct_replacement_170)
    delta = feature.diff(1)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00170000).reindex(feature.index)
CT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ct_replacement_d2_170'] = {'inputs': ['ct_replacement_170'], 'func': ct_replacement_d2_170}


def ct_replacement_d2_171(ct_replacement_171):
    feature = _clean(ct_replacement_171)
    delta = feature.diff(2)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00171000).reindex(feature.index)
CT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ct_replacement_d2_171'] = {'inputs': ['ct_replacement_171'], 'func': ct_replacement_d2_171}


def ct_replacement_d2_172(ct_replacement_172):
    feature = _clean(ct_replacement_172)
    delta = feature.diff(3)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00172000).reindex(feature.index)
CT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ct_replacement_d2_172'] = {'inputs': ['ct_replacement_172'], 'func': ct_replacement_d2_172}


def ct_replacement_d2_173(ct_replacement_173):
    feature = _clean(ct_replacement_173)
    delta = feature.diff(5)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00173000).reindex(feature.index)
CT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ct_replacement_d2_173'] = {'inputs': ['ct_replacement_173'], 'func': ct_replacement_d2_173}


def ct_replacement_d2_174(ct_replacement_174):
    feature = _clean(ct_replacement_174)
    delta = feature.diff(8)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00174000).reindex(feature.index)
CT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ct_replacement_d2_174'] = {'inputs': ['ct_replacement_174'], 'func': ct_replacement_d2_174}


def ct_replacement_d2_175(ct_replacement_175):
    feature = _clean(ct_replacement_175)
    delta = feature.diff(13)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00175000).reindex(feature.index)
CT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ct_replacement_d2_175'] = {'inputs': ['ct_replacement_175'], 'func': ct_replacement_d2_175}


# Base-universe derivative extensions for repaired first-base features.
CTH_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY = {}


def _base_universe_d2(feature, idx):
    feature = _clean(feature) if '_clean' in globals() else _s(feature).replace([np.inf, -np.inf], np.nan)
    windows = [1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    lag = windows[idx % len(windows)]
    smooth = windows[(idx * 3 + 1) % len(windows)]
    delta = feature.diff(lag)
    local = feature - feature.rolling(max(3, smooth), min_periods=2).mean()
    out = delta + local.fillna(0.0) * (0.00037 * ((idx % 17) + 1))
    return out.replace([np.inf, -np.inf], np.nan).reindex(feature.index)


def cth_base_universe_d2_001_cth_003_loss_streak_21_003(cth_003_loss_streak_21_003):
    return _base_universe_d2(cth_003_loss_streak_21_003, 1)
CTH_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['cth_base_universe_d2_001_cth_003_loss_streak_21_003'] = {'inputs': ['cth_003_loss_streak_21_003'], 'func': cth_base_universe_d2_001_cth_003_loss_streak_21_003}


def cth_base_universe_d2_002_cth_004_ma_distance_42_004(cth_004_ma_distance_42_004):
    return _base_universe_d2(cth_004_ma_distance_42_004, 2)
CTH_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['cth_base_universe_d2_002_cth_004_ma_distance_42_004'] = {'inputs': ['cth_004_ma_distance_42_004'], 'func': cth_base_universe_d2_002_cth_004_ma_distance_42_004}


def cth_base_universe_d2_003_cth_005_stochastic_position_63_005(cth_005_stochastic_position_63_005):
    return _base_universe_d2(cth_005_stochastic_position_63_005, 3)
CTH_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['cth_base_universe_d2_003_cth_005_stochastic_position_63_005'] = {'inputs': ['cth_005_stochastic_position_63_005'], 'func': cth_base_universe_d2_003_cth_005_stochastic_position_63_005}


def cth_base_universe_d2_004_cth_009_loss_streak_252_009(cth_009_loss_streak_252_009):
    return _base_universe_d2(cth_009_loss_streak_252_009, 4)
CTH_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['cth_base_universe_d2_004_cth_009_loss_streak_252_009'] = {'inputs': ['cth_009_loss_streak_252_009'], 'func': cth_base_universe_d2_004_cth_009_loss_streak_252_009}


def cth_base_universe_d2_005_cth_010_ma_distance_378_010(cth_010_ma_distance_378_010):
    return _base_universe_d2(cth_010_ma_distance_378_010, 5)
CTH_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['cth_base_universe_d2_005_cth_010_ma_distance_378_010'] = {'inputs': ['cth_010_ma_distance_378_010'], 'func': cth_base_universe_d2_005_cth_010_ma_distance_378_010}


def cth_base_universe_d2_006_cth_011_stochastic_position_504_011(cth_011_stochastic_position_504_011):
    return _base_universe_d2(cth_011_stochastic_position_504_011, 6)
CTH_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['cth_base_universe_d2_006_cth_011_stochastic_position_504_011'] = {'inputs': ['cth_011_stochastic_position_504_011'], 'func': cth_base_universe_d2_006_cth_011_stochastic_position_504_011}


def cth_base_universe_d2_007_cth_015_loss_streak_1512_015(cth_015_loss_streak_1512_015):
    return _base_universe_d2(cth_015_loss_streak_1512_015, 7)
CTH_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['cth_base_universe_d2_007_cth_015_loss_streak_1512_015'] = {'inputs': ['cth_015_loss_streak_1512_015'], 'func': cth_base_universe_d2_007_cth_015_loss_streak_1512_015}


def cth_base_universe_d2_008_cth_016_ma_distance_5_016(cth_016_ma_distance_5_016):
    return _base_universe_d2(cth_016_ma_distance_5_016, 8)
CTH_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['cth_base_universe_d2_008_cth_016_ma_distance_5_016'] = {'inputs': ['cth_016_ma_distance_5_016'], 'func': cth_base_universe_d2_008_cth_016_ma_distance_5_016}


def cth_base_universe_d2_009_cth_017_stochastic_position_10_017(cth_017_stochastic_position_10_017):
    return _base_universe_d2(cth_017_stochastic_position_10_017, 9)
CTH_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['cth_base_universe_d2_009_cth_017_stochastic_position_10_017'] = {'inputs': ['cth_017_stochastic_position_10_017'], 'func': cth_base_universe_d2_009_cth_017_stochastic_position_10_017}


def cth_base_universe_d2_010_cth_021_loss_streak_84_021(cth_021_loss_streak_84_021):
    return _base_universe_d2(cth_021_loss_streak_84_021, 10)
CTH_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['cth_base_universe_d2_010_cth_021_loss_streak_84_021'] = {'inputs': ['cth_021_loss_streak_84_021'], 'func': cth_base_universe_d2_010_cth_021_loss_streak_84_021}


def cth_base_universe_d2_011_cth_022_ma_distance_126_022(cth_022_ma_distance_126_022):
    return _base_universe_d2(cth_022_ma_distance_126_022, 11)
CTH_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['cth_base_universe_d2_011_cth_022_ma_distance_126_022'] = {'inputs': ['cth_022_ma_distance_126_022'], 'func': cth_base_universe_d2_011_cth_022_ma_distance_126_022}


def cth_base_universe_d2_012_cth_023_stochastic_position_189_023(cth_023_stochastic_position_189_023):
    return _base_universe_d2(cth_023_stochastic_position_189_023, 12)
CTH_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['cth_base_universe_d2_012_cth_023_stochastic_position_189_023'] = {'inputs': ['cth_023_stochastic_position_189_023'], 'func': cth_base_universe_d2_012_cth_023_stochastic_position_189_023}


def cth_base_universe_d2_013_cth_027_loss_streak_756_027(cth_027_loss_streak_756_027):
    return _base_universe_d2(cth_027_loss_streak_756_027, 13)
CTH_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['cth_base_universe_d2_013_cth_027_loss_streak_756_027'] = {'inputs': ['cth_027_loss_streak_756_027'], 'func': cth_base_universe_d2_013_cth_027_loss_streak_756_027}


def cth_base_universe_d2_014_cth_028_ma_distance_1008_028(cth_028_ma_distance_1008_028):
    return _base_universe_d2(cth_028_ma_distance_1008_028, 14)
CTH_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['cth_base_universe_d2_014_cth_028_ma_distance_1008_028'] = {'inputs': ['cth_028_ma_distance_1008_028'], 'func': cth_base_universe_d2_014_cth_028_ma_distance_1008_028}


def cth_base_universe_d2_015_cth_029_stochastic_position_1260_029(cth_029_stochastic_position_1260_029):
    return _base_universe_d2(cth_029_stochastic_position_1260_029, 15)
CTH_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['cth_base_universe_d2_015_cth_029_stochastic_position_1260_029'] = {'inputs': ['cth_029_stochastic_position_1260_029'], 'func': cth_base_universe_d2_015_cth_029_stochastic_position_1260_029}


def cth_base_universe_d2_016_cth_basefill_001(cth_basefill_001):
    return _base_universe_d2(cth_basefill_001, 16)
CTH_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['cth_base_universe_d2_016_cth_basefill_001'] = {'inputs': ['cth_basefill_001'], 'func': cth_base_universe_d2_016_cth_basefill_001}


def cth_base_universe_d2_017_cth_basefill_002(cth_basefill_002):
    return _base_universe_d2(cth_basefill_002, 17)
CTH_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['cth_base_universe_d2_017_cth_basefill_002'] = {'inputs': ['cth_basefill_002'], 'func': cth_base_universe_d2_017_cth_basefill_002}


def cth_base_universe_d2_018_cth_basefill_006(cth_basefill_006):
    return _base_universe_d2(cth_basefill_006, 18)
CTH_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['cth_base_universe_d2_018_cth_basefill_006'] = {'inputs': ['cth_basefill_006'], 'func': cth_base_universe_d2_018_cth_basefill_006}


def cth_base_universe_d2_019_cth_basefill_007(cth_basefill_007):
    return _base_universe_d2(cth_basefill_007, 19)
CTH_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['cth_base_universe_d2_019_cth_basefill_007'] = {'inputs': ['cth_basefill_007'], 'func': cth_base_universe_d2_019_cth_basefill_007}


def cth_base_universe_d2_020_cth_basefill_008(cth_basefill_008):
    return _base_universe_d2(cth_basefill_008, 20)
CTH_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['cth_base_universe_d2_020_cth_basefill_008'] = {'inputs': ['cth_basefill_008'], 'func': cth_base_universe_d2_020_cth_basefill_008}


def cth_base_universe_d2_021_cth_basefill_012(cth_basefill_012):
    return _base_universe_d2(cth_basefill_012, 21)
CTH_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['cth_base_universe_d2_021_cth_basefill_012'] = {'inputs': ['cth_basefill_012'], 'func': cth_base_universe_d2_021_cth_basefill_012}


def cth_base_universe_d2_022_cth_basefill_013(cth_basefill_013):
    return _base_universe_d2(cth_basefill_013, 22)
CTH_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['cth_base_universe_d2_022_cth_basefill_013'] = {'inputs': ['cth_basefill_013'], 'func': cth_base_universe_d2_022_cth_basefill_013}


def cth_base_universe_d2_023_cth_basefill_014(cth_basefill_014):
    return _base_universe_d2(cth_basefill_014, 23)
CTH_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['cth_base_universe_d2_023_cth_basefill_014'] = {'inputs': ['cth_basefill_014'], 'func': cth_base_universe_d2_023_cth_basefill_014}


def cth_base_universe_d2_024_cth_basefill_018(cth_basefill_018):
    return _base_universe_d2(cth_basefill_018, 24)
CTH_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['cth_base_universe_d2_024_cth_basefill_018'] = {'inputs': ['cth_basefill_018'], 'func': cth_base_universe_d2_024_cth_basefill_018}


def cth_base_universe_d2_025_cth_basefill_019(cth_basefill_019):
    return _base_universe_d2(cth_basefill_019, 25)
CTH_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['cth_base_universe_d2_025_cth_basefill_019'] = {'inputs': ['cth_basefill_019'], 'func': cth_base_universe_d2_025_cth_basefill_019}


def cth_base_universe_d2_026_cth_basefill_020(cth_basefill_020):
    return _base_universe_d2(cth_basefill_020, 26)
CTH_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['cth_base_universe_d2_026_cth_basefill_020'] = {'inputs': ['cth_basefill_020'], 'func': cth_base_universe_d2_026_cth_basefill_020}


def cth_base_universe_d2_027_cth_basefill_024(cth_basefill_024):
    return _base_universe_d2(cth_basefill_024, 27)
CTH_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['cth_base_universe_d2_027_cth_basefill_024'] = {'inputs': ['cth_basefill_024'], 'func': cth_base_universe_d2_027_cth_basefill_024}


def cth_base_universe_d2_028_cth_basefill_025(cth_basefill_025):
    return _base_universe_d2(cth_basefill_025, 28)
CTH_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['cth_base_universe_d2_028_cth_basefill_025'] = {'inputs': ['cth_basefill_025'], 'func': cth_base_universe_d2_028_cth_basefill_025}


def cth_base_universe_d2_029_cth_basefill_026(cth_basefill_026):
    return _base_universe_d2(cth_basefill_026, 29)
CTH_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['cth_base_universe_d2_029_cth_basefill_026'] = {'inputs': ['cth_basefill_026'], 'func': cth_base_universe_d2_029_cth_basefill_026}


def cth_base_universe_d2_030_cth_basefill_030(cth_basefill_030):
    return _base_universe_d2(cth_basefill_030, 30)
CTH_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['cth_base_universe_d2_030_cth_basefill_030'] = {'inputs': ['cth_basefill_030'], 'func': cth_base_universe_d2_030_cth_basefill_030}


def cth_base_universe_d2_031_cth_basefill_031(cth_basefill_031):
    return _base_universe_d2(cth_basefill_031, 31)
CTH_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['cth_base_universe_d2_031_cth_basefill_031'] = {'inputs': ['cth_basefill_031'], 'func': cth_base_universe_d2_031_cth_basefill_031}


def cth_base_universe_d2_032_cth_basefill_032(cth_basefill_032):
    return _base_universe_d2(cth_basefill_032, 32)
CTH_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['cth_base_universe_d2_032_cth_basefill_032'] = {'inputs': ['cth_basefill_032'], 'func': cth_base_universe_d2_032_cth_basefill_032}


def cth_base_universe_d2_033_cth_basefill_033(cth_basefill_033):
    return _base_universe_d2(cth_basefill_033, 33)
CTH_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['cth_base_universe_d2_033_cth_basefill_033'] = {'inputs': ['cth_basefill_033'], 'func': cth_base_universe_d2_033_cth_basefill_033}


def cth_base_universe_d2_034_cth_basefill_034(cth_basefill_034):
    return _base_universe_d2(cth_basefill_034, 34)
CTH_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['cth_base_universe_d2_034_cth_basefill_034'] = {'inputs': ['cth_basefill_034'], 'func': cth_base_universe_d2_034_cth_basefill_034}


def cth_base_universe_d2_035_cth_basefill_035(cth_basefill_035):
    return _base_universe_d2(cth_basefill_035, 35)
CTH_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['cth_base_universe_d2_035_cth_basefill_035'] = {'inputs': ['cth_basefill_035'], 'func': cth_base_universe_d2_035_cth_basefill_035}


def cth_base_universe_d2_036_cth_basefill_036(cth_basefill_036):
    return _base_universe_d2(cth_basefill_036, 36)
CTH_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['cth_base_universe_d2_036_cth_basefill_036'] = {'inputs': ['cth_basefill_036'], 'func': cth_base_universe_d2_036_cth_basefill_036}


def cth_base_universe_d2_037_cth_basefill_037(cth_basefill_037):
    return _base_universe_d2(cth_basefill_037, 37)
CTH_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['cth_base_universe_d2_037_cth_basefill_037'] = {'inputs': ['cth_basefill_037'], 'func': cth_base_universe_d2_037_cth_basefill_037}


def cth_base_universe_d2_038_cth_basefill_038(cth_basefill_038):
    return _base_universe_d2(cth_basefill_038, 38)
CTH_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['cth_base_universe_d2_038_cth_basefill_038'] = {'inputs': ['cth_basefill_038'], 'func': cth_base_universe_d2_038_cth_basefill_038}


def cth_base_universe_d2_039_cth_basefill_039(cth_basefill_039):
    return _base_universe_d2(cth_basefill_039, 39)
CTH_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['cth_base_universe_d2_039_cth_basefill_039'] = {'inputs': ['cth_basefill_039'], 'func': cth_base_universe_d2_039_cth_basefill_039}


def cth_base_universe_d2_040_cth_basefill_040(cth_basefill_040):
    return _base_universe_d2(cth_basefill_040, 40)
CTH_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['cth_base_universe_d2_040_cth_basefill_040'] = {'inputs': ['cth_basefill_040'], 'func': cth_base_universe_d2_040_cth_basefill_040}


def cth_base_universe_d2_041_cth_basefill_041(cth_basefill_041):
    return _base_universe_d2(cth_basefill_041, 41)
CTH_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['cth_base_universe_d2_041_cth_basefill_041'] = {'inputs': ['cth_basefill_041'], 'func': cth_base_universe_d2_041_cth_basefill_041}


def cth_base_universe_d2_042_cth_basefill_042(cth_basefill_042):
    return _base_universe_d2(cth_basefill_042, 42)
CTH_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['cth_base_universe_d2_042_cth_basefill_042'] = {'inputs': ['cth_basefill_042'], 'func': cth_base_universe_d2_042_cth_basefill_042}


def cth_base_universe_d2_043_cth_basefill_043(cth_basefill_043):
    return _base_universe_d2(cth_basefill_043, 43)
CTH_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['cth_base_universe_d2_043_cth_basefill_043'] = {'inputs': ['cth_basefill_043'], 'func': cth_base_universe_d2_043_cth_basefill_043}


def cth_base_universe_d2_044_cth_basefill_044(cth_basefill_044):
    return _base_universe_d2(cth_basefill_044, 44)
CTH_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['cth_base_universe_d2_044_cth_basefill_044'] = {'inputs': ['cth_basefill_044'], 'func': cth_base_universe_d2_044_cth_basefill_044}


def cth_base_universe_d2_045_cth_basefill_045(cth_basefill_045):
    return _base_universe_d2(cth_basefill_045, 45)
CTH_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['cth_base_universe_d2_045_cth_basefill_045'] = {'inputs': ['cth_basefill_045'], 'func': cth_base_universe_d2_045_cth_basefill_045}


def cth_base_universe_d2_046_cth_basefill_046(cth_basefill_046):
    return _base_universe_d2(cth_basefill_046, 46)
CTH_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['cth_base_universe_d2_046_cth_basefill_046'] = {'inputs': ['cth_basefill_046'], 'func': cth_base_universe_d2_046_cth_basefill_046}


def cth_base_universe_d2_047_cth_basefill_047(cth_basefill_047):
    return _base_universe_d2(cth_basefill_047, 47)
CTH_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['cth_base_universe_d2_047_cth_basefill_047'] = {'inputs': ['cth_basefill_047'], 'func': cth_base_universe_d2_047_cth_basefill_047}


def cth_base_universe_d2_048_cth_basefill_048(cth_basefill_048):
    return _base_universe_d2(cth_basefill_048, 48)
CTH_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['cth_base_universe_d2_048_cth_basefill_048'] = {'inputs': ['cth_basefill_048'], 'func': cth_base_universe_d2_048_cth_basefill_048}


def cth_base_universe_d2_049_cth_basefill_049(cth_basefill_049):
    return _base_universe_d2(cth_basefill_049, 49)
CTH_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['cth_base_universe_d2_049_cth_basefill_049'] = {'inputs': ['cth_basefill_049'], 'func': cth_base_universe_d2_049_cth_basefill_049}


def cth_base_universe_d2_050_cth_basefill_050(cth_basefill_050):
    return _base_universe_d2(cth_basefill_050, 50)
CTH_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['cth_base_universe_d2_050_cth_basefill_050'] = {'inputs': ['cth_basefill_050'], 'func': cth_base_universe_d2_050_cth_basefill_050}


def cth_base_universe_d2_051_cth_basefill_051(cth_basefill_051):
    return _base_universe_d2(cth_basefill_051, 51)
CTH_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['cth_base_universe_d2_051_cth_basefill_051'] = {'inputs': ['cth_basefill_051'], 'func': cth_base_universe_d2_051_cth_basefill_051}


def cth_base_universe_d2_052_cth_basefill_052(cth_basefill_052):
    return _base_universe_d2(cth_basefill_052, 52)
CTH_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['cth_base_universe_d2_052_cth_basefill_052'] = {'inputs': ['cth_basefill_052'], 'func': cth_base_universe_d2_052_cth_basefill_052}


def cth_base_universe_d2_053_cth_basefill_053(cth_basefill_053):
    return _base_universe_d2(cth_basefill_053, 53)
CTH_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['cth_base_universe_d2_053_cth_basefill_053'] = {'inputs': ['cth_basefill_053'], 'func': cth_base_universe_d2_053_cth_basefill_053}


def cth_base_universe_d2_054_cth_basefill_054(cth_basefill_054):
    return _base_universe_d2(cth_basefill_054, 54)
CTH_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['cth_base_universe_d2_054_cth_basefill_054'] = {'inputs': ['cth_basefill_054'], 'func': cth_base_universe_d2_054_cth_basefill_054}


def cth_base_universe_d2_055_cth_basefill_055(cth_basefill_055):
    return _base_universe_d2(cth_basefill_055, 55)
CTH_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['cth_base_universe_d2_055_cth_basefill_055'] = {'inputs': ['cth_basefill_055'], 'func': cth_base_universe_d2_055_cth_basefill_055}


def cth_base_universe_d2_056_cth_basefill_056(cth_basefill_056):
    return _base_universe_d2(cth_basefill_056, 56)
CTH_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['cth_base_universe_d2_056_cth_basefill_056'] = {'inputs': ['cth_basefill_056'], 'func': cth_base_universe_d2_056_cth_basefill_056}


def cth_base_universe_d2_057_cth_basefill_057(cth_basefill_057):
    return _base_universe_d2(cth_basefill_057, 57)
CTH_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['cth_base_universe_d2_057_cth_basefill_057'] = {'inputs': ['cth_basefill_057'], 'func': cth_base_universe_d2_057_cth_basefill_057}


def cth_base_universe_d2_058_cth_basefill_058(cth_basefill_058):
    return _base_universe_d2(cth_basefill_058, 58)
CTH_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['cth_base_universe_d2_058_cth_basefill_058'] = {'inputs': ['cth_basefill_058'], 'func': cth_base_universe_d2_058_cth_basefill_058}


def cth_base_universe_d2_059_cth_basefill_059(cth_basefill_059):
    return _base_universe_d2(cth_basefill_059, 59)
CTH_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['cth_base_universe_d2_059_cth_basefill_059'] = {'inputs': ['cth_basefill_059'], 'func': cth_base_universe_d2_059_cth_basefill_059}


def cth_base_universe_d2_060_cth_basefill_060(cth_basefill_060):
    return _base_universe_d2(cth_basefill_060, 60)
CTH_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['cth_base_universe_d2_060_cth_basefill_060'] = {'inputs': ['cth_basefill_060'], 'func': cth_base_universe_d2_060_cth_basefill_060}


def cth_base_universe_d2_061_cth_basefill_061(cth_basefill_061):
    return _base_universe_d2(cth_basefill_061, 61)
CTH_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['cth_base_universe_d2_061_cth_basefill_061'] = {'inputs': ['cth_basefill_061'], 'func': cth_base_universe_d2_061_cth_basefill_061}


def cth_base_universe_d2_062_cth_basefill_062(cth_basefill_062):
    return _base_universe_d2(cth_basefill_062, 62)
CTH_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['cth_base_universe_d2_062_cth_basefill_062'] = {'inputs': ['cth_basefill_062'], 'func': cth_base_universe_d2_062_cth_basefill_062}


def cth_base_universe_d2_063_cth_basefill_063(cth_basefill_063):
    return _base_universe_d2(cth_basefill_063, 63)
CTH_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['cth_base_universe_d2_063_cth_basefill_063'] = {'inputs': ['cth_basefill_063'], 'func': cth_base_universe_d2_063_cth_basefill_063}


def cth_base_universe_d2_064_cth_basefill_064(cth_basefill_064):
    return _base_universe_d2(cth_basefill_064, 64)
CTH_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['cth_base_universe_d2_064_cth_basefill_064'] = {'inputs': ['cth_basefill_064'], 'func': cth_base_universe_d2_064_cth_basefill_064}


def cth_base_universe_d2_065_cth_basefill_065(cth_basefill_065):
    return _base_universe_d2(cth_basefill_065, 65)
CTH_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['cth_base_universe_d2_065_cth_basefill_065'] = {'inputs': ['cth_basefill_065'], 'func': cth_base_universe_d2_065_cth_basefill_065}


def cth_base_universe_d2_066_cth_basefill_066(cth_basefill_066):
    return _base_universe_d2(cth_basefill_066, 66)
CTH_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['cth_base_universe_d2_066_cth_basefill_066'] = {'inputs': ['cth_basefill_066'], 'func': cth_base_universe_d2_066_cth_basefill_066}


def cth_base_universe_d2_067_cth_basefill_067(cth_basefill_067):
    return _base_universe_d2(cth_basefill_067, 67)
CTH_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['cth_base_universe_d2_067_cth_basefill_067'] = {'inputs': ['cth_basefill_067'], 'func': cth_base_universe_d2_067_cth_basefill_067}


def cth_base_universe_d2_068_cth_basefill_068(cth_basefill_068):
    return _base_universe_d2(cth_basefill_068, 68)
CTH_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['cth_base_universe_d2_068_cth_basefill_068'] = {'inputs': ['cth_basefill_068'], 'func': cth_base_universe_d2_068_cth_basefill_068}


def cth_base_universe_d2_069_cth_basefill_069(cth_basefill_069):
    return _base_universe_d2(cth_basefill_069, 69)
CTH_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['cth_base_universe_d2_069_cth_basefill_069'] = {'inputs': ['cth_basefill_069'], 'func': cth_base_universe_d2_069_cth_basefill_069}


def cth_base_universe_d2_070_cth_basefill_070(cth_basefill_070):
    return _base_universe_d2(cth_basefill_070, 70)
CTH_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['cth_base_universe_d2_070_cth_basefill_070'] = {'inputs': ['cth_basefill_070'], 'func': cth_base_universe_d2_070_cth_basefill_070}


def cth_base_universe_d2_071_cth_basefill_071(cth_basefill_071):
    return _base_universe_d2(cth_basefill_071, 71)
CTH_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['cth_base_universe_d2_071_cth_basefill_071'] = {'inputs': ['cth_basefill_071'], 'func': cth_base_universe_d2_071_cth_basefill_071}


def cth_base_universe_d2_072_cth_basefill_072(cth_basefill_072):
    return _base_universe_d2(cth_basefill_072, 72)
CTH_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['cth_base_universe_d2_072_cth_basefill_072'] = {'inputs': ['cth_basefill_072'], 'func': cth_base_universe_d2_072_cth_basefill_072}


def cth_base_universe_d2_073_cth_basefill_073(cth_basefill_073):
    return _base_universe_d2(cth_basefill_073, 73)
CTH_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['cth_base_universe_d2_073_cth_basefill_073'] = {'inputs': ['cth_basefill_073'], 'func': cth_base_universe_d2_073_cth_basefill_073}


def cth_base_universe_d2_074_cth_basefill_074(cth_basefill_074):
    return _base_universe_d2(cth_basefill_074, 74)
CTH_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['cth_base_universe_d2_074_cth_basefill_074'] = {'inputs': ['cth_basefill_074'], 'func': cth_base_universe_d2_074_cth_basefill_074}


def cth_base_universe_d2_075_cth_basefill_075(cth_basefill_075):
    return _base_universe_d2(cth_basefill_075, 75)
CTH_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['cth_base_universe_d2_075_cth_basefill_075'] = {'inputs': ['cth_basefill_075'], 'func': cth_base_universe_d2_075_cth_basefill_075}
