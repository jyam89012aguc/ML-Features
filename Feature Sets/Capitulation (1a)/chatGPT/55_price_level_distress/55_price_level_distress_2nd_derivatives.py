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



def pld_001_amihud_illiquidity_roc_1(amihud_illiquidity):
    feature = _s(amihud_illiquidity)
    return (_roc(feature, 1)).reindex(feature.index)

def pld_007_amihud_illiquidity_roc_5(amihud_illiquidity):
    feature = _s(amihud_illiquidity)
    return (_roc(feature, 5)).reindex(feature.index)

def pld_013_amihud_illiquidity_roc_42(amihud_illiquidity):
    feature = _s(amihud_illiquidity)
    return (_roc(feature, 42)).reindex(feature.index)

def pld_154_pld_019_amihud_illiquidity_42_019_roc_126(amihud_illiquidity):
    feature = _s(amihud_illiquidity)
    return (_roc(feature, 126)).reindex(feature.index)

def pld_155_pld_025_amihud_illiquidity_378_025_roc_378(amihud_illiquidity):
    feature = _s(amihud_illiquidity)
    return (_roc(feature, 378)).reindex(feature.index)






















PRICE_LEVEL_DISTRESS_REGISTRY_2ND_DERIVATIVES = {
    'pld_001_amihud_illiquidity_roc_1': {'inputs': ['amihud_illiquidity'], 'func': pld_001_amihud_illiquidity_roc_1},
    'pld_007_amihud_illiquidity_roc_5': {'inputs': ['amihud_illiquidity'], 'func': pld_007_amihud_illiquidity_roc_5},
    'pld_013_amihud_illiquidity_roc_42': {'inputs': ['amihud_illiquidity'], 'func': pld_013_amihud_illiquidity_roc_42},
    'pld_154_pld_019_amihud_illiquidity_42_019_roc_126': {'inputs': ['amihud_illiquidity'], 'func': pld_154_pld_019_amihud_illiquidity_42_019_roc_126},
    'pld_155_pld_025_amihud_illiquidity_378_025_roc_378': {'inputs': ['amihud_illiquidity'], 'func': pld_155_pld_025_amihud_illiquidity_378_025_roc_378},
}


# Replacement 2nd-derivative features restored after redundancy audit.

import numpy as np
import pandas as pd


def _s(x):
    return pd.Series(x).astype(float)


def _clean(x):
    return _s(x).replace([np.inf, -np.inf], np.nan)


PLD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY = {}


def pld_replacement_d2_001(pld_replacement_001):
    feature = _clean(pld_replacement_001)
    delta = feature.diff(2)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00001000).reindex(feature.index)
PLD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['pld_replacement_d2_001'] = {'inputs': ['pld_replacement_001'], 'func': pld_replacement_d2_001}


def pld_replacement_d2_002(pld_replacement_002):
    feature = _clean(pld_replacement_002)
    delta = feature.diff(3)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00002000).reindex(feature.index)
PLD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['pld_replacement_d2_002'] = {'inputs': ['pld_replacement_002'], 'func': pld_replacement_d2_002}


def pld_replacement_d2_003(pld_replacement_003):
    feature = _clean(pld_replacement_003)
    delta = feature.diff(5)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00003000).reindex(feature.index)
PLD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['pld_replacement_d2_003'] = {'inputs': ['pld_replacement_003'], 'func': pld_replacement_d2_003}


def pld_replacement_d2_004(pld_replacement_004):
    feature = _clean(pld_replacement_004)
    delta = feature.diff(8)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00004000).reindex(feature.index)
PLD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['pld_replacement_d2_004'] = {'inputs': ['pld_replacement_004'], 'func': pld_replacement_d2_004}


def pld_replacement_d2_005(pld_replacement_005):
    feature = _clean(pld_replacement_005)
    delta = feature.diff(13)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00005000).reindex(feature.index)
PLD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['pld_replacement_d2_005'] = {'inputs': ['pld_replacement_005'], 'func': pld_replacement_d2_005}


def pld_replacement_d2_006(pld_replacement_006):
    feature = _clean(pld_replacement_006)
    delta = feature.diff(21)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00006000).reindex(feature.index)
PLD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['pld_replacement_d2_006'] = {'inputs': ['pld_replacement_006'], 'func': pld_replacement_d2_006}


def pld_replacement_d2_007(pld_replacement_007):
    feature = _clean(pld_replacement_007)
    delta = feature.diff(34)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00007000).reindex(feature.index)
PLD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['pld_replacement_d2_007'] = {'inputs': ['pld_replacement_007'], 'func': pld_replacement_d2_007}


def pld_replacement_d2_008(pld_replacement_008):
    feature = _clean(pld_replacement_008)
    delta = feature.diff(55)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00008000).reindex(feature.index)
PLD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['pld_replacement_d2_008'] = {'inputs': ['pld_replacement_008'], 'func': pld_replacement_d2_008}


def pld_replacement_d2_009(pld_replacement_009):
    feature = _clean(pld_replacement_009)
    delta = feature.diff(89)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00009000).reindex(feature.index)
PLD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['pld_replacement_d2_009'] = {'inputs': ['pld_replacement_009'], 'func': pld_replacement_d2_009}


def pld_replacement_d2_010(pld_replacement_010):
    feature = _clean(pld_replacement_010)
    delta = feature.diff(1)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00010000).reindex(feature.index)
PLD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['pld_replacement_d2_010'] = {'inputs': ['pld_replacement_010'], 'func': pld_replacement_d2_010}


def pld_replacement_d2_011(pld_replacement_011):
    feature = _clean(pld_replacement_011)
    delta = feature.diff(2)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00011000).reindex(feature.index)
PLD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['pld_replacement_d2_011'] = {'inputs': ['pld_replacement_011'], 'func': pld_replacement_d2_011}


def pld_replacement_d2_012(pld_replacement_012):
    feature = _clean(pld_replacement_012)
    delta = feature.diff(3)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00012000).reindex(feature.index)
PLD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['pld_replacement_d2_012'] = {'inputs': ['pld_replacement_012'], 'func': pld_replacement_d2_012}


def pld_replacement_d2_013(pld_replacement_013):
    feature = _clean(pld_replacement_013)
    delta = feature.diff(5)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00013000).reindex(feature.index)
PLD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['pld_replacement_d2_013'] = {'inputs': ['pld_replacement_013'], 'func': pld_replacement_d2_013}


def pld_replacement_d2_014(pld_replacement_014):
    feature = _clean(pld_replacement_014)
    delta = feature.diff(8)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00014000).reindex(feature.index)
PLD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['pld_replacement_d2_014'] = {'inputs': ['pld_replacement_014'], 'func': pld_replacement_d2_014}


def pld_replacement_d2_015(pld_replacement_015):
    feature = _clean(pld_replacement_015)
    delta = feature.diff(13)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00015000).reindex(feature.index)
PLD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['pld_replacement_d2_015'] = {'inputs': ['pld_replacement_015'], 'func': pld_replacement_d2_015}


def pld_replacement_d2_016(pld_replacement_016):
    feature = _clean(pld_replacement_016)
    delta = feature.diff(21)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00016000).reindex(feature.index)
PLD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['pld_replacement_d2_016'] = {'inputs': ['pld_replacement_016'], 'func': pld_replacement_d2_016}


def pld_replacement_d2_017(pld_replacement_017):
    feature = _clean(pld_replacement_017)
    delta = feature.diff(34)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00017000).reindex(feature.index)
PLD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['pld_replacement_d2_017'] = {'inputs': ['pld_replacement_017'], 'func': pld_replacement_d2_017}


def pld_replacement_d2_018(pld_replacement_018):
    feature = _clean(pld_replacement_018)
    delta = feature.diff(55)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00018000).reindex(feature.index)
PLD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['pld_replacement_d2_018'] = {'inputs': ['pld_replacement_018'], 'func': pld_replacement_d2_018}


def pld_replacement_d2_019(pld_replacement_019):
    feature = _clean(pld_replacement_019)
    delta = feature.diff(89)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00019000).reindex(feature.index)
PLD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['pld_replacement_d2_019'] = {'inputs': ['pld_replacement_019'], 'func': pld_replacement_d2_019}


def pld_replacement_d2_020(pld_replacement_020):
    feature = _clean(pld_replacement_020)
    delta = feature.diff(1)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00020000).reindex(feature.index)
PLD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['pld_replacement_d2_020'] = {'inputs': ['pld_replacement_020'], 'func': pld_replacement_d2_020}


def pld_replacement_d2_021(pld_replacement_021):
    feature = _clean(pld_replacement_021)
    delta = feature.diff(2)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00021000).reindex(feature.index)
PLD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['pld_replacement_d2_021'] = {'inputs': ['pld_replacement_021'], 'func': pld_replacement_d2_021}


def pld_replacement_d2_022(pld_replacement_022):
    feature = _clean(pld_replacement_022)
    delta = feature.diff(3)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00022000).reindex(feature.index)
PLD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['pld_replacement_d2_022'] = {'inputs': ['pld_replacement_022'], 'func': pld_replacement_d2_022}


def pld_replacement_d2_023(pld_replacement_023):
    feature = _clean(pld_replacement_023)
    delta = feature.diff(5)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00023000).reindex(feature.index)
PLD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['pld_replacement_d2_023'] = {'inputs': ['pld_replacement_023'], 'func': pld_replacement_d2_023}


def pld_replacement_d2_024(pld_replacement_024):
    feature = _clean(pld_replacement_024)
    delta = feature.diff(8)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00024000).reindex(feature.index)
PLD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['pld_replacement_d2_024'] = {'inputs': ['pld_replacement_024'], 'func': pld_replacement_d2_024}


def pld_replacement_d2_025(pld_replacement_025):
    feature = _clean(pld_replacement_025)
    delta = feature.diff(13)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00025000).reindex(feature.index)
PLD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['pld_replacement_d2_025'] = {'inputs': ['pld_replacement_025'], 'func': pld_replacement_d2_025}


def pld_replacement_d2_026(pld_replacement_026):
    feature = _clean(pld_replacement_026)
    delta = feature.diff(21)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00026000).reindex(feature.index)
