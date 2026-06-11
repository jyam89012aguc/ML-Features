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



def dstk_001_amihud_illiquidity_roc_1(amihud_illiquidity):
    feature = _s(amihud_illiquidity)
    return (_roc(feature, 1)).reindex(feature.index)

def dstk_007_amihud_illiquidity_roc_5(amihud_illiquidity):
    feature = _s(amihud_illiquidity)
    return (_roc(feature, 5)).reindex(feature.index)

def dstk_013_amihud_illiquidity_roc_42(amihud_illiquidity):
    feature = _s(amihud_illiquidity)
    return (_roc(feature, 42)).reindex(feature.index)

def dstk_154_dstk_019_amihud_illiquidity_42_019_roc_126(amihud_illiquidity):
    feature = _s(amihud_illiquidity)
    return (_roc(feature, 126)).reindex(feature.index)

def dstk_155_dstk_025_amihud_illiquidity_378_025_roc_378(amihud_illiquidity):
    feature = _s(amihud_illiquidity)
    return (_roc(feature, 378)).reindex(feature.index)






















DECLINE_STREAKS_REGISTRY_2ND_DERIVATIVES = {
    'dstk_001_amihud_illiquidity_roc_1': {'inputs': ['amihud_illiquidity'], 'func': dstk_001_amihud_illiquidity_roc_1},
    'dstk_007_amihud_illiquidity_roc_5': {'inputs': ['amihud_illiquidity'], 'func': dstk_007_amihud_illiquidity_roc_5},
    'dstk_013_amihud_illiquidity_roc_42': {'inputs': ['amihud_illiquidity'], 'func': dstk_013_amihud_illiquidity_roc_42},
    'dstk_154_dstk_019_amihud_illiquidity_42_019_roc_126': {'inputs': ['amihud_illiquidity'], 'func': dstk_154_dstk_019_amihud_illiquidity_42_019_roc_126},
    'dstk_155_dstk_025_amihud_illiquidity_378_025_roc_378': {'inputs': ['amihud_illiquidity'], 'func': dstk_155_dstk_025_amihud_illiquidity_378_025_roc_378},
}


# Replacement 2nd-derivative features restored after redundancy audit.

import numpy as np
import pandas as pd


def _s(x):
    return pd.Series(x).astype(float)


def _clean(x):
    return _s(x).replace([np.inf, -np.inf], np.nan)


DS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY = {}


def ds_replacement_d2_001(ds_replacement_001):
    feature = _clean(ds_replacement_001)
    delta = feature.diff(2)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00001000).reindex(feature.index)
DS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ds_replacement_d2_001'] = {'inputs': ['ds_replacement_001'], 'func': ds_replacement_d2_001}


def ds_replacement_d2_002(ds_replacement_002):
    feature = _clean(ds_replacement_002)
    delta = feature.diff(3)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00002000).reindex(feature.index)
DS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ds_replacement_d2_002'] = {'inputs': ['ds_replacement_002'], 'func': ds_replacement_d2_002}


def ds_replacement_d2_003(ds_replacement_003):
    feature = _clean(ds_replacement_003)
    delta = feature.diff(5)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00003000).reindex(feature.index)
DS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ds_replacement_d2_003'] = {'inputs': ['ds_replacement_003'], 'func': ds_replacement_d2_003}


def ds_replacement_d2_004(ds_replacement_004):
    feature = _clean(ds_replacement_004)
    delta = feature.diff(8)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00004000).reindex(feature.index)
DS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ds_replacement_d2_004'] = {'inputs': ['ds_replacement_004'], 'func': ds_replacement_d2_004}


def ds_replacement_d2_005(ds_replacement_005):
    feature = _clean(ds_replacement_005)
    delta = feature.diff(13)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00005000).reindex(feature.index)
DS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ds_replacement_d2_005'] = {'inputs': ['ds_replacement_005'], 'func': ds_replacement_d2_005}


def ds_replacement_d2_006(ds_replacement_006):
    feature = _clean(ds_replacement_006)
    delta = feature.diff(21)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00006000).reindex(feature.index)
DS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ds_replacement_d2_006'] = {'inputs': ['ds_replacement_006'], 'func': ds_replacement_d2_006}


def ds_replacement_d2_007(ds_replacement_007):
    feature = _clean(ds_replacement_007)
    delta = feature.diff(34)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00007000).reindex(feature.index)
DS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ds_replacement_d2_007'] = {'inputs': ['ds_replacement_007'], 'func': ds_replacement_d2_007}


def ds_replacement_d2_008(ds_replacement_008):
    feature = _clean(ds_replacement_008)
    delta = feature.diff(55)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00008000).reindex(feature.index)
DS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ds_replacement_d2_008'] = {'inputs': ['ds_replacement_008'], 'func': ds_replacement_d2_008}


def ds_replacement_d2_009(ds_replacement_009):
    feature = _clean(ds_replacement_009)
    delta = feature.diff(89)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00009000).reindex(feature.index)
DS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ds_replacement_d2_009'] = {'inputs': ['ds_replacement_009'], 'func': ds_replacement_d2_009}


def ds_replacement_d2_010(ds_replacement_010):
    feature = _clean(ds_replacement_010)
    delta = feature.diff(1)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00010000).reindex(feature.index)
DS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ds_replacement_d2_010'] = {'inputs': ['ds_replacement_010'], 'func': ds_replacement_d2_010}


def ds_replacement_d2_011(ds_replacement_011):
    feature = _clean(ds_replacement_011)
    delta = feature.diff(2)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00011000).reindex(feature.index)
DS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ds_replacement_d2_011'] = {'inputs': ['ds_replacement_011'], 'func': ds_replacement_d2_011}


def ds_replacement_d2_012(ds_replacement_012):
    feature = _clean(ds_replacement_012)
    delta = feature.diff(3)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00012000).reindex(feature.index)
DS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ds_replacement_d2_012'] = {'inputs': ['ds_replacement_012'], 'func': ds_replacement_d2_012}


def ds_replacement_d2_013(ds_replacement_013):
    feature = _clean(ds_replacement_013)
    delta = feature.diff(5)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00013000).reindex(feature.index)
DS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ds_replacement_d2_013'] = {'inputs': ['ds_replacement_013'], 'func': ds_replacement_d2_013}


def ds_replacement_d2_014(ds_replacement_014):
    feature = _clean(ds_replacement_014)
    delta = feature.diff(8)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00014000).reindex(feature.index)
DS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ds_replacement_d2_014'] = {'inputs': ['ds_replacement_014'], 'func': ds_replacement_d2_014}


def ds_replacement_d2_015(ds_replacement_015):
    feature = _clean(ds_replacement_015)
    delta = feature.diff(13)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00015000).reindex(feature.index)
DS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ds_replacement_d2_015'] = {'inputs': ['ds_replacement_015'], 'func': ds_replacement_d2_015}


def ds_replacement_d2_016(ds_replacement_016):
    feature = _clean(ds_replacement_016)
    delta = feature.diff(21)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00016000).reindex(feature.index)
DS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ds_replacement_d2_016'] = {'inputs': ['ds_replacement_016'], 'func': ds_replacement_d2_016}


def ds_replacement_d2_017(ds_replacement_017):
    feature = _clean(ds_replacement_017)
    delta = feature.diff(34)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00017000).reindex(feature.index)
DS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ds_replacement_d2_017'] = {'inputs': ['ds_replacement_017'], 'func': ds_replacement_d2_017}


def ds_replacement_d2_018(ds_replacement_018):
    feature = _clean(ds_replacement_018)
    delta = feature.diff(55)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00018000).reindex(feature.index)
DS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ds_replacement_d2_018'] = {'inputs': ['ds_replacement_018'], 'func': ds_replacement_d2_018}


def ds_replacement_d2_019(ds_replacement_019):
    feature = _clean(ds_replacement_019)
    delta = feature.diff(89)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00019000).reindex(feature.index)
DS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ds_replacement_d2_019'] = {'inputs': ['ds_replacement_019'], 'func': ds_replacement_d2_019}


def ds_replacement_d2_020(ds_replacement_020):
    feature = _clean(ds_replacement_020)
    delta = feature.diff(1)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00020000).reindex(feature.index)
DS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ds_replacement_d2_020'] = {'inputs': ['ds_replacement_020'], 'func': ds_replacement_d2_020}


def ds_replacement_d2_021(ds_replacement_021):
    feature = _clean(ds_replacement_021)
    delta = feature.diff(2)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00021000).reindex(feature.index)
DS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ds_replacement_d2_021'] = {'inputs': ['ds_replacement_021'], 'func': ds_replacement_d2_021}


def ds_replacement_d2_022(ds_replacement_022):
    feature = _clean(ds_replacement_022)
    delta = feature.diff(3)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00022000).reindex(feature.index)
DS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ds_replacement_d2_022'] = {'inputs': ['ds_replacement_022'], 'func': ds_replacement_d2_022}


def ds_replacement_d2_023(ds_replacement_023):
    feature = _clean(ds_replacement_023)
    delta = feature.diff(5)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00023000).reindex(feature.index)
DS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ds_replacement_d2_023'] = {'inputs': ['ds_replacement_023'], 'func': ds_replacement_d2_023}


def ds_replacement_d2_024(ds_replacement_024):
    feature = _clean(ds_replacement_024)
    delta = feature.diff(8)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00024000).reindex(feature.index)
DS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ds_replacement_d2_024'] = {'inputs': ['ds_replacement_024'], 'func': ds_replacement_d2_024}


def ds_replacement_d2_025(ds_replacement_025):
    feature = _clean(ds_replacement_025)
    delta = feature.diff(13)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00025000).reindex(feature.index)
DS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ds_replacement_d2_025'] = {'inputs': ['ds_replacement_025'], 'func': ds_replacement_d2_025}


def ds_replacement_d2_026(ds_replacement_026):
    feature = _clean(ds_replacement_026)
    delta = feature.diff(21)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00026000).reindex(feature.index)
DS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ds_replacement_d2_026'] = {'inputs': ['ds_replacement_026'], 'func': ds_replacement_d2_026}


def ds_replacement_d2_027(ds_replacement_027):
    feature = _clean(ds_replacement_027)
    delta = feature.diff(34)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00027000).reindex(feature.index)
