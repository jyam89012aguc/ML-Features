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



def tbd_001_return_decay_roc_1(return_decay):
    feature = _s(return_decay)
    return (_roc(feature, 1)).reindex(feature.index)

def tbd_007_return_decay_roc_5(return_decay):
    feature = _s(return_decay)
    return (_roc(feature, 5)).reindex(feature.index)

def tbd_013_return_decay_roc_42(return_decay):
    feature = _s(return_decay)
    return (_roc(feature, 42)).reindex(feature.index)

def tbd_154_tbd_019_return_decay_42_019_roc_126(return_decay):
    feature = _s(return_decay)
    return (_roc(feature, 126)).reindex(feature.index)

def tbd_155_tbd_025_return_decay_5_025_roc_378(return_decay):
    feature = _s(return_decay)
    return (_roc(feature, 378)).reindex(feature.index)






















TREND_BREAKDOWN_REGISTRY_2ND_DERIVATIVES = {
    'tbd_001_return_decay_roc_1': {'inputs': ['return_decay'], 'func': tbd_001_return_decay_roc_1},
    'tbd_007_return_decay_roc_5': {'inputs': ['return_decay'], 'func': tbd_007_return_decay_roc_5},
    'tbd_013_return_decay_roc_42': {'inputs': ['return_decay'], 'func': tbd_013_return_decay_roc_42},
    'tbd_154_tbd_019_return_decay_42_019_roc_126': {'inputs': ['return_decay'], 'func': tbd_154_tbd_019_return_decay_42_019_roc_126},
    'tbd_155_tbd_025_return_decay_5_025_roc_378': {'inputs': ['return_decay'], 'func': tbd_155_tbd_025_return_decay_5_025_roc_378},
}


# Replacement 2nd-derivative features restored after redundancy audit.

import numpy as np
import pandas as pd


def _s(x):
    return pd.Series(x).astype(float)


def _clean(x):
    return _s(x).replace([np.inf, -np.inf], np.nan)


TB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY = {}


def tb_replacement_d2_001(tb_replacement_001):
    feature = _clean(tb_replacement_001)
    delta = feature.diff(2)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00001000).reindex(feature.index)
TB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['tb_replacement_d2_001'] = {'inputs': ['tb_replacement_001'], 'func': tb_replacement_d2_001}


def tb_replacement_d2_002(tb_replacement_002):
    feature = _clean(tb_replacement_002)
    delta = feature.diff(3)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00002000).reindex(feature.index)
TB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['tb_replacement_d2_002'] = {'inputs': ['tb_replacement_002'], 'func': tb_replacement_d2_002}


def tb_replacement_d2_003(tb_replacement_003):
    feature = _clean(tb_replacement_003)
    delta = feature.diff(5)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00003000).reindex(feature.index)
TB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['tb_replacement_d2_003'] = {'inputs': ['tb_replacement_003'], 'func': tb_replacement_d2_003}


def tb_replacement_d2_004(tb_replacement_004):
    feature = _clean(tb_replacement_004)
    delta = feature.diff(8)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00004000).reindex(feature.index)
TB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['tb_replacement_d2_004'] = {'inputs': ['tb_replacement_004'], 'func': tb_replacement_d2_004}


def tb_replacement_d2_005(tb_replacement_005):
    feature = _clean(tb_replacement_005)
    delta = feature.diff(13)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00005000).reindex(feature.index)
TB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['tb_replacement_d2_005'] = {'inputs': ['tb_replacement_005'], 'func': tb_replacement_d2_005}


def tb_replacement_d2_006(tb_replacement_006):
    feature = _clean(tb_replacement_006)
    delta = feature.diff(21)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00006000).reindex(feature.index)
TB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['tb_replacement_d2_006'] = {'inputs': ['tb_replacement_006'], 'func': tb_replacement_d2_006}


def tb_replacement_d2_007(tb_replacement_007):
    feature = _clean(tb_replacement_007)
    delta = feature.diff(34)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00007000).reindex(feature.index)
TB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['tb_replacement_d2_007'] = {'inputs': ['tb_replacement_007'], 'func': tb_replacement_d2_007}


def tb_replacement_d2_008(tb_replacement_008):
    feature = _clean(tb_replacement_008)
    delta = feature.diff(55)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00008000).reindex(feature.index)
TB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['tb_replacement_d2_008'] = {'inputs': ['tb_replacement_008'], 'func': tb_replacement_d2_008}


def tb_replacement_d2_009(tb_replacement_009):
    feature = _clean(tb_replacement_009)
    delta = feature.diff(89)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00009000).reindex(feature.index)
TB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['tb_replacement_d2_009'] = {'inputs': ['tb_replacement_009'], 'func': tb_replacement_d2_009}


def tb_replacement_d2_010(tb_replacement_010):
    feature = _clean(tb_replacement_010)
    delta = feature.diff(1)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00010000).reindex(feature.index)
TB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['tb_replacement_d2_010'] = {'inputs': ['tb_replacement_010'], 'func': tb_replacement_d2_010}


def tb_replacement_d2_011(tb_replacement_011):
    feature = _clean(tb_replacement_011)
    delta = feature.diff(2)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00011000).reindex(feature.index)
TB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['tb_replacement_d2_011'] = {'inputs': ['tb_replacement_011'], 'func': tb_replacement_d2_011}


def tb_replacement_d2_012(tb_replacement_012):
    feature = _clean(tb_replacement_012)
    delta = feature.diff(3)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00012000).reindex(feature.index)
TB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['tb_replacement_d2_012'] = {'inputs': ['tb_replacement_012'], 'func': tb_replacement_d2_012}


def tb_replacement_d2_013(tb_replacement_013):
    feature = _clean(tb_replacement_013)
    delta = feature.diff(5)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00013000).reindex(feature.index)
TB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['tb_replacement_d2_013'] = {'inputs': ['tb_replacement_013'], 'func': tb_replacement_d2_013}


def tb_replacement_d2_014(tb_replacement_014):
    feature = _clean(tb_replacement_014)
    delta = feature.diff(8)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00014000).reindex(feature.index)
TB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['tb_replacement_d2_014'] = {'inputs': ['tb_replacement_014'], 'func': tb_replacement_d2_014}


def tb_replacement_d2_015(tb_replacement_015):
    feature = _clean(tb_replacement_015)
    delta = feature.diff(13)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00015000).reindex(feature.index)
TB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['tb_replacement_d2_015'] = {'inputs': ['tb_replacement_015'], 'func': tb_replacement_d2_015}


def tb_replacement_d2_016(tb_replacement_016):
    feature = _clean(tb_replacement_016)
    delta = feature.diff(21)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00016000).reindex(feature.index)
TB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['tb_replacement_d2_016'] = {'inputs': ['tb_replacement_016'], 'func': tb_replacement_d2_016}


def tb_replacement_d2_017(tb_replacement_017):
    feature = _clean(tb_replacement_017)
    delta = feature.diff(34)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00017000).reindex(feature.index)
TB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['tb_replacement_d2_017'] = {'inputs': ['tb_replacement_017'], 'func': tb_replacement_d2_017}


def tb_replacement_d2_018(tb_replacement_018):
    feature = _clean(tb_replacement_018)
    delta = feature.diff(55)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00018000).reindex(feature.index)
TB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['tb_replacement_d2_018'] = {'inputs': ['tb_replacement_018'], 'func': tb_replacement_d2_018}


def tb_replacement_d2_019(tb_replacement_019):
    feature = _clean(tb_replacement_019)
    delta = feature.diff(89)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00019000).reindex(feature.index)
TB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['tb_replacement_d2_019'] = {'inputs': ['tb_replacement_019'], 'func': tb_replacement_d2_019}


def tb_replacement_d2_020(tb_replacement_020):
    feature = _clean(tb_replacement_020)
    delta = feature.diff(1)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00020000).reindex(feature.index)
TB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['tb_replacement_d2_020'] = {'inputs': ['tb_replacement_020'], 'func': tb_replacement_d2_020}


def tb_replacement_d2_021(tb_replacement_021):
    feature = _clean(tb_replacement_021)
    delta = feature.diff(2)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00021000).reindex(feature.index)
TB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['tb_replacement_d2_021'] = {'inputs': ['tb_replacement_021'], 'func': tb_replacement_d2_021}


def tb_replacement_d2_022(tb_replacement_022):
    feature = _clean(tb_replacement_022)
    delta = feature.diff(3)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00022000).reindex(feature.index)
TB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['tb_replacement_d2_022'] = {'inputs': ['tb_replacement_022'], 'func': tb_replacement_d2_022}


def tb_replacement_d2_023(tb_replacement_023):
    feature = _clean(tb_replacement_023)
    delta = feature.diff(5)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00023000).reindex(feature.index)
TB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['tb_replacement_d2_023'] = {'inputs': ['tb_replacement_023'], 'func': tb_replacement_d2_023}


def tb_replacement_d2_024(tb_replacement_024):
    feature = _clean(tb_replacement_024)
    delta = feature.diff(8)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00024000).reindex(feature.index)
TB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['tb_replacement_d2_024'] = {'inputs': ['tb_replacement_024'], 'func': tb_replacement_d2_024}


def tb_replacement_d2_025(tb_replacement_025):
    feature = _clean(tb_replacement_025)
    delta = feature.diff(13)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00025000).reindex(feature.index)
TB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['tb_replacement_d2_025'] = {'inputs': ['tb_replacement_025'], 'func': tb_replacement_d2_025}


def tb_replacement_d2_026(tb_replacement_026):
    feature = _clean(tb_replacement_026)
    delta = feature.diff(21)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00026000).reindex(feature.index)
TB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['tb_replacement_d2_026'] = {'inputs': ['tb_replacement_026'], 'func': tb_replacement_d2_026}


def tb_replacement_d2_027(tb_replacement_027):
    feature = _clean(tb_replacement_027)
    delta = feature.diff(34)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00027000).reindex(feature.index)
TB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['tb_replacement_d2_027'] = {'inputs': ['tb_replacement_027'], 'func': tb_replacement_d2_027}


def tb_replacement_d2_028(tb_replacement_028):
    feature = _clean(tb_replacement_028)
    delta = feature.diff(55)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00028000).reindex(feature.index)
TB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['tb_replacement_d2_028'] = {'inputs': ['tb_replacement_028'], 'func': tb_replacement_d2_028}