PLD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['pld_replacement_d2_026'] = {'inputs': ['pld_replacement_026'], 'func': pld_replacement_d2_026}


def pld_replacement_d2_027(pld_replacement_027):
    feature = _clean(pld_replacement_027)
    delta = feature.diff(34)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00027000).reindex(feature.index)
PLD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['pld_replacement_d2_027'] = {'inputs': ['pld_replacement_027'], 'func': pld_replacement_d2_027}


def pld_replacement_d2_028(pld_replacement_028):
    feature = _clean(pld_replacement_028)
    delta = feature.diff(55)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00028000).reindex(feature.index)
PLD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['pld_replacement_d2_028'] = {'inputs': ['pld_replacement_028'], 'func': pld_replacement_d2_028}


def pld_replacement_d2_029(pld_replacement_029):
    feature = _clean(pld_replacement_029)
    delta = feature.diff(89)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00029000).reindex(feature.index)
PLD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['pld_replacement_d2_029'] = {'inputs': ['pld_replacement_029'], 'func': pld_replacement_d2_029}


def pld_replacement_d2_030(pld_replacement_030):
    feature = _clean(pld_replacement_030)
    delta = feature.diff(1)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00030000).reindex(feature.index)
PLD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['pld_replacement_d2_030'] = {'inputs': ['pld_replacement_030'], 'func': pld_replacement_d2_030}


def pld_replacement_d2_031(pld_replacement_031):
    feature = _clean(pld_replacement_031)
    delta = feature.diff(2)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00031000).reindex(feature.index)
PLD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['pld_replacement_d2_031'] = {'inputs': ['pld_replacement_031'], 'func': pld_replacement_d2_031}


def pld_replacement_d2_032(pld_replacement_032):
    feature = _clean(pld_replacement_032)
    delta = feature.diff(3)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00032000).reindex(feature.index)
PLD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['pld_replacement_d2_032'] = {'inputs': ['pld_replacement_032'], 'func': pld_replacement_d2_032}


def pld_replacement_d2_033(pld_replacement_033):
    feature = _clean(pld_replacement_033)
    delta = feature.diff(5)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00033000).reindex(feature.index)
PLD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['pld_replacement_d2_033'] = {'inputs': ['pld_replacement_033'], 'func': pld_replacement_d2_033}


def pld_replacement_d2_034(pld_replacement_034):
    feature = _clean(pld_replacement_034)
    delta = feature.diff(8)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00034000).reindex(feature.index)
PLD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['pld_replacement_d2_034'] = {'inputs': ['pld_replacement_034'], 'func': pld_replacement_d2_034}


def pld_replacement_d2_035(pld_replacement_035):
    feature = _clean(pld_replacement_035)
    delta = feature.diff(13)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00035000).reindex(feature.index)
PLD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['pld_replacement_d2_035'] = {'inputs': ['pld_replacement_035'], 'func': pld_replacement_d2_035}


def pld_replacement_d2_036(pld_replacement_036):
    feature = _clean(pld_replacement_036)
    delta = feature.diff(21)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00036000).reindex(feature.index)
PLD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['pld_replacement_d2_036'] = {'inputs': ['pld_replacement_036'], 'func': pld_replacement_d2_036}


def pld_replacement_d2_037(pld_replacement_037):
    feature = _clean(pld_replacement_037)
    delta = feature.diff(34)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00037000).reindex(feature.index)
PLD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['pld_replacement_d2_037'] = {'inputs': ['pld_replacement_037'], 'func': pld_replacement_d2_037}


def pld_replacement_d2_038(pld_replacement_038):
    feature = _clean(pld_replacement_038)
    delta = feature.diff(55)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00038000).reindex(feature.index)
PLD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['pld_replacement_d2_038'] = {'inputs': ['pld_replacement_038'], 'func': pld_replacement_d2_038}


def pld_replacement_d2_039(pld_replacement_039):
    feature = _clean(pld_replacement_039)
    delta = feature.diff(89)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00039000).reindex(feature.index)
PLD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['pld_replacement_d2_039'] = {'inputs': ['pld_replacement_039'], 'func': pld_replacement_d2_039}


def pld_replacement_d2_040(pld_replacement_040):
    feature = _clean(pld_replacement_040)
    delta = feature.diff(1)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00040000).reindex(feature.index)
PLD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['pld_replacement_d2_040'] = {'inputs': ['pld_replacement_040'], 'func': pld_replacement_d2_040}


def pld_replacement_d2_041(pld_replacement_041):
    feature = _clean(pld_replacement_041)
    delta = feature.diff(2)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00041000).reindex(feature.index)
PLD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['pld_replacement_d2_041'] = {'inputs': ['pld_replacement_041'], 'func': pld_replacement_d2_041}


def pld_replacement_d2_042(pld_replacement_042):
    feature = _clean(pld_replacement_042)
    delta = feature.diff(3)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00042000).reindex(feature.index)
PLD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['pld_replacement_d2_042'] = {'inputs': ['pld_replacement_042'], 'func': pld_replacement_d2_042}


def pld_replacement_d2_043(pld_replacement_043):
    feature = _clean(pld_replacement_043)
    delta = feature.diff(5)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00043000).reindex(feature.index)
PLD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['pld_replacement_d2_043'] = {'inputs': ['pld_replacement_043'], 'func': pld_replacement_d2_043}


def pld_replacement_d2_044(pld_replacement_044):
    feature = _clean(pld_replacement_044)
    delta = feature.diff(8)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00044000).reindex(feature.index)
PLD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['pld_replacement_d2_044'] = {'inputs': ['pld_replacement_044'], 'func': pld_replacement_d2_044}


def pld_replacement_d2_045(pld_replacement_045):
    feature = _clean(pld_replacement_045)
    delta = feature.diff(13)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00045000).reindex(feature.index)
PLD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['pld_replacement_d2_045'] = {'inputs': ['pld_replacement_045'], 'func': pld_replacement_d2_045}


def pld_replacement_d2_046(pld_replacement_046):
    feature = _clean(pld_replacement_046)
    delta = feature.diff(21)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00046000).reindex(feature.index)
PLD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['pld_replacement_d2_046'] = {'inputs': ['pld_replacement_046'], 'func': pld_replacement_d2_046}


def pld_replacement_d2_047(pld_replacement_047):
    feature = _clean(pld_replacement_047)
    delta = feature.diff(34)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00047000).reindex(feature.index)
PLD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['pld_replacement_d2_047'] = {'inputs': ['pld_replacement_047'], 'func': pld_replacement_d2_047}


def pld_replacement_d2_048(pld_replacement_048):
    feature = _clean(pld_replacement_048)
    delta = feature.diff(55)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00048000).reindex(feature.index)
PLD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['pld_replacement_d2_048'] = {'inputs': ['pld_replacement_048'], 'func': pld_replacement_d2_048}


def pld_replacement_d2_049(pld_replacement_049):
    feature = _clean(pld_replacement_049)
    delta = feature.diff(89)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00049000).reindex(feature.index)
PLD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['pld_replacement_d2_049'] = {'inputs': ['pld_replacement_049'], 'func': pld_replacement_d2_049}


def pld_replacement_d2_050(pld_replacement_050):
    feature = _clean(pld_replacement_050)
    delta = feature.diff(1)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00050000).reindex(feature.index)
PLD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['pld_replacement_d2_050'] = {'inputs': ['pld_replacement_050'], 'func': pld_replacement_d2_050}


def pld_replacement_d2_051(pld_replacement_051):
    feature = _clean(pld_replacement_051)
    delta = feature.diff(2)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00051000).reindex(feature.index)
PLD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['pld_replacement_d2_051'] = {'inputs': ['pld_replacement_051'], 'func': pld_replacement_d2_051}


def pld_replacement_d2_052(pld_replacement_052):
    feature = _clean(pld_replacement_052)
    delta = feature.diff(3)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00052000).reindex(feature.index)
PLD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['pld_replacement_d2_052'] = {'inputs': ['pld_replacement_052'], 'func': pld_replacement_d2_052}


def pld_replacement_d2_053(pld_replacement_053):
    feature = _clean(pld_replacement_053)
    delta = feature.diff(5)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00053000).reindex(feature.index)
PLD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['pld_replacement_d2_053'] = {'inputs': ['pld_replacement_053'], 'func': pld_replacement_d2_053}


def pld_replacement_d2_054(pld_replacement_054):
    feature = _clean(pld_replacement_054)
    delta = feature.diff(8)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00054000).reindex(feature.index)
PLD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['pld_replacement_d2_054'] = {'inputs': ['pld_replacement_054'], 'func': pld_replacement_d2_054}


def pld_replacement_d2_055(pld_replacement_055):
    feature = _clean(pld_replacement_055)
    delta = feature.diff(13)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00055000).reindex(feature.index)
PLD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['pld_replacement_d2_055'] = {'inputs': ['pld_replacement_055'], 'func': pld_replacement_d2_055}


def pld_replacement_d2_056(pld_replacement_056):
    feature = _clean(pld_replacement_056)
    delta = feature.diff(21)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00056000).reindex(feature.index)
PLD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['pld_replacement_d2_056'] = {'inputs': ['pld_replacement_056'], 'func': pld_replacement_d2_056}


def pld_replacement_d2_057(pld_replacement_057):
    feature = _clean(pld_replacement_057)
    delta = feature.diff(34)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00057000).reindex(feature.index)
PLD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['pld_replacement_d2_057'] = {'inputs': ['pld_replacement_057'], 'func': pld_replacement_d2_057}


def pld_replacement_d2_058(pld_replacement_058):
    feature = _clean(pld_replacement_058)
    delta = feature.diff(55)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00058000).reindex(feature.index)
PLD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['pld_replacement_d2_058'] = {'inputs': ['pld_replacement_058'], 'func': pld_replacement_d2_058}


def pld_replacement_d2_059(pld_replacement_059):
    feature = _clean(pld_replacement_059)
    delta = feature.diff(89)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00059000).reindex(feature.index)
PLD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['pld_replacement_d2_059'] = {'inputs': ['pld_replacement_059'], 'func': pld_replacement_d2_059}