DS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ds_replacement_d2_027'] = {'inputs': ['ds_replacement_027'], 'func': ds_replacement_d2_027}


def ds_replacement_d2_028(ds_replacement_028):
    feature = _clean(ds_replacement_028)
    delta = feature.diff(55)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00028000).reindex(feature.index)
DS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ds_replacement_d2_028'] = {'inputs': ['ds_replacement_028'], 'func': ds_replacement_d2_028}


def ds_replacement_d2_029(ds_replacement_029):
    feature = _clean(ds_replacement_029)
    delta = feature.diff(89)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00029000).reindex(feature.index)
DS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ds_replacement_d2_029'] = {'inputs': ['ds_replacement_029'], 'func': ds_replacement_d2_029}


def ds_replacement_d2_030(ds_replacement_030):
    feature = _clean(ds_replacement_030)
    delta = feature.diff(1)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00030000).reindex(feature.index)
DS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ds_replacement_d2_030'] = {'inputs': ['ds_replacement_030'], 'func': ds_replacement_d2_030}


def ds_replacement_d2_031(ds_replacement_031):
    feature = _clean(ds_replacement_031)
    delta = feature.diff(2)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00031000).reindex(feature.index)
DS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ds_replacement_d2_031'] = {'inputs': ['ds_replacement_031'], 'func': ds_replacement_d2_031}


def ds_replacement_d2_032(ds_replacement_032):
    feature = _clean(ds_replacement_032)
    delta = feature.diff(3)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00032000).reindex(feature.index)
DS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ds_replacement_d2_032'] = {'inputs': ['ds_replacement_032'], 'func': ds_replacement_d2_032}


def ds_replacement_d2_033(ds_replacement_033):
    feature = _clean(ds_replacement_033)
    delta = feature.diff(5)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00033000).reindex(feature.index)
DS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ds_replacement_d2_033'] = {'inputs': ['ds_replacement_033'], 'func': ds_replacement_d2_033}


def ds_replacement_d2_034(ds_replacement_034):
    feature = _clean(ds_replacement_034)
    delta = feature.diff(8)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00034000).reindex(feature.index)
DS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ds_replacement_d2_034'] = {'inputs': ['ds_replacement_034'], 'func': ds_replacement_d2_034}


def ds_replacement_d2_035(ds_replacement_035):
    feature = _clean(ds_replacement_035)
    delta = feature.diff(13)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00035000).reindex(feature.index)
DS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ds_replacement_d2_035'] = {'inputs': ['ds_replacement_035'], 'func': ds_replacement_d2_035}


def ds_replacement_d2_036(ds_replacement_036):
    feature = _clean(ds_replacement_036)
    delta = feature.diff(21)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00036000).reindex(feature.index)
DS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ds_replacement_d2_036'] = {'inputs': ['ds_replacement_036'], 'func': ds_replacement_d2_036}


def ds_replacement_d2_037(ds_replacement_037):
    feature = _clean(ds_replacement_037)
    delta = feature.diff(34)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00037000).reindex(feature.index)
DS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ds_replacement_d2_037'] = {'inputs': ['ds_replacement_037'], 'func': ds_replacement_d2_037}


def ds_replacement_d2_038(ds_replacement_038):
    feature = _clean(ds_replacement_038)
    delta = feature.diff(55)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00038000).reindex(feature.index)
DS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ds_replacement_d2_038'] = {'inputs': ['ds_replacement_038'], 'func': ds_replacement_d2_038}


def ds_replacement_d2_039(ds_replacement_039):
    feature = _clean(ds_replacement_039)
    delta = feature.diff(89)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00039000).reindex(feature.index)
DS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ds_replacement_d2_039'] = {'inputs': ['ds_replacement_039'], 'func': ds_replacement_d2_039}


def ds_replacement_d2_040(ds_replacement_040):
    feature = _clean(ds_replacement_040)
    delta = feature.diff(1)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00040000).reindex(feature.index)
DS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ds_replacement_d2_040'] = {'inputs': ['ds_replacement_040'], 'func': ds_replacement_d2_040}


def ds_replacement_d2_041(ds_replacement_041):
    feature = _clean(ds_replacement_041)
    delta = feature.diff(2)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00041000).reindex(feature.index)
DS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ds_replacement_d2_041'] = {'inputs': ['ds_replacement_041'], 'func': ds_replacement_d2_041}


def ds_replacement_d2_042(ds_replacement_042):
    feature = _clean(ds_replacement_042)
    delta = feature.diff(3)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00042000).reindex(feature.index)
DS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ds_replacement_d2_042'] = {'inputs': ['ds_replacement_042'], 'func': ds_replacement_d2_042}


def ds_replacement_d2_043(ds_replacement_043):
    feature = _clean(ds_replacement_043)
    delta = feature.diff(5)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00043000).reindex(feature.index)
DS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ds_replacement_d2_043'] = {'inputs': ['ds_replacement_043'], 'func': ds_replacement_d2_043}


def ds_replacement_d2_044(ds_replacement_044):
    feature = _clean(ds_replacement_044)
    delta = feature.diff(8)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00044000).reindex(feature.index)
DS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ds_replacement_d2_044'] = {'inputs': ['ds_replacement_044'], 'func': ds_replacement_d2_044}


def ds_replacement_d2_045(ds_replacement_045):
    feature = _clean(ds_replacement_045)
    delta = feature.diff(13)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00045000).reindex(feature.index)
DS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ds_replacement_d2_045'] = {'inputs': ['ds_replacement_045'], 'func': ds_replacement_d2_045}


def ds_replacement_d2_046(ds_replacement_046):
    feature = _clean(ds_replacement_046)
    delta = feature.diff(21)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00046000).reindex(feature.index)
DS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ds_replacement_d2_046'] = {'inputs': ['ds_replacement_046'], 'func': ds_replacement_d2_046}


def ds_replacement_d2_047(ds_replacement_047):
    feature = _clean(ds_replacement_047)
    delta = feature.diff(34)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00047000).reindex(feature.index)
DS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ds_replacement_d2_047'] = {'inputs': ['ds_replacement_047'], 'func': ds_replacement_d2_047}


def ds_replacement_d2_048(ds_replacement_048):
    feature = _clean(ds_replacement_048)
    delta = feature.diff(55)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00048000).reindex(feature.index)
DS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ds_replacement_d2_048'] = {'inputs': ['ds_replacement_048'], 'func': ds_replacement_d2_048}


def ds_replacement_d2_049(ds_replacement_049):
    feature = _clean(ds_replacement_049)
    delta = feature.diff(89)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00049000).reindex(feature.index)
DS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ds_replacement_d2_049'] = {'inputs': ['ds_replacement_049'], 'func': ds_replacement_d2_049}


def ds_replacement_d2_050(ds_replacement_050):
    feature = _clean(ds_replacement_050)
    delta = feature.diff(1)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00050000).reindex(feature.index)
DS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ds_replacement_d2_050'] = {'inputs': ['ds_replacement_050'], 'func': ds_replacement_d2_050}


def ds_replacement_d2_051(ds_replacement_051):
    feature = _clean(ds_replacement_051)
    delta = feature.diff(2)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00051000).reindex(feature.index)
DS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ds_replacement_d2_051'] = {'inputs': ['ds_replacement_051'], 'func': ds_replacement_d2_051}


def ds_replacement_d2_052(ds_replacement_052):
    feature = _clean(ds_replacement_052)
    delta = feature.diff(3)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00052000).reindex(feature.index)
DS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ds_replacement_d2_052'] = {'inputs': ['ds_replacement_052'], 'func': ds_replacement_d2_052}


def ds_replacement_d2_053(ds_replacement_053):
    feature = _clean(ds_replacement_053)
    delta = feature.diff(5)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00053000).reindex(feature.index)
DS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ds_replacement_d2_053'] = {'inputs': ['ds_replacement_053'], 'func': ds_replacement_d2_053}


def ds_replacement_d2_054(ds_replacement_054):
    feature = _clean(ds_replacement_054)
    delta = feature.diff(8)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00054000).reindex(feature.index)
DS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ds_replacement_d2_054'] = {'inputs': ['ds_replacement_054'], 'func': ds_replacement_d2_054}


def ds_replacement_d2_055(ds_replacement_055):
    feature = _clean(ds_replacement_055)
    delta = feature.diff(13)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00055000).reindex(feature.index)
DS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ds_replacement_d2_055'] = {'inputs': ['ds_replacement_055'], 'func': ds_replacement_d2_055}


def ds_replacement_d2_056(ds_replacement_056):
    feature = _clean(ds_replacement_056)
    delta = feature.diff(21)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00056000).reindex(feature.index)
DS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ds_replacement_d2_056'] = {'inputs': ['ds_replacement_056'], 'func': ds_replacement_d2_056}


def ds_replacement_d2_057(ds_replacement_057):
    feature = _clean(ds_replacement_057)
    delta = feature.diff(34)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00057000).reindex(feature.index)
DS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ds_replacement_d2_057'] = {'inputs': ['ds_replacement_057'], 'func': ds_replacement_d2_057}


def ds_replacement_d2_058(ds_replacement_058):
    feature = _clean(ds_replacement_058)
    delta = feature.diff(55)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00058000).reindex(feature.index)
DS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ds_replacement_d2_058'] = {'inputs': ['ds_replacement_058'], 'func': ds_replacement_d2_058}


def ds_replacement_d2_059(ds_replacement_059):
    feature = _clean(ds_replacement_059)
    delta = feature.diff(89)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00059000).reindex(feature.index)
DS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ds_replacement_d2_059'] = {'inputs': ['ds_replacement_059'], 'func': ds_replacement_d2_059}


def ds_replacement_d2_060(ds_replacement_060):
    feature = _clean(ds_replacement_060)
    delta = feature.diff(1)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00060000).reindex(feature.index)
DS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ds_replacement_d2_060'] = {'inputs': ['ds_replacement_060'], 'func': ds_replacement_d2_060}


def ds_replacement_d2_061(ds_replacement_061):
    feature = _clean(ds_replacement_061)
    delta = feature.diff(2)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00061000).reindex(feature.index)
DS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ds_replacement_d2_061'] = {'inputs': ['ds_replacement_061'], 'func': ds_replacement_d2_061}


def ds_replacement_d2_062(ds_replacement_062):
    feature = _clean(ds_replacement_062)
    delta = feature.diff(3)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00062000).reindex(feature.index)
