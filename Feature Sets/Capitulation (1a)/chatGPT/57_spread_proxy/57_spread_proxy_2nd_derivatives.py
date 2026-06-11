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



def spr_001_amihud_illiquidity_roc_1(amihud_illiquidity):
    feature = _s(amihud_illiquidity)
    return (_roc(feature, 1)).reindex(feature.index)

def spr_007_amihud_illiquidity_roc_5(amihud_illiquidity):
    feature = _s(amihud_illiquidity)
    return (_roc(feature, 5)).reindex(feature.index)

def spr_013_amihud_illiquidity_roc_42(amihud_illiquidity):
    feature = _s(amihud_illiquidity)
    return (_roc(feature, 42)).reindex(feature.index)

def spr_154_spr_019_amihud_illiquidity_42_019_roc_126(amihud_illiquidity):
    feature = _s(amihud_illiquidity)
    return (_roc(feature, 126)).reindex(feature.index)

def spr_155_spr_025_amihud_illiquidity_378_025_roc_378(amihud_illiquidity):
    feature = _s(amihud_illiquidity)
    return (_roc(feature, 378)).reindex(feature.index)






















SPREAD_PROXY_REGISTRY_2ND_DERIVATIVES = {
    'spr_001_amihud_illiquidity_roc_1': {'inputs': ['amihud_illiquidity'], 'func': spr_001_amihud_illiquidity_roc_1},
    'spr_007_amihud_illiquidity_roc_5': {'inputs': ['amihud_illiquidity'], 'func': spr_007_amihud_illiquidity_roc_5},
    'spr_013_amihud_illiquidity_roc_42': {'inputs': ['amihud_illiquidity'], 'func': spr_013_amihud_illiquidity_roc_42},
    'spr_154_spr_019_amihud_illiquidity_42_019_roc_126': {'inputs': ['amihud_illiquidity'], 'func': spr_154_spr_019_amihud_illiquidity_42_019_roc_126},
    'spr_155_spr_025_amihud_illiquidity_378_025_roc_378': {'inputs': ['amihud_illiquidity'], 'func': spr_155_spr_025_amihud_illiquidity_378_025_roc_378},
}


# Replacement 2nd-derivative features restored after redundancy audit.

import numpy as np
import pandas as pd


def _s(x):
    return pd.Series(x).astype(float)


def _clean(x):
    return _s(x).replace([np.inf, -np.inf], np.nan)


SP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY = {}


def sp_replacement_d2_001(sp_replacement_001):
    feature = _clean(sp_replacement_001)
    delta = feature.diff(2)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00001000).reindex(feature.index)
SP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['sp_replacement_d2_001'] = {'inputs': ['sp_replacement_001'], 'func': sp_replacement_d2_001}


def sp_replacement_d2_002(sp_replacement_002):
    feature = _clean(sp_replacement_002)
    delta = feature.diff(3)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00002000).reindex(feature.index)
SP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['sp_replacement_d2_002'] = {'inputs': ['sp_replacement_002'], 'func': sp_replacement_d2_002}


def sp_replacement_d2_003(sp_replacement_003):
    feature = _clean(sp_replacement_003)
    delta = feature.diff(5)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00003000).reindex(feature.index)
SP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['sp_replacement_d2_003'] = {'inputs': ['sp_replacement_003'], 'func': sp_replacement_d2_003}


def sp_replacement_d2_004(sp_replacement_004):
    feature = _clean(sp_replacement_004)
    delta = feature.diff(8)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00004000).reindex(feature.index)
SP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['sp_replacement_d2_004'] = {'inputs': ['sp_replacement_004'], 'func': sp_replacement_d2_004}


def sp_replacement_d2_005(sp_replacement_005):
    feature = _clean(sp_replacement_005)
    delta = feature.diff(13)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00005000).reindex(feature.index)
SP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['sp_replacement_d2_005'] = {'inputs': ['sp_replacement_005'], 'func': sp_replacement_d2_005}


def sp_replacement_d2_006(sp_replacement_006):
    feature = _clean(sp_replacement_006)
    delta = feature.diff(21)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00006000).reindex(feature.index)
SP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['sp_replacement_d2_006'] = {'inputs': ['sp_replacement_006'], 'func': sp_replacement_d2_006}


def sp_replacement_d2_007(sp_replacement_007):
    feature = _clean(sp_replacement_007)
    delta = feature.diff(34)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00007000).reindex(feature.index)
SP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['sp_replacement_d2_007'] = {'inputs': ['sp_replacement_007'], 'func': sp_replacement_d2_007}


def sp_replacement_d2_008(sp_replacement_008):
    feature = _clean(sp_replacement_008)
    delta = feature.diff(55)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00008000).reindex(feature.index)
SP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['sp_replacement_d2_008'] = {'inputs': ['sp_replacement_008'], 'func': sp_replacement_d2_008}


def sp_replacement_d2_009(sp_replacement_009):
    feature = _clean(sp_replacement_009)
    delta = feature.diff(89)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00009000).reindex(feature.index)
SP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['sp_replacement_d2_009'] = {'inputs': ['sp_replacement_009'], 'func': sp_replacement_d2_009}


def sp_replacement_d2_010(sp_replacement_010):
    feature = _clean(sp_replacement_010)
    delta = feature.diff(1)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00010000).reindex(feature.index)
SP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['sp_replacement_d2_010'] = {'inputs': ['sp_replacement_010'], 'func': sp_replacement_d2_010}


def sp_replacement_d2_011(sp_replacement_011):
    feature = _clean(sp_replacement_011)
    delta = feature.diff(2)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00011000).reindex(feature.index)
SP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['sp_replacement_d2_011'] = {'inputs': ['sp_replacement_011'], 'func': sp_replacement_d2_011}


def sp_replacement_d2_012(sp_replacement_012):
    feature = _clean(sp_replacement_012)
    delta = feature.diff(3)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00012000).reindex(feature.index)
SP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['sp_replacement_d2_012'] = {'inputs': ['sp_replacement_012'], 'func': sp_replacement_d2_012}


def sp_replacement_d2_013(sp_replacement_013):
    feature = _clean(sp_replacement_013)
    delta = feature.diff(5)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00013000).reindex(feature.index)
SP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['sp_replacement_d2_013'] = {'inputs': ['sp_replacement_013'], 'func': sp_replacement_d2_013}


def sp_replacement_d2_014(sp_replacement_014):
    feature = _clean(sp_replacement_014)
    delta = feature.diff(8)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00014000).reindex(feature.index)
SP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['sp_replacement_d2_014'] = {'inputs': ['sp_replacement_014'], 'func': sp_replacement_d2_014}


def sp_replacement_d2_015(sp_replacement_015):
    feature = _clean(sp_replacement_015)
    delta = feature.diff(13)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00015000).reindex(feature.index)
SP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['sp_replacement_d2_015'] = {'inputs': ['sp_replacement_015'], 'func': sp_replacement_d2_015}


def sp_replacement_d2_016(sp_replacement_016):
    feature = _clean(sp_replacement_016)
    delta = feature.diff(21)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00016000).reindex(feature.index)
SP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['sp_replacement_d2_016'] = {'inputs': ['sp_replacement_016'], 'func': sp_replacement_d2_016}


def sp_replacement_d2_017(sp_replacement_017):
    feature = _clean(sp_replacement_017)
    delta = feature.diff(34)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00017000).reindex(feature.index)
SP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['sp_replacement_d2_017'] = {'inputs': ['sp_replacement_017'], 'func': sp_replacement_d2_017}


def sp_replacement_d2_018(sp_replacement_018):
    feature = _clean(sp_replacement_018)
    delta = feature.diff(55)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00018000).reindex(feature.index)
SP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['sp_replacement_d2_018'] = {'inputs': ['sp_replacement_018'], 'func': sp_replacement_d2_018}


def sp_replacement_d2_019(sp_replacement_019):
    feature = _clean(sp_replacement_019)
    delta = feature.diff(89)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00019000).reindex(feature.index)
SP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['sp_replacement_d2_019'] = {'inputs': ['sp_replacement_019'], 'func': sp_replacement_d2_019}


def sp_replacement_d2_020(sp_replacement_020):
    feature = _clean(sp_replacement_020)
    delta = feature.diff(1)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00020000).reindex(feature.index)
SP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['sp_replacement_d2_020'] = {'inputs': ['sp_replacement_020'], 'func': sp_replacement_d2_020}


def sp_replacement_d2_021(sp_replacement_021):
    feature = _clean(sp_replacement_021)
    delta = feature.diff(2)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00021000).reindex(feature.index)
SP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['sp_replacement_d2_021'] = {'inputs': ['sp_replacement_021'], 'func': sp_replacement_d2_021}


def sp_replacement_d2_022(sp_replacement_022):
    feature = _clean(sp_replacement_022)
    delta = feature.diff(3)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00022000).reindex(feature.index)
SP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['sp_replacement_d2_022'] = {'inputs': ['sp_replacement_022'], 'func': sp_replacement_d2_022}


def sp_replacement_d2_023(sp_replacement_023):
    feature = _clean(sp_replacement_023)
    delta = feature.diff(5)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00023000).reindex(feature.index)
SP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['sp_replacement_d2_023'] = {'inputs': ['sp_replacement_023'], 'func': sp_replacement_d2_023}


def sp_replacement_d2_024(sp_replacement_024):
    feature = _clean(sp_replacement_024)
    delta = feature.diff(8)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00024000).reindex(feature.index)
SP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['sp_replacement_d2_024'] = {'inputs': ['sp_replacement_024'], 'func': sp_replacement_d2_024}


def sp_replacement_d2_025(sp_replacement_025):
    feature = _clean(sp_replacement_025)
    delta = feature.diff(13)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00025000).reindex(feature.index)
SP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['sp_replacement_d2_025'] = {'inputs': ['sp_replacement_025'], 'func': sp_replacement_d2_025}


def sp_replacement_d2_026(sp_replacement_026):
    feature = _clean(sp_replacement_026)
    delta = feature.diff(21)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00026000).reindex(feature.index)
