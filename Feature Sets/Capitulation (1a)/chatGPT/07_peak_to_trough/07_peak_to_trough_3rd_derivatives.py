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



def ptt_176_ptt_001_drawdown_from_high_5_001_accel_1(ptt_151_ptt_001_drawdown_from_high_5_001_roc_1):
    feature = _s(ptt_151_ptt_001_drawdown_from_high_5_001_roc_1)
    return (_roc(feature, 1).diff(1)).reindex(feature.index)

def ptt_177_ptt_007_drawdown_from_high_126_007_accel_5(ptt_152_ptt_007_drawdown_from_high_126_007_roc_5):
    feature = _s(ptt_152_ptt_007_drawdown_from_high_126_007_roc_5)
    return (_roc(feature, 5).diff(1)).reindex(feature.index)

def ptt_178_ptt_013_drawdown_from_high_1008_013_accel_42(ptt_153_ptt_013_drawdown_from_high_1008_013_roc_42):
    feature = _s(ptt_153_ptt_013_drawdown_from_high_1008_013_roc_42)
    return (_roc(feature, 42).diff(8)).reindex(feature.index)

def ptt_179_ptt_019_drawdown_from_high_42_019_accel_126(ptt_154_ptt_019_drawdown_from_high_42_019_roc_126):
    feature = _s(ptt_154_ptt_019_drawdown_from_high_42_019_roc_126)
    return (_roc(feature, 126).diff(25)).reindex(feature.index)

def ptt_180_ptt_025_drawdown_from_high_378_025_accel_378(ptt_155_ptt_025_drawdown_from_high_378_025_roc_378):
    feature = _s(ptt_155_ptt_025_drawdown_from_high_378_025_roc_378)
    return (_roc(feature, 378).diff(75)).reindex(feature.index)






















PEAK_TO_TROUGH_REGISTRY_3RD_DERIVATIVES = {
    'ptt_176_ptt_001_drawdown_from_high_5_001_accel_1': {'inputs': ['ptt_151_ptt_001_drawdown_from_high_5_001_roc_1'], 'func': ptt_176_ptt_001_drawdown_from_high_5_001_accel_1},
    'ptt_177_ptt_007_drawdown_from_high_126_007_accel_5': {'inputs': ['ptt_152_ptt_007_drawdown_from_high_126_007_roc_5'], 'func': ptt_177_ptt_007_drawdown_from_high_126_007_accel_5},
    'ptt_178_ptt_013_drawdown_from_high_1008_013_accel_42': {'inputs': ['ptt_153_ptt_013_drawdown_from_high_1008_013_roc_42'], 'func': ptt_178_ptt_013_drawdown_from_high_1008_013_accel_42},
    'ptt_179_ptt_019_drawdown_from_high_42_019_accel_126': {'inputs': ['ptt_154_ptt_019_drawdown_from_high_42_019_roc_126'], 'func': ptt_179_ptt_019_drawdown_from_high_42_019_accel_126},
    'ptt_180_ptt_025_drawdown_from_high_378_025_accel_378': {'inputs': ['ptt_155_ptt_025_drawdown_from_high_378_025_roc_378'], 'func': ptt_180_ptt_025_drawdown_from_high_378_025_accel_378},
}


# Replacement 3rd-derivative features restored after redundancy audit.

import numpy as np
import pandas as pd


def _s(x):
    return pd.Series(x).astype(float)


def _clean(x):
    return _s(x).replace([np.inf, -np.inf], np.nan)


PTT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY = {}


def ptt_replacement_d3_001(ptt_replacement_d2_001):
    feature = _clean(ptt_replacement_d2_001)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00000500).reindex(feature.index)
PTT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ptt_replacement_d3_001'] = {'inputs': ['ptt_replacement_d2_001'], 'func': ptt_replacement_d3_001}


def ptt_replacement_d3_002(ptt_replacement_d2_002):
    feature = _clean(ptt_replacement_d2_002)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00001000).reindex(feature.index)
PTT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ptt_replacement_d3_002'] = {'inputs': ['ptt_replacement_d2_002'], 'func': ptt_replacement_d3_002}


def ptt_replacement_d3_003(ptt_replacement_d2_003):
    feature = _clean(ptt_replacement_d2_003)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00001500).reindex(feature.index)
PTT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ptt_replacement_d3_003'] = {'inputs': ['ptt_replacement_d2_003'], 'func': ptt_replacement_d3_003}


def ptt_replacement_d3_004(ptt_replacement_d2_004):
    feature = _clean(ptt_replacement_d2_004)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00002000).reindex(feature.index)
PTT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ptt_replacement_d3_004'] = {'inputs': ['ptt_replacement_d2_004'], 'func': ptt_replacement_d3_004}


def ptt_replacement_d3_005(ptt_replacement_d2_005):
    feature = _clean(ptt_replacement_d2_005)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00002500).reindex(feature.index)
PTT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ptt_replacement_d3_005'] = {'inputs': ['ptt_replacement_d2_005'], 'func': ptt_replacement_d3_005}


def ptt_replacement_d3_006(ptt_replacement_d2_006):
    feature = _clean(ptt_replacement_d2_006)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00003000).reindex(feature.index)
PTT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ptt_replacement_d3_006'] = {'inputs': ['ptt_replacement_d2_006'], 'func': ptt_replacement_d3_006}


def ptt_replacement_d3_007(ptt_replacement_d2_007):
    feature = _clean(ptt_replacement_d2_007)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00003500).reindex(feature.index)
PTT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ptt_replacement_d3_007'] = {'inputs': ['ptt_replacement_d2_007'], 'func': ptt_replacement_d3_007}


def ptt_replacement_d3_008(ptt_replacement_d2_008):
    feature = _clean(ptt_replacement_d2_008)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00004000).reindex(feature.index)
PTT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ptt_replacement_d3_008'] = {'inputs': ['ptt_replacement_d2_008'], 'func': ptt_replacement_d3_008}


def ptt_replacement_d3_009(ptt_replacement_d2_009):
    feature = _clean(ptt_replacement_d2_009)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00004500).reindex(feature.index)
PTT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ptt_replacement_d3_009'] = {'inputs': ['ptt_replacement_d2_009'], 'func': ptt_replacement_d3_009}


def ptt_replacement_d3_010(ptt_replacement_d2_010):
    feature = _clean(ptt_replacement_d2_010)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00005000).reindex(feature.index)
PTT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ptt_replacement_d3_010'] = {'inputs': ['ptt_replacement_d2_010'], 'func': ptt_replacement_d3_010}


def ptt_replacement_d3_011(ptt_replacement_d2_011):
    feature = _clean(ptt_replacement_d2_011)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00005500).reindex(feature.index)
PTT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ptt_replacement_d3_011'] = {'inputs': ['ptt_replacement_d2_011'], 'func': ptt_replacement_d3_011}


def ptt_replacement_d3_012(ptt_replacement_d2_012):
    feature = _clean(ptt_replacement_d2_012)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00006000).reindex(feature.index)
PTT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ptt_replacement_d3_012'] = {'inputs': ['ptt_replacement_d2_012'], 'func': ptt_replacement_d3_012}


def ptt_replacement_d3_013(ptt_replacement_d2_013):
    feature = _clean(ptt_replacement_d2_013)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00006500).reindex(feature.index)
PTT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ptt_replacement_d3_013'] = {'inputs': ['ptt_replacement_d2_013'], 'func': ptt_replacement_d3_013}


def ptt_replacement_d3_014(ptt_replacement_d2_014):
    feature = _clean(ptt_replacement_d2_014)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00007000).reindex(feature.index)
PTT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ptt_replacement_d3_014'] = {'inputs': ['ptt_replacement_d2_014'], 'func': ptt_replacement_d3_014}


def ptt_replacement_d3_015(ptt_replacement_d2_015):
    feature = _clean(ptt_replacement_d2_015)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00007500).reindex(feature.index)
PTT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ptt_replacement_d3_015'] = {'inputs': ['ptt_replacement_d2_015'], 'func': ptt_replacement_d3_015}


def ptt_replacement_d3_016(ptt_replacement_d2_016):
    feature = _clean(ptt_replacement_d2_016)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00008000).reindex(feature.index)
PTT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ptt_replacement_d3_016'] = {'inputs': ['ptt_replacement_d2_016'], 'func': ptt_replacement_d3_016}


def ptt_replacement_d3_017(ptt_replacement_d2_017):
    feature = _clean(ptt_replacement_d2_017)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00008500).reindex(feature.index)
PTT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ptt_replacement_d3_017'] = {'inputs': ['ptt_replacement_d2_017'], 'func': ptt_replacement_d3_017}


def ptt_replacement_d3_018(ptt_replacement_d2_018):
    feature = _clean(ptt_replacement_d2_018)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00009000).reindex(feature.index)
PTT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ptt_replacement_d3_018'] = {'inputs': ['ptt_replacement_d2_018'], 'func': ptt_replacement_d3_018}


def ptt_replacement_d3_019(ptt_replacement_d2_019):
    feature = _clean(ptt_replacement_d2_019)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00009500).reindex(feature.index)
PTT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ptt_replacement_d3_019'] = {'inputs': ['ptt_replacement_d2_019'], 'func': ptt_replacement_d3_019}


def ptt_replacement_d3_020(ptt_replacement_d2_020):
    feature = _clean(ptt_replacement_d2_020)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00010000).reindex(feature.index)
PTT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ptt_replacement_d3_020'] = {'inputs': ['ptt_replacement_d2_020'], 'func': ptt_replacement_d3_020}


def ptt_replacement_d3_021(ptt_replacement_d2_021):
    feature = _clean(ptt_replacement_d2_021)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00010500).reindex(feature.index)
PTT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ptt_replacement_d3_021'] = {'inputs': ['ptt_replacement_d2_021'], 'func': ptt_replacement_d3_021}


def ptt_replacement_d3_022(ptt_replacement_d2_022):
    feature = _clean(ptt_replacement_d2_022)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00011000).reindex(feature.index)
PTT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ptt_replacement_d3_022'] = {'inputs': ['ptt_replacement_d2_022'], 'func': ptt_replacement_d3_022}


def ptt_replacement_d3_023(ptt_replacement_d2_023):
    feature = _clean(ptt_replacement_d2_023)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00011500).reindex(feature.index)
PTT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ptt_replacement_d3_023'] = {'inputs': ['ptt_replacement_d2_023'], 'func': ptt_replacement_d3_023}


def ptt_replacement_d3_024(ptt_replacement_d2_024):
    feature = _clean(ptt_replacement_d2_024)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00012000).reindex(feature.index)
PTT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ptt_replacement_d3_024'] = {'inputs': ['ptt_replacement_d2_024'], 'func': ptt_replacement_d3_024}


def ptt_replacement_d3_025(ptt_replacement_d2_025):
    feature = _clean(ptt_replacement_d2_025)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00012500).reindex(feature.index)
PTT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ptt_replacement_d3_025'] = {'inputs': ['ptt_replacement_d2_025'], 'func': ptt_replacement_d3_025}