DS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ds_replacement_d2_062'] = {'inputs': ['ds_replacement_062'], 'func': ds_replacement_d2_062}


def ds_replacement_d2_063(ds_replacement_063):
    feature = _clean(ds_replacement_063)
    delta = feature.diff(5)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00063000).reindex(feature.index)
DS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ds_replacement_d2_063'] = {'inputs': ['ds_replacement_063'], 'func': ds_replacement_d2_063}


def ds_replacement_d2_064(ds_replacement_064):
    feature = _clean(ds_replacement_064)
    delta = feature.diff(8)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00064000).reindex(feature.index)
DS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ds_replacement_d2_064'] = {'inputs': ['ds_replacement_064'], 'func': ds_replacement_d2_064}


def ds_replacement_d2_065(ds_replacement_065):
    feature = _clean(ds_replacement_065)
    delta = feature.diff(13)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00065000).reindex(feature.index)
DS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ds_replacement_d2_065'] = {'inputs': ['ds_replacement_065'], 'func': ds_replacement_d2_065}


def ds_replacement_d2_066(ds_replacement_066):
    feature = _clean(ds_replacement_066)
    delta = feature.diff(21)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00066000).reindex(feature.index)
DS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ds_replacement_d2_066'] = {'inputs': ['ds_replacement_066'], 'func': ds_replacement_d2_066}


def ds_replacement_d2_067(ds_replacement_067):
    feature = _clean(ds_replacement_067)
    delta = feature.diff(34)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00067000).reindex(feature.index)
DS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ds_replacement_d2_067'] = {'inputs': ['ds_replacement_067'], 'func': ds_replacement_d2_067}


def ds_replacement_d2_068(ds_replacement_068):
    feature = _clean(ds_replacement_068)
    delta = feature.diff(55)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00068000).reindex(feature.index)
DS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ds_replacement_d2_068'] = {'inputs': ['ds_replacement_068'], 'func': ds_replacement_d2_068}


def ds_replacement_d2_069(ds_replacement_069):
    feature = _clean(ds_replacement_069)
    delta = feature.diff(89)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00069000).reindex(feature.index)
DS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ds_replacement_d2_069'] = {'inputs': ['ds_replacement_069'], 'func': ds_replacement_d2_069}


def ds_replacement_d2_070(ds_replacement_070):
    feature = _clean(ds_replacement_070)
    delta = feature.diff(1)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00070000).reindex(feature.index)
DS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ds_replacement_d2_070'] = {'inputs': ['ds_replacement_070'], 'func': ds_replacement_d2_070}


def ds_replacement_d2_071(ds_replacement_071):
    feature = _clean(ds_replacement_071)
    delta = feature.diff(2)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00071000).reindex(feature.index)
DS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ds_replacement_d2_071'] = {'inputs': ['ds_replacement_071'], 'func': ds_replacement_d2_071}


def ds_replacement_d2_072(ds_replacement_072):
    feature = _clean(ds_replacement_072)
    delta = feature.diff(3)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00072000).reindex(feature.index)
DS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ds_replacement_d2_072'] = {'inputs': ['ds_replacement_072'], 'func': ds_replacement_d2_072}


def ds_replacement_d2_073(ds_replacement_073):
    feature = _clean(ds_replacement_073)
    delta = feature.diff(5)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00073000).reindex(feature.index)
DS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ds_replacement_d2_073'] = {'inputs': ['ds_replacement_073'], 'func': ds_replacement_d2_073}


def ds_replacement_d2_074(ds_replacement_074):
    feature = _clean(ds_replacement_074)
    delta = feature.diff(8)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00074000).reindex(feature.index)
DS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ds_replacement_d2_074'] = {'inputs': ['ds_replacement_074'], 'func': ds_replacement_d2_074}


def ds_replacement_d2_075(ds_replacement_075):
    feature = _clean(ds_replacement_075)
    delta = feature.diff(13)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00075000).reindex(feature.index)
DS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ds_replacement_d2_075'] = {'inputs': ['ds_replacement_075'], 'func': ds_replacement_d2_075}


def ds_replacement_d2_076(ds_replacement_076):
    feature = _clean(ds_replacement_076)
    delta = feature.diff(21)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00076000).reindex(feature.index)
DS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ds_replacement_d2_076'] = {'inputs': ['ds_replacement_076'], 'func': ds_replacement_d2_076}


def ds_replacement_d2_077(ds_replacement_077):
    feature = _clean(ds_replacement_077)
    delta = feature.diff(34)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00077000).reindex(feature.index)
DS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ds_replacement_d2_077'] = {'inputs': ['ds_replacement_077'], 'func': ds_replacement_d2_077}


def ds_replacement_d2_078(ds_replacement_078):
    feature = _clean(ds_replacement_078)
    delta = feature.diff(55)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00078000).reindex(feature.index)
DS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ds_replacement_d2_078'] = {'inputs': ['ds_replacement_078'], 'func': ds_replacement_d2_078}


def ds_replacement_d2_079(ds_replacement_079):
    feature = _clean(ds_replacement_079)
    delta = feature.diff(89)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00079000).reindex(feature.index)
DS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ds_replacement_d2_079'] = {'inputs': ['ds_replacement_079'], 'func': ds_replacement_d2_079}


def ds_replacement_d2_080(ds_replacement_080):
    feature = _clean(ds_replacement_080)
    delta = feature.diff(1)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00080000).reindex(feature.index)
DS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ds_replacement_d2_080'] = {'inputs': ['ds_replacement_080'], 'func': ds_replacement_d2_080}


def ds_replacement_d2_081(ds_replacement_081):
    feature = _clean(ds_replacement_081)
    delta = feature.diff(2)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00081000).reindex(feature.index)
DS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ds_replacement_d2_081'] = {'inputs': ['ds_replacement_081'], 'func': ds_replacement_d2_081}


def ds_replacement_d2_082(ds_replacement_082):
    feature = _clean(ds_replacement_082)
    delta = feature.diff(3)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00082000).reindex(feature.index)
DS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ds_replacement_d2_082'] = {'inputs': ['ds_replacement_082'], 'func': ds_replacement_d2_082}


def ds_replacement_d2_083(ds_replacement_083):
    feature = _clean(ds_replacement_083)
    delta = feature.diff(5)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00083000).reindex(feature.index)
DS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ds_replacement_d2_083'] = {'inputs': ['ds_replacement_083'], 'func': ds_replacement_d2_083}


def ds_replacement_d2_084(ds_replacement_084):
    feature = _clean(ds_replacement_084)
    delta = feature.diff(8)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00084000).reindex(feature.index)
DS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ds_replacement_d2_084'] = {'inputs': ['ds_replacement_084'], 'func': ds_replacement_d2_084}


def ds_replacement_d2_085(ds_replacement_085):
    feature = _clean(ds_replacement_085)
    delta = feature.diff(13)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00085000).reindex(feature.index)
DS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ds_replacement_d2_085'] = {'inputs': ['ds_replacement_085'], 'func': ds_replacement_d2_085}


def ds_replacement_d2_086(ds_replacement_086):
    feature = _clean(ds_replacement_086)
    delta = feature.diff(21)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00086000).reindex(feature.index)
DS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ds_replacement_d2_086'] = {'inputs': ['ds_replacement_086'], 'func': ds_replacement_d2_086}


def ds_replacement_d2_087(ds_replacement_087):
    feature = _clean(ds_replacement_087)
    delta = feature.diff(34)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00087000).reindex(feature.index)
DS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ds_replacement_d2_087'] = {'inputs': ['ds_replacement_087'], 'func': ds_replacement_d2_087}


def ds_replacement_d2_088(ds_replacement_088):
    feature = _clean(ds_replacement_088)
    delta = feature.diff(55)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00088000).reindex(feature.index)
DS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ds_replacement_d2_088'] = {'inputs': ['ds_replacement_088'], 'func': ds_replacement_d2_088}


def ds_replacement_d2_089(ds_replacement_089):
    feature = _clean(ds_replacement_089)
    delta = feature.diff(89)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00089000).reindex(feature.index)
DS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ds_replacement_d2_089'] = {'inputs': ['ds_replacement_089'], 'func': ds_replacement_d2_089}


def ds_replacement_d2_090(ds_replacement_090):
    feature = _clean(ds_replacement_090)
    delta = feature.diff(1)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00090000).reindex(feature.index)
DS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ds_replacement_d2_090'] = {'inputs': ['ds_replacement_090'], 'func': ds_replacement_d2_090}


def ds_replacement_d2_091(ds_replacement_091):
    feature = _clean(ds_replacement_091)
    delta = feature.diff(2)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00091000).reindex(feature.index)
DS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ds_replacement_d2_091'] = {'inputs': ['ds_replacement_091'], 'func': ds_replacement_d2_091}


def ds_replacement_d2_092(ds_replacement_092):
    feature = _clean(ds_replacement_092)
    delta = feature.diff(3)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00092000).reindex(feature.index)
DS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ds_replacement_d2_092'] = {'inputs': ['ds_replacement_092'], 'func': ds_replacement_d2_092}


def ds_replacement_d2_093(ds_replacement_093):
    feature = _clean(ds_replacement_093)
    delta = feature.diff(5)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00093000).reindex(feature.index)
DS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ds_replacement_d2_093'] = {'inputs': ['ds_replacement_093'], 'func': ds_replacement_d2_093}


def ds_replacement_d2_094(ds_replacement_094):
    feature = _clean(ds_replacement_094)
    delta = feature.diff(8)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00094000).reindex(feature.index)
DS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ds_replacement_d2_094'] = {'inputs': ['ds_replacement_094'], 'func': ds_replacement_d2_094}


def ds_replacement_d2_095(ds_replacement_095):
    feature = _clean(ds_replacement_095)
    delta = feature.diff(13)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00095000).reindex(feature.index)
DS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ds_replacement_d2_095'] = {'inputs': ['ds_replacement_095'], 'func': ds_replacement_d2_095}


def ds_replacement_d2_096(ds_replacement_096):
    feature = _clean(ds_replacement_096)
    delta = feature.diff(21)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00096000).reindex(feature.index)
DS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ds_replacement_d2_096'] = {'inputs': ['ds_replacement_096'], 'func': ds_replacement_d2_096}


