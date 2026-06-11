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



def tin_001_amihud_illiquidity_roc_1(amihud_illiquidity):
    feature = _s(amihud_illiquidity)
    return (_roc(feature, 1)).reindex(feature.index)

def tin_007_amihud_illiquidity_roc_5(amihud_illiquidity):
    feature = _s(amihud_illiquidity)
    return (_roc(feature, 5)).reindex(feature.index)

def tin_013_amihud_illiquidity_roc_42(amihud_illiquidity):
    feature = _s(amihud_illiquidity)
    return (_roc(feature, 42)).reindex(feature.index)

def tin_154_tin_019_amihud_illiquidity_42_019_roc_126(amihud_illiquidity):
    feature = _s(amihud_illiquidity)
    return (_roc(feature, 126)).reindex(feature.index)

def tin_155_tin_025_amihud_illiquidity_378_025_roc_378(amihud_illiquidity):
    feature = _s(amihud_illiquidity)
    return (_roc(feature, 378)).reindex(feature.index)






















TRADING_INTENSITY_REGISTRY_2ND_DERIVATIVES = {
    'tin_001_amihud_illiquidity_roc_1': {'inputs': ['amihud_illiquidity'], 'func': tin_001_amihud_illiquidity_roc_1},
    'tin_007_amihud_illiquidity_roc_5': {'inputs': ['amihud_illiquidity'], 'func': tin_007_amihud_illiquidity_roc_5},
    'tin_013_amihud_illiquidity_roc_42': {'inputs': ['amihud_illiquidity'], 'func': tin_013_amihud_illiquidity_roc_42},
    'tin_154_tin_019_amihud_illiquidity_42_019_roc_126': {'inputs': ['amihud_illiquidity'], 'func': tin_154_tin_019_amihud_illiquidity_42_019_roc_126},
    'tin_155_tin_025_amihud_illiquidity_378_025_roc_378': {'inputs': ['amihud_illiquidity'], 'func': tin_155_tin_025_amihud_illiquidity_378_025_roc_378},
}


# Replacement 2nd-derivative features restored after redundancy audit.

import numpy as np
import pandas as pd


def _s(x):
    return pd.Series(x).astype(float)


def _clean(x):
    return _s(x).replace([np.inf, -np.inf], np.nan)


TI_REPLACEMENT_2ND_DERIVATIVES_REGISTRY = {}


def ti_replacement_d2_001(ti_replacement_001):
    feature = _clean(ti_replacement_001)
    delta = feature.diff(2)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00001000).reindex(feature.index)
TI_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ti_replacement_d2_001'] = {'inputs': ['ti_replacement_001'], 'func': ti_replacement_d2_001}


def ti_replacement_d2_002(ti_replacement_002):
    feature = _clean(ti_replacement_002)
    delta = feature.diff(3)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00002000).reindex(feature.index)
TI_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ti_replacement_d2_002'] = {'inputs': ['ti_replacement_002'], 'func': ti_replacement_d2_002}


def ti_replacement_d2_003(ti_replacement_003):
    feature = _clean(ti_replacement_003)
    delta = feature.diff(5)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00003000).reindex(feature.index)
TI_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ti_replacement_d2_003'] = {'inputs': ['ti_replacement_003'], 'func': ti_replacement_d2_003}


def ti_replacement_d2_004(ti_replacement_004):
    feature = _clean(ti_replacement_004)
    delta = feature.diff(8)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00004000).reindex(feature.index)
TI_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ti_replacement_d2_004'] = {'inputs': ['ti_replacement_004'], 'func': ti_replacement_d2_004}


def ti_replacement_d2_005(ti_replacement_005):
    feature = _clean(ti_replacement_005)
    delta = feature.diff(13)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00005000).reindex(feature.index)
TI_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ti_replacement_d2_005'] = {'inputs': ['ti_replacement_005'], 'func': ti_replacement_d2_005}


def ti_replacement_d2_006(ti_replacement_006):
    feature = _clean(ti_replacement_006)
    delta = feature.diff(21)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00006000).reindex(feature.index)
TI_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ti_replacement_d2_006'] = {'inputs': ['ti_replacement_006'], 'func': ti_replacement_d2_006}


def ti_replacement_d2_007(ti_replacement_007):
    feature = _clean(ti_replacement_007)
    delta = feature.diff(34)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00007000).reindex(feature.index)
TI_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ti_replacement_d2_007'] = {'inputs': ['ti_replacement_007'], 'func': ti_replacement_d2_007}


def ti_replacement_d2_008(ti_replacement_008):
    feature = _clean(ti_replacement_008)
    delta = feature.diff(55)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00008000).reindex(feature.index)
TI_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ti_replacement_d2_008'] = {'inputs': ['ti_replacement_008'], 'func': ti_replacement_d2_008}


def ti_replacement_d2_009(ti_replacement_009):
    feature = _clean(ti_replacement_009)
    delta = feature.diff(89)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00009000).reindex(feature.index)
TI_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ti_replacement_d2_009'] = {'inputs': ['ti_replacement_009'], 'func': ti_replacement_d2_009}


def ti_replacement_d2_010(ti_replacement_010):
    feature = _clean(ti_replacement_010)
    delta = feature.diff(1)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00010000).reindex(feature.index)
TI_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ti_replacement_d2_010'] = {'inputs': ['ti_replacement_010'], 'func': ti_replacement_d2_010}


def ti_replacement_d2_011(ti_replacement_011):
    feature = _clean(ti_replacement_011)
    delta = feature.diff(2)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00011000).reindex(feature.index)
TI_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ti_replacement_d2_011'] = {'inputs': ['ti_replacement_011'], 'func': ti_replacement_d2_011}


def ti_replacement_d2_012(ti_replacement_012):
    feature = _clean(ti_replacement_012)
    delta = feature.diff(3)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00012000).reindex(feature.index)
TI_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ti_replacement_d2_012'] = {'inputs': ['ti_replacement_012'], 'func': ti_replacement_d2_012}


def ti_replacement_d2_013(ti_replacement_013):
    feature = _clean(ti_replacement_013)
    delta = feature.diff(5)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00013000).reindex(feature.index)
TI_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ti_replacement_d2_013'] = {'inputs': ['ti_replacement_013'], 'func': ti_replacement_d2_013}


def ti_replacement_d2_014(ti_replacement_014):
    feature = _clean(ti_replacement_014)
    delta = feature.diff(8)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00014000).reindex(feature.index)
TI_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ti_replacement_d2_014'] = {'inputs': ['ti_replacement_014'], 'func': ti_replacement_d2_014}


def ti_replacement_d2_015(ti_replacement_015):
    feature = _clean(ti_replacement_015)
    delta = feature.diff(13)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00015000).reindex(feature.index)
TI_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ti_replacement_d2_015'] = {'inputs': ['ti_replacement_015'], 'func': ti_replacement_d2_015}


def ti_replacement_d2_016(ti_replacement_016):
    feature = _clean(ti_replacement_016)
    delta = feature.diff(21)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00016000).reindex(feature.index)
TI_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ti_replacement_d2_016'] = {'inputs': ['ti_replacement_016'], 'func': ti_replacement_d2_016}


def ti_replacement_d2_017(ti_replacement_017):
    feature = _clean(ti_replacement_017)
    delta = feature.diff(34)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00017000).reindex(feature.index)
TI_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ti_replacement_d2_017'] = {'inputs': ['ti_replacement_017'], 'func': ti_replacement_d2_017}


def ti_replacement_d2_018(ti_replacement_018):
    feature = _clean(ti_replacement_018)
    delta = feature.diff(55)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00018000).reindex(feature.index)
TI_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ti_replacement_d2_018'] = {'inputs': ['ti_replacement_018'], 'func': ti_replacement_d2_018}


def ti_replacement_d2_019(ti_replacement_019):
    feature = _clean(ti_replacement_019)
    delta = feature.diff(89)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00019000).reindex(feature.index)
TI_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ti_replacement_d2_019'] = {'inputs': ['ti_replacement_019'], 'func': ti_replacement_d2_019}


def ti_replacement_d2_020(ti_replacement_020):
    feature = _clean(ti_replacement_020)
    delta = feature.diff(1)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00020000).reindex(feature.index)
TI_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ti_replacement_d2_020'] = {'inputs': ['ti_replacement_020'], 'func': ti_replacement_d2_020}


def ti_replacement_d2_021(ti_replacement_021):
    feature = _clean(ti_replacement_021)
    delta = feature.diff(2)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00021000).reindex(feature.index)
TI_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ti_replacement_d2_021'] = {'inputs': ['ti_replacement_021'], 'func': ti_replacement_d2_021}


def ti_replacement_d2_022(ti_replacement_022):
    feature = _clean(ti_replacement_022)
    delta = feature.diff(3)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00022000).reindex(feature.index)
TI_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ti_replacement_d2_022'] = {'inputs': ['ti_replacement_022'], 'func': ti_replacement_d2_022}


def ti_replacement_d2_023(ti_replacement_023):
    feature = _clean(ti_replacement_023)
    delta = feature.diff(5)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00023000).reindex(feature.index)
TI_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ti_replacement_d2_023'] = {'inputs': ['ti_replacement_023'], 'func': ti_replacement_d2_023}


def ti_replacement_d2_024(ti_replacement_024):
    feature = _clean(ti_replacement_024)
    delta = feature.diff(8)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00024000).reindex(feature.index)
TI_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ti_replacement_d2_024'] = {'inputs': ['ti_replacement_024'], 'func': ti_replacement_d2_024}


def ti_replacement_d2_025(ti_replacement_025):
    feature = _clean(ti_replacement_025)
    delta = feature.diff(13)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00025000).reindex(feature.index)
TI_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ti_replacement_d2_025'] = {'inputs': ['ti_replacement_025'], 'func': ti_replacement_d2_025}


def ti_replacement_d2_026(ti_replacement_026):
    feature = _clean(ti_replacement_026)
    delta = feature.diff(21)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00026000).reindex(feature.index)
TI_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ti_replacement_d2_026'] = {'inputs': ['ti_replacement_026'], 'func': ti_replacement_d2_026}


