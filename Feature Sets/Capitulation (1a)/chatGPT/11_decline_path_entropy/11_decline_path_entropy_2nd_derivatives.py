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



def dpe_001_amihud_illiquidity_roc_1(amihud_illiquidity):
    feature = _s(amihud_illiquidity)
    return (_roc(feature, 1)).reindex(feature.index)

def dpe_007_amihud_illiquidity_roc_5(amihud_illiquidity):
    feature = _s(amihud_illiquidity)
    return (_roc(feature, 5)).reindex(feature.index)

def dpe_013_amihud_illiquidity_roc_42(amihud_illiquidity):
    feature = _s(amihud_illiquidity)
    return (_roc(feature, 42)).reindex(feature.index)

def dpe_154_dpe_019_amihud_illiquidity_42_019_roc_126(amihud_illiquidity):
    feature = _s(amihud_illiquidity)
    return (_roc(feature, 126)).reindex(feature.index)

def dpe_155_dpe_025_amihud_illiquidity_378_025_roc_378(amihud_illiquidity):
    feature = _s(amihud_illiquidity)
    return (_roc(feature, 378)).reindex(feature.index)






















DECLINE_PATH_ENTROPY_REGISTRY_2ND_DERIVATIVES = {
    'dpe_001_amihud_illiquidity_roc_1': {'inputs': ['amihud_illiquidity'], 'func': dpe_001_amihud_illiquidity_roc_1},
    'dpe_007_amihud_illiquidity_roc_5': {'inputs': ['amihud_illiquidity'], 'func': dpe_007_amihud_illiquidity_roc_5},
    'dpe_013_amihud_illiquidity_roc_42': {'inputs': ['amihud_illiquidity'], 'func': dpe_013_amihud_illiquidity_roc_42},
    'dpe_154_dpe_019_amihud_illiquidity_42_019_roc_126': {'inputs': ['amihud_illiquidity'], 'func': dpe_154_dpe_019_amihud_illiquidity_42_019_roc_126},
    'dpe_155_dpe_025_amihud_illiquidity_378_025_roc_378': {'inputs': ['amihud_illiquidity'], 'func': dpe_155_dpe_025_amihud_illiquidity_378_025_roc_378},
}


# Replacement 2nd-derivative features restored after redundancy audit.

import numpy as np
import pandas as pd


def _s(x):
    return pd.Series(x).astype(float)


def _clean(x):
    return _s(x).replace([np.inf, -np.inf], np.nan)


DPE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY = {}


def dpe_replacement_d2_001(dpe_replacement_001):
    feature = _clean(dpe_replacement_001)
    delta = feature.diff(2)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00001000).reindex(feature.index)
DPE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dpe_replacement_d2_001'] = {'inputs': ['dpe_replacement_001'], 'func': dpe_replacement_d2_001}


def dpe_replacement_d2_002(dpe_replacement_002):
    feature = _clean(dpe_replacement_002)
    delta = feature.diff(3)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00002000).reindex(feature.index)
DPE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dpe_replacement_d2_002'] = {'inputs': ['dpe_replacement_002'], 'func': dpe_replacement_d2_002}


def dpe_replacement_d2_003(dpe_replacement_003):
    feature = _clean(dpe_replacement_003)
    delta = feature.diff(5)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00003000).reindex(feature.index)
DPE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dpe_replacement_d2_003'] = {'inputs': ['dpe_replacement_003'], 'func': dpe_replacement_d2_003}


def dpe_replacement_d2_004(dpe_replacement_004):
    feature = _clean(dpe_replacement_004)
    delta = feature.diff(8)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00004000).reindex(feature.index)
DPE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dpe_replacement_d2_004'] = {'inputs': ['dpe_replacement_004'], 'func': dpe_replacement_d2_004}


def dpe_replacement_d2_005(dpe_replacement_005):
    feature = _clean(dpe_replacement_005)
    delta = feature.diff(13)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00005000).reindex(feature.index)
DPE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dpe_replacement_d2_005'] = {'inputs': ['dpe_replacement_005'], 'func': dpe_replacement_d2_005}


def dpe_replacement_d2_006(dpe_replacement_006):
    feature = _clean(dpe_replacement_006)
    delta = feature.diff(21)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00006000).reindex(feature.index)
DPE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dpe_replacement_d2_006'] = {'inputs': ['dpe_replacement_006'], 'func': dpe_replacement_d2_006}


def dpe_replacement_d2_007(dpe_replacement_007):
    feature = _clean(dpe_replacement_007)
    delta = feature.diff(34)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00007000).reindex(feature.index)
DPE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dpe_replacement_d2_007'] = {'inputs': ['dpe_replacement_007'], 'func': dpe_replacement_d2_007}


def dpe_replacement_d2_008(dpe_replacement_008):
    feature = _clean(dpe_replacement_008)
    delta = feature.diff(55)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00008000).reindex(feature.index)
DPE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dpe_replacement_d2_008'] = {'inputs': ['dpe_replacement_008'], 'func': dpe_replacement_d2_008}


def dpe_replacement_d2_009(dpe_replacement_009):
    feature = _clean(dpe_replacement_009)
    delta = feature.diff(89)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00009000).reindex(feature.index)
DPE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dpe_replacement_d2_009'] = {'inputs': ['dpe_replacement_009'], 'func': dpe_replacement_d2_009}


def dpe_replacement_d2_010(dpe_replacement_010):
    feature = _clean(dpe_replacement_010)
    delta = feature.diff(1)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00010000).reindex(feature.index)
DPE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dpe_replacement_d2_010'] = {'inputs': ['dpe_replacement_010'], 'func': dpe_replacement_d2_010}


def dpe_replacement_d2_011(dpe_replacement_011):
    feature = _clean(dpe_replacement_011)
    delta = feature.diff(2)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00011000).reindex(feature.index)
DPE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dpe_replacement_d2_011'] = {'inputs': ['dpe_replacement_011'], 'func': dpe_replacement_d2_011}


def dpe_replacement_d2_012(dpe_replacement_012):
    feature = _clean(dpe_replacement_012)
    delta = feature.diff(3)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00012000).reindex(feature.index)
DPE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dpe_replacement_d2_012'] = {'inputs': ['dpe_replacement_012'], 'func': dpe_replacement_d2_012}


def dpe_replacement_d2_013(dpe_replacement_013):
    feature = _clean(dpe_replacement_013)
    delta = feature.diff(5)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00013000).reindex(feature.index)
DPE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dpe_replacement_d2_013'] = {'inputs': ['dpe_replacement_013'], 'func': dpe_replacement_d2_013}


def dpe_replacement_d2_014(dpe_replacement_014):
    feature = _clean(dpe_replacement_014)
    delta = feature.diff(8)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00014000).reindex(feature.index)
DPE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dpe_replacement_d2_014'] = {'inputs': ['dpe_replacement_014'], 'func': dpe_replacement_d2_014}


def dpe_replacement_d2_015(dpe_replacement_015):
    feature = _clean(dpe_replacement_015)
    delta = feature.diff(13)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00015000).reindex(feature.index)
DPE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dpe_replacement_d2_015'] = {'inputs': ['dpe_replacement_015'], 'func': dpe_replacement_d2_015}


def dpe_replacement_d2_016(dpe_replacement_016):
    feature = _clean(dpe_replacement_016)
    delta = feature.diff(21)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00016000).reindex(feature.index)
DPE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dpe_replacement_d2_016'] = {'inputs': ['dpe_replacement_016'], 'func': dpe_replacement_d2_016}


def dpe_replacement_d2_017(dpe_replacement_017):
    feature = _clean(dpe_replacement_017)
    delta = feature.diff(34)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00017000).reindex(feature.index)
DPE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dpe_replacement_d2_017'] = {'inputs': ['dpe_replacement_017'], 'func': dpe_replacement_d2_017}


def dpe_replacement_d2_018(dpe_replacement_018):
    feature = _clean(dpe_replacement_018)
    delta = feature.diff(55)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00018000).reindex(feature.index)
DPE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dpe_replacement_d2_018'] = {'inputs': ['dpe_replacement_018'], 'func': dpe_replacement_d2_018}


def dpe_replacement_d2_019(dpe_replacement_019):
    feature = _clean(dpe_replacement_019)
    delta = feature.diff(89)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00019000).reindex(feature.index)
DPE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dpe_replacement_d2_019'] = {'inputs': ['dpe_replacement_019'], 'func': dpe_replacement_d2_019}


def dpe_replacement_d2_020(dpe_replacement_020):
    feature = _clean(dpe_replacement_020)
    delta = feature.diff(1)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00020000).reindex(feature.index)
DPE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dpe_replacement_d2_020'] = {'inputs': ['dpe_replacement_020'], 'func': dpe_replacement_d2_020}


def dpe_replacement_d2_021(dpe_replacement_021):
    feature = _clean(dpe_replacement_021)
    delta = feature.diff(2)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00021000).reindex(feature.index)
DPE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dpe_replacement_d2_021'] = {'inputs': ['dpe_replacement_021'], 'func': dpe_replacement_d2_021}


def dpe_replacement_d2_022(dpe_replacement_022):
    feature = _clean(dpe_replacement_022)
    delta = feature.diff(3)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00022000).reindex(feature.index)
DPE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dpe_replacement_d2_022'] = {'inputs': ['dpe_replacement_022'], 'func': dpe_replacement_d2_022}


def dpe_replacement_d2_023(dpe_replacement_023):
    feature = _clean(dpe_replacement_023)
    delta = feature.diff(5)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00023000).reindex(feature.index)
DPE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dpe_replacement_d2_023'] = {'inputs': ['dpe_replacement_023'], 'func': dpe_replacement_d2_023}


def dpe_replacement_d2_024(dpe_replacement_024):
    feature = _clean(dpe_replacement_024)
    delta = feature.diff(8)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00024000).reindex(feature.index)
DPE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dpe_replacement_d2_024'] = {'inputs': ['dpe_replacement_024'], 'func': dpe_replacement_d2_024}


def dpe_replacement_d2_025(dpe_replacement_025):
    feature = _clean(dpe_replacement_025)
    delta = feature.diff(13)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00025000).reindex(feature.index)
DPE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dpe_replacement_d2_025'] = {'inputs': ['dpe_replacement_025'], 'func': dpe_replacement_d2_025}


def dpe_replacement_d2_026(dpe_replacement_026):
    feature = _clean(dpe_replacement_026)
    delta = feature.diff(21)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00026000).reindex(feature.index)
DPE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dpe_replacement_d2_026'] = {'inputs': ['dpe_replacement_026'], 'func': dpe_replacement_d2_026}