def pld_replacement_d2_060(pld_replacement_060):
    feature = _clean(pld_replacement_060)
    delta = feature.diff(1)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00060000).reindex(feature.index)
PLD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['pld_replacement_d2_060'] = {'inputs': ['pld_replacement_060'], 'func': pld_replacement_d2_060}


def pld_replacement_d2_061(pld_replacement_061):
    feature = _clean(pld_replacement_061)
    delta = feature.diff(2)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00061000).reindex(feature.index)
PLD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['pld_replacement_d2_061'] = {'inputs': ['pld_replacement_061'], 'func': pld_replacement_d2_061}


def pld_replacement_d2_062(pld_replacement_062):
    feature = _clean(pld_replacement_062)
    delta = feature.diff(3)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00062000).reindex(feature.index)
PLD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['pld_replacement_d2_062'] = {'inputs': ['pld_replacement_062'], 'func': pld_replacement_d2_062}


def pld_replacement_d2_063(pld_replacement_063):
    feature = _clean(pld_replacement_063)
    delta = feature.diff(5)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00063000).reindex(feature.index)
PLD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['pld_replacement_d2_063'] = {'inputs': ['pld_replacement_063'], 'func': pld_replacement_d2_063}


def pld_replacement_d2_064(pld_replacement_064):
    feature = _clean(pld_replacement_064)
    delta = feature.diff(8)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00064000).reindex(feature.index)
PLD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['pld_replacement_d2_064'] = {'inputs': ['pld_replacement_064'], 'func': pld_replacement_d2_064}


def pld_replacement_d2_065(pld_replacement_065):
    feature = _clean(pld_replacement_065)
    delta = feature.diff(13)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00065000).reindex(feature.index)
PLD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['pld_replacement_d2_065'] = {'inputs': ['pld_replacement_065'], 'func': pld_replacement_d2_065}


def pld_replacement_d2_066(pld_replacement_066):
    feature = _clean(pld_replacement_066)
    delta = feature.diff(21)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00066000).reindex(feature.index)
PLD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['pld_replacement_d2_066'] = {'inputs': ['pld_replacement_066'], 'func': pld_replacement_d2_066}


def pld_replacement_d2_067(pld_replacement_067):
    feature = _clean(pld_replacement_067)
    delta = feature.diff(34)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00067000).reindex(feature.index)
PLD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['pld_replacement_d2_067'] = {'inputs': ['pld_replacement_067'], 'func': pld_replacement_d2_067}


def pld_replacement_d2_068(pld_replacement_068):
    feature = _clean(pld_replacement_068)
    delta = feature.diff(55)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00068000).reindex(feature.index)
PLD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['pld_replacement_d2_068'] = {'inputs': ['pld_replacement_068'], 'func': pld_replacement_d2_068}


def pld_replacement_d2_069(pld_replacement_069):
    feature = _clean(pld_replacement_069)
    delta = feature.diff(89)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00069000).reindex(feature.index)
PLD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['pld_replacement_d2_069'] = {'inputs': ['pld_replacement_069'], 'func': pld_replacement_d2_069}


def pld_replacement_d2_070(pld_replacement_070):
    feature = _clean(pld_replacement_070)
    delta = feature.diff(1)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00070000).reindex(feature.index)
PLD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['pld_replacement_d2_070'] = {'inputs': ['pld_replacement_070'], 'func': pld_replacement_d2_070}


def pld_replacement_d2_071(pld_replacement_071):
    feature = _clean(pld_replacement_071)
    delta = feature.diff(2)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00071000).reindex(feature.index)
PLD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['pld_replacement_d2_071'] = {'inputs': ['pld_replacement_071'], 'func': pld_replacement_d2_071}


def pld_replacement_d2_072(pld_replacement_072):
    feature = _clean(pld_replacement_072)
    delta = feature.diff(3)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00072000).reindex(feature.index)
PLD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['pld_replacement_d2_072'] = {'inputs': ['pld_replacement_072'], 'func': pld_replacement_d2_072}


def pld_replacement_d2_073(pld_replacement_073):
    feature = _clean(pld_replacement_073)
    delta = feature.diff(5)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00073000).reindex(feature.index)
PLD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['pld_replacement_d2_073'] = {'inputs': ['pld_replacement_073'], 'func': pld_replacement_d2_073}


def pld_replacement_d2_074(pld_replacement_074):
    feature = _clean(pld_replacement_074)
    delta = feature.diff(8)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00074000).reindex(feature.index)
PLD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['pld_replacement_d2_074'] = {'inputs': ['pld_replacement_074'], 'func': pld_replacement_d2_074}


def pld_replacement_d2_075(pld_replacement_075):
    feature = _clean(pld_replacement_075)
    delta = feature.diff(13)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00075000).reindex(feature.index)
PLD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['pld_replacement_d2_075'] = {'inputs': ['pld_replacement_075'], 'func': pld_replacement_d2_075}


def pld_replacement_d2_076(pld_replacement_076):
    feature = _clean(pld_replacement_076)
    delta = feature.diff(21)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00076000).reindex(feature.index)
PLD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['pld_replacement_d2_076'] = {'inputs': ['pld_replacement_076'], 'func': pld_replacement_d2_076}


def pld_replacement_d2_077(pld_replacement_077):
    feature = _clean(pld_replacement_077)
    delta = feature.diff(34)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00077000).reindex(feature.index)
PLD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['pld_replacement_d2_077'] = {'inputs': ['pld_replacement_077'], 'func': pld_replacement_d2_077}


def pld_replacement_d2_078(pld_replacement_078):
    feature = _clean(pld_replacement_078)
    delta = feature.diff(55)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00078000).reindex(feature.index)
PLD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['pld_replacement_d2_078'] = {'inputs': ['pld_replacement_078'], 'func': pld_replacement_d2_078}


def pld_replacement_d2_079(pld_replacement_079):
    feature = _clean(pld_replacement_079)
    delta = feature.diff(89)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00079000).reindex(feature.index)
PLD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['pld_replacement_d2_079'] = {'inputs': ['pld_replacement_079'], 'func': pld_replacement_d2_079}


def pld_replacement_d2_080(pld_replacement_080):
    feature = _clean(pld_replacement_080)
    delta = feature.diff(1)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00080000).reindex(feature.index)
PLD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['pld_replacement_d2_080'] = {'inputs': ['pld_replacement_080'], 'func': pld_replacement_d2_080}


def pld_replacement_d2_081(pld_replacement_081):
    feature = _clean(pld_replacement_081)
    delta = feature.diff(2)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00081000).reindex(feature.index)
PLD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['pld_replacement_d2_081'] = {'inputs': ['pld_replacement_081'], 'func': pld_replacement_d2_081}


def pld_replacement_d2_082(pld_replacement_082):
    feature = _clean(pld_replacement_082)
    delta = feature.diff(3)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00082000).reindex(feature.index)
PLD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['pld_replacement_d2_082'] = {'inputs': ['pld_replacement_082'], 'func': pld_replacement_d2_082}


def pld_replacement_d2_083(pld_replacement_083):
    feature = _clean(pld_replacement_083)
    delta = feature.diff(5)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00083000).reindex(feature.index)
PLD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['pld_replacement_d2_083'] = {'inputs': ['pld_replacement_083'], 'func': pld_replacement_d2_083}


def pld_replacement_d2_084(pld_replacement_084):
    feature = _clean(pld_replacement_084)
    delta = feature.diff(8)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00084000).reindex(feature.index)
PLD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['pld_replacement_d2_084'] = {'inputs': ['pld_replacement_084'], 'func': pld_replacement_d2_084}


def pld_replacement_d2_085(pld_replacement_085):
    feature = _clean(pld_replacement_085)
    delta = feature.diff(13)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00085000).reindex(feature.index)
PLD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['pld_replacement_d2_085'] = {'inputs': ['pld_replacement_085'], 'func': pld_replacement_d2_085}


def pld_replacement_d2_086(pld_replacement_086):
    feature = _clean(pld_replacement_086)
    delta = feature.diff(21)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00086000).reindex(feature.index)
PLD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['pld_replacement_d2_086'] = {'inputs': ['pld_replacement_086'], 'func': pld_replacement_d2_086}


def pld_replacement_d2_087(pld_replacement_087):
    feature = _clean(pld_replacement_087)
    delta = feature.diff(34)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00087000).reindex(feature.index)
PLD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['pld_replacement_d2_087'] = {'inputs': ['pld_replacement_087'], 'func': pld_replacement_d2_087}


def pld_replacement_d2_088(pld_replacement_088):
    feature = _clean(pld_replacement_088)
    delta = feature.diff(55)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00088000).reindex(feature.index)
PLD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['pld_replacement_d2_088'] = {'inputs': ['pld_replacement_088'], 'func': pld_replacement_d2_088}


def pld_replacement_d2_089(pld_replacement_089):
    feature = _clean(pld_replacement_089)
    delta = feature.diff(89)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00089000).reindex(feature.index)
PLD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['pld_replacement_d2_089'] = {'inputs': ['pld_replacement_089'], 'func': pld_replacement_d2_089}


def pld_replacement_d2_090(pld_replacement_090):
    feature = _clean(pld_replacement_090)
    delta = feature.diff(1)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00090000).reindex(feature.index)
PLD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['pld_replacement_d2_090'] = {'inputs': ['pld_replacement_090'], 'func': pld_replacement_d2_090}


def pld_replacement_d2_091(pld_replacement_091):
    feature = _clean(pld_replacement_091)
    delta = feature.diff(2)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00091000).reindex(feature.index)
PLD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['pld_replacement_d2_091'] = {'inputs': ['pld_replacement_091'], 'func': pld_replacement_d2_091}


def pld_replacement_d2_092(pld_replacement_092):
    feature = _clean(pld_replacement_092)
    delta = feature.diff(3)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00092000).reindex(feature.index)
PLD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['pld_replacement_d2_092'] = {'inputs': ['pld_replacement_092'], 'func': pld_replacement_d2_092}


def pld_replacement_d2_093(pld_replacement_093):
    feature = _clean(pld_replacement_093)
    delta = feature.diff(5)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00093000).reindex(feature.index)
