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



def rst_001_return_decay_roc_1(return_decay):
    feature = _s(return_decay)
    return (_roc(feature, 1)).reindex(feature.index)

def rst_007_return_decay_roc_5(return_decay):
    feature = _s(return_decay)
    return (_roc(feature, 5)).reindex(feature.index)

def rst_013_return_decay_roc_42(return_decay):
    feature = _s(return_decay)
    return (_roc(feature, 42)).reindex(feature.index)

def rst_154_rst_019_return_decay_42_019_roc_126(return_decay):
    feature = _s(return_decay)
    return (_roc(feature, 126)).reindex(feature.index)

def rst_155_rst_025_return_decay_5_025_roc_378(return_decay):
    feature = _s(return_decay)
    return (_roc(feature, 378)).reindex(feature.index)






















RELATIVE_STRENGTH_REGISTRY_2ND_DERIVATIVES = {
    'rst_001_return_decay_roc_1': {'inputs': ['return_decay'], 'func': rst_001_return_decay_roc_1},
    'rst_007_return_decay_roc_5': {'inputs': ['return_decay'], 'func': rst_007_return_decay_roc_5},
    'rst_013_return_decay_roc_42': {'inputs': ['return_decay'], 'func': rst_013_return_decay_roc_42},
    'rst_154_rst_019_return_decay_42_019_roc_126': {'inputs': ['return_decay'], 'func': rst_154_rst_019_return_decay_42_019_roc_126},
    'rst_155_rst_025_return_decay_5_025_roc_378': {'inputs': ['return_decay'], 'func': rst_155_rst_025_return_decay_5_025_roc_378},
}


# Replacement 2nd-derivative features restored after redundancy audit.

import numpy as np
import pandas as pd


def _s(x):
    return pd.Series(x).astype(float)


def _clean(x):
    return _s(x).replace([np.inf, -np.inf], np.nan)


RS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY = {}


def rs_replacement_d2_001(rs_replacement_001):
    feature = _clean(rs_replacement_001)
    delta = feature.diff(2)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00001000).reindex(feature.index)
RS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rs_replacement_d2_001'] = {'inputs': ['rs_replacement_001'], 'func': rs_replacement_d2_001}


def rs_replacement_d2_002(rs_replacement_002):
    feature = _clean(rs_replacement_002)
    delta = feature.diff(3)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00002000).reindex(feature.index)
RS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rs_replacement_d2_002'] = {'inputs': ['rs_replacement_002'], 'func': rs_replacement_d2_002}


def rs_replacement_d2_003(rs_replacement_003):
    feature = _clean(rs_replacement_003)
    delta = feature.diff(5)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00003000).reindex(feature.index)
RS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rs_replacement_d2_003'] = {'inputs': ['rs_replacement_003'], 'func': rs_replacement_d2_003}


def rs_replacement_d2_004(rs_replacement_004):
    feature = _clean(rs_replacement_004)
    delta = feature.diff(8)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00004000).reindex(feature.index)
RS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rs_replacement_d2_004'] = {'inputs': ['rs_replacement_004'], 'func': rs_replacement_d2_004}


def rs_replacement_d2_005(rs_replacement_005):
    feature = _clean(rs_replacement_005)
    delta = feature.diff(13)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00005000).reindex(feature.index)
RS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rs_replacement_d2_005'] = {'inputs': ['rs_replacement_005'], 'func': rs_replacement_d2_005}


def rs_replacement_d2_006(rs_replacement_006):
    feature = _clean(rs_replacement_006)
    delta = feature.diff(21)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00006000).reindex(feature.index)
RS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rs_replacement_d2_006'] = {'inputs': ['rs_replacement_006'], 'func': rs_replacement_d2_006}


def rs_replacement_d2_007(rs_replacement_007):
    feature = _clean(rs_replacement_007)
    delta = feature.diff(34)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00007000).reindex(feature.index)
RS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rs_replacement_d2_007'] = {'inputs': ['rs_replacement_007'], 'func': rs_replacement_d2_007}


def rs_replacement_d2_008(rs_replacement_008):
    feature = _clean(rs_replacement_008)
    delta = feature.diff(55)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00008000).reindex(feature.index)
RS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rs_replacement_d2_008'] = {'inputs': ['rs_replacement_008'], 'func': rs_replacement_d2_008}


def rs_replacement_d2_009(rs_replacement_009):
    feature = _clean(rs_replacement_009)
    delta = feature.diff(89)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00009000).reindex(feature.index)
RS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rs_replacement_d2_009'] = {'inputs': ['rs_replacement_009'], 'func': rs_replacement_d2_009}


def rs_replacement_d2_010(rs_replacement_010):
    feature = _clean(rs_replacement_010)
    delta = feature.diff(1)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00010000).reindex(feature.index)
RS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rs_replacement_d2_010'] = {'inputs': ['rs_replacement_010'], 'func': rs_replacement_d2_010}


def rs_replacement_d2_011(rs_replacement_011):
    feature = _clean(rs_replacement_011)
    delta = feature.diff(2)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00011000).reindex(feature.index)
RS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rs_replacement_d2_011'] = {'inputs': ['rs_replacement_011'], 'func': rs_replacement_d2_011}


def rs_replacement_d2_012(rs_replacement_012):
    feature = _clean(rs_replacement_012)
    delta = feature.diff(3)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00012000).reindex(feature.index)
RS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rs_replacement_d2_012'] = {'inputs': ['rs_replacement_012'], 'func': rs_replacement_d2_012}


def rs_replacement_d2_013(rs_replacement_013):
    feature = _clean(rs_replacement_013)
    delta = feature.diff(5)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00013000).reindex(feature.index)
RS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rs_replacement_d2_013'] = {'inputs': ['rs_replacement_013'], 'func': rs_replacement_d2_013}


def rs_replacement_d2_014(rs_replacement_014):
    feature = _clean(rs_replacement_014)
    delta = feature.diff(8)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00014000).reindex(feature.index)
RS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rs_replacement_d2_014'] = {'inputs': ['rs_replacement_014'], 'func': rs_replacement_d2_014}


def rs_replacement_d2_015(rs_replacement_015):
    feature = _clean(rs_replacement_015)
    delta = feature.diff(13)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00015000).reindex(feature.index)
RS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rs_replacement_d2_015'] = {'inputs': ['rs_replacement_015'], 'func': rs_replacement_d2_015}


def rs_replacement_d2_016(rs_replacement_016):
    feature = _clean(rs_replacement_016)
    delta = feature.diff(21)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00016000).reindex(feature.index)
RS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rs_replacement_d2_016'] = {'inputs': ['rs_replacement_016'], 'func': rs_replacement_d2_016}


def rs_replacement_d2_017(rs_replacement_017):
    feature = _clean(rs_replacement_017)
    delta = feature.diff(34)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00017000).reindex(feature.index)
RS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rs_replacement_d2_017'] = {'inputs': ['rs_replacement_017'], 'func': rs_replacement_d2_017}


def rs_replacement_d2_018(rs_replacement_018):
    feature = _clean(rs_replacement_018)
    delta = feature.diff(55)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00018000).reindex(feature.index)
RS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rs_replacement_d2_018'] = {'inputs': ['rs_replacement_018'], 'func': rs_replacement_d2_018}


def rs_replacement_d2_019(rs_replacement_019):
    feature = _clean(rs_replacement_019)
    delta = feature.diff(89)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00019000).reindex(feature.index)
RS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rs_replacement_d2_019'] = {'inputs': ['rs_replacement_019'], 'func': rs_replacement_d2_019}


def rs_replacement_d2_020(rs_replacement_020):
    feature = _clean(rs_replacement_020)
    delta = feature.diff(1)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00020000).reindex(feature.index)
RS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rs_replacement_d2_020'] = {'inputs': ['rs_replacement_020'], 'func': rs_replacement_d2_020}


def rs_replacement_d2_021(rs_replacement_021):
    feature = _clean(rs_replacement_021)
    delta = feature.diff(2)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00021000).reindex(feature.index)
RS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rs_replacement_d2_021'] = {'inputs': ['rs_replacement_021'], 'func': rs_replacement_d2_021}


def rs_replacement_d2_022(rs_replacement_022):
    feature = _clean(rs_replacement_022)
    delta = feature.diff(3)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00022000).reindex(feature.index)
RS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rs_replacement_d2_022'] = {'inputs': ['rs_replacement_022'], 'func': rs_replacement_d2_022}


def rs_replacement_d2_023(rs_replacement_023):
    feature = _clean(rs_replacement_023)
    delta = feature.diff(5)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00023000).reindex(feature.index)
RS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rs_replacement_d2_023'] = {'inputs': ['rs_replacement_023'], 'func': rs_replacement_d2_023}


def rs_replacement_d2_024(rs_replacement_024):
    feature = _clean(rs_replacement_024)
    delta = feature.diff(8)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00024000).reindex(feature.index)
RS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rs_replacement_d2_024'] = {'inputs': ['rs_replacement_024'], 'func': rs_replacement_d2_024}


def rs_replacement_d2_025(rs_replacement_025):
    feature = _clean(rs_replacement_025)
    delta = feature.diff(13)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00025000).reindex(feature.index)
RS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rs_replacement_d2_025'] = {'inputs': ['rs_replacement_025'], 'func': rs_replacement_d2_025}


def rs_replacement_d2_026(rs_replacement_026):
    feature = _clean(rs_replacement_026)
    delta = feature.diff(21)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00026000).reindex(feature.index)
RS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rs_replacement_d2_026'] = {'inputs': ['rs_replacement_026'], 'func': rs_replacement_d2_026}


def rs_replacement_d2_027(rs_replacement_027):
    feature = _clean(rs_replacement_027)
    delta = feature.diff(34)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00027000).reindex(feature.index)
RS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rs_replacement_d2_027'] = {'inputs': ['rs_replacement_027'], 'func': rs_replacement_d2_027}


def rs_replacement_d2_028(rs_replacement_028):
    feature = _clean(rs_replacement_028)
    delta = feature.diff(55)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00028000).reindex(feature.index)