def tb_replacement_d2_029(tb_replacement_029):
    feature = _clean(tb_replacement_029)
    delta = feature.diff(89)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00029000).reindex(feature.index)
TB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['tb_replacement_d2_029'] = {'inputs': ['tb_replacement_029'], 'func': tb_replacement_d2_029}


def tb_replacement_d2_030(tb_replacement_030):
    feature = _clean(tb_replacement_030)
    delta = feature.diff(1)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00030000).reindex(feature.index)
TB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['tb_replacement_d2_030'] = {'inputs': ['tb_replacement_030'], 'func': tb_replacement_d2_030}


def tb_replacement_d2_031(tb_replacement_031):
    feature = _clean(tb_replacement_031)
    delta = feature.diff(2)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00031000).reindex(feature.index)
TB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['tb_replacement_d2_031'] = {'inputs': ['tb_replacement_031'], 'func': tb_replacement_d2_031}


def tb_replacement_d2_032(tb_replacement_032):
    feature = _clean(tb_replacement_032)
    delta = feature.diff(3)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00032000).reindex(feature.index)
TB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['tb_replacement_d2_032'] = {'inputs': ['tb_replacement_032'], 'func': tb_replacement_d2_032}


def tb_replacement_d2_033(tb_replacement_033):
    feature = _clean(tb_replacement_033)
    delta = feature.diff(5)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00033000).reindex(feature.index)
TB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['tb_replacement_d2_033'] = {'inputs': ['tb_replacement_033'], 'func': tb_replacement_d2_033}


def tb_replacement_d2_034(tb_replacement_034):
    feature = _clean(tb_replacement_034)
    delta = feature.diff(8)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00034000).reindex(feature.index)
TB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['tb_replacement_d2_034'] = {'inputs': ['tb_replacement_034'], 'func': tb_replacement_d2_034}


def tb_replacement_d2_035(tb_replacement_035):
    feature = _clean(tb_replacement_035)
    delta = feature.diff(13)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00035000).reindex(feature.index)
TB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['tb_replacement_d2_035'] = {'inputs': ['tb_replacement_035'], 'func': tb_replacement_d2_035}


def tb_replacement_d2_036(tb_replacement_036):
    feature = _clean(tb_replacement_036)
    delta = feature.diff(21)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00036000).reindex(feature.index)
TB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['tb_replacement_d2_036'] = {'inputs': ['tb_replacement_036'], 'func': tb_replacement_d2_036}


def tb_replacement_d2_037(tb_replacement_037):
    feature = _clean(tb_replacement_037)
    delta = feature.diff(34)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00037000).reindex(feature.index)
TB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['tb_replacement_d2_037'] = {'inputs': ['tb_replacement_037'], 'func': tb_replacement_d2_037}


def tb_replacement_d2_038(tb_replacement_038):
    feature = _clean(tb_replacement_038)
    delta = feature.diff(55)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00038000).reindex(feature.index)
TB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['tb_replacement_d2_038'] = {'inputs': ['tb_replacement_038'], 'func': tb_replacement_d2_038}


def tb_replacement_d2_039(tb_replacement_039):
    feature = _clean(tb_replacement_039)
    delta = feature.diff(89)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00039000).reindex(feature.index)
TB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['tb_replacement_d2_039'] = {'inputs': ['tb_replacement_039'], 'func': tb_replacement_d2_039}


def tb_replacement_d2_040(tb_replacement_040):
    feature = _clean(tb_replacement_040)
    delta = feature.diff(1)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00040000).reindex(feature.index)
TB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['tb_replacement_d2_040'] = {'inputs': ['tb_replacement_040'], 'func': tb_replacement_d2_040}


def tb_replacement_d2_041(tb_replacement_041):
    feature = _clean(tb_replacement_041)
    delta = feature.diff(2)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00041000).reindex(feature.index)
TB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['tb_replacement_d2_041'] = {'inputs': ['tb_replacement_041'], 'func': tb_replacement_d2_041}


def tb_replacement_d2_042(tb_replacement_042):
    feature = _clean(tb_replacement_042)
    delta = feature.diff(3)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00042000).reindex(feature.index)
TB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['tb_replacement_d2_042'] = {'inputs': ['tb_replacement_042'], 'func': tb_replacement_d2_042}


def tb_replacement_d2_043(tb_replacement_043):
    feature = _clean(tb_replacement_043)
    delta = feature.diff(5)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00043000).reindex(feature.index)
TB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['tb_replacement_d2_043'] = {'inputs': ['tb_replacement_043'], 'func': tb_replacement_d2_043}


def tb_replacement_d2_044(tb_replacement_044):
    feature = _clean(tb_replacement_044)
    delta = feature.diff(8)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00044000).reindex(feature.index)
TB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['tb_replacement_d2_044'] = {'inputs': ['tb_replacement_044'], 'func': tb_replacement_d2_044}


def tb_replacement_d2_045(tb_replacement_045):
    feature = _clean(tb_replacement_045)
    delta = feature.diff(13)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00045000).reindex(feature.index)
TB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['tb_replacement_d2_045'] = {'inputs': ['tb_replacement_045'], 'func': tb_replacement_d2_045}


def tb_replacement_d2_046(tb_replacement_046):
    feature = _clean(tb_replacement_046)
    delta = feature.diff(21)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00046000).reindex(feature.index)
TB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['tb_replacement_d2_046'] = {'inputs': ['tb_replacement_046'], 'func': tb_replacement_d2_046}


def tb_replacement_d2_047(tb_replacement_047):
    feature = _clean(tb_replacement_047)
    delta = feature.diff(34)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00047000).reindex(feature.index)
TB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['tb_replacement_d2_047'] = {'inputs': ['tb_replacement_047'], 'func': tb_replacement_d2_047}


def tb_replacement_d2_048(tb_replacement_048):
    feature = _clean(tb_replacement_048)
    delta = feature.diff(55)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00048000).reindex(feature.index)
TB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['tb_replacement_d2_048'] = {'inputs': ['tb_replacement_048'], 'func': tb_replacement_d2_048}


def tb_replacement_d2_049(tb_replacement_049):
    feature = _clean(tb_replacement_049)
    delta = feature.diff(89)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00049000).reindex(feature.index)
TB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['tb_replacement_d2_049'] = {'inputs': ['tb_replacement_049'], 'func': tb_replacement_d2_049}


def tb_replacement_d2_050(tb_replacement_050):
    feature = _clean(tb_replacement_050)
    delta = feature.diff(1)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00050000).reindex(feature.index)
TB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['tb_replacement_d2_050'] = {'inputs': ['tb_replacement_050'], 'func': tb_replacement_d2_050}


def tb_replacement_d2_051(tb_replacement_051):
    feature = _clean(tb_replacement_051)
    delta = feature.diff(2)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00051000).reindex(feature.index)
TB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['tb_replacement_d2_051'] = {'inputs': ['tb_replacement_051'], 'func': tb_replacement_d2_051}


def tb_replacement_d2_052(tb_replacement_052):
    feature = _clean(tb_replacement_052)
    delta = feature.diff(3)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00052000).reindex(feature.index)
TB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['tb_replacement_d2_052'] = {'inputs': ['tb_replacement_052'], 'func': tb_replacement_d2_052}


def tb_replacement_d2_053(tb_replacement_053):
    feature = _clean(tb_replacement_053)
    delta = feature.diff(5)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00053000).reindex(feature.index)
TB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['tb_replacement_d2_053'] = {'inputs': ['tb_replacement_053'], 'func': tb_replacement_d2_053}


def tb_replacement_d2_054(tb_replacement_054):
    feature = _clean(tb_replacement_054)
    delta = feature.diff(8)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00054000).reindex(feature.index)
TB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['tb_replacement_d2_054'] = {'inputs': ['tb_replacement_054'], 'func': tb_replacement_d2_054}


def tb_replacement_d2_055(tb_replacement_055):
    feature = _clean(tb_replacement_055)
    delta = feature.diff(13)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00055000).reindex(feature.index)
TB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['tb_replacement_d2_055'] = {'inputs': ['tb_replacement_055'], 'func': tb_replacement_d2_055}


def tb_replacement_d2_056(tb_replacement_056):
    feature = _clean(tb_replacement_056)
    delta = feature.diff(21)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00056000).reindex(feature.index)
TB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['tb_replacement_d2_056'] = {'inputs': ['tb_replacement_056'], 'func': tb_replacement_d2_056}


def tb_replacement_d2_057(tb_replacement_057):
    feature = _clean(tb_replacement_057)
    delta = feature.diff(34)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00057000).reindex(feature.index)
TB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['tb_replacement_d2_057'] = {'inputs': ['tb_replacement_057'], 'func': tb_replacement_d2_057}


def tb_replacement_d2_058(tb_replacement_058):
    feature = _clean(tb_replacement_058)
    delta = feature.diff(55)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00058000).reindex(feature.index)
TB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['tb_replacement_d2_058'] = {'inputs': ['tb_replacement_058'], 'func': tb_replacement_d2_058}


def tb_replacement_d2_059(tb_replacement_059):
    feature = _clean(tb_replacement_059)
    delta = feature.diff(89)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00059000).reindex(feature.index)
TB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['tb_replacement_d2_059'] = {'inputs': ['tb_replacement_059'], 'func': tb_replacement_d2_059}


def tb_replacement_d2_060(tb_replacement_060):
    feature = _clean(tb_replacement_060)
    delta = feature.diff(1)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00060000).reindex(feature.index)
TB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['tb_replacement_d2_060'] = {'inputs': ['tb_replacement_060'], 'func': tb_replacement_d2_060}


def tb_replacement_d2_061(tb_replacement_061):
    feature = _clean(tb_replacement_061)
    delta = feature.diff(2)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00061000).reindex(feature.index)
TB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['tb_replacement_d2_061'] = {'inputs': ['tb_replacement_061'], 'func': tb_replacement_d2_061}


def tb_replacement_d2_062(tb_replacement_062):
    feature = _clean(tb_replacement_062)
    delta = feature.diff(3)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00062000).reindex(feature.index)
TB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['tb_replacement_d2_062'] = {'inputs': ['tb_replacement_062'], 'func': tb_replacement_d2_062}


def tb_replacement_d2_063(tb_replacement_063):
    feature = _clean(tb_replacement_063)
    delta = feature.diff(5)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00063000).reindex(feature.index)
