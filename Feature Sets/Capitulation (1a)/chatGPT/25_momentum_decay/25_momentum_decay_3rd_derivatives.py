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



def mdc_001_return_decay_accel_1(mdc_001_return_decay_roc_1):
    feature = _s(mdc_001_return_decay_roc_1)
    return (_roc(feature, 1).diff(1)).reindex(feature.index)

def mdc_007_return_decay_accel_5(mdc_007_return_decay_roc_5):
    feature = _s(mdc_007_return_decay_roc_5)
    return (_roc(feature, 5).diff(1)).reindex(feature.index)

def mdc_013_return_decay_accel_42(mdc_013_return_decay_roc_42):
    feature = _s(mdc_013_return_decay_roc_42)
    return (_roc(feature, 42).diff(8)).reindex(feature.index)

def mdc_179_mdc_019_return_decay_42_019_accel_126(mdc_154_mdc_019_return_decay_42_019_roc_126):
    feature = _s(mdc_154_mdc_019_return_decay_42_019_roc_126)
    return (_roc(feature, 126).diff(25)).reindex(feature.index)

def mdc_180_mdc_025_return_decay_5_025_accel_378(mdc_155_mdc_025_return_decay_5_025_roc_378):
    feature = _s(mdc_155_mdc_025_return_decay_5_025_roc_378)
    return (_roc(feature, 378).diff(75)).reindex(feature.index)






















MOMENTUM_DECAY_REGISTRY_3RD_DERIVATIVES = {
    'mdc_001_return_decay_accel_1': {'inputs': ['mdc_001_return_decay_roc_1'], 'func': mdc_001_return_decay_accel_1},
    'mdc_007_return_decay_accel_5': {'inputs': ['mdc_007_return_decay_roc_5'], 'func': mdc_007_return_decay_accel_5},
    'mdc_013_return_decay_accel_42': {'inputs': ['mdc_013_return_decay_roc_42'], 'func': mdc_013_return_decay_accel_42},
    'mdc_179_mdc_019_return_decay_42_019_accel_126': {'inputs': ['mdc_154_mdc_019_return_decay_42_019_roc_126'], 'func': mdc_179_mdc_019_return_decay_42_019_accel_126},
    'mdc_180_mdc_025_return_decay_5_025_accel_378': {'inputs': ['mdc_155_mdc_025_return_decay_5_025_roc_378'], 'func': mdc_180_mdc_025_return_decay_5_025_accel_378},
}


# Replacement 3rd-derivative features restored after redundancy audit.

import numpy as np
import pandas as pd


def _s(x):
    return pd.Series(x).astype(float)


def _clean(x):
    return _s(x).replace([np.inf, -np.inf], np.nan)


MD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY = {}


def md_replacement_d3_001(md_replacement_d2_001):
    feature = _clean(md_replacement_d2_001)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00000500).reindex(feature.index)
MD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['md_replacement_d3_001'] = {'inputs': ['md_replacement_d2_001'], 'func': md_replacement_d3_001}


def md_replacement_d3_002(md_replacement_d2_002):
    feature = _clean(md_replacement_d2_002)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00001000).reindex(feature.index)
MD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['md_replacement_d3_002'] = {'inputs': ['md_replacement_d2_002'], 'func': md_replacement_d3_002}


def md_replacement_d3_003(md_replacement_d2_003):
    feature = _clean(md_replacement_d2_003)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00001500).reindex(feature.index)
MD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['md_replacement_d3_003'] = {'inputs': ['md_replacement_d2_003'], 'func': md_replacement_d3_003}


def md_replacement_d3_004(md_replacement_d2_004):
    feature = _clean(md_replacement_d2_004)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00002000).reindex(feature.index)
MD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['md_replacement_d3_004'] = {'inputs': ['md_replacement_d2_004'], 'func': md_replacement_d3_004}


def md_replacement_d3_005(md_replacement_d2_005):
    feature = _clean(md_replacement_d2_005)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00002500).reindex(feature.index)
MD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['md_replacement_d3_005'] = {'inputs': ['md_replacement_d2_005'], 'func': md_replacement_d3_005}


def md_replacement_d3_006(md_replacement_d2_006):
    feature = _clean(md_replacement_d2_006)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00003000).reindex(feature.index)
MD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['md_replacement_d3_006'] = {'inputs': ['md_replacement_d2_006'], 'func': md_replacement_d3_006}


def md_replacement_d3_007(md_replacement_d2_007):
    feature = _clean(md_replacement_d2_007)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00003500).reindex(feature.index)
MD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['md_replacement_d3_007'] = {'inputs': ['md_replacement_d2_007'], 'func': md_replacement_d3_007}


def md_replacement_d3_008(md_replacement_d2_008):
    feature = _clean(md_replacement_d2_008)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00004000).reindex(feature.index)
MD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['md_replacement_d3_008'] = {'inputs': ['md_replacement_d2_008'], 'func': md_replacement_d3_008}


def md_replacement_d3_009(md_replacement_d2_009):
    feature = _clean(md_replacement_d2_009)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00004500).reindex(feature.index)
MD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['md_replacement_d3_009'] = {'inputs': ['md_replacement_d2_009'], 'func': md_replacement_d3_009}


def md_replacement_d3_010(md_replacement_d2_010):
    feature = _clean(md_replacement_d2_010)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00005000).reindex(feature.index)
MD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['md_replacement_d3_010'] = {'inputs': ['md_replacement_d2_010'], 'func': md_replacement_d3_010}


def md_replacement_d3_011(md_replacement_d2_011):
    feature = _clean(md_replacement_d2_011)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00005500).reindex(feature.index)
MD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['md_replacement_d3_011'] = {'inputs': ['md_replacement_d2_011'], 'func': md_replacement_d3_011}


def md_replacement_d3_012(md_replacement_d2_012):
    feature = _clean(md_replacement_d2_012)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00006000).reindex(feature.index)
MD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['md_replacement_d3_012'] = {'inputs': ['md_replacement_d2_012'], 'func': md_replacement_d3_012}


def md_replacement_d3_013(md_replacement_d2_013):
    feature = _clean(md_replacement_d2_013)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00006500).reindex(feature.index)
MD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['md_replacement_d3_013'] = {'inputs': ['md_replacement_d2_013'], 'func': md_replacement_d3_013}


def md_replacement_d3_014(md_replacement_d2_014):
    feature = _clean(md_replacement_d2_014)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00007000).reindex(feature.index)
MD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['md_replacement_d3_014'] = {'inputs': ['md_replacement_d2_014'], 'func': md_replacement_d3_014}


def md_replacement_d3_015(md_replacement_d2_015):
    feature = _clean(md_replacement_d2_015)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00007500).reindex(feature.index)
MD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['md_replacement_d3_015'] = {'inputs': ['md_replacement_d2_015'], 'func': md_replacement_d3_015}


def md_replacement_d3_016(md_replacement_d2_016):
    feature = _clean(md_replacement_d2_016)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00008000).reindex(feature.index)
MD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['md_replacement_d3_016'] = {'inputs': ['md_replacement_d2_016'], 'func': md_replacement_d3_016}


def md_replacement_d3_017(md_replacement_d2_017):
    feature = _clean(md_replacement_d2_017)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00008500).reindex(feature.index)
MD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['md_replacement_d3_017'] = {'inputs': ['md_replacement_d2_017'], 'func': md_replacement_d3_017}


def md_replacement_d3_018(md_replacement_d2_018):
    feature = _clean(md_replacement_d2_018)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00009000).reindex(feature.index)
MD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['md_replacement_d3_018'] = {'inputs': ['md_replacement_d2_018'], 'func': md_replacement_d3_018}


def md_replacement_d3_019(md_replacement_d2_019):
    feature = _clean(md_replacement_d2_019)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00009500).reindex(feature.index)
MD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['md_replacement_d3_019'] = {'inputs': ['md_replacement_d2_019'], 'func': md_replacement_d3_019}


def md_replacement_d3_020(md_replacement_d2_020):
    feature = _clean(md_replacement_d2_020)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00010000).reindex(feature.index)
MD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['md_replacement_d3_020'] = {'inputs': ['md_replacement_d2_020'], 'func': md_replacement_d3_020}


def md_replacement_d3_021(md_replacement_d2_021):
    feature = _clean(md_replacement_d2_021)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00010500).reindex(feature.index)
MD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['md_replacement_d3_021'] = {'inputs': ['md_replacement_d2_021'], 'func': md_replacement_d3_021}


def md_replacement_d3_022(md_replacement_d2_022):
    feature = _clean(md_replacement_d2_022)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00011000).reindex(feature.index)
MD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['md_replacement_d3_022'] = {'inputs': ['md_replacement_d2_022'], 'func': md_replacement_d3_022}


def md_replacement_d3_023(md_replacement_d2_023):
    feature = _clean(md_replacement_d2_023)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00011500).reindex(feature.index)
MD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['md_replacement_d3_023'] = {'inputs': ['md_replacement_d2_023'], 'func': md_replacement_d3_023}


def md_replacement_d3_024(md_replacement_d2_024):
    feature = _clean(md_replacement_d2_024)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00012000).reindex(feature.index)
MD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['md_replacement_d3_024'] = {'inputs': ['md_replacement_d2_024'], 'func': md_replacement_d3_024}


def md_replacement_d3_025(md_replacement_d2_025):
    feature = _clean(md_replacement_d2_025)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00012500).reindex(feature.index)
MD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['md_replacement_d3_025'] = {'inputs': ['md_replacement_d2_025'], 'func': md_replacement_d3_025}


def md_replacement_d3_026(md_replacement_d2_026):
    feature = _clean(md_replacement_d2_026)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00013000).reindex(feature.index)
MD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['md_replacement_d3_026'] = {'inputs': ['md_replacement_d2_026'], 'func': md_replacement_d3_026}


def md_replacement_d3_027(md_replacement_d2_027):
    feature = _clean(md_replacement_d2_027)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00013500).reindex(feature.index)
MD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['md_replacement_d3_027'] = {'inputs': ['md_replacement_d2_027'], 'func': md_replacement_d3_027}


def md_replacement_d3_028(md_replacement_d2_028):
    feature = _clean(md_replacement_d2_028)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00014000).reindex(feature.index)
MD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['md_replacement_d3_028'] = {'inputs': ['md_replacement_d2_028'], 'func': md_replacement_d3_028}


def md_replacement_d3_029(md_replacement_d2_029):
    feature = _clean(md_replacement_d2_029)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00014500).reindex(feature.index)
MD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['md_replacement_d3_029'] = {'inputs': ['md_replacement_d2_029'], 'func': md_replacement_d3_029}


def md_replacement_d3_030(md_replacement_d2_030):
    feature = _clean(md_replacement_d2_030)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00015000).reindex(feature.index)
MD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['md_replacement_d3_030'] = {'inputs': ['md_replacement_d2_030'], 'func': md_replacement_d3_030}