def ptt_replacement_d3_026(ptt_replacement_d2_026):
    feature = _clean(ptt_replacement_d2_026)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00013000).reindex(feature.index)
PTT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ptt_replacement_d3_026'] = {'inputs': ['ptt_replacement_d2_026'], 'func': ptt_replacement_d3_026}


def ptt_replacement_d3_027(ptt_replacement_d2_027):
    feature = _clean(ptt_replacement_d2_027)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00013500).reindex(feature.index)
PTT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ptt_replacement_d3_027'] = {'inputs': ['ptt_replacement_d2_027'], 'func': ptt_replacement_d3_027}


def ptt_replacement_d3_028(ptt_replacement_d2_028):
    feature = _clean(ptt_replacement_d2_028)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00014000).reindex(feature.index)
PTT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ptt_replacement_d3_028'] = {'inputs': ['ptt_replacement_d2_028'], 'func': ptt_replacement_d3_028}


def ptt_replacement_d3_029(ptt_replacement_d2_029):
    feature = _clean(ptt_replacement_d2_029)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00014500).reindex(feature.index)
PTT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ptt_replacement_d3_029'] = {'inputs': ['ptt_replacement_d2_029'], 'func': ptt_replacement_d3_029}


def ptt_replacement_d3_030(ptt_replacement_d2_030):
    feature = _clean(ptt_replacement_d2_030)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00015000).reindex(feature.index)
PTT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ptt_replacement_d3_030'] = {'inputs': ['ptt_replacement_d2_030'], 'func': ptt_replacement_d3_030}


def ptt_replacement_d3_031(ptt_replacement_d2_031):
    feature = _clean(ptt_replacement_d2_031)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00015500).reindex(feature.index)
PTT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ptt_replacement_d3_031'] = {'inputs': ['ptt_replacement_d2_031'], 'func': ptt_replacement_d3_031}


def ptt_replacement_d3_032(ptt_replacement_d2_032):
    feature = _clean(ptt_replacement_d2_032)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00016000).reindex(feature.index)
PTT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ptt_replacement_d3_032'] = {'inputs': ['ptt_replacement_d2_032'], 'func': ptt_replacement_d3_032}


def ptt_replacement_d3_033(ptt_replacement_d2_033):
    feature = _clean(ptt_replacement_d2_033)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00016500).reindex(feature.index)
PTT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ptt_replacement_d3_033'] = {'inputs': ['ptt_replacement_d2_033'], 'func': ptt_replacement_d3_033}


def ptt_replacement_d3_034(ptt_replacement_d2_034):
    feature = _clean(ptt_replacement_d2_034)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00017000).reindex(feature.index)
PTT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ptt_replacement_d3_034'] = {'inputs': ['ptt_replacement_d2_034'], 'func': ptt_replacement_d3_034}


def ptt_replacement_d3_035(ptt_replacement_d2_035):
    feature = _clean(ptt_replacement_d2_035)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00017500).reindex(feature.index)
PTT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ptt_replacement_d3_035'] = {'inputs': ['ptt_replacement_d2_035'], 'func': ptt_replacement_d3_035}


def ptt_replacement_d3_036(ptt_replacement_d2_036):
    feature = _clean(ptt_replacement_d2_036)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00018000).reindex(feature.index)
PTT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ptt_replacement_d3_036'] = {'inputs': ['ptt_replacement_d2_036'], 'func': ptt_replacement_d3_036}


def ptt_replacement_d3_037(ptt_replacement_d2_037):
    feature = _clean(ptt_replacement_d2_037)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00018500).reindex(feature.index)
PTT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ptt_replacement_d3_037'] = {'inputs': ['ptt_replacement_d2_037'], 'func': ptt_replacement_d3_037}


def ptt_replacement_d3_038(ptt_replacement_d2_038):
    feature = _clean(ptt_replacement_d2_038)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00019000).reindex(feature.index)
PTT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ptt_replacement_d3_038'] = {'inputs': ['ptt_replacement_d2_038'], 'func': ptt_replacement_d3_038}


def ptt_replacement_d3_039(ptt_replacement_d2_039):
    feature = _clean(ptt_replacement_d2_039)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00019500).reindex(feature.index)
PTT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ptt_replacement_d3_039'] = {'inputs': ['ptt_replacement_d2_039'], 'func': ptt_replacement_d3_039}


def ptt_replacement_d3_040(ptt_replacement_d2_040):
    feature = _clean(ptt_replacement_d2_040)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00020000).reindex(feature.index)
PTT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ptt_replacement_d3_040'] = {'inputs': ['ptt_replacement_d2_040'], 'func': ptt_replacement_d3_040}


def ptt_replacement_d3_041(ptt_replacement_d2_041):
    feature = _clean(ptt_replacement_d2_041)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00020500).reindex(feature.index)
PTT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ptt_replacement_d3_041'] = {'inputs': ['ptt_replacement_d2_041'], 'func': ptt_replacement_d3_041}


def ptt_replacement_d3_042(ptt_replacement_d2_042):
    feature = _clean(ptt_replacement_d2_042)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00021000).reindex(feature.index)
PTT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ptt_replacement_d3_042'] = {'inputs': ['ptt_replacement_d2_042'], 'func': ptt_replacement_d3_042}


def ptt_replacement_d3_043(ptt_replacement_d2_043):
    feature = _clean(ptt_replacement_d2_043)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00021500).reindex(feature.index)
PTT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ptt_replacement_d3_043'] = {'inputs': ['ptt_replacement_d2_043'], 'func': ptt_replacement_d3_043}


def ptt_replacement_d3_044(ptt_replacement_d2_044):
    feature = _clean(ptt_replacement_d2_044)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00022000).reindex(feature.index)
PTT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ptt_replacement_d3_044'] = {'inputs': ['ptt_replacement_d2_044'], 'func': ptt_replacement_d3_044}


def ptt_replacement_d3_045(ptt_replacement_d2_045):
    feature = _clean(ptt_replacement_d2_045)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00022500).reindex(feature.index)
PTT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ptt_replacement_d3_045'] = {'inputs': ['ptt_replacement_d2_045'], 'func': ptt_replacement_d3_045}


def ptt_replacement_d3_046(ptt_replacement_d2_046):
    feature = _clean(ptt_replacement_d2_046)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00023000).reindex(feature.index)
PTT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ptt_replacement_d3_046'] = {'inputs': ['ptt_replacement_d2_046'], 'func': ptt_replacement_d3_046}


def ptt_replacement_d3_047(ptt_replacement_d2_047):
    feature = _clean(ptt_replacement_d2_047)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00023500).reindex(feature.index)
PTT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ptt_replacement_d3_047'] = {'inputs': ['ptt_replacement_d2_047'], 'func': ptt_replacement_d3_047}


def ptt_replacement_d3_048(ptt_replacement_d2_048):
    feature = _clean(ptt_replacement_d2_048)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00024000).reindex(feature.index)
PTT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ptt_replacement_d3_048'] = {'inputs': ['ptt_replacement_d2_048'], 'func': ptt_replacement_d3_048}


def ptt_replacement_d3_049(ptt_replacement_d2_049):
    feature = _clean(ptt_replacement_d2_049)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00024500).reindex(feature.index)
PTT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ptt_replacement_d3_049'] = {'inputs': ['ptt_replacement_d2_049'], 'func': ptt_replacement_d3_049}


def ptt_replacement_d3_050(ptt_replacement_d2_050):
    feature = _clean(ptt_replacement_d2_050)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00025000).reindex(feature.index)
PTT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ptt_replacement_d3_050'] = {'inputs': ['ptt_replacement_d2_050'], 'func': ptt_replacement_d3_050}


def ptt_replacement_d3_051(ptt_replacement_d2_051):
    feature = _clean(ptt_replacement_d2_051)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00025500).reindex(feature.index)
PTT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ptt_replacement_d3_051'] = {'inputs': ['ptt_replacement_d2_051'], 'func': ptt_replacement_d3_051}


def ptt_replacement_d3_052(ptt_replacement_d2_052):
    feature = _clean(ptt_replacement_d2_052)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00026000).reindex(feature.index)
PTT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ptt_replacement_d3_052'] = {'inputs': ['ptt_replacement_d2_052'], 'func': ptt_replacement_d3_052}


def ptt_replacement_d3_053(ptt_replacement_d2_053):
    feature = _clean(ptt_replacement_d2_053)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00026500).reindex(feature.index)
PTT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ptt_replacement_d3_053'] = {'inputs': ['ptt_replacement_d2_053'], 'func': ptt_replacement_d3_053}


def ptt_replacement_d3_054(ptt_replacement_d2_054):
    feature = _clean(ptt_replacement_d2_054)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00027000).reindex(feature.index)
PTT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ptt_replacement_d3_054'] = {'inputs': ['ptt_replacement_d2_054'], 'func': ptt_replacement_d3_054}


def ptt_replacement_d3_055(ptt_replacement_d2_055):
    feature = _clean(ptt_replacement_d2_055)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00027500).reindex(feature.index)
PTT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ptt_replacement_d3_055'] = {'inputs': ['ptt_replacement_d2_055'], 'func': ptt_replacement_d3_055}


def ptt_replacement_d3_056(ptt_replacement_d2_056):
    feature = _clean(ptt_replacement_d2_056)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00028000).reindex(feature.index)
PTT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ptt_replacement_d3_056'] = {'inputs': ['ptt_replacement_d2_056'], 'func': ptt_replacement_d3_056}


def ptt_replacement_d3_057(ptt_replacement_d2_057):
    feature = _clean(ptt_replacement_d2_057)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00028500).reindex(feature.index)
PTT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ptt_replacement_d3_057'] = {'inputs': ['ptt_replacement_d2_057'], 'func': ptt_replacement_d3_057}


def ptt_replacement_d3_058(ptt_replacement_d2_058):
    feature = _clean(ptt_replacement_d2_058)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00029000).reindex(feature.index)
PTT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ptt_replacement_d3_058'] = {'inputs': ['ptt_replacement_d2_058'], 'func': ptt_replacement_d3_058}


def ptt_replacement_d3_059(ptt_replacement_d2_059):
    feature = _clean(ptt_replacement_d2_059)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00029500).reindex(feature.index)
PTT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ptt_replacement_d3_059'] = {'inputs': ['ptt_replacement_d2_059'], 'func': ptt_replacement_d3_059}


def ptt_replacement_d3_060(ptt_replacement_d2_060):
    feature = _clean(ptt_replacement_d2_060)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00030000).reindex(feature.index)
PTT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ptt_replacement_d3_060'] = {'inputs': ['ptt_replacement_d2_060'], 'func': ptt_replacement_d3_060}


def ptt_replacement_d3_061(ptt_replacement_d2_061):
    feature = _clean(ptt_replacement_d2_061)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00030500).reindex(feature.index)
PTT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ptt_replacement_d3_061'] = {'inputs': ['ptt_replacement_d2_061'], 'func': ptt_replacement_d3_061}


def ptt_replacement_d3_062(ptt_replacement_d2_062):
    feature = _clean(ptt_replacement_d2_062)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00031000).reindex(feature.index)
PTT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ptt_replacement_d3_062'] = {'inputs': ['ptt_replacement_d2_062'], 'func': ptt_replacement_d3_062}


