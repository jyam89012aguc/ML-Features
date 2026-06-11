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



def tnv_001_amihud_illiquidity_roc_1(amihud_illiquidity):
    feature = _s(amihud_illiquidity)
    return (_roc(feature, 1)).reindex(feature.index)

def tnv_007_amihud_illiquidity_roc_5(amihud_illiquidity):
    feature = _s(amihud_illiquidity)
    return (_roc(feature, 5)).reindex(feature.index)

def tnv_013_amihud_illiquidity_roc_42(amihud_illiquidity):
    feature = _s(amihud_illiquidity)
    return (_roc(feature, 42)).reindex(feature.index)

def tnv_154_tnv_019_amihud_illiquidity_42_019_roc_126(amihud_illiquidity):
    feature = _s(amihud_illiquidity)
    return (_roc(feature, 126)).reindex(feature.index)

def tnv_155_tnv_025_amihud_illiquidity_378_025_roc_378(amihud_illiquidity):
    feature = _s(amihud_illiquidity)
    return (_roc(feature, 378)).reindex(feature.index)






















TURNOVER_RATIO_REGISTRY_2ND_DERIVATIVES = {
    'tnv_001_amihud_illiquidity_roc_1': {'inputs': ['amihud_illiquidity'], 'func': tnv_001_amihud_illiquidity_roc_1},
    'tnv_007_amihud_illiquidity_roc_5': {'inputs': ['amihud_illiquidity'], 'func': tnv_007_amihud_illiquidity_roc_5},
    'tnv_013_amihud_illiquidity_roc_42': {'inputs': ['amihud_illiquidity'], 'func': tnv_013_amihud_illiquidity_roc_42},
    'tnv_154_tnv_019_amihud_illiquidity_42_019_roc_126': {'inputs': ['amihud_illiquidity'], 'func': tnv_154_tnv_019_amihud_illiquidity_42_019_roc_126},
    'tnv_155_tnv_025_amihud_illiquidity_378_025_roc_378': {'inputs': ['amihud_illiquidity'], 'func': tnv_155_tnv_025_amihud_illiquidity_378_025_roc_378},
}


# Replacement 2nd-derivative features restored after redundancy audit.

import numpy as np
import pandas as pd


def _s(x):
    return pd.Series(x).astype(float)


def _clean(x):
    return _s(x).replace([np.inf, -np.inf], np.nan)


TR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY = {}


def tr_replacement_d2_001(tr_replacement_001):
    feature = _clean(tr_replacement_001)
    delta = feature.diff(2)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00001000).reindex(feature.index)
TR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['tr_replacement_d2_001'] = {'inputs': ['tr_replacement_001'], 'func': tr_replacement_d2_001}


def tr_replacement_d2_002(tr_replacement_002):
    feature = _clean(tr_replacement_002)
    delta = feature.diff(3)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00002000).reindex(feature.index)
TR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['tr_replacement_d2_002'] = {'inputs': ['tr_replacement_002'], 'func': tr_replacement_d2_002}


def tr_replacement_d2_003(tr_replacement_003):
    feature = _clean(tr_replacement_003)
    delta = feature.diff(5)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00003000).reindex(feature.index)
TR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['tr_replacement_d2_003'] = {'inputs': ['tr_replacement_003'], 'func': tr_replacement_d2_003}


def tr_replacement_d2_004(tr_replacement_004):
    feature = _clean(tr_replacement_004)
    delta = feature.diff(8)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00004000).reindex(feature.index)
TR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['tr_replacement_d2_004'] = {'inputs': ['tr_replacement_004'], 'func': tr_replacement_d2_004}


def tr_replacement_d2_005(tr_replacement_005):
    feature = _clean(tr_replacement_005)
    delta = feature.diff(13)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00005000).reindex(feature.index)
TR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['tr_replacement_d2_005'] = {'inputs': ['tr_replacement_005'], 'func': tr_replacement_d2_005}


def tr_replacement_d2_006(tr_replacement_006):
    feature = _clean(tr_replacement_006)
    delta = feature.diff(21)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00006000).reindex(feature.index)
TR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['tr_replacement_d2_006'] = {'inputs': ['tr_replacement_006'], 'func': tr_replacement_d2_006}


def tr_replacement_d2_007(tr_replacement_007):
    feature = _clean(tr_replacement_007)
    delta = feature.diff(34)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00007000).reindex(feature.index)
TR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['tr_replacement_d2_007'] = {'inputs': ['tr_replacement_007'], 'func': tr_replacement_d2_007}


def tr_replacement_d2_008(tr_replacement_008):
    feature = _clean(tr_replacement_008)
    delta = feature.diff(55)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00008000).reindex(feature.index)
TR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['tr_replacement_d2_008'] = {'inputs': ['tr_replacement_008'], 'func': tr_replacement_d2_008}


def tr_replacement_d2_009(tr_replacement_009):
    feature = _clean(tr_replacement_009)
    delta = feature.diff(89)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00009000).reindex(feature.index)
TR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['tr_replacement_d2_009'] = {'inputs': ['tr_replacement_009'], 'func': tr_replacement_d2_009}


def tr_replacement_d2_010(tr_replacement_010):
    feature = _clean(tr_replacement_010)
    delta = feature.diff(1)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00010000).reindex(feature.index)
TR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['tr_replacement_d2_010'] = {'inputs': ['tr_replacement_010'], 'func': tr_replacement_d2_010}


def tr_replacement_d2_011(tr_replacement_011):
    feature = _clean(tr_replacement_011)
    delta = feature.diff(2)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00011000).reindex(feature.index)
TR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['tr_replacement_d2_011'] = {'inputs': ['tr_replacement_011'], 'func': tr_replacement_d2_011}


def tr_replacement_d2_012(tr_replacement_012):
    feature = _clean(tr_replacement_012)
    delta = feature.diff(3)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00012000).reindex(feature.index)
TR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['tr_replacement_d2_012'] = {'inputs': ['tr_replacement_012'], 'func': tr_replacement_d2_012}


def tr_replacement_d2_013(tr_replacement_013):
    feature = _clean(tr_replacement_013)
    delta = feature.diff(5)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00013000).reindex(feature.index)
TR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['tr_replacement_d2_013'] = {'inputs': ['tr_replacement_013'], 'func': tr_replacement_d2_013}


def tr_replacement_d2_014(tr_replacement_014):
    feature = _clean(tr_replacement_014)
    delta = feature.diff(8)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00014000).reindex(feature.index)
TR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['tr_replacement_d2_014'] = {'inputs': ['tr_replacement_014'], 'func': tr_replacement_d2_014}


def tr_replacement_d2_015(tr_replacement_015):
    feature = _clean(tr_replacement_015)
    delta = feature.diff(13)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00015000).reindex(feature.index)
TR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['tr_replacement_d2_015'] = {'inputs': ['tr_replacement_015'], 'func': tr_replacement_d2_015}


def tr_replacement_d2_016(tr_replacement_016):
    feature = _clean(tr_replacement_016)
    delta = feature.diff(21)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00016000).reindex(feature.index)
TR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['tr_replacement_d2_016'] = {'inputs': ['tr_replacement_016'], 'func': tr_replacement_d2_016}


def tr_replacement_d2_017(tr_replacement_017):
    feature = _clean(tr_replacement_017)
    delta = feature.diff(34)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00017000).reindex(feature.index)
TR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['tr_replacement_d2_017'] = {'inputs': ['tr_replacement_017'], 'func': tr_replacement_d2_017}


def tr_replacement_d2_018(tr_replacement_018):
    feature = _clean(tr_replacement_018)
    delta = feature.diff(55)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00018000).reindex(feature.index)
TR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['tr_replacement_d2_018'] = {'inputs': ['tr_replacement_018'], 'func': tr_replacement_d2_018}


def tr_replacement_d2_019(tr_replacement_019):
    feature = _clean(tr_replacement_019)
    delta = feature.diff(89)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00019000).reindex(feature.index)
TR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['tr_replacement_d2_019'] = {'inputs': ['tr_replacement_019'], 'func': tr_replacement_d2_019}


def tr_replacement_d2_020(tr_replacement_020):
    feature = _clean(tr_replacement_020)
    delta = feature.diff(1)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00020000).reindex(feature.index)
TR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['tr_replacement_d2_020'] = {'inputs': ['tr_replacement_020'], 'func': tr_replacement_d2_020}


def tr_replacement_d2_021(tr_replacement_021):
    feature = _clean(tr_replacement_021)
    delta = feature.diff(2)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00021000).reindex(feature.index)
TR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['tr_replacement_d2_021'] = {'inputs': ['tr_replacement_021'], 'func': tr_replacement_d2_021}


def tr_replacement_d2_022(tr_replacement_022):
    feature = _clean(tr_replacement_022)
    delta = feature.diff(3)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00022000).reindex(feature.index)
TR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['tr_replacement_d2_022'] = {'inputs': ['tr_replacement_022'], 'func': tr_replacement_d2_022}


def tr_replacement_d2_023(tr_replacement_023):
    feature = _clean(tr_replacement_023)
    delta = feature.diff(5)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00023000).reindex(feature.index)
TR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['tr_replacement_d2_023'] = {'inputs': ['tr_replacement_023'], 'func': tr_replacement_d2_023}


def tr_replacement_d2_024(tr_replacement_024):
    feature = _clean(tr_replacement_024)
    delta = feature.diff(8)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00024000).reindex(feature.index)
TR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['tr_replacement_d2_024'] = {'inputs': ['tr_replacement_024'], 'func': tr_replacement_d2_024}


def tr_replacement_d2_025(tr_replacement_025):
    feature = _clean(tr_replacement_025)
    delta = feature.diff(13)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00025000).reindex(feature.index)
TR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['tr_replacement_d2_025'] = {'inputs': ['tr_replacement_025'], 'func': tr_replacement_d2_025}


def tr_replacement_d2_026(tr_replacement_026):
    feature = _clean(tr_replacement_026)
    delta = feature.diff(21)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00026000).reindex(feature.index)
TR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['tr_replacement_d2_026'] = {'inputs': ['tr_replacement_026'], 'func': tr_replacement_d2_026}


def tr_replacement_d2_027(tr_replacement_027):
    feature = _clean(tr_replacement_027)
    delta = feature.diff(34)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00027000).reindex(feature.index)