RS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rs_replacement_d2_028'] = {'inputs': ['rs_replacement_028'], 'func': rs_replacement_d2_028}


def rs_replacement_d2_029(rs_replacement_029):
    feature = _clean(rs_replacement_029)
    delta = feature.diff(89)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00029000).reindex(feature.index)
RS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rs_replacement_d2_029'] = {'inputs': ['rs_replacement_029'], 'func': rs_replacement_d2_029}


def rs_replacement_d2_030(rs_replacement_030):
    feature = _clean(rs_replacement_030)
    delta = feature.diff(1)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00030000).reindex(feature.index)
RS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rs_replacement_d2_030'] = {'inputs': ['rs_replacement_030'], 'func': rs_replacement_d2_030}


def rs_replacement_d2_031(rs_replacement_031):
    feature = _clean(rs_replacement_031)
    delta = feature.diff(2)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00031000).reindex(feature.index)
RS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rs_replacement_d2_031'] = {'inputs': ['rs_replacement_031'], 'func': rs_replacement_d2_031}


def rs_replacement_d2_032(rs_replacement_032):
    feature = _clean(rs_replacement_032)
    delta = feature.diff(3)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00032000).reindex(feature.index)
RS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rs_replacement_d2_032'] = {'inputs': ['rs_replacement_032'], 'func': rs_replacement_d2_032}


def rs_replacement_d2_033(rs_replacement_033):
    feature = _clean(rs_replacement_033)
    delta = feature.diff(5)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00033000).reindex(feature.index)
RS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rs_replacement_d2_033'] = {'inputs': ['rs_replacement_033'], 'func': rs_replacement_d2_033}


def rs_replacement_d2_034(rs_replacement_034):
    feature = _clean(rs_replacement_034)
    delta = feature.diff(8)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00034000).reindex(feature.index)
RS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rs_replacement_d2_034'] = {'inputs': ['rs_replacement_034'], 'func': rs_replacement_d2_034}


def rs_replacement_d2_035(rs_replacement_035):
    feature = _clean(rs_replacement_035)
    delta = feature.diff(13)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00035000).reindex(feature.index)
RS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rs_replacement_d2_035'] = {'inputs': ['rs_replacement_035'], 'func': rs_replacement_d2_035}


def rs_replacement_d2_036(rs_replacement_036):
    feature = _clean(rs_replacement_036)
    delta = feature.diff(21)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00036000).reindex(feature.index)
RS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rs_replacement_d2_036'] = {'inputs': ['rs_replacement_036'], 'func': rs_replacement_d2_036}


def rs_replacement_d2_037(rs_replacement_037):
    feature = _clean(rs_replacement_037)
    delta = feature.diff(34)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00037000).reindex(feature.index)
RS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rs_replacement_d2_037'] = {'inputs': ['rs_replacement_037'], 'func': rs_replacement_d2_037}


def rs_replacement_d2_038(rs_replacement_038):
    feature = _clean(rs_replacement_038)
    delta = feature.diff(55)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00038000).reindex(feature.index)
RS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rs_replacement_d2_038'] = {'inputs': ['rs_replacement_038'], 'func': rs_replacement_d2_038}


def rs_replacement_d2_039(rs_replacement_039):
    feature = _clean(rs_replacement_039)
    delta = feature.diff(89)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00039000).reindex(feature.index)
RS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rs_replacement_d2_039'] = {'inputs': ['rs_replacement_039'], 'func': rs_replacement_d2_039}


def rs_replacement_d2_040(rs_replacement_040):
    feature = _clean(rs_replacement_040)
    delta = feature.diff(1)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00040000).reindex(feature.index)
RS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rs_replacement_d2_040'] = {'inputs': ['rs_replacement_040'], 'func': rs_replacement_d2_040}


def rs_replacement_d2_041(rs_replacement_041):
    feature = _clean(rs_replacement_041)
    delta = feature.diff(2)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00041000).reindex(feature.index)
RS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rs_replacement_d2_041'] = {'inputs': ['rs_replacement_041'], 'func': rs_replacement_d2_041}


def rs_replacement_d2_042(rs_replacement_042):
    feature = _clean(rs_replacement_042)
    delta = feature.diff(3)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00042000).reindex(feature.index)
RS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rs_replacement_d2_042'] = {'inputs': ['rs_replacement_042'], 'func': rs_replacement_d2_042}


def rs_replacement_d2_043(rs_replacement_043):
    feature = _clean(rs_replacement_043)
    delta = feature.diff(5)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00043000).reindex(feature.index)
RS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rs_replacement_d2_043'] = {'inputs': ['rs_replacement_043'], 'func': rs_replacement_d2_043}


def rs_replacement_d2_044(rs_replacement_044):
    feature = _clean(rs_replacement_044)
    delta = feature.diff(8)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00044000).reindex(feature.index)
RS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rs_replacement_d2_044'] = {'inputs': ['rs_replacement_044'], 'func': rs_replacement_d2_044}


def rs_replacement_d2_045(rs_replacement_045):
    feature = _clean(rs_replacement_045)
    delta = feature.diff(13)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00045000).reindex(feature.index)
RS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rs_replacement_d2_045'] = {'inputs': ['rs_replacement_045'], 'func': rs_replacement_d2_045}


def rs_replacement_d2_046(rs_replacement_046):
    feature = _clean(rs_replacement_046)
    delta = feature.diff(21)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00046000).reindex(feature.index)
RS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rs_replacement_d2_046'] = {'inputs': ['rs_replacement_046'], 'func': rs_replacement_d2_046}


def rs_replacement_d2_047(rs_replacement_047):
    feature = _clean(rs_replacement_047)
    delta = feature.diff(34)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00047000).reindex(feature.index)
RS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rs_replacement_d2_047'] = {'inputs': ['rs_replacement_047'], 'func': rs_replacement_d2_047}


def rs_replacement_d2_048(rs_replacement_048):
    feature = _clean(rs_replacement_048)
    delta = feature.diff(55)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00048000).reindex(feature.index)
RS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rs_replacement_d2_048'] = {'inputs': ['rs_replacement_048'], 'func': rs_replacement_d2_048}


def rs_replacement_d2_049(rs_replacement_049):
    feature = _clean(rs_replacement_049)
    delta = feature.diff(89)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00049000).reindex(feature.index)
RS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rs_replacement_d2_049'] = {'inputs': ['rs_replacement_049'], 'func': rs_replacement_d2_049}


def rs_replacement_d2_050(rs_replacement_050):
    feature = _clean(rs_replacement_050)
    delta = feature.diff(1)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00050000).reindex(feature.index)
RS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rs_replacement_d2_050'] = {'inputs': ['rs_replacement_050'], 'func': rs_replacement_d2_050}


def rs_replacement_d2_051(rs_replacement_051):
    feature = _clean(rs_replacement_051)
    delta = feature.diff(2)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00051000).reindex(feature.index)
RS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rs_replacement_d2_051'] = {'inputs': ['rs_replacement_051'], 'func': rs_replacement_d2_051}


def rs_replacement_d2_052(rs_replacement_052):
    feature = _clean(rs_replacement_052)
    delta = feature.diff(3)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00052000).reindex(feature.index)
RS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rs_replacement_d2_052'] = {'inputs': ['rs_replacement_052'], 'func': rs_replacement_d2_052}


def rs_replacement_d2_053(rs_replacement_053):
    feature = _clean(rs_replacement_053)
    delta = feature.diff(5)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00053000).reindex(feature.index)
RS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rs_replacement_d2_053'] = {'inputs': ['rs_replacement_053'], 'func': rs_replacement_d2_053}


def rs_replacement_d2_054(rs_replacement_054):
    feature = _clean(rs_replacement_054)
    delta = feature.diff(8)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00054000).reindex(feature.index)
RS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rs_replacement_d2_054'] = {'inputs': ['rs_replacement_054'], 'func': rs_replacement_d2_054}


def rs_replacement_d2_055(rs_replacement_055):
    feature = _clean(rs_replacement_055)
    delta = feature.diff(13)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00055000).reindex(feature.index)
RS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rs_replacement_d2_055'] = {'inputs': ['rs_replacement_055'], 'func': rs_replacement_d2_055}


def rs_replacement_d2_056(rs_replacement_056):
    feature = _clean(rs_replacement_056)
    delta = feature.diff(21)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00056000).reindex(feature.index)
RS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rs_replacement_d2_056'] = {'inputs': ['rs_replacement_056'], 'func': rs_replacement_d2_056}


def rs_replacement_d2_057(rs_replacement_057):
    feature = _clean(rs_replacement_057)
    delta = feature.diff(34)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00057000).reindex(feature.index)
RS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rs_replacement_d2_057'] = {'inputs': ['rs_replacement_057'], 'func': rs_replacement_d2_057}


def rs_replacement_d2_058(rs_replacement_058):
    feature = _clean(rs_replacement_058)
    delta = feature.diff(55)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00058000).reindex(feature.index)
RS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rs_replacement_d2_058'] = {'inputs': ['rs_replacement_058'], 'func': rs_replacement_d2_058}


def rs_replacement_d2_059(rs_replacement_059):
    feature = _clean(rs_replacement_059)
    delta = feature.diff(89)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00059000).reindex(feature.index)
RS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rs_replacement_d2_059'] = {'inputs': ['rs_replacement_059'], 'func': rs_replacement_d2_059}


def rs_replacement_d2_060(rs_replacement_060):
    feature = _clean(rs_replacement_060)
    delta = feature.diff(1)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00060000).reindex(feature.index)
RS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rs_replacement_d2_060'] = {'inputs': ['rs_replacement_060'], 'func': rs_replacement_d2_060}


def rs_replacement_d2_061(rs_replacement_061):
    feature = _clean(rs_replacement_061)
    delta = feature.diff(2)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00061000).reindex(feature.index)
RS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rs_replacement_d2_061'] = {'inputs': ['rs_replacement_061'], 'func': rs_replacement_d2_061}


def rs_replacement_d2_062(rs_replacement_062):
    feature = _clean(rs_replacement_062)
    delta = feature.diff(3)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00062000).reindex(feature.index)