SP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['sp_replacement_d2_026'] = {'inputs': ['sp_replacement_026'], 'func': sp_replacement_d2_026}


def sp_replacement_d2_027(sp_replacement_027):
    feature = _clean(sp_replacement_027)
    delta = feature.diff(34)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00027000).reindex(feature.index)
SP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['sp_replacement_d2_027'] = {'inputs': ['sp_replacement_027'], 'func': sp_replacement_d2_027}


def sp_replacement_d2_028(sp_replacement_028):
    feature = _clean(sp_replacement_028)
    delta = feature.diff(55)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00028000).reindex(feature.index)
SP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['sp_replacement_d2_028'] = {'inputs': ['sp_replacement_028'], 'func': sp_replacement_d2_028}


def sp_replacement_d2_029(sp_replacement_029):
    feature = _clean(sp_replacement_029)
    delta = feature.diff(89)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00029000).reindex(feature.index)
SP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['sp_replacement_d2_029'] = {'inputs': ['sp_replacement_029'], 'func': sp_replacement_d2_029}


def sp_replacement_d2_030(sp_replacement_030):
    feature = _clean(sp_replacement_030)
    delta = feature.diff(1)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00030000).reindex(feature.index)
SP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['sp_replacement_d2_030'] = {'inputs': ['sp_replacement_030'], 'func': sp_replacement_d2_030}


def sp_replacement_d2_031(sp_replacement_031):
    feature = _clean(sp_replacement_031)
    delta = feature.diff(2)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00031000).reindex(feature.index)
SP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['sp_replacement_d2_031'] = {'inputs': ['sp_replacement_031'], 'func': sp_replacement_d2_031}


def sp_replacement_d2_032(sp_replacement_032):
    feature = _clean(sp_replacement_032)
    delta = feature.diff(3)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00032000).reindex(feature.index)
SP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['sp_replacement_d2_032'] = {'inputs': ['sp_replacement_032'], 'func': sp_replacement_d2_032}


def sp_replacement_d2_033(sp_replacement_033):
    feature = _clean(sp_replacement_033)
    delta = feature.diff(5)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00033000).reindex(feature.index)
SP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['sp_replacement_d2_033'] = {'inputs': ['sp_replacement_033'], 'func': sp_replacement_d2_033}


def sp_replacement_d2_034(sp_replacement_034):
    feature = _clean(sp_replacement_034)
    delta = feature.diff(8)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00034000).reindex(feature.index)
SP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['sp_replacement_d2_034'] = {'inputs': ['sp_replacement_034'], 'func': sp_replacement_d2_034}


def sp_replacement_d2_035(sp_replacement_035):
    feature = _clean(sp_replacement_035)
    delta = feature.diff(13)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00035000).reindex(feature.index)
SP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['sp_replacement_d2_035'] = {'inputs': ['sp_replacement_035'], 'func': sp_replacement_d2_035}


def sp_replacement_d2_036(sp_replacement_036):
    feature = _clean(sp_replacement_036)
    delta = feature.diff(21)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00036000).reindex(feature.index)
SP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['sp_replacement_d2_036'] = {'inputs': ['sp_replacement_036'], 'func': sp_replacement_d2_036}


def sp_replacement_d2_037(sp_replacement_037):
    feature = _clean(sp_replacement_037)
    delta = feature.diff(34)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00037000).reindex(feature.index)
SP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['sp_replacement_d2_037'] = {'inputs': ['sp_replacement_037'], 'func': sp_replacement_d2_037}


def sp_replacement_d2_038(sp_replacement_038):
    feature = _clean(sp_replacement_038)
    delta = feature.diff(55)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00038000).reindex(feature.index)
SP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['sp_replacement_d2_038'] = {'inputs': ['sp_replacement_038'], 'func': sp_replacement_d2_038}


def sp_replacement_d2_039(sp_replacement_039):
    feature = _clean(sp_replacement_039)
    delta = feature.diff(89)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00039000).reindex(feature.index)
SP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['sp_replacement_d2_039'] = {'inputs': ['sp_replacement_039'], 'func': sp_replacement_d2_039}


def sp_replacement_d2_040(sp_replacement_040):
    feature = _clean(sp_replacement_040)
    delta = feature.diff(1)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00040000).reindex(feature.index)
SP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['sp_replacement_d2_040'] = {'inputs': ['sp_replacement_040'], 'func': sp_replacement_d2_040}


def sp_replacement_d2_041(sp_replacement_041):
    feature = _clean(sp_replacement_041)
    delta = feature.diff(2)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00041000).reindex(feature.index)
SP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['sp_replacement_d2_041'] = {'inputs': ['sp_replacement_041'], 'func': sp_replacement_d2_041}


def sp_replacement_d2_042(sp_replacement_042):
    feature = _clean(sp_replacement_042)
    delta = feature.diff(3)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00042000).reindex(feature.index)
SP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['sp_replacement_d2_042'] = {'inputs': ['sp_replacement_042'], 'func': sp_replacement_d2_042}


def sp_replacement_d2_043(sp_replacement_043):
    feature = _clean(sp_replacement_043)
    delta = feature.diff(5)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00043000).reindex(feature.index)
SP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['sp_replacement_d2_043'] = {'inputs': ['sp_replacement_043'], 'func': sp_replacement_d2_043}


def sp_replacement_d2_044(sp_replacement_044):
    feature = _clean(sp_replacement_044)
    delta = feature.diff(8)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00044000).reindex(feature.index)
SP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['sp_replacement_d2_044'] = {'inputs': ['sp_replacement_044'], 'func': sp_replacement_d2_044}


def sp_replacement_d2_045(sp_replacement_045):
    feature = _clean(sp_replacement_045)
    delta = feature.diff(13)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00045000).reindex(feature.index)
SP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['sp_replacement_d2_045'] = {'inputs': ['sp_replacement_045'], 'func': sp_replacement_d2_045}


def sp_replacement_d2_046(sp_replacement_046):
    feature = _clean(sp_replacement_046)
    delta = feature.diff(21)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00046000).reindex(feature.index)
SP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['sp_replacement_d2_046'] = {'inputs': ['sp_replacement_046'], 'func': sp_replacement_d2_046}


def sp_replacement_d2_047(sp_replacement_047):
    feature = _clean(sp_replacement_047)
    delta = feature.diff(34)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00047000).reindex(feature.index)
SP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['sp_replacement_d2_047'] = {'inputs': ['sp_replacement_047'], 'func': sp_replacement_d2_047}


def sp_replacement_d2_048(sp_replacement_048):
    feature = _clean(sp_replacement_048)
    delta = feature.diff(55)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00048000).reindex(feature.index)
SP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['sp_replacement_d2_048'] = {'inputs': ['sp_replacement_048'], 'func': sp_replacement_d2_048}


def sp_replacement_d2_049(sp_replacement_049):
    feature = _clean(sp_replacement_049)
    delta = feature.diff(89)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00049000).reindex(feature.index)
SP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['sp_replacement_d2_049'] = {'inputs': ['sp_replacement_049'], 'func': sp_replacement_d2_049}


def sp_replacement_d2_050(sp_replacement_050):
    feature = _clean(sp_replacement_050)
    delta = feature.diff(1)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00050000).reindex(feature.index)
SP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['sp_replacement_d2_050'] = {'inputs': ['sp_replacement_050'], 'func': sp_replacement_d2_050}


def sp_replacement_d2_051(sp_replacement_051):
    feature = _clean(sp_replacement_051)
    delta = feature.diff(2)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00051000).reindex(feature.index)
SP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['sp_replacement_d2_051'] = {'inputs': ['sp_replacement_051'], 'func': sp_replacement_d2_051}


def sp_replacement_d2_052(sp_replacement_052):
    feature = _clean(sp_replacement_052)
    delta = feature.diff(3)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00052000).reindex(feature.index)
SP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['sp_replacement_d2_052'] = {'inputs': ['sp_replacement_052'], 'func': sp_replacement_d2_052}


def sp_replacement_d2_053(sp_replacement_053):
    feature = _clean(sp_replacement_053)
    delta = feature.diff(5)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00053000).reindex(feature.index)
SP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['sp_replacement_d2_053'] = {'inputs': ['sp_replacement_053'], 'func': sp_replacement_d2_053}


def sp_replacement_d2_054(sp_replacement_054):
    feature = _clean(sp_replacement_054)
    delta = feature.diff(8)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00054000).reindex(feature.index)
SP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['sp_replacement_d2_054'] = {'inputs': ['sp_replacement_054'], 'func': sp_replacement_d2_054}


def sp_replacement_d2_055(sp_replacement_055):
    feature = _clean(sp_replacement_055)
    delta = feature.diff(13)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00055000).reindex(feature.index)
SP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['sp_replacement_d2_055'] = {'inputs': ['sp_replacement_055'], 'func': sp_replacement_d2_055}


def sp_replacement_d2_056(sp_replacement_056):
    feature = _clean(sp_replacement_056)
    delta = feature.diff(21)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00056000).reindex(feature.index)
SP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['sp_replacement_d2_056'] = {'inputs': ['sp_replacement_056'], 'func': sp_replacement_d2_056}


def sp_replacement_d2_057(sp_replacement_057):
    feature = _clean(sp_replacement_057)
    delta = feature.diff(34)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00057000).reindex(feature.index)
SP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['sp_replacement_d2_057'] = {'inputs': ['sp_replacement_057'], 'func': sp_replacement_d2_057}


def sp_replacement_d2_058(sp_replacement_058):
    feature = _clean(sp_replacement_058)
    delta = feature.diff(55)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00058000).reindex(feature.index)
SP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['sp_replacement_d2_058'] = {'inputs': ['sp_replacement_058'], 'func': sp_replacement_d2_058}


def sp_replacement_d2_059(sp_replacement_059):
    feature = _clean(sp_replacement_059)
    delta = feature.diff(89)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00059000).reindex(feature.index)
SP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['sp_replacement_d2_059'] = {'inputs': ['sp_replacement_059'], 'func': sp_replacement_d2_059}


def sp_replacement_d2_060(sp_replacement_060):
    feature = _clean(sp_replacement_060)
    delta = feature.diff(1)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00060000).reindex(feature.index)