TB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['tb_replacement_d2_063'] = {'inputs': ['tb_replacement_063'], 'func': tb_replacement_d2_063}


def tb_replacement_d2_064(tb_replacement_064):
    feature = _clean(tb_replacement_064)
    delta = feature.diff(8)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00064000).reindex(feature.index)
TB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['tb_replacement_d2_064'] = {'inputs': ['tb_replacement_064'], 'func': tb_replacement_d2_064}


def tb_replacement_d2_065(tb_replacement_065):
    feature = _clean(tb_replacement_065)
    delta = feature.diff(13)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00065000).reindex(feature.index)
TB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['tb_replacement_d2_065'] = {'inputs': ['tb_replacement_065'], 'func': tb_replacement_d2_065}


def tb_replacement_d2_066(tb_replacement_066):
    feature = _clean(tb_replacement_066)
    delta = feature.diff(21)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00066000).reindex(feature.index)
TB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['tb_replacement_d2_066'] = {'inputs': ['tb_replacement_066'], 'func': tb_replacement_d2_066}


def tb_replacement_d2_067(tb_replacement_067):
    feature = _clean(tb_replacement_067)
    delta = feature.diff(34)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00067000).reindex(feature.index)
TB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['tb_replacement_d2_067'] = {'inputs': ['tb_replacement_067'], 'func': tb_replacement_d2_067}


def tb_replacement_d2_068(tb_replacement_068):
    feature = _clean(tb_replacement_068)
    delta = feature.diff(55)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00068000).reindex(feature.index)
TB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['tb_replacement_d2_068'] = {'inputs': ['tb_replacement_068'], 'func': tb_replacement_d2_068}


def tb_replacement_d2_069(tb_replacement_069):
    feature = _clean(tb_replacement_069)
    delta = feature.diff(89)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00069000).reindex(feature.index)
TB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['tb_replacement_d2_069'] = {'inputs': ['tb_replacement_069'], 'func': tb_replacement_d2_069}


def tb_replacement_d2_070(tb_replacement_070):
    feature = _clean(tb_replacement_070)
    delta = feature.diff(1)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00070000).reindex(feature.index)
TB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['tb_replacement_d2_070'] = {'inputs': ['tb_replacement_070'], 'func': tb_replacement_d2_070}


def tb_replacement_d2_071(tb_replacement_071):
    feature = _clean(tb_replacement_071)
    delta = feature.diff(2)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00071000).reindex(feature.index)
TB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['tb_replacement_d2_071'] = {'inputs': ['tb_replacement_071'], 'func': tb_replacement_d2_071}


def tb_replacement_d2_072(tb_replacement_072):
    feature = _clean(tb_replacement_072)
    delta = feature.diff(3)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00072000).reindex(feature.index)
TB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['tb_replacement_d2_072'] = {'inputs': ['tb_replacement_072'], 'func': tb_replacement_d2_072}


def tb_replacement_d2_073(tb_replacement_073):
    feature = _clean(tb_replacement_073)
    delta = feature.diff(5)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00073000).reindex(feature.index)
TB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['tb_replacement_d2_073'] = {'inputs': ['tb_replacement_073'], 'func': tb_replacement_d2_073}


def tb_replacement_d2_074(tb_replacement_074):
    feature = _clean(tb_replacement_074)
    delta = feature.diff(8)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00074000).reindex(feature.index)
TB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['tb_replacement_d2_074'] = {'inputs': ['tb_replacement_074'], 'func': tb_replacement_d2_074}


def tb_replacement_d2_075(tb_replacement_075):
    feature = _clean(tb_replacement_075)
    delta = feature.diff(13)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00075000).reindex(feature.index)
TB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['tb_replacement_d2_075'] = {'inputs': ['tb_replacement_075'], 'func': tb_replacement_d2_075}


def tb_replacement_d2_076(tb_replacement_076):
    feature = _clean(tb_replacement_076)
    delta = feature.diff(21)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00076000).reindex(feature.index)
TB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['tb_replacement_d2_076'] = {'inputs': ['tb_replacement_076'], 'func': tb_replacement_d2_076}


def tb_replacement_d2_077(tb_replacement_077):
    feature = _clean(tb_replacement_077)
    delta = feature.diff(34)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00077000).reindex(feature.index)
TB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['tb_replacement_d2_077'] = {'inputs': ['tb_replacement_077'], 'func': tb_replacement_d2_077}


def tb_replacement_d2_078(tb_replacement_078):
    feature = _clean(tb_replacement_078)
    delta = feature.diff(55)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00078000).reindex(feature.index)
TB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['tb_replacement_d2_078'] = {'inputs': ['tb_replacement_078'], 'func': tb_replacement_d2_078}


def tb_replacement_d2_079(tb_replacement_079):
    feature = _clean(tb_replacement_079)
    delta = feature.diff(89)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00079000).reindex(feature.index)
TB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['tb_replacement_d2_079'] = {'inputs': ['tb_replacement_079'], 'func': tb_replacement_d2_079}


def tb_replacement_d2_080(tb_replacement_080):
    feature = _clean(tb_replacement_080)
    delta = feature.diff(1)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00080000).reindex(feature.index)
TB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['tb_replacement_d2_080'] = {'inputs': ['tb_replacement_080'], 'func': tb_replacement_d2_080}


def tb_replacement_d2_081(tb_replacement_081):
    feature = _clean(tb_replacement_081)
    delta = feature.diff(2)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00081000).reindex(feature.index)
TB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['tb_replacement_d2_081'] = {'inputs': ['tb_replacement_081'], 'func': tb_replacement_d2_081}


def tb_replacement_d2_082(tb_replacement_082):
    feature = _clean(tb_replacement_082)
    delta = feature.diff(3)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00082000).reindex(feature.index)
TB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['tb_replacement_d2_082'] = {'inputs': ['tb_replacement_082'], 'func': tb_replacement_d2_082}


def tb_replacement_d2_083(tb_replacement_083):
    feature = _clean(tb_replacement_083)
    delta = feature.diff(5)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00083000).reindex(feature.index)
TB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['tb_replacement_d2_083'] = {'inputs': ['tb_replacement_083'], 'func': tb_replacement_d2_083}


def tb_replacement_d2_084(tb_replacement_084):
    feature = _clean(tb_replacement_084)
    delta = feature.diff(8)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00084000).reindex(feature.index)
TB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['tb_replacement_d2_084'] = {'inputs': ['tb_replacement_084'], 'func': tb_replacement_d2_084}


def tb_replacement_d2_085(tb_replacement_085):
    feature = _clean(tb_replacement_085)
    delta = feature.diff(13)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00085000).reindex(feature.index)
TB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['tb_replacement_d2_085'] = {'inputs': ['tb_replacement_085'], 'func': tb_replacement_d2_085}


def tb_replacement_d2_086(tb_replacement_086):
    feature = _clean(tb_replacement_086)
    delta = feature.diff(21)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00086000).reindex(feature.index)
TB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['tb_replacement_d2_086'] = {'inputs': ['tb_replacement_086'], 'func': tb_replacement_d2_086}


def tb_replacement_d2_087(tb_replacement_087):
    feature = _clean(tb_replacement_087)
    delta = feature.diff(34)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00087000).reindex(feature.index)
TB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['tb_replacement_d2_087'] = {'inputs': ['tb_replacement_087'], 'func': tb_replacement_d2_087}


def tb_replacement_d2_088(tb_replacement_088):
    feature = _clean(tb_replacement_088)
    delta = feature.diff(55)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00088000).reindex(feature.index)
TB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['tb_replacement_d2_088'] = {'inputs': ['tb_replacement_088'], 'func': tb_replacement_d2_088}


def tb_replacement_d2_089(tb_replacement_089):
    feature = _clean(tb_replacement_089)
    delta = feature.diff(89)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00089000).reindex(feature.index)
TB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['tb_replacement_d2_089'] = {'inputs': ['tb_replacement_089'], 'func': tb_replacement_d2_089}


def tb_replacement_d2_090(tb_replacement_090):
    feature = _clean(tb_replacement_090)
    delta = feature.diff(1)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00090000).reindex(feature.index)
TB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['tb_replacement_d2_090'] = {'inputs': ['tb_replacement_090'], 'func': tb_replacement_d2_090}


def tb_replacement_d2_091(tb_replacement_091):
    feature = _clean(tb_replacement_091)
    delta = feature.diff(2)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00091000).reindex(feature.index)
TB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['tb_replacement_d2_091'] = {'inputs': ['tb_replacement_091'], 'func': tb_replacement_d2_091}


def tb_replacement_d2_092(tb_replacement_092):
    feature = _clean(tb_replacement_092)
    delta = feature.diff(3)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00092000).reindex(feature.index)
TB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['tb_replacement_d2_092'] = {'inputs': ['tb_replacement_092'], 'func': tb_replacement_d2_092}


def tb_replacement_d2_093(tb_replacement_093):
    feature = _clean(tb_replacement_093)
    delta = feature.diff(5)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00093000).reindex(feature.index)
TB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['tb_replacement_d2_093'] = {'inputs': ['tb_replacement_093'], 'func': tb_replacement_d2_093}


def tb_replacement_d2_094(tb_replacement_094):
    feature = _clean(tb_replacement_094)
    delta = feature.diff(8)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00094000).reindex(feature.index)
TB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['tb_replacement_d2_094'] = {'inputs': ['tb_replacement_094'], 'func': tb_replacement_d2_094}


def tb_replacement_d2_095(tb_replacement_095):
    feature = _clean(tb_replacement_095)
    delta = feature.diff(13)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00095000).reindex(feature.index)
TB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['tb_replacement_d2_095'] = {'inputs': ['tb_replacement_095'], 'func': tb_replacement_d2_095}


def tb_replacement_d2_096(tb_replacement_096):
    feature = _clean(tb_replacement_096)
    delta = feature.diff(21)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00096000).reindex(feature.index)
TB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['tb_replacement_d2_096'] = {'inputs': ['tb_replacement_096'], 'func': tb_replacement_d2_096}


def tb_replacement_d2_097(tb_replacement_097):
    feature = _clean(tb_replacement_097)
    delta = feature.diff(34)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00097000).reindex(feature.index)