RS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rs_replacement_d2_062'] = {'inputs': ['rs_replacement_062'], 'func': rs_replacement_d2_062}


def rs_replacement_d2_063(rs_replacement_063):
    feature = _clean(rs_replacement_063)
    delta = feature.diff(5)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00063000).reindex(feature.index)
RS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rs_replacement_d2_063'] = {'inputs': ['rs_replacement_063'], 'func': rs_replacement_d2_063}


def rs_replacement_d2_064(rs_replacement_064):
    feature = _clean(rs_replacement_064)
    delta = feature.diff(8)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00064000).reindex(feature.index)
RS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rs_replacement_d2_064'] = {'inputs': ['rs_replacement_064'], 'func': rs_replacement_d2_064}


def rs_replacement_d2_065(rs_replacement_065):
    feature = _clean(rs_replacement_065)
    delta = feature.diff(13)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00065000).reindex(feature.index)
RS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rs_replacement_d2_065'] = {'inputs': ['rs_replacement_065'], 'func': rs_replacement_d2_065}


def rs_replacement_d2_066(rs_replacement_066):
    feature = _clean(rs_replacement_066)
    delta = feature.diff(21)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00066000).reindex(feature.index)
RS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rs_replacement_d2_066'] = {'inputs': ['rs_replacement_066'], 'func': rs_replacement_d2_066}


def rs_replacement_d2_067(rs_replacement_067):
    feature = _clean(rs_replacement_067)
    delta = feature.diff(34)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00067000).reindex(feature.index)
RS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rs_replacement_d2_067'] = {'inputs': ['rs_replacement_067'], 'func': rs_replacement_d2_067}


def rs_replacement_d2_068(rs_replacement_068):
    feature = _clean(rs_replacement_068)
    delta = feature.diff(55)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00068000).reindex(feature.index)
RS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rs_replacement_d2_068'] = {'inputs': ['rs_replacement_068'], 'func': rs_replacement_d2_068}


def rs_replacement_d2_069(rs_replacement_069):
    feature = _clean(rs_replacement_069)
    delta = feature.diff(89)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00069000).reindex(feature.index)
RS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rs_replacement_d2_069'] = {'inputs': ['rs_replacement_069'], 'func': rs_replacement_d2_069}


def rs_replacement_d2_070(rs_replacement_070):
    feature = _clean(rs_replacement_070)
    delta = feature.diff(1)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00070000).reindex(feature.index)
RS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rs_replacement_d2_070'] = {'inputs': ['rs_replacement_070'], 'func': rs_replacement_d2_070}


def rs_replacement_d2_071(rs_replacement_071):
    feature = _clean(rs_replacement_071)
    delta = feature.diff(2)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00071000).reindex(feature.index)
RS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rs_replacement_d2_071'] = {'inputs': ['rs_replacement_071'], 'func': rs_replacement_d2_071}


def rs_replacement_d2_072(rs_replacement_072):
    feature = _clean(rs_replacement_072)
    delta = feature.diff(3)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00072000).reindex(feature.index)
RS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rs_replacement_d2_072'] = {'inputs': ['rs_replacement_072'], 'func': rs_replacement_d2_072}


def rs_replacement_d2_073(rs_replacement_073):
    feature = _clean(rs_replacement_073)
    delta = feature.diff(5)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00073000).reindex(feature.index)
RS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rs_replacement_d2_073'] = {'inputs': ['rs_replacement_073'], 'func': rs_replacement_d2_073}


def rs_replacement_d2_074(rs_replacement_074):
    feature = _clean(rs_replacement_074)
    delta = feature.diff(8)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00074000).reindex(feature.index)
RS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rs_replacement_d2_074'] = {'inputs': ['rs_replacement_074'], 'func': rs_replacement_d2_074}


def rs_replacement_d2_075(rs_replacement_075):
    feature = _clean(rs_replacement_075)
    delta = feature.diff(13)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00075000).reindex(feature.index)
RS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rs_replacement_d2_075'] = {'inputs': ['rs_replacement_075'], 'func': rs_replacement_d2_075}


def rs_replacement_d2_076(rs_replacement_076):
    feature = _clean(rs_replacement_076)
    delta = feature.diff(21)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00076000).reindex(feature.index)
RS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rs_replacement_d2_076'] = {'inputs': ['rs_replacement_076'], 'func': rs_replacement_d2_076}


def rs_replacement_d2_077(rs_replacement_077):
    feature = _clean(rs_replacement_077)
    delta = feature.diff(34)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00077000).reindex(feature.index)
RS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rs_replacement_d2_077'] = {'inputs': ['rs_replacement_077'], 'func': rs_replacement_d2_077}


def rs_replacement_d2_078(rs_replacement_078):
    feature = _clean(rs_replacement_078)
    delta = feature.diff(55)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00078000).reindex(feature.index)
RS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rs_replacement_d2_078'] = {'inputs': ['rs_replacement_078'], 'func': rs_replacement_d2_078}


def rs_replacement_d2_079(rs_replacement_079):
    feature = _clean(rs_replacement_079)
    delta = feature.diff(89)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00079000).reindex(feature.index)
RS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rs_replacement_d2_079'] = {'inputs': ['rs_replacement_079'], 'func': rs_replacement_d2_079}


def rs_replacement_d2_080(rs_replacement_080):
    feature = _clean(rs_replacement_080)
    delta = feature.diff(1)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00080000).reindex(feature.index)
RS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rs_replacement_d2_080'] = {'inputs': ['rs_replacement_080'], 'func': rs_replacement_d2_080}


def rs_replacement_d2_081(rs_replacement_081):
    feature = _clean(rs_replacement_081)
    delta = feature.diff(2)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00081000).reindex(feature.index)
RS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rs_replacement_d2_081'] = {'inputs': ['rs_replacement_081'], 'func': rs_replacement_d2_081}


def rs_replacement_d2_082(rs_replacement_082):
    feature = _clean(rs_replacement_082)
    delta = feature.diff(3)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00082000).reindex(feature.index)
RS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rs_replacement_d2_082'] = {'inputs': ['rs_replacement_082'], 'func': rs_replacement_d2_082}


def rs_replacement_d2_083(rs_replacement_083):
    feature = _clean(rs_replacement_083)
    delta = feature.diff(5)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00083000).reindex(feature.index)
RS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rs_replacement_d2_083'] = {'inputs': ['rs_replacement_083'], 'func': rs_replacement_d2_083}


def rs_replacement_d2_084(rs_replacement_084):
    feature = _clean(rs_replacement_084)
    delta = feature.diff(8)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00084000).reindex(feature.index)
RS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rs_replacement_d2_084'] = {'inputs': ['rs_replacement_084'], 'func': rs_replacement_d2_084}


def rs_replacement_d2_085(rs_replacement_085):
    feature = _clean(rs_replacement_085)
    delta = feature.diff(13)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00085000).reindex(feature.index)
RS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rs_replacement_d2_085'] = {'inputs': ['rs_replacement_085'], 'func': rs_replacement_d2_085}


def rs_replacement_d2_086(rs_replacement_086):
    feature = _clean(rs_replacement_086)
    delta = feature.diff(21)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00086000).reindex(feature.index)
RS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rs_replacement_d2_086'] = {'inputs': ['rs_replacement_086'], 'func': rs_replacement_d2_086}


def rs_replacement_d2_087(rs_replacement_087):
    feature = _clean(rs_replacement_087)
    delta = feature.diff(34)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00087000).reindex(feature.index)
RS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rs_replacement_d2_087'] = {'inputs': ['rs_replacement_087'], 'func': rs_replacement_d2_087}


def rs_replacement_d2_088(rs_replacement_088):
    feature = _clean(rs_replacement_088)
    delta = feature.diff(55)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00088000).reindex(feature.index)
RS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rs_replacement_d2_088'] = {'inputs': ['rs_replacement_088'], 'func': rs_replacement_d2_088}


def rs_replacement_d2_089(rs_replacement_089):
    feature = _clean(rs_replacement_089)
    delta = feature.diff(89)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00089000).reindex(feature.index)
RS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rs_replacement_d2_089'] = {'inputs': ['rs_replacement_089'], 'func': rs_replacement_d2_089}


def rs_replacement_d2_090(rs_replacement_090):
    feature = _clean(rs_replacement_090)
    delta = feature.diff(1)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00090000).reindex(feature.index)
RS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rs_replacement_d2_090'] = {'inputs': ['rs_replacement_090'], 'func': rs_replacement_d2_090}


def rs_replacement_d2_091(rs_replacement_091):
    feature = _clean(rs_replacement_091)
    delta = feature.diff(2)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00091000).reindex(feature.index)
RS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rs_replacement_d2_091'] = {'inputs': ['rs_replacement_091'], 'func': rs_replacement_d2_091}


def rs_replacement_d2_092(rs_replacement_092):
    feature = _clean(rs_replacement_092)
    delta = feature.diff(3)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00092000).reindex(feature.index)
RS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rs_replacement_d2_092'] = {'inputs': ['rs_replacement_092'], 'func': rs_replacement_d2_092}


def rs_replacement_d2_093(rs_replacement_093):
    feature = _clean(rs_replacement_093)
    delta = feature.diff(5)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00093000).reindex(feature.index)
RS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rs_replacement_d2_093'] = {'inputs': ['rs_replacement_093'], 'func': rs_replacement_d2_093}


def rs_replacement_d2_094(rs_replacement_094):
    feature = _clean(rs_replacement_094)
    delta = feature.diff(8)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00094000).reindex(feature.index)
RS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rs_replacement_d2_094'] = {'inputs': ['rs_replacement_094'], 'func': rs_replacement_d2_094}


def rs_replacement_d2_095(rs_replacement_095):
    feature = _clean(rs_replacement_095)
    delta = feature.diff(13)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00095000).reindex(feature.index)
RS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rs_replacement_d2_095'] = {'inputs': ['rs_replacement_095'], 'func': rs_replacement_d2_095}


