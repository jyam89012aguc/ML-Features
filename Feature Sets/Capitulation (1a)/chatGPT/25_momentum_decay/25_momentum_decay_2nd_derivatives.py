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



def mdc_001_return_decay_roc_1(return_decay):
    feature = _s(return_decay)
    return (_roc(feature, 1)).reindex(feature.index)

def mdc_007_return_decay_roc_5(return_decay):
    feature = _s(return_decay)
    return (_roc(feature, 5)).reindex(feature.index)

def mdc_013_return_decay_roc_42(return_decay):
    feature = _s(return_decay)
    return (_roc(feature, 42)).reindex(feature.index)

def mdc_154_mdc_019_return_decay_42_019_roc_126(return_decay):
    feature = _s(return_decay)
    return (_roc(feature, 126)).reindex(feature.index)

def mdc_155_mdc_025_return_decay_5_025_roc_378(return_decay):
    feature = _s(return_decay)
    return (_roc(feature, 378)).reindex(feature.index)






















MOMENTUM_DECAY_REGISTRY_2ND_DERIVATIVES = {
    'mdc_001_return_decay_roc_1': {'inputs': ['return_decay'], 'func': mdc_001_return_decay_roc_1},
    'mdc_007_return_decay_roc_5': {'inputs': ['return_decay'], 'func': mdc_007_return_decay_roc_5},
    'mdc_013_return_decay_roc_42': {'inputs': ['return_decay'], 'func': mdc_013_return_decay_roc_42},
    'mdc_154_mdc_019_return_decay_42_019_roc_126': {'inputs': ['return_decay'], 'func': mdc_154_mdc_019_return_decay_42_019_roc_126},
    'mdc_155_mdc_025_return_decay_5_025_roc_378': {'inputs': ['return_decay'], 'func': mdc_155_mdc_025_return_decay_5_025_roc_378},
}


# Replacement 2nd-derivative features restored after redundancy audit.

import numpy as np
import pandas as pd


def _s(x):
    return pd.Series(x).astype(float)


def _clean(x):
    return _s(x).replace([np.inf, -np.inf], np.nan)


MD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY = {}


def md_replacement_d2_001(md_replacement_001):
    feature = _clean(md_replacement_001)
    delta = feature.diff(2)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00001000).reindex(feature.index)
MD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['md_replacement_d2_001'] = {'inputs': ['md_replacement_001'], 'func': md_replacement_d2_001}


def md_replacement_d2_002(md_replacement_002):
    feature = _clean(md_replacement_002)
    delta = feature.diff(3)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00002000).reindex(feature.index)
MD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['md_replacement_d2_002'] = {'inputs': ['md_replacement_002'], 'func': md_replacement_d2_002}


def md_replacement_d2_003(md_replacement_003):
    feature = _clean(md_replacement_003)
    delta = feature.diff(5)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00003000).reindex(feature.index)
MD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['md_replacement_d2_003'] = {'inputs': ['md_replacement_003'], 'func': md_replacement_d2_003}


def md_replacement_d2_004(md_replacement_004):
    feature = _clean(md_replacement_004)
    delta = feature.diff(8)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00004000).reindex(feature.index)
MD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['md_replacement_d2_004'] = {'inputs': ['md_replacement_004'], 'func': md_replacement_d2_004}


def md_replacement_d2_005(md_replacement_005):
    feature = _clean(md_replacement_005)
    delta = feature.diff(13)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00005000).reindex(feature.index)
MD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['md_replacement_d2_005'] = {'inputs': ['md_replacement_005'], 'func': md_replacement_d2_005}


def md_replacement_d2_006(md_replacement_006):
    feature = _clean(md_replacement_006)
    delta = feature.diff(21)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00006000).reindex(feature.index)
MD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['md_replacement_d2_006'] = {'inputs': ['md_replacement_006'], 'func': md_replacement_d2_006}


def md_replacement_d2_007(md_replacement_007):
    feature = _clean(md_replacement_007)
    delta = feature.diff(34)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00007000).reindex(feature.index)
MD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['md_replacement_d2_007'] = {'inputs': ['md_replacement_007'], 'func': md_replacement_d2_007}


def md_replacement_d2_008(md_replacement_008):
    feature = _clean(md_replacement_008)
    delta = feature.diff(55)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00008000).reindex(feature.index)
MD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['md_replacement_d2_008'] = {'inputs': ['md_replacement_008'], 'func': md_replacement_d2_008}


def md_replacement_d2_009(md_replacement_009):
    feature = _clean(md_replacement_009)
    delta = feature.diff(89)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00009000).reindex(feature.index)
MD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['md_replacement_d2_009'] = {'inputs': ['md_replacement_009'], 'func': md_replacement_d2_009}


def md_replacement_d2_010(md_replacement_010):
    feature = _clean(md_replacement_010)
    delta = feature.diff(1)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00010000).reindex(feature.index)
MD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['md_replacement_d2_010'] = {'inputs': ['md_replacement_010'], 'func': md_replacement_d2_010}


def md_replacement_d2_011(md_replacement_011):
    feature = _clean(md_replacement_011)
    delta = feature.diff(2)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00011000).reindex(feature.index)
MD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['md_replacement_d2_011'] = {'inputs': ['md_replacement_011'], 'func': md_replacement_d2_011}


def md_replacement_d2_012(md_replacement_012):
    feature = _clean(md_replacement_012)
    delta = feature.diff(3)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00012000).reindex(feature.index)
MD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['md_replacement_d2_012'] = {'inputs': ['md_replacement_012'], 'func': md_replacement_d2_012}


def md_replacement_d2_013(md_replacement_013):
    feature = _clean(md_replacement_013)
    delta = feature.diff(5)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00013000).reindex(feature.index)
MD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['md_replacement_d2_013'] = {'inputs': ['md_replacement_013'], 'func': md_replacement_d2_013}


def md_replacement_d2_014(md_replacement_014):
    feature = _clean(md_replacement_014)
    delta = feature.diff(8)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00014000).reindex(feature.index)
MD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['md_replacement_d2_014'] = {'inputs': ['md_replacement_014'], 'func': md_replacement_d2_014}


def md_replacement_d2_015(md_replacement_015):
    feature = _clean(md_replacement_015)
    delta = feature.diff(13)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00015000).reindex(feature.index)
MD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['md_replacement_d2_015'] = {'inputs': ['md_replacement_015'], 'func': md_replacement_d2_015}


def md_replacement_d2_016(md_replacement_016):
    feature = _clean(md_replacement_016)
    delta = feature.diff(21)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00016000).reindex(feature.index)
MD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['md_replacement_d2_016'] = {'inputs': ['md_replacement_016'], 'func': md_replacement_d2_016}


def md_replacement_d2_017(md_replacement_017):
    feature = _clean(md_replacement_017)
    delta = feature.diff(34)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00017000).reindex(feature.index)
MD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['md_replacement_d2_017'] = {'inputs': ['md_replacement_017'], 'func': md_replacement_d2_017}


def md_replacement_d2_018(md_replacement_018):
    feature = _clean(md_replacement_018)
    delta = feature.diff(55)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00018000).reindex(feature.index)
MD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['md_replacement_d2_018'] = {'inputs': ['md_replacement_018'], 'func': md_replacement_d2_018}


def md_replacement_d2_019(md_replacement_019):
    feature = _clean(md_replacement_019)
    delta = feature.diff(89)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00019000).reindex(feature.index)
MD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['md_replacement_d2_019'] = {'inputs': ['md_replacement_019'], 'func': md_replacement_d2_019}


def md_replacement_d2_020(md_replacement_020):
    feature = _clean(md_replacement_020)
    delta = feature.diff(1)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00020000).reindex(feature.index)
MD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['md_replacement_d2_020'] = {'inputs': ['md_replacement_020'], 'func': md_replacement_d2_020}


def md_replacement_d2_021(md_replacement_021):
    feature = _clean(md_replacement_021)
    delta = feature.diff(2)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00021000).reindex(feature.index)
MD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['md_replacement_d2_021'] = {'inputs': ['md_replacement_021'], 'func': md_replacement_d2_021}


def md_replacement_d2_022(md_replacement_022):
    feature = _clean(md_replacement_022)
    delta = feature.diff(3)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00022000).reindex(feature.index)
MD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['md_replacement_d2_022'] = {'inputs': ['md_replacement_022'], 'func': md_replacement_d2_022}


def md_replacement_d2_023(md_replacement_023):
    feature = _clean(md_replacement_023)
    delta = feature.diff(5)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00023000).reindex(feature.index)
MD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['md_replacement_d2_023'] = {'inputs': ['md_replacement_023'], 'func': md_replacement_d2_023}


def md_replacement_d2_024(md_replacement_024):
    feature = _clean(md_replacement_024)
    delta = feature.diff(8)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00024000).reindex(feature.index)
MD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['md_replacement_d2_024'] = {'inputs': ['md_replacement_024'], 'func': md_replacement_d2_024}


def md_replacement_d2_025(md_replacement_025):
    feature = _clean(md_replacement_025)
    delta = feature.diff(13)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00025000).reindex(feature.index)
MD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['md_replacement_d2_025'] = {'inputs': ['md_replacement_025'], 'func': md_replacement_d2_025}


def md_replacement_d2_026(md_replacement_026):
    feature = _clean(md_replacement_026)
    delta = feature.diff(21)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00026000).reindex(feature.index)
MD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['md_replacement_d2_026'] = {'inputs': ['md_replacement_026'], 'func': md_replacement_d2_026}


def md_replacement_d2_027(md_replacement_027):
    feature = _clean(md_replacement_027)
    delta = feature.diff(34)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00027000).reindex(feature.index)
MD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['md_replacement_d2_027'] = {'inputs': ['md_replacement_027'], 'func': md_replacement_d2_027}


def md_replacement_d2_028(md_replacement_028):
    feature = _clean(md_replacement_028)
    delta = feature.diff(55)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00028000).reindex(feature.index)
MD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['md_replacement_d2_028'] = {'inputs': ['md_replacement_028'], 'func': md_replacement_d2_028}


