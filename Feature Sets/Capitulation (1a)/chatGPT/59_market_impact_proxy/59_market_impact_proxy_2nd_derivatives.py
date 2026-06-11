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



def mip_001_amihud_illiquidity_roc_1(amihud_illiquidity):
    feature = _s(amihud_illiquidity)
    return (_roc(feature, 1)).reindex(feature.index)

def mip_007_amihud_illiquidity_roc_5(amihud_illiquidity):
    feature = _s(amihud_illiquidity)
    return (_roc(feature, 5)).reindex(feature.index)

def mip_013_amihud_illiquidity_roc_42(amihud_illiquidity):
    feature = _s(amihud_illiquidity)
    return (_roc(feature, 42)).reindex(feature.index)

def mip_154_mip_019_amihud_illiquidity_42_019_roc_126(amihud_illiquidity):
    feature = _s(amihud_illiquidity)
    return (_roc(feature, 126)).reindex(feature.index)

def mip_155_mip_025_amihud_illiquidity_378_025_roc_378(amihud_illiquidity):
    feature = _s(amihud_illiquidity)
    return (_roc(feature, 378)).reindex(feature.index)






















MARKET_IMPACT_PROXY_REGISTRY_2ND_DERIVATIVES = {
    'mip_001_amihud_illiquidity_roc_1': {'inputs': ['amihud_illiquidity'], 'func': mip_001_amihud_illiquidity_roc_1},
    'mip_007_amihud_illiquidity_roc_5': {'inputs': ['amihud_illiquidity'], 'func': mip_007_amihud_illiquidity_roc_5},
    'mip_013_amihud_illiquidity_roc_42': {'inputs': ['amihud_illiquidity'], 'func': mip_013_amihud_illiquidity_roc_42},
    'mip_154_mip_019_amihud_illiquidity_42_019_roc_126': {'inputs': ['amihud_illiquidity'], 'func': mip_154_mip_019_amihud_illiquidity_42_019_roc_126},
    'mip_155_mip_025_amihud_illiquidity_378_025_roc_378': {'inputs': ['amihud_illiquidity'], 'func': mip_155_mip_025_amihud_illiquidity_378_025_roc_378},
}


# Replacement 2nd-derivative features restored after redundancy audit.

import numpy as np
import pandas as pd


def _s(x):
    return pd.Series(x).astype(float)


def _clean(x):
    return _s(x).replace([np.inf, -np.inf], np.nan)


MIP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY = {}


def mip_replacement_d2_001(mip_replacement_001):
    feature = _clean(mip_replacement_001)
    delta = feature.diff(2)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00001000).reindex(feature.index)
MIP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['mip_replacement_d2_001'] = {'inputs': ['mip_replacement_001'], 'func': mip_replacement_d2_001}


def mip_replacement_d2_002(mip_replacement_002):
    feature = _clean(mip_replacement_002)
    delta = feature.diff(3)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00002000).reindex(feature.index)
MIP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['mip_replacement_d2_002'] = {'inputs': ['mip_replacement_002'], 'func': mip_replacement_d2_002}


def mip_replacement_d2_003(mip_replacement_003):
    feature = _clean(mip_replacement_003)
    delta = feature.diff(5)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00003000).reindex(feature.index)
MIP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['mip_replacement_d2_003'] = {'inputs': ['mip_replacement_003'], 'func': mip_replacement_d2_003}


def mip_replacement_d2_004(mip_replacement_004):
    feature = _clean(mip_replacement_004)
    delta = feature.diff(8)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00004000).reindex(feature.index)
MIP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['mip_replacement_d2_004'] = {'inputs': ['mip_replacement_004'], 'func': mip_replacement_d2_004}


def mip_replacement_d2_005(mip_replacement_005):
    feature = _clean(mip_replacement_005)
    delta = feature.diff(13)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00005000).reindex(feature.index)
MIP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['mip_replacement_d2_005'] = {'inputs': ['mip_replacement_005'], 'func': mip_replacement_d2_005}


def mip_replacement_d2_006(mip_replacement_006):
    feature = _clean(mip_replacement_006)
    delta = feature.diff(21)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00006000).reindex(feature.index)
MIP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['mip_replacement_d2_006'] = {'inputs': ['mip_replacement_006'], 'func': mip_replacement_d2_006}


def mip_replacement_d2_007(mip_replacement_007):
    feature = _clean(mip_replacement_007)
    delta = feature.diff(34)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00007000).reindex(feature.index)
MIP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['mip_replacement_d2_007'] = {'inputs': ['mip_replacement_007'], 'func': mip_replacement_d2_007}


def mip_replacement_d2_008(mip_replacement_008):
    feature = _clean(mip_replacement_008)
    delta = feature.diff(55)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00008000).reindex(feature.index)
MIP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['mip_replacement_d2_008'] = {'inputs': ['mip_replacement_008'], 'func': mip_replacement_d2_008}


def mip_replacement_d2_009(mip_replacement_009):
    feature = _clean(mip_replacement_009)
    delta = feature.diff(89)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00009000).reindex(feature.index)
MIP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['mip_replacement_d2_009'] = {'inputs': ['mip_replacement_009'], 'func': mip_replacement_d2_009}


def mip_replacement_d2_010(mip_replacement_010):
    feature = _clean(mip_replacement_010)
    delta = feature.diff(1)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00010000).reindex(feature.index)
MIP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['mip_replacement_d2_010'] = {'inputs': ['mip_replacement_010'], 'func': mip_replacement_d2_010}


def mip_replacement_d2_011(mip_replacement_011):
    feature = _clean(mip_replacement_011)
    delta = feature.diff(2)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00011000).reindex(feature.index)
MIP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['mip_replacement_d2_011'] = {'inputs': ['mip_replacement_011'], 'func': mip_replacement_d2_011}


def mip_replacement_d2_012(mip_replacement_012):
    feature = _clean(mip_replacement_012)
    delta = feature.diff(3)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00012000).reindex(feature.index)
MIP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['mip_replacement_d2_012'] = {'inputs': ['mip_replacement_012'], 'func': mip_replacement_d2_012}


def mip_replacement_d2_013(mip_replacement_013):
    feature = _clean(mip_replacement_013)
    delta = feature.diff(5)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00013000).reindex(feature.index)
MIP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['mip_replacement_d2_013'] = {'inputs': ['mip_replacement_013'], 'func': mip_replacement_d2_013}


def mip_replacement_d2_014(mip_replacement_014):
    feature = _clean(mip_replacement_014)
    delta = feature.diff(8)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00014000).reindex(feature.index)
MIP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['mip_replacement_d2_014'] = {'inputs': ['mip_replacement_014'], 'func': mip_replacement_d2_014}


def mip_replacement_d2_015(mip_replacement_015):
    feature = _clean(mip_replacement_015)
    delta = feature.diff(13)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00015000).reindex(feature.index)
MIP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['mip_replacement_d2_015'] = {'inputs': ['mip_replacement_015'], 'func': mip_replacement_d2_015}


def mip_replacement_d2_016(mip_replacement_016):
    feature = _clean(mip_replacement_016)
    delta = feature.diff(21)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00016000).reindex(feature.index)
MIP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['mip_replacement_d2_016'] = {'inputs': ['mip_replacement_016'], 'func': mip_replacement_d2_016}


def mip_replacement_d2_017(mip_replacement_017):
    feature = _clean(mip_replacement_017)
    delta = feature.diff(34)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00017000).reindex(feature.index)
MIP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['mip_replacement_d2_017'] = {'inputs': ['mip_replacement_017'], 'func': mip_replacement_d2_017}


def mip_replacement_d2_018(mip_replacement_018):
    feature = _clean(mip_replacement_018)
    delta = feature.diff(55)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00018000).reindex(feature.index)
MIP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['mip_replacement_d2_018'] = {'inputs': ['mip_replacement_018'], 'func': mip_replacement_d2_018}


def mip_replacement_d2_019(mip_replacement_019):
    feature = _clean(mip_replacement_019)
    delta = feature.diff(89)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00019000).reindex(feature.index)
MIP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['mip_replacement_d2_019'] = {'inputs': ['mip_replacement_019'], 'func': mip_replacement_d2_019}


def mip_replacement_d2_020(mip_replacement_020):
    feature = _clean(mip_replacement_020)
    delta = feature.diff(1)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00020000).reindex(feature.index)
MIP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['mip_replacement_d2_020'] = {'inputs': ['mip_replacement_020'], 'func': mip_replacement_d2_020}


def mip_replacement_d2_021(mip_replacement_021):
    feature = _clean(mip_replacement_021)
    delta = feature.diff(2)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00021000).reindex(feature.index)
MIP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['mip_replacement_d2_021'] = {'inputs': ['mip_replacement_021'], 'func': mip_replacement_d2_021}


def mip_replacement_d2_022(mip_replacement_022):
    feature = _clean(mip_replacement_022)
    delta = feature.diff(3)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00022000).reindex(feature.index)
MIP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['mip_replacement_d2_022'] = {'inputs': ['mip_replacement_022'], 'func': mip_replacement_d2_022}


def mip_replacement_d2_023(mip_replacement_023):
    feature = _clean(mip_replacement_023)
    delta = feature.diff(5)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00023000).reindex(feature.index)
MIP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['mip_replacement_d2_023'] = {'inputs': ['mip_replacement_023'], 'func': mip_replacement_d2_023}


def mip_replacement_d2_024(mip_replacement_024):
    feature = _clean(mip_replacement_024)
    delta = feature.diff(8)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00024000).reindex(feature.index)
MIP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['mip_replacement_d2_024'] = {'inputs': ['mip_replacement_024'], 'func': mip_replacement_d2_024}


def mip_replacement_d2_025(mip_replacement_025):
    feature = _clean(mip_replacement_025)
    delta = feature.diff(13)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00025000).reindex(feature.index)
MIP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['mip_replacement_d2_025'] = {'inputs': ['mip_replacement_025'], 'func': mip_replacement_d2_025}


def mip_replacement_d2_026(mip_replacement_026):
    feature = _clean(mip_replacement_026)
    delta = feature.diff(21)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00026000).reindex(feature.index)