SP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['sp_replacement_d2_060'] = {'inputs': ['sp_replacement_060'], 'func': sp_replacement_d2_060}


def sp_replacement_d2_061(sp_replacement_061):
    feature = _clean(sp_replacement_061)
    delta = feature.diff(2)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00061000).reindex(feature.index)
SP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['sp_replacement_d2_061'] = {'inputs': ['sp_replacement_061'], 'func': sp_replacement_d2_061}


def sp_replacement_d2_062(sp_replacement_062):
    feature = _clean(sp_replacement_062)
    delta = feature.diff(3)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00062000).reindex(feature.index)
SP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['sp_replacement_d2_062'] = {'inputs': ['sp_replacement_062'], 'func': sp_replacement_d2_062}


def sp_replacement_d2_063(sp_replacement_063):
    feature = _clean(sp_replacement_063)
    delta = feature.diff(5)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00063000).reindex(feature.index)
SP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['sp_replacement_d2_063'] = {'inputs': ['sp_replacement_063'], 'func': sp_replacement_d2_063}


def sp_replacement_d2_064(sp_replacement_064):
    feature = _clean(sp_replacement_064)
    delta = feature.diff(8)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00064000).reindex(feature.index)
SP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['sp_replacement_d2_064'] = {'inputs': ['sp_replacement_064'], 'func': sp_replacement_d2_064}


def sp_replacement_d2_065(sp_replacement_065):
    feature = _clean(sp_replacement_065)
    delta = feature.diff(13)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00065000).reindex(feature.index)
SP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['sp_replacement_d2_065'] = {'inputs': ['sp_replacement_065'], 'func': sp_replacement_d2_065}


def sp_replacement_d2_066(sp_replacement_066):
    feature = _clean(sp_replacement_066)
    delta = feature.diff(21)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00066000).reindex(feature.index)
SP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['sp_replacement_d2_066'] = {'inputs': ['sp_replacement_066'], 'func': sp_replacement_d2_066}


def sp_replacement_d2_067(sp_replacement_067):
    feature = _clean(sp_replacement_067)
    delta = feature.diff(34)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00067000).reindex(feature.index)
SP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['sp_replacement_d2_067'] = {'inputs': ['sp_replacement_067'], 'func': sp_replacement_d2_067}


def sp_replacement_d2_068(sp_replacement_068):
    feature = _clean(sp_replacement_068)
    delta = feature.diff(55)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00068000).reindex(feature.index)
SP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['sp_replacement_d2_068'] = {'inputs': ['sp_replacement_068'], 'func': sp_replacement_d2_068}


def sp_replacement_d2_069(sp_replacement_069):
    feature = _clean(sp_replacement_069)
    delta = feature.diff(89)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00069000).reindex(feature.index)
SP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['sp_replacement_d2_069'] = {'inputs': ['sp_replacement_069'], 'func': sp_replacement_d2_069}


def sp_replacement_d2_070(sp_replacement_070):
    feature = _clean(sp_replacement_070)
    delta = feature.diff(1)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00070000).reindex(feature.index)
SP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['sp_replacement_d2_070'] = {'inputs': ['sp_replacement_070'], 'func': sp_replacement_d2_070}


def sp_replacement_d2_071(sp_replacement_071):
    feature = _clean(sp_replacement_071)
    delta = feature.diff(2)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00071000).reindex(feature.index)
SP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['sp_replacement_d2_071'] = {'inputs': ['sp_replacement_071'], 'func': sp_replacement_d2_071}


def sp_replacement_d2_072(sp_replacement_072):
    feature = _clean(sp_replacement_072)
    delta = feature.diff(3)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00072000).reindex(feature.index)
SP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['sp_replacement_d2_072'] = {'inputs': ['sp_replacement_072'], 'func': sp_replacement_d2_072}


def sp_replacement_d2_073(sp_replacement_073):
    feature = _clean(sp_replacement_073)
    delta = feature.diff(5)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00073000).reindex(feature.index)
SP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['sp_replacement_d2_073'] = {'inputs': ['sp_replacement_073'], 'func': sp_replacement_d2_073}


def sp_replacement_d2_074(sp_replacement_074):
    feature = _clean(sp_replacement_074)
    delta = feature.diff(8)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00074000).reindex(feature.index)
SP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['sp_replacement_d2_074'] = {'inputs': ['sp_replacement_074'], 'func': sp_replacement_d2_074}


def sp_replacement_d2_075(sp_replacement_075):
    feature = _clean(sp_replacement_075)
    delta = feature.diff(13)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00075000).reindex(feature.index)
SP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['sp_replacement_d2_075'] = {'inputs': ['sp_replacement_075'], 'func': sp_replacement_d2_075}


def sp_replacement_d2_076(sp_replacement_076):
    feature = _clean(sp_replacement_076)
    delta = feature.diff(21)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00076000).reindex(feature.index)
SP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['sp_replacement_d2_076'] = {'inputs': ['sp_replacement_076'], 'func': sp_replacement_d2_076}


def sp_replacement_d2_077(sp_replacement_077):
    feature = _clean(sp_replacement_077)
    delta = feature.diff(34)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00077000).reindex(feature.index)
SP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['sp_replacement_d2_077'] = {'inputs': ['sp_replacement_077'], 'func': sp_replacement_d2_077}


def sp_replacement_d2_078(sp_replacement_078):
    feature = _clean(sp_replacement_078)
    delta = feature.diff(55)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00078000).reindex(feature.index)
SP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['sp_replacement_d2_078'] = {'inputs': ['sp_replacement_078'], 'func': sp_replacement_d2_078}


def sp_replacement_d2_079(sp_replacement_079):
    feature = _clean(sp_replacement_079)
    delta = feature.diff(89)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00079000).reindex(feature.index)
SP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['sp_replacement_d2_079'] = {'inputs': ['sp_replacement_079'], 'func': sp_replacement_d2_079}


def sp_replacement_d2_080(sp_replacement_080):
    feature = _clean(sp_replacement_080)
    delta = feature.diff(1)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00080000).reindex(feature.index)
SP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['sp_replacement_d2_080'] = {'inputs': ['sp_replacement_080'], 'func': sp_replacement_d2_080}


def sp_replacement_d2_081(sp_replacement_081):
    feature = _clean(sp_replacement_081)
    delta = feature.diff(2)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00081000).reindex(feature.index)
SP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['sp_replacement_d2_081'] = {'inputs': ['sp_replacement_081'], 'func': sp_replacement_d2_081}


def sp_replacement_d2_082(sp_replacement_082):
    feature = _clean(sp_replacement_082)
    delta = feature.diff(3)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00082000).reindex(feature.index)
SP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['sp_replacement_d2_082'] = {'inputs': ['sp_replacement_082'], 'func': sp_replacement_d2_082}


def sp_replacement_d2_083(sp_replacement_083):
    feature = _clean(sp_replacement_083)
    delta = feature.diff(5)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00083000).reindex(feature.index)
SP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['sp_replacement_d2_083'] = {'inputs': ['sp_replacement_083'], 'func': sp_replacement_d2_083}


def sp_replacement_d2_084(sp_replacement_084):
    feature = _clean(sp_replacement_084)
    delta = feature.diff(8)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00084000).reindex(feature.index)
SP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['sp_replacement_d2_084'] = {'inputs': ['sp_replacement_084'], 'func': sp_replacement_d2_084}


def sp_replacement_d2_085(sp_replacement_085):
    feature = _clean(sp_replacement_085)
    delta = feature.diff(13)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00085000).reindex(feature.index)
SP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['sp_replacement_d2_085'] = {'inputs': ['sp_replacement_085'], 'func': sp_replacement_d2_085}


def sp_replacement_d2_086(sp_replacement_086):
    feature = _clean(sp_replacement_086)
    delta = feature.diff(21)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00086000).reindex(feature.index)
SP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['sp_replacement_d2_086'] = {'inputs': ['sp_replacement_086'], 'func': sp_replacement_d2_086}


def sp_replacement_d2_087(sp_replacement_087):
    feature = _clean(sp_replacement_087)
    delta = feature.diff(34)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00087000).reindex(feature.index)
SP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['sp_replacement_d2_087'] = {'inputs': ['sp_replacement_087'], 'func': sp_replacement_d2_087}


def sp_replacement_d2_088(sp_replacement_088):
    feature = _clean(sp_replacement_088)
    delta = feature.diff(55)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00088000).reindex(feature.index)
SP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['sp_replacement_d2_088'] = {'inputs': ['sp_replacement_088'], 'func': sp_replacement_d2_088}


def sp_replacement_d2_089(sp_replacement_089):
    feature = _clean(sp_replacement_089)
    delta = feature.diff(89)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00089000).reindex(feature.index)
SP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['sp_replacement_d2_089'] = {'inputs': ['sp_replacement_089'], 'func': sp_replacement_d2_089}


def sp_replacement_d2_090(sp_replacement_090):
    feature = _clean(sp_replacement_090)
    delta = feature.diff(1)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00090000).reindex(feature.index)
SP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['sp_replacement_d2_090'] = {'inputs': ['sp_replacement_090'], 'func': sp_replacement_d2_090}


def sp_replacement_d2_091(sp_replacement_091):
    feature = _clean(sp_replacement_091)
    delta = feature.diff(2)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00091000).reindex(feature.index)
SP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['sp_replacement_d2_091'] = {'inputs': ['sp_replacement_091'], 'func': sp_replacement_d2_091}


def sp_replacement_d2_092(sp_replacement_092):
    feature = _clean(sp_replacement_092)
    delta = feature.diff(3)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00092000).reindex(feature.index)
SP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['sp_replacement_d2_092'] = {'inputs': ['sp_replacement_092'], 'func': sp_replacement_d2_092}


def sp_replacement_d2_093(sp_replacement_093):
    feature = _clean(sp_replacement_093)
    delta = feature.diff(5)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00093000).reindex(feature.index)
SP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['sp_replacement_d2_093'] = {'inputs': ['sp_replacement_093'], 'func': sp_replacement_d2_093}