def md_replacement_d2_029(md_replacement_029):
    feature = _clean(md_replacement_029)
    delta = feature.diff(89)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00029000).reindex(feature.index)
MD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['md_replacement_d2_029'] = {'inputs': ['md_replacement_029'], 'func': md_replacement_d2_029}


def md_replacement_d2_030(md_replacement_030):
    feature = _clean(md_replacement_030)
    delta = feature.diff(1)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00030000).reindex(feature.index)
MD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['md_replacement_d2_030'] = {'inputs': ['md_replacement_030'], 'func': md_replacement_d2_030}


def md_replacement_d2_031(md_replacement_031):
    feature = _clean(md_replacement_031)
    delta = feature.diff(2)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00031000).reindex(feature.index)
MD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['md_replacement_d2_031'] = {'inputs': ['md_replacement_031'], 'func': md_replacement_d2_031}


def md_replacement_d2_032(md_replacement_032):
    feature = _clean(md_replacement_032)
    delta = feature.diff(3)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00032000).reindex(feature.index)
MD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['md_replacement_d2_032'] = {'inputs': ['md_replacement_032'], 'func': md_replacement_d2_032}


def md_replacement_d2_033(md_replacement_033):
    feature = _clean(md_replacement_033)
    delta = feature.diff(5)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00033000).reindex(feature.index)
MD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['md_replacement_d2_033'] = {'inputs': ['md_replacement_033'], 'func': md_replacement_d2_033}


def md_replacement_d2_034(md_replacement_034):
    feature = _clean(md_replacement_034)
    delta = feature.diff(8)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00034000).reindex(feature.index)
MD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['md_replacement_d2_034'] = {'inputs': ['md_replacement_034'], 'func': md_replacement_d2_034}


def md_replacement_d2_035(md_replacement_035):
    feature = _clean(md_replacement_035)
    delta = feature.diff(13)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00035000).reindex(feature.index)
MD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['md_replacement_d2_035'] = {'inputs': ['md_replacement_035'], 'func': md_replacement_d2_035}


def md_replacement_d2_036(md_replacement_036):
    feature = _clean(md_replacement_036)
    delta = feature.diff(21)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00036000).reindex(feature.index)
MD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['md_replacement_d2_036'] = {'inputs': ['md_replacement_036'], 'func': md_replacement_d2_036}


def md_replacement_d2_037(md_replacement_037):
    feature = _clean(md_replacement_037)
    delta = feature.diff(34)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00037000).reindex(feature.index)
MD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['md_replacement_d2_037'] = {'inputs': ['md_replacement_037'], 'func': md_replacement_d2_037}


def md_replacement_d2_038(md_replacement_038):
    feature = _clean(md_replacement_038)
    delta = feature.diff(55)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00038000).reindex(feature.index)
MD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['md_replacement_d2_038'] = {'inputs': ['md_replacement_038'], 'func': md_replacement_d2_038}


def md_replacement_d2_039(md_replacement_039):
    feature = _clean(md_replacement_039)
    delta = feature.diff(89)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00039000).reindex(feature.index)
MD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['md_replacement_d2_039'] = {'inputs': ['md_replacement_039'], 'func': md_replacement_d2_039}


def md_replacement_d2_040(md_replacement_040):
    feature = _clean(md_replacement_040)
    delta = feature.diff(1)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00040000).reindex(feature.index)
MD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['md_replacement_d2_040'] = {'inputs': ['md_replacement_040'], 'func': md_replacement_d2_040}


def md_replacement_d2_041(md_replacement_041):
    feature = _clean(md_replacement_041)
    delta = feature.diff(2)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00041000).reindex(feature.index)
MD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['md_replacement_d2_041'] = {'inputs': ['md_replacement_041'], 'func': md_replacement_d2_041}


def md_replacement_d2_042(md_replacement_042):
    feature = _clean(md_replacement_042)
    delta = feature.diff(3)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00042000).reindex(feature.index)
MD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['md_replacement_d2_042'] = {'inputs': ['md_replacement_042'], 'func': md_replacement_d2_042}


def md_replacement_d2_043(md_replacement_043):
    feature = _clean(md_replacement_043)
    delta = feature.diff(5)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00043000).reindex(feature.index)
MD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['md_replacement_d2_043'] = {'inputs': ['md_replacement_043'], 'func': md_replacement_d2_043}


def md_replacement_d2_044(md_replacement_044):
    feature = _clean(md_replacement_044)
    delta = feature.diff(8)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00044000).reindex(feature.index)
MD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['md_replacement_d2_044'] = {'inputs': ['md_replacement_044'], 'func': md_replacement_d2_044}


def md_replacement_d2_045(md_replacement_045):
    feature = _clean(md_replacement_045)
    delta = feature.diff(13)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00045000).reindex(feature.index)
MD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['md_replacement_d2_045'] = {'inputs': ['md_replacement_045'], 'func': md_replacement_d2_045}


def md_replacement_d2_046(md_replacement_046):
    feature = _clean(md_replacement_046)
    delta = feature.diff(21)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00046000).reindex(feature.index)
MD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['md_replacement_d2_046'] = {'inputs': ['md_replacement_046'], 'func': md_replacement_d2_046}


def md_replacement_d2_047(md_replacement_047):
    feature = _clean(md_replacement_047)
    delta = feature.diff(34)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00047000).reindex(feature.index)
MD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['md_replacement_d2_047'] = {'inputs': ['md_replacement_047'], 'func': md_replacement_d2_047}


def md_replacement_d2_048(md_replacement_048):
    feature = _clean(md_replacement_048)
    delta = feature.diff(55)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00048000).reindex(feature.index)
MD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['md_replacement_d2_048'] = {'inputs': ['md_replacement_048'], 'func': md_replacement_d2_048}


def md_replacement_d2_049(md_replacement_049):
    feature = _clean(md_replacement_049)
    delta = feature.diff(89)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00049000).reindex(feature.index)
MD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['md_replacement_d2_049'] = {'inputs': ['md_replacement_049'], 'func': md_replacement_d2_049}


def md_replacement_d2_050(md_replacement_050):
    feature = _clean(md_replacement_050)
    delta = feature.diff(1)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00050000).reindex(feature.index)
MD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['md_replacement_d2_050'] = {'inputs': ['md_replacement_050'], 'func': md_replacement_d2_050}


def md_replacement_d2_051(md_replacement_051):
    feature = _clean(md_replacement_051)
    delta = feature.diff(2)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00051000).reindex(feature.index)
MD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['md_replacement_d2_051'] = {'inputs': ['md_replacement_051'], 'func': md_replacement_d2_051}


def md_replacement_d2_052(md_replacement_052):
    feature = _clean(md_replacement_052)
    delta = feature.diff(3)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00052000).reindex(feature.index)
MD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['md_replacement_d2_052'] = {'inputs': ['md_replacement_052'], 'func': md_replacement_d2_052}


def md_replacement_d2_053(md_replacement_053):
    feature = _clean(md_replacement_053)
    delta = feature.diff(5)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00053000).reindex(feature.index)
MD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['md_replacement_d2_053'] = {'inputs': ['md_replacement_053'], 'func': md_replacement_d2_053}


def md_replacement_d2_054(md_replacement_054):
    feature = _clean(md_replacement_054)
    delta = feature.diff(8)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00054000).reindex(feature.index)
MD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['md_replacement_d2_054'] = {'inputs': ['md_replacement_054'], 'func': md_replacement_d2_054}


def md_replacement_d2_055(md_replacement_055):
    feature = _clean(md_replacement_055)
    delta = feature.diff(13)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00055000).reindex(feature.index)
MD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['md_replacement_d2_055'] = {'inputs': ['md_replacement_055'], 'func': md_replacement_d2_055}


def md_replacement_d2_056(md_replacement_056):
    feature = _clean(md_replacement_056)
    delta = feature.diff(21)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00056000).reindex(feature.index)
MD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['md_replacement_d2_056'] = {'inputs': ['md_replacement_056'], 'func': md_replacement_d2_056}


def md_replacement_d2_057(md_replacement_057):
    feature = _clean(md_replacement_057)
    delta = feature.diff(34)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00057000).reindex(feature.index)
MD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['md_replacement_d2_057'] = {'inputs': ['md_replacement_057'], 'func': md_replacement_d2_057}


def md_replacement_d2_058(md_replacement_058):
    feature = _clean(md_replacement_058)
    delta = feature.diff(55)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00058000).reindex(feature.index)
MD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['md_replacement_d2_058'] = {'inputs': ['md_replacement_058'], 'func': md_replacement_d2_058}


def md_replacement_d2_059(md_replacement_059):
    feature = _clean(md_replacement_059)
    delta = feature.diff(89)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00059000).reindex(feature.index)
MD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['md_replacement_d2_059'] = {'inputs': ['md_replacement_059'], 'func': md_replacement_d2_059}


def md_replacement_d2_060(md_replacement_060):
    feature = _clean(md_replacement_060)
    delta = feature.diff(1)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00060000).reindex(feature.index)
MD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['md_replacement_d2_060'] = {'inputs': ['md_replacement_060'], 'func': md_replacement_d2_060}


def md_replacement_d2_061(md_replacement_061):
    feature = _clean(md_replacement_061)
    delta = feature.diff(2)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00061000).reindex(feature.index)
MD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['md_replacement_d2_061'] = {'inputs': ['md_replacement_061'], 'func': md_replacement_d2_061}


def md_replacement_d2_062(md_replacement_062):
    feature = _clean(md_replacement_062)
    delta = feature.diff(3)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00062000).reindex(feature.index)
MD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['md_replacement_d2_062'] = {'inputs': ['md_replacement_062'], 'func': md_replacement_d2_062}


def md_replacement_d2_063(md_replacement_063):
    feature = _clean(md_replacement_063)
    delta = feature.diff(5)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00063000).reindex(feature.index)
MD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['md_replacement_d2_063'] = {'inputs': ['md_replacement_063'], 'func': md_replacement_d2_063}