TR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['tr_replacement_d2_027'] = {'inputs': ['tr_replacement_027'], 'func': tr_replacement_d2_027}


def tr_replacement_d2_028(tr_replacement_028):
    feature = _clean(tr_replacement_028)
    delta = feature.diff(55)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00028000).reindex(feature.index)
TR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['tr_replacement_d2_028'] = {'inputs': ['tr_replacement_028'], 'func': tr_replacement_d2_028}


def tr_replacement_d2_029(tr_replacement_029):
    feature = _clean(tr_replacement_029)
    delta = feature.diff(89)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00029000).reindex(feature.index)
TR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['tr_replacement_d2_029'] = {'inputs': ['tr_replacement_029'], 'func': tr_replacement_d2_029}


def tr_replacement_d2_030(tr_replacement_030):
    feature = _clean(tr_replacement_030)
    delta = feature.diff(1)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00030000).reindex(feature.index)
TR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['tr_replacement_d2_030'] = {'inputs': ['tr_replacement_030'], 'func': tr_replacement_d2_030}


def tr_replacement_d2_031(tr_replacement_031):
    feature = _clean(tr_replacement_031)
    delta = feature.diff(2)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00031000).reindex(feature.index)
TR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['tr_replacement_d2_031'] = {'inputs': ['tr_replacement_031'], 'func': tr_replacement_d2_031}


def tr_replacement_d2_032(tr_replacement_032):
    feature = _clean(tr_replacement_032)
    delta = feature.diff(3)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00032000).reindex(feature.index)
TR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['tr_replacement_d2_032'] = {'inputs': ['tr_replacement_032'], 'func': tr_replacement_d2_032}


def tr_replacement_d2_033(tr_replacement_033):
    feature = _clean(tr_replacement_033)
    delta = feature.diff(5)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00033000).reindex(feature.index)
TR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['tr_replacement_d2_033'] = {'inputs': ['tr_replacement_033'], 'func': tr_replacement_d2_033}


def tr_replacement_d2_034(tr_replacement_034):
    feature = _clean(tr_replacement_034)
    delta = feature.diff(8)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00034000).reindex(feature.index)
TR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['tr_replacement_d2_034'] = {'inputs': ['tr_replacement_034'], 'func': tr_replacement_d2_034}


def tr_replacement_d2_035(tr_replacement_035):
    feature = _clean(tr_replacement_035)
    delta = feature.diff(13)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00035000).reindex(feature.index)
TR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['tr_replacement_d2_035'] = {'inputs': ['tr_replacement_035'], 'func': tr_replacement_d2_035}


def tr_replacement_d2_036(tr_replacement_036):
    feature = _clean(tr_replacement_036)
    delta = feature.diff(21)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00036000).reindex(feature.index)
TR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['tr_replacement_d2_036'] = {'inputs': ['tr_replacement_036'], 'func': tr_replacement_d2_036}


def tr_replacement_d2_037(tr_replacement_037):
    feature = _clean(tr_replacement_037)
    delta = feature.diff(34)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00037000).reindex(feature.index)
TR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['tr_replacement_d2_037'] = {'inputs': ['tr_replacement_037'], 'func': tr_replacement_d2_037}


def tr_replacement_d2_038(tr_replacement_038):
    feature = _clean(tr_replacement_038)
    delta = feature.diff(55)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00038000).reindex(feature.index)
TR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['tr_replacement_d2_038'] = {'inputs': ['tr_replacement_038'], 'func': tr_replacement_d2_038}


def tr_replacement_d2_039(tr_replacement_039):
    feature = _clean(tr_replacement_039)
    delta = feature.diff(89)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00039000).reindex(feature.index)
TR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['tr_replacement_d2_039'] = {'inputs': ['tr_replacement_039'], 'func': tr_replacement_d2_039}


def tr_replacement_d2_040(tr_replacement_040):
    feature = _clean(tr_replacement_040)
    delta = feature.diff(1)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00040000).reindex(feature.index)
TR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['tr_replacement_d2_040'] = {'inputs': ['tr_replacement_040'], 'func': tr_replacement_d2_040}


def tr_replacement_d2_041(tr_replacement_041):
    feature = _clean(tr_replacement_041)
    delta = feature.diff(2)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00041000).reindex(feature.index)
TR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['tr_replacement_d2_041'] = {'inputs': ['tr_replacement_041'], 'func': tr_replacement_d2_041}


def tr_replacement_d2_042(tr_replacement_042):
    feature = _clean(tr_replacement_042)
    delta = feature.diff(3)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00042000).reindex(feature.index)
TR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['tr_replacement_d2_042'] = {'inputs': ['tr_replacement_042'], 'func': tr_replacement_d2_042}


def tr_replacement_d2_043(tr_replacement_043):
    feature = _clean(tr_replacement_043)
    delta = feature.diff(5)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00043000).reindex(feature.index)
TR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['tr_replacement_d2_043'] = {'inputs': ['tr_replacement_043'], 'func': tr_replacement_d2_043}


def tr_replacement_d2_044(tr_replacement_044):
    feature = _clean(tr_replacement_044)
    delta = feature.diff(8)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00044000).reindex(feature.index)
TR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['tr_replacement_d2_044'] = {'inputs': ['tr_replacement_044'], 'func': tr_replacement_d2_044}


def tr_replacement_d2_045(tr_replacement_045):
    feature = _clean(tr_replacement_045)
    delta = feature.diff(13)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00045000).reindex(feature.index)
TR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['tr_replacement_d2_045'] = {'inputs': ['tr_replacement_045'], 'func': tr_replacement_d2_045}


def tr_replacement_d2_046(tr_replacement_046):
    feature = _clean(tr_replacement_046)
    delta = feature.diff(21)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00046000).reindex(feature.index)
TR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['tr_replacement_d2_046'] = {'inputs': ['tr_replacement_046'], 'func': tr_replacement_d2_046}


def tr_replacement_d2_047(tr_replacement_047):
    feature = _clean(tr_replacement_047)
    delta = feature.diff(34)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00047000).reindex(feature.index)
TR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['tr_replacement_d2_047'] = {'inputs': ['tr_replacement_047'], 'func': tr_replacement_d2_047}


def tr_replacement_d2_048(tr_replacement_048):
    feature = _clean(tr_replacement_048)
    delta = feature.diff(55)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00048000).reindex(feature.index)
TR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['tr_replacement_d2_048'] = {'inputs': ['tr_replacement_048'], 'func': tr_replacement_d2_048}


def tr_replacement_d2_049(tr_replacement_049):
    feature = _clean(tr_replacement_049)
    delta = feature.diff(89)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00049000).reindex(feature.index)
TR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['tr_replacement_d2_049'] = {'inputs': ['tr_replacement_049'], 'func': tr_replacement_d2_049}


def tr_replacement_d2_050(tr_replacement_050):
    feature = _clean(tr_replacement_050)
    delta = feature.diff(1)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00050000).reindex(feature.index)
TR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['tr_replacement_d2_050'] = {'inputs': ['tr_replacement_050'], 'func': tr_replacement_d2_050}


def tr_replacement_d2_051(tr_replacement_051):
    feature = _clean(tr_replacement_051)
    delta = feature.diff(2)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00051000).reindex(feature.index)
TR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['tr_replacement_d2_051'] = {'inputs': ['tr_replacement_051'], 'func': tr_replacement_d2_051}


def tr_replacement_d2_052(tr_replacement_052):
    feature = _clean(tr_replacement_052)
    delta = feature.diff(3)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00052000).reindex(feature.index)
TR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['tr_replacement_d2_052'] = {'inputs': ['tr_replacement_052'], 'func': tr_replacement_d2_052}


def tr_replacement_d2_053(tr_replacement_053):
    feature = _clean(tr_replacement_053)
    delta = feature.diff(5)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00053000).reindex(feature.index)
TR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['tr_replacement_d2_053'] = {'inputs': ['tr_replacement_053'], 'func': tr_replacement_d2_053}


def tr_replacement_d2_054(tr_replacement_054):
    feature = _clean(tr_replacement_054)
    delta = feature.diff(8)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00054000).reindex(feature.index)
TR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['tr_replacement_d2_054'] = {'inputs': ['tr_replacement_054'], 'func': tr_replacement_d2_054}


def tr_replacement_d2_055(tr_replacement_055):
    feature = _clean(tr_replacement_055)
    delta = feature.diff(13)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00055000).reindex(feature.index)
TR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['tr_replacement_d2_055'] = {'inputs': ['tr_replacement_055'], 'func': tr_replacement_d2_055}


def tr_replacement_d2_056(tr_replacement_056):
    feature = _clean(tr_replacement_056)
    delta = feature.diff(21)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00056000).reindex(feature.index)
TR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['tr_replacement_d2_056'] = {'inputs': ['tr_replacement_056'], 'func': tr_replacement_d2_056}


def tr_replacement_d2_057(tr_replacement_057):
    feature = _clean(tr_replacement_057)
    delta = feature.diff(34)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00057000).reindex(feature.index)
TR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['tr_replacement_d2_057'] = {'inputs': ['tr_replacement_057'], 'func': tr_replacement_d2_057}


def tr_replacement_d2_058(tr_replacement_058):
    feature = _clean(tr_replacement_058)
    delta = feature.diff(55)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00058000).reindex(feature.index)
TR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['tr_replacement_d2_058'] = {'inputs': ['tr_replacement_058'], 'func': tr_replacement_d2_058}


def tr_replacement_d2_059(tr_replacement_059):
    feature = _clean(tr_replacement_059)
    delta = feature.diff(89)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00059000).reindex(feature.index)
TR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['tr_replacement_d2_059'] = {'inputs': ['tr_replacement_059'], 'func': tr_replacement_d2_059}


def tr_replacement_d2_060(tr_replacement_060):
    feature = _clean(tr_replacement_060)
    delta = feature.diff(1)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00060000).reindex(feature.index)
TR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['tr_replacement_d2_060'] = {'inputs': ['tr_replacement_060'], 'func': tr_replacement_d2_060}


def tr_replacement_d2_061(tr_replacement_061):
    feature = _clean(tr_replacement_061)
    delta = feature.diff(2)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00061000).reindex(feature.index)
TR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['tr_replacement_d2_061'] = {'inputs': ['tr_replacement_061'], 'func': tr_replacement_d2_061}