def ds_replacement_d2_097(ds_replacement_097):
    feature = _clean(ds_replacement_097)
    delta = feature.diff(34)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00097000).reindex(feature.index)
DS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ds_replacement_d2_097'] = {'inputs': ['ds_replacement_097'], 'func': ds_replacement_d2_097}


def ds_replacement_d2_098(ds_replacement_098):
    feature = _clean(ds_replacement_098)
    delta = feature.diff(55)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00098000).reindex(feature.index)
DS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ds_replacement_d2_098'] = {'inputs': ['ds_replacement_098'], 'func': ds_replacement_d2_098}


def ds_replacement_d2_099(ds_replacement_099):
    feature = _clean(ds_replacement_099)
    delta = feature.diff(89)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00099000).reindex(feature.index)
DS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ds_replacement_d2_099'] = {'inputs': ['ds_replacement_099'], 'func': ds_replacement_d2_099}


def ds_replacement_d2_100(ds_replacement_100):
    feature = _clean(ds_replacement_100)
    delta = feature.diff(1)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00100000).reindex(feature.index)
DS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ds_replacement_d2_100'] = {'inputs': ['ds_replacement_100'], 'func': ds_replacement_d2_100}


def ds_replacement_d2_101(ds_replacement_101):
    feature = _clean(ds_replacement_101)
    delta = feature.diff(2)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00101000).reindex(feature.index)
DS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ds_replacement_d2_101'] = {'inputs': ['ds_replacement_101'], 'func': ds_replacement_d2_101}


def ds_replacement_d2_102(ds_replacement_102):
    feature = _clean(ds_replacement_102)
    delta = feature.diff(3)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00102000).reindex(feature.index)
DS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ds_replacement_d2_102'] = {'inputs': ['ds_replacement_102'], 'func': ds_replacement_d2_102}


def ds_replacement_d2_103(ds_replacement_103):
    feature = _clean(ds_replacement_103)
    delta = feature.diff(5)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00103000).reindex(feature.index)
DS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ds_replacement_d2_103'] = {'inputs': ['ds_replacement_103'], 'func': ds_replacement_d2_103}


def ds_replacement_d2_104(ds_replacement_104):
    feature = _clean(ds_replacement_104)
    delta = feature.diff(8)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00104000).reindex(feature.index)
DS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ds_replacement_d2_104'] = {'inputs': ['ds_replacement_104'], 'func': ds_replacement_d2_104}


def ds_replacement_d2_105(ds_replacement_105):
    feature = _clean(ds_replacement_105)
    delta = feature.diff(13)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00105000).reindex(feature.index)
DS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ds_replacement_d2_105'] = {'inputs': ['ds_replacement_105'], 'func': ds_replacement_d2_105}


def ds_replacement_d2_106(ds_replacement_106):
    feature = _clean(ds_replacement_106)
    delta = feature.diff(21)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00106000).reindex(feature.index)
DS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ds_replacement_d2_106'] = {'inputs': ['ds_replacement_106'], 'func': ds_replacement_d2_106}


def ds_replacement_d2_107(ds_replacement_107):
    feature = _clean(ds_replacement_107)
    delta = feature.diff(34)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00107000).reindex(feature.index)
DS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ds_replacement_d2_107'] = {'inputs': ['ds_replacement_107'], 'func': ds_replacement_d2_107}


def ds_replacement_d2_108(ds_replacement_108):
    feature = _clean(ds_replacement_108)
    delta = feature.diff(55)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00108000).reindex(feature.index)
DS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ds_replacement_d2_108'] = {'inputs': ['ds_replacement_108'], 'func': ds_replacement_d2_108}


def ds_replacement_d2_109(ds_replacement_109):
    feature = _clean(ds_replacement_109)
    delta = feature.diff(89)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00109000).reindex(feature.index)
DS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ds_replacement_d2_109'] = {'inputs': ['ds_replacement_109'], 'func': ds_replacement_d2_109}


def ds_replacement_d2_110(ds_replacement_110):
    feature = _clean(ds_replacement_110)
    delta = feature.diff(1)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00110000).reindex(feature.index)
DS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ds_replacement_d2_110'] = {'inputs': ['ds_replacement_110'], 'func': ds_replacement_d2_110}


def ds_replacement_d2_111(ds_replacement_111):
    feature = _clean(ds_replacement_111)
    delta = feature.diff(2)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00111000).reindex(feature.index)
DS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ds_replacement_d2_111'] = {'inputs': ['ds_replacement_111'], 'func': ds_replacement_d2_111}


def ds_replacement_d2_112(ds_replacement_112):
    feature = _clean(ds_replacement_112)
    delta = feature.diff(3)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00112000).reindex(feature.index)
DS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ds_replacement_d2_112'] = {'inputs': ['ds_replacement_112'], 'func': ds_replacement_d2_112}


def ds_replacement_d2_113(ds_replacement_113):
    feature = _clean(ds_replacement_113)
    delta = feature.diff(5)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00113000).reindex(feature.index)
DS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ds_replacement_d2_113'] = {'inputs': ['ds_replacement_113'], 'func': ds_replacement_d2_113}


def ds_replacement_d2_114(ds_replacement_114):
    feature = _clean(ds_replacement_114)
    delta = feature.diff(8)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00114000).reindex(feature.index)
DS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ds_replacement_d2_114'] = {'inputs': ['ds_replacement_114'], 'func': ds_replacement_d2_114}


def ds_replacement_d2_115(ds_replacement_115):
    feature = _clean(ds_replacement_115)
    delta = feature.diff(13)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00115000).reindex(feature.index)
DS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ds_replacement_d2_115'] = {'inputs': ['ds_replacement_115'], 'func': ds_replacement_d2_115}


def ds_replacement_d2_116(ds_replacement_116):
    feature = _clean(ds_replacement_116)
    delta = feature.diff(21)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00116000).reindex(feature.index)
DS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ds_replacement_d2_116'] = {'inputs': ['ds_replacement_116'], 'func': ds_replacement_d2_116}


def ds_replacement_d2_117(ds_replacement_117):
    feature = _clean(ds_replacement_117)
    delta = feature.diff(34)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00117000).reindex(feature.index)
DS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ds_replacement_d2_117'] = {'inputs': ['ds_replacement_117'], 'func': ds_replacement_d2_117}


def ds_replacement_d2_118(ds_replacement_118):
    feature = _clean(ds_replacement_118)
    delta = feature.diff(55)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00118000).reindex(feature.index)
DS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ds_replacement_d2_118'] = {'inputs': ['ds_replacement_118'], 'func': ds_replacement_d2_118}


def ds_replacement_d2_119(ds_replacement_119):
    feature = _clean(ds_replacement_119)
    delta = feature.diff(89)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00119000).reindex(feature.index)
DS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ds_replacement_d2_119'] = {'inputs': ['ds_replacement_119'], 'func': ds_replacement_d2_119}


def ds_replacement_d2_120(ds_replacement_120):
    feature = _clean(ds_replacement_120)
    delta = feature.diff(1)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00120000).reindex(feature.index)
DS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ds_replacement_d2_120'] = {'inputs': ['ds_replacement_120'], 'func': ds_replacement_d2_120}


def ds_replacement_d2_121(ds_replacement_121):
    feature = _clean(ds_replacement_121)
    delta = feature.diff(2)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00121000).reindex(feature.index)
DS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ds_replacement_d2_121'] = {'inputs': ['ds_replacement_121'], 'func': ds_replacement_d2_121}


def ds_replacement_d2_122(ds_replacement_122):
    feature = _clean(ds_replacement_122)
    delta = feature.diff(3)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00122000).reindex(feature.index)
DS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ds_replacement_d2_122'] = {'inputs': ['ds_replacement_122'], 'func': ds_replacement_d2_122}


def ds_replacement_d2_123(ds_replacement_123):
    feature = _clean(ds_replacement_123)
    delta = feature.diff(5)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00123000).reindex(feature.index)
DS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ds_replacement_d2_123'] = {'inputs': ['ds_replacement_123'], 'func': ds_replacement_d2_123}


def ds_replacement_d2_124(ds_replacement_124):
    feature = _clean(ds_replacement_124)
    delta = feature.diff(8)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00124000).reindex(feature.index)
DS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ds_replacement_d2_124'] = {'inputs': ['ds_replacement_124'], 'func': ds_replacement_d2_124}


def ds_replacement_d2_125(ds_replacement_125):
    feature = _clean(ds_replacement_125)
    delta = feature.diff(13)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00125000).reindex(feature.index)
DS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ds_replacement_d2_125'] = {'inputs': ['ds_replacement_125'], 'func': ds_replacement_d2_125}


def ds_replacement_d2_126(ds_replacement_126):
    feature = _clean(ds_replacement_126)
    delta = feature.diff(21)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00126000).reindex(feature.index)
DS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ds_replacement_d2_126'] = {'inputs': ['ds_replacement_126'], 'func': ds_replacement_d2_126}


def ds_replacement_d2_127(ds_replacement_127):
    feature = _clean(ds_replacement_127)
    delta = feature.diff(34)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00127000).reindex(feature.index)
DS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ds_replacement_d2_127'] = {'inputs': ['ds_replacement_127'], 'func': ds_replacement_d2_127}


def ds_replacement_d2_128(ds_replacement_128):
    feature = _clean(ds_replacement_128)
    delta = feature.diff(55)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00128000).reindex(feature.index)
DS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ds_replacement_d2_128'] = {'inputs': ['ds_replacement_128'], 'func': ds_replacement_d2_128}


def ds_replacement_d2_129(ds_replacement_129):
    feature = _clean(ds_replacement_129)
    delta = feature.diff(89)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00129000).reindex(feature.index)
DS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ds_replacement_d2_129'] = {'inputs': ['ds_replacement_129'], 'func': ds_replacement_d2_129}


def ds_replacement_d2_130(ds_replacement_130):
    feature = _clean(ds_replacement_130)
    delta = feature.diff(1)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00130000).reindex(feature.index)
DS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ds_replacement_d2_130'] = {'inputs': ['ds_replacement_130'], 'func': ds_replacement_d2_130}


def ds_replacement_d2_131(ds_replacement_131):
    feature = _clean(ds_replacement_131)
    delta = feature.diff(2)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00131000).reindex(feature.index)