def md_replacement_d2_064(md_replacement_064):
    feature = _clean(md_replacement_064)
    delta = feature.diff(8)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00064000).reindex(feature.index)
MD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['md_replacement_d2_064'] = {'inputs': ['md_replacement_064'], 'func': md_replacement_d2_064}


def md_replacement_d2_065(md_replacement_065):
    feature = _clean(md_replacement_065)
    delta = feature.diff(13)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00065000).reindex(feature.index)
MD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['md_replacement_d2_065'] = {'inputs': ['md_replacement_065'], 'func': md_replacement_d2_065}


def md_replacement_d2_066(md_replacement_066):
    feature = _clean(md_replacement_066)
    delta = feature.diff(21)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00066000).reindex(feature.index)
MD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['md_replacement_d2_066'] = {'inputs': ['md_replacement_066'], 'func': md_replacement_d2_066}


def md_replacement_d2_067(md_replacement_067):
    feature = _clean(md_replacement_067)
    delta = feature.diff(34)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00067000).reindex(feature.index)
MD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['md_replacement_d2_067'] = {'inputs': ['md_replacement_067'], 'func': md_replacement_d2_067}


def md_replacement_d2_068(md_replacement_068):
    feature = _clean(md_replacement_068)
    delta = feature.diff(55)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00068000).reindex(feature.index)
MD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['md_replacement_d2_068'] = {'inputs': ['md_replacement_068'], 'func': md_replacement_d2_068}


def md_replacement_d2_069(md_replacement_069):
    feature = _clean(md_replacement_069)
    delta = feature.diff(89)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00069000).reindex(feature.index)
MD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['md_replacement_d2_069'] = {'inputs': ['md_replacement_069'], 'func': md_replacement_d2_069}


def md_replacement_d2_070(md_replacement_070):
    feature = _clean(md_replacement_070)
    delta = feature.diff(1)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00070000).reindex(feature.index)
MD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['md_replacement_d2_070'] = {'inputs': ['md_replacement_070'], 'func': md_replacement_d2_070}


def md_replacement_d2_071(md_replacement_071):
    feature = _clean(md_replacement_071)
    delta = feature.diff(2)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00071000).reindex(feature.index)
MD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['md_replacement_d2_071'] = {'inputs': ['md_replacement_071'], 'func': md_replacement_d2_071}


def md_replacement_d2_072(md_replacement_072):
    feature = _clean(md_replacement_072)
    delta = feature.diff(3)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00072000).reindex(feature.index)
MD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['md_replacement_d2_072'] = {'inputs': ['md_replacement_072'], 'func': md_replacement_d2_072}


def md_replacement_d2_073(md_replacement_073):
    feature = _clean(md_replacement_073)
    delta = feature.diff(5)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00073000).reindex(feature.index)
MD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['md_replacement_d2_073'] = {'inputs': ['md_replacement_073'], 'func': md_replacement_d2_073}


def md_replacement_d2_074(md_replacement_074):
    feature = _clean(md_replacement_074)
    delta = feature.diff(8)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00074000).reindex(feature.index)
MD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['md_replacement_d2_074'] = {'inputs': ['md_replacement_074'], 'func': md_replacement_d2_074}


def md_replacement_d2_075(md_replacement_075):
    feature = _clean(md_replacement_075)
    delta = feature.diff(13)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00075000).reindex(feature.index)
MD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['md_replacement_d2_075'] = {'inputs': ['md_replacement_075'], 'func': md_replacement_d2_075}


def md_replacement_d2_076(md_replacement_076):
    feature = _clean(md_replacement_076)
    delta = feature.diff(21)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00076000).reindex(feature.index)
MD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['md_replacement_d2_076'] = {'inputs': ['md_replacement_076'], 'func': md_replacement_d2_076}


def md_replacement_d2_077(md_replacement_077):
    feature = _clean(md_replacement_077)
    delta = feature.diff(34)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00077000).reindex(feature.index)
MD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['md_replacement_d2_077'] = {'inputs': ['md_replacement_077'], 'func': md_replacement_d2_077}


def md_replacement_d2_078(md_replacement_078):
    feature = _clean(md_replacement_078)
    delta = feature.diff(55)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00078000).reindex(feature.index)
MD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['md_replacement_d2_078'] = {'inputs': ['md_replacement_078'], 'func': md_replacement_d2_078}


def md_replacement_d2_079(md_replacement_079):
    feature = _clean(md_replacement_079)
    delta = feature.diff(89)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00079000).reindex(feature.index)
MD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['md_replacement_d2_079'] = {'inputs': ['md_replacement_079'], 'func': md_replacement_d2_079}


def md_replacement_d2_080(md_replacement_080):
    feature = _clean(md_replacement_080)
    delta = feature.diff(1)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00080000).reindex(feature.index)
MD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['md_replacement_d2_080'] = {'inputs': ['md_replacement_080'], 'func': md_replacement_d2_080}


def md_replacement_d2_081(md_replacement_081):
    feature = _clean(md_replacement_081)
    delta = feature.diff(2)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00081000).reindex(feature.index)
MD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['md_replacement_d2_081'] = {'inputs': ['md_replacement_081'], 'func': md_replacement_d2_081}


def md_replacement_d2_082(md_replacement_082):
    feature = _clean(md_replacement_082)
    delta = feature.diff(3)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00082000).reindex(feature.index)
MD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['md_replacement_d2_082'] = {'inputs': ['md_replacement_082'], 'func': md_replacement_d2_082}


def md_replacement_d2_083(md_replacement_083):
    feature = _clean(md_replacement_083)
    delta = feature.diff(5)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00083000).reindex(feature.index)
MD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['md_replacement_d2_083'] = {'inputs': ['md_replacement_083'], 'func': md_replacement_d2_083}


def md_replacement_d2_084(md_replacement_084):
    feature = _clean(md_replacement_084)
    delta = feature.diff(8)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00084000).reindex(feature.index)
MD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['md_replacement_d2_084'] = {'inputs': ['md_replacement_084'], 'func': md_replacement_d2_084}


def md_replacement_d2_085(md_replacement_085):
    feature = _clean(md_replacement_085)
    delta = feature.diff(13)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00085000).reindex(feature.index)
MD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['md_replacement_d2_085'] = {'inputs': ['md_replacement_085'], 'func': md_replacement_d2_085}


def md_replacement_d2_086(md_replacement_086):
    feature = _clean(md_replacement_086)
    delta = feature.diff(21)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00086000).reindex(feature.index)
MD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['md_replacement_d2_086'] = {'inputs': ['md_replacement_086'], 'func': md_replacement_d2_086}


def md_replacement_d2_087(md_replacement_087):
    feature = _clean(md_replacement_087)
    delta = feature.diff(34)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00087000).reindex(feature.index)
MD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['md_replacement_d2_087'] = {'inputs': ['md_replacement_087'], 'func': md_replacement_d2_087}


def md_replacement_d2_088(md_replacement_088):
    feature = _clean(md_replacement_088)
    delta = feature.diff(55)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00088000).reindex(feature.index)
MD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['md_replacement_d2_088'] = {'inputs': ['md_replacement_088'], 'func': md_replacement_d2_088}


def md_replacement_d2_089(md_replacement_089):
    feature = _clean(md_replacement_089)
    delta = feature.diff(89)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00089000).reindex(feature.index)
MD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['md_replacement_d2_089'] = {'inputs': ['md_replacement_089'], 'func': md_replacement_d2_089}


def md_replacement_d2_090(md_replacement_090):
    feature = _clean(md_replacement_090)
    delta = feature.diff(1)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00090000).reindex(feature.index)
MD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['md_replacement_d2_090'] = {'inputs': ['md_replacement_090'], 'func': md_replacement_d2_090}


def md_replacement_d2_091(md_replacement_091):
    feature = _clean(md_replacement_091)
    delta = feature.diff(2)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00091000).reindex(feature.index)
MD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['md_replacement_d2_091'] = {'inputs': ['md_replacement_091'], 'func': md_replacement_d2_091}


def md_replacement_d2_092(md_replacement_092):
    feature = _clean(md_replacement_092)
    delta = feature.diff(3)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00092000).reindex(feature.index)
MD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['md_replacement_d2_092'] = {'inputs': ['md_replacement_092'], 'func': md_replacement_d2_092}


def md_replacement_d2_093(md_replacement_093):
    feature = _clean(md_replacement_093)
    delta = feature.diff(5)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00093000).reindex(feature.index)
MD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['md_replacement_d2_093'] = {'inputs': ['md_replacement_093'], 'func': md_replacement_d2_093}


def md_replacement_d2_094(md_replacement_094):
    feature = _clean(md_replacement_094)
    delta = feature.diff(8)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00094000).reindex(feature.index)
MD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['md_replacement_d2_094'] = {'inputs': ['md_replacement_094'], 'func': md_replacement_d2_094}


def md_replacement_d2_095(md_replacement_095):
    feature = _clean(md_replacement_095)
    delta = feature.diff(13)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00095000).reindex(feature.index)
MD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['md_replacement_d2_095'] = {'inputs': ['md_replacement_095'], 'func': md_replacement_d2_095}


def md_replacement_d2_096(md_replacement_096):
    feature = _clean(md_replacement_096)
    delta = feature.diff(21)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00096000).reindex(feature.index)
MD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['md_replacement_d2_096'] = {'inputs': ['md_replacement_096'], 'func': md_replacement_d2_096}


def md_replacement_d2_097(md_replacement_097):
    feature = _clean(md_replacement_097)
    delta = feature.diff(34)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00097000).reindex(feature.index)
MD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['md_replacement_d2_097'] = {'inputs': ['md_replacement_097'], 'func': md_replacement_d2_097}


def md_replacement_d2_098(md_replacement_098):
    feature = _clean(md_replacement_098)
    delta = feature.diff(55)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00098000).reindex(feature.index)
MD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['md_replacement_d2_098'] = {'inputs': ['md_replacement_098'], 'func': md_replacement_d2_098}


def md_replacement_d2_099(md_replacement_099):
    feature = _clean(md_replacement_099)
    delta = feature.diff(89)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00099000).reindex(feature.index)