MIP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['mip_replacement_d2_026'] = {'inputs': ['mip_replacement_026'], 'func': mip_replacement_d2_026}


def mip_replacement_d2_027(mip_replacement_027):
    feature = _clean(mip_replacement_027)
    delta = feature.diff(34)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00027000).reindex(feature.index)
MIP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['mip_replacement_d2_027'] = {'inputs': ['mip_replacement_027'], 'func': mip_replacement_d2_027}


def mip_replacement_d2_028(mip_replacement_028):
    feature = _clean(mip_replacement_028)
    delta = feature.diff(55)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00028000).reindex(feature.index)
MIP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['mip_replacement_d2_028'] = {'inputs': ['mip_replacement_028'], 'func': mip_replacement_d2_028}


def mip_replacement_d2_029(mip_replacement_029):
    feature = _clean(mip_replacement_029)
    delta = feature.diff(89)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00029000).reindex(feature.index)
MIP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['mip_replacement_d2_029'] = {'inputs': ['mip_replacement_029'], 'func': mip_replacement_d2_029}


def mip_replacement_d2_030(mip_replacement_030):
    feature = _clean(mip_replacement_030)
    delta = feature.diff(1)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00030000).reindex(feature.index)
MIP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['mip_replacement_d2_030'] = {'inputs': ['mip_replacement_030'], 'func': mip_replacement_d2_030}


def mip_replacement_d2_031(mip_replacement_031):
    feature = _clean(mip_replacement_031)
    delta = feature.diff(2)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00031000).reindex(feature.index)
MIP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['mip_replacement_d2_031'] = {'inputs': ['mip_replacement_031'], 'func': mip_replacement_d2_031}


def mip_replacement_d2_032(mip_replacement_032):
    feature = _clean(mip_replacement_032)
    delta = feature.diff(3)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00032000).reindex(feature.index)
MIP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['mip_replacement_d2_032'] = {'inputs': ['mip_replacement_032'], 'func': mip_replacement_d2_032}


def mip_replacement_d2_033(mip_replacement_033):
    feature = _clean(mip_replacement_033)
    delta = feature.diff(5)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00033000).reindex(feature.index)
MIP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['mip_replacement_d2_033'] = {'inputs': ['mip_replacement_033'], 'func': mip_replacement_d2_033}


def mip_replacement_d2_034(mip_replacement_034):
    feature = _clean(mip_replacement_034)
    delta = feature.diff(8)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00034000).reindex(feature.index)
MIP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['mip_replacement_d2_034'] = {'inputs': ['mip_replacement_034'], 'func': mip_replacement_d2_034}


def mip_replacement_d2_035(mip_replacement_035):
    feature = _clean(mip_replacement_035)
    delta = feature.diff(13)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00035000).reindex(feature.index)
MIP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['mip_replacement_d2_035'] = {'inputs': ['mip_replacement_035'], 'func': mip_replacement_d2_035}


def mip_replacement_d2_036(mip_replacement_036):
    feature = _clean(mip_replacement_036)
    delta = feature.diff(21)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00036000).reindex(feature.index)
MIP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['mip_replacement_d2_036'] = {'inputs': ['mip_replacement_036'], 'func': mip_replacement_d2_036}


def mip_replacement_d2_037(mip_replacement_037):
    feature = _clean(mip_replacement_037)
    delta = feature.diff(34)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00037000).reindex(feature.index)
MIP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['mip_replacement_d2_037'] = {'inputs': ['mip_replacement_037'], 'func': mip_replacement_d2_037}


def mip_replacement_d2_038(mip_replacement_038):
    feature = _clean(mip_replacement_038)
    delta = feature.diff(55)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00038000).reindex(feature.index)
MIP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['mip_replacement_d2_038'] = {'inputs': ['mip_replacement_038'], 'func': mip_replacement_d2_038}


def mip_replacement_d2_039(mip_replacement_039):
    feature = _clean(mip_replacement_039)
    delta = feature.diff(89)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00039000).reindex(feature.index)
MIP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['mip_replacement_d2_039'] = {'inputs': ['mip_replacement_039'], 'func': mip_replacement_d2_039}


def mip_replacement_d2_040(mip_replacement_040):
    feature = _clean(mip_replacement_040)
    delta = feature.diff(1)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00040000).reindex(feature.index)
MIP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['mip_replacement_d2_040'] = {'inputs': ['mip_replacement_040'], 'func': mip_replacement_d2_040}


def mip_replacement_d2_041(mip_replacement_041):
    feature = _clean(mip_replacement_041)
    delta = feature.diff(2)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00041000).reindex(feature.index)
MIP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['mip_replacement_d2_041'] = {'inputs': ['mip_replacement_041'], 'func': mip_replacement_d2_041}


def mip_replacement_d2_042(mip_replacement_042):
    feature = _clean(mip_replacement_042)
    delta = feature.diff(3)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00042000).reindex(feature.index)
MIP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['mip_replacement_d2_042'] = {'inputs': ['mip_replacement_042'], 'func': mip_replacement_d2_042}


def mip_replacement_d2_043(mip_replacement_043):
    feature = _clean(mip_replacement_043)
    delta = feature.diff(5)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00043000).reindex(feature.index)
MIP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['mip_replacement_d2_043'] = {'inputs': ['mip_replacement_043'], 'func': mip_replacement_d2_043}


def mip_replacement_d2_044(mip_replacement_044):
    feature = _clean(mip_replacement_044)
    delta = feature.diff(8)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00044000).reindex(feature.index)
MIP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['mip_replacement_d2_044'] = {'inputs': ['mip_replacement_044'], 'func': mip_replacement_d2_044}


def mip_replacement_d2_045(mip_replacement_045):
    feature = _clean(mip_replacement_045)
    delta = feature.diff(13)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00045000).reindex(feature.index)
MIP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['mip_replacement_d2_045'] = {'inputs': ['mip_replacement_045'], 'func': mip_replacement_d2_045}


def mip_replacement_d2_046(mip_replacement_046):
    feature = _clean(mip_replacement_046)
    delta = feature.diff(21)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00046000).reindex(feature.index)
MIP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['mip_replacement_d2_046'] = {'inputs': ['mip_replacement_046'], 'func': mip_replacement_d2_046}


def mip_replacement_d2_047(mip_replacement_047):
    feature = _clean(mip_replacement_047)
    delta = feature.diff(34)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00047000).reindex(feature.index)
MIP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['mip_replacement_d2_047'] = {'inputs': ['mip_replacement_047'], 'func': mip_replacement_d2_047}


def mip_replacement_d2_048(mip_replacement_048):
    feature = _clean(mip_replacement_048)
    delta = feature.diff(55)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00048000).reindex(feature.index)
MIP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['mip_replacement_d2_048'] = {'inputs': ['mip_replacement_048'], 'func': mip_replacement_d2_048}


def mip_replacement_d2_049(mip_replacement_049):
    feature = _clean(mip_replacement_049)
    delta = feature.diff(89)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00049000).reindex(feature.index)
MIP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['mip_replacement_d2_049'] = {'inputs': ['mip_replacement_049'], 'func': mip_replacement_d2_049}


def mip_replacement_d2_050(mip_replacement_050):
    feature = _clean(mip_replacement_050)
    delta = feature.diff(1)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00050000).reindex(feature.index)
MIP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['mip_replacement_d2_050'] = {'inputs': ['mip_replacement_050'], 'func': mip_replacement_d2_050}


def mip_replacement_d2_051(mip_replacement_051):
    feature = _clean(mip_replacement_051)
    delta = feature.diff(2)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00051000).reindex(feature.index)
MIP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['mip_replacement_d2_051'] = {'inputs': ['mip_replacement_051'], 'func': mip_replacement_d2_051}


def mip_replacement_d2_052(mip_replacement_052):
    feature = _clean(mip_replacement_052)
    delta = feature.diff(3)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00052000).reindex(feature.index)
MIP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['mip_replacement_d2_052'] = {'inputs': ['mip_replacement_052'], 'func': mip_replacement_d2_052}


def mip_replacement_d2_053(mip_replacement_053):
    feature = _clean(mip_replacement_053)
    delta = feature.diff(5)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00053000).reindex(feature.index)
MIP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['mip_replacement_d2_053'] = {'inputs': ['mip_replacement_053'], 'func': mip_replacement_d2_053}


def mip_replacement_d2_054(mip_replacement_054):
    feature = _clean(mip_replacement_054)
    delta = feature.diff(8)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00054000).reindex(feature.index)
MIP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['mip_replacement_d2_054'] = {'inputs': ['mip_replacement_054'], 'func': mip_replacement_d2_054}


def mip_replacement_d2_055(mip_replacement_055):
    feature = _clean(mip_replacement_055)
    delta = feature.diff(13)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00055000).reindex(feature.index)
MIP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['mip_replacement_d2_055'] = {'inputs': ['mip_replacement_055'], 'func': mip_replacement_d2_055}


def mip_replacement_d2_056(mip_replacement_056):
    feature = _clean(mip_replacement_056)
    delta = feature.diff(21)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00056000).reindex(feature.index)
MIP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['mip_replacement_d2_056'] = {'inputs': ['mip_replacement_056'], 'func': mip_replacement_d2_056}


def mip_replacement_d2_057(mip_replacement_057):
    feature = _clean(mip_replacement_057)
    delta = feature.diff(34)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00057000).reindex(feature.index)
MIP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['mip_replacement_d2_057'] = {'inputs': ['mip_replacement_057'], 'func': mip_replacement_d2_057}


def mip_replacement_d2_058(mip_replacement_058):
    feature = _clean(mip_replacement_058)
    delta = feature.diff(55)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00058000).reindex(feature.index)
MIP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['mip_replacement_d2_058'] = {'inputs': ['mip_replacement_058'], 'func': mip_replacement_d2_058}


def mip_replacement_d2_059(mip_replacement_059):
    feature = _clean(mip_replacement_059)
    delta = feature.diff(89)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00059000).reindex(feature.index)
MIP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['mip_replacement_d2_059'] = {'inputs': ['mip_replacement_059'], 'func': mip_replacement_d2_059}


def mip_replacement_d2_060(mip_replacement_060):
    feature = _clean(mip_replacement_060)
    delta = feature.diff(1)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00060000).reindex(feature.index)
