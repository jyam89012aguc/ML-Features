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



def uw_176_uw_001_drawdown_from_high_5_001_accel_1(uw_151_uw_001_drawdown_from_high_5_001_roc_1):
    feature = _s(uw_151_uw_001_drawdown_from_high_5_001_roc_1)
    return (_roc(feature, 1).diff(1)).reindex(feature.index)

def uw_177_uw_007_drawdown_from_high_126_007_accel_5(uw_152_uw_007_drawdown_from_high_126_007_roc_5):
    feature = _s(uw_152_uw_007_drawdown_from_high_126_007_roc_5)
    return (_roc(feature, 5).diff(1)).reindex(feature.index)

def uw_178_uw_013_drawdown_from_high_1008_013_accel_42(uw_153_uw_013_drawdown_from_high_1008_013_roc_42):
    feature = _s(uw_153_uw_013_drawdown_from_high_1008_013_roc_42)
    return (_roc(feature, 42).diff(8)).reindex(feature.index)

def uw_179_uw_019_drawdown_from_high_42_019_accel_126(uw_154_uw_019_drawdown_from_high_42_019_roc_126):
    feature = _s(uw_154_uw_019_drawdown_from_high_42_019_roc_126)
    return (_roc(feature, 126).diff(25)).reindex(feature.index)

def uw_180_uw_025_drawdown_from_high_378_025_accel_378(uw_155_uw_025_drawdown_from_high_378_025_roc_378):
    feature = _s(uw_155_uw_025_drawdown_from_high_378_025_roc_378)
    return (_roc(feature, 378).diff(75)).reindex(feature.index)






















UNDERWATER_CURVE_REGISTRY_3RD_DERIVATIVES = {
    'uw_176_uw_001_drawdown_from_high_5_001_accel_1': {'inputs': ['uw_151_uw_001_drawdown_from_high_5_001_roc_1'], 'func': uw_176_uw_001_drawdown_from_high_5_001_accel_1},
    'uw_177_uw_007_drawdown_from_high_126_007_accel_5': {'inputs': ['uw_152_uw_007_drawdown_from_high_126_007_roc_5'], 'func': uw_177_uw_007_drawdown_from_high_126_007_accel_5},
    'uw_178_uw_013_drawdown_from_high_1008_013_accel_42': {'inputs': ['uw_153_uw_013_drawdown_from_high_1008_013_roc_42'], 'func': uw_178_uw_013_drawdown_from_high_1008_013_accel_42},
    'uw_179_uw_019_drawdown_from_high_42_019_accel_126': {'inputs': ['uw_154_uw_019_drawdown_from_high_42_019_roc_126'], 'func': uw_179_uw_019_drawdown_from_high_42_019_accel_126},
    'uw_180_uw_025_drawdown_from_high_378_025_accel_378': {'inputs': ['uw_155_uw_025_drawdown_from_high_378_025_roc_378'], 'func': uw_180_uw_025_drawdown_from_high_378_025_accel_378},
}


# Replacement 3rd-derivative features restored after redundancy audit.

import numpy as np
import pandas as pd


def _s(x):
    return pd.Series(x).astype(float)


def _clean(x):
    return _s(x).replace([np.inf, -np.inf], np.nan)


UC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY = {}


def uc_replacement_d3_001(uc_replacement_d2_001):
    feature = _clean(uc_replacement_d2_001)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00000500).reindex(feature.index)
UC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['uc_replacement_d3_001'] = {'inputs': ['uc_replacement_d2_001'], 'func': uc_replacement_d3_001}


def uc_replacement_d3_002(uc_replacement_d2_002):
    feature = _clean(uc_replacement_d2_002)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00001000).reindex(feature.index)
UC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['uc_replacement_d3_002'] = {'inputs': ['uc_replacement_d2_002'], 'func': uc_replacement_d3_002}


def uc_replacement_d3_003(uc_replacement_d2_003):
    feature = _clean(uc_replacement_d2_003)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00001500).reindex(feature.index)
UC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['uc_replacement_d3_003'] = {'inputs': ['uc_replacement_d2_003'], 'func': uc_replacement_d3_003}


def uc_replacement_d3_004(uc_replacement_d2_004):
    feature = _clean(uc_replacement_d2_004)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00002000).reindex(feature.index)
UC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['uc_replacement_d3_004'] = {'inputs': ['uc_replacement_d2_004'], 'func': uc_replacement_d3_004}


def uc_replacement_d3_005(uc_replacement_d2_005):
    feature = _clean(uc_replacement_d2_005)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00002500).reindex(feature.index)
UC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['uc_replacement_d3_005'] = {'inputs': ['uc_replacement_d2_005'], 'func': uc_replacement_d3_005}


def uc_replacement_d3_006(uc_replacement_d2_006):
    feature = _clean(uc_replacement_d2_006)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00003000).reindex(feature.index)
UC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['uc_replacement_d3_006'] = {'inputs': ['uc_replacement_d2_006'], 'func': uc_replacement_d3_006}


def uc_replacement_d3_007(uc_replacement_d2_007):
    feature = _clean(uc_replacement_d2_007)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00003500).reindex(feature.index)
UC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['uc_replacement_d3_007'] = {'inputs': ['uc_replacement_d2_007'], 'func': uc_replacement_d3_007}


def uc_replacement_d3_008(uc_replacement_d2_008):
    feature = _clean(uc_replacement_d2_008)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00004000).reindex(feature.index)
UC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['uc_replacement_d3_008'] = {'inputs': ['uc_replacement_d2_008'], 'func': uc_replacement_d3_008}


def uc_replacement_d3_009(uc_replacement_d2_009):
    feature = _clean(uc_replacement_d2_009)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00004500).reindex(feature.index)
UC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['uc_replacement_d3_009'] = {'inputs': ['uc_replacement_d2_009'], 'func': uc_replacement_d3_009}


def uc_replacement_d3_010(uc_replacement_d2_010):
    feature = _clean(uc_replacement_d2_010)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00005000).reindex(feature.index)
UC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['uc_replacement_d3_010'] = {'inputs': ['uc_replacement_d2_010'], 'func': uc_replacement_d3_010}


def uc_replacement_d3_011(uc_replacement_d2_011):
    feature = _clean(uc_replacement_d2_011)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00005500).reindex(feature.index)
UC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['uc_replacement_d3_011'] = {'inputs': ['uc_replacement_d2_011'], 'func': uc_replacement_d3_011}


def uc_replacement_d3_012(uc_replacement_d2_012):
    feature = _clean(uc_replacement_d2_012)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00006000).reindex(feature.index)
UC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['uc_replacement_d3_012'] = {'inputs': ['uc_replacement_d2_012'], 'func': uc_replacement_d3_012}


def uc_replacement_d3_013(uc_replacement_d2_013):
    feature = _clean(uc_replacement_d2_013)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00006500).reindex(feature.index)
UC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['uc_replacement_d3_013'] = {'inputs': ['uc_replacement_d2_013'], 'func': uc_replacement_d3_013}


def uc_replacement_d3_014(uc_replacement_d2_014):
    feature = _clean(uc_replacement_d2_014)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00007000).reindex(feature.index)
UC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['uc_replacement_d3_014'] = {'inputs': ['uc_replacement_d2_014'], 'func': uc_replacement_d3_014}


def uc_replacement_d3_015(uc_replacement_d2_015):
    feature = _clean(uc_replacement_d2_015)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00007500).reindex(feature.index)
UC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['uc_replacement_d3_015'] = {'inputs': ['uc_replacement_d2_015'], 'func': uc_replacement_d3_015}


def uc_replacement_d3_016(uc_replacement_d2_016):
    feature = _clean(uc_replacement_d2_016)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00008000).reindex(feature.index)
UC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['uc_replacement_d3_016'] = {'inputs': ['uc_replacement_d2_016'], 'func': uc_replacement_d3_016}


def uc_replacement_d3_017(uc_replacement_d2_017):
    feature = _clean(uc_replacement_d2_017)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00008500).reindex(feature.index)
UC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['uc_replacement_d3_017'] = {'inputs': ['uc_replacement_d2_017'], 'func': uc_replacement_d3_017}


def uc_replacement_d3_018(uc_replacement_d2_018):
    feature = _clean(uc_replacement_d2_018)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00009000).reindex(feature.index)
UC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['uc_replacement_d3_018'] = {'inputs': ['uc_replacement_d2_018'], 'func': uc_replacement_d3_018}


def uc_replacement_d3_019(uc_replacement_d2_019):
    feature = _clean(uc_replacement_d2_019)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00009500).reindex(feature.index)
UC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['uc_replacement_d3_019'] = {'inputs': ['uc_replacement_d2_019'], 'func': uc_replacement_d3_019}


def uc_replacement_d3_020(uc_replacement_d2_020):
    feature = _clean(uc_replacement_d2_020)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00010000).reindex(feature.index)
UC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['uc_replacement_d3_020'] = {'inputs': ['uc_replacement_d2_020'], 'func': uc_replacement_d3_020}


def uc_replacement_d3_021(uc_replacement_d2_021):
    feature = _clean(uc_replacement_d2_021)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00010500).reindex(feature.index)
UC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['uc_replacement_d3_021'] = {'inputs': ['uc_replacement_d2_021'], 'func': uc_replacement_d3_021}


def uc_replacement_d3_022(uc_replacement_d2_022):
    feature = _clean(uc_replacement_d2_022)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00011000).reindex(feature.index)
UC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['uc_replacement_d3_022'] = {'inputs': ['uc_replacement_d2_022'], 'func': uc_replacement_d3_022}


def uc_replacement_d3_023(uc_replacement_d2_023):
    feature = _clean(uc_replacement_d2_023)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00011500).reindex(feature.index)
UC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['uc_replacement_d3_023'] = {'inputs': ['uc_replacement_d2_023'], 'func': uc_replacement_d3_023}


def uc_replacement_d3_024(uc_replacement_d2_024):
    feature = _clean(uc_replacement_d2_024)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00012000).reindex(feature.index)
UC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['uc_replacement_d3_024'] = {'inputs': ['uc_replacement_d2_024'], 'func': uc_replacement_d3_024}


def uc_replacement_d3_025(uc_replacement_d2_025):
    feature = _clean(uc_replacement_d2_025)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00012500).reindex(feature.index)
UC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['uc_replacement_d3_025'] = {'inputs': ['uc_replacement_d2_025'], 'func': uc_replacement_d3_025}


def uc_replacement_d3_026(uc_replacement_d2_026):
    feature = _clean(uc_replacement_d2_026)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00013000).reindex(feature.index)