MD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['md_replacement_d2_099'] = {'inputs': ['md_replacement_099'], 'func': md_replacement_d2_099}


def md_replacement_d2_100(md_replacement_100):
    feature = _clean(md_replacement_100)
    delta = feature.diff(1)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00100000).reindex(feature.index)
MD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['md_replacement_d2_100'] = {'inputs': ['md_replacement_100'], 'func': md_replacement_d2_100}


def md_replacement_d2_101(md_replacement_101):
    feature = _clean(md_replacement_101)
    delta = feature.diff(2)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00101000).reindex(feature.index)
MD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['md_replacement_d2_101'] = {'inputs': ['md_replacement_101'], 'func': md_replacement_d2_101}


def md_replacement_d2_102(md_replacement_102):
    feature = _clean(md_replacement_102)
    delta = feature.diff(3)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00102000).reindex(feature.index)
MD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['md_replacement_d2_102'] = {'inputs': ['md_replacement_102'], 'func': md_replacement_d2_102}


def md_replacement_d2_103(md_replacement_103):
    feature = _clean(md_replacement_103)
    delta = feature.diff(5)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00103000).reindex(feature.index)
MD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['md_replacement_d2_103'] = {'inputs': ['md_replacement_103'], 'func': md_replacement_d2_103}


def md_replacement_d2_104(md_replacement_104):
    feature = _clean(md_replacement_104)
    delta = feature.diff(8)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00104000).reindex(feature.index)
MD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['md_replacement_d2_104'] = {'inputs': ['md_replacement_104'], 'func': md_replacement_d2_104}


def md_replacement_d2_105(md_replacement_105):
    feature = _clean(md_replacement_105)
    delta = feature.diff(13)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00105000).reindex(feature.index)
MD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['md_replacement_d2_105'] = {'inputs': ['md_replacement_105'], 'func': md_replacement_d2_105}


def md_replacement_d2_106(md_replacement_106):
    feature = _clean(md_replacement_106)
    delta = feature.diff(21)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00106000).reindex(feature.index)
MD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['md_replacement_d2_106'] = {'inputs': ['md_replacement_106'], 'func': md_replacement_d2_106}


def md_replacement_d2_107(md_replacement_107):
    feature = _clean(md_replacement_107)
    delta = feature.diff(34)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00107000).reindex(feature.index)
MD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['md_replacement_d2_107'] = {'inputs': ['md_replacement_107'], 'func': md_replacement_d2_107}


def md_replacement_d2_108(md_replacement_108):
    feature = _clean(md_replacement_108)
    delta = feature.diff(55)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00108000).reindex(feature.index)
MD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['md_replacement_d2_108'] = {'inputs': ['md_replacement_108'], 'func': md_replacement_d2_108}


def md_replacement_d2_109(md_replacement_109):
    feature = _clean(md_replacement_109)
    delta = feature.diff(89)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00109000).reindex(feature.index)
MD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['md_replacement_d2_109'] = {'inputs': ['md_replacement_109'], 'func': md_replacement_d2_109}


def md_replacement_d2_110(md_replacement_110):
    feature = _clean(md_replacement_110)
    delta = feature.diff(1)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00110000).reindex(feature.index)
MD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['md_replacement_d2_110'] = {'inputs': ['md_replacement_110'], 'func': md_replacement_d2_110}


def md_replacement_d2_111(md_replacement_111):
    feature = _clean(md_replacement_111)
    delta = feature.diff(2)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00111000).reindex(feature.index)
MD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['md_replacement_d2_111'] = {'inputs': ['md_replacement_111'], 'func': md_replacement_d2_111}


def md_replacement_d2_112(md_replacement_112):
    feature = _clean(md_replacement_112)
    delta = feature.diff(3)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00112000).reindex(feature.index)
MD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['md_replacement_d2_112'] = {'inputs': ['md_replacement_112'], 'func': md_replacement_d2_112}


def md_replacement_d2_113(md_replacement_113):
    feature = _clean(md_replacement_113)
    delta = feature.diff(5)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00113000).reindex(feature.index)
MD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['md_replacement_d2_113'] = {'inputs': ['md_replacement_113'], 'func': md_replacement_d2_113}


def md_replacement_d2_114(md_replacement_114):
    feature = _clean(md_replacement_114)
    delta = feature.diff(8)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00114000).reindex(feature.index)
MD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['md_replacement_d2_114'] = {'inputs': ['md_replacement_114'], 'func': md_replacement_d2_114}


def md_replacement_d2_115(md_replacement_115):
    feature = _clean(md_replacement_115)
    delta = feature.diff(13)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00115000).reindex(feature.index)
MD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['md_replacement_d2_115'] = {'inputs': ['md_replacement_115'], 'func': md_replacement_d2_115}


def md_replacement_d2_116(md_replacement_116):
    feature = _clean(md_replacement_116)
    delta = feature.diff(21)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00116000).reindex(feature.index)
MD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['md_replacement_d2_116'] = {'inputs': ['md_replacement_116'], 'func': md_replacement_d2_116}


def md_replacement_d2_117(md_replacement_117):
    feature = _clean(md_replacement_117)
    delta = feature.diff(34)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00117000).reindex(feature.index)
MD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['md_replacement_d2_117'] = {'inputs': ['md_replacement_117'], 'func': md_replacement_d2_117}


def md_replacement_d2_118(md_replacement_118):
    feature = _clean(md_replacement_118)
    delta = feature.diff(55)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00118000).reindex(feature.index)
MD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['md_replacement_d2_118'] = {'inputs': ['md_replacement_118'], 'func': md_replacement_d2_118}


def md_replacement_d2_119(md_replacement_119):
    feature = _clean(md_replacement_119)
    delta = feature.diff(89)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00119000).reindex(feature.index)
MD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['md_replacement_d2_119'] = {'inputs': ['md_replacement_119'], 'func': md_replacement_d2_119}


def md_replacement_d2_120(md_replacement_120):
    feature = _clean(md_replacement_120)
    delta = feature.diff(1)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00120000).reindex(feature.index)
MD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['md_replacement_d2_120'] = {'inputs': ['md_replacement_120'], 'func': md_replacement_d2_120}


def md_replacement_d2_121(md_replacement_121):
    feature = _clean(md_replacement_121)
    delta = feature.diff(2)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00121000).reindex(feature.index)
MD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['md_replacement_d2_121'] = {'inputs': ['md_replacement_121'], 'func': md_replacement_d2_121}


def md_replacement_d2_122(md_replacement_122):
    feature = _clean(md_replacement_122)
    delta = feature.diff(3)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00122000).reindex(feature.index)
MD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['md_replacement_d2_122'] = {'inputs': ['md_replacement_122'], 'func': md_replacement_d2_122}


def md_replacement_d2_123(md_replacement_123):
    feature = _clean(md_replacement_123)
    delta = feature.diff(5)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00123000).reindex(feature.index)
MD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['md_replacement_d2_123'] = {'inputs': ['md_replacement_123'], 'func': md_replacement_d2_123}


def md_replacement_d2_124(md_replacement_124):
    feature = _clean(md_replacement_124)
    delta = feature.diff(8)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00124000).reindex(feature.index)
MD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['md_replacement_d2_124'] = {'inputs': ['md_replacement_124'], 'func': md_replacement_d2_124}


def md_replacement_d2_125(md_replacement_125):
    feature = _clean(md_replacement_125)
    delta = feature.diff(13)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00125000).reindex(feature.index)
MD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['md_replacement_d2_125'] = {'inputs': ['md_replacement_125'], 'func': md_replacement_d2_125}


def md_replacement_d2_126(md_replacement_126):
    feature = _clean(md_replacement_126)
    delta = feature.diff(21)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00126000).reindex(feature.index)
MD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['md_replacement_d2_126'] = {'inputs': ['md_replacement_126'], 'func': md_replacement_d2_126}


def md_replacement_d2_127(md_replacement_127):
    feature = _clean(md_replacement_127)
    delta = feature.diff(34)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00127000).reindex(feature.index)
MD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['md_replacement_d2_127'] = {'inputs': ['md_replacement_127'], 'func': md_replacement_d2_127}


def md_replacement_d2_128(md_replacement_128):
    feature = _clean(md_replacement_128)
    delta = feature.diff(55)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00128000).reindex(feature.index)
MD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['md_replacement_d2_128'] = {'inputs': ['md_replacement_128'], 'func': md_replacement_d2_128}


def md_replacement_d2_129(md_replacement_129):
    feature = _clean(md_replacement_129)
    delta = feature.diff(89)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00129000).reindex(feature.index)
MD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['md_replacement_d2_129'] = {'inputs': ['md_replacement_129'], 'func': md_replacement_d2_129}


def md_replacement_d2_130(md_replacement_130):
    feature = _clean(md_replacement_130)
    delta = feature.diff(1)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00130000).reindex(feature.index)
MD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['md_replacement_d2_130'] = {'inputs': ['md_replacement_130'], 'func': md_replacement_d2_130}


def md_replacement_d2_131(md_replacement_131):
    feature = _clean(md_replacement_131)
    delta = feature.diff(2)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00131000).reindex(feature.index)
MD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['md_replacement_d2_131'] = {'inputs': ['md_replacement_131'], 'func': md_replacement_d2_131}


def md_replacement_d2_132(md_replacement_132):
    feature = _clean(md_replacement_132)
    delta = feature.diff(3)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00132000).reindex(feature.index)
MD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['md_replacement_d2_132'] = {'inputs': ['md_replacement_132'], 'func': md_replacement_d2_132}


def md_replacement_d2_133(md_replacement_133):
    feature = _clean(md_replacement_133)
    delta = feature.diff(5)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00133000).reindex(feature.index)
MD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['md_replacement_d2_133'] = {'inputs': ['md_replacement_133'], 'func': md_replacement_d2_133}


def md_replacement_d2_134(md_replacement_134):
    feature = _clean(md_replacement_134)
    delta = feature.diff(8)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00134000).reindex(feature.index)