PLD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['pld_replacement_d2_093'] = {'inputs': ['pld_replacement_093'], 'func': pld_replacement_d2_093}


def pld_replacement_d2_094(pld_replacement_094):
    feature = _clean(pld_replacement_094)
    delta = feature.diff(8)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00094000).reindex(feature.index)
PLD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['pld_replacement_d2_094'] = {'inputs': ['pld_replacement_094'], 'func': pld_replacement_d2_094}


def pld_replacement_d2_095(pld_replacement_095):
    feature = _clean(pld_replacement_095)
    delta = feature.diff(13)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00095000).reindex(feature.index)
PLD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['pld_replacement_d2_095'] = {'inputs': ['pld_replacement_095'], 'func': pld_replacement_d2_095}


def pld_replacement_d2_096(pld_replacement_096):
    feature = _clean(pld_replacement_096)
    delta = feature.diff(21)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00096000).reindex(feature.index)
PLD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['pld_replacement_d2_096'] = {'inputs': ['pld_replacement_096'], 'func': pld_replacement_d2_096}


def pld_replacement_d2_097(pld_replacement_097):
    feature = _clean(pld_replacement_097)
    delta = feature.diff(34)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00097000).reindex(feature.index)
PLD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['pld_replacement_d2_097'] = {'inputs': ['pld_replacement_097'], 'func': pld_replacement_d2_097}


def pld_replacement_d2_098(pld_replacement_098):
    feature = _clean(pld_replacement_098)
    delta = feature.diff(55)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00098000).reindex(feature.index)
PLD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['pld_replacement_d2_098'] = {'inputs': ['pld_replacement_098'], 'func': pld_replacement_d2_098}


def pld_replacement_d2_099(pld_replacement_099):
    feature = _clean(pld_replacement_099)
    delta = feature.diff(89)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00099000).reindex(feature.index)
PLD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['pld_replacement_d2_099'] = {'inputs': ['pld_replacement_099'], 'func': pld_replacement_d2_099}


def pld_replacement_d2_100(pld_replacement_100):
    feature = _clean(pld_replacement_100)
    delta = feature.diff(1)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00100000).reindex(feature.index)
PLD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['pld_replacement_d2_100'] = {'inputs': ['pld_replacement_100'], 'func': pld_replacement_d2_100}


def pld_replacement_d2_101(pld_replacement_101):
    feature = _clean(pld_replacement_101)
    delta = feature.diff(2)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00101000).reindex(feature.index)
PLD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['pld_replacement_d2_101'] = {'inputs': ['pld_replacement_101'], 'func': pld_replacement_d2_101}


def pld_replacement_d2_102(pld_replacement_102):
    feature = _clean(pld_replacement_102)
    delta = feature.diff(3)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00102000).reindex(feature.index)
PLD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['pld_replacement_d2_102'] = {'inputs': ['pld_replacement_102'], 'func': pld_replacement_d2_102}


def pld_replacement_d2_103(pld_replacement_103):
    feature = _clean(pld_replacement_103)
    delta = feature.diff(5)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00103000).reindex(feature.index)
PLD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['pld_replacement_d2_103'] = {'inputs': ['pld_replacement_103'], 'func': pld_replacement_d2_103}


def pld_replacement_d2_104(pld_replacement_104):
    feature = _clean(pld_replacement_104)
    delta = feature.diff(8)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00104000).reindex(feature.index)
PLD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['pld_replacement_d2_104'] = {'inputs': ['pld_replacement_104'], 'func': pld_replacement_d2_104}


def pld_replacement_d2_105(pld_replacement_105):
    feature = _clean(pld_replacement_105)
    delta = feature.diff(13)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00105000).reindex(feature.index)
PLD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['pld_replacement_d2_105'] = {'inputs': ['pld_replacement_105'], 'func': pld_replacement_d2_105}


def pld_replacement_d2_106(pld_replacement_106):
    feature = _clean(pld_replacement_106)
    delta = feature.diff(21)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00106000).reindex(feature.index)
PLD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['pld_replacement_d2_106'] = {'inputs': ['pld_replacement_106'], 'func': pld_replacement_d2_106}


def pld_replacement_d2_107(pld_replacement_107):
    feature = _clean(pld_replacement_107)
    delta = feature.diff(34)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00107000).reindex(feature.index)
PLD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['pld_replacement_d2_107'] = {'inputs': ['pld_replacement_107'], 'func': pld_replacement_d2_107}


def pld_replacement_d2_108(pld_replacement_108):
    feature = _clean(pld_replacement_108)
    delta = feature.diff(55)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00108000).reindex(feature.index)
PLD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['pld_replacement_d2_108'] = {'inputs': ['pld_replacement_108'], 'func': pld_replacement_d2_108}


def pld_replacement_d2_109(pld_replacement_109):
    feature = _clean(pld_replacement_109)
    delta = feature.diff(89)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00109000).reindex(feature.index)
PLD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['pld_replacement_d2_109'] = {'inputs': ['pld_replacement_109'], 'func': pld_replacement_d2_109}


def pld_replacement_d2_110(pld_replacement_110):
    feature = _clean(pld_replacement_110)
    delta = feature.diff(1)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00110000).reindex(feature.index)
PLD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['pld_replacement_d2_110'] = {'inputs': ['pld_replacement_110'], 'func': pld_replacement_d2_110}


def pld_replacement_d2_111(pld_replacement_111):
    feature = _clean(pld_replacement_111)
    delta = feature.diff(2)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00111000).reindex(feature.index)
PLD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['pld_replacement_d2_111'] = {'inputs': ['pld_replacement_111'], 'func': pld_replacement_d2_111}


def pld_replacement_d2_112(pld_replacement_112):
    feature = _clean(pld_replacement_112)
    delta = feature.diff(3)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00112000).reindex(feature.index)
PLD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['pld_replacement_d2_112'] = {'inputs': ['pld_replacement_112'], 'func': pld_replacement_d2_112}


def pld_replacement_d2_113(pld_replacement_113):
    feature = _clean(pld_replacement_113)
    delta = feature.diff(5)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00113000).reindex(feature.index)
PLD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['pld_replacement_d2_113'] = {'inputs': ['pld_replacement_113'], 'func': pld_replacement_d2_113}


def pld_replacement_d2_114(pld_replacement_114):
    feature = _clean(pld_replacement_114)
    delta = feature.diff(8)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00114000).reindex(feature.index)
PLD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['pld_replacement_d2_114'] = {'inputs': ['pld_replacement_114'], 'func': pld_replacement_d2_114}


def pld_replacement_d2_115(pld_replacement_115):
    feature = _clean(pld_replacement_115)
    delta = feature.diff(13)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00115000).reindex(feature.index)
PLD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['pld_replacement_d2_115'] = {'inputs': ['pld_replacement_115'], 'func': pld_replacement_d2_115}


def pld_replacement_d2_116(pld_replacement_116):
    feature = _clean(pld_replacement_116)
    delta = feature.diff(21)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00116000).reindex(feature.index)
PLD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['pld_replacement_d2_116'] = {'inputs': ['pld_replacement_116'], 'func': pld_replacement_d2_116}


def pld_replacement_d2_117(pld_replacement_117):
    feature = _clean(pld_replacement_117)
    delta = feature.diff(34)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00117000).reindex(feature.index)
PLD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['pld_replacement_d2_117'] = {'inputs': ['pld_replacement_117'], 'func': pld_replacement_d2_117}


def pld_replacement_d2_118(pld_replacement_118):
    feature = _clean(pld_replacement_118)
    delta = feature.diff(55)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00118000).reindex(feature.index)
PLD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['pld_replacement_d2_118'] = {'inputs': ['pld_replacement_118'], 'func': pld_replacement_d2_118}


def pld_replacement_d2_119(pld_replacement_119):
    feature = _clean(pld_replacement_119)
    delta = feature.diff(89)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00119000).reindex(feature.index)
PLD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['pld_replacement_d2_119'] = {'inputs': ['pld_replacement_119'], 'func': pld_replacement_d2_119}


def pld_replacement_d2_120(pld_replacement_120):
    feature = _clean(pld_replacement_120)
    delta = feature.diff(1)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00120000).reindex(feature.index)
PLD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['pld_replacement_d2_120'] = {'inputs': ['pld_replacement_120'], 'func': pld_replacement_d2_120}


def pld_replacement_d2_121(pld_replacement_121):
    feature = _clean(pld_replacement_121)
    delta = feature.diff(2)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00121000).reindex(feature.index)
PLD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['pld_replacement_d2_121'] = {'inputs': ['pld_replacement_121'], 'func': pld_replacement_d2_121}


def pld_replacement_d2_122(pld_replacement_122):
    feature = _clean(pld_replacement_122)
    delta = feature.diff(3)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00122000).reindex(feature.index)
PLD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['pld_replacement_d2_122'] = {'inputs': ['pld_replacement_122'], 'func': pld_replacement_d2_122}


def pld_replacement_d2_123(pld_replacement_123):
    feature = _clean(pld_replacement_123)
    delta = feature.diff(5)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00123000).reindex(feature.index)
PLD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['pld_replacement_d2_123'] = {'inputs': ['pld_replacement_123'], 'func': pld_replacement_d2_123}


def pld_replacement_d2_124(pld_replacement_124):
    feature = _clean(pld_replacement_124)
    delta = feature.diff(8)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00124000).reindex(feature.index)
PLD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['pld_replacement_d2_124'] = {'inputs': ['pld_replacement_124'], 'func': pld_replacement_d2_124}


def pld_replacement_d2_125(pld_replacement_125):
    feature = _clean(pld_replacement_125)
    delta = feature.diff(13)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00125000).reindex(feature.index)
PLD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['pld_replacement_d2_125'] = {'inputs': ['pld_replacement_125'], 'func': pld_replacement_d2_125}


def pld_replacement_d2_126(pld_replacement_126):
    feature = _clean(pld_replacement_126)
    delta = feature.diff(21)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00126000).reindex(feature.index)
PLD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['pld_replacement_d2_126'] = {'inputs': ['pld_replacement_126'], 'func': pld_replacement_d2_126}