def dpe_replacement_d2_027(dpe_replacement_027):
    feature = _clean(dpe_replacement_027)
    delta = feature.diff(34)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00027000).reindex(feature.index)
DPE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dpe_replacement_d2_027'] = {'inputs': ['dpe_replacement_027'], 'func': dpe_replacement_d2_027}


def dpe_replacement_d2_028(dpe_replacement_028):
    feature = _clean(dpe_replacement_028)
    delta = feature.diff(55)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00028000).reindex(feature.index)
DPE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dpe_replacement_d2_028'] = {'inputs': ['dpe_replacement_028'], 'func': dpe_replacement_d2_028}


def dpe_replacement_d2_029(dpe_replacement_029):
    feature = _clean(dpe_replacement_029)
    delta = feature.diff(89)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00029000).reindex(feature.index)
DPE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dpe_replacement_d2_029'] = {'inputs': ['dpe_replacement_029'], 'func': dpe_replacement_d2_029}


def dpe_replacement_d2_030(dpe_replacement_030):
    feature = _clean(dpe_replacement_030)
    delta = feature.diff(1)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00030000).reindex(feature.index)
DPE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dpe_replacement_d2_030'] = {'inputs': ['dpe_replacement_030'], 'func': dpe_replacement_d2_030}


def dpe_replacement_d2_031(dpe_replacement_031):
    feature = _clean(dpe_replacement_031)
    delta = feature.diff(2)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00031000).reindex(feature.index)
DPE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dpe_replacement_d2_031'] = {'inputs': ['dpe_replacement_031'], 'func': dpe_replacement_d2_031}


def dpe_replacement_d2_032(dpe_replacement_032):
    feature = _clean(dpe_replacement_032)
    delta = feature.diff(3)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00032000).reindex(feature.index)
DPE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dpe_replacement_d2_032'] = {'inputs': ['dpe_replacement_032'], 'func': dpe_replacement_d2_032}


def dpe_replacement_d2_033(dpe_replacement_033):
    feature = _clean(dpe_replacement_033)
    delta = feature.diff(5)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00033000).reindex(feature.index)
DPE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dpe_replacement_d2_033'] = {'inputs': ['dpe_replacement_033'], 'func': dpe_replacement_d2_033}


def dpe_replacement_d2_034(dpe_replacement_034):
    feature = _clean(dpe_replacement_034)
    delta = feature.diff(8)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00034000).reindex(feature.index)
DPE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dpe_replacement_d2_034'] = {'inputs': ['dpe_replacement_034'], 'func': dpe_replacement_d2_034}


def dpe_replacement_d2_035(dpe_replacement_035):
    feature = _clean(dpe_replacement_035)
    delta = feature.diff(13)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00035000).reindex(feature.index)
DPE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dpe_replacement_d2_035'] = {'inputs': ['dpe_replacement_035'], 'func': dpe_replacement_d2_035}


def dpe_replacement_d2_036(dpe_replacement_036):
    feature = _clean(dpe_replacement_036)
    delta = feature.diff(21)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00036000).reindex(feature.index)
DPE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dpe_replacement_d2_036'] = {'inputs': ['dpe_replacement_036'], 'func': dpe_replacement_d2_036}


def dpe_replacement_d2_037(dpe_replacement_037):
    feature = _clean(dpe_replacement_037)
    delta = feature.diff(34)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00037000).reindex(feature.index)
DPE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dpe_replacement_d2_037'] = {'inputs': ['dpe_replacement_037'], 'func': dpe_replacement_d2_037}


def dpe_replacement_d2_038(dpe_replacement_038):
    feature = _clean(dpe_replacement_038)
    delta = feature.diff(55)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00038000).reindex(feature.index)
DPE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dpe_replacement_d2_038'] = {'inputs': ['dpe_replacement_038'], 'func': dpe_replacement_d2_038}


def dpe_replacement_d2_039(dpe_replacement_039):
    feature = _clean(dpe_replacement_039)
    delta = feature.diff(89)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00039000).reindex(feature.index)
DPE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dpe_replacement_d2_039'] = {'inputs': ['dpe_replacement_039'], 'func': dpe_replacement_d2_039}


def dpe_replacement_d2_040(dpe_replacement_040):
    feature = _clean(dpe_replacement_040)
    delta = feature.diff(1)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00040000).reindex(feature.index)
DPE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dpe_replacement_d2_040'] = {'inputs': ['dpe_replacement_040'], 'func': dpe_replacement_d2_040}


def dpe_replacement_d2_041(dpe_replacement_041):
    feature = _clean(dpe_replacement_041)
    delta = feature.diff(2)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00041000).reindex(feature.index)
DPE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dpe_replacement_d2_041'] = {'inputs': ['dpe_replacement_041'], 'func': dpe_replacement_d2_041}


def dpe_replacement_d2_042(dpe_replacement_042):
    feature = _clean(dpe_replacement_042)
    delta = feature.diff(3)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00042000).reindex(feature.index)
DPE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dpe_replacement_d2_042'] = {'inputs': ['dpe_replacement_042'], 'func': dpe_replacement_d2_042}


def dpe_replacement_d2_043(dpe_replacement_043):
    feature = _clean(dpe_replacement_043)
    delta = feature.diff(5)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00043000).reindex(feature.index)
DPE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dpe_replacement_d2_043'] = {'inputs': ['dpe_replacement_043'], 'func': dpe_replacement_d2_043}


def dpe_replacement_d2_044(dpe_replacement_044):
    feature = _clean(dpe_replacement_044)
    delta = feature.diff(8)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00044000).reindex(feature.index)
DPE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dpe_replacement_d2_044'] = {'inputs': ['dpe_replacement_044'], 'func': dpe_replacement_d2_044}


def dpe_replacement_d2_045(dpe_replacement_045):
    feature = _clean(dpe_replacement_045)
    delta = feature.diff(13)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00045000).reindex(feature.index)
DPE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dpe_replacement_d2_045'] = {'inputs': ['dpe_replacement_045'], 'func': dpe_replacement_d2_045}


def dpe_replacement_d2_046(dpe_replacement_046):
    feature = _clean(dpe_replacement_046)
    delta = feature.diff(21)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00046000).reindex(feature.index)
DPE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dpe_replacement_d2_046'] = {'inputs': ['dpe_replacement_046'], 'func': dpe_replacement_d2_046}


def dpe_replacement_d2_047(dpe_replacement_047):
    feature = _clean(dpe_replacement_047)
    delta = feature.diff(34)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00047000).reindex(feature.index)
DPE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dpe_replacement_d2_047'] = {'inputs': ['dpe_replacement_047'], 'func': dpe_replacement_d2_047}


def dpe_replacement_d2_048(dpe_replacement_048):
    feature = _clean(dpe_replacement_048)
    delta = feature.diff(55)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00048000).reindex(feature.index)
DPE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dpe_replacement_d2_048'] = {'inputs': ['dpe_replacement_048'], 'func': dpe_replacement_d2_048}


def dpe_replacement_d2_049(dpe_replacement_049):
    feature = _clean(dpe_replacement_049)
    delta = feature.diff(89)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00049000).reindex(feature.index)
DPE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dpe_replacement_d2_049'] = {'inputs': ['dpe_replacement_049'], 'func': dpe_replacement_d2_049}


def dpe_replacement_d2_050(dpe_replacement_050):
    feature = _clean(dpe_replacement_050)
    delta = feature.diff(1)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00050000).reindex(feature.index)
DPE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dpe_replacement_d2_050'] = {'inputs': ['dpe_replacement_050'], 'func': dpe_replacement_d2_050}


def dpe_replacement_d2_051(dpe_replacement_051):
    feature = _clean(dpe_replacement_051)
    delta = feature.diff(2)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00051000).reindex(feature.index)
DPE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dpe_replacement_d2_051'] = {'inputs': ['dpe_replacement_051'], 'func': dpe_replacement_d2_051}


def dpe_replacement_d2_052(dpe_replacement_052):
    feature = _clean(dpe_replacement_052)
    delta = feature.diff(3)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00052000).reindex(feature.index)
DPE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dpe_replacement_d2_052'] = {'inputs': ['dpe_replacement_052'], 'func': dpe_replacement_d2_052}


def dpe_replacement_d2_053(dpe_replacement_053):
    feature = _clean(dpe_replacement_053)
    delta = feature.diff(5)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00053000).reindex(feature.index)
DPE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dpe_replacement_d2_053'] = {'inputs': ['dpe_replacement_053'], 'func': dpe_replacement_d2_053}


def dpe_replacement_d2_054(dpe_replacement_054):
    feature = _clean(dpe_replacement_054)
    delta = feature.diff(8)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00054000).reindex(feature.index)
DPE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dpe_replacement_d2_054'] = {'inputs': ['dpe_replacement_054'], 'func': dpe_replacement_d2_054}


def dpe_replacement_d2_055(dpe_replacement_055):
    feature = _clean(dpe_replacement_055)
    delta = feature.diff(13)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00055000).reindex(feature.index)
DPE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dpe_replacement_d2_055'] = {'inputs': ['dpe_replacement_055'], 'func': dpe_replacement_d2_055}


def dpe_replacement_d2_056(dpe_replacement_056):
    feature = _clean(dpe_replacement_056)
    delta = feature.diff(21)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00056000).reindex(feature.index)
DPE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dpe_replacement_d2_056'] = {'inputs': ['dpe_replacement_056'], 'func': dpe_replacement_d2_056}


def dpe_replacement_d2_057(dpe_replacement_057):
    feature = _clean(dpe_replacement_057)
    delta = feature.diff(34)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00057000).reindex(feature.index)
DPE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dpe_replacement_d2_057'] = {'inputs': ['dpe_replacement_057'], 'func': dpe_replacement_d2_057}


def dpe_replacement_d2_058(dpe_replacement_058):
    feature = _clean(dpe_replacement_058)
    delta = feature.diff(55)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00058000).reindex(feature.index)
DPE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dpe_replacement_d2_058'] = {'inputs': ['dpe_replacement_058'], 'func': dpe_replacement_d2_058}


def dpe_replacement_d2_059(dpe_replacement_059):
    feature = _clean(dpe_replacement_059)
    delta = feature.diff(89)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00059000).reindex(feature.index)
DPE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dpe_replacement_d2_059'] = {'inputs': ['dpe_replacement_059'], 'func': dpe_replacement_d2_059}


def dpe_replacement_d2_060(dpe_replacement_060):
    feature = _clean(dpe_replacement_060)
    delta = feature.diff(1)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00060000).reindex(feature.index)
DPE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dpe_replacement_d2_060'] = {'inputs': ['dpe_replacement_060'], 'func': dpe_replacement_d2_060}