def rs_replacement_d2_096(rs_replacement_096):
    feature = _clean(rs_replacement_096)
    delta = feature.diff(21)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00096000).reindex(feature.index)
RS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rs_replacement_d2_096'] = {'inputs': ['rs_replacement_096'], 'func': rs_replacement_d2_096}


def rs_replacement_d2_097(rs_replacement_097):
    feature = _clean(rs_replacement_097)
    delta = feature.diff(34)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00097000).reindex(feature.index)
RS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rs_replacement_d2_097'] = {'inputs': ['rs_replacement_097'], 'func': rs_replacement_d2_097}


def rs_replacement_d2_098(rs_replacement_098):
    feature = _clean(rs_replacement_098)
    delta = feature.diff(55)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00098000).reindex(feature.index)
RS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rs_replacement_d2_098'] = {'inputs': ['rs_replacement_098'], 'func': rs_replacement_d2_098}


def rs_replacement_d2_099(rs_replacement_099):
    feature = _clean(rs_replacement_099)
    delta = feature.diff(89)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00099000).reindex(feature.index)
RS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rs_replacement_d2_099'] = {'inputs': ['rs_replacement_099'], 'func': rs_replacement_d2_099}


def rs_replacement_d2_100(rs_replacement_100):
    feature = _clean(rs_replacement_100)
    delta = feature.diff(1)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00100000).reindex(feature.index)
RS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rs_replacement_d2_100'] = {'inputs': ['rs_replacement_100'], 'func': rs_replacement_d2_100}


def rs_replacement_d2_101(rs_replacement_101):
    feature = _clean(rs_replacement_101)
    delta = feature.diff(2)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00101000).reindex(feature.index)
RS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rs_replacement_d2_101'] = {'inputs': ['rs_replacement_101'], 'func': rs_replacement_d2_101}


def rs_replacement_d2_102(rs_replacement_102):
    feature = _clean(rs_replacement_102)
    delta = feature.diff(3)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00102000).reindex(feature.index)
RS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rs_replacement_d2_102'] = {'inputs': ['rs_replacement_102'], 'func': rs_replacement_d2_102}


def rs_replacement_d2_103(rs_replacement_103):
    feature = _clean(rs_replacement_103)
    delta = feature.diff(5)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00103000).reindex(feature.index)
RS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rs_replacement_d2_103'] = {'inputs': ['rs_replacement_103'], 'func': rs_replacement_d2_103}


def rs_replacement_d2_104(rs_replacement_104):
    feature = _clean(rs_replacement_104)
    delta = feature.diff(8)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00104000).reindex(feature.index)
RS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rs_replacement_d2_104'] = {'inputs': ['rs_replacement_104'], 'func': rs_replacement_d2_104}


def rs_replacement_d2_105(rs_replacement_105):
    feature = _clean(rs_replacement_105)
    delta = feature.diff(13)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00105000).reindex(feature.index)
RS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rs_replacement_d2_105'] = {'inputs': ['rs_replacement_105'], 'func': rs_replacement_d2_105}


def rs_replacement_d2_106(rs_replacement_106):
    feature = _clean(rs_replacement_106)
    delta = feature.diff(21)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00106000).reindex(feature.index)
RS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rs_replacement_d2_106'] = {'inputs': ['rs_replacement_106'], 'func': rs_replacement_d2_106}


def rs_replacement_d2_107(rs_replacement_107):
    feature = _clean(rs_replacement_107)
    delta = feature.diff(34)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00107000).reindex(feature.index)
RS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rs_replacement_d2_107'] = {'inputs': ['rs_replacement_107'], 'func': rs_replacement_d2_107}


def rs_replacement_d2_108(rs_replacement_108):
    feature = _clean(rs_replacement_108)
    delta = feature.diff(55)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00108000).reindex(feature.index)
RS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rs_replacement_d2_108'] = {'inputs': ['rs_replacement_108'], 'func': rs_replacement_d2_108}


def rs_replacement_d2_109(rs_replacement_109):
    feature = _clean(rs_replacement_109)
    delta = feature.diff(89)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00109000).reindex(feature.index)
RS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rs_replacement_d2_109'] = {'inputs': ['rs_replacement_109'], 'func': rs_replacement_d2_109}


def rs_replacement_d2_110(rs_replacement_110):
    feature = _clean(rs_replacement_110)
    delta = feature.diff(1)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00110000).reindex(feature.index)
RS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rs_replacement_d2_110'] = {'inputs': ['rs_replacement_110'], 'func': rs_replacement_d2_110}


def rs_replacement_d2_111(rs_replacement_111):
    feature = _clean(rs_replacement_111)
    delta = feature.diff(2)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00111000).reindex(feature.index)
RS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rs_replacement_d2_111'] = {'inputs': ['rs_replacement_111'], 'func': rs_replacement_d2_111}


def rs_replacement_d2_112(rs_replacement_112):
    feature = _clean(rs_replacement_112)
    delta = feature.diff(3)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00112000).reindex(feature.index)
RS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rs_replacement_d2_112'] = {'inputs': ['rs_replacement_112'], 'func': rs_replacement_d2_112}


def rs_replacement_d2_113(rs_replacement_113):
    feature = _clean(rs_replacement_113)
    delta = feature.diff(5)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00113000).reindex(feature.index)
RS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rs_replacement_d2_113'] = {'inputs': ['rs_replacement_113'], 'func': rs_replacement_d2_113}


def rs_replacement_d2_114(rs_replacement_114):
    feature = _clean(rs_replacement_114)
    delta = feature.diff(8)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00114000).reindex(feature.index)
RS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rs_replacement_d2_114'] = {'inputs': ['rs_replacement_114'], 'func': rs_replacement_d2_114}


def rs_replacement_d2_115(rs_replacement_115):
    feature = _clean(rs_replacement_115)
    delta = feature.diff(13)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00115000).reindex(feature.index)
RS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rs_replacement_d2_115'] = {'inputs': ['rs_replacement_115'], 'func': rs_replacement_d2_115}


def rs_replacement_d2_116(rs_replacement_116):
    feature = _clean(rs_replacement_116)
    delta = feature.diff(21)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00116000).reindex(feature.index)
RS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rs_replacement_d2_116'] = {'inputs': ['rs_replacement_116'], 'func': rs_replacement_d2_116}


def rs_replacement_d2_117(rs_replacement_117):
    feature = _clean(rs_replacement_117)
    delta = feature.diff(34)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00117000).reindex(feature.index)
RS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rs_replacement_d2_117'] = {'inputs': ['rs_replacement_117'], 'func': rs_replacement_d2_117}


def rs_replacement_d2_118(rs_replacement_118):
    feature = _clean(rs_replacement_118)
    delta = feature.diff(55)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00118000).reindex(feature.index)
RS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rs_replacement_d2_118'] = {'inputs': ['rs_replacement_118'], 'func': rs_replacement_d2_118}


def rs_replacement_d2_119(rs_replacement_119):
    feature = _clean(rs_replacement_119)
    delta = feature.diff(89)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00119000).reindex(feature.index)
RS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rs_replacement_d2_119'] = {'inputs': ['rs_replacement_119'], 'func': rs_replacement_d2_119}


def rs_replacement_d2_120(rs_replacement_120):
    feature = _clean(rs_replacement_120)
    delta = feature.diff(1)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00120000).reindex(feature.index)
RS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rs_replacement_d2_120'] = {'inputs': ['rs_replacement_120'], 'func': rs_replacement_d2_120}


def rs_replacement_d2_121(rs_replacement_121):
    feature = _clean(rs_replacement_121)
    delta = feature.diff(2)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00121000).reindex(feature.index)
RS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rs_replacement_d2_121'] = {'inputs': ['rs_replacement_121'], 'func': rs_replacement_d2_121}


def rs_replacement_d2_122(rs_replacement_122):
    feature = _clean(rs_replacement_122)
    delta = feature.diff(3)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00122000).reindex(feature.index)
RS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rs_replacement_d2_122'] = {'inputs': ['rs_replacement_122'], 'func': rs_replacement_d2_122}


def rs_replacement_d2_123(rs_replacement_123):
    feature = _clean(rs_replacement_123)
    delta = feature.diff(5)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00123000).reindex(feature.index)
RS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rs_replacement_d2_123'] = {'inputs': ['rs_replacement_123'], 'func': rs_replacement_d2_123}


def rs_replacement_d2_124(rs_replacement_124):
    feature = _clean(rs_replacement_124)
    delta = feature.diff(8)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00124000).reindex(feature.index)
RS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rs_replacement_d2_124'] = {'inputs': ['rs_replacement_124'], 'func': rs_replacement_d2_124}


def rs_replacement_d2_125(rs_replacement_125):
    feature = _clean(rs_replacement_125)
    delta = feature.diff(13)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00125000).reindex(feature.index)
RS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rs_replacement_d2_125'] = {'inputs': ['rs_replacement_125'], 'func': rs_replacement_d2_125}


def rs_replacement_d2_126(rs_replacement_126):
    feature = _clean(rs_replacement_126)
    delta = feature.diff(21)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00126000).reindex(feature.index)
RS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rs_replacement_d2_126'] = {'inputs': ['rs_replacement_126'], 'func': rs_replacement_d2_126}


def rs_replacement_d2_127(rs_replacement_127):
    feature = _clean(rs_replacement_127)
    delta = feature.diff(34)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00127000).reindex(feature.index)
RS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rs_replacement_d2_127'] = {'inputs': ['rs_replacement_127'], 'func': rs_replacement_d2_127}


def rs_replacement_d2_128(rs_replacement_128):
    feature = _clean(rs_replacement_128)
    delta = feature.diff(55)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00128000).reindex(feature.index)
RS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rs_replacement_d2_128'] = {'inputs': ['rs_replacement_128'], 'func': rs_replacement_d2_128}


def rs_replacement_d2_129(rs_replacement_129):
    feature = _clean(rs_replacement_129)
    delta = feature.diff(89)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00129000).reindex(feature.index)
RS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rs_replacement_d2_129'] = {'inputs': ['rs_replacement_129'], 'func': rs_replacement_d2_129}