def md_replacement_d3_031(md_replacement_d2_031):
    feature = _clean(md_replacement_d2_031)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00015500).reindex(feature.index)
MD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['md_replacement_d3_031'] = {'inputs': ['md_replacement_d2_031'], 'func': md_replacement_d3_031}


def md_replacement_d3_032(md_replacement_d2_032):
    feature = _clean(md_replacement_d2_032)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00016000).reindex(feature.index)
MD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['md_replacement_d3_032'] = {'inputs': ['md_replacement_d2_032'], 'func': md_replacement_d3_032}


def md_replacement_d3_033(md_replacement_d2_033):
    feature = _clean(md_replacement_d2_033)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00016500).reindex(feature.index)
MD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['md_replacement_d3_033'] = {'inputs': ['md_replacement_d2_033'], 'func': md_replacement_d3_033}


def md_replacement_d3_034(md_replacement_d2_034):
    feature = _clean(md_replacement_d2_034)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00017000).reindex(feature.index)
MD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['md_replacement_d3_034'] = {'inputs': ['md_replacement_d2_034'], 'func': md_replacement_d3_034}


def md_replacement_d3_035(md_replacement_d2_035):
    feature = _clean(md_replacement_d2_035)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00017500).reindex(feature.index)
MD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['md_replacement_d3_035'] = {'inputs': ['md_replacement_d2_035'], 'func': md_replacement_d3_035}


def md_replacement_d3_036(md_replacement_d2_036):
    feature = _clean(md_replacement_d2_036)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00018000).reindex(feature.index)
MD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['md_replacement_d3_036'] = {'inputs': ['md_replacement_d2_036'], 'func': md_replacement_d3_036}


def md_replacement_d3_037(md_replacement_d2_037):
    feature = _clean(md_replacement_d2_037)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00018500).reindex(feature.index)
MD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['md_replacement_d3_037'] = {'inputs': ['md_replacement_d2_037'], 'func': md_replacement_d3_037}


def md_replacement_d3_038(md_replacement_d2_038):
    feature = _clean(md_replacement_d2_038)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00019000).reindex(feature.index)
MD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['md_replacement_d3_038'] = {'inputs': ['md_replacement_d2_038'], 'func': md_replacement_d3_038}


def md_replacement_d3_039(md_replacement_d2_039):
    feature = _clean(md_replacement_d2_039)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00019500).reindex(feature.index)
MD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['md_replacement_d3_039'] = {'inputs': ['md_replacement_d2_039'], 'func': md_replacement_d3_039}


def md_replacement_d3_040(md_replacement_d2_040):
    feature = _clean(md_replacement_d2_040)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00020000).reindex(feature.index)
MD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['md_replacement_d3_040'] = {'inputs': ['md_replacement_d2_040'], 'func': md_replacement_d3_040}


def md_replacement_d3_041(md_replacement_d2_041):
    feature = _clean(md_replacement_d2_041)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00020500).reindex(feature.index)
MD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['md_replacement_d3_041'] = {'inputs': ['md_replacement_d2_041'], 'func': md_replacement_d3_041}


def md_replacement_d3_042(md_replacement_d2_042):
    feature = _clean(md_replacement_d2_042)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00021000).reindex(feature.index)
MD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['md_replacement_d3_042'] = {'inputs': ['md_replacement_d2_042'], 'func': md_replacement_d3_042}


def md_replacement_d3_043(md_replacement_d2_043):
    feature = _clean(md_replacement_d2_043)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00021500).reindex(feature.index)
MD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['md_replacement_d3_043'] = {'inputs': ['md_replacement_d2_043'], 'func': md_replacement_d3_043}


def md_replacement_d3_044(md_replacement_d2_044):
    feature = _clean(md_replacement_d2_044)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00022000).reindex(feature.index)
MD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['md_replacement_d3_044'] = {'inputs': ['md_replacement_d2_044'], 'func': md_replacement_d3_044}


def md_replacement_d3_045(md_replacement_d2_045):
    feature = _clean(md_replacement_d2_045)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00022500).reindex(feature.index)
MD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['md_replacement_d3_045'] = {'inputs': ['md_replacement_d2_045'], 'func': md_replacement_d3_045}


def md_replacement_d3_046(md_replacement_d2_046):
    feature = _clean(md_replacement_d2_046)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00023000).reindex(feature.index)
MD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['md_replacement_d3_046'] = {'inputs': ['md_replacement_d2_046'], 'func': md_replacement_d3_046}


def md_replacement_d3_047(md_replacement_d2_047):
    feature = _clean(md_replacement_d2_047)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00023500).reindex(feature.index)
MD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['md_replacement_d3_047'] = {'inputs': ['md_replacement_d2_047'], 'func': md_replacement_d3_047}


def md_replacement_d3_048(md_replacement_d2_048):
    feature = _clean(md_replacement_d2_048)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00024000).reindex(feature.index)
MD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['md_replacement_d3_048'] = {'inputs': ['md_replacement_d2_048'], 'func': md_replacement_d3_048}


def md_replacement_d3_049(md_replacement_d2_049):
    feature = _clean(md_replacement_d2_049)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00024500).reindex(feature.index)
MD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['md_replacement_d3_049'] = {'inputs': ['md_replacement_d2_049'], 'func': md_replacement_d3_049}


def md_replacement_d3_050(md_replacement_d2_050):
    feature = _clean(md_replacement_d2_050)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00025000).reindex(feature.index)
MD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['md_replacement_d3_050'] = {'inputs': ['md_replacement_d2_050'], 'func': md_replacement_d3_050}


def md_replacement_d3_051(md_replacement_d2_051):
    feature = _clean(md_replacement_d2_051)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00025500).reindex(feature.index)
MD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['md_replacement_d3_051'] = {'inputs': ['md_replacement_d2_051'], 'func': md_replacement_d3_051}


def md_replacement_d3_052(md_replacement_d2_052):
    feature = _clean(md_replacement_d2_052)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00026000).reindex(feature.index)
MD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['md_replacement_d3_052'] = {'inputs': ['md_replacement_d2_052'], 'func': md_replacement_d3_052}


def md_replacement_d3_053(md_replacement_d2_053):
    feature = _clean(md_replacement_d2_053)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00026500).reindex(feature.index)
MD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['md_replacement_d3_053'] = {'inputs': ['md_replacement_d2_053'], 'func': md_replacement_d3_053}


def md_replacement_d3_054(md_replacement_d2_054):
    feature = _clean(md_replacement_d2_054)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00027000).reindex(feature.index)
MD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['md_replacement_d3_054'] = {'inputs': ['md_replacement_d2_054'], 'func': md_replacement_d3_054}


def md_replacement_d3_055(md_replacement_d2_055):
    feature = _clean(md_replacement_d2_055)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00027500).reindex(feature.index)
MD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['md_replacement_d3_055'] = {'inputs': ['md_replacement_d2_055'], 'func': md_replacement_d3_055}


def md_replacement_d3_056(md_replacement_d2_056):
    feature = _clean(md_replacement_d2_056)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00028000).reindex(feature.index)
MD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['md_replacement_d3_056'] = {'inputs': ['md_replacement_d2_056'], 'func': md_replacement_d3_056}


def md_replacement_d3_057(md_replacement_d2_057):
    feature = _clean(md_replacement_d2_057)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00028500).reindex(feature.index)
MD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['md_replacement_d3_057'] = {'inputs': ['md_replacement_d2_057'], 'func': md_replacement_d3_057}


def md_replacement_d3_058(md_replacement_d2_058):
    feature = _clean(md_replacement_d2_058)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00029000).reindex(feature.index)
MD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['md_replacement_d3_058'] = {'inputs': ['md_replacement_d2_058'], 'func': md_replacement_d3_058}


def md_replacement_d3_059(md_replacement_d2_059):
    feature = _clean(md_replacement_d2_059)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00029500).reindex(feature.index)
MD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['md_replacement_d3_059'] = {'inputs': ['md_replacement_d2_059'], 'func': md_replacement_d3_059}


def md_replacement_d3_060(md_replacement_d2_060):
    feature = _clean(md_replacement_d2_060)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00030000).reindex(feature.index)
MD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['md_replacement_d3_060'] = {'inputs': ['md_replacement_d2_060'], 'func': md_replacement_d3_060}


def md_replacement_d3_061(md_replacement_d2_061):
    feature = _clean(md_replacement_d2_061)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00030500).reindex(feature.index)
MD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['md_replacement_d3_061'] = {'inputs': ['md_replacement_d2_061'], 'func': md_replacement_d3_061}


def md_replacement_d3_062(md_replacement_d2_062):
    feature = _clean(md_replacement_d2_062)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00031000).reindex(feature.index)
MD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['md_replacement_d3_062'] = {'inputs': ['md_replacement_d2_062'], 'func': md_replacement_d3_062}


def md_replacement_d3_063(md_replacement_d2_063):
    feature = _clean(md_replacement_d2_063)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00031500).reindex(feature.index)
MD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['md_replacement_d3_063'] = {'inputs': ['md_replacement_d2_063'], 'func': md_replacement_d3_063}


def md_replacement_d3_064(md_replacement_d2_064):
    feature = _clean(md_replacement_d2_064)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00032000).reindex(feature.index)
MD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['md_replacement_d3_064'] = {'inputs': ['md_replacement_d2_064'], 'func': md_replacement_d3_064}


def md_replacement_d3_065(md_replacement_d2_065):
    feature = _clean(md_replacement_d2_065)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00032500).reindex(feature.index)
MD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['md_replacement_d3_065'] = {'inputs': ['md_replacement_d2_065'], 'func': md_replacement_d3_065}


def md_replacement_d3_066(md_replacement_d2_066):
    feature = _clean(md_replacement_d2_066)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00033000).reindex(feature.index)
MD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['md_replacement_d3_066'] = {'inputs': ['md_replacement_d2_066'], 'func': md_replacement_d3_066}


def md_replacement_d3_067(md_replacement_d2_067):
    feature = _clean(md_replacement_d2_067)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00033500).reindex(feature.index)
MD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['md_replacement_d3_067'] = {'inputs': ['md_replacement_d2_067'], 'func': md_replacement_d3_067}


def md_replacement_d3_068(md_replacement_d2_068):
    feature = _clean(md_replacement_d2_068)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00034000).reindex(feature.index)
MD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['md_replacement_d3_068'] = {'inputs': ['md_replacement_d2_068'], 'func': md_replacement_d3_068}


def md_replacement_d3_069(md_replacement_d2_069):
    feature = _clean(md_replacement_d2_069)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00034500).reindex(feature.index)
MD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['md_replacement_d3_069'] = {'inputs': ['md_replacement_d2_069'], 'func': md_replacement_d3_069}


def md_replacement_d3_070(md_replacement_d2_070):
    feature = _clean(md_replacement_d2_070)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00035000).reindex(feature.index)