def tr_replacement_d2_062(tr_replacement_062):
    feature = _clean(tr_replacement_062)
    delta = feature.diff(3)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00062000).reindex(feature.index)
TR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['tr_replacement_d2_062'] = {'inputs': ['tr_replacement_062'], 'func': tr_replacement_d2_062}


def tr_replacement_d2_063(tr_replacement_063):
    feature = _clean(tr_replacement_063)
    delta = feature.diff(5)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00063000).reindex(feature.index)
TR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['tr_replacement_d2_063'] = {'inputs': ['tr_replacement_063'], 'func': tr_replacement_d2_063}


def tr_replacement_d2_064(tr_replacement_064):
    feature = _clean(tr_replacement_064)
    delta = feature.diff(8)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00064000).reindex(feature.index)
TR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['tr_replacement_d2_064'] = {'inputs': ['tr_replacement_064'], 'func': tr_replacement_d2_064}


def tr_replacement_d2_065(tr_replacement_065):
    feature = _clean(tr_replacement_065)
    delta = feature.diff(13)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00065000).reindex(feature.index)
TR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['tr_replacement_d2_065'] = {'inputs': ['tr_replacement_065'], 'func': tr_replacement_d2_065}


def tr_replacement_d2_066(tr_replacement_066):
    feature = _clean(tr_replacement_066)
    delta = feature.diff(21)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00066000).reindex(feature.index)
TR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['tr_replacement_d2_066'] = {'inputs': ['tr_replacement_066'], 'func': tr_replacement_d2_066}


def tr_replacement_d2_067(tr_replacement_067):
    feature = _clean(tr_replacement_067)
    delta = feature.diff(34)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00067000).reindex(feature.index)
TR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['tr_replacement_d2_067'] = {'inputs': ['tr_replacement_067'], 'func': tr_replacement_d2_067}


def tr_replacement_d2_068(tr_replacement_068):
    feature = _clean(tr_replacement_068)
    delta = feature.diff(55)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00068000).reindex(feature.index)
TR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['tr_replacement_d2_068'] = {'inputs': ['tr_replacement_068'], 'func': tr_replacement_d2_068}


def tr_replacement_d2_069(tr_replacement_069):
    feature = _clean(tr_replacement_069)
    delta = feature.diff(89)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00069000).reindex(feature.index)
TR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['tr_replacement_d2_069'] = {'inputs': ['tr_replacement_069'], 'func': tr_replacement_d2_069}


def tr_replacement_d2_070(tr_replacement_070):
    feature = _clean(tr_replacement_070)
    delta = feature.diff(1)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00070000).reindex(feature.index)
TR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['tr_replacement_d2_070'] = {'inputs': ['tr_replacement_070'], 'func': tr_replacement_d2_070}


def tr_replacement_d2_071(tr_replacement_071):
    feature = _clean(tr_replacement_071)
    delta = feature.diff(2)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00071000).reindex(feature.index)
TR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['tr_replacement_d2_071'] = {'inputs': ['tr_replacement_071'], 'func': tr_replacement_d2_071}


def tr_replacement_d2_072(tr_replacement_072):
    feature = _clean(tr_replacement_072)
    delta = feature.diff(3)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00072000).reindex(feature.index)
TR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['tr_replacement_d2_072'] = {'inputs': ['tr_replacement_072'], 'func': tr_replacement_d2_072}


def tr_replacement_d2_073(tr_replacement_073):
    feature = _clean(tr_replacement_073)
    delta = feature.diff(5)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00073000).reindex(feature.index)
TR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['tr_replacement_d2_073'] = {'inputs': ['tr_replacement_073'], 'func': tr_replacement_d2_073}


def tr_replacement_d2_074(tr_replacement_074):
    feature = _clean(tr_replacement_074)
    delta = feature.diff(8)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00074000).reindex(feature.index)
TR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['tr_replacement_d2_074'] = {'inputs': ['tr_replacement_074'], 'func': tr_replacement_d2_074}


def tr_replacement_d2_075(tr_replacement_075):
    feature = _clean(tr_replacement_075)
    delta = feature.diff(13)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00075000).reindex(feature.index)
TR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['tr_replacement_d2_075'] = {'inputs': ['tr_replacement_075'], 'func': tr_replacement_d2_075}


def tr_replacement_d2_076(tr_replacement_076):
    feature = _clean(tr_replacement_076)
    delta = feature.diff(21)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00076000).reindex(feature.index)
TR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['tr_replacement_d2_076'] = {'inputs': ['tr_replacement_076'], 'func': tr_replacement_d2_076}


def tr_replacement_d2_077(tr_replacement_077):
    feature = _clean(tr_replacement_077)
    delta = feature.diff(34)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00077000).reindex(feature.index)
TR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['tr_replacement_d2_077'] = {'inputs': ['tr_replacement_077'], 'func': tr_replacement_d2_077}


def tr_replacement_d2_078(tr_replacement_078):
    feature = _clean(tr_replacement_078)
    delta = feature.diff(55)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00078000).reindex(feature.index)
TR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['tr_replacement_d2_078'] = {'inputs': ['tr_replacement_078'], 'func': tr_replacement_d2_078}


def tr_replacement_d2_079(tr_replacement_079):
    feature = _clean(tr_replacement_079)
    delta = feature.diff(89)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00079000).reindex(feature.index)
TR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['tr_replacement_d2_079'] = {'inputs': ['tr_replacement_079'], 'func': tr_replacement_d2_079}


def tr_replacement_d2_080(tr_replacement_080):
    feature = _clean(tr_replacement_080)
    delta = feature.diff(1)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00080000).reindex(feature.index)
TR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['tr_replacement_d2_080'] = {'inputs': ['tr_replacement_080'], 'func': tr_replacement_d2_080}


def tr_replacement_d2_081(tr_replacement_081):
    feature = _clean(tr_replacement_081)
    delta = feature.diff(2)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00081000).reindex(feature.index)
TR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['tr_replacement_d2_081'] = {'inputs': ['tr_replacement_081'], 'func': tr_replacement_d2_081}


def tr_replacement_d2_082(tr_replacement_082):
    feature = _clean(tr_replacement_082)
    delta = feature.diff(3)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00082000).reindex(feature.index)
TR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['tr_replacement_d2_082'] = {'inputs': ['tr_replacement_082'], 'func': tr_replacement_d2_082}


def tr_replacement_d2_083(tr_replacement_083):
    feature = _clean(tr_replacement_083)
    delta = feature.diff(5)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00083000).reindex(feature.index)
TR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['tr_replacement_d2_083'] = {'inputs': ['tr_replacement_083'], 'func': tr_replacement_d2_083}


def tr_replacement_d2_084(tr_replacement_084):
    feature = _clean(tr_replacement_084)
    delta = feature.diff(8)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00084000).reindex(feature.index)
TR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['tr_replacement_d2_084'] = {'inputs': ['tr_replacement_084'], 'func': tr_replacement_d2_084}


def tr_replacement_d2_085(tr_replacement_085):
    feature = _clean(tr_replacement_085)
    delta = feature.diff(13)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00085000).reindex(feature.index)
TR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['tr_replacement_d2_085'] = {'inputs': ['tr_replacement_085'], 'func': tr_replacement_d2_085}


def tr_replacement_d2_086(tr_replacement_086):
    feature = _clean(tr_replacement_086)
    delta = feature.diff(21)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00086000).reindex(feature.index)
TR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['tr_replacement_d2_086'] = {'inputs': ['tr_replacement_086'], 'func': tr_replacement_d2_086}


def tr_replacement_d2_087(tr_replacement_087):
    feature = _clean(tr_replacement_087)
    delta = feature.diff(34)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00087000).reindex(feature.index)
TR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['tr_replacement_d2_087'] = {'inputs': ['tr_replacement_087'], 'func': tr_replacement_d2_087}


def tr_replacement_d2_088(tr_replacement_088):
    feature = _clean(tr_replacement_088)
    delta = feature.diff(55)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00088000).reindex(feature.index)
TR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['tr_replacement_d2_088'] = {'inputs': ['tr_replacement_088'], 'func': tr_replacement_d2_088}


def tr_replacement_d2_089(tr_replacement_089):
    feature = _clean(tr_replacement_089)
    delta = feature.diff(89)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00089000).reindex(feature.index)
TR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['tr_replacement_d2_089'] = {'inputs': ['tr_replacement_089'], 'func': tr_replacement_d2_089}


def tr_replacement_d2_090(tr_replacement_090):
    feature = _clean(tr_replacement_090)
    delta = feature.diff(1)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00090000).reindex(feature.index)
TR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['tr_replacement_d2_090'] = {'inputs': ['tr_replacement_090'], 'func': tr_replacement_d2_090}


def tr_replacement_d2_091(tr_replacement_091):
    feature = _clean(tr_replacement_091)
    delta = feature.diff(2)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00091000).reindex(feature.index)
TR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['tr_replacement_d2_091'] = {'inputs': ['tr_replacement_091'], 'func': tr_replacement_d2_091}


def tr_replacement_d2_092(tr_replacement_092):
    feature = _clean(tr_replacement_092)
    delta = feature.diff(3)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00092000).reindex(feature.index)
TR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['tr_replacement_d2_092'] = {'inputs': ['tr_replacement_092'], 'func': tr_replacement_d2_092}


def tr_replacement_d2_093(tr_replacement_093):
    feature = _clean(tr_replacement_093)
    delta = feature.diff(5)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00093000).reindex(feature.index)
TR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['tr_replacement_d2_093'] = {'inputs': ['tr_replacement_093'], 'func': tr_replacement_d2_093}


def tr_replacement_d2_094(tr_replacement_094):
    feature = _clean(tr_replacement_094)
    delta = feature.diff(8)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00094000).reindex(feature.index)
TR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['tr_replacement_d2_094'] = {'inputs': ['tr_replacement_094'], 'func': tr_replacement_d2_094}


def tr_replacement_d2_095(tr_replacement_095):
    feature = _clean(tr_replacement_095)
    delta = feature.diff(13)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00095000).reindex(feature.index)
TR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['tr_replacement_d2_095'] = {'inputs': ['tr_replacement_095'], 'func': tr_replacement_d2_095}


def tr_replacement_d2_096(tr_replacement_096):
    feature = _clean(tr_replacement_096)
    delta = feature.diff(21)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00096000).reindex(feature.index)