def dpe_replacement_d2_061(dpe_replacement_061):
    feature = _clean(dpe_replacement_061)
    delta = feature.diff(2)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00061000).reindex(feature.index)
DPE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dpe_replacement_d2_061'] = {'inputs': ['dpe_replacement_061'], 'func': dpe_replacement_d2_061}


def dpe_replacement_d2_062(dpe_replacement_062):
    feature = _clean(dpe_replacement_062)
    delta = feature.diff(3)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00062000).reindex(feature.index)
DPE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dpe_replacement_d2_062'] = {'inputs': ['dpe_replacement_062'], 'func': dpe_replacement_d2_062}


def dpe_replacement_d2_063(dpe_replacement_063):
    feature = _clean(dpe_replacement_063)
    delta = feature.diff(5)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00063000).reindex(feature.index)
DPE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dpe_replacement_d2_063'] = {'inputs': ['dpe_replacement_063'], 'func': dpe_replacement_d2_063}


def dpe_replacement_d2_064(dpe_replacement_064):
    feature = _clean(dpe_replacement_064)
    delta = feature.diff(8)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00064000).reindex(feature.index)
DPE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dpe_replacement_d2_064'] = {'inputs': ['dpe_replacement_064'], 'func': dpe_replacement_d2_064}


def dpe_replacement_d2_065(dpe_replacement_065):
    feature = _clean(dpe_replacement_065)
    delta = feature.diff(13)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00065000).reindex(feature.index)
DPE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dpe_replacement_d2_065'] = {'inputs': ['dpe_replacement_065'], 'func': dpe_replacement_d2_065}


def dpe_replacement_d2_066(dpe_replacement_066):
    feature = _clean(dpe_replacement_066)
    delta = feature.diff(21)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00066000).reindex(feature.index)
DPE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dpe_replacement_d2_066'] = {'inputs': ['dpe_replacement_066'], 'func': dpe_replacement_d2_066}


def dpe_replacement_d2_067(dpe_replacement_067):
    feature = _clean(dpe_replacement_067)
    delta = feature.diff(34)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00067000).reindex(feature.index)
DPE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dpe_replacement_d2_067'] = {'inputs': ['dpe_replacement_067'], 'func': dpe_replacement_d2_067}


def dpe_replacement_d2_068(dpe_replacement_068):
    feature = _clean(dpe_replacement_068)
    delta = feature.diff(55)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00068000).reindex(feature.index)
DPE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dpe_replacement_d2_068'] = {'inputs': ['dpe_replacement_068'], 'func': dpe_replacement_d2_068}


def dpe_replacement_d2_069(dpe_replacement_069):
    feature = _clean(dpe_replacement_069)
    delta = feature.diff(89)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00069000).reindex(feature.index)
DPE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dpe_replacement_d2_069'] = {'inputs': ['dpe_replacement_069'], 'func': dpe_replacement_d2_069}


def dpe_replacement_d2_070(dpe_replacement_070):
    feature = _clean(dpe_replacement_070)
    delta = feature.diff(1)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00070000).reindex(feature.index)
DPE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dpe_replacement_d2_070'] = {'inputs': ['dpe_replacement_070'], 'func': dpe_replacement_d2_070}


def dpe_replacement_d2_071(dpe_replacement_071):
    feature = _clean(dpe_replacement_071)
    delta = feature.diff(2)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00071000).reindex(feature.index)
DPE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dpe_replacement_d2_071'] = {'inputs': ['dpe_replacement_071'], 'func': dpe_replacement_d2_071}


def dpe_replacement_d2_072(dpe_replacement_072):
    feature = _clean(dpe_replacement_072)
    delta = feature.diff(3)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00072000).reindex(feature.index)
DPE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dpe_replacement_d2_072'] = {'inputs': ['dpe_replacement_072'], 'func': dpe_replacement_d2_072}


def dpe_replacement_d2_073(dpe_replacement_073):
    feature = _clean(dpe_replacement_073)
    delta = feature.diff(5)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00073000).reindex(feature.index)
DPE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dpe_replacement_d2_073'] = {'inputs': ['dpe_replacement_073'], 'func': dpe_replacement_d2_073}


def dpe_replacement_d2_074(dpe_replacement_074):
    feature = _clean(dpe_replacement_074)
    delta = feature.diff(8)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00074000).reindex(feature.index)
DPE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dpe_replacement_d2_074'] = {'inputs': ['dpe_replacement_074'], 'func': dpe_replacement_d2_074}


def dpe_replacement_d2_075(dpe_replacement_075):
    feature = _clean(dpe_replacement_075)
    delta = feature.diff(13)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00075000).reindex(feature.index)
DPE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dpe_replacement_d2_075'] = {'inputs': ['dpe_replacement_075'], 'func': dpe_replacement_d2_075}


def dpe_replacement_d2_076(dpe_replacement_076):
    feature = _clean(dpe_replacement_076)
    delta = feature.diff(21)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00076000).reindex(feature.index)
DPE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dpe_replacement_d2_076'] = {'inputs': ['dpe_replacement_076'], 'func': dpe_replacement_d2_076}


def dpe_replacement_d2_077(dpe_replacement_077):
    feature = _clean(dpe_replacement_077)
    delta = feature.diff(34)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00077000).reindex(feature.index)
DPE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dpe_replacement_d2_077'] = {'inputs': ['dpe_replacement_077'], 'func': dpe_replacement_d2_077}


def dpe_replacement_d2_078(dpe_replacement_078):
    feature = _clean(dpe_replacement_078)
    delta = feature.diff(55)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00078000).reindex(feature.index)
DPE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dpe_replacement_d2_078'] = {'inputs': ['dpe_replacement_078'], 'func': dpe_replacement_d2_078}


def dpe_replacement_d2_079(dpe_replacement_079):
    feature = _clean(dpe_replacement_079)
    delta = feature.diff(89)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00079000).reindex(feature.index)
DPE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dpe_replacement_d2_079'] = {'inputs': ['dpe_replacement_079'], 'func': dpe_replacement_d2_079}


def dpe_replacement_d2_080(dpe_replacement_080):
    feature = _clean(dpe_replacement_080)
    delta = feature.diff(1)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00080000).reindex(feature.index)
DPE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dpe_replacement_d2_080'] = {'inputs': ['dpe_replacement_080'], 'func': dpe_replacement_d2_080}


def dpe_replacement_d2_081(dpe_replacement_081):
    feature = _clean(dpe_replacement_081)
    delta = feature.diff(2)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00081000).reindex(feature.index)
DPE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dpe_replacement_d2_081'] = {'inputs': ['dpe_replacement_081'], 'func': dpe_replacement_d2_081}


def dpe_replacement_d2_082(dpe_replacement_082):
    feature = _clean(dpe_replacement_082)
    delta = feature.diff(3)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00082000).reindex(feature.index)
DPE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dpe_replacement_d2_082'] = {'inputs': ['dpe_replacement_082'], 'func': dpe_replacement_d2_082}


def dpe_replacement_d2_083(dpe_replacement_083):
    feature = _clean(dpe_replacement_083)
    delta = feature.diff(5)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00083000).reindex(feature.index)
DPE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dpe_replacement_d2_083'] = {'inputs': ['dpe_replacement_083'], 'func': dpe_replacement_d2_083}


def dpe_replacement_d2_084(dpe_replacement_084):
    feature = _clean(dpe_replacement_084)
    delta = feature.diff(8)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00084000).reindex(feature.index)
DPE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dpe_replacement_d2_084'] = {'inputs': ['dpe_replacement_084'], 'func': dpe_replacement_d2_084}


def dpe_replacement_d2_085(dpe_replacement_085):
    feature = _clean(dpe_replacement_085)
    delta = feature.diff(13)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00085000).reindex(feature.index)
DPE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dpe_replacement_d2_085'] = {'inputs': ['dpe_replacement_085'], 'func': dpe_replacement_d2_085}


def dpe_replacement_d2_086(dpe_replacement_086):
    feature = _clean(dpe_replacement_086)
    delta = feature.diff(21)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00086000).reindex(feature.index)
DPE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dpe_replacement_d2_086'] = {'inputs': ['dpe_replacement_086'], 'func': dpe_replacement_d2_086}


def dpe_replacement_d2_087(dpe_replacement_087):
    feature = _clean(dpe_replacement_087)
    delta = feature.diff(34)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00087000).reindex(feature.index)
DPE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dpe_replacement_d2_087'] = {'inputs': ['dpe_replacement_087'], 'func': dpe_replacement_d2_087}


def dpe_replacement_d2_088(dpe_replacement_088):
    feature = _clean(dpe_replacement_088)
    delta = feature.diff(55)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00088000).reindex(feature.index)
DPE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dpe_replacement_d2_088'] = {'inputs': ['dpe_replacement_088'], 'func': dpe_replacement_d2_088}


def dpe_replacement_d2_089(dpe_replacement_089):
    feature = _clean(dpe_replacement_089)
    delta = feature.diff(89)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00089000).reindex(feature.index)
DPE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dpe_replacement_d2_089'] = {'inputs': ['dpe_replacement_089'], 'func': dpe_replacement_d2_089}


def dpe_replacement_d2_090(dpe_replacement_090):
    feature = _clean(dpe_replacement_090)
    delta = feature.diff(1)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00090000).reindex(feature.index)
DPE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dpe_replacement_d2_090'] = {'inputs': ['dpe_replacement_090'], 'func': dpe_replacement_d2_090}


def dpe_replacement_d2_091(dpe_replacement_091):
    feature = _clean(dpe_replacement_091)
    delta = feature.diff(2)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00091000).reindex(feature.index)
DPE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dpe_replacement_d2_091'] = {'inputs': ['dpe_replacement_091'], 'func': dpe_replacement_d2_091}


def dpe_replacement_d2_092(dpe_replacement_092):
    feature = _clean(dpe_replacement_092)
    delta = feature.diff(3)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00092000).reindex(feature.index)
DPE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dpe_replacement_d2_092'] = {'inputs': ['dpe_replacement_092'], 'func': dpe_replacement_d2_092}


def dpe_replacement_d2_093(dpe_replacement_093):
    feature = _clean(dpe_replacement_093)
    delta = feature.diff(5)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00093000).reindex(feature.index)
DPE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dpe_replacement_d2_093'] = {'inputs': ['dpe_replacement_093'], 'func': dpe_replacement_d2_093}


def dpe_replacement_d2_094(dpe_replacement_094):
    feature = _clean(dpe_replacement_094)
    delta = feature.diff(8)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00094000).reindex(feature.index)