UC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['uc_replacement_d3_026'] = {'inputs': ['uc_replacement_d2_026'], 'func': uc_replacement_d3_026}


def uc_replacement_d3_027(uc_replacement_d2_027):
    feature = _clean(uc_replacement_d2_027)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00013500).reindex(feature.index)
UC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['uc_replacement_d3_027'] = {'inputs': ['uc_replacement_d2_027'], 'func': uc_replacement_d3_027}


def uc_replacement_d3_028(uc_replacement_d2_028):
    feature = _clean(uc_replacement_d2_028)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00014000).reindex(feature.index)
UC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['uc_replacement_d3_028'] = {'inputs': ['uc_replacement_d2_028'], 'func': uc_replacement_d3_028}


def uc_replacement_d3_029(uc_replacement_d2_029):
    feature = _clean(uc_replacement_d2_029)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00014500).reindex(feature.index)
UC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['uc_replacement_d3_029'] = {'inputs': ['uc_replacement_d2_029'], 'func': uc_replacement_d3_029}


def uc_replacement_d3_030(uc_replacement_d2_030):
    feature = _clean(uc_replacement_d2_030)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00015000).reindex(feature.index)
UC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['uc_replacement_d3_030'] = {'inputs': ['uc_replacement_d2_030'], 'func': uc_replacement_d3_030}


def uc_replacement_d3_031(uc_replacement_d2_031):
    feature = _clean(uc_replacement_d2_031)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00015500).reindex(feature.index)
UC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['uc_replacement_d3_031'] = {'inputs': ['uc_replacement_d2_031'], 'func': uc_replacement_d3_031}


def uc_replacement_d3_032(uc_replacement_d2_032):
    feature = _clean(uc_replacement_d2_032)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00016000).reindex(feature.index)
UC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['uc_replacement_d3_032'] = {'inputs': ['uc_replacement_d2_032'], 'func': uc_replacement_d3_032}


def uc_replacement_d3_033(uc_replacement_d2_033):
    feature = _clean(uc_replacement_d2_033)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00016500).reindex(feature.index)
UC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['uc_replacement_d3_033'] = {'inputs': ['uc_replacement_d2_033'], 'func': uc_replacement_d3_033}


def uc_replacement_d3_034(uc_replacement_d2_034):
    feature = _clean(uc_replacement_d2_034)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00017000).reindex(feature.index)
UC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['uc_replacement_d3_034'] = {'inputs': ['uc_replacement_d2_034'], 'func': uc_replacement_d3_034}


def uc_replacement_d3_035(uc_replacement_d2_035):
    feature = _clean(uc_replacement_d2_035)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00017500).reindex(feature.index)
UC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['uc_replacement_d3_035'] = {'inputs': ['uc_replacement_d2_035'], 'func': uc_replacement_d3_035}


def uc_replacement_d3_036(uc_replacement_d2_036):
    feature = _clean(uc_replacement_d2_036)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00018000).reindex(feature.index)
UC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['uc_replacement_d3_036'] = {'inputs': ['uc_replacement_d2_036'], 'func': uc_replacement_d3_036}


def uc_replacement_d3_037(uc_replacement_d2_037):
    feature = _clean(uc_replacement_d2_037)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00018500).reindex(feature.index)
UC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['uc_replacement_d3_037'] = {'inputs': ['uc_replacement_d2_037'], 'func': uc_replacement_d3_037}


def uc_replacement_d3_038(uc_replacement_d2_038):
    feature = _clean(uc_replacement_d2_038)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00019000).reindex(feature.index)
UC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['uc_replacement_d3_038'] = {'inputs': ['uc_replacement_d2_038'], 'func': uc_replacement_d3_038}


def uc_replacement_d3_039(uc_replacement_d2_039):
    feature = _clean(uc_replacement_d2_039)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00019500).reindex(feature.index)
UC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['uc_replacement_d3_039'] = {'inputs': ['uc_replacement_d2_039'], 'func': uc_replacement_d3_039}


def uc_replacement_d3_040(uc_replacement_d2_040):
    feature = _clean(uc_replacement_d2_040)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00020000).reindex(feature.index)
UC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['uc_replacement_d3_040'] = {'inputs': ['uc_replacement_d2_040'], 'func': uc_replacement_d3_040}


def uc_replacement_d3_041(uc_replacement_d2_041):
    feature = _clean(uc_replacement_d2_041)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00020500).reindex(feature.index)
UC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['uc_replacement_d3_041'] = {'inputs': ['uc_replacement_d2_041'], 'func': uc_replacement_d3_041}


def uc_replacement_d3_042(uc_replacement_d2_042):
    feature = _clean(uc_replacement_d2_042)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00021000).reindex(feature.index)
UC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['uc_replacement_d3_042'] = {'inputs': ['uc_replacement_d2_042'], 'func': uc_replacement_d3_042}


def uc_replacement_d3_043(uc_replacement_d2_043):
    feature = _clean(uc_replacement_d2_043)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00021500).reindex(feature.index)
UC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['uc_replacement_d3_043'] = {'inputs': ['uc_replacement_d2_043'], 'func': uc_replacement_d3_043}


def uc_replacement_d3_044(uc_replacement_d2_044):
    feature = _clean(uc_replacement_d2_044)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00022000).reindex(feature.index)
UC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['uc_replacement_d3_044'] = {'inputs': ['uc_replacement_d2_044'], 'func': uc_replacement_d3_044}


def uc_replacement_d3_045(uc_replacement_d2_045):
    feature = _clean(uc_replacement_d2_045)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00022500).reindex(feature.index)
UC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['uc_replacement_d3_045'] = {'inputs': ['uc_replacement_d2_045'], 'func': uc_replacement_d3_045}


def uc_replacement_d3_046(uc_replacement_d2_046):
    feature = _clean(uc_replacement_d2_046)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00023000).reindex(feature.index)
UC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['uc_replacement_d3_046'] = {'inputs': ['uc_replacement_d2_046'], 'func': uc_replacement_d3_046}


def uc_replacement_d3_047(uc_replacement_d2_047):
    feature = _clean(uc_replacement_d2_047)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00023500).reindex(feature.index)
UC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['uc_replacement_d3_047'] = {'inputs': ['uc_replacement_d2_047'], 'func': uc_replacement_d3_047}


def uc_replacement_d3_048(uc_replacement_d2_048):
    feature = _clean(uc_replacement_d2_048)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00024000).reindex(feature.index)
UC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['uc_replacement_d3_048'] = {'inputs': ['uc_replacement_d2_048'], 'func': uc_replacement_d3_048}


def uc_replacement_d3_049(uc_replacement_d2_049):
    feature = _clean(uc_replacement_d2_049)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00024500).reindex(feature.index)
UC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['uc_replacement_d3_049'] = {'inputs': ['uc_replacement_d2_049'], 'func': uc_replacement_d3_049}


def uc_replacement_d3_050(uc_replacement_d2_050):
    feature = _clean(uc_replacement_d2_050)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00025000).reindex(feature.index)
UC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['uc_replacement_d3_050'] = {'inputs': ['uc_replacement_d2_050'], 'func': uc_replacement_d3_050}


def uc_replacement_d3_051(uc_replacement_d2_051):
    feature = _clean(uc_replacement_d2_051)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00025500).reindex(feature.index)
UC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['uc_replacement_d3_051'] = {'inputs': ['uc_replacement_d2_051'], 'func': uc_replacement_d3_051}


def uc_replacement_d3_052(uc_replacement_d2_052):
    feature = _clean(uc_replacement_d2_052)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00026000).reindex(feature.index)
UC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['uc_replacement_d3_052'] = {'inputs': ['uc_replacement_d2_052'], 'func': uc_replacement_d3_052}


def uc_replacement_d3_053(uc_replacement_d2_053):
    feature = _clean(uc_replacement_d2_053)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00026500).reindex(feature.index)
UC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['uc_replacement_d3_053'] = {'inputs': ['uc_replacement_d2_053'], 'func': uc_replacement_d3_053}


def uc_replacement_d3_054(uc_replacement_d2_054):
    feature = _clean(uc_replacement_d2_054)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00027000).reindex(feature.index)
UC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['uc_replacement_d3_054'] = {'inputs': ['uc_replacement_d2_054'], 'func': uc_replacement_d3_054}


def uc_replacement_d3_055(uc_replacement_d2_055):
    feature = _clean(uc_replacement_d2_055)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00027500).reindex(feature.index)
UC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['uc_replacement_d3_055'] = {'inputs': ['uc_replacement_d2_055'], 'func': uc_replacement_d3_055}


def uc_replacement_d3_056(uc_replacement_d2_056):
    feature = _clean(uc_replacement_d2_056)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00028000).reindex(feature.index)
UC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['uc_replacement_d3_056'] = {'inputs': ['uc_replacement_d2_056'], 'func': uc_replacement_d3_056}


def uc_replacement_d3_057(uc_replacement_d2_057):
    feature = _clean(uc_replacement_d2_057)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00028500).reindex(feature.index)
UC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['uc_replacement_d3_057'] = {'inputs': ['uc_replacement_d2_057'], 'func': uc_replacement_d3_057}


def uc_replacement_d3_058(uc_replacement_d2_058):
    feature = _clean(uc_replacement_d2_058)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00029000).reindex(feature.index)
UC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['uc_replacement_d3_058'] = {'inputs': ['uc_replacement_d2_058'], 'func': uc_replacement_d3_058}


def uc_replacement_d3_059(uc_replacement_d2_059):
    feature = _clean(uc_replacement_d2_059)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00029500).reindex(feature.index)
UC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['uc_replacement_d3_059'] = {'inputs': ['uc_replacement_d2_059'], 'func': uc_replacement_d3_059}


def uc_replacement_d3_060(uc_replacement_d2_060):
    feature = _clean(uc_replacement_d2_060)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00030000).reindex(feature.index)
UC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['uc_replacement_d3_060'] = {'inputs': ['uc_replacement_d2_060'], 'func': uc_replacement_d3_060}


def uc_replacement_d3_061(uc_replacement_d2_061):
    feature = _clean(uc_replacement_d2_061)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00030500).reindex(feature.index)
UC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['uc_replacement_d3_061'] = {'inputs': ['uc_replacement_d2_061'], 'func': uc_replacement_d3_061}


def uc_replacement_d3_062(uc_replacement_d2_062):
    feature = _clean(uc_replacement_d2_062)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00031000).reindex(feature.index)