MD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['md_replacement_d3_070'] = {'inputs': ['md_replacement_d2_070'], 'func': md_replacement_d3_070}


def md_replacement_d3_071(md_replacement_d2_071):
    feature = _clean(md_replacement_d2_071)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00035500).reindex(feature.index)
MD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['md_replacement_d3_071'] = {'inputs': ['md_replacement_d2_071'], 'func': md_replacement_d3_071}


def md_replacement_d3_072(md_replacement_d2_072):
    feature = _clean(md_replacement_d2_072)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00036000).reindex(feature.index)
MD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['md_replacement_d3_072'] = {'inputs': ['md_replacement_d2_072'], 'func': md_replacement_d3_072}


def md_replacement_d3_073(md_replacement_d2_073):
    feature = _clean(md_replacement_d2_073)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00036500).reindex(feature.index)
MD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['md_replacement_d3_073'] = {'inputs': ['md_replacement_d2_073'], 'func': md_replacement_d3_073}


def md_replacement_d3_074(md_replacement_d2_074):
    feature = _clean(md_replacement_d2_074)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00037000).reindex(feature.index)
MD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['md_replacement_d3_074'] = {'inputs': ['md_replacement_d2_074'], 'func': md_replacement_d3_074}


def md_replacement_d3_075(md_replacement_d2_075):
    feature = _clean(md_replacement_d2_075)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00037500).reindex(feature.index)
MD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['md_replacement_d3_075'] = {'inputs': ['md_replacement_d2_075'], 'func': md_replacement_d3_075}


def md_replacement_d3_076(md_replacement_d2_076):
    feature = _clean(md_replacement_d2_076)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00038000).reindex(feature.index)
MD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['md_replacement_d3_076'] = {'inputs': ['md_replacement_d2_076'], 'func': md_replacement_d3_076}


def md_replacement_d3_077(md_replacement_d2_077):
    feature = _clean(md_replacement_d2_077)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00038500).reindex(feature.index)
MD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['md_replacement_d3_077'] = {'inputs': ['md_replacement_d2_077'], 'func': md_replacement_d3_077}


def md_replacement_d3_078(md_replacement_d2_078):
    feature = _clean(md_replacement_d2_078)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00039000).reindex(feature.index)
MD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['md_replacement_d3_078'] = {'inputs': ['md_replacement_d2_078'], 'func': md_replacement_d3_078}


def md_replacement_d3_079(md_replacement_d2_079):
    feature = _clean(md_replacement_d2_079)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00039500).reindex(feature.index)
MD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['md_replacement_d3_079'] = {'inputs': ['md_replacement_d2_079'], 'func': md_replacement_d3_079}


def md_replacement_d3_080(md_replacement_d2_080):
    feature = _clean(md_replacement_d2_080)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00040000).reindex(feature.index)
MD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['md_replacement_d3_080'] = {'inputs': ['md_replacement_d2_080'], 'func': md_replacement_d3_080}


def md_replacement_d3_081(md_replacement_d2_081):
    feature = _clean(md_replacement_d2_081)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00040500).reindex(feature.index)
MD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['md_replacement_d3_081'] = {'inputs': ['md_replacement_d2_081'], 'func': md_replacement_d3_081}


def md_replacement_d3_082(md_replacement_d2_082):
    feature = _clean(md_replacement_d2_082)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00041000).reindex(feature.index)
MD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['md_replacement_d3_082'] = {'inputs': ['md_replacement_d2_082'], 'func': md_replacement_d3_082}


def md_replacement_d3_083(md_replacement_d2_083):
    feature = _clean(md_replacement_d2_083)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00041500).reindex(feature.index)
MD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['md_replacement_d3_083'] = {'inputs': ['md_replacement_d2_083'], 'func': md_replacement_d3_083}


def md_replacement_d3_084(md_replacement_d2_084):
    feature = _clean(md_replacement_d2_084)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00042000).reindex(feature.index)
MD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['md_replacement_d3_084'] = {'inputs': ['md_replacement_d2_084'], 'func': md_replacement_d3_084}


def md_replacement_d3_085(md_replacement_d2_085):
    feature = _clean(md_replacement_d2_085)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00042500).reindex(feature.index)
MD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['md_replacement_d3_085'] = {'inputs': ['md_replacement_d2_085'], 'func': md_replacement_d3_085}


def md_replacement_d3_086(md_replacement_d2_086):
    feature = _clean(md_replacement_d2_086)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00043000).reindex(feature.index)
MD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['md_replacement_d3_086'] = {'inputs': ['md_replacement_d2_086'], 'func': md_replacement_d3_086}


def md_replacement_d3_087(md_replacement_d2_087):
    feature = _clean(md_replacement_d2_087)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00043500).reindex(feature.index)
MD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['md_replacement_d3_087'] = {'inputs': ['md_replacement_d2_087'], 'func': md_replacement_d3_087}


def md_replacement_d3_088(md_replacement_d2_088):
    feature = _clean(md_replacement_d2_088)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00044000).reindex(feature.index)
MD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['md_replacement_d3_088'] = {'inputs': ['md_replacement_d2_088'], 'func': md_replacement_d3_088}


def md_replacement_d3_089(md_replacement_d2_089):
    feature = _clean(md_replacement_d2_089)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00044500).reindex(feature.index)
MD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['md_replacement_d3_089'] = {'inputs': ['md_replacement_d2_089'], 'func': md_replacement_d3_089}


def md_replacement_d3_090(md_replacement_d2_090):
    feature = _clean(md_replacement_d2_090)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00045000).reindex(feature.index)
MD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['md_replacement_d3_090'] = {'inputs': ['md_replacement_d2_090'], 'func': md_replacement_d3_090}


def md_replacement_d3_091(md_replacement_d2_091):
    feature = _clean(md_replacement_d2_091)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00045500).reindex(feature.index)
MD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['md_replacement_d3_091'] = {'inputs': ['md_replacement_d2_091'], 'func': md_replacement_d3_091}


def md_replacement_d3_092(md_replacement_d2_092):
    feature = _clean(md_replacement_d2_092)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00046000).reindex(feature.index)
MD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['md_replacement_d3_092'] = {'inputs': ['md_replacement_d2_092'], 'func': md_replacement_d3_092}


def md_replacement_d3_093(md_replacement_d2_093):
    feature = _clean(md_replacement_d2_093)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00046500).reindex(feature.index)
MD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['md_replacement_d3_093'] = {'inputs': ['md_replacement_d2_093'], 'func': md_replacement_d3_093}


def md_replacement_d3_094(md_replacement_d2_094):
    feature = _clean(md_replacement_d2_094)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00047000).reindex(feature.index)
MD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['md_replacement_d3_094'] = {'inputs': ['md_replacement_d2_094'], 'func': md_replacement_d3_094}


def md_replacement_d3_095(md_replacement_d2_095):
    feature = _clean(md_replacement_d2_095)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00047500).reindex(feature.index)
MD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['md_replacement_d3_095'] = {'inputs': ['md_replacement_d2_095'], 'func': md_replacement_d3_095}


def md_replacement_d3_096(md_replacement_d2_096):
    feature = _clean(md_replacement_d2_096)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00048000).reindex(feature.index)
MD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['md_replacement_d3_096'] = {'inputs': ['md_replacement_d2_096'], 'func': md_replacement_d3_096}


def md_replacement_d3_097(md_replacement_d2_097):
    feature = _clean(md_replacement_d2_097)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00048500).reindex(feature.index)
MD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['md_replacement_d3_097'] = {'inputs': ['md_replacement_d2_097'], 'func': md_replacement_d3_097}


def md_replacement_d3_098(md_replacement_d2_098):
    feature = _clean(md_replacement_d2_098)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00049000).reindex(feature.index)
MD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['md_replacement_d3_098'] = {'inputs': ['md_replacement_d2_098'], 'func': md_replacement_d3_098}


def md_replacement_d3_099(md_replacement_d2_099):
    feature = _clean(md_replacement_d2_099)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00049500).reindex(feature.index)
MD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['md_replacement_d3_099'] = {'inputs': ['md_replacement_d2_099'], 'func': md_replacement_d3_099}


def md_replacement_d3_100(md_replacement_d2_100):
    feature = _clean(md_replacement_d2_100)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00050000).reindex(feature.index)
MD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['md_replacement_d3_100'] = {'inputs': ['md_replacement_d2_100'], 'func': md_replacement_d3_100}


def md_replacement_d3_101(md_replacement_d2_101):
    feature = _clean(md_replacement_d2_101)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00050500).reindex(feature.index)
MD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['md_replacement_d3_101'] = {'inputs': ['md_replacement_d2_101'], 'func': md_replacement_d3_101}


def md_replacement_d3_102(md_replacement_d2_102):
    feature = _clean(md_replacement_d2_102)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00051000).reindex(feature.index)
MD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['md_replacement_d3_102'] = {'inputs': ['md_replacement_d2_102'], 'func': md_replacement_d3_102}


def md_replacement_d3_103(md_replacement_d2_103):
    feature = _clean(md_replacement_d2_103)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00051500).reindex(feature.index)
MD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['md_replacement_d3_103'] = {'inputs': ['md_replacement_d2_103'], 'func': md_replacement_d3_103}


def md_replacement_d3_104(md_replacement_d2_104):
    feature = _clean(md_replacement_d2_104)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00052000).reindex(feature.index)
MD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['md_replacement_d3_104'] = {'inputs': ['md_replacement_d2_104'], 'func': md_replacement_d3_104}


def md_replacement_d3_105(md_replacement_d2_105):
    feature = _clean(md_replacement_d2_105)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00052500).reindex(feature.index)
MD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['md_replacement_d3_105'] = {'inputs': ['md_replacement_d2_105'], 'func': md_replacement_d3_105}


def md_replacement_d3_106(md_replacement_d2_106):
    feature = _clean(md_replacement_d2_106)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00053000).reindex(feature.index)
MD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['md_replacement_d3_106'] = {'inputs': ['md_replacement_d2_106'], 'func': md_replacement_d3_106}


def md_replacement_d3_107(md_replacement_d2_107):
    feature = _clean(md_replacement_d2_107)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00053500).reindex(feature.index)
MD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['md_replacement_d3_107'] = {'inputs': ['md_replacement_d2_107'], 'func': md_replacement_d3_107}


def md_replacement_d3_108(md_replacement_d2_108):
    feature = _clean(md_replacement_d2_108)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00054000).reindex(feature.index)
MD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['md_replacement_d3_108'] = {'inputs': ['md_replacement_d2_108'], 'func': md_replacement_d3_108}


def md_replacement_d3_109(md_replacement_d2_109):
    feature = _clean(md_replacement_d2_109)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00054500).reindex(feature.index)
MD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['md_replacement_d3_109'] = {'inputs': ['md_replacement_d2_109'], 'func': md_replacement_d3_109}