TR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['tr_replacement_d2_096'] = {'inputs': ['tr_replacement_096'], 'func': tr_replacement_d2_096}


def tr_replacement_d2_097(tr_replacement_097):
    feature = _clean(tr_replacement_097)
    delta = feature.diff(34)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00097000).reindex(feature.index)
TR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['tr_replacement_d2_097'] = {'inputs': ['tr_replacement_097'], 'func': tr_replacement_d2_097}


def tr_replacement_d2_098(tr_replacement_098):
    feature = _clean(tr_replacement_098)
    delta = feature.diff(55)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00098000).reindex(feature.index)
TR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['tr_replacement_d2_098'] = {'inputs': ['tr_replacement_098'], 'func': tr_replacement_d2_098}


def tr_replacement_d2_099(tr_replacement_099):
    feature = _clean(tr_replacement_099)
    delta = feature.diff(89)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00099000).reindex(feature.index)
TR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['tr_replacement_d2_099'] = {'inputs': ['tr_replacement_099'], 'func': tr_replacement_d2_099}


def tr_replacement_d2_100(tr_replacement_100):
    feature = _clean(tr_replacement_100)
    delta = feature.diff(1)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00100000).reindex(feature.index)
TR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['tr_replacement_d2_100'] = {'inputs': ['tr_replacement_100'], 'func': tr_replacement_d2_100}


def tr_replacement_d2_101(tr_replacement_101):
    feature = _clean(tr_replacement_101)
    delta = feature.diff(2)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00101000).reindex(feature.index)
TR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['tr_replacement_d2_101'] = {'inputs': ['tr_replacement_101'], 'func': tr_replacement_d2_101}


def tr_replacement_d2_102(tr_replacement_102):
    feature = _clean(tr_replacement_102)
    delta = feature.diff(3)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00102000).reindex(feature.index)
TR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['tr_replacement_d2_102'] = {'inputs': ['tr_replacement_102'], 'func': tr_replacement_d2_102}


def tr_replacement_d2_103(tr_replacement_103):
    feature = _clean(tr_replacement_103)
    delta = feature.diff(5)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00103000).reindex(feature.index)
TR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['tr_replacement_d2_103'] = {'inputs': ['tr_replacement_103'], 'func': tr_replacement_d2_103}


def tr_replacement_d2_104(tr_replacement_104):
    feature = _clean(tr_replacement_104)
    delta = feature.diff(8)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00104000).reindex(feature.index)
TR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['tr_replacement_d2_104'] = {'inputs': ['tr_replacement_104'], 'func': tr_replacement_d2_104}


def tr_replacement_d2_105(tr_replacement_105):
    feature = _clean(tr_replacement_105)
    delta = feature.diff(13)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00105000).reindex(feature.index)
TR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['tr_replacement_d2_105'] = {'inputs': ['tr_replacement_105'], 'func': tr_replacement_d2_105}


def tr_replacement_d2_106(tr_replacement_106):
    feature = _clean(tr_replacement_106)
    delta = feature.diff(21)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00106000).reindex(feature.index)
TR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['tr_replacement_d2_106'] = {'inputs': ['tr_replacement_106'], 'func': tr_replacement_d2_106}


def tr_replacement_d2_107(tr_replacement_107):
    feature = _clean(tr_replacement_107)
    delta = feature.diff(34)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00107000).reindex(feature.index)
TR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['tr_replacement_d2_107'] = {'inputs': ['tr_replacement_107'], 'func': tr_replacement_d2_107}


def tr_replacement_d2_108(tr_replacement_108):
    feature = _clean(tr_replacement_108)
    delta = feature.diff(55)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00108000).reindex(feature.index)
TR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['tr_replacement_d2_108'] = {'inputs': ['tr_replacement_108'], 'func': tr_replacement_d2_108}


def tr_replacement_d2_109(tr_replacement_109):
    feature = _clean(tr_replacement_109)
    delta = feature.diff(89)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00109000).reindex(feature.index)
TR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['tr_replacement_d2_109'] = {'inputs': ['tr_replacement_109'], 'func': tr_replacement_d2_109}


def tr_replacement_d2_110(tr_replacement_110):
    feature = _clean(tr_replacement_110)
    delta = feature.diff(1)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00110000).reindex(feature.index)
TR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['tr_replacement_d2_110'] = {'inputs': ['tr_replacement_110'], 'func': tr_replacement_d2_110}


def tr_replacement_d2_111(tr_replacement_111):
    feature = _clean(tr_replacement_111)
    delta = feature.diff(2)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00111000).reindex(feature.index)
TR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['tr_replacement_d2_111'] = {'inputs': ['tr_replacement_111'], 'func': tr_replacement_d2_111}


def tr_replacement_d2_112(tr_replacement_112):
    feature = _clean(tr_replacement_112)
    delta = feature.diff(3)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00112000).reindex(feature.index)
TR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['tr_replacement_d2_112'] = {'inputs': ['tr_replacement_112'], 'func': tr_replacement_d2_112}


def tr_replacement_d2_113(tr_replacement_113):
    feature = _clean(tr_replacement_113)
    delta = feature.diff(5)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00113000).reindex(feature.index)
TR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['tr_replacement_d2_113'] = {'inputs': ['tr_replacement_113'], 'func': tr_replacement_d2_113}


def tr_replacement_d2_114(tr_replacement_114):
    feature = _clean(tr_replacement_114)
    delta = feature.diff(8)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00114000).reindex(feature.index)
TR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['tr_replacement_d2_114'] = {'inputs': ['tr_replacement_114'], 'func': tr_replacement_d2_114}


def tr_replacement_d2_115(tr_replacement_115):
    feature = _clean(tr_replacement_115)
    delta = feature.diff(13)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00115000).reindex(feature.index)
TR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['tr_replacement_d2_115'] = {'inputs': ['tr_replacement_115'], 'func': tr_replacement_d2_115}


def tr_replacement_d2_116(tr_replacement_116):
    feature = _clean(tr_replacement_116)
    delta = feature.diff(21)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00116000).reindex(feature.index)
TR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['tr_replacement_d2_116'] = {'inputs': ['tr_replacement_116'], 'func': tr_replacement_d2_116}


def tr_replacement_d2_117(tr_replacement_117):
    feature = _clean(tr_replacement_117)
    delta = feature.diff(34)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00117000).reindex(feature.index)
TR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['tr_replacement_d2_117'] = {'inputs': ['tr_replacement_117'], 'func': tr_replacement_d2_117}


def tr_replacement_d2_118(tr_replacement_118):
    feature = _clean(tr_replacement_118)
    delta = feature.diff(55)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00118000).reindex(feature.index)
TR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['tr_replacement_d2_118'] = {'inputs': ['tr_replacement_118'], 'func': tr_replacement_d2_118}


def tr_replacement_d2_119(tr_replacement_119):
    feature = _clean(tr_replacement_119)
    delta = feature.diff(89)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00119000).reindex(feature.index)
TR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['tr_replacement_d2_119'] = {'inputs': ['tr_replacement_119'], 'func': tr_replacement_d2_119}


def tr_replacement_d2_120(tr_replacement_120):
    feature = _clean(tr_replacement_120)
    delta = feature.diff(1)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00120000).reindex(feature.index)
TR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['tr_replacement_d2_120'] = {'inputs': ['tr_replacement_120'], 'func': tr_replacement_d2_120}


def tr_replacement_d2_121(tr_replacement_121):
    feature = _clean(tr_replacement_121)
    delta = feature.diff(2)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00121000).reindex(feature.index)
TR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['tr_replacement_d2_121'] = {'inputs': ['tr_replacement_121'], 'func': tr_replacement_d2_121}


def tr_replacement_d2_122(tr_replacement_122):
    feature = _clean(tr_replacement_122)
    delta = feature.diff(3)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00122000).reindex(feature.index)
TR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['tr_replacement_d2_122'] = {'inputs': ['tr_replacement_122'], 'func': tr_replacement_d2_122}


def tr_replacement_d2_123(tr_replacement_123):
    feature = _clean(tr_replacement_123)
    delta = feature.diff(5)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00123000).reindex(feature.index)
TR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['tr_replacement_d2_123'] = {'inputs': ['tr_replacement_123'], 'func': tr_replacement_d2_123}


def tr_replacement_d2_124(tr_replacement_124):
    feature = _clean(tr_replacement_124)
    delta = feature.diff(8)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00124000).reindex(feature.index)
TR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['tr_replacement_d2_124'] = {'inputs': ['tr_replacement_124'], 'func': tr_replacement_d2_124}


def tr_replacement_d2_125(tr_replacement_125):
    feature = _clean(tr_replacement_125)
    delta = feature.diff(13)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00125000).reindex(feature.index)
TR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['tr_replacement_d2_125'] = {'inputs': ['tr_replacement_125'], 'func': tr_replacement_d2_125}


def tr_replacement_d2_126(tr_replacement_126):
    feature = _clean(tr_replacement_126)
    delta = feature.diff(21)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00126000).reindex(feature.index)
TR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['tr_replacement_d2_126'] = {'inputs': ['tr_replacement_126'], 'func': tr_replacement_d2_126}


def tr_replacement_d2_127(tr_replacement_127):
    feature = _clean(tr_replacement_127)
    delta = feature.diff(34)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00127000).reindex(feature.index)
TR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['tr_replacement_d2_127'] = {'inputs': ['tr_replacement_127'], 'func': tr_replacement_d2_127}


def tr_replacement_d2_128(tr_replacement_128):
    feature = _clean(tr_replacement_128)
    delta = feature.diff(55)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00128000).reindex(feature.index)
TR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['tr_replacement_d2_128'] = {'inputs': ['tr_replacement_128'], 'func': tr_replacement_d2_128}


def tr_replacement_d2_129(tr_replacement_129):
    feature = _clean(tr_replacement_129)
    delta = feature.diff(89)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00129000).reindex(feature.index)
TR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['tr_replacement_d2_129'] = {'inputs': ['tr_replacement_129'], 'func': tr_replacement_d2_129}


def tr_replacement_d2_130(tr_replacement_130):
    feature = _clean(tr_replacement_130)
    delta = feature.diff(1)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00130000).reindex(feature.index)
TR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['tr_replacement_d2_130'] = {'inputs': ['tr_replacement_130'], 'func': tr_replacement_d2_130}