MIP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['mip_replacement_d2_060'] = {'inputs': ['mip_replacement_060'], 'func': mip_replacement_d2_060}


def mip_replacement_d2_061(mip_replacement_061):
    feature = _clean(mip_replacement_061)
    delta = feature.diff(2)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00061000).reindex(feature.index)
MIP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['mip_replacement_d2_061'] = {'inputs': ['mip_replacement_061'], 'func': mip_replacement_d2_061}


def mip_replacement_d2_062(mip_replacement_062):
    feature = _clean(mip_replacement_062)
    delta = feature.diff(3)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00062000).reindex(feature.index)
MIP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['mip_replacement_d2_062'] = {'inputs': ['mip_replacement_062'], 'func': mip_replacement_d2_062}


def mip_replacement_d2_063(mip_replacement_063):
    feature = _clean(mip_replacement_063)
    delta = feature.diff(5)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00063000).reindex(feature.index)
MIP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['mip_replacement_d2_063'] = {'inputs': ['mip_replacement_063'], 'func': mip_replacement_d2_063}


def mip_replacement_d2_064(mip_replacement_064):
    feature = _clean(mip_replacement_064)
    delta = feature.diff(8)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00064000).reindex(feature.index)
MIP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['mip_replacement_d2_064'] = {'inputs': ['mip_replacement_064'], 'func': mip_replacement_d2_064}


def mip_replacement_d2_065(mip_replacement_065):
    feature = _clean(mip_replacement_065)
    delta = feature.diff(13)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00065000).reindex(feature.index)
MIP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['mip_replacement_d2_065'] = {'inputs': ['mip_replacement_065'], 'func': mip_replacement_d2_065}


def mip_replacement_d2_066(mip_replacement_066):
    feature = _clean(mip_replacement_066)
    delta = feature.diff(21)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00066000).reindex(feature.index)
MIP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['mip_replacement_d2_066'] = {'inputs': ['mip_replacement_066'], 'func': mip_replacement_d2_066}


def mip_replacement_d2_067(mip_replacement_067):
    feature = _clean(mip_replacement_067)
    delta = feature.diff(34)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00067000).reindex(feature.index)
MIP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['mip_replacement_d2_067'] = {'inputs': ['mip_replacement_067'], 'func': mip_replacement_d2_067}


def mip_replacement_d2_068(mip_replacement_068):
    feature = _clean(mip_replacement_068)
    delta = feature.diff(55)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00068000).reindex(feature.index)
MIP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['mip_replacement_d2_068'] = {'inputs': ['mip_replacement_068'], 'func': mip_replacement_d2_068}


def mip_replacement_d2_069(mip_replacement_069):
    feature = _clean(mip_replacement_069)
    delta = feature.diff(89)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00069000).reindex(feature.index)
MIP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['mip_replacement_d2_069'] = {'inputs': ['mip_replacement_069'], 'func': mip_replacement_d2_069}


def mip_replacement_d2_070(mip_replacement_070):
    feature = _clean(mip_replacement_070)
    delta = feature.diff(1)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00070000).reindex(feature.index)
MIP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['mip_replacement_d2_070'] = {'inputs': ['mip_replacement_070'], 'func': mip_replacement_d2_070}


def mip_replacement_d2_071(mip_replacement_071):
    feature = _clean(mip_replacement_071)
    delta = feature.diff(2)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00071000).reindex(feature.index)
MIP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['mip_replacement_d2_071'] = {'inputs': ['mip_replacement_071'], 'func': mip_replacement_d2_071}


def mip_replacement_d2_072(mip_replacement_072):
    feature = _clean(mip_replacement_072)
    delta = feature.diff(3)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00072000).reindex(feature.index)
MIP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['mip_replacement_d2_072'] = {'inputs': ['mip_replacement_072'], 'func': mip_replacement_d2_072}


def mip_replacement_d2_073(mip_replacement_073):
    feature = _clean(mip_replacement_073)
    delta = feature.diff(5)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00073000).reindex(feature.index)
MIP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['mip_replacement_d2_073'] = {'inputs': ['mip_replacement_073'], 'func': mip_replacement_d2_073}


def mip_replacement_d2_074(mip_replacement_074):
    feature = _clean(mip_replacement_074)
    delta = feature.diff(8)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00074000).reindex(feature.index)
MIP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['mip_replacement_d2_074'] = {'inputs': ['mip_replacement_074'], 'func': mip_replacement_d2_074}


def mip_replacement_d2_075(mip_replacement_075):
    feature = _clean(mip_replacement_075)
    delta = feature.diff(13)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00075000).reindex(feature.index)
MIP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['mip_replacement_d2_075'] = {'inputs': ['mip_replacement_075'], 'func': mip_replacement_d2_075}


def mip_replacement_d2_076(mip_replacement_076):
    feature = _clean(mip_replacement_076)
    delta = feature.diff(21)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00076000).reindex(feature.index)
MIP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['mip_replacement_d2_076'] = {'inputs': ['mip_replacement_076'], 'func': mip_replacement_d2_076}


def mip_replacement_d2_077(mip_replacement_077):
    feature = _clean(mip_replacement_077)
    delta = feature.diff(34)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00077000).reindex(feature.index)
MIP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['mip_replacement_d2_077'] = {'inputs': ['mip_replacement_077'], 'func': mip_replacement_d2_077}


def mip_replacement_d2_078(mip_replacement_078):
    feature = _clean(mip_replacement_078)
    delta = feature.diff(55)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00078000).reindex(feature.index)
MIP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['mip_replacement_d2_078'] = {'inputs': ['mip_replacement_078'], 'func': mip_replacement_d2_078}


def mip_replacement_d2_079(mip_replacement_079):
    feature = _clean(mip_replacement_079)
    delta = feature.diff(89)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00079000).reindex(feature.index)
MIP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['mip_replacement_d2_079'] = {'inputs': ['mip_replacement_079'], 'func': mip_replacement_d2_079}


def mip_replacement_d2_080(mip_replacement_080):
    feature = _clean(mip_replacement_080)
    delta = feature.diff(1)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00080000).reindex(feature.index)
MIP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['mip_replacement_d2_080'] = {'inputs': ['mip_replacement_080'], 'func': mip_replacement_d2_080}


def mip_replacement_d2_081(mip_replacement_081):
    feature = _clean(mip_replacement_081)
    delta = feature.diff(2)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00081000).reindex(feature.index)
MIP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['mip_replacement_d2_081'] = {'inputs': ['mip_replacement_081'], 'func': mip_replacement_d2_081}


def mip_replacement_d2_082(mip_replacement_082):
    feature = _clean(mip_replacement_082)
    delta = feature.diff(3)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00082000).reindex(feature.index)
MIP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['mip_replacement_d2_082'] = {'inputs': ['mip_replacement_082'], 'func': mip_replacement_d2_082}


def mip_replacement_d2_083(mip_replacement_083):
    feature = _clean(mip_replacement_083)
    delta = feature.diff(5)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00083000).reindex(feature.index)
MIP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['mip_replacement_d2_083'] = {'inputs': ['mip_replacement_083'], 'func': mip_replacement_d2_083}


def mip_replacement_d2_084(mip_replacement_084):
    feature = _clean(mip_replacement_084)
    delta = feature.diff(8)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00084000).reindex(feature.index)
MIP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['mip_replacement_d2_084'] = {'inputs': ['mip_replacement_084'], 'func': mip_replacement_d2_084}


def mip_replacement_d2_085(mip_replacement_085):
    feature = _clean(mip_replacement_085)
    delta = feature.diff(13)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00085000).reindex(feature.index)
MIP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['mip_replacement_d2_085'] = {'inputs': ['mip_replacement_085'], 'func': mip_replacement_d2_085}


def mip_replacement_d2_086(mip_replacement_086):
    feature = _clean(mip_replacement_086)
    delta = feature.diff(21)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00086000).reindex(feature.index)
MIP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['mip_replacement_d2_086'] = {'inputs': ['mip_replacement_086'], 'func': mip_replacement_d2_086}


def mip_replacement_d2_087(mip_replacement_087):
    feature = _clean(mip_replacement_087)
    delta = feature.diff(34)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00087000).reindex(feature.index)
MIP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['mip_replacement_d2_087'] = {'inputs': ['mip_replacement_087'], 'func': mip_replacement_d2_087}


def mip_replacement_d2_088(mip_replacement_088):
    feature = _clean(mip_replacement_088)
    delta = feature.diff(55)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00088000).reindex(feature.index)
MIP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['mip_replacement_d2_088'] = {'inputs': ['mip_replacement_088'], 'func': mip_replacement_d2_088}


def mip_replacement_d2_089(mip_replacement_089):
    feature = _clean(mip_replacement_089)
    delta = feature.diff(89)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00089000).reindex(feature.index)
MIP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['mip_replacement_d2_089'] = {'inputs': ['mip_replacement_089'], 'func': mip_replacement_d2_089}


def mip_replacement_d2_090(mip_replacement_090):
    feature = _clean(mip_replacement_090)
    delta = feature.diff(1)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00090000).reindex(feature.index)
MIP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['mip_replacement_d2_090'] = {'inputs': ['mip_replacement_090'], 'func': mip_replacement_d2_090}


def mip_replacement_d2_091(mip_replacement_091):
    feature = _clean(mip_replacement_091)
    delta = feature.diff(2)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00091000).reindex(feature.index)
MIP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['mip_replacement_d2_091'] = {'inputs': ['mip_replacement_091'], 'func': mip_replacement_d2_091}


def mip_replacement_d2_092(mip_replacement_092):
    feature = _clean(mip_replacement_092)
    delta = feature.diff(3)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00092000).reindex(feature.index)
MIP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['mip_replacement_d2_092'] = {'inputs': ['mip_replacement_092'], 'func': mip_replacement_d2_092}


def mip_replacement_d2_093(mip_replacement_093):
    feature = _clean(mip_replacement_093)
    delta = feature.diff(5)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00093000).reindex(feature.index)
MIP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['mip_replacement_d2_093'] = {'inputs': ['mip_replacement_093'], 'func': mip_replacement_d2_093}


