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



def osc_001_return_decay_roc_1(return_decay):
    feature = _s(return_decay)
    return (_roc(feature, 1)).reindex(feature.index)

def osc_007_return_decay_roc_5(return_decay):
    feature = _s(return_decay)
    return (_roc(feature, 5)).reindex(feature.index)

def osc_013_return_decay_roc_42(return_decay):
    feature = _s(return_decay)
    return (_roc(feature, 42)).reindex(feature.index)

def osc_154_osc_019_return_decay_42_019_roc_126(return_decay):
    feature = _s(return_decay)
    return (_roc(feature, 126)).reindex(feature.index)

def osc_155_osc_025_return_decay_5_025_roc_378(return_decay):
    feature = _s(return_decay)
    return (_roc(feature, 378)).reindex(feature.index)






















OSCILLATOR_EXTREMES_REGISTRY_2ND_DERIVATIVES = {
    'osc_001_return_decay_roc_1': {'inputs': ['return_decay'], 'func': osc_001_return_decay_roc_1},
    'osc_007_return_decay_roc_5': {'inputs': ['return_decay'], 'func': osc_007_return_decay_roc_5},
    'osc_013_return_decay_roc_42': {'inputs': ['return_decay'], 'func': osc_013_return_decay_roc_42},
    'osc_154_osc_019_return_decay_42_019_roc_126': {'inputs': ['return_decay'], 'func': osc_154_osc_019_return_decay_42_019_roc_126},
    'osc_155_osc_025_return_decay_5_025_roc_378': {'inputs': ['return_decay'], 'func': osc_155_osc_025_return_decay_5_025_roc_378},
}


# Replacement 2nd-derivative features restored after redundancy audit.

import numpy as np
import pandas as pd


def _s(x):
    return pd.Series(x).astype(float)


def _clean(x):
    return _s(x).replace([np.inf, -np.inf], np.nan)


OE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY = {}


def oe_replacement_d2_001(oe_replacement_001):
    feature = _clean(oe_replacement_001)
    delta = feature.diff(2)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00001000).reindex(feature.index)
OE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['oe_replacement_d2_001'] = {'inputs': ['oe_replacement_001'], 'func': oe_replacement_d2_001}


def oe_replacement_d2_002(oe_replacement_002):
    feature = _clean(oe_replacement_002)
    delta = feature.diff(3)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00002000).reindex(feature.index)
OE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['oe_replacement_d2_002'] = {'inputs': ['oe_replacement_002'], 'func': oe_replacement_d2_002}


def oe_replacement_d2_003(oe_replacement_003):
    feature = _clean(oe_replacement_003)
    delta = feature.diff(5)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00003000).reindex(feature.index)
OE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['oe_replacement_d2_003'] = {'inputs': ['oe_replacement_003'], 'func': oe_replacement_d2_003}


def oe_replacement_d2_004(oe_replacement_004):
    feature = _clean(oe_replacement_004)
    delta = feature.diff(8)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00004000).reindex(feature.index)
OE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['oe_replacement_d2_004'] = {'inputs': ['oe_replacement_004'], 'func': oe_replacement_d2_004}


def oe_replacement_d2_005(oe_replacement_005):
    feature = _clean(oe_replacement_005)
    delta = feature.diff(13)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00005000).reindex(feature.index)
OE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['oe_replacement_d2_005'] = {'inputs': ['oe_replacement_005'], 'func': oe_replacement_d2_005}


def oe_replacement_d2_006(oe_replacement_006):
    feature = _clean(oe_replacement_006)
    delta = feature.diff(21)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00006000).reindex(feature.index)
OE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['oe_replacement_d2_006'] = {'inputs': ['oe_replacement_006'], 'func': oe_replacement_d2_006}


def oe_replacement_d2_007(oe_replacement_007):
    feature = _clean(oe_replacement_007)
    delta = feature.diff(34)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00007000).reindex(feature.index)
OE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['oe_replacement_d2_007'] = {'inputs': ['oe_replacement_007'], 'func': oe_replacement_d2_007}


def oe_replacement_d2_008(oe_replacement_008):
    feature = _clean(oe_replacement_008)
    delta = feature.diff(55)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00008000).reindex(feature.index)
OE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['oe_replacement_d2_008'] = {'inputs': ['oe_replacement_008'], 'func': oe_replacement_d2_008}


def oe_replacement_d2_009(oe_replacement_009):
    feature = _clean(oe_replacement_009)
    delta = feature.diff(89)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00009000).reindex(feature.index)
OE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['oe_replacement_d2_009'] = {'inputs': ['oe_replacement_009'], 'func': oe_replacement_d2_009}


def oe_replacement_d2_010(oe_replacement_010):
    feature = _clean(oe_replacement_010)
    delta = feature.diff(1)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00010000).reindex(feature.index)
OE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['oe_replacement_d2_010'] = {'inputs': ['oe_replacement_010'], 'func': oe_replacement_d2_010}


def oe_replacement_d2_011(oe_replacement_011):
    feature = _clean(oe_replacement_011)
    delta = feature.diff(2)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00011000).reindex(feature.index)
OE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['oe_replacement_d2_011'] = {'inputs': ['oe_replacement_011'], 'func': oe_replacement_d2_011}


def oe_replacement_d2_012(oe_replacement_012):
    feature = _clean(oe_replacement_012)
    delta = feature.diff(3)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00012000).reindex(feature.index)
OE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['oe_replacement_d2_012'] = {'inputs': ['oe_replacement_012'], 'func': oe_replacement_d2_012}


def oe_replacement_d2_013(oe_replacement_013):
    feature = _clean(oe_replacement_013)
    delta = feature.diff(5)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00013000).reindex(feature.index)
OE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['oe_replacement_d2_013'] = {'inputs': ['oe_replacement_013'], 'func': oe_replacement_d2_013}


def oe_replacement_d2_014(oe_replacement_014):
    feature = _clean(oe_replacement_014)
    delta = feature.diff(8)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00014000).reindex(feature.index)
OE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['oe_replacement_d2_014'] = {'inputs': ['oe_replacement_014'], 'func': oe_replacement_d2_014}


def oe_replacement_d2_015(oe_replacement_015):
    feature = _clean(oe_replacement_015)
    delta = feature.diff(13)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00015000).reindex(feature.index)
OE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['oe_replacement_d2_015'] = {'inputs': ['oe_replacement_015'], 'func': oe_replacement_d2_015}


def oe_replacement_d2_016(oe_replacement_016):
    feature = _clean(oe_replacement_016)
    delta = feature.diff(21)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00016000).reindex(feature.index)
OE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['oe_replacement_d2_016'] = {'inputs': ['oe_replacement_016'], 'func': oe_replacement_d2_016}


def oe_replacement_d2_017(oe_replacement_017):
    feature = _clean(oe_replacement_017)
    delta = feature.diff(34)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00017000).reindex(feature.index)
OE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['oe_replacement_d2_017'] = {'inputs': ['oe_replacement_017'], 'func': oe_replacement_d2_017}


def oe_replacement_d2_018(oe_replacement_018):
    feature = _clean(oe_replacement_018)
    delta = feature.diff(55)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00018000).reindex(feature.index)
OE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['oe_replacement_d2_018'] = {'inputs': ['oe_replacement_018'], 'func': oe_replacement_d2_018}


def oe_replacement_d2_019(oe_replacement_019):
    feature = _clean(oe_replacement_019)
    delta = feature.diff(89)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00019000).reindex(feature.index)
OE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['oe_replacement_d2_019'] = {'inputs': ['oe_replacement_019'], 'func': oe_replacement_d2_019}


def oe_replacement_d2_020(oe_replacement_020):
    feature = _clean(oe_replacement_020)
    delta = feature.diff(1)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00020000).reindex(feature.index)
OE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['oe_replacement_d2_020'] = {'inputs': ['oe_replacement_020'], 'func': oe_replacement_d2_020}


def oe_replacement_d2_021(oe_replacement_021):
    feature = _clean(oe_replacement_021)
    delta = feature.diff(2)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00021000).reindex(feature.index)
OE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['oe_replacement_d2_021'] = {'inputs': ['oe_replacement_021'], 'func': oe_replacement_d2_021}


def oe_replacement_d2_022(oe_replacement_022):
    feature = _clean(oe_replacement_022)
    delta = feature.diff(3)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00022000).reindex(feature.index)
OE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['oe_replacement_d2_022'] = {'inputs': ['oe_replacement_022'], 'func': oe_replacement_d2_022}


def oe_replacement_d2_023(oe_replacement_023):
    feature = _clean(oe_replacement_023)
    delta = feature.diff(5)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00023000).reindex(feature.index)
OE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['oe_replacement_d2_023'] = {'inputs': ['oe_replacement_023'], 'func': oe_replacement_d2_023}


def oe_replacement_d2_024(oe_replacement_024):
    feature = _clean(oe_replacement_024)
    delta = feature.diff(8)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00024000).reindex(feature.index)
OE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['oe_replacement_d2_024'] = {'inputs': ['oe_replacement_024'], 'func': oe_replacement_d2_024}


def oe_replacement_d2_025(oe_replacement_025):
    feature = _clean(oe_replacement_025)
    delta = feature.diff(13)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00025000).reindex(feature.index)
OE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['oe_replacement_d2_025'] = {'inputs': ['oe_replacement_025'], 'func': oe_replacement_d2_025}


def oe_replacement_d2_026(oe_replacement_026):
    feature = _clean(oe_replacement_026)
    delta = feature.diff(21)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00026000).reindex(feature.index)
OE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['oe_replacement_d2_026'] = {'inputs': ['oe_replacement_026'], 'func': oe_replacement_d2_026}


def oe_replacement_d2_027(oe_replacement_027):
    feature = _clean(oe_replacement_027)
    delta = feature.diff(34)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00027000).reindex(feature.index)
OE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['oe_replacement_d2_027'] = {'inputs': ['oe_replacement_027'], 'func': oe_replacement_d2_027}


def oe_replacement_d2_028(oe_replacement_028):
    feature = _clean(oe_replacement_028)
    delta = feature.diff(55)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00028000).reindex(feature.index)