DS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ds_replacement_d2_131'] = {'inputs': ['ds_replacement_131'], 'func': ds_replacement_d2_131}


def ds_replacement_d2_132(ds_replacement_132):
    feature = _clean(ds_replacement_132)
    delta = feature.diff(3)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00132000).reindex(feature.index)
DS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ds_replacement_d2_132'] = {'inputs': ['ds_replacement_132'], 'func': ds_replacement_d2_132}


def ds_replacement_d2_133(ds_replacement_133):
    feature = _clean(ds_replacement_133)
    delta = feature.diff(5)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00133000).reindex(feature.index)
DS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ds_replacement_d2_133'] = {'inputs': ['ds_replacement_133'], 'func': ds_replacement_d2_133}


def ds_replacement_d2_134(ds_replacement_134):
    feature = _clean(ds_replacement_134)
    delta = feature.diff(8)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00134000).reindex(feature.index)
DS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ds_replacement_d2_134'] = {'inputs': ['ds_replacement_134'], 'func': ds_replacement_d2_134}


def ds_replacement_d2_135(ds_replacement_135):
    feature = _clean(ds_replacement_135)
    delta = feature.diff(13)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00135000).reindex(feature.index)
DS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ds_replacement_d2_135'] = {'inputs': ['ds_replacement_135'], 'func': ds_replacement_d2_135}


def ds_replacement_d2_136(ds_replacement_136):
    feature = _clean(ds_replacement_136)
    delta = feature.diff(21)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00136000).reindex(feature.index)
DS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ds_replacement_d2_136'] = {'inputs': ['ds_replacement_136'], 'func': ds_replacement_d2_136}


def ds_replacement_d2_137(ds_replacement_137):
    feature = _clean(ds_replacement_137)
    delta = feature.diff(34)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00137000).reindex(feature.index)
DS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ds_replacement_d2_137'] = {'inputs': ['ds_replacement_137'], 'func': ds_replacement_d2_137}


def ds_replacement_d2_138(ds_replacement_138):
    feature = _clean(ds_replacement_138)
    delta = feature.diff(55)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00138000).reindex(feature.index)
DS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ds_replacement_d2_138'] = {'inputs': ['ds_replacement_138'], 'func': ds_replacement_d2_138}


def ds_replacement_d2_139(ds_replacement_139):
    feature = _clean(ds_replacement_139)
    delta = feature.diff(89)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00139000).reindex(feature.index)
DS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ds_replacement_d2_139'] = {'inputs': ['ds_replacement_139'], 'func': ds_replacement_d2_139}


def ds_replacement_d2_140(ds_replacement_140):
    feature = _clean(ds_replacement_140)
    delta = feature.diff(1)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00140000).reindex(feature.index)
DS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ds_replacement_d2_140'] = {'inputs': ['ds_replacement_140'], 'func': ds_replacement_d2_140}


def ds_replacement_d2_141(ds_replacement_141):
    feature = _clean(ds_replacement_141)
    delta = feature.diff(2)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00141000).reindex(feature.index)
DS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ds_replacement_d2_141'] = {'inputs': ['ds_replacement_141'], 'func': ds_replacement_d2_141}


def ds_replacement_d2_142(ds_replacement_142):
    feature = _clean(ds_replacement_142)
    delta = feature.diff(3)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00142000).reindex(feature.index)
DS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ds_replacement_d2_142'] = {'inputs': ['ds_replacement_142'], 'func': ds_replacement_d2_142}


def ds_replacement_d2_143(ds_replacement_143):
    feature = _clean(ds_replacement_143)
    delta = feature.diff(5)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00143000).reindex(feature.index)
DS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ds_replacement_d2_143'] = {'inputs': ['ds_replacement_143'], 'func': ds_replacement_d2_143}


def ds_replacement_d2_144(ds_replacement_144):
    feature = _clean(ds_replacement_144)
    delta = feature.diff(8)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00144000).reindex(feature.index)
DS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ds_replacement_d2_144'] = {'inputs': ['ds_replacement_144'], 'func': ds_replacement_d2_144}


def ds_replacement_d2_145(ds_replacement_145):
    feature = _clean(ds_replacement_145)
    delta = feature.diff(13)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00145000).reindex(feature.index)
DS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ds_replacement_d2_145'] = {'inputs': ['ds_replacement_145'], 'func': ds_replacement_d2_145}


def ds_replacement_d2_146(ds_replacement_146):
    feature = _clean(ds_replacement_146)
    delta = feature.diff(21)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00146000).reindex(feature.index)
DS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ds_replacement_d2_146'] = {'inputs': ['ds_replacement_146'], 'func': ds_replacement_d2_146}


def ds_replacement_d2_147(ds_replacement_147):
    feature = _clean(ds_replacement_147)
    delta = feature.diff(34)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00147000).reindex(feature.index)
DS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ds_replacement_d2_147'] = {'inputs': ['ds_replacement_147'], 'func': ds_replacement_d2_147}


def ds_replacement_d2_148(ds_replacement_148):
    feature = _clean(ds_replacement_148)
    delta = feature.diff(55)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00148000).reindex(feature.index)
DS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ds_replacement_d2_148'] = {'inputs': ['ds_replacement_148'], 'func': ds_replacement_d2_148}


def ds_replacement_d2_149(ds_replacement_149):
    feature = _clean(ds_replacement_149)
    delta = feature.diff(89)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00149000).reindex(feature.index)
DS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ds_replacement_d2_149'] = {'inputs': ['ds_replacement_149'], 'func': ds_replacement_d2_149}


def ds_replacement_d2_150(ds_replacement_150):
    feature = _clean(ds_replacement_150)
    delta = feature.diff(1)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00150000).reindex(feature.index)
DS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ds_replacement_d2_150'] = {'inputs': ['ds_replacement_150'], 'func': ds_replacement_d2_150}


def ds_replacement_d2_151(ds_replacement_151):
    feature = _clean(ds_replacement_151)
    delta = feature.diff(2)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00151000).reindex(feature.index)
DS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ds_replacement_d2_151'] = {'inputs': ['ds_replacement_151'], 'func': ds_replacement_d2_151}


def ds_replacement_d2_152(ds_replacement_152):
    feature = _clean(ds_replacement_152)
    delta = feature.diff(3)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00152000).reindex(feature.index)
DS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ds_replacement_d2_152'] = {'inputs': ['ds_replacement_152'], 'func': ds_replacement_d2_152}


def ds_replacement_d2_153(ds_replacement_153):
    feature = _clean(ds_replacement_153)
    delta = feature.diff(5)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00153000).reindex(feature.index)
DS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ds_replacement_d2_153'] = {'inputs': ['ds_replacement_153'], 'func': ds_replacement_d2_153}


def ds_replacement_d2_154(ds_replacement_154):
    feature = _clean(ds_replacement_154)
    delta = feature.diff(8)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00154000).reindex(feature.index)
DS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ds_replacement_d2_154'] = {'inputs': ['ds_replacement_154'], 'func': ds_replacement_d2_154}


def ds_replacement_d2_155(ds_replacement_155):
    feature = _clean(ds_replacement_155)
    delta = feature.diff(13)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00155000).reindex(feature.index)
DS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ds_replacement_d2_155'] = {'inputs': ['ds_replacement_155'], 'func': ds_replacement_d2_155}


def ds_replacement_d2_156(ds_replacement_156):
    feature = _clean(ds_replacement_156)
    delta = feature.diff(21)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00156000).reindex(feature.index)
DS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ds_replacement_d2_156'] = {'inputs': ['ds_replacement_156'], 'func': ds_replacement_d2_156}


def ds_replacement_d2_157(ds_replacement_157):
    feature = _clean(ds_replacement_157)
    delta = feature.diff(34)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00157000).reindex(feature.index)
DS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ds_replacement_d2_157'] = {'inputs': ['ds_replacement_157'], 'func': ds_replacement_d2_157}


def ds_replacement_d2_158(ds_replacement_158):
    feature = _clean(ds_replacement_158)
    delta = feature.diff(55)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00158000).reindex(feature.index)
DS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ds_replacement_d2_158'] = {'inputs': ['ds_replacement_158'], 'func': ds_replacement_d2_158}


def ds_replacement_d2_159(ds_replacement_159):
    feature = _clean(ds_replacement_159)
    delta = feature.diff(89)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00159000).reindex(feature.index)
DS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ds_replacement_d2_159'] = {'inputs': ['ds_replacement_159'], 'func': ds_replacement_d2_159}


def ds_replacement_d2_160(ds_replacement_160):
    feature = _clean(ds_replacement_160)
    delta = feature.diff(1)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00160000).reindex(feature.index)
DS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ds_replacement_d2_160'] = {'inputs': ['ds_replacement_160'], 'func': ds_replacement_d2_160}


def ds_replacement_d2_161(ds_replacement_161):
    feature = _clean(ds_replacement_161)
    delta = feature.diff(2)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00161000).reindex(feature.index)
DS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ds_replacement_d2_161'] = {'inputs': ['ds_replacement_161'], 'func': ds_replacement_d2_161}


def ds_replacement_d2_162(ds_replacement_162):
    feature = _clean(ds_replacement_162)
    delta = feature.diff(3)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00162000).reindex(feature.index)
DS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ds_replacement_d2_162'] = {'inputs': ['ds_replacement_162'], 'func': ds_replacement_d2_162}


def ds_replacement_d2_163(ds_replacement_163):
    feature = _clean(ds_replacement_163)
    delta = feature.diff(5)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00163000).reindex(feature.index)
DS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ds_replacement_d2_163'] = {'inputs': ['ds_replacement_163'], 'func': ds_replacement_d2_163}


def ds_replacement_d2_164(ds_replacement_164):
    feature = _clean(ds_replacement_164)
    delta = feature.diff(8)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00164000).reindex(feature.index)
DS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ds_replacement_d2_164'] = {'inputs': ['ds_replacement_164'], 'func': ds_replacement_d2_164}


def ds_replacement_d2_165(ds_replacement_165):
    feature = _clean(ds_replacement_165)
    delta = feature.diff(13)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00165000).reindex(feature.index)
DS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ds_replacement_d2_165'] = {'inputs': ['ds_replacement_165'], 'func': ds_replacement_d2_165}