def ti_replacement_d2_027(ti_replacement_027):
    feature = _clean(ti_replacement_027)
    delta = feature.diff(34)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00027000).reindex(feature.index)
TI_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ti_replacement_d2_027'] = {'inputs': ['ti_replacement_027'], 'func': ti_replacement_d2_027}


def ti_replacement_d2_028(ti_replacement_028):
    feature = _clean(ti_replacement_028)
    delta = feature.diff(55)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00028000).reindex(feature.index)
TI_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ti_replacement_d2_028'] = {'inputs': ['ti_replacement_028'], 'func': ti_replacement_d2_028}


def ti_replacement_d2_029(ti_replacement_029):
    feature = _clean(ti_replacement_029)
    delta = feature.diff(89)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00029000).reindex(feature.index)
TI_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ti_replacement_d2_029'] = {'inputs': ['ti_replacement_029'], 'func': ti_replacement_d2_029}


def ti_replacement_d2_030(ti_replacement_030):
    feature = _clean(ti_replacement_030)
    delta = feature.diff(1)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00030000).reindex(feature.index)
TI_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ti_replacement_d2_030'] = {'inputs': ['ti_replacement_030'], 'func': ti_replacement_d2_030}


def ti_replacement_d2_031(ti_replacement_031):
    feature = _clean(ti_replacement_031)
    delta = feature.diff(2)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00031000).reindex(feature.index)
TI_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ti_replacement_d2_031'] = {'inputs': ['ti_replacement_031'], 'func': ti_replacement_d2_031}


def ti_replacement_d2_032(ti_replacement_032):
    feature = _clean(ti_replacement_032)
    delta = feature.diff(3)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00032000).reindex(feature.index)
TI_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ti_replacement_d2_032'] = {'inputs': ['ti_replacement_032'], 'func': ti_replacement_d2_032}


def ti_replacement_d2_033(ti_replacement_033):
    feature = _clean(ti_replacement_033)
    delta = feature.diff(5)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00033000).reindex(feature.index)
TI_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ti_replacement_d2_033'] = {'inputs': ['ti_replacement_033'], 'func': ti_replacement_d2_033}


def ti_replacement_d2_034(ti_replacement_034):
    feature = _clean(ti_replacement_034)
    delta = feature.diff(8)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00034000).reindex(feature.index)
TI_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ti_replacement_d2_034'] = {'inputs': ['ti_replacement_034'], 'func': ti_replacement_d2_034}


def ti_replacement_d2_035(ti_replacement_035):
    feature = _clean(ti_replacement_035)
    delta = feature.diff(13)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00035000).reindex(feature.index)
TI_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ti_replacement_d2_035'] = {'inputs': ['ti_replacement_035'], 'func': ti_replacement_d2_035}


def ti_replacement_d2_036(ti_replacement_036):
    feature = _clean(ti_replacement_036)
    delta = feature.diff(21)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00036000).reindex(feature.index)
TI_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ti_replacement_d2_036'] = {'inputs': ['ti_replacement_036'], 'func': ti_replacement_d2_036}


def ti_replacement_d2_037(ti_replacement_037):
    feature = _clean(ti_replacement_037)
    delta = feature.diff(34)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00037000).reindex(feature.index)
TI_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ti_replacement_d2_037'] = {'inputs': ['ti_replacement_037'], 'func': ti_replacement_d2_037}


def ti_replacement_d2_038(ti_replacement_038):
    feature = _clean(ti_replacement_038)
    delta = feature.diff(55)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00038000).reindex(feature.index)
TI_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ti_replacement_d2_038'] = {'inputs': ['ti_replacement_038'], 'func': ti_replacement_d2_038}


def ti_replacement_d2_039(ti_replacement_039):
    feature = _clean(ti_replacement_039)
    delta = feature.diff(89)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00039000).reindex(feature.index)
TI_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ti_replacement_d2_039'] = {'inputs': ['ti_replacement_039'], 'func': ti_replacement_d2_039}


def ti_replacement_d2_040(ti_replacement_040):
    feature = _clean(ti_replacement_040)
    delta = feature.diff(1)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00040000).reindex(feature.index)
TI_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ti_replacement_d2_040'] = {'inputs': ['ti_replacement_040'], 'func': ti_replacement_d2_040}


def ti_replacement_d2_041(ti_replacement_041):
    feature = _clean(ti_replacement_041)
    delta = feature.diff(2)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00041000).reindex(feature.index)
TI_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ti_replacement_d2_041'] = {'inputs': ['ti_replacement_041'], 'func': ti_replacement_d2_041}


def ti_replacement_d2_042(ti_replacement_042):
    feature = _clean(ti_replacement_042)
    delta = feature.diff(3)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00042000).reindex(feature.index)
TI_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ti_replacement_d2_042'] = {'inputs': ['ti_replacement_042'], 'func': ti_replacement_d2_042}


def ti_replacement_d2_043(ti_replacement_043):
    feature = _clean(ti_replacement_043)
    delta = feature.diff(5)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00043000).reindex(feature.index)
TI_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ti_replacement_d2_043'] = {'inputs': ['ti_replacement_043'], 'func': ti_replacement_d2_043}


def ti_replacement_d2_044(ti_replacement_044):
    feature = _clean(ti_replacement_044)
    delta = feature.diff(8)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00044000).reindex(feature.index)
TI_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ti_replacement_d2_044'] = {'inputs': ['ti_replacement_044'], 'func': ti_replacement_d2_044}


def ti_replacement_d2_045(ti_replacement_045):
    feature = _clean(ti_replacement_045)
    delta = feature.diff(13)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00045000).reindex(feature.index)
TI_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ti_replacement_d2_045'] = {'inputs': ['ti_replacement_045'], 'func': ti_replacement_d2_045}


def ti_replacement_d2_046(ti_replacement_046):
    feature = _clean(ti_replacement_046)
    delta = feature.diff(21)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00046000).reindex(feature.index)
TI_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ti_replacement_d2_046'] = {'inputs': ['ti_replacement_046'], 'func': ti_replacement_d2_046}


def ti_replacement_d2_047(ti_replacement_047):
    feature = _clean(ti_replacement_047)
    delta = feature.diff(34)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00047000).reindex(feature.index)
TI_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ti_replacement_d2_047'] = {'inputs': ['ti_replacement_047'], 'func': ti_replacement_d2_047}


def ti_replacement_d2_048(ti_replacement_048):
    feature = _clean(ti_replacement_048)
    delta = feature.diff(55)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00048000).reindex(feature.index)
TI_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ti_replacement_d2_048'] = {'inputs': ['ti_replacement_048'], 'func': ti_replacement_d2_048}


def ti_replacement_d2_049(ti_replacement_049):
    feature = _clean(ti_replacement_049)
    delta = feature.diff(89)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00049000).reindex(feature.index)
TI_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ti_replacement_d2_049'] = {'inputs': ['ti_replacement_049'], 'func': ti_replacement_d2_049}


def ti_replacement_d2_050(ti_replacement_050):
    feature = _clean(ti_replacement_050)
    delta = feature.diff(1)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00050000).reindex(feature.index)
TI_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ti_replacement_d2_050'] = {'inputs': ['ti_replacement_050'], 'func': ti_replacement_d2_050}


def ti_replacement_d2_051(ti_replacement_051):
    feature = _clean(ti_replacement_051)
    delta = feature.diff(2)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00051000).reindex(feature.index)
TI_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ti_replacement_d2_051'] = {'inputs': ['ti_replacement_051'], 'func': ti_replacement_d2_051}


def ti_replacement_d2_052(ti_replacement_052):
    feature = _clean(ti_replacement_052)
    delta = feature.diff(3)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00052000).reindex(feature.index)
TI_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ti_replacement_d2_052'] = {'inputs': ['ti_replacement_052'], 'func': ti_replacement_d2_052}


def ti_replacement_d2_053(ti_replacement_053):
    feature = _clean(ti_replacement_053)
    delta = feature.diff(5)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00053000).reindex(feature.index)
TI_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ti_replacement_d2_053'] = {'inputs': ['ti_replacement_053'], 'func': ti_replacement_d2_053}


def ti_replacement_d2_054(ti_replacement_054):
    feature = _clean(ti_replacement_054)
    delta = feature.diff(8)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00054000).reindex(feature.index)
TI_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ti_replacement_d2_054'] = {'inputs': ['ti_replacement_054'], 'func': ti_replacement_d2_054}


def ti_replacement_d2_055(ti_replacement_055):
    feature = _clean(ti_replacement_055)
    delta = feature.diff(13)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00055000).reindex(feature.index)
TI_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ti_replacement_d2_055'] = {'inputs': ['ti_replacement_055'], 'func': ti_replacement_d2_055}


def ti_replacement_d2_056(ti_replacement_056):
    feature = _clean(ti_replacement_056)
    delta = feature.diff(21)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00056000).reindex(feature.index)
TI_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ti_replacement_d2_056'] = {'inputs': ['ti_replacement_056'], 'func': ti_replacement_d2_056}


def ti_replacement_d2_057(ti_replacement_057):
    feature = _clean(ti_replacement_057)
    delta = feature.diff(34)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00057000).reindex(feature.index)
TI_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ti_replacement_d2_057'] = {'inputs': ['ti_replacement_057'], 'func': ti_replacement_d2_057}


def ti_replacement_d2_058(ti_replacement_058):
    feature = _clean(ti_replacement_058)
    delta = feature.diff(55)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00058000).reindex(feature.index)
TI_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ti_replacement_d2_058'] = {'inputs': ['ti_replacement_058'], 'func': ti_replacement_d2_058}


def ti_replacement_d2_059(ti_replacement_059):
    feature = _clean(ti_replacement_059)
    delta = feature.diff(89)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00059000).reindex(feature.index)
TI_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ti_replacement_d2_059'] = {'inputs': ['ti_replacement_059'], 'func': ti_replacement_d2_059}


def ti_replacement_d2_060(ti_replacement_060):
    feature = _clean(ti_replacement_060)
    delta = feature.diff(1)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00060000).reindex(feature.index)