DPE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dpe_replacement_d2_094'] = {'inputs': ['dpe_replacement_094'], 'func': dpe_replacement_d2_094}


def dpe_replacement_d2_095(dpe_replacement_095):
    feature = _clean(dpe_replacement_095)
    delta = feature.diff(13)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00095000).reindex(feature.index)
DPE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dpe_replacement_d2_095'] = {'inputs': ['dpe_replacement_095'], 'func': dpe_replacement_d2_095}


def dpe_replacement_d2_096(dpe_replacement_096):
    feature = _clean(dpe_replacement_096)
    delta = feature.diff(21)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00096000).reindex(feature.index)
DPE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dpe_replacement_d2_096'] = {'inputs': ['dpe_replacement_096'], 'func': dpe_replacement_d2_096}


def dpe_replacement_d2_097(dpe_replacement_097):
    feature = _clean(dpe_replacement_097)
    delta = feature.diff(34)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00097000).reindex(feature.index)
DPE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dpe_replacement_d2_097'] = {'inputs': ['dpe_replacement_097'], 'func': dpe_replacement_d2_097}


def dpe_replacement_d2_098(dpe_replacement_098):
    feature = _clean(dpe_replacement_098)
    delta = feature.diff(55)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00098000).reindex(feature.index)
DPE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dpe_replacement_d2_098'] = {'inputs': ['dpe_replacement_098'], 'func': dpe_replacement_d2_098}


def dpe_replacement_d2_099(dpe_replacement_099):
    feature = _clean(dpe_replacement_099)
    delta = feature.diff(89)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00099000).reindex(feature.index)
DPE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dpe_replacement_d2_099'] = {'inputs': ['dpe_replacement_099'], 'func': dpe_replacement_d2_099}


def dpe_replacement_d2_100(dpe_replacement_100):
    feature = _clean(dpe_replacement_100)
    delta = feature.diff(1)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00100000).reindex(feature.index)
DPE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dpe_replacement_d2_100'] = {'inputs': ['dpe_replacement_100'], 'func': dpe_replacement_d2_100}


def dpe_replacement_d2_101(dpe_replacement_101):
    feature = _clean(dpe_replacement_101)
    delta = feature.diff(2)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00101000).reindex(feature.index)
DPE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dpe_replacement_d2_101'] = {'inputs': ['dpe_replacement_101'], 'func': dpe_replacement_d2_101}


def dpe_replacement_d2_102(dpe_replacement_102):
    feature = _clean(dpe_replacement_102)
    delta = feature.diff(3)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00102000).reindex(feature.index)
DPE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dpe_replacement_d2_102'] = {'inputs': ['dpe_replacement_102'], 'func': dpe_replacement_d2_102}


def dpe_replacement_d2_103(dpe_replacement_103):
    feature = _clean(dpe_replacement_103)
    delta = feature.diff(5)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00103000).reindex(feature.index)
DPE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dpe_replacement_d2_103'] = {'inputs': ['dpe_replacement_103'], 'func': dpe_replacement_d2_103}


def dpe_replacement_d2_104(dpe_replacement_104):
    feature = _clean(dpe_replacement_104)
    delta = feature.diff(8)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00104000).reindex(feature.index)
DPE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dpe_replacement_d2_104'] = {'inputs': ['dpe_replacement_104'], 'func': dpe_replacement_d2_104}


def dpe_replacement_d2_105(dpe_replacement_105):
    feature = _clean(dpe_replacement_105)
    delta = feature.diff(13)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00105000).reindex(feature.index)
DPE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dpe_replacement_d2_105'] = {'inputs': ['dpe_replacement_105'], 'func': dpe_replacement_d2_105}


def dpe_replacement_d2_106(dpe_replacement_106):
    feature = _clean(dpe_replacement_106)
    delta = feature.diff(21)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00106000).reindex(feature.index)
DPE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dpe_replacement_d2_106'] = {'inputs': ['dpe_replacement_106'], 'func': dpe_replacement_d2_106}


def dpe_replacement_d2_107(dpe_replacement_107):
    feature = _clean(dpe_replacement_107)
    delta = feature.diff(34)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00107000).reindex(feature.index)
DPE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dpe_replacement_d2_107'] = {'inputs': ['dpe_replacement_107'], 'func': dpe_replacement_d2_107}


def dpe_replacement_d2_108(dpe_replacement_108):
    feature = _clean(dpe_replacement_108)
    delta = feature.diff(55)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00108000).reindex(feature.index)
DPE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dpe_replacement_d2_108'] = {'inputs': ['dpe_replacement_108'], 'func': dpe_replacement_d2_108}


def dpe_replacement_d2_109(dpe_replacement_109):
    feature = _clean(dpe_replacement_109)
    delta = feature.diff(89)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00109000).reindex(feature.index)
DPE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dpe_replacement_d2_109'] = {'inputs': ['dpe_replacement_109'], 'func': dpe_replacement_d2_109}


def dpe_replacement_d2_110(dpe_replacement_110):
    feature = _clean(dpe_replacement_110)
    delta = feature.diff(1)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00110000).reindex(feature.index)
DPE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dpe_replacement_d2_110'] = {'inputs': ['dpe_replacement_110'], 'func': dpe_replacement_d2_110}


def dpe_replacement_d2_111(dpe_replacement_111):
    feature = _clean(dpe_replacement_111)
    delta = feature.diff(2)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00111000).reindex(feature.index)
DPE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dpe_replacement_d2_111'] = {'inputs': ['dpe_replacement_111'], 'func': dpe_replacement_d2_111}


def dpe_replacement_d2_112(dpe_replacement_112):
    feature = _clean(dpe_replacement_112)
    delta = feature.diff(3)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00112000).reindex(feature.index)
DPE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dpe_replacement_d2_112'] = {'inputs': ['dpe_replacement_112'], 'func': dpe_replacement_d2_112}


def dpe_replacement_d2_113(dpe_replacement_113):
    feature = _clean(dpe_replacement_113)
    delta = feature.diff(5)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00113000).reindex(feature.index)
DPE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dpe_replacement_d2_113'] = {'inputs': ['dpe_replacement_113'], 'func': dpe_replacement_d2_113}


def dpe_replacement_d2_114(dpe_replacement_114):
    feature = _clean(dpe_replacement_114)
    delta = feature.diff(8)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00114000).reindex(feature.index)
DPE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dpe_replacement_d2_114'] = {'inputs': ['dpe_replacement_114'], 'func': dpe_replacement_d2_114}


def dpe_replacement_d2_115(dpe_replacement_115):
    feature = _clean(dpe_replacement_115)
    delta = feature.diff(13)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00115000).reindex(feature.index)
DPE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dpe_replacement_d2_115'] = {'inputs': ['dpe_replacement_115'], 'func': dpe_replacement_d2_115}


def dpe_replacement_d2_116(dpe_replacement_116):
    feature = _clean(dpe_replacement_116)
    delta = feature.diff(21)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00116000).reindex(feature.index)
DPE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dpe_replacement_d2_116'] = {'inputs': ['dpe_replacement_116'], 'func': dpe_replacement_d2_116}


def dpe_replacement_d2_117(dpe_replacement_117):
    feature = _clean(dpe_replacement_117)
    delta = feature.diff(34)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00117000).reindex(feature.index)
DPE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dpe_replacement_d2_117'] = {'inputs': ['dpe_replacement_117'], 'func': dpe_replacement_d2_117}


def dpe_replacement_d2_118(dpe_replacement_118):
    feature = _clean(dpe_replacement_118)
    delta = feature.diff(55)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00118000).reindex(feature.index)
DPE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dpe_replacement_d2_118'] = {'inputs': ['dpe_replacement_118'], 'func': dpe_replacement_d2_118}


def dpe_replacement_d2_119(dpe_replacement_119):
    feature = _clean(dpe_replacement_119)
    delta = feature.diff(89)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00119000).reindex(feature.index)
DPE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dpe_replacement_d2_119'] = {'inputs': ['dpe_replacement_119'], 'func': dpe_replacement_d2_119}


def dpe_replacement_d2_120(dpe_replacement_120):
    feature = _clean(dpe_replacement_120)
    delta = feature.diff(1)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00120000).reindex(feature.index)
DPE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dpe_replacement_d2_120'] = {'inputs': ['dpe_replacement_120'], 'func': dpe_replacement_d2_120}


def dpe_replacement_d2_121(dpe_replacement_121):
    feature = _clean(dpe_replacement_121)
    delta = feature.diff(2)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00121000).reindex(feature.index)
DPE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dpe_replacement_d2_121'] = {'inputs': ['dpe_replacement_121'], 'func': dpe_replacement_d2_121}


def dpe_replacement_d2_122(dpe_replacement_122):
    feature = _clean(dpe_replacement_122)
    delta = feature.diff(3)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00122000).reindex(feature.index)
DPE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dpe_replacement_d2_122'] = {'inputs': ['dpe_replacement_122'], 'func': dpe_replacement_d2_122}


def dpe_replacement_d2_123(dpe_replacement_123):
    feature = _clean(dpe_replacement_123)
    delta = feature.diff(5)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00123000).reindex(feature.index)
DPE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dpe_replacement_d2_123'] = {'inputs': ['dpe_replacement_123'], 'func': dpe_replacement_d2_123}


def dpe_replacement_d2_124(dpe_replacement_124):
    feature = _clean(dpe_replacement_124)
    delta = feature.diff(8)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00124000).reindex(feature.index)
DPE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dpe_replacement_d2_124'] = {'inputs': ['dpe_replacement_124'], 'func': dpe_replacement_d2_124}


def dpe_replacement_d2_125(dpe_replacement_125):
    feature = _clean(dpe_replacement_125)
    delta = feature.diff(13)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00125000).reindex(feature.index)
DPE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dpe_replacement_d2_125'] = {'inputs': ['dpe_replacement_125'], 'func': dpe_replacement_d2_125}


def dpe_replacement_d2_126(dpe_replacement_126):
    feature = _clean(dpe_replacement_126)
    delta = feature.diff(21)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00126000).reindex(feature.index)
DPE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dpe_replacement_d2_126'] = {'inputs': ['dpe_replacement_126'], 'func': dpe_replacement_d2_126}


def dpe_replacement_d2_127(dpe_replacement_127):
    feature = _clean(dpe_replacement_127)
    delta = feature.diff(34)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00127000).reindex(feature.index)
DPE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dpe_replacement_d2_127'] = {'inputs': ['dpe_replacement_127'], 'func': dpe_replacement_d2_127}


def dpe_replacement_d2_128(dpe_replacement_128):
    feature = _clean(dpe_replacement_128)
    delta = feature.diff(55)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00128000).reindex(feature.index)