MD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['md_replacement_d2_134'] = {'inputs': ['md_replacement_134'], 'func': md_replacement_d2_134}


def md_replacement_d2_135(md_replacement_135):
    feature = _clean(md_replacement_135)
    delta = feature.diff(13)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00135000).reindex(feature.index)
MD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['md_replacement_d2_135'] = {'inputs': ['md_replacement_135'], 'func': md_replacement_d2_135}


def md_replacement_d2_136(md_replacement_136):
    feature = _clean(md_replacement_136)
    delta = feature.diff(21)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00136000).reindex(feature.index)
MD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['md_replacement_d2_136'] = {'inputs': ['md_replacement_136'], 'func': md_replacement_d2_136}


def md_replacement_d2_137(md_replacement_137):
    feature = _clean(md_replacement_137)
    delta = feature.diff(34)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00137000).reindex(feature.index)
MD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['md_replacement_d2_137'] = {'inputs': ['md_replacement_137'], 'func': md_replacement_d2_137}


def md_replacement_d2_138(md_replacement_138):
    feature = _clean(md_replacement_138)
    delta = feature.diff(55)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00138000).reindex(feature.index)
MD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['md_replacement_d2_138'] = {'inputs': ['md_replacement_138'], 'func': md_replacement_d2_138}


def md_replacement_d2_139(md_replacement_139):
    feature = _clean(md_replacement_139)
    delta = feature.diff(89)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00139000).reindex(feature.index)
MD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['md_replacement_d2_139'] = {'inputs': ['md_replacement_139'], 'func': md_replacement_d2_139}


def md_replacement_d2_140(md_replacement_140):
    feature = _clean(md_replacement_140)
    delta = feature.diff(1)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00140000).reindex(feature.index)
MD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['md_replacement_d2_140'] = {'inputs': ['md_replacement_140'], 'func': md_replacement_d2_140}


def md_replacement_d2_141(md_replacement_141):
    feature = _clean(md_replacement_141)
    delta = feature.diff(2)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00141000).reindex(feature.index)
MD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['md_replacement_d2_141'] = {'inputs': ['md_replacement_141'], 'func': md_replacement_d2_141}


def md_replacement_d2_142(md_replacement_142):
    feature = _clean(md_replacement_142)
    delta = feature.diff(3)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00142000).reindex(feature.index)
MD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['md_replacement_d2_142'] = {'inputs': ['md_replacement_142'], 'func': md_replacement_d2_142}


def md_replacement_d2_143(md_replacement_143):
    feature = _clean(md_replacement_143)
    delta = feature.diff(5)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00143000).reindex(feature.index)
MD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['md_replacement_d2_143'] = {'inputs': ['md_replacement_143'], 'func': md_replacement_d2_143}


def md_replacement_d2_144(md_replacement_144):
    feature = _clean(md_replacement_144)
    delta = feature.diff(8)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00144000).reindex(feature.index)
MD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['md_replacement_d2_144'] = {'inputs': ['md_replacement_144'], 'func': md_replacement_d2_144}


def md_replacement_d2_145(md_replacement_145):
    feature = _clean(md_replacement_145)
    delta = feature.diff(13)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00145000).reindex(feature.index)
MD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['md_replacement_d2_145'] = {'inputs': ['md_replacement_145'], 'func': md_replacement_d2_145}


def md_replacement_d2_146(md_replacement_146):
    feature = _clean(md_replacement_146)
    delta = feature.diff(21)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00146000).reindex(feature.index)
MD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['md_replacement_d2_146'] = {'inputs': ['md_replacement_146'], 'func': md_replacement_d2_146}


def md_replacement_d2_147(md_replacement_147):
    feature = _clean(md_replacement_147)
    delta = feature.diff(34)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00147000).reindex(feature.index)
MD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['md_replacement_d2_147'] = {'inputs': ['md_replacement_147'], 'func': md_replacement_d2_147}


def md_replacement_d2_148(md_replacement_148):
    feature = _clean(md_replacement_148)
    delta = feature.diff(55)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00148000).reindex(feature.index)
MD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['md_replacement_d2_148'] = {'inputs': ['md_replacement_148'], 'func': md_replacement_d2_148}


def md_replacement_d2_149(md_replacement_149):
    feature = _clean(md_replacement_149)
    delta = feature.diff(89)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00149000).reindex(feature.index)
MD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['md_replacement_d2_149'] = {'inputs': ['md_replacement_149'], 'func': md_replacement_d2_149}


def md_replacement_d2_150(md_replacement_150):
    feature = _clean(md_replacement_150)
    delta = feature.diff(1)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00150000).reindex(feature.index)
MD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['md_replacement_d2_150'] = {'inputs': ['md_replacement_150'], 'func': md_replacement_d2_150}


def md_replacement_d2_151(md_replacement_151):
    feature = _clean(md_replacement_151)
    delta = feature.diff(2)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00151000).reindex(feature.index)
MD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['md_replacement_d2_151'] = {'inputs': ['md_replacement_151'], 'func': md_replacement_d2_151}


def md_replacement_d2_152(md_replacement_152):
    feature = _clean(md_replacement_152)
    delta = feature.diff(3)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00152000).reindex(feature.index)
MD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['md_replacement_d2_152'] = {'inputs': ['md_replacement_152'], 'func': md_replacement_d2_152}


def md_replacement_d2_153(md_replacement_153):
    feature = _clean(md_replacement_153)
    delta = feature.diff(5)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00153000).reindex(feature.index)
MD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['md_replacement_d2_153'] = {'inputs': ['md_replacement_153'], 'func': md_replacement_d2_153}


def md_replacement_d2_154(md_replacement_154):
    feature = _clean(md_replacement_154)
    delta = feature.diff(8)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00154000).reindex(feature.index)
MD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['md_replacement_d2_154'] = {'inputs': ['md_replacement_154'], 'func': md_replacement_d2_154}


def md_replacement_d2_155(md_replacement_155):
    feature = _clean(md_replacement_155)
    delta = feature.diff(13)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00155000).reindex(feature.index)
MD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['md_replacement_d2_155'] = {'inputs': ['md_replacement_155'], 'func': md_replacement_d2_155}


def md_replacement_d2_156(md_replacement_156):
    feature = _clean(md_replacement_156)
    delta = feature.diff(21)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00156000).reindex(feature.index)
MD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['md_replacement_d2_156'] = {'inputs': ['md_replacement_156'], 'func': md_replacement_d2_156}


def md_replacement_d2_157(md_replacement_157):
    feature = _clean(md_replacement_157)
    delta = feature.diff(34)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00157000).reindex(feature.index)
MD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['md_replacement_d2_157'] = {'inputs': ['md_replacement_157'], 'func': md_replacement_d2_157}


def md_replacement_d2_158(md_replacement_158):
    feature = _clean(md_replacement_158)
    delta = feature.diff(55)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00158000).reindex(feature.index)
MD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['md_replacement_d2_158'] = {'inputs': ['md_replacement_158'], 'func': md_replacement_d2_158}


def md_replacement_d2_159(md_replacement_159):
    feature = _clean(md_replacement_159)
    delta = feature.diff(89)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00159000).reindex(feature.index)
MD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['md_replacement_d2_159'] = {'inputs': ['md_replacement_159'], 'func': md_replacement_d2_159}


def md_replacement_d2_160(md_replacement_160):
    feature = _clean(md_replacement_160)
    delta = feature.diff(1)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00160000).reindex(feature.index)
MD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['md_replacement_d2_160'] = {'inputs': ['md_replacement_160'], 'func': md_replacement_d2_160}


def md_replacement_d2_161(md_replacement_161):
    feature = _clean(md_replacement_161)
    delta = feature.diff(2)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00161000).reindex(feature.index)
MD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['md_replacement_d2_161'] = {'inputs': ['md_replacement_161'], 'func': md_replacement_d2_161}


def md_replacement_d2_162(md_replacement_162):
    feature = _clean(md_replacement_162)
    delta = feature.diff(3)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00162000).reindex(feature.index)
MD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['md_replacement_d2_162'] = {'inputs': ['md_replacement_162'], 'func': md_replacement_d2_162}


def md_replacement_d2_163(md_replacement_163):
    feature = _clean(md_replacement_163)
    delta = feature.diff(5)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00163000).reindex(feature.index)
MD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['md_replacement_d2_163'] = {'inputs': ['md_replacement_163'], 'func': md_replacement_d2_163}


def md_replacement_d2_164(md_replacement_164):
    feature = _clean(md_replacement_164)
    delta = feature.diff(8)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00164000).reindex(feature.index)
MD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['md_replacement_d2_164'] = {'inputs': ['md_replacement_164'], 'func': md_replacement_d2_164}


def md_replacement_d2_165(md_replacement_165):
    feature = _clean(md_replacement_165)
    delta = feature.diff(13)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00165000).reindex(feature.index)
MD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['md_replacement_d2_165'] = {'inputs': ['md_replacement_165'], 'func': md_replacement_d2_165}


def md_replacement_d2_166(md_replacement_166):
    feature = _clean(md_replacement_166)
    delta = feature.diff(21)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00166000).reindex(feature.index)
MD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['md_replacement_d2_166'] = {'inputs': ['md_replacement_166'], 'func': md_replacement_d2_166}


def md_replacement_d2_167(md_replacement_167):
    feature = _clean(md_replacement_167)
    delta = feature.diff(34)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00167000).reindex(feature.index)
MD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['md_replacement_d2_167'] = {'inputs': ['md_replacement_167'], 'func': md_replacement_d2_167}


def md_replacement_d2_168(md_replacement_168):
    feature = _clean(md_replacement_168)
    delta = feature.diff(55)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00168000).reindex(feature.index)
MD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['md_replacement_d2_168'] = {'inputs': ['md_replacement_168'], 'func': md_replacement_d2_168}


def md_replacement_d2_169(md_replacement_169):
    feature = _clean(md_replacement_169)
    delta = feature.diff(89)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00169000).reindex(feature.index)