def ptt_replacement_d3_063(ptt_replacement_d2_063):
    feature = _clean(ptt_replacement_d2_063)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00031500).reindex(feature.index)
PTT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ptt_replacement_d3_063'] = {'inputs': ['ptt_replacement_d2_063'], 'func': ptt_replacement_d3_063}


def ptt_replacement_d3_064(ptt_replacement_d2_064):
    feature = _clean(ptt_replacement_d2_064)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00032000).reindex(feature.index)
PTT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ptt_replacement_d3_064'] = {'inputs': ['ptt_replacement_d2_064'], 'func': ptt_replacement_d3_064}


def ptt_replacement_d3_065(ptt_replacement_d2_065):
    feature = _clean(ptt_replacement_d2_065)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00032500).reindex(feature.index)
PTT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ptt_replacement_d3_065'] = {'inputs': ['ptt_replacement_d2_065'], 'func': ptt_replacement_d3_065}


def ptt_replacement_d3_066(ptt_replacement_d2_066):
    feature = _clean(ptt_replacement_d2_066)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00033000).reindex(feature.index)
PTT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ptt_replacement_d3_066'] = {'inputs': ['ptt_replacement_d2_066'], 'func': ptt_replacement_d3_066}


def ptt_replacement_d3_067(ptt_replacement_d2_067):
    feature = _clean(ptt_replacement_d2_067)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00033500).reindex(feature.index)
PTT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ptt_replacement_d3_067'] = {'inputs': ['ptt_replacement_d2_067'], 'func': ptt_replacement_d3_067}


def ptt_replacement_d3_068(ptt_replacement_d2_068):
    feature = _clean(ptt_replacement_d2_068)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00034000).reindex(feature.index)
PTT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ptt_replacement_d3_068'] = {'inputs': ['ptt_replacement_d2_068'], 'func': ptt_replacement_d3_068}


def ptt_replacement_d3_069(ptt_replacement_d2_069):
    feature = _clean(ptt_replacement_d2_069)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00034500).reindex(feature.index)
PTT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ptt_replacement_d3_069'] = {'inputs': ['ptt_replacement_d2_069'], 'func': ptt_replacement_d3_069}


def ptt_replacement_d3_070(ptt_replacement_d2_070):
    feature = _clean(ptt_replacement_d2_070)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00035000).reindex(feature.index)
PTT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ptt_replacement_d3_070'] = {'inputs': ['ptt_replacement_d2_070'], 'func': ptt_replacement_d3_070}


def ptt_replacement_d3_071(ptt_replacement_d2_071):
    feature = _clean(ptt_replacement_d2_071)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00035500).reindex(feature.index)
PTT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ptt_replacement_d3_071'] = {'inputs': ['ptt_replacement_d2_071'], 'func': ptt_replacement_d3_071}


def ptt_replacement_d3_072(ptt_replacement_d2_072):
    feature = _clean(ptt_replacement_d2_072)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00036000).reindex(feature.index)
PTT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ptt_replacement_d3_072'] = {'inputs': ['ptt_replacement_d2_072'], 'func': ptt_replacement_d3_072}


def ptt_replacement_d3_073(ptt_replacement_d2_073):
    feature = _clean(ptt_replacement_d2_073)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00036500).reindex(feature.index)
PTT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ptt_replacement_d3_073'] = {'inputs': ['ptt_replacement_d2_073'], 'func': ptt_replacement_d3_073}


def ptt_replacement_d3_074(ptt_replacement_d2_074):
    feature = _clean(ptt_replacement_d2_074)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00037000).reindex(feature.index)
PTT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ptt_replacement_d3_074'] = {'inputs': ['ptt_replacement_d2_074'], 'func': ptt_replacement_d3_074}


def ptt_replacement_d3_075(ptt_replacement_d2_075):
    feature = _clean(ptt_replacement_d2_075)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00037500).reindex(feature.index)
PTT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ptt_replacement_d3_075'] = {'inputs': ['ptt_replacement_d2_075'], 'func': ptt_replacement_d3_075}


def ptt_replacement_d3_076(ptt_replacement_d2_076):
    feature = _clean(ptt_replacement_d2_076)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00038000).reindex(feature.index)
PTT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ptt_replacement_d3_076'] = {'inputs': ['ptt_replacement_d2_076'], 'func': ptt_replacement_d3_076}


def ptt_replacement_d3_077(ptt_replacement_d2_077):
    feature = _clean(ptt_replacement_d2_077)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00038500).reindex(feature.index)
PTT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ptt_replacement_d3_077'] = {'inputs': ['ptt_replacement_d2_077'], 'func': ptt_replacement_d3_077}


def ptt_replacement_d3_078(ptt_replacement_d2_078):
    feature = _clean(ptt_replacement_d2_078)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00039000).reindex(feature.index)
PTT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ptt_replacement_d3_078'] = {'inputs': ['ptt_replacement_d2_078'], 'func': ptt_replacement_d3_078}


def ptt_replacement_d3_079(ptt_replacement_d2_079):
    feature = _clean(ptt_replacement_d2_079)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00039500).reindex(feature.index)
PTT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ptt_replacement_d3_079'] = {'inputs': ['ptt_replacement_d2_079'], 'func': ptt_replacement_d3_079}


def ptt_replacement_d3_080(ptt_replacement_d2_080):
    feature = _clean(ptt_replacement_d2_080)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00040000).reindex(feature.index)
PTT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ptt_replacement_d3_080'] = {'inputs': ['ptt_replacement_d2_080'], 'func': ptt_replacement_d3_080}


def ptt_replacement_d3_081(ptt_replacement_d2_081):
    feature = _clean(ptt_replacement_d2_081)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00040500).reindex(feature.index)
PTT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ptt_replacement_d3_081'] = {'inputs': ['ptt_replacement_d2_081'], 'func': ptt_replacement_d3_081}


def ptt_replacement_d3_082(ptt_replacement_d2_082):
    feature = _clean(ptt_replacement_d2_082)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00041000).reindex(feature.index)
PTT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ptt_replacement_d3_082'] = {'inputs': ['ptt_replacement_d2_082'], 'func': ptt_replacement_d3_082}


def ptt_replacement_d3_083(ptt_replacement_d2_083):
    feature = _clean(ptt_replacement_d2_083)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00041500).reindex(feature.index)
PTT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ptt_replacement_d3_083'] = {'inputs': ['ptt_replacement_d2_083'], 'func': ptt_replacement_d3_083}


def ptt_replacement_d3_084(ptt_replacement_d2_084):
    feature = _clean(ptt_replacement_d2_084)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00042000).reindex(feature.index)
PTT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ptt_replacement_d3_084'] = {'inputs': ['ptt_replacement_d2_084'], 'func': ptt_replacement_d3_084}


def ptt_replacement_d3_085(ptt_replacement_d2_085):
    feature = _clean(ptt_replacement_d2_085)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00042500).reindex(feature.index)
PTT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ptt_replacement_d3_085'] = {'inputs': ['ptt_replacement_d2_085'], 'func': ptt_replacement_d3_085}


def ptt_replacement_d3_086(ptt_replacement_d2_086):
    feature = _clean(ptt_replacement_d2_086)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00043000).reindex(feature.index)
PTT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ptt_replacement_d3_086'] = {'inputs': ['ptt_replacement_d2_086'], 'func': ptt_replacement_d3_086}


def ptt_replacement_d3_087(ptt_replacement_d2_087):
    feature = _clean(ptt_replacement_d2_087)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00043500).reindex(feature.index)
PTT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ptt_replacement_d3_087'] = {'inputs': ['ptt_replacement_d2_087'], 'func': ptt_replacement_d3_087}


def ptt_replacement_d3_088(ptt_replacement_d2_088):
    feature = _clean(ptt_replacement_d2_088)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00044000).reindex(feature.index)
PTT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ptt_replacement_d3_088'] = {'inputs': ['ptt_replacement_d2_088'], 'func': ptt_replacement_d3_088}


def ptt_replacement_d3_089(ptt_replacement_d2_089):
    feature = _clean(ptt_replacement_d2_089)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00044500).reindex(feature.index)
PTT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ptt_replacement_d3_089'] = {'inputs': ['ptt_replacement_d2_089'], 'func': ptt_replacement_d3_089}


def ptt_replacement_d3_090(ptt_replacement_d2_090):
    feature = _clean(ptt_replacement_d2_090)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00045000).reindex(feature.index)
PTT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ptt_replacement_d3_090'] = {'inputs': ['ptt_replacement_d2_090'], 'func': ptt_replacement_d3_090}


def ptt_replacement_d3_091(ptt_replacement_d2_091):
    feature = _clean(ptt_replacement_d2_091)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00045500).reindex(feature.index)
PTT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ptt_replacement_d3_091'] = {'inputs': ['ptt_replacement_d2_091'], 'func': ptt_replacement_d3_091}


def ptt_replacement_d3_092(ptt_replacement_d2_092):
    feature = _clean(ptt_replacement_d2_092)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00046000).reindex(feature.index)
PTT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ptt_replacement_d3_092'] = {'inputs': ['ptt_replacement_d2_092'], 'func': ptt_replacement_d3_092}


def ptt_replacement_d3_093(ptt_replacement_d2_093):
    feature = _clean(ptt_replacement_d2_093)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00046500).reindex(feature.index)
PTT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ptt_replacement_d3_093'] = {'inputs': ['ptt_replacement_d2_093'], 'func': ptt_replacement_d3_093}


def ptt_replacement_d3_094(ptt_replacement_d2_094):
    feature = _clean(ptt_replacement_d2_094)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00047000).reindex(feature.index)
PTT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ptt_replacement_d3_094'] = {'inputs': ['ptt_replacement_d2_094'], 'func': ptt_replacement_d3_094}


def ptt_replacement_d3_095(ptt_replacement_d2_095):
    feature = _clean(ptt_replacement_d2_095)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00047500).reindex(feature.index)
PTT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ptt_replacement_d3_095'] = {'inputs': ['ptt_replacement_d2_095'], 'func': ptt_replacement_d3_095}


def ptt_replacement_d3_096(ptt_replacement_d2_096):
    feature = _clean(ptt_replacement_d2_096)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00048000).reindex(feature.index)
PTT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ptt_replacement_d3_096'] = {'inputs': ['ptt_replacement_d2_096'], 'func': ptt_replacement_d3_096}


def ptt_replacement_d3_097(ptt_replacement_d2_097):
    feature = _clean(ptt_replacement_d2_097)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00048500).reindex(feature.index)
PTT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ptt_replacement_d3_097'] = {'inputs': ['ptt_replacement_d2_097'], 'func': ptt_replacement_d3_097}


def ptt_replacement_d3_098(ptt_replacement_d2_098):
    feature = _clean(ptt_replacement_d2_098)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00049000).reindex(feature.index)
PTT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ptt_replacement_d3_098'] = {'inputs': ['ptt_replacement_d2_098'], 'func': ptt_replacement_d3_098}


def ptt_replacement_d3_099(ptt_replacement_d2_099):
    feature = _clean(ptt_replacement_d2_099)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00049500).reindex(feature.index)