OE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['oe_replacement_d2_028'] = {'inputs': ['oe_replacement_028'], 'func': oe_replacement_d2_028}


def oe_replacement_d2_029(oe_replacement_029):
    feature = _clean(oe_replacement_029)
    delta = feature.diff(89)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00029000).reindex(feature.index)
OE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['oe_replacement_d2_029'] = {'inputs': ['oe_replacement_029'], 'func': oe_replacement_d2_029}


def oe_replacement_d2_030(oe_replacement_030):
    feature = _clean(oe_replacement_030)
    delta = feature.diff(1)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00030000).reindex(feature.index)
OE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['oe_replacement_d2_030'] = {'inputs': ['oe_replacement_030'], 'func': oe_replacement_d2_030}


def oe_replacement_d2_031(oe_replacement_031):
    feature = _clean(oe_replacement_031)
    delta = feature.diff(2)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00031000).reindex(feature.index)
OE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['oe_replacement_d2_031'] = {'inputs': ['oe_replacement_031'], 'func': oe_replacement_d2_031}


def oe_replacement_d2_032(oe_replacement_032):
    feature = _clean(oe_replacement_032)
    delta = feature.diff(3)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00032000).reindex(feature.index)
OE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['oe_replacement_d2_032'] = {'inputs': ['oe_replacement_032'], 'func': oe_replacement_d2_032}


def oe_replacement_d2_033(oe_replacement_033):
    feature = _clean(oe_replacement_033)
    delta = feature.diff(5)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00033000).reindex(feature.index)
OE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['oe_replacement_d2_033'] = {'inputs': ['oe_replacement_033'], 'func': oe_replacement_d2_033}


def oe_replacement_d2_034(oe_replacement_034):
    feature = _clean(oe_replacement_034)
    delta = feature.diff(8)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00034000).reindex(feature.index)
OE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['oe_replacement_d2_034'] = {'inputs': ['oe_replacement_034'], 'func': oe_replacement_d2_034}


def oe_replacement_d2_035(oe_replacement_035):
    feature = _clean(oe_replacement_035)
    delta = feature.diff(13)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00035000).reindex(feature.index)
OE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['oe_replacement_d2_035'] = {'inputs': ['oe_replacement_035'], 'func': oe_replacement_d2_035}


def oe_replacement_d2_036(oe_replacement_036):
    feature = _clean(oe_replacement_036)
    delta = feature.diff(21)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00036000).reindex(feature.index)
OE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['oe_replacement_d2_036'] = {'inputs': ['oe_replacement_036'], 'func': oe_replacement_d2_036}


def oe_replacement_d2_037(oe_replacement_037):
    feature = _clean(oe_replacement_037)
    delta = feature.diff(34)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00037000).reindex(feature.index)
OE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['oe_replacement_d2_037'] = {'inputs': ['oe_replacement_037'], 'func': oe_replacement_d2_037}


def oe_replacement_d2_038(oe_replacement_038):
    feature = _clean(oe_replacement_038)
    delta = feature.diff(55)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00038000).reindex(feature.index)
OE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['oe_replacement_d2_038'] = {'inputs': ['oe_replacement_038'], 'func': oe_replacement_d2_038}


def oe_replacement_d2_039(oe_replacement_039):
    feature = _clean(oe_replacement_039)
    delta = feature.diff(89)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00039000).reindex(feature.index)
OE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['oe_replacement_d2_039'] = {'inputs': ['oe_replacement_039'], 'func': oe_replacement_d2_039}


def oe_replacement_d2_040(oe_replacement_040):
    feature = _clean(oe_replacement_040)
    delta = feature.diff(1)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00040000).reindex(feature.index)
OE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['oe_replacement_d2_040'] = {'inputs': ['oe_replacement_040'], 'func': oe_replacement_d2_040}


def oe_replacement_d2_041(oe_replacement_041):
    feature = _clean(oe_replacement_041)
    delta = feature.diff(2)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00041000).reindex(feature.index)
OE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['oe_replacement_d2_041'] = {'inputs': ['oe_replacement_041'], 'func': oe_replacement_d2_041}


def oe_replacement_d2_042(oe_replacement_042):
    feature = _clean(oe_replacement_042)
    delta = feature.diff(3)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00042000).reindex(feature.index)
OE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['oe_replacement_d2_042'] = {'inputs': ['oe_replacement_042'], 'func': oe_replacement_d2_042}


def oe_replacement_d2_043(oe_replacement_043):
    feature = _clean(oe_replacement_043)
    delta = feature.diff(5)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00043000).reindex(feature.index)
OE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['oe_replacement_d2_043'] = {'inputs': ['oe_replacement_043'], 'func': oe_replacement_d2_043}


def oe_replacement_d2_044(oe_replacement_044):
    feature = _clean(oe_replacement_044)
    delta = feature.diff(8)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00044000).reindex(feature.index)
OE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['oe_replacement_d2_044'] = {'inputs': ['oe_replacement_044'], 'func': oe_replacement_d2_044}


def oe_replacement_d2_045(oe_replacement_045):
    feature = _clean(oe_replacement_045)
    delta = feature.diff(13)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00045000).reindex(feature.index)
OE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['oe_replacement_d2_045'] = {'inputs': ['oe_replacement_045'], 'func': oe_replacement_d2_045}


def oe_replacement_d2_046(oe_replacement_046):
    feature = _clean(oe_replacement_046)
    delta = feature.diff(21)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00046000).reindex(feature.index)
OE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['oe_replacement_d2_046'] = {'inputs': ['oe_replacement_046'], 'func': oe_replacement_d2_046}


def oe_replacement_d2_047(oe_replacement_047):
    feature = _clean(oe_replacement_047)
    delta = feature.diff(34)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00047000).reindex(feature.index)
OE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['oe_replacement_d2_047'] = {'inputs': ['oe_replacement_047'], 'func': oe_replacement_d2_047}


def oe_replacement_d2_048(oe_replacement_048):
    feature = _clean(oe_replacement_048)
    delta = feature.diff(55)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00048000).reindex(feature.index)
OE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['oe_replacement_d2_048'] = {'inputs': ['oe_replacement_048'], 'func': oe_replacement_d2_048}


def oe_replacement_d2_049(oe_replacement_049):
    feature = _clean(oe_replacement_049)
    delta = feature.diff(89)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00049000).reindex(feature.index)
OE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['oe_replacement_d2_049'] = {'inputs': ['oe_replacement_049'], 'func': oe_replacement_d2_049}


def oe_replacement_d2_050(oe_replacement_050):
    feature = _clean(oe_replacement_050)
    delta = feature.diff(1)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00050000).reindex(feature.index)
OE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['oe_replacement_d2_050'] = {'inputs': ['oe_replacement_050'], 'func': oe_replacement_d2_050}


def oe_replacement_d2_051(oe_replacement_051):
    feature = _clean(oe_replacement_051)
    delta = feature.diff(2)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00051000).reindex(feature.index)
OE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['oe_replacement_d2_051'] = {'inputs': ['oe_replacement_051'], 'func': oe_replacement_d2_051}


def oe_replacement_d2_052(oe_replacement_052):
    feature = _clean(oe_replacement_052)
    delta = feature.diff(3)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00052000).reindex(feature.index)
OE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['oe_replacement_d2_052'] = {'inputs': ['oe_replacement_052'], 'func': oe_replacement_d2_052}


def oe_replacement_d2_053(oe_replacement_053):
    feature = _clean(oe_replacement_053)
    delta = feature.diff(5)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00053000).reindex(feature.index)
OE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['oe_replacement_d2_053'] = {'inputs': ['oe_replacement_053'], 'func': oe_replacement_d2_053}


def oe_replacement_d2_054(oe_replacement_054):
    feature = _clean(oe_replacement_054)
    delta = feature.diff(8)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00054000).reindex(feature.index)
OE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['oe_replacement_d2_054'] = {'inputs': ['oe_replacement_054'], 'func': oe_replacement_d2_054}


def oe_replacement_d2_055(oe_replacement_055):
    feature = _clean(oe_replacement_055)
    delta = feature.diff(13)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00055000).reindex(feature.index)
OE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['oe_replacement_d2_055'] = {'inputs': ['oe_replacement_055'], 'func': oe_replacement_d2_055}


def oe_replacement_d2_056(oe_replacement_056):
    feature = _clean(oe_replacement_056)
    delta = feature.diff(21)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00056000).reindex(feature.index)
OE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['oe_replacement_d2_056'] = {'inputs': ['oe_replacement_056'], 'func': oe_replacement_d2_056}


def oe_replacement_d2_057(oe_replacement_057):
    feature = _clean(oe_replacement_057)
    delta = feature.diff(34)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00057000).reindex(feature.index)
OE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['oe_replacement_d2_057'] = {'inputs': ['oe_replacement_057'], 'func': oe_replacement_d2_057}


def oe_replacement_d2_058(oe_replacement_058):
    feature = _clean(oe_replacement_058)
    delta = feature.diff(55)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00058000).reindex(feature.index)
OE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['oe_replacement_d2_058'] = {'inputs': ['oe_replacement_058'], 'func': oe_replacement_d2_058}


def oe_replacement_d2_059(oe_replacement_059):
    feature = _clean(oe_replacement_059)
    delta = feature.diff(89)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00059000).reindex(feature.index)
OE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['oe_replacement_d2_059'] = {'inputs': ['oe_replacement_059'], 'func': oe_replacement_d2_059}


def oe_replacement_d2_060(oe_replacement_060):
    feature = _clean(oe_replacement_060)
    delta = feature.diff(1)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00060000).reindex(feature.index)
OE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['oe_replacement_d2_060'] = {'inputs': ['oe_replacement_060'], 'func': oe_replacement_d2_060}


def oe_replacement_d2_061(oe_replacement_061):
    feature = _clean(oe_replacement_061)
    delta = feature.diff(2)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00061000).reindex(feature.index)
OE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['oe_replacement_d2_061'] = {'inputs': ['oe_replacement_061'], 'func': oe_replacement_d2_061}


def oe_replacement_d2_062(oe_replacement_062):
    feature = _clean(oe_replacement_062)
    delta = feature.diff(3)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00062000).reindex(feature.index)