def ds_replacement_d2_166(ds_replacement_166):
    feature = _clean(ds_replacement_166)
    delta = feature.diff(21)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00166000).reindex(feature.index)
DS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ds_replacement_d2_166'] = {'inputs': ['ds_replacement_166'], 'func': ds_replacement_d2_166}


def ds_replacement_d2_167(ds_replacement_167):
    feature = _clean(ds_replacement_167)
    delta = feature.diff(34)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00167000).reindex(feature.index)
DS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ds_replacement_d2_167'] = {'inputs': ['ds_replacement_167'], 'func': ds_replacement_d2_167}


def ds_replacement_d2_168(ds_replacement_168):
    feature = _clean(ds_replacement_168)
    delta = feature.diff(55)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00168000).reindex(feature.index)
DS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ds_replacement_d2_168'] = {'inputs': ['ds_replacement_168'], 'func': ds_replacement_d2_168}


def ds_replacement_d2_169(ds_replacement_169):
    feature = _clean(ds_replacement_169)
    delta = feature.diff(89)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00169000).reindex(feature.index)
DS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ds_replacement_d2_169'] = {'inputs': ['ds_replacement_169'], 'func': ds_replacement_d2_169}


def ds_replacement_d2_170(ds_replacement_170):
    feature = _clean(ds_replacement_170)
    delta = feature.diff(1)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00170000).reindex(feature.index)
DS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ds_replacement_d2_170'] = {'inputs': ['ds_replacement_170'], 'func': ds_replacement_d2_170}


# Base-universe derivative extensions for repaired first-base features.
DSTK_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY = {}