def md_replacement_d3_110(md_replacement_d2_110):
    feature = _clean(md_replacement_d2_110)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00055000).reindex(feature.index)
MD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['md_replacement_d3_110'] = {'inputs': ['md_replacement_d2_110'], 'func': md_replacement_d3_110}


def md_replacement_d3_111(md_replacement_d2_111):
    feature = _clean(md_replacement_d2_111)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00055500).reindex(feature.index)
MD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['md_replacement_d3_111'] = {'inputs': ['md_replacement_d2_111'], 'func': md_replacement_d3_111}


def md_replacement_d3_112(md_replacement_d2_112):
    feature = _clean(md_replacement_d2_112)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00056000).reindex(feature.index)
MD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['md_replacement_d3_112'] = {'inputs': ['md_replacement_d2_112'], 'func': md_replacement_d3_112}


def md_replacement_d3_113(md_replacement_d2_113):
    feature = _clean(md_replacement_d2_113)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00056500).reindex(feature.index)
MD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['md_replacement_d3_113'] = {'inputs': ['md_replacement_d2_113'], 'func': md_replacement_d3_113}


def md_replacement_d3_114(md_replacement_d2_114):
    feature = _clean(md_replacement_d2_114)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00057000).reindex(feature.index)
MD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['md_replacement_d3_114'] = {'inputs': ['md_replacement_d2_114'], 'func': md_replacement_d3_114}


def md_replacement_d3_115(md_replacement_d2_115):
    feature = _clean(md_replacement_d2_115)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00057500).reindex(feature.index)
MD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['md_replacement_d3_115'] = {'inputs': ['md_replacement_d2_115'], 'func': md_replacement_d3_115}


def md_replacement_d3_116(md_replacement_d2_116):
    feature = _clean(md_replacement_d2_116)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00058000).reindex(feature.index)
MD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['md_replacement_d3_116'] = {'inputs': ['md_replacement_d2_116'], 'func': md_replacement_d3_116}


def md_replacement_d3_117(md_replacement_d2_117):
    feature = _clean(md_replacement_d2_117)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00058500).reindex(feature.index)
MD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['md_replacement_d3_117'] = {'inputs': ['md_replacement_d2_117'], 'func': md_replacement_d3_117}


def md_replacement_d3_118(md_replacement_d2_118):
    feature = _clean(md_replacement_d2_118)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00059000).reindex(feature.index)
MD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['md_replacement_d3_118'] = {'inputs': ['md_replacement_d2_118'], 'func': md_replacement_d3_118}


def md_replacement_d3_119(md_replacement_d2_119):
    feature = _clean(md_replacement_d2_119)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00059500).reindex(feature.index)
MD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['md_replacement_d3_119'] = {'inputs': ['md_replacement_d2_119'], 'func': md_replacement_d3_119}


def md_replacement_d3_120(md_replacement_d2_120):
    feature = _clean(md_replacement_d2_120)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00060000).reindex(feature.index)
MD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['md_replacement_d3_120'] = {'inputs': ['md_replacement_d2_120'], 'func': md_replacement_d3_120}


def md_replacement_d3_121(md_replacement_d2_121):
    feature = _clean(md_replacement_d2_121)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00060500).reindex(feature.index)
MD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['md_replacement_d3_121'] = {'inputs': ['md_replacement_d2_121'], 'func': md_replacement_d3_121}


def md_replacement_d3_122(md_replacement_d2_122):
    feature = _clean(md_replacement_d2_122)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00061000).reindex(feature.index)
MD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['md_replacement_d3_122'] = {'inputs': ['md_replacement_d2_122'], 'func': md_replacement_d3_122}


def md_replacement_d3_123(md_replacement_d2_123):
    feature = _clean(md_replacement_d2_123)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00061500).reindex(feature.index)
MD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['md_replacement_d3_123'] = {'inputs': ['md_replacement_d2_123'], 'func': md_replacement_d3_123}


def md_replacement_d3_124(md_replacement_d2_124):
    feature = _clean(md_replacement_d2_124)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00062000).reindex(feature.index)
MD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['md_replacement_d3_124'] = {'inputs': ['md_replacement_d2_124'], 'func': md_replacement_d3_124}


def md_replacement_d3_125(md_replacement_d2_125):
    feature = _clean(md_replacement_d2_125)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00062500).reindex(feature.index)
MD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['md_replacement_d3_125'] = {'inputs': ['md_replacement_d2_125'], 'func': md_replacement_d3_125}


def md_replacement_d3_126(md_replacement_d2_126):
    feature = _clean(md_replacement_d2_126)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00063000).reindex(feature.index)
MD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['md_replacement_d3_126'] = {'inputs': ['md_replacement_d2_126'], 'func': md_replacement_d3_126}


def md_replacement_d3_127(md_replacement_d2_127):
    feature = _clean(md_replacement_d2_127)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00063500).reindex(feature.index)
MD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['md_replacement_d3_127'] = {'inputs': ['md_replacement_d2_127'], 'func': md_replacement_d3_127}


def md_replacement_d3_128(md_replacement_d2_128):
    feature = _clean(md_replacement_d2_128)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00064000).reindex(feature.index)
MD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['md_replacement_d3_128'] = {'inputs': ['md_replacement_d2_128'], 'func': md_replacement_d3_128}


def md_replacement_d3_129(md_replacement_d2_129):
    feature = _clean(md_replacement_d2_129)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00064500).reindex(feature.index)
MD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['md_replacement_d3_129'] = {'inputs': ['md_replacement_d2_129'], 'func': md_replacement_d3_129}


def md_replacement_d3_130(md_replacement_d2_130):
    feature = _clean(md_replacement_d2_130)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00065000).reindex(feature.index)
MD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['md_replacement_d3_130'] = {'inputs': ['md_replacement_d2_130'], 'func': md_replacement_d3_130}


def md_replacement_d3_131(md_replacement_d2_131):
    feature = _clean(md_replacement_d2_131)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00065500).reindex(feature.index)
MD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['md_replacement_d3_131'] = {'inputs': ['md_replacement_d2_131'], 'func': md_replacement_d3_131}


def md_replacement_d3_132(md_replacement_d2_132):
    feature = _clean(md_replacement_d2_132)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00066000).reindex(feature.index)
MD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['md_replacement_d3_132'] = {'inputs': ['md_replacement_d2_132'], 'func': md_replacement_d3_132}


def md_replacement_d3_133(md_replacement_d2_133):
    feature = _clean(md_replacement_d2_133)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00066500).reindex(feature.index)
MD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['md_replacement_d3_133'] = {'inputs': ['md_replacement_d2_133'], 'func': md_replacement_d3_133}


def md_replacement_d3_134(md_replacement_d2_134):
    feature = _clean(md_replacement_d2_134)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00067000).reindex(feature.index)
MD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['md_replacement_d3_134'] = {'inputs': ['md_replacement_d2_134'], 'func': md_replacement_d3_134}


def md_replacement_d3_135(md_replacement_d2_135):
    feature = _clean(md_replacement_d2_135)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00067500).reindex(feature.index)
MD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['md_replacement_d3_135'] = {'inputs': ['md_replacement_d2_135'], 'func': md_replacement_d3_135}


def md_replacement_d3_136(md_replacement_d2_136):
    feature = _clean(md_replacement_d2_136)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00068000).reindex(feature.index)
MD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['md_replacement_d3_136'] = {'inputs': ['md_replacement_d2_136'], 'func': md_replacement_d3_136}


def md_replacement_d3_137(md_replacement_d2_137):
    feature = _clean(md_replacement_d2_137)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00068500).reindex(feature.index)
MD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['md_replacement_d3_137'] = {'inputs': ['md_replacement_d2_137'], 'func': md_replacement_d3_137}


def md_replacement_d3_138(md_replacement_d2_138):
    feature = _clean(md_replacement_d2_138)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00069000).reindex(feature.index)
MD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['md_replacement_d3_138'] = {'inputs': ['md_replacement_d2_138'], 'func': md_replacement_d3_138}


def md_replacement_d3_139(md_replacement_d2_139):
    feature = _clean(md_replacement_d2_139)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00069500).reindex(feature.index)
MD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['md_replacement_d3_139'] = {'inputs': ['md_replacement_d2_139'], 'func': md_replacement_d3_139}


def md_replacement_d3_140(md_replacement_d2_140):
    feature = _clean(md_replacement_d2_140)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00070000).reindex(feature.index)
MD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['md_replacement_d3_140'] = {'inputs': ['md_replacement_d2_140'], 'func': md_replacement_d3_140}


def md_replacement_d3_141(md_replacement_d2_141):
    feature = _clean(md_replacement_d2_141)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00070500).reindex(feature.index)
MD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['md_replacement_d3_141'] = {'inputs': ['md_replacement_d2_141'], 'func': md_replacement_d3_141}


def md_replacement_d3_142(md_replacement_d2_142):
    feature = _clean(md_replacement_d2_142)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00071000).reindex(feature.index)
MD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['md_replacement_d3_142'] = {'inputs': ['md_replacement_d2_142'], 'func': md_replacement_d3_142}


def md_replacement_d3_143(md_replacement_d2_143):
    feature = _clean(md_replacement_d2_143)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00071500).reindex(feature.index)
MD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['md_replacement_d3_143'] = {'inputs': ['md_replacement_d2_143'], 'func': md_replacement_d3_143}


def md_replacement_d3_144(md_replacement_d2_144):
    feature = _clean(md_replacement_d2_144)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00072000).reindex(feature.index)
MD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['md_replacement_d3_144'] = {'inputs': ['md_replacement_d2_144'], 'func': md_replacement_d3_144}


def md_replacement_d3_145(md_replacement_d2_145):
    feature = _clean(md_replacement_d2_145)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00072500).reindex(feature.index)
MD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['md_replacement_d3_145'] = {'inputs': ['md_replacement_d2_145'], 'func': md_replacement_d3_145}


def md_replacement_d3_146(md_replacement_d2_146):
    feature = _clean(md_replacement_d2_146)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00073000).reindex(feature.index)
MD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['md_replacement_d3_146'] = {'inputs': ['md_replacement_d2_146'], 'func': md_replacement_d3_146}


def md_replacement_d3_147(md_replacement_d2_147):
    feature = _clean(md_replacement_d2_147)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00073500).reindex(feature.index)
MD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['md_replacement_d3_147'] = {'inputs': ['md_replacement_d2_147'], 'func': md_replacement_d3_147}


def md_replacement_d3_148(md_replacement_d2_148):
    feature = _clean(md_replacement_d2_148)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00074000).reindex(feature.index)
MD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['md_replacement_d3_148'] = {'inputs': ['md_replacement_d2_148'], 'func': md_replacement_d3_148}


def md_replacement_d3_149(md_replacement_d2_149):
    feature = _clean(md_replacement_d2_149)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00074500).reindex(feature.index)