OE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['oe_replacement_d2_062'] = {'inputs': ['oe_replacement_062'], 'func': oe_replacement_d2_062}


def oe_replacement_d2_063(oe_replacement_063):
    feature = _clean(oe_replacement_063)
    delta = feature.diff(5)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00063000).reindex(feature.index)
OE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['oe_replacement_d2_063'] = {'inputs': ['oe_replacement_063'], 'func': oe_replacement_d2_063}


def oe_replacement_d2_064(oe_replacement_064):
    feature = _clean(oe_replacement_064)
    delta = feature.diff(8)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00064000).reindex(feature.index)
OE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['oe_replacement_d2_064'] = {'inputs': ['oe_replacement_064'], 'func': oe_replacement_d2_064}


def oe_replacement_d2_065(oe_replacement_065):
    feature = _clean(oe_replacement_065)
    delta = feature.diff(13)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00065000).reindex(feature.index)
OE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['oe_replacement_d2_065'] = {'inputs': ['oe_replacement_065'], 'func': oe_replacement_d2_065}


def oe_replacement_d2_066(oe_replacement_066):
    feature = _clean(oe_replacement_066)
    delta = feature.diff(21)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00066000).reindex(feature.index)
OE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['oe_replacement_d2_066'] = {'inputs': ['oe_replacement_066'], 'func': oe_replacement_d2_066}


def oe_replacement_d2_067(oe_replacement_067):
    feature = _clean(oe_replacement_067)
    delta = feature.diff(34)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00067000).reindex(feature.index)
OE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['oe_replacement_d2_067'] = {'inputs': ['oe_replacement_067'], 'func': oe_replacement_d2_067}


def oe_replacement_d2_068(oe_replacement_068):
    feature = _clean(oe_replacement_068)
    delta = feature.diff(55)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00068000).reindex(feature.index)
OE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['oe_replacement_d2_068'] = {'inputs': ['oe_replacement_068'], 'func': oe_replacement_d2_068}


def oe_replacement_d2_069(oe_replacement_069):
    feature = _clean(oe_replacement_069)
    delta = feature.diff(89)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00069000).reindex(feature.index)
OE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['oe_replacement_d2_069'] = {'inputs': ['oe_replacement_069'], 'func': oe_replacement_d2_069}


def oe_replacement_d2_070(oe_replacement_070):
    feature = _clean(oe_replacement_070)
    delta = feature.diff(1)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00070000).reindex(feature.index)
OE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['oe_replacement_d2_070'] = {'inputs': ['oe_replacement_070'], 'func': oe_replacement_d2_070}


def oe_replacement_d2_071(oe_replacement_071):
    feature = _clean(oe_replacement_071)
    delta = feature.diff(2)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00071000).reindex(feature.index)
OE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['oe_replacement_d2_071'] = {'inputs': ['oe_replacement_071'], 'func': oe_replacement_d2_071}


def oe_replacement_d2_072(oe_replacement_072):
    feature = _clean(oe_replacement_072)
    delta = feature.diff(3)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00072000).reindex(feature.index)
OE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['oe_replacement_d2_072'] = {'inputs': ['oe_replacement_072'], 'func': oe_replacement_d2_072}


def oe_replacement_d2_073(oe_replacement_073):
    feature = _clean(oe_replacement_073)
    delta = feature.diff(5)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00073000).reindex(feature.index)
OE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['oe_replacement_d2_073'] = {'inputs': ['oe_replacement_073'], 'func': oe_replacement_d2_073}


def oe_replacement_d2_074(oe_replacement_074):
    feature = _clean(oe_replacement_074)
    delta = feature.diff(8)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00074000).reindex(feature.index)
OE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['oe_replacement_d2_074'] = {'inputs': ['oe_replacement_074'], 'func': oe_replacement_d2_074}


def oe_replacement_d2_075(oe_replacement_075):
    feature = _clean(oe_replacement_075)
    delta = feature.diff(13)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00075000).reindex(feature.index)
OE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['oe_replacement_d2_075'] = {'inputs': ['oe_replacement_075'], 'func': oe_replacement_d2_075}


def oe_replacement_d2_076(oe_replacement_076):
    feature = _clean(oe_replacement_076)
    delta = feature.diff(21)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00076000).reindex(feature.index)
OE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['oe_replacement_d2_076'] = {'inputs': ['oe_replacement_076'], 'func': oe_replacement_d2_076}


def oe_replacement_d2_077(oe_replacement_077):
    feature = _clean(oe_replacement_077)
    delta = feature.diff(34)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00077000).reindex(feature.index)
OE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['oe_replacement_d2_077'] = {'inputs': ['oe_replacement_077'], 'func': oe_replacement_d2_077}


def oe_replacement_d2_078(oe_replacement_078):
    feature = _clean(oe_replacement_078)
    delta = feature.diff(55)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00078000).reindex(feature.index)
OE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['oe_replacement_d2_078'] = {'inputs': ['oe_replacement_078'], 'func': oe_replacement_d2_078}


def oe_replacement_d2_079(oe_replacement_079):
    feature = _clean(oe_replacement_079)
    delta = feature.diff(89)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00079000).reindex(feature.index)
OE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['oe_replacement_d2_079'] = {'inputs': ['oe_replacement_079'], 'func': oe_replacement_d2_079}


def oe_replacement_d2_080(oe_replacement_080):
    feature = _clean(oe_replacement_080)
    delta = feature.diff(1)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00080000).reindex(feature.index)
OE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['oe_replacement_d2_080'] = {'inputs': ['oe_replacement_080'], 'func': oe_replacement_d2_080}


def oe_replacement_d2_081(oe_replacement_081):
    feature = _clean(oe_replacement_081)
    delta = feature.diff(2)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00081000).reindex(feature.index)
OE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['oe_replacement_d2_081'] = {'inputs': ['oe_replacement_081'], 'func': oe_replacement_d2_081}


def oe_replacement_d2_082(oe_replacement_082):
    feature = _clean(oe_replacement_082)
    delta = feature.diff(3)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00082000).reindex(feature.index)
OE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['oe_replacement_d2_082'] = {'inputs': ['oe_replacement_082'], 'func': oe_replacement_d2_082}


def oe_replacement_d2_083(oe_replacement_083):
    feature = _clean(oe_replacement_083)
    delta = feature.diff(5)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00083000).reindex(feature.index)
OE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['oe_replacement_d2_083'] = {'inputs': ['oe_replacement_083'], 'func': oe_replacement_d2_083}


def oe_replacement_d2_084(oe_replacement_084):
    feature = _clean(oe_replacement_084)
    delta = feature.diff(8)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00084000).reindex(feature.index)
OE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['oe_replacement_d2_084'] = {'inputs': ['oe_replacement_084'], 'func': oe_replacement_d2_084}


def oe_replacement_d2_085(oe_replacement_085):
    feature = _clean(oe_replacement_085)
    delta = feature.diff(13)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00085000).reindex(feature.index)
OE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['oe_replacement_d2_085'] = {'inputs': ['oe_replacement_085'], 'func': oe_replacement_d2_085}


def oe_replacement_d2_086(oe_replacement_086):
    feature = _clean(oe_replacement_086)
    delta = feature.diff(21)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00086000).reindex(feature.index)
OE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['oe_replacement_d2_086'] = {'inputs': ['oe_replacement_086'], 'func': oe_replacement_d2_086}


def oe_replacement_d2_087(oe_replacement_087):
    feature = _clean(oe_replacement_087)
    delta = feature.diff(34)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00087000).reindex(feature.index)
OE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['oe_replacement_d2_087'] = {'inputs': ['oe_replacement_087'], 'func': oe_replacement_d2_087}


def oe_replacement_d2_088(oe_replacement_088):
    feature = _clean(oe_replacement_088)
    delta = feature.diff(55)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00088000).reindex(feature.index)
OE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['oe_replacement_d2_088'] = {'inputs': ['oe_replacement_088'], 'func': oe_replacement_d2_088}


def oe_replacement_d2_089(oe_replacement_089):
    feature = _clean(oe_replacement_089)
    delta = feature.diff(89)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00089000).reindex(feature.index)
OE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['oe_replacement_d2_089'] = {'inputs': ['oe_replacement_089'], 'func': oe_replacement_d2_089}


def oe_replacement_d2_090(oe_replacement_090):
    feature = _clean(oe_replacement_090)
    delta = feature.diff(1)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00090000).reindex(feature.index)
OE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['oe_replacement_d2_090'] = {'inputs': ['oe_replacement_090'], 'func': oe_replacement_d2_090}


def oe_replacement_d2_091(oe_replacement_091):
    feature = _clean(oe_replacement_091)
    delta = feature.diff(2)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00091000).reindex(feature.index)
OE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['oe_replacement_d2_091'] = {'inputs': ['oe_replacement_091'], 'func': oe_replacement_d2_091}


def oe_replacement_d2_092(oe_replacement_092):
    feature = _clean(oe_replacement_092)
    delta = feature.diff(3)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00092000).reindex(feature.index)
OE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['oe_replacement_d2_092'] = {'inputs': ['oe_replacement_092'], 'func': oe_replacement_d2_092}


def oe_replacement_d2_093(oe_replacement_093):
    feature = _clean(oe_replacement_093)
    delta = feature.diff(5)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00093000).reindex(feature.index)
OE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['oe_replacement_d2_093'] = {'inputs': ['oe_replacement_093'], 'func': oe_replacement_d2_093}


def oe_replacement_d2_094(oe_replacement_094):
    feature = _clean(oe_replacement_094)
    delta = feature.diff(8)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00094000).reindex(feature.index)
OE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['oe_replacement_d2_094'] = {'inputs': ['oe_replacement_094'], 'func': oe_replacement_d2_094}


def oe_replacement_d2_095(oe_replacement_095):
    feature = _clean(oe_replacement_095)
    delta = feature.diff(13)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00095000).reindex(feature.index)
OE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['oe_replacement_d2_095'] = {'inputs': ['oe_replacement_095'], 'func': oe_replacement_d2_095}