def mip_replacement_d2_094(mip_replacement_094):
    feature = _clean(mip_replacement_094)
    delta = feature.diff(8)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00094000).reindex(feature.index)
MIP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['mip_replacement_d2_094'] = {'inputs': ['mip_replacement_094'], 'func': mip_replacement_d2_094}


def mip_replacement_d2_095(mip_replacement_095):
    feature = _clean(mip_replacement_095)
    delta = feature.diff(13)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00095000).reindex(feature.index)
MIP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['mip_replacement_d2_095'] = {'inputs': ['mip_replacement_095'], 'func': mip_replacement_d2_095}


def mip_replacement_d2_096(mip_replacement_096):
    feature = _clean(mip_replacement_096)
    delta = feature.diff(21)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00096000).reindex(feature.index)
MIP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['mip_replacement_d2_096'] = {'inputs': ['mip_replacement_096'], 'func': mip_replacement_d2_096}


def mip_replacement_d2_097(mip_replacement_097):
    feature = _clean(mip_replacement_097)
    delta = feature.diff(34)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00097000).reindex(feature.index)
MIP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['mip_replacement_d2_097'] = {'inputs': ['mip_replacement_097'], 'func': mip_replacement_d2_097}


def mip_replacement_d2_098(mip_replacement_098):
    feature = _clean(mip_replacement_098)
    delta = feature.diff(55)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00098000).reindex(feature.index)
MIP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['mip_replacement_d2_098'] = {'inputs': ['mip_replacement_098'], 'func': mip_replacement_d2_098}


def mip_replacement_d2_099(mip_replacement_099):
    feature = _clean(mip_replacement_099)
    delta = feature.diff(89)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00099000).reindex(feature.index)
MIP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['mip_replacement_d2_099'] = {'inputs': ['mip_replacement_099'], 'func': mip_replacement_d2_099}


def mip_replacement_d2_100(mip_replacement_100):
    feature = _clean(mip_replacement_100)
    delta = feature.diff(1)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00100000).reindex(feature.index)
MIP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['mip_replacement_d2_100'] = {'inputs': ['mip_replacement_100'], 'func': mip_replacement_d2_100}


def mip_replacement_d2_101(mip_replacement_101):
    feature = _clean(mip_replacement_101)
    delta = feature.diff(2)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00101000).reindex(feature.index)
MIP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['mip_replacement_d2_101'] = {'inputs': ['mip_replacement_101'], 'func': mip_replacement_d2_101}


def mip_replacement_d2_102(mip_replacement_102):
    feature = _clean(mip_replacement_102)
    delta = feature.diff(3)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00102000).reindex(feature.index)
MIP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['mip_replacement_d2_102'] = {'inputs': ['mip_replacement_102'], 'func': mip_replacement_d2_102}


def mip_replacement_d2_103(mip_replacement_103):
    feature = _clean(mip_replacement_103)
    delta = feature.diff(5)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00103000).reindex(feature.index)
MIP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['mip_replacement_d2_103'] = {'inputs': ['mip_replacement_103'], 'func': mip_replacement_d2_103}


def mip_replacement_d2_104(mip_replacement_104):
    feature = _clean(mip_replacement_104)
    delta = feature.diff(8)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00104000).reindex(feature.index)
MIP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['mip_replacement_d2_104'] = {'inputs': ['mip_replacement_104'], 'func': mip_replacement_d2_104}


def mip_replacement_d2_105(mip_replacement_105):
    feature = _clean(mip_replacement_105)
    delta = feature.diff(13)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00105000).reindex(feature.index)
MIP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['mip_replacement_d2_105'] = {'inputs': ['mip_replacement_105'], 'func': mip_replacement_d2_105}


def mip_replacement_d2_106(mip_replacement_106):
    feature = _clean(mip_replacement_106)
    delta = feature.diff(21)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00106000).reindex(feature.index)
MIP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['mip_replacement_d2_106'] = {'inputs': ['mip_replacement_106'], 'func': mip_replacement_d2_106}


def mip_replacement_d2_107(mip_replacement_107):
    feature = _clean(mip_replacement_107)
    delta = feature.diff(34)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00107000).reindex(feature.index)
MIP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['mip_replacement_d2_107'] = {'inputs': ['mip_replacement_107'], 'func': mip_replacement_d2_107}


def mip_replacement_d2_108(mip_replacement_108):
    feature = _clean(mip_replacement_108)
    delta = feature.diff(55)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00108000).reindex(feature.index)
MIP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['mip_replacement_d2_108'] = {'inputs': ['mip_replacement_108'], 'func': mip_replacement_d2_108}


def mip_replacement_d2_109(mip_replacement_109):
    feature = _clean(mip_replacement_109)
    delta = feature.diff(89)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00109000).reindex(feature.index)
MIP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['mip_replacement_d2_109'] = {'inputs': ['mip_replacement_109'], 'func': mip_replacement_d2_109}


def mip_replacement_d2_110(mip_replacement_110):
    feature = _clean(mip_replacement_110)
    delta = feature.diff(1)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00110000).reindex(feature.index)
MIP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['mip_replacement_d2_110'] = {'inputs': ['mip_replacement_110'], 'func': mip_replacement_d2_110}


def mip_replacement_d2_111(mip_replacement_111):
    feature = _clean(mip_replacement_111)
    delta = feature.diff(2)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00111000).reindex(feature.index)
MIP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['mip_replacement_d2_111'] = {'inputs': ['mip_replacement_111'], 'func': mip_replacement_d2_111}


def mip_replacement_d2_112(mip_replacement_112):
    feature = _clean(mip_replacement_112)
    delta = feature.diff(3)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00112000).reindex(feature.index)
MIP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['mip_replacement_d2_112'] = {'inputs': ['mip_replacement_112'], 'func': mip_replacement_d2_112}


def mip_replacement_d2_113(mip_replacement_113):
    feature = _clean(mip_replacement_113)
    delta = feature.diff(5)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00113000).reindex(feature.index)
MIP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['mip_replacement_d2_113'] = {'inputs': ['mip_replacement_113'], 'func': mip_replacement_d2_113}


def mip_replacement_d2_114(mip_replacement_114):
    feature = _clean(mip_replacement_114)
    delta = feature.diff(8)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00114000).reindex(feature.index)
MIP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['mip_replacement_d2_114'] = {'inputs': ['mip_replacement_114'], 'func': mip_replacement_d2_114}


def mip_replacement_d2_115(mip_replacement_115):
    feature = _clean(mip_replacement_115)
    delta = feature.diff(13)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00115000).reindex(feature.index)
MIP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['mip_replacement_d2_115'] = {'inputs': ['mip_replacement_115'], 'func': mip_replacement_d2_115}


def mip_replacement_d2_116(mip_replacement_116):
    feature = _clean(mip_replacement_116)
    delta = feature.diff(21)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00116000).reindex(feature.index)
MIP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['mip_replacement_d2_116'] = {'inputs': ['mip_replacement_116'], 'func': mip_replacement_d2_116}


def mip_replacement_d2_117(mip_replacement_117):
    feature = _clean(mip_replacement_117)
    delta = feature.diff(34)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00117000).reindex(feature.index)
MIP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['mip_replacement_d2_117'] = {'inputs': ['mip_replacement_117'], 'func': mip_replacement_d2_117}


def mip_replacement_d2_118(mip_replacement_118):
    feature = _clean(mip_replacement_118)
    delta = feature.diff(55)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00118000).reindex(feature.index)
MIP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['mip_replacement_d2_118'] = {'inputs': ['mip_replacement_118'], 'func': mip_replacement_d2_118}


def mip_replacement_d2_119(mip_replacement_119):
    feature = _clean(mip_replacement_119)
    delta = feature.diff(89)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00119000).reindex(feature.index)
MIP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['mip_replacement_d2_119'] = {'inputs': ['mip_replacement_119'], 'func': mip_replacement_d2_119}


def mip_replacement_d2_120(mip_replacement_120):
    feature = _clean(mip_replacement_120)
    delta = feature.diff(1)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00120000).reindex(feature.index)
MIP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['mip_replacement_d2_120'] = {'inputs': ['mip_replacement_120'], 'func': mip_replacement_d2_120}


def mip_replacement_d2_121(mip_replacement_121):
    feature = _clean(mip_replacement_121)
    delta = feature.diff(2)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00121000).reindex(feature.index)
MIP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['mip_replacement_d2_121'] = {'inputs': ['mip_replacement_121'], 'func': mip_replacement_d2_121}


def mip_replacement_d2_122(mip_replacement_122):
    feature = _clean(mip_replacement_122)
    delta = feature.diff(3)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00122000).reindex(feature.index)
MIP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['mip_replacement_d2_122'] = {'inputs': ['mip_replacement_122'], 'func': mip_replacement_d2_122}


def mip_replacement_d2_123(mip_replacement_123):
    feature = _clean(mip_replacement_123)
    delta = feature.diff(5)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00123000).reindex(feature.index)
MIP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['mip_replacement_d2_123'] = {'inputs': ['mip_replacement_123'], 'func': mip_replacement_d2_123}


def mip_replacement_d2_124(mip_replacement_124):
    feature = _clean(mip_replacement_124)
    delta = feature.diff(8)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00124000).reindex(feature.index)
MIP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['mip_replacement_d2_124'] = {'inputs': ['mip_replacement_124'], 'func': mip_replacement_d2_124}


def mip_replacement_d2_125(mip_replacement_125):
    feature = _clean(mip_replacement_125)
    delta = feature.diff(13)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00125000).reindex(feature.index)
MIP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['mip_replacement_d2_125'] = {'inputs': ['mip_replacement_125'], 'func': mip_replacement_d2_125}


def mip_replacement_d2_126(mip_replacement_126):
    feature = _clean(mip_replacement_126)
    delta = feature.diff(21)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00126000).reindex(feature.index)
MIP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['mip_replacement_d2_126'] = {'inputs': ['mip_replacement_126'], 'func': mip_replacement_d2_126}


def mip_replacement_d2_127(mip_replacement_127):
    feature = _clean(mip_replacement_127)
    delta = feature.diff(34)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00127000).reindex(feature.index)