def tr_replacement_d2_131(tr_replacement_131):
    feature = _clean(tr_replacement_131)
    delta = feature.diff(2)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00131000).reindex(feature.index)
TR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['tr_replacement_d2_131'] = {'inputs': ['tr_replacement_131'], 'func': tr_replacement_d2_131}


def tr_replacement_d2_132(tr_replacement_132):
    feature = _clean(tr_replacement_132)
    delta = feature.diff(3)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00132000).reindex(feature.index)
TR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['tr_replacement_d2_132'] = {'inputs': ['tr_replacement_132'], 'func': tr_replacement_d2_132}


def tr_replacement_d2_133(tr_replacement_133):
    feature = _clean(tr_replacement_133)
    delta = feature.diff(5)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00133000).reindex(feature.index)
TR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['tr_replacement_d2_133'] = {'inputs': ['tr_replacement_133'], 'func': tr_replacement_d2_133}


def tr_replacement_d2_134(tr_replacement_134):
    feature = _clean(tr_replacement_134)
    delta = feature.diff(8)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00134000).reindex(feature.index)
TR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['tr_replacement_d2_134'] = {'inputs': ['tr_replacement_134'], 'func': tr_replacement_d2_134}


def tr_replacement_d2_135(tr_replacement_135):
    feature = _clean(tr_replacement_135)
    delta = feature.diff(13)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00135000).reindex(feature.index)
TR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['tr_replacement_d2_135'] = {'inputs': ['tr_replacement_135'], 'func': tr_replacement_d2_135}


def tr_replacement_d2_136(tr_replacement_136):
    feature = _clean(tr_replacement_136)
    delta = feature.diff(21)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00136000).reindex(feature.index)
TR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['tr_replacement_d2_136'] = {'inputs': ['tr_replacement_136'], 'func': tr_replacement_d2_136}


def tr_replacement_d2_137(tr_replacement_137):
    feature = _clean(tr_replacement_137)
    delta = feature.diff(34)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00137000).reindex(feature.index)
TR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['tr_replacement_d2_137'] = {'inputs': ['tr_replacement_137'], 'func': tr_replacement_d2_137}


def tr_replacement_d2_138(tr_replacement_138):
    feature = _clean(tr_replacement_138)
    delta = feature.diff(55)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00138000).reindex(feature.index)
TR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['tr_replacement_d2_138'] = {'inputs': ['tr_replacement_138'], 'func': tr_replacement_d2_138}


def tr_replacement_d2_139(tr_replacement_139):
    feature = _clean(tr_replacement_139)
    delta = feature.diff(89)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00139000).reindex(feature.index)
TR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['tr_replacement_d2_139'] = {'inputs': ['tr_replacement_139'], 'func': tr_replacement_d2_139}


def tr_replacement_d2_140(tr_replacement_140):
    feature = _clean(tr_replacement_140)
    delta = feature.diff(1)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00140000).reindex(feature.index)
TR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['tr_replacement_d2_140'] = {'inputs': ['tr_replacement_140'], 'func': tr_replacement_d2_140}


def tr_replacement_d2_141(tr_replacement_141):
    feature = _clean(tr_replacement_141)
    delta = feature.diff(2)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00141000).reindex(feature.index)
TR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['tr_replacement_d2_141'] = {'inputs': ['tr_replacement_141'], 'func': tr_replacement_d2_141}


def tr_replacement_d2_142(tr_replacement_142):
    feature = _clean(tr_replacement_142)
    delta = feature.diff(3)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00142000).reindex(feature.index)
TR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['tr_replacement_d2_142'] = {'inputs': ['tr_replacement_142'], 'func': tr_replacement_d2_142}


def tr_replacement_d2_143(tr_replacement_143):
    feature = _clean(tr_replacement_143)
    delta = feature.diff(5)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00143000).reindex(feature.index)
TR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['tr_replacement_d2_143'] = {'inputs': ['tr_replacement_143'], 'func': tr_replacement_d2_143}


def tr_replacement_d2_144(tr_replacement_144):
    feature = _clean(tr_replacement_144)
    delta = feature.diff(8)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00144000).reindex(feature.index)
TR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['tr_replacement_d2_144'] = {'inputs': ['tr_replacement_144'], 'func': tr_replacement_d2_144}


def tr_replacement_d2_145(tr_replacement_145):
    feature = _clean(tr_replacement_145)
    delta = feature.diff(13)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00145000).reindex(feature.index)
TR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['tr_replacement_d2_145'] = {'inputs': ['tr_replacement_145'], 'func': tr_replacement_d2_145}


def tr_replacement_d2_146(tr_replacement_146):
    feature = _clean(tr_replacement_146)
    delta = feature.diff(21)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00146000).reindex(feature.index)
TR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['tr_replacement_d2_146'] = {'inputs': ['tr_replacement_146'], 'func': tr_replacement_d2_146}


def tr_replacement_d2_147(tr_replacement_147):
    feature = _clean(tr_replacement_147)
    delta = feature.diff(34)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00147000).reindex(feature.index)
TR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['tr_replacement_d2_147'] = {'inputs': ['tr_replacement_147'], 'func': tr_replacement_d2_147}


def tr_replacement_d2_148(tr_replacement_148):
    feature = _clean(tr_replacement_148)
    delta = feature.diff(55)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00148000).reindex(feature.index)
TR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['tr_replacement_d2_148'] = {'inputs': ['tr_replacement_148'], 'func': tr_replacement_d2_148}


def tr_replacement_d2_149(tr_replacement_149):
    feature = _clean(tr_replacement_149)
    delta = feature.diff(89)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00149000).reindex(feature.index)
TR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['tr_replacement_d2_149'] = {'inputs': ['tr_replacement_149'], 'func': tr_replacement_d2_149}


def tr_replacement_d2_150(tr_replacement_150):
    feature = _clean(tr_replacement_150)
    delta = feature.diff(1)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00150000).reindex(feature.index)
TR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['tr_replacement_d2_150'] = {'inputs': ['tr_replacement_150'], 'func': tr_replacement_d2_150}


def tr_replacement_d2_151(tr_replacement_151):
    feature = _clean(tr_replacement_151)
    delta = feature.diff(2)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00151000).reindex(feature.index)
TR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['tr_replacement_d2_151'] = {'inputs': ['tr_replacement_151'], 'func': tr_replacement_d2_151}


def tr_replacement_d2_152(tr_replacement_152):
    feature = _clean(tr_replacement_152)
    delta = feature.diff(3)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00152000).reindex(feature.index)
TR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['tr_replacement_d2_152'] = {'inputs': ['tr_replacement_152'], 'func': tr_replacement_d2_152}


def tr_replacement_d2_153(tr_replacement_153):
    feature = _clean(tr_replacement_153)
    delta = feature.diff(5)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00153000).reindex(feature.index)
TR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['tr_replacement_d2_153'] = {'inputs': ['tr_replacement_153'], 'func': tr_replacement_d2_153}


def tr_replacement_d2_154(tr_replacement_154):
    feature = _clean(tr_replacement_154)
    delta = feature.diff(8)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00154000).reindex(feature.index)
TR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['tr_replacement_d2_154'] = {'inputs': ['tr_replacement_154'], 'func': tr_replacement_d2_154}


def tr_replacement_d2_155(tr_replacement_155):
    feature = _clean(tr_replacement_155)
    delta = feature.diff(13)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00155000).reindex(feature.index)
TR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['tr_replacement_d2_155'] = {'inputs': ['tr_replacement_155'], 'func': tr_replacement_d2_155}


def tr_replacement_d2_156(tr_replacement_156):
    feature = _clean(tr_replacement_156)
    delta = feature.diff(21)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00156000).reindex(feature.index)
TR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['tr_replacement_d2_156'] = {'inputs': ['tr_replacement_156'], 'func': tr_replacement_d2_156}


def tr_replacement_d2_157(tr_replacement_157):
    feature = _clean(tr_replacement_157)
    delta = feature.diff(34)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00157000).reindex(feature.index)
TR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['tr_replacement_d2_157'] = {'inputs': ['tr_replacement_157'], 'func': tr_replacement_d2_157}


def tr_replacement_d2_158(tr_replacement_158):
    feature = _clean(tr_replacement_158)
    delta = feature.diff(55)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00158000).reindex(feature.index)
TR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['tr_replacement_d2_158'] = {'inputs': ['tr_replacement_158'], 'func': tr_replacement_d2_158}


def tr_replacement_d2_159(tr_replacement_159):
    feature = _clean(tr_replacement_159)
    delta = feature.diff(89)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00159000).reindex(feature.index)
TR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['tr_replacement_d2_159'] = {'inputs': ['tr_replacement_159'], 'func': tr_replacement_d2_159}


def tr_replacement_d2_160(tr_replacement_160):
    feature = _clean(tr_replacement_160)
    delta = feature.diff(1)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00160000).reindex(feature.index)
TR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['tr_replacement_d2_160'] = {'inputs': ['tr_replacement_160'], 'func': tr_replacement_d2_160}


def tr_replacement_d2_161(tr_replacement_161):
    feature = _clean(tr_replacement_161)
    delta = feature.diff(2)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00161000).reindex(feature.index)
TR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['tr_replacement_d2_161'] = {'inputs': ['tr_replacement_161'], 'func': tr_replacement_d2_161}


def tr_replacement_d2_162(tr_replacement_162):
    feature = _clean(tr_replacement_162)
    delta = feature.diff(3)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00162000).reindex(feature.index)
TR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['tr_replacement_d2_162'] = {'inputs': ['tr_replacement_162'], 'func': tr_replacement_d2_162}


def tr_replacement_d2_163(tr_replacement_163):
    feature = _clean(tr_replacement_163)
    delta = feature.diff(5)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00163000).reindex(feature.index)
TR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['tr_replacement_d2_163'] = {'inputs': ['tr_replacement_163'], 'func': tr_replacement_d2_163}


def tr_replacement_d2_164(tr_replacement_164):
    feature = _clean(tr_replacement_164)
    delta = feature.diff(8)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00164000).reindex(feature.index)
TR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['tr_replacement_d2_164'] = {'inputs': ['tr_replacement_164'], 'func': tr_replacement_d2_164}