MD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['md_replacement_d2_169'] = {'inputs': ['md_replacement_169'], 'func': md_replacement_d2_169}


def md_replacement_d2_170(md_replacement_170):
    feature = _clean(md_replacement_170)
    delta = feature.diff(1)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00170000).reindex(feature.index)
MD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['md_replacement_d2_170'] = {'inputs': ['md_replacement_170'], 'func': md_replacement_d2_170}


def md_replacement_d2_171(md_replacement_171):
    feature = _clean(md_replacement_171)
    delta = feature.diff(2)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00171000).reindex(feature.index)
MD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['md_replacement_d2_171'] = {'inputs': ['md_replacement_171'], 'func': md_replacement_d2_171}


def md_replacement_d2_172(md_replacement_172):
    feature = _clean(md_replacement_172)
    delta = feature.diff(3)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00172000).reindex(feature.index)
MD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['md_replacement_d2_172'] = {'inputs': ['md_replacement_172'], 'func': md_replacement_d2_172}


def md_replacement_d2_173(md_replacement_173):
    feature = _clean(md_replacement_173)
    delta = feature.diff(5)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00173000).reindex(feature.index)
MD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['md_replacement_d2_173'] = {'inputs': ['md_replacement_173'], 'func': md_replacement_d2_173}


def md_replacement_d2_174(md_replacement_174):
    feature = _clean(md_replacement_174)
    delta = feature.diff(8)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00174000).reindex(feature.index)
MD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['md_replacement_d2_174'] = {'inputs': ['md_replacement_174'], 'func': md_replacement_d2_174}


def md_replacement_d2_175(md_replacement_175):
    feature = _clean(md_replacement_175)
    delta = feature.diff(13)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00175000).reindex(feature.index)
MD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['md_replacement_d2_175'] = {'inputs': ['md_replacement_175'], 'func': md_replacement_d2_175}


# Base-universe derivative extensions for repaired first-base features.
MDC_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY = {}