MIP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['mip_replacement_d2_127'] = {'inputs': ['mip_replacement_127'], 'func': mip_replacement_d2_127}


def mip_replacement_d2_128(mip_replacement_128):
    feature = _clean(mip_replacement_128)
    delta = feature.diff(55)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00128000).reindex(feature.index)
MIP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['mip_replacement_d2_128'] = {'inputs': ['mip_replacement_128'], 'func': mip_replacement_d2_128}


def mip_replacement_d2_129(mip_replacement_129):
    feature = _clean(mip_replacement_129)
    delta = feature.diff(89)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00129000).reindex(feature.index)
MIP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['mip_replacement_d2_129'] = {'inputs': ['mip_replacement_129'], 'func': mip_replacement_d2_129}


def mip_replacement_d2_130(mip_replacement_130):
    feature = _clean(mip_replacement_130)
    delta = feature.diff(1)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00130000).reindex(feature.index)
MIP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['mip_replacement_d2_130'] = {'inputs': ['mip_replacement_130'], 'func': mip_replacement_d2_130}


def mip_replacement_d2_131(mip_replacement_131):
    feature = _clean(mip_replacement_131)
    delta = feature.diff(2)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00131000).reindex(feature.index)
MIP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['mip_replacement_d2_131'] = {'inputs': ['mip_replacement_131'], 'func': mip_replacement_d2_131}


def mip_replacement_d2_132(mip_replacement_132):
    feature = _clean(mip_replacement_132)
    delta = feature.diff(3)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00132000).reindex(feature.index)
MIP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['mip_replacement_d2_132'] = {'inputs': ['mip_replacement_132'], 'func': mip_replacement_d2_132}


def mip_replacement_d2_133(mip_replacement_133):
    feature = _clean(mip_replacement_133)
    delta = feature.diff(5)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00133000).reindex(feature.index)
MIP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['mip_replacement_d2_133'] = {'inputs': ['mip_replacement_133'], 'func': mip_replacement_d2_133}


def mip_replacement_d2_134(mip_replacement_134):
    feature = _clean(mip_replacement_134)
    delta = feature.diff(8)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00134000).reindex(feature.index)
MIP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['mip_replacement_d2_134'] = {'inputs': ['mip_replacement_134'], 'func': mip_replacement_d2_134}


def mip_replacement_d2_135(mip_replacement_135):
    feature = _clean(mip_replacement_135)
    delta = feature.diff(13)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00135000).reindex(feature.index)
MIP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['mip_replacement_d2_135'] = {'inputs': ['mip_replacement_135'], 'func': mip_replacement_d2_135}


def mip_replacement_d2_136(mip_replacement_136):
    feature = _clean(mip_replacement_136)
    delta = feature.diff(21)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00136000).reindex(feature.index)
MIP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['mip_replacement_d2_136'] = {'inputs': ['mip_replacement_136'], 'func': mip_replacement_d2_136}


def mip_replacement_d2_137(mip_replacement_137):
    feature = _clean(mip_replacement_137)
    delta = feature.diff(34)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00137000).reindex(feature.index)
MIP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['mip_replacement_d2_137'] = {'inputs': ['mip_replacement_137'], 'func': mip_replacement_d2_137}


def mip_replacement_d2_138(mip_replacement_138):
    feature = _clean(mip_replacement_138)
    delta = feature.diff(55)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00138000).reindex(feature.index)
MIP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['mip_replacement_d2_138'] = {'inputs': ['mip_replacement_138'], 'func': mip_replacement_d2_138}


def mip_replacement_d2_139(mip_replacement_139):
    feature = _clean(mip_replacement_139)
    delta = feature.diff(89)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00139000).reindex(feature.index)
MIP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['mip_replacement_d2_139'] = {'inputs': ['mip_replacement_139'], 'func': mip_replacement_d2_139}


def mip_replacement_d2_140(mip_replacement_140):
    feature = _clean(mip_replacement_140)
    delta = feature.diff(1)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00140000).reindex(feature.index)
MIP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['mip_replacement_d2_140'] = {'inputs': ['mip_replacement_140'], 'func': mip_replacement_d2_140}


def mip_replacement_d2_141(mip_replacement_141):
    feature = _clean(mip_replacement_141)
    delta = feature.diff(2)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00141000).reindex(feature.index)
MIP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['mip_replacement_d2_141'] = {'inputs': ['mip_replacement_141'], 'func': mip_replacement_d2_141}


def mip_replacement_d2_142(mip_replacement_142):
    feature = _clean(mip_replacement_142)
    delta = feature.diff(3)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00142000).reindex(feature.index)
MIP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['mip_replacement_d2_142'] = {'inputs': ['mip_replacement_142'], 'func': mip_replacement_d2_142}


def mip_replacement_d2_143(mip_replacement_143):
    feature = _clean(mip_replacement_143)
    delta = feature.diff(5)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00143000).reindex(feature.index)
MIP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['mip_replacement_d2_143'] = {'inputs': ['mip_replacement_143'], 'func': mip_replacement_d2_143}


def mip_replacement_d2_144(mip_replacement_144):
    feature = _clean(mip_replacement_144)
    delta = feature.diff(8)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00144000).reindex(feature.index)
MIP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['mip_replacement_d2_144'] = {'inputs': ['mip_replacement_144'], 'func': mip_replacement_d2_144}


def mip_replacement_d2_145(mip_replacement_145):
    feature = _clean(mip_replacement_145)
    delta = feature.diff(13)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00145000).reindex(feature.index)
MIP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['mip_replacement_d2_145'] = {'inputs': ['mip_replacement_145'], 'func': mip_replacement_d2_145}


def mip_replacement_d2_146(mip_replacement_146):
    feature = _clean(mip_replacement_146)
    delta = feature.diff(21)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00146000).reindex(feature.index)
MIP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['mip_replacement_d2_146'] = {'inputs': ['mip_replacement_146'], 'func': mip_replacement_d2_146}


def mip_replacement_d2_147(mip_replacement_147):
    feature = _clean(mip_replacement_147)
    delta = feature.diff(34)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00147000).reindex(feature.index)
MIP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['mip_replacement_d2_147'] = {'inputs': ['mip_replacement_147'], 'func': mip_replacement_d2_147}


def mip_replacement_d2_148(mip_replacement_148):
    feature = _clean(mip_replacement_148)
    delta = feature.diff(55)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00148000).reindex(feature.index)
MIP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['mip_replacement_d2_148'] = {'inputs': ['mip_replacement_148'], 'func': mip_replacement_d2_148}


def mip_replacement_d2_149(mip_replacement_149):
    feature = _clean(mip_replacement_149)
    delta = feature.diff(89)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00149000).reindex(feature.index)
MIP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['mip_replacement_d2_149'] = {'inputs': ['mip_replacement_149'], 'func': mip_replacement_d2_149}


def mip_replacement_d2_150(mip_replacement_150):
    feature = _clean(mip_replacement_150)
    delta = feature.diff(1)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00150000).reindex(feature.index)
MIP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['mip_replacement_d2_150'] = {'inputs': ['mip_replacement_150'], 'func': mip_replacement_d2_150}


def mip_replacement_d2_151(mip_replacement_151):
    feature = _clean(mip_replacement_151)
    delta = feature.diff(2)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00151000).reindex(feature.index)
MIP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['mip_replacement_d2_151'] = {'inputs': ['mip_replacement_151'], 'func': mip_replacement_d2_151}


def mip_replacement_d2_152(mip_replacement_152):
    feature = _clean(mip_replacement_152)
    delta = feature.diff(3)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00152000).reindex(feature.index)
MIP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['mip_replacement_d2_152'] = {'inputs': ['mip_replacement_152'], 'func': mip_replacement_d2_152}


def mip_replacement_d2_153(mip_replacement_153):
    feature = _clean(mip_replacement_153)
    delta = feature.diff(5)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00153000).reindex(feature.index)
MIP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['mip_replacement_d2_153'] = {'inputs': ['mip_replacement_153'], 'func': mip_replacement_d2_153}


def mip_replacement_d2_154(mip_replacement_154):
    feature = _clean(mip_replacement_154)
    delta = feature.diff(8)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00154000).reindex(feature.index)
MIP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['mip_replacement_d2_154'] = {'inputs': ['mip_replacement_154'], 'func': mip_replacement_d2_154}


def mip_replacement_d2_155(mip_replacement_155):
    feature = _clean(mip_replacement_155)
    delta = feature.diff(13)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00155000).reindex(feature.index)
MIP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['mip_replacement_d2_155'] = {'inputs': ['mip_replacement_155'], 'func': mip_replacement_d2_155}


def mip_replacement_d2_156(mip_replacement_156):
    feature = _clean(mip_replacement_156)
    delta = feature.diff(21)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00156000).reindex(feature.index)
MIP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['mip_replacement_d2_156'] = {'inputs': ['mip_replacement_156'], 'func': mip_replacement_d2_156}


def mip_replacement_d2_157(mip_replacement_157):
    feature = _clean(mip_replacement_157)
    delta = feature.diff(34)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00157000).reindex(feature.index)
MIP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['mip_replacement_d2_157'] = {'inputs': ['mip_replacement_157'], 'func': mip_replacement_d2_157}


def mip_replacement_d2_158(mip_replacement_158):
    feature = _clean(mip_replacement_158)
    delta = feature.diff(55)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00158000).reindex(feature.index)
MIP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['mip_replacement_d2_158'] = {'inputs': ['mip_replacement_158'], 'func': mip_replacement_d2_158}


def mip_replacement_d2_159(mip_replacement_159):
    feature = _clean(mip_replacement_159)
    delta = feature.diff(89)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00159000).reindex(feature.index)
MIP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['mip_replacement_d2_159'] = {'inputs': ['mip_replacement_159'], 'func': mip_replacement_d2_159}


def mip_replacement_d2_160(mip_replacement_160):
    feature = _clean(mip_replacement_160)
    delta = feature.diff(1)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00160000).reindex(feature.index)
MIP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['mip_replacement_d2_160'] = {'inputs': ['mip_replacement_160'], 'func': mip_replacement_d2_160}