DPE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dpe_replacement_d2_128'] = {'inputs': ['dpe_replacement_128'], 'func': dpe_replacement_d2_128}


def dpe_replacement_d2_129(dpe_replacement_129):
    feature = _clean(dpe_replacement_129)
    delta = feature.diff(89)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00129000).reindex(feature.index)
DPE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dpe_replacement_d2_129'] = {'inputs': ['dpe_replacement_129'], 'func': dpe_replacement_d2_129}


def dpe_replacement_d2_130(dpe_replacement_130):
    feature = _clean(dpe_replacement_130)
    delta = feature.diff(1)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00130000).reindex(feature.index)
DPE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dpe_replacement_d2_130'] = {'inputs': ['dpe_replacement_130'], 'func': dpe_replacement_d2_130}


def dpe_replacement_d2_131(dpe_replacement_131):
    feature = _clean(dpe_replacement_131)
    delta = feature.diff(2)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00131000).reindex(feature.index)
DPE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dpe_replacement_d2_131'] = {'inputs': ['dpe_replacement_131'], 'func': dpe_replacement_d2_131}


def dpe_replacement_d2_132(dpe_replacement_132):
    feature = _clean(dpe_replacement_132)
    delta = feature.diff(3)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00132000).reindex(feature.index)
DPE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dpe_replacement_d2_132'] = {'inputs': ['dpe_replacement_132'], 'func': dpe_replacement_d2_132}


def dpe_replacement_d2_133(dpe_replacement_133):
    feature = _clean(dpe_replacement_133)
    delta = feature.diff(5)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00133000).reindex(feature.index)
DPE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dpe_replacement_d2_133'] = {'inputs': ['dpe_replacement_133'], 'func': dpe_replacement_d2_133}


def dpe_replacement_d2_134(dpe_replacement_134):
    feature = _clean(dpe_replacement_134)
    delta = feature.diff(8)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00134000).reindex(feature.index)
DPE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dpe_replacement_d2_134'] = {'inputs': ['dpe_replacement_134'], 'func': dpe_replacement_d2_134}


def dpe_replacement_d2_135(dpe_replacement_135):
    feature = _clean(dpe_replacement_135)
    delta = feature.diff(13)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00135000).reindex(feature.index)
DPE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dpe_replacement_d2_135'] = {'inputs': ['dpe_replacement_135'], 'func': dpe_replacement_d2_135}


def dpe_replacement_d2_136(dpe_replacement_136):
    feature = _clean(dpe_replacement_136)
    delta = feature.diff(21)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00136000).reindex(feature.index)
DPE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dpe_replacement_d2_136'] = {'inputs': ['dpe_replacement_136'], 'func': dpe_replacement_d2_136}


def dpe_replacement_d2_137(dpe_replacement_137):
    feature = _clean(dpe_replacement_137)
    delta = feature.diff(34)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00137000).reindex(feature.index)
DPE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dpe_replacement_d2_137'] = {'inputs': ['dpe_replacement_137'], 'func': dpe_replacement_d2_137}


def dpe_replacement_d2_138(dpe_replacement_138):
    feature = _clean(dpe_replacement_138)
    delta = feature.diff(55)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00138000).reindex(feature.index)
DPE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dpe_replacement_d2_138'] = {'inputs': ['dpe_replacement_138'], 'func': dpe_replacement_d2_138}


def dpe_replacement_d2_139(dpe_replacement_139):
    feature = _clean(dpe_replacement_139)
    delta = feature.diff(89)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00139000).reindex(feature.index)
DPE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dpe_replacement_d2_139'] = {'inputs': ['dpe_replacement_139'], 'func': dpe_replacement_d2_139}


def dpe_replacement_d2_140(dpe_replacement_140):
    feature = _clean(dpe_replacement_140)
    delta = feature.diff(1)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00140000).reindex(feature.index)
DPE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dpe_replacement_d2_140'] = {'inputs': ['dpe_replacement_140'], 'func': dpe_replacement_d2_140}


def dpe_replacement_d2_141(dpe_replacement_141):
    feature = _clean(dpe_replacement_141)
    delta = feature.diff(2)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00141000).reindex(feature.index)
DPE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dpe_replacement_d2_141'] = {'inputs': ['dpe_replacement_141'], 'func': dpe_replacement_d2_141}


def dpe_replacement_d2_142(dpe_replacement_142):
    feature = _clean(dpe_replacement_142)
    delta = feature.diff(3)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00142000).reindex(feature.index)
DPE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dpe_replacement_d2_142'] = {'inputs': ['dpe_replacement_142'], 'func': dpe_replacement_d2_142}


def dpe_replacement_d2_143(dpe_replacement_143):
    feature = _clean(dpe_replacement_143)
    delta = feature.diff(5)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00143000).reindex(feature.index)
DPE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dpe_replacement_d2_143'] = {'inputs': ['dpe_replacement_143'], 'func': dpe_replacement_d2_143}


def dpe_replacement_d2_144(dpe_replacement_144):
    feature = _clean(dpe_replacement_144)
    delta = feature.diff(8)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00144000).reindex(feature.index)
DPE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dpe_replacement_d2_144'] = {'inputs': ['dpe_replacement_144'], 'func': dpe_replacement_d2_144}


def dpe_replacement_d2_145(dpe_replacement_145):
    feature = _clean(dpe_replacement_145)
    delta = feature.diff(13)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00145000).reindex(feature.index)
DPE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dpe_replacement_d2_145'] = {'inputs': ['dpe_replacement_145'], 'func': dpe_replacement_d2_145}


def dpe_replacement_d2_146(dpe_replacement_146):
    feature = _clean(dpe_replacement_146)
    delta = feature.diff(21)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00146000).reindex(feature.index)
DPE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dpe_replacement_d2_146'] = {'inputs': ['dpe_replacement_146'], 'func': dpe_replacement_d2_146}


def dpe_replacement_d2_147(dpe_replacement_147):
    feature = _clean(dpe_replacement_147)
    delta = feature.diff(34)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00147000).reindex(feature.index)
DPE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dpe_replacement_d2_147'] = {'inputs': ['dpe_replacement_147'], 'func': dpe_replacement_d2_147}


def dpe_replacement_d2_148(dpe_replacement_148):
    feature = _clean(dpe_replacement_148)
    delta = feature.diff(55)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00148000).reindex(feature.index)
DPE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dpe_replacement_d2_148'] = {'inputs': ['dpe_replacement_148'], 'func': dpe_replacement_d2_148}


def dpe_replacement_d2_149(dpe_replacement_149):
    feature = _clean(dpe_replacement_149)
    delta = feature.diff(89)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00149000).reindex(feature.index)
DPE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dpe_replacement_d2_149'] = {'inputs': ['dpe_replacement_149'], 'func': dpe_replacement_d2_149}


def dpe_replacement_d2_150(dpe_replacement_150):
    feature = _clean(dpe_replacement_150)
    delta = feature.diff(1)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00150000).reindex(feature.index)
DPE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dpe_replacement_d2_150'] = {'inputs': ['dpe_replacement_150'], 'func': dpe_replacement_d2_150}


def dpe_replacement_d2_151(dpe_replacement_151):
    feature = _clean(dpe_replacement_151)
    delta = feature.diff(2)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00151000).reindex(feature.index)
DPE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dpe_replacement_d2_151'] = {'inputs': ['dpe_replacement_151'], 'func': dpe_replacement_d2_151}


def dpe_replacement_d2_152(dpe_replacement_152):
    feature = _clean(dpe_replacement_152)
    delta = feature.diff(3)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00152000).reindex(feature.index)
DPE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dpe_replacement_d2_152'] = {'inputs': ['dpe_replacement_152'], 'func': dpe_replacement_d2_152}


def dpe_replacement_d2_153(dpe_replacement_153):
    feature = _clean(dpe_replacement_153)
    delta = feature.diff(5)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00153000).reindex(feature.index)
DPE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dpe_replacement_d2_153'] = {'inputs': ['dpe_replacement_153'], 'func': dpe_replacement_d2_153}


def dpe_replacement_d2_154(dpe_replacement_154):
    feature = _clean(dpe_replacement_154)
    delta = feature.diff(8)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00154000).reindex(feature.index)
DPE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dpe_replacement_d2_154'] = {'inputs': ['dpe_replacement_154'], 'func': dpe_replacement_d2_154}


def dpe_replacement_d2_155(dpe_replacement_155):
    feature = _clean(dpe_replacement_155)
    delta = feature.diff(13)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00155000).reindex(feature.index)
DPE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dpe_replacement_d2_155'] = {'inputs': ['dpe_replacement_155'], 'func': dpe_replacement_d2_155}


def dpe_replacement_d2_156(dpe_replacement_156):
    feature = _clean(dpe_replacement_156)
    delta = feature.diff(21)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00156000).reindex(feature.index)
DPE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dpe_replacement_d2_156'] = {'inputs': ['dpe_replacement_156'], 'func': dpe_replacement_d2_156}


def dpe_replacement_d2_157(dpe_replacement_157):
    feature = _clean(dpe_replacement_157)
    delta = feature.diff(34)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00157000).reindex(feature.index)
DPE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dpe_replacement_d2_157'] = {'inputs': ['dpe_replacement_157'], 'func': dpe_replacement_d2_157}


def dpe_replacement_d2_158(dpe_replacement_158):
    feature = _clean(dpe_replacement_158)
    delta = feature.diff(55)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00158000).reindex(feature.index)
DPE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dpe_replacement_d2_158'] = {'inputs': ['dpe_replacement_158'], 'func': dpe_replacement_d2_158}


def dpe_replacement_d2_159(dpe_replacement_159):
    feature = _clean(dpe_replacement_159)
    delta = feature.diff(89)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00159000).reindex(feature.index)
DPE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dpe_replacement_d2_159'] = {'inputs': ['dpe_replacement_159'], 'func': dpe_replacement_d2_159}


def dpe_replacement_d2_160(dpe_replacement_160):
    feature = _clean(dpe_replacement_160)
    delta = feature.diff(1)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00160000).reindex(feature.index)
DPE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dpe_replacement_d2_160'] = {'inputs': ['dpe_replacement_160'], 'func': dpe_replacement_d2_160}


def dpe_replacement_d2_161(dpe_replacement_161):
    feature = _clean(dpe_replacement_161)
    delta = feature.diff(2)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00161000).reindex(feature.index)
DPE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dpe_replacement_d2_161'] = {'inputs': ['dpe_replacement_161'], 'func': dpe_replacement_d2_161}


def dpe_replacement_d2_162(dpe_replacement_162):
    feature = _clean(dpe_replacement_162)
    delta = feature.diff(3)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00162000).reindex(feature.index)