MD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['md_replacement_d3_149'] = {'inputs': ['md_replacement_d2_149'], 'func': md_replacement_d3_149}


def md_replacement_d3_150(md_replacement_d2_150):
    feature = _clean(md_replacement_d2_150)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00075000).reindex(feature.index)
MD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['md_replacement_d3_150'] = {'inputs': ['md_replacement_d2_150'], 'func': md_replacement_d3_150}


def md_replacement_d3_151(md_replacement_d2_151):
    feature = _clean(md_replacement_d2_151)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00075500).reindex(feature.index)
MD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['md_replacement_d3_151'] = {'inputs': ['md_replacement_d2_151'], 'func': md_replacement_d3_151}


def md_replacement_d3_152(md_replacement_d2_152):
    feature = _clean(md_replacement_d2_152)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00076000).reindex(feature.index)
MD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['md_replacement_d3_152'] = {'inputs': ['md_replacement_d2_152'], 'func': md_replacement_d3_152}


def md_replacement_d3_153(md_replacement_d2_153):
    feature = _clean(md_replacement_d2_153)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00076500).reindex(feature.index)
MD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['md_replacement_d3_153'] = {'inputs': ['md_replacement_d2_153'], 'func': md_replacement_d3_153}


def md_replacement_d3_154(md_replacement_d2_154):
    feature = _clean(md_replacement_d2_154)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00077000).reindex(feature.index)
MD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['md_replacement_d3_154'] = {'inputs': ['md_replacement_d2_154'], 'func': md_replacement_d3_154}


def md_replacement_d3_155(md_replacement_d2_155):
    feature = _clean(md_replacement_d2_155)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00077500).reindex(feature.index)
MD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['md_replacement_d3_155'] = {'inputs': ['md_replacement_d2_155'], 'func': md_replacement_d3_155}


def md_replacement_d3_156(md_replacement_d2_156):
    feature = _clean(md_replacement_d2_156)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00078000).reindex(feature.index)
MD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['md_replacement_d3_156'] = {'inputs': ['md_replacement_d2_156'], 'func': md_replacement_d3_156}


def md_replacement_d3_157(md_replacement_d2_157):
    feature = _clean(md_replacement_d2_157)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00078500).reindex(feature.index)
MD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['md_replacement_d3_157'] = {'inputs': ['md_replacement_d2_157'], 'func': md_replacement_d3_157}


def md_replacement_d3_158(md_replacement_d2_158):
    feature = _clean(md_replacement_d2_158)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00079000).reindex(feature.index)
MD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['md_replacement_d3_158'] = {'inputs': ['md_replacement_d2_158'], 'func': md_replacement_d3_158}


def md_replacement_d3_159(md_replacement_d2_159):
    feature = _clean(md_replacement_d2_159)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00079500).reindex(feature.index)
MD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['md_replacement_d3_159'] = {'inputs': ['md_replacement_d2_159'], 'func': md_replacement_d3_159}


def md_replacement_d3_160(md_replacement_d2_160):
    feature = _clean(md_replacement_d2_160)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00080000).reindex(feature.index)
MD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['md_replacement_d3_160'] = {'inputs': ['md_replacement_d2_160'], 'func': md_replacement_d3_160}


def md_replacement_d3_161(md_replacement_d2_161):
    feature = _clean(md_replacement_d2_161)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00080500).reindex(feature.index)
MD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['md_replacement_d3_161'] = {'inputs': ['md_replacement_d2_161'], 'func': md_replacement_d3_161}


def md_replacement_d3_162(md_replacement_d2_162):
    feature = _clean(md_replacement_d2_162)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00081000).reindex(feature.index)
MD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['md_replacement_d3_162'] = {'inputs': ['md_replacement_d2_162'], 'func': md_replacement_d3_162}


def md_replacement_d3_163(md_replacement_d2_163):
    feature = _clean(md_replacement_d2_163)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00081500).reindex(feature.index)
MD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['md_replacement_d3_163'] = {'inputs': ['md_replacement_d2_163'], 'func': md_replacement_d3_163}


def md_replacement_d3_164(md_replacement_d2_164):
    feature = _clean(md_replacement_d2_164)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00082000).reindex(feature.index)
MD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['md_replacement_d3_164'] = {'inputs': ['md_replacement_d2_164'], 'func': md_replacement_d3_164}


def md_replacement_d3_165(md_replacement_d2_165):
    feature = _clean(md_replacement_d2_165)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00082500).reindex(feature.index)
MD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['md_replacement_d3_165'] = {'inputs': ['md_replacement_d2_165'], 'func': md_replacement_d3_165}


def md_replacement_d3_166(md_replacement_d2_166):
    feature = _clean(md_replacement_d2_166)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00083000).reindex(feature.index)
MD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['md_replacement_d3_166'] = {'inputs': ['md_replacement_d2_166'], 'func': md_replacement_d3_166}


def md_replacement_d3_167(md_replacement_d2_167):
    feature = _clean(md_replacement_d2_167)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00083500).reindex(feature.index)
MD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['md_replacement_d3_167'] = {'inputs': ['md_replacement_d2_167'], 'func': md_replacement_d3_167}


def md_replacement_d3_168(md_replacement_d2_168):
    feature = _clean(md_replacement_d2_168)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00084000).reindex(feature.index)
MD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['md_replacement_d3_168'] = {'inputs': ['md_replacement_d2_168'], 'func': md_replacement_d3_168}


def md_replacement_d3_169(md_replacement_d2_169):
    feature = _clean(md_replacement_d2_169)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00084500).reindex(feature.index)
MD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['md_replacement_d3_169'] = {'inputs': ['md_replacement_d2_169'], 'func': md_replacement_d3_169}


def md_replacement_d3_170(md_replacement_d2_170):
    feature = _clean(md_replacement_d2_170)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00085000).reindex(feature.index)
MD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['md_replacement_d3_170'] = {'inputs': ['md_replacement_d2_170'], 'func': md_replacement_d3_170}


def md_replacement_d3_171(md_replacement_d2_171):
    feature = _clean(md_replacement_d2_171)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00085500).reindex(feature.index)
MD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['md_replacement_d3_171'] = {'inputs': ['md_replacement_d2_171'], 'func': md_replacement_d3_171}


def md_replacement_d3_172(md_replacement_d2_172):
    feature = _clean(md_replacement_d2_172)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00086000).reindex(feature.index)
MD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['md_replacement_d3_172'] = {'inputs': ['md_replacement_d2_172'], 'func': md_replacement_d3_172}


def md_replacement_d3_173(md_replacement_d2_173):
    feature = _clean(md_replacement_d2_173)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00086500).reindex(feature.index)
MD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['md_replacement_d3_173'] = {'inputs': ['md_replacement_d2_173'], 'func': md_replacement_d3_173}


def md_replacement_d3_174(md_replacement_d2_174):
    feature = _clean(md_replacement_d2_174)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00087000).reindex(feature.index)
MD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['md_replacement_d3_174'] = {'inputs': ['md_replacement_d2_174'], 'func': md_replacement_d3_174}


def md_replacement_d3_175(md_replacement_d2_175):
    feature = _clean(md_replacement_d2_175)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00087500).reindex(feature.index)
MD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['md_replacement_d3_175'] = {'inputs': ['md_replacement_d2_175'], 'func': md_replacement_d3_175}


# Third-derivative extensions for repaired first-base features.
MDC_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY = {}


def _base_universe_d3(feature, idx):
    feature = _clean(feature) if '_clean' in globals() else _s(feature).replace([np.inf, -np.inf], np.nan)
    windows = [1, 2, 3, 5, 8, 13, 21, 34, 55]
    lag = windows[(idx * 2) % len(windows)]
    smooth = windows[(idx * 5 + 2) % len(windows)]
    accel = feature.diff(lag)
    curve = feature - feature.rolling(max(3, smooth), min_periods=2).mean()
    out = accel + curve.fillna(0.0) * (0.00019 * ((idx % 19) + 1))
    return out.replace([np.inf, -np.inf], np.nan).reindex(feature.index)


def mdc_base_universe_d3_001_mdc_003_loss_streak_21_003(mdc_base_universe_d2_001_mdc_003_loss_streak_21_003):
    return _base_universe_d3(mdc_base_universe_d2_001_mdc_003_loss_streak_21_003, 1)
MDC_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['mdc_base_universe_d3_001_mdc_003_loss_streak_21_003'] = {'inputs': ['mdc_base_universe_d2_001_mdc_003_loss_streak_21_003'], 'func': mdc_base_universe_d3_001_mdc_003_loss_streak_21_003}


def mdc_base_universe_d3_002_mdc_004_ma_distance_42_004(mdc_base_universe_d2_002_mdc_004_ma_distance_42_004):
    return _base_universe_d3(mdc_base_universe_d2_002_mdc_004_ma_distance_42_004, 2)
MDC_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['mdc_base_universe_d3_002_mdc_004_ma_distance_42_004'] = {'inputs': ['mdc_base_universe_d2_002_mdc_004_ma_distance_42_004'], 'func': mdc_base_universe_d3_002_mdc_004_ma_distance_42_004}


def mdc_base_universe_d3_003_mdc_005_stochastic_position_63_005(mdc_base_universe_d2_003_mdc_005_stochastic_position_63_005):
    return _base_universe_d3(mdc_base_universe_d2_003_mdc_005_stochastic_position_63_005, 3)
MDC_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['mdc_base_universe_d3_003_mdc_005_stochastic_position_63_005'] = {'inputs': ['mdc_base_universe_d2_003_mdc_005_stochastic_position_63_005'], 'func': mdc_base_universe_d3_003_mdc_005_stochastic_position_63_005}


def mdc_base_universe_d3_004_mdc_009_loss_streak_252_009(mdc_base_universe_d2_004_mdc_009_loss_streak_252_009):
    return _base_universe_d3(mdc_base_universe_d2_004_mdc_009_loss_streak_252_009, 4)
MDC_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['mdc_base_universe_d3_004_mdc_009_loss_streak_252_009'] = {'inputs': ['mdc_base_universe_d2_004_mdc_009_loss_streak_252_009'], 'func': mdc_base_universe_d3_004_mdc_009_loss_streak_252_009}


def mdc_base_universe_d3_005_mdc_010_ma_distance_378_010(mdc_base_universe_d2_005_mdc_010_ma_distance_378_010):
    return _base_universe_d3(mdc_base_universe_d2_005_mdc_010_ma_distance_378_010, 5)
MDC_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['mdc_base_universe_d3_005_mdc_010_ma_distance_378_010'] = {'inputs': ['mdc_base_universe_d2_005_mdc_010_ma_distance_378_010'], 'func': mdc_base_universe_d3_005_mdc_010_ma_distance_378_010}


