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



def pcmp_001_amihud_illiquidity_roc_1(amihud_illiquidity):
    feature = _s(amihud_illiquidity)
    return (_roc(feature, 1)).reindex(feature.index)

def pcmp_007_amihud_illiquidity_roc_5(amihud_illiquidity):
    feature = _s(amihud_illiquidity)
    return (_roc(feature, 5)).reindex(feature.index)

def pcmp_013_amihud_illiquidity_roc_42(amihud_illiquidity):
    feature = _s(amihud_illiquidity)
    return (_roc(feature, 42)).reindex(feature.index)

def pcmp_154_pcmp_019_amihud_illiquidity_42_019_roc_126(amihud_illiquidity):
    feature = _s(amihud_illiquidity)
    return (_roc(feature, 126)).reindex(feature.index)

def pcmp_155_pcmp_025_amihud_illiquidity_378_025_roc_378(amihud_illiquidity):
    feature = _s(amihud_illiquidity)
    return (_roc(feature, 378)).reindex(feature.index)






















PRICE_COMPRESSION_REGISTRY_2ND_DERIVATIVES = {
    'pcmp_001_amihud_illiquidity_roc_1': {'inputs': ['amihud_illiquidity'], 'func': pcmp_001_amihud_illiquidity_roc_1},
    'pcmp_007_amihud_illiquidity_roc_5': {'inputs': ['amihud_illiquidity'], 'func': pcmp_007_amihud_illiquidity_roc_5},
    'pcmp_013_amihud_illiquidity_roc_42': {'inputs': ['amihud_illiquidity'], 'func': pcmp_013_amihud_illiquidity_roc_42},
    'pcmp_154_pcmp_019_amihud_illiquidity_42_019_roc_126': {'inputs': ['amihud_illiquidity'], 'func': pcmp_154_pcmp_019_amihud_illiquidity_42_019_roc_126},
    'pcmp_155_pcmp_025_amihud_illiquidity_378_025_roc_378': {'inputs': ['amihud_illiquidity'], 'func': pcmp_155_pcmp_025_amihud_illiquidity_378_025_roc_378},
}


# Replacement 2nd-derivative features restored after redundancy audit.

import numpy as np
import pandas as pd


def _s(x):
    return pd.Series(x).astype(float)


def _clean(x):
    return _s(x).replace([np.inf, -np.inf], np.nan)


PC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY = {}


def pc_replacement_d2_001(pc_replacement_001):
    feature = _clean(pc_replacement_001)
    delta = feature.diff(2)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00001000).reindex(feature.index)
PC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['pc_replacement_d2_001'] = {'inputs': ['pc_replacement_001'], 'func': pc_replacement_d2_001}


def pc_replacement_d2_002(pc_replacement_002):
    feature = _clean(pc_replacement_002)
    delta = feature.diff(3)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00002000).reindex(feature.index)
PC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['pc_replacement_d2_002'] = {'inputs': ['pc_replacement_002'], 'func': pc_replacement_d2_002}


def pc_replacement_d2_003(pc_replacement_003):
    feature = _clean(pc_replacement_003)
    delta = feature.diff(5)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00003000).reindex(feature.index)
PC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['pc_replacement_d2_003'] = {'inputs': ['pc_replacement_003'], 'func': pc_replacement_d2_003}


def pc_replacement_d2_004(pc_replacement_004):
    feature = _clean(pc_replacement_004)
    delta = feature.diff(8)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00004000).reindex(feature.index)
PC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['pc_replacement_d2_004'] = {'inputs': ['pc_replacement_004'], 'func': pc_replacement_d2_004}


def pc_replacement_d2_005(pc_replacement_005):
    feature = _clean(pc_replacement_005)
    delta = feature.diff(13)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00005000).reindex(feature.index)
PC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['pc_replacement_d2_005'] = {'inputs': ['pc_replacement_005'], 'func': pc_replacement_d2_005}


def pc_replacement_d2_006(pc_replacement_006):
    feature = _clean(pc_replacement_006)
    delta = feature.diff(21)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00006000).reindex(feature.index)
PC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['pc_replacement_d2_006'] = {'inputs': ['pc_replacement_006'], 'func': pc_replacement_d2_006}


def pc_replacement_d2_007(pc_replacement_007):
    feature = _clean(pc_replacement_007)
    delta = feature.diff(34)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00007000).reindex(feature.index)
PC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['pc_replacement_d2_007'] = {'inputs': ['pc_replacement_007'], 'func': pc_replacement_d2_007}


def pc_replacement_d2_008(pc_replacement_008):
    feature = _clean(pc_replacement_008)
    delta = feature.diff(55)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00008000).reindex(feature.index)
PC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['pc_replacement_d2_008'] = {'inputs': ['pc_replacement_008'], 'func': pc_replacement_d2_008}


def pc_replacement_d2_009(pc_replacement_009):
    feature = _clean(pc_replacement_009)
    delta = feature.diff(89)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00009000).reindex(feature.index)
PC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['pc_replacement_d2_009'] = {'inputs': ['pc_replacement_009'], 'func': pc_replacement_d2_009}


def pc_replacement_d2_010(pc_replacement_010):
    feature = _clean(pc_replacement_010)
    delta = feature.diff(1)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00010000).reindex(feature.index)
PC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['pc_replacement_d2_010'] = {'inputs': ['pc_replacement_010'], 'func': pc_replacement_d2_010}


def pc_replacement_d2_011(pc_replacement_011):
    feature = _clean(pc_replacement_011)
    delta = feature.diff(2)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00011000).reindex(feature.index)
PC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['pc_replacement_d2_011'] = {'inputs': ['pc_replacement_011'], 'func': pc_replacement_d2_011}


def pc_replacement_d2_012(pc_replacement_012):
    feature = _clean(pc_replacement_012)
    delta = feature.diff(3)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00012000).reindex(feature.index)
PC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['pc_replacement_d2_012'] = {'inputs': ['pc_replacement_012'], 'func': pc_replacement_d2_012}


def pc_replacement_d2_013(pc_replacement_013):
    feature = _clean(pc_replacement_013)
    delta = feature.diff(5)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00013000).reindex(feature.index)
PC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['pc_replacement_d2_013'] = {'inputs': ['pc_replacement_013'], 'func': pc_replacement_d2_013}


def pc_replacement_d2_014(pc_replacement_014):
    feature = _clean(pc_replacement_014)
    delta = feature.diff(8)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00014000).reindex(feature.index)
PC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['pc_replacement_d2_014'] = {'inputs': ['pc_replacement_014'], 'func': pc_replacement_d2_014}


def pc_replacement_d2_015(pc_replacement_015):
    feature = _clean(pc_replacement_015)
    delta = feature.diff(13)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00015000).reindex(feature.index)
PC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['pc_replacement_d2_015'] = {'inputs': ['pc_replacement_015'], 'func': pc_replacement_d2_015}


def pc_replacement_d2_016(pc_replacement_016):
    feature = _clean(pc_replacement_016)
    delta = feature.diff(21)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00016000).reindex(feature.index)
PC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['pc_replacement_d2_016'] = {'inputs': ['pc_replacement_016'], 'func': pc_replacement_d2_016}


def pc_replacement_d2_017(pc_replacement_017):
    feature = _clean(pc_replacement_017)
    delta = feature.diff(34)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00017000).reindex(feature.index)
PC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['pc_replacement_d2_017'] = {'inputs': ['pc_replacement_017'], 'func': pc_replacement_d2_017}


def pc_replacement_d2_018(pc_replacement_018):
    feature = _clean(pc_replacement_018)
    delta = feature.diff(55)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00018000).reindex(feature.index)
PC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['pc_replacement_d2_018'] = {'inputs': ['pc_replacement_018'], 'func': pc_replacement_d2_018}


def pc_replacement_d2_019(pc_replacement_019):
    feature = _clean(pc_replacement_019)
    delta = feature.diff(89)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00019000).reindex(feature.index)
PC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['pc_replacement_d2_019'] = {'inputs': ['pc_replacement_019'], 'func': pc_replacement_d2_019}


def pc_replacement_d2_020(pc_replacement_020):
    feature = _clean(pc_replacement_020)
    delta = feature.diff(1)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00020000).reindex(feature.index)
PC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['pc_replacement_d2_020'] = {'inputs': ['pc_replacement_020'], 'func': pc_replacement_d2_020}


def pc_replacement_d2_021(pc_replacement_021):
    feature = _clean(pc_replacement_021)
    delta = feature.diff(2)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00021000).reindex(feature.index)
PC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['pc_replacement_d2_021'] = {'inputs': ['pc_replacement_021'], 'func': pc_replacement_d2_021}


def pc_replacement_d2_022(pc_replacement_022):
    feature = _clean(pc_replacement_022)
    delta = feature.diff(3)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00022000).reindex(feature.index)
PC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['pc_replacement_d2_022'] = {'inputs': ['pc_replacement_022'], 'func': pc_replacement_d2_022}


def pc_replacement_d2_023(pc_replacement_023):
    feature = _clean(pc_replacement_023)
    delta = feature.diff(5)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00023000).reindex(feature.index)
PC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['pc_replacement_d2_023'] = {'inputs': ['pc_replacement_023'], 'func': pc_replacement_d2_023}


def pc_replacement_d2_024(pc_replacement_024):
    feature = _clean(pc_replacement_024)
    delta = feature.diff(8)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00024000).reindex(feature.index)
PC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['pc_replacement_d2_024'] = {'inputs': ['pc_replacement_024'], 'func': pc_replacement_d2_024}


def pc_replacement_d2_025(pc_replacement_025):
    feature = _clean(pc_replacement_025)
    delta = feature.diff(13)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00025000).reindex(feature.index)
PC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['pc_replacement_d2_025'] = {'inputs': ['pc_replacement_025'], 'func': pc_replacement_d2_025}


def pc_replacement_d2_026(pc_replacement_026):
    feature = _clean(pc_replacement_026)
    delta = feature.diff(21)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00026000).reindex(feature.index)
PC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['pc_replacement_d2_026'] = {'inputs': ['pc_replacement_026'], 'func': pc_replacement_d2_026}


def pc_replacement_d2_027(pc_replacement_027):
    feature = _clean(pc_replacement_027)
    delta = feature.diff(34)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00027000).reindex(feature.index)
PC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['pc_replacement_d2_027'] = {'inputs': ['pc_replacement_027'], 'func': pc_replacement_d2_027}


def pc_replacement_d2_028(pc_replacement_028):
    feature = _clean(pc_replacement_028)
    delta = feature.diff(55)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00028000).reindex(feature.index)