def pld_replacement_d2_127(pld_replacement_127):
    feature = _clean(pld_replacement_127)
    delta = feature.diff(34)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00127000).reindex(feature.index)
PLD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['pld_replacement_d2_127'] = {'inputs': ['pld_replacement_127'], 'func': pld_replacement_d2_127}


def pld_replacement_d2_128(pld_replacement_128):
    feature = _clean(pld_replacement_128)
    delta = feature.diff(55)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00128000).reindex(feature.index)
PLD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['pld_replacement_d2_128'] = {'inputs': ['pld_replacement_128'], 'func': pld_replacement_d2_128}


def pld_replacement_d2_129(pld_replacement_129):
    feature = _clean(pld_replacement_129)
    delta = feature.diff(89)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00129000).reindex(feature.index)
PLD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['pld_replacement_d2_129'] = {'inputs': ['pld_replacement_129'], 'func': pld_replacement_d2_129}


def pld_replacement_d2_130(pld_replacement_130):
    feature = _clean(pld_replacement_130)
    delta = feature.diff(1)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00130000).reindex(feature.index)
PLD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['pld_replacement_d2_130'] = {'inputs': ['pld_replacement_130'], 'func': pld_replacement_d2_130}


def pld_replacement_d2_131(pld_replacement_131):
    feature = _clean(pld_replacement_131)
    delta = feature.diff(2)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00131000).reindex(feature.index)
PLD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['pld_replacement_d2_131'] = {'inputs': ['pld_replacement_131'], 'func': pld_replacement_d2_131}


def pld_replacement_d2_132(pld_replacement_132):
    feature = _clean(pld_replacement_132)
    delta = feature.diff(3)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00132000).reindex(feature.index)
PLD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['pld_replacement_d2_132'] = {'inputs': ['pld_replacement_132'], 'func': pld_replacement_d2_132}


def pld_replacement_d2_133(pld_replacement_133):
    feature = _clean(pld_replacement_133)
    delta = feature.diff(5)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00133000).reindex(feature.index)
PLD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['pld_replacement_d2_133'] = {'inputs': ['pld_replacement_133'], 'func': pld_replacement_d2_133}


def pld_replacement_d2_134(pld_replacement_134):
    feature = _clean(pld_replacement_134)
    delta = feature.diff(8)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00134000).reindex(feature.index)
PLD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['pld_replacement_d2_134'] = {'inputs': ['pld_replacement_134'], 'func': pld_replacement_d2_134}


def pld_replacement_d2_135(pld_replacement_135):
    feature = _clean(pld_replacement_135)
    delta = feature.diff(13)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00135000).reindex(feature.index)
PLD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['pld_replacement_d2_135'] = {'inputs': ['pld_replacement_135'], 'func': pld_replacement_d2_135}


def pld_replacement_d2_136(pld_replacement_136):
    feature = _clean(pld_replacement_136)
    delta = feature.diff(21)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00136000).reindex(feature.index)
PLD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['pld_replacement_d2_136'] = {'inputs': ['pld_replacement_136'], 'func': pld_replacement_d2_136}


def pld_replacement_d2_137(pld_replacement_137):
    feature = _clean(pld_replacement_137)
    delta = feature.diff(34)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00137000).reindex(feature.index)
PLD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['pld_replacement_d2_137'] = {'inputs': ['pld_replacement_137'], 'func': pld_replacement_d2_137}


def pld_replacement_d2_138(pld_replacement_138):
    feature = _clean(pld_replacement_138)
    delta = feature.diff(55)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00138000).reindex(feature.index)
PLD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['pld_replacement_d2_138'] = {'inputs': ['pld_replacement_138'], 'func': pld_replacement_d2_138}


def pld_replacement_d2_139(pld_replacement_139):
    feature = _clean(pld_replacement_139)
    delta = feature.diff(89)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00139000).reindex(feature.index)
PLD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['pld_replacement_d2_139'] = {'inputs': ['pld_replacement_139'], 'func': pld_replacement_d2_139}


def pld_replacement_d2_140(pld_replacement_140):
    feature = _clean(pld_replacement_140)
    delta = feature.diff(1)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00140000).reindex(feature.index)
PLD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['pld_replacement_d2_140'] = {'inputs': ['pld_replacement_140'], 'func': pld_replacement_d2_140}


def pld_replacement_d2_141(pld_replacement_141):
    feature = _clean(pld_replacement_141)
    delta = feature.diff(2)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00141000).reindex(feature.index)
PLD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['pld_replacement_d2_141'] = {'inputs': ['pld_replacement_141'], 'func': pld_replacement_d2_141}


def pld_replacement_d2_142(pld_replacement_142):
    feature = _clean(pld_replacement_142)
    delta = feature.diff(3)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00142000).reindex(feature.index)
PLD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['pld_replacement_d2_142'] = {'inputs': ['pld_replacement_142'], 'func': pld_replacement_d2_142}


def pld_replacement_d2_143(pld_replacement_143):
    feature = _clean(pld_replacement_143)
    delta = feature.diff(5)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00143000).reindex(feature.index)
PLD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['pld_replacement_d2_143'] = {'inputs': ['pld_replacement_143'], 'func': pld_replacement_d2_143}


def pld_replacement_d2_144(pld_replacement_144):
    feature = _clean(pld_replacement_144)
    delta = feature.diff(8)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00144000).reindex(feature.index)
PLD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['pld_replacement_d2_144'] = {'inputs': ['pld_replacement_144'], 'func': pld_replacement_d2_144}


def pld_replacement_d2_145(pld_replacement_145):
    feature = _clean(pld_replacement_145)
    delta = feature.diff(13)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00145000).reindex(feature.index)
PLD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['pld_replacement_d2_145'] = {'inputs': ['pld_replacement_145'], 'func': pld_replacement_d2_145}


def pld_replacement_d2_146(pld_replacement_146):
    feature = _clean(pld_replacement_146)
    delta = feature.diff(21)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00146000).reindex(feature.index)
PLD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['pld_replacement_d2_146'] = {'inputs': ['pld_replacement_146'], 'func': pld_replacement_d2_146}


def pld_replacement_d2_147(pld_replacement_147):
    feature = _clean(pld_replacement_147)
    delta = feature.diff(34)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00147000).reindex(feature.index)
PLD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['pld_replacement_d2_147'] = {'inputs': ['pld_replacement_147'], 'func': pld_replacement_d2_147}


def pld_replacement_d2_148(pld_replacement_148):
    feature = _clean(pld_replacement_148)
    delta = feature.diff(55)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00148000).reindex(feature.index)
PLD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['pld_replacement_d2_148'] = {'inputs': ['pld_replacement_148'], 'func': pld_replacement_d2_148}


def pld_replacement_d2_149(pld_replacement_149):
    feature = _clean(pld_replacement_149)
    delta = feature.diff(89)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00149000).reindex(feature.index)
PLD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['pld_replacement_d2_149'] = {'inputs': ['pld_replacement_149'], 'func': pld_replacement_d2_149}


def pld_replacement_d2_150(pld_replacement_150):
    feature = _clean(pld_replacement_150)
    delta = feature.diff(1)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00150000).reindex(feature.index)
PLD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['pld_replacement_d2_150'] = {'inputs': ['pld_replacement_150'], 'func': pld_replacement_d2_150}


def pld_replacement_d2_151(pld_replacement_151):
    feature = _clean(pld_replacement_151)
    delta = feature.diff(2)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00151000).reindex(feature.index)
PLD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['pld_replacement_d2_151'] = {'inputs': ['pld_replacement_151'], 'func': pld_replacement_d2_151}


def pld_replacement_d2_152(pld_replacement_152):
    feature = _clean(pld_replacement_152)
    delta = feature.diff(3)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00152000).reindex(feature.index)
PLD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['pld_replacement_d2_152'] = {'inputs': ['pld_replacement_152'], 'func': pld_replacement_d2_152}


def pld_replacement_d2_153(pld_replacement_153):
    feature = _clean(pld_replacement_153)
    delta = feature.diff(5)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00153000).reindex(feature.index)
PLD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['pld_replacement_d2_153'] = {'inputs': ['pld_replacement_153'], 'func': pld_replacement_d2_153}


def pld_replacement_d2_154(pld_replacement_154):
    feature = _clean(pld_replacement_154)
    delta = feature.diff(8)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00154000).reindex(feature.index)
PLD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['pld_replacement_d2_154'] = {'inputs': ['pld_replacement_154'], 'func': pld_replacement_d2_154}


def pld_replacement_d2_155(pld_replacement_155):
    feature = _clean(pld_replacement_155)
    delta = feature.diff(13)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00155000).reindex(feature.index)
PLD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['pld_replacement_d2_155'] = {'inputs': ['pld_replacement_155'], 'func': pld_replacement_d2_155}


def pld_replacement_d2_156(pld_replacement_156):
    feature = _clean(pld_replacement_156)
    delta = feature.diff(21)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00156000).reindex(feature.index)
PLD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['pld_replacement_d2_156'] = {'inputs': ['pld_replacement_156'], 'func': pld_replacement_d2_156}


def pld_replacement_d2_157(pld_replacement_157):
    feature = _clean(pld_replacement_157)
    delta = feature.diff(34)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00157000).reindex(feature.index)
PLD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['pld_replacement_d2_157'] = {'inputs': ['pld_replacement_157'], 'func': pld_replacement_d2_157}


def pld_replacement_d2_158(pld_replacement_158):
    feature = _clean(pld_replacement_158)
    delta = feature.diff(55)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00158000).reindex(feature.index)
PLD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['pld_replacement_d2_158'] = {'inputs': ['pld_replacement_158'], 'func': pld_replacement_d2_158}


def pld_replacement_d2_159(pld_replacement_159):
    feature = _clean(pld_replacement_159)
    delta = feature.diff(89)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00159000).reindex(feature.index)
PLD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['pld_replacement_d2_159'] = {'inputs': ['pld_replacement_159'], 'func': pld_replacement_d2_159}


def pld_replacement_d2_160(pld_replacement_160):
    feature = _clean(pld_replacement_160)
    delta = feature.diff(1)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00160000).reindex(feature.index)
PLD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['pld_replacement_d2_160'] = {'inputs': ['pld_replacement_160'], 'func': pld_replacement_d2_160}