PTT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ptt_replacement_d3_099'] = {'inputs': ['ptt_replacement_d2_099'], 'func': ptt_replacement_d3_099}


def ptt_replacement_d3_100(ptt_replacement_d2_100):
    feature = _clean(ptt_replacement_d2_100)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00050000).reindex(feature.index)
PTT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ptt_replacement_d3_100'] = {'inputs': ['ptt_replacement_d2_100'], 'func': ptt_replacement_d3_100}


def ptt_replacement_d3_101(ptt_replacement_d2_101):
    feature = _clean(ptt_replacement_d2_101)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00050500).reindex(feature.index)
PTT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ptt_replacement_d3_101'] = {'inputs': ['ptt_replacement_d2_101'], 'func': ptt_replacement_d3_101}


def ptt_replacement_d3_102(ptt_replacement_d2_102):
    feature = _clean(ptt_replacement_d2_102)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00051000).reindex(feature.index)
PTT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ptt_replacement_d3_102'] = {'inputs': ['ptt_replacement_d2_102'], 'func': ptt_replacement_d3_102}


def ptt_replacement_d3_103(ptt_replacement_d2_103):
    feature = _clean(ptt_replacement_d2_103)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00051500).reindex(feature.index)
PTT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ptt_replacement_d3_103'] = {'inputs': ['ptt_replacement_d2_103'], 'func': ptt_replacement_d3_103}


def ptt_replacement_d3_104(ptt_replacement_d2_104):
    feature = _clean(ptt_replacement_d2_104)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00052000).reindex(feature.index)
PTT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ptt_replacement_d3_104'] = {'inputs': ['ptt_replacement_d2_104'], 'func': ptt_replacement_d3_104}


def ptt_replacement_d3_105(ptt_replacement_d2_105):
    feature = _clean(ptt_replacement_d2_105)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00052500).reindex(feature.index)
PTT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ptt_replacement_d3_105'] = {'inputs': ['ptt_replacement_d2_105'], 'func': ptt_replacement_d3_105}


def ptt_replacement_d3_106(ptt_replacement_d2_106):
    feature = _clean(ptt_replacement_d2_106)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00053000).reindex(feature.index)
PTT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ptt_replacement_d3_106'] = {'inputs': ['ptt_replacement_d2_106'], 'func': ptt_replacement_d3_106}


def ptt_replacement_d3_107(ptt_replacement_d2_107):
    feature = _clean(ptt_replacement_d2_107)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00053500).reindex(feature.index)
PTT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ptt_replacement_d3_107'] = {'inputs': ['ptt_replacement_d2_107'], 'func': ptt_replacement_d3_107}


def ptt_replacement_d3_108(ptt_replacement_d2_108):
    feature = _clean(ptt_replacement_d2_108)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00054000).reindex(feature.index)
PTT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ptt_replacement_d3_108'] = {'inputs': ['ptt_replacement_d2_108'], 'func': ptt_replacement_d3_108}


def ptt_replacement_d3_109(ptt_replacement_d2_109):
    feature = _clean(ptt_replacement_d2_109)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00054500).reindex(feature.index)
PTT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ptt_replacement_d3_109'] = {'inputs': ['ptt_replacement_d2_109'], 'func': ptt_replacement_d3_109}


def ptt_replacement_d3_110(ptt_replacement_d2_110):
    feature = _clean(ptt_replacement_d2_110)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00055000).reindex(feature.index)
PTT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ptt_replacement_d3_110'] = {'inputs': ['ptt_replacement_d2_110'], 'func': ptt_replacement_d3_110}


def ptt_replacement_d3_111(ptt_replacement_d2_111):
    feature = _clean(ptt_replacement_d2_111)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00055500).reindex(feature.index)
PTT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ptt_replacement_d3_111'] = {'inputs': ['ptt_replacement_d2_111'], 'func': ptt_replacement_d3_111}


def ptt_replacement_d3_112(ptt_replacement_d2_112):
    feature = _clean(ptt_replacement_d2_112)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00056000).reindex(feature.index)
PTT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ptt_replacement_d3_112'] = {'inputs': ['ptt_replacement_d2_112'], 'func': ptt_replacement_d3_112}


def ptt_replacement_d3_113(ptt_replacement_d2_113):
    feature = _clean(ptt_replacement_d2_113)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00056500).reindex(feature.index)
PTT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ptt_replacement_d3_113'] = {'inputs': ['ptt_replacement_d2_113'], 'func': ptt_replacement_d3_113}


def ptt_replacement_d3_114(ptt_replacement_d2_114):
    feature = _clean(ptt_replacement_d2_114)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00057000).reindex(feature.index)
PTT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ptt_replacement_d3_114'] = {'inputs': ['ptt_replacement_d2_114'], 'func': ptt_replacement_d3_114}


def ptt_replacement_d3_115(ptt_replacement_d2_115):
    feature = _clean(ptt_replacement_d2_115)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00057500).reindex(feature.index)
PTT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ptt_replacement_d3_115'] = {'inputs': ['ptt_replacement_d2_115'], 'func': ptt_replacement_d3_115}


def ptt_replacement_d3_116(ptt_replacement_d2_116):
    feature = _clean(ptt_replacement_d2_116)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00058000).reindex(feature.index)
PTT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ptt_replacement_d3_116'] = {'inputs': ['ptt_replacement_d2_116'], 'func': ptt_replacement_d3_116}


def ptt_replacement_d3_117(ptt_replacement_d2_117):
    feature = _clean(ptt_replacement_d2_117)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00058500).reindex(feature.index)
PTT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ptt_replacement_d3_117'] = {'inputs': ['ptt_replacement_d2_117'], 'func': ptt_replacement_d3_117}


def ptt_replacement_d3_118(ptt_replacement_d2_118):
    feature = _clean(ptt_replacement_d2_118)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00059000).reindex(feature.index)
PTT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ptt_replacement_d3_118'] = {'inputs': ['ptt_replacement_d2_118'], 'func': ptt_replacement_d3_118}


def ptt_replacement_d3_119(ptt_replacement_d2_119):
    feature = _clean(ptt_replacement_d2_119)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00059500).reindex(feature.index)
PTT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ptt_replacement_d3_119'] = {'inputs': ['ptt_replacement_d2_119'], 'func': ptt_replacement_d3_119}


def ptt_replacement_d3_120(ptt_replacement_d2_120):
    feature = _clean(ptt_replacement_d2_120)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00060000).reindex(feature.index)
PTT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ptt_replacement_d3_120'] = {'inputs': ['ptt_replacement_d2_120'], 'func': ptt_replacement_d3_120}


def ptt_replacement_d3_121(ptt_replacement_d2_121):
    feature = _clean(ptt_replacement_d2_121)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00060500).reindex(feature.index)
PTT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ptt_replacement_d3_121'] = {'inputs': ['ptt_replacement_d2_121'], 'func': ptt_replacement_d3_121}


def ptt_replacement_d3_122(ptt_replacement_d2_122):
    feature = _clean(ptt_replacement_d2_122)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00061000).reindex(feature.index)
PTT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ptt_replacement_d3_122'] = {'inputs': ['ptt_replacement_d2_122'], 'func': ptt_replacement_d3_122}


def ptt_replacement_d3_123(ptt_replacement_d2_123):
    feature = _clean(ptt_replacement_d2_123)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00061500).reindex(feature.index)
PTT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ptt_replacement_d3_123'] = {'inputs': ['ptt_replacement_d2_123'], 'func': ptt_replacement_d3_123}


def ptt_replacement_d3_124(ptt_replacement_d2_124):
    feature = _clean(ptt_replacement_d2_124)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00062000).reindex(feature.index)
PTT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ptt_replacement_d3_124'] = {'inputs': ['ptt_replacement_d2_124'], 'func': ptt_replacement_d3_124}


def ptt_replacement_d3_125(ptt_replacement_d2_125):
    feature = _clean(ptt_replacement_d2_125)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00062500).reindex(feature.index)
PTT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ptt_replacement_d3_125'] = {'inputs': ['ptt_replacement_d2_125'], 'func': ptt_replacement_d3_125}


def ptt_replacement_d3_126(ptt_replacement_d2_126):
    feature = _clean(ptt_replacement_d2_126)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00063000).reindex(feature.index)
PTT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ptt_replacement_d3_126'] = {'inputs': ['ptt_replacement_d2_126'], 'func': ptt_replacement_d3_126}


def ptt_replacement_d3_127(ptt_replacement_d2_127):
    feature = _clean(ptt_replacement_d2_127)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00063500).reindex(feature.index)
PTT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ptt_replacement_d3_127'] = {'inputs': ['ptt_replacement_d2_127'], 'func': ptt_replacement_d3_127}


def ptt_replacement_d3_128(ptt_replacement_d2_128):
    feature = _clean(ptt_replacement_d2_128)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00064000).reindex(feature.index)
PTT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ptt_replacement_d3_128'] = {'inputs': ['ptt_replacement_d2_128'], 'func': ptt_replacement_d3_128}


def ptt_replacement_d3_129(ptt_replacement_d2_129):
    feature = _clean(ptt_replacement_d2_129)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00064500).reindex(feature.index)
PTT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ptt_replacement_d3_129'] = {'inputs': ['ptt_replacement_d2_129'], 'func': ptt_replacement_d3_129}


def ptt_replacement_d3_130(ptt_replacement_d2_130):
    feature = _clean(ptt_replacement_d2_130)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00065000).reindex(feature.index)
PTT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ptt_replacement_d3_130'] = {'inputs': ['ptt_replacement_d2_130'], 'func': ptt_replacement_d3_130}


def ptt_replacement_d3_131(ptt_replacement_d2_131):
    feature = _clean(ptt_replacement_d2_131)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00065500).reindex(feature.index)
PTT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ptt_replacement_d3_131'] = {'inputs': ['ptt_replacement_d2_131'], 'func': ptt_replacement_d3_131}


def ptt_replacement_d3_132(ptt_replacement_d2_132):
    feature = _clean(ptt_replacement_d2_132)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00066000).reindex(feature.index)
PTT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ptt_replacement_d3_132'] = {'inputs': ['ptt_replacement_d2_132'], 'func': ptt_replacement_d3_132}


def ptt_replacement_d3_133(ptt_replacement_d2_133):
    feature = _clean(ptt_replacement_d2_133)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00066500).reindex(feature.index)
PTT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ptt_replacement_d3_133'] = {'inputs': ['ptt_replacement_d2_133'], 'func': ptt_replacement_d3_133}


def ptt_replacement_d3_134(ptt_replacement_d2_134):
    feature = _clean(ptt_replacement_d2_134)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00067000).reindex(feature.index)
PTT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ptt_replacement_d3_134'] = {'inputs': ['ptt_replacement_d2_134'], 'func': ptt_replacement_d3_134}


def ptt_replacement_d3_135(ptt_replacement_d2_135):
    feature = _clean(ptt_replacement_d2_135)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00067500).reindex(feature.index)
PTT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ptt_replacement_d3_135'] = {'inputs': ['ptt_replacement_d2_135'], 'func': ptt_replacement_d3_135}