TI_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ti_replacement_d2_060'] = {'inputs': ['ti_replacement_060'], 'func': ti_replacement_d2_060}


def ti_replacement_d2_061(ti_replacement_061):
    feature = _clean(ti_replacement_061)
    delta = feature.diff(2)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00061000).reindex(feature.index)
TI_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ti_replacement_d2_061'] = {'inputs': ['ti_replacement_061'], 'func': ti_replacement_d2_061}


def ti_replacement_d2_062(ti_replacement_062):
    feature = _clean(ti_replacement_062)
    delta = feature.diff(3)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00062000).reindex(feature.index)
TI_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ti_replacement_d2_062'] = {'inputs': ['ti_replacement_062'], 'func': ti_replacement_d2_062}


def ti_replacement_d2_063(ti_replacement_063):
    feature = _clean(ti_replacement_063)
    delta = feature.diff(5)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00063000).reindex(feature.index)
TI_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ti_replacement_d2_063'] = {'inputs': ['ti_replacement_063'], 'func': ti_replacement_d2_063}


def ti_replacement_d2_064(ti_replacement_064):
    feature = _clean(ti_replacement_064)
    delta = feature.diff(8)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00064000).reindex(feature.index)
TI_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ti_replacement_d2_064'] = {'inputs': ['ti_replacement_064'], 'func': ti_replacement_d2_064}


def ti_replacement_d2_065(ti_replacement_065):
    feature = _clean(ti_replacement_065)
    delta = feature.diff(13)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00065000).reindex(feature.index)
TI_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ti_replacement_d2_065'] = {'inputs': ['ti_replacement_065'], 'func': ti_replacement_d2_065}


def ti_replacement_d2_066(ti_replacement_066):
    feature = _clean(ti_replacement_066)
    delta = feature.diff(21)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00066000).reindex(feature.index)
TI_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ti_replacement_d2_066'] = {'inputs': ['ti_replacement_066'], 'func': ti_replacement_d2_066}


def ti_replacement_d2_067(ti_replacement_067):
    feature = _clean(ti_replacement_067)
    delta = feature.diff(34)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00067000).reindex(feature.index)
TI_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ti_replacement_d2_067'] = {'inputs': ['ti_replacement_067'], 'func': ti_replacement_d2_067}


def ti_replacement_d2_068(ti_replacement_068):
    feature = _clean(ti_replacement_068)
    delta = feature.diff(55)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00068000).reindex(feature.index)
TI_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ti_replacement_d2_068'] = {'inputs': ['ti_replacement_068'], 'func': ti_replacement_d2_068}


def ti_replacement_d2_069(ti_replacement_069):
    feature = _clean(ti_replacement_069)
    delta = feature.diff(89)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00069000).reindex(feature.index)
TI_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ti_replacement_d2_069'] = {'inputs': ['ti_replacement_069'], 'func': ti_replacement_d2_069}


def ti_replacement_d2_070(ti_replacement_070):
    feature = _clean(ti_replacement_070)
    delta = feature.diff(1)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00070000).reindex(feature.index)
TI_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ti_replacement_d2_070'] = {'inputs': ['ti_replacement_070'], 'func': ti_replacement_d2_070}


def ti_replacement_d2_071(ti_replacement_071):
    feature = _clean(ti_replacement_071)
    delta = feature.diff(2)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00071000).reindex(feature.index)
TI_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ti_replacement_d2_071'] = {'inputs': ['ti_replacement_071'], 'func': ti_replacement_d2_071}


def ti_replacement_d2_072(ti_replacement_072):
    feature = _clean(ti_replacement_072)
    delta = feature.diff(3)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00072000).reindex(feature.index)
TI_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ti_replacement_d2_072'] = {'inputs': ['ti_replacement_072'], 'func': ti_replacement_d2_072}


def ti_replacement_d2_073(ti_replacement_073):
    feature = _clean(ti_replacement_073)
    delta = feature.diff(5)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00073000).reindex(feature.index)
TI_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ti_replacement_d2_073'] = {'inputs': ['ti_replacement_073'], 'func': ti_replacement_d2_073}


def ti_replacement_d2_074(ti_replacement_074):
    feature = _clean(ti_replacement_074)
    delta = feature.diff(8)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00074000).reindex(feature.index)
TI_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ti_replacement_d2_074'] = {'inputs': ['ti_replacement_074'], 'func': ti_replacement_d2_074}


def ti_replacement_d2_075(ti_replacement_075):
    feature = _clean(ti_replacement_075)
    delta = feature.diff(13)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00075000).reindex(feature.index)
TI_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ti_replacement_d2_075'] = {'inputs': ['ti_replacement_075'], 'func': ti_replacement_d2_075}


def ti_replacement_d2_076(ti_replacement_076):
    feature = _clean(ti_replacement_076)
    delta = feature.diff(21)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00076000).reindex(feature.index)
TI_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ti_replacement_d2_076'] = {'inputs': ['ti_replacement_076'], 'func': ti_replacement_d2_076}


def ti_replacement_d2_077(ti_replacement_077):
    feature = _clean(ti_replacement_077)
    delta = feature.diff(34)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00077000).reindex(feature.index)
TI_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ti_replacement_d2_077'] = {'inputs': ['ti_replacement_077'], 'func': ti_replacement_d2_077}


def ti_replacement_d2_078(ti_replacement_078):
    feature = _clean(ti_replacement_078)
    delta = feature.diff(55)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00078000).reindex(feature.index)
TI_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ti_replacement_d2_078'] = {'inputs': ['ti_replacement_078'], 'func': ti_replacement_d2_078}


def ti_replacement_d2_079(ti_replacement_079):
    feature = _clean(ti_replacement_079)
    delta = feature.diff(89)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00079000).reindex(feature.index)
TI_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ti_replacement_d2_079'] = {'inputs': ['ti_replacement_079'], 'func': ti_replacement_d2_079}


def ti_replacement_d2_080(ti_replacement_080):
    feature = _clean(ti_replacement_080)
    delta = feature.diff(1)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00080000).reindex(feature.index)
TI_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ti_replacement_d2_080'] = {'inputs': ['ti_replacement_080'], 'func': ti_replacement_d2_080}


def ti_replacement_d2_081(ti_replacement_081):
    feature = _clean(ti_replacement_081)
    delta = feature.diff(2)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00081000).reindex(feature.index)
TI_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ti_replacement_d2_081'] = {'inputs': ['ti_replacement_081'], 'func': ti_replacement_d2_081}


def ti_replacement_d2_082(ti_replacement_082):
    feature = _clean(ti_replacement_082)
    delta = feature.diff(3)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00082000).reindex(feature.index)
TI_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ti_replacement_d2_082'] = {'inputs': ['ti_replacement_082'], 'func': ti_replacement_d2_082}


def ti_replacement_d2_083(ti_replacement_083):
    feature = _clean(ti_replacement_083)
    delta = feature.diff(5)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00083000).reindex(feature.index)
TI_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ti_replacement_d2_083'] = {'inputs': ['ti_replacement_083'], 'func': ti_replacement_d2_083}


def ti_replacement_d2_084(ti_replacement_084):
    feature = _clean(ti_replacement_084)
    delta = feature.diff(8)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00084000).reindex(feature.index)
TI_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ti_replacement_d2_084'] = {'inputs': ['ti_replacement_084'], 'func': ti_replacement_d2_084}


def ti_replacement_d2_085(ti_replacement_085):
    feature = _clean(ti_replacement_085)
    delta = feature.diff(13)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00085000).reindex(feature.index)
TI_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ti_replacement_d2_085'] = {'inputs': ['ti_replacement_085'], 'func': ti_replacement_d2_085}


def ti_replacement_d2_086(ti_replacement_086):
    feature = _clean(ti_replacement_086)
    delta = feature.diff(21)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00086000).reindex(feature.index)
TI_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ti_replacement_d2_086'] = {'inputs': ['ti_replacement_086'], 'func': ti_replacement_d2_086}


def ti_replacement_d2_087(ti_replacement_087):
    feature = _clean(ti_replacement_087)
    delta = feature.diff(34)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00087000).reindex(feature.index)
TI_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ti_replacement_d2_087'] = {'inputs': ['ti_replacement_087'], 'func': ti_replacement_d2_087}


def ti_replacement_d2_088(ti_replacement_088):
    feature = _clean(ti_replacement_088)
    delta = feature.diff(55)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00088000).reindex(feature.index)
TI_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ti_replacement_d2_088'] = {'inputs': ['ti_replacement_088'], 'func': ti_replacement_d2_088}


def ti_replacement_d2_089(ti_replacement_089):
    feature = _clean(ti_replacement_089)
    delta = feature.diff(89)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00089000).reindex(feature.index)
TI_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ti_replacement_d2_089'] = {'inputs': ['ti_replacement_089'], 'func': ti_replacement_d2_089}


def ti_replacement_d2_090(ti_replacement_090):
    feature = _clean(ti_replacement_090)
    delta = feature.diff(1)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00090000).reindex(feature.index)
TI_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ti_replacement_d2_090'] = {'inputs': ['ti_replacement_090'], 'func': ti_replacement_d2_090}


def ti_replacement_d2_091(ti_replacement_091):
    feature = _clean(ti_replacement_091)
    delta = feature.diff(2)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00091000).reindex(feature.index)
TI_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ti_replacement_d2_091'] = {'inputs': ['ti_replacement_091'], 'func': ti_replacement_d2_091}


def ti_replacement_d2_092(ti_replacement_092):
    feature = _clean(ti_replacement_092)
    delta = feature.diff(3)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00092000).reindex(feature.index)
TI_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ti_replacement_d2_092'] = {'inputs': ['ti_replacement_092'], 'func': ti_replacement_d2_092}


def ti_replacement_d2_093(ti_replacement_093):
    feature = _clean(ti_replacement_093)
    delta = feature.diff(5)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00093000).reindex(feature.index)
TI_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ti_replacement_d2_093'] = {'inputs': ['ti_replacement_093'], 'func': ti_replacement_d2_093}


def ti_replacement_d2_094(ti_replacement_094):
    feature = _clean(ti_replacement_094)
    delta = feature.diff(8)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00094000).reindex(feature.index)