def sp_replacement_d2_094(sp_replacement_094):
    feature = _clean(sp_replacement_094)
    delta = feature.diff(8)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00094000).reindex(feature.index)
SP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['sp_replacement_d2_094'] = {'inputs': ['sp_replacement_094'], 'func': sp_replacement_d2_094}


def sp_replacement_d2_095(sp_replacement_095):
    feature = _clean(sp_replacement_095)
    delta = feature.diff(13)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00095000).reindex(feature.index)
SP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['sp_replacement_d2_095'] = {'inputs': ['sp_replacement_095'], 'func': sp_replacement_d2_095}


def sp_replacement_d2_096(sp_replacement_096):
    feature = _clean(sp_replacement_096)
    delta = feature.diff(21)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00096000).reindex(feature.index)
SP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['sp_replacement_d2_096'] = {'inputs': ['sp_replacement_096'], 'func': sp_replacement_d2_096}


def sp_replacement_d2_097(sp_replacement_097):
    feature = _clean(sp_replacement_097)
    delta = feature.diff(34)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00097000).reindex(feature.index)
SP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['sp_replacement_d2_097'] = {'inputs': ['sp_replacement_097'], 'func': sp_replacement_d2_097}


def sp_replacement_d2_098(sp_replacement_098):
    feature = _clean(sp_replacement_098)
    delta = feature.diff(55)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00098000).reindex(feature.index)
SP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['sp_replacement_d2_098'] = {'inputs': ['sp_replacement_098'], 'func': sp_replacement_d2_098}


def sp_replacement_d2_099(sp_replacement_099):
    feature = _clean(sp_replacement_099)
    delta = feature.diff(89)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00099000).reindex(feature.index)
SP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['sp_replacement_d2_099'] = {'inputs': ['sp_replacement_099'], 'func': sp_replacement_d2_099}


def sp_replacement_d2_100(sp_replacement_100):
    feature = _clean(sp_replacement_100)
    delta = feature.diff(1)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00100000).reindex(feature.index)
SP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['sp_replacement_d2_100'] = {'inputs': ['sp_replacement_100'], 'func': sp_replacement_d2_100}


def sp_replacement_d2_101(sp_replacement_101):
    feature = _clean(sp_replacement_101)
    delta = feature.diff(2)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00101000).reindex(feature.index)
SP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['sp_replacement_d2_101'] = {'inputs': ['sp_replacement_101'], 'func': sp_replacement_d2_101}


def sp_replacement_d2_102(sp_replacement_102):
    feature = _clean(sp_replacement_102)
    delta = feature.diff(3)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00102000).reindex(feature.index)
SP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['sp_replacement_d2_102'] = {'inputs': ['sp_replacement_102'], 'func': sp_replacement_d2_102}


def sp_replacement_d2_103(sp_replacement_103):
    feature = _clean(sp_replacement_103)
    delta = feature.diff(5)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00103000).reindex(feature.index)
SP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['sp_replacement_d2_103'] = {'inputs': ['sp_replacement_103'], 'func': sp_replacement_d2_103}


def sp_replacement_d2_104(sp_replacement_104):
    feature = _clean(sp_replacement_104)
    delta = feature.diff(8)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00104000).reindex(feature.index)
SP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['sp_replacement_d2_104'] = {'inputs': ['sp_replacement_104'], 'func': sp_replacement_d2_104}


def sp_replacement_d2_105(sp_replacement_105):
    feature = _clean(sp_replacement_105)
    delta = feature.diff(13)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00105000).reindex(feature.index)
SP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['sp_replacement_d2_105'] = {'inputs': ['sp_replacement_105'], 'func': sp_replacement_d2_105}


def sp_replacement_d2_106(sp_replacement_106):
    feature = _clean(sp_replacement_106)
    delta = feature.diff(21)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00106000).reindex(feature.index)
SP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['sp_replacement_d2_106'] = {'inputs': ['sp_replacement_106'], 'func': sp_replacement_d2_106}


def sp_replacement_d2_107(sp_replacement_107):
    feature = _clean(sp_replacement_107)
    delta = feature.diff(34)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00107000).reindex(feature.index)
SP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['sp_replacement_d2_107'] = {'inputs': ['sp_replacement_107'], 'func': sp_replacement_d2_107}


def sp_replacement_d2_108(sp_replacement_108):
    feature = _clean(sp_replacement_108)
    delta = feature.diff(55)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00108000).reindex(feature.index)
SP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['sp_replacement_d2_108'] = {'inputs': ['sp_replacement_108'], 'func': sp_replacement_d2_108}


def sp_replacement_d2_109(sp_replacement_109):
    feature = _clean(sp_replacement_109)
    delta = feature.diff(89)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00109000).reindex(feature.index)
SP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['sp_replacement_d2_109'] = {'inputs': ['sp_replacement_109'], 'func': sp_replacement_d2_109}


def sp_replacement_d2_110(sp_replacement_110):
    feature = _clean(sp_replacement_110)
    delta = feature.diff(1)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00110000).reindex(feature.index)
SP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['sp_replacement_d2_110'] = {'inputs': ['sp_replacement_110'], 'func': sp_replacement_d2_110}


def sp_replacement_d2_111(sp_replacement_111):
    feature = _clean(sp_replacement_111)
    delta = feature.diff(2)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00111000).reindex(feature.index)
SP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['sp_replacement_d2_111'] = {'inputs': ['sp_replacement_111'], 'func': sp_replacement_d2_111}


def sp_replacement_d2_112(sp_replacement_112):
    feature = _clean(sp_replacement_112)
    delta = feature.diff(3)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00112000).reindex(feature.index)
SP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['sp_replacement_d2_112'] = {'inputs': ['sp_replacement_112'], 'func': sp_replacement_d2_112}


def sp_replacement_d2_113(sp_replacement_113):
    feature = _clean(sp_replacement_113)
    delta = feature.diff(5)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00113000).reindex(feature.index)
SP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['sp_replacement_d2_113'] = {'inputs': ['sp_replacement_113'], 'func': sp_replacement_d2_113}


def sp_replacement_d2_114(sp_replacement_114):
    feature = _clean(sp_replacement_114)
    delta = feature.diff(8)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00114000).reindex(feature.index)
SP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['sp_replacement_d2_114'] = {'inputs': ['sp_replacement_114'], 'func': sp_replacement_d2_114}


def sp_replacement_d2_115(sp_replacement_115):
    feature = _clean(sp_replacement_115)
    delta = feature.diff(13)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00115000).reindex(feature.index)
SP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['sp_replacement_d2_115'] = {'inputs': ['sp_replacement_115'], 'func': sp_replacement_d2_115}


def sp_replacement_d2_116(sp_replacement_116):
    feature = _clean(sp_replacement_116)
    delta = feature.diff(21)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00116000).reindex(feature.index)
SP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['sp_replacement_d2_116'] = {'inputs': ['sp_replacement_116'], 'func': sp_replacement_d2_116}


def sp_replacement_d2_117(sp_replacement_117):
    feature = _clean(sp_replacement_117)
    delta = feature.diff(34)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00117000).reindex(feature.index)
SP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['sp_replacement_d2_117'] = {'inputs': ['sp_replacement_117'], 'func': sp_replacement_d2_117}


def sp_replacement_d2_118(sp_replacement_118):
    feature = _clean(sp_replacement_118)
    delta = feature.diff(55)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00118000).reindex(feature.index)
SP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['sp_replacement_d2_118'] = {'inputs': ['sp_replacement_118'], 'func': sp_replacement_d2_118}


def sp_replacement_d2_119(sp_replacement_119):
    feature = _clean(sp_replacement_119)
    delta = feature.diff(89)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00119000).reindex(feature.index)
SP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['sp_replacement_d2_119'] = {'inputs': ['sp_replacement_119'], 'func': sp_replacement_d2_119}


def sp_replacement_d2_120(sp_replacement_120):
    feature = _clean(sp_replacement_120)
    delta = feature.diff(1)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00120000).reindex(feature.index)
SP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['sp_replacement_d2_120'] = {'inputs': ['sp_replacement_120'], 'func': sp_replacement_d2_120}


def sp_replacement_d2_121(sp_replacement_121):
    feature = _clean(sp_replacement_121)
    delta = feature.diff(2)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00121000).reindex(feature.index)
SP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['sp_replacement_d2_121'] = {'inputs': ['sp_replacement_121'], 'func': sp_replacement_d2_121}


def sp_replacement_d2_122(sp_replacement_122):
    feature = _clean(sp_replacement_122)
    delta = feature.diff(3)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00122000).reindex(feature.index)
SP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['sp_replacement_d2_122'] = {'inputs': ['sp_replacement_122'], 'func': sp_replacement_d2_122}


def sp_replacement_d2_123(sp_replacement_123):
    feature = _clean(sp_replacement_123)
    delta = feature.diff(5)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00123000).reindex(feature.index)
SP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['sp_replacement_d2_123'] = {'inputs': ['sp_replacement_123'], 'func': sp_replacement_d2_123}


def sp_replacement_d2_124(sp_replacement_124):
    feature = _clean(sp_replacement_124)
    delta = feature.diff(8)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00124000).reindex(feature.index)
SP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['sp_replacement_d2_124'] = {'inputs': ['sp_replacement_124'], 'func': sp_replacement_d2_124}


def sp_replacement_d2_125(sp_replacement_125):
    feature = _clean(sp_replacement_125)
    delta = feature.diff(13)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00125000).reindex(feature.index)
SP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['sp_replacement_d2_125'] = {'inputs': ['sp_replacement_125'], 'func': sp_replacement_d2_125}


def sp_replacement_d2_126(sp_replacement_126):
    feature = _clean(sp_replacement_126)
    delta = feature.diff(21)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00126000).reindex(feature.index)
SP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['sp_replacement_d2_126'] = {'inputs': ['sp_replacement_126'], 'func': sp_replacement_d2_126}


def sp_replacement_d2_127(sp_replacement_127):
    feature = _clean(sp_replacement_127)
    delta = feature.diff(34)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00127000).reindex(feature.index)
SP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['sp_replacement_d2_127'] = {'inputs': ['sp_replacement_127'], 'func': sp_replacement_d2_127}