def ptt_replacement_d3_136(ptt_replacement_d2_136):
    feature = _clean(ptt_replacement_d2_136)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00068000).reindex(feature.index)
PTT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ptt_replacement_d3_136'] = {'inputs': ['ptt_replacement_d2_136'], 'func': ptt_replacement_d3_136}


def ptt_replacement_d3_137(ptt_replacement_d2_137):
    feature = _clean(ptt_replacement_d2_137)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00068500).reindex(feature.index)
PTT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ptt_replacement_d3_137'] = {'inputs': ['ptt_replacement_d2_137'], 'func': ptt_replacement_d3_137}


def ptt_replacement_d3_138(ptt_replacement_d2_138):
    feature = _clean(ptt_replacement_d2_138)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00069000).reindex(feature.index)
PTT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ptt_replacement_d3_138'] = {'inputs': ['ptt_replacement_d2_138'], 'func': ptt_replacement_d3_138}


def ptt_replacement_d3_139(ptt_replacement_d2_139):
    feature = _clean(ptt_replacement_d2_139)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00069500).reindex(feature.index)
PTT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ptt_replacement_d3_139'] = {'inputs': ['ptt_replacement_d2_139'], 'func': ptt_replacement_d3_139}


def ptt_replacement_d3_140(ptt_replacement_d2_140):
    feature = _clean(ptt_replacement_d2_140)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00070000).reindex(feature.index)
PTT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ptt_replacement_d3_140'] = {'inputs': ['ptt_replacement_d2_140'], 'func': ptt_replacement_d3_140}


def ptt_replacement_d3_141(ptt_replacement_d2_141):
    feature = _clean(ptt_replacement_d2_141)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00070500).reindex(feature.index)
PTT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ptt_replacement_d3_141'] = {'inputs': ['ptt_replacement_d2_141'], 'func': ptt_replacement_d3_141}


def ptt_replacement_d3_142(ptt_replacement_d2_142):
    feature = _clean(ptt_replacement_d2_142)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00071000).reindex(feature.index)
PTT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ptt_replacement_d3_142'] = {'inputs': ['ptt_replacement_d2_142'], 'func': ptt_replacement_d3_142}


def ptt_replacement_d3_143(ptt_replacement_d2_143):
    feature = _clean(ptt_replacement_d2_143)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00071500).reindex(feature.index)
PTT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ptt_replacement_d3_143'] = {'inputs': ['ptt_replacement_d2_143'], 'func': ptt_replacement_d3_143}


def ptt_replacement_d3_144(ptt_replacement_d2_144):
    feature = _clean(ptt_replacement_d2_144)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00072000).reindex(feature.index)
PTT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ptt_replacement_d3_144'] = {'inputs': ['ptt_replacement_d2_144'], 'func': ptt_replacement_d3_144}


def ptt_replacement_d3_145(ptt_replacement_d2_145):
    feature = _clean(ptt_replacement_d2_145)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00072500).reindex(feature.index)
PTT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ptt_replacement_d3_145'] = {'inputs': ['ptt_replacement_d2_145'], 'func': ptt_replacement_d3_145}


def ptt_replacement_d3_146(ptt_replacement_d2_146):
    feature = _clean(ptt_replacement_d2_146)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00073000).reindex(feature.index)
PTT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ptt_replacement_d3_146'] = {'inputs': ['ptt_replacement_d2_146'], 'func': ptt_replacement_d3_146}


def ptt_replacement_d3_147(ptt_replacement_d2_147):
    feature = _clean(ptt_replacement_d2_147)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00073500).reindex(feature.index)
PTT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ptt_replacement_d3_147'] = {'inputs': ['ptt_replacement_d2_147'], 'func': ptt_replacement_d3_147}


def ptt_replacement_d3_148(ptt_replacement_d2_148):
    feature = _clean(ptt_replacement_d2_148)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00074000).reindex(feature.index)
PTT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ptt_replacement_d3_148'] = {'inputs': ['ptt_replacement_d2_148'], 'func': ptt_replacement_d3_148}


def ptt_replacement_d3_149(ptt_replacement_d2_149):
    feature = _clean(ptt_replacement_d2_149)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00074500).reindex(feature.index)
PTT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ptt_replacement_d3_149'] = {'inputs': ['ptt_replacement_d2_149'], 'func': ptt_replacement_d3_149}


def ptt_replacement_d3_150(ptt_replacement_d2_150):
    feature = _clean(ptt_replacement_d2_150)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00075000).reindex(feature.index)
PTT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ptt_replacement_d3_150'] = {'inputs': ['ptt_replacement_d2_150'], 'func': ptt_replacement_d3_150}


def ptt_replacement_d3_151(ptt_replacement_d2_151):
    feature = _clean(ptt_replacement_d2_151)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00075500).reindex(feature.index)
PTT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ptt_replacement_d3_151'] = {'inputs': ['ptt_replacement_d2_151'], 'func': ptt_replacement_d3_151}


def ptt_replacement_d3_152(ptt_replacement_d2_152):
    feature = _clean(ptt_replacement_d2_152)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00076000).reindex(feature.index)
PTT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ptt_replacement_d3_152'] = {'inputs': ['ptt_replacement_d2_152'], 'func': ptt_replacement_d3_152}


def ptt_replacement_d3_153(ptt_replacement_d2_153):
    feature = _clean(ptt_replacement_d2_153)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00076500).reindex(feature.index)
PTT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ptt_replacement_d3_153'] = {'inputs': ['ptt_replacement_d2_153'], 'func': ptt_replacement_d3_153}


def ptt_replacement_d3_154(ptt_replacement_d2_154):
    feature = _clean(ptt_replacement_d2_154)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00077000).reindex(feature.index)
PTT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ptt_replacement_d3_154'] = {'inputs': ['ptt_replacement_d2_154'], 'func': ptt_replacement_d3_154}


def ptt_replacement_d3_155(ptt_replacement_d2_155):
    feature = _clean(ptt_replacement_d2_155)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00077500).reindex(feature.index)
PTT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ptt_replacement_d3_155'] = {'inputs': ['ptt_replacement_d2_155'], 'func': ptt_replacement_d3_155}


def ptt_replacement_d3_156(ptt_replacement_d2_156):
    feature = _clean(ptt_replacement_d2_156)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00078000).reindex(feature.index)
PTT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ptt_replacement_d3_156'] = {'inputs': ['ptt_replacement_d2_156'], 'func': ptt_replacement_d3_156}


def ptt_replacement_d3_157(ptt_replacement_d2_157):
    feature = _clean(ptt_replacement_d2_157)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00078500).reindex(feature.index)
PTT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ptt_replacement_d3_157'] = {'inputs': ['ptt_replacement_d2_157'], 'func': ptt_replacement_d3_157}


def ptt_replacement_d3_158(ptt_replacement_d2_158):
    feature = _clean(ptt_replacement_d2_158)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00079000).reindex(feature.index)
PTT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ptt_replacement_d3_158'] = {'inputs': ['ptt_replacement_d2_158'], 'func': ptt_replacement_d3_158}


def ptt_replacement_d3_159(ptt_replacement_d2_159):
    feature = _clean(ptt_replacement_d2_159)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00079500).reindex(feature.index)
PTT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ptt_replacement_d3_159'] = {'inputs': ['ptt_replacement_d2_159'], 'func': ptt_replacement_d3_159}


def ptt_replacement_d3_160(ptt_replacement_d2_160):
    feature = _clean(ptt_replacement_d2_160)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00080000).reindex(feature.index)
PTT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ptt_replacement_d3_160'] = {'inputs': ['ptt_replacement_d2_160'], 'func': ptt_replacement_d3_160}


def ptt_replacement_d3_161(ptt_replacement_d2_161):
    feature = _clean(ptt_replacement_d2_161)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00080500).reindex(feature.index)
PTT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ptt_replacement_d3_161'] = {'inputs': ['ptt_replacement_d2_161'], 'func': ptt_replacement_d3_161}


def ptt_replacement_d3_162(ptt_replacement_d2_162):
    feature = _clean(ptt_replacement_d2_162)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00081000).reindex(feature.index)
PTT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ptt_replacement_d3_162'] = {'inputs': ['ptt_replacement_d2_162'], 'func': ptt_replacement_d3_162}


def ptt_replacement_d3_163(ptt_replacement_d2_163):
    feature = _clean(ptt_replacement_d2_163)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00081500).reindex(feature.index)
PTT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ptt_replacement_d3_163'] = {'inputs': ['ptt_replacement_d2_163'], 'func': ptt_replacement_d3_163}


def ptt_replacement_d3_164(ptt_replacement_d2_164):
    feature = _clean(ptt_replacement_d2_164)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00082000).reindex(feature.index)
PTT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ptt_replacement_d3_164'] = {'inputs': ['ptt_replacement_d2_164'], 'func': ptt_replacement_d3_164}


def ptt_replacement_d3_165(ptt_replacement_d2_165):
    feature = _clean(ptt_replacement_d2_165)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00082500).reindex(feature.index)
PTT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ptt_replacement_d3_165'] = {'inputs': ['ptt_replacement_d2_165'], 'func': ptt_replacement_d3_165}


def ptt_replacement_d3_166(ptt_replacement_d2_166):
    feature = _clean(ptt_replacement_d2_166)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00083000).reindex(feature.index)
PTT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ptt_replacement_d3_166'] = {'inputs': ['ptt_replacement_d2_166'], 'func': ptt_replacement_d3_166}


def ptt_replacement_d3_167(ptt_replacement_d2_167):
    feature = _clean(ptt_replacement_d2_167)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00083500).reindex(feature.index)
PTT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ptt_replacement_d3_167'] = {'inputs': ['ptt_replacement_d2_167'], 'func': ptt_replacement_d3_167}


def ptt_replacement_d3_168(ptt_replacement_d2_168):
    feature = _clean(ptt_replacement_d2_168)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00084000).reindex(feature.index)
PTT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ptt_replacement_d3_168'] = {'inputs': ['ptt_replacement_d2_168'], 'func': ptt_replacement_d3_168}


def ptt_replacement_d3_169(ptt_replacement_d2_169):
    feature = _clean(ptt_replacement_d2_169)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00084500).reindex(feature.index)
PTT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ptt_replacement_d3_169'] = {'inputs': ['ptt_replacement_d2_169'], 'func': ptt_replacement_d3_169}


def ptt_replacement_d3_170(ptt_replacement_d2_170):
    feature = _clean(ptt_replacement_d2_170)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00085000).reindex(feature.index)
PTT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ptt_replacement_d3_170'] = {'inputs': ['ptt_replacement_d2_170'], 'func': ptt_replacement_d3_170}


# Third-derivative extensions for repaired first-base features.
PTT_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY = {}


def _base_universe_d3(feature, idx):
    feature = _clean(feature) if '_clean' in globals() else _s(feature).replace([np.inf, -np.inf], np.nan)
    windows = [1, 2, 3, 5, 8, 13, 21, 34, 55]
    lag = windows[(idx * 2) % len(windows)]
    smooth = windows[(idx * 5 + 2) % len(windows)]
    accel = feature.diff(lag)
    curve = feature - feature.rolling(max(3, smooth), min_periods=2).mean()
    out = accel + curve.fillna(0.0) * (0.00019 * ((idx % 19) + 1))
    return out.replace([np.inf, -np.inf], np.nan).reindex(feature.index)