PC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['pc_replacement_d2_028'] = {'inputs': ['pc_replacement_028'], 'func': pc_replacement_d2_028}


def pc_replacement_d2_029(pc_replacement_029):
    feature = _clean(pc_replacement_029)
    delta = feature.diff(89)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00029000).reindex(feature.index)
PC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['pc_replacement_d2_029'] = {'inputs': ['pc_replacement_029'], 'func': pc_replacement_d2_029}


def pc_replacement_d2_030(pc_replacement_030):
    feature = _clean(pc_replacement_030)
    delta = feature.diff(1)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00030000).reindex(feature.index)
PC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['pc_replacement_d2_030'] = {'inputs': ['pc_replacement_030'], 'func': pc_replacement_d2_030}


def pc_replacement_d2_031(pc_replacement_031):
    feature = _clean(pc_replacement_031)
    delta = feature.diff(2)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00031000).reindex(feature.index)
PC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['pc_replacement_d2_031'] = {'inputs': ['pc_replacement_031'], 'func': pc_replacement_d2_031}


def pc_replacement_d2_032(pc_replacement_032):
    feature = _clean(pc_replacement_032)
    delta = feature.diff(3)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00032000).reindex(feature.index)
PC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['pc_replacement_d2_032'] = {'inputs': ['pc_replacement_032'], 'func': pc_replacement_d2_032}


def pc_replacement_d2_033(pc_replacement_033):
    feature = _clean(pc_replacement_033)
    delta = feature.diff(5)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00033000).reindex(feature.index)
PC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['pc_replacement_d2_033'] = {'inputs': ['pc_replacement_033'], 'func': pc_replacement_d2_033}


def pc_replacement_d2_034(pc_replacement_034):
    feature = _clean(pc_replacement_034)
    delta = feature.diff(8)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00034000).reindex(feature.index)
PC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['pc_replacement_d2_034'] = {'inputs': ['pc_replacement_034'], 'func': pc_replacement_d2_034}


def pc_replacement_d2_035(pc_replacement_035):
    feature = _clean(pc_replacement_035)
    delta = feature.diff(13)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00035000).reindex(feature.index)
PC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['pc_replacement_d2_035'] = {'inputs': ['pc_replacement_035'], 'func': pc_replacement_d2_035}


def pc_replacement_d2_036(pc_replacement_036):
    feature = _clean(pc_replacement_036)
    delta = feature.diff(21)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00036000).reindex(feature.index)
PC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['pc_replacement_d2_036'] = {'inputs': ['pc_replacement_036'], 'func': pc_replacement_d2_036}


def pc_replacement_d2_037(pc_replacement_037):
    feature = _clean(pc_replacement_037)
    delta = feature.diff(34)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00037000).reindex(feature.index)
PC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['pc_replacement_d2_037'] = {'inputs': ['pc_replacement_037'], 'func': pc_replacement_d2_037}


def pc_replacement_d2_038(pc_replacement_038):
    feature = _clean(pc_replacement_038)
    delta = feature.diff(55)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00038000).reindex(feature.index)
PC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['pc_replacement_d2_038'] = {'inputs': ['pc_replacement_038'], 'func': pc_replacement_d2_038}


def pc_replacement_d2_039(pc_replacement_039):
    feature = _clean(pc_replacement_039)
    delta = feature.diff(89)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00039000).reindex(feature.index)
PC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['pc_replacement_d2_039'] = {'inputs': ['pc_replacement_039'], 'func': pc_replacement_d2_039}


def pc_replacement_d2_040(pc_replacement_040):
    feature = _clean(pc_replacement_040)
    delta = feature.diff(1)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00040000).reindex(feature.index)
PC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['pc_replacement_d2_040'] = {'inputs': ['pc_replacement_040'], 'func': pc_replacement_d2_040}


def pc_replacement_d2_041(pc_replacement_041):
    feature = _clean(pc_replacement_041)
    delta = feature.diff(2)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00041000).reindex(feature.index)
PC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['pc_replacement_d2_041'] = {'inputs': ['pc_replacement_041'], 'func': pc_replacement_d2_041}


def pc_replacement_d2_042(pc_replacement_042):
    feature = _clean(pc_replacement_042)
    delta = feature.diff(3)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00042000).reindex(feature.index)
PC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['pc_replacement_d2_042'] = {'inputs': ['pc_replacement_042'], 'func': pc_replacement_d2_042}


def pc_replacement_d2_043(pc_replacement_043):
    feature = _clean(pc_replacement_043)
    delta = feature.diff(5)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00043000).reindex(feature.index)
PC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['pc_replacement_d2_043'] = {'inputs': ['pc_replacement_043'], 'func': pc_replacement_d2_043}


def pc_replacement_d2_044(pc_replacement_044):
    feature = _clean(pc_replacement_044)
    delta = feature.diff(8)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00044000).reindex(feature.index)
PC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['pc_replacement_d2_044'] = {'inputs': ['pc_replacement_044'], 'func': pc_replacement_d2_044}


def pc_replacement_d2_045(pc_replacement_045):
    feature = _clean(pc_replacement_045)
    delta = feature.diff(13)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00045000).reindex(feature.index)
PC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['pc_replacement_d2_045'] = {'inputs': ['pc_replacement_045'], 'func': pc_replacement_d2_045}


def pc_replacement_d2_046(pc_replacement_046):
    feature = _clean(pc_replacement_046)
    delta = feature.diff(21)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00046000).reindex(feature.index)
PC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['pc_replacement_d2_046'] = {'inputs': ['pc_replacement_046'], 'func': pc_replacement_d2_046}


def pc_replacement_d2_047(pc_replacement_047):
    feature = _clean(pc_replacement_047)
    delta = feature.diff(34)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00047000).reindex(feature.index)
PC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['pc_replacement_d2_047'] = {'inputs': ['pc_replacement_047'], 'func': pc_replacement_d2_047}


def pc_replacement_d2_048(pc_replacement_048):
    feature = _clean(pc_replacement_048)
    delta = feature.diff(55)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00048000).reindex(feature.index)
PC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['pc_replacement_d2_048'] = {'inputs': ['pc_replacement_048'], 'func': pc_replacement_d2_048}


def pc_replacement_d2_049(pc_replacement_049):
    feature = _clean(pc_replacement_049)
    delta = feature.diff(89)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00049000).reindex(feature.index)
PC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['pc_replacement_d2_049'] = {'inputs': ['pc_replacement_049'], 'func': pc_replacement_d2_049}


def pc_replacement_d2_050(pc_replacement_050):
    feature = _clean(pc_replacement_050)
    delta = feature.diff(1)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00050000).reindex(feature.index)
PC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['pc_replacement_d2_050'] = {'inputs': ['pc_replacement_050'], 'func': pc_replacement_d2_050}


def pc_replacement_d2_051(pc_replacement_051):
    feature = _clean(pc_replacement_051)
    delta = feature.diff(2)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00051000).reindex(feature.index)
PC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['pc_replacement_d2_051'] = {'inputs': ['pc_replacement_051'], 'func': pc_replacement_d2_051}


def pc_replacement_d2_052(pc_replacement_052):
    feature = _clean(pc_replacement_052)
    delta = feature.diff(3)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00052000).reindex(feature.index)
PC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['pc_replacement_d2_052'] = {'inputs': ['pc_replacement_052'], 'func': pc_replacement_d2_052}


def pc_replacement_d2_053(pc_replacement_053):
    feature = _clean(pc_replacement_053)
    delta = feature.diff(5)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00053000).reindex(feature.index)
PC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['pc_replacement_d2_053'] = {'inputs': ['pc_replacement_053'], 'func': pc_replacement_d2_053}


def pc_replacement_d2_054(pc_replacement_054):
    feature = _clean(pc_replacement_054)
    delta = feature.diff(8)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00054000).reindex(feature.index)
PC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['pc_replacement_d2_054'] = {'inputs': ['pc_replacement_054'], 'func': pc_replacement_d2_054}


def pc_replacement_d2_055(pc_replacement_055):
    feature = _clean(pc_replacement_055)
    delta = feature.diff(13)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00055000).reindex(feature.index)
PC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['pc_replacement_d2_055'] = {'inputs': ['pc_replacement_055'], 'func': pc_replacement_d2_055}


def pc_replacement_d2_056(pc_replacement_056):
    feature = _clean(pc_replacement_056)
    delta = feature.diff(21)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00056000).reindex(feature.index)
PC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['pc_replacement_d2_056'] = {'inputs': ['pc_replacement_056'], 'func': pc_replacement_d2_056}


def pc_replacement_d2_057(pc_replacement_057):
    feature = _clean(pc_replacement_057)
    delta = feature.diff(34)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00057000).reindex(feature.index)
PC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['pc_replacement_d2_057'] = {'inputs': ['pc_replacement_057'], 'func': pc_replacement_d2_057}


def pc_replacement_d2_058(pc_replacement_058):
    feature = _clean(pc_replacement_058)
    delta = feature.diff(55)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00058000).reindex(feature.index)
PC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['pc_replacement_d2_058'] = {'inputs': ['pc_replacement_058'], 'func': pc_replacement_d2_058}


def pc_replacement_d2_059(pc_replacement_059):
    feature = _clean(pc_replacement_059)
    delta = feature.diff(89)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00059000).reindex(feature.index)
PC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['pc_replacement_d2_059'] = {'inputs': ['pc_replacement_059'], 'func': pc_replacement_d2_059}


def pc_replacement_d2_060(pc_replacement_060):
    feature = _clean(pc_replacement_060)
    delta = feature.diff(1)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00060000).reindex(feature.index)
PC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['pc_replacement_d2_060'] = {'inputs': ['pc_replacement_060'], 'func': pc_replacement_d2_060}


def pc_replacement_d2_061(pc_replacement_061):
    feature = _clean(pc_replacement_061)
    delta = feature.diff(2)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00061000).reindex(feature.index)
PC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['pc_replacement_d2_061'] = {'inputs': ['pc_replacement_061'], 'func': pc_replacement_d2_061}


def pc_replacement_d2_062(pc_replacement_062):
    feature = _clean(pc_replacement_062)
    delta = feature.diff(3)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00062000).reindex(feature.index)
PC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['pc_replacement_d2_062'] = {'inputs': ['pc_replacement_062'], 'func': pc_replacement_d2_062}


def pc_replacement_d2_063(pc_replacement_063):
    feature = _clean(pc_replacement_063)
    delta = feature.diff(5)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00063000).reindex(feature.index)