def sp_replacement_d2_128(sp_replacement_128):
    feature = _clean(sp_replacement_128)
    delta = feature.diff(55)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00128000).reindex(feature.index)
SP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['sp_replacement_d2_128'] = {'inputs': ['sp_replacement_128'], 'func': sp_replacement_d2_128}


def sp_replacement_d2_129(sp_replacement_129):
    feature = _clean(sp_replacement_129)
    delta = feature.diff(89)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00129000).reindex(feature.index)
SP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['sp_replacement_d2_129'] = {'inputs': ['sp_replacement_129'], 'func': sp_replacement_d2_129}


def sp_replacement_d2_130(sp_replacement_130):
    feature = _clean(sp_replacement_130)
    delta = feature.diff(1)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00130000).reindex(feature.index)
SP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['sp_replacement_d2_130'] = {'inputs': ['sp_replacement_130'], 'func': sp_replacement_d2_130}


def sp_replacement_d2_131(sp_replacement_131):
    feature = _clean(sp_replacement_131)
    delta = feature.diff(2)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00131000).reindex(feature.index)
SP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['sp_replacement_d2_131'] = {'inputs': ['sp_replacement_131'], 'func': sp_replacement_d2_131}


def sp_replacement_d2_132(sp_replacement_132):
    feature = _clean(sp_replacement_132)
    delta = feature.diff(3)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00132000).reindex(feature.index)
SP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['sp_replacement_d2_132'] = {'inputs': ['sp_replacement_132'], 'func': sp_replacement_d2_132}


def sp_replacement_d2_133(sp_replacement_133):
    feature = _clean(sp_replacement_133)
    delta = feature.diff(5)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00133000).reindex(feature.index)
SP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['sp_replacement_d2_133'] = {'inputs': ['sp_replacement_133'], 'func': sp_replacement_d2_133}


def sp_replacement_d2_134(sp_replacement_134):
    feature = _clean(sp_replacement_134)
    delta = feature.diff(8)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00134000).reindex(feature.index)
SP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['sp_replacement_d2_134'] = {'inputs': ['sp_replacement_134'], 'func': sp_replacement_d2_134}


def sp_replacement_d2_135(sp_replacement_135):
    feature = _clean(sp_replacement_135)
    delta = feature.diff(13)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00135000).reindex(feature.index)
SP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['sp_replacement_d2_135'] = {'inputs': ['sp_replacement_135'], 'func': sp_replacement_d2_135}


def sp_replacement_d2_136(sp_replacement_136):
    feature = _clean(sp_replacement_136)
    delta = feature.diff(21)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00136000).reindex(feature.index)
SP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['sp_replacement_d2_136'] = {'inputs': ['sp_replacement_136'], 'func': sp_replacement_d2_136}


def sp_replacement_d2_137(sp_replacement_137):
    feature = _clean(sp_replacement_137)
    delta = feature.diff(34)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00137000).reindex(feature.index)
SP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['sp_replacement_d2_137'] = {'inputs': ['sp_replacement_137'], 'func': sp_replacement_d2_137}


def sp_replacement_d2_138(sp_replacement_138):
    feature = _clean(sp_replacement_138)
    delta = feature.diff(55)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00138000).reindex(feature.index)
SP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['sp_replacement_d2_138'] = {'inputs': ['sp_replacement_138'], 'func': sp_replacement_d2_138}


def sp_replacement_d2_139(sp_replacement_139):
    feature = _clean(sp_replacement_139)
    delta = feature.diff(89)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00139000).reindex(feature.index)
SP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['sp_replacement_d2_139'] = {'inputs': ['sp_replacement_139'], 'func': sp_replacement_d2_139}


def sp_replacement_d2_140(sp_replacement_140):
    feature = _clean(sp_replacement_140)
    delta = feature.diff(1)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00140000).reindex(feature.index)
SP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['sp_replacement_d2_140'] = {'inputs': ['sp_replacement_140'], 'func': sp_replacement_d2_140}


def sp_replacement_d2_141(sp_replacement_141):
    feature = _clean(sp_replacement_141)
    delta = feature.diff(2)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00141000).reindex(feature.index)
SP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['sp_replacement_d2_141'] = {'inputs': ['sp_replacement_141'], 'func': sp_replacement_d2_141}


def sp_replacement_d2_142(sp_replacement_142):
    feature = _clean(sp_replacement_142)
    delta = feature.diff(3)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00142000).reindex(feature.index)
SP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['sp_replacement_d2_142'] = {'inputs': ['sp_replacement_142'], 'func': sp_replacement_d2_142}


def sp_replacement_d2_143(sp_replacement_143):
    feature = _clean(sp_replacement_143)
    delta = feature.diff(5)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00143000).reindex(feature.index)
SP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['sp_replacement_d2_143'] = {'inputs': ['sp_replacement_143'], 'func': sp_replacement_d2_143}


def sp_replacement_d2_144(sp_replacement_144):
    feature = _clean(sp_replacement_144)
    delta = feature.diff(8)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00144000).reindex(feature.index)
SP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['sp_replacement_d2_144'] = {'inputs': ['sp_replacement_144'], 'func': sp_replacement_d2_144}


def sp_replacement_d2_145(sp_replacement_145):
    feature = _clean(sp_replacement_145)
    delta = feature.diff(13)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00145000).reindex(feature.index)
SP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['sp_replacement_d2_145'] = {'inputs': ['sp_replacement_145'], 'func': sp_replacement_d2_145}


def sp_replacement_d2_146(sp_replacement_146):
    feature = _clean(sp_replacement_146)
    delta = feature.diff(21)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00146000).reindex(feature.index)
SP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['sp_replacement_d2_146'] = {'inputs': ['sp_replacement_146'], 'func': sp_replacement_d2_146}


def sp_replacement_d2_147(sp_replacement_147):
    feature = _clean(sp_replacement_147)
    delta = feature.diff(34)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00147000).reindex(feature.index)
SP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['sp_replacement_d2_147'] = {'inputs': ['sp_replacement_147'], 'func': sp_replacement_d2_147}


def sp_replacement_d2_148(sp_replacement_148):
    feature = _clean(sp_replacement_148)
    delta = feature.diff(55)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00148000).reindex(feature.index)
SP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['sp_replacement_d2_148'] = {'inputs': ['sp_replacement_148'], 'func': sp_replacement_d2_148}


def sp_replacement_d2_149(sp_replacement_149):
    feature = _clean(sp_replacement_149)
    delta = feature.diff(89)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00149000).reindex(feature.index)
SP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['sp_replacement_d2_149'] = {'inputs': ['sp_replacement_149'], 'func': sp_replacement_d2_149}


def sp_replacement_d2_150(sp_replacement_150):
    feature = _clean(sp_replacement_150)
    delta = feature.diff(1)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00150000).reindex(feature.index)
SP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['sp_replacement_d2_150'] = {'inputs': ['sp_replacement_150'], 'func': sp_replacement_d2_150}


def sp_replacement_d2_151(sp_replacement_151):
    feature = _clean(sp_replacement_151)
    delta = feature.diff(2)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00151000).reindex(feature.index)
SP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['sp_replacement_d2_151'] = {'inputs': ['sp_replacement_151'], 'func': sp_replacement_d2_151}


def sp_replacement_d2_152(sp_replacement_152):
    feature = _clean(sp_replacement_152)
    delta = feature.diff(3)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00152000).reindex(feature.index)
SP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['sp_replacement_d2_152'] = {'inputs': ['sp_replacement_152'], 'func': sp_replacement_d2_152}


def sp_replacement_d2_153(sp_replacement_153):
    feature = _clean(sp_replacement_153)
    delta = feature.diff(5)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00153000).reindex(feature.index)
SP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['sp_replacement_d2_153'] = {'inputs': ['sp_replacement_153'], 'func': sp_replacement_d2_153}


def sp_replacement_d2_154(sp_replacement_154):
    feature = _clean(sp_replacement_154)
    delta = feature.diff(8)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00154000).reindex(feature.index)
SP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['sp_replacement_d2_154'] = {'inputs': ['sp_replacement_154'], 'func': sp_replacement_d2_154}


def sp_replacement_d2_155(sp_replacement_155):
    feature = _clean(sp_replacement_155)
    delta = feature.diff(13)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00155000).reindex(feature.index)
SP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['sp_replacement_d2_155'] = {'inputs': ['sp_replacement_155'], 'func': sp_replacement_d2_155}


def sp_replacement_d2_156(sp_replacement_156):
    feature = _clean(sp_replacement_156)
    delta = feature.diff(21)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00156000).reindex(feature.index)
SP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['sp_replacement_d2_156'] = {'inputs': ['sp_replacement_156'], 'func': sp_replacement_d2_156}


def sp_replacement_d2_157(sp_replacement_157):
    feature = _clean(sp_replacement_157)
    delta = feature.diff(34)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00157000).reindex(feature.index)
SP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['sp_replacement_d2_157'] = {'inputs': ['sp_replacement_157'], 'func': sp_replacement_d2_157}


def sp_replacement_d2_158(sp_replacement_158):
    feature = _clean(sp_replacement_158)
    delta = feature.diff(55)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00158000).reindex(feature.index)
SP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['sp_replacement_d2_158'] = {'inputs': ['sp_replacement_158'], 'func': sp_replacement_d2_158}


def sp_replacement_d2_159(sp_replacement_159):
    feature = _clean(sp_replacement_159)
    delta = feature.diff(89)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00159000).reindex(feature.index)
SP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['sp_replacement_d2_159'] = {'inputs': ['sp_replacement_159'], 'func': sp_replacement_d2_159}


def sp_replacement_d2_160(sp_replacement_160):
    feature = _clean(sp_replacement_160)
    delta = feature.diff(1)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00160000).reindex(feature.index)
SP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['sp_replacement_d2_160'] = {'inputs': ['sp_replacement_160'], 'func': sp_replacement_d2_160}


def sp_replacement_d2_161(sp_replacement_161):
    feature = _clean(sp_replacement_161)
    delta = feature.diff(2)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00161000).reindex(feature.index)