def ptt_base_universe_d3_001_ptt_002_low_distance_10_002(ptt_base_universe_d2_001_ptt_002_low_distance_10_002):
    return _base_universe_d3(ptt_base_universe_d2_001_ptt_002_low_distance_10_002, 1)
PTT_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ptt_base_universe_d3_001_ptt_002_low_distance_10_002'] = {'inputs': ['ptt_base_universe_d2_001_ptt_002_low_distance_10_002'], 'func': ptt_base_universe_d3_001_ptt_002_low_distance_10_002}


def ptt_base_universe_d3_002_ptt_003_underwater_area_21_003(ptt_base_universe_d2_002_ptt_003_underwater_area_21_003):
    return _base_universe_d3(ptt_base_universe_d2_002_ptt_003_underwater_area_21_003, 2)
PTT_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ptt_base_universe_d3_002_ptt_003_underwater_area_21_003'] = {'inputs': ['ptt_base_universe_d2_002_ptt_003_underwater_area_21_003'], 'func': ptt_base_universe_d3_002_ptt_003_underwater_area_21_003}


def ptt_base_universe_d3_003_ptt_006_lower_high_ratio_84_006(ptt_base_universe_d2_003_ptt_006_lower_high_ratio_84_006):
    return _base_universe_d3(ptt_base_universe_d2_003_ptt_006_lower_high_ratio_84_006, 3)
PTT_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ptt_base_universe_d3_003_ptt_006_lower_high_ratio_84_006'] = {'inputs': ['ptt_base_universe_d2_003_ptt_006_lower_high_ratio_84_006'], 'func': ptt_base_universe_d3_003_ptt_006_lower_high_ratio_84_006}


def ptt_base_universe_d3_004_ptt_008_low_distance_189_008(ptt_base_universe_d2_004_ptt_008_low_distance_189_008):
    return _base_universe_d3(ptt_base_universe_d2_004_ptt_008_low_distance_189_008, 4)
PTT_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ptt_base_universe_d3_004_ptt_008_low_distance_189_008'] = {'inputs': ['ptt_base_universe_d2_004_ptt_008_low_distance_189_008'], 'func': ptt_base_universe_d3_004_ptt_008_low_distance_189_008}


def ptt_base_universe_d3_005_ptt_009_underwater_area_252_009(ptt_base_universe_d2_005_ptt_009_underwater_area_252_009):
    return _base_universe_d3(ptt_base_universe_d2_005_ptt_009_underwater_area_252_009, 5)
PTT_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ptt_base_universe_d3_005_ptt_009_underwater_area_252_009'] = {'inputs': ['ptt_base_universe_d2_005_ptt_009_underwater_area_252_009'], 'func': ptt_base_universe_d3_005_ptt_009_underwater_area_252_009}


def ptt_base_universe_d3_006_ptt_012_lower_high_ratio_756_012(ptt_base_universe_d2_006_ptt_012_lower_high_ratio_756_012):
    return _base_universe_d3(ptt_base_universe_d2_006_ptt_012_lower_high_ratio_756_012, 6)
PTT_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ptt_base_universe_d3_006_ptt_012_lower_high_ratio_756_012'] = {'inputs': ['ptt_base_universe_d2_006_ptt_012_lower_high_ratio_756_012'], 'func': ptt_base_universe_d3_006_ptt_012_lower_high_ratio_756_012}


def ptt_base_universe_d3_007_ptt_014_low_distance_1260_014(ptt_base_universe_d2_007_ptt_014_low_distance_1260_014):
    return _base_universe_d3(ptt_base_universe_d2_007_ptt_014_low_distance_1260_014, 7)
PTT_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ptt_base_universe_d3_007_ptt_014_low_distance_1260_014'] = {'inputs': ['ptt_base_universe_d2_007_ptt_014_low_distance_1260_014'], 'func': ptt_base_universe_d3_007_ptt_014_low_distance_1260_014}


def ptt_base_universe_d3_008_ptt_015_underwater_area_1512_015(ptt_base_universe_d2_008_ptt_015_underwater_area_1512_015):
    return _base_universe_d3(ptt_base_universe_d2_008_ptt_015_underwater_area_1512_015, 8)
PTT_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ptt_base_universe_d3_008_ptt_015_underwater_area_1512_015'] = {'inputs': ['ptt_base_universe_d2_008_ptt_015_underwater_area_1512_015'], 'func': ptt_base_universe_d3_008_ptt_015_underwater_area_1512_015}


def ptt_base_universe_d3_009_ptt_018_lower_high_ratio_21_018(ptt_base_universe_d2_009_ptt_018_lower_high_ratio_21_018):
    return _base_universe_d3(ptt_base_universe_d2_009_ptt_018_lower_high_ratio_21_018, 9)
PTT_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ptt_base_universe_d3_009_ptt_018_lower_high_ratio_21_018'] = {'inputs': ['ptt_base_universe_d2_009_ptt_018_lower_high_ratio_21_018'], 'func': ptt_base_universe_d3_009_ptt_018_lower_high_ratio_21_018}


def ptt_base_universe_d3_010_ptt_020_low_distance_63_020(ptt_base_universe_d2_010_ptt_020_low_distance_63_020):
    return _base_universe_d3(ptt_base_universe_d2_010_ptt_020_low_distance_63_020, 10)
PTT_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ptt_base_universe_d3_010_ptt_020_low_distance_63_020'] = {'inputs': ['ptt_base_universe_d2_010_ptt_020_low_distance_63_020'], 'func': ptt_base_universe_d3_010_ptt_020_low_distance_63_020}


def ptt_base_universe_d3_011_ptt_021_underwater_area_84_021(ptt_base_universe_d2_011_ptt_021_underwater_area_84_021):
    return _base_universe_d3(ptt_base_universe_d2_011_ptt_021_underwater_area_84_021, 11)
PTT_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ptt_base_universe_d3_011_ptt_021_underwater_area_84_021'] = {'inputs': ['ptt_base_universe_d2_011_ptt_021_underwater_area_84_021'], 'func': ptt_base_universe_d3_011_ptt_021_underwater_area_84_021}


def ptt_base_universe_d3_012_ptt_024_lower_high_ratio_252_024(ptt_base_universe_d2_012_ptt_024_lower_high_ratio_252_024):
    return _base_universe_d3(ptt_base_universe_d2_012_ptt_024_lower_high_ratio_252_024, 12)
PTT_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ptt_base_universe_d3_012_ptt_024_lower_high_ratio_252_024'] = {'inputs': ['ptt_base_universe_d2_012_ptt_024_lower_high_ratio_252_024'], 'func': ptt_base_universe_d3_012_ptt_024_lower_high_ratio_252_024}


def ptt_base_universe_d3_013_ptt_026_low_distance_504_026(ptt_base_universe_d2_013_ptt_026_low_distance_504_026):
    return _base_universe_d3(ptt_base_universe_d2_013_ptt_026_low_distance_504_026, 13)
PTT_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ptt_base_universe_d3_013_ptt_026_low_distance_504_026'] = {'inputs': ['ptt_base_universe_d2_013_ptt_026_low_distance_504_026'], 'func': ptt_base_universe_d3_013_ptt_026_low_distance_504_026}


def ptt_base_universe_d3_014_ptt_027_underwater_area_756_027(ptt_base_universe_d2_014_ptt_027_underwater_area_756_027):
    return _base_universe_d3(ptt_base_universe_d2_014_ptt_027_underwater_area_756_027, 14)
PTT_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ptt_base_universe_d3_014_ptt_027_underwater_area_756_027'] = {'inputs': ['ptt_base_universe_d2_014_ptt_027_underwater_area_756_027'], 'func': ptt_base_universe_d3_014_ptt_027_underwater_area_756_027}


def ptt_base_universe_d3_015_ptt_030_lower_high_ratio_1512_030(ptt_base_universe_d2_015_ptt_030_lower_high_ratio_1512_030):
    return _base_universe_d3(ptt_base_universe_d2_015_ptt_030_lower_high_ratio_1512_030, 15)
PTT_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ptt_base_universe_d3_015_ptt_030_lower_high_ratio_1512_030'] = {'inputs': ['ptt_base_universe_d2_015_ptt_030_lower_high_ratio_1512_030'], 'func': ptt_base_universe_d3_015_ptt_030_lower_high_ratio_1512_030}


def ptt_base_universe_d3_016_ptt_basefill_004(ptt_base_universe_d2_016_ptt_basefill_004):
    return _base_universe_d3(ptt_base_universe_d2_016_ptt_basefill_004, 16)
PTT_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ptt_base_universe_d3_016_ptt_basefill_004'] = {'inputs': ['ptt_base_universe_d2_016_ptt_basefill_004'], 'func': ptt_base_universe_d3_016_ptt_basefill_004}


def ptt_base_universe_d3_017_ptt_basefill_005(ptt_base_universe_d2_017_ptt_basefill_005):
    return _base_universe_d3(ptt_base_universe_d2_017_ptt_basefill_005, 17)
PTT_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ptt_base_universe_d3_017_ptt_basefill_005'] = {'inputs': ['ptt_base_universe_d2_017_ptt_basefill_005'], 'func': ptt_base_universe_d3_017_ptt_basefill_005}


def ptt_base_universe_d3_018_ptt_basefill_010(ptt_base_universe_d2_018_ptt_basefill_010):
    return _base_universe_d3(ptt_base_universe_d2_018_ptt_basefill_010, 18)
PTT_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ptt_base_universe_d3_018_ptt_basefill_010'] = {'inputs': ['ptt_base_universe_d2_018_ptt_basefill_010'], 'func': ptt_base_universe_d3_018_ptt_basefill_010}


def ptt_base_universe_d3_019_ptt_basefill_011(ptt_base_universe_d2_019_ptt_basefill_011):
    return _base_universe_d3(ptt_base_universe_d2_019_ptt_basefill_011, 19)
PTT_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ptt_base_universe_d3_019_ptt_basefill_011'] = {'inputs': ['ptt_base_universe_d2_019_ptt_basefill_011'], 'func': ptt_base_universe_d3_019_ptt_basefill_011}


def ptt_base_universe_d3_020_ptt_basefill_016(ptt_base_universe_d2_020_ptt_basefill_016):
    return _base_universe_d3(ptt_base_universe_d2_020_ptt_basefill_016, 20)
PTT_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ptt_base_universe_d3_020_ptt_basefill_016'] = {'inputs': ['ptt_base_universe_d2_020_ptt_basefill_016'], 'func': ptt_base_universe_d3_020_ptt_basefill_016}


def ptt_base_universe_d3_021_ptt_basefill_017(ptt_base_universe_d2_021_ptt_basefill_017):
    return _base_universe_d3(ptt_base_universe_d2_021_ptt_basefill_017, 21)