PC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['pc_replacement_d2_063'] = {'inputs': ['pc_replacement_063'], 'func': pc_replacement_d2_063}


def pc_replacement_d2_064(pc_replacement_064):
    feature = _clean(pc_replacement_064)
    delta = feature.diff(8)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00064000).reindex(feature.index)
PC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['pc_replacement_d2_064'] = {'inputs': ['pc_replacement_064'], 'func': pc_replacement_d2_064}


def pc_replacement_d2_065(pc_replacement_065):
    feature = _clean(pc_replacement_065)
    delta = feature.diff(13)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00065000).reindex(feature.index)
PC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['pc_replacement_d2_065'] = {'inputs': ['pc_replacement_065'], 'func': pc_replacement_d2_065}


def pc_replacement_d2_066(pc_replacement_066):
    feature = _clean(pc_replacement_066)
    delta = feature.diff(21)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00066000).reindex(feature.index)
PC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['pc_replacement_d2_066'] = {'inputs': ['pc_replacement_066'], 'func': pc_replacement_d2_066}


def pc_replacement_d2_067(pc_replacement_067):
    feature = _clean(pc_replacement_067)
    delta = feature.diff(34)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00067000).reindex(feature.index)
PC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['pc_replacement_d2_067'] = {'inputs': ['pc_replacement_067'], 'func': pc_replacement_d2_067}


def pc_replacement_d2_068(pc_replacement_068):
    feature = _clean(pc_replacement_068)
    delta = feature.diff(55)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00068000).reindex(feature.index)
PC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['pc_replacement_d2_068'] = {'inputs': ['pc_replacement_068'], 'func': pc_replacement_d2_068}


def pc_replacement_d2_069(pc_replacement_069):
    feature = _clean(pc_replacement_069)
    delta = feature.diff(89)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00069000).reindex(feature.index)
PC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['pc_replacement_d2_069'] = {'inputs': ['pc_replacement_069'], 'func': pc_replacement_d2_069}


def pc_replacement_d2_070(pc_replacement_070):
    feature = _clean(pc_replacement_070)
    delta = feature.diff(1)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00070000).reindex(feature.index)
PC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['pc_replacement_d2_070'] = {'inputs': ['pc_replacement_070'], 'func': pc_replacement_d2_070}


def pc_replacement_d2_071(pc_replacement_071):
    feature = _clean(pc_replacement_071)
    delta = feature.diff(2)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00071000).reindex(feature.index)
PC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['pc_replacement_d2_071'] = {'inputs': ['pc_replacement_071'], 'func': pc_replacement_d2_071}


def pc_replacement_d2_072(pc_replacement_072):
    feature = _clean(pc_replacement_072)
    delta = feature.diff(3)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00072000).reindex(feature.index)
PC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['pc_replacement_d2_072'] = {'inputs': ['pc_replacement_072'], 'func': pc_replacement_d2_072}


def pc_replacement_d2_073(pc_replacement_073):
    feature = _clean(pc_replacement_073)
    delta = feature.diff(5)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00073000).reindex(feature.index)
PC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['pc_replacement_d2_073'] = {'inputs': ['pc_replacement_073'], 'func': pc_replacement_d2_073}


def pc_replacement_d2_074(pc_replacement_074):
    feature = _clean(pc_replacement_074)
    delta = feature.diff(8)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00074000).reindex(feature.index)
PC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['pc_replacement_d2_074'] = {'inputs': ['pc_replacement_074'], 'func': pc_replacement_d2_074}


def pc_replacement_d2_075(pc_replacement_075):
    feature = _clean(pc_replacement_075)
    delta = feature.diff(13)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00075000).reindex(feature.index)
PC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['pc_replacement_d2_075'] = {'inputs': ['pc_replacement_075'], 'func': pc_replacement_d2_075}


def pc_replacement_d2_076(pc_replacement_076):
    feature = _clean(pc_replacement_076)
    delta = feature.diff(21)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00076000).reindex(feature.index)
PC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['pc_replacement_d2_076'] = {'inputs': ['pc_replacement_076'], 'func': pc_replacement_d2_076}


def pc_replacement_d2_077(pc_replacement_077):
    feature = _clean(pc_replacement_077)
    delta = feature.diff(34)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00077000).reindex(feature.index)
PC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['pc_replacement_d2_077'] = {'inputs': ['pc_replacement_077'], 'func': pc_replacement_d2_077}


def pc_replacement_d2_078(pc_replacement_078):
    feature = _clean(pc_replacement_078)
    delta = feature.diff(55)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00078000).reindex(feature.index)
PC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['pc_replacement_d2_078'] = {'inputs': ['pc_replacement_078'], 'func': pc_replacement_d2_078}


def pc_replacement_d2_079(pc_replacement_079):
    feature = _clean(pc_replacement_079)
    delta = feature.diff(89)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00079000).reindex(feature.index)
PC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['pc_replacement_d2_079'] = {'inputs': ['pc_replacement_079'], 'func': pc_replacement_d2_079}


def pc_replacement_d2_080(pc_replacement_080):
    feature = _clean(pc_replacement_080)
    delta = feature.diff(1)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00080000).reindex(feature.index)
PC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['pc_replacement_d2_080'] = {'inputs': ['pc_replacement_080'], 'func': pc_replacement_d2_080}


def pc_replacement_d2_081(pc_replacement_081):
    feature = _clean(pc_replacement_081)
    delta = feature.diff(2)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00081000).reindex(feature.index)
PC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['pc_replacement_d2_081'] = {'inputs': ['pc_replacement_081'], 'func': pc_replacement_d2_081}


def pc_replacement_d2_082(pc_replacement_082):
    feature = _clean(pc_replacement_082)
    delta = feature.diff(3)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00082000).reindex(feature.index)
PC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['pc_replacement_d2_082'] = {'inputs': ['pc_replacement_082'], 'func': pc_replacement_d2_082}


def pc_replacement_d2_083(pc_replacement_083):
    feature = _clean(pc_replacement_083)
    delta = feature.diff(5)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00083000).reindex(feature.index)
PC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['pc_replacement_d2_083'] = {'inputs': ['pc_replacement_083'], 'func': pc_replacement_d2_083}


def pc_replacement_d2_084(pc_replacement_084):
    feature = _clean(pc_replacement_084)
    delta = feature.diff(8)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00084000).reindex(feature.index)
PC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['pc_replacement_d2_084'] = {'inputs': ['pc_replacement_084'], 'func': pc_replacement_d2_084}


def pc_replacement_d2_085(pc_replacement_085):
    feature = _clean(pc_replacement_085)
    delta = feature.diff(13)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00085000).reindex(feature.index)
PC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['pc_replacement_d2_085'] = {'inputs': ['pc_replacement_085'], 'func': pc_replacement_d2_085}


def pc_replacement_d2_086(pc_replacement_086):
    feature = _clean(pc_replacement_086)
    delta = feature.diff(21)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00086000).reindex(feature.index)
PC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['pc_replacement_d2_086'] = {'inputs': ['pc_replacement_086'], 'func': pc_replacement_d2_086}


def pc_replacement_d2_087(pc_replacement_087):
    feature = _clean(pc_replacement_087)
    delta = feature.diff(34)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00087000).reindex(feature.index)
PC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['pc_replacement_d2_087'] = {'inputs': ['pc_replacement_087'], 'func': pc_replacement_d2_087}


def pc_replacement_d2_088(pc_replacement_088):
    feature = _clean(pc_replacement_088)
    delta = feature.diff(55)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00088000).reindex(feature.index)
PC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['pc_replacement_d2_088'] = {'inputs': ['pc_replacement_088'], 'func': pc_replacement_d2_088}


def pc_replacement_d2_089(pc_replacement_089):
    feature = _clean(pc_replacement_089)
    delta = feature.diff(89)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00089000).reindex(feature.index)
PC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['pc_replacement_d2_089'] = {'inputs': ['pc_replacement_089'], 'func': pc_replacement_d2_089}


def pc_replacement_d2_090(pc_replacement_090):
    feature = _clean(pc_replacement_090)
    delta = feature.diff(1)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00090000).reindex(feature.index)
PC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['pc_replacement_d2_090'] = {'inputs': ['pc_replacement_090'], 'func': pc_replacement_d2_090}


def pc_replacement_d2_091(pc_replacement_091):
    feature = _clean(pc_replacement_091)
    delta = feature.diff(2)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00091000).reindex(feature.index)
PC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['pc_replacement_d2_091'] = {'inputs': ['pc_replacement_091'], 'func': pc_replacement_d2_091}


def pc_replacement_d2_092(pc_replacement_092):
    feature = _clean(pc_replacement_092)
    delta = feature.diff(3)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00092000).reindex(feature.index)
PC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['pc_replacement_d2_092'] = {'inputs': ['pc_replacement_092'], 'func': pc_replacement_d2_092}


def pc_replacement_d2_093(pc_replacement_093):
    feature = _clean(pc_replacement_093)
    delta = feature.diff(5)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00093000).reindex(feature.index)
PC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['pc_replacement_d2_093'] = {'inputs': ['pc_replacement_093'], 'func': pc_replacement_d2_093}


def pc_replacement_d2_094(pc_replacement_094):
    feature = _clean(pc_replacement_094)
    delta = feature.diff(8)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00094000).reindex(feature.index)
PC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['pc_replacement_d2_094'] = {'inputs': ['pc_replacement_094'], 'func': pc_replacement_d2_094}


def pc_replacement_d2_095(pc_replacement_095):
    feature = _clean(pc_replacement_095)
    delta = feature.diff(13)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00095000).reindex(feature.index)
PC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['pc_replacement_d2_095'] = {'inputs': ['pc_replacement_095'], 'func': pc_replacement_d2_095}


def pc_replacement_d2_096(pc_replacement_096):
    feature = _clean(pc_replacement_096)
    delta = feature.diff(21)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00096000).reindex(feature.index)
PC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['pc_replacement_d2_096'] = {'inputs': ['pc_replacement_096'], 'func': pc_replacement_d2_096}


def pc_replacement_d2_097(pc_replacement_097):
    feature = _clean(pc_replacement_097)
    delta = feature.diff(34)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00097000).reindex(feature.index)
PC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['pc_replacement_d2_097'] = {'inputs': ['pc_replacement_097'], 'func': pc_replacement_d2_097}


def pc_replacement_d2_098(pc_replacement_098):
    feature = _clean(pc_replacement_098)
    delta = feature.diff(55)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00098000).reindex(feature.index)