def _base_universe_d2(feature, idx):
    feature = _clean(feature) if '_clean' in globals() else _s(feature).replace([np.inf, -np.inf], np.nan)
    windows = [1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    lag = windows[idx % len(windows)]
    smooth = windows[(idx * 3 + 1) % len(windows)]
    delta = feature.diff(lag)
    local = feature - feature.rolling(max(3, smooth), min_periods=2).mean()
    out = delta + local.fillna(0.0) * (0.00037 * ((idx % 17) + 1))
    return out.replace([np.inf, -np.inf], np.nan).reindex(feature.index)


def dstk_base_universe_d2_001_dstk_002_zero_volume_frequency_10_002(dstk_002_zero_volume_frequency_10_002):
    return _base_universe_d2(dstk_002_zero_volume_frequency_10_002, 1)
DSTK_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['dstk_base_universe_d2_001_dstk_002_zero_volume_frequency_10_002'] = {'inputs': ['dstk_002_zero_volume_frequency_10_002'], 'func': dstk_base_universe_d2_001_dstk_002_zero_volume_frequency_10_002}


def dstk_base_universe_d2_002_dstk_003_spread_proxy_21_003(dstk_003_spread_proxy_21_003):
    return _base_universe_d2(dstk_003_spread_proxy_21_003, 2)
DSTK_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['dstk_base_universe_d2_002_dstk_003_spread_proxy_21_003'] = {'inputs': ['dstk_003_spread_proxy_21_003'], 'func': dstk_base_universe_d2_002_dstk_003_spread_proxy_21_003}


def dstk_base_universe_d2_003_dstk_004_trading_intensity_42_004(dstk_004_trading_intensity_42_004):
    return _base_universe_d2(dstk_004_trading_intensity_42_004, 3)
DSTK_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['dstk_base_universe_d2_003_dstk_004_trading_intensity_42_004'] = {'inputs': ['dstk_004_trading_intensity_42_004'], 'func': dstk_base_universe_d2_003_dstk_004_trading_intensity_42_004}


def dstk_base_universe_d2_004_dstk_006_price_level_distress_84_006(dstk_006_price_level_distress_84_006):
    return _base_universe_d2(dstk_006_price_level_distress_84_006, 4)
DSTK_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['dstk_base_universe_d2_004_dstk_006_price_level_distress_84_006'] = {'inputs': ['dstk_006_price_level_distress_84_006'], 'func': dstk_base_universe_d2_004_dstk_006_price_level_distress_84_006}


def dstk_base_universe_d2_005_dstk_008_zero_volume_frequency_189_008(dstk_008_zero_volume_frequency_189_008):
    return _base_universe_d2(dstk_008_zero_volume_frequency_189_008, 5)
DSTK_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['dstk_base_universe_d2_005_dstk_008_zero_volume_frequency_189_008'] = {'inputs': ['dstk_008_zero_volume_frequency_189_008'], 'func': dstk_base_universe_d2_005_dstk_008_zero_volume_frequency_189_008}


def dstk_base_universe_d2_006_dstk_009_spread_proxy_252_009(dstk_009_spread_proxy_252_009):
    return _base_universe_d2(dstk_009_spread_proxy_252_009, 6)
DSTK_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['dstk_base_universe_d2_006_dstk_009_spread_proxy_252_009'] = {'inputs': ['dstk_009_spread_proxy_252_009'], 'func': dstk_base_universe_d2_006_dstk_009_spread_proxy_252_009}


def dstk_base_universe_d2_007_dstk_010_trading_intensity_378_010(dstk_010_trading_intensity_378_010):
    return _base_universe_d2(dstk_010_trading_intensity_378_010, 7)
DSTK_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['dstk_base_universe_d2_007_dstk_010_trading_intensity_378_010'] = {'inputs': ['dstk_010_trading_intensity_378_010'], 'func': dstk_base_universe_d2_007_dstk_010_trading_intensity_378_010}


def dstk_base_universe_d2_008_dstk_012_price_level_distress_756_012(dstk_012_price_level_distress_756_012):
    return _base_universe_d2(dstk_012_price_level_distress_756_012, 8)
DSTK_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['dstk_base_universe_d2_008_dstk_012_price_level_distress_756_012'] = {'inputs': ['dstk_012_price_level_distress_756_012'], 'func': dstk_base_universe_d2_008_dstk_012_price_level_distress_756_012}


def dstk_base_universe_d2_009_dstk_014_zero_volume_frequency_1260_014(dstk_014_zero_volume_frequency_1260_014):
    return _base_universe_d2(dstk_014_zero_volume_frequency_1260_014, 9)
DSTK_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['dstk_base_universe_d2_009_dstk_014_zero_volume_frequency_1260_014'] = {'inputs': ['dstk_014_zero_volume_frequency_1260_014'], 'func': dstk_base_universe_d2_009_dstk_014_zero_volume_frequency_1260_014}


def dstk_base_universe_d2_010_dstk_015_spread_proxy_1512_015(dstk_015_spread_proxy_1512_015):
    return _base_universe_d2(dstk_015_spread_proxy_1512_015, 10)
DSTK_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['dstk_base_universe_d2_010_dstk_015_spread_proxy_1512_015'] = {'inputs': ['dstk_015_spread_proxy_1512_015'], 'func': dstk_base_universe_d2_010_dstk_015_spread_proxy_1512_015}


def dstk_base_universe_d2_011_dstk_016_trading_intensity_5_016(dstk_016_trading_intensity_5_016):
    return _base_universe_d2(dstk_016_trading_intensity_5_016, 11)
DSTK_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['dstk_base_universe_d2_011_dstk_016_trading_intensity_5_016'] = {'inputs': ['dstk_016_trading_intensity_5_016'], 'func': dstk_base_universe_d2_011_dstk_016_trading_intensity_5_016}


def dstk_base_universe_d2_012_dstk_018_price_level_distress_21_018(dstk_018_price_level_distress_21_018):
    return _base_universe_d2(dstk_018_price_level_distress_21_018, 12)
DSTK_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['dstk_base_universe_d2_012_dstk_018_price_level_distress_21_018'] = {'inputs': ['dstk_018_price_level_distress_21_018'], 'func': dstk_base_universe_d2_012_dstk_018_price_level_distress_21_018}


def dstk_base_universe_d2_013_dstk_020_zero_volume_frequency_63_020(dstk_020_zero_volume_frequency_63_020):
    return _base_universe_d2(dstk_020_zero_volume_frequency_63_020, 13)
DSTK_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['dstk_base_universe_d2_013_dstk_020_zero_volume_frequency_63_020'] = {'inputs': ['dstk_020_zero_volume_frequency_63_020'], 'func': dstk_base_universe_d2_013_dstk_020_zero_volume_frequency_63_020}


def dstk_base_universe_d2_014_dstk_021_spread_proxy_84_021(dstk_021_spread_proxy_84_021):
    return _base_universe_d2(dstk_021_spread_proxy_84_021, 14)
DSTK_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['dstk_base_universe_d2_014_dstk_021_spread_proxy_84_021'] = {'inputs': ['dstk_021_spread_proxy_84_021'], 'func': dstk_base_universe_d2_014_dstk_021_spread_proxy_84_021}


def dstk_base_universe_d2_015_dstk_022_trading_intensity_126_022(dstk_022_trading_intensity_126_022):
    return _base_universe_d2(dstk_022_trading_intensity_126_022, 15)
DSTK_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['dstk_base_universe_d2_015_dstk_022_trading_intensity_126_022'] = {'inputs': ['dstk_022_trading_intensity_126_022'], 'func': dstk_base_universe_d2_015_dstk_022_trading_intensity_126_022}


def dstk_base_universe_d2_016_dstk_024_price_level_distress_252_024(dstk_024_price_level_distress_252_024):
    return _base_universe_d2(dstk_024_price_level_distress_252_024, 16)
DSTK_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['dstk_base_universe_d2_016_dstk_024_price_level_distress_252_024'] = {'inputs': ['dstk_024_price_level_distress_252_024'], 'func': dstk_base_universe_d2_016_dstk_024_price_level_distress_252_024}


def dstk_base_universe_d2_017_dstk_026_zero_volume_frequency_504_026(dstk_026_zero_volume_frequency_504_026):
    return _base_universe_d2(dstk_026_zero_volume_frequency_504_026, 17)
DSTK_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['dstk_base_universe_d2_017_dstk_026_zero_volume_frequency_504_026'] = {'inputs': ['dstk_026_zero_volume_frequency_504_026'], 'func': dstk_base_universe_d2_017_dstk_026_zero_volume_frequency_504_026}


def dstk_base_universe_d2_018_dstk_027_spread_proxy_756_027(dstk_027_spread_proxy_756_027):
    return _base_universe_d2(dstk_027_spread_proxy_756_027, 18)
DSTK_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['dstk_base_universe_d2_018_dstk_027_spread_proxy_756_027'] = {'inputs': ['dstk_027_spread_proxy_756_027'], 'func': dstk_base_universe_d2_018_dstk_027_spread_proxy_756_027}


def dstk_base_universe_d2_019_dstk_028_trading_intensity_1008_028(dstk_028_trading_intensity_1008_028):
    return _base_universe_d2(dstk_028_trading_intensity_1008_028, 19)
DSTK_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['dstk_base_universe_d2_019_dstk_028_trading_intensity_1008_028'] = {'inputs': ['dstk_028_trading_intensity_1008_028'], 'func': dstk_base_universe_d2_019_dstk_028_trading_intensity_1008_028}


def dstk_base_universe_d2_020_dstk_030_price_level_distress_1512_030(dstk_030_price_level_distress_1512_030):
    return _base_universe_d2(dstk_030_price_level_distress_1512_030, 20)
DSTK_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['dstk_base_universe_d2_020_dstk_030_price_level_distress_1512_030'] = {'inputs': ['dstk_030_price_level_distress_1512_030'], 'func': dstk_base_universe_d2_020_dstk_030_price_level_distress_1512_030}


def dstk_base_universe_d2_021_dstk_basefill_001(dstk_basefill_001):
    return _base_universe_d2(dstk_basefill_001, 21)
DSTK_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['dstk_base_universe_d2_021_dstk_basefill_001'] = {'inputs': ['dstk_basefill_001'], 'func': dstk_base_universe_d2_021_dstk_basefill_001}


def dstk_base_universe_d2_022_dstk_basefill_005(dstk_basefill_005):
    return _base_universe_d2(dstk_basefill_005, 22)
DSTK_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['dstk_base_universe_d2_022_dstk_basefill_005'] = {'inputs': ['dstk_basefill_005'], 'func': dstk_base_universe_d2_022_dstk_basefill_005}


def dstk_base_universe_d2_023_dstk_basefill_007(dstk_basefill_007):
    return _base_universe_d2(dstk_basefill_007, 23)
DSTK_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['dstk_base_universe_d2_023_dstk_basefill_007'] = {'inputs': ['dstk_basefill_007'], 'func': dstk_base_universe_d2_023_dstk_basefill_007}


def dstk_base_universe_d2_024_dstk_basefill_011(dstk_basefill_011):
    return _base_universe_d2(dstk_basefill_011, 24)
DSTK_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['dstk_base_universe_d2_024_dstk_basefill_011'] = {'inputs': ['dstk_basefill_011'], 'func': dstk_base_universe_d2_024_dstk_basefill_011}


def dstk_base_universe_d2_025_dstk_basefill_013(dstk_basefill_013):
    return _base_universe_d2(dstk_basefill_013, 25)
DSTK_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['dstk_base_universe_d2_025_dstk_basefill_013'] = {'inputs': ['dstk_basefill_013'], 'func': dstk_base_universe_d2_025_dstk_basefill_013}


def dstk_base_universe_d2_026_dstk_basefill_017(dstk_basefill_017):
    return _base_universe_d2(dstk_basefill_017, 26)
DSTK_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['dstk_base_universe_d2_026_dstk_basefill_017'] = {'inputs': ['dstk_basefill_017'], 'func': dstk_base_universe_d2_026_dstk_basefill_017}


def dstk_base_universe_d2_027_dstk_basefill_019(dstk_basefill_019):
    return _base_universe_d2(dstk_basefill_019, 27)
DSTK_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['dstk_base_universe_d2_027_dstk_basefill_019'] = {'inputs': ['dstk_basefill_019'], 'func': dstk_base_universe_d2_027_dstk_basefill_019}


def dstk_base_universe_d2_028_dstk_basefill_023(dstk_basefill_023):
    return _base_universe_d2(dstk_basefill_023, 28)
DSTK_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['dstk_base_universe_d2_028_dstk_basefill_023'] = {'inputs': ['dstk_basefill_023'], 'func': dstk_base_universe_d2_028_dstk_basefill_023}


def dstk_base_universe_d2_029_dstk_basefill_025(dstk_basefill_025):
    return _base_universe_d2(dstk_basefill_025, 29)
DSTK_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['dstk_base_universe_d2_029_dstk_basefill_025'] = {'inputs': ['dstk_basefill_025'], 'func': dstk_base_universe_d2_029_dstk_basefill_025}


def dstk_base_universe_d2_030_dstk_basefill_029(dstk_basefill_029):
    return _base_universe_d2(dstk_basefill_029, 30)
DSTK_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['dstk_base_universe_d2_030_dstk_basefill_029'] = {'inputs': ['dstk_basefill_029'], 'func': dstk_base_universe_d2_030_dstk_basefill_029}


def dstk_base_universe_d2_031_dstk_basefill_031(dstk_basefill_031):
    return _base_universe_d2(dstk_basefill_031, 31)
DSTK_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['dstk_base_universe_d2_031_dstk_basefill_031'] = {'inputs': ['dstk_basefill_031'], 'func': dstk_base_universe_d2_031_dstk_basefill_031}


def dstk_base_universe_d2_032_dstk_basefill_032(dstk_basefill_032):
    return _base_universe_d2(dstk_basefill_032, 32)
DSTK_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['dstk_base_universe_d2_032_dstk_basefill_032'] = {'inputs': ['dstk_basefill_032'], 'func': dstk_base_universe_d2_032_dstk_basefill_032}


def dstk_base_universe_d2_033_dstk_basefill_033(dstk_basefill_033):
    return _base_universe_d2(dstk_basefill_033, 33)
DSTK_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['dstk_base_universe_d2_033_dstk_basefill_033'] = {'inputs': ['dstk_basefill_033'], 'func': dstk_base_universe_d2_033_dstk_basefill_033}


def dstk_base_universe_d2_034_dstk_basefill_034(dstk_basefill_034):
    return _base_universe_d2(dstk_basefill_034, 34)
DSTK_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['dstk_base_universe_d2_034_dstk_basefill_034'] = {'inputs': ['dstk_basefill_034'], 'func': dstk_base_universe_d2_034_dstk_basefill_034}


def dstk_base_universe_d2_035_dstk_basefill_035(dstk_basefill_035):
    return _base_universe_d2(dstk_basefill_035, 35)
DSTK_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['dstk_base_universe_d2_035_dstk_basefill_035'] = {'inputs': ['dstk_basefill_035'], 'func': dstk_base_universe_d2_035_dstk_basefill_035}


def dstk_base_universe_d2_036_dstk_basefill_036(dstk_basefill_036):
    return _base_universe_d2(dstk_basefill_036, 36)
DSTK_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['dstk_base_universe_d2_036_dstk_basefill_036'] = {'inputs': ['dstk_basefill_036'], 'func': dstk_base_universe_d2_036_dstk_basefill_036}


def dstk_base_universe_d2_037_dstk_basefill_037(dstk_basefill_037):
    return _base_universe_d2(dstk_basefill_037, 37)
DSTK_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['dstk_base_universe_d2_037_dstk_basefill_037'] = {'inputs': ['dstk_basefill_037'], 'func': dstk_base_universe_d2_037_dstk_basefill_037}


def dstk_base_universe_d2_038_dstk_basefill_038(dstk_basefill_038):
    return _base_universe_d2(dstk_basefill_038, 38)
DSTK_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['dstk_base_universe_d2_038_dstk_basefill_038'] = {'inputs': ['dstk_basefill_038'], 'func': dstk_base_universe_d2_038_dstk_basefill_038}


def dstk_base_universe_d2_039_dstk_basefill_039(dstk_basefill_039):
    return _base_universe_d2(dstk_basefill_039, 39)
DSTK_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['dstk_base_universe_d2_039_dstk_basefill_039'] = {'inputs': ['dstk_basefill_039'], 'func': dstk_base_universe_d2_039_dstk_basefill_039}


def dstk_base_universe_d2_040_dstk_basefill_040(dstk_basefill_040):
    return _base_universe_d2(dstk_basefill_040, 40)
DSTK_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['dstk_base_universe_d2_040_dstk_basefill_040'] = {'inputs': ['dstk_basefill_040'], 'func': dstk_base_universe_d2_040_dstk_basefill_040}


def dstk_base_universe_d2_041_dstk_basefill_041(dstk_basefill_041):
    return _base_universe_d2(dstk_basefill_041, 41)
DSTK_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['dstk_base_universe_d2_041_dstk_basefill_041'] = {'inputs': ['dstk_basefill_041'], 'func': dstk_base_universe_d2_041_dstk_basefill_041}


def dstk_base_universe_d2_042_dstk_basefill_042(dstk_basefill_042):
    return _base_universe_d2(dstk_basefill_042, 42)
DSTK_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['dstk_base_universe_d2_042_dstk_basefill_042'] = {'inputs': ['dstk_basefill_042'], 'func': dstk_base_universe_d2_042_dstk_basefill_042}


def dstk_base_universe_d2_043_dstk_basefill_043(dstk_basefill_043):
    return _base_universe_d2(dstk_basefill_043, 43)
DSTK_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['dstk_base_universe_d2_043_dstk_basefill_043'] = {'inputs': ['dstk_basefill_043'], 'func': dstk_base_universe_d2_043_dstk_basefill_043}


def dstk_base_universe_d2_044_dstk_basefill_044(dstk_basefill_044):
    return _base_universe_d2(dstk_basefill_044, 44)
DSTK_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['dstk_base_universe_d2_044_dstk_basefill_044'] = {'inputs': ['dstk_basefill_044'], 'func': dstk_base_universe_d2_044_dstk_basefill_044}


def dstk_base_universe_d2_045_dstk_basefill_045(dstk_basefill_045):
    return _base_universe_d2(dstk_basefill_045, 45)
DSTK_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['dstk_base_universe_d2_045_dstk_basefill_045'] = {'inputs': ['dstk_basefill_045'], 'func': dstk_base_universe_d2_045_dstk_basefill_045}


def dstk_base_universe_d2_046_dstk_basefill_046(dstk_basefill_046):
    return _base_universe_d2(dstk_basefill_046, 46)
DSTK_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['dstk_base_universe_d2_046_dstk_basefill_046'] = {'inputs': ['dstk_basefill_046'], 'func': dstk_base_universe_d2_046_dstk_basefill_046}


def dstk_base_universe_d2_047_dstk_basefill_047(dstk_basefill_047):
    return _base_universe_d2(dstk_basefill_047, 47)
DSTK_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['dstk_base_universe_d2_047_dstk_basefill_047'] = {'inputs': ['dstk_basefill_047'], 'func': dstk_base_universe_d2_047_dstk_basefill_047}


def dstk_base_universe_d2_048_dstk_basefill_048(dstk_basefill_048):
    return _base_universe_d2(dstk_basefill_048, 48)
DSTK_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['dstk_base_universe_d2_048_dstk_basefill_048'] = {'inputs': ['dstk_basefill_048'], 'func': dstk_base_universe_d2_048_dstk_basefill_048}


def dstk_base_universe_d2_049_dstk_basefill_049(dstk_basefill_049):
    return _base_universe_d2(dstk_basefill_049, 49)
DSTK_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['dstk_base_universe_d2_049_dstk_basefill_049'] = {'inputs': ['dstk_basefill_049'], 'func': dstk_base_universe_d2_049_dstk_basefill_049}


def dstk_base_universe_d2_050_dstk_basefill_050(dstk_basefill_050):
    return _base_universe_d2(dstk_basefill_050, 50)
DSTK_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['dstk_base_universe_d2_050_dstk_basefill_050'] = {'inputs': ['dstk_basefill_050'], 'func': dstk_base_universe_d2_050_dstk_basefill_050}


def dstk_base_universe_d2_051_dstk_basefill_051(dstk_basefill_051):
    return _base_universe_d2(dstk_basefill_051, 51)
DSTK_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['dstk_base_universe_d2_051_dstk_basefill_051'] = {'inputs': ['dstk_basefill_051'], 'func': dstk_base_universe_d2_051_dstk_basefill_051}


def dstk_base_universe_d2_052_dstk_basefill_052(dstk_basefill_052):
    return _base_universe_d2(dstk_basefill_052, 52)
DSTK_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['dstk_base_universe_d2_052_dstk_basefill_052'] = {'inputs': ['dstk_basefill_052'], 'func': dstk_base_universe_d2_052_dstk_basefill_052}


def dstk_base_universe_d2_053_dstk_basefill_053(dstk_basefill_053):
    return _base_universe_d2(dstk_basefill_053, 53)
DSTK_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['dstk_base_universe_d2_053_dstk_basefill_053'] = {'inputs': ['dstk_basefill_053'], 'func': dstk_base_universe_d2_053_dstk_basefill_053}


def dstk_base_universe_d2_054_dstk_basefill_054(dstk_basefill_054):
    return _base_universe_d2(dstk_basefill_054, 54)
DSTK_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['dstk_base_universe_d2_054_dstk_basefill_054'] = {'inputs': ['dstk_basefill_054'], 'func': dstk_base_universe_d2_054_dstk_basefill_054}


def dstk_base_universe_d2_055_dstk_basefill_055(dstk_basefill_055):
    return _base_universe_d2(dstk_basefill_055, 55)
DSTK_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['dstk_base_universe_d2_055_dstk_basefill_055'] = {'inputs': ['dstk_basefill_055'], 'func': dstk_base_universe_d2_055_dstk_basefill_055}


def dstk_base_universe_d2_056_dstk_basefill_056(dstk_basefill_056):
    return _base_universe_d2(dstk_basefill_056, 56)
DSTK_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['dstk_base_universe_d2_056_dstk_basefill_056'] = {'inputs': ['dstk_basefill_056'], 'func': dstk_base_universe_d2_056_dstk_basefill_056}


def dstk_base_universe_d2_057_dstk_basefill_057(dstk_basefill_057):
    return _base_universe_d2(dstk_basefill_057, 57)
DSTK_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['dstk_base_universe_d2_057_dstk_basefill_057'] = {'inputs': ['dstk_basefill_057'], 'func': dstk_base_universe_d2_057_dstk_basefill_057}


def dstk_base_universe_d2_058_dstk_basefill_058(dstk_basefill_058):
    return _base_universe_d2(dstk_basefill_058, 58)
DSTK_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['dstk_base_universe_d2_058_dstk_basefill_058'] = {'inputs': ['dstk_basefill_058'], 'func': dstk_base_universe_d2_058_dstk_basefill_058}


def dstk_base_universe_d2_059_dstk_basefill_059(dstk_basefill_059):
    return _base_universe_d2(dstk_basefill_059, 59)
DSTK_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['dstk_base_universe_d2_059_dstk_basefill_059'] = {'inputs': ['dstk_basefill_059'], 'func': dstk_base_universe_d2_059_dstk_basefill_059}


def dstk_base_universe_d2_060_dstk_basefill_060(dstk_basefill_060):
    return _base_universe_d2(dstk_basefill_060, 60)
DSTK_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['dstk_base_universe_d2_060_dstk_basefill_060'] = {'inputs': ['dstk_basefill_060'], 'func': dstk_base_universe_d2_060_dstk_basefill_060}


def dstk_base_universe_d2_061_dstk_basefill_061(dstk_basefill_061):
    return _base_universe_d2(dstk_basefill_061, 61)
DSTK_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['dstk_base_universe_d2_061_dstk_basefill_061'] = {'inputs': ['dstk_basefill_061'], 'func': dstk_base_universe_d2_061_dstk_basefill_061}


def dstk_base_universe_d2_062_dstk_basefill_062(dstk_basefill_062):
    return _base_universe_d2(dstk_basefill_062, 62)
DSTK_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['dstk_base_universe_d2_062_dstk_basefill_062'] = {'inputs': ['dstk_basefill_062'], 'func': dstk_base_universe_d2_062_dstk_basefill_062}


def dstk_base_universe_d2_063_dstk_basefill_063(dstk_basefill_063):
    return _base_universe_d2(dstk_basefill_063, 63)
DSTK_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['dstk_base_universe_d2_063_dstk_basefill_063'] = {'inputs': ['dstk_basefill_063'], 'func': dstk_base_universe_d2_063_dstk_basefill_063}


def dstk_base_universe_d2_064_dstk_basefill_064(dstk_basefill_064):
    return _base_universe_d2(dstk_basefill_064, 64)
DSTK_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['dstk_base_universe_d2_064_dstk_basefill_064'] = {'inputs': ['dstk_basefill_064'], 'func': dstk_base_universe_d2_064_dstk_basefill_064}


def dstk_base_universe_d2_065_dstk_basefill_065(dstk_basefill_065):
    return _base_universe_d2(dstk_basefill_065, 65)
DSTK_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['dstk_base_universe_d2_065_dstk_basefill_065'] = {'inputs': ['dstk_basefill_065'], 'func': dstk_base_universe_d2_065_dstk_basefill_065}


def dstk_base_universe_d2_066_dstk_basefill_066(dstk_basefill_066):
    return _base_universe_d2(dstk_basefill_066, 66)
DSTK_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['dstk_base_universe_d2_066_dstk_basefill_066'] = {'inputs': ['dstk_basefill_066'], 'func': dstk_base_universe_d2_066_dstk_basefill_066}


def dstk_base_universe_d2_067_dstk_basefill_067(dstk_basefill_067):
    return _base_universe_d2(dstk_basefill_067, 67)
DSTK_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['dstk_base_universe_d2_067_dstk_basefill_067'] = {'inputs': ['dstk_basefill_067'], 'func': dstk_base_universe_d2_067_dstk_basefill_067}


def dstk_base_universe_d2_068_dstk_basefill_068(dstk_basefill_068):
    return _base_universe_d2(dstk_basefill_068, 68)
DSTK_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['dstk_base_universe_d2_068_dstk_basefill_068'] = {'inputs': ['dstk_basefill_068'], 'func': dstk_base_universe_d2_068_dstk_basefill_068}


def dstk_base_universe_d2_069_dstk_basefill_069(dstk_basefill_069):
    return _base_universe_d2(dstk_basefill_069, 69)
DSTK_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['dstk_base_universe_d2_069_dstk_basefill_069'] = {'inputs': ['dstk_basefill_069'], 'func': dstk_base_universe_d2_069_dstk_basefill_069}


def dstk_base_universe_d2_070_dstk_basefill_070(dstk_basefill_070):
    return _base_universe_d2(dstk_basefill_070, 70)
DSTK_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['dstk_base_universe_d2_070_dstk_basefill_070'] = {'inputs': ['dstk_basefill_070'], 'func': dstk_base_universe_d2_070_dstk_basefill_070}


def dstk_base_universe_d2_071_dstk_basefill_071(dstk_basefill_071):
    return _base_universe_d2(dstk_basefill_071, 71)
DSTK_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['dstk_base_universe_d2_071_dstk_basefill_071'] = {'inputs': ['dstk_basefill_071'], 'func': dstk_base_universe_d2_071_dstk_basefill_071}


def dstk_base_universe_d2_072_dstk_basefill_072(dstk_basefill_072):
    return _base_universe_d2(dstk_basefill_072, 72)
DSTK_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['dstk_base_universe_d2_072_dstk_basefill_072'] = {'inputs': ['dstk_basefill_072'], 'func': dstk_base_universe_d2_072_dstk_basefill_072}


def dstk_base_universe_d2_073_dstk_basefill_073(dstk_basefill_073):
    return _base_universe_d2(dstk_basefill_073, 73)
DSTK_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['dstk_base_universe_d2_073_dstk_basefill_073'] = {'inputs': ['dstk_basefill_073'], 'func': dstk_base_universe_d2_073_dstk_basefill_073}


def dstk_base_universe_d2_074_dstk_basefill_074(dstk_basefill_074):
    return _base_universe_d2(dstk_basefill_074, 74)
DSTK_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['dstk_base_universe_d2_074_dstk_basefill_074'] = {'inputs': ['dstk_basefill_074'], 'func': dstk_base_universe_d2_074_dstk_basefill_074}


def dstk_base_universe_d2_075_dstk_basefill_075(dstk_basefill_075):
    return _base_universe_d2(dstk_basefill_075, 75)
DSTK_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['dstk_base_universe_d2_075_dstk_basefill_075'] = {'inputs': ['dstk_basefill_075'], 'func': dstk_base_universe_d2_075_dstk_basefill_075}