def pld_replacement_d2_161(pld_replacement_161):
    feature = _clean(pld_replacement_161)
    delta = feature.diff(2)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00161000).reindex(feature.index)
PLD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['pld_replacement_d2_161'] = {'inputs': ['pld_replacement_161'], 'func': pld_replacement_d2_161}


def pld_replacement_d2_162(pld_replacement_162):
    feature = _clean(pld_replacement_162)
    delta = feature.diff(3)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00162000).reindex(feature.index)
PLD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['pld_replacement_d2_162'] = {'inputs': ['pld_replacement_162'], 'func': pld_replacement_d2_162}


def pld_replacement_d2_163(pld_replacement_163):
    feature = _clean(pld_replacement_163)
    delta = feature.diff(5)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00163000).reindex(feature.index)
PLD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['pld_replacement_d2_163'] = {'inputs': ['pld_replacement_163'], 'func': pld_replacement_d2_163}


def pld_replacement_d2_164(pld_replacement_164):
    feature = _clean(pld_replacement_164)
    delta = feature.diff(8)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00164000).reindex(feature.index)
PLD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['pld_replacement_d2_164'] = {'inputs': ['pld_replacement_164'], 'func': pld_replacement_d2_164}


def pld_replacement_d2_165(pld_replacement_165):
    feature = _clean(pld_replacement_165)
    delta = feature.diff(13)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00165000).reindex(feature.index)
PLD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['pld_replacement_d2_165'] = {'inputs': ['pld_replacement_165'], 'func': pld_replacement_d2_165}


def pld_replacement_d2_166(pld_replacement_166):
    feature = _clean(pld_replacement_166)
    delta = feature.diff(21)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00166000).reindex(feature.index)
PLD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['pld_replacement_d2_166'] = {'inputs': ['pld_replacement_166'], 'func': pld_replacement_d2_166}


def pld_replacement_d2_167(pld_replacement_167):
    feature = _clean(pld_replacement_167)
    delta = feature.diff(34)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00167000).reindex(feature.index)
PLD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['pld_replacement_d2_167'] = {'inputs': ['pld_replacement_167'], 'func': pld_replacement_d2_167}


def pld_replacement_d2_168(pld_replacement_168):
    feature = _clean(pld_replacement_168)
    delta = feature.diff(55)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00168000).reindex(feature.index)
PLD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['pld_replacement_d2_168'] = {'inputs': ['pld_replacement_168'], 'func': pld_replacement_d2_168}


def pld_replacement_d2_169(pld_replacement_169):
    feature = _clean(pld_replacement_169)
    delta = feature.diff(89)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00169000).reindex(feature.index)
PLD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['pld_replacement_d2_169'] = {'inputs': ['pld_replacement_169'], 'func': pld_replacement_d2_169}


def pld_replacement_d2_170(pld_replacement_170):
    feature = _clean(pld_replacement_170)
    delta = feature.diff(1)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00170000).reindex(feature.index)
PLD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['pld_replacement_d2_170'] = {'inputs': ['pld_replacement_170'], 'func': pld_replacement_d2_170}


# Base-universe derivative extensions for repaired first-base features.
PLD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY = {}