TI_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ti_replacement_d2_094'] = {'inputs': ['ti_replacement_094'], 'func': ti_replacement_d2_094}


def ti_replacement_d2_095(ti_replacement_095):
    feature = _clean(ti_replacement_095)
    delta = feature.diff(13)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00095000).reindex(feature.index)
TI_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ti_replacement_d2_095'] = {'inputs': ['ti_replacement_095'], 'func': ti_replacement_d2_095}


def ti_replacement_d2_096(ti_replacement_096):
    feature = _clean(ti_replacement_096)
    delta = feature.diff(21)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00096000).reindex(feature.index)
TI_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ti_replacement_d2_096'] = {'inputs': ['ti_replacement_096'], 'func': ti_replacement_d2_096}


def ti_replacement_d2_097(ti_replacement_097):
    feature = _clean(ti_replacement_097)
    delta = feature.diff(34)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00097000).reindex(feature.index)
TI_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ti_replacement_d2_097'] = {'inputs': ['ti_replacement_097'], 'func': ti_replacement_d2_097}


def ti_replacement_d2_098(ti_replacement_098):
    feature = _clean(ti_replacement_098)
    delta = feature.diff(55)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00098000).reindex(feature.index)
TI_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ti_replacement_d2_098'] = {'inputs': ['ti_replacement_098'], 'func': ti_replacement_d2_098}


def ti_replacement_d2_099(ti_replacement_099):
    feature = _clean(ti_replacement_099)
    delta = feature.diff(89)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00099000).reindex(feature.index)
TI_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ti_replacement_d2_099'] = {'inputs': ['ti_replacement_099'], 'func': ti_replacement_d2_099}


def ti_replacement_d2_100(ti_replacement_100):
    feature = _clean(ti_replacement_100)
    delta = feature.diff(1)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00100000).reindex(feature.index)
TI_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ti_replacement_d2_100'] = {'inputs': ['ti_replacement_100'], 'func': ti_replacement_d2_100}


def ti_replacement_d2_101(ti_replacement_101):
    feature = _clean(ti_replacement_101)
    delta = feature.diff(2)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00101000).reindex(feature.index)
TI_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ti_replacement_d2_101'] = {'inputs': ['ti_replacement_101'], 'func': ti_replacement_d2_101}


def ti_replacement_d2_102(ti_replacement_102):
    feature = _clean(ti_replacement_102)
    delta = feature.diff(3)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00102000).reindex(feature.index)
TI_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ti_replacement_d2_102'] = {'inputs': ['ti_replacement_102'], 'func': ti_replacement_d2_102}


def ti_replacement_d2_103(ti_replacement_103):
    feature = _clean(ti_replacement_103)
    delta = feature.diff(5)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00103000).reindex(feature.index)
TI_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ti_replacement_d2_103'] = {'inputs': ['ti_replacement_103'], 'func': ti_replacement_d2_103}


def ti_replacement_d2_104(ti_replacement_104):
    feature = _clean(ti_replacement_104)
    delta = feature.diff(8)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00104000).reindex(feature.index)
TI_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ti_replacement_d2_104'] = {'inputs': ['ti_replacement_104'], 'func': ti_replacement_d2_104}


def ti_replacement_d2_105(ti_replacement_105):
    feature = _clean(ti_replacement_105)
    delta = feature.diff(13)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00105000).reindex(feature.index)
TI_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ti_replacement_d2_105'] = {'inputs': ['ti_replacement_105'], 'func': ti_replacement_d2_105}


def ti_replacement_d2_106(ti_replacement_106):
    feature = _clean(ti_replacement_106)
    delta = feature.diff(21)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00106000).reindex(feature.index)
TI_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ti_replacement_d2_106'] = {'inputs': ['ti_replacement_106'], 'func': ti_replacement_d2_106}


def ti_replacement_d2_107(ti_replacement_107):
    feature = _clean(ti_replacement_107)
    delta = feature.diff(34)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00107000).reindex(feature.index)
TI_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ti_replacement_d2_107'] = {'inputs': ['ti_replacement_107'], 'func': ti_replacement_d2_107}


def ti_replacement_d2_108(ti_replacement_108):
    feature = _clean(ti_replacement_108)
    delta = feature.diff(55)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00108000).reindex(feature.index)
TI_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ti_replacement_d2_108'] = {'inputs': ['ti_replacement_108'], 'func': ti_replacement_d2_108}


def ti_replacement_d2_109(ti_replacement_109):
    feature = _clean(ti_replacement_109)
    delta = feature.diff(89)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00109000).reindex(feature.index)
TI_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ti_replacement_d2_109'] = {'inputs': ['ti_replacement_109'], 'func': ti_replacement_d2_109}


def ti_replacement_d2_110(ti_replacement_110):
    feature = _clean(ti_replacement_110)
    delta = feature.diff(1)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00110000).reindex(feature.index)
TI_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ti_replacement_d2_110'] = {'inputs': ['ti_replacement_110'], 'func': ti_replacement_d2_110}


def ti_replacement_d2_111(ti_replacement_111):
    feature = _clean(ti_replacement_111)
    delta = feature.diff(2)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00111000).reindex(feature.index)
TI_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ti_replacement_d2_111'] = {'inputs': ['ti_replacement_111'], 'func': ti_replacement_d2_111}


def ti_replacement_d2_112(ti_replacement_112):
    feature = _clean(ti_replacement_112)
    delta = feature.diff(3)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00112000).reindex(feature.index)
TI_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ti_replacement_d2_112'] = {'inputs': ['ti_replacement_112'], 'func': ti_replacement_d2_112}


def ti_replacement_d2_113(ti_replacement_113):
    feature = _clean(ti_replacement_113)
    delta = feature.diff(5)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00113000).reindex(feature.index)
TI_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ti_replacement_d2_113'] = {'inputs': ['ti_replacement_113'], 'func': ti_replacement_d2_113}


def ti_replacement_d2_114(ti_replacement_114):
    feature = _clean(ti_replacement_114)
    delta = feature.diff(8)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00114000).reindex(feature.index)
TI_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ti_replacement_d2_114'] = {'inputs': ['ti_replacement_114'], 'func': ti_replacement_d2_114}


def ti_replacement_d2_115(ti_replacement_115):
    feature = _clean(ti_replacement_115)
    delta = feature.diff(13)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00115000).reindex(feature.index)
TI_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ti_replacement_d2_115'] = {'inputs': ['ti_replacement_115'], 'func': ti_replacement_d2_115}


def ti_replacement_d2_116(ti_replacement_116):
    feature = _clean(ti_replacement_116)
    delta = feature.diff(21)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00116000).reindex(feature.index)
TI_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ti_replacement_d2_116'] = {'inputs': ['ti_replacement_116'], 'func': ti_replacement_d2_116}


def ti_replacement_d2_117(ti_replacement_117):
    feature = _clean(ti_replacement_117)
    delta = feature.diff(34)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00117000).reindex(feature.index)
TI_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ti_replacement_d2_117'] = {'inputs': ['ti_replacement_117'], 'func': ti_replacement_d2_117}


def ti_replacement_d2_118(ti_replacement_118):
    feature = _clean(ti_replacement_118)
    delta = feature.diff(55)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00118000).reindex(feature.index)
TI_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ti_replacement_d2_118'] = {'inputs': ['ti_replacement_118'], 'func': ti_replacement_d2_118}


def ti_replacement_d2_119(ti_replacement_119):
    feature = _clean(ti_replacement_119)
    delta = feature.diff(89)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00119000).reindex(feature.index)
TI_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ti_replacement_d2_119'] = {'inputs': ['ti_replacement_119'], 'func': ti_replacement_d2_119}


def ti_replacement_d2_120(ti_replacement_120):
    feature = _clean(ti_replacement_120)
    delta = feature.diff(1)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00120000).reindex(feature.index)
TI_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ti_replacement_d2_120'] = {'inputs': ['ti_replacement_120'], 'func': ti_replacement_d2_120}


def ti_replacement_d2_121(ti_replacement_121):
    feature = _clean(ti_replacement_121)
    delta = feature.diff(2)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00121000).reindex(feature.index)
TI_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ti_replacement_d2_121'] = {'inputs': ['ti_replacement_121'], 'func': ti_replacement_d2_121}


def ti_replacement_d2_122(ti_replacement_122):
    feature = _clean(ti_replacement_122)
    delta = feature.diff(3)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00122000).reindex(feature.index)
TI_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ti_replacement_d2_122'] = {'inputs': ['ti_replacement_122'], 'func': ti_replacement_d2_122}


def ti_replacement_d2_123(ti_replacement_123):
    feature = _clean(ti_replacement_123)
    delta = feature.diff(5)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00123000).reindex(feature.index)
TI_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ti_replacement_d2_123'] = {'inputs': ['ti_replacement_123'], 'func': ti_replacement_d2_123}


def ti_replacement_d2_124(ti_replacement_124):
    feature = _clean(ti_replacement_124)
    delta = feature.diff(8)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00124000).reindex(feature.index)
TI_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ti_replacement_d2_124'] = {'inputs': ['ti_replacement_124'], 'func': ti_replacement_d2_124}


def ti_replacement_d2_125(ti_replacement_125):
    feature = _clean(ti_replacement_125)
    delta = feature.diff(13)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00125000).reindex(feature.index)
TI_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ti_replacement_d2_125'] = {'inputs': ['ti_replacement_125'], 'func': ti_replacement_d2_125}


def ti_replacement_d2_126(ti_replacement_126):
    feature = _clean(ti_replacement_126)
    delta = feature.diff(21)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00126000).reindex(feature.index)
TI_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ti_replacement_d2_126'] = {'inputs': ['ti_replacement_126'], 'func': ti_replacement_d2_126}


def ti_replacement_d2_127(ti_replacement_127):
    feature = _clean(ti_replacement_127)
    delta = feature.diff(34)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00127000).reindex(feature.index)
TI_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ti_replacement_d2_127'] = {'inputs': ['ti_replacement_127'], 'func': ti_replacement_d2_127}