def mdc_base_universe_d3_006_mdc_011_stochastic_position_504_011(mdc_base_universe_d2_006_mdc_011_stochastic_position_504_011):
    return _base_universe_d3(mdc_base_universe_d2_006_mdc_011_stochastic_position_504_011, 6)
MDC_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['mdc_base_universe_d3_006_mdc_011_stochastic_position_504_011'] = {'inputs': ['mdc_base_universe_d2_006_mdc_011_stochastic_position_504_011'], 'func': mdc_base_universe_d3_006_mdc_011_stochastic_position_504_011}


def mdc_base_universe_d3_007_mdc_015_loss_streak_1512_015(mdc_base_universe_d2_007_mdc_015_loss_streak_1512_015):
    return _base_universe_d3(mdc_base_universe_d2_007_mdc_015_loss_streak_1512_015, 7)
MDC_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['mdc_base_universe_d3_007_mdc_015_loss_streak_1512_015'] = {'inputs': ['mdc_base_universe_d2_007_mdc_015_loss_streak_1512_015'], 'func': mdc_base_universe_d3_007_mdc_015_loss_streak_1512_015}


def mdc_base_universe_d3_008_mdc_016_ma_distance_5_016(mdc_base_universe_d2_008_mdc_016_ma_distance_5_016):
    return _base_universe_d3(mdc_base_universe_d2_008_mdc_016_ma_distance_5_016, 8)
MDC_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['mdc_base_universe_d3_008_mdc_016_ma_distance_5_016'] = {'inputs': ['mdc_base_universe_d2_008_mdc_016_ma_distance_5_016'], 'func': mdc_base_universe_d3_008_mdc_016_ma_distance_5_016}


def mdc_base_universe_d3_009_mdc_017_stochastic_position_10_017(mdc_base_universe_d2_009_mdc_017_stochastic_position_10_017):
    return _base_universe_d3(mdc_base_universe_d2_009_mdc_017_stochastic_position_10_017, 9)
MDC_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['mdc_base_universe_d3_009_mdc_017_stochastic_position_10_017'] = {'inputs': ['mdc_base_universe_d2_009_mdc_017_stochastic_position_10_017'], 'func': mdc_base_universe_d3_009_mdc_017_stochastic_position_10_017}


def mdc_base_universe_d3_010_mdc_021_loss_streak_84_021(mdc_base_universe_d2_010_mdc_021_loss_streak_84_021):
    return _base_universe_d3(mdc_base_universe_d2_010_mdc_021_loss_streak_84_021, 10)
MDC_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['mdc_base_universe_d3_010_mdc_021_loss_streak_84_021'] = {'inputs': ['mdc_base_universe_d2_010_mdc_021_loss_streak_84_021'], 'func': mdc_base_universe_d3_010_mdc_021_loss_streak_84_021}


def mdc_base_universe_d3_011_mdc_022_ma_distance_126_022(mdc_base_universe_d2_011_mdc_022_ma_distance_126_022):
    return _base_universe_d3(mdc_base_universe_d2_011_mdc_022_ma_distance_126_022, 11)
MDC_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['mdc_base_universe_d3_011_mdc_022_ma_distance_126_022'] = {'inputs': ['mdc_base_universe_d2_011_mdc_022_ma_distance_126_022'], 'func': mdc_base_universe_d3_011_mdc_022_ma_distance_126_022}


def mdc_base_universe_d3_012_mdc_023_stochastic_position_189_023(mdc_base_universe_d2_012_mdc_023_stochastic_position_189_023):
    return _base_universe_d3(mdc_base_universe_d2_012_mdc_023_stochastic_position_189_023, 12)
MDC_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['mdc_base_universe_d3_012_mdc_023_stochastic_position_189_023'] = {'inputs': ['mdc_base_universe_d2_012_mdc_023_stochastic_position_189_023'], 'func': mdc_base_universe_d3_012_mdc_023_stochastic_position_189_023}


def mdc_base_universe_d3_013_mdc_027_loss_streak_756_027(mdc_base_universe_d2_013_mdc_027_loss_streak_756_027):
    return _base_universe_d3(mdc_base_universe_d2_013_mdc_027_loss_streak_756_027, 13)
MDC_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['mdc_base_universe_d3_013_mdc_027_loss_streak_756_027'] = {'inputs': ['mdc_base_universe_d2_013_mdc_027_loss_streak_756_027'], 'func': mdc_base_universe_d3_013_mdc_027_loss_streak_756_027}


def mdc_base_universe_d3_014_mdc_028_ma_distance_1008_028(mdc_base_universe_d2_014_mdc_028_ma_distance_1008_028):
    return _base_universe_d3(mdc_base_universe_d2_014_mdc_028_ma_distance_1008_028, 14)
MDC_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['mdc_base_universe_d3_014_mdc_028_ma_distance_1008_028'] = {'inputs': ['mdc_base_universe_d2_014_mdc_028_ma_distance_1008_028'], 'func': mdc_base_universe_d3_014_mdc_028_ma_distance_1008_028}


def mdc_base_universe_d3_015_mdc_029_stochastic_position_1260_029(mdc_base_universe_d2_015_mdc_029_stochastic_position_1260_029):
    return _base_universe_d3(mdc_base_universe_d2_015_mdc_029_stochastic_position_1260_029, 15)
MDC_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['mdc_base_universe_d3_015_mdc_029_stochastic_position_1260_029'] = {'inputs': ['mdc_base_universe_d2_015_mdc_029_stochastic_position_1260_029'], 'func': mdc_base_universe_d3_015_mdc_029_stochastic_position_1260_029}


def mdc_base_universe_d3_016_mdc_basefill_001(mdc_base_universe_d2_016_mdc_basefill_001):
    return _base_universe_d3(mdc_base_universe_d2_016_mdc_basefill_001, 16)
MDC_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['mdc_base_universe_d3_016_mdc_basefill_001'] = {'inputs': ['mdc_base_universe_d2_016_mdc_basefill_001'], 'func': mdc_base_universe_d3_016_mdc_basefill_001}


def mdc_base_universe_d3_017_mdc_basefill_002(mdc_base_universe_d2_017_mdc_basefill_002):
    return _base_universe_d3(mdc_base_universe_d2_017_mdc_basefill_002, 17)
MDC_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['mdc_base_universe_d3_017_mdc_basefill_002'] = {'inputs': ['mdc_base_universe_d2_017_mdc_basefill_002'], 'func': mdc_base_universe_d3_017_mdc_basefill_002}


def mdc_base_universe_d3_018_mdc_basefill_006(mdc_base_universe_d2_018_mdc_basefill_006):
    return _base_universe_d3(mdc_base_universe_d2_018_mdc_basefill_006, 18)
MDC_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['mdc_base_universe_d3_018_mdc_basefill_006'] = {'inputs': ['mdc_base_universe_d2_018_mdc_basefill_006'], 'func': mdc_base_universe_d3_018_mdc_basefill_006}


def mdc_base_universe_d3_019_mdc_basefill_007(mdc_base_universe_d2_019_mdc_basefill_007):
    return _base_universe_d3(mdc_base_universe_d2_019_mdc_basefill_007, 19)
MDC_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['mdc_base_universe_d3_019_mdc_basefill_007'] = {'inputs': ['mdc_base_universe_d2_019_mdc_basefill_007'], 'func': mdc_base_universe_d3_019_mdc_basefill_007}


def mdc_base_universe_d3_020_mdc_basefill_008(mdc_base_universe_d2_020_mdc_basefill_008):
    return _base_universe_d3(mdc_base_universe_d2_020_mdc_basefill_008, 20)
MDC_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['mdc_base_universe_d3_020_mdc_basefill_008'] = {'inputs': ['mdc_base_universe_d2_020_mdc_basefill_008'], 'func': mdc_base_universe_d3_020_mdc_basefill_008}


def mdc_base_universe_d3_021_mdc_basefill_012(mdc_base_universe_d2_021_mdc_basefill_012):
    return _base_universe_d3(mdc_base_universe_d2_021_mdc_basefill_012, 21)
MDC_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['mdc_base_universe_d3_021_mdc_basefill_012'] = {'inputs': ['mdc_base_universe_d2_021_mdc_basefill_012'], 'func': mdc_base_universe_d3_021_mdc_basefill_012}


def mdc_base_universe_d3_022_mdc_basefill_013(mdc_base_universe_d2_022_mdc_basefill_013):
    return _base_universe_d3(mdc_base_universe_d2_022_mdc_basefill_013, 22)
MDC_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['mdc_base_universe_d3_022_mdc_basefill_013'] = {'inputs': ['mdc_base_universe_d2_022_mdc_basefill_013'], 'func': mdc_base_universe_d3_022_mdc_basefill_013}


def mdc_base_universe_d3_023_mdc_basefill_014(mdc_base_universe_d2_023_mdc_basefill_014):
    return _base_universe_d3(mdc_base_universe_d2_023_mdc_basefill_014, 23)
MDC_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['mdc_base_universe_d3_023_mdc_basefill_014'] = {'inputs': ['mdc_base_universe_d2_023_mdc_basefill_014'], 'func': mdc_base_universe_d3_023_mdc_basefill_014}


def mdc_base_universe_d3_024_mdc_basefill_018(mdc_base_universe_d2_024_mdc_basefill_018):
    return _base_universe_d3(mdc_base_universe_d2_024_mdc_basefill_018, 24)
MDC_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['mdc_base_universe_d3_024_mdc_basefill_018'] = {'inputs': ['mdc_base_universe_d2_024_mdc_basefill_018'], 'func': mdc_base_universe_d3_024_mdc_basefill_018}


def mdc_base_universe_d3_025_mdc_basefill_019(mdc_base_universe_d2_025_mdc_basefill_019):
    return _base_universe_d3(mdc_base_universe_d2_025_mdc_basefill_019, 25)
MDC_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['mdc_base_universe_d3_025_mdc_basefill_019'] = {'inputs': ['mdc_base_universe_d2_025_mdc_basefill_019'], 'func': mdc_base_universe_d3_025_mdc_basefill_019}


def mdc_base_universe_d3_026_mdc_basefill_020(mdc_base_universe_d2_026_mdc_basefill_020):
    return _base_universe_d3(mdc_base_universe_d2_026_mdc_basefill_020, 26)
MDC_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['mdc_base_universe_d3_026_mdc_basefill_020'] = {'inputs': ['mdc_base_universe_d2_026_mdc_basefill_020'], 'func': mdc_base_universe_d3_026_mdc_basefill_020}


def mdc_base_universe_d3_027_mdc_basefill_024(mdc_base_universe_d2_027_mdc_basefill_024):
    return _base_universe_d3(mdc_base_universe_d2_027_mdc_basefill_024, 27)
MDC_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['mdc_base_universe_d3_027_mdc_basefill_024'] = {'inputs': ['mdc_base_universe_d2_027_mdc_basefill_024'], 'func': mdc_base_universe_d3_027_mdc_basefill_024}