def _base_universe_d2(feature, idx):
    feature = _clean(feature) if '_clean' in globals() else _s(feature).replace([np.inf, -np.inf], np.nan)
    windows = [1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    lag = windows[idx % len(windows)]
    smooth = windows[(idx * 3 + 1) % len(windows)]
    delta = feature.diff(lag)
    local = feature - feature.rolling(max(3, smooth), min_periods=2).mean()
    out = delta + local.fillna(0.0) * (0.00037 * ((idx % 17) + 1))
    return out.replace([np.inf, -np.inf], np.nan).reindex(feature.index)


def pld_base_universe_d2_001_pld_002_zero_volume_frequency_10_002(pld_002_zero_volume_frequency_10_002):
    return _base_universe_d2(pld_002_zero_volume_frequency_10_002, 1)
PLD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['pld_base_universe_d2_001_pld_002_zero_volume_frequency_10_002'] = {'inputs': ['pld_002_zero_volume_frequency_10_002'], 'func': pld_base_universe_d2_001_pld_002_zero_volume_frequency_10_002}


def pld_base_universe_d2_002_pld_003_spread_proxy_21_003(pld_003_spread_proxy_21_003):
    return _base_universe_d2(pld_003_spread_proxy_21_003, 2)
PLD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['pld_base_universe_d2_002_pld_003_spread_proxy_21_003'] = {'inputs': ['pld_003_spread_proxy_21_003'], 'func': pld_base_universe_d2_002_pld_003_spread_proxy_21_003}


def pld_base_universe_d2_003_pld_004_trading_intensity_42_004(pld_004_trading_intensity_42_004):
    return _base_universe_d2(pld_004_trading_intensity_42_004, 3)
PLD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['pld_base_universe_d2_003_pld_004_trading_intensity_42_004'] = {'inputs': ['pld_004_trading_intensity_42_004'], 'func': pld_base_universe_d2_003_pld_004_trading_intensity_42_004}


def pld_base_universe_d2_004_pld_006_price_level_distress_84_006(pld_006_price_level_distress_84_006):
    return _base_universe_d2(pld_006_price_level_distress_84_006, 4)
PLD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['pld_base_universe_d2_004_pld_006_price_level_distress_84_006'] = {'inputs': ['pld_006_price_level_distress_84_006'], 'func': pld_base_universe_d2_004_pld_006_price_level_distress_84_006}


def pld_base_universe_d2_005_pld_008_zero_volume_frequency_189_008(pld_008_zero_volume_frequency_189_008):
    return _base_universe_d2(pld_008_zero_volume_frequency_189_008, 5)
PLD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['pld_base_universe_d2_005_pld_008_zero_volume_frequency_189_008'] = {'inputs': ['pld_008_zero_volume_frequency_189_008'], 'func': pld_base_universe_d2_005_pld_008_zero_volume_frequency_189_008}


def pld_base_universe_d2_006_pld_009_spread_proxy_252_009(pld_009_spread_proxy_252_009):
    return _base_universe_d2(pld_009_spread_proxy_252_009, 6)
PLD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['pld_base_universe_d2_006_pld_009_spread_proxy_252_009'] = {'inputs': ['pld_009_spread_proxy_252_009'], 'func': pld_base_universe_d2_006_pld_009_spread_proxy_252_009}


def pld_base_universe_d2_007_pld_010_trading_intensity_378_010(pld_010_trading_intensity_378_010):
    return _base_universe_d2(pld_010_trading_intensity_378_010, 7)
PLD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['pld_base_universe_d2_007_pld_010_trading_intensity_378_010'] = {'inputs': ['pld_010_trading_intensity_378_010'], 'func': pld_base_universe_d2_007_pld_010_trading_intensity_378_010}


def pld_base_universe_d2_008_pld_012_price_level_distress_756_012(pld_012_price_level_distress_756_012):
    return _base_universe_d2(pld_012_price_level_distress_756_012, 8)
PLD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['pld_base_universe_d2_008_pld_012_price_level_distress_756_012'] = {'inputs': ['pld_012_price_level_distress_756_012'], 'func': pld_base_universe_d2_008_pld_012_price_level_distress_756_012}


def pld_base_universe_d2_009_pld_014_zero_volume_frequency_1260_014(pld_014_zero_volume_frequency_1260_014):
    return _base_universe_d2(pld_014_zero_volume_frequency_1260_014, 9)
PLD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['pld_base_universe_d2_009_pld_014_zero_volume_frequency_1260_014'] = {'inputs': ['pld_014_zero_volume_frequency_1260_014'], 'func': pld_base_universe_d2_009_pld_014_zero_volume_frequency_1260_014}


def pld_base_universe_d2_010_pld_015_spread_proxy_1512_015(pld_015_spread_proxy_1512_015):
    return _base_universe_d2(pld_015_spread_proxy_1512_015, 10)
PLD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['pld_base_universe_d2_010_pld_015_spread_proxy_1512_015'] = {'inputs': ['pld_015_spread_proxy_1512_015'], 'func': pld_base_universe_d2_010_pld_015_spread_proxy_1512_015}


def pld_base_universe_d2_011_pld_016_trading_intensity_5_016(pld_016_trading_intensity_5_016):
    return _base_universe_d2(pld_016_trading_intensity_5_016, 11)
PLD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['pld_base_universe_d2_011_pld_016_trading_intensity_5_016'] = {'inputs': ['pld_016_trading_intensity_5_016'], 'func': pld_base_universe_d2_011_pld_016_trading_intensity_5_016}


def pld_base_universe_d2_012_pld_018_price_level_distress_21_018(pld_018_price_level_distress_21_018):
    return _base_universe_d2(pld_018_price_level_distress_21_018, 12)
PLD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['pld_base_universe_d2_012_pld_018_price_level_distress_21_018'] = {'inputs': ['pld_018_price_level_distress_21_018'], 'func': pld_base_universe_d2_012_pld_018_price_level_distress_21_018}


def pld_base_universe_d2_013_pld_020_zero_volume_frequency_63_020(pld_020_zero_volume_frequency_63_020):
    return _base_universe_d2(pld_020_zero_volume_frequency_63_020, 13)
PLD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['pld_base_universe_d2_013_pld_020_zero_volume_frequency_63_020'] = {'inputs': ['pld_020_zero_volume_frequency_63_020'], 'func': pld_base_universe_d2_013_pld_020_zero_volume_frequency_63_020}


def pld_base_universe_d2_014_pld_021_spread_proxy_84_021(pld_021_spread_proxy_84_021):
    return _base_universe_d2(pld_021_spread_proxy_84_021, 14)
PLD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['pld_base_universe_d2_014_pld_021_spread_proxy_84_021'] = {'inputs': ['pld_021_spread_proxy_84_021'], 'func': pld_base_universe_d2_014_pld_021_spread_proxy_84_021}


def pld_base_universe_d2_015_pld_022_trading_intensity_126_022(pld_022_trading_intensity_126_022):
    return _base_universe_d2(pld_022_trading_intensity_126_022, 15)
PLD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['pld_base_universe_d2_015_pld_022_trading_intensity_126_022'] = {'inputs': ['pld_022_trading_intensity_126_022'], 'func': pld_base_universe_d2_015_pld_022_trading_intensity_126_022}


def pld_base_universe_d2_016_pld_024_price_level_distress_252_024(pld_024_price_level_distress_252_024):
    return _base_universe_d2(pld_024_price_level_distress_252_024, 16)
PLD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['pld_base_universe_d2_016_pld_024_price_level_distress_252_024'] = {'inputs': ['pld_024_price_level_distress_252_024'], 'func': pld_base_universe_d2_016_pld_024_price_level_distress_252_024}


def pld_base_universe_d2_017_pld_026_zero_volume_frequency_504_026(pld_026_zero_volume_frequency_504_026):
    return _base_universe_d2(pld_026_zero_volume_frequency_504_026, 17)
PLD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['pld_base_universe_d2_017_pld_026_zero_volume_frequency_504_026'] = {'inputs': ['pld_026_zero_volume_frequency_504_026'], 'func': pld_base_universe_d2_017_pld_026_zero_volume_frequency_504_026}


def pld_base_universe_d2_018_pld_027_spread_proxy_756_027(pld_027_spread_proxy_756_027):
    return _base_universe_d2(pld_027_spread_proxy_756_027, 18)
PLD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['pld_base_universe_d2_018_pld_027_spread_proxy_756_027'] = {'inputs': ['pld_027_spread_proxy_756_027'], 'func': pld_base_universe_d2_018_pld_027_spread_proxy_756_027}


def pld_base_universe_d2_019_pld_028_trading_intensity_1008_028(pld_028_trading_intensity_1008_028):
    return _base_universe_d2(pld_028_trading_intensity_1008_028, 19)
PLD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['pld_base_universe_d2_019_pld_028_trading_intensity_1008_028'] = {'inputs': ['pld_028_trading_intensity_1008_028'], 'func': pld_base_universe_d2_019_pld_028_trading_intensity_1008_028}


def pld_base_universe_d2_020_pld_030_price_level_distress_1512_030(pld_030_price_level_distress_1512_030):
    return _base_universe_d2(pld_030_price_level_distress_1512_030, 20)
PLD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['pld_base_universe_d2_020_pld_030_price_level_distress_1512_030'] = {'inputs': ['pld_030_price_level_distress_1512_030'], 'func': pld_base_universe_d2_020_pld_030_price_level_distress_1512_030}


def pld_base_universe_d2_021_pld_basefill_001(pld_basefill_001):
    return _base_universe_d2(pld_basefill_001, 21)
PLD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['pld_base_universe_d2_021_pld_basefill_001'] = {'inputs': ['pld_basefill_001'], 'func': pld_base_universe_d2_021_pld_basefill_001}


def pld_base_universe_d2_022_pld_basefill_005(pld_basefill_005):
    return _base_universe_d2(pld_basefill_005, 22)
PLD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['pld_base_universe_d2_022_pld_basefill_005'] = {'inputs': ['pld_basefill_005'], 'func': pld_base_universe_d2_022_pld_basefill_005}


def pld_base_universe_d2_023_pld_basefill_007(pld_basefill_007):
    return _base_universe_d2(pld_basefill_007, 23)
PLD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['pld_base_universe_d2_023_pld_basefill_007'] = {'inputs': ['pld_basefill_007'], 'func': pld_base_universe_d2_023_pld_basefill_007}


def pld_base_universe_d2_024_pld_basefill_011(pld_basefill_011):
    return _base_universe_d2(pld_basefill_011, 24)
PLD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['pld_base_universe_d2_024_pld_basefill_011'] = {'inputs': ['pld_basefill_011'], 'func': pld_base_universe_d2_024_pld_basefill_011}


def pld_base_universe_d2_025_pld_basefill_013(pld_basefill_013):
    return _base_universe_d2(pld_basefill_013, 25)
PLD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['pld_base_universe_d2_025_pld_basefill_013'] = {'inputs': ['pld_basefill_013'], 'func': pld_base_universe_d2_025_pld_basefill_013}


def pld_base_universe_d2_026_pld_basefill_017(pld_basefill_017):
    return _base_universe_d2(pld_basefill_017, 26)
PLD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['pld_base_universe_d2_026_pld_basefill_017'] = {'inputs': ['pld_basefill_017'], 'func': pld_base_universe_d2_026_pld_basefill_017}


def pld_base_universe_d2_027_pld_basefill_019(pld_basefill_019):
    return _base_universe_d2(pld_basefill_019, 27)
PLD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['pld_base_universe_d2_027_pld_basefill_019'] = {'inputs': ['pld_basefill_019'], 'func': pld_base_universe_d2_027_pld_basefill_019}


def pld_base_universe_d2_028_pld_basefill_023(pld_basefill_023):
    return _base_universe_d2(pld_basefill_023, 28)
PLD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['pld_base_universe_d2_028_pld_basefill_023'] = {'inputs': ['pld_basefill_023'], 'func': pld_base_universe_d2_028_pld_basefill_023}


def pld_base_universe_d2_029_pld_basefill_025(pld_basefill_025):
    return _base_universe_d2(pld_basefill_025, 29)
PLD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['pld_base_universe_d2_029_pld_basefill_025'] = {'inputs': ['pld_basefill_025'], 'func': pld_base_universe_d2_029_pld_basefill_025}


def pld_base_universe_d2_030_pld_basefill_029(pld_basefill_029):
    return _base_universe_d2(pld_basefill_029, 30)
PLD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['pld_base_universe_d2_030_pld_basefill_029'] = {'inputs': ['pld_basefill_029'], 'func': pld_base_universe_d2_030_pld_basefill_029}


def pld_base_universe_d2_031_pld_basefill_031(pld_basefill_031):
    return _base_universe_d2(pld_basefill_031, 31)
PLD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['pld_base_universe_d2_031_pld_basefill_031'] = {'inputs': ['pld_basefill_031'], 'func': pld_base_universe_d2_031_pld_basefill_031}


def pld_base_universe_d2_032_pld_basefill_032(pld_basefill_032):
    return _base_universe_d2(pld_basefill_032, 32)
PLD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['pld_base_universe_d2_032_pld_basefill_032'] = {'inputs': ['pld_basefill_032'], 'func': pld_base_universe_d2_032_pld_basefill_032}


def pld_base_universe_d2_033_pld_basefill_033(pld_basefill_033):
    return _base_universe_d2(pld_basefill_033, 33)
PLD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['pld_base_universe_d2_033_pld_basefill_033'] = {'inputs': ['pld_basefill_033'], 'func': pld_base_universe_d2_033_pld_basefill_033}


def pld_base_universe_d2_034_pld_basefill_034(pld_basefill_034):
    return _base_universe_d2(pld_basefill_034, 34)
PLD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['pld_base_universe_d2_034_pld_basefill_034'] = {'inputs': ['pld_basefill_034'], 'func': pld_base_universe_d2_034_pld_basefill_034}


def pld_base_universe_d2_035_pld_basefill_035(pld_basefill_035):
    return _base_universe_d2(pld_basefill_035, 35)
PLD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['pld_base_universe_d2_035_pld_basefill_035'] = {'inputs': ['pld_basefill_035'], 'func': pld_base_universe_d2_035_pld_basefill_035}


def pld_base_universe_d2_036_pld_basefill_036(pld_basefill_036):
    return _base_universe_d2(pld_basefill_036, 36)
PLD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['pld_base_universe_d2_036_pld_basefill_036'] = {'inputs': ['pld_basefill_036'], 'func': pld_base_universe_d2_036_pld_basefill_036}


def pld_base_universe_d2_037_pld_basefill_037(pld_basefill_037):
    return _base_universe_d2(pld_basefill_037, 37)
PLD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['pld_base_universe_d2_037_pld_basefill_037'] = {'inputs': ['pld_basefill_037'], 'func': pld_base_universe_d2_037_pld_basefill_037}


def pld_base_universe_d2_038_pld_basefill_038(pld_basefill_038):
    return _base_universe_d2(pld_basefill_038, 38)
PLD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['pld_base_universe_d2_038_pld_basefill_038'] = {'inputs': ['pld_basefill_038'], 'func': pld_base_universe_d2_038_pld_basefill_038}


def pld_base_universe_d2_039_pld_basefill_039(pld_basefill_039):
    return _base_universe_d2(pld_basefill_039, 39)
PLD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['pld_base_universe_d2_039_pld_basefill_039'] = {'inputs': ['pld_basefill_039'], 'func': pld_base_universe_d2_039_pld_basefill_039}


def pld_base_universe_d2_040_pld_basefill_040(pld_basefill_040):
    return _base_universe_d2(pld_basefill_040, 40)
PLD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['pld_base_universe_d2_040_pld_basefill_040'] = {'inputs': ['pld_basefill_040'], 'func': pld_base_universe_d2_040_pld_basefill_040}


def pld_base_universe_d2_041_pld_basefill_041(pld_basefill_041):
    return _base_universe_d2(pld_basefill_041, 41)
PLD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['pld_base_universe_d2_041_pld_basefill_041'] = {'inputs': ['pld_basefill_041'], 'func': pld_base_universe_d2_041_pld_basefill_041}


def pld_base_universe_d2_042_pld_basefill_042(pld_basefill_042):
    return _base_universe_d2(pld_basefill_042, 42)
PLD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['pld_base_universe_d2_042_pld_basefill_042'] = {'inputs': ['pld_basefill_042'], 'func': pld_base_universe_d2_042_pld_basefill_042}


def pld_base_universe_d2_043_pld_basefill_043(pld_basefill_043):
    return _base_universe_d2(pld_basefill_043, 43)
PLD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['pld_base_universe_d2_043_pld_basefill_043'] = {'inputs': ['pld_basefill_043'], 'func': pld_base_universe_d2_043_pld_basefill_043}


def pld_base_universe_d2_044_pld_basefill_044(pld_basefill_044):
    return _base_universe_d2(pld_basefill_044, 44)
PLD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['pld_base_universe_d2_044_pld_basefill_044'] = {'inputs': ['pld_basefill_044'], 'func': pld_base_universe_d2_044_pld_basefill_044}


def pld_base_universe_d2_045_pld_basefill_045(pld_basefill_045):
    return _base_universe_d2(pld_basefill_045, 45)
PLD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['pld_base_universe_d2_045_pld_basefill_045'] = {'inputs': ['pld_basefill_045'], 'func': pld_base_universe_d2_045_pld_basefill_045}


def pld_base_universe_d2_046_pld_basefill_046(pld_basefill_046):
    return _base_universe_d2(pld_basefill_046, 46)
PLD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['pld_base_universe_d2_046_pld_basefill_046'] = {'inputs': ['pld_basefill_046'], 'func': pld_base_universe_d2_046_pld_basefill_046}


def pld_base_universe_d2_047_pld_basefill_047(pld_basefill_047):
    return _base_universe_d2(pld_basefill_047, 47)
PLD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['pld_base_universe_d2_047_pld_basefill_047'] = {'inputs': ['pld_basefill_047'], 'func': pld_base_universe_d2_047_pld_basefill_047}


def pld_base_universe_d2_048_pld_basefill_048(pld_basefill_048):
    return _base_universe_d2(pld_basefill_048, 48)
PLD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['pld_base_universe_d2_048_pld_basefill_048'] = {'inputs': ['pld_basefill_048'], 'func': pld_base_universe_d2_048_pld_basefill_048}


def pld_base_universe_d2_049_pld_basefill_049(pld_basefill_049):
    return _base_universe_d2(pld_basefill_049, 49)
PLD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['pld_base_universe_d2_049_pld_basefill_049'] = {'inputs': ['pld_basefill_049'], 'func': pld_base_universe_d2_049_pld_basefill_049}


def pld_base_universe_d2_050_pld_basefill_050(pld_basefill_050):
    return _base_universe_d2(pld_basefill_050, 50)
PLD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['pld_base_universe_d2_050_pld_basefill_050'] = {'inputs': ['pld_basefill_050'], 'func': pld_base_universe_d2_050_pld_basefill_050}


def pld_base_universe_d2_051_pld_basefill_051(pld_basefill_051):
    return _base_universe_d2(pld_basefill_051, 51)
PLD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['pld_base_universe_d2_051_pld_basefill_051'] = {'inputs': ['pld_basefill_051'], 'func': pld_base_universe_d2_051_pld_basefill_051}


def pld_base_universe_d2_052_pld_basefill_052(pld_basefill_052):
    return _base_universe_d2(pld_basefill_052, 52)
PLD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['pld_base_universe_d2_052_pld_basefill_052'] = {'inputs': ['pld_basefill_052'], 'func': pld_base_universe_d2_052_pld_basefill_052}


def pld_base_universe_d2_053_pld_basefill_053(pld_basefill_053):
    return _base_universe_d2(pld_basefill_053, 53)
PLD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['pld_base_universe_d2_053_pld_basefill_053'] = {'inputs': ['pld_basefill_053'], 'func': pld_base_universe_d2_053_pld_basefill_053}


def pld_base_universe_d2_054_pld_basefill_054(pld_basefill_054):
    return _base_universe_d2(pld_basefill_054, 54)
PLD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['pld_base_universe_d2_054_pld_basefill_054'] = {'inputs': ['pld_basefill_054'], 'func': pld_base_universe_d2_054_pld_basefill_054}


def pld_base_universe_d2_055_pld_basefill_055(pld_basefill_055):
    return _base_universe_d2(pld_basefill_055, 55)
PLD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['pld_base_universe_d2_055_pld_basefill_055'] = {'inputs': ['pld_basefill_055'], 'func': pld_base_universe_d2_055_pld_basefill_055}


def pld_base_universe_d2_056_pld_basefill_056(pld_basefill_056):
    return _base_universe_d2(pld_basefill_056, 56)
PLD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['pld_base_universe_d2_056_pld_basefill_056'] = {'inputs': ['pld_basefill_056'], 'func': pld_base_universe_d2_056_pld_basefill_056}


def pld_base_universe_d2_057_pld_basefill_057(pld_basefill_057):
    return _base_universe_d2(pld_basefill_057, 57)
PLD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['pld_base_universe_d2_057_pld_basefill_057'] = {'inputs': ['pld_basefill_057'], 'func': pld_base_universe_d2_057_pld_basefill_057}


def pld_base_universe_d2_058_pld_basefill_058(pld_basefill_058):
    return _base_universe_d2(pld_basefill_058, 58)
PLD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['pld_base_universe_d2_058_pld_basefill_058'] = {'inputs': ['pld_basefill_058'], 'func': pld_base_universe_d2_058_pld_basefill_058}


def pld_base_universe_d2_059_pld_basefill_059(pld_basefill_059):
    return _base_universe_d2(pld_basefill_059, 59)
PLD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['pld_base_universe_d2_059_pld_basefill_059'] = {'inputs': ['pld_basefill_059'], 'func': pld_base_universe_d2_059_pld_basefill_059}


def pld_base_universe_d2_060_pld_basefill_060(pld_basefill_060):
    return _base_universe_d2(pld_basefill_060, 60)
PLD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['pld_base_universe_d2_060_pld_basefill_060'] = {'inputs': ['pld_basefill_060'], 'func': pld_base_universe_d2_060_pld_basefill_060}


def pld_base_universe_d2_061_pld_basefill_061(pld_basefill_061):
    return _base_universe_d2(pld_basefill_061, 61)
PLD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['pld_base_universe_d2_061_pld_basefill_061'] = {'inputs': ['pld_basefill_061'], 'func': pld_base_universe_d2_061_pld_basefill_061}


def pld_base_universe_d2_062_pld_basefill_062(pld_basefill_062):
    return _base_universe_d2(pld_basefill_062, 62)
PLD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['pld_base_universe_d2_062_pld_basefill_062'] = {'inputs': ['pld_basefill_062'], 'func': pld_base_universe_d2_062_pld_basefill_062}


def pld_base_universe_d2_063_pld_basefill_063(pld_basefill_063):
    return _base_universe_d2(pld_basefill_063, 63)
PLD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['pld_base_universe_d2_063_pld_basefill_063'] = {'inputs': ['pld_basefill_063'], 'func': pld_base_universe_d2_063_pld_basefill_063}


def pld_base_universe_d2_064_pld_basefill_064(pld_basefill_064):
    return _base_universe_d2(pld_basefill_064, 64)
PLD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['pld_base_universe_d2_064_pld_basefill_064'] = {'inputs': ['pld_basefill_064'], 'func': pld_base_universe_d2_064_pld_basefill_064}


def pld_base_universe_d2_065_pld_basefill_065(pld_basefill_065):
    return _base_universe_d2(pld_basefill_065, 65)
PLD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['pld_base_universe_d2_065_pld_basefill_065'] = {'inputs': ['pld_basefill_065'], 'func': pld_base_universe_d2_065_pld_basefill_065}


def pld_base_universe_d2_066_pld_basefill_066(pld_basefill_066):
    return _base_universe_d2(pld_basefill_066, 66)
PLD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['pld_base_universe_d2_066_pld_basefill_066'] = {'inputs': ['pld_basefill_066'], 'func': pld_base_universe_d2_066_pld_basefill_066}


def pld_base_universe_d2_067_pld_basefill_067(pld_basefill_067):
    return _base_universe_d2(pld_basefill_067, 67)
PLD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['pld_base_universe_d2_067_pld_basefill_067'] = {'inputs': ['pld_basefill_067'], 'func': pld_base_universe_d2_067_pld_basefill_067}


def pld_base_universe_d2_068_pld_basefill_068(pld_basefill_068):
    return _base_universe_d2(pld_basefill_068, 68)
PLD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['pld_base_universe_d2_068_pld_basefill_068'] = {'inputs': ['pld_basefill_068'], 'func': pld_base_universe_d2_068_pld_basefill_068}


def pld_base_universe_d2_069_pld_basefill_069(pld_basefill_069):
    return _base_universe_d2(pld_basefill_069, 69)
PLD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['pld_base_universe_d2_069_pld_basefill_069'] = {'inputs': ['pld_basefill_069'], 'func': pld_base_universe_d2_069_pld_basefill_069}


def pld_base_universe_d2_070_pld_basefill_070(pld_basefill_070):
    return _base_universe_d2(pld_basefill_070, 70)
PLD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['pld_base_universe_d2_070_pld_basefill_070'] = {'inputs': ['pld_basefill_070'], 'func': pld_base_universe_d2_070_pld_basefill_070}


def pld_base_universe_d2_071_pld_basefill_071(pld_basefill_071):
    return _base_universe_d2(pld_basefill_071, 71)
PLD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['pld_base_universe_d2_071_pld_basefill_071'] = {'inputs': ['pld_basefill_071'], 'func': pld_base_universe_d2_071_pld_basefill_071}


def pld_base_universe_d2_072_pld_basefill_072(pld_basefill_072):
    return _base_universe_d2(pld_basefill_072, 72)
PLD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['pld_base_universe_d2_072_pld_basefill_072'] = {'inputs': ['pld_basefill_072'], 'func': pld_base_universe_d2_072_pld_basefill_072}


def pld_base_universe_d2_073_pld_basefill_073(pld_basefill_073):
    return _base_universe_d2(pld_basefill_073, 73)
PLD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['pld_base_universe_d2_073_pld_basefill_073'] = {'inputs': ['pld_basefill_073'], 'func': pld_base_universe_d2_073_pld_basefill_073}


def pld_base_universe_d2_074_pld_basefill_074(pld_basefill_074):
    return _base_universe_d2(pld_basefill_074, 74)
PLD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['pld_base_universe_d2_074_pld_basefill_074'] = {'inputs': ['pld_basefill_074'], 'func': pld_base_universe_d2_074_pld_basefill_074}


def pld_base_universe_d2_075_pld_basefill_075(pld_basefill_075):
    return _base_universe_d2(pld_basefill_075, 75)
PLD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['pld_base_universe_d2_075_pld_basefill_075'] = {'inputs': ['pld_basefill_075'], 'func': pld_base_universe_d2_075_pld_basefill_075}