UC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['uc_replacement_d3_062'] = {'inputs': ['uc_replacement_d2_062'], 'func': uc_replacement_d3_062}


def uc_replacement_d3_063(uc_replacement_d2_063):
    feature = _clean(uc_replacement_d2_063)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00031500).reindex(feature.index)
UC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['uc_replacement_d3_063'] = {'inputs': ['uc_replacement_d2_063'], 'func': uc_replacement_d3_063}


def uc_replacement_d3_064(uc_replacement_d2_064):
    feature = _clean(uc_replacement_d2_064)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00032000).reindex(feature.index)
UC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['uc_replacement_d3_064'] = {'inputs': ['uc_replacement_d2_064'], 'func': uc_replacement_d3_064}


def uc_replacement_d3_065(uc_replacement_d2_065):
    feature = _clean(uc_replacement_d2_065)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00032500).reindex(feature.index)
UC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['uc_replacement_d3_065'] = {'inputs': ['uc_replacement_d2_065'], 'func': uc_replacement_d3_065}


def uc_replacement_d3_066(uc_replacement_d2_066):
    feature = _clean(uc_replacement_d2_066)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00033000).reindex(feature.index)
UC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['uc_replacement_d3_066'] = {'inputs': ['uc_replacement_d2_066'], 'func': uc_replacement_d3_066}


def uc_replacement_d3_067(uc_replacement_d2_067):
    feature = _clean(uc_replacement_d2_067)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00033500).reindex(feature.index)
UC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['uc_replacement_d3_067'] = {'inputs': ['uc_replacement_d2_067'], 'func': uc_replacement_d3_067}


def uc_replacement_d3_068(uc_replacement_d2_068):
    feature = _clean(uc_replacement_d2_068)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00034000).reindex(feature.index)
UC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['uc_replacement_d3_068'] = {'inputs': ['uc_replacement_d2_068'], 'func': uc_replacement_d3_068}


def uc_replacement_d3_069(uc_replacement_d2_069):
    feature = _clean(uc_replacement_d2_069)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00034500).reindex(feature.index)
UC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['uc_replacement_d3_069'] = {'inputs': ['uc_replacement_d2_069'], 'func': uc_replacement_d3_069}


def uc_replacement_d3_070(uc_replacement_d2_070):
    feature = _clean(uc_replacement_d2_070)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00035000).reindex(feature.index)
UC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['uc_replacement_d3_070'] = {'inputs': ['uc_replacement_d2_070'], 'func': uc_replacement_d3_070}


def uc_replacement_d3_071(uc_replacement_d2_071):
    feature = _clean(uc_replacement_d2_071)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00035500).reindex(feature.index)
UC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['uc_replacement_d3_071'] = {'inputs': ['uc_replacement_d2_071'], 'func': uc_replacement_d3_071}


def uc_replacement_d3_072(uc_replacement_d2_072):
    feature = _clean(uc_replacement_d2_072)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00036000).reindex(feature.index)
UC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['uc_replacement_d3_072'] = {'inputs': ['uc_replacement_d2_072'], 'func': uc_replacement_d3_072}


def uc_replacement_d3_073(uc_replacement_d2_073):
    feature = _clean(uc_replacement_d2_073)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00036500).reindex(feature.index)
UC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['uc_replacement_d3_073'] = {'inputs': ['uc_replacement_d2_073'], 'func': uc_replacement_d3_073}


def uc_replacement_d3_074(uc_replacement_d2_074):
    feature = _clean(uc_replacement_d2_074)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00037000).reindex(feature.index)
UC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['uc_replacement_d3_074'] = {'inputs': ['uc_replacement_d2_074'], 'func': uc_replacement_d3_074}


def uc_replacement_d3_075(uc_replacement_d2_075):
    feature = _clean(uc_replacement_d2_075)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00037500).reindex(feature.index)
UC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['uc_replacement_d3_075'] = {'inputs': ['uc_replacement_d2_075'], 'func': uc_replacement_d3_075}


def uc_replacement_d3_076(uc_replacement_d2_076):
    feature = _clean(uc_replacement_d2_076)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00038000).reindex(feature.index)
UC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['uc_replacement_d3_076'] = {'inputs': ['uc_replacement_d2_076'], 'func': uc_replacement_d3_076}


def uc_replacement_d3_077(uc_replacement_d2_077):
    feature = _clean(uc_replacement_d2_077)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00038500).reindex(feature.index)
UC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['uc_replacement_d3_077'] = {'inputs': ['uc_replacement_d2_077'], 'func': uc_replacement_d3_077}


def uc_replacement_d3_078(uc_replacement_d2_078):
    feature = _clean(uc_replacement_d2_078)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00039000).reindex(feature.index)
UC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['uc_replacement_d3_078'] = {'inputs': ['uc_replacement_d2_078'], 'func': uc_replacement_d3_078}


def uc_replacement_d3_079(uc_replacement_d2_079):
    feature = _clean(uc_replacement_d2_079)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00039500).reindex(feature.index)
UC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['uc_replacement_d3_079'] = {'inputs': ['uc_replacement_d2_079'], 'func': uc_replacement_d3_079}


def uc_replacement_d3_080(uc_replacement_d2_080):
    feature = _clean(uc_replacement_d2_080)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00040000).reindex(feature.index)
UC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['uc_replacement_d3_080'] = {'inputs': ['uc_replacement_d2_080'], 'func': uc_replacement_d3_080}


def uc_replacement_d3_081(uc_replacement_d2_081):
    feature = _clean(uc_replacement_d2_081)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00040500).reindex(feature.index)
UC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['uc_replacement_d3_081'] = {'inputs': ['uc_replacement_d2_081'], 'func': uc_replacement_d3_081}


def uc_replacement_d3_082(uc_replacement_d2_082):
    feature = _clean(uc_replacement_d2_082)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00041000).reindex(feature.index)
UC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['uc_replacement_d3_082'] = {'inputs': ['uc_replacement_d2_082'], 'func': uc_replacement_d3_082}


def uc_replacement_d3_083(uc_replacement_d2_083):
    feature = _clean(uc_replacement_d2_083)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00041500).reindex(feature.index)
UC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['uc_replacement_d3_083'] = {'inputs': ['uc_replacement_d2_083'], 'func': uc_replacement_d3_083}


def uc_replacement_d3_084(uc_replacement_d2_084):
    feature = _clean(uc_replacement_d2_084)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00042000).reindex(feature.index)
UC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['uc_replacement_d3_084'] = {'inputs': ['uc_replacement_d2_084'], 'func': uc_replacement_d3_084}


def uc_replacement_d3_085(uc_replacement_d2_085):
    feature = _clean(uc_replacement_d2_085)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00042500).reindex(feature.index)
UC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['uc_replacement_d3_085'] = {'inputs': ['uc_replacement_d2_085'], 'func': uc_replacement_d3_085}


def uc_replacement_d3_086(uc_replacement_d2_086):
    feature = _clean(uc_replacement_d2_086)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00043000).reindex(feature.index)
UC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['uc_replacement_d3_086'] = {'inputs': ['uc_replacement_d2_086'], 'func': uc_replacement_d3_086}


def uc_replacement_d3_087(uc_replacement_d2_087):
    feature = _clean(uc_replacement_d2_087)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00043500).reindex(feature.index)
UC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['uc_replacement_d3_087'] = {'inputs': ['uc_replacement_d2_087'], 'func': uc_replacement_d3_087}


def uc_replacement_d3_088(uc_replacement_d2_088):
    feature = _clean(uc_replacement_d2_088)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00044000).reindex(feature.index)
UC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['uc_replacement_d3_088'] = {'inputs': ['uc_replacement_d2_088'], 'func': uc_replacement_d3_088}


def uc_replacement_d3_089(uc_replacement_d2_089):
    feature = _clean(uc_replacement_d2_089)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00044500).reindex(feature.index)
UC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['uc_replacement_d3_089'] = {'inputs': ['uc_replacement_d2_089'], 'func': uc_replacement_d3_089}


def uc_replacement_d3_090(uc_replacement_d2_090):
    feature = _clean(uc_replacement_d2_090)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00045000).reindex(feature.index)
UC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['uc_replacement_d3_090'] = {'inputs': ['uc_replacement_d2_090'], 'func': uc_replacement_d3_090}


def uc_replacement_d3_091(uc_replacement_d2_091):
    feature = _clean(uc_replacement_d2_091)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00045500).reindex(feature.index)
UC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['uc_replacement_d3_091'] = {'inputs': ['uc_replacement_d2_091'], 'func': uc_replacement_d3_091}


def uc_replacement_d3_092(uc_replacement_d2_092):
    feature = _clean(uc_replacement_d2_092)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00046000).reindex(feature.index)
UC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['uc_replacement_d3_092'] = {'inputs': ['uc_replacement_d2_092'], 'func': uc_replacement_d3_092}


def uc_replacement_d3_093(uc_replacement_d2_093):
    feature = _clean(uc_replacement_d2_093)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00046500).reindex(feature.index)
UC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['uc_replacement_d3_093'] = {'inputs': ['uc_replacement_d2_093'], 'func': uc_replacement_d3_093}


def uc_replacement_d3_094(uc_replacement_d2_094):
    feature = _clean(uc_replacement_d2_094)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00047000).reindex(feature.index)
UC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['uc_replacement_d3_094'] = {'inputs': ['uc_replacement_d2_094'], 'func': uc_replacement_d3_094}


def uc_replacement_d3_095(uc_replacement_d2_095):
    feature = _clean(uc_replacement_d2_095)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00047500).reindex(feature.index)
UC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['uc_replacement_d3_095'] = {'inputs': ['uc_replacement_d2_095'], 'func': uc_replacement_d3_095}


def uc_replacement_d3_096(uc_replacement_d2_096):
    feature = _clean(uc_replacement_d2_096)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00048000).reindex(feature.index)
UC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['uc_replacement_d3_096'] = {'inputs': ['uc_replacement_d2_096'], 'func': uc_replacement_d3_096}


def uc_replacement_d3_097(uc_replacement_d2_097):
    feature = _clean(uc_replacement_d2_097)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00048500).reindex(feature.index)
UC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['uc_replacement_d3_097'] = {'inputs': ['uc_replacement_d2_097'], 'func': uc_replacement_d3_097}


def uc_replacement_d3_098(uc_replacement_d2_098):
    feature = _clean(uc_replacement_d2_098)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00049000).reindex(feature.index)
UC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['uc_replacement_d3_098'] = {'inputs': ['uc_replacement_d2_098'], 'func': uc_replacement_d3_098}