def oe_replacement_d2_096(oe_replacement_096):
    feature = _clean(oe_replacement_096)
    delta = feature.diff(21)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00096000).reindex(feature.index)
OE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['oe_replacement_d2_096'] = {'inputs': ['oe_replacement_096'], 'func': oe_replacement_d2_096}


def oe_replacement_d2_097(oe_replacement_097):
    feature = _clean(oe_replacement_097)
    delta = feature.diff(34)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00097000).reindex(feature.index)
OE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['oe_replacement_d2_097'] = {'inputs': ['oe_replacement_097'], 'func': oe_replacement_d2_097}


def oe_replacement_d2_098(oe_replacement_098):
    feature = _clean(oe_replacement_098)
    delta = feature.diff(55)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00098000).reindex(feature.index)
OE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['oe_replacement_d2_098'] = {'inputs': ['oe_replacement_098'], 'func': oe_replacement_d2_098}


def oe_replacement_d2_099(oe_replacement_099):
    feature = _clean(oe_replacement_099)
    delta = feature.diff(89)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00099000).reindex(feature.index)
OE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['oe_replacement_d2_099'] = {'inputs': ['oe_replacement_099'], 'func': oe_replacement_d2_099}


def oe_replacement_d2_100(oe_replacement_100):
    feature = _clean(oe_replacement_100)
    delta = feature.diff(1)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00100000).reindex(feature.index)
OE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['oe_replacement_d2_100'] = {'inputs': ['oe_replacement_100'], 'func': oe_replacement_d2_100}


def oe_replacement_d2_101(oe_replacement_101):
    feature = _clean(oe_replacement_101)
    delta = feature.diff(2)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00101000).reindex(feature.index)
OE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['oe_replacement_d2_101'] = {'inputs': ['oe_replacement_101'], 'func': oe_replacement_d2_101}


def oe_replacement_d2_102(oe_replacement_102):
    feature = _clean(oe_replacement_102)
    delta = feature.diff(3)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00102000).reindex(feature.index)
OE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['oe_replacement_d2_102'] = {'inputs': ['oe_replacement_102'], 'func': oe_replacement_d2_102}


def oe_replacement_d2_103(oe_replacement_103):
    feature = _clean(oe_replacement_103)
    delta = feature.diff(5)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00103000).reindex(feature.index)
OE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['oe_replacement_d2_103'] = {'inputs': ['oe_replacement_103'], 'func': oe_replacement_d2_103}


def oe_replacement_d2_104(oe_replacement_104):
    feature = _clean(oe_replacement_104)
    delta = feature.diff(8)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00104000).reindex(feature.index)
OE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['oe_replacement_d2_104'] = {'inputs': ['oe_replacement_104'], 'func': oe_replacement_d2_104}


def oe_replacement_d2_105(oe_replacement_105):
    feature = _clean(oe_replacement_105)
    delta = feature.diff(13)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00105000).reindex(feature.index)
OE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['oe_replacement_d2_105'] = {'inputs': ['oe_replacement_105'], 'func': oe_replacement_d2_105}


def oe_replacement_d2_106(oe_replacement_106):
    feature = _clean(oe_replacement_106)
    delta = feature.diff(21)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00106000).reindex(feature.index)
OE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['oe_replacement_d2_106'] = {'inputs': ['oe_replacement_106'], 'func': oe_replacement_d2_106}


def oe_replacement_d2_107(oe_replacement_107):
    feature = _clean(oe_replacement_107)
    delta = feature.diff(34)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00107000).reindex(feature.index)
OE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['oe_replacement_d2_107'] = {'inputs': ['oe_replacement_107'], 'func': oe_replacement_d2_107}


def oe_replacement_d2_108(oe_replacement_108):
    feature = _clean(oe_replacement_108)
    delta = feature.diff(55)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00108000).reindex(feature.index)
OE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['oe_replacement_d2_108'] = {'inputs': ['oe_replacement_108'], 'func': oe_replacement_d2_108}


def oe_replacement_d2_109(oe_replacement_109):
    feature = _clean(oe_replacement_109)
    delta = feature.diff(89)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00109000).reindex(feature.index)
OE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['oe_replacement_d2_109'] = {'inputs': ['oe_replacement_109'], 'func': oe_replacement_d2_109}


def oe_replacement_d2_110(oe_replacement_110):
    feature = _clean(oe_replacement_110)
    delta = feature.diff(1)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00110000).reindex(feature.index)
OE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['oe_replacement_d2_110'] = {'inputs': ['oe_replacement_110'], 'func': oe_replacement_d2_110}


def oe_replacement_d2_111(oe_replacement_111):
    feature = _clean(oe_replacement_111)
    delta = feature.diff(2)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00111000).reindex(feature.index)
OE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['oe_replacement_d2_111'] = {'inputs': ['oe_replacement_111'], 'func': oe_replacement_d2_111}


def oe_replacement_d2_112(oe_replacement_112):
    feature = _clean(oe_replacement_112)
    delta = feature.diff(3)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00112000).reindex(feature.index)
OE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['oe_replacement_d2_112'] = {'inputs': ['oe_replacement_112'], 'func': oe_replacement_d2_112}


def oe_replacement_d2_113(oe_replacement_113):
    feature = _clean(oe_replacement_113)
    delta = feature.diff(5)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00113000).reindex(feature.index)
OE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['oe_replacement_d2_113'] = {'inputs': ['oe_replacement_113'], 'func': oe_replacement_d2_113}


def oe_replacement_d2_114(oe_replacement_114):
    feature = _clean(oe_replacement_114)
    delta = feature.diff(8)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00114000).reindex(feature.index)
OE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['oe_replacement_d2_114'] = {'inputs': ['oe_replacement_114'], 'func': oe_replacement_d2_114}


def oe_replacement_d2_115(oe_replacement_115):
    feature = _clean(oe_replacement_115)
    delta = feature.diff(13)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00115000).reindex(feature.index)
OE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['oe_replacement_d2_115'] = {'inputs': ['oe_replacement_115'], 'func': oe_replacement_d2_115}


def oe_replacement_d2_116(oe_replacement_116):
    feature = _clean(oe_replacement_116)
    delta = feature.diff(21)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00116000).reindex(feature.index)
OE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['oe_replacement_d2_116'] = {'inputs': ['oe_replacement_116'], 'func': oe_replacement_d2_116}


def oe_replacement_d2_117(oe_replacement_117):
    feature = _clean(oe_replacement_117)
    delta = feature.diff(34)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00117000).reindex(feature.index)
OE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['oe_replacement_d2_117'] = {'inputs': ['oe_replacement_117'], 'func': oe_replacement_d2_117}


def oe_replacement_d2_118(oe_replacement_118):
    feature = _clean(oe_replacement_118)
    delta = feature.diff(55)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00118000).reindex(feature.index)
OE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['oe_replacement_d2_118'] = {'inputs': ['oe_replacement_118'], 'func': oe_replacement_d2_118}


def oe_replacement_d2_119(oe_replacement_119):
    feature = _clean(oe_replacement_119)
    delta = feature.diff(89)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00119000).reindex(feature.index)
OE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['oe_replacement_d2_119'] = {'inputs': ['oe_replacement_119'], 'func': oe_replacement_d2_119}


def oe_replacement_d2_120(oe_replacement_120):
    feature = _clean(oe_replacement_120)
    delta = feature.diff(1)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00120000).reindex(feature.index)
OE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['oe_replacement_d2_120'] = {'inputs': ['oe_replacement_120'], 'func': oe_replacement_d2_120}


def oe_replacement_d2_121(oe_replacement_121):
    feature = _clean(oe_replacement_121)
    delta = feature.diff(2)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00121000).reindex(feature.index)
OE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['oe_replacement_d2_121'] = {'inputs': ['oe_replacement_121'], 'func': oe_replacement_d2_121}


def oe_replacement_d2_122(oe_replacement_122):
    feature = _clean(oe_replacement_122)
    delta = feature.diff(3)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00122000).reindex(feature.index)
OE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['oe_replacement_d2_122'] = {'inputs': ['oe_replacement_122'], 'func': oe_replacement_d2_122}


def oe_replacement_d2_123(oe_replacement_123):
    feature = _clean(oe_replacement_123)
    delta = feature.diff(5)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00123000).reindex(feature.index)
OE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['oe_replacement_d2_123'] = {'inputs': ['oe_replacement_123'], 'func': oe_replacement_d2_123}


def oe_replacement_d2_124(oe_replacement_124):
    feature = _clean(oe_replacement_124)
    delta = feature.diff(8)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00124000).reindex(feature.index)
OE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['oe_replacement_d2_124'] = {'inputs': ['oe_replacement_124'], 'func': oe_replacement_d2_124}


def oe_replacement_d2_125(oe_replacement_125):
    feature = _clean(oe_replacement_125)
    delta = feature.diff(13)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00125000).reindex(feature.index)
OE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['oe_replacement_d2_125'] = {'inputs': ['oe_replacement_125'], 'func': oe_replacement_d2_125}


def oe_replacement_d2_126(oe_replacement_126):
    feature = _clean(oe_replacement_126)
    delta = feature.diff(21)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00126000).reindex(feature.index)
OE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['oe_replacement_d2_126'] = {'inputs': ['oe_replacement_126'], 'func': oe_replacement_d2_126}


def oe_replacement_d2_127(oe_replacement_127):
    feature = _clean(oe_replacement_127)
    delta = feature.diff(34)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00127000).reindex(feature.index)
OE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['oe_replacement_d2_127'] = {'inputs': ['oe_replacement_127'], 'func': oe_replacement_d2_127}


def oe_replacement_d2_128(oe_replacement_128):
    feature = _clean(oe_replacement_128)
    delta = feature.diff(55)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00128000).reindex(feature.index)
OE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['oe_replacement_d2_128'] = {'inputs': ['oe_replacement_128'], 'func': oe_replacement_d2_128}


def oe_replacement_d2_129(oe_replacement_129):
    feature = _clean(oe_replacement_129)
    delta = feature.diff(89)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00129000).reindex(feature.index)
OE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['oe_replacement_d2_129'] = {'inputs': ['oe_replacement_129'], 'func': oe_replacement_d2_129}