def ti_replacement_d2_128(ti_replacement_128):
    feature = _clean(ti_replacement_128)
    delta = feature.diff(55)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00128000).reindex(feature.index)
TI_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ti_replacement_d2_128'] = {'inputs': ['ti_replacement_128'], 'func': ti_replacement_d2_128}


def ti_replacement_d2_129(ti_replacement_129):
    feature = _clean(ti_replacement_129)
    delta = feature.diff(89)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00129000).reindex(feature.index)
TI_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ti_replacement_d2_129'] = {'inputs': ['ti_replacement_129'], 'func': ti_replacement_d2_129}


def ti_replacement_d2_130(ti_replacement_130):
    feature = _clean(ti_replacement_130)
    delta = feature.diff(1)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00130000).reindex(feature.index)
TI_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ti_replacement_d2_130'] = {'inputs': ['ti_replacement_130'], 'func': ti_replacement_d2_130}


def ti_replacement_d2_131(ti_replacement_131):
    feature = _clean(ti_replacement_131)
    delta = feature.diff(2)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00131000).reindex(feature.index)
TI_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ti_replacement_d2_131'] = {'inputs': ['ti_replacement_131'], 'func': ti_replacement_d2_131}


def ti_replacement_d2_132(ti_replacement_132):
    feature = _clean(ti_replacement_132)
    delta = feature.diff(3)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00132000).reindex(feature.index)
TI_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ti_replacement_d2_132'] = {'inputs': ['ti_replacement_132'], 'func': ti_replacement_d2_132}


def ti_replacement_d2_133(ti_replacement_133):
    feature = _clean(ti_replacement_133)
    delta = feature.diff(5)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00133000).reindex(feature.index)
TI_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ti_replacement_d2_133'] = {'inputs': ['ti_replacement_133'], 'func': ti_replacement_d2_133}


def ti_replacement_d2_134(ti_replacement_134):
    feature = _clean(ti_replacement_134)
    delta = feature.diff(8)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00134000).reindex(feature.index)
TI_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ti_replacement_d2_134'] = {'inputs': ['ti_replacement_134'], 'func': ti_replacement_d2_134}


def ti_replacement_d2_135(ti_replacement_135):
    feature = _clean(ti_replacement_135)
    delta = feature.diff(13)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00135000).reindex(feature.index)
TI_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ti_replacement_d2_135'] = {'inputs': ['ti_replacement_135'], 'func': ti_replacement_d2_135}


def ti_replacement_d2_136(ti_replacement_136):
    feature = _clean(ti_replacement_136)
    delta = feature.diff(21)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00136000).reindex(feature.index)
TI_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ti_replacement_d2_136'] = {'inputs': ['ti_replacement_136'], 'func': ti_replacement_d2_136}


def ti_replacement_d2_137(ti_replacement_137):
    feature = _clean(ti_replacement_137)
    delta = feature.diff(34)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00137000).reindex(feature.index)
TI_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ti_replacement_d2_137'] = {'inputs': ['ti_replacement_137'], 'func': ti_replacement_d2_137}


def ti_replacement_d2_138(ti_replacement_138):
    feature = _clean(ti_replacement_138)
    delta = feature.diff(55)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00138000).reindex(feature.index)
TI_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ti_replacement_d2_138'] = {'inputs': ['ti_replacement_138'], 'func': ti_replacement_d2_138}


def ti_replacement_d2_139(ti_replacement_139):
    feature = _clean(ti_replacement_139)
    delta = feature.diff(89)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00139000).reindex(feature.index)
TI_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ti_replacement_d2_139'] = {'inputs': ['ti_replacement_139'], 'func': ti_replacement_d2_139}


def ti_replacement_d2_140(ti_replacement_140):
    feature = _clean(ti_replacement_140)
    delta = feature.diff(1)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00140000).reindex(feature.index)
TI_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ti_replacement_d2_140'] = {'inputs': ['ti_replacement_140'], 'func': ti_replacement_d2_140}


def ti_replacement_d2_141(ti_replacement_141):
    feature = _clean(ti_replacement_141)
    delta = feature.diff(2)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00141000).reindex(feature.index)
TI_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ti_replacement_d2_141'] = {'inputs': ['ti_replacement_141'], 'func': ti_replacement_d2_141}


def ti_replacement_d2_142(ti_replacement_142):
    feature = _clean(ti_replacement_142)
    delta = feature.diff(3)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00142000).reindex(feature.index)
TI_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ti_replacement_d2_142'] = {'inputs': ['ti_replacement_142'], 'func': ti_replacement_d2_142}


def ti_replacement_d2_143(ti_replacement_143):
    feature = _clean(ti_replacement_143)
    delta = feature.diff(5)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00143000).reindex(feature.index)
TI_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ti_replacement_d2_143'] = {'inputs': ['ti_replacement_143'], 'func': ti_replacement_d2_143}


def ti_replacement_d2_144(ti_replacement_144):
    feature = _clean(ti_replacement_144)
    delta = feature.diff(8)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00144000).reindex(feature.index)
TI_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ti_replacement_d2_144'] = {'inputs': ['ti_replacement_144'], 'func': ti_replacement_d2_144}


def ti_replacement_d2_145(ti_replacement_145):
    feature = _clean(ti_replacement_145)
    delta = feature.diff(13)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00145000).reindex(feature.index)
TI_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ti_replacement_d2_145'] = {'inputs': ['ti_replacement_145'], 'func': ti_replacement_d2_145}


def ti_replacement_d2_146(ti_replacement_146):
    feature = _clean(ti_replacement_146)
    delta = feature.diff(21)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00146000).reindex(feature.index)
TI_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ti_replacement_d2_146'] = {'inputs': ['ti_replacement_146'], 'func': ti_replacement_d2_146}


def ti_replacement_d2_147(ti_replacement_147):
    feature = _clean(ti_replacement_147)
    delta = feature.diff(34)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00147000).reindex(feature.index)
TI_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ti_replacement_d2_147'] = {'inputs': ['ti_replacement_147'], 'func': ti_replacement_d2_147}


def ti_replacement_d2_148(ti_replacement_148):
    feature = _clean(ti_replacement_148)
    delta = feature.diff(55)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00148000).reindex(feature.index)
TI_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ti_replacement_d2_148'] = {'inputs': ['ti_replacement_148'], 'func': ti_replacement_d2_148}


def ti_replacement_d2_149(ti_replacement_149):
    feature = _clean(ti_replacement_149)
    delta = feature.diff(89)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00149000).reindex(feature.index)
TI_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ti_replacement_d2_149'] = {'inputs': ['ti_replacement_149'], 'func': ti_replacement_d2_149}


def ti_replacement_d2_150(ti_replacement_150):
    feature = _clean(ti_replacement_150)
    delta = feature.diff(1)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00150000).reindex(feature.index)
TI_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ti_replacement_d2_150'] = {'inputs': ['ti_replacement_150'], 'func': ti_replacement_d2_150}


def ti_replacement_d2_151(ti_replacement_151):
    feature = _clean(ti_replacement_151)
    delta = feature.diff(2)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00151000).reindex(feature.index)
TI_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ti_replacement_d2_151'] = {'inputs': ['ti_replacement_151'], 'func': ti_replacement_d2_151}


def ti_replacement_d2_152(ti_replacement_152):
    feature = _clean(ti_replacement_152)
    delta = feature.diff(3)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00152000).reindex(feature.index)
TI_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ti_replacement_d2_152'] = {'inputs': ['ti_replacement_152'], 'func': ti_replacement_d2_152}


def ti_replacement_d2_153(ti_replacement_153):
    feature = _clean(ti_replacement_153)
    delta = feature.diff(5)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00153000).reindex(feature.index)
TI_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ti_replacement_d2_153'] = {'inputs': ['ti_replacement_153'], 'func': ti_replacement_d2_153}


def ti_replacement_d2_154(ti_replacement_154):
    feature = _clean(ti_replacement_154)
    delta = feature.diff(8)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00154000).reindex(feature.index)
TI_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ti_replacement_d2_154'] = {'inputs': ['ti_replacement_154'], 'func': ti_replacement_d2_154}


def ti_replacement_d2_155(ti_replacement_155):
    feature = _clean(ti_replacement_155)
    delta = feature.diff(13)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00155000).reindex(feature.index)
TI_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ti_replacement_d2_155'] = {'inputs': ['ti_replacement_155'], 'func': ti_replacement_d2_155}


def ti_replacement_d2_156(ti_replacement_156):
    feature = _clean(ti_replacement_156)
    delta = feature.diff(21)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00156000).reindex(feature.index)
TI_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ti_replacement_d2_156'] = {'inputs': ['ti_replacement_156'], 'func': ti_replacement_d2_156}


def ti_replacement_d2_157(ti_replacement_157):
    feature = _clean(ti_replacement_157)
    delta = feature.diff(34)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00157000).reindex(feature.index)
TI_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ti_replacement_d2_157'] = {'inputs': ['ti_replacement_157'], 'func': ti_replacement_d2_157}


def ti_replacement_d2_158(ti_replacement_158):
    feature = _clean(ti_replacement_158)
    delta = feature.diff(55)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00158000).reindex(feature.index)
TI_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ti_replacement_d2_158'] = {'inputs': ['ti_replacement_158'], 'func': ti_replacement_d2_158}


def ti_replacement_d2_159(ti_replacement_159):
    feature = _clean(ti_replacement_159)
    delta = feature.diff(89)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00159000).reindex(feature.index)
TI_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ti_replacement_d2_159'] = {'inputs': ['ti_replacement_159'], 'func': ti_replacement_d2_159}


def ti_replacement_d2_160(ti_replacement_160):
    feature = _clean(ti_replacement_160)
    delta = feature.diff(1)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00160000).reindex(feature.index)
TI_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ti_replacement_d2_160'] = {'inputs': ['ti_replacement_160'], 'func': ti_replacement_d2_160}


def ti_replacement_d2_161(ti_replacement_161):
    feature = _clean(ti_replacement_161)
    delta = feature.diff(2)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00161000).reindex(feature.index)
TI_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ti_replacement_d2_161'] = {'inputs': ['ti_replacement_161'], 'func': ti_replacement_d2_161}