def uc_replacement_d3_099(uc_replacement_d2_099):
    feature = _clean(uc_replacement_d2_099)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00049500).reindex(feature.index)
UC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['uc_replacement_d3_099'] = {'inputs': ['uc_replacement_d2_099'], 'func': uc_replacement_d3_099}


def uc_replacement_d3_100(uc_replacement_d2_100):
    feature = _clean(uc_replacement_d2_100)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00050000).reindex(feature.index)
UC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['uc_replacement_d3_100'] = {'inputs': ['uc_replacement_d2_100'], 'func': uc_replacement_d3_100}


def uc_replacement_d3_101(uc_replacement_d2_101):
    feature = _clean(uc_replacement_d2_101)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00050500).reindex(feature.index)
UC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['uc_replacement_d3_101'] = {'inputs': ['uc_replacement_d2_101'], 'func': uc_replacement_d3_101}


def uc_replacement_d3_102(uc_replacement_d2_102):
    feature = _clean(uc_replacement_d2_102)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00051000).reindex(feature.index)
UC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['uc_replacement_d3_102'] = {'inputs': ['uc_replacement_d2_102'], 'func': uc_replacement_d3_102}


def uc_replacement_d3_103(uc_replacement_d2_103):
    feature = _clean(uc_replacement_d2_103)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00051500).reindex(feature.index)
UC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['uc_replacement_d3_103'] = {'inputs': ['uc_replacement_d2_103'], 'func': uc_replacement_d3_103}


def uc_replacement_d3_104(uc_replacement_d2_104):
    feature = _clean(uc_replacement_d2_104)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00052000).reindex(feature.index)
UC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['uc_replacement_d3_104'] = {'inputs': ['uc_replacement_d2_104'], 'func': uc_replacement_d3_104}


def uc_replacement_d3_105(uc_replacement_d2_105):
    feature = _clean(uc_replacement_d2_105)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00052500).reindex(feature.index)
UC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['uc_replacement_d3_105'] = {'inputs': ['uc_replacement_d2_105'], 'func': uc_replacement_d3_105}


def uc_replacement_d3_106(uc_replacement_d2_106):
    feature = _clean(uc_replacement_d2_106)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00053000).reindex(feature.index)
UC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['uc_replacement_d3_106'] = {'inputs': ['uc_replacement_d2_106'], 'func': uc_replacement_d3_106}


def uc_replacement_d3_107(uc_replacement_d2_107):
    feature = _clean(uc_replacement_d2_107)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00053500).reindex(feature.index)
UC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['uc_replacement_d3_107'] = {'inputs': ['uc_replacement_d2_107'], 'func': uc_replacement_d3_107}


def uc_replacement_d3_108(uc_replacement_d2_108):
    feature = _clean(uc_replacement_d2_108)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00054000).reindex(feature.index)
UC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['uc_replacement_d3_108'] = {'inputs': ['uc_replacement_d2_108'], 'func': uc_replacement_d3_108}


def uc_replacement_d3_109(uc_replacement_d2_109):
    feature = _clean(uc_replacement_d2_109)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00054500).reindex(feature.index)
UC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['uc_replacement_d3_109'] = {'inputs': ['uc_replacement_d2_109'], 'func': uc_replacement_d3_109}


def uc_replacement_d3_110(uc_replacement_d2_110):
    feature = _clean(uc_replacement_d2_110)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00055000).reindex(feature.index)
UC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['uc_replacement_d3_110'] = {'inputs': ['uc_replacement_d2_110'], 'func': uc_replacement_d3_110}


def uc_replacement_d3_111(uc_replacement_d2_111):
    feature = _clean(uc_replacement_d2_111)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00055500).reindex(feature.index)
UC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['uc_replacement_d3_111'] = {'inputs': ['uc_replacement_d2_111'], 'func': uc_replacement_d3_111}


def uc_replacement_d3_112(uc_replacement_d2_112):
    feature = _clean(uc_replacement_d2_112)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00056000).reindex(feature.index)
UC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['uc_replacement_d3_112'] = {'inputs': ['uc_replacement_d2_112'], 'func': uc_replacement_d3_112}


def uc_replacement_d3_113(uc_replacement_d2_113):
    feature = _clean(uc_replacement_d2_113)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00056500).reindex(feature.index)
UC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['uc_replacement_d3_113'] = {'inputs': ['uc_replacement_d2_113'], 'func': uc_replacement_d3_113}


def uc_replacement_d3_114(uc_replacement_d2_114):
    feature = _clean(uc_replacement_d2_114)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00057000).reindex(feature.index)
UC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['uc_replacement_d3_114'] = {'inputs': ['uc_replacement_d2_114'], 'func': uc_replacement_d3_114}


def uc_replacement_d3_115(uc_replacement_d2_115):
    feature = _clean(uc_replacement_d2_115)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00057500).reindex(feature.index)
UC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['uc_replacement_d3_115'] = {'inputs': ['uc_replacement_d2_115'], 'func': uc_replacement_d3_115}


def uc_replacement_d3_116(uc_replacement_d2_116):
    feature = _clean(uc_replacement_d2_116)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00058000).reindex(feature.index)
UC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['uc_replacement_d3_116'] = {'inputs': ['uc_replacement_d2_116'], 'func': uc_replacement_d3_116}


def uc_replacement_d3_117(uc_replacement_d2_117):
    feature = _clean(uc_replacement_d2_117)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00058500).reindex(feature.index)
UC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['uc_replacement_d3_117'] = {'inputs': ['uc_replacement_d2_117'], 'func': uc_replacement_d3_117}


def uc_replacement_d3_118(uc_replacement_d2_118):
    feature = _clean(uc_replacement_d2_118)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00059000).reindex(feature.index)
UC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['uc_replacement_d3_118'] = {'inputs': ['uc_replacement_d2_118'], 'func': uc_replacement_d3_118}


def uc_replacement_d3_119(uc_replacement_d2_119):
    feature = _clean(uc_replacement_d2_119)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00059500).reindex(feature.index)
UC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['uc_replacement_d3_119'] = {'inputs': ['uc_replacement_d2_119'], 'func': uc_replacement_d3_119}


def uc_replacement_d3_120(uc_replacement_d2_120):
    feature = _clean(uc_replacement_d2_120)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00060000).reindex(feature.index)
UC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['uc_replacement_d3_120'] = {'inputs': ['uc_replacement_d2_120'], 'func': uc_replacement_d3_120}


def uc_replacement_d3_121(uc_replacement_d2_121):
    feature = _clean(uc_replacement_d2_121)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00060500).reindex(feature.index)
UC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['uc_replacement_d3_121'] = {'inputs': ['uc_replacement_d2_121'], 'func': uc_replacement_d3_121}


def uc_replacement_d3_122(uc_replacement_d2_122):
    feature = _clean(uc_replacement_d2_122)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00061000).reindex(feature.index)
UC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['uc_replacement_d3_122'] = {'inputs': ['uc_replacement_d2_122'], 'func': uc_replacement_d3_122}


def uc_replacement_d3_123(uc_replacement_d2_123):
    feature = _clean(uc_replacement_d2_123)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00061500).reindex(feature.index)
UC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['uc_replacement_d3_123'] = {'inputs': ['uc_replacement_d2_123'], 'func': uc_replacement_d3_123}


def uc_replacement_d3_124(uc_replacement_d2_124):
    feature = _clean(uc_replacement_d2_124)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00062000).reindex(feature.index)
UC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['uc_replacement_d3_124'] = {'inputs': ['uc_replacement_d2_124'], 'func': uc_replacement_d3_124}


def uc_replacement_d3_125(uc_replacement_d2_125):
    feature = _clean(uc_replacement_d2_125)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00062500).reindex(feature.index)
UC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['uc_replacement_d3_125'] = {'inputs': ['uc_replacement_d2_125'], 'func': uc_replacement_d3_125}


def uc_replacement_d3_126(uc_replacement_d2_126):
    feature = _clean(uc_replacement_d2_126)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00063000).reindex(feature.index)
UC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['uc_replacement_d3_126'] = {'inputs': ['uc_replacement_d2_126'], 'func': uc_replacement_d3_126}


def uc_replacement_d3_127(uc_replacement_d2_127):
    feature = _clean(uc_replacement_d2_127)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00063500).reindex(feature.index)
UC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['uc_replacement_d3_127'] = {'inputs': ['uc_replacement_d2_127'], 'func': uc_replacement_d3_127}


def uc_replacement_d3_128(uc_replacement_d2_128):
    feature = _clean(uc_replacement_d2_128)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00064000).reindex(feature.index)
UC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['uc_replacement_d3_128'] = {'inputs': ['uc_replacement_d2_128'], 'func': uc_replacement_d3_128}


def uc_replacement_d3_129(uc_replacement_d2_129):
    feature = _clean(uc_replacement_d2_129)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00064500).reindex(feature.index)
UC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['uc_replacement_d3_129'] = {'inputs': ['uc_replacement_d2_129'], 'func': uc_replacement_d3_129}


def uc_replacement_d3_130(uc_replacement_d2_130):
    feature = _clean(uc_replacement_d2_130)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00065000).reindex(feature.index)
UC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['uc_replacement_d3_130'] = {'inputs': ['uc_replacement_d2_130'], 'func': uc_replacement_d3_130}


def uc_replacement_d3_131(uc_replacement_d2_131):
    feature = _clean(uc_replacement_d2_131)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00065500).reindex(feature.index)
UC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['uc_replacement_d3_131'] = {'inputs': ['uc_replacement_d2_131'], 'func': uc_replacement_d3_131}


def uc_replacement_d3_132(uc_replacement_d2_132):
    feature = _clean(uc_replacement_d2_132)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00066000).reindex(feature.index)
UC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['uc_replacement_d3_132'] = {'inputs': ['uc_replacement_d2_132'], 'func': uc_replacement_d3_132}


def uc_replacement_d3_133(uc_replacement_d2_133):
    feature = _clean(uc_replacement_d2_133)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00066500).reindex(feature.index)
UC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['uc_replacement_d3_133'] = {'inputs': ['uc_replacement_d2_133'], 'func': uc_replacement_d3_133}


def uc_replacement_d3_134(uc_replacement_d2_134):
    feature = _clean(uc_replacement_d2_134)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00067000).reindex(feature.index)
UC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['uc_replacement_d3_134'] = {'inputs': ['uc_replacement_d2_134'], 'func': uc_replacement_d3_134}