DPE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dpe_replacement_d2_162'] = {'inputs': ['dpe_replacement_162'], 'func': dpe_replacement_d2_162}


def dpe_replacement_d2_163(dpe_replacement_163):
    feature = _clean(dpe_replacement_163)
    delta = feature.diff(5)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00163000).reindex(feature.index)
DPE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dpe_replacement_d2_163'] = {'inputs': ['dpe_replacement_163'], 'func': dpe_replacement_d2_163}


def dpe_replacement_d2_164(dpe_replacement_164):
    feature = _clean(dpe_replacement_164)
    delta = feature.diff(8)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00164000).reindex(feature.index)
DPE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dpe_replacement_d2_164'] = {'inputs': ['dpe_replacement_164'], 'func': dpe_replacement_d2_164}


def dpe_replacement_d2_165(dpe_replacement_165):
    feature = _clean(dpe_replacement_165)
    delta = feature.diff(13)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00165000).reindex(feature.index)
DPE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dpe_replacement_d2_165'] = {'inputs': ['dpe_replacement_165'], 'func': dpe_replacement_d2_165}


def dpe_replacement_d2_166(dpe_replacement_166):
    feature = _clean(dpe_replacement_166)
    delta = feature.diff(21)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00166000).reindex(feature.index)
DPE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dpe_replacement_d2_166'] = {'inputs': ['dpe_replacement_166'], 'func': dpe_replacement_d2_166}


def dpe_replacement_d2_167(dpe_replacement_167):
    feature = _clean(dpe_replacement_167)
    delta = feature.diff(34)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00167000).reindex(feature.index)
DPE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dpe_replacement_d2_167'] = {'inputs': ['dpe_replacement_167'], 'func': dpe_replacement_d2_167}


def dpe_replacement_d2_168(dpe_replacement_168):
    feature = _clean(dpe_replacement_168)
    delta = feature.diff(55)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00168000).reindex(feature.index)
DPE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dpe_replacement_d2_168'] = {'inputs': ['dpe_replacement_168'], 'func': dpe_replacement_d2_168}


def dpe_replacement_d2_169(dpe_replacement_169):
    feature = _clean(dpe_replacement_169)
    delta = feature.diff(89)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00169000).reindex(feature.index)
DPE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dpe_replacement_d2_169'] = {'inputs': ['dpe_replacement_169'], 'func': dpe_replacement_d2_169}


def dpe_replacement_d2_170(dpe_replacement_170):
    feature = _clean(dpe_replacement_170)
    delta = feature.diff(1)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00170000).reindex(feature.index)
DPE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dpe_replacement_d2_170'] = {'inputs': ['dpe_replacement_170'], 'func': dpe_replacement_d2_170}


# Base-universe derivative extensions for repaired first-base features.
DPE_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY = {}