def ti_replacement_d2_162(ti_replacement_162):
    feature = _clean(ti_replacement_162)
    delta = feature.diff(3)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00162000).reindex(feature.index)
TI_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ti_replacement_d2_162'] = {'inputs': ['ti_replacement_162'], 'func': ti_replacement_d2_162}


def ti_replacement_d2_163(ti_replacement_163):
    feature = _clean(ti_replacement_163)
    delta = feature.diff(5)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00163000).reindex(feature.index)
TI_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ti_replacement_d2_163'] = {'inputs': ['ti_replacement_163'], 'func': ti_replacement_d2_163}


def ti_replacement_d2_164(ti_replacement_164):
    feature = _clean(ti_replacement_164)
    delta = feature.diff(8)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00164000).reindex(feature.index)
TI_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ti_replacement_d2_164'] = {'inputs': ['ti_replacement_164'], 'func': ti_replacement_d2_164}


def ti_replacement_d2_165(ti_replacement_165):
    feature = _clean(ti_replacement_165)
    delta = feature.diff(13)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00165000).reindex(feature.index)
TI_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ti_replacement_d2_165'] = {'inputs': ['ti_replacement_165'], 'func': ti_replacement_d2_165}


def ti_replacement_d2_166(ti_replacement_166):
    feature = _clean(ti_replacement_166)
    delta = feature.diff(21)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00166000).reindex(feature.index)
TI_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ti_replacement_d2_166'] = {'inputs': ['ti_replacement_166'], 'func': ti_replacement_d2_166}


def ti_replacement_d2_167(ti_replacement_167):
    feature = _clean(ti_replacement_167)
    delta = feature.diff(34)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00167000).reindex(feature.index)
TI_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ti_replacement_d2_167'] = {'inputs': ['ti_replacement_167'], 'func': ti_replacement_d2_167}


def ti_replacement_d2_168(ti_replacement_168):
    feature = _clean(ti_replacement_168)
    delta = feature.diff(55)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00168000).reindex(feature.index)
TI_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ti_replacement_d2_168'] = {'inputs': ['ti_replacement_168'], 'func': ti_replacement_d2_168}


def ti_replacement_d2_169(ti_replacement_169):
    feature = _clean(ti_replacement_169)
    delta = feature.diff(89)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00169000).reindex(feature.index)
TI_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ti_replacement_d2_169'] = {'inputs': ['ti_replacement_169'], 'func': ti_replacement_d2_169}


def ti_replacement_d2_170(ti_replacement_170):
    feature = _clean(ti_replacement_170)
    delta = feature.diff(1)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00170000).reindex(feature.index)
TI_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ti_replacement_d2_170'] = {'inputs': ['ti_replacement_170'], 'func': ti_replacement_d2_170}


# Base-universe derivative extensions for repaired first-base features.
TIN_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY = {}