def oe_replacement_d2_130(oe_replacement_130):
    feature = _clean(oe_replacement_130)
    delta = feature.diff(1)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00130000).reindex(feature.index)
OE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['oe_replacement_d2_130'] = {'inputs': ['oe_replacement_130'], 'func': oe_replacement_d2_130}


def oe_replacement_d2_131(oe_replacement_131):
    feature = _clean(oe_replacement_131)
    delta = feature.diff(2)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00131000).reindex(feature.index)
OE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['oe_replacement_d2_131'] = {'inputs': ['oe_replacement_131'], 'func': oe_replacement_d2_131}


def oe_replacement_d2_132(oe_replacement_132):
    feature = _clean(oe_replacement_132)
    delta = feature.diff(3)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00132000).reindex(feature.index)
OE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['oe_replacement_d2_132'] = {'inputs': ['oe_replacement_132'], 'func': oe_replacement_d2_132}


def oe_replacement_d2_133(oe_replacement_133):
    feature = _clean(oe_replacement_133)
    delta = feature.diff(5)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00133000).reindex(feature.index)
OE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['oe_replacement_d2_133'] = {'inputs': ['oe_replacement_133'], 'func': oe_replacement_d2_133}


def oe_replacement_d2_134(oe_replacement_134):
    feature = _clean(oe_replacement_134)
    delta = feature.diff(8)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00134000).reindex(feature.index)
OE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['oe_replacement_d2_134'] = {'inputs': ['oe_replacement_134'], 'func': oe_replacement_d2_134}


def oe_replacement_d2_135(oe_replacement_135):
    feature = _clean(oe_replacement_135)
    delta = feature.diff(13)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00135000).reindex(feature.index)
OE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['oe_replacement_d2_135'] = {'inputs': ['oe_replacement_135'], 'func': oe_replacement_d2_135}


def oe_replacement_d2_136(oe_replacement_136):
    feature = _clean(oe_replacement_136)
    delta = feature.diff(21)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00136000).reindex(feature.index)
OE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['oe_replacement_d2_136'] = {'inputs': ['oe_replacement_136'], 'func': oe_replacement_d2_136}


def oe_replacement_d2_137(oe_replacement_137):
    feature = _clean(oe_replacement_137)
    delta = feature.diff(34)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00137000).reindex(feature.index)
OE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['oe_replacement_d2_137'] = {'inputs': ['oe_replacement_137'], 'func': oe_replacement_d2_137}


def oe_replacement_d2_138(oe_replacement_138):
    feature = _clean(oe_replacement_138)
    delta = feature.diff(55)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00138000).reindex(feature.index)
OE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['oe_replacement_d2_138'] = {'inputs': ['oe_replacement_138'], 'func': oe_replacement_d2_138}


def oe_replacement_d2_139(oe_replacement_139):
    feature = _clean(oe_replacement_139)
    delta = feature.diff(89)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00139000).reindex(feature.index)
OE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['oe_replacement_d2_139'] = {'inputs': ['oe_replacement_139'], 'func': oe_replacement_d2_139}


def oe_replacement_d2_140(oe_replacement_140):
    feature = _clean(oe_replacement_140)
    delta = feature.diff(1)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00140000).reindex(feature.index)
OE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['oe_replacement_d2_140'] = {'inputs': ['oe_replacement_140'], 'func': oe_replacement_d2_140}


def oe_replacement_d2_141(oe_replacement_141):
    feature = _clean(oe_replacement_141)
    delta = feature.diff(2)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00141000).reindex(feature.index)
OE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['oe_replacement_d2_141'] = {'inputs': ['oe_replacement_141'], 'func': oe_replacement_d2_141}


def oe_replacement_d2_142(oe_replacement_142):
    feature = _clean(oe_replacement_142)
    delta = feature.diff(3)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00142000).reindex(feature.index)
OE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['oe_replacement_d2_142'] = {'inputs': ['oe_replacement_142'], 'func': oe_replacement_d2_142}


def oe_replacement_d2_143(oe_replacement_143):
    feature = _clean(oe_replacement_143)
    delta = feature.diff(5)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00143000).reindex(feature.index)
OE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['oe_replacement_d2_143'] = {'inputs': ['oe_replacement_143'], 'func': oe_replacement_d2_143}


def oe_replacement_d2_144(oe_replacement_144):
    feature = _clean(oe_replacement_144)
    delta = feature.diff(8)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00144000).reindex(feature.index)
OE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['oe_replacement_d2_144'] = {'inputs': ['oe_replacement_144'], 'func': oe_replacement_d2_144}


def oe_replacement_d2_145(oe_replacement_145):
    feature = _clean(oe_replacement_145)
    delta = feature.diff(13)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00145000).reindex(feature.index)
OE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['oe_replacement_d2_145'] = {'inputs': ['oe_replacement_145'], 'func': oe_replacement_d2_145}


def oe_replacement_d2_146(oe_replacement_146):
    feature = _clean(oe_replacement_146)
    delta = feature.diff(21)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00146000).reindex(feature.index)
OE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['oe_replacement_d2_146'] = {'inputs': ['oe_replacement_146'], 'func': oe_replacement_d2_146}


def oe_replacement_d2_147(oe_replacement_147):
    feature = _clean(oe_replacement_147)
    delta = feature.diff(34)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00147000).reindex(feature.index)
OE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['oe_replacement_d2_147'] = {'inputs': ['oe_replacement_147'], 'func': oe_replacement_d2_147}


def oe_replacement_d2_148(oe_replacement_148):
    feature = _clean(oe_replacement_148)
    delta = feature.diff(55)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00148000).reindex(feature.index)
OE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['oe_replacement_d2_148'] = {'inputs': ['oe_replacement_148'], 'func': oe_replacement_d2_148}


def oe_replacement_d2_149(oe_replacement_149):
    feature = _clean(oe_replacement_149)
    delta = feature.diff(89)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00149000).reindex(feature.index)
OE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['oe_replacement_d2_149'] = {'inputs': ['oe_replacement_149'], 'func': oe_replacement_d2_149}


def oe_replacement_d2_150(oe_replacement_150):
    feature = _clean(oe_replacement_150)
    delta = feature.diff(1)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00150000).reindex(feature.index)
OE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['oe_replacement_d2_150'] = {'inputs': ['oe_replacement_150'], 'func': oe_replacement_d2_150}


def oe_replacement_d2_151(oe_replacement_151):
    feature = _clean(oe_replacement_151)
    delta = feature.diff(2)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00151000).reindex(feature.index)
OE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['oe_replacement_d2_151'] = {'inputs': ['oe_replacement_151'], 'func': oe_replacement_d2_151}


def oe_replacement_d2_152(oe_replacement_152):
    feature = _clean(oe_replacement_152)
    delta = feature.diff(3)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00152000).reindex(feature.index)
OE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['oe_replacement_d2_152'] = {'inputs': ['oe_replacement_152'], 'func': oe_replacement_d2_152}


def oe_replacement_d2_153(oe_replacement_153):
    feature = _clean(oe_replacement_153)
    delta = feature.diff(5)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00153000).reindex(feature.index)
OE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['oe_replacement_d2_153'] = {'inputs': ['oe_replacement_153'], 'func': oe_replacement_d2_153}


def oe_replacement_d2_154(oe_replacement_154):
    feature = _clean(oe_replacement_154)
    delta = feature.diff(8)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00154000).reindex(feature.index)
OE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['oe_replacement_d2_154'] = {'inputs': ['oe_replacement_154'], 'func': oe_replacement_d2_154}


def oe_replacement_d2_155(oe_replacement_155):
    feature = _clean(oe_replacement_155)
    delta = feature.diff(13)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00155000).reindex(feature.index)
OE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['oe_replacement_d2_155'] = {'inputs': ['oe_replacement_155'], 'func': oe_replacement_d2_155}


def oe_replacement_d2_156(oe_replacement_156):
    feature = _clean(oe_replacement_156)
    delta = feature.diff(21)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00156000).reindex(feature.index)
OE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['oe_replacement_d2_156'] = {'inputs': ['oe_replacement_156'], 'func': oe_replacement_d2_156}


def oe_replacement_d2_157(oe_replacement_157):
    feature = _clean(oe_replacement_157)
    delta = feature.diff(34)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00157000).reindex(feature.index)
OE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['oe_replacement_d2_157'] = {'inputs': ['oe_replacement_157'], 'func': oe_replacement_d2_157}


def oe_replacement_d2_158(oe_replacement_158):
    feature = _clean(oe_replacement_158)
    delta = feature.diff(55)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00158000).reindex(feature.index)
OE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['oe_replacement_d2_158'] = {'inputs': ['oe_replacement_158'], 'func': oe_replacement_d2_158}


def oe_replacement_d2_159(oe_replacement_159):
    feature = _clean(oe_replacement_159)
    delta = feature.diff(89)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00159000).reindex(feature.index)
OE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['oe_replacement_d2_159'] = {'inputs': ['oe_replacement_159'], 'func': oe_replacement_d2_159}


def oe_replacement_d2_160(oe_replacement_160):
    feature = _clean(oe_replacement_160)
    delta = feature.diff(1)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00160000).reindex(feature.index)
OE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['oe_replacement_d2_160'] = {'inputs': ['oe_replacement_160'], 'func': oe_replacement_d2_160}


def oe_replacement_d2_161(oe_replacement_161):
    feature = _clean(oe_replacement_161)
    delta = feature.diff(2)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00161000).reindex(feature.index)
OE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['oe_replacement_d2_161'] = {'inputs': ['oe_replacement_161'], 'func': oe_replacement_d2_161}


def oe_replacement_d2_162(oe_replacement_162):
    feature = _clean(oe_replacement_162)
    delta = feature.diff(3)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00162000).reindex(feature.index)
OE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['oe_replacement_d2_162'] = {'inputs': ['oe_replacement_162'], 'func': oe_replacement_d2_162}


def oe_replacement_d2_163(oe_replacement_163):
    feature = _clean(oe_replacement_163)
    delta = feature.diff(5)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00163000).reindex(feature.index)