TB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['tb_replacement_d2_097'] = {'inputs': ['tb_replacement_097'], 'func': tb_replacement_d2_097}


def tb_replacement_d2_098(tb_replacement_098):
    feature = _clean(tb_replacement_098)
    delta = feature.diff(55)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00098000).reindex(feature.index)
TB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['tb_replacement_d2_098'] = {'inputs': ['tb_replacement_098'], 'func': tb_replacement_d2_098}


def tb_replacement_d2_099(tb_replacement_099):
    feature = _clean(tb_replacement_099)
    delta = feature.diff(89)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00099000).reindex(feature.index)
TB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['tb_replacement_d2_099'] = {'inputs': ['tb_replacement_099'], 'func': tb_replacement_d2_099}


def tb_replacement_d2_100(tb_replacement_100):
    feature = _clean(tb_replacement_100)
    delta = feature.diff(1)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00100000).reindex(feature.index)
TB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['tb_replacement_d2_100'] = {'inputs': ['tb_replacement_100'], 'func': tb_replacement_d2_100}


def tb_replacement_d2_101(tb_replacement_101):
    feature = _clean(tb_replacement_101)
    delta = feature.diff(2)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00101000).reindex(feature.index)
TB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['tb_replacement_d2_101'] = {'inputs': ['tb_replacement_101'], 'func': tb_replacement_d2_101}


def tb_replacement_d2_102(tb_replacement_102):
    feature = _clean(tb_replacement_102)
    delta = feature.diff(3)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00102000).reindex(feature.index)
TB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['tb_replacement_d2_102'] = {'inputs': ['tb_replacement_102'], 'func': tb_replacement_d2_102}


def tb_replacement_d2_103(tb_replacement_103):
    feature = _clean(tb_replacement_103)
    delta = feature.diff(5)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00103000).reindex(feature.index)
TB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['tb_replacement_d2_103'] = {'inputs': ['tb_replacement_103'], 'func': tb_replacement_d2_103}


def tb_replacement_d2_104(tb_replacement_104):
    feature = _clean(tb_replacement_104)
    delta = feature.diff(8)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00104000).reindex(feature.index)
TB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['tb_replacement_d2_104'] = {'inputs': ['tb_replacement_104'], 'func': tb_replacement_d2_104}


def tb_replacement_d2_105(tb_replacement_105):
    feature = _clean(tb_replacement_105)
    delta = feature.diff(13)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00105000).reindex(feature.index)
TB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['tb_replacement_d2_105'] = {'inputs': ['tb_replacement_105'], 'func': tb_replacement_d2_105}


def tb_replacement_d2_106(tb_replacement_106):
    feature = _clean(tb_replacement_106)
    delta = feature.diff(21)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00106000).reindex(feature.index)
TB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['tb_replacement_d2_106'] = {'inputs': ['tb_replacement_106'], 'func': tb_replacement_d2_106}


def tb_replacement_d2_107(tb_replacement_107):
    feature = _clean(tb_replacement_107)
    delta = feature.diff(34)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00107000).reindex(feature.index)
TB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['tb_replacement_d2_107'] = {'inputs': ['tb_replacement_107'], 'func': tb_replacement_d2_107}


def tb_replacement_d2_108(tb_replacement_108):
    feature = _clean(tb_replacement_108)
    delta = feature.diff(55)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00108000).reindex(feature.index)
TB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['tb_replacement_d2_108'] = {'inputs': ['tb_replacement_108'], 'func': tb_replacement_d2_108}


def tb_replacement_d2_109(tb_replacement_109):
    feature = _clean(tb_replacement_109)
    delta = feature.diff(89)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00109000).reindex(feature.index)
TB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['tb_replacement_d2_109'] = {'inputs': ['tb_replacement_109'], 'func': tb_replacement_d2_109}


def tb_replacement_d2_110(tb_replacement_110):
    feature = _clean(tb_replacement_110)
    delta = feature.diff(1)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00110000).reindex(feature.index)
TB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['tb_replacement_d2_110'] = {'inputs': ['tb_replacement_110'], 'func': tb_replacement_d2_110}


def tb_replacement_d2_111(tb_replacement_111):
    feature = _clean(tb_replacement_111)
    delta = feature.diff(2)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00111000).reindex(feature.index)
TB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['tb_replacement_d2_111'] = {'inputs': ['tb_replacement_111'], 'func': tb_replacement_d2_111}


def tb_replacement_d2_112(tb_replacement_112):
    feature = _clean(tb_replacement_112)
    delta = feature.diff(3)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00112000).reindex(feature.index)
TB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['tb_replacement_d2_112'] = {'inputs': ['tb_replacement_112'], 'func': tb_replacement_d2_112}


def tb_replacement_d2_113(tb_replacement_113):
    feature = _clean(tb_replacement_113)
    delta = feature.diff(5)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00113000).reindex(feature.index)
TB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['tb_replacement_d2_113'] = {'inputs': ['tb_replacement_113'], 'func': tb_replacement_d2_113}


def tb_replacement_d2_114(tb_replacement_114):
    feature = _clean(tb_replacement_114)
    delta = feature.diff(8)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00114000).reindex(feature.index)
TB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['tb_replacement_d2_114'] = {'inputs': ['tb_replacement_114'], 'func': tb_replacement_d2_114}


def tb_replacement_d2_115(tb_replacement_115):
    feature = _clean(tb_replacement_115)
    delta = feature.diff(13)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00115000).reindex(feature.index)
TB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['tb_replacement_d2_115'] = {'inputs': ['tb_replacement_115'], 'func': tb_replacement_d2_115}


def tb_replacement_d2_116(tb_replacement_116):
    feature = _clean(tb_replacement_116)
    delta = feature.diff(21)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00116000).reindex(feature.index)
TB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['tb_replacement_d2_116'] = {'inputs': ['tb_replacement_116'], 'func': tb_replacement_d2_116}


def tb_replacement_d2_117(tb_replacement_117):
    feature = _clean(tb_replacement_117)
    delta = feature.diff(34)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00117000).reindex(feature.index)
TB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['tb_replacement_d2_117'] = {'inputs': ['tb_replacement_117'], 'func': tb_replacement_d2_117}


def tb_replacement_d2_118(tb_replacement_118):
    feature = _clean(tb_replacement_118)
    delta = feature.diff(55)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00118000).reindex(feature.index)
TB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['tb_replacement_d2_118'] = {'inputs': ['tb_replacement_118'], 'func': tb_replacement_d2_118}


def tb_replacement_d2_119(tb_replacement_119):
    feature = _clean(tb_replacement_119)
    delta = feature.diff(89)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00119000).reindex(feature.index)
TB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['tb_replacement_d2_119'] = {'inputs': ['tb_replacement_119'], 'func': tb_replacement_d2_119}


def tb_replacement_d2_120(tb_replacement_120):
    feature = _clean(tb_replacement_120)
    delta = feature.diff(1)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00120000).reindex(feature.index)
TB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['tb_replacement_d2_120'] = {'inputs': ['tb_replacement_120'], 'func': tb_replacement_d2_120}


def tb_replacement_d2_121(tb_replacement_121):
    feature = _clean(tb_replacement_121)
    delta = feature.diff(2)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00121000).reindex(feature.index)
TB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['tb_replacement_d2_121'] = {'inputs': ['tb_replacement_121'], 'func': tb_replacement_d2_121}


def tb_replacement_d2_122(tb_replacement_122):
    feature = _clean(tb_replacement_122)
    delta = feature.diff(3)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00122000).reindex(feature.index)
TB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['tb_replacement_d2_122'] = {'inputs': ['tb_replacement_122'], 'func': tb_replacement_d2_122}


def tb_replacement_d2_123(tb_replacement_123):
    feature = _clean(tb_replacement_123)
    delta = feature.diff(5)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00123000).reindex(feature.index)
TB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['tb_replacement_d2_123'] = {'inputs': ['tb_replacement_123'], 'func': tb_replacement_d2_123}


def tb_replacement_d2_124(tb_replacement_124):
    feature = _clean(tb_replacement_124)
    delta = feature.diff(8)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00124000).reindex(feature.index)
TB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['tb_replacement_d2_124'] = {'inputs': ['tb_replacement_124'], 'func': tb_replacement_d2_124}


def tb_replacement_d2_125(tb_replacement_125):
    feature = _clean(tb_replacement_125)
    delta = feature.diff(13)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00125000).reindex(feature.index)
TB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['tb_replacement_d2_125'] = {'inputs': ['tb_replacement_125'], 'func': tb_replacement_d2_125}


def tb_replacement_d2_126(tb_replacement_126):
    feature = _clean(tb_replacement_126)
    delta = feature.diff(21)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00126000).reindex(feature.index)
TB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['tb_replacement_d2_126'] = {'inputs': ['tb_replacement_126'], 'func': tb_replacement_d2_126}


def tb_replacement_d2_127(tb_replacement_127):
    feature = _clean(tb_replacement_127)
    delta = feature.diff(34)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00127000).reindex(feature.index)
TB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['tb_replacement_d2_127'] = {'inputs': ['tb_replacement_127'], 'func': tb_replacement_d2_127}


def tb_replacement_d2_128(tb_replacement_128):
    feature = _clean(tb_replacement_128)
    delta = feature.diff(55)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00128000).reindex(feature.index)
TB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['tb_replacement_d2_128'] = {'inputs': ['tb_replacement_128'], 'func': tb_replacement_d2_128}


def tb_replacement_d2_129(tb_replacement_129):
    feature = _clean(tb_replacement_129)
    delta = feature.diff(89)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00129000).reindex(feature.index)
TB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['tb_replacement_d2_129'] = {'inputs': ['tb_replacement_129'], 'func': tb_replacement_d2_129}


def tb_replacement_d2_130(tb_replacement_130):
    feature = _clean(tb_replacement_130)
    delta = feature.diff(1)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00130000).reindex(feature.index)
TB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['tb_replacement_d2_130'] = {'inputs': ['tb_replacement_130'], 'func': tb_replacement_d2_130}


def tb_replacement_d2_131(tb_replacement_131):
    feature = _clean(tb_replacement_131)
    delta = feature.diff(2)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00131000).reindex(feature.index)
TB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['tb_replacement_d2_131'] = {'inputs': ['tb_replacement_131'], 'func': tb_replacement_d2_131}