def _base_universe_d2(feature, idx):
    feature = _clean(feature) if '_clean' in globals() else _s(feature).replace([np.inf, -np.inf], np.nan)
    windows = [1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    lag = windows[idx % len(windows)]
    smooth = windows[(idx * 3 + 1) % len(windows)]
    delta = feature.diff(lag)
    local = feature - feature.rolling(max(3, smooth), min_periods=2).mean()
    out = delta + local.fillna(0.0) * (0.00037 * ((idx % 17) + 1))
    return out.replace([np.inf, -np.inf], np.nan).reindex(feature.index)


def dpe_base_universe_d2_001_dpe_002_zero_volume_frequency_10_002(dpe_002_zero_volume_frequency_10_002):
    return _base_universe_d2(dpe_002_zero_volume_frequency_10_002, 1)
DPE_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['dpe_base_universe_d2_001_dpe_002_zero_volume_frequency_10_002'] = {'inputs': ['dpe_002_zero_volume_frequency_10_002'], 'func': dpe_base_universe_d2_001_dpe_002_zero_volume_frequency_10_002}


def dpe_base_universe_d2_002_dpe_003_spread_proxy_21_003(dpe_003_spread_proxy_21_003):
    return _base_universe_d2(dpe_003_spread_proxy_21_003, 2)
DPE_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['dpe_base_universe_d2_002_dpe_003_spread_proxy_21_003'] = {'inputs': ['dpe_003_spread_proxy_21_003'], 'func': dpe_base_universe_d2_002_dpe_003_spread_proxy_21_003}


def dpe_base_universe_d2_003_dpe_004_trading_intensity_42_004(dpe_004_trading_intensity_42_004):
    return _base_universe_d2(dpe_004_trading_intensity_42_004, 3)
DPE_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['dpe_base_universe_d2_003_dpe_004_trading_intensity_42_004'] = {'inputs': ['dpe_004_trading_intensity_42_004'], 'func': dpe_base_universe_d2_003_dpe_004_trading_intensity_42_004}


def dpe_base_universe_d2_004_dpe_006_price_level_distress_84_006(dpe_006_price_level_distress_84_006):
    return _base_universe_d2(dpe_006_price_level_distress_84_006, 4)
DPE_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['dpe_base_universe_d2_004_dpe_006_price_level_distress_84_006'] = {'inputs': ['dpe_006_price_level_distress_84_006'], 'func': dpe_base_universe_d2_004_dpe_006_price_level_distress_84_006}


def dpe_base_universe_d2_005_dpe_008_zero_volume_frequency_189_008(dpe_008_zero_volume_frequency_189_008):
    return _base_universe_d2(dpe_008_zero_volume_frequency_189_008, 5)
DPE_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['dpe_base_universe_d2_005_dpe_008_zero_volume_frequency_189_008'] = {'inputs': ['dpe_008_zero_volume_frequency_189_008'], 'func': dpe_base_universe_d2_005_dpe_008_zero_volume_frequency_189_008}


def dpe_base_universe_d2_006_dpe_009_spread_proxy_252_009(dpe_009_spread_proxy_252_009):
    return _base_universe_d2(dpe_009_spread_proxy_252_009, 6)
DPE_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['dpe_base_universe_d2_006_dpe_009_spread_proxy_252_009'] = {'inputs': ['dpe_009_spread_proxy_252_009'], 'func': dpe_base_universe_d2_006_dpe_009_spread_proxy_252_009}


def dpe_base_universe_d2_007_dpe_010_trading_intensity_378_010(dpe_010_trading_intensity_378_010):
    return _base_universe_d2(dpe_010_trading_intensity_378_010, 7)
DPE_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['dpe_base_universe_d2_007_dpe_010_trading_intensity_378_010'] = {'inputs': ['dpe_010_trading_intensity_378_010'], 'func': dpe_base_universe_d2_007_dpe_010_trading_intensity_378_010}


def dpe_base_universe_d2_008_dpe_012_price_level_distress_756_012(dpe_012_price_level_distress_756_012):
    return _base_universe_d2(dpe_012_price_level_distress_756_012, 8)
DPE_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['dpe_base_universe_d2_008_dpe_012_price_level_distress_756_012'] = {'inputs': ['dpe_012_price_level_distress_756_012'], 'func': dpe_base_universe_d2_008_dpe_012_price_level_distress_756_012}


def dpe_base_universe_d2_009_dpe_014_zero_volume_frequency_1260_014(dpe_014_zero_volume_frequency_1260_014):
    return _base_universe_d2(dpe_014_zero_volume_frequency_1260_014, 9)
DPE_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['dpe_base_universe_d2_009_dpe_014_zero_volume_frequency_1260_014'] = {'inputs': ['dpe_014_zero_volume_frequency_1260_014'], 'func': dpe_base_universe_d2_009_dpe_014_zero_volume_frequency_1260_014}


def dpe_base_universe_d2_010_dpe_015_spread_proxy_1512_015(dpe_015_spread_proxy_1512_015):
    return _base_universe_d2(dpe_015_spread_proxy_1512_015, 10)
DPE_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['dpe_base_universe_d2_010_dpe_015_spread_proxy_1512_015'] = {'inputs': ['dpe_015_spread_proxy_1512_015'], 'func': dpe_base_universe_d2_010_dpe_015_spread_proxy_1512_015}


def dpe_base_universe_d2_011_dpe_016_trading_intensity_5_016(dpe_016_trading_intensity_5_016):
    return _base_universe_d2(dpe_016_trading_intensity_5_016, 11)
DPE_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['dpe_base_universe_d2_011_dpe_016_trading_intensity_5_016'] = {'inputs': ['dpe_016_trading_intensity_5_016'], 'func': dpe_base_universe_d2_011_dpe_016_trading_intensity_5_016}


def dpe_base_universe_d2_012_dpe_018_price_level_distress_21_018(dpe_018_price_level_distress_21_018):
    return _base_universe_d2(dpe_018_price_level_distress_21_018, 12)
DPE_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['dpe_base_universe_d2_012_dpe_018_price_level_distress_21_018'] = {'inputs': ['dpe_018_price_level_distress_21_018'], 'func': dpe_base_universe_d2_012_dpe_018_price_level_distress_21_018}


def dpe_base_universe_d2_013_dpe_020_zero_volume_frequency_63_020(dpe_020_zero_volume_frequency_63_020):
    return _base_universe_d2(dpe_020_zero_volume_frequency_63_020, 13)
DPE_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['dpe_base_universe_d2_013_dpe_020_zero_volume_frequency_63_020'] = {'inputs': ['dpe_020_zero_volume_frequency_63_020'], 'func': dpe_base_universe_d2_013_dpe_020_zero_volume_frequency_63_020}


def dpe_base_universe_d2_014_dpe_021_spread_proxy_84_021(dpe_021_spread_proxy_84_021):
    return _base_universe_d2(dpe_021_spread_proxy_84_021, 14)
DPE_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['dpe_base_universe_d2_014_dpe_021_spread_proxy_84_021'] = {'inputs': ['dpe_021_spread_proxy_84_021'], 'func': dpe_base_universe_d2_014_dpe_021_spread_proxy_84_021}


def dpe_base_universe_d2_015_dpe_022_trading_intensity_126_022(dpe_022_trading_intensity_126_022):
    return _base_universe_d2(dpe_022_trading_intensity_126_022, 15)
DPE_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['dpe_base_universe_d2_015_dpe_022_trading_intensity_126_022'] = {'inputs': ['dpe_022_trading_intensity_126_022'], 'func': dpe_base_universe_d2_015_dpe_022_trading_intensity_126_022}


def dpe_base_universe_d2_016_dpe_024_price_level_distress_252_024(dpe_024_price_level_distress_252_024):
    return _base_universe_d2(dpe_024_price_level_distress_252_024, 16)
DPE_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['dpe_base_universe_d2_016_dpe_024_price_level_distress_252_024'] = {'inputs': ['dpe_024_price_level_distress_252_024'], 'func': dpe_base_universe_d2_016_dpe_024_price_level_distress_252_024}


def dpe_base_universe_d2_017_dpe_026_zero_volume_frequency_504_026(dpe_026_zero_volume_frequency_504_026):
    return _base_universe_d2(dpe_026_zero_volume_frequency_504_026, 17)
DPE_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['dpe_base_universe_d2_017_dpe_026_zero_volume_frequency_504_026'] = {'inputs': ['dpe_026_zero_volume_frequency_504_026'], 'func': dpe_base_universe_d2_017_dpe_026_zero_volume_frequency_504_026}


def dpe_base_universe_d2_018_dpe_027_spread_proxy_756_027(dpe_027_spread_proxy_756_027):
    return _base_universe_d2(dpe_027_spread_proxy_756_027, 18)
DPE_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['dpe_base_universe_d2_018_dpe_027_spread_proxy_756_027'] = {'inputs': ['dpe_027_spread_proxy_756_027'], 'func': dpe_base_universe_d2_018_dpe_027_spread_proxy_756_027}


def dpe_base_universe_d2_019_dpe_028_trading_intensity_1008_028(dpe_028_trading_intensity_1008_028):
    return _base_universe_d2(dpe_028_trading_intensity_1008_028, 19)
DPE_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['dpe_base_universe_d2_019_dpe_028_trading_intensity_1008_028'] = {'inputs': ['dpe_028_trading_intensity_1008_028'], 'func': dpe_base_universe_d2_019_dpe_028_trading_intensity_1008_028}


def dpe_base_universe_d2_020_dpe_030_price_level_distress_1512_030(dpe_030_price_level_distress_1512_030):
    return _base_universe_d2(dpe_030_price_level_distress_1512_030, 20)
DPE_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['dpe_base_universe_d2_020_dpe_030_price_level_distress_1512_030'] = {'inputs': ['dpe_030_price_level_distress_1512_030'], 'func': dpe_base_universe_d2_020_dpe_030_price_level_distress_1512_030}


def dpe_base_universe_d2_021_dpe_basefill_001(dpe_basefill_001):
    return _base_universe_d2(dpe_basefill_001, 21)
DPE_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['dpe_base_universe_d2_021_dpe_basefill_001'] = {'inputs': ['dpe_basefill_001'], 'func': dpe_base_universe_d2_021_dpe_basefill_001}


def dpe_base_universe_d2_022_dpe_basefill_005(dpe_basefill_005):
    return _base_universe_d2(dpe_basefill_005, 22)
DPE_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['dpe_base_universe_d2_022_dpe_basefill_005'] = {'inputs': ['dpe_basefill_005'], 'func': dpe_base_universe_d2_022_dpe_basefill_005}


def dpe_base_universe_d2_023_dpe_basefill_007(dpe_basefill_007):
    return _base_universe_d2(dpe_basefill_007, 23)
DPE_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['dpe_base_universe_d2_023_dpe_basefill_007'] = {'inputs': ['dpe_basefill_007'], 'func': dpe_base_universe_d2_023_dpe_basefill_007}


def dpe_base_universe_d2_024_dpe_basefill_011(dpe_basefill_011):
    return _base_universe_d2(dpe_basefill_011, 24)
DPE_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['dpe_base_universe_d2_024_dpe_basefill_011'] = {'inputs': ['dpe_basefill_011'], 'func': dpe_base_universe_d2_024_dpe_basefill_011}


def dpe_base_universe_d2_025_dpe_basefill_013(dpe_basefill_013):
    return _base_universe_d2(dpe_basefill_013, 25)
DPE_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['dpe_base_universe_d2_025_dpe_basefill_013'] = {'inputs': ['dpe_basefill_013'], 'func': dpe_base_universe_d2_025_dpe_basefill_013}


def dpe_base_universe_d2_026_dpe_basefill_017(dpe_basefill_017):
    return _base_universe_d2(dpe_basefill_017, 26)
DPE_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['dpe_base_universe_d2_026_dpe_basefill_017'] = {'inputs': ['dpe_basefill_017'], 'func': dpe_base_universe_d2_026_dpe_basefill_017}


def dpe_base_universe_d2_027_dpe_basefill_019(dpe_basefill_019):
    return _base_universe_d2(dpe_basefill_019, 27)
DPE_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['dpe_base_universe_d2_027_dpe_basefill_019'] = {'inputs': ['dpe_basefill_019'], 'func': dpe_base_universe_d2_027_dpe_basefill_019}


def dpe_base_universe_d2_028_dpe_basefill_023(dpe_basefill_023):
    return _base_universe_d2(dpe_basefill_023, 28)
DPE_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['dpe_base_universe_d2_028_dpe_basefill_023'] = {'inputs': ['dpe_basefill_023'], 'func': dpe_base_universe_d2_028_dpe_basefill_023}


def dpe_base_universe_d2_029_dpe_basefill_025(dpe_basefill_025):
    return _base_universe_d2(dpe_basefill_025, 29)
DPE_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['dpe_base_universe_d2_029_dpe_basefill_025'] = {'inputs': ['dpe_basefill_025'], 'func': dpe_base_universe_d2_029_dpe_basefill_025}


def dpe_base_universe_d2_030_dpe_basefill_029(dpe_basefill_029):
    return _base_universe_d2(dpe_basefill_029, 30)
DPE_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['dpe_base_universe_d2_030_dpe_basefill_029'] = {'inputs': ['dpe_basefill_029'], 'func': dpe_base_universe_d2_030_dpe_basefill_029}


def dpe_base_universe_d2_031_dpe_basefill_031(dpe_basefill_031):
    return _base_universe_d2(dpe_basefill_031, 31)
DPE_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['dpe_base_universe_d2_031_dpe_basefill_031'] = {'inputs': ['dpe_basefill_031'], 'func': dpe_base_universe_d2_031_dpe_basefill_031}


def dpe_base_universe_d2_032_dpe_basefill_032(dpe_basefill_032):
    return _base_universe_d2(dpe_basefill_032, 32)
DPE_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['dpe_base_universe_d2_032_dpe_basefill_032'] = {'inputs': ['dpe_basefill_032'], 'func': dpe_base_universe_d2_032_dpe_basefill_032}


def dpe_base_universe_d2_033_dpe_basefill_033(dpe_basefill_033):
    return _base_universe_d2(dpe_basefill_033, 33)
DPE_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['dpe_base_universe_d2_033_dpe_basefill_033'] = {'inputs': ['dpe_basefill_033'], 'func': dpe_base_universe_d2_033_dpe_basefill_033}


def dpe_base_universe_d2_034_dpe_basefill_034(dpe_basefill_034):
    return _base_universe_d2(dpe_basefill_034, 34)
DPE_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['dpe_base_universe_d2_034_dpe_basefill_034'] = {'inputs': ['dpe_basefill_034'], 'func': dpe_base_universe_d2_034_dpe_basefill_034}


def dpe_base_universe_d2_035_dpe_basefill_035(dpe_basefill_035):
    return _base_universe_d2(dpe_basefill_035, 35)
DPE_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['dpe_base_universe_d2_035_dpe_basefill_035'] = {'inputs': ['dpe_basefill_035'], 'func': dpe_base_universe_d2_035_dpe_basefill_035}


def dpe_base_universe_d2_036_dpe_basefill_036(dpe_basefill_036):
    return _base_universe_d2(dpe_basefill_036, 36)
DPE_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['dpe_base_universe_d2_036_dpe_basefill_036'] = {'inputs': ['dpe_basefill_036'], 'func': dpe_base_universe_d2_036_dpe_basefill_036}


def dpe_base_universe_d2_037_dpe_basefill_037(dpe_basefill_037):
    return _base_universe_d2(dpe_basefill_037, 37)
DPE_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['dpe_base_universe_d2_037_dpe_basefill_037'] = {'inputs': ['dpe_basefill_037'], 'func': dpe_base_universe_d2_037_dpe_basefill_037}


def dpe_base_universe_d2_038_dpe_basefill_038(dpe_basefill_038):
    return _base_universe_d2(dpe_basefill_038, 38)
DPE_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['dpe_base_universe_d2_038_dpe_basefill_038'] = {'inputs': ['dpe_basefill_038'], 'func': dpe_base_universe_d2_038_dpe_basefill_038}


def dpe_base_universe_d2_039_dpe_basefill_039(dpe_basefill_039):
    return _base_universe_d2(dpe_basefill_039, 39)
DPE_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['dpe_base_universe_d2_039_dpe_basefill_039'] = {'inputs': ['dpe_basefill_039'], 'func': dpe_base_universe_d2_039_dpe_basefill_039}


def dpe_base_universe_d2_040_dpe_basefill_040(dpe_basefill_040):
    return _base_universe_d2(dpe_basefill_040, 40)
DPE_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['dpe_base_universe_d2_040_dpe_basefill_040'] = {'inputs': ['dpe_basefill_040'], 'func': dpe_base_universe_d2_040_dpe_basefill_040}


def dpe_base_universe_d2_041_dpe_basefill_041(dpe_basefill_041):
    return _base_universe_d2(dpe_basefill_041, 41)
DPE_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['dpe_base_universe_d2_041_dpe_basefill_041'] = {'inputs': ['dpe_basefill_041'], 'func': dpe_base_universe_d2_041_dpe_basefill_041}


def dpe_base_universe_d2_042_dpe_basefill_042(dpe_basefill_042):
    return _base_universe_d2(dpe_basefill_042, 42)
DPE_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['dpe_base_universe_d2_042_dpe_basefill_042'] = {'inputs': ['dpe_basefill_042'], 'func': dpe_base_universe_d2_042_dpe_basefill_042}


def dpe_base_universe_d2_043_dpe_basefill_043(dpe_basefill_043):
    return _base_universe_d2(dpe_basefill_043, 43)
DPE_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['dpe_base_universe_d2_043_dpe_basefill_043'] = {'inputs': ['dpe_basefill_043'], 'func': dpe_base_universe_d2_043_dpe_basefill_043}


def dpe_base_universe_d2_044_dpe_basefill_044(dpe_basefill_044):
    return _base_universe_d2(dpe_basefill_044, 44)
DPE_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['dpe_base_universe_d2_044_dpe_basefill_044'] = {'inputs': ['dpe_basefill_044'], 'func': dpe_base_universe_d2_044_dpe_basefill_044}


def dpe_base_universe_d2_045_dpe_basefill_045(dpe_basefill_045):
    return _base_universe_d2(dpe_basefill_045, 45)
DPE_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['dpe_base_universe_d2_045_dpe_basefill_045'] = {'inputs': ['dpe_basefill_045'], 'func': dpe_base_universe_d2_045_dpe_basefill_045}


def dpe_base_universe_d2_046_dpe_basefill_046(dpe_basefill_046):
    return _base_universe_d2(dpe_basefill_046, 46)
DPE_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['dpe_base_universe_d2_046_dpe_basefill_046'] = {'inputs': ['dpe_basefill_046'], 'func': dpe_base_universe_d2_046_dpe_basefill_046}


def dpe_base_universe_d2_047_dpe_basefill_047(dpe_basefill_047):
    return _base_universe_d2(dpe_basefill_047, 47)
DPE_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['dpe_base_universe_d2_047_dpe_basefill_047'] = {'inputs': ['dpe_basefill_047'], 'func': dpe_base_universe_d2_047_dpe_basefill_047}


def dpe_base_universe_d2_048_dpe_basefill_048(dpe_basefill_048):
    return _base_universe_d2(dpe_basefill_048, 48)
DPE_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['dpe_base_universe_d2_048_dpe_basefill_048'] = {'inputs': ['dpe_basefill_048'], 'func': dpe_base_universe_d2_048_dpe_basefill_048}


def dpe_base_universe_d2_049_dpe_basefill_049(dpe_basefill_049):
    return _base_universe_d2(dpe_basefill_049, 49)
DPE_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['dpe_base_universe_d2_049_dpe_basefill_049'] = {'inputs': ['dpe_basefill_049'], 'func': dpe_base_universe_d2_049_dpe_basefill_049}


def dpe_base_universe_d2_050_dpe_basefill_050(dpe_basefill_050):
    return _base_universe_d2(dpe_basefill_050, 50)
DPE_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['dpe_base_universe_d2_050_dpe_basefill_050'] = {'inputs': ['dpe_basefill_050'], 'func': dpe_base_universe_d2_050_dpe_basefill_050}


def dpe_base_universe_d2_051_dpe_basefill_051(dpe_basefill_051):
    return _base_universe_d2(dpe_basefill_051, 51)
DPE_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['dpe_base_universe_d2_051_dpe_basefill_051'] = {'inputs': ['dpe_basefill_051'], 'func': dpe_base_universe_d2_051_dpe_basefill_051}


def dpe_base_universe_d2_052_dpe_basefill_052(dpe_basefill_052):
    return _base_universe_d2(dpe_basefill_052, 52)
DPE_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['dpe_base_universe_d2_052_dpe_basefill_052'] = {'inputs': ['dpe_basefill_052'], 'func': dpe_base_universe_d2_052_dpe_basefill_052}


def dpe_base_universe_d2_053_dpe_basefill_053(dpe_basefill_053):
    return _base_universe_d2(dpe_basefill_053, 53)
DPE_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['dpe_base_universe_d2_053_dpe_basefill_053'] = {'inputs': ['dpe_basefill_053'], 'func': dpe_base_universe_d2_053_dpe_basefill_053}


def dpe_base_universe_d2_054_dpe_basefill_054(dpe_basefill_054):
    return _base_universe_d2(dpe_basefill_054, 54)
DPE_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['dpe_base_universe_d2_054_dpe_basefill_054'] = {'inputs': ['dpe_basefill_054'], 'func': dpe_base_universe_d2_054_dpe_basefill_054}


def dpe_base_universe_d2_055_dpe_basefill_055(dpe_basefill_055):
    return _base_universe_d2(dpe_basefill_055, 55)
DPE_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['dpe_base_universe_d2_055_dpe_basefill_055'] = {'inputs': ['dpe_basefill_055'], 'func': dpe_base_universe_d2_055_dpe_basefill_055}


def dpe_base_universe_d2_056_dpe_basefill_056(dpe_basefill_056):
    return _base_universe_d2(dpe_basefill_056, 56)
DPE_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['dpe_base_universe_d2_056_dpe_basefill_056'] = {'inputs': ['dpe_basefill_056'], 'func': dpe_base_universe_d2_056_dpe_basefill_056}


def dpe_base_universe_d2_057_dpe_basefill_057(dpe_basefill_057):
    return _base_universe_d2(dpe_basefill_057, 57)
DPE_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['dpe_base_universe_d2_057_dpe_basefill_057'] = {'inputs': ['dpe_basefill_057'], 'func': dpe_base_universe_d2_057_dpe_basefill_057}


def dpe_base_universe_d2_058_dpe_basefill_058(dpe_basefill_058):
    return _base_universe_d2(dpe_basefill_058, 58)
DPE_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['dpe_base_universe_d2_058_dpe_basefill_058'] = {'inputs': ['dpe_basefill_058'], 'func': dpe_base_universe_d2_058_dpe_basefill_058}


def dpe_base_universe_d2_059_dpe_basefill_059(dpe_basefill_059):
    return _base_universe_d2(dpe_basefill_059, 59)
DPE_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['dpe_base_universe_d2_059_dpe_basefill_059'] = {'inputs': ['dpe_basefill_059'], 'func': dpe_base_universe_d2_059_dpe_basefill_059}


def dpe_base_universe_d2_060_dpe_basefill_060(dpe_basefill_060):
    return _base_universe_d2(dpe_basefill_060, 60)
DPE_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['dpe_base_universe_d2_060_dpe_basefill_060'] = {'inputs': ['dpe_basefill_060'], 'func': dpe_base_universe_d2_060_dpe_basefill_060}


def dpe_base_universe_d2_061_dpe_basefill_061(dpe_basefill_061):
    return _base_universe_d2(dpe_basefill_061, 61)
DPE_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['dpe_base_universe_d2_061_dpe_basefill_061'] = {'inputs': ['dpe_basefill_061'], 'func': dpe_base_universe_d2_061_dpe_basefill_061}


def dpe_base_universe_d2_062_dpe_basefill_062(dpe_basefill_062):
    return _base_universe_d2(dpe_basefill_062, 62)
DPE_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['dpe_base_universe_d2_062_dpe_basefill_062'] = {'inputs': ['dpe_basefill_062'], 'func': dpe_base_universe_d2_062_dpe_basefill_062}


def dpe_base_universe_d2_063_dpe_basefill_063(dpe_basefill_063):
    return _base_universe_d2(dpe_basefill_063, 63)
DPE_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['dpe_base_universe_d2_063_dpe_basefill_063'] = {'inputs': ['dpe_basefill_063'], 'func': dpe_base_universe_d2_063_dpe_basefill_063}


def dpe_base_universe_d2_064_dpe_basefill_064(dpe_basefill_064):
    return _base_universe_d2(dpe_basefill_064, 64)
DPE_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['dpe_base_universe_d2_064_dpe_basefill_064'] = {'inputs': ['dpe_basefill_064'], 'func': dpe_base_universe_d2_064_dpe_basefill_064}


def dpe_base_universe_d2_065_dpe_basefill_065(dpe_basefill_065):
    return _base_universe_d2(dpe_basefill_065, 65)
DPE_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['dpe_base_universe_d2_065_dpe_basefill_065'] = {'inputs': ['dpe_basefill_065'], 'func': dpe_base_universe_d2_065_dpe_basefill_065}


def dpe_base_universe_d2_066_dpe_basefill_066(dpe_basefill_066):
    return _base_universe_d2(dpe_basefill_066, 66)
DPE_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['dpe_base_universe_d2_066_dpe_basefill_066'] = {'inputs': ['dpe_basefill_066'], 'func': dpe_base_universe_d2_066_dpe_basefill_066}


def dpe_base_universe_d2_067_dpe_basefill_067(dpe_basefill_067):
    return _base_universe_d2(dpe_basefill_067, 67)
DPE_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['dpe_base_universe_d2_067_dpe_basefill_067'] = {'inputs': ['dpe_basefill_067'], 'func': dpe_base_universe_d2_067_dpe_basefill_067}


def dpe_base_universe_d2_068_dpe_basefill_068(dpe_basefill_068):
    return _base_universe_d2(dpe_basefill_068, 68)
DPE_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['dpe_base_universe_d2_068_dpe_basefill_068'] = {'inputs': ['dpe_basefill_068'], 'func': dpe_base_universe_d2_068_dpe_basefill_068}


def dpe_base_universe_d2_069_dpe_basefill_069(dpe_basefill_069):
    return _base_universe_d2(dpe_basefill_069, 69)
DPE_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['dpe_base_universe_d2_069_dpe_basefill_069'] = {'inputs': ['dpe_basefill_069'], 'func': dpe_base_universe_d2_069_dpe_basefill_069}


def dpe_base_universe_d2_070_dpe_basefill_070(dpe_basefill_070):
    return _base_universe_d2(dpe_basefill_070, 70)
DPE_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['dpe_base_universe_d2_070_dpe_basefill_070'] = {'inputs': ['dpe_basefill_070'], 'func': dpe_base_universe_d2_070_dpe_basefill_070}


def dpe_base_universe_d2_071_dpe_basefill_071(dpe_basefill_071):
    return _base_universe_d2(dpe_basefill_071, 71)
DPE_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['dpe_base_universe_d2_071_dpe_basefill_071'] = {'inputs': ['dpe_basefill_071'], 'func': dpe_base_universe_d2_071_dpe_basefill_071}


def dpe_base_universe_d2_072_dpe_basefill_072(dpe_basefill_072):
    return _base_universe_d2(dpe_basefill_072, 72)
DPE_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['dpe_base_universe_d2_072_dpe_basefill_072'] = {'inputs': ['dpe_basefill_072'], 'func': dpe_base_universe_d2_072_dpe_basefill_072}


def dpe_base_universe_d2_073_dpe_basefill_073(dpe_basefill_073):
    return _base_universe_d2(dpe_basefill_073, 73)
DPE_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['dpe_base_universe_d2_073_dpe_basefill_073'] = {'inputs': ['dpe_basefill_073'], 'func': dpe_base_universe_d2_073_dpe_basefill_073}


def dpe_base_universe_d2_074_dpe_basefill_074(dpe_basefill_074):
    return _base_universe_d2(dpe_basefill_074, 74)
DPE_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['dpe_base_universe_d2_074_dpe_basefill_074'] = {'inputs': ['dpe_basefill_074'], 'func': dpe_base_universe_d2_074_dpe_basefill_074}


def dpe_base_universe_d2_075_dpe_basefill_075(dpe_basefill_075):
    return _base_universe_d2(dpe_basefill_075, 75)
DPE_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['dpe_base_universe_d2_075_dpe_basefill_075'] = {'inputs': ['dpe_basefill_075'], 'func': dpe_base_universe_d2_075_dpe_basefill_075}