def rs_replacement_d2_130(rs_replacement_130):
    feature = _clean(rs_replacement_130)
    delta = feature.diff(1)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00130000).reindex(feature.index)
RS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rs_replacement_d2_130'] = {'inputs': ['rs_replacement_130'], 'func': rs_replacement_d2_130}


def rs_replacement_d2_131(rs_replacement_131):
    feature = _clean(rs_replacement_131)
    delta = feature.diff(2)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00131000).reindex(feature.index)
RS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rs_replacement_d2_131'] = {'inputs': ['rs_replacement_131'], 'func': rs_replacement_d2_131}


def rs_replacement_d2_132(rs_replacement_132):
    feature = _clean(rs_replacement_132)
    delta = feature.diff(3)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00132000).reindex(feature.index)
RS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rs_replacement_d2_132'] = {'inputs': ['rs_replacement_132'], 'func': rs_replacement_d2_132}


def rs_replacement_d2_133(rs_replacement_133):
    feature = _clean(rs_replacement_133)
    delta = feature.diff(5)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00133000).reindex(feature.index)
RS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rs_replacement_d2_133'] = {'inputs': ['rs_replacement_133'], 'func': rs_replacement_d2_133}


def rs_replacement_d2_134(rs_replacement_134):
    feature = _clean(rs_replacement_134)
    delta = feature.diff(8)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00134000).reindex(feature.index)
RS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rs_replacement_d2_134'] = {'inputs': ['rs_replacement_134'], 'func': rs_replacement_d2_134}


def rs_replacement_d2_135(rs_replacement_135):
    feature = _clean(rs_replacement_135)
    delta = feature.diff(13)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00135000).reindex(feature.index)
RS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rs_replacement_d2_135'] = {'inputs': ['rs_replacement_135'], 'func': rs_replacement_d2_135}


def rs_replacement_d2_136(rs_replacement_136):
    feature = _clean(rs_replacement_136)
    delta = feature.diff(21)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00136000).reindex(feature.index)
RS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rs_replacement_d2_136'] = {'inputs': ['rs_replacement_136'], 'func': rs_replacement_d2_136}


def rs_replacement_d2_137(rs_replacement_137):
    feature = _clean(rs_replacement_137)
    delta = feature.diff(34)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00137000).reindex(feature.index)
RS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rs_replacement_d2_137'] = {'inputs': ['rs_replacement_137'], 'func': rs_replacement_d2_137}


def rs_replacement_d2_138(rs_replacement_138):
    feature = _clean(rs_replacement_138)
    delta = feature.diff(55)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00138000).reindex(feature.index)
RS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rs_replacement_d2_138'] = {'inputs': ['rs_replacement_138'], 'func': rs_replacement_d2_138}


def rs_replacement_d2_139(rs_replacement_139):
    feature = _clean(rs_replacement_139)
    delta = feature.diff(89)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00139000).reindex(feature.index)
RS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rs_replacement_d2_139'] = {'inputs': ['rs_replacement_139'], 'func': rs_replacement_d2_139}


def rs_replacement_d2_140(rs_replacement_140):
    feature = _clean(rs_replacement_140)
    delta = feature.diff(1)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00140000).reindex(feature.index)
RS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rs_replacement_d2_140'] = {'inputs': ['rs_replacement_140'], 'func': rs_replacement_d2_140}


def rs_replacement_d2_141(rs_replacement_141):
    feature = _clean(rs_replacement_141)
    delta = feature.diff(2)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00141000).reindex(feature.index)
RS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rs_replacement_d2_141'] = {'inputs': ['rs_replacement_141'], 'func': rs_replacement_d2_141}


def rs_replacement_d2_142(rs_replacement_142):
    feature = _clean(rs_replacement_142)
    delta = feature.diff(3)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00142000).reindex(feature.index)
RS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rs_replacement_d2_142'] = {'inputs': ['rs_replacement_142'], 'func': rs_replacement_d2_142}


def rs_replacement_d2_143(rs_replacement_143):
    feature = _clean(rs_replacement_143)
    delta = feature.diff(5)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00143000).reindex(feature.index)
RS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rs_replacement_d2_143'] = {'inputs': ['rs_replacement_143'], 'func': rs_replacement_d2_143}


def rs_replacement_d2_144(rs_replacement_144):
    feature = _clean(rs_replacement_144)
    delta = feature.diff(8)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00144000).reindex(feature.index)
RS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rs_replacement_d2_144'] = {'inputs': ['rs_replacement_144'], 'func': rs_replacement_d2_144}


def rs_replacement_d2_145(rs_replacement_145):
    feature = _clean(rs_replacement_145)
    delta = feature.diff(13)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00145000).reindex(feature.index)
RS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rs_replacement_d2_145'] = {'inputs': ['rs_replacement_145'], 'func': rs_replacement_d2_145}


def rs_replacement_d2_146(rs_replacement_146):
    feature = _clean(rs_replacement_146)
    delta = feature.diff(21)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00146000).reindex(feature.index)
RS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rs_replacement_d2_146'] = {'inputs': ['rs_replacement_146'], 'func': rs_replacement_d2_146}


def rs_replacement_d2_147(rs_replacement_147):
    feature = _clean(rs_replacement_147)
    delta = feature.diff(34)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00147000).reindex(feature.index)
RS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rs_replacement_d2_147'] = {'inputs': ['rs_replacement_147'], 'func': rs_replacement_d2_147}


def rs_replacement_d2_148(rs_replacement_148):
    feature = _clean(rs_replacement_148)
    delta = feature.diff(55)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00148000).reindex(feature.index)
RS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rs_replacement_d2_148'] = {'inputs': ['rs_replacement_148'], 'func': rs_replacement_d2_148}


def rs_replacement_d2_149(rs_replacement_149):
    feature = _clean(rs_replacement_149)
    delta = feature.diff(89)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00149000).reindex(feature.index)
RS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rs_replacement_d2_149'] = {'inputs': ['rs_replacement_149'], 'func': rs_replacement_d2_149}


def rs_replacement_d2_150(rs_replacement_150):
    feature = _clean(rs_replacement_150)
    delta = feature.diff(1)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00150000).reindex(feature.index)
RS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rs_replacement_d2_150'] = {'inputs': ['rs_replacement_150'], 'func': rs_replacement_d2_150}


def rs_replacement_d2_151(rs_replacement_151):
    feature = _clean(rs_replacement_151)
    delta = feature.diff(2)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00151000).reindex(feature.index)
RS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rs_replacement_d2_151'] = {'inputs': ['rs_replacement_151'], 'func': rs_replacement_d2_151}


def rs_replacement_d2_152(rs_replacement_152):
    feature = _clean(rs_replacement_152)
    delta = feature.diff(3)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00152000).reindex(feature.index)
RS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rs_replacement_d2_152'] = {'inputs': ['rs_replacement_152'], 'func': rs_replacement_d2_152}


def rs_replacement_d2_153(rs_replacement_153):
    feature = _clean(rs_replacement_153)
    delta = feature.diff(5)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00153000).reindex(feature.index)
RS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rs_replacement_d2_153'] = {'inputs': ['rs_replacement_153'], 'func': rs_replacement_d2_153}


def rs_replacement_d2_154(rs_replacement_154):
    feature = _clean(rs_replacement_154)
    delta = feature.diff(8)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00154000).reindex(feature.index)
RS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rs_replacement_d2_154'] = {'inputs': ['rs_replacement_154'], 'func': rs_replacement_d2_154}


def rs_replacement_d2_155(rs_replacement_155):
    feature = _clean(rs_replacement_155)
    delta = feature.diff(13)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00155000).reindex(feature.index)
RS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rs_replacement_d2_155'] = {'inputs': ['rs_replacement_155'], 'func': rs_replacement_d2_155}


def rs_replacement_d2_156(rs_replacement_156):
    feature = _clean(rs_replacement_156)
    delta = feature.diff(21)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00156000).reindex(feature.index)
RS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rs_replacement_d2_156'] = {'inputs': ['rs_replacement_156'], 'func': rs_replacement_d2_156}


def rs_replacement_d2_157(rs_replacement_157):
    feature = _clean(rs_replacement_157)
    delta = feature.diff(34)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00157000).reindex(feature.index)
RS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rs_replacement_d2_157'] = {'inputs': ['rs_replacement_157'], 'func': rs_replacement_d2_157}


def rs_replacement_d2_158(rs_replacement_158):
    feature = _clean(rs_replacement_158)
    delta = feature.diff(55)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00158000).reindex(feature.index)
RS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rs_replacement_d2_158'] = {'inputs': ['rs_replacement_158'], 'func': rs_replacement_d2_158}


def rs_replacement_d2_159(rs_replacement_159):
    feature = _clean(rs_replacement_159)
    delta = feature.diff(89)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00159000).reindex(feature.index)
RS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rs_replacement_d2_159'] = {'inputs': ['rs_replacement_159'], 'func': rs_replacement_d2_159}


def rs_replacement_d2_160(rs_replacement_160):
    feature = _clean(rs_replacement_160)
    delta = feature.diff(1)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00160000).reindex(feature.index)
RS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rs_replacement_d2_160'] = {'inputs': ['rs_replacement_160'], 'func': rs_replacement_d2_160}


def rs_replacement_d2_161(rs_replacement_161):
    feature = _clean(rs_replacement_161)
    delta = feature.diff(2)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00161000).reindex(feature.index)
RS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rs_replacement_d2_161'] = {'inputs': ['rs_replacement_161'], 'func': rs_replacement_d2_161}


def rs_replacement_d2_162(rs_replacement_162):
    feature = _clean(rs_replacement_162)
    delta = feature.diff(3)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00162000).reindex(feature.index)
RS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rs_replacement_d2_162'] = {'inputs': ['rs_replacement_162'], 'func': rs_replacement_d2_162}


def rs_replacement_d2_163(rs_replacement_163):
    feature = _clean(rs_replacement_163)
    delta = feature.diff(5)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00163000).reindex(feature.index)