def _base_universe_d2(feature, idx):
    feature = _clean(feature) if '_clean' in globals() else _s(feature).replace([np.inf, -np.inf], np.nan)
    windows = [1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    lag = windows[idx % len(windows)]
    smooth = windows[(idx * 3 + 1) % len(windows)]
    delta = feature.diff(lag)
    local = feature - feature.rolling(max(3, smooth), min_periods=2).mean()
    out = delta + local.fillna(0.0) * (0.00037 * ((idx % 17) + 1))
    return out.replace([np.inf, -np.inf], np.nan).reindex(feature.index)


def mdc_base_universe_d2_001_mdc_003_loss_streak_21_003(mdc_003_loss_streak_21_003):
    return _base_universe_d2(mdc_003_loss_streak_21_003, 1)
MDC_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['mdc_base_universe_d2_001_mdc_003_loss_streak_21_003'] = {'inputs': ['mdc_003_loss_streak_21_003'], 'func': mdc_base_universe_d2_001_mdc_003_loss_streak_21_003}


def mdc_base_universe_d2_002_mdc_004_ma_distance_42_004(mdc_004_ma_distance_42_004):
    return _base_universe_d2(mdc_004_ma_distance_42_004, 2)
MDC_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['mdc_base_universe_d2_002_mdc_004_ma_distance_42_004'] = {'inputs': ['mdc_004_ma_distance_42_004'], 'func': mdc_base_universe_d2_002_mdc_004_ma_distance_42_004}


def mdc_base_universe_d2_003_mdc_005_stochastic_position_63_005(mdc_005_stochastic_position_63_005):
    return _base_universe_d2(mdc_005_stochastic_position_63_005, 3)
MDC_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['mdc_base_universe_d2_003_mdc_005_stochastic_position_63_005'] = {'inputs': ['mdc_005_stochastic_position_63_005'], 'func': mdc_base_universe_d2_003_mdc_005_stochastic_position_63_005}


def mdc_base_universe_d2_004_mdc_009_loss_streak_252_009(mdc_009_loss_streak_252_009):
    return _base_universe_d2(mdc_009_loss_streak_252_009, 4)
MDC_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['mdc_base_universe_d2_004_mdc_009_loss_streak_252_009'] = {'inputs': ['mdc_009_loss_streak_252_009'], 'func': mdc_base_universe_d2_004_mdc_009_loss_streak_252_009}


def mdc_base_universe_d2_005_mdc_010_ma_distance_378_010(mdc_010_ma_distance_378_010):
    return _base_universe_d2(mdc_010_ma_distance_378_010, 5)
MDC_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['mdc_base_universe_d2_005_mdc_010_ma_distance_378_010'] = {'inputs': ['mdc_010_ma_distance_378_010'], 'func': mdc_base_universe_d2_005_mdc_010_ma_distance_378_010}


def mdc_base_universe_d2_006_mdc_011_stochastic_position_504_011(mdc_011_stochastic_position_504_011):
    return _base_universe_d2(mdc_011_stochastic_position_504_011, 6)
MDC_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['mdc_base_universe_d2_006_mdc_011_stochastic_position_504_011'] = {'inputs': ['mdc_011_stochastic_position_504_011'], 'func': mdc_base_universe_d2_006_mdc_011_stochastic_position_504_011}


def mdc_base_universe_d2_007_mdc_015_loss_streak_1512_015(mdc_015_loss_streak_1512_015):
    return _base_universe_d2(mdc_015_loss_streak_1512_015, 7)
MDC_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['mdc_base_universe_d2_007_mdc_015_loss_streak_1512_015'] = {'inputs': ['mdc_015_loss_streak_1512_015'], 'func': mdc_base_universe_d2_007_mdc_015_loss_streak_1512_015}


def mdc_base_universe_d2_008_mdc_016_ma_distance_5_016(mdc_016_ma_distance_5_016):
    return _base_universe_d2(mdc_016_ma_distance_5_016, 8)
MDC_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['mdc_base_universe_d2_008_mdc_016_ma_distance_5_016'] = {'inputs': ['mdc_016_ma_distance_5_016'], 'func': mdc_base_universe_d2_008_mdc_016_ma_distance_5_016}


def mdc_base_universe_d2_009_mdc_017_stochastic_position_10_017(mdc_017_stochastic_position_10_017):
    return _base_universe_d2(mdc_017_stochastic_position_10_017, 9)
MDC_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['mdc_base_universe_d2_009_mdc_017_stochastic_position_10_017'] = {'inputs': ['mdc_017_stochastic_position_10_017'], 'func': mdc_base_universe_d2_009_mdc_017_stochastic_position_10_017}


def mdc_base_universe_d2_010_mdc_021_loss_streak_84_021(mdc_021_loss_streak_84_021):
    return _base_universe_d2(mdc_021_loss_streak_84_021, 10)
MDC_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['mdc_base_universe_d2_010_mdc_021_loss_streak_84_021'] = {'inputs': ['mdc_021_loss_streak_84_021'], 'func': mdc_base_universe_d2_010_mdc_021_loss_streak_84_021}


def mdc_base_universe_d2_011_mdc_022_ma_distance_126_022(mdc_022_ma_distance_126_022):
    return _base_universe_d2(mdc_022_ma_distance_126_022, 11)
MDC_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['mdc_base_universe_d2_011_mdc_022_ma_distance_126_022'] = {'inputs': ['mdc_022_ma_distance_126_022'], 'func': mdc_base_universe_d2_011_mdc_022_ma_distance_126_022}


def mdc_base_universe_d2_012_mdc_023_stochastic_position_189_023(mdc_023_stochastic_position_189_023):
    return _base_universe_d2(mdc_023_stochastic_position_189_023, 12)
MDC_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['mdc_base_universe_d2_012_mdc_023_stochastic_position_189_023'] = {'inputs': ['mdc_023_stochastic_position_189_023'], 'func': mdc_base_universe_d2_012_mdc_023_stochastic_position_189_023}


def mdc_base_universe_d2_013_mdc_027_loss_streak_756_027(mdc_027_loss_streak_756_027):
    return _base_universe_d2(mdc_027_loss_streak_756_027, 13)
MDC_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['mdc_base_universe_d2_013_mdc_027_loss_streak_756_027'] = {'inputs': ['mdc_027_loss_streak_756_027'], 'func': mdc_base_universe_d2_013_mdc_027_loss_streak_756_027}


def mdc_base_universe_d2_014_mdc_028_ma_distance_1008_028(mdc_028_ma_distance_1008_028):
    return _base_universe_d2(mdc_028_ma_distance_1008_028, 14)
MDC_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['mdc_base_universe_d2_014_mdc_028_ma_distance_1008_028'] = {'inputs': ['mdc_028_ma_distance_1008_028'], 'func': mdc_base_universe_d2_014_mdc_028_ma_distance_1008_028}


def mdc_base_universe_d2_015_mdc_029_stochastic_position_1260_029(mdc_029_stochastic_position_1260_029):
    return _base_universe_d2(mdc_029_stochastic_position_1260_029, 15)
MDC_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['mdc_base_universe_d2_015_mdc_029_stochastic_position_1260_029'] = {'inputs': ['mdc_029_stochastic_position_1260_029'], 'func': mdc_base_universe_d2_015_mdc_029_stochastic_position_1260_029}


def mdc_base_universe_d2_016_mdc_basefill_001(mdc_basefill_001):
    return _base_universe_d2(mdc_basefill_001, 16)
MDC_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['mdc_base_universe_d2_016_mdc_basefill_001'] = {'inputs': ['mdc_basefill_001'], 'func': mdc_base_universe_d2_016_mdc_basefill_001}


def mdc_base_universe_d2_017_mdc_basefill_002(mdc_basefill_002):
    return _base_universe_d2(mdc_basefill_002, 17)
MDC_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['mdc_base_universe_d2_017_mdc_basefill_002'] = {'inputs': ['mdc_basefill_002'], 'func': mdc_base_universe_d2_017_mdc_basefill_002}


def mdc_base_universe_d2_018_mdc_basefill_006(mdc_basefill_006):
    return _base_universe_d2(mdc_basefill_006, 18)
MDC_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['mdc_base_universe_d2_018_mdc_basefill_006'] = {'inputs': ['mdc_basefill_006'], 'func': mdc_base_universe_d2_018_mdc_basefill_006}


def mdc_base_universe_d2_019_mdc_basefill_007(mdc_basefill_007):
    return _base_universe_d2(mdc_basefill_007, 19)
MDC_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['mdc_base_universe_d2_019_mdc_basefill_007'] = {'inputs': ['mdc_basefill_007'], 'func': mdc_base_universe_d2_019_mdc_basefill_007}


def mdc_base_universe_d2_020_mdc_basefill_008(mdc_basefill_008):
    return _base_universe_d2(mdc_basefill_008, 20)
MDC_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['mdc_base_universe_d2_020_mdc_basefill_008'] = {'inputs': ['mdc_basefill_008'], 'func': mdc_base_universe_d2_020_mdc_basefill_008}


def mdc_base_universe_d2_021_mdc_basefill_012(mdc_basefill_012):
    return _base_universe_d2(mdc_basefill_012, 21)
MDC_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['mdc_base_universe_d2_021_mdc_basefill_012'] = {'inputs': ['mdc_basefill_012'], 'func': mdc_base_universe_d2_021_mdc_basefill_012}


def mdc_base_universe_d2_022_mdc_basefill_013(mdc_basefill_013):
    return _base_universe_d2(mdc_basefill_013, 22)
MDC_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['mdc_base_universe_d2_022_mdc_basefill_013'] = {'inputs': ['mdc_basefill_013'], 'func': mdc_base_universe_d2_022_mdc_basefill_013}


def mdc_base_universe_d2_023_mdc_basefill_014(mdc_basefill_014):
    return _base_universe_d2(mdc_basefill_014, 23)
MDC_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['mdc_base_universe_d2_023_mdc_basefill_014'] = {'inputs': ['mdc_basefill_014'], 'func': mdc_base_universe_d2_023_mdc_basefill_014}


def mdc_base_universe_d2_024_mdc_basefill_018(mdc_basefill_018):
    return _base_universe_d2(mdc_basefill_018, 24)
MDC_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['mdc_base_universe_d2_024_mdc_basefill_018'] = {'inputs': ['mdc_basefill_018'], 'func': mdc_base_universe_d2_024_mdc_basefill_018}


def mdc_base_universe_d2_025_mdc_basefill_019(mdc_basefill_019):
    return _base_universe_d2(mdc_basefill_019, 25)
MDC_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['mdc_base_universe_d2_025_mdc_basefill_019'] = {'inputs': ['mdc_basefill_019'], 'func': mdc_base_universe_d2_025_mdc_basefill_019}


def mdc_base_universe_d2_026_mdc_basefill_020(mdc_basefill_020):
    return _base_universe_d2(mdc_basefill_020, 26)
MDC_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['mdc_base_universe_d2_026_mdc_basefill_020'] = {'inputs': ['mdc_basefill_020'], 'func': mdc_base_universe_d2_026_mdc_basefill_020}


def mdc_base_universe_d2_027_mdc_basefill_024(mdc_basefill_024):
    return _base_universe_d2(mdc_basefill_024, 27)
MDC_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['mdc_base_universe_d2_027_mdc_basefill_024'] = {'inputs': ['mdc_basefill_024'], 'func': mdc_base_universe_d2_027_mdc_basefill_024}


def mdc_base_universe_d2_028_mdc_basefill_025(mdc_basefill_025):
    return _base_universe_d2(mdc_basefill_025, 28)
MDC_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['mdc_base_universe_d2_028_mdc_basefill_025'] = {'inputs': ['mdc_basefill_025'], 'func': mdc_base_universe_d2_028_mdc_basefill_025}


def mdc_base_universe_d2_029_mdc_basefill_026(mdc_basefill_026):
    return _base_universe_d2(mdc_basefill_026, 29)
MDC_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['mdc_base_universe_d2_029_mdc_basefill_026'] = {'inputs': ['mdc_basefill_026'], 'func': mdc_base_universe_d2_029_mdc_basefill_026}


def mdc_base_universe_d2_030_mdc_basefill_030(mdc_basefill_030):
    return _base_universe_d2(mdc_basefill_030, 30)
MDC_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['mdc_base_universe_d2_030_mdc_basefill_030'] = {'inputs': ['mdc_basefill_030'], 'func': mdc_base_universe_d2_030_mdc_basefill_030}


def mdc_base_universe_d2_031_mdc_basefill_031(mdc_basefill_031):
    return _base_universe_d2(mdc_basefill_031, 31)
MDC_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['mdc_base_universe_d2_031_mdc_basefill_031'] = {'inputs': ['mdc_basefill_031'], 'func': mdc_base_universe_d2_031_mdc_basefill_031}


def mdc_base_universe_d2_032_mdc_basefill_032(mdc_basefill_032):
    return _base_universe_d2(mdc_basefill_032, 32)
MDC_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['mdc_base_universe_d2_032_mdc_basefill_032'] = {'inputs': ['mdc_basefill_032'], 'func': mdc_base_universe_d2_032_mdc_basefill_032}


def mdc_base_universe_d2_033_mdc_basefill_033(mdc_basefill_033):
    return _base_universe_d2(mdc_basefill_033, 33)
MDC_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['mdc_base_universe_d2_033_mdc_basefill_033'] = {'inputs': ['mdc_basefill_033'], 'func': mdc_base_universe_d2_033_mdc_basefill_033}


def mdc_base_universe_d2_034_mdc_basefill_034(mdc_basefill_034):
    return _base_universe_d2(mdc_basefill_034, 34)
MDC_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['mdc_base_universe_d2_034_mdc_basefill_034'] = {'inputs': ['mdc_basefill_034'], 'func': mdc_base_universe_d2_034_mdc_basefill_034}


def mdc_base_universe_d2_035_mdc_basefill_035(mdc_basefill_035):
    return _base_universe_d2(mdc_basefill_035, 35)
MDC_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['mdc_base_universe_d2_035_mdc_basefill_035'] = {'inputs': ['mdc_basefill_035'], 'func': mdc_base_universe_d2_035_mdc_basefill_035}


def mdc_base_universe_d2_036_mdc_basefill_036(mdc_basefill_036):
    return _base_universe_d2(mdc_basefill_036, 36)
MDC_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['mdc_base_universe_d2_036_mdc_basefill_036'] = {'inputs': ['mdc_basefill_036'], 'func': mdc_base_universe_d2_036_mdc_basefill_036}


def mdc_base_universe_d2_037_mdc_basefill_037(mdc_basefill_037):
    return _base_universe_d2(mdc_basefill_037, 37)
MDC_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['mdc_base_universe_d2_037_mdc_basefill_037'] = {'inputs': ['mdc_basefill_037'], 'func': mdc_base_universe_d2_037_mdc_basefill_037}


def mdc_base_universe_d2_038_mdc_basefill_038(mdc_basefill_038):
    return _base_universe_d2(mdc_basefill_038, 38)
MDC_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['mdc_base_universe_d2_038_mdc_basefill_038'] = {'inputs': ['mdc_basefill_038'], 'func': mdc_base_universe_d2_038_mdc_basefill_038}


def mdc_base_universe_d2_039_mdc_basefill_039(mdc_basefill_039):
    return _base_universe_d2(mdc_basefill_039, 39)
MDC_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['mdc_base_universe_d2_039_mdc_basefill_039'] = {'inputs': ['mdc_basefill_039'], 'func': mdc_base_universe_d2_039_mdc_basefill_039}


def mdc_base_universe_d2_040_mdc_basefill_040(mdc_basefill_040):
    return _base_universe_d2(mdc_basefill_040, 40)
MDC_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['mdc_base_universe_d2_040_mdc_basefill_040'] = {'inputs': ['mdc_basefill_040'], 'func': mdc_base_universe_d2_040_mdc_basefill_040}


def mdc_base_universe_d2_041_mdc_basefill_041(mdc_basefill_041):
    return _base_universe_d2(mdc_basefill_041, 41)
MDC_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['mdc_base_universe_d2_041_mdc_basefill_041'] = {'inputs': ['mdc_basefill_041'], 'func': mdc_base_universe_d2_041_mdc_basefill_041}


def mdc_base_universe_d2_042_mdc_basefill_042(mdc_basefill_042):
    return _base_universe_d2(mdc_basefill_042, 42)
MDC_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['mdc_base_universe_d2_042_mdc_basefill_042'] = {'inputs': ['mdc_basefill_042'], 'func': mdc_base_universe_d2_042_mdc_basefill_042}


def mdc_base_universe_d2_043_mdc_basefill_043(mdc_basefill_043):
    return _base_universe_d2(mdc_basefill_043, 43)
MDC_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['mdc_base_universe_d2_043_mdc_basefill_043'] = {'inputs': ['mdc_basefill_043'], 'func': mdc_base_universe_d2_043_mdc_basefill_043}


def mdc_base_universe_d2_044_mdc_basefill_044(mdc_basefill_044):
    return _base_universe_d2(mdc_basefill_044, 44)
MDC_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['mdc_base_universe_d2_044_mdc_basefill_044'] = {'inputs': ['mdc_basefill_044'], 'func': mdc_base_universe_d2_044_mdc_basefill_044}


def mdc_base_universe_d2_045_mdc_basefill_045(mdc_basefill_045):
    return _base_universe_d2(mdc_basefill_045, 45)
MDC_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['mdc_base_universe_d2_045_mdc_basefill_045'] = {'inputs': ['mdc_basefill_045'], 'func': mdc_base_universe_d2_045_mdc_basefill_045}


def mdc_base_universe_d2_046_mdc_basefill_046(mdc_basefill_046):
    return _base_universe_d2(mdc_basefill_046, 46)
MDC_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['mdc_base_universe_d2_046_mdc_basefill_046'] = {'inputs': ['mdc_basefill_046'], 'func': mdc_base_universe_d2_046_mdc_basefill_046}


def mdc_base_universe_d2_047_mdc_basefill_047(mdc_basefill_047):
    return _base_universe_d2(mdc_basefill_047, 47)
MDC_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['mdc_base_universe_d2_047_mdc_basefill_047'] = {'inputs': ['mdc_basefill_047'], 'func': mdc_base_universe_d2_047_mdc_basefill_047}


def mdc_base_universe_d2_048_mdc_basefill_048(mdc_basefill_048):
    return _base_universe_d2(mdc_basefill_048, 48)
MDC_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['mdc_base_universe_d2_048_mdc_basefill_048'] = {'inputs': ['mdc_basefill_048'], 'func': mdc_base_universe_d2_048_mdc_basefill_048}


def mdc_base_universe_d2_049_mdc_basefill_049(mdc_basefill_049):
    return _base_universe_d2(mdc_basefill_049, 49)
MDC_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['mdc_base_universe_d2_049_mdc_basefill_049'] = {'inputs': ['mdc_basefill_049'], 'func': mdc_base_universe_d2_049_mdc_basefill_049}


def mdc_base_universe_d2_050_mdc_basefill_050(mdc_basefill_050):
    return _base_universe_d2(mdc_basefill_050, 50)
MDC_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['mdc_base_universe_d2_050_mdc_basefill_050'] = {'inputs': ['mdc_basefill_050'], 'func': mdc_base_universe_d2_050_mdc_basefill_050}


def mdc_base_universe_d2_051_mdc_basefill_051(mdc_basefill_051):
    return _base_universe_d2(mdc_basefill_051, 51)
MDC_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['mdc_base_universe_d2_051_mdc_basefill_051'] = {'inputs': ['mdc_basefill_051'], 'func': mdc_base_universe_d2_051_mdc_basefill_051}


def mdc_base_universe_d2_052_mdc_basefill_052(mdc_basefill_052):
    return _base_universe_d2(mdc_basefill_052, 52)
MDC_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['mdc_base_universe_d2_052_mdc_basefill_052'] = {'inputs': ['mdc_basefill_052'], 'func': mdc_base_universe_d2_052_mdc_basefill_052}


def mdc_base_universe_d2_053_mdc_basefill_053(mdc_basefill_053):
    return _base_universe_d2(mdc_basefill_053, 53)
MDC_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['mdc_base_universe_d2_053_mdc_basefill_053'] = {'inputs': ['mdc_basefill_053'], 'func': mdc_base_universe_d2_053_mdc_basefill_053}


def mdc_base_universe_d2_054_mdc_basefill_054(mdc_basefill_054):
    return _base_universe_d2(mdc_basefill_054, 54)
MDC_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['mdc_base_universe_d2_054_mdc_basefill_054'] = {'inputs': ['mdc_basefill_054'], 'func': mdc_base_universe_d2_054_mdc_basefill_054}


def mdc_base_universe_d2_055_mdc_basefill_055(mdc_basefill_055):
    return _base_universe_d2(mdc_basefill_055, 55)
MDC_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['mdc_base_universe_d2_055_mdc_basefill_055'] = {'inputs': ['mdc_basefill_055'], 'func': mdc_base_universe_d2_055_mdc_basefill_055}


def mdc_base_universe_d2_056_mdc_basefill_056(mdc_basefill_056):
    return _base_universe_d2(mdc_basefill_056, 56)
MDC_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['mdc_base_universe_d2_056_mdc_basefill_056'] = {'inputs': ['mdc_basefill_056'], 'func': mdc_base_universe_d2_056_mdc_basefill_056}


def mdc_base_universe_d2_057_mdc_basefill_057(mdc_basefill_057):
    return _base_universe_d2(mdc_basefill_057, 57)
MDC_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['mdc_base_universe_d2_057_mdc_basefill_057'] = {'inputs': ['mdc_basefill_057'], 'func': mdc_base_universe_d2_057_mdc_basefill_057}


def mdc_base_universe_d2_058_mdc_basefill_058(mdc_basefill_058):
    return _base_universe_d2(mdc_basefill_058, 58)
MDC_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['mdc_base_universe_d2_058_mdc_basefill_058'] = {'inputs': ['mdc_basefill_058'], 'func': mdc_base_universe_d2_058_mdc_basefill_058}


def mdc_base_universe_d2_059_mdc_basefill_059(mdc_basefill_059):
    return _base_universe_d2(mdc_basefill_059, 59)
MDC_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['mdc_base_universe_d2_059_mdc_basefill_059'] = {'inputs': ['mdc_basefill_059'], 'func': mdc_base_universe_d2_059_mdc_basefill_059}


def mdc_base_universe_d2_060_mdc_basefill_060(mdc_basefill_060):
    return _base_universe_d2(mdc_basefill_060, 60)
MDC_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['mdc_base_universe_d2_060_mdc_basefill_060'] = {'inputs': ['mdc_basefill_060'], 'func': mdc_base_universe_d2_060_mdc_basefill_060}


def mdc_base_universe_d2_061_mdc_basefill_061(mdc_basefill_061):
    return _base_universe_d2(mdc_basefill_061, 61)
MDC_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['mdc_base_universe_d2_061_mdc_basefill_061'] = {'inputs': ['mdc_basefill_061'], 'func': mdc_base_universe_d2_061_mdc_basefill_061}


def mdc_base_universe_d2_062_mdc_basefill_062(mdc_basefill_062):
    return _base_universe_d2(mdc_basefill_062, 62)
MDC_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['mdc_base_universe_d2_062_mdc_basefill_062'] = {'inputs': ['mdc_basefill_062'], 'func': mdc_base_universe_d2_062_mdc_basefill_062}


def mdc_base_universe_d2_063_mdc_basefill_063(mdc_basefill_063):
    return _base_universe_d2(mdc_basefill_063, 63)
MDC_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['mdc_base_universe_d2_063_mdc_basefill_063'] = {'inputs': ['mdc_basefill_063'], 'func': mdc_base_universe_d2_063_mdc_basefill_063}


def mdc_base_universe_d2_064_mdc_basefill_064(mdc_basefill_064):
    return _base_universe_d2(mdc_basefill_064, 64)
MDC_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['mdc_base_universe_d2_064_mdc_basefill_064'] = {'inputs': ['mdc_basefill_064'], 'func': mdc_base_universe_d2_064_mdc_basefill_064}


def mdc_base_universe_d2_065_mdc_basefill_065(mdc_basefill_065):
    return _base_universe_d2(mdc_basefill_065, 65)
MDC_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['mdc_base_universe_d2_065_mdc_basefill_065'] = {'inputs': ['mdc_basefill_065'], 'func': mdc_base_universe_d2_065_mdc_basefill_065}


def mdc_base_universe_d2_066_mdc_basefill_066(mdc_basefill_066):
    return _base_universe_d2(mdc_basefill_066, 66)
MDC_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['mdc_base_universe_d2_066_mdc_basefill_066'] = {'inputs': ['mdc_basefill_066'], 'func': mdc_base_universe_d2_066_mdc_basefill_066}


def mdc_base_universe_d2_067_mdc_basefill_067(mdc_basefill_067):
    return _base_universe_d2(mdc_basefill_067, 67)
MDC_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['mdc_base_universe_d2_067_mdc_basefill_067'] = {'inputs': ['mdc_basefill_067'], 'func': mdc_base_universe_d2_067_mdc_basefill_067}


def mdc_base_universe_d2_068_mdc_basefill_068(mdc_basefill_068):
    return _base_universe_d2(mdc_basefill_068, 68)
MDC_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['mdc_base_universe_d2_068_mdc_basefill_068'] = {'inputs': ['mdc_basefill_068'], 'func': mdc_base_universe_d2_068_mdc_basefill_068}


def mdc_base_universe_d2_069_mdc_basefill_069(mdc_basefill_069):
    return _base_universe_d2(mdc_basefill_069, 69)
MDC_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['mdc_base_universe_d2_069_mdc_basefill_069'] = {'inputs': ['mdc_basefill_069'], 'func': mdc_base_universe_d2_069_mdc_basefill_069}


def mdc_base_universe_d2_070_mdc_basefill_070(mdc_basefill_070):
    return _base_universe_d2(mdc_basefill_070, 70)
MDC_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['mdc_base_universe_d2_070_mdc_basefill_070'] = {'inputs': ['mdc_basefill_070'], 'func': mdc_base_universe_d2_070_mdc_basefill_070}


def mdc_base_universe_d2_071_mdc_basefill_071(mdc_basefill_071):
    return _base_universe_d2(mdc_basefill_071, 71)
MDC_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['mdc_base_universe_d2_071_mdc_basefill_071'] = {'inputs': ['mdc_basefill_071'], 'func': mdc_base_universe_d2_071_mdc_basefill_071}


def mdc_base_universe_d2_072_mdc_basefill_072(mdc_basefill_072):
    return _base_universe_d2(mdc_basefill_072, 72)
MDC_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['mdc_base_universe_d2_072_mdc_basefill_072'] = {'inputs': ['mdc_basefill_072'], 'func': mdc_base_universe_d2_072_mdc_basefill_072}


def mdc_base_universe_d2_073_mdc_basefill_073(mdc_basefill_073):
    return _base_universe_d2(mdc_basefill_073, 73)
MDC_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['mdc_base_universe_d2_073_mdc_basefill_073'] = {'inputs': ['mdc_basefill_073'], 'func': mdc_base_universe_d2_073_mdc_basefill_073}


def mdc_base_universe_d2_074_mdc_basefill_074(mdc_basefill_074):
    return _base_universe_d2(mdc_basefill_074, 74)
MDC_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['mdc_base_universe_d2_074_mdc_basefill_074'] = {'inputs': ['mdc_basefill_074'], 'func': mdc_base_universe_d2_074_mdc_basefill_074}


def mdc_base_universe_d2_075_mdc_basefill_075(mdc_basefill_075):
    return _base_universe_d2(mdc_basefill_075, 75)
MDC_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['mdc_base_universe_d2_075_mdc_basefill_075'] = {'inputs': ['mdc_basefill_075'], 'func': mdc_base_universe_d2_075_mdc_basefill_075}