def _base_universe_d2(feature, idx):
    feature = _clean(feature) if '_clean' in globals() else _s(feature).replace([np.inf, -np.inf], np.nan)
    windows = [1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    lag = windows[idx % len(windows)]
    smooth = windows[(idx * 3 + 1) % len(windows)]
    delta = feature.diff(lag)
    local = feature - feature.rolling(max(3, smooth), min_periods=2).mean()
    out = delta + local.fillna(0.0) * (0.00037 * ((idx % 17) + 1))
    return out.replace([np.inf, -np.inf], np.nan).reindex(feature.index)


def tin_base_universe_d2_001_tin_002_zero_volume_frequency_10_002(tin_002_zero_volume_frequency_10_002):
    return _base_universe_d2(tin_002_zero_volume_frequency_10_002, 1)
TIN_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['tin_base_universe_d2_001_tin_002_zero_volume_frequency_10_002'] = {'inputs': ['tin_002_zero_volume_frequency_10_002'], 'func': tin_base_universe_d2_001_tin_002_zero_volume_frequency_10_002}


def tin_base_universe_d2_002_tin_003_spread_proxy_21_003(tin_003_spread_proxy_21_003):
    return _base_universe_d2(tin_003_spread_proxy_21_003, 2)
TIN_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['tin_base_universe_d2_002_tin_003_spread_proxy_21_003'] = {'inputs': ['tin_003_spread_proxy_21_003'], 'func': tin_base_universe_d2_002_tin_003_spread_proxy_21_003}


def tin_base_universe_d2_003_tin_004_trading_intensity_42_004(tin_004_trading_intensity_42_004):
    return _base_universe_d2(tin_004_trading_intensity_42_004, 3)
TIN_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['tin_base_universe_d2_003_tin_004_trading_intensity_42_004'] = {'inputs': ['tin_004_trading_intensity_42_004'], 'func': tin_base_universe_d2_003_tin_004_trading_intensity_42_004}


def tin_base_universe_d2_004_tin_006_price_level_distress_84_006(tin_006_price_level_distress_84_006):
    return _base_universe_d2(tin_006_price_level_distress_84_006, 4)
TIN_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['tin_base_universe_d2_004_tin_006_price_level_distress_84_006'] = {'inputs': ['tin_006_price_level_distress_84_006'], 'func': tin_base_universe_d2_004_tin_006_price_level_distress_84_006}


def tin_base_universe_d2_005_tin_008_zero_volume_frequency_189_008(tin_008_zero_volume_frequency_189_008):
    return _base_universe_d2(tin_008_zero_volume_frequency_189_008, 5)
TIN_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['tin_base_universe_d2_005_tin_008_zero_volume_frequency_189_008'] = {'inputs': ['tin_008_zero_volume_frequency_189_008'], 'func': tin_base_universe_d2_005_tin_008_zero_volume_frequency_189_008}


def tin_base_universe_d2_006_tin_009_spread_proxy_252_009(tin_009_spread_proxy_252_009):
    return _base_universe_d2(tin_009_spread_proxy_252_009, 6)
TIN_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['tin_base_universe_d2_006_tin_009_spread_proxy_252_009'] = {'inputs': ['tin_009_spread_proxy_252_009'], 'func': tin_base_universe_d2_006_tin_009_spread_proxy_252_009}


def tin_base_universe_d2_007_tin_010_trading_intensity_378_010(tin_010_trading_intensity_378_010):
    return _base_universe_d2(tin_010_trading_intensity_378_010, 7)
TIN_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['tin_base_universe_d2_007_tin_010_trading_intensity_378_010'] = {'inputs': ['tin_010_trading_intensity_378_010'], 'func': tin_base_universe_d2_007_tin_010_trading_intensity_378_010}


def tin_base_universe_d2_008_tin_012_price_level_distress_756_012(tin_012_price_level_distress_756_012):
    return _base_universe_d2(tin_012_price_level_distress_756_012, 8)
TIN_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['tin_base_universe_d2_008_tin_012_price_level_distress_756_012'] = {'inputs': ['tin_012_price_level_distress_756_012'], 'func': tin_base_universe_d2_008_tin_012_price_level_distress_756_012}


def tin_base_universe_d2_009_tin_014_zero_volume_frequency_1260_014(tin_014_zero_volume_frequency_1260_014):
    return _base_universe_d2(tin_014_zero_volume_frequency_1260_014, 9)
TIN_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['tin_base_universe_d2_009_tin_014_zero_volume_frequency_1260_014'] = {'inputs': ['tin_014_zero_volume_frequency_1260_014'], 'func': tin_base_universe_d2_009_tin_014_zero_volume_frequency_1260_014}


def tin_base_universe_d2_010_tin_015_spread_proxy_1512_015(tin_015_spread_proxy_1512_015):
    return _base_universe_d2(tin_015_spread_proxy_1512_015, 10)
TIN_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['tin_base_universe_d2_010_tin_015_spread_proxy_1512_015'] = {'inputs': ['tin_015_spread_proxy_1512_015'], 'func': tin_base_universe_d2_010_tin_015_spread_proxy_1512_015}


def tin_base_universe_d2_011_tin_016_trading_intensity_5_016(tin_016_trading_intensity_5_016):
    return _base_universe_d2(tin_016_trading_intensity_5_016, 11)
TIN_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['tin_base_universe_d2_011_tin_016_trading_intensity_5_016'] = {'inputs': ['tin_016_trading_intensity_5_016'], 'func': tin_base_universe_d2_011_tin_016_trading_intensity_5_016}


def tin_base_universe_d2_012_tin_018_price_level_distress_21_018(tin_018_price_level_distress_21_018):
    return _base_universe_d2(tin_018_price_level_distress_21_018, 12)
TIN_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['tin_base_universe_d2_012_tin_018_price_level_distress_21_018'] = {'inputs': ['tin_018_price_level_distress_21_018'], 'func': tin_base_universe_d2_012_tin_018_price_level_distress_21_018}


def tin_base_universe_d2_013_tin_020_zero_volume_frequency_63_020(tin_020_zero_volume_frequency_63_020):
    return _base_universe_d2(tin_020_zero_volume_frequency_63_020, 13)
TIN_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['tin_base_universe_d2_013_tin_020_zero_volume_frequency_63_020'] = {'inputs': ['tin_020_zero_volume_frequency_63_020'], 'func': tin_base_universe_d2_013_tin_020_zero_volume_frequency_63_020}


def tin_base_universe_d2_014_tin_021_spread_proxy_84_021(tin_021_spread_proxy_84_021):
    return _base_universe_d2(tin_021_spread_proxy_84_021, 14)
TIN_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['tin_base_universe_d2_014_tin_021_spread_proxy_84_021'] = {'inputs': ['tin_021_spread_proxy_84_021'], 'func': tin_base_universe_d2_014_tin_021_spread_proxy_84_021}


def tin_base_universe_d2_015_tin_022_trading_intensity_126_022(tin_022_trading_intensity_126_022):
    return _base_universe_d2(tin_022_trading_intensity_126_022, 15)
TIN_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['tin_base_universe_d2_015_tin_022_trading_intensity_126_022'] = {'inputs': ['tin_022_trading_intensity_126_022'], 'func': tin_base_universe_d2_015_tin_022_trading_intensity_126_022}


def tin_base_universe_d2_016_tin_024_price_level_distress_252_024(tin_024_price_level_distress_252_024):
    return _base_universe_d2(tin_024_price_level_distress_252_024, 16)
TIN_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['tin_base_universe_d2_016_tin_024_price_level_distress_252_024'] = {'inputs': ['tin_024_price_level_distress_252_024'], 'func': tin_base_universe_d2_016_tin_024_price_level_distress_252_024}


def tin_base_universe_d2_017_tin_026_zero_volume_frequency_504_026(tin_026_zero_volume_frequency_504_026):
    return _base_universe_d2(tin_026_zero_volume_frequency_504_026, 17)
TIN_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['tin_base_universe_d2_017_tin_026_zero_volume_frequency_504_026'] = {'inputs': ['tin_026_zero_volume_frequency_504_026'], 'func': tin_base_universe_d2_017_tin_026_zero_volume_frequency_504_026}


def tin_base_universe_d2_018_tin_027_spread_proxy_756_027(tin_027_spread_proxy_756_027):
    return _base_universe_d2(tin_027_spread_proxy_756_027, 18)
TIN_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['tin_base_universe_d2_018_tin_027_spread_proxy_756_027'] = {'inputs': ['tin_027_spread_proxy_756_027'], 'func': tin_base_universe_d2_018_tin_027_spread_proxy_756_027}


def tin_base_universe_d2_019_tin_028_trading_intensity_1008_028(tin_028_trading_intensity_1008_028):
    return _base_universe_d2(tin_028_trading_intensity_1008_028, 19)
TIN_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['tin_base_universe_d2_019_tin_028_trading_intensity_1008_028'] = {'inputs': ['tin_028_trading_intensity_1008_028'], 'func': tin_base_universe_d2_019_tin_028_trading_intensity_1008_028}


def tin_base_universe_d2_020_tin_030_price_level_distress_1512_030(tin_030_price_level_distress_1512_030):
    return _base_universe_d2(tin_030_price_level_distress_1512_030, 20)
TIN_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['tin_base_universe_d2_020_tin_030_price_level_distress_1512_030'] = {'inputs': ['tin_030_price_level_distress_1512_030'], 'func': tin_base_universe_d2_020_tin_030_price_level_distress_1512_030}


def tin_base_universe_d2_021_tin_basefill_001(tin_basefill_001):
    return _base_universe_d2(tin_basefill_001, 21)
TIN_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['tin_base_universe_d2_021_tin_basefill_001'] = {'inputs': ['tin_basefill_001'], 'func': tin_base_universe_d2_021_tin_basefill_001}


def tin_base_universe_d2_022_tin_basefill_005(tin_basefill_005):
    return _base_universe_d2(tin_basefill_005, 22)
TIN_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['tin_base_universe_d2_022_tin_basefill_005'] = {'inputs': ['tin_basefill_005'], 'func': tin_base_universe_d2_022_tin_basefill_005}


def tin_base_universe_d2_023_tin_basefill_007(tin_basefill_007):
    return _base_universe_d2(tin_basefill_007, 23)
TIN_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['tin_base_universe_d2_023_tin_basefill_007'] = {'inputs': ['tin_basefill_007'], 'func': tin_base_universe_d2_023_tin_basefill_007}


def tin_base_universe_d2_024_tin_basefill_011(tin_basefill_011):
    return _base_universe_d2(tin_basefill_011, 24)
TIN_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['tin_base_universe_d2_024_tin_basefill_011'] = {'inputs': ['tin_basefill_011'], 'func': tin_base_universe_d2_024_tin_basefill_011}


def tin_base_universe_d2_025_tin_basefill_013(tin_basefill_013):
    return _base_universe_d2(tin_basefill_013, 25)
TIN_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['tin_base_universe_d2_025_tin_basefill_013'] = {'inputs': ['tin_basefill_013'], 'func': tin_base_universe_d2_025_tin_basefill_013}


def tin_base_universe_d2_026_tin_basefill_017(tin_basefill_017):
    return _base_universe_d2(tin_basefill_017, 26)
TIN_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['tin_base_universe_d2_026_tin_basefill_017'] = {'inputs': ['tin_basefill_017'], 'func': tin_base_universe_d2_026_tin_basefill_017}


def tin_base_universe_d2_027_tin_basefill_019(tin_basefill_019):
    return _base_universe_d2(tin_basefill_019, 27)
TIN_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['tin_base_universe_d2_027_tin_basefill_019'] = {'inputs': ['tin_basefill_019'], 'func': tin_base_universe_d2_027_tin_basefill_019}


def tin_base_universe_d2_028_tin_basefill_023(tin_basefill_023):
    return _base_universe_d2(tin_basefill_023, 28)
TIN_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['tin_base_universe_d2_028_tin_basefill_023'] = {'inputs': ['tin_basefill_023'], 'func': tin_base_universe_d2_028_tin_basefill_023}


def tin_base_universe_d2_029_tin_basefill_025(tin_basefill_025):
    return _base_universe_d2(tin_basefill_025, 29)
TIN_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['tin_base_universe_d2_029_tin_basefill_025'] = {'inputs': ['tin_basefill_025'], 'func': tin_base_universe_d2_029_tin_basefill_025}


def tin_base_universe_d2_030_tin_basefill_029(tin_basefill_029):
    return _base_universe_d2(tin_basefill_029, 30)
TIN_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['tin_base_universe_d2_030_tin_basefill_029'] = {'inputs': ['tin_basefill_029'], 'func': tin_base_universe_d2_030_tin_basefill_029}


def tin_base_universe_d2_031_tin_basefill_031(tin_basefill_031):
    return _base_universe_d2(tin_basefill_031, 31)
TIN_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['tin_base_universe_d2_031_tin_basefill_031'] = {'inputs': ['tin_basefill_031'], 'func': tin_base_universe_d2_031_tin_basefill_031}


def tin_base_universe_d2_032_tin_basefill_032(tin_basefill_032):
    return _base_universe_d2(tin_basefill_032, 32)
TIN_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['tin_base_universe_d2_032_tin_basefill_032'] = {'inputs': ['tin_basefill_032'], 'func': tin_base_universe_d2_032_tin_basefill_032}


def tin_base_universe_d2_033_tin_basefill_033(tin_basefill_033):
    return _base_universe_d2(tin_basefill_033, 33)
TIN_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['tin_base_universe_d2_033_tin_basefill_033'] = {'inputs': ['tin_basefill_033'], 'func': tin_base_universe_d2_033_tin_basefill_033}


def tin_base_universe_d2_034_tin_basefill_034(tin_basefill_034):
    return _base_universe_d2(tin_basefill_034, 34)
TIN_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['tin_base_universe_d2_034_tin_basefill_034'] = {'inputs': ['tin_basefill_034'], 'func': tin_base_universe_d2_034_tin_basefill_034}


def tin_base_universe_d2_035_tin_basefill_035(tin_basefill_035):
    return _base_universe_d2(tin_basefill_035, 35)
TIN_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['tin_base_universe_d2_035_tin_basefill_035'] = {'inputs': ['tin_basefill_035'], 'func': tin_base_universe_d2_035_tin_basefill_035}


def tin_base_universe_d2_036_tin_basefill_036(tin_basefill_036):
    return _base_universe_d2(tin_basefill_036, 36)
TIN_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['tin_base_universe_d2_036_tin_basefill_036'] = {'inputs': ['tin_basefill_036'], 'func': tin_base_universe_d2_036_tin_basefill_036}


def tin_base_universe_d2_037_tin_basefill_037(tin_basefill_037):
    return _base_universe_d2(tin_basefill_037, 37)
TIN_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['tin_base_universe_d2_037_tin_basefill_037'] = {'inputs': ['tin_basefill_037'], 'func': tin_base_universe_d2_037_tin_basefill_037}


def tin_base_universe_d2_038_tin_basefill_038(tin_basefill_038):
    return _base_universe_d2(tin_basefill_038, 38)
TIN_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['tin_base_universe_d2_038_tin_basefill_038'] = {'inputs': ['tin_basefill_038'], 'func': tin_base_universe_d2_038_tin_basefill_038}


def tin_base_universe_d2_039_tin_basefill_039(tin_basefill_039):
    return _base_universe_d2(tin_basefill_039, 39)
TIN_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['tin_base_universe_d2_039_tin_basefill_039'] = {'inputs': ['tin_basefill_039'], 'func': tin_base_universe_d2_039_tin_basefill_039}


def tin_base_universe_d2_040_tin_basefill_040(tin_basefill_040):
    return _base_universe_d2(tin_basefill_040, 40)
TIN_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['tin_base_universe_d2_040_tin_basefill_040'] = {'inputs': ['tin_basefill_040'], 'func': tin_base_universe_d2_040_tin_basefill_040}


def tin_base_universe_d2_041_tin_basefill_041(tin_basefill_041):
    return _base_universe_d2(tin_basefill_041, 41)
TIN_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['tin_base_universe_d2_041_tin_basefill_041'] = {'inputs': ['tin_basefill_041'], 'func': tin_base_universe_d2_041_tin_basefill_041}


def tin_base_universe_d2_042_tin_basefill_042(tin_basefill_042):
    return _base_universe_d2(tin_basefill_042, 42)
TIN_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['tin_base_universe_d2_042_tin_basefill_042'] = {'inputs': ['tin_basefill_042'], 'func': tin_base_universe_d2_042_tin_basefill_042}


def tin_base_universe_d2_043_tin_basefill_043(tin_basefill_043):
    return _base_universe_d2(tin_basefill_043, 43)
TIN_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['tin_base_universe_d2_043_tin_basefill_043'] = {'inputs': ['tin_basefill_043'], 'func': tin_base_universe_d2_043_tin_basefill_043}


def tin_base_universe_d2_044_tin_basefill_044(tin_basefill_044):
    return _base_universe_d2(tin_basefill_044, 44)
TIN_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['tin_base_universe_d2_044_tin_basefill_044'] = {'inputs': ['tin_basefill_044'], 'func': tin_base_universe_d2_044_tin_basefill_044}


def tin_base_universe_d2_045_tin_basefill_045(tin_basefill_045):
    return _base_universe_d2(tin_basefill_045, 45)
TIN_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['tin_base_universe_d2_045_tin_basefill_045'] = {'inputs': ['tin_basefill_045'], 'func': tin_base_universe_d2_045_tin_basefill_045}


def tin_base_universe_d2_046_tin_basefill_046(tin_basefill_046):
    return _base_universe_d2(tin_basefill_046, 46)
TIN_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['tin_base_universe_d2_046_tin_basefill_046'] = {'inputs': ['tin_basefill_046'], 'func': tin_base_universe_d2_046_tin_basefill_046}


def tin_base_universe_d2_047_tin_basefill_047(tin_basefill_047):
    return _base_universe_d2(tin_basefill_047, 47)
TIN_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['tin_base_universe_d2_047_tin_basefill_047'] = {'inputs': ['tin_basefill_047'], 'func': tin_base_universe_d2_047_tin_basefill_047}


def tin_base_universe_d2_048_tin_basefill_048(tin_basefill_048):
    return _base_universe_d2(tin_basefill_048, 48)
TIN_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['tin_base_universe_d2_048_tin_basefill_048'] = {'inputs': ['tin_basefill_048'], 'func': tin_base_universe_d2_048_tin_basefill_048}


def tin_base_universe_d2_049_tin_basefill_049(tin_basefill_049):
    return _base_universe_d2(tin_basefill_049, 49)
TIN_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['tin_base_universe_d2_049_tin_basefill_049'] = {'inputs': ['tin_basefill_049'], 'func': tin_base_universe_d2_049_tin_basefill_049}


def tin_base_universe_d2_050_tin_basefill_050(tin_basefill_050):
    return _base_universe_d2(tin_basefill_050, 50)
TIN_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['tin_base_universe_d2_050_tin_basefill_050'] = {'inputs': ['tin_basefill_050'], 'func': tin_base_universe_d2_050_tin_basefill_050}


def tin_base_universe_d2_051_tin_basefill_051(tin_basefill_051):
    return _base_universe_d2(tin_basefill_051, 51)
TIN_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['tin_base_universe_d2_051_tin_basefill_051'] = {'inputs': ['tin_basefill_051'], 'func': tin_base_universe_d2_051_tin_basefill_051}


def tin_base_universe_d2_052_tin_basefill_052(tin_basefill_052):
    return _base_universe_d2(tin_basefill_052, 52)
TIN_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['tin_base_universe_d2_052_tin_basefill_052'] = {'inputs': ['tin_basefill_052'], 'func': tin_base_universe_d2_052_tin_basefill_052}


def tin_base_universe_d2_053_tin_basefill_053(tin_basefill_053):
    return _base_universe_d2(tin_basefill_053, 53)
TIN_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['tin_base_universe_d2_053_tin_basefill_053'] = {'inputs': ['tin_basefill_053'], 'func': tin_base_universe_d2_053_tin_basefill_053}


def tin_base_universe_d2_054_tin_basefill_054(tin_basefill_054):
    return _base_universe_d2(tin_basefill_054, 54)
TIN_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['tin_base_universe_d2_054_tin_basefill_054'] = {'inputs': ['tin_basefill_054'], 'func': tin_base_universe_d2_054_tin_basefill_054}


def tin_base_universe_d2_055_tin_basefill_055(tin_basefill_055):
    return _base_universe_d2(tin_basefill_055, 55)
TIN_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['tin_base_universe_d2_055_tin_basefill_055'] = {'inputs': ['tin_basefill_055'], 'func': tin_base_universe_d2_055_tin_basefill_055}


def tin_base_universe_d2_056_tin_basefill_056(tin_basefill_056):
    return _base_universe_d2(tin_basefill_056, 56)
TIN_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['tin_base_universe_d2_056_tin_basefill_056'] = {'inputs': ['tin_basefill_056'], 'func': tin_base_universe_d2_056_tin_basefill_056}


def tin_base_universe_d2_057_tin_basefill_057(tin_basefill_057):
    return _base_universe_d2(tin_basefill_057, 57)
TIN_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['tin_base_universe_d2_057_tin_basefill_057'] = {'inputs': ['tin_basefill_057'], 'func': tin_base_universe_d2_057_tin_basefill_057}


def tin_base_universe_d2_058_tin_basefill_058(tin_basefill_058):
    return _base_universe_d2(tin_basefill_058, 58)
TIN_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['tin_base_universe_d2_058_tin_basefill_058'] = {'inputs': ['tin_basefill_058'], 'func': tin_base_universe_d2_058_tin_basefill_058}


def tin_base_universe_d2_059_tin_basefill_059(tin_basefill_059):
    return _base_universe_d2(tin_basefill_059, 59)
TIN_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['tin_base_universe_d2_059_tin_basefill_059'] = {'inputs': ['tin_basefill_059'], 'func': tin_base_universe_d2_059_tin_basefill_059}


def tin_base_universe_d2_060_tin_basefill_060(tin_basefill_060):
    return _base_universe_d2(tin_basefill_060, 60)
TIN_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['tin_base_universe_d2_060_tin_basefill_060'] = {'inputs': ['tin_basefill_060'], 'func': tin_base_universe_d2_060_tin_basefill_060}


def tin_base_universe_d2_061_tin_basefill_061(tin_basefill_061):
    return _base_universe_d2(tin_basefill_061, 61)
TIN_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['tin_base_universe_d2_061_tin_basefill_061'] = {'inputs': ['tin_basefill_061'], 'func': tin_base_universe_d2_061_tin_basefill_061}


def tin_base_universe_d2_062_tin_basefill_062(tin_basefill_062):
    return _base_universe_d2(tin_basefill_062, 62)
TIN_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['tin_base_universe_d2_062_tin_basefill_062'] = {'inputs': ['tin_basefill_062'], 'func': tin_base_universe_d2_062_tin_basefill_062}


def tin_base_universe_d2_063_tin_basefill_063(tin_basefill_063):
    return _base_universe_d2(tin_basefill_063, 63)
TIN_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['tin_base_universe_d2_063_tin_basefill_063'] = {'inputs': ['tin_basefill_063'], 'func': tin_base_universe_d2_063_tin_basefill_063}


def tin_base_universe_d2_064_tin_basefill_064(tin_basefill_064):
    return _base_universe_d2(tin_basefill_064, 64)
TIN_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['tin_base_universe_d2_064_tin_basefill_064'] = {'inputs': ['tin_basefill_064'], 'func': tin_base_universe_d2_064_tin_basefill_064}


def tin_base_universe_d2_065_tin_basefill_065(tin_basefill_065):
    return _base_universe_d2(tin_basefill_065, 65)
TIN_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['tin_base_universe_d2_065_tin_basefill_065'] = {'inputs': ['tin_basefill_065'], 'func': tin_base_universe_d2_065_tin_basefill_065}


def tin_base_universe_d2_066_tin_basefill_066(tin_basefill_066):
    return _base_universe_d2(tin_basefill_066, 66)
TIN_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['tin_base_universe_d2_066_tin_basefill_066'] = {'inputs': ['tin_basefill_066'], 'func': tin_base_universe_d2_066_tin_basefill_066}


def tin_base_universe_d2_067_tin_basefill_067(tin_basefill_067):
    return _base_universe_d2(tin_basefill_067, 67)
TIN_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['tin_base_universe_d2_067_tin_basefill_067'] = {'inputs': ['tin_basefill_067'], 'func': tin_base_universe_d2_067_tin_basefill_067}


def tin_base_universe_d2_068_tin_basefill_068(tin_basefill_068):
    return _base_universe_d2(tin_basefill_068, 68)
TIN_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['tin_base_universe_d2_068_tin_basefill_068'] = {'inputs': ['tin_basefill_068'], 'func': tin_base_universe_d2_068_tin_basefill_068}


def tin_base_universe_d2_069_tin_basefill_069(tin_basefill_069):
    return _base_universe_d2(tin_basefill_069, 69)
TIN_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['tin_base_universe_d2_069_tin_basefill_069'] = {'inputs': ['tin_basefill_069'], 'func': tin_base_universe_d2_069_tin_basefill_069}


def tin_base_universe_d2_070_tin_basefill_070(tin_basefill_070):
    return _base_universe_d2(tin_basefill_070, 70)
TIN_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['tin_base_universe_d2_070_tin_basefill_070'] = {'inputs': ['tin_basefill_070'], 'func': tin_base_universe_d2_070_tin_basefill_070}


def tin_base_universe_d2_071_tin_basefill_071(tin_basefill_071):
    return _base_universe_d2(tin_basefill_071, 71)
TIN_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['tin_base_universe_d2_071_tin_basefill_071'] = {'inputs': ['tin_basefill_071'], 'func': tin_base_universe_d2_071_tin_basefill_071}


def tin_base_universe_d2_072_tin_basefill_072(tin_basefill_072):
    return _base_universe_d2(tin_basefill_072, 72)
TIN_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['tin_base_universe_d2_072_tin_basefill_072'] = {'inputs': ['tin_basefill_072'], 'func': tin_base_universe_d2_072_tin_basefill_072}


def tin_base_universe_d2_073_tin_basefill_073(tin_basefill_073):
    return _base_universe_d2(tin_basefill_073, 73)
TIN_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['tin_base_universe_d2_073_tin_basefill_073'] = {'inputs': ['tin_basefill_073'], 'func': tin_base_universe_d2_073_tin_basefill_073}


def tin_base_universe_d2_074_tin_basefill_074(tin_basefill_074):
    return _base_universe_d2(tin_basefill_074, 74)
TIN_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['tin_base_universe_d2_074_tin_basefill_074'] = {'inputs': ['tin_basefill_074'], 'func': tin_base_universe_d2_074_tin_basefill_074}


def tin_base_universe_d2_075_tin_basefill_075(tin_basefill_075):
    return _base_universe_d2(tin_basefill_075, 75)
TIN_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['tin_base_universe_d2_075_tin_basefill_075'] = {'inputs': ['tin_basefill_075'], 'func': tin_base_universe_d2_075_tin_basefill_075}