def uc_replacement_d3_135(uc_replacement_d2_135):
    feature = _clean(uc_replacement_d2_135)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00067500).reindex(feature.index)
UC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['uc_replacement_d3_135'] = {'inputs': ['uc_replacement_d2_135'], 'func': uc_replacement_d3_135}


def uc_replacement_d3_136(uc_replacement_d2_136):
    feature = _clean(uc_replacement_d2_136)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00068000).reindex(feature.index)
UC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['uc_replacement_d3_136'] = {'inputs': ['uc_replacement_d2_136'], 'func': uc_replacement_d3_136}


def uc_replacement_d3_137(uc_replacement_d2_137):
    feature = _clean(uc_replacement_d2_137)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00068500).reindex(feature.index)
UC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['uc_replacement_d3_137'] = {'inputs': ['uc_replacement_d2_137'], 'func': uc_replacement_d3_137}


def uc_replacement_d3_138(uc_replacement_d2_138):
    feature = _clean(uc_replacement_d2_138)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00069000).reindex(feature.index)
UC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['uc_replacement_d3_138'] = {'inputs': ['uc_replacement_d2_138'], 'func': uc_replacement_d3_138}


def uc_replacement_d3_139(uc_replacement_d2_139):
    feature = _clean(uc_replacement_d2_139)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00069500).reindex(feature.index)
UC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['uc_replacement_d3_139'] = {'inputs': ['uc_replacement_d2_139'], 'func': uc_replacement_d3_139}


def uc_replacement_d3_140(uc_replacement_d2_140):
    feature = _clean(uc_replacement_d2_140)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00070000).reindex(feature.index)
UC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['uc_replacement_d3_140'] = {'inputs': ['uc_replacement_d2_140'], 'func': uc_replacement_d3_140}


def uc_replacement_d3_141(uc_replacement_d2_141):
    feature = _clean(uc_replacement_d2_141)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00070500).reindex(feature.index)
UC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['uc_replacement_d3_141'] = {'inputs': ['uc_replacement_d2_141'], 'func': uc_replacement_d3_141}


def uc_replacement_d3_142(uc_replacement_d2_142):
    feature = _clean(uc_replacement_d2_142)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00071000).reindex(feature.index)
UC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['uc_replacement_d3_142'] = {'inputs': ['uc_replacement_d2_142'], 'func': uc_replacement_d3_142}


def uc_replacement_d3_143(uc_replacement_d2_143):
    feature = _clean(uc_replacement_d2_143)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00071500).reindex(feature.index)
UC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['uc_replacement_d3_143'] = {'inputs': ['uc_replacement_d2_143'], 'func': uc_replacement_d3_143}


def uc_replacement_d3_144(uc_replacement_d2_144):
    feature = _clean(uc_replacement_d2_144)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00072000).reindex(feature.index)
UC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['uc_replacement_d3_144'] = {'inputs': ['uc_replacement_d2_144'], 'func': uc_replacement_d3_144}


def uc_replacement_d3_145(uc_replacement_d2_145):
    feature = _clean(uc_replacement_d2_145)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00072500).reindex(feature.index)
UC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['uc_replacement_d3_145'] = {'inputs': ['uc_replacement_d2_145'], 'func': uc_replacement_d3_145}


def uc_replacement_d3_146(uc_replacement_d2_146):
    feature = _clean(uc_replacement_d2_146)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00073000).reindex(feature.index)
UC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['uc_replacement_d3_146'] = {'inputs': ['uc_replacement_d2_146'], 'func': uc_replacement_d3_146}


def uc_replacement_d3_147(uc_replacement_d2_147):
    feature = _clean(uc_replacement_d2_147)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00073500).reindex(feature.index)
UC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['uc_replacement_d3_147'] = {'inputs': ['uc_replacement_d2_147'], 'func': uc_replacement_d3_147}


def uc_replacement_d3_148(uc_replacement_d2_148):
    feature = _clean(uc_replacement_d2_148)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00074000).reindex(feature.index)
UC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['uc_replacement_d3_148'] = {'inputs': ['uc_replacement_d2_148'], 'func': uc_replacement_d3_148}


def uc_replacement_d3_149(uc_replacement_d2_149):
    feature = _clean(uc_replacement_d2_149)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00074500).reindex(feature.index)
UC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['uc_replacement_d3_149'] = {'inputs': ['uc_replacement_d2_149'], 'func': uc_replacement_d3_149}


def uc_replacement_d3_150(uc_replacement_d2_150):
    feature = _clean(uc_replacement_d2_150)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00075000).reindex(feature.index)
UC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['uc_replacement_d3_150'] = {'inputs': ['uc_replacement_d2_150'], 'func': uc_replacement_d3_150}


def uc_replacement_d3_151(uc_replacement_d2_151):
    feature = _clean(uc_replacement_d2_151)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00075500).reindex(feature.index)
UC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['uc_replacement_d3_151'] = {'inputs': ['uc_replacement_d2_151'], 'func': uc_replacement_d3_151}


def uc_replacement_d3_152(uc_replacement_d2_152):
    feature = _clean(uc_replacement_d2_152)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00076000).reindex(feature.index)
UC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['uc_replacement_d3_152'] = {'inputs': ['uc_replacement_d2_152'], 'func': uc_replacement_d3_152}


def uc_replacement_d3_153(uc_replacement_d2_153):
    feature = _clean(uc_replacement_d2_153)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00076500).reindex(feature.index)
UC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['uc_replacement_d3_153'] = {'inputs': ['uc_replacement_d2_153'], 'func': uc_replacement_d3_153}


def uc_replacement_d3_154(uc_replacement_d2_154):
    feature = _clean(uc_replacement_d2_154)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00077000).reindex(feature.index)
UC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['uc_replacement_d3_154'] = {'inputs': ['uc_replacement_d2_154'], 'func': uc_replacement_d3_154}


def uc_replacement_d3_155(uc_replacement_d2_155):
    feature = _clean(uc_replacement_d2_155)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00077500).reindex(feature.index)
UC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['uc_replacement_d3_155'] = {'inputs': ['uc_replacement_d2_155'], 'func': uc_replacement_d3_155}


def uc_replacement_d3_156(uc_replacement_d2_156):
    feature = _clean(uc_replacement_d2_156)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00078000).reindex(feature.index)
UC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['uc_replacement_d3_156'] = {'inputs': ['uc_replacement_d2_156'], 'func': uc_replacement_d3_156}


def uc_replacement_d3_157(uc_replacement_d2_157):
    feature = _clean(uc_replacement_d2_157)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00078500).reindex(feature.index)
UC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['uc_replacement_d3_157'] = {'inputs': ['uc_replacement_d2_157'], 'func': uc_replacement_d3_157}


def uc_replacement_d3_158(uc_replacement_d2_158):
    feature = _clean(uc_replacement_d2_158)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00079000).reindex(feature.index)
UC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['uc_replacement_d3_158'] = {'inputs': ['uc_replacement_d2_158'], 'func': uc_replacement_d3_158}


def uc_replacement_d3_159(uc_replacement_d2_159):
    feature = _clean(uc_replacement_d2_159)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00079500).reindex(feature.index)
UC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['uc_replacement_d3_159'] = {'inputs': ['uc_replacement_d2_159'], 'func': uc_replacement_d3_159}


def uc_replacement_d3_160(uc_replacement_d2_160):
    feature = _clean(uc_replacement_d2_160)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00080000).reindex(feature.index)
UC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['uc_replacement_d3_160'] = {'inputs': ['uc_replacement_d2_160'], 'func': uc_replacement_d3_160}


def uc_replacement_d3_161(uc_replacement_d2_161):
    feature = _clean(uc_replacement_d2_161)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00080500).reindex(feature.index)
UC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['uc_replacement_d3_161'] = {'inputs': ['uc_replacement_d2_161'], 'func': uc_replacement_d3_161}


def uc_replacement_d3_162(uc_replacement_d2_162):
    feature = _clean(uc_replacement_d2_162)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00081000).reindex(feature.index)
UC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['uc_replacement_d3_162'] = {'inputs': ['uc_replacement_d2_162'], 'func': uc_replacement_d3_162}


def uc_replacement_d3_163(uc_replacement_d2_163):
    feature = _clean(uc_replacement_d2_163)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00081500).reindex(feature.index)
UC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['uc_replacement_d3_163'] = {'inputs': ['uc_replacement_d2_163'], 'func': uc_replacement_d3_163}


def uc_replacement_d3_164(uc_replacement_d2_164):
    feature = _clean(uc_replacement_d2_164)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00082000).reindex(feature.index)
UC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['uc_replacement_d3_164'] = {'inputs': ['uc_replacement_d2_164'], 'func': uc_replacement_d3_164}


def uc_replacement_d3_165(uc_replacement_d2_165):
    feature = _clean(uc_replacement_d2_165)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00082500).reindex(feature.index)
UC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['uc_replacement_d3_165'] = {'inputs': ['uc_replacement_d2_165'], 'func': uc_replacement_d3_165}


def uc_replacement_d3_166(uc_replacement_d2_166):
    feature = _clean(uc_replacement_d2_166)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00083000).reindex(feature.index)
UC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['uc_replacement_d3_166'] = {'inputs': ['uc_replacement_d2_166'], 'func': uc_replacement_d3_166}


def uc_replacement_d3_167(uc_replacement_d2_167):
    feature = _clean(uc_replacement_d2_167)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00083500).reindex(feature.index)
UC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['uc_replacement_d3_167'] = {'inputs': ['uc_replacement_d2_167'], 'func': uc_replacement_d3_167}


def uc_replacement_d3_168(uc_replacement_d2_168):
    feature = _clean(uc_replacement_d2_168)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00084000).reindex(feature.index)
UC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['uc_replacement_d3_168'] = {'inputs': ['uc_replacement_d2_168'], 'func': uc_replacement_d3_168}


def uc_replacement_d3_169(uc_replacement_d2_169):
    feature = _clean(uc_replacement_d2_169)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00084500).reindex(feature.index)
UC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['uc_replacement_d3_169'] = {'inputs': ['uc_replacement_d2_169'], 'func': uc_replacement_d3_169}


def uc_replacement_d3_170(uc_replacement_d2_170):
    feature = _clean(uc_replacement_d2_170)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00085000).reindex(feature.index)
UC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['uc_replacement_d3_170'] = {'inputs': ['uc_replacement_d2_170'], 'func': uc_replacement_d3_170}


# Third-derivative extensions for repaired first-base features.
UW_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY = {}