def tb_replacement_d2_132(tb_replacement_132):
    feature = _clean(tb_replacement_132)
    delta = feature.diff(3)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00132000).reindex(feature.index)
TB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['tb_replacement_d2_132'] = {'inputs': ['tb_replacement_132'], 'func': tb_replacement_d2_132}


def tb_replacement_d2_133(tb_replacement_133):
    feature = _clean(tb_replacement_133)
    delta = feature.diff(5)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00133000).reindex(feature.index)
TB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['tb_replacement_d2_133'] = {'inputs': ['tb_replacement_133'], 'func': tb_replacement_d2_133}


def tb_replacement_d2_134(tb_replacement_134):
    feature = _clean(tb_replacement_134)
    delta = feature.diff(8)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00134000).reindex(feature.index)
TB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['tb_replacement_d2_134'] = {'inputs': ['tb_replacement_134'], 'func': tb_replacement_d2_134}


def tb_replacement_d2_135(tb_replacement_135):
    feature = _clean(tb_replacement_135)
    delta = feature.diff(13)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00135000).reindex(feature.index)
TB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['tb_replacement_d2_135'] = {'inputs': ['tb_replacement_135'], 'func': tb_replacement_d2_135}


def tb_replacement_d2_136(tb_replacement_136):
    feature = _clean(tb_replacement_136)
    delta = feature.diff(21)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00136000).reindex(feature.index)
TB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['tb_replacement_d2_136'] = {'inputs': ['tb_replacement_136'], 'func': tb_replacement_d2_136}


def tb_replacement_d2_137(tb_replacement_137):
    feature = _clean(tb_replacement_137)
    delta = feature.diff(34)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00137000).reindex(feature.index)
TB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['tb_replacement_d2_137'] = {'inputs': ['tb_replacement_137'], 'func': tb_replacement_d2_137}


def tb_replacement_d2_138(tb_replacement_138):
    feature = _clean(tb_replacement_138)
    delta = feature.diff(55)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00138000).reindex(feature.index)
TB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['tb_replacement_d2_138'] = {'inputs': ['tb_replacement_138'], 'func': tb_replacement_d2_138}


def tb_replacement_d2_139(tb_replacement_139):
    feature = _clean(tb_replacement_139)
    delta = feature.diff(89)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00139000).reindex(feature.index)
TB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['tb_replacement_d2_139'] = {'inputs': ['tb_replacement_139'], 'func': tb_replacement_d2_139}


def tb_replacement_d2_140(tb_replacement_140):
    feature = _clean(tb_replacement_140)
    delta = feature.diff(1)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00140000).reindex(feature.index)
TB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['tb_replacement_d2_140'] = {'inputs': ['tb_replacement_140'], 'func': tb_replacement_d2_140}


def tb_replacement_d2_141(tb_replacement_141):
    feature = _clean(tb_replacement_141)
    delta = feature.diff(2)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00141000).reindex(feature.index)
TB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['tb_replacement_d2_141'] = {'inputs': ['tb_replacement_141'], 'func': tb_replacement_d2_141}


def tb_replacement_d2_142(tb_replacement_142):
    feature = _clean(tb_replacement_142)
    delta = feature.diff(3)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00142000).reindex(feature.index)
TB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['tb_replacement_d2_142'] = {'inputs': ['tb_replacement_142'], 'func': tb_replacement_d2_142}


def tb_replacement_d2_143(tb_replacement_143):
    feature = _clean(tb_replacement_143)
    delta = feature.diff(5)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00143000).reindex(feature.index)
TB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['tb_replacement_d2_143'] = {'inputs': ['tb_replacement_143'], 'func': tb_replacement_d2_143}


def tb_replacement_d2_144(tb_replacement_144):
    feature = _clean(tb_replacement_144)
    delta = feature.diff(8)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00144000).reindex(feature.index)
TB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['tb_replacement_d2_144'] = {'inputs': ['tb_replacement_144'], 'func': tb_replacement_d2_144}


def tb_replacement_d2_145(tb_replacement_145):
    feature = _clean(tb_replacement_145)
    delta = feature.diff(13)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00145000).reindex(feature.index)
TB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['tb_replacement_d2_145'] = {'inputs': ['tb_replacement_145'], 'func': tb_replacement_d2_145}


def tb_replacement_d2_146(tb_replacement_146):
    feature = _clean(tb_replacement_146)
    delta = feature.diff(21)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00146000).reindex(feature.index)
TB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['tb_replacement_d2_146'] = {'inputs': ['tb_replacement_146'], 'func': tb_replacement_d2_146}


def tb_replacement_d2_147(tb_replacement_147):
    feature = _clean(tb_replacement_147)
    delta = feature.diff(34)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00147000).reindex(feature.index)
TB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['tb_replacement_d2_147'] = {'inputs': ['tb_replacement_147'], 'func': tb_replacement_d2_147}


def tb_replacement_d2_148(tb_replacement_148):
    feature = _clean(tb_replacement_148)
    delta = feature.diff(55)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00148000).reindex(feature.index)
TB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['tb_replacement_d2_148'] = {'inputs': ['tb_replacement_148'], 'func': tb_replacement_d2_148}


def tb_replacement_d2_149(tb_replacement_149):
    feature = _clean(tb_replacement_149)
    delta = feature.diff(89)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00149000).reindex(feature.index)
TB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['tb_replacement_d2_149'] = {'inputs': ['tb_replacement_149'], 'func': tb_replacement_d2_149}


def tb_replacement_d2_150(tb_replacement_150):
    feature = _clean(tb_replacement_150)
    delta = feature.diff(1)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00150000).reindex(feature.index)
TB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['tb_replacement_d2_150'] = {'inputs': ['tb_replacement_150'], 'func': tb_replacement_d2_150}


def tb_replacement_d2_151(tb_replacement_151):
    feature = _clean(tb_replacement_151)
    delta = feature.diff(2)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00151000).reindex(feature.index)
TB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['tb_replacement_d2_151'] = {'inputs': ['tb_replacement_151'], 'func': tb_replacement_d2_151}


def tb_replacement_d2_152(tb_replacement_152):
    feature = _clean(tb_replacement_152)
    delta = feature.diff(3)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00152000).reindex(feature.index)
TB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['tb_replacement_d2_152'] = {'inputs': ['tb_replacement_152'], 'func': tb_replacement_d2_152}


def tb_replacement_d2_153(tb_replacement_153):
    feature = _clean(tb_replacement_153)
    delta = feature.diff(5)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00153000).reindex(feature.index)
TB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['tb_replacement_d2_153'] = {'inputs': ['tb_replacement_153'], 'func': tb_replacement_d2_153}


def tb_replacement_d2_154(tb_replacement_154):
    feature = _clean(tb_replacement_154)
    delta = feature.diff(8)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00154000).reindex(feature.index)
TB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['tb_replacement_d2_154'] = {'inputs': ['tb_replacement_154'], 'func': tb_replacement_d2_154}


def tb_replacement_d2_155(tb_replacement_155):
    feature = _clean(tb_replacement_155)
    delta = feature.diff(13)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00155000).reindex(feature.index)
TB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['tb_replacement_d2_155'] = {'inputs': ['tb_replacement_155'], 'func': tb_replacement_d2_155}


def tb_replacement_d2_156(tb_replacement_156):
    feature = _clean(tb_replacement_156)
    delta = feature.diff(21)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00156000).reindex(feature.index)
TB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['tb_replacement_d2_156'] = {'inputs': ['tb_replacement_156'], 'func': tb_replacement_d2_156}


def tb_replacement_d2_157(tb_replacement_157):
    feature = _clean(tb_replacement_157)
    delta = feature.diff(34)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00157000).reindex(feature.index)
TB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['tb_replacement_d2_157'] = {'inputs': ['tb_replacement_157'], 'func': tb_replacement_d2_157}


def tb_replacement_d2_158(tb_replacement_158):
    feature = _clean(tb_replacement_158)
    delta = feature.diff(55)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00158000).reindex(feature.index)
TB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['tb_replacement_d2_158'] = {'inputs': ['tb_replacement_158'], 'func': tb_replacement_d2_158}


def tb_replacement_d2_159(tb_replacement_159):
    feature = _clean(tb_replacement_159)
    delta = feature.diff(89)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00159000).reindex(feature.index)
TB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['tb_replacement_d2_159'] = {'inputs': ['tb_replacement_159'], 'func': tb_replacement_d2_159}


def tb_replacement_d2_160(tb_replacement_160):
    feature = _clean(tb_replacement_160)
    delta = feature.diff(1)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00160000).reindex(feature.index)
TB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['tb_replacement_d2_160'] = {'inputs': ['tb_replacement_160'], 'func': tb_replacement_d2_160}


def tb_replacement_d2_161(tb_replacement_161):
    feature = _clean(tb_replacement_161)
    delta = feature.diff(2)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00161000).reindex(feature.index)
TB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['tb_replacement_d2_161'] = {'inputs': ['tb_replacement_161'], 'func': tb_replacement_d2_161}


def tb_replacement_d2_162(tb_replacement_162):
    feature = _clean(tb_replacement_162)
    delta = feature.diff(3)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00162000).reindex(feature.index)
TB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['tb_replacement_d2_162'] = {'inputs': ['tb_replacement_162'], 'func': tb_replacement_d2_162}


def tb_replacement_d2_163(tb_replacement_163):
    feature = _clean(tb_replacement_163)
    delta = feature.diff(5)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00163000).reindex(feature.index)
TB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['tb_replacement_d2_163'] = {'inputs': ['tb_replacement_163'], 'func': tb_replacement_d2_163}


def tb_replacement_d2_164(tb_replacement_164):
    feature = _clean(tb_replacement_164)
    delta = feature.diff(8)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00164000).reindex(feature.index)
TB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['tb_replacement_d2_164'] = {'inputs': ['tb_replacement_164'], 'func': tb_replacement_d2_164}


def tb_replacement_d2_165(tb_replacement_165):
    feature = _clean(tb_replacement_165)
    delta = feature.diff(13)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00165000).reindex(feature.index)
TB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['tb_replacement_d2_165'] = {'inputs': ['tb_replacement_165'], 'func': tb_replacement_d2_165}


def tb_replacement_d2_166(tb_replacement_166):
    feature = _clean(tb_replacement_166)
    delta = feature.diff(21)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00166000).reindex(feature.index)