PC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['pc_replacement_d2_098'] = {'inputs': ['pc_replacement_098'], 'func': pc_replacement_d2_098}


def pc_replacement_d2_099(pc_replacement_099):
    feature = _clean(pc_replacement_099)
    delta = feature.diff(89)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00099000).reindex(feature.index)
PC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['pc_replacement_d2_099'] = {'inputs': ['pc_replacement_099'], 'func': pc_replacement_d2_099}


def pc_replacement_d2_100(pc_replacement_100):
    feature = _clean(pc_replacement_100)
    delta = feature.diff(1)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00100000).reindex(feature.index)
PC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['pc_replacement_d2_100'] = {'inputs': ['pc_replacement_100'], 'func': pc_replacement_d2_100}


def pc_replacement_d2_101(pc_replacement_101):
    feature = _clean(pc_replacement_101)
    delta = feature.diff(2)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00101000).reindex(feature.index)
PC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['pc_replacement_d2_101'] = {'inputs': ['pc_replacement_101'], 'func': pc_replacement_d2_101}


def pc_replacement_d2_102(pc_replacement_102):
    feature = _clean(pc_replacement_102)
    delta = feature.diff(3)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00102000).reindex(feature.index)
PC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['pc_replacement_d2_102'] = {'inputs': ['pc_replacement_102'], 'func': pc_replacement_d2_102}


def pc_replacement_d2_103(pc_replacement_103):
    feature = _clean(pc_replacement_103)
    delta = feature.diff(5)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00103000).reindex(feature.index)
PC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['pc_replacement_d2_103'] = {'inputs': ['pc_replacement_103'], 'func': pc_replacement_d2_103}


def pc_replacement_d2_104(pc_replacement_104):
    feature = _clean(pc_replacement_104)
    delta = feature.diff(8)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00104000).reindex(feature.index)
PC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['pc_replacement_d2_104'] = {'inputs': ['pc_replacement_104'], 'func': pc_replacement_d2_104}


def pc_replacement_d2_105(pc_replacement_105):
    feature = _clean(pc_replacement_105)
    delta = feature.diff(13)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00105000).reindex(feature.index)
PC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['pc_replacement_d2_105'] = {'inputs': ['pc_replacement_105'], 'func': pc_replacement_d2_105}


def pc_replacement_d2_106(pc_replacement_106):
    feature = _clean(pc_replacement_106)
    delta = feature.diff(21)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00106000).reindex(feature.index)
PC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['pc_replacement_d2_106'] = {'inputs': ['pc_replacement_106'], 'func': pc_replacement_d2_106}


def pc_replacement_d2_107(pc_replacement_107):
    feature = _clean(pc_replacement_107)
    delta = feature.diff(34)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00107000).reindex(feature.index)
PC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['pc_replacement_d2_107'] = {'inputs': ['pc_replacement_107'], 'func': pc_replacement_d2_107}


def pc_replacement_d2_108(pc_replacement_108):
    feature = _clean(pc_replacement_108)
    delta = feature.diff(55)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00108000).reindex(feature.index)
PC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['pc_replacement_d2_108'] = {'inputs': ['pc_replacement_108'], 'func': pc_replacement_d2_108}


def pc_replacement_d2_109(pc_replacement_109):
    feature = _clean(pc_replacement_109)
    delta = feature.diff(89)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00109000).reindex(feature.index)
PC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['pc_replacement_d2_109'] = {'inputs': ['pc_replacement_109'], 'func': pc_replacement_d2_109}


def pc_replacement_d2_110(pc_replacement_110):
    feature = _clean(pc_replacement_110)
    delta = feature.diff(1)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00110000).reindex(feature.index)
PC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['pc_replacement_d2_110'] = {'inputs': ['pc_replacement_110'], 'func': pc_replacement_d2_110}


def pc_replacement_d2_111(pc_replacement_111):
    feature = _clean(pc_replacement_111)
    delta = feature.diff(2)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00111000).reindex(feature.index)
PC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['pc_replacement_d2_111'] = {'inputs': ['pc_replacement_111'], 'func': pc_replacement_d2_111}


def pc_replacement_d2_112(pc_replacement_112):
    feature = _clean(pc_replacement_112)
    delta = feature.diff(3)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00112000).reindex(feature.index)
PC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['pc_replacement_d2_112'] = {'inputs': ['pc_replacement_112'], 'func': pc_replacement_d2_112}


def pc_replacement_d2_113(pc_replacement_113):
    feature = _clean(pc_replacement_113)
    delta = feature.diff(5)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00113000).reindex(feature.index)
PC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['pc_replacement_d2_113'] = {'inputs': ['pc_replacement_113'], 'func': pc_replacement_d2_113}


def pc_replacement_d2_114(pc_replacement_114):
    feature = _clean(pc_replacement_114)
    delta = feature.diff(8)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00114000).reindex(feature.index)
PC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['pc_replacement_d2_114'] = {'inputs': ['pc_replacement_114'], 'func': pc_replacement_d2_114}


def pc_replacement_d2_115(pc_replacement_115):
    feature = _clean(pc_replacement_115)
    delta = feature.diff(13)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00115000).reindex(feature.index)
PC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['pc_replacement_d2_115'] = {'inputs': ['pc_replacement_115'], 'func': pc_replacement_d2_115}


def pc_replacement_d2_116(pc_replacement_116):
    feature = _clean(pc_replacement_116)
    delta = feature.diff(21)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00116000).reindex(feature.index)
PC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['pc_replacement_d2_116'] = {'inputs': ['pc_replacement_116'], 'func': pc_replacement_d2_116}


def pc_replacement_d2_117(pc_replacement_117):
    feature = _clean(pc_replacement_117)
    delta = feature.diff(34)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00117000).reindex(feature.index)
PC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['pc_replacement_d2_117'] = {'inputs': ['pc_replacement_117'], 'func': pc_replacement_d2_117}


def pc_replacement_d2_118(pc_replacement_118):
    feature = _clean(pc_replacement_118)
    delta = feature.diff(55)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00118000).reindex(feature.index)
PC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['pc_replacement_d2_118'] = {'inputs': ['pc_replacement_118'], 'func': pc_replacement_d2_118}


def pc_replacement_d2_119(pc_replacement_119):
    feature = _clean(pc_replacement_119)
    delta = feature.diff(89)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00119000).reindex(feature.index)
PC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['pc_replacement_d2_119'] = {'inputs': ['pc_replacement_119'], 'func': pc_replacement_d2_119}


def pc_replacement_d2_120(pc_replacement_120):
    feature = _clean(pc_replacement_120)
    delta = feature.diff(1)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00120000).reindex(feature.index)
PC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['pc_replacement_d2_120'] = {'inputs': ['pc_replacement_120'], 'func': pc_replacement_d2_120}


def pc_replacement_d2_121(pc_replacement_121):
    feature = _clean(pc_replacement_121)
    delta = feature.diff(2)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00121000).reindex(feature.index)
PC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['pc_replacement_d2_121'] = {'inputs': ['pc_replacement_121'], 'func': pc_replacement_d2_121}


def pc_replacement_d2_122(pc_replacement_122):
    feature = _clean(pc_replacement_122)
    delta = feature.diff(3)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00122000).reindex(feature.index)
PC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['pc_replacement_d2_122'] = {'inputs': ['pc_replacement_122'], 'func': pc_replacement_d2_122}


def pc_replacement_d2_123(pc_replacement_123):
    feature = _clean(pc_replacement_123)
    delta = feature.diff(5)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00123000).reindex(feature.index)
PC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['pc_replacement_d2_123'] = {'inputs': ['pc_replacement_123'], 'func': pc_replacement_d2_123}


def pc_replacement_d2_124(pc_replacement_124):
    feature = _clean(pc_replacement_124)
    delta = feature.diff(8)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00124000).reindex(feature.index)
PC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['pc_replacement_d2_124'] = {'inputs': ['pc_replacement_124'], 'func': pc_replacement_d2_124}


def pc_replacement_d2_125(pc_replacement_125):
    feature = _clean(pc_replacement_125)
    delta = feature.diff(13)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00125000).reindex(feature.index)
PC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['pc_replacement_d2_125'] = {'inputs': ['pc_replacement_125'], 'func': pc_replacement_d2_125}


def pc_replacement_d2_126(pc_replacement_126):
    feature = _clean(pc_replacement_126)
    delta = feature.diff(21)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00126000).reindex(feature.index)
PC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['pc_replacement_d2_126'] = {'inputs': ['pc_replacement_126'], 'func': pc_replacement_d2_126}


def pc_replacement_d2_127(pc_replacement_127):
    feature = _clean(pc_replacement_127)
    delta = feature.diff(34)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00127000).reindex(feature.index)
PC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['pc_replacement_d2_127'] = {'inputs': ['pc_replacement_127'], 'func': pc_replacement_d2_127}


def pc_replacement_d2_128(pc_replacement_128):
    feature = _clean(pc_replacement_128)
    delta = feature.diff(55)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00128000).reindex(feature.index)
PC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['pc_replacement_d2_128'] = {'inputs': ['pc_replacement_128'], 'func': pc_replacement_d2_128}


def pc_replacement_d2_129(pc_replacement_129):
    feature = _clean(pc_replacement_129)
    delta = feature.diff(89)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00129000).reindex(feature.index)
PC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['pc_replacement_d2_129'] = {'inputs': ['pc_replacement_129'], 'func': pc_replacement_d2_129}


def pc_replacement_d2_130(pc_replacement_130):
    feature = _clean(pc_replacement_130)
    delta = feature.diff(1)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00130000).reindex(feature.index)
PC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['pc_replacement_d2_130'] = {'inputs': ['pc_replacement_130'], 'func': pc_replacement_d2_130}


def pc_replacement_d2_131(pc_replacement_131):
    feature = _clean(pc_replacement_131)
    delta = feature.diff(2)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00131000).reindex(feature.index)
PC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['pc_replacement_d2_131'] = {'inputs': ['pc_replacement_131'], 'func': pc_replacement_d2_131}


def pc_replacement_d2_132(pc_replacement_132):
    feature = _clean(pc_replacement_132)
    delta = feature.diff(3)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00132000).reindex(feature.index)
PC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['pc_replacement_d2_132'] = {'inputs': ['pc_replacement_132'], 'func': pc_replacement_d2_132}


def pc_replacement_d2_133(pc_replacement_133):
    feature = _clean(pc_replacement_133)
    delta = feature.diff(5)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00133000).reindex(feature.index)
PC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['pc_replacement_d2_133'] = {'inputs': ['pc_replacement_133'], 'func': pc_replacement_d2_133}