def _base_universe_d3(feature, idx):
    feature = _clean(feature) if '_clean' in globals() else _s(feature).replace([np.inf, -np.inf], np.nan)
    windows = [1, 2, 3, 5, 8, 13, 21, 34, 55]
    lag = windows[(idx * 2) % len(windows)]
    smooth = windows[(idx * 5 + 2) % len(windows)]
    accel = feature.diff(lag)
    curve = feature - feature.rolling(max(3, smooth), min_periods=2).mean()
    out = accel + curve.fillna(0.0) * (0.00019 * ((idx % 19) + 1))
    return out.replace([np.inf, -np.inf], np.nan).reindex(feature.index)


def uw_base_universe_d3_001_uw_002_low_distance_10_002(uw_base_universe_d2_001_uw_002_low_distance_10_002):
    return _base_universe_d3(uw_base_universe_d2_001_uw_002_low_distance_10_002, 1)
UW_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['uw_base_universe_d3_001_uw_002_low_distance_10_002'] = {'inputs': ['uw_base_universe_d2_001_uw_002_low_distance_10_002'], 'func': uw_base_universe_d3_001_uw_002_low_distance_10_002}


def uw_base_universe_d3_002_uw_003_underwater_area_21_003(uw_base_universe_d2_002_uw_003_underwater_area_21_003):
    return _base_universe_d3(uw_base_universe_d2_002_uw_003_underwater_area_21_003, 2)
UW_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['uw_base_universe_d3_002_uw_003_underwater_area_21_003'] = {'inputs': ['uw_base_universe_d2_002_uw_003_underwater_area_21_003'], 'func': uw_base_universe_d3_002_uw_003_underwater_area_21_003}


def uw_base_universe_d3_003_uw_006_lower_high_ratio_84_006(uw_base_universe_d2_003_uw_006_lower_high_ratio_84_006):
    return _base_universe_d3(uw_base_universe_d2_003_uw_006_lower_high_ratio_84_006, 3)
UW_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['uw_base_universe_d3_003_uw_006_lower_high_ratio_84_006'] = {'inputs': ['uw_base_universe_d2_003_uw_006_lower_high_ratio_84_006'], 'func': uw_base_universe_d3_003_uw_006_lower_high_ratio_84_006}


def uw_base_universe_d3_004_uw_008_low_distance_189_008(uw_base_universe_d2_004_uw_008_low_distance_189_008):
    return _base_universe_d3(uw_base_universe_d2_004_uw_008_low_distance_189_008, 4)
UW_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['uw_base_universe_d3_004_uw_008_low_distance_189_008'] = {'inputs': ['uw_base_universe_d2_004_uw_008_low_distance_189_008'], 'func': uw_base_universe_d3_004_uw_008_low_distance_189_008}


def uw_base_universe_d3_005_uw_009_underwater_area_252_009(uw_base_universe_d2_005_uw_009_underwater_area_252_009):
    return _base_universe_d3(uw_base_universe_d2_005_uw_009_underwater_area_252_009, 5)
UW_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['uw_base_universe_d3_005_uw_009_underwater_area_252_009'] = {'inputs': ['uw_base_universe_d2_005_uw_009_underwater_area_252_009'], 'func': uw_base_universe_d3_005_uw_009_underwater_area_252_009}


def uw_base_universe_d3_006_uw_012_lower_high_ratio_756_012(uw_base_universe_d2_006_uw_012_lower_high_ratio_756_012):
    return _base_universe_d3(uw_base_universe_d2_006_uw_012_lower_high_ratio_756_012, 6)
UW_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['uw_base_universe_d3_006_uw_012_lower_high_ratio_756_012'] = {'inputs': ['uw_base_universe_d2_006_uw_012_lower_high_ratio_756_012'], 'func': uw_base_universe_d3_006_uw_012_lower_high_ratio_756_012}


def uw_base_universe_d3_007_uw_014_low_distance_1260_014(uw_base_universe_d2_007_uw_014_low_distance_1260_014):
    return _base_universe_d3(uw_base_universe_d2_007_uw_014_low_distance_1260_014, 7)
UW_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['uw_base_universe_d3_007_uw_014_low_distance_1260_014'] = {'inputs': ['uw_base_universe_d2_007_uw_014_low_distance_1260_014'], 'func': uw_base_universe_d3_007_uw_014_low_distance_1260_014}


def uw_base_universe_d3_008_uw_015_underwater_area_1512_015(uw_base_universe_d2_008_uw_015_underwater_area_1512_015):
    return _base_universe_d3(uw_base_universe_d2_008_uw_015_underwater_area_1512_015, 8)
UW_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['uw_base_universe_d3_008_uw_015_underwater_area_1512_015'] = {'inputs': ['uw_base_universe_d2_008_uw_015_underwater_area_1512_015'], 'func': uw_base_universe_d3_008_uw_015_underwater_area_1512_015}


def uw_base_universe_d3_009_uw_018_lower_high_ratio_21_018(uw_base_universe_d2_009_uw_018_lower_high_ratio_21_018):
    return _base_universe_d3(uw_base_universe_d2_009_uw_018_lower_high_ratio_21_018, 9)
UW_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['uw_base_universe_d3_009_uw_018_lower_high_ratio_21_018'] = {'inputs': ['uw_base_universe_d2_009_uw_018_lower_high_ratio_21_018'], 'func': uw_base_universe_d3_009_uw_018_lower_high_ratio_21_018}


def uw_base_universe_d3_010_uw_020_low_distance_63_020(uw_base_universe_d2_010_uw_020_low_distance_63_020):
    return _base_universe_d3(uw_base_universe_d2_010_uw_020_low_distance_63_020, 10)
UW_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['uw_base_universe_d3_010_uw_020_low_distance_63_020'] = {'inputs': ['uw_base_universe_d2_010_uw_020_low_distance_63_020'], 'func': uw_base_universe_d3_010_uw_020_low_distance_63_020}


def uw_base_universe_d3_011_uw_021_underwater_area_84_021(uw_base_universe_d2_011_uw_021_underwater_area_84_021):
    return _base_universe_d3(uw_base_universe_d2_011_uw_021_underwater_area_84_021, 11)
UW_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['uw_base_universe_d3_011_uw_021_underwater_area_84_021'] = {'inputs': ['uw_base_universe_d2_011_uw_021_underwater_area_84_021'], 'func': uw_base_universe_d3_011_uw_021_underwater_area_84_021}


def uw_base_universe_d3_012_uw_024_lower_high_ratio_252_024(uw_base_universe_d2_012_uw_024_lower_high_ratio_252_024):
    return _base_universe_d3(uw_base_universe_d2_012_uw_024_lower_high_ratio_252_024, 12)
UW_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['uw_base_universe_d3_012_uw_024_lower_high_ratio_252_024'] = {'inputs': ['uw_base_universe_d2_012_uw_024_lower_high_ratio_252_024'], 'func': uw_base_universe_d3_012_uw_024_lower_high_ratio_252_024}


def uw_base_universe_d3_013_uw_026_low_distance_504_026(uw_base_universe_d2_013_uw_026_low_distance_504_026):
    return _base_universe_d3(uw_base_universe_d2_013_uw_026_low_distance_504_026, 13)
UW_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['uw_base_universe_d3_013_uw_026_low_distance_504_026'] = {'inputs': ['uw_base_universe_d2_013_uw_026_low_distance_504_026'], 'func': uw_base_universe_d3_013_uw_026_low_distance_504_026}


def uw_base_universe_d3_014_uw_027_underwater_area_756_027(uw_base_universe_d2_014_uw_027_underwater_area_756_027):
    return _base_universe_d3(uw_base_universe_d2_014_uw_027_underwater_area_756_027, 14)
UW_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['uw_base_universe_d3_014_uw_027_underwater_area_756_027'] = {'inputs': ['uw_base_universe_d2_014_uw_027_underwater_area_756_027'], 'func': uw_base_universe_d3_014_uw_027_underwater_area_756_027}


def uw_base_universe_d3_015_uw_030_lower_high_ratio_1512_030(uw_base_universe_d2_015_uw_030_lower_high_ratio_1512_030):
    return _base_universe_d3(uw_base_universe_d2_015_uw_030_lower_high_ratio_1512_030, 15)
UW_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['uw_base_universe_d3_015_uw_030_lower_high_ratio_1512_030'] = {'inputs': ['uw_base_universe_d2_015_uw_030_lower_high_ratio_1512_030'], 'func': uw_base_universe_d3_015_uw_030_lower_high_ratio_1512_030}


def uw_base_universe_d3_016_uw_basefill_004(uw_base_universe_d2_016_uw_basefill_004):
    return _base_universe_d3(uw_base_universe_d2_016_uw_basefill_004, 16)
UW_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['uw_base_universe_d3_016_uw_basefill_004'] = {'inputs': ['uw_base_universe_d2_016_uw_basefill_004'], 'func': uw_base_universe_d3_016_uw_basefill_004}


def uw_base_universe_d3_017_uw_basefill_005(uw_base_universe_d2_017_uw_basefill_005):
    return _base_universe_d3(uw_base_universe_d2_017_uw_basefill_005, 17)
UW_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['uw_base_universe_d3_017_uw_basefill_005'] = {'inputs': ['uw_base_universe_d2_017_uw_basefill_005'], 'func': uw_base_universe_d3_017_uw_basefill_005}


def uw_base_universe_d3_018_uw_basefill_010(uw_base_universe_d2_018_uw_basefill_010):
    return _base_universe_d3(uw_base_universe_d2_018_uw_basefill_010, 18)
UW_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['uw_base_universe_d3_018_uw_basefill_010'] = {'inputs': ['uw_base_universe_d2_018_uw_basefill_010'], 'func': uw_base_universe_d3_018_uw_basefill_010}


def uw_base_universe_d3_019_uw_basefill_011(uw_base_universe_d2_019_uw_basefill_011):
    return _base_universe_d3(uw_base_universe_d2_019_uw_basefill_011, 19)
UW_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['uw_base_universe_d3_019_uw_basefill_011'] = {'inputs': ['uw_base_universe_d2_019_uw_basefill_011'], 'func': uw_base_universe_d3_019_uw_basefill_011}


def uw_base_universe_d3_020_uw_basefill_016(uw_base_universe_d2_020_uw_basefill_016):
    return _base_universe_d3(uw_base_universe_d2_020_uw_basefill_016, 20)
UW_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['uw_base_universe_d3_020_uw_basefill_016'] = {'inputs': ['uw_base_universe_d2_020_uw_basefill_016'], 'func': uw_base_universe_d3_020_uw_basefill_016}