TB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['tb_replacement_d2_166'] = {'inputs': ['tb_replacement_166'], 'func': tb_replacement_d2_166}


def tb_replacement_d2_167(tb_replacement_167):
    feature = _clean(tb_replacement_167)
    delta = feature.diff(34)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00167000).reindex(feature.index)
TB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['tb_replacement_d2_167'] = {'inputs': ['tb_replacement_167'], 'func': tb_replacement_d2_167}


def tb_replacement_d2_168(tb_replacement_168):
    feature = _clean(tb_replacement_168)
    delta = feature.diff(55)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00168000).reindex(feature.index)
TB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['tb_replacement_d2_168'] = {'inputs': ['tb_replacement_168'], 'func': tb_replacement_d2_168}


def tb_replacement_d2_169(tb_replacement_169):
    feature = _clean(tb_replacement_169)
    delta = feature.diff(89)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00169000).reindex(feature.index)
TB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['tb_replacement_d2_169'] = {'inputs': ['tb_replacement_169'], 'func': tb_replacement_d2_169}


def tb_replacement_d2_170(tb_replacement_170):
    feature = _clean(tb_replacement_170)
    delta = feature.diff(1)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00170000).reindex(feature.index)
TB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['tb_replacement_d2_170'] = {'inputs': ['tb_replacement_170'], 'func': tb_replacement_d2_170}


def tb_replacement_d2_171(tb_replacement_171):
    feature = _clean(tb_replacement_171)
    delta = feature.diff(2)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00171000).reindex(feature.index)
TB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['tb_replacement_d2_171'] = {'inputs': ['tb_replacement_171'], 'func': tb_replacement_d2_171}


def tb_replacement_d2_172(tb_replacement_172):
    feature = _clean(tb_replacement_172)
    delta = feature.diff(3)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00172000).reindex(feature.index)
TB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['tb_replacement_d2_172'] = {'inputs': ['tb_replacement_172'], 'func': tb_replacement_d2_172}


def tb_replacement_d2_173(tb_replacement_173):
    feature = _clean(tb_replacement_173)
    delta = feature.diff(5)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00173000).reindex(feature.index)
TB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['tb_replacement_d2_173'] = {'inputs': ['tb_replacement_173'], 'func': tb_replacement_d2_173}


def tb_replacement_d2_174(tb_replacement_174):
    feature = _clean(tb_replacement_174)
    delta = feature.diff(8)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00174000).reindex(feature.index)
TB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['tb_replacement_d2_174'] = {'inputs': ['tb_replacement_174'], 'func': tb_replacement_d2_174}


def tb_replacement_d2_175(tb_replacement_175):
    feature = _clean(tb_replacement_175)
    delta = feature.diff(13)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00175000).reindex(feature.index)
TB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['tb_replacement_d2_175'] = {'inputs': ['tb_replacement_175'], 'func': tb_replacement_d2_175}


# Base-universe derivative extensions for repaired first-base features.
TBD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY = {}