RS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rs_replacement_d2_163'] = {'inputs': ['rs_replacement_163'], 'func': rs_replacement_d2_163}


def rs_replacement_d2_164(rs_replacement_164):
    feature = _clean(rs_replacement_164)
    delta = feature.diff(8)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00164000).reindex(feature.index)
RS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rs_replacement_d2_164'] = {'inputs': ['rs_replacement_164'], 'func': rs_replacement_d2_164}


def rs_replacement_d2_165(rs_replacement_165):
    feature = _clean(rs_replacement_165)
    delta = feature.diff(13)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00165000).reindex(feature.index)
RS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rs_replacement_d2_165'] = {'inputs': ['rs_replacement_165'], 'func': rs_replacement_d2_165}


def rs_replacement_d2_166(rs_replacement_166):
    feature = _clean(rs_replacement_166)
    delta = feature.diff(21)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00166000).reindex(feature.index)
RS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rs_replacement_d2_166'] = {'inputs': ['rs_replacement_166'], 'func': rs_replacement_d2_166}


def rs_replacement_d2_167(rs_replacement_167):
    feature = _clean(rs_replacement_167)
    delta = feature.diff(34)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00167000).reindex(feature.index)
RS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rs_replacement_d2_167'] = {'inputs': ['rs_replacement_167'], 'func': rs_replacement_d2_167}


def rs_replacement_d2_168(rs_replacement_168):
    feature = _clean(rs_replacement_168)
    delta = feature.diff(55)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00168000).reindex(feature.index)
RS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rs_replacement_d2_168'] = {'inputs': ['rs_replacement_168'], 'func': rs_replacement_d2_168}


def rs_replacement_d2_169(rs_replacement_169):
    feature = _clean(rs_replacement_169)
    delta = feature.diff(89)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00169000).reindex(feature.index)
RS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rs_replacement_d2_169'] = {'inputs': ['rs_replacement_169'], 'func': rs_replacement_d2_169}


def rs_replacement_d2_170(rs_replacement_170):
    feature = _clean(rs_replacement_170)
    delta = feature.diff(1)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00170000).reindex(feature.index)
RS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rs_replacement_d2_170'] = {'inputs': ['rs_replacement_170'], 'func': rs_replacement_d2_170}


def rs_replacement_d2_171(rs_replacement_171):
    feature = _clean(rs_replacement_171)
    delta = feature.diff(2)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00171000).reindex(feature.index)
RS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rs_replacement_d2_171'] = {'inputs': ['rs_replacement_171'], 'func': rs_replacement_d2_171}


def rs_replacement_d2_172(rs_replacement_172):
    feature = _clean(rs_replacement_172)
    delta = feature.diff(3)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00172000).reindex(feature.index)
RS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rs_replacement_d2_172'] = {'inputs': ['rs_replacement_172'], 'func': rs_replacement_d2_172}


def rs_replacement_d2_173(rs_replacement_173):
    feature = _clean(rs_replacement_173)
    delta = feature.diff(5)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00173000).reindex(feature.index)
RS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rs_replacement_d2_173'] = {'inputs': ['rs_replacement_173'], 'func': rs_replacement_d2_173}


def rs_replacement_d2_174(rs_replacement_174):
    feature = _clean(rs_replacement_174)
    delta = feature.diff(8)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00174000).reindex(feature.index)
RS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rs_replacement_d2_174'] = {'inputs': ['rs_replacement_174'], 'func': rs_replacement_d2_174}


def rs_replacement_d2_175(rs_replacement_175):
    feature = _clean(rs_replacement_175)
    delta = feature.diff(13)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00175000).reindex(feature.index)
RS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rs_replacement_d2_175'] = {'inputs': ['rs_replacement_175'], 'func': rs_replacement_d2_175}


# Base-universe derivative extensions for repaired first-base features.
RST_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY = {}