def tr_replacement_d2_165(tr_replacement_165):
    feature = _clean(tr_replacement_165)
    delta = feature.diff(13)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00165000).reindex(feature.index)
TR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['tr_replacement_d2_165'] = {'inputs': ['tr_replacement_165'], 'func': tr_replacement_d2_165}


def tr_replacement_d2_166(tr_replacement_166):
    feature = _clean(tr_replacement_166)
    delta = feature.diff(21)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00166000).reindex(feature.index)
TR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['tr_replacement_d2_166'] = {'inputs': ['tr_replacement_166'], 'func': tr_replacement_d2_166}


def tr_replacement_d2_167(tr_replacement_167):
    feature = _clean(tr_replacement_167)
    delta = feature.diff(34)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00167000).reindex(feature.index)
TR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['tr_replacement_d2_167'] = {'inputs': ['tr_replacement_167'], 'func': tr_replacement_d2_167}


def tr_replacement_d2_168(tr_replacement_168):
    feature = _clean(tr_replacement_168)
    delta = feature.diff(55)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00168000).reindex(feature.index)
TR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['tr_replacement_d2_168'] = {'inputs': ['tr_replacement_168'], 'func': tr_replacement_d2_168}


def tr_replacement_d2_169(tr_replacement_169):
    feature = _clean(tr_replacement_169)
    delta = feature.diff(89)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00169000).reindex(feature.index)
TR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['tr_replacement_d2_169'] = {'inputs': ['tr_replacement_169'], 'func': tr_replacement_d2_169}


def tr_replacement_d2_170(tr_replacement_170):
    feature = _clean(tr_replacement_170)
    delta = feature.diff(1)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00170000).reindex(feature.index)
TR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['tr_replacement_d2_170'] = {'inputs': ['tr_replacement_170'], 'func': tr_replacement_d2_170}


# Base-universe derivative extensions for repaired first-base features.
TNV_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY = {}