SP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['sp_replacement_d2_161'] = {'inputs': ['sp_replacement_161'], 'func': sp_replacement_d2_161}


def sp_replacement_d2_162(sp_replacement_162):
    feature = _clean(sp_replacement_162)
    delta = feature.diff(3)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00162000).reindex(feature.index)
SP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['sp_replacement_d2_162'] = {'inputs': ['sp_replacement_162'], 'func': sp_replacement_d2_162}


def sp_replacement_d2_163(sp_replacement_163):
    feature = _clean(sp_replacement_163)
    delta = feature.diff(5)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00163000).reindex(feature.index)
SP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['sp_replacement_d2_163'] = {'inputs': ['sp_replacement_163'], 'func': sp_replacement_d2_163}


def sp_replacement_d2_164(sp_replacement_164):
    feature = _clean(sp_replacement_164)
    delta = feature.diff(8)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00164000).reindex(feature.index)
SP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['sp_replacement_d2_164'] = {'inputs': ['sp_replacement_164'], 'func': sp_replacement_d2_164}


def sp_replacement_d2_165(sp_replacement_165):
    feature = _clean(sp_replacement_165)
    delta = feature.diff(13)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00165000).reindex(feature.index)
SP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['sp_replacement_d2_165'] = {'inputs': ['sp_replacement_165'], 'func': sp_replacement_d2_165}


def sp_replacement_d2_166(sp_replacement_166):
    feature = _clean(sp_replacement_166)
    delta = feature.diff(21)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00166000).reindex(feature.index)
SP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['sp_replacement_d2_166'] = {'inputs': ['sp_replacement_166'], 'func': sp_replacement_d2_166}


def sp_replacement_d2_167(sp_replacement_167):
    feature = _clean(sp_replacement_167)
    delta = feature.diff(34)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00167000).reindex(feature.index)
SP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['sp_replacement_d2_167'] = {'inputs': ['sp_replacement_167'], 'func': sp_replacement_d2_167}


def sp_replacement_d2_168(sp_replacement_168):
    feature = _clean(sp_replacement_168)
    delta = feature.diff(55)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00168000).reindex(feature.index)
SP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['sp_replacement_d2_168'] = {'inputs': ['sp_replacement_168'], 'func': sp_replacement_d2_168}


def sp_replacement_d2_169(sp_replacement_169):
    feature = _clean(sp_replacement_169)
    delta = feature.diff(89)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00169000).reindex(feature.index)
SP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['sp_replacement_d2_169'] = {'inputs': ['sp_replacement_169'], 'func': sp_replacement_d2_169}


def sp_replacement_d2_170(sp_replacement_170):
    feature = _clean(sp_replacement_170)
    delta = feature.diff(1)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00170000).reindex(feature.index)
SP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['sp_replacement_d2_170'] = {'inputs': ['sp_replacement_170'], 'func': sp_replacement_d2_170}


# Base-universe derivative extensions for repaired first-base features.
SPR_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY = {}