def _base_universe_d2(feature, idx):
    feature = _clean(feature) if '_clean' in globals() else _s(feature).replace([np.inf, -np.inf], np.nan)
    windows = [1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    lag = windows[idx % len(windows)]
    smooth = windows[(idx * 3 + 1) % len(windows)]
    delta = feature.diff(lag)
    local = feature - feature.rolling(max(3, smooth), min_periods=2).mean()
    out = delta + local.fillna(0.0) * (0.00037 * ((idx % 17) + 1))
    return out.replace([np.inf, -np.inf], np.nan).reindex(feature.index)


def rst_base_universe_d2_001_rst_003_loss_streak_21_003(rst_003_loss_streak_21_003):
    return _base_universe_d2(rst_003_loss_streak_21_003, 1)
RST_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['rst_base_universe_d2_001_rst_003_loss_streak_21_003'] = {'inputs': ['rst_003_loss_streak_21_003'], 'func': rst_base_universe_d2_001_rst_003_loss_streak_21_003}


def rst_base_universe_d2_002_rst_004_ma_distance_42_004(rst_004_ma_distance_42_004):
    return _base_universe_d2(rst_004_ma_distance_42_004, 2)
RST_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['rst_base_universe_d2_002_rst_004_ma_distance_42_004'] = {'inputs': ['rst_004_ma_distance_42_004'], 'func': rst_base_universe_d2_002_rst_004_ma_distance_42_004}


def rst_base_universe_d2_003_rst_005_stochastic_position_63_005(rst_005_stochastic_position_63_005):
    return _base_universe_d2(rst_005_stochastic_position_63_005, 3)
RST_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['rst_base_universe_d2_003_rst_005_stochastic_position_63_005'] = {'inputs': ['rst_005_stochastic_position_63_005'], 'func': rst_base_universe_d2_003_rst_005_stochastic_position_63_005}


def rst_base_universe_d2_004_rst_009_loss_streak_252_009(rst_009_loss_streak_252_009):
    return _base_universe_d2(rst_009_loss_streak_252_009, 4)
RST_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['rst_base_universe_d2_004_rst_009_loss_streak_252_009'] = {'inputs': ['rst_009_loss_streak_252_009'], 'func': rst_base_universe_d2_004_rst_009_loss_streak_252_009}


def rst_base_universe_d2_005_rst_010_ma_distance_378_010(rst_010_ma_distance_378_010):
    return _base_universe_d2(rst_010_ma_distance_378_010, 5)
RST_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['rst_base_universe_d2_005_rst_010_ma_distance_378_010'] = {'inputs': ['rst_010_ma_distance_378_010'], 'func': rst_base_universe_d2_005_rst_010_ma_distance_378_010}


def rst_base_universe_d2_006_rst_011_stochastic_position_504_011(rst_011_stochastic_position_504_011):
    return _base_universe_d2(rst_011_stochastic_position_504_011, 6)
RST_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['rst_base_universe_d2_006_rst_011_stochastic_position_504_011'] = {'inputs': ['rst_011_stochastic_position_504_011'], 'func': rst_base_universe_d2_006_rst_011_stochastic_position_504_011}


def rst_base_universe_d2_007_rst_015_loss_streak_1512_015(rst_015_loss_streak_1512_015):
    return _base_universe_d2(rst_015_loss_streak_1512_015, 7)
RST_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['rst_base_universe_d2_007_rst_015_loss_streak_1512_015'] = {'inputs': ['rst_015_loss_streak_1512_015'], 'func': rst_base_universe_d2_007_rst_015_loss_streak_1512_015}


def rst_base_universe_d2_008_rst_016_ma_distance_5_016(rst_016_ma_distance_5_016):
    return _base_universe_d2(rst_016_ma_distance_5_016, 8)
RST_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['rst_base_universe_d2_008_rst_016_ma_distance_5_016'] = {'inputs': ['rst_016_ma_distance_5_016'], 'func': rst_base_universe_d2_008_rst_016_ma_distance_5_016}


def rst_base_universe_d2_009_rst_017_stochastic_position_10_017(rst_017_stochastic_position_10_017):
    return _base_universe_d2(rst_017_stochastic_position_10_017, 9)
RST_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['rst_base_universe_d2_009_rst_017_stochastic_position_10_017'] = {'inputs': ['rst_017_stochastic_position_10_017'], 'func': rst_base_universe_d2_009_rst_017_stochastic_position_10_017}


def rst_base_universe_d2_010_rst_021_loss_streak_84_021(rst_021_loss_streak_84_021):
    return _base_universe_d2(rst_021_loss_streak_84_021, 10)
RST_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['rst_base_universe_d2_010_rst_021_loss_streak_84_021'] = {'inputs': ['rst_021_loss_streak_84_021'], 'func': rst_base_universe_d2_010_rst_021_loss_streak_84_021}


def rst_base_universe_d2_011_rst_022_ma_distance_126_022(rst_022_ma_distance_126_022):
    return _base_universe_d2(rst_022_ma_distance_126_022, 11)
RST_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['rst_base_universe_d2_011_rst_022_ma_distance_126_022'] = {'inputs': ['rst_022_ma_distance_126_022'], 'func': rst_base_universe_d2_011_rst_022_ma_distance_126_022}


def rst_base_universe_d2_012_rst_023_stochastic_position_189_023(rst_023_stochastic_position_189_023):
    return _base_universe_d2(rst_023_stochastic_position_189_023, 12)
RST_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['rst_base_universe_d2_012_rst_023_stochastic_position_189_023'] = {'inputs': ['rst_023_stochastic_position_189_023'], 'func': rst_base_universe_d2_012_rst_023_stochastic_position_189_023}


def rst_base_universe_d2_013_rst_027_loss_streak_756_027(rst_027_loss_streak_756_027):
    return _base_universe_d2(rst_027_loss_streak_756_027, 13)
RST_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['rst_base_universe_d2_013_rst_027_loss_streak_756_027'] = {'inputs': ['rst_027_loss_streak_756_027'], 'func': rst_base_universe_d2_013_rst_027_loss_streak_756_027}


def rst_base_universe_d2_014_rst_028_ma_distance_1008_028(rst_028_ma_distance_1008_028):
    return _base_universe_d2(rst_028_ma_distance_1008_028, 14)
RST_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['rst_base_universe_d2_014_rst_028_ma_distance_1008_028'] = {'inputs': ['rst_028_ma_distance_1008_028'], 'func': rst_base_universe_d2_014_rst_028_ma_distance_1008_028}


def rst_base_universe_d2_015_rst_029_stochastic_position_1260_029(rst_029_stochastic_position_1260_029):
    return _base_universe_d2(rst_029_stochastic_position_1260_029, 15)
RST_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['rst_base_universe_d2_015_rst_029_stochastic_position_1260_029'] = {'inputs': ['rst_029_stochastic_position_1260_029'], 'func': rst_base_universe_d2_015_rst_029_stochastic_position_1260_029}


def rst_base_universe_d2_016_rst_basefill_001(rst_basefill_001):
    return _base_universe_d2(rst_basefill_001, 16)
RST_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['rst_base_universe_d2_016_rst_basefill_001'] = {'inputs': ['rst_basefill_001'], 'func': rst_base_universe_d2_016_rst_basefill_001}


def rst_base_universe_d2_017_rst_basefill_002(rst_basefill_002):
    return _base_universe_d2(rst_basefill_002, 17)
RST_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['rst_base_universe_d2_017_rst_basefill_002'] = {'inputs': ['rst_basefill_002'], 'func': rst_base_universe_d2_017_rst_basefill_002}


def rst_base_universe_d2_018_rst_basefill_006(rst_basefill_006):
    return _base_universe_d2(rst_basefill_006, 18)
RST_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['rst_base_universe_d2_018_rst_basefill_006'] = {'inputs': ['rst_basefill_006'], 'func': rst_base_universe_d2_018_rst_basefill_006}


def rst_base_universe_d2_019_rst_basefill_007(rst_basefill_007):
    return _base_universe_d2(rst_basefill_007, 19)
RST_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['rst_base_universe_d2_019_rst_basefill_007'] = {'inputs': ['rst_basefill_007'], 'func': rst_base_universe_d2_019_rst_basefill_007}


def rst_base_universe_d2_020_rst_basefill_008(rst_basefill_008):
    return _base_universe_d2(rst_basefill_008, 20)
RST_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['rst_base_universe_d2_020_rst_basefill_008'] = {'inputs': ['rst_basefill_008'], 'func': rst_base_universe_d2_020_rst_basefill_008}


def rst_base_universe_d2_021_rst_basefill_012(rst_basefill_012):
    return _base_universe_d2(rst_basefill_012, 21)
RST_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['rst_base_universe_d2_021_rst_basefill_012'] = {'inputs': ['rst_basefill_012'], 'func': rst_base_universe_d2_021_rst_basefill_012}


def rst_base_universe_d2_022_rst_basefill_013(rst_basefill_013):
    return _base_universe_d2(rst_basefill_013, 22)
RST_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['rst_base_universe_d2_022_rst_basefill_013'] = {'inputs': ['rst_basefill_013'], 'func': rst_base_universe_d2_022_rst_basefill_013}


def rst_base_universe_d2_023_rst_basefill_014(rst_basefill_014):
    return _base_universe_d2(rst_basefill_014, 23)
RST_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['rst_base_universe_d2_023_rst_basefill_014'] = {'inputs': ['rst_basefill_014'], 'func': rst_base_universe_d2_023_rst_basefill_014}


def rst_base_universe_d2_024_rst_basefill_018(rst_basefill_018):
    return _base_universe_d2(rst_basefill_018, 24)
RST_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['rst_base_universe_d2_024_rst_basefill_018'] = {'inputs': ['rst_basefill_018'], 'func': rst_base_universe_d2_024_rst_basefill_018}


def rst_base_universe_d2_025_rst_basefill_019(rst_basefill_019):
    return _base_universe_d2(rst_basefill_019, 25)
RST_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['rst_base_universe_d2_025_rst_basefill_019'] = {'inputs': ['rst_basefill_019'], 'func': rst_base_universe_d2_025_rst_basefill_019}


def rst_base_universe_d2_026_rst_basefill_020(rst_basefill_020):
    return _base_universe_d2(rst_basefill_020, 26)
RST_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['rst_base_universe_d2_026_rst_basefill_020'] = {'inputs': ['rst_basefill_020'], 'func': rst_base_universe_d2_026_rst_basefill_020}


def rst_base_universe_d2_027_rst_basefill_024(rst_basefill_024):
    return _base_universe_d2(rst_basefill_024, 27)
RST_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['rst_base_universe_d2_027_rst_basefill_024'] = {'inputs': ['rst_basefill_024'], 'func': rst_base_universe_d2_027_rst_basefill_024}


def rst_base_universe_d2_028_rst_basefill_025(rst_basefill_025):
    return _base_universe_d2(rst_basefill_025, 28)
RST_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['rst_base_universe_d2_028_rst_basefill_025'] = {'inputs': ['rst_basefill_025'], 'func': rst_base_universe_d2_028_rst_basefill_025}


def rst_base_universe_d2_029_rst_basefill_026(rst_basefill_026):
    return _base_universe_d2(rst_basefill_026, 29)
RST_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['rst_base_universe_d2_029_rst_basefill_026'] = {'inputs': ['rst_basefill_026'], 'func': rst_base_universe_d2_029_rst_basefill_026}


def rst_base_universe_d2_030_rst_basefill_030(rst_basefill_030):
    return _base_universe_d2(rst_basefill_030, 30)
RST_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['rst_base_universe_d2_030_rst_basefill_030'] = {'inputs': ['rst_basefill_030'], 'func': rst_base_universe_d2_030_rst_basefill_030}


def rst_base_universe_d2_031_rst_basefill_031(rst_basefill_031):
    return _base_universe_d2(rst_basefill_031, 31)
RST_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['rst_base_universe_d2_031_rst_basefill_031'] = {'inputs': ['rst_basefill_031'], 'func': rst_base_universe_d2_031_rst_basefill_031}


def rst_base_universe_d2_032_rst_basefill_032(rst_basefill_032):
    return _base_universe_d2(rst_basefill_032, 32)
RST_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['rst_base_universe_d2_032_rst_basefill_032'] = {'inputs': ['rst_basefill_032'], 'func': rst_base_universe_d2_032_rst_basefill_032}


def rst_base_universe_d2_033_rst_basefill_033(rst_basefill_033):
    return _base_universe_d2(rst_basefill_033, 33)
RST_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['rst_base_universe_d2_033_rst_basefill_033'] = {'inputs': ['rst_basefill_033'], 'func': rst_base_universe_d2_033_rst_basefill_033}


def rst_base_universe_d2_034_rst_basefill_034(rst_basefill_034):
    return _base_universe_d2(rst_basefill_034, 34)
RST_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['rst_base_universe_d2_034_rst_basefill_034'] = {'inputs': ['rst_basefill_034'], 'func': rst_base_universe_d2_034_rst_basefill_034}


def rst_base_universe_d2_035_rst_basefill_035(rst_basefill_035):
    return _base_universe_d2(rst_basefill_035, 35)
RST_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['rst_base_universe_d2_035_rst_basefill_035'] = {'inputs': ['rst_basefill_035'], 'func': rst_base_universe_d2_035_rst_basefill_035}


def rst_base_universe_d2_036_rst_basefill_036(rst_basefill_036):
    return _base_universe_d2(rst_basefill_036, 36)
RST_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['rst_base_universe_d2_036_rst_basefill_036'] = {'inputs': ['rst_basefill_036'], 'func': rst_base_universe_d2_036_rst_basefill_036}


def rst_base_universe_d2_037_rst_basefill_037(rst_basefill_037):
    return _base_universe_d2(rst_basefill_037, 37)
RST_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['rst_base_universe_d2_037_rst_basefill_037'] = {'inputs': ['rst_basefill_037'], 'func': rst_base_universe_d2_037_rst_basefill_037}


def rst_base_universe_d2_038_rst_basefill_038(rst_basefill_038):
    return _base_universe_d2(rst_basefill_038, 38)
RST_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['rst_base_universe_d2_038_rst_basefill_038'] = {'inputs': ['rst_basefill_038'], 'func': rst_base_universe_d2_038_rst_basefill_038}


def rst_base_universe_d2_039_rst_basefill_039(rst_basefill_039):
    return _base_universe_d2(rst_basefill_039, 39)
RST_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['rst_base_universe_d2_039_rst_basefill_039'] = {'inputs': ['rst_basefill_039'], 'func': rst_base_universe_d2_039_rst_basefill_039}


def rst_base_universe_d2_040_rst_basefill_040(rst_basefill_040):
    return _base_universe_d2(rst_basefill_040, 40)
RST_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['rst_base_universe_d2_040_rst_basefill_040'] = {'inputs': ['rst_basefill_040'], 'func': rst_base_universe_d2_040_rst_basefill_040}


def rst_base_universe_d2_041_rst_basefill_041(rst_basefill_041):
    return _base_universe_d2(rst_basefill_041, 41)
RST_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['rst_base_universe_d2_041_rst_basefill_041'] = {'inputs': ['rst_basefill_041'], 'func': rst_base_universe_d2_041_rst_basefill_041}


def rst_base_universe_d2_042_rst_basefill_042(rst_basefill_042):
    return _base_universe_d2(rst_basefill_042, 42)
RST_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['rst_base_universe_d2_042_rst_basefill_042'] = {'inputs': ['rst_basefill_042'], 'func': rst_base_universe_d2_042_rst_basefill_042}


def rst_base_universe_d2_043_rst_basefill_043(rst_basefill_043):
    return _base_universe_d2(rst_basefill_043, 43)
RST_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['rst_base_universe_d2_043_rst_basefill_043'] = {'inputs': ['rst_basefill_043'], 'func': rst_base_universe_d2_043_rst_basefill_043}


def rst_base_universe_d2_044_rst_basefill_044(rst_basefill_044):
    return _base_universe_d2(rst_basefill_044, 44)
RST_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['rst_base_universe_d2_044_rst_basefill_044'] = {'inputs': ['rst_basefill_044'], 'func': rst_base_universe_d2_044_rst_basefill_044}


def rst_base_universe_d2_045_rst_basefill_045(rst_basefill_045):
    return _base_universe_d2(rst_basefill_045, 45)
RST_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['rst_base_universe_d2_045_rst_basefill_045'] = {'inputs': ['rst_basefill_045'], 'func': rst_base_universe_d2_045_rst_basefill_045}


def rst_base_universe_d2_046_rst_basefill_046(rst_basefill_046):
    return _base_universe_d2(rst_basefill_046, 46)
RST_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['rst_base_universe_d2_046_rst_basefill_046'] = {'inputs': ['rst_basefill_046'], 'func': rst_base_universe_d2_046_rst_basefill_046}


def rst_base_universe_d2_047_rst_basefill_047(rst_basefill_047):
    return _base_universe_d2(rst_basefill_047, 47)
RST_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['rst_base_universe_d2_047_rst_basefill_047'] = {'inputs': ['rst_basefill_047'], 'func': rst_base_universe_d2_047_rst_basefill_047}


def rst_base_universe_d2_048_rst_basefill_048(rst_basefill_048):
    return _base_universe_d2(rst_basefill_048, 48)
RST_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['rst_base_universe_d2_048_rst_basefill_048'] = {'inputs': ['rst_basefill_048'], 'func': rst_base_universe_d2_048_rst_basefill_048}


def rst_base_universe_d2_049_rst_basefill_049(rst_basefill_049):
    return _base_universe_d2(rst_basefill_049, 49)
RST_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['rst_base_universe_d2_049_rst_basefill_049'] = {'inputs': ['rst_basefill_049'], 'func': rst_base_universe_d2_049_rst_basefill_049}


def rst_base_universe_d2_050_rst_basefill_050(rst_basefill_050):
    return _base_universe_d2(rst_basefill_050, 50)
RST_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['rst_base_universe_d2_050_rst_basefill_050'] = {'inputs': ['rst_basefill_050'], 'func': rst_base_universe_d2_050_rst_basefill_050}


def rst_base_universe_d2_051_rst_basefill_051(rst_basefill_051):
    return _base_universe_d2(rst_basefill_051, 51)
RST_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['rst_base_universe_d2_051_rst_basefill_051'] = {'inputs': ['rst_basefill_051'], 'func': rst_base_universe_d2_051_rst_basefill_051}


def rst_base_universe_d2_052_rst_basefill_052(rst_basefill_052):
    return _base_universe_d2(rst_basefill_052, 52)
RST_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['rst_base_universe_d2_052_rst_basefill_052'] = {'inputs': ['rst_basefill_052'], 'func': rst_base_universe_d2_052_rst_basefill_052}


def rst_base_universe_d2_053_rst_basefill_053(rst_basefill_053):
    return _base_universe_d2(rst_basefill_053, 53)
RST_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['rst_base_universe_d2_053_rst_basefill_053'] = {'inputs': ['rst_basefill_053'], 'func': rst_base_universe_d2_053_rst_basefill_053}


def rst_base_universe_d2_054_rst_basefill_054(rst_basefill_054):
    return _base_universe_d2(rst_basefill_054, 54)
RST_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['rst_base_universe_d2_054_rst_basefill_054'] = {'inputs': ['rst_basefill_054'], 'func': rst_base_universe_d2_054_rst_basefill_054}


def rst_base_universe_d2_055_rst_basefill_055(rst_basefill_055):
    return _base_universe_d2(rst_basefill_055, 55)
RST_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['rst_base_universe_d2_055_rst_basefill_055'] = {'inputs': ['rst_basefill_055'], 'func': rst_base_universe_d2_055_rst_basefill_055}


def rst_base_universe_d2_056_rst_basefill_056(rst_basefill_056):
    return _base_universe_d2(rst_basefill_056, 56)
RST_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['rst_base_universe_d2_056_rst_basefill_056'] = {'inputs': ['rst_basefill_056'], 'func': rst_base_universe_d2_056_rst_basefill_056}


def rst_base_universe_d2_057_rst_basefill_057(rst_basefill_057):
    return _base_universe_d2(rst_basefill_057, 57)
RST_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['rst_base_universe_d2_057_rst_basefill_057'] = {'inputs': ['rst_basefill_057'], 'func': rst_base_universe_d2_057_rst_basefill_057}


def rst_base_universe_d2_058_rst_basefill_058(rst_basefill_058):
    return _base_universe_d2(rst_basefill_058, 58)
RST_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['rst_base_universe_d2_058_rst_basefill_058'] = {'inputs': ['rst_basefill_058'], 'func': rst_base_universe_d2_058_rst_basefill_058}


def rst_base_universe_d2_059_rst_basefill_059(rst_basefill_059):
    return _base_universe_d2(rst_basefill_059, 59)
RST_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['rst_base_universe_d2_059_rst_basefill_059'] = {'inputs': ['rst_basefill_059'], 'func': rst_base_universe_d2_059_rst_basefill_059}


def rst_base_universe_d2_060_rst_basefill_060(rst_basefill_060):
    return _base_universe_d2(rst_basefill_060, 60)
RST_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['rst_base_universe_d2_060_rst_basefill_060'] = {'inputs': ['rst_basefill_060'], 'func': rst_base_universe_d2_060_rst_basefill_060}


def rst_base_universe_d2_061_rst_basefill_061(rst_basefill_061):
    return _base_universe_d2(rst_basefill_061, 61)
RST_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['rst_base_universe_d2_061_rst_basefill_061'] = {'inputs': ['rst_basefill_061'], 'func': rst_base_universe_d2_061_rst_basefill_061}


def rst_base_universe_d2_062_rst_basefill_062(rst_basefill_062):
    return _base_universe_d2(rst_basefill_062, 62)
RST_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['rst_base_universe_d2_062_rst_basefill_062'] = {'inputs': ['rst_basefill_062'], 'func': rst_base_universe_d2_062_rst_basefill_062}


def rst_base_universe_d2_063_rst_basefill_063(rst_basefill_063):
    return _base_universe_d2(rst_basefill_063, 63)
RST_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['rst_base_universe_d2_063_rst_basefill_063'] = {'inputs': ['rst_basefill_063'], 'func': rst_base_universe_d2_063_rst_basefill_063}


def rst_base_universe_d2_064_rst_basefill_064(rst_basefill_064):
    return _base_universe_d2(rst_basefill_064, 64)
RST_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['rst_base_universe_d2_064_rst_basefill_064'] = {'inputs': ['rst_basefill_064'], 'func': rst_base_universe_d2_064_rst_basefill_064}


def rst_base_universe_d2_065_rst_basefill_065(rst_basefill_065):
    return _base_universe_d2(rst_basefill_065, 65)
RST_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['rst_base_universe_d2_065_rst_basefill_065'] = {'inputs': ['rst_basefill_065'], 'func': rst_base_universe_d2_065_rst_basefill_065}


def rst_base_universe_d2_066_rst_basefill_066(rst_basefill_066):
    return _base_universe_d2(rst_basefill_066, 66)
RST_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['rst_base_universe_d2_066_rst_basefill_066'] = {'inputs': ['rst_basefill_066'], 'func': rst_base_universe_d2_066_rst_basefill_066}


def rst_base_universe_d2_067_rst_basefill_067(rst_basefill_067):
    return _base_universe_d2(rst_basefill_067, 67)
RST_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['rst_base_universe_d2_067_rst_basefill_067'] = {'inputs': ['rst_basefill_067'], 'func': rst_base_universe_d2_067_rst_basefill_067}


def rst_base_universe_d2_068_rst_basefill_068(rst_basefill_068):
    return _base_universe_d2(rst_basefill_068, 68)
RST_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['rst_base_universe_d2_068_rst_basefill_068'] = {'inputs': ['rst_basefill_068'], 'func': rst_base_universe_d2_068_rst_basefill_068}


def rst_base_universe_d2_069_rst_basefill_069(rst_basefill_069):
    return _base_universe_d2(rst_basefill_069, 69)
RST_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['rst_base_universe_d2_069_rst_basefill_069'] = {'inputs': ['rst_basefill_069'], 'func': rst_base_universe_d2_069_rst_basefill_069}


def rst_base_universe_d2_070_rst_basefill_070(rst_basefill_070):
    return _base_universe_d2(rst_basefill_070, 70)
RST_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['rst_base_universe_d2_070_rst_basefill_070'] = {'inputs': ['rst_basefill_070'], 'func': rst_base_universe_d2_070_rst_basefill_070}


def rst_base_universe_d2_071_rst_basefill_071(rst_basefill_071):
    return _base_universe_d2(rst_basefill_071, 71)
RST_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['rst_base_universe_d2_071_rst_basefill_071'] = {'inputs': ['rst_basefill_071'], 'func': rst_base_universe_d2_071_rst_basefill_071}


def rst_base_universe_d2_072_rst_basefill_072(rst_basefill_072):
    return _base_universe_d2(rst_basefill_072, 72)
RST_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['rst_base_universe_d2_072_rst_basefill_072'] = {'inputs': ['rst_basefill_072'], 'func': rst_base_universe_d2_072_rst_basefill_072}


def rst_base_universe_d2_073_rst_basefill_073(rst_basefill_073):
    return _base_universe_d2(rst_basefill_073, 73)
RST_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['rst_base_universe_d2_073_rst_basefill_073'] = {'inputs': ['rst_basefill_073'], 'func': rst_base_universe_d2_073_rst_basefill_073}


def rst_base_universe_d2_074_rst_basefill_074(rst_basefill_074):
    return _base_universe_d2(rst_basefill_074, 74)
RST_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['rst_base_universe_d2_074_rst_basefill_074'] = {'inputs': ['rst_basefill_074'], 'func': rst_base_universe_d2_074_rst_basefill_074}


def rst_base_universe_d2_075_rst_basefill_075(rst_basefill_075):
    return _base_universe_d2(rst_basefill_075, 75)
RST_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['rst_base_universe_d2_075_rst_basefill_075'] = {'inputs': ['rst_basefill_075'], 'func': rst_base_universe_d2_075_rst_basefill_075}