def mdc_base_universe_d3_028_mdc_basefill_025(mdc_base_universe_d2_028_mdc_basefill_025):
    return _base_universe_d3(mdc_base_universe_d2_028_mdc_basefill_025, 28)
MDC_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['mdc_base_universe_d3_028_mdc_basefill_025'] = {'inputs': ['mdc_base_universe_d2_028_mdc_basefill_025'], 'func': mdc_base_universe_d3_028_mdc_basefill_025}


def mdc_base_universe_d3_029_mdc_basefill_026(mdc_base_universe_d2_029_mdc_basefill_026):
    return _base_universe_d3(mdc_base_universe_d2_029_mdc_basefill_026, 29)
MDC_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['mdc_base_universe_d3_029_mdc_basefill_026'] = {'inputs': ['mdc_base_universe_d2_029_mdc_basefill_026'], 'func': mdc_base_universe_d3_029_mdc_basefill_026}


def mdc_base_universe_d3_030_mdc_basefill_030(mdc_base_universe_d2_030_mdc_basefill_030):
    return _base_universe_d3(mdc_base_universe_d2_030_mdc_basefill_030, 30)
MDC_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['mdc_base_universe_d3_030_mdc_basefill_030'] = {'inputs': ['mdc_base_universe_d2_030_mdc_basefill_030'], 'func': mdc_base_universe_d3_030_mdc_basefill_030}


def mdc_base_universe_d3_031_mdc_basefill_031(mdc_base_universe_d2_031_mdc_basefill_031):
    return _base_universe_d3(mdc_base_universe_d2_031_mdc_basefill_031, 31)
MDC_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['mdc_base_universe_d3_031_mdc_basefill_031'] = {'inputs': ['mdc_base_universe_d2_031_mdc_basefill_031'], 'func': mdc_base_universe_d3_031_mdc_basefill_031}


def mdc_base_universe_d3_032_mdc_basefill_032(mdc_base_universe_d2_032_mdc_basefill_032):
    return _base_universe_d3(mdc_base_universe_d2_032_mdc_basefill_032, 32)
MDC_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['mdc_base_universe_d3_032_mdc_basefill_032'] = {'inputs': ['mdc_base_universe_d2_032_mdc_basefill_032'], 'func': mdc_base_universe_d3_032_mdc_basefill_032}


def mdc_base_universe_d3_033_mdc_basefill_033(mdc_base_universe_d2_033_mdc_basefill_033):
    return _base_universe_d3(mdc_base_universe_d2_033_mdc_basefill_033, 33)
MDC_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['mdc_base_universe_d3_033_mdc_basefill_033'] = {'inputs': ['mdc_base_universe_d2_033_mdc_basefill_033'], 'func': mdc_base_universe_d3_033_mdc_basefill_033}


def mdc_base_universe_d3_034_mdc_basefill_034(mdc_base_universe_d2_034_mdc_basefill_034):
    return _base_universe_d3(mdc_base_universe_d2_034_mdc_basefill_034, 34)
MDC_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['mdc_base_universe_d3_034_mdc_basefill_034'] = {'inputs': ['mdc_base_universe_d2_034_mdc_basefill_034'], 'func': mdc_base_universe_d3_034_mdc_basefill_034}


def mdc_base_universe_d3_035_mdc_basefill_035(mdc_base_universe_d2_035_mdc_basefill_035):
    return _base_universe_d3(mdc_base_universe_d2_035_mdc_basefill_035, 35)
MDC_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['mdc_base_universe_d3_035_mdc_basefill_035'] = {'inputs': ['mdc_base_universe_d2_035_mdc_basefill_035'], 'func': mdc_base_universe_d3_035_mdc_basefill_035}


def mdc_base_universe_d3_036_mdc_basefill_036(mdc_base_universe_d2_036_mdc_basefill_036):
    return _base_universe_d3(mdc_base_universe_d2_036_mdc_basefill_036, 36)
MDC_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['mdc_base_universe_d3_036_mdc_basefill_036'] = {'inputs': ['mdc_base_universe_d2_036_mdc_basefill_036'], 'func': mdc_base_universe_d3_036_mdc_basefill_036}


def mdc_base_universe_d3_037_mdc_basefill_037(mdc_base_universe_d2_037_mdc_basefill_037):
    return _base_universe_d3(mdc_base_universe_d2_037_mdc_basefill_037, 37)
MDC_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['mdc_base_universe_d3_037_mdc_basefill_037'] = {'inputs': ['mdc_base_universe_d2_037_mdc_basefill_037'], 'func': mdc_base_universe_d3_037_mdc_basefill_037}


def mdc_base_universe_d3_038_mdc_basefill_038(mdc_base_universe_d2_038_mdc_basefill_038):
    return _base_universe_d3(mdc_base_universe_d2_038_mdc_basefill_038, 38)
MDC_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['mdc_base_universe_d3_038_mdc_basefill_038'] = {'inputs': ['mdc_base_universe_d2_038_mdc_basefill_038'], 'func': mdc_base_universe_d3_038_mdc_basefill_038}


def mdc_base_universe_d3_039_mdc_basefill_039(mdc_base_universe_d2_039_mdc_basefill_039):
    return _base_universe_d3(mdc_base_universe_d2_039_mdc_basefill_039, 39)
MDC_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['mdc_base_universe_d3_039_mdc_basefill_039'] = {'inputs': ['mdc_base_universe_d2_039_mdc_basefill_039'], 'func': mdc_base_universe_d3_039_mdc_basefill_039}


def mdc_base_universe_d3_040_mdc_basefill_040(mdc_base_universe_d2_040_mdc_basefill_040):
    return _base_universe_d3(mdc_base_universe_d2_040_mdc_basefill_040, 40)
MDC_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['mdc_base_universe_d3_040_mdc_basefill_040'] = {'inputs': ['mdc_base_universe_d2_040_mdc_basefill_040'], 'func': mdc_base_universe_d3_040_mdc_basefill_040}


def mdc_base_universe_d3_041_mdc_basefill_041(mdc_base_universe_d2_041_mdc_basefill_041):
    return _base_universe_d3(mdc_base_universe_d2_041_mdc_basefill_041, 41)
MDC_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['mdc_base_universe_d3_041_mdc_basefill_041'] = {'inputs': ['mdc_base_universe_d2_041_mdc_basefill_041'], 'func': mdc_base_universe_d3_041_mdc_basefill_041}


def mdc_base_universe_d3_042_mdc_basefill_042(mdc_base_universe_d2_042_mdc_basefill_042):
    return _base_universe_d3(mdc_base_universe_d2_042_mdc_basefill_042, 42)
MDC_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['mdc_base_universe_d3_042_mdc_basefill_042'] = {'inputs': ['mdc_base_universe_d2_042_mdc_basefill_042'], 'func': mdc_base_universe_d3_042_mdc_basefill_042}


def mdc_base_universe_d3_043_mdc_basefill_043(mdc_base_universe_d2_043_mdc_basefill_043):
    return _base_universe_d3(mdc_base_universe_d2_043_mdc_basefill_043, 43)
MDC_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['mdc_base_universe_d3_043_mdc_basefill_043'] = {'inputs': ['mdc_base_universe_d2_043_mdc_basefill_043'], 'func': mdc_base_universe_d3_043_mdc_basefill_043}


def mdc_base_universe_d3_044_mdc_basefill_044(mdc_base_universe_d2_044_mdc_basefill_044):
    return _base_universe_d3(mdc_base_universe_d2_044_mdc_basefill_044, 44)
MDC_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['mdc_base_universe_d3_044_mdc_basefill_044'] = {'inputs': ['mdc_base_universe_d2_044_mdc_basefill_044'], 'func': mdc_base_universe_d3_044_mdc_basefill_044}


def mdc_base_universe_d3_045_mdc_basefill_045(mdc_base_universe_d2_045_mdc_basefill_045):
    return _base_universe_d3(mdc_base_universe_d2_045_mdc_basefill_045, 45)
MDC_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['mdc_base_universe_d3_045_mdc_basefill_045'] = {'inputs': ['mdc_base_universe_d2_045_mdc_basefill_045'], 'func': mdc_base_universe_d3_045_mdc_basefill_045}


def mdc_base_universe_d3_046_mdc_basefill_046(mdc_base_universe_d2_046_mdc_basefill_046):
    return _base_universe_d3(mdc_base_universe_d2_046_mdc_basefill_046, 46)
MDC_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['mdc_base_universe_d3_046_mdc_basefill_046'] = {'inputs': ['mdc_base_universe_d2_046_mdc_basefill_046'], 'func': mdc_base_universe_d3_046_mdc_basefill_046}


def mdc_base_universe_d3_047_mdc_basefill_047(mdc_base_universe_d2_047_mdc_basefill_047):
    return _base_universe_d3(mdc_base_universe_d2_047_mdc_basefill_047, 47)
MDC_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['mdc_base_universe_d3_047_mdc_basefill_047'] = {'inputs': ['mdc_base_universe_d2_047_mdc_basefill_047'], 'func': mdc_base_universe_d3_047_mdc_basefill_047}


def mdc_base_universe_d3_048_mdc_basefill_048(mdc_base_universe_d2_048_mdc_basefill_048):
    return _base_universe_d3(mdc_base_universe_d2_048_mdc_basefill_048, 48)
MDC_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['mdc_base_universe_d3_048_mdc_basefill_048'] = {'inputs': ['mdc_base_universe_d2_048_mdc_basefill_048'], 'func': mdc_base_universe_d3_048_mdc_basefill_048}


def mdc_base_universe_d3_049_mdc_basefill_049(mdc_base_universe_d2_049_mdc_basefill_049):
    return _base_universe_d3(mdc_base_universe_d2_049_mdc_basefill_049, 49)
MDC_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['mdc_base_universe_d3_049_mdc_basefill_049'] = {'inputs': ['mdc_base_universe_d2_049_mdc_basefill_049'], 'func': mdc_base_universe_d3_049_mdc_basefill_049}


def mdc_base_universe_d3_050_mdc_basefill_050(mdc_base_universe_d2_050_mdc_basefill_050):
    return _base_universe_d3(mdc_base_universe_d2_050_mdc_basefill_050, 50)
MDC_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['mdc_base_universe_d3_050_mdc_basefill_050'] = {'inputs': ['mdc_base_universe_d2_050_mdc_basefill_050'], 'func': mdc_base_universe_d3_050_mdc_basefill_050}


def mdc_base_universe_d3_051_mdc_basefill_051(mdc_base_universe_d2_051_mdc_basefill_051):
    return _base_universe_d3(mdc_base_universe_d2_051_mdc_basefill_051, 51)
MDC_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['mdc_base_universe_d3_051_mdc_basefill_051'] = {'inputs': ['mdc_base_universe_d2_051_mdc_basefill_051'], 'func': mdc_base_universe_d3_051_mdc_basefill_051}