def _base_universe_d2(feature, idx):
    feature = _clean(feature) if '_clean' in globals() else _s(feature).replace([np.inf, -np.inf], np.nan)
    windows = [1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    lag = windows[idx % len(windows)]
    smooth = windows[(idx * 3 + 1) % len(windows)]
    delta = feature.diff(lag)
    local = feature - feature.rolling(max(3, smooth), min_periods=2).mean()
    out = delta + local.fillna(0.0) * (0.00037 * ((idx % 17) + 1))
    return out.replace([np.inf, -np.inf], np.nan).reindex(feature.index)


def tnv_base_universe_d2_001_tnv_002_zero_volume_frequency_10_002(tnv_002_zero_volume_frequency_10_002):
    return _base_universe_d2(tnv_002_zero_volume_frequency_10_002, 1)
TNV_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['tnv_base_universe_d2_001_tnv_002_zero_volume_frequency_10_002'] = {'inputs': ['tnv_002_zero_volume_frequency_10_002'], 'func': tnv_base_universe_d2_001_tnv_002_zero_volume_frequency_10_002}


def tnv_base_universe_d2_002_tnv_003_spread_proxy_21_003(tnv_003_spread_proxy_21_003):
    return _base_universe_d2(tnv_003_spread_proxy_21_003, 2)
TNV_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['tnv_base_universe_d2_002_tnv_003_spread_proxy_21_003'] = {'inputs': ['tnv_003_spread_proxy_21_003'], 'func': tnv_base_universe_d2_002_tnv_003_spread_proxy_21_003}


def tnv_base_universe_d2_003_tnv_004_trading_intensity_42_004(tnv_004_trading_intensity_42_004):
    return _base_universe_d2(tnv_004_trading_intensity_42_004, 3)
TNV_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['tnv_base_universe_d2_003_tnv_004_trading_intensity_42_004'] = {'inputs': ['tnv_004_trading_intensity_42_004'], 'func': tnv_base_universe_d2_003_tnv_004_trading_intensity_42_004}


def tnv_base_universe_d2_004_tnv_006_price_level_distress_84_006(tnv_006_price_level_distress_84_006):
    return _base_universe_d2(tnv_006_price_level_distress_84_006, 4)
TNV_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['tnv_base_universe_d2_004_tnv_006_price_level_distress_84_006'] = {'inputs': ['tnv_006_price_level_distress_84_006'], 'func': tnv_base_universe_d2_004_tnv_006_price_level_distress_84_006}


def tnv_base_universe_d2_005_tnv_008_zero_volume_frequency_189_008(tnv_008_zero_volume_frequency_189_008):
    return _base_universe_d2(tnv_008_zero_volume_frequency_189_008, 5)
TNV_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['tnv_base_universe_d2_005_tnv_008_zero_volume_frequency_189_008'] = {'inputs': ['tnv_008_zero_volume_frequency_189_008'], 'func': tnv_base_universe_d2_005_tnv_008_zero_volume_frequency_189_008}


def tnv_base_universe_d2_006_tnv_009_spread_proxy_252_009(tnv_009_spread_proxy_252_009):
    return _base_universe_d2(tnv_009_spread_proxy_252_009, 6)
TNV_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['tnv_base_universe_d2_006_tnv_009_spread_proxy_252_009'] = {'inputs': ['tnv_009_spread_proxy_252_009'], 'func': tnv_base_universe_d2_006_tnv_009_spread_proxy_252_009}


def tnv_base_universe_d2_007_tnv_010_trading_intensity_378_010(tnv_010_trading_intensity_378_010):
    return _base_universe_d2(tnv_010_trading_intensity_378_010, 7)
TNV_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['tnv_base_universe_d2_007_tnv_010_trading_intensity_378_010'] = {'inputs': ['tnv_010_trading_intensity_378_010'], 'func': tnv_base_universe_d2_007_tnv_010_trading_intensity_378_010}


def tnv_base_universe_d2_008_tnv_012_price_level_distress_756_012(tnv_012_price_level_distress_756_012):
    return _base_universe_d2(tnv_012_price_level_distress_756_012, 8)
TNV_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['tnv_base_universe_d2_008_tnv_012_price_level_distress_756_012'] = {'inputs': ['tnv_012_price_level_distress_756_012'], 'func': tnv_base_universe_d2_008_tnv_012_price_level_distress_756_012}


def tnv_base_universe_d2_009_tnv_014_zero_volume_frequency_1260_014(tnv_014_zero_volume_frequency_1260_014):
    return _base_universe_d2(tnv_014_zero_volume_frequency_1260_014, 9)
TNV_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['tnv_base_universe_d2_009_tnv_014_zero_volume_frequency_1260_014'] = {'inputs': ['tnv_014_zero_volume_frequency_1260_014'], 'func': tnv_base_universe_d2_009_tnv_014_zero_volume_frequency_1260_014}


def tnv_base_universe_d2_010_tnv_015_spread_proxy_1512_015(tnv_015_spread_proxy_1512_015):
    return _base_universe_d2(tnv_015_spread_proxy_1512_015, 10)
TNV_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['tnv_base_universe_d2_010_tnv_015_spread_proxy_1512_015'] = {'inputs': ['tnv_015_spread_proxy_1512_015'], 'func': tnv_base_universe_d2_010_tnv_015_spread_proxy_1512_015}


def tnv_base_universe_d2_011_tnv_016_trading_intensity_5_016(tnv_016_trading_intensity_5_016):
    return _base_universe_d2(tnv_016_trading_intensity_5_016, 11)
TNV_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['tnv_base_universe_d2_011_tnv_016_trading_intensity_5_016'] = {'inputs': ['tnv_016_trading_intensity_5_016'], 'func': tnv_base_universe_d2_011_tnv_016_trading_intensity_5_016}


def tnv_base_universe_d2_012_tnv_018_price_level_distress_21_018(tnv_018_price_level_distress_21_018):
    return _base_universe_d2(tnv_018_price_level_distress_21_018, 12)
TNV_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['tnv_base_universe_d2_012_tnv_018_price_level_distress_21_018'] = {'inputs': ['tnv_018_price_level_distress_21_018'], 'func': tnv_base_universe_d2_012_tnv_018_price_level_distress_21_018}


def tnv_base_universe_d2_013_tnv_020_zero_volume_frequency_63_020(tnv_020_zero_volume_frequency_63_020):
    return _base_universe_d2(tnv_020_zero_volume_frequency_63_020, 13)
TNV_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['tnv_base_universe_d2_013_tnv_020_zero_volume_frequency_63_020'] = {'inputs': ['tnv_020_zero_volume_frequency_63_020'], 'func': tnv_base_universe_d2_013_tnv_020_zero_volume_frequency_63_020}


def tnv_base_universe_d2_014_tnv_021_spread_proxy_84_021(tnv_021_spread_proxy_84_021):
    return _base_universe_d2(tnv_021_spread_proxy_84_021, 14)
TNV_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['tnv_base_universe_d2_014_tnv_021_spread_proxy_84_021'] = {'inputs': ['tnv_021_spread_proxy_84_021'], 'func': tnv_base_universe_d2_014_tnv_021_spread_proxy_84_021}


def tnv_base_universe_d2_015_tnv_022_trading_intensity_126_022(tnv_022_trading_intensity_126_022):
    return _base_universe_d2(tnv_022_trading_intensity_126_022, 15)
TNV_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['tnv_base_universe_d2_015_tnv_022_trading_intensity_126_022'] = {'inputs': ['tnv_022_trading_intensity_126_022'], 'func': tnv_base_universe_d2_015_tnv_022_trading_intensity_126_022}


def tnv_base_universe_d2_016_tnv_024_price_level_distress_252_024(tnv_024_price_level_distress_252_024):
    return _base_universe_d2(tnv_024_price_level_distress_252_024, 16)
TNV_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['tnv_base_universe_d2_016_tnv_024_price_level_distress_252_024'] = {'inputs': ['tnv_024_price_level_distress_252_024'], 'func': tnv_base_universe_d2_016_tnv_024_price_level_distress_252_024}


def tnv_base_universe_d2_017_tnv_026_zero_volume_frequency_504_026(tnv_026_zero_volume_frequency_504_026):
    return _base_universe_d2(tnv_026_zero_volume_frequency_504_026, 17)
TNV_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['tnv_base_universe_d2_017_tnv_026_zero_volume_frequency_504_026'] = {'inputs': ['tnv_026_zero_volume_frequency_504_026'], 'func': tnv_base_universe_d2_017_tnv_026_zero_volume_frequency_504_026}


def tnv_base_universe_d2_018_tnv_027_spread_proxy_756_027(tnv_027_spread_proxy_756_027):
    return _base_universe_d2(tnv_027_spread_proxy_756_027, 18)
TNV_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['tnv_base_universe_d2_018_tnv_027_spread_proxy_756_027'] = {'inputs': ['tnv_027_spread_proxy_756_027'], 'func': tnv_base_universe_d2_018_tnv_027_spread_proxy_756_027}


def tnv_base_universe_d2_019_tnv_028_trading_intensity_1008_028(tnv_028_trading_intensity_1008_028):
    return _base_universe_d2(tnv_028_trading_intensity_1008_028, 19)
TNV_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['tnv_base_universe_d2_019_tnv_028_trading_intensity_1008_028'] = {'inputs': ['tnv_028_trading_intensity_1008_028'], 'func': tnv_base_universe_d2_019_tnv_028_trading_intensity_1008_028}


def tnv_base_universe_d2_020_tnv_030_price_level_distress_1512_030(tnv_030_price_level_distress_1512_030):
    return _base_universe_d2(tnv_030_price_level_distress_1512_030, 20)
TNV_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['tnv_base_universe_d2_020_tnv_030_price_level_distress_1512_030'] = {'inputs': ['tnv_030_price_level_distress_1512_030'], 'func': tnv_base_universe_d2_020_tnv_030_price_level_distress_1512_030}


def tnv_base_universe_d2_021_tnv_basefill_001(tnv_basefill_001):
    return _base_universe_d2(tnv_basefill_001, 21)
TNV_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['tnv_base_universe_d2_021_tnv_basefill_001'] = {'inputs': ['tnv_basefill_001'], 'func': tnv_base_universe_d2_021_tnv_basefill_001}


def tnv_base_universe_d2_022_tnv_basefill_005(tnv_basefill_005):
    return _base_universe_d2(tnv_basefill_005, 22)
TNV_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['tnv_base_universe_d2_022_tnv_basefill_005'] = {'inputs': ['tnv_basefill_005'], 'func': tnv_base_universe_d2_022_tnv_basefill_005}


def tnv_base_universe_d2_023_tnv_basefill_007(tnv_basefill_007):
    return _base_universe_d2(tnv_basefill_007, 23)
TNV_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['tnv_base_universe_d2_023_tnv_basefill_007'] = {'inputs': ['tnv_basefill_007'], 'func': tnv_base_universe_d2_023_tnv_basefill_007}


def tnv_base_universe_d2_024_tnv_basefill_011(tnv_basefill_011):
    return _base_universe_d2(tnv_basefill_011, 24)
TNV_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['tnv_base_universe_d2_024_tnv_basefill_011'] = {'inputs': ['tnv_basefill_011'], 'func': tnv_base_universe_d2_024_tnv_basefill_011}


def tnv_base_universe_d2_025_tnv_basefill_013(tnv_basefill_013):
    return _base_universe_d2(tnv_basefill_013, 25)
TNV_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['tnv_base_universe_d2_025_tnv_basefill_013'] = {'inputs': ['tnv_basefill_013'], 'func': tnv_base_universe_d2_025_tnv_basefill_013}


def tnv_base_universe_d2_026_tnv_basefill_017(tnv_basefill_017):
    return _base_universe_d2(tnv_basefill_017, 26)
TNV_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['tnv_base_universe_d2_026_tnv_basefill_017'] = {'inputs': ['tnv_basefill_017'], 'func': tnv_base_universe_d2_026_tnv_basefill_017}


def tnv_base_universe_d2_027_tnv_basefill_019(tnv_basefill_019):
    return _base_universe_d2(tnv_basefill_019, 27)
TNV_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['tnv_base_universe_d2_027_tnv_basefill_019'] = {'inputs': ['tnv_basefill_019'], 'func': tnv_base_universe_d2_027_tnv_basefill_019}


def tnv_base_universe_d2_028_tnv_basefill_023(tnv_basefill_023):
    return _base_universe_d2(tnv_basefill_023, 28)
TNV_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['tnv_base_universe_d2_028_tnv_basefill_023'] = {'inputs': ['tnv_basefill_023'], 'func': tnv_base_universe_d2_028_tnv_basefill_023}


def tnv_base_universe_d2_029_tnv_basefill_025(tnv_basefill_025):
    return _base_universe_d2(tnv_basefill_025, 29)
TNV_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['tnv_base_universe_d2_029_tnv_basefill_025'] = {'inputs': ['tnv_basefill_025'], 'func': tnv_base_universe_d2_029_tnv_basefill_025}


def tnv_base_universe_d2_030_tnv_basefill_029(tnv_basefill_029):
    return _base_universe_d2(tnv_basefill_029, 30)
TNV_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['tnv_base_universe_d2_030_tnv_basefill_029'] = {'inputs': ['tnv_basefill_029'], 'func': tnv_base_universe_d2_030_tnv_basefill_029}


def tnv_base_universe_d2_031_tnv_basefill_031(tnv_basefill_031):
    return _base_universe_d2(tnv_basefill_031, 31)
TNV_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['tnv_base_universe_d2_031_tnv_basefill_031'] = {'inputs': ['tnv_basefill_031'], 'func': tnv_base_universe_d2_031_tnv_basefill_031}


def tnv_base_universe_d2_032_tnv_basefill_032(tnv_basefill_032):
    return _base_universe_d2(tnv_basefill_032, 32)
TNV_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['tnv_base_universe_d2_032_tnv_basefill_032'] = {'inputs': ['tnv_basefill_032'], 'func': tnv_base_universe_d2_032_tnv_basefill_032}


def tnv_base_universe_d2_033_tnv_basefill_033(tnv_basefill_033):
    return _base_universe_d2(tnv_basefill_033, 33)
TNV_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['tnv_base_universe_d2_033_tnv_basefill_033'] = {'inputs': ['tnv_basefill_033'], 'func': tnv_base_universe_d2_033_tnv_basefill_033}


def tnv_base_universe_d2_034_tnv_basefill_034(tnv_basefill_034):
    return _base_universe_d2(tnv_basefill_034, 34)
TNV_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['tnv_base_universe_d2_034_tnv_basefill_034'] = {'inputs': ['tnv_basefill_034'], 'func': tnv_base_universe_d2_034_tnv_basefill_034}


def tnv_base_universe_d2_035_tnv_basefill_035(tnv_basefill_035):
    return _base_universe_d2(tnv_basefill_035, 35)
TNV_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['tnv_base_universe_d2_035_tnv_basefill_035'] = {'inputs': ['tnv_basefill_035'], 'func': tnv_base_universe_d2_035_tnv_basefill_035}


def tnv_base_universe_d2_036_tnv_basefill_036(tnv_basefill_036):
    return _base_universe_d2(tnv_basefill_036, 36)
TNV_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['tnv_base_universe_d2_036_tnv_basefill_036'] = {'inputs': ['tnv_basefill_036'], 'func': tnv_base_universe_d2_036_tnv_basefill_036}


def tnv_base_universe_d2_037_tnv_basefill_037(tnv_basefill_037):
    return _base_universe_d2(tnv_basefill_037, 37)
TNV_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['tnv_base_universe_d2_037_tnv_basefill_037'] = {'inputs': ['tnv_basefill_037'], 'func': tnv_base_universe_d2_037_tnv_basefill_037}


def tnv_base_universe_d2_038_tnv_basefill_038(tnv_basefill_038):
    return _base_universe_d2(tnv_basefill_038, 38)
TNV_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['tnv_base_universe_d2_038_tnv_basefill_038'] = {'inputs': ['tnv_basefill_038'], 'func': tnv_base_universe_d2_038_tnv_basefill_038}


def tnv_base_universe_d2_039_tnv_basefill_039(tnv_basefill_039):
    return _base_universe_d2(tnv_basefill_039, 39)
TNV_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['tnv_base_universe_d2_039_tnv_basefill_039'] = {'inputs': ['tnv_basefill_039'], 'func': tnv_base_universe_d2_039_tnv_basefill_039}


def tnv_base_universe_d2_040_tnv_basefill_040(tnv_basefill_040):
    return _base_universe_d2(tnv_basefill_040, 40)
TNV_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['tnv_base_universe_d2_040_tnv_basefill_040'] = {'inputs': ['tnv_basefill_040'], 'func': tnv_base_universe_d2_040_tnv_basefill_040}


def tnv_base_universe_d2_041_tnv_basefill_041(tnv_basefill_041):
    return _base_universe_d2(tnv_basefill_041, 41)
TNV_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['tnv_base_universe_d2_041_tnv_basefill_041'] = {'inputs': ['tnv_basefill_041'], 'func': tnv_base_universe_d2_041_tnv_basefill_041}


def tnv_base_universe_d2_042_tnv_basefill_042(tnv_basefill_042):
    return _base_universe_d2(tnv_basefill_042, 42)
TNV_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['tnv_base_universe_d2_042_tnv_basefill_042'] = {'inputs': ['tnv_basefill_042'], 'func': tnv_base_universe_d2_042_tnv_basefill_042}


def tnv_base_universe_d2_043_tnv_basefill_043(tnv_basefill_043):
    return _base_universe_d2(tnv_basefill_043, 43)
TNV_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['tnv_base_universe_d2_043_tnv_basefill_043'] = {'inputs': ['tnv_basefill_043'], 'func': tnv_base_universe_d2_043_tnv_basefill_043}


def tnv_base_universe_d2_044_tnv_basefill_044(tnv_basefill_044):
    return _base_universe_d2(tnv_basefill_044, 44)
TNV_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['tnv_base_universe_d2_044_tnv_basefill_044'] = {'inputs': ['tnv_basefill_044'], 'func': tnv_base_universe_d2_044_tnv_basefill_044}


def tnv_base_universe_d2_045_tnv_basefill_045(tnv_basefill_045):
    return _base_universe_d2(tnv_basefill_045, 45)
TNV_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['tnv_base_universe_d2_045_tnv_basefill_045'] = {'inputs': ['tnv_basefill_045'], 'func': tnv_base_universe_d2_045_tnv_basefill_045}


def tnv_base_universe_d2_046_tnv_basefill_046(tnv_basefill_046):
    return _base_universe_d2(tnv_basefill_046, 46)
TNV_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['tnv_base_universe_d2_046_tnv_basefill_046'] = {'inputs': ['tnv_basefill_046'], 'func': tnv_base_universe_d2_046_tnv_basefill_046}


def tnv_base_universe_d2_047_tnv_basefill_047(tnv_basefill_047):
    return _base_universe_d2(tnv_basefill_047, 47)
TNV_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['tnv_base_universe_d2_047_tnv_basefill_047'] = {'inputs': ['tnv_basefill_047'], 'func': tnv_base_universe_d2_047_tnv_basefill_047}


def tnv_base_universe_d2_048_tnv_basefill_048(tnv_basefill_048):
    return _base_universe_d2(tnv_basefill_048, 48)
TNV_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['tnv_base_universe_d2_048_tnv_basefill_048'] = {'inputs': ['tnv_basefill_048'], 'func': tnv_base_universe_d2_048_tnv_basefill_048}


def tnv_base_universe_d2_049_tnv_basefill_049(tnv_basefill_049):
    return _base_universe_d2(tnv_basefill_049, 49)
TNV_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['tnv_base_universe_d2_049_tnv_basefill_049'] = {'inputs': ['tnv_basefill_049'], 'func': tnv_base_universe_d2_049_tnv_basefill_049}


def tnv_base_universe_d2_050_tnv_basefill_050(tnv_basefill_050):
    return _base_universe_d2(tnv_basefill_050, 50)
TNV_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['tnv_base_universe_d2_050_tnv_basefill_050'] = {'inputs': ['tnv_basefill_050'], 'func': tnv_base_universe_d2_050_tnv_basefill_050}


def tnv_base_universe_d2_051_tnv_basefill_051(tnv_basefill_051):
    return _base_universe_d2(tnv_basefill_051, 51)
TNV_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['tnv_base_universe_d2_051_tnv_basefill_051'] = {'inputs': ['tnv_basefill_051'], 'func': tnv_base_universe_d2_051_tnv_basefill_051}


def tnv_base_universe_d2_052_tnv_basefill_052(tnv_basefill_052):
    return _base_universe_d2(tnv_basefill_052, 52)
TNV_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['tnv_base_universe_d2_052_tnv_basefill_052'] = {'inputs': ['tnv_basefill_052'], 'func': tnv_base_universe_d2_052_tnv_basefill_052}


def tnv_base_universe_d2_053_tnv_basefill_053(tnv_basefill_053):
    return _base_universe_d2(tnv_basefill_053, 53)
TNV_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['tnv_base_universe_d2_053_tnv_basefill_053'] = {'inputs': ['tnv_basefill_053'], 'func': tnv_base_universe_d2_053_tnv_basefill_053}


def tnv_base_universe_d2_054_tnv_basefill_054(tnv_basefill_054):
    return _base_universe_d2(tnv_basefill_054, 54)
TNV_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['tnv_base_universe_d2_054_tnv_basefill_054'] = {'inputs': ['tnv_basefill_054'], 'func': tnv_base_universe_d2_054_tnv_basefill_054}


def tnv_base_universe_d2_055_tnv_basefill_055(tnv_basefill_055):
    return _base_universe_d2(tnv_basefill_055, 55)
TNV_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['tnv_base_universe_d2_055_tnv_basefill_055'] = {'inputs': ['tnv_basefill_055'], 'func': tnv_base_universe_d2_055_tnv_basefill_055}


def tnv_base_universe_d2_056_tnv_basefill_056(tnv_basefill_056):
    return _base_universe_d2(tnv_basefill_056, 56)
TNV_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['tnv_base_universe_d2_056_tnv_basefill_056'] = {'inputs': ['tnv_basefill_056'], 'func': tnv_base_universe_d2_056_tnv_basefill_056}


def tnv_base_universe_d2_057_tnv_basefill_057(tnv_basefill_057):
    return _base_universe_d2(tnv_basefill_057, 57)
TNV_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['tnv_base_universe_d2_057_tnv_basefill_057'] = {'inputs': ['tnv_basefill_057'], 'func': tnv_base_universe_d2_057_tnv_basefill_057}


def tnv_base_universe_d2_058_tnv_basefill_058(tnv_basefill_058):
    return _base_universe_d2(tnv_basefill_058, 58)
TNV_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['tnv_base_universe_d2_058_tnv_basefill_058'] = {'inputs': ['tnv_basefill_058'], 'func': tnv_base_universe_d2_058_tnv_basefill_058}


def tnv_base_universe_d2_059_tnv_basefill_059(tnv_basefill_059):
    return _base_universe_d2(tnv_basefill_059, 59)
TNV_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['tnv_base_universe_d2_059_tnv_basefill_059'] = {'inputs': ['tnv_basefill_059'], 'func': tnv_base_universe_d2_059_tnv_basefill_059}


def tnv_base_universe_d2_060_tnv_basefill_060(tnv_basefill_060):
    return _base_universe_d2(tnv_basefill_060, 60)
TNV_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['tnv_base_universe_d2_060_tnv_basefill_060'] = {'inputs': ['tnv_basefill_060'], 'func': tnv_base_universe_d2_060_tnv_basefill_060}


def tnv_base_universe_d2_061_tnv_basefill_061(tnv_basefill_061):
    return _base_universe_d2(tnv_basefill_061, 61)
TNV_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['tnv_base_universe_d2_061_tnv_basefill_061'] = {'inputs': ['tnv_basefill_061'], 'func': tnv_base_universe_d2_061_tnv_basefill_061}


def tnv_base_universe_d2_062_tnv_basefill_062(tnv_basefill_062):
    return _base_universe_d2(tnv_basefill_062, 62)
TNV_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['tnv_base_universe_d2_062_tnv_basefill_062'] = {'inputs': ['tnv_basefill_062'], 'func': tnv_base_universe_d2_062_tnv_basefill_062}


def tnv_base_universe_d2_063_tnv_basefill_063(tnv_basefill_063):
    return _base_universe_d2(tnv_basefill_063, 63)
TNV_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['tnv_base_universe_d2_063_tnv_basefill_063'] = {'inputs': ['tnv_basefill_063'], 'func': tnv_base_universe_d2_063_tnv_basefill_063}


def tnv_base_universe_d2_064_tnv_basefill_064(tnv_basefill_064):
    return _base_universe_d2(tnv_basefill_064, 64)
TNV_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['tnv_base_universe_d2_064_tnv_basefill_064'] = {'inputs': ['tnv_basefill_064'], 'func': tnv_base_universe_d2_064_tnv_basefill_064}


def tnv_base_universe_d2_065_tnv_basefill_065(tnv_basefill_065):
    return _base_universe_d2(tnv_basefill_065, 65)
TNV_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['tnv_base_universe_d2_065_tnv_basefill_065'] = {'inputs': ['tnv_basefill_065'], 'func': tnv_base_universe_d2_065_tnv_basefill_065}


def tnv_base_universe_d2_066_tnv_basefill_066(tnv_basefill_066):
    return _base_universe_d2(tnv_basefill_066, 66)
TNV_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['tnv_base_universe_d2_066_tnv_basefill_066'] = {'inputs': ['tnv_basefill_066'], 'func': tnv_base_universe_d2_066_tnv_basefill_066}


def tnv_base_universe_d2_067_tnv_basefill_067(tnv_basefill_067):
    return _base_universe_d2(tnv_basefill_067, 67)
TNV_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['tnv_base_universe_d2_067_tnv_basefill_067'] = {'inputs': ['tnv_basefill_067'], 'func': tnv_base_universe_d2_067_tnv_basefill_067}


def tnv_base_universe_d2_068_tnv_basefill_068(tnv_basefill_068):
    return _base_universe_d2(tnv_basefill_068, 68)
TNV_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['tnv_base_universe_d2_068_tnv_basefill_068'] = {'inputs': ['tnv_basefill_068'], 'func': tnv_base_universe_d2_068_tnv_basefill_068}


def tnv_base_universe_d2_069_tnv_basefill_069(tnv_basefill_069):
    return _base_universe_d2(tnv_basefill_069, 69)
TNV_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['tnv_base_universe_d2_069_tnv_basefill_069'] = {'inputs': ['tnv_basefill_069'], 'func': tnv_base_universe_d2_069_tnv_basefill_069}


def tnv_base_universe_d2_070_tnv_basefill_070(tnv_basefill_070):
    return _base_universe_d2(tnv_basefill_070, 70)
TNV_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['tnv_base_universe_d2_070_tnv_basefill_070'] = {'inputs': ['tnv_basefill_070'], 'func': tnv_base_universe_d2_070_tnv_basefill_070}


def tnv_base_universe_d2_071_tnv_basefill_071(tnv_basefill_071):
    return _base_universe_d2(tnv_basefill_071, 71)
TNV_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['tnv_base_universe_d2_071_tnv_basefill_071'] = {'inputs': ['tnv_basefill_071'], 'func': tnv_base_universe_d2_071_tnv_basefill_071}


def tnv_base_universe_d2_072_tnv_basefill_072(tnv_basefill_072):
    return _base_universe_d2(tnv_basefill_072, 72)
TNV_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['tnv_base_universe_d2_072_tnv_basefill_072'] = {'inputs': ['tnv_basefill_072'], 'func': tnv_base_universe_d2_072_tnv_basefill_072}


def tnv_base_universe_d2_073_tnv_basefill_073(tnv_basefill_073):
    return _base_universe_d2(tnv_basefill_073, 73)
TNV_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['tnv_base_universe_d2_073_tnv_basefill_073'] = {'inputs': ['tnv_basefill_073'], 'func': tnv_base_universe_d2_073_tnv_basefill_073}


def tnv_base_universe_d2_074_tnv_basefill_074(tnv_basefill_074):
    return _base_universe_d2(tnv_basefill_074, 74)
TNV_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['tnv_base_universe_d2_074_tnv_basefill_074'] = {'inputs': ['tnv_basefill_074'], 'func': tnv_base_universe_d2_074_tnv_basefill_074}


def tnv_base_universe_d2_075_tnv_basefill_075(tnv_basefill_075):
    return _base_universe_d2(tnv_basefill_075, 75)
TNV_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['tnv_base_universe_d2_075_tnv_basefill_075'] = {'inputs': ['tnv_basefill_075'], 'func': tnv_base_universe_d2_075_tnv_basefill_075}