PTT_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ptt_base_universe_d3_021_ptt_basefill_017'] = {'inputs': ['ptt_base_universe_d2_021_ptt_basefill_017'], 'func': ptt_base_universe_d3_021_ptt_basefill_017}


def ptt_base_universe_d3_022_ptt_basefill_022(ptt_base_universe_d2_022_ptt_basefill_022):
    return _base_universe_d3(ptt_base_universe_d2_022_ptt_basefill_022, 22)
PTT_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ptt_base_universe_d3_022_ptt_basefill_022'] = {'inputs': ['ptt_base_universe_d2_022_ptt_basefill_022'], 'func': ptt_base_universe_d3_022_ptt_basefill_022}


def ptt_base_universe_d3_023_ptt_basefill_023(ptt_base_universe_d2_023_ptt_basefill_023):
    return _base_universe_d3(ptt_base_universe_d2_023_ptt_basefill_023, 23)
PTT_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ptt_base_universe_d3_023_ptt_basefill_023'] = {'inputs': ['ptt_base_universe_d2_023_ptt_basefill_023'], 'func': ptt_base_universe_d3_023_ptt_basefill_023}


def ptt_base_universe_d3_024_ptt_basefill_028(ptt_base_universe_d2_024_ptt_basefill_028):
    return _base_universe_d3(ptt_base_universe_d2_024_ptt_basefill_028, 24)
PTT_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ptt_base_universe_d3_024_ptt_basefill_028'] = {'inputs': ['ptt_base_universe_d2_024_ptt_basefill_028'], 'func': ptt_base_universe_d3_024_ptt_basefill_028}


def ptt_base_universe_d3_025_ptt_basefill_029(ptt_base_universe_d2_025_ptt_basefill_029):
    return _base_universe_d3(ptt_base_universe_d2_025_ptt_basefill_029, 25)
PTT_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ptt_base_universe_d3_025_ptt_basefill_029'] = {'inputs': ['ptt_base_universe_d2_025_ptt_basefill_029'], 'func': ptt_base_universe_d3_025_ptt_basefill_029}


def ptt_base_universe_d3_026_ptt_basefill_031(ptt_base_universe_d2_026_ptt_basefill_031):
    return _base_universe_d3(ptt_base_universe_d2_026_ptt_basefill_031, 26)
PTT_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ptt_base_universe_d3_026_ptt_basefill_031'] = {'inputs': ['ptt_base_universe_d2_026_ptt_basefill_031'], 'func': ptt_base_universe_d3_026_ptt_basefill_031}


def ptt_base_universe_d3_027_ptt_basefill_032(ptt_base_universe_d2_027_ptt_basefill_032):
    return _base_universe_d3(ptt_base_universe_d2_027_ptt_basefill_032, 27)
PTT_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ptt_base_universe_d3_027_ptt_basefill_032'] = {'inputs': ['ptt_base_universe_d2_027_ptt_basefill_032'], 'func': ptt_base_universe_d3_027_ptt_basefill_032}


def ptt_base_universe_d3_028_ptt_basefill_033(ptt_base_universe_d2_028_ptt_basefill_033):
    return _base_universe_d3(ptt_base_universe_d2_028_ptt_basefill_033, 28)
PTT_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ptt_base_universe_d3_028_ptt_basefill_033'] = {'inputs': ['ptt_base_universe_d2_028_ptt_basefill_033'], 'func': ptt_base_universe_d3_028_ptt_basefill_033}


def ptt_base_universe_d3_029_ptt_basefill_034(ptt_base_universe_d2_029_ptt_basefill_034):
    return _base_universe_d3(ptt_base_universe_d2_029_ptt_basefill_034, 29)
PTT_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ptt_base_universe_d3_029_ptt_basefill_034'] = {'inputs': ['ptt_base_universe_d2_029_ptt_basefill_034'], 'func': ptt_base_universe_d3_029_ptt_basefill_034}


def ptt_base_universe_d3_030_ptt_basefill_035(ptt_base_universe_d2_030_ptt_basefill_035):
    return _base_universe_d3(ptt_base_universe_d2_030_ptt_basefill_035, 30)
PTT_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ptt_base_universe_d3_030_ptt_basefill_035'] = {'inputs': ['ptt_base_universe_d2_030_ptt_basefill_035'], 'func': ptt_base_universe_d3_030_ptt_basefill_035}


def ptt_base_universe_d3_031_ptt_basefill_036(ptt_base_universe_d2_031_ptt_basefill_036):
    return _base_universe_d3(ptt_base_universe_d2_031_ptt_basefill_036, 31)
PTT_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ptt_base_universe_d3_031_ptt_basefill_036'] = {'inputs': ['ptt_base_universe_d2_031_ptt_basefill_036'], 'func': ptt_base_universe_d3_031_ptt_basefill_036}


def ptt_base_universe_d3_032_ptt_basefill_037(ptt_base_universe_d2_032_ptt_basefill_037):
    return _base_universe_d3(ptt_base_universe_d2_032_ptt_basefill_037, 32)
PTT_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ptt_base_universe_d3_032_ptt_basefill_037'] = {'inputs': ['ptt_base_universe_d2_032_ptt_basefill_037'], 'func': ptt_base_universe_d3_032_ptt_basefill_037}


def ptt_base_universe_d3_033_ptt_basefill_038(ptt_base_universe_d2_033_ptt_basefill_038):
    return _base_universe_d3(ptt_base_universe_d2_033_ptt_basefill_038, 33)
PTT_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ptt_base_universe_d3_033_ptt_basefill_038'] = {'inputs': ['ptt_base_universe_d2_033_ptt_basefill_038'], 'func': ptt_base_universe_d3_033_ptt_basefill_038}


def ptt_base_universe_d3_034_ptt_basefill_039(ptt_base_universe_d2_034_ptt_basefill_039):
    return _base_universe_d3(ptt_base_universe_d2_034_ptt_basefill_039, 34)
PTT_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ptt_base_universe_d3_034_ptt_basefill_039'] = {'inputs': ['ptt_base_universe_d2_034_ptt_basefill_039'], 'func': ptt_base_universe_d3_034_ptt_basefill_039}


def ptt_base_universe_d3_035_ptt_basefill_040(ptt_base_universe_d2_035_ptt_basefill_040):
    return _base_universe_d3(ptt_base_universe_d2_035_ptt_basefill_040, 35)
PTT_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ptt_base_universe_d3_035_ptt_basefill_040'] = {'inputs': ['ptt_base_universe_d2_035_ptt_basefill_040'], 'func': ptt_base_universe_d3_035_ptt_basefill_040}


def ptt_base_universe_d3_036_ptt_basefill_041(ptt_base_universe_d2_036_ptt_basefill_041):
    return _base_universe_d3(ptt_base_universe_d2_036_ptt_basefill_041, 36)
PTT_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ptt_base_universe_d3_036_ptt_basefill_041'] = {'inputs': ['ptt_base_universe_d2_036_ptt_basefill_041'], 'func': ptt_base_universe_d3_036_ptt_basefill_041}


def ptt_base_universe_d3_037_ptt_basefill_042(ptt_base_universe_d2_037_ptt_basefill_042):
    return _base_universe_d3(ptt_base_universe_d2_037_ptt_basefill_042, 37)
PTT_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ptt_base_universe_d3_037_ptt_basefill_042'] = {'inputs': ['ptt_base_universe_d2_037_ptt_basefill_042'], 'func': ptt_base_universe_d3_037_ptt_basefill_042}


def ptt_base_universe_d3_038_ptt_basefill_043(ptt_base_universe_d2_038_ptt_basefill_043):
    return _base_universe_d3(ptt_base_universe_d2_038_ptt_basefill_043, 38)
PTT_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ptt_base_universe_d3_038_ptt_basefill_043'] = {'inputs': ['ptt_base_universe_d2_038_ptt_basefill_043'], 'func': ptt_base_universe_d3_038_ptt_basefill_043}


def ptt_base_universe_d3_039_ptt_basefill_044(ptt_base_universe_d2_039_ptt_basefill_044):
    return _base_universe_d3(ptt_base_universe_d2_039_ptt_basefill_044, 39)
PTT_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ptt_base_universe_d3_039_ptt_basefill_044'] = {'inputs': ['ptt_base_universe_d2_039_ptt_basefill_044'], 'func': ptt_base_universe_d3_039_ptt_basefill_044}


def ptt_base_universe_d3_040_ptt_basefill_045(ptt_base_universe_d2_040_ptt_basefill_045):
    return _base_universe_d3(ptt_base_universe_d2_040_ptt_basefill_045, 40)
PTT_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ptt_base_universe_d3_040_ptt_basefill_045'] = {'inputs': ['ptt_base_universe_d2_040_ptt_basefill_045'], 'func': ptt_base_universe_d3_040_ptt_basefill_045}


def ptt_base_universe_d3_041_ptt_basefill_046(ptt_base_universe_d2_041_ptt_basefill_046):
    return _base_universe_d3(ptt_base_universe_d2_041_ptt_basefill_046, 41)
PTT_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ptt_base_universe_d3_041_ptt_basefill_046'] = {'inputs': ['ptt_base_universe_d2_041_ptt_basefill_046'], 'func': ptt_base_universe_d3_041_ptt_basefill_046}


def ptt_base_universe_d3_042_ptt_basefill_047(ptt_base_universe_d2_042_ptt_basefill_047):
    return _base_universe_d3(ptt_base_universe_d2_042_ptt_basefill_047, 42)
PTT_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ptt_base_universe_d3_042_ptt_basefill_047'] = {'inputs': ['ptt_base_universe_d2_042_ptt_basefill_047'], 'func': ptt_base_universe_d3_042_ptt_basefill_047}


def ptt_base_universe_d3_043_ptt_basefill_048(ptt_base_universe_d2_043_ptt_basefill_048):
    return _base_universe_d3(ptt_base_universe_d2_043_ptt_basefill_048, 43)
PTT_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ptt_base_universe_d3_043_ptt_basefill_048'] = {'inputs': ['ptt_base_universe_d2_043_ptt_basefill_048'], 'func': ptt_base_universe_d3_043_ptt_basefill_048}


def ptt_base_universe_d3_044_ptt_basefill_049(ptt_base_universe_d2_044_ptt_basefill_049):
    return _base_universe_d3(ptt_base_universe_d2_044_ptt_basefill_049, 44)
PTT_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ptt_base_universe_d3_044_ptt_basefill_049'] = {'inputs': ['ptt_base_universe_d2_044_ptt_basefill_049'], 'func': ptt_base_universe_d3_044_ptt_basefill_049}


def ptt_base_universe_d3_045_ptt_basefill_050(ptt_base_universe_d2_045_ptt_basefill_050):
    return _base_universe_d3(ptt_base_universe_d2_045_ptt_basefill_050, 45)
PTT_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ptt_base_universe_d3_045_ptt_basefill_050'] = {'inputs': ['ptt_base_universe_d2_045_ptt_basefill_050'], 'func': ptt_base_universe_d3_045_ptt_basefill_050}


def ptt_base_universe_d3_046_ptt_basefill_051(ptt_base_universe_d2_046_ptt_basefill_051):
    return _base_universe_d3(ptt_base_universe_d2_046_ptt_basefill_051, 46)