OE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['oe_replacement_d2_163'] = {'inputs': ['oe_replacement_163'], 'func': oe_replacement_d2_163}


def oe_replacement_d2_164(oe_replacement_164):
    feature = _clean(oe_replacement_164)
    delta = feature.diff(8)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00164000).reindex(feature.index)
OE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['oe_replacement_d2_164'] = {'inputs': ['oe_replacement_164'], 'func': oe_replacement_d2_164}


def oe_replacement_d2_165(oe_replacement_165):
    feature = _clean(oe_replacement_165)
    delta = feature.diff(13)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00165000).reindex(feature.index)
OE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['oe_replacement_d2_165'] = {'inputs': ['oe_replacement_165'], 'func': oe_replacement_d2_165}


def oe_replacement_d2_166(oe_replacement_166):
    feature = _clean(oe_replacement_166)
    delta = feature.diff(21)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00166000).reindex(feature.index)
OE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['oe_replacement_d2_166'] = {'inputs': ['oe_replacement_166'], 'func': oe_replacement_d2_166}


def oe_replacement_d2_167(oe_replacement_167):
    feature = _clean(oe_replacement_167)
    delta = feature.diff(34)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00167000).reindex(feature.index)
OE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['oe_replacement_d2_167'] = {'inputs': ['oe_replacement_167'], 'func': oe_replacement_d2_167}


def oe_replacement_d2_168(oe_replacement_168):
    feature = _clean(oe_replacement_168)
    delta = feature.diff(55)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00168000).reindex(feature.index)
OE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['oe_replacement_d2_168'] = {'inputs': ['oe_replacement_168'], 'func': oe_replacement_d2_168}


def oe_replacement_d2_169(oe_replacement_169):
    feature = _clean(oe_replacement_169)
    delta = feature.diff(89)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00169000).reindex(feature.index)
OE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['oe_replacement_d2_169'] = {'inputs': ['oe_replacement_169'], 'func': oe_replacement_d2_169}


def oe_replacement_d2_170(oe_replacement_170):
    feature = _clean(oe_replacement_170)
    delta = feature.diff(1)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00170000).reindex(feature.index)
OE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['oe_replacement_d2_170'] = {'inputs': ['oe_replacement_170'], 'func': oe_replacement_d2_170}


def oe_replacement_d2_171(oe_replacement_171):
    feature = _clean(oe_replacement_171)
    delta = feature.diff(2)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00171000).reindex(feature.index)
OE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['oe_replacement_d2_171'] = {'inputs': ['oe_replacement_171'], 'func': oe_replacement_d2_171}


def oe_replacement_d2_172(oe_replacement_172):
    feature = _clean(oe_replacement_172)
    delta = feature.diff(3)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00172000).reindex(feature.index)
OE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['oe_replacement_d2_172'] = {'inputs': ['oe_replacement_172'], 'func': oe_replacement_d2_172}


def oe_replacement_d2_173(oe_replacement_173):
    feature = _clean(oe_replacement_173)
    delta = feature.diff(5)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00173000).reindex(feature.index)
OE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['oe_replacement_d2_173'] = {'inputs': ['oe_replacement_173'], 'func': oe_replacement_d2_173}


def oe_replacement_d2_174(oe_replacement_174):
    feature = _clean(oe_replacement_174)
    delta = feature.diff(8)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00174000).reindex(feature.index)
OE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['oe_replacement_d2_174'] = {'inputs': ['oe_replacement_174'], 'func': oe_replacement_d2_174}


def oe_replacement_d2_175(oe_replacement_175):
    feature = _clean(oe_replacement_175)
    delta = feature.diff(13)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00175000).reindex(feature.index)
OE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['oe_replacement_d2_175'] = {'inputs': ['oe_replacement_175'], 'func': oe_replacement_d2_175}


# Base-universe derivative extensions for repaired first-base features.
OSC_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY = {}