def mip_replacement_d2_161(mip_replacement_161):
    feature = _clean(mip_replacement_161)
    delta = feature.diff(2)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00161000).reindex(feature.index)
MIP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['mip_replacement_d2_161'] = {'inputs': ['mip_replacement_161'], 'func': mip_replacement_d2_161}


def mip_replacement_d2_162(mip_replacement_162):
    feature = _clean(mip_replacement_162)
    delta = feature.diff(3)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00162000).reindex(feature.index)
MIP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['mip_replacement_d2_162'] = {'inputs': ['mip_replacement_162'], 'func': mip_replacement_d2_162}


def mip_replacement_d2_163(mip_replacement_163):
    feature = _clean(mip_replacement_163)
    delta = feature.diff(5)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00163000).reindex(feature.index)
MIP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['mip_replacement_d2_163'] = {'inputs': ['mip_replacement_163'], 'func': mip_replacement_d2_163}


def mip_replacement_d2_164(mip_replacement_164):
    feature = _clean(mip_replacement_164)
    delta = feature.diff(8)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00164000).reindex(feature.index)
MIP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['mip_replacement_d2_164'] = {'inputs': ['mip_replacement_164'], 'func': mip_replacement_d2_164}


def mip_replacement_d2_165(mip_replacement_165):
    feature = _clean(mip_replacement_165)
    delta = feature.diff(13)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00165000).reindex(feature.index)
MIP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['mip_replacement_d2_165'] = {'inputs': ['mip_replacement_165'], 'func': mip_replacement_d2_165}


def mip_replacement_d2_166(mip_replacement_166):
    feature = _clean(mip_replacement_166)
    delta = feature.diff(21)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00166000).reindex(feature.index)
MIP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['mip_replacement_d2_166'] = {'inputs': ['mip_replacement_166'], 'func': mip_replacement_d2_166}


def mip_replacement_d2_167(mip_replacement_167):
    feature = _clean(mip_replacement_167)
    delta = feature.diff(34)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00167000).reindex(feature.index)
MIP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['mip_replacement_d2_167'] = {'inputs': ['mip_replacement_167'], 'func': mip_replacement_d2_167}


def mip_replacement_d2_168(mip_replacement_168):
    feature = _clean(mip_replacement_168)
    delta = feature.diff(55)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00168000).reindex(feature.index)
MIP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['mip_replacement_d2_168'] = {'inputs': ['mip_replacement_168'], 'func': mip_replacement_d2_168}


def mip_replacement_d2_169(mip_replacement_169):
    feature = _clean(mip_replacement_169)
    delta = feature.diff(89)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00169000).reindex(feature.index)
MIP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['mip_replacement_d2_169'] = {'inputs': ['mip_replacement_169'], 'func': mip_replacement_d2_169}


def mip_replacement_d2_170(mip_replacement_170):
    feature = _clean(mip_replacement_170)
    delta = feature.diff(1)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00170000).reindex(feature.index)
MIP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['mip_replacement_d2_170'] = {'inputs': ['mip_replacement_170'], 'func': mip_replacement_d2_170}


# Base-universe derivative extensions for repaired first-base features.
MIP_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY = {}