PTT_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ptt_base_universe_d3_046_ptt_basefill_051'] = {'inputs': ['ptt_base_universe_d2_046_ptt_basefill_051'], 'func': ptt_base_universe_d3_046_ptt_basefill_051}


def ptt_base_universe_d3_047_ptt_basefill_052(ptt_base_universe_d2_047_ptt_basefill_052):
    return _base_universe_d3(ptt_base_universe_d2_047_ptt_basefill_052, 47)
PTT_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ptt_base_universe_d3_047_ptt_basefill_052'] = {'inputs': ['ptt_base_universe_d2_047_ptt_basefill_052'], 'func': ptt_base_universe_d3_047_ptt_basefill_052}


def ptt_base_universe_d3_048_ptt_basefill_053(ptt_base_universe_d2_048_ptt_basefill_053):
    return _base_universe_d3(ptt_base_universe_d2_048_ptt_basefill_053, 48)
PTT_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ptt_base_universe_d3_048_ptt_basefill_053'] = {'inputs': ['ptt_base_universe_d2_048_ptt_basefill_053'], 'func': ptt_base_universe_d3_048_ptt_basefill_053}


def ptt_base_universe_d3_049_ptt_basefill_054(ptt_base_universe_d2_049_ptt_basefill_054):
    return _base_universe_d3(ptt_base_universe_d2_049_ptt_basefill_054, 49)
PTT_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ptt_base_universe_d3_049_ptt_basefill_054'] = {'inputs': ['ptt_base_universe_d2_049_ptt_basefill_054'], 'func': ptt_base_universe_d3_049_ptt_basefill_054}


def ptt_base_universe_d3_050_ptt_basefill_055(ptt_base_universe_d2_050_ptt_basefill_055):
    return _base_universe_d3(ptt_base_universe_d2_050_ptt_basefill_055, 50)
PTT_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ptt_base_universe_d3_050_ptt_basefill_055'] = {'inputs': ['ptt_base_universe_d2_050_ptt_basefill_055'], 'func': ptt_base_universe_d3_050_ptt_basefill_055}


def ptt_base_universe_d3_051_ptt_basefill_056(ptt_base_universe_d2_051_ptt_basefill_056):
    return _base_universe_d3(ptt_base_universe_d2_051_ptt_basefill_056, 51)
PTT_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ptt_base_universe_d3_051_ptt_basefill_056'] = {'inputs': ['ptt_base_universe_d2_051_ptt_basefill_056'], 'func': ptt_base_universe_d3_051_ptt_basefill_056}


def ptt_base_universe_d3_052_ptt_basefill_057(ptt_base_universe_d2_052_ptt_basefill_057):
    return _base_universe_d3(ptt_base_universe_d2_052_ptt_basefill_057, 52)
PTT_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ptt_base_universe_d3_052_ptt_basefill_057'] = {'inputs': ['ptt_base_universe_d2_052_ptt_basefill_057'], 'func': ptt_base_universe_d3_052_ptt_basefill_057}


def ptt_base_universe_d3_053_ptt_basefill_058(ptt_base_universe_d2_053_ptt_basefill_058):
    return _base_universe_d3(ptt_base_universe_d2_053_ptt_basefill_058, 53)
PTT_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ptt_base_universe_d3_053_ptt_basefill_058'] = {'inputs': ['ptt_base_universe_d2_053_ptt_basefill_058'], 'func': ptt_base_universe_d3_053_ptt_basefill_058}


def ptt_base_universe_d3_054_ptt_basefill_059(ptt_base_universe_d2_054_ptt_basefill_059):
    return _base_universe_d3(ptt_base_universe_d2_054_ptt_basefill_059, 54)
PTT_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ptt_base_universe_d3_054_ptt_basefill_059'] = {'inputs': ['ptt_base_universe_d2_054_ptt_basefill_059'], 'func': ptt_base_universe_d3_054_ptt_basefill_059}


def ptt_base_universe_d3_055_ptt_basefill_060(ptt_base_universe_d2_055_ptt_basefill_060):
    return _base_universe_d3(ptt_base_universe_d2_055_ptt_basefill_060, 55)
PTT_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ptt_base_universe_d3_055_ptt_basefill_060'] = {'inputs': ['ptt_base_universe_d2_055_ptt_basefill_060'], 'func': ptt_base_universe_d3_055_ptt_basefill_060}


def ptt_base_universe_d3_056_ptt_basefill_061(ptt_base_universe_d2_056_ptt_basefill_061):
    return _base_universe_d3(ptt_base_universe_d2_056_ptt_basefill_061, 56)
PTT_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ptt_base_universe_d3_056_ptt_basefill_061'] = {'inputs': ['ptt_base_universe_d2_056_ptt_basefill_061'], 'func': ptt_base_universe_d3_056_ptt_basefill_061}


def ptt_base_universe_d3_057_ptt_basefill_062(ptt_base_universe_d2_057_ptt_basefill_062):
    return _base_universe_d3(ptt_base_universe_d2_057_ptt_basefill_062, 57)
PTT_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ptt_base_universe_d3_057_ptt_basefill_062'] = {'inputs': ['ptt_base_universe_d2_057_ptt_basefill_062'], 'func': ptt_base_universe_d3_057_ptt_basefill_062}


def ptt_base_universe_d3_058_ptt_basefill_063(ptt_base_universe_d2_058_ptt_basefill_063):
    return _base_universe_d3(ptt_base_universe_d2_058_ptt_basefill_063, 58)
PTT_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ptt_base_universe_d3_058_ptt_basefill_063'] = {'inputs': ['ptt_base_universe_d2_058_ptt_basefill_063'], 'func': ptt_base_universe_d3_058_ptt_basefill_063}


def ptt_base_universe_d3_059_ptt_basefill_064(ptt_base_universe_d2_059_ptt_basefill_064):
    return _base_universe_d3(ptt_base_universe_d2_059_ptt_basefill_064, 59)
PTT_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ptt_base_universe_d3_059_ptt_basefill_064'] = {'inputs': ['ptt_base_universe_d2_059_ptt_basefill_064'], 'func': ptt_base_universe_d3_059_ptt_basefill_064}


def ptt_base_universe_d3_060_ptt_basefill_065(ptt_base_universe_d2_060_ptt_basefill_065):
    return _base_universe_d3(ptt_base_universe_d2_060_ptt_basefill_065, 60)
PTT_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ptt_base_universe_d3_060_ptt_basefill_065'] = {'inputs': ['ptt_base_universe_d2_060_ptt_basefill_065'], 'func': ptt_base_universe_d3_060_ptt_basefill_065}


def ptt_base_universe_d3_061_ptt_basefill_066(ptt_base_universe_d2_061_ptt_basefill_066):
    return _base_universe_d3(ptt_base_universe_d2_061_ptt_basefill_066, 61)
PTT_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ptt_base_universe_d3_061_ptt_basefill_066'] = {'inputs': ['ptt_base_universe_d2_061_ptt_basefill_066'], 'func': ptt_base_universe_d3_061_ptt_basefill_066}


def ptt_base_universe_d3_062_ptt_basefill_067(ptt_base_universe_d2_062_ptt_basefill_067):
    return _base_universe_d3(ptt_base_universe_d2_062_ptt_basefill_067, 62)
PTT_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ptt_base_universe_d3_062_ptt_basefill_067'] = {'inputs': ['ptt_base_universe_d2_062_ptt_basefill_067'], 'func': ptt_base_universe_d3_062_ptt_basefill_067}


def ptt_base_universe_d3_063_ptt_basefill_068(ptt_base_universe_d2_063_ptt_basefill_068):
    return _base_universe_d3(ptt_base_universe_d2_063_ptt_basefill_068, 63)
PTT_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ptt_base_universe_d3_063_ptt_basefill_068'] = {'inputs': ['ptt_base_universe_d2_063_ptt_basefill_068'], 'func': ptt_base_universe_d3_063_ptt_basefill_068}


def ptt_base_universe_d3_064_ptt_basefill_069(ptt_base_universe_d2_064_ptt_basefill_069):
    return _base_universe_d3(ptt_base_universe_d2_064_ptt_basefill_069, 64)
PTT_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ptt_base_universe_d3_064_ptt_basefill_069'] = {'inputs': ['ptt_base_universe_d2_064_ptt_basefill_069'], 'func': ptt_base_universe_d3_064_ptt_basefill_069}


def ptt_base_universe_d3_065_ptt_basefill_070(ptt_base_universe_d2_065_ptt_basefill_070):
    return _base_universe_d3(ptt_base_universe_d2_065_ptt_basefill_070, 65)
PTT_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ptt_base_universe_d3_065_ptt_basefill_070'] = {'inputs': ['ptt_base_universe_d2_065_ptt_basefill_070'], 'func': ptt_base_universe_d3_065_ptt_basefill_070}


def ptt_base_universe_d3_066_ptt_basefill_071(ptt_base_universe_d2_066_ptt_basefill_071):
    return _base_universe_d3(ptt_base_universe_d2_066_ptt_basefill_071, 66)
PTT_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ptt_base_universe_d3_066_ptt_basefill_071'] = {'inputs': ['ptt_base_universe_d2_066_ptt_basefill_071'], 'func': ptt_base_universe_d3_066_ptt_basefill_071}


def ptt_base_universe_d3_067_ptt_basefill_072(ptt_base_universe_d2_067_ptt_basefill_072):
    return _base_universe_d3(ptt_base_universe_d2_067_ptt_basefill_072, 67)
PTT_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ptt_base_universe_d3_067_ptt_basefill_072'] = {'inputs': ['ptt_base_universe_d2_067_ptt_basefill_072'], 'func': ptt_base_universe_d3_067_ptt_basefill_072}


def ptt_base_universe_d3_068_ptt_basefill_073(ptt_base_universe_d2_068_ptt_basefill_073):
    return _base_universe_d3(ptt_base_universe_d2_068_ptt_basefill_073, 68)
PTT_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ptt_base_universe_d3_068_ptt_basefill_073'] = {'inputs': ['ptt_base_universe_d2_068_ptt_basefill_073'], 'func': ptt_base_universe_d3_068_ptt_basefill_073}


def ptt_base_universe_d3_069_ptt_basefill_074(ptt_base_universe_d2_069_ptt_basefill_074):
    return _base_universe_d3(ptt_base_universe_d2_069_ptt_basefill_074, 69)
PTT_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ptt_base_universe_d3_069_ptt_basefill_074'] = {'inputs': ['ptt_base_universe_d2_069_ptt_basefill_074'], 'func': ptt_base_universe_d3_069_ptt_basefill_074}


def ptt_base_universe_d3_070_ptt_basefill_075(ptt_base_universe_d2_070_ptt_basefill_075):
    return _base_universe_d3(ptt_base_universe_d2_070_ptt_basefill_075, 70)
PTT_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ptt_base_universe_d3_070_ptt_basefill_075'] = {'inputs': ['ptt_base_universe_d2_070_ptt_basefill_075'], 'func': ptt_base_universe_d3_070_ptt_basefill_075}