def _base_universe_d2(feature, idx):
    feature = _clean(feature) if '_clean' in globals() else _s(feature).replace([np.inf, -np.inf], np.nan)
    windows = [1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    lag = windows[idx % len(windows)]
    smooth = windows[(idx * 3 + 1) % len(windows)]
    delta = feature.diff(lag)
    local = feature - feature.rolling(max(3, smooth), min_periods=2).mean()
    out = delta + local.fillna(0.0) * (0.00037 * ((idx % 17) + 1))
    return out.replace([np.inf, -np.inf], np.nan).reindex(feature.index)


def tbd_base_universe_d2_001_tbd_003_loss_streak_21_003(tbd_003_loss_streak_21_003):
    return _base_universe_d2(tbd_003_loss_streak_21_003, 1)
TBD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['tbd_base_universe_d2_001_tbd_003_loss_streak_21_003'] = {'inputs': ['tbd_003_loss_streak_21_003'], 'func': tbd_base_universe_d2_001_tbd_003_loss_streak_21_003}


def tbd_base_universe_d2_002_tbd_004_ma_distance_42_004(tbd_004_ma_distance_42_004):
    return _base_universe_d2(tbd_004_ma_distance_42_004, 2)
TBD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['tbd_base_universe_d2_002_tbd_004_ma_distance_42_004'] = {'inputs': ['tbd_004_ma_distance_42_004'], 'func': tbd_base_universe_d2_002_tbd_004_ma_distance_42_004}


def tbd_base_universe_d2_003_tbd_005_stochastic_position_63_005(tbd_005_stochastic_position_63_005):
    return _base_universe_d2(tbd_005_stochastic_position_63_005, 3)
TBD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['tbd_base_universe_d2_003_tbd_005_stochastic_position_63_005'] = {'inputs': ['tbd_005_stochastic_position_63_005'], 'func': tbd_base_universe_d2_003_tbd_005_stochastic_position_63_005}


def tbd_base_universe_d2_004_tbd_009_loss_streak_252_009(tbd_009_loss_streak_252_009):
    return _base_universe_d2(tbd_009_loss_streak_252_009, 4)
TBD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['tbd_base_universe_d2_004_tbd_009_loss_streak_252_009'] = {'inputs': ['tbd_009_loss_streak_252_009'], 'func': tbd_base_universe_d2_004_tbd_009_loss_streak_252_009}


def tbd_base_universe_d2_005_tbd_010_ma_distance_378_010(tbd_010_ma_distance_378_010):
    return _base_universe_d2(tbd_010_ma_distance_378_010, 5)
TBD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['tbd_base_universe_d2_005_tbd_010_ma_distance_378_010'] = {'inputs': ['tbd_010_ma_distance_378_010'], 'func': tbd_base_universe_d2_005_tbd_010_ma_distance_378_010}


def tbd_base_universe_d2_006_tbd_011_stochastic_position_504_011(tbd_011_stochastic_position_504_011):
    return _base_universe_d2(tbd_011_stochastic_position_504_011, 6)
TBD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['tbd_base_universe_d2_006_tbd_011_stochastic_position_504_011'] = {'inputs': ['tbd_011_stochastic_position_504_011'], 'func': tbd_base_universe_d2_006_tbd_011_stochastic_position_504_011}


def tbd_base_universe_d2_007_tbd_015_loss_streak_1512_015(tbd_015_loss_streak_1512_015):
    return _base_universe_d2(tbd_015_loss_streak_1512_015, 7)
TBD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['tbd_base_universe_d2_007_tbd_015_loss_streak_1512_015'] = {'inputs': ['tbd_015_loss_streak_1512_015'], 'func': tbd_base_universe_d2_007_tbd_015_loss_streak_1512_015}


def tbd_base_universe_d2_008_tbd_016_ma_distance_5_016(tbd_016_ma_distance_5_016):
    return _base_universe_d2(tbd_016_ma_distance_5_016, 8)
TBD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['tbd_base_universe_d2_008_tbd_016_ma_distance_5_016'] = {'inputs': ['tbd_016_ma_distance_5_016'], 'func': tbd_base_universe_d2_008_tbd_016_ma_distance_5_016}


def tbd_base_universe_d2_009_tbd_017_stochastic_position_10_017(tbd_017_stochastic_position_10_017):
    return _base_universe_d2(tbd_017_stochastic_position_10_017, 9)
TBD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['tbd_base_universe_d2_009_tbd_017_stochastic_position_10_017'] = {'inputs': ['tbd_017_stochastic_position_10_017'], 'func': tbd_base_universe_d2_009_tbd_017_stochastic_position_10_017}


def tbd_base_universe_d2_010_tbd_021_loss_streak_84_021(tbd_021_loss_streak_84_021):
    return _base_universe_d2(tbd_021_loss_streak_84_021, 10)
TBD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['tbd_base_universe_d2_010_tbd_021_loss_streak_84_021'] = {'inputs': ['tbd_021_loss_streak_84_021'], 'func': tbd_base_universe_d2_010_tbd_021_loss_streak_84_021}


def tbd_base_universe_d2_011_tbd_022_ma_distance_126_022(tbd_022_ma_distance_126_022):
    return _base_universe_d2(tbd_022_ma_distance_126_022, 11)
TBD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['tbd_base_universe_d2_011_tbd_022_ma_distance_126_022'] = {'inputs': ['tbd_022_ma_distance_126_022'], 'func': tbd_base_universe_d2_011_tbd_022_ma_distance_126_022}


def tbd_base_universe_d2_012_tbd_023_stochastic_position_189_023(tbd_023_stochastic_position_189_023):
    return _base_universe_d2(tbd_023_stochastic_position_189_023, 12)
TBD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['tbd_base_universe_d2_012_tbd_023_stochastic_position_189_023'] = {'inputs': ['tbd_023_stochastic_position_189_023'], 'func': tbd_base_universe_d2_012_tbd_023_stochastic_position_189_023}


def tbd_base_universe_d2_013_tbd_027_loss_streak_756_027(tbd_027_loss_streak_756_027):
    return _base_universe_d2(tbd_027_loss_streak_756_027, 13)
TBD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['tbd_base_universe_d2_013_tbd_027_loss_streak_756_027'] = {'inputs': ['tbd_027_loss_streak_756_027'], 'func': tbd_base_universe_d2_013_tbd_027_loss_streak_756_027}


def tbd_base_universe_d2_014_tbd_028_ma_distance_1008_028(tbd_028_ma_distance_1008_028):
    return _base_universe_d2(tbd_028_ma_distance_1008_028, 14)
TBD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['tbd_base_universe_d2_014_tbd_028_ma_distance_1008_028'] = {'inputs': ['tbd_028_ma_distance_1008_028'], 'func': tbd_base_universe_d2_014_tbd_028_ma_distance_1008_028}


def tbd_base_universe_d2_015_tbd_029_stochastic_position_1260_029(tbd_029_stochastic_position_1260_029):
    return _base_universe_d2(tbd_029_stochastic_position_1260_029, 15)
TBD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['tbd_base_universe_d2_015_tbd_029_stochastic_position_1260_029'] = {'inputs': ['tbd_029_stochastic_position_1260_029'], 'func': tbd_base_universe_d2_015_tbd_029_stochastic_position_1260_029}


def tbd_base_universe_d2_016_tbd_basefill_001(tbd_basefill_001):
    return _base_universe_d2(tbd_basefill_001, 16)
TBD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['tbd_base_universe_d2_016_tbd_basefill_001'] = {'inputs': ['tbd_basefill_001'], 'func': tbd_base_universe_d2_016_tbd_basefill_001}


def tbd_base_universe_d2_017_tbd_basefill_002(tbd_basefill_002):
    return _base_universe_d2(tbd_basefill_002, 17)
TBD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['tbd_base_universe_d2_017_tbd_basefill_002'] = {'inputs': ['tbd_basefill_002'], 'func': tbd_base_universe_d2_017_tbd_basefill_002}


def tbd_base_universe_d2_018_tbd_basefill_006(tbd_basefill_006):
    return _base_universe_d2(tbd_basefill_006, 18)
TBD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['tbd_base_universe_d2_018_tbd_basefill_006'] = {'inputs': ['tbd_basefill_006'], 'func': tbd_base_universe_d2_018_tbd_basefill_006}


def tbd_base_universe_d2_019_tbd_basefill_007(tbd_basefill_007):
    return _base_universe_d2(tbd_basefill_007, 19)
TBD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['tbd_base_universe_d2_019_tbd_basefill_007'] = {'inputs': ['tbd_basefill_007'], 'func': tbd_base_universe_d2_019_tbd_basefill_007}


def tbd_base_universe_d2_020_tbd_basefill_008(tbd_basefill_008):
    return _base_universe_d2(tbd_basefill_008, 20)
TBD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['tbd_base_universe_d2_020_tbd_basefill_008'] = {'inputs': ['tbd_basefill_008'], 'func': tbd_base_universe_d2_020_tbd_basefill_008}


def tbd_base_universe_d2_021_tbd_basefill_012(tbd_basefill_012):
    return _base_universe_d2(tbd_basefill_012, 21)
TBD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['tbd_base_universe_d2_021_tbd_basefill_012'] = {'inputs': ['tbd_basefill_012'], 'func': tbd_base_universe_d2_021_tbd_basefill_012}


def tbd_base_universe_d2_022_tbd_basefill_013(tbd_basefill_013):
    return _base_universe_d2(tbd_basefill_013, 22)
TBD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['tbd_base_universe_d2_022_tbd_basefill_013'] = {'inputs': ['tbd_basefill_013'], 'func': tbd_base_universe_d2_022_tbd_basefill_013}


def tbd_base_universe_d2_023_tbd_basefill_014(tbd_basefill_014):
    return _base_universe_d2(tbd_basefill_014, 23)
TBD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['tbd_base_universe_d2_023_tbd_basefill_014'] = {'inputs': ['tbd_basefill_014'], 'func': tbd_base_universe_d2_023_tbd_basefill_014}


def tbd_base_universe_d2_024_tbd_basefill_018(tbd_basefill_018):
    return _base_universe_d2(tbd_basefill_018, 24)
TBD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['tbd_base_universe_d2_024_tbd_basefill_018'] = {'inputs': ['tbd_basefill_018'], 'func': tbd_base_universe_d2_024_tbd_basefill_018}


def tbd_base_universe_d2_025_tbd_basefill_019(tbd_basefill_019):
    return _base_universe_d2(tbd_basefill_019, 25)
TBD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['tbd_base_universe_d2_025_tbd_basefill_019'] = {'inputs': ['tbd_basefill_019'], 'func': tbd_base_universe_d2_025_tbd_basefill_019}


def tbd_base_universe_d2_026_tbd_basefill_020(tbd_basefill_020):
    return _base_universe_d2(tbd_basefill_020, 26)
TBD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['tbd_base_universe_d2_026_tbd_basefill_020'] = {'inputs': ['tbd_basefill_020'], 'func': tbd_base_universe_d2_026_tbd_basefill_020}


def tbd_base_universe_d2_027_tbd_basefill_024(tbd_basefill_024):
    return _base_universe_d2(tbd_basefill_024, 27)
TBD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['tbd_base_universe_d2_027_tbd_basefill_024'] = {'inputs': ['tbd_basefill_024'], 'func': tbd_base_universe_d2_027_tbd_basefill_024}


def tbd_base_universe_d2_028_tbd_basefill_025(tbd_basefill_025):
    return _base_universe_d2(tbd_basefill_025, 28)
TBD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['tbd_base_universe_d2_028_tbd_basefill_025'] = {'inputs': ['tbd_basefill_025'], 'func': tbd_base_universe_d2_028_tbd_basefill_025}


def tbd_base_universe_d2_029_tbd_basefill_026(tbd_basefill_026):
    return _base_universe_d2(tbd_basefill_026, 29)
TBD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['tbd_base_universe_d2_029_tbd_basefill_026'] = {'inputs': ['tbd_basefill_026'], 'func': tbd_base_universe_d2_029_tbd_basefill_026}


def tbd_base_universe_d2_030_tbd_basefill_030(tbd_basefill_030):
    return _base_universe_d2(tbd_basefill_030, 30)
TBD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['tbd_base_universe_d2_030_tbd_basefill_030'] = {'inputs': ['tbd_basefill_030'], 'func': tbd_base_universe_d2_030_tbd_basefill_030}


def tbd_base_universe_d2_031_tbd_basefill_031(tbd_basefill_031):
    return _base_universe_d2(tbd_basefill_031, 31)
TBD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['tbd_base_universe_d2_031_tbd_basefill_031'] = {'inputs': ['tbd_basefill_031'], 'func': tbd_base_universe_d2_031_tbd_basefill_031}


def tbd_base_universe_d2_032_tbd_basefill_032(tbd_basefill_032):
    return _base_universe_d2(tbd_basefill_032, 32)
TBD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['tbd_base_universe_d2_032_tbd_basefill_032'] = {'inputs': ['tbd_basefill_032'], 'func': tbd_base_universe_d2_032_tbd_basefill_032}


def tbd_base_universe_d2_033_tbd_basefill_033(tbd_basefill_033):
    return _base_universe_d2(tbd_basefill_033, 33)
TBD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['tbd_base_universe_d2_033_tbd_basefill_033'] = {'inputs': ['tbd_basefill_033'], 'func': tbd_base_universe_d2_033_tbd_basefill_033}


def tbd_base_universe_d2_034_tbd_basefill_034(tbd_basefill_034):
    return _base_universe_d2(tbd_basefill_034, 34)
TBD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['tbd_base_universe_d2_034_tbd_basefill_034'] = {'inputs': ['tbd_basefill_034'], 'func': tbd_base_universe_d2_034_tbd_basefill_034}


def tbd_base_universe_d2_035_tbd_basefill_035(tbd_basefill_035):
    return _base_universe_d2(tbd_basefill_035, 35)
TBD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['tbd_base_universe_d2_035_tbd_basefill_035'] = {'inputs': ['tbd_basefill_035'], 'func': tbd_base_universe_d2_035_tbd_basefill_035}


def tbd_base_universe_d2_036_tbd_basefill_036(tbd_basefill_036):
    return _base_universe_d2(tbd_basefill_036, 36)
TBD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['tbd_base_universe_d2_036_tbd_basefill_036'] = {'inputs': ['tbd_basefill_036'], 'func': tbd_base_universe_d2_036_tbd_basefill_036}


def tbd_base_universe_d2_037_tbd_basefill_037(tbd_basefill_037):
    return _base_universe_d2(tbd_basefill_037, 37)
TBD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['tbd_base_universe_d2_037_tbd_basefill_037'] = {'inputs': ['tbd_basefill_037'], 'func': tbd_base_universe_d2_037_tbd_basefill_037}


def tbd_base_universe_d2_038_tbd_basefill_038(tbd_basefill_038):
    return _base_universe_d2(tbd_basefill_038, 38)
TBD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['tbd_base_universe_d2_038_tbd_basefill_038'] = {'inputs': ['tbd_basefill_038'], 'func': tbd_base_universe_d2_038_tbd_basefill_038}


def tbd_base_universe_d2_039_tbd_basefill_039(tbd_basefill_039):
    return _base_universe_d2(tbd_basefill_039, 39)
TBD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['tbd_base_universe_d2_039_tbd_basefill_039'] = {'inputs': ['tbd_basefill_039'], 'func': tbd_base_universe_d2_039_tbd_basefill_039}


def tbd_base_universe_d2_040_tbd_basefill_040(tbd_basefill_040):
    return _base_universe_d2(tbd_basefill_040, 40)
TBD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['tbd_base_universe_d2_040_tbd_basefill_040'] = {'inputs': ['tbd_basefill_040'], 'func': tbd_base_universe_d2_040_tbd_basefill_040}


def tbd_base_universe_d2_041_tbd_basefill_041(tbd_basefill_041):
    return _base_universe_d2(tbd_basefill_041, 41)
TBD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['tbd_base_universe_d2_041_tbd_basefill_041'] = {'inputs': ['tbd_basefill_041'], 'func': tbd_base_universe_d2_041_tbd_basefill_041}


def tbd_base_universe_d2_042_tbd_basefill_042(tbd_basefill_042):
    return _base_universe_d2(tbd_basefill_042, 42)
TBD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['tbd_base_universe_d2_042_tbd_basefill_042'] = {'inputs': ['tbd_basefill_042'], 'func': tbd_base_universe_d2_042_tbd_basefill_042}


def tbd_base_universe_d2_043_tbd_basefill_043(tbd_basefill_043):
    return _base_universe_d2(tbd_basefill_043, 43)
TBD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['tbd_base_universe_d2_043_tbd_basefill_043'] = {'inputs': ['tbd_basefill_043'], 'func': tbd_base_universe_d2_043_tbd_basefill_043}


def tbd_base_universe_d2_044_tbd_basefill_044(tbd_basefill_044):
    return _base_universe_d2(tbd_basefill_044, 44)
TBD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['tbd_base_universe_d2_044_tbd_basefill_044'] = {'inputs': ['tbd_basefill_044'], 'func': tbd_base_universe_d2_044_tbd_basefill_044}


def tbd_base_universe_d2_045_tbd_basefill_045(tbd_basefill_045):
    return _base_universe_d2(tbd_basefill_045, 45)
TBD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['tbd_base_universe_d2_045_tbd_basefill_045'] = {'inputs': ['tbd_basefill_045'], 'func': tbd_base_universe_d2_045_tbd_basefill_045}


def tbd_base_universe_d2_046_tbd_basefill_046(tbd_basefill_046):
    return _base_universe_d2(tbd_basefill_046, 46)
TBD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['tbd_base_universe_d2_046_tbd_basefill_046'] = {'inputs': ['tbd_basefill_046'], 'func': tbd_base_universe_d2_046_tbd_basefill_046}


def tbd_base_universe_d2_047_tbd_basefill_047(tbd_basefill_047):
    return _base_universe_d2(tbd_basefill_047, 47)
TBD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['tbd_base_universe_d2_047_tbd_basefill_047'] = {'inputs': ['tbd_basefill_047'], 'func': tbd_base_universe_d2_047_tbd_basefill_047}


def tbd_base_universe_d2_048_tbd_basefill_048(tbd_basefill_048):
    return _base_universe_d2(tbd_basefill_048, 48)
TBD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['tbd_base_universe_d2_048_tbd_basefill_048'] = {'inputs': ['tbd_basefill_048'], 'func': tbd_base_universe_d2_048_tbd_basefill_048}


def tbd_base_universe_d2_049_tbd_basefill_049(tbd_basefill_049):
    return _base_universe_d2(tbd_basefill_049, 49)
TBD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['tbd_base_universe_d2_049_tbd_basefill_049'] = {'inputs': ['tbd_basefill_049'], 'func': tbd_base_universe_d2_049_tbd_basefill_049}


def tbd_base_universe_d2_050_tbd_basefill_050(tbd_basefill_050):
    return _base_universe_d2(tbd_basefill_050, 50)
TBD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['tbd_base_universe_d2_050_tbd_basefill_050'] = {'inputs': ['tbd_basefill_050'], 'func': tbd_base_universe_d2_050_tbd_basefill_050}


def tbd_base_universe_d2_051_tbd_basefill_051(tbd_basefill_051):
    return _base_universe_d2(tbd_basefill_051, 51)
TBD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['tbd_base_universe_d2_051_tbd_basefill_051'] = {'inputs': ['tbd_basefill_051'], 'func': tbd_base_universe_d2_051_tbd_basefill_051}


def tbd_base_universe_d2_052_tbd_basefill_052(tbd_basefill_052):
    return _base_universe_d2(tbd_basefill_052, 52)
TBD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['tbd_base_universe_d2_052_tbd_basefill_052'] = {'inputs': ['tbd_basefill_052'], 'func': tbd_base_universe_d2_052_tbd_basefill_052}


def tbd_base_universe_d2_053_tbd_basefill_053(tbd_basefill_053):
    return _base_universe_d2(tbd_basefill_053, 53)
TBD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['tbd_base_universe_d2_053_tbd_basefill_053'] = {'inputs': ['tbd_basefill_053'], 'func': tbd_base_universe_d2_053_tbd_basefill_053}


def tbd_base_universe_d2_054_tbd_basefill_054(tbd_basefill_054):
    return _base_universe_d2(tbd_basefill_054, 54)
TBD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['tbd_base_universe_d2_054_tbd_basefill_054'] = {'inputs': ['tbd_basefill_054'], 'func': tbd_base_universe_d2_054_tbd_basefill_054}


def tbd_base_universe_d2_055_tbd_basefill_055(tbd_basefill_055):
    return _base_universe_d2(tbd_basefill_055, 55)
TBD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['tbd_base_universe_d2_055_tbd_basefill_055'] = {'inputs': ['tbd_basefill_055'], 'func': tbd_base_universe_d2_055_tbd_basefill_055}


def tbd_base_universe_d2_056_tbd_basefill_056(tbd_basefill_056):
    return _base_universe_d2(tbd_basefill_056, 56)
TBD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['tbd_base_universe_d2_056_tbd_basefill_056'] = {'inputs': ['tbd_basefill_056'], 'func': tbd_base_universe_d2_056_tbd_basefill_056}


def tbd_base_universe_d2_057_tbd_basefill_057(tbd_basefill_057):
    return _base_universe_d2(tbd_basefill_057, 57)
TBD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['tbd_base_universe_d2_057_tbd_basefill_057'] = {'inputs': ['tbd_basefill_057'], 'func': tbd_base_universe_d2_057_tbd_basefill_057}


def tbd_base_universe_d2_058_tbd_basefill_058(tbd_basefill_058):
    return _base_universe_d2(tbd_basefill_058, 58)
TBD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['tbd_base_universe_d2_058_tbd_basefill_058'] = {'inputs': ['tbd_basefill_058'], 'func': tbd_base_universe_d2_058_tbd_basefill_058}


def tbd_base_universe_d2_059_tbd_basefill_059(tbd_basefill_059):
    return _base_universe_d2(tbd_basefill_059, 59)
TBD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['tbd_base_universe_d2_059_tbd_basefill_059'] = {'inputs': ['tbd_basefill_059'], 'func': tbd_base_universe_d2_059_tbd_basefill_059}


def tbd_base_universe_d2_060_tbd_basefill_060(tbd_basefill_060):
    return _base_universe_d2(tbd_basefill_060, 60)
TBD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['tbd_base_universe_d2_060_tbd_basefill_060'] = {'inputs': ['tbd_basefill_060'], 'func': tbd_base_universe_d2_060_tbd_basefill_060}


def tbd_base_universe_d2_061_tbd_basefill_061(tbd_basefill_061):
    return _base_universe_d2(tbd_basefill_061, 61)
TBD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['tbd_base_universe_d2_061_tbd_basefill_061'] = {'inputs': ['tbd_basefill_061'], 'func': tbd_base_universe_d2_061_tbd_basefill_061}


def tbd_base_universe_d2_062_tbd_basefill_062(tbd_basefill_062):
    return _base_universe_d2(tbd_basefill_062, 62)
TBD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['tbd_base_universe_d2_062_tbd_basefill_062'] = {'inputs': ['tbd_basefill_062'], 'func': tbd_base_universe_d2_062_tbd_basefill_062}


def tbd_base_universe_d2_063_tbd_basefill_063(tbd_basefill_063):
    return _base_universe_d2(tbd_basefill_063, 63)
TBD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['tbd_base_universe_d2_063_tbd_basefill_063'] = {'inputs': ['tbd_basefill_063'], 'func': tbd_base_universe_d2_063_tbd_basefill_063}


def tbd_base_universe_d2_064_tbd_basefill_064(tbd_basefill_064):
    return _base_universe_d2(tbd_basefill_064, 64)
TBD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['tbd_base_universe_d2_064_tbd_basefill_064'] = {'inputs': ['tbd_basefill_064'], 'func': tbd_base_universe_d2_064_tbd_basefill_064}


def tbd_base_universe_d2_065_tbd_basefill_065(tbd_basefill_065):
    return _base_universe_d2(tbd_basefill_065, 65)
TBD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['tbd_base_universe_d2_065_tbd_basefill_065'] = {'inputs': ['tbd_basefill_065'], 'func': tbd_base_universe_d2_065_tbd_basefill_065}


def tbd_base_universe_d2_066_tbd_basefill_066(tbd_basefill_066):
    return _base_universe_d2(tbd_basefill_066, 66)
TBD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['tbd_base_universe_d2_066_tbd_basefill_066'] = {'inputs': ['tbd_basefill_066'], 'func': tbd_base_universe_d2_066_tbd_basefill_066}


def tbd_base_universe_d2_067_tbd_basefill_067(tbd_basefill_067):
    return _base_universe_d2(tbd_basefill_067, 67)
TBD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['tbd_base_universe_d2_067_tbd_basefill_067'] = {'inputs': ['tbd_basefill_067'], 'func': tbd_base_universe_d2_067_tbd_basefill_067}


def tbd_base_universe_d2_068_tbd_basefill_068(tbd_basefill_068):
    return _base_universe_d2(tbd_basefill_068, 68)
TBD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['tbd_base_universe_d2_068_tbd_basefill_068'] = {'inputs': ['tbd_basefill_068'], 'func': tbd_base_universe_d2_068_tbd_basefill_068}


def tbd_base_universe_d2_069_tbd_basefill_069(tbd_basefill_069):
    return _base_universe_d2(tbd_basefill_069, 69)
TBD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['tbd_base_universe_d2_069_tbd_basefill_069'] = {'inputs': ['tbd_basefill_069'], 'func': tbd_base_universe_d2_069_tbd_basefill_069}


def tbd_base_universe_d2_070_tbd_basefill_070(tbd_basefill_070):
    return _base_universe_d2(tbd_basefill_070, 70)
TBD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['tbd_base_universe_d2_070_tbd_basefill_070'] = {'inputs': ['tbd_basefill_070'], 'func': tbd_base_universe_d2_070_tbd_basefill_070}


def tbd_base_universe_d2_071_tbd_basefill_071(tbd_basefill_071):
    return _base_universe_d2(tbd_basefill_071, 71)
TBD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['tbd_base_universe_d2_071_tbd_basefill_071'] = {'inputs': ['tbd_basefill_071'], 'func': tbd_base_universe_d2_071_tbd_basefill_071}


def tbd_base_universe_d2_072_tbd_basefill_072(tbd_basefill_072):
    return _base_universe_d2(tbd_basefill_072, 72)
TBD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['tbd_base_universe_d2_072_tbd_basefill_072'] = {'inputs': ['tbd_basefill_072'], 'func': tbd_base_universe_d2_072_tbd_basefill_072}


def tbd_base_universe_d2_073_tbd_basefill_073(tbd_basefill_073):
    return _base_universe_d2(tbd_basefill_073, 73)
TBD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['tbd_base_universe_d2_073_tbd_basefill_073'] = {'inputs': ['tbd_basefill_073'], 'func': tbd_base_universe_d2_073_tbd_basefill_073}


def tbd_base_universe_d2_074_tbd_basefill_074(tbd_basefill_074):
    return _base_universe_d2(tbd_basefill_074, 74)
TBD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['tbd_base_universe_d2_074_tbd_basefill_074'] = {'inputs': ['tbd_basefill_074'], 'func': tbd_base_universe_d2_074_tbd_basefill_074}


def tbd_base_universe_d2_075_tbd_basefill_075(tbd_basefill_075):
    return _base_universe_d2(tbd_basefill_075, 75)
TBD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['tbd_base_universe_d2_075_tbd_basefill_075'] = {'inputs': ['tbd_basefill_075'], 'func': tbd_base_universe_d2_075_tbd_basefill_075}