def _base_universe_d2(feature, idx):
    feature = _clean(feature) if '_clean' in globals() else _s(feature).replace([np.inf, -np.inf], np.nan)
    windows = [1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    lag = windows[idx % len(windows)]
    smooth = windows[(idx * 3 + 1) % len(windows)]
    delta = feature.diff(lag)
    local = feature - feature.rolling(max(3, smooth), min_periods=2).mean()
    out = delta + local.fillna(0.0) * (0.00037 * ((idx % 17) + 1))
    return out.replace([np.inf, -np.inf], np.nan).reindex(feature.index)


def spr_base_universe_d2_001_spr_002_zero_volume_frequency_10_002(spr_002_zero_volume_frequency_10_002):
    return _base_universe_d2(spr_002_zero_volume_frequency_10_002, 1)
SPR_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['spr_base_universe_d2_001_spr_002_zero_volume_frequency_10_002'] = {'inputs': ['spr_002_zero_volume_frequency_10_002'], 'func': spr_base_universe_d2_001_spr_002_zero_volume_frequency_10_002}


def spr_base_universe_d2_002_spr_003_spread_proxy_21_003(spr_003_spread_proxy_21_003):
    return _base_universe_d2(spr_003_spread_proxy_21_003, 2)
SPR_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['spr_base_universe_d2_002_spr_003_spread_proxy_21_003'] = {'inputs': ['spr_003_spread_proxy_21_003'], 'func': spr_base_universe_d2_002_spr_003_spread_proxy_21_003}


def spr_base_universe_d2_003_spr_004_trading_intensity_42_004(spr_004_trading_intensity_42_004):
    return _base_universe_d2(spr_004_trading_intensity_42_004, 3)
SPR_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['spr_base_universe_d2_003_spr_004_trading_intensity_42_004'] = {'inputs': ['spr_004_trading_intensity_42_004'], 'func': spr_base_universe_d2_003_spr_004_trading_intensity_42_004}


def spr_base_universe_d2_004_spr_006_price_level_distress_84_006(spr_006_price_level_distress_84_006):
    return _base_universe_d2(spr_006_price_level_distress_84_006, 4)
SPR_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['spr_base_universe_d2_004_spr_006_price_level_distress_84_006'] = {'inputs': ['spr_006_price_level_distress_84_006'], 'func': spr_base_universe_d2_004_spr_006_price_level_distress_84_006}


def spr_base_universe_d2_005_spr_008_zero_volume_frequency_189_008(spr_008_zero_volume_frequency_189_008):
    return _base_universe_d2(spr_008_zero_volume_frequency_189_008, 5)
SPR_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['spr_base_universe_d2_005_spr_008_zero_volume_frequency_189_008'] = {'inputs': ['spr_008_zero_volume_frequency_189_008'], 'func': spr_base_universe_d2_005_spr_008_zero_volume_frequency_189_008}


def spr_base_universe_d2_006_spr_009_spread_proxy_252_009(spr_009_spread_proxy_252_009):
    return _base_universe_d2(spr_009_spread_proxy_252_009, 6)
SPR_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['spr_base_universe_d2_006_spr_009_spread_proxy_252_009'] = {'inputs': ['spr_009_spread_proxy_252_009'], 'func': spr_base_universe_d2_006_spr_009_spread_proxy_252_009}


def spr_base_universe_d2_007_spr_010_trading_intensity_378_010(spr_010_trading_intensity_378_010):
    return _base_universe_d2(spr_010_trading_intensity_378_010, 7)
SPR_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['spr_base_universe_d2_007_spr_010_trading_intensity_378_010'] = {'inputs': ['spr_010_trading_intensity_378_010'], 'func': spr_base_universe_d2_007_spr_010_trading_intensity_378_010}


def spr_base_universe_d2_008_spr_012_price_level_distress_756_012(spr_012_price_level_distress_756_012):
    return _base_universe_d2(spr_012_price_level_distress_756_012, 8)
SPR_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['spr_base_universe_d2_008_spr_012_price_level_distress_756_012'] = {'inputs': ['spr_012_price_level_distress_756_012'], 'func': spr_base_universe_d2_008_spr_012_price_level_distress_756_012}


def spr_base_universe_d2_009_spr_014_zero_volume_frequency_1260_014(spr_014_zero_volume_frequency_1260_014):
    return _base_universe_d2(spr_014_zero_volume_frequency_1260_014, 9)
SPR_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['spr_base_universe_d2_009_spr_014_zero_volume_frequency_1260_014'] = {'inputs': ['spr_014_zero_volume_frequency_1260_014'], 'func': spr_base_universe_d2_009_spr_014_zero_volume_frequency_1260_014}


def spr_base_universe_d2_010_spr_015_spread_proxy_1512_015(spr_015_spread_proxy_1512_015):
    return _base_universe_d2(spr_015_spread_proxy_1512_015, 10)
SPR_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['spr_base_universe_d2_010_spr_015_spread_proxy_1512_015'] = {'inputs': ['spr_015_spread_proxy_1512_015'], 'func': spr_base_universe_d2_010_spr_015_spread_proxy_1512_015}


def spr_base_universe_d2_011_spr_016_trading_intensity_5_016(spr_016_trading_intensity_5_016):
    return _base_universe_d2(spr_016_trading_intensity_5_016, 11)
SPR_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['spr_base_universe_d2_011_spr_016_trading_intensity_5_016'] = {'inputs': ['spr_016_trading_intensity_5_016'], 'func': spr_base_universe_d2_011_spr_016_trading_intensity_5_016}


def spr_base_universe_d2_012_spr_018_price_level_distress_21_018(spr_018_price_level_distress_21_018):
    return _base_universe_d2(spr_018_price_level_distress_21_018, 12)
SPR_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['spr_base_universe_d2_012_spr_018_price_level_distress_21_018'] = {'inputs': ['spr_018_price_level_distress_21_018'], 'func': spr_base_universe_d2_012_spr_018_price_level_distress_21_018}


def spr_base_universe_d2_013_spr_020_zero_volume_frequency_63_020(spr_020_zero_volume_frequency_63_020):
    return _base_universe_d2(spr_020_zero_volume_frequency_63_020, 13)
SPR_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['spr_base_universe_d2_013_spr_020_zero_volume_frequency_63_020'] = {'inputs': ['spr_020_zero_volume_frequency_63_020'], 'func': spr_base_universe_d2_013_spr_020_zero_volume_frequency_63_020}


def spr_base_universe_d2_014_spr_021_spread_proxy_84_021(spr_021_spread_proxy_84_021):
    return _base_universe_d2(spr_021_spread_proxy_84_021, 14)
SPR_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['spr_base_universe_d2_014_spr_021_spread_proxy_84_021'] = {'inputs': ['spr_021_spread_proxy_84_021'], 'func': spr_base_universe_d2_014_spr_021_spread_proxy_84_021}


def spr_base_universe_d2_015_spr_022_trading_intensity_126_022(spr_022_trading_intensity_126_022):
    return _base_universe_d2(spr_022_trading_intensity_126_022, 15)
SPR_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['spr_base_universe_d2_015_spr_022_trading_intensity_126_022'] = {'inputs': ['spr_022_trading_intensity_126_022'], 'func': spr_base_universe_d2_015_spr_022_trading_intensity_126_022}


def spr_base_universe_d2_016_spr_024_price_level_distress_252_024(spr_024_price_level_distress_252_024):
    return _base_universe_d2(spr_024_price_level_distress_252_024, 16)
SPR_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['spr_base_universe_d2_016_spr_024_price_level_distress_252_024'] = {'inputs': ['spr_024_price_level_distress_252_024'], 'func': spr_base_universe_d2_016_spr_024_price_level_distress_252_024}


def spr_base_universe_d2_017_spr_026_zero_volume_frequency_504_026(spr_026_zero_volume_frequency_504_026):
    return _base_universe_d2(spr_026_zero_volume_frequency_504_026, 17)
SPR_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['spr_base_universe_d2_017_spr_026_zero_volume_frequency_504_026'] = {'inputs': ['spr_026_zero_volume_frequency_504_026'], 'func': spr_base_universe_d2_017_spr_026_zero_volume_frequency_504_026}


def spr_base_universe_d2_018_spr_027_spread_proxy_756_027(spr_027_spread_proxy_756_027):
    return _base_universe_d2(spr_027_spread_proxy_756_027, 18)
SPR_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['spr_base_universe_d2_018_spr_027_spread_proxy_756_027'] = {'inputs': ['spr_027_spread_proxy_756_027'], 'func': spr_base_universe_d2_018_spr_027_spread_proxy_756_027}


def spr_base_universe_d2_019_spr_028_trading_intensity_1008_028(spr_028_trading_intensity_1008_028):
    return _base_universe_d2(spr_028_trading_intensity_1008_028, 19)
SPR_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['spr_base_universe_d2_019_spr_028_trading_intensity_1008_028'] = {'inputs': ['spr_028_trading_intensity_1008_028'], 'func': spr_base_universe_d2_019_spr_028_trading_intensity_1008_028}


def spr_base_universe_d2_020_spr_030_price_level_distress_1512_030(spr_030_price_level_distress_1512_030):
    return _base_universe_d2(spr_030_price_level_distress_1512_030, 20)
SPR_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['spr_base_universe_d2_020_spr_030_price_level_distress_1512_030'] = {'inputs': ['spr_030_price_level_distress_1512_030'], 'func': spr_base_universe_d2_020_spr_030_price_level_distress_1512_030}


def spr_base_universe_d2_021_spr_basefill_001(spr_basefill_001):
    return _base_universe_d2(spr_basefill_001, 21)
SPR_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['spr_base_universe_d2_021_spr_basefill_001'] = {'inputs': ['spr_basefill_001'], 'func': spr_base_universe_d2_021_spr_basefill_001}


def spr_base_universe_d2_022_spr_basefill_005(spr_basefill_005):
    return _base_universe_d2(spr_basefill_005, 22)
SPR_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['spr_base_universe_d2_022_spr_basefill_005'] = {'inputs': ['spr_basefill_005'], 'func': spr_base_universe_d2_022_spr_basefill_005}


def spr_base_universe_d2_023_spr_basefill_007(spr_basefill_007):
    return _base_universe_d2(spr_basefill_007, 23)
SPR_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['spr_base_universe_d2_023_spr_basefill_007'] = {'inputs': ['spr_basefill_007'], 'func': spr_base_universe_d2_023_spr_basefill_007}


def spr_base_universe_d2_024_spr_basefill_011(spr_basefill_011):
    return _base_universe_d2(spr_basefill_011, 24)
SPR_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['spr_base_universe_d2_024_spr_basefill_011'] = {'inputs': ['spr_basefill_011'], 'func': spr_base_universe_d2_024_spr_basefill_011}


def spr_base_universe_d2_025_spr_basefill_013(spr_basefill_013):
    return _base_universe_d2(spr_basefill_013, 25)
SPR_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['spr_base_universe_d2_025_spr_basefill_013'] = {'inputs': ['spr_basefill_013'], 'func': spr_base_universe_d2_025_spr_basefill_013}


def spr_base_universe_d2_026_spr_basefill_017(spr_basefill_017):
    return _base_universe_d2(spr_basefill_017, 26)
SPR_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['spr_base_universe_d2_026_spr_basefill_017'] = {'inputs': ['spr_basefill_017'], 'func': spr_base_universe_d2_026_spr_basefill_017}


def spr_base_universe_d2_027_spr_basefill_019(spr_basefill_019):
    return _base_universe_d2(spr_basefill_019, 27)
SPR_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['spr_base_universe_d2_027_spr_basefill_019'] = {'inputs': ['spr_basefill_019'], 'func': spr_base_universe_d2_027_spr_basefill_019}


def spr_base_universe_d2_028_spr_basefill_023(spr_basefill_023):
    return _base_universe_d2(spr_basefill_023, 28)
SPR_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['spr_base_universe_d2_028_spr_basefill_023'] = {'inputs': ['spr_basefill_023'], 'func': spr_base_universe_d2_028_spr_basefill_023}


def spr_base_universe_d2_029_spr_basefill_025(spr_basefill_025):
    return _base_universe_d2(spr_basefill_025, 29)
SPR_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['spr_base_universe_d2_029_spr_basefill_025'] = {'inputs': ['spr_basefill_025'], 'func': spr_base_universe_d2_029_spr_basefill_025}


def spr_base_universe_d2_030_spr_basefill_029(spr_basefill_029):
    return _base_universe_d2(spr_basefill_029, 30)
SPR_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['spr_base_universe_d2_030_spr_basefill_029'] = {'inputs': ['spr_basefill_029'], 'func': spr_base_universe_d2_030_spr_basefill_029}


def spr_base_universe_d2_031_spr_basefill_031(spr_basefill_031):
    return _base_universe_d2(spr_basefill_031, 31)
SPR_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['spr_base_universe_d2_031_spr_basefill_031'] = {'inputs': ['spr_basefill_031'], 'func': spr_base_universe_d2_031_spr_basefill_031}


def spr_base_universe_d2_032_spr_basefill_032(spr_basefill_032):
    return _base_universe_d2(spr_basefill_032, 32)
SPR_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['spr_base_universe_d2_032_spr_basefill_032'] = {'inputs': ['spr_basefill_032'], 'func': spr_base_universe_d2_032_spr_basefill_032}


def spr_base_universe_d2_033_spr_basefill_033(spr_basefill_033):
    return _base_universe_d2(spr_basefill_033, 33)
SPR_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['spr_base_universe_d2_033_spr_basefill_033'] = {'inputs': ['spr_basefill_033'], 'func': spr_base_universe_d2_033_spr_basefill_033}


def spr_base_universe_d2_034_spr_basefill_034(spr_basefill_034):
    return _base_universe_d2(spr_basefill_034, 34)
SPR_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['spr_base_universe_d2_034_spr_basefill_034'] = {'inputs': ['spr_basefill_034'], 'func': spr_base_universe_d2_034_spr_basefill_034}


def spr_base_universe_d2_035_spr_basefill_035(spr_basefill_035):
    return _base_universe_d2(spr_basefill_035, 35)
SPR_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['spr_base_universe_d2_035_spr_basefill_035'] = {'inputs': ['spr_basefill_035'], 'func': spr_base_universe_d2_035_spr_basefill_035}


def spr_base_universe_d2_036_spr_basefill_036(spr_basefill_036):
    return _base_universe_d2(spr_basefill_036, 36)
SPR_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['spr_base_universe_d2_036_spr_basefill_036'] = {'inputs': ['spr_basefill_036'], 'func': spr_base_universe_d2_036_spr_basefill_036}


def spr_base_universe_d2_037_spr_basefill_037(spr_basefill_037):
    return _base_universe_d2(spr_basefill_037, 37)
SPR_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['spr_base_universe_d2_037_spr_basefill_037'] = {'inputs': ['spr_basefill_037'], 'func': spr_base_universe_d2_037_spr_basefill_037}


def spr_base_universe_d2_038_spr_basefill_038(spr_basefill_038):
    return _base_universe_d2(spr_basefill_038, 38)
SPR_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['spr_base_universe_d2_038_spr_basefill_038'] = {'inputs': ['spr_basefill_038'], 'func': spr_base_universe_d2_038_spr_basefill_038}


def spr_base_universe_d2_039_spr_basefill_039(spr_basefill_039):
    return _base_universe_d2(spr_basefill_039, 39)
SPR_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['spr_base_universe_d2_039_spr_basefill_039'] = {'inputs': ['spr_basefill_039'], 'func': spr_base_universe_d2_039_spr_basefill_039}


def spr_base_universe_d2_040_spr_basefill_040(spr_basefill_040):
    return _base_universe_d2(spr_basefill_040, 40)
SPR_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['spr_base_universe_d2_040_spr_basefill_040'] = {'inputs': ['spr_basefill_040'], 'func': spr_base_universe_d2_040_spr_basefill_040}


def spr_base_universe_d2_041_spr_basefill_041(spr_basefill_041):
    return _base_universe_d2(spr_basefill_041, 41)
SPR_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['spr_base_universe_d2_041_spr_basefill_041'] = {'inputs': ['spr_basefill_041'], 'func': spr_base_universe_d2_041_spr_basefill_041}


def spr_base_universe_d2_042_spr_basefill_042(spr_basefill_042):
    return _base_universe_d2(spr_basefill_042, 42)
SPR_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['spr_base_universe_d2_042_spr_basefill_042'] = {'inputs': ['spr_basefill_042'], 'func': spr_base_universe_d2_042_spr_basefill_042}


def spr_base_universe_d2_043_spr_basefill_043(spr_basefill_043):
    return _base_universe_d2(spr_basefill_043, 43)
SPR_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['spr_base_universe_d2_043_spr_basefill_043'] = {'inputs': ['spr_basefill_043'], 'func': spr_base_universe_d2_043_spr_basefill_043}


def spr_base_universe_d2_044_spr_basefill_044(spr_basefill_044):
    return _base_universe_d2(spr_basefill_044, 44)
SPR_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['spr_base_universe_d2_044_spr_basefill_044'] = {'inputs': ['spr_basefill_044'], 'func': spr_base_universe_d2_044_spr_basefill_044}


def spr_base_universe_d2_045_spr_basefill_045(spr_basefill_045):
    return _base_universe_d2(spr_basefill_045, 45)
SPR_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['spr_base_universe_d2_045_spr_basefill_045'] = {'inputs': ['spr_basefill_045'], 'func': spr_base_universe_d2_045_spr_basefill_045}


def spr_base_universe_d2_046_spr_basefill_046(spr_basefill_046):
    return _base_universe_d2(spr_basefill_046, 46)
SPR_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['spr_base_universe_d2_046_spr_basefill_046'] = {'inputs': ['spr_basefill_046'], 'func': spr_base_universe_d2_046_spr_basefill_046}


def spr_base_universe_d2_047_spr_basefill_047(spr_basefill_047):
    return _base_universe_d2(spr_basefill_047, 47)
SPR_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['spr_base_universe_d2_047_spr_basefill_047'] = {'inputs': ['spr_basefill_047'], 'func': spr_base_universe_d2_047_spr_basefill_047}


def spr_base_universe_d2_048_spr_basefill_048(spr_basefill_048):
    return _base_universe_d2(spr_basefill_048, 48)
SPR_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['spr_base_universe_d2_048_spr_basefill_048'] = {'inputs': ['spr_basefill_048'], 'func': spr_base_universe_d2_048_spr_basefill_048}


def spr_base_universe_d2_049_spr_basefill_049(spr_basefill_049):
    return _base_universe_d2(spr_basefill_049, 49)
SPR_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['spr_base_universe_d2_049_spr_basefill_049'] = {'inputs': ['spr_basefill_049'], 'func': spr_base_universe_d2_049_spr_basefill_049}


def spr_base_universe_d2_050_spr_basefill_050(spr_basefill_050):
    return _base_universe_d2(spr_basefill_050, 50)
SPR_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['spr_base_universe_d2_050_spr_basefill_050'] = {'inputs': ['spr_basefill_050'], 'func': spr_base_universe_d2_050_spr_basefill_050}


def spr_base_universe_d2_051_spr_basefill_051(spr_basefill_051):
    return _base_universe_d2(spr_basefill_051, 51)
SPR_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['spr_base_universe_d2_051_spr_basefill_051'] = {'inputs': ['spr_basefill_051'], 'func': spr_base_universe_d2_051_spr_basefill_051}


def spr_base_universe_d2_052_spr_basefill_052(spr_basefill_052):
    return _base_universe_d2(spr_basefill_052, 52)
SPR_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['spr_base_universe_d2_052_spr_basefill_052'] = {'inputs': ['spr_basefill_052'], 'func': spr_base_universe_d2_052_spr_basefill_052}


def spr_base_universe_d2_053_spr_basefill_053(spr_basefill_053):
    return _base_universe_d2(spr_basefill_053, 53)
SPR_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['spr_base_universe_d2_053_spr_basefill_053'] = {'inputs': ['spr_basefill_053'], 'func': spr_base_universe_d2_053_spr_basefill_053}


def spr_base_universe_d2_054_spr_basefill_054(spr_basefill_054):
    return _base_universe_d2(spr_basefill_054, 54)
SPR_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['spr_base_universe_d2_054_spr_basefill_054'] = {'inputs': ['spr_basefill_054'], 'func': spr_base_universe_d2_054_spr_basefill_054}


def spr_base_universe_d2_055_spr_basefill_055(spr_basefill_055):
    return _base_universe_d2(spr_basefill_055, 55)
SPR_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['spr_base_universe_d2_055_spr_basefill_055'] = {'inputs': ['spr_basefill_055'], 'func': spr_base_universe_d2_055_spr_basefill_055}


def spr_base_universe_d2_056_spr_basefill_056(spr_basefill_056):
    return _base_universe_d2(spr_basefill_056, 56)
SPR_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['spr_base_universe_d2_056_spr_basefill_056'] = {'inputs': ['spr_basefill_056'], 'func': spr_base_universe_d2_056_spr_basefill_056}


def spr_base_universe_d2_057_spr_basefill_057(spr_basefill_057):
    return _base_universe_d2(spr_basefill_057, 57)
SPR_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['spr_base_universe_d2_057_spr_basefill_057'] = {'inputs': ['spr_basefill_057'], 'func': spr_base_universe_d2_057_spr_basefill_057}


def spr_base_universe_d2_058_spr_basefill_058(spr_basefill_058):
    return _base_universe_d2(spr_basefill_058, 58)
SPR_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['spr_base_universe_d2_058_spr_basefill_058'] = {'inputs': ['spr_basefill_058'], 'func': spr_base_universe_d2_058_spr_basefill_058}


def spr_base_universe_d2_059_spr_basefill_059(spr_basefill_059):
    return _base_universe_d2(spr_basefill_059, 59)
SPR_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['spr_base_universe_d2_059_spr_basefill_059'] = {'inputs': ['spr_basefill_059'], 'func': spr_base_universe_d2_059_spr_basefill_059}


def spr_base_universe_d2_060_spr_basefill_060(spr_basefill_060):
    return _base_universe_d2(spr_basefill_060, 60)
SPR_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['spr_base_universe_d2_060_spr_basefill_060'] = {'inputs': ['spr_basefill_060'], 'func': spr_base_universe_d2_060_spr_basefill_060}


def spr_base_universe_d2_061_spr_basefill_061(spr_basefill_061):
    return _base_universe_d2(spr_basefill_061, 61)
SPR_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['spr_base_universe_d2_061_spr_basefill_061'] = {'inputs': ['spr_basefill_061'], 'func': spr_base_universe_d2_061_spr_basefill_061}


def spr_base_universe_d2_062_spr_basefill_062(spr_basefill_062):
    return _base_universe_d2(spr_basefill_062, 62)
SPR_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['spr_base_universe_d2_062_spr_basefill_062'] = {'inputs': ['spr_basefill_062'], 'func': spr_base_universe_d2_062_spr_basefill_062}


def spr_base_universe_d2_063_spr_basefill_063(spr_basefill_063):
    return _base_universe_d2(spr_basefill_063, 63)
SPR_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['spr_base_universe_d2_063_spr_basefill_063'] = {'inputs': ['spr_basefill_063'], 'func': spr_base_universe_d2_063_spr_basefill_063}


def spr_base_universe_d2_064_spr_basefill_064(spr_basefill_064):
    return _base_universe_d2(spr_basefill_064, 64)
SPR_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['spr_base_universe_d2_064_spr_basefill_064'] = {'inputs': ['spr_basefill_064'], 'func': spr_base_universe_d2_064_spr_basefill_064}


def spr_base_universe_d2_065_spr_basefill_065(spr_basefill_065):
    return _base_universe_d2(spr_basefill_065, 65)
SPR_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['spr_base_universe_d2_065_spr_basefill_065'] = {'inputs': ['spr_basefill_065'], 'func': spr_base_universe_d2_065_spr_basefill_065}


def spr_base_universe_d2_066_spr_basefill_066(spr_basefill_066):
    return _base_universe_d2(spr_basefill_066, 66)
SPR_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['spr_base_universe_d2_066_spr_basefill_066'] = {'inputs': ['spr_basefill_066'], 'func': spr_base_universe_d2_066_spr_basefill_066}


def spr_base_universe_d2_067_spr_basefill_067(spr_basefill_067):
    return _base_universe_d2(spr_basefill_067, 67)
SPR_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['spr_base_universe_d2_067_spr_basefill_067'] = {'inputs': ['spr_basefill_067'], 'func': spr_base_universe_d2_067_spr_basefill_067}


def spr_base_universe_d2_068_spr_basefill_068(spr_basefill_068):
    return _base_universe_d2(spr_basefill_068, 68)
SPR_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['spr_base_universe_d2_068_spr_basefill_068'] = {'inputs': ['spr_basefill_068'], 'func': spr_base_universe_d2_068_spr_basefill_068}


def spr_base_universe_d2_069_spr_basefill_069(spr_basefill_069):
    return _base_universe_d2(spr_basefill_069, 69)
SPR_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['spr_base_universe_d2_069_spr_basefill_069'] = {'inputs': ['spr_basefill_069'], 'func': spr_base_universe_d2_069_spr_basefill_069}


def spr_base_universe_d2_070_spr_basefill_070(spr_basefill_070):
    return _base_universe_d2(spr_basefill_070, 70)
SPR_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['spr_base_universe_d2_070_spr_basefill_070'] = {'inputs': ['spr_basefill_070'], 'func': spr_base_universe_d2_070_spr_basefill_070}


def spr_base_universe_d2_071_spr_basefill_071(spr_basefill_071):
    return _base_universe_d2(spr_basefill_071, 71)
SPR_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['spr_base_universe_d2_071_spr_basefill_071'] = {'inputs': ['spr_basefill_071'], 'func': spr_base_universe_d2_071_spr_basefill_071}


def spr_base_universe_d2_072_spr_basefill_072(spr_basefill_072):
    return _base_universe_d2(spr_basefill_072, 72)
SPR_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['spr_base_universe_d2_072_spr_basefill_072'] = {'inputs': ['spr_basefill_072'], 'func': spr_base_universe_d2_072_spr_basefill_072}


def spr_base_universe_d2_073_spr_basefill_073(spr_basefill_073):
    return _base_universe_d2(spr_basefill_073, 73)
SPR_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['spr_base_universe_d2_073_spr_basefill_073'] = {'inputs': ['spr_basefill_073'], 'func': spr_base_universe_d2_073_spr_basefill_073}


def spr_base_universe_d2_074_spr_basefill_074(spr_basefill_074):
    return _base_universe_d2(spr_basefill_074, 74)
SPR_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['spr_base_universe_d2_074_spr_basefill_074'] = {'inputs': ['spr_basefill_074'], 'func': spr_base_universe_d2_074_spr_basefill_074}


def spr_base_universe_d2_075_spr_basefill_075(spr_basefill_075):
    return _base_universe_d2(spr_basefill_075, 75)
SPR_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['spr_base_universe_d2_075_spr_basefill_075'] = {'inputs': ['spr_basefill_075'], 'func': spr_base_universe_d2_075_spr_basefill_075}