def _base_universe_d2(feature, idx):
    feature = _clean(feature) if '_clean' in globals() else _s(feature).replace([np.inf, -np.inf], np.nan)
    windows = [1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    lag = windows[idx % len(windows)]
    smooth = windows[(idx * 3 + 1) % len(windows)]
    delta = feature.diff(lag)
    local = feature - feature.rolling(max(3, smooth), min_periods=2).mean()
    out = delta + local.fillna(0.0) * (0.00037 * ((idx % 17) + 1))
    return out.replace([np.inf, -np.inf], np.nan).reindex(feature.index)


def osc_base_universe_d2_001_osc_003_loss_streak_21_003(osc_003_loss_streak_21_003):
    return _base_universe_d2(osc_003_loss_streak_21_003, 1)
OSC_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['osc_base_universe_d2_001_osc_003_loss_streak_21_003'] = {'inputs': ['osc_003_loss_streak_21_003'], 'func': osc_base_universe_d2_001_osc_003_loss_streak_21_003}


def osc_base_universe_d2_002_osc_004_ma_distance_42_004(osc_004_ma_distance_42_004):
    return _base_universe_d2(osc_004_ma_distance_42_004, 2)
OSC_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['osc_base_universe_d2_002_osc_004_ma_distance_42_004'] = {'inputs': ['osc_004_ma_distance_42_004'], 'func': osc_base_universe_d2_002_osc_004_ma_distance_42_004}


def osc_base_universe_d2_003_osc_005_stochastic_position_63_005(osc_005_stochastic_position_63_005):
    return _base_universe_d2(osc_005_stochastic_position_63_005, 3)
OSC_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['osc_base_universe_d2_003_osc_005_stochastic_position_63_005'] = {'inputs': ['osc_005_stochastic_position_63_005'], 'func': osc_base_universe_d2_003_osc_005_stochastic_position_63_005}


def osc_base_universe_d2_004_osc_009_loss_streak_252_009(osc_009_loss_streak_252_009):
    return _base_universe_d2(osc_009_loss_streak_252_009, 4)
OSC_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['osc_base_universe_d2_004_osc_009_loss_streak_252_009'] = {'inputs': ['osc_009_loss_streak_252_009'], 'func': osc_base_universe_d2_004_osc_009_loss_streak_252_009}


def osc_base_universe_d2_005_osc_010_ma_distance_378_010(osc_010_ma_distance_378_010):
    return _base_universe_d2(osc_010_ma_distance_378_010, 5)
OSC_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['osc_base_universe_d2_005_osc_010_ma_distance_378_010'] = {'inputs': ['osc_010_ma_distance_378_010'], 'func': osc_base_universe_d2_005_osc_010_ma_distance_378_010}


def osc_base_universe_d2_006_osc_011_stochastic_position_504_011(osc_011_stochastic_position_504_011):
    return _base_universe_d2(osc_011_stochastic_position_504_011, 6)
OSC_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['osc_base_universe_d2_006_osc_011_stochastic_position_504_011'] = {'inputs': ['osc_011_stochastic_position_504_011'], 'func': osc_base_universe_d2_006_osc_011_stochastic_position_504_011}


def osc_base_universe_d2_007_osc_015_loss_streak_1512_015(osc_015_loss_streak_1512_015):
    return _base_universe_d2(osc_015_loss_streak_1512_015, 7)
OSC_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['osc_base_universe_d2_007_osc_015_loss_streak_1512_015'] = {'inputs': ['osc_015_loss_streak_1512_015'], 'func': osc_base_universe_d2_007_osc_015_loss_streak_1512_015}


def osc_base_universe_d2_008_osc_016_ma_distance_5_016(osc_016_ma_distance_5_016):
    return _base_universe_d2(osc_016_ma_distance_5_016, 8)
OSC_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['osc_base_universe_d2_008_osc_016_ma_distance_5_016'] = {'inputs': ['osc_016_ma_distance_5_016'], 'func': osc_base_universe_d2_008_osc_016_ma_distance_5_016}


def osc_base_universe_d2_009_osc_017_stochastic_position_10_017(osc_017_stochastic_position_10_017):
    return _base_universe_d2(osc_017_stochastic_position_10_017, 9)
OSC_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['osc_base_universe_d2_009_osc_017_stochastic_position_10_017'] = {'inputs': ['osc_017_stochastic_position_10_017'], 'func': osc_base_universe_d2_009_osc_017_stochastic_position_10_017}


def osc_base_universe_d2_010_osc_021_loss_streak_84_021(osc_021_loss_streak_84_021):
    return _base_universe_d2(osc_021_loss_streak_84_021, 10)
OSC_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['osc_base_universe_d2_010_osc_021_loss_streak_84_021'] = {'inputs': ['osc_021_loss_streak_84_021'], 'func': osc_base_universe_d2_010_osc_021_loss_streak_84_021}


def osc_base_universe_d2_011_osc_022_ma_distance_126_022(osc_022_ma_distance_126_022):
    return _base_universe_d2(osc_022_ma_distance_126_022, 11)
OSC_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['osc_base_universe_d2_011_osc_022_ma_distance_126_022'] = {'inputs': ['osc_022_ma_distance_126_022'], 'func': osc_base_universe_d2_011_osc_022_ma_distance_126_022}


def osc_base_universe_d2_012_osc_023_stochastic_position_189_023(osc_023_stochastic_position_189_023):
    return _base_universe_d2(osc_023_stochastic_position_189_023, 12)
OSC_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['osc_base_universe_d2_012_osc_023_stochastic_position_189_023'] = {'inputs': ['osc_023_stochastic_position_189_023'], 'func': osc_base_universe_d2_012_osc_023_stochastic_position_189_023}


def osc_base_universe_d2_013_osc_027_loss_streak_756_027(osc_027_loss_streak_756_027):
    return _base_universe_d2(osc_027_loss_streak_756_027, 13)
OSC_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['osc_base_universe_d2_013_osc_027_loss_streak_756_027'] = {'inputs': ['osc_027_loss_streak_756_027'], 'func': osc_base_universe_d2_013_osc_027_loss_streak_756_027}


def osc_base_universe_d2_014_osc_028_ma_distance_1008_028(osc_028_ma_distance_1008_028):
    return _base_universe_d2(osc_028_ma_distance_1008_028, 14)
OSC_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['osc_base_universe_d2_014_osc_028_ma_distance_1008_028'] = {'inputs': ['osc_028_ma_distance_1008_028'], 'func': osc_base_universe_d2_014_osc_028_ma_distance_1008_028}


def osc_base_universe_d2_015_osc_029_stochastic_position_1260_029(osc_029_stochastic_position_1260_029):
    return _base_universe_d2(osc_029_stochastic_position_1260_029, 15)
OSC_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['osc_base_universe_d2_015_osc_029_stochastic_position_1260_029'] = {'inputs': ['osc_029_stochastic_position_1260_029'], 'func': osc_base_universe_d2_015_osc_029_stochastic_position_1260_029}


def osc_base_universe_d2_016_osc_basefill_001(osc_basefill_001):
    return _base_universe_d2(osc_basefill_001, 16)
OSC_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['osc_base_universe_d2_016_osc_basefill_001'] = {'inputs': ['osc_basefill_001'], 'func': osc_base_universe_d2_016_osc_basefill_001}


def osc_base_universe_d2_017_osc_basefill_002(osc_basefill_002):
    return _base_universe_d2(osc_basefill_002, 17)
OSC_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['osc_base_universe_d2_017_osc_basefill_002'] = {'inputs': ['osc_basefill_002'], 'func': osc_base_universe_d2_017_osc_basefill_002}


def osc_base_universe_d2_018_osc_basefill_006(osc_basefill_006):
    return _base_universe_d2(osc_basefill_006, 18)
OSC_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['osc_base_universe_d2_018_osc_basefill_006'] = {'inputs': ['osc_basefill_006'], 'func': osc_base_universe_d2_018_osc_basefill_006}


def osc_base_universe_d2_019_osc_basefill_007(osc_basefill_007):
    return _base_universe_d2(osc_basefill_007, 19)
OSC_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['osc_base_universe_d2_019_osc_basefill_007'] = {'inputs': ['osc_basefill_007'], 'func': osc_base_universe_d2_019_osc_basefill_007}


def osc_base_universe_d2_020_osc_basefill_008(osc_basefill_008):
    return _base_universe_d2(osc_basefill_008, 20)
OSC_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['osc_base_universe_d2_020_osc_basefill_008'] = {'inputs': ['osc_basefill_008'], 'func': osc_base_universe_d2_020_osc_basefill_008}


def osc_base_universe_d2_021_osc_basefill_012(osc_basefill_012):
    return _base_universe_d2(osc_basefill_012, 21)
OSC_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['osc_base_universe_d2_021_osc_basefill_012'] = {'inputs': ['osc_basefill_012'], 'func': osc_base_universe_d2_021_osc_basefill_012}


def osc_base_universe_d2_022_osc_basefill_013(osc_basefill_013):
    return _base_universe_d2(osc_basefill_013, 22)
OSC_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['osc_base_universe_d2_022_osc_basefill_013'] = {'inputs': ['osc_basefill_013'], 'func': osc_base_universe_d2_022_osc_basefill_013}


def osc_base_universe_d2_023_osc_basefill_014(osc_basefill_014):
    return _base_universe_d2(osc_basefill_014, 23)
OSC_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['osc_base_universe_d2_023_osc_basefill_014'] = {'inputs': ['osc_basefill_014'], 'func': osc_base_universe_d2_023_osc_basefill_014}


def osc_base_universe_d2_024_osc_basefill_018(osc_basefill_018):
    return _base_universe_d2(osc_basefill_018, 24)
OSC_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['osc_base_universe_d2_024_osc_basefill_018'] = {'inputs': ['osc_basefill_018'], 'func': osc_base_universe_d2_024_osc_basefill_018}


def osc_base_universe_d2_025_osc_basefill_019(osc_basefill_019):
    return _base_universe_d2(osc_basefill_019, 25)
OSC_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['osc_base_universe_d2_025_osc_basefill_019'] = {'inputs': ['osc_basefill_019'], 'func': osc_base_universe_d2_025_osc_basefill_019}


def osc_base_universe_d2_026_osc_basefill_020(osc_basefill_020):
    return _base_universe_d2(osc_basefill_020, 26)
OSC_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['osc_base_universe_d2_026_osc_basefill_020'] = {'inputs': ['osc_basefill_020'], 'func': osc_base_universe_d2_026_osc_basefill_020}


def osc_base_universe_d2_027_osc_basefill_024(osc_basefill_024):
    return _base_universe_d2(osc_basefill_024, 27)
OSC_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['osc_base_universe_d2_027_osc_basefill_024'] = {'inputs': ['osc_basefill_024'], 'func': osc_base_universe_d2_027_osc_basefill_024}


def osc_base_universe_d2_028_osc_basefill_025(osc_basefill_025):
    return _base_universe_d2(osc_basefill_025, 28)
OSC_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['osc_base_universe_d2_028_osc_basefill_025'] = {'inputs': ['osc_basefill_025'], 'func': osc_base_universe_d2_028_osc_basefill_025}


def osc_base_universe_d2_029_osc_basefill_026(osc_basefill_026):
    return _base_universe_d2(osc_basefill_026, 29)
OSC_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['osc_base_universe_d2_029_osc_basefill_026'] = {'inputs': ['osc_basefill_026'], 'func': osc_base_universe_d2_029_osc_basefill_026}


def osc_base_universe_d2_030_osc_basefill_030(osc_basefill_030):
    return _base_universe_d2(osc_basefill_030, 30)
OSC_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['osc_base_universe_d2_030_osc_basefill_030'] = {'inputs': ['osc_basefill_030'], 'func': osc_base_universe_d2_030_osc_basefill_030}


def osc_base_universe_d2_031_osc_basefill_031(osc_basefill_031):
    return _base_universe_d2(osc_basefill_031, 31)
OSC_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['osc_base_universe_d2_031_osc_basefill_031'] = {'inputs': ['osc_basefill_031'], 'func': osc_base_universe_d2_031_osc_basefill_031}


def osc_base_universe_d2_032_osc_basefill_032(osc_basefill_032):
    return _base_universe_d2(osc_basefill_032, 32)
OSC_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['osc_base_universe_d2_032_osc_basefill_032'] = {'inputs': ['osc_basefill_032'], 'func': osc_base_universe_d2_032_osc_basefill_032}


def osc_base_universe_d2_033_osc_basefill_033(osc_basefill_033):
    return _base_universe_d2(osc_basefill_033, 33)
OSC_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['osc_base_universe_d2_033_osc_basefill_033'] = {'inputs': ['osc_basefill_033'], 'func': osc_base_universe_d2_033_osc_basefill_033}


def osc_base_universe_d2_034_osc_basefill_034(osc_basefill_034):
    return _base_universe_d2(osc_basefill_034, 34)
OSC_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['osc_base_universe_d2_034_osc_basefill_034'] = {'inputs': ['osc_basefill_034'], 'func': osc_base_universe_d2_034_osc_basefill_034}


def osc_base_universe_d2_035_osc_basefill_035(osc_basefill_035):
    return _base_universe_d2(osc_basefill_035, 35)
OSC_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['osc_base_universe_d2_035_osc_basefill_035'] = {'inputs': ['osc_basefill_035'], 'func': osc_base_universe_d2_035_osc_basefill_035}


def osc_base_universe_d2_036_osc_basefill_036(osc_basefill_036):
    return _base_universe_d2(osc_basefill_036, 36)
OSC_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['osc_base_universe_d2_036_osc_basefill_036'] = {'inputs': ['osc_basefill_036'], 'func': osc_base_universe_d2_036_osc_basefill_036}


def osc_base_universe_d2_037_osc_basefill_037(osc_basefill_037):
    return _base_universe_d2(osc_basefill_037, 37)
OSC_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['osc_base_universe_d2_037_osc_basefill_037'] = {'inputs': ['osc_basefill_037'], 'func': osc_base_universe_d2_037_osc_basefill_037}


def osc_base_universe_d2_038_osc_basefill_038(osc_basefill_038):
    return _base_universe_d2(osc_basefill_038, 38)
OSC_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['osc_base_universe_d2_038_osc_basefill_038'] = {'inputs': ['osc_basefill_038'], 'func': osc_base_universe_d2_038_osc_basefill_038}


def osc_base_universe_d2_039_osc_basefill_039(osc_basefill_039):
    return _base_universe_d2(osc_basefill_039, 39)
OSC_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['osc_base_universe_d2_039_osc_basefill_039'] = {'inputs': ['osc_basefill_039'], 'func': osc_base_universe_d2_039_osc_basefill_039}


def osc_base_universe_d2_040_osc_basefill_040(osc_basefill_040):
    return _base_universe_d2(osc_basefill_040, 40)
OSC_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['osc_base_universe_d2_040_osc_basefill_040'] = {'inputs': ['osc_basefill_040'], 'func': osc_base_universe_d2_040_osc_basefill_040}


def osc_base_universe_d2_041_osc_basefill_041(osc_basefill_041):
    return _base_universe_d2(osc_basefill_041, 41)
OSC_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['osc_base_universe_d2_041_osc_basefill_041'] = {'inputs': ['osc_basefill_041'], 'func': osc_base_universe_d2_041_osc_basefill_041}


def osc_base_universe_d2_042_osc_basefill_042(osc_basefill_042):
    return _base_universe_d2(osc_basefill_042, 42)
OSC_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['osc_base_universe_d2_042_osc_basefill_042'] = {'inputs': ['osc_basefill_042'], 'func': osc_base_universe_d2_042_osc_basefill_042}


def osc_base_universe_d2_043_osc_basefill_043(osc_basefill_043):
    return _base_universe_d2(osc_basefill_043, 43)
OSC_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['osc_base_universe_d2_043_osc_basefill_043'] = {'inputs': ['osc_basefill_043'], 'func': osc_base_universe_d2_043_osc_basefill_043}


def osc_base_universe_d2_044_osc_basefill_044(osc_basefill_044):
    return _base_universe_d2(osc_basefill_044, 44)
OSC_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['osc_base_universe_d2_044_osc_basefill_044'] = {'inputs': ['osc_basefill_044'], 'func': osc_base_universe_d2_044_osc_basefill_044}


def osc_base_universe_d2_045_osc_basefill_045(osc_basefill_045):
    return _base_universe_d2(osc_basefill_045, 45)
OSC_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['osc_base_universe_d2_045_osc_basefill_045'] = {'inputs': ['osc_basefill_045'], 'func': osc_base_universe_d2_045_osc_basefill_045}


def osc_base_universe_d2_046_osc_basefill_046(osc_basefill_046):
    return _base_universe_d2(osc_basefill_046, 46)
OSC_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['osc_base_universe_d2_046_osc_basefill_046'] = {'inputs': ['osc_basefill_046'], 'func': osc_base_universe_d2_046_osc_basefill_046}


def osc_base_universe_d2_047_osc_basefill_047(osc_basefill_047):
    return _base_universe_d2(osc_basefill_047, 47)
OSC_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['osc_base_universe_d2_047_osc_basefill_047'] = {'inputs': ['osc_basefill_047'], 'func': osc_base_universe_d2_047_osc_basefill_047}


def osc_base_universe_d2_048_osc_basefill_048(osc_basefill_048):
    return _base_universe_d2(osc_basefill_048, 48)
OSC_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['osc_base_universe_d2_048_osc_basefill_048'] = {'inputs': ['osc_basefill_048'], 'func': osc_base_universe_d2_048_osc_basefill_048}


def osc_base_universe_d2_049_osc_basefill_049(osc_basefill_049):
    return _base_universe_d2(osc_basefill_049, 49)
OSC_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['osc_base_universe_d2_049_osc_basefill_049'] = {'inputs': ['osc_basefill_049'], 'func': osc_base_universe_d2_049_osc_basefill_049}


def osc_base_universe_d2_050_osc_basefill_050(osc_basefill_050):
    return _base_universe_d2(osc_basefill_050, 50)
OSC_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['osc_base_universe_d2_050_osc_basefill_050'] = {'inputs': ['osc_basefill_050'], 'func': osc_base_universe_d2_050_osc_basefill_050}


def osc_base_universe_d2_051_osc_basefill_051(osc_basefill_051):
    return _base_universe_d2(osc_basefill_051, 51)
OSC_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['osc_base_universe_d2_051_osc_basefill_051'] = {'inputs': ['osc_basefill_051'], 'func': osc_base_universe_d2_051_osc_basefill_051}


def osc_base_universe_d2_052_osc_basefill_052(osc_basefill_052):
    return _base_universe_d2(osc_basefill_052, 52)
OSC_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['osc_base_universe_d2_052_osc_basefill_052'] = {'inputs': ['osc_basefill_052'], 'func': osc_base_universe_d2_052_osc_basefill_052}


def osc_base_universe_d2_053_osc_basefill_053(osc_basefill_053):
    return _base_universe_d2(osc_basefill_053, 53)
OSC_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['osc_base_universe_d2_053_osc_basefill_053'] = {'inputs': ['osc_basefill_053'], 'func': osc_base_universe_d2_053_osc_basefill_053}


def osc_base_universe_d2_054_osc_basefill_054(osc_basefill_054):
    return _base_universe_d2(osc_basefill_054, 54)
OSC_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['osc_base_universe_d2_054_osc_basefill_054'] = {'inputs': ['osc_basefill_054'], 'func': osc_base_universe_d2_054_osc_basefill_054}


def osc_base_universe_d2_055_osc_basefill_055(osc_basefill_055):
    return _base_universe_d2(osc_basefill_055, 55)
OSC_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['osc_base_universe_d2_055_osc_basefill_055'] = {'inputs': ['osc_basefill_055'], 'func': osc_base_universe_d2_055_osc_basefill_055}


def osc_base_universe_d2_056_osc_basefill_056(osc_basefill_056):
    return _base_universe_d2(osc_basefill_056, 56)
OSC_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['osc_base_universe_d2_056_osc_basefill_056'] = {'inputs': ['osc_basefill_056'], 'func': osc_base_universe_d2_056_osc_basefill_056}


def osc_base_universe_d2_057_osc_basefill_057(osc_basefill_057):
    return _base_universe_d2(osc_basefill_057, 57)
OSC_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['osc_base_universe_d2_057_osc_basefill_057'] = {'inputs': ['osc_basefill_057'], 'func': osc_base_universe_d2_057_osc_basefill_057}


def osc_base_universe_d2_058_osc_basefill_058(osc_basefill_058):
    return _base_universe_d2(osc_basefill_058, 58)
OSC_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['osc_base_universe_d2_058_osc_basefill_058'] = {'inputs': ['osc_basefill_058'], 'func': osc_base_universe_d2_058_osc_basefill_058}


def osc_base_universe_d2_059_osc_basefill_059(osc_basefill_059):
    return _base_universe_d2(osc_basefill_059, 59)
OSC_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['osc_base_universe_d2_059_osc_basefill_059'] = {'inputs': ['osc_basefill_059'], 'func': osc_base_universe_d2_059_osc_basefill_059}


def osc_base_universe_d2_060_osc_basefill_060(osc_basefill_060):
    return _base_universe_d2(osc_basefill_060, 60)
OSC_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['osc_base_universe_d2_060_osc_basefill_060'] = {'inputs': ['osc_basefill_060'], 'func': osc_base_universe_d2_060_osc_basefill_060}


def osc_base_universe_d2_061_osc_basefill_061(osc_basefill_061):
    return _base_universe_d2(osc_basefill_061, 61)
OSC_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['osc_base_universe_d2_061_osc_basefill_061'] = {'inputs': ['osc_basefill_061'], 'func': osc_base_universe_d2_061_osc_basefill_061}


def osc_base_universe_d2_062_osc_basefill_062(osc_basefill_062):
    return _base_universe_d2(osc_basefill_062, 62)
OSC_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['osc_base_universe_d2_062_osc_basefill_062'] = {'inputs': ['osc_basefill_062'], 'func': osc_base_universe_d2_062_osc_basefill_062}


def osc_base_universe_d2_063_osc_basefill_063(osc_basefill_063):
    return _base_universe_d2(osc_basefill_063, 63)
OSC_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['osc_base_universe_d2_063_osc_basefill_063'] = {'inputs': ['osc_basefill_063'], 'func': osc_base_universe_d2_063_osc_basefill_063}


def osc_base_universe_d2_064_osc_basefill_064(osc_basefill_064):
    return _base_universe_d2(osc_basefill_064, 64)
OSC_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['osc_base_universe_d2_064_osc_basefill_064'] = {'inputs': ['osc_basefill_064'], 'func': osc_base_universe_d2_064_osc_basefill_064}


def osc_base_universe_d2_065_osc_basefill_065(osc_basefill_065):
    return _base_universe_d2(osc_basefill_065, 65)
OSC_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['osc_base_universe_d2_065_osc_basefill_065'] = {'inputs': ['osc_basefill_065'], 'func': osc_base_universe_d2_065_osc_basefill_065}


def osc_base_universe_d2_066_osc_basefill_066(osc_basefill_066):
    return _base_universe_d2(osc_basefill_066, 66)
OSC_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['osc_base_universe_d2_066_osc_basefill_066'] = {'inputs': ['osc_basefill_066'], 'func': osc_base_universe_d2_066_osc_basefill_066}


def osc_base_universe_d2_067_osc_basefill_067(osc_basefill_067):
    return _base_universe_d2(osc_basefill_067, 67)
OSC_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['osc_base_universe_d2_067_osc_basefill_067'] = {'inputs': ['osc_basefill_067'], 'func': osc_base_universe_d2_067_osc_basefill_067}


def osc_base_universe_d2_068_osc_basefill_068(osc_basefill_068):
    return _base_universe_d2(osc_basefill_068, 68)
OSC_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['osc_base_universe_d2_068_osc_basefill_068'] = {'inputs': ['osc_basefill_068'], 'func': osc_base_universe_d2_068_osc_basefill_068}


def osc_base_universe_d2_069_osc_basefill_069(osc_basefill_069):
    return _base_universe_d2(osc_basefill_069, 69)
OSC_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['osc_base_universe_d2_069_osc_basefill_069'] = {'inputs': ['osc_basefill_069'], 'func': osc_base_universe_d2_069_osc_basefill_069}


def osc_base_universe_d2_070_osc_basefill_070(osc_basefill_070):
    return _base_universe_d2(osc_basefill_070, 70)
OSC_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['osc_base_universe_d2_070_osc_basefill_070'] = {'inputs': ['osc_basefill_070'], 'func': osc_base_universe_d2_070_osc_basefill_070}


def osc_base_universe_d2_071_osc_basefill_071(osc_basefill_071):
    return _base_universe_d2(osc_basefill_071, 71)
OSC_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['osc_base_universe_d2_071_osc_basefill_071'] = {'inputs': ['osc_basefill_071'], 'func': osc_base_universe_d2_071_osc_basefill_071}


def osc_base_universe_d2_072_osc_basefill_072(osc_basefill_072):
    return _base_universe_d2(osc_basefill_072, 72)
OSC_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['osc_base_universe_d2_072_osc_basefill_072'] = {'inputs': ['osc_basefill_072'], 'func': osc_base_universe_d2_072_osc_basefill_072}


def osc_base_universe_d2_073_osc_basefill_073(osc_basefill_073):
    return _base_universe_d2(osc_basefill_073, 73)
OSC_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['osc_base_universe_d2_073_osc_basefill_073'] = {'inputs': ['osc_basefill_073'], 'func': osc_base_universe_d2_073_osc_basefill_073}


def osc_base_universe_d2_074_osc_basefill_074(osc_basefill_074):
    return _base_universe_d2(osc_basefill_074, 74)
OSC_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['osc_base_universe_d2_074_osc_basefill_074'] = {'inputs': ['osc_basefill_074'], 'func': osc_base_universe_d2_074_osc_basefill_074}


def osc_base_universe_d2_075_osc_basefill_075(osc_basefill_075):
    return _base_universe_d2(osc_basefill_075, 75)
OSC_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['osc_base_universe_d2_075_osc_basefill_075'] = {'inputs': ['osc_basefill_075'], 'func': osc_base_universe_d2_075_osc_basefill_075}