def uw_base_universe_d3_021_uw_basefill_017(uw_base_universe_d2_021_uw_basefill_017):
    return _base_universe_d3(uw_base_universe_d2_021_uw_basefill_017, 21)
UW_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['uw_base_universe_d3_021_uw_basefill_017'] = {'inputs': ['uw_base_universe_d2_021_uw_basefill_017'], 'func': uw_base_universe_d3_021_uw_basefill_017}


def uw_base_universe_d3_022_uw_basefill_022(uw_base_universe_d2_022_uw_basefill_022):
    return _base_universe_d3(uw_base_universe_d2_022_uw_basefill_022, 22)
UW_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['uw_base_universe_d3_022_uw_basefill_022'] = {'inputs': ['uw_base_universe_d2_022_uw_basefill_022'], 'func': uw_base_universe_d3_022_uw_basefill_022}


def uw_base_universe_d3_023_uw_basefill_023(uw_base_universe_d2_023_uw_basefill_023):
    return _base_universe_d3(uw_base_universe_d2_023_uw_basefill_023, 23)
UW_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['uw_base_universe_d3_023_uw_basefill_023'] = {'inputs': ['uw_base_universe_d2_023_uw_basefill_023'], 'func': uw_base_universe_d3_023_uw_basefill_023}


def uw_base_universe_d3_024_uw_basefill_028(uw_base_universe_d2_024_uw_basefill_028):
    return _base_universe_d3(uw_base_universe_d2_024_uw_basefill_028, 24)
UW_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['uw_base_universe_d3_024_uw_basefill_028'] = {'inputs': ['uw_base_universe_d2_024_uw_basefill_028'], 'func': uw_base_universe_d3_024_uw_basefill_028}


def uw_base_universe_d3_025_uw_basefill_029(uw_base_universe_d2_025_uw_basefill_029):
    return _base_universe_d3(uw_base_universe_d2_025_uw_basefill_029, 25)
UW_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['uw_base_universe_d3_025_uw_basefill_029'] = {'inputs': ['uw_base_universe_d2_025_uw_basefill_029'], 'func': uw_base_universe_d3_025_uw_basefill_029}


def uw_base_universe_d3_026_uw_basefill_031(uw_base_universe_d2_026_uw_basefill_031):
    return _base_universe_d3(uw_base_universe_d2_026_uw_basefill_031, 26)
UW_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['uw_base_universe_d3_026_uw_basefill_031'] = {'inputs': ['uw_base_universe_d2_026_uw_basefill_031'], 'func': uw_base_universe_d3_026_uw_basefill_031}


def uw_base_universe_d3_027_uw_basefill_032(uw_base_universe_d2_027_uw_basefill_032):
    return _base_universe_d3(uw_base_universe_d2_027_uw_basefill_032, 27)
UW_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['uw_base_universe_d3_027_uw_basefill_032'] = {'inputs': ['uw_base_universe_d2_027_uw_basefill_032'], 'func': uw_base_universe_d3_027_uw_basefill_032}


def uw_base_universe_d3_028_uw_basefill_033(uw_base_universe_d2_028_uw_basefill_033):
    return _base_universe_d3(uw_base_universe_d2_028_uw_basefill_033, 28)
UW_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['uw_base_universe_d3_028_uw_basefill_033'] = {'inputs': ['uw_base_universe_d2_028_uw_basefill_033'], 'func': uw_base_universe_d3_028_uw_basefill_033}


def uw_base_universe_d3_029_uw_basefill_034(uw_base_universe_d2_029_uw_basefill_034):
    return _base_universe_d3(uw_base_universe_d2_029_uw_basefill_034, 29)
UW_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['uw_base_universe_d3_029_uw_basefill_034'] = {'inputs': ['uw_base_universe_d2_029_uw_basefill_034'], 'func': uw_base_universe_d3_029_uw_basefill_034}


def uw_base_universe_d3_030_uw_basefill_035(uw_base_universe_d2_030_uw_basefill_035):
    return _base_universe_d3(uw_base_universe_d2_030_uw_basefill_035, 30)
UW_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['uw_base_universe_d3_030_uw_basefill_035'] = {'inputs': ['uw_base_universe_d2_030_uw_basefill_035'], 'func': uw_base_universe_d3_030_uw_basefill_035}


def uw_base_universe_d3_031_uw_basefill_036(uw_base_universe_d2_031_uw_basefill_036):
    return _base_universe_d3(uw_base_universe_d2_031_uw_basefill_036, 31)
UW_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['uw_base_universe_d3_031_uw_basefill_036'] = {'inputs': ['uw_base_universe_d2_031_uw_basefill_036'], 'func': uw_base_universe_d3_031_uw_basefill_036}


def uw_base_universe_d3_032_uw_basefill_037(uw_base_universe_d2_032_uw_basefill_037):
    return _base_universe_d3(uw_base_universe_d2_032_uw_basefill_037, 32)
UW_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['uw_base_universe_d3_032_uw_basefill_037'] = {'inputs': ['uw_base_universe_d2_032_uw_basefill_037'], 'func': uw_base_universe_d3_032_uw_basefill_037}


def uw_base_universe_d3_033_uw_basefill_038(uw_base_universe_d2_033_uw_basefill_038):
    return _base_universe_d3(uw_base_universe_d2_033_uw_basefill_038, 33)
UW_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['uw_base_universe_d3_033_uw_basefill_038'] = {'inputs': ['uw_base_universe_d2_033_uw_basefill_038'], 'func': uw_base_universe_d3_033_uw_basefill_038}


def uw_base_universe_d3_034_uw_basefill_039(uw_base_universe_d2_034_uw_basefill_039):
    return _base_universe_d3(uw_base_universe_d2_034_uw_basefill_039, 34)
UW_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['uw_base_universe_d3_034_uw_basefill_039'] = {'inputs': ['uw_base_universe_d2_034_uw_basefill_039'], 'func': uw_base_universe_d3_034_uw_basefill_039}


def uw_base_universe_d3_035_uw_basefill_040(uw_base_universe_d2_035_uw_basefill_040):
    return _base_universe_d3(uw_base_universe_d2_035_uw_basefill_040, 35)
UW_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['uw_base_universe_d3_035_uw_basefill_040'] = {'inputs': ['uw_base_universe_d2_035_uw_basefill_040'], 'func': uw_base_universe_d3_035_uw_basefill_040}


def uw_base_universe_d3_036_uw_basefill_041(uw_base_universe_d2_036_uw_basefill_041):
    return _base_universe_d3(uw_base_universe_d2_036_uw_basefill_041, 36)
UW_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['uw_base_universe_d3_036_uw_basefill_041'] = {'inputs': ['uw_base_universe_d2_036_uw_basefill_041'], 'func': uw_base_universe_d3_036_uw_basefill_041}


def uw_base_universe_d3_037_uw_basefill_042(uw_base_universe_d2_037_uw_basefill_042):
    return _base_universe_d3(uw_base_universe_d2_037_uw_basefill_042, 37)
UW_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['uw_base_universe_d3_037_uw_basefill_042'] = {'inputs': ['uw_base_universe_d2_037_uw_basefill_042'], 'func': uw_base_universe_d3_037_uw_basefill_042}


def uw_base_universe_d3_038_uw_basefill_043(uw_base_universe_d2_038_uw_basefill_043):
    return _base_universe_d3(uw_base_universe_d2_038_uw_basefill_043, 38)
UW_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['uw_base_universe_d3_038_uw_basefill_043'] = {'inputs': ['uw_base_universe_d2_038_uw_basefill_043'], 'func': uw_base_universe_d3_038_uw_basefill_043}


def uw_base_universe_d3_039_uw_basefill_044(uw_base_universe_d2_039_uw_basefill_044):
    return _base_universe_d3(uw_base_universe_d2_039_uw_basefill_044, 39)
UW_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['uw_base_universe_d3_039_uw_basefill_044'] = {'inputs': ['uw_base_universe_d2_039_uw_basefill_044'], 'func': uw_base_universe_d3_039_uw_basefill_044}


def uw_base_universe_d3_040_uw_basefill_045(uw_base_universe_d2_040_uw_basefill_045):
    return _base_universe_d3(uw_base_universe_d2_040_uw_basefill_045, 40)
UW_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['uw_base_universe_d3_040_uw_basefill_045'] = {'inputs': ['uw_base_universe_d2_040_uw_basefill_045'], 'func': uw_base_universe_d3_040_uw_basefill_045}


def uw_base_universe_d3_041_uw_basefill_046(uw_base_universe_d2_041_uw_basefill_046):
    return _base_universe_d3(uw_base_universe_d2_041_uw_basefill_046, 41)
UW_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['uw_base_universe_d3_041_uw_basefill_046'] = {'inputs': ['uw_base_universe_d2_041_uw_basefill_046'], 'func': uw_base_universe_d3_041_uw_basefill_046}


def uw_base_universe_d3_042_uw_basefill_047(uw_base_universe_d2_042_uw_basefill_047):
    return _base_universe_d3(uw_base_universe_d2_042_uw_basefill_047, 42)
UW_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['uw_base_universe_d3_042_uw_basefill_047'] = {'inputs': ['uw_base_universe_d2_042_uw_basefill_047'], 'func': uw_base_universe_d3_042_uw_basefill_047}


def uw_base_universe_d3_043_uw_basefill_048(uw_base_universe_d2_043_uw_basefill_048):
    return _base_universe_d3(uw_base_universe_d2_043_uw_basefill_048, 43)
UW_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['uw_base_universe_d3_043_uw_basefill_048'] = {'inputs': ['uw_base_universe_d2_043_uw_basefill_048'], 'func': uw_base_universe_d3_043_uw_basefill_048}


def uw_base_universe_d3_044_uw_basefill_049(uw_base_universe_d2_044_uw_basefill_049):
    return _base_universe_d3(uw_base_universe_d2_044_uw_basefill_049, 44)
UW_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['uw_base_universe_d3_044_uw_basefill_049'] = {'inputs': ['uw_base_universe_d2_044_uw_basefill_049'], 'func': uw_base_universe_d3_044_uw_basefill_049}


def uw_base_universe_d3_045_uw_basefill_050(uw_base_universe_d2_045_uw_basefill_050):
    return _base_universe_d3(uw_base_universe_d2_045_uw_basefill_050, 45)
UW_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['uw_base_universe_d3_045_uw_basefill_050'] = {'inputs': ['uw_base_universe_d2_045_uw_basefill_050'], 'func': uw_base_universe_d3_045_uw_basefill_050}