def mdc_base_universe_d3_052_mdc_basefill_052(mdc_base_universe_d2_052_mdc_basefill_052):
    return _base_universe_d3(mdc_base_universe_d2_052_mdc_basefill_052, 52)
MDC_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['mdc_base_universe_d3_052_mdc_basefill_052'] = {'inputs': ['mdc_base_universe_d2_052_mdc_basefill_052'], 'func': mdc_base_universe_d3_052_mdc_basefill_052}


def mdc_base_universe_d3_053_mdc_basefill_053(mdc_base_universe_d2_053_mdc_basefill_053):
    return _base_universe_d3(mdc_base_universe_d2_053_mdc_basefill_053, 53)
MDC_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['mdc_base_universe_d3_053_mdc_basefill_053'] = {'inputs': ['mdc_base_universe_d2_053_mdc_basefill_053'], 'func': mdc_base_universe_d3_053_mdc_basefill_053}


def mdc_base_universe_d3_054_mdc_basefill_054(mdc_base_universe_d2_054_mdc_basefill_054):
    return _base_universe_d3(mdc_base_universe_d2_054_mdc_basefill_054, 54)
MDC_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['mdc_base_universe_d3_054_mdc_basefill_054'] = {'inputs': ['mdc_base_universe_d2_054_mdc_basefill_054'], 'func': mdc_base_universe_d3_054_mdc_basefill_054}


def mdc_base_universe_d3_055_mdc_basefill_055(mdc_base_universe_d2_055_mdc_basefill_055):
    return _base_universe_d3(mdc_base_universe_d2_055_mdc_basefill_055, 55)
MDC_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['mdc_base_universe_d3_055_mdc_basefill_055'] = {'inputs': ['mdc_base_universe_d2_055_mdc_basefill_055'], 'func': mdc_base_universe_d3_055_mdc_basefill_055}


def mdc_base_universe_d3_056_mdc_basefill_056(mdc_base_universe_d2_056_mdc_basefill_056):
    return _base_universe_d3(mdc_base_universe_d2_056_mdc_basefill_056, 56)
MDC_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['mdc_base_universe_d3_056_mdc_basefill_056'] = {'inputs': ['mdc_base_universe_d2_056_mdc_basefill_056'], 'func': mdc_base_universe_d3_056_mdc_basefill_056}


def mdc_base_universe_d3_057_mdc_basefill_057(mdc_base_universe_d2_057_mdc_basefill_057):
    return _base_universe_d3(mdc_base_universe_d2_057_mdc_basefill_057, 57)
MDC_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['mdc_base_universe_d3_057_mdc_basefill_057'] = {'inputs': ['mdc_base_universe_d2_057_mdc_basefill_057'], 'func': mdc_base_universe_d3_057_mdc_basefill_057}


def mdc_base_universe_d3_058_mdc_basefill_058(mdc_base_universe_d2_058_mdc_basefill_058):
    return _base_universe_d3(mdc_base_universe_d2_058_mdc_basefill_058, 58)
MDC_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['mdc_base_universe_d3_058_mdc_basefill_058'] = {'inputs': ['mdc_base_universe_d2_058_mdc_basefill_058'], 'func': mdc_base_universe_d3_058_mdc_basefill_058}


def mdc_base_universe_d3_059_mdc_basefill_059(mdc_base_universe_d2_059_mdc_basefill_059):
    return _base_universe_d3(mdc_base_universe_d2_059_mdc_basefill_059, 59)
MDC_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['mdc_base_universe_d3_059_mdc_basefill_059'] = {'inputs': ['mdc_base_universe_d2_059_mdc_basefill_059'], 'func': mdc_base_universe_d3_059_mdc_basefill_059}


def mdc_base_universe_d3_060_mdc_basefill_060(mdc_base_universe_d2_060_mdc_basefill_060):
    return _base_universe_d3(mdc_base_universe_d2_060_mdc_basefill_060, 60)
MDC_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['mdc_base_universe_d3_060_mdc_basefill_060'] = {'inputs': ['mdc_base_universe_d2_060_mdc_basefill_060'], 'func': mdc_base_universe_d3_060_mdc_basefill_060}


def mdc_base_universe_d3_061_mdc_basefill_061(mdc_base_universe_d2_061_mdc_basefill_061):
    return _base_universe_d3(mdc_base_universe_d2_061_mdc_basefill_061, 61)
MDC_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['mdc_base_universe_d3_061_mdc_basefill_061'] = {'inputs': ['mdc_base_universe_d2_061_mdc_basefill_061'], 'func': mdc_base_universe_d3_061_mdc_basefill_061}


def mdc_base_universe_d3_062_mdc_basefill_062(mdc_base_universe_d2_062_mdc_basefill_062):
    return _base_universe_d3(mdc_base_universe_d2_062_mdc_basefill_062, 62)
MDC_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['mdc_base_universe_d3_062_mdc_basefill_062'] = {'inputs': ['mdc_base_universe_d2_062_mdc_basefill_062'], 'func': mdc_base_universe_d3_062_mdc_basefill_062}


def mdc_base_universe_d3_063_mdc_basefill_063(mdc_base_universe_d2_063_mdc_basefill_063):
    return _base_universe_d3(mdc_base_universe_d2_063_mdc_basefill_063, 63)
MDC_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['mdc_base_universe_d3_063_mdc_basefill_063'] = {'inputs': ['mdc_base_universe_d2_063_mdc_basefill_063'], 'func': mdc_base_universe_d3_063_mdc_basefill_063}


def mdc_base_universe_d3_064_mdc_basefill_064(mdc_base_universe_d2_064_mdc_basefill_064):
    return _base_universe_d3(mdc_base_universe_d2_064_mdc_basefill_064, 64)
MDC_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['mdc_base_universe_d3_064_mdc_basefill_064'] = {'inputs': ['mdc_base_universe_d2_064_mdc_basefill_064'], 'func': mdc_base_universe_d3_064_mdc_basefill_064}


def mdc_base_universe_d3_065_mdc_basefill_065(mdc_base_universe_d2_065_mdc_basefill_065):
    return _base_universe_d3(mdc_base_universe_d2_065_mdc_basefill_065, 65)
MDC_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['mdc_base_universe_d3_065_mdc_basefill_065'] = {'inputs': ['mdc_base_universe_d2_065_mdc_basefill_065'], 'func': mdc_base_universe_d3_065_mdc_basefill_065}


def mdc_base_universe_d3_066_mdc_basefill_066(mdc_base_universe_d2_066_mdc_basefill_066):
    return _base_universe_d3(mdc_base_universe_d2_066_mdc_basefill_066, 66)
MDC_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['mdc_base_universe_d3_066_mdc_basefill_066'] = {'inputs': ['mdc_base_universe_d2_066_mdc_basefill_066'], 'func': mdc_base_universe_d3_066_mdc_basefill_066}


def mdc_base_universe_d3_067_mdc_basefill_067(mdc_base_universe_d2_067_mdc_basefill_067):
    return _base_universe_d3(mdc_base_universe_d2_067_mdc_basefill_067, 67)
MDC_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['mdc_base_universe_d3_067_mdc_basefill_067'] = {'inputs': ['mdc_base_universe_d2_067_mdc_basefill_067'], 'func': mdc_base_universe_d3_067_mdc_basefill_067}


def mdc_base_universe_d3_068_mdc_basefill_068(mdc_base_universe_d2_068_mdc_basefill_068):
    return _base_universe_d3(mdc_base_universe_d2_068_mdc_basefill_068, 68)
MDC_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['mdc_base_universe_d3_068_mdc_basefill_068'] = {'inputs': ['mdc_base_universe_d2_068_mdc_basefill_068'], 'func': mdc_base_universe_d3_068_mdc_basefill_068}


def mdc_base_universe_d3_069_mdc_basefill_069(mdc_base_universe_d2_069_mdc_basefill_069):
    return _base_universe_d3(mdc_base_universe_d2_069_mdc_basefill_069, 69)
MDC_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['mdc_base_universe_d3_069_mdc_basefill_069'] = {'inputs': ['mdc_base_universe_d2_069_mdc_basefill_069'], 'func': mdc_base_universe_d3_069_mdc_basefill_069}


def mdc_base_universe_d3_070_mdc_basefill_070(mdc_base_universe_d2_070_mdc_basefill_070):
    return _base_universe_d3(mdc_base_universe_d2_070_mdc_basefill_070, 70)
MDC_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['mdc_base_universe_d3_070_mdc_basefill_070'] = {'inputs': ['mdc_base_universe_d2_070_mdc_basefill_070'], 'func': mdc_base_universe_d3_070_mdc_basefill_070}


def mdc_base_universe_d3_071_mdc_basefill_071(mdc_base_universe_d2_071_mdc_basefill_071):
    return _base_universe_d3(mdc_base_universe_d2_071_mdc_basefill_071, 71)
MDC_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['mdc_base_universe_d3_071_mdc_basefill_071'] = {'inputs': ['mdc_base_universe_d2_071_mdc_basefill_071'], 'func': mdc_base_universe_d3_071_mdc_basefill_071}


def mdc_base_universe_d3_072_mdc_basefill_072(mdc_base_universe_d2_072_mdc_basefill_072):
    return _base_universe_d3(mdc_base_universe_d2_072_mdc_basefill_072, 72)
MDC_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['mdc_base_universe_d3_072_mdc_basefill_072'] = {'inputs': ['mdc_base_universe_d2_072_mdc_basefill_072'], 'func': mdc_base_universe_d3_072_mdc_basefill_072}


def mdc_base_universe_d3_073_mdc_basefill_073(mdc_base_universe_d2_073_mdc_basefill_073):
    return _base_universe_d3(mdc_base_universe_d2_073_mdc_basefill_073, 73)
MDC_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['mdc_base_universe_d3_073_mdc_basefill_073'] = {'inputs': ['mdc_base_universe_d2_073_mdc_basefill_073'], 'func': mdc_base_universe_d3_073_mdc_basefill_073}


def mdc_base_universe_d3_074_mdc_basefill_074(mdc_base_universe_d2_074_mdc_basefill_074):
    return _base_universe_d3(mdc_base_universe_d2_074_mdc_basefill_074, 74)
MDC_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['mdc_base_universe_d3_074_mdc_basefill_074'] = {'inputs': ['mdc_base_universe_d2_074_mdc_basefill_074'], 'func': mdc_base_universe_d3_074_mdc_basefill_074}


def mdc_base_universe_d3_075_mdc_basefill_075(mdc_base_universe_d2_075_mdc_basefill_075):
    return _base_universe_d3(mdc_base_universe_d2_075_mdc_basefill_075, 75)
MDC_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['mdc_base_universe_d3_075_mdc_basefill_075'] = {'inputs': ['mdc_base_universe_d2_075_mdc_basefill_075'], 'func': mdc_base_universe_d3_075_mdc_basefill_075}