def pc_replacement_d2_134(pc_replacement_134):
    feature = _clean(pc_replacement_134)
    delta = feature.diff(8)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00134000).reindex(feature.index)
PC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['pc_replacement_d2_134'] = {'inputs': ['pc_replacement_134'], 'func': pc_replacement_d2_134}


def pc_replacement_d2_135(pc_replacement_135):
    feature = _clean(pc_replacement_135)
    delta = feature.diff(13)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00135000).reindex(feature.index)
PC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['pc_replacement_d2_135'] = {'inputs': ['pc_replacement_135'], 'func': pc_replacement_d2_135}


def pc_replacement_d2_136(pc_replacement_136):
    feature = _clean(pc_replacement_136)
    delta = feature.diff(21)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00136000).reindex(feature.index)
PC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['pc_replacement_d2_136'] = {'inputs': ['pc_replacement_136'], 'func': pc_replacement_d2_136}


def pc_replacement_d2_137(pc_replacement_137):
    feature = _clean(pc_replacement_137)
    delta = feature.diff(34)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00137000).reindex(feature.index)
PC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['pc_replacement_d2_137'] = {'inputs': ['pc_replacement_137'], 'func': pc_replacement_d2_137}


def pc_replacement_d2_138(pc_replacement_138):
    feature = _clean(pc_replacement_138)
    delta = feature.diff(55)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00138000).reindex(feature.index)
PC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['pc_replacement_d2_138'] = {'inputs': ['pc_replacement_138'], 'func': pc_replacement_d2_138}


def pc_replacement_d2_139(pc_replacement_139):
    feature = _clean(pc_replacement_139)
    delta = feature.diff(89)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00139000).reindex(feature.index)
PC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['pc_replacement_d2_139'] = {'inputs': ['pc_replacement_139'], 'func': pc_replacement_d2_139}


def pc_replacement_d2_140(pc_replacement_140):
    feature = _clean(pc_replacement_140)
    delta = feature.diff(1)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00140000).reindex(feature.index)
PC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['pc_replacement_d2_140'] = {'inputs': ['pc_replacement_140'], 'func': pc_replacement_d2_140}


def pc_replacement_d2_141(pc_replacement_141):
    feature = _clean(pc_replacement_141)
    delta = feature.diff(2)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00141000).reindex(feature.index)
PC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['pc_replacement_d2_141'] = {'inputs': ['pc_replacement_141'], 'func': pc_replacement_d2_141}


def pc_replacement_d2_142(pc_replacement_142):
    feature = _clean(pc_replacement_142)
    delta = feature.diff(3)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00142000).reindex(feature.index)
PC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['pc_replacement_d2_142'] = {'inputs': ['pc_replacement_142'], 'func': pc_replacement_d2_142}


def pc_replacement_d2_143(pc_replacement_143):
    feature = _clean(pc_replacement_143)
    delta = feature.diff(5)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00143000).reindex(feature.index)
PC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['pc_replacement_d2_143'] = {'inputs': ['pc_replacement_143'], 'func': pc_replacement_d2_143}


def pc_replacement_d2_144(pc_replacement_144):
    feature = _clean(pc_replacement_144)
    delta = feature.diff(8)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00144000).reindex(feature.index)
PC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['pc_replacement_d2_144'] = {'inputs': ['pc_replacement_144'], 'func': pc_replacement_d2_144}


def pc_replacement_d2_145(pc_replacement_145):
    feature = _clean(pc_replacement_145)
    delta = feature.diff(13)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00145000).reindex(feature.index)
PC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['pc_replacement_d2_145'] = {'inputs': ['pc_replacement_145'], 'func': pc_replacement_d2_145}


def pc_replacement_d2_146(pc_replacement_146):
    feature = _clean(pc_replacement_146)
    delta = feature.diff(21)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00146000).reindex(feature.index)
PC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['pc_replacement_d2_146'] = {'inputs': ['pc_replacement_146'], 'func': pc_replacement_d2_146}


def pc_replacement_d2_147(pc_replacement_147):
    feature = _clean(pc_replacement_147)
    delta = feature.diff(34)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00147000).reindex(feature.index)
PC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['pc_replacement_d2_147'] = {'inputs': ['pc_replacement_147'], 'func': pc_replacement_d2_147}


def pc_replacement_d2_148(pc_replacement_148):
    feature = _clean(pc_replacement_148)
    delta = feature.diff(55)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00148000).reindex(feature.index)
PC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['pc_replacement_d2_148'] = {'inputs': ['pc_replacement_148'], 'func': pc_replacement_d2_148}


def pc_replacement_d2_149(pc_replacement_149):
    feature = _clean(pc_replacement_149)
    delta = feature.diff(89)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00149000).reindex(feature.index)
PC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['pc_replacement_d2_149'] = {'inputs': ['pc_replacement_149'], 'func': pc_replacement_d2_149}


def pc_replacement_d2_150(pc_replacement_150):
    feature = _clean(pc_replacement_150)
    delta = feature.diff(1)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00150000).reindex(feature.index)
PC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['pc_replacement_d2_150'] = {'inputs': ['pc_replacement_150'], 'func': pc_replacement_d2_150}


def pc_replacement_d2_151(pc_replacement_151):
    feature = _clean(pc_replacement_151)
    delta = feature.diff(2)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00151000).reindex(feature.index)
PC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['pc_replacement_d2_151'] = {'inputs': ['pc_replacement_151'], 'func': pc_replacement_d2_151}


def pc_replacement_d2_152(pc_replacement_152):
    feature = _clean(pc_replacement_152)
    delta = feature.diff(3)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00152000).reindex(feature.index)
PC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['pc_replacement_d2_152'] = {'inputs': ['pc_replacement_152'], 'func': pc_replacement_d2_152}


def pc_replacement_d2_153(pc_replacement_153):
    feature = _clean(pc_replacement_153)
    delta = feature.diff(5)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00153000).reindex(feature.index)
PC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['pc_replacement_d2_153'] = {'inputs': ['pc_replacement_153'], 'func': pc_replacement_d2_153}


def pc_replacement_d2_154(pc_replacement_154):
    feature = _clean(pc_replacement_154)
    delta = feature.diff(8)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00154000).reindex(feature.index)
PC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['pc_replacement_d2_154'] = {'inputs': ['pc_replacement_154'], 'func': pc_replacement_d2_154}


def pc_replacement_d2_155(pc_replacement_155):
    feature = _clean(pc_replacement_155)
    delta = feature.diff(13)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00155000).reindex(feature.index)
PC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['pc_replacement_d2_155'] = {'inputs': ['pc_replacement_155'], 'func': pc_replacement_d2_155}


def pc_replacement_d2_156(pc_replacement_156):
    feature = _clean(pc_replacement_156)
    delta = feature.diff(21)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00156000).reindex(feature.index)
PC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['pc_replacement_d2_156'] = {'inputs': ['pc_replacement_156'], 'func': pc_replacement_d2_156}


def pc_replacement_d2_157(pc_replacement_157):
    feature = _clean(pc_replacement_157)
    delta = feature.diff(34)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00157000).reindex(feature.index)
PC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['pc_replacement_d2_157'] = {'inputs': ['pc_replacement_157'], 'func': pc_replacement_d2_157}


def pc_replacement_d2_158(pc_replacement_158):
    feature = _clean(pc_replacement_158)
    delta = feature.diff(55)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00158000).reindex(feature.index)
PC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['pc_replacement_d2_158'] = {'inputs': ['pc_replacement_158'], 'func': pc_replacement_d2_158}


def pc_replacement_d2_159(pc_replacement_159):
    feature = _clean(pc_replacement_159)
    delta = feature.diff(89)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00159000).reindex(feature.index)
PC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['pc_replacement_d2_159'] = {'inputs': ['pc_replacement_159'], 'func': pc_replacement_d2_159}


def pc_replacement_d2_160(pc_replacement_160):
    feature = _clean(pc_replacement_160)
    delta = feature.diff(1)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00160000).reindex(feature.index)
PC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['pc_replacement_d2_160'] = {'inputs': ['pc_replacement_160'], 'func': pc_replacement_d2_160}


def pc_replacement_d2_161(pc_replacement_161):
    feature = _clean(pc_replacement_161)
    delta = feature.diff(2)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00161000).reindex(feature.index)
PC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['pc_replacement_d2_161'] = {'inputs': ['pc_replacement_161'], 'func': pc_replacement_d2_161}


def pc_replacement_d2_162(pc_replacement_162):
    feature = _clean(pc_replacement_162)
    delta = feature.diff(3)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00162000).reindex(feature.index)
PC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['pc_replacement_d2_162'] = {'inputs': ['pc_replacement_162'], 'func': pc_replacement_d2_162}


def pc_replacement_d2_163(pc_replacement_163):
    feature = _clean(pc_replacement_163)
    delta = feature.diff(5)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00163000).reindex(feature.index)
PC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['pc_replacement_d2_163'] = {'inputs': ['pc_replacement_163'], 'func': pc_replacement_d2_163}


def pc_replacement_d2_164(pc_replacement_164):
    feature = _clean(pc_replacement_164)
    delta = feature.diff(8)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00164000).reindex(feature.index)
PC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['pc_replacement_d2_164'] = {'inputs': ['pc_replacement_164'], 'func': pc_replacement_d2_164}


def pc_replacement_d2_165(pc_replacement_165):
    feature = _clean(pc_replacement_165)
    delta = feature.diff(13)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00165000).reindex(feature.index)
PC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['pc_replacement_d2_165'] = {'inputs': ['pc_replacement_165'], 'func': pc_replacement_d2_165}


def pc_replacement_d2_166(pc_replacement_166):
    feature = _clean(pc_replacement_166)
    delta = feature.diff(21)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00166000).reindex(feature.index)
PC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['pc_replacement_d2_166'] = {'inputs': ['pc_replacement_166'], 'func': pc_replacement_d2_166}


def pc_replacement_d2_167(pc_replacement_167):
    feature = _clean(pc_replacement_167)
    delta = feature.diff(34)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00167000).reindex(feature.index)
PC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['pc_replacement_d2_167'] = {'inputs': ['pc_replacement_167'], 'func': pc_replacement_d2_167}


def pc_replacement_d2_168(pc_replacement_168):
    feature = _clean(pc_replacement_168)
    delta = feature.diff(55)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00168000).reindex(feature.index)
PC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['pc_replacement_d2_168'] = {'inputs': ['pc_replacement_168'], 'func': pc_replacement_d2_168}