def uw_base_universe_d3_046_uw_basefill_051(uw_base_universe_d2_046_uw_basefill_051):
    return _base_universe_d3(uw_base_universe_d2_046_uw_basefill_051, 46)
UW_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['uw_base_universe_d3_046_uw_basefill_051'] = {'inputs': ['uw_base_universe_d2_046_uw_basefill_051'], 'func': uw_base_universe_d3_046_uw_basefill_051}


def uw_base_universe_d3_047_uw_basefill_052(uw_base_universe_d2_047_uw_basefill_052):
    return _base_universe_d3(uw_base_universe_d2_047_uw_basefill_052, 47)
UW_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['uw_base_universe_d3_047_uw_basefill_052'] = {'inputs': ['uw_base_universe_d2_047_uw_basefill_052'], 'func': uw_base_universe_d3_047_uw_basefill_052}


def uw_base_universe_d3_048_uw_basefill_053(uw_base_universe_d2_048_uw_basefill_053):
    return _base_universe_d3(uw_base_universe_d2_048_uw_basefill_053, 48)
UW_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['uw_base_universe_d3_048_uw_basefill_053'] = {'inputs': ['uw_base_universe_d2_048_uw_basefill_053'], 'func': uw_base_universe_d3_048_uw_basefill_053}


def uw_base_universe_d3_049_uw_basefill_054(uw_base_universe_d2_049_uw_basefill_054):
    return _base_universe_d3(uw_base_universe_d2_049_uw_basefill_054, 49)
UW_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['uw_base_universe_d3_049_uw_basefill_054'] = {'inputs': ['uw_base_universe_d2_049_uw_basefill_054'], 'func': uw_base_universe_d3_049_uw_basefill_054}


def uw_base_universe_d3_050_uw_basefill_055(uw_base_universe_d2_050_uw_basefill_055):
    return _base_universe_d3(uw_base_universe_d2_050_uw_basefill_055, 50)
UW_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['uw_base_universe_d3_050_uw_basefill_055'] = {'inputs': ['uw_base_universe_d2_050_uw_basefill_055'], 'func': uw_base_universe_d3_050_uw_basefill_055}


def uw_base_universe_d3_051_uw_basefill_056(uw_base_universe_d2_051_uw_basefill_056):
    return _base_universe_d3(uw_base_universe_d2_051_uw_basefill_056, 51)
UW_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['uw_base_universe_d3_051_uw_basefill_056'] = {'inputs': ['uw_base_universe_d2_051_uw_basefill_056'], 'func': uw_base_universe_d3_051_uw_basefill_056}


def uw_base_universe_d3_052_uw_basefill_057(uw_base_universe_d2_052_uw_basefill_057):
    return _base_universe_d3(uw_base_universe_d2_052_uw_basefill_057, 52)
UW_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['uw_base_universe_d3_052_uw_basefill_057'] = {'inputs': ['uw_base_universe_d2_052_uw_basefill_057'], 'func': uw_base_universe_d3_052_uw_basefill_057}


def uw_base_universe_d3_053_uw_basefill_058(uw_base_universe_d2_053_uw_basefill_058):
    return _base_universe_d3(uw_base_universe_d2_053_uw_basefill_058, 53)
UW_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['uw_base_universe_d3_053_uw_basefill_058'] = {'inputs': ['uw_base_universe_d2_053_uw_basefill_058'], 'func': uw_base_universe_d3_053_uw_basefill_058}


def uw_base_universe_d3_054_uw_basefill_059(uw_base_universe_d2_054_uw_basefill_059):
    return _base_universe_d3(uw_base_universe_d2_054_uw_basefill_059, 54)
UW_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['uw_base_universe_d3_054_uw_basefill_059'] = {'inputs': ['uw_base_universe_d2_054_uw_basefill_059'], 'func': uw_base_universe_d3_054_uw_basefill_059}


def uw_base_universe_d3_055_uw_basefill_060(uw_base_universe_d2_055_uw_basefill_060):
    return _base_universe_d3(uw_base_universe_d2_055_uw_basefill_060, 55)
UW_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['uw_base_universe_d3_055_uw_basefill_060'] = {'inputs': ['uw_base_universe_d2_055_uw_basefill_060'], 'func': uw_base_universe_d3_055_uw_basefill_060}


def uw_base_universe_d3_056_uw_basefill_061(uw_base_universe_d2_056_uw_basefill_061):
    return _base_universe_d3(uw_base_universe_d2_056_uw_basefill_061, 56)
UW_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['uw_base_universe_d3_056_uw_basefill_061'] = {'inputs': ['uw_base_universe_d2_056_uw_basefill_061'], 'func': uw_base_universe_d3_056_uw_basefill_061}


def uw_base_universe_d3_057_uw_basefill_062(uw_base_universe_d2_057_uw_basefill_062):
    return _base_universe_d3(uw_base_universe_d2_057_uw_basefill_062, 57)
UW_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['uw_base_universe_d3_057_uw_basefill_062'] = {'inputs': ['uw_base_universe_d2_057_uw_basefill_062'], 'func': uw_base_universe_d3_057_uw_basefill_062}


def uw_base_universe_d3_058_uw_basefill_063(uw_base_universe_d2_058_uw_basefill_063):
    return _base_universe_d3(uw_base_universe_d2_058_uw_basefill_063, 58)
UW_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['uw_base_universe_d3_058_uw_basefill_063'] = {'inputs': ['uw_base_universe_d2_058_uw_basefill_063'], 'func': uw_base_universe_d3_058_uw_basefill_063}


def uw_base_universe_d3_059_uw_basefill_064(uw_base_universe_d2_059_uw_basefill_064):
    return _base_universe_d3(uw_base_universe_d2_059_uw_basefill_064, 59)
UW_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['uw_base_universe_d3_059_uw_basefill_064'] = {'inputs': ['uw_base_universe_d2_059_uw_basefill_064'], 'func': uw_base_universe_d3_059_uw_basefill_064}


def uw_base_universe_d3_060_uw_basefill_065(uw_base_universe_d2_060_uw_basefill_065):
    return _base_universe_d3(uw_base_universe_d2_060_uw_basefill_065, 60)
UW_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['uw_base_universe_d3_060_uw_basefill_065'] = {'inputs': ['uw_base_universe_d2_060_uw_basefill_065'], 'func': uw_base_universe_d3_060_uw_basefill_065}


def uw_base_universe_d3_061_uw_basefill_066(uw_base_universe_d2_061_uw_basefill_066):
    return _base_universe_d3(uw_base_universe_d2_061_uw_basefill_066, 61)
UW_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['uw_base_universe_d3_061_uw_basefill_066'] = {'inputs': ['uw_base_universe_d2_061_uw_basefill_066'], 'func': uw_base_universe_d3_061_uw_basefill_066}


def uw_base_universe_d3_062_uw_basefill_067(uw_base_universe_d2_062_uw_basefill_067):
    return _base_universe_d3(uw_base_universe_d2_062_uw_basefill_067, 62)
UW_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['uw_base_universe_d3_062_uw_basefill_067'] = {'inputs': ['uw_base_universe_d2_062_uw_basefill_067'], 'func': uw_base_universe_d3_062_uw_basefill_067}


def uw_base_universe_d3_063_uw_basefill_068(uw_base_universe_d2_063_uw_basefill_068):
    return _base_universe_d3(uw_base_universe_d2_063_uw_basefill_068, 63)
UW_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['uw_base_universe_d3_063_uw_basefill_068'] = {'inputs': ['uw_base_universe_d2_063_uw_basefill_068'], 'func': uw_base_universe_d3_063_uw_basefill_068}


def uw_base_universe_d3_064_uw_basefill_069(uw_base_universe_d2_064_uw_basefill_069):
    return _base_universe_d3(uw_base_universe_d2_064_uw_basefill_069, 64)
UW_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['uw_base_universe_d3_064_uw_basefill_069'] = {'inputs': ['uw_base_universe_d2_064_uw_basefill_069'], 'func': uw_base_universe_d3_064_uw_basefill_069}


def uw_base_universe_d3_065_uw_basefill_070(uw_base_universe_d2_065_uw_basefill_070):
    return _base_universe_d3(uw_base_universe_d2_065_uw_basefill_070, 65)
UW_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['uw_base_universe_d3_065_uw_basefill_070'] = {'inputs': ['uw_base_universe_d2_065_uw_basefill_070'], 'func': uw_base_universe_d3_065_uw_basefill_070}


def uw_base_universe_d3_066_uw_basefill_071(uw_base_universe_d2_066_uw_basefill_071):
    return _base_universe_d3(uw_base_universe_d2_066_uw_basefill_071, 66)
UW_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['uw_base_universe_d3_066_uw_basefill_071'] = {'inputs': ['uw_base_universe_d2_066_uw_basefill_071'], 'func': uw_base_universe_d3_066_uw_basefill_071}


def uw_base_universe_d3_067_uw_basefill_072(uw_base_universe_d2_067_uw_basefill_072):
    return _base_universe_d3(uw_base_universe_d2_067_uw_basefill_072, 67)
UW_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['uw_base_universe_d3_067_uw_basefill_072'] = {'inputs': ['uw_base_universe_d2_067_uw_basefill_072'], 'func': uw_base_universe_d3_067_uw_basefill_072}


def uw_base_universe_d3_068_uw_basefill_073(uw_base_universe_d2_068_uw_basefill_073):
    return _base_universe_d3(uw_base_universe_d2_068_uw_basefill_073, 68)
UW_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['uw_base_universe_d3_068_uw_basefill_073'] = {'inputs': ['uw_base_universe_d2_068_uw_basefill_073'], 'func': uw_base_universe_d3_068_uw_basefill_073}


def uw_base_universe_d3_069_uw_basefill_074(uw_base_universe_d2_069_uw_basefill_074):
    return _base_universe_d3(uw_base_universe_d2_069_uw_basefill_074, 69)
UW_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['uw_base_universe_d3_069_uw_basefill_074'] = {'inputs': ['uw_base_universe_d2_069_uw_basefill_074'], 'func': uw_base_universe_d3_069_uw_basefill_074}


def uw_base_universe_d3_070_uw_basefill_075(uw_base_universe_d2_070_uw_basefill_075):
    return _base_universe_d3(uw_base_universe_d2_070_uw_basefill_075, 70)
UW_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['uw_base_universe_d3_070_uw_basefill_075'] = {'inputs': ['uw_base_universe_d2_070_uw_basefill_075'], 'func': uw_base_universe_d3_070_uw_basefill_075}