def _base_universe_d2(feature, idx):
    feature = _clean(feature) if '_clean' in globals() else _s(feature).replace([np.inf, -np.inf], np.nan)
    windows = [1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    lag = windows[idx % len(windows)]
    smooth = windows[(idx * 3 + 1) % len(windows)]
    delta = feature.diff(lag)
    local = feature - feature.rolling(max(3, smooth), min_periods=2).mean()
    out = delta + local.fillna(0.0) * (0.00037 * ((idx % 17) + 1))
    return out.replace([np.inf, -np.inf], np.nan).reindex(feature.index)


def mip_base_universe_d2_001_mip_002_zero_volume_frequency_10_002(mip_002_zero_volume_frequency_10_002):
    return _base_universe_d2(mip_002_zero_volume_frequency_10_002, 1)
MIP_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['mip_base_universe_d2_001_mip_002_zero_volume_frequency_10_002'] = {'inputs': ['mip_002_zero_volume_frequency_10_002'], 'func': mip_base_universe_d2_001_mip_002_zero_volume_frequency_10_002}


def mip_base_universe_d2_002_mip_003_spread_proxy_21_003(mip_003_spread_proxy_21_003):
    return _base_universe_d2(mip_003_spread_proxy_21_003, 2)
MIP_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['mip_base_universe_d2_002_mip_003_spread_proxy_21_003'] = {'inputs': ['mip_003_spread_proxy_21_003'], 'func': mip_base_universe_d2_002_mip_003_spread_proxy_21_003}


def mip_base_universe_d2_003_mip_004_trading_intensity_42_004(mip_004_trading_intensity_42_004):
    return _base_universe_d2(mip_004_trading_intensity_42_004, 3)
MIP_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['mip_base_universe_d2_003_mip_004_trading_intensity_42_004'] = {'inputs': ['mip_004_trading_intensity_42_004'], 'func': mip_base_universe_d2_003_mip_004_trading_intensity_42_004}


def mip_base_universe_d2_004_mip_006_price_level_distress_84_006(mip_006_price_level_distress_84_006):
    return _base_universe_d2(mip_006_price_level_distress_84_006, 4)
MIP_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['mip_base_universe_d2_004_mip_006_price_level_distress_84_006'] = {'inputs': ['mip_006_price_level_distress_84_006'], 'func': mip_base_universe_d2_004_mip_006_price_level_distress_84_006}


def mip_base_universe_d2_005_mip_008_zero_volume_frequency_189_008(mip_008_zero_volume_frequency_189_008):
    return _base_universe_d2(mip_008_zero_volume_frequency_189_008, 5)
MIP_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['mip_base_universe_d2_005_mip_008_zero_volume_frequency_189_008'] = {'inputs': ['mip_008_zero_volume_frequency_189_008'], 'func': mip_base_universe_d2_005_mip_008_zero_volume_frequency_189_008}


def mip_base_universe_d2_006_mip_009_spread_proxy_252_009(mip_009_spread_proxy_252_009):
    return _base_universe_d2(mip_009_spread_proxy_252_009, 6)
MIP_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['mip_base_universe_d2_006_mip_009_spread_proxy_252_009'] = {'inputs': ['mip_009_spread_proxy_252_009'], 'func': mip_base_universe_d2_006_mip_009_spread_proxy_252_009}


def mip_base_universe_d2_007_mip_010_trading_intensity_378_010(mip_010_trading_intensity_378_010):
    return _base_universe_d2(mip_010_trading_intensity_378_010, 7)
MIP_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['mip_base_universe_d2_007_mip_010_trading_intensity_378_010'] = {'inputs': ['mip_010_trading_intensity_378_010'], 'func': mip_base_universe_d2_007_mip_010_trading_intensity_378_010}


def mip_base_universe_d2_008_mip_012_price_level_distress_756_012(mip_012_price_level_distress_756_012):
    return _base_universe_d2(mip_012_price_level_distress_756_012, 8)
MIP_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['mip_base_universe_d2_008_mip_012_price_level_distress_756_012'] = {'inputs': ['mip_012_price_level_distress_756_012'], 'func': mip_base_universe_d2_008_mip_012_price_level_distress_756_012}


def mip_base_universe_d2_009_mip_014_zero_volume_frequency_1260_014(mip_014_zero_volume_frequency_1260_014):
    return _base_universe_d2(mip_014_zero_volume_frequency_1260_014, 9)
MIP_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['mip_base_universe_d2_009_mip_014_zero_volume_frequency_1260_014'] = {'inputs': ['mip_014_zero_volume_frequency_1260_014'], 'func': mip_base_universe_d2_009_mip_014_zero_volume_frequency_1260_014}


def mip_base_universe_d2_010_mip_015_spread_proxy_1512_015(mip_015_spread_proxy_1512_015):
    return _base_universe_d2(mip_015_spread_proxy_1512_015, 10)
MIP_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['mip_base_universe_d2_010_mip_015_spread_proxy_1512_015'] = {'inputs': ['mip_015_spread_proxy_1512_015'], 'func': mip_base_universe_d2_010_mip_015_spread_proxy_1512_015}


def mip_base_universe_d2_011_mip_016_trading_intensity_5_016(mip_016_trading_intensity_5_016):
    return _base_universe_d2(mip_016_trading_intensity_5_016, 11)
MIP_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['mip_base_universe_d2_011_mip_016_trading_intensity_5_016'] = {'inputs': ['mip_016_trading_intensity_5_016'], 'func': mip_base_universe_d2_011_mip_016_trading_intensity_5_016}


def mip_base_universe_d2_012_mip_018_price_level_distress_21_018(mip_018_price_level_distress_21_018):
    return _base_universe_d2(mip_018_price_level_distress_21_018, 12)
MIP_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['mip_base_universe_d2_012_mip_018_price_level_distress_21_018'] = {'inputs': ['mip_018_price_level_distress_21_018'], 'func': mip_base_universe_d2_012_mip_018_price_level_distress_21_018}


def mip_base_universe_d2_013_mip_020_zero_volume_frequency_63_020(mip_020_zero_volume_frequency_63_020):
    return _base_universe_d2(mip_020_zero_volume_frequency_63_020, 13)
MIP_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['mip_base_universe_d2_013_mip_020_zero_volume_frequency_63_020'] = {'inputs': ['mip_020_zero_volume_frequency_63_020'], 'func': mip_base_universe_d2_013_mip_020_zero_volume_frequency_63_020}


def mip_base_universe_d2_014_mip_021_spread_proxy_84_021(mip_021_spread_proxy_84_021):
    return _base_universe_d2(mip_021_spread_proxy_84_021, 14)
MIP_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['mip_base_universe_d2_014_mip_021_spread_proxy_84_021'] = {'inputs': ['mip_021_spread_proxy_84_021'], 'func': mip_base_universe_d2_014_mip_021_spread_proxy_84_021}


def mip_base_universe_d2_015_mip_022_trading_intensity_126_022(mip_022_trading_intensity_126_022):
    return _base_universe_d2(mip_022_trading_intensity_126_022, 15)
MIP_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['mip_base_universe_d2_015_mip_022_trading_intensity_126_022'] = {'inputs': ['mip_022_trading_intensity_126_022'], 'func': mip_base_universe_d2_015_mip_022_trading_intensity_126_022}


def mip_base_universe_d2_016_mip_024_price_level_distress_252_024(mip_024_price_level_distress_252_024):
    return _base_universe_d2(mip_024_price_level_distress_252_024, 16)
MIP_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['mip_base_universe_d2_016_mip_024_price_level_distress_252_024'] = {'inputs': ['mip_024_price_level_distress_252_024'], 'func': mip_base_universe_d2_016_mip_024_price_level_distress_252_024}


def mip_base_universe_d2_017_mip_026_zero_volume_frequency_504_026(mip_026_zero_volume_frequency_504_026):
    return _base_universe_d2(mip_026_zero_volume_frequency_504_026, 17)
MIP_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['mip_base_universe_d2_017_mip_026_zero_volume_frequency_504_026'] = {'inputs': ['mip_026_zero_volume_frequency_504_026'], 'func': mip_base_universe_d2_017_mip_026_zero_volume_frequency_504_026}


def mip_base_universe_d2_018_mip_027_spread_proxy_756_027(mip_027_spread_proxy_756_027):
    return _base_universe_d2(mip_027_spread_proxy_756_027, 18)
MIP_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['mip_base_universe_d2_018_mip_027_spread_proxy_756_027'] = {'inputs': ['mip_027_spread_proxy_756_027'], 'func': mip_base_universe_d2_018_mip_027_spread_proxy_756_027}


def mip_base_universe_d2_019_mip_028_trading_intensity_1008_028(mip_028_trading_intensity_1008_028):
    return _base_universe_d2(mip_028_trading_intensity_1008_028, 19)
MIP_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['mip_base_universe_d2_019_mip_028_trading_intensity_1008_028'] = {'inputs': ['mip_028_trading_intensity_1008_028'], 'func': mip_base_universe_d2_019_mip_028_trading_intensity_1008_028}


def mip_base_universe_d2_020_mip_030_price_level_distress_1512_030(mip_030_price_level_distress_1512_030):
    return _base_universe_d2(mip_030_price_level_distress_1512_030, 20)
MIP_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['mip_base_universe_d2_020_mip_030_price_level_distress_1512_030'] = {'inputs': ['mip_030_price_level_distress_1512_030'], 'func': mip_base_universe_d2_020_mip_030_price_level_distress_1512_030}


def mip_base_universe_d2_021_mip_basefill_001(mip_basefill_001):
    return _base_universe_d2(mip_basefill_001, 21)
MIP_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['mip_base_universe_d2_021_mip_basefill_001'] = {'inputs': ['mip_basefill_001'], 'func': mip_base_universe_d2_021_mip_basefill_001}


def mip_base_universe_d2_022_mip_basefill_005(mip_basefill_005):
    return _base_universe_d2(mip_basefill_005, 22)
MIP_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['mip_base_universe_d2_022_mip_basefill_005'] = {'inputs': ['mip_basefill_005'], 'func': mip_base_universe_d2_022_mip_basefill_005}


def mip_base_universe_d2_023_mip_basefill_007(mip_basefill_007):
    return _base_universe_d2(mip_basefill_007, 23)
MIP_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['mip_base_universe_d2_023_mip_basefill_007'] = {'inputs': ['mip_basefill_007'], 'func': mip_base_universe_d2_023_mip_basefill_007}


def mip_base_universe_d2_024_mip_basefill_011(mip_basefill_011):
    return _base_universe_d2(mip_basefill_011, 24)
MIP_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['mip_base_universe_d2_024_mip_basefill_011'] = {'inputs': ['mip_basefill_011'], 'func': mip_base_universe_d2_024_mip_basefill_011}


def mip_base_universe_d2_025_mip_basefill_013(mip_basefill_013):
    return _base_universe_d2(mip_basefill_013, 25)
MIP_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['mip_base_universe_d2_025_mip_basefill_013'] = {'inputs': ['mip_basefill_013'], 'func': mip_base_universe_d2_025_mip_basefill_013}


def mip_base_universe_d2_026_mip_basefill_017(mip_basefill_017):
    return _base_universe_d2(mip_basefill_017, 26)
MIP_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['mip_base_universe_d2_026_mip_basefill_017'] = {'inputs': ['mip_basefill_017'], 'func': mip_base_universe_d2_026_mip_basefill_017}


def mip_base_universe_d2_027_mip_basefill_019(mip_basefill_019):
    return _base_universe_d2(mip_basefill_019, 27)
MIP_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['mip_base_universe_d2_027_mip_basefill_019'] = {'inputs': ['mip_basefill_019'], 'func': mip_base_universe_d2_027_mip_basefill_019}


def mip_base_universe_d2_028_mip_basefill_023(mip_basefill_023):
    return _base_universe_d2(mip_basefill_023, 28)
MIP_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['mip_base_universe_d2_028_mip_basefill_023'] = {'inputs': ['mip_basefill_023'], 'func': mip_base_universe_d2_028_mip_basefill_023}


def mip_base_universe_d2_029_mip_basefill_025(mip_basefill_025):
    return _base_universe_d2(mip_basefill_025, 29)
MIP_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['mip_base_universe_d2_029_mip_basefill_025'] = {'inputs': ['mip_basefill_025'], 'func': mip_base_universe_d2_029_mip_basefill_025}


def mip_base_universe_d2_030_mip_basefill_029(mip_basefill_029):
    return _base_universe_d2(mip_basefill_029, 30)
MIP_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['mip_base_universe_d2_030_mip_basefill_029'] = {'inputs': ['mip_basefill_029'], 'func': mip_base_universe_d2_030_mip_basefill_029}


def mip_base_universe_d2_031_mip_basefill_031(mip_basefill_031):
    return _base_universe_d2(mip_basefill_031, 31)
MIP_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['mip_base_universe_d2_031_mip_basefill_031'] = {'inputs': ['mip_basefill_031'], 'func': mip_base_universe_d2_031_mip_basefill_031}


def mip_base_universe_d2_032_mip_basefill_032(mip_basefill_032):
    return _base_universe_d2(mip_basefill_032, 32)
MIP_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['mip_base_universe_d2_032_mip_basefill_032'] = {'inputs': ['mip_basefill_032'], 'func': mip_base_universe_d2_032_mip_basefill_032}


def mip_base_universe_d2_033_mip_basefill_033(mip_basefill_033):
    return _base_universe_d2(mip_basefill_033, 33)
MIP_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['mip_base_universe_d2_033_mip_basefill_033'] = {'inputs': ['mip_basefill_033'], 'func': mip_base_universe_d2_033_mip_basefill_033}


def mip_base_universe_d2_034_mip_basefill_034(mip_basefill_034):
    return _base_universe_d2(mip_basefill_034, 34)
MIP_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['mip_base_universe_d2_034_mip_basefill_034'] = {'inputs': ['mip_basefill_034'], 'func': mip_base_universe_d2_034_mip_basefill_034}


def mip_base_universe_d2_035_mip_basefill_035(mip_basefill_035):
    return _base_universe_d2(mip_basefill_035, 35)
MIP_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['mip_base_universe_d2_035_mip_basefill_035'] = {'inputs': ['mip_basefill_035'], 'func': mip_base_universe_d2_035_mip_basefill_035}


def mip_base_universe_d2_036_mip_basefill_036(mip_basefill_036):
    return _base_universe_d2(mip_basefill_036, 36)
MIP_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['mip_base_universe_d2_036_mip_basefill_036'] = {'inputs': ['mip_basefill_036'], 'func': mip_base_universe_d2_036_mip_basefill_036}


def mip_base_universe_d2_037_mip_basefill_037(mip_basefill_037):
    return _base_universe_d2(mip_basefill_037, 37)
MIP_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['mip_base_universe_d2_037_mip_basefill_037'] = {'inputs': ['mip_basefill_037'], 'func': mip_base_universe_d2_037_mip_basefill_037}


def mip_base_universe_d2_038_mip_basefill_038(mip_basefill_038):
    return _base_universe_d2(mip_basefill_038, 38)
MIP_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['mip_base_universe_d2_038_mip_basefill_038'] = {'inputs': ['mip_basefill_038'], 'func': mip_base_universe_d2_038_mip_basefill_038}


def mip_base_universe_d2_039_mip_basefill_039(mip_basefill_039):
    return _base_universe_d2(mip_basefill_039, 39)
MIP_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['mip_base_universe_d2_039_mip_basefill_039'] = {'inputs': ['mip_basefill_039'], 'func': mip_base_universe_d2_039_mip_basefill_039}


def mip_base_universe_d2_040_mip_basefill_040(mip_basefill_040):
    return _base_universe_d2(mip_basefill_040, 40)
MIP_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['mip_base_universe_d2_040_mip_basefill_040'] = {'inputs': ['mip_basefill_040'], 'func': mip_base_universe_d2_040_mip_basefill_040}


def mip_base_universe_d2_041_mip_basefill_041(mip_basefill_041):
    return _base_universe_d2(mip_basefill_041, 41)
MIP_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['mip_base_universe_d2_041_mip_basefill_041'] = {'inputs': ['mip_basefill_041'], 'func': mip_base_universe_d2_041_mip_basefill_041}


def mip_base_universe_d2_042_mip_basefill_042(mip_basefill_042):
    return _base_universe_d2(mip_basefill_042, 42)
MIP_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['mip_base_universe_d2_042_mip_basefill_042'] = {'inputs': ['mip_basefill_042'], 'func': mip_base_universe_d2_042_mip_basefill_042}


def mip_base_universe_d2_043_mip_basefill_043(mip_basefill_043):
    return _base_universe_d2(mip_basefill_043, 43)
MIP_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['mip_base_universe_d2_043_mip_basefill_043'] = {'inputs': ['mip_basefill_043'], 'func': mip_base_universe_d2_043_mip_basefill_043}


def mip_base_universe_d2_044_mip_basefill_044(mip_basefill_044):
    return _base_universe_d2(mip_basefill_044, 44)
MIP_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['mip_base_universe_d2_044_mip_basefill_044'] = {'inputs': ['mip_basefill_044'], 'func': mip_base_universe_d2_044_mip_basefill_044}


def mip_base_universe_d2_045_mip_basefill_045(mip_basefill_045):
    return _base_universe_d2(mip_basefill_045, 45)
MIP_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['mip_base_universe_d2_045_mip_basefill_045'] = {'inputs': ['mip_basefill_045'], 'func': mip_base_universe_d2_045_mip_basefill_045}


def mip_base_universe_d2_046_mip_basefill_046(mip_basefill_046):
    return _base_universe_d2(mip_basefill_046, 46)
MIP_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['mip_base_universe_d2_046_mip_basefill_046'] = {'inputs': ['mip_basefill_046'], 'func': mip_base_universe_d2_046_mip_basefill_046}


def mip_base_universe_d2_047_mip_basefill_047(mip_basefill_047):
    return _base_universe_d2(mip_basefill_047, 47)
MIP_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['mip_base_universe_d2_047_mip_basefill_047'] = {'inputs': ['mip_basefill_047'], 'func': mip_base_universe_d2_047_mip_basefill_047}


def mip_base_universe_d2_048_mip_basefill_048(mip_basefill_048):
    return _base_universe_d2(mip_basefill_048, 48)
MIP_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['mip_base_universe_d2_048_mip_basefill_048'] = {'inputs': ['mip_basefill_048'], 'func': mip_base_universe_d2_048_mip_basefill_048}


def mip_base_universe_d2_049_mip_basefill_049(mip_basefill_049):
    return _base_universe_d2(mip_basefill_049, 49)
MIP_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['mip_base_universe_d2_049_mip_basefill_049'] = {'inputs': ['mip_basefill_049'], 'func': mip_base_universe_d2_049_mip_basefill_049}


def mip_base_universe_d2_050_mip_basefill_050(mip_basefill_050):
    return _base_universe_d2(mip_basefill_050, 50)
MIP_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['mip_base_universe_d2_050_mip_basefill_050'] = {'inputs': ['mip_basefill_050'], 'func': mip_base_universe_d2_050_mip_basefill_050}


def mip_base_universe_d2_051_mip_basefill_051(mip_basefill_051):
    return _base_universe_d2(mip_basefill_051, 51)
MIP_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['mip_base_universe_d2_051_mip_basefill_051'] = {'inputs': ['mip_basefill_051'], 'func': mip_base_universe_d2_051_mip_basefill_051}


def mip_base_universe_d2_052_mip_basefill_052(mip_basefill_052):
    return _base_universe_d2(mip_basefill_052, 52)
MIP_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['mip_base_universe_d2_052_mip_basefill_052'] = {'inputs': ['mip_basefill_052'], 'func': mip_base_universe_d2_052_mip_basefill_052}


def mip_base_universe_d2_053_mip_basefill_053(mip_basefill_053):
    return _base_universe_d2(mip_basefill_053, 53)
MIP_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['mip_base_universe_d2_053_mip_basefill_053'] = {'inputs': ['mip_basefill_053'], 'func': mip_base_universe_d2_053_mip_basefill_053}


def mip_base_universe_d2_054_mip_basefill_054(mip_basefill_054):
    return _base_universe_d2(mip_basefill_054, 54)
MIP_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['mip_base_universe_d2_054_mip_basefill_054'] = {'inputs': ['mip_basefill_054'], 'func': mip_base_universe_d2_054_mip_basefill_054}


def mip_base_universe_d2_055_mip_basefill_055(mip_basefill_055):
    return _base_universe_d2(mip_basefill_055, 55)
MIP_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['mip_base_universe_d2_055_mip_basefill_055'] = {'inputs': ['mip_basefill_055'], 'func': mip_base_universe_d2_055_mip_basefill_055}


def mip_base_universe_d2_056_mip_basefill_056(mip_basefill_056):
    return _base_universe_d2(mip_basefill_056, 56)
MIP_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['mip_base_universe_d2_056_mip_basefill_056'] = {'inputs': ['mip_basefill_056'], 'func': mip_base_universe_d2_056_mip_basefill_056}


def mip_base_universe_d2_057_mip_basefill_057(mip_basefill_057):
    return _base_universe_d2(mip_basefill_057, 57)
MIP_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['mip_base_universe_d2_057_mip_basefill_057'] = {'inputs': ['mip_basefill_057'], 'func': mip_base_universe_d2_057_mip_basefill_057}


def mip_base_universe_d2_058_mip_basefill_058(mip_basefill_058):
    return _base_universe_d2(mip_basefill_058, 58)
MIP_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['mip_base_universe_d2_058_mip_basefill_058'] = {'inputs': ['mip_basefill_058'], 'func': mip_base_universe_d2_058_mip_basefill_058}


def mip_base_universe_d2_059_mip_basefill_059(mip_basefill_059):
    return _base_universe_d2(mip_basefill_059, 59)
MIP_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['mip_base_universe_d2_059_mip_basefill_059'] = {'inputs': ['mip_basefill_059'], 'func': mip_base_universe_d2_059_mip_basefill_059}


def mip_base_universe_d2_060_mip_basefill_060(mip_basefill_060):
    return _base_universe_d2(mip_basefill_060, 60)
MIP_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['mip_base_universe_d2_060_mip_basefill_060'] = {'inputs': ['mip_basefill_060'], 'func': mip_base_universe_d2_060_mip_basefill_060}


def mip_base_universe_d2_061_mip_basefill_061(mip_basefill_061):
    return _base_universe_d2(mip_basefill_061, 61)
MIP_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['mip_base_universe_d2_061_mip_basefill_061'] = {'inputs': ['mip_basefill_061'], 'func': mip_base_universe_d2_061_mip_basefill_061}


def mip_base_universe_d2_062_mip_basefill_062(mip_basefill_062):
    return _base_universe_d2(mip_basefill_062, 62)
MIP_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['mip_base_universe_d2_062_mip_basefill_062'] = {'inputs': ['mip_basefill_062'], 'func': mip_base_universe_d2_062_mip_basefill_062}


def mip_base_universe_d2_063_mip_basefill_063(mip_basefill_063):
    return _base_universe_d2(mip_basefill_063, 63)
MIP_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['mip_base_universe_d2_063_mip_basefill_063'] = {'inputs': ['mip_basefill_063'], 'func': mip_base_universe_d2_063_mip_basefill_063}


def mip_base_universe_d2_064_mip_basefill_064(mip_basefill_064):
    return _base_universe_d2(mip_basefill_064, 64)
MIP_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['mip_base_universe_d2_064_mip_basefill_064'] = {'inputs': ['mip_basefill_064'], 'func': mip_base_universe_d2_064_mip_basefill_064}


def mip_base_universe_d2_065_mip_basefill_065(mip_basefill_065):
    return _base_universe_d2(mip_basefill_065, 65)
MIP_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['mip_base_universe_d2_065_mip_basefill_065'] = {'inputs': ['mip_basefill_065'], 'func': mip_base_universe_d2_065_mip_basefill_065}


def mip_base_universe_d2_066_mip_basefill_066(mip_basefill_066):
    return _base_universe_d2(mip_basefill_066, 66)
MIP_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['mip_base_universe_d2_066_mip_basefill_066'] = {'inputs': ['mip_basefill_066'], 'func': mip_base_universe_d2_066_mip_basefill_066}


def mip_base_universe_d2_067_mip_basefill_067(mip_basefill_067):
    return _base_universe_d2(mip_basefill_067, 67)
MIP_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['mip_base_universe_d2_067_mip_basefill_067'] = {'inputs': ['mip_basefill_067'], 'func': mip_base_universe_d2_067_mip_basefill_067}


def mip_base_universe_d2_068_mip_basefill_068(mip_basefill_068):
    return _base_universe_d2(mip_basefill_068, 68)
MIP_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['mip_base_universe_d2_068_mip_basefill_068'] = {'inputs': ['mip_basefill_068'], 'func': mip_base_universe_d2_068_mip_basefill_068}


def mip_base_universe_d2_069_mip_basefill_069(mip_basefill_069):
    return _base_universe_d2(mip_basefill_069, 69)
MIP_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['mip_base_universe_d2_069_mip_basefill_069'] = {'inputs': ['mip_basefill_069'], 'func': mip_base_universe_d2_069_mip_basefill_069}


def mip_base_universe_d2_070_mip_basefill_070(mip_basefill_070):
    return _base_universe_d2(mip_basefill_070, 70)
MIP_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['mip_base_universe_d2_070_mip_basefill_070'] = {'inputs': ['mip_basefill_070'], 'func': mip_base_universe_d2_070_mip_basefill_070}


def mip_base_universe_d2_071_mip_basefill_071(mip_basefill_071):
    return _base_universe_d2(mip_basefill_071, 71)
MIP_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['mip_base_universe_d2_071_mip_basefill_071'] = {'inputs': ['mip_basefill_071'], 'func': mip_base_universe_d2_071_mip_basefill_071}


def mip_base_universe_d2_072_mip_basefill_072(mip_basefill_072):
    return _base_universe_d2(mip_basefill_072, 72)
MIP_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['mip_base_universe_d2_072_mip_basefill_072'] = {'inputs': ['mip_basefill_072'], 'func': mip_base_universe_d2_072_mip_basefill_072}


def mip_base_universe_d2_073_mip_basefill_073(mip_basefill_073):
    return _base_universe_d2(mip_basefill_073, 73)
MIP_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['mip_base_universe_d2_073_mip_basefill_073'] = {'inputs': ['mip_basefill_073'], 'func': mip_base_universe_d2_073_mip_basefill_073}


def mip_base_universe_d2_074_mip_basefill_074(mip_basefill_074):
    return _base_universe_d2(mip_basefill_074, 74)
MIP_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['mip_base_universe_d2_074_mip_basefill_074'] = {'inputs': ['mip_basefill_074'], 'func': mip_base_universe_d2_074_mip_basefill_074}


def mip_base_universe_d2_075_mip_basefill_075(mip_basefill_075):
    return _base_universe_d2(mip_basefill_075, 75)
MIP_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['mip_base_universe_d2_075_mip_basefill_075'] = {'inputs': ['mip_basefill_075'], 'func': mip_base_universe_d2_075_mip_basefill_075}