def pc_replacement_d2_169(pc_replacement_169):
    feature = _clean(pc_replacement_169)
    delta = feature.diff(89)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00169000).reindex(feature.index)
PC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['pc_replacement_d2_169'] = {'inputs': ['pc_replacement_169'], 'func': pc_replacement_d2_169}


def pc_replacement_d2_170(pc_replacement_170):
    feature = _clean(pc_replacement_170)
    delta = feature.diff(1)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00170000).reindex(feature.index)
PC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['pc_replacement_d2_170'] = {'inputs': ['pc_replacement_170'], 'func': pc_replacement_d2_170}


# Base-universe derivative extensions for repaired first-base features.
PCMP_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY = {}


def _base_universe_d2(feature, idx):
    feature = _clean(feature) if '_clean' in globals() else _s(feature).replace([np.inf, -np.inf], np.nan)
    windows = [1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    lag = windows[idx % len(windows)]
    smooth = windows[(idx * 3 + 1) % len(windows)]
    delta = feature.diff(lag)
    local = feature - feature.rolling(max(3, smooth), min_periods=2).mean()
    out = delta + local.fillna(0.0) * (0.00037 * ((idx % 17) + 1))
    return out.replace([np.inf, -np.inf], np.nan).reindex(feature.index)


def pcmp_base_universe_d2_001_pcmp_002_zero_volume_frequency_10_002(pcmp_002_zero_volume_frequency_10_002):
    return _base_universe_d2(pcmp_002_zero_volume_frequency_10_002, 1)
PCMP_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['pcmp_base_universe_d2_001_pcmp_002_zero_volume_frequency_10_002'] = {'inputs': ['pcmp_002_zero_volume_frequency_10_002'], 'func': pcmp_base_universe_d2_001_pcmp_002_zero_volume_frequency_10_002}


def pcmp_base_universe_d2_002_pcmp_003_spread_proxy_21_003(pcmp_003_spread_proxy_21_003):
    return _base_universe_d2(pcmp_003_spread_proxy_21_003, 2)
PCMP_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['pcmp_base_universe_d2_002_pcmp_003_spread_proxy_21_003'] = {'inputs': ['pcmp_003_spread_proxy_21_003'], 'func': pcmp_base_universe_d2_002_pcmp_003_spread_proxy_21_003}


def pcmp_base_universe_d2_003_pcmp_004_trading_intensity_42_004(pcmp_004_trading_intensity_42_004):
    return _base_universe_d2(pcmp_004_trading_intensity_42_004, 3)
PCMP_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['pcmp_base_universe_d2_003_pcmp_004_trading_intensity_42_004'] = {'inputs': ['pcmp_004_trading_intensity_42_004'], 'func': pcmp_base_universe_d2_003_pcmp_004_trading_intensity_42_004}


def pcmp_base_universe_d2_004_pcmp_006_price_level_distress_84_006(pcmp_006_price_level_distress_84_006):
    return _base_universe_d2(pcmp_006_price_level_distress_84_006, 4)
PCMP_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['pcmp_base_universe_d2_004_pcmp_006_price_level_distress_84_006'] = {'inputs': ['pcmp_006_price_level_distress_84_006'], 'func': pcmp_base_universe_d2_004_pcmp_006_price_level_distress_84_006}


def pcmp_base_universe_d2_005_pcmp_008_zero_volume_frequency_189_008(pcmp_008_zero_volume_frequency_189_008):
    return _base_universe_d2(pcmp_008_zero_volume_frequency_189_008, 5)
PCMP_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['pcmp_base_universe_d2_005_pcmp_008_zero_volume_frequency_189_008'] = {'inputs': ['pcmp_008_zero_volume_frequency_189_008'], 'func': pcmp_base_universe_d2_005_pcmp_008_zero_volume_frequency_189_008}


def pcmp_base_universe_d2_006_pcmp_009_spread_proxy_252_009(pcmp_009_spread_proxy_252_009):
    return _base_universe_d2(pcmp_009_spread_proxy_252_009, 6)
PCMP_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['pcmp_base_universe_d2_006_pcmp_009_spread_proxy_252_009'] = {'inputs': ['pcmp_009_spread_proxy_252_009'], 'func': pcmp_base_universe_d2_006_pcmp_009_spread_proxy_252_009}


def pcmp_base_universe_d2_007_pcmp_010_trading_intensity_378_010(pcmp_010_trading_intensity_378_010):
    return _base_universe_d2(pcmp_010_trading_intensity_378_010, 7)
PCMP_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['pcmp_base_universe_d2_007_pcmp_010_trading_intensity_378_010'] = {'inputs': ['pcmp_010_trading_intensity_378_010'], 'func': pcmp_base_universe_d2_007_pcmp_010_trading_intensity_378_010}


def pcmp_base_universe_d2_008_pcmp_012_price_level_distress_756_012(pcmp_012_price_level_distress_756_012):
    return _base_universe_d2(pcmp_012_price_level_distress_756_012, 8)
PCMP_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['pcmp_base_universe_d2_008_pcmp_012_price_level_distress_756_012'] = {'inputs': ['pcmp_012_price_level_distress_756_012'], 'func': pcmp_base_universe_d2_008_pcmp_012_price_level_distress_756_012}


def pcmp_base_universe_d2_009_pcmp_014_zero_volume_frequency_1260_014(pcmp_014_zero_volume_frequency_1260_014):
    return _base_universe_d2(pcmp_014_zero_volume_frequency_1260_014, 9)
PCMP_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['pcmp_base_universe_d2_009_pcmp_014_zero_volume_frequency_1260_014'] = {'inputs': ['pcmp_014_zero_volume_frequency_1260_014'], 'func': pcmp_base_universe_d2_009_pcmp_014_zero_volume_frequency_1260_014}


def pcmp_base_universe_d2_010_pcmp_015_spread_proxy_1512_015(pcmp_015_spread_proxy_1512_015):
    return _base_universe_d2(pcmp_015_spread_proxy_1512_015, 10)
PCMP_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['pcmp_base_universe_d2_010_pcmp_015_spread_proxy_1512_015'] = {'inputs': ['pcmp_015_spread_proxy_1512_015'], 'func': pcmp_base_universe_d2_010_pcmp_015_spread_proxy_1512_015}


def pcmp_base_universe_d2_011_pcmp_016_trading_intensity_5_016(pcmp_016_trading_intensity_5_016):
    return _base_universe_d2(pcmp_016_trading_intensity_5_016, 11)
PCMP_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['pcmp_base_universe_d2_011_pcmp_016_trading_intensity_5_016'] = {'inputs': ['pcmp_016_trading_intensity_5_016'], 'func': pcmp_base_universe_d2_011_pcmp_016_trading_intensity_5_016}


def pcmp_base_universe_d2_012_pcmp_018_price_level_distress_21_018(pcmp_018_price_level_distress_21_018):
    return _base_universe_d2(pcmp_018_price_level_distress_21_018, 12)
PCMP_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['pcmp_base_universe_d2_012_pcmp_018_price_level_distress_21_018'] = {'inputs': ['pcmp_018_price_level_distress_21_018'], 'func': pcmp_base_universe_d2_012_pcmp_018_price_level_distress_21_018}


def pcmp_base_universe_d2_013_pcmp_020_zero_volume_frequency_63_020(pcmp_020_zero_volume_frequency_63_020):
    return _base_universe_d2(pcmp_020_zero_volume_frequency_63_020, 13)
PCMP_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['pcmp_base_universe_d2_013_pcmp_020_zero_volume_frequency_63_020'] = {'inputs': ['pcmp_020_zero_volume_frequency_63_020'], 'func': pcmp_base_universe_d2_013_pcmp_020_zero_volume_frequency_63_020}


def pcmp_base_universe_d2_014_pcmp_021_spread_proxy_84_021(pcmp_021_spread_proxy_84_021):
    return _base_universe_d2(pcmp_021_spread_proxy_84_021, 14)
PCMP_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['pcmp_base_universe_d2_014_pcmp_021_spread_proxy_84_021'] = {'inputs': ['pcmp_021_spread_proxy_84_021'], 'func': pcmp_base_universe_d2_014_pcmp_021_spread_proxy_84_021}


def pcmp_base_universe_d2_015_pcmp_022_trading_intensity_126_022(pcmp_022_trading_intensity_126_022):
    return _base_universe_d2(pcmp_022_trading_intensity_126_022, 15)
PCMP_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['pcmp_base_universe_d2_015_pcmp_022_trading_intensity_126_022'] = {'inputs': ['pcmp_022_trading_intensity_126_022'], 'func': pcmp_base_universe_d2_015_pcmp_022_trading_intensity_126_022}


def pcmp_base_universe_d2_016_pcmp_024_price_level_distress_252_024(pcmp_024_price_level_distress_252_024):
    return _base_universe_d2(pcmp_024_price_level_distress_252_024, 16)
PCMP_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['pcmp_base_universe_d2_016_pcmp_024_price_level_distress_252_024'] = {'inputs': ['pcmp_024_price_level_distress_252_024'], 'func': pcmp_base_universe_d2_016_pcmp_024_price_level_distress_252_024}


def pcmp_base_universe_d2_017_pcmp_026_zero_volume_frequency_504_026(pcmp_026_zero_volume_frequency_504_026):
    return _base_universe_d2(pcmp_026_zero_volume_frequency_504_026, 17)
PCMP_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['pcmp_base_universe_d2_017_pcmp_026_zero_volume_frequency_504_026'] = {'inputs': ['pcmp_026_zero_volume_frequency_504_026'], 'func': pcmp_base_universe_d2_017_pcmp_026_zero_volume_frequency_504_026}


def pcmp_base_universe_d2_018_pcmp_027_spread_proxy_756_027(pcmp_027_spread_proxy_756_027):
    return _base_universe_d2(pcmp_027_spread_proxy_756_027, 18)
PCMP_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['pcmp_base_universe_d2_018_pcmp_027_spread_proxy_756_027'] = {'inputs': ['pcmp_027_spread_proxy_756_027'], 'func': pcmp_base_universe_d2_018_pcmp_027_spread_proxy_756_027}


def pcmp_base_universe_d2_019_pcmp_028_trading_intensity_1008_028(pcmp_028_trading_intensity_1008_028):
    return _base_universe_d2(pcmp_028_trading_intensity_1008_028, 19)
PCMP_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['pcmp_base_universe_d2_019_pcmp_028_trading_intensity_1008_028'] = {'inputs': ['pcmp_028_trading_intensity_1008_028'], 'func': pcmp_base_universe_d2_019_pcmp_028_trading_intensity_1008_028}


def pcmp_base_universe_d2_020_pcmp_030_price_level_distress_1512_030(pcmp_030_price_level_distress_1512_030):
    return _base_universe_d2(pcmp_030_price_level_distress_1512_030, 20)
PCMP_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['pcmp_base_universe_d2_020_pcmp_030_price_level_distress_1512_030'] = {'inputs': ['pcmp_030_price_level_distress_1512_030'], 'func': pcmp_base_universe_d2_020_pcmp_030_price_level_distress_1512_030}


def pcmp_base_universe_d2_021_pcmp_basefill_001(pcmp_basefill_001):
    return _base_universe_d2(pcmp_basefill_001, 21)
PCMP_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['pcmp_base_universe_d2_021_pcmp_basefill_001'] = {'inputs': ['pcmp_basefill_001'], 'func': pcmp_base_universe_d2_021_pcmp_basefill_001}


def pcmp_base_universe_d2_022_pcmp_basefill_005(pcmp_basefill_005):
    return _base_universe_d2(pcmp_basefill_005, 22)
PCMP_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['pcmp_base_universe_d2_022_pcmp_basefill_005'] = {'inputs': ['pcmp_basefill_005'], 'func': pcmp_base_universe_d2_022_pcmp_basefill_005}


def pcmp_base_universe_d2_023_pcmp_basefill_007(pcmp_basefill_007):
    return _base_universe_d2(pcmp_basefill_007, 23)
PCMP_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['pcmp_base_universe_d2_023_pcmp_basefill_007'] = {'inputs': ['pcmp_basefill_007'], 'func': pcmp_base_universe_d2_023_pcmp_basefill_007}


def pcmp_base_universe_d2_024_pcmp_basefill_011(pcmp_basefill_011):
    return _base_universe_d2(pcmp_basefill_011, 24)
PCMP_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['pcmp_base_universe_d2_024_pcmp_basefill_011'] = {'inputs': ['pcmp_basefill_011'], 'func': pcmp_base_universe_d2_024_pcmp_basefill_011}


def pcmp_base_universe_d2_025_pcmp_basefill_013(pcmp_basefill_013):
    return _base_universe_d2(pcmp_basefill_013, 25)
PCMP_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['pcmp_base_universe_d2_025_pcmp_basefill_013'] = {'inputs': ['pcmp_basefill_013'], 'func': pcmp_base_universe_d2_025_pcmp_basefill_013}


def pcmp_base_universe_d2_026_pcmp_basefill_017(pcmp_basefill_017):
    return _base_universe_d2(pcmp_basefill_017, 26)
PCMP_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['pcmp_base_universe_d2_026_pcmp_basefill_017'] = {'inputs': ['pcmp_basefill_017'], 'func': pcmp_base_universe_d2_026_pcmp_basefill_017}


def pcmp_base_universe_d2_027_pcmp_basefill_019(pcmp_basefill_019):
    return _base_universe_d2(pcmp_basefill_019, 27)
PCMP_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['pcmp_base_universe_d2_027_pcmp_basefill_019'] = {'inputs': ['pcmp_basefill_019'], 'func': pcmp_base_universe_d2_027_pcmp_basefill_019}


def pcmp_base_universe_d2_028_pcmp_basefill_023(pcmp_basefill_023):
    return _base_universe_d2(pcmp_basefill_023, 28)
PCMP_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['pcmp_base_universe_d2_028_pcmp_basefill_023'] = {'inputs': ['pcmp_basefill_023'], 'func': pcmp_base_universe_d2_028_pcmp_basefill_023}


def pcmp_base_universe_d2_029_pcmp_basefill_025(pcmp_basefill_025):
    return _base_universe_d2(pcmp_basefill_025, 29)
PCMP_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['pcmp_base_universe_d2_029_pcmp_basefill_025'] = {'inputs': ['pcmp_basefill_025'], 'func': pcmp_base_universe_d2_029_pcmp_basefill_025}


def pcmp_base_universe_d2_030_pcmp_basefill_029(pcmp_basefill_029):
    return _base_universe_d2(pcmp_basefill_029, 30)
PCMP_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['pcmp_base_universe_d2_030_pcmp_basefill_029'] = {'inputs': ['pcmp_basefill_029'], 'func': pcmp_base_universe_d2_030_pcmp_basefill_029}


def pcmp_base_universe_d2_031_pcmp_basefill_031(pcmp_basefill_031):
    return _base_universe_d2(pcmp_basefill_031, 31)
PCMP_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['pcmp_base_universe_d2_031_pcmp_basefill_031'] = {'inputs': ['pcmp_basefill_031'], 'func': pcmp_base_universe_d2_031_pcmp_basefill_031}


def pcmp_base_universe_d2_032_pcmp_basefill_032(pcmp_basefill_032):
    return _base_universe_d2(pcmp_basefill_032, 32)
PCMP_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['pcmp_base_universe_d2_032_pcmp_basefill_032'] = {'inputs': ['pcmp_basefill_032'], 'func': pcmp_base_universe_d2_032_pcmp_basefill_032}


def pcmp_base_universe_d2_033_pcmp_basefill_033(pcmp_basefill_033):
    return _base_universe_d2(pcmp_basefill_033, 33)
PCMP_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['pcmp_base_universe_d2_033_pcmp_basefill_033'] = {'inputs': ['pcmp_basefill_033'], 'func': pcmp_base_universe_d2_033_pcmp_basefill_033}


def pcmp_base_universe_d2_034_pcmp_basefill_034(pcmp_basefill_034):
    return _base_universe_d2(pcmp_basefill_034, 34)
PCMP_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['pcmp_base_universe_d2_034_pcmp_basefill_034'] = {'inputs': ['pcmp_basefill_034'], 'func': pcmp_base_universe_d2_034_pcmp_basefill_034}


def pcmp_base_universe_d2_035_pcmp_basefill_035(pcmp_basefill_035):
    return _base_universe_d2(pcmp_basefill_035, 35)
PCMP_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['pcmp_base_universe_d2_035_pcmp_basefill_035'] = {'inputs': ['pcmp_basefill_035'], 'func': pcmp_base_universe_d2_035_pcmp_basefill_035}


def pcmp_base_universe_d2_036_pcmp_basefill_036(pcmp_basefill_036):
    return _base_universe_d2(pcmp_basefill_036, 36)
PCMP_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['pcmp_base_universe_d2_036_pcmp_basefill_036'] = {'inputs': ['pcmp_basefill_036'], 'func': pcmp_base_universe_d2_036_pcmp_basefill_036}


def pcmp_base_universe_d2_037_pcmp_basefill_037(pcmp_basefill_037):
    return _base_universe_d2(pcmp_basefill_037, 37)
PCMP_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['pcmp_base_universe_d2_037_pcmp_basefill_037'] = {'inputs': ['pcmp_basefill_037'], 'func': pcmp_base_universe_d2_037_pcmp_basefill_037}


def pcmp_base_universe_d2_038_pcmp_basefill_038(pcmp_basefill_038):
    return _base_universe_d2(pcmp_basefill_038, 38)
PCMP_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['pcmp_base_universe_d2_038_pcmp_basefill_038'] = {'inputs': ['pcmp_basefill_038'], 'func': pcmp_base_universe_d2_038_pcmp_basefill_038}


def pcmp_base_universe_d2_039_pcmp_basefill_039(pcmp_basefill_039):
    return _base_universe_d2(pcmp_basefill_039, 39)
PCMP_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['pcmp_base_universe_d2_039_pcmp_basefill_039'] = {'inputs': ['pcmp_basefill_039'], 'func': pcmp_base_universe_d2_039_pcmp_basefill_039}


def pcmp_base_universe_d2_040_pcmp_basefill_040(pcmp_basefill_040):
    return _base_universe_d2(pcmp_basefill_040, 40)
PCMP_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['pcmp_base_universe_d2_040_pcmp_basefill_040'] = {'inputs': ['pcmp_basefill_040'], 'func': pcmp_base_universe_d2_040_pcmp_basefill_040}


def pcmp_base_universe_d2_041_pcmp_basefill_041(pcmp_basefill_041):
    return _base_universe_d2(pcmp_basefill_041, 41)
PCMP_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['pcmp_base_universe_d2_041_pcmp_basefill_041'] = {'inputs': ['pcmp_basefill_041'], 'func': pcmp_base_universe_d2_041_pcmp_basefill_041}


def pcmp_base_universe_d2_042_pcmp_basefill_042(pcmp_basefill_042):
    return _base_universe_d2(pcmp_basefill_042, 42)
PCMP_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['pcmp_base_universe_d2_042_pcmp_basefill_042'] = {'inputs': ['pcmp_basefill_042'], 'func': pcmp_base_universe_d2_042_pcmp_basefill_042}


def pcmp_base_universe_d2_043_pcmp_basefill_043(pcmp_basefill_043):
    return _base_universe_d2(pcmp_basefill_043, 43)
PCMP_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['pcmp_base_universe_d2_043_pcmp_basefill_043'] = {'inputs': ['pcmp_basefill_043'], 'func': pcmp_base_universe_d2_043_pcmp_basefill_043}


def pcmp_base_universe_d2_044_pcmp_basefill_044(pcmp_basefill_044):
    return _base_universe_d2(pcmp_basefill_044, 44)
PCMP_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['pcmp_base_universe_d2_044_pcmp_basefill_044'] = {'inputs': ['pcmp_basefill_044'], 'func': pcmp_base_universe_d2_044_pcmp_basefill_044}


def pcmp_base_universe_d2_045_pcmp_basefill_045(pcmp_basefill_045):
    return _base_universe_d2(pcmp_basefill_045, 45)
PCMP_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['pcmp_base_universe_d2_045_pcmp_basefill_045'] = {'inputs': ['pcmp_basefill_045'], 'func': pcmp_base_universe_d2_045_pcmp_basefill_045}


def pcmp_base_universe_d2_046_pcmp_basefill_046(pcmp_basefill_046):
    return _base_universe_d2(pcmp_basefill_046, 46)
PCMP_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['pcmp_base_universe_d2_046_pcmp_basefill_046'] = {'inputs': ['pcmp_basefill_046'], 'func': pcmp_base_universe_d2_046_pcmp_basefill_046}


def pcmp_base_universe_d2_047_pcmp_basefill_047(pcmp_basefill_047):
    return _base_universe_d2(pcmp_basefill_047, 47)
PCMP_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['pcmp_base_universe_d2_047_pcmp_basefill_047'] = {'inputs': ['pcmp_basefill_047'], 'func': pcmp_base_universe_d2_047_pcmp_basefill_047}


def pcmp_base_universe_d2_048_pcmp_basefill_048(pcmp_basefill_048):
    return _base_universe_d2(pcmp_basefill_048, 48)
PCMP_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['pcmp_base_universe_d2_048_pcmp_basefill_048'] = {'inputs': ['pcmp_basefill_048'], 'func': pcmp_base_universe_d2_048_pcmp_basefill_048}


def pcmp_base_universe_d2_049_pcmp_basefill_049(pcmp_basefill_049):
    return _base_universe_d2(pcmp_basefill_049, 49)
PCMP_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['pcmp_base_universe_d2_049_pcmp_basefill_049'] = {'inputs': ['pcmp_basefill_049'], 'func': pcmp_base_universe_d2_049_pcmp_basefill_049}


def pcmp_base_universe_d2_050_pcmp_basefill_050(pcmp_basefill_050):
    return _base_universe_d2(pcmp_basefill_050, 50)
PCMP_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['pcmp_base_universe_d2_050_pcmp_basefill_050'] = {'inputs': ['pcmp_basefill_050'], 'func': pcmp_base_universe_d2_050_pcmp_basefill_050}


def pcmp_base_universe_d2_051_pcmp_basefill_051(pcmp_basefill_051):
    return _base_universe_d2(pcmp_basefill_051, 51)
PCMP_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['pcmp_base_universe_d2_051_pcmp_basefill_051'] = {'inputs': ['pcmp_basefill_051'], 'func': pcmp_base_universe_d2_051_pcmp_basefill_051}


def pcmp_base_universe_d2_052_pcmp_basefill_052(pcmp_basefill_052):
    return _base_universe_d2(pcmp_basefill_052, 52)
PCMP_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['pcmp_base_universe_d2_052_pcmp_basefill_052'] = {'inputs': ['pcmp_basefill_052'], 'func': pcmp_base_universe_d2_052_pcmp_basefill_052}


def pcmp_base_universe_d2_053_pcmp_basefill_053(pcmp_basefill_053):
    return _base_universe_d2(pcmp_basefill_053, 53)
PCMP_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['pcmp_base_universe_d2_053_pcmp_basefill_053'] = {'inputs': ['pcmp_basefill_053'], 'func': pcmp_base_universe_d2_053_pcmp_basefill_053}


def pcmp_base_universe_d2_054_pcmp_basefill_054(pcmp_basefill_054):
    return _base_universe_d2(pcmp_basefill_054, 54)
PCMP_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['pcmp_base_universe_d2_054_pcmp_basefill_054'] = {'inputs': ['pcmp_basefill_054'], 'func': pcmp_base_universe_d2_054_pcmp_basefill_054}


def pcmp_base_universe_d2_055_pcmp_basefill_055(pcmp_basefill_055):
    return _base_universe_d2(pcmp_basefill_055, 55)
PCMP_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['pcmp_base_universe_d2_055_pcmp_basefill_055'] = {'inputs': ['pcmp_basefill_055'], 'func': pcmp_base_universe_d2_055_pcmp_basefill_055}


def pcmp_base_universe_d2_056_pcmp_basefill_056(pcmp_basefill_056):
    return _base_universe_d2(pcmp_basefill_056, 56)
PCMP_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['pcmp_base_universe_d2_056_pcmp_basefill_056'] = {'inputs': ['pcmp_basefill_056'], 'func': pcmp_base_universe_d2_056_pcmp_basefill_056}


def pcmp_base_universe_d2_057_pcmp_basefill_057(pcmp_basefill_057):
    return _base_universe_d2(pcmp_basefill_057, 57)
PCMP_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['pcmp_base_universe_d2_057_pcmp_basefill_057'] = {'inputs': ['pcmp_basefill_057'], 'func': pcmp_base_universe_d2_057_pcmp_basefill_057}


def pcmp_base_universe_d2_058_pcmp_basefill_058(pcmp_basefill_058):
    return _base_universe_d2(pcmp_basefill_058, 58)
PCMP_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['pcmp_base_universe_d2_058_pcmp_basefill_058'] = {'inputs': ['pcmp_basefill_058'], 'func': pcmp_base_universe_d2_058_pcmp_basefill_058}


def pcmp_base_universe_d2_059_pcmp_basefill_059(pcmp_basefill_059):
    return _base_universe_d2(pcmp_basefill_059, 59)
PCMP_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['pcmp_base_universe_d2_059_pcmp_basefill_059'] = {'inputs': ['pcmp_basefill_059'], 'func': pcmp_base_universe_d2_059_pcmp_basefill_059}


def pcmp_base_universe_d2_060_pcmp_basefill_060(pcmp_basefill_060):
    return _base_universe_d2(pcmp_basefill_060, 60)
PCMP_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['pcmp_base_universe_d2_060_pcmp_basefill_060'] = {'inputs': ['pcmp_basefill_060'], 'func': pcmp_base_universe_d2_060_pcmp_basefill_060}


def pcmp_base_universe_d2_061_pcmp_basefill_061(pcmp_basefill_061):
    return _base_universe_d2(pcmp_basefill_061, 61)
PCMP_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['pcmp_base_universe_d2_061_pcmp_basefill_061'] = {'inputs': ['pcmp_basefill_061'], 'func': pcmp_base_universe_d2_061_pcmp_basefill_061}


def pcmp_base_universe_d2_062_pcmp_basefill_062(pcmp_basefill_062):
    return _base_universe_d2(pcmp_basefill_062, 62)
PCMP_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['pcmp_base_universe_d2_062_pcmp_basefill_062'] = {'inputs': ['pcmp_basefill_062'], 'func': pcmp_base_universe_d2_062_pcmp_basefill_062}


def pcmp_base_universe_d2_063_pcmp_basefill_063(pcmp_basefill_063):
    return _base_universe_d2(pcmp_basefill_063, 63)
PCMP_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['pcmp_base_universe_d2_063_pcmp_basefill_063'] = {'inputs': ['pcmp_basefill_063'], 'func': pcmp_base_universe_d2_063_pcmp_basefill_063}


def pcmp_base_universe_d2_064_pcmp_basefill_064(pcmp_basefill_064):
    return _base_universe_d2(pcmp_basefill_064, 64)
PCMP_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['pcmp_base_universe_d2_064_pcmp_basefill_064'] = {'inputs': ['pcmp_basefill_064'], 'func': pcmp_base_universe_d2_064_pcmp_basefill_064}


def pcmp_base_universe_d2_065_pcmp_basefill_065(pcmp_basefill_065):
    return _base_universe_d2(pcmp_basefill_065, 65)
PCMP_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['pcmp_base_universe_d2_065_pcmp_basefill_065'] = {'inputs': ['pcmp_basefill_065'], 'func': pcmp_base_universe_d2_065_pcmp_basefill_065}


def pcmp_base_universe_d2_066_pcmp_basefill_066(pcmp_basefill_066):
    return _base_universe_d2(pcmp_basefill_066, 66)
PCMP_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['pcmp_base_universe_d2_066_pcmp_basefill_066'] = {'inputs': ['pcmp_basefill_066'], 'func': pcmp_base_universe_d2_066_pcmp_basefill_066}


def pcmp_base_universe_d2_067_pcmp_basefill_067(pcmp_basefill_067):
    return _base_universe_d2(pcmp_basefill_067, 67)
PCMP_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['pcmp_base_universe_d2_067_pcmp_basefill_067'] = {'inputs': ['pcmp_basefill_067'], 'func': pcmp_base_universe_d2_067_pcmp_basefill_067}


def pcmp_base_universe_d2_068_pcmp_basefill_068(pcmp_basefill_068):
    return _base_universe_d2(pcmp_basefill_068, 68)
PCMP_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['pcmp_base_universe_d2_068_pcmp_basefill_068'] = {'inputs': ['pcmp_basefill_068'], 'func': pcmp_base_universe_d2_068_pcmp_basefill_068}


def pcmp_base_universe_d2_069_pcmp_basefill_069(pcmp_basefill_069):
    return _base_universe_d2(pcmp_basefill_069, 69)
PCMP_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['pcmp_base_universe_d2_069_pcmp_basefill_069'] = {'inputs': ['pcmp_basefill_069'], 'func': pcmp_base_universe_d2_069_pcmp_basefill_069}


def pcmp_base_universe_d2_070_pcmp_basefill_070(pcmp_basefill_070):
    return _base_universe_d2(pcmp_basefill_070, 70)
PCMP_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['pcmp_base_universe_d2_070_pcmp_basefill_070'] = {'inputs': ['pcmp_basefill_070'], 'func': pcmp_base_universe_d2_070_pcmp_basefill_070}


def pcmp_base_universe_d2_071_pcmp_basefill_071(pcmp_basefill_071):
    return _base_universe_d2(pcmp_basefill_071, 71)
PCMP_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['pcmp_base_universe_d2_071_pcmp_basefill_071'] = {'inputs': ['pcmp_basefill_071'], 'func': pcmp_base_universe_d2_071_pcmp_basefill_071}


def pcmp_base_universe_d2_072_pcmp_basefill_072(pcmp_basefill_072):
    return _base_universe_d2(pcmp_basefill_072, 72)
PCMP_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['pcmp_base_universe_d2_072_pcmp_basefill_072'] = {'inputs': ['pcmp_basefill_072'], 'func': pcmp_base_universe_d2_072_pcmp_basefill_072}


def pcmp_base_universe_d2_073_pcmp_basefill_073(pcmp_basefill_073):
    return _base_universe_d2(pcmp_basefill_073, 73)
PCMP_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['pcmp_base_universe_d2_073_pcmp_basefill_073'] = {'inputs': ['pcmp_basefill_073'], 'func': pcmp_base_universe_d2_073_pcmp_basefill_073}


def pcmp_base_universe_d2_074_pcmp_basefill_074(pcmp_basefill_074):
    return _base_universe_d2(pcmp_basefill_074, 74)
PCMP_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['pcmp_base_universe_d2_074_pcmp_basefill_074'] = {'inputs': ['pcmp_basefill_074'], 'func': pcmp_base_universe_d2_074_pcmp_basefill_074}


def pcmp_base_universe_d2_075_pcmp_basefill_075(pcmp_basefill_075):
    return _base_universe_d2(pcmp_basefill_075, 75)
PCMP_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['pcmp_base_universe_d2_075_pcmp_basefill_075'] = {'inputs': ['pcmp_basefill_075'], 'func': pcmp_base_universe_d2_075_pcmp_basefill_075}
