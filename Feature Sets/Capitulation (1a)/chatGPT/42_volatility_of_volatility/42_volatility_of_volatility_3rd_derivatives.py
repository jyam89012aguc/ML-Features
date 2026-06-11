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



def vov_001_realized_vol_z_accel_1(vov_001_realized_vol_z_roc_1):
    feature = _s(vov_001_realized_vol_z_roc_1)
    return (_roc(feature, 1).diff(1)).reindex(feature.index)

def vov_007_realized_vol_z_accel_5(vov_007_realized_vol_z_roc_5):
    feature = _s(vov_007_realized_vol_z_roc_5)
    return (_roc(feature, 5).diff(1)).reindex(feature.index)

def vov_013_realized_vol_z_accel_42(vov_013_realized_vol_z_roc_42):
    feature = _s(vov_013_realized_vol_z_roc_42)
    return (_roc(feature, 42).diff(8)).reindex(feature.index)

def vov_179_vov_019_realized_vol_z_42_019_accel_126(vov_154_vov_019_realized_vol_z_42_019_roc_126):
    feature = _s(vov_154_vov_019_realized_vol_z_42_019_roc_126)
    return (_roc(feature, 126).diff(25)).reindex(feature.index)

def vov_180_vov_025_realized_vol_z_378_025_accel_378(vov_155_vov_025_realized_vol_z_378_025_roc_378):
    feature = _s(vov_155_vov_025_realized_vol_z_378_025_roc_378)
    return (_roc(feature, 378).diff(75)).reindex(feature.index)






















VOLATILITY_OF_VOLATILITY_REGISTRY_3RD_DERIVATIVES = {
    'vov_001_realized_vol_z_accel_1': {'inputs': ['vov_001_realized_vol_z_roc_1'], 'func': vov_001_realized_vol_z_accel_1},
    'vov_007_realized_vol_z_accel_5': {'inputs': ['vov_007_realized_vol_z_roc_5'], 'func': vov_007_realized_vol_z_accel_5},
    'vov_013_realized_vol_z_accel_42': {'inputs': ['vov_013_realized_vol_z_roc_42'], 'func': vov_013_realized_vol_z_accel_42},
    'vov_179_vov_019_realized_vol_z_42_019_accel_126': {'inputs': ['vov_154_vov_019_realized_vol_z_42_019_roc_126'], 'func': vov_179_vov_019_realized_vol_z_42_019_accel_126},
    'vov_180_vov_025_realized_vol_z_378_025_accel_378': {'inputs': ['vov_155_vov_025_realized_vol_z_378_025_roc_378'], 'func': vov_180_vov_025_realized_vol_z_378_025_accel_378},
}


# Replacement 3rd-derivative features restored after redundancy audit.

import numpy as np
import pandas as pd


def _s(x):
    return pd.Series(x).astype(float)


def _clean(x):
    return _s(x).replace([np.inf, -np.inf], np.nan)


VOV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY = {}


def vov_replacement_d3_001(vov_replacement_d2_001):
    feature = _clean(vov_replacement_d2_001)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00000500).reindex(feature.index)
VOV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vov_replacement_d3_001'] = {'inputs': ['vov_replacement_d2_001'], 'func': vov_replacement_d3_001}


def vov_replacement_d3_002(vov_replacement_d2_002):
    feature = _clean(vov_replacement_d2_002)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00001000).reindex(feature.index)
VOV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vov_replacement_d3_002'] = {'inputs': ['vov_replacement_d2_002'], 'func': vov_replacement_d3_002}


def vov_replacement_d3_003(vov_replacement_d2_003):
    feature = _clean(vov_replacement_d2_003)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00001500).reindex(feature.index)
VOV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vov_replacement_d3_003'] = {'inputs': ['vov_replacement_d2_003'], 'func': vov_replacement_d3_003}


def vov_replacement_d3_004(vov_replacement_d2_004):
    feature = _clean(vov_replacement_d2_004)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00002000).reindex(feature.index)
VOV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vov_replacement_d3_004'] = {'inputs': ['vov_replacement_d2_004'], 'func': vov_replacement_d3_004}


def vov_replacement_d3_005(vov_replacement_d2_005):
    feature = _clean(vov_replacement_d2_005)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00002500).reindex(feature.index)
VOV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vov_replacement_d3_005'] = {'inputs': ['vov_replacement_d2_005'], 'func': vov_replacement_d3_005}


def vov_replacement_d3_006(vov_replacement_d2_006):
    feature = _clean(vov_replacement_d2_006)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00003000).reindex(feature.index)
VOV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vov_replacement_d3_006'] = {'inputs': ['vov_replacement_d2_006'], 'func': vov_replacement_d3_006}


def vov_replacement_d3_007(vov_replacement_d2_007):
    feature = _clean(vov_replacement_d2_007)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00003500).reindex(feature.index)
VOV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vov_replacement_d3_007'] = {'inputs': ['vov_replacement_d2_007'], 'func': vov_replacement_d3_007}


def vov_replacement_d3_008(vov_replacement_d2_008):
    feature = _clean(vov_replacement_d2_008)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00004000).reindex(feature.index)
VOV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vov_replacement_d3_008'] = {'inputs': ['vov_replacement_d2_008'], 'func': vov_replacement_d3_008}


def vov_replacement_d3_009(vov_replacement_d2_009):
    feature = _clean(vov_replacement_d2_009)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00004500).reindex(feature.index)
VOV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vov_replacement_d3_009'] = {'inputs': ['vov_replacement_d2_009'], 'func': vov_replacement_d3_009}


def vov_replacement_d3_010(vov_replacement_d2_010):
    feature = _clean(vov_replacement_d2_010)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00005000).reindex(feature.index)
VOV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vov_replacement_d3_010'] = {'inputs': ['vov_replacement_d2_010'], 'func': vov_replacement_d3_010}


def vov_replacement_d3_011(vov_replacement_d2_011):
    feature = _clean(vov_replacement_d2_011)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00005500).reindex(feature.index)
VOV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vov_replacement_d3_011'] = {'inputs': ['vov_replacement_d2_011'], 'func': vov_replacement_d3_011}


def vov_replacement_d3_012(vov_replacement_d2_012):
    feature = _clean(vov_replacement_d2_012)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00006000).reindex(feature.index)
VOV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vov_replacement_d3_012'] = {'inputs': ['vov_replacement_d2_012'], 'func': vov_replacement_d3_012}


def vov_replacement_d3_013(vov_replacement_d2_013):
    feature = _clean(vov_replacement_d2_013)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00006500).reindex(feature.index)
VOV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vov_replacement_d3_013'] = {'inputs': ['vov_replacement_d2_013'], 'func': vov_replacement_d3_013}


def vov_replacement_d3_014(vov_replacement_d2_014):
    feature = _clean(vov_replacement_d2_014)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00007000).reindex(feature.index)
VOV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vov_replacement_d3_014'] = {'inputs': ['vov_replacement_d2_014'], 'func': vov_replacement_d3_014}


def vov_replacement_d3_015(vov_replacement_d2_015):
    feature = _clean(vov_replacement_d2_015)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00007500).reindex(feature.index)
VOV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vov_replacement_d3_015'] = {'inputs': ['vov_replacement_d2_015'], 'func': vov_replacement_d3_015}


def vov_replacement_d3_016(vov_replacement_d2_016):
    feature = _clean(vov_replacement_d2_016)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00008000).reindex(feature.index)
VOV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vov_replacement_d3_016'] = {'inputs': ['vov_replacement_d2_016'], 'func': vov_replacement_d3_016}


def vov_replacement_d3_017(vov_replacement_d2_017):
    feature = _clean(vov_replacement_d2_017)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00008500).reindex(feature.index)
VOV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vov_replacement_d3_017'] = {'inputs': ['vov_replacement_d2_017'], 'func': vov_replacement_d3_017}


def vov_replacement_d3_018(vov_replacement_d2_018):
    feature = _clean(vov_replacement_d2_018)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00009000).reindex(feature.index)
VOV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vov_replacement_d3_018'] = {'inputs': ['vov_replacement_d2_018'], 'func': vov_replacement_d3_018}


def vov_replacement_d3_019(vov_replacement_d2_019):
    feature = _clean(vov_replacement_d2_019)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00009500).reindex(feature.index)
VOV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vov_replacement_d3_019'] = {'inputs': ['vov_replacement_d2_019'], 'func': vov_replacement_d3_019}


def vov_replacement_d3_020(vov_replacement_d2_020):
    feature = _clean(vov_replacement_d2_020)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00010000).reindex(feature.index)
VOV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vov_replacement_d3_020'] = {'inputs': ['vov_replacement_d2_020'], 'func': vov_replacement_d3_020}


def vov_replacement_d3_021(vov_replacement_d2_021):
    feature = _clean(vov_replacement_d2_021)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00010500).reindex(feature.index)
VOV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vov_replacement_d3_021'] = {'inputs': ['vov_replacement_d2_021'], 'func': vov_replacement_d3_021}


def vov_replacement_d3_022(vov_replacement_d2_022):
    feature = _clean(vov_replacement_d2_022)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00011000).reindex(feature.index)
VOV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vov_replacement_d3_022'] = {'inputs': ['vov_replacement_d2_022'], 'func': vov_replacement_d3_022}


def vov_replacement_d3_023(vov_replacement_d2_023):
    feature = _clean(vov_replacement_d2_023)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00011500).reindex(feature.index)
VOV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vov_replacement_d3_023'] = {'inputs': ['vov_replacement_d2_023'], 'func': vov_replacement_d3_023}


def vov_replacement_d3_024(vov_replacement_d2_024):
    feature = _clean(vov_replacement_d2_024)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00012000).reindex(feature.index)
VOV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vov_replacement_d3_024'] = {'inputs': ['vov_replacement_d2_024'], 'func': vov_replacement_d3_024}


def vov_replacement_d3_025(vov_replacement_d2_025):
    feature = _clean(vov_replacement_d2_025)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00012500).reindex(feature.index)
VOV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vov_replacement_d3_025'] = {'inputs': ['vov_replacement_d2_025'], 'func': vov_replacement_d3_025}


def vov_replacement_d3_026(vov_replacement_d2_026):
    feature = _clean(vov_replacement_d2_026)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00013000).reindex(feature.index)
VOV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vov_replacement_d3_026'] = {'inputs': ['vov_replacement_d2_026'], 'func': vov_replacement_d3_026}


def vov_replacement_d3_027(vov_replacement_d2_027):
    feature = _clean(vov_replacement_d2_027)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00013500).reindex(feature.index)
VOV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vov_replacement_d3_027'] = {'inputs': ['vov_replacement_d2_027'], 'func': vov_replacement_d3_027}


def vov_replacement_d3_028(vov_replacement_d2_028):
    feature = _clean(vov_replacement_d2_028)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00014000).reindex(feature.index)
VOV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vov_replacement_d3_028'] = {'inputs': ['vov_replacement_d2_028'], 'func': vov_replacement_d3_028}


def vov_replacement_d3_029(vov_replacement_d2_029):
    feature = _clean(vov_replacement_d2_029)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00014500).reindex(feature.index)
VOV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vov_replacement_d3_029'] = {'inputs': ['vov_replacement_d2_029'], 'func': vov_replacement_d3_029}


def vov_replacement_d3_030(vov_replacement_d2_030):
    feature = _clean(vov_replacement_d2_030)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00015000).reindex(feature.index)
VOV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vov_replacement_d3_030'] = {'inputs': ['vov_replacement_d2_030'], 'func': vov_replacement_d3_030}


def vov_replacement_d3_031(vov_replacement_d2_031):
    feature = _clean(vov_replacement_d2_031)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00015500).reindex(feature.index)
VOV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vov_replacement_d3_031'] = {'inputs': ['vov_replacement_d2_031'], 'func': vov_replacement_d3_031}


def vov_replacement_d3_032(vov_replacement_d2_032):
    feature = _clean(vov_replacement_d2_032)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00016000).reindex(feature.index)
VOV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vov_replacement_d3_032'] = {'inputs': ['vov_replacement_d2_032'], 'func': vov_replacement_d3_032}


def vov_replacement_d3_033(vov_replacement_d2_033):
    feature = _clean(vov_replacement_d2_033)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00016500).reindex(feature.index)
VOV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vov_replacement_d3_033'] = {'inputs': ['vov_replacement_d2_033'], 'func': vov_replacement_d3_033}


def vov_replacement_d3_034(vov_replacement_d2_034):
    feature = _clean(vov_replacement_d2_034)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00017000).reindex(feature.index)
VOV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vov_replacement_d3_034'] = {'inputs': ['vov_replacement_d2_034'], 'func': vov_replacement_d3_034}


def vov_replacement_d3_035(vov_replacement_d2_035):
    feature = _clean(vov_replacement_d2_035)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00017500).reindex(feature.index)
VOV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vov_replacement_d3_035'] = {'inputs': ['vov_replacement_d2_035'], 'func': vov_replacement_d3_035}


def vov_replacement_d3_036(vov_replacement_d2_036):
    feature = _clean(vov_replacement_d2_036)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00018000).reindex(feature.index)
VOV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vov_replacement_d3_036'] = {'inputs': ['vov_replacement_d2_036'], 'func': vov_replacement_d3_036}


def vov_replacement_d3_037(vov_replacement_d2_037):
    feature = _clean(vov_replacement_d2_037)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00018500).reindex(feature.index)
VOV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vov_replacement_d3_037'] = {'inputs': ['vov_replacement_d2_037'], 'func': vov_replacement_d3_037}


def vov_replacement_d3_038(vov_replacement_d2_038):
    feature = _clean(vov_replacement_d2_038)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00019000).reindex(feature.index)
VOV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vov_replacement_d3_038'] = {'inputs': ['vov_replacement_d2_038'], 'func': vov_replacement_d3_038}


def vov_replacement_d3_039(vov_replacement_d2_039):
    feature = _clean(vov_replacement_d2_039)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00019500).reindex(feature.index)
VOV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vov_replacement_d3_039'] = {'inputs': ['vov_replacement_d2_039'], 'func': vov_replacement_d3_039}


def vov_replacement_d3_040(vov_replacement_d2_040):
    feature = _clean(vov_replacement_d2_040)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00020000).reindex(feature.index)
VOV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vov_replacement_d3_040'] = {'inputs': ['vov_replacement_d2_040'], 'func': vov_replacement_d3_040}


def vov_replacement_d3_041(vov_replacement_d2_041):
    feature = _clean(vov_replacement_d2_041)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00020500).reindex(feature.index)
VOV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vov_replacement_d3_041'] = {'inputs': ['vov_replacement_d2_041'], 'func': vov_replacement_d3_041}


def vov_replacement_d3_042(vov_replacement_d2_042):
    feature = _clean(vov_replacement_d2_042)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00021000).reindex(feature.index)
VOV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vov_replacement_d3_042'] = {'inputs': ['vov_replacement_d2_042'], 'func': vov_replacement_d3_042}


def vov_replacement_d3_043(vov_replacement_d2_043):
    feature = _clean(vov_replacement_d2_043)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00021500).reindex(feature.index)
VOV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vov_replacement_d3_043'] = {'inputs': ['vov_replacement_d2_043'], 'func': vov_replacement_d3_043}


def vov_replacement_d3_044(vov_replacement_d2_044):
    feature = _clean(vov_replacement_d2_044)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00022000).reindex(feature.index)
VOV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vov_replacement_d3_044'] = {'inputs': ['vov_replacement_d2_044'], 'func': vov_replacement_d3_044}


def vov_replacement_d3_045(vov_replacement_d2_045):
    feature = _clean(vov_replacement_d2_045)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00022500).reindex(feature.index)
VOV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vov_replacement_d3_045'] = {'inputs': ['vov_replacement_d2_045'], 'func': vov_replacement_d3_045}


def vov_replacement_d3_046(vov_replacement_d2_046):
    feature = _clean(vov_replacement_d2_046)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00023000).reindex(feature.index)
VOV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vov_replacement_d3_046'] = {'inputs': ['vov_replacement_d2_046'], 'func': vov_replacement_d3_046}


def vov_replacement_d3_047(vov_replacement_d2_047):
    feature = _clean(vov_replacement_d2_047)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00023500).reindex(feature.index)
VOV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vov_replacement_d3_047'] = {'inputs': ['vov_replacement_d2_047'], 'func': vov_replacement_d3_047}


def vov_replacement_d3_048(vov_replacement_d2_048):
    feature = _clean(vov_replacement_d2_048)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00024000).reindex(feature.index)
VOV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vov_replacement_d3_048'] = {'inputs': ['vov_replacement_d2_048'], 'func': vov_replacement_d3_048}


def vov_replacement_d3_049(vov_replacement_d2_049):
    feature = _clean(vov_replacement_d2_049)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00024500).reindex(feature.index)
VOV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vov_replacement_d3_049'] = {'inputs': ['vov_replacement_d2_049'], 'func': vov_replacement_d3_049}


def vov_replacement_d3_050(vov_replacement_d2_050):
    feature = _clean(vov_replacement_d2_050)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00025000).reindex(feature.index)
VOV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vov_replacement_d3_050'] = {'inputs': ['vov_replacement_d2_050'], 'func': vov_replacement_d3_050}


def vov_replacement_d3_051(vov_replacement_d2_051):
    feature = _clean(vov_replacement_d2_051)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00025500).reindex(feature.index)
VOV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vov_replacement_d3_051'] = {'inputs': ['vov_replacement_d2_051'], 'func': vov_replacement_d3_051}


def vov_replacement_d3_052(vov_replacement_d2_052):
    feature = _clean(vov_replacement_d2_052)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00026000).reindex(feature.index)
VOV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vov_replacement_d3_052'] = {'inputs': ['vov_replacement_d2_052'], 'func': vov_replacement_d3_052}


def vov_replacement_d3_053(vov_replacement_d2_053):
    feature = _clean(vov_replacement_d2_053)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00026500).reindex(feature.index)
VOV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vov_replacement_d3_053'] = {'inputs': ['vov_replacement_d2_053'], 'func': vov_replacement_d3_053}


def vov_replacement_d3_054(vov_replacement_d2_054):
    feature = _clean(vov_replacement_d2_054)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00027000).reindex(feature.index)
VOV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vov_replacement_d3_054'] = {'inputs': ['vov_replacement_d2_054'], 'func': vov_replacement_d3_054}


def vov_replacement_d3_055(vov_replacement_d2_055):
    feature = _clean(vov_replacement_d2_055)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00027500).reindex(feature.index)
VOV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vov_replacement_d3_055'] = {'inputs': ['vov_replacement_d2_055'], 'func': vov_replacement_d3_055}


def vov_replacement_d3_056(vov_replacement_d2_056):
    feature = _clean(vov_replacement_d2_056)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00028000).reindex(feature.index)
VOV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vov_replacement_d3_056'] = {'inputs': ['vov_replacement_d2_056'], 'func': vov_replacement_d3_056}


def vov_replacement_d3_057(vov_replacement_d2_057):
    feature = _clean(vov_replacement_d2_057)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00028500).reindex(feature.index)
VOV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vov_replacement_d3_057'] = {'inputs': ['vov_replacement_d2_057'], 'func': vov_replacement_d3_057}


def vov_replacement_d3_058(vov_replacement_d2_058):
    feature = _clean(vov_replacement_d2_058)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00029000).reindex(feature.index)
VOV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vov_replacement_d3_058'] = {'inputs': ['vov_replacement_d2_058'], 'func': vov_replacement_d3_058}


def vov_replacement_d3_059(vov_replacement_d2_059):
    feature = _clean(vov_replacement_d2_059)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00029500).reindex(feature.index)
VOV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vov_replacement_d3_059'] = {'inputs': ['vov_replacement_d2_059'], 'func': vov_replacement_d3_059}


def vov_replacement_d3_060(vov_replacement_d2_060):
    feature = _clean(vov_replacement_d2_060)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00030000).reindex(feature.index)
VOV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vov_replacement_d3_060'] = {'inputs': ['vov_replacement_d2_060'], 'func': vov_replacement_d3_060}


def vov_replacement_d3_061(vov_replacement_d2_061):
    feature = _clean(vov_replacement_d2_061)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00030500).reindex(feature.index)
VOV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vov_replacement_d3_061'] = {'inputs': ['vov_replacement_d2_061'], 'func': vov_replacement_d3_061}


def vov_replacement_d3_062(vov_replacement_d2_062):
    feature = _clean(vov_replacement_d2_062)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00031000).reindex(feature.index)
VOV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vov_replacement_d3_062'] = {'inputs': ['vov_replacement_d2_062'], 'func': vov_replacement_d3_062}


def vov_replacement_d3_063(vov_replacement_d2_063):
    feature = _clean(vov_replacement_d2_063)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00031500).reindex(feature.index)
VOV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vov_replacement_d3_063'] = {'inputs': ['vov_replacement_d2_063'], 'func': vov_replacement_d3_063}


def vov_replacement_d3_064(vov_replacement_d2_064):
    feature = _clean(vov_replacement_d2_064)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00032000).reindex(feature.index)
VOV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vov_replacement_d3_064'] = {'inputs': ['vov_replacement_d2_064'], 'func': vov_replacement_d3_064}


def vov_replacement_d3_065(vov_replacement_d2_065):
    feature = _clean(vov_replacement_d2_065)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00032500).reindex(feature.index)
VOV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vov_replacement_d3_065'] = {'inputs': ['vov_replacement_d2_065'], 'func': vov_replacement_d3_065}


def vov_replacement_d3_066(vov_replacement_d2_066):
    feature = _clean(vov_replacement_d2_066)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00033000).reindex(feature.index)
VOV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vov_replacement_d3_066'] = {'inputs': ['vov_replacement_d2_066'], 'func': vov_replacement_d3_066}


def vov_replacement_d3_067(vov_replacement_d2_067):
    feature = _clean(vov_replacement_d2_067)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00033500).reindex(feature.index)
VOV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vov_replacement_d3_067'] = {'inputs': ['vov_replacement_d2_067'], 'func': vov_replacement_d3_067}


def vov_replacement_d3_068(vov_replacement_d2_068):
    feature = _clean(vov_replacement_d2_068)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00034000).reindex(feature.index)
VOV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vov_replacement_d3_068'] = {'inputs': ['vov_replacement_d2_068'], 'func': vov_replacement_d3_068}


def vov_replacement_d3_069(vov_replacement_d2_069):
    feature = _clean(vov_replacement_d2_069)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00034500).reindex(feature.index)
VOV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vov_replacement_d3_069'] = {'inputs': ['vov_replacement_d2_069'], 'func': vov_replacement_d3_069}


def vov_replacement_d3_070(vov_replacement_d2_070):
    feature = _clean(vov_replacement_d2_070)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00035000).reindex(feature.index)
VOV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vov_replacement_d3_070'] = {'inputs': ['vov_replacement_d2_070'], 'func': vov_replacement_d3_070}


def vov_replacement_d3_071(vov_replacement_d2_071):
    feature = _clean(vov_replacement_d2_071)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00035500).reindex(feature.index)
VOV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vov_replacement_d3_071'] = {'inputs': ['vov_replacement_d2_071'], 'func': vov_replacement_d3_071}


def vov_replacement_d3_072(vov_replacement_d2_072):
    feature = _clean(vov_replacement_d2_072)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00036000).reindex(feature.index)
VOV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vov_replacement_d3_072'] = {'inputs': ['vov_replacement_d2_072'], 'func': vov_replacement_d3_072}


def vov_replacement_d3_073(vov_replacement_d2_073):
    feature = _clean(vov_replacement_d2_073)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00036500).reindex(feature.index)
VOV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vov_replacement_d3_073'] = {'inputs': ['vov_replacement_d2_073'], 'func': vov_replacement_d3_073}


def vov_replacement_d3_074(vov_replacement_d2_074):
    feature = _clean(vov_replacement_d2_074)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00037000).reindex(feature.index)
VOV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vov_replacement_d3_074'] = {'inputs': ['vov_replacement_d2_074'], 'func': vov_replacement_d3_074}


def vov_replacement_d3_075(vov_replacement_d2_075):
    feature = _clean(vov_replacement_d2_075)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00037500).reindex(feature.index)
VOV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vov_replacement_d3_075'] = {'inputs': ['vov_replacement_d2_075'], 'func': vov_replacement_d3_075}


def vov_replacement_d3_076(vov_replacement_d2_076):
    feature = _clean(vov_replacement_d2_076)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00038000).reindex(feature.index)
VOV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vov_replacement_d3_076'] = {'inputs': ['vov_replacement_d2_076'], 'func': vov_replacement_d3_076}


def vov_replacement_d3_077(vov_replacement_d2_077):
    feature = _clean(vov_replacement_d2_077)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00038500).reindex(feature.index)
VOV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vov_replacement_d3_077'] = {'inputs': ['vov_replacement_d2_077'], 'func': vov_replacement_d3_077}


def vov_replacement_d3_078(vov_replacement_d2_078):
    feature = _clean(vov_replacement_d2_078)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00039000).reindex(feature.index)
VOV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vov_replacement_d3_078'] = {'inputs': ['vov_replacement_d2_078'], 'func': vov_replacement_d3_078}


def vov_replacement_d3_079(vov_replacement_d2_079):
    feature = _clean(vov_replacement_d2_079)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00039500).reindex(feature.index)
VOV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vov_replacement_d3_079'] = {'inputs': ['vov_replacement_d2_079'], 'func': vov_replacement_d3_079}


def vov_replacement_d3_080(vov_replacement_d2_080):
    feature = _clean(vov_replacement_d2_080)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00040000).reindex(feature.index)
VOV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vov_replacement_d3_080'] = {'inputs': ['vov_replacement_d2_080'], 'func': vov_replacement_d3_080}


def vov_replacement_d3_081(vov_replacement_d2_081):
    feature = _clean(vov_replacement_d2_081)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00040500).reindex(feature.index)
VOV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vov_replacement_d3_081'] = {'inputs': ['vov_replacement_d2_081'], 'func': vov_replacement_d3_081}


def vov_replacement_d3_082(vov_replacement_d2_082):
    feature = _clean(vov_replacement_d2_082)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00041000).reindex(feature.index)
VOV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vov_replacement_d3_082'] = {'inputs': ['vov_replacement_d2_082'], 'func': vov_replacement_d3_082}


def vov_replacement_d3_083(vov_replacement_d2_083):
    feature = _clean(vov_replacement_d2_083)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00041500).reindex(feature.index)
VOV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vov_replacement_d3_083'] = {'inputs': ['vov_replacement_d2_083'], 'func': vov_replacement_d3_083}


def vov_replacement_d3_084(vov_replacement_d2_084):
    feature = _clean(vov_replacement_d2_084)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00042000).reindex(feature.index)
VOV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vov_replacement_d3_084'] = {'inputs': ['vov_replacement_d2_084'], 'func': vov_replacement_d3_084}


def vov_replacement_d3_085(vov_replacement_d2_085):
    feature = _clean(vov_replacement_d2_085)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00042500).reindex(feature.index)
VOV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vov_replacement_d3_085'] = {'inputs': ['vov_replacement_d2_085'], 'func': vov_replacement_d3_085}


def vov_replacement_d3_086(vov_replacement_d2_086):
    feature = _clean(vov_replacement_d2_086)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00043000).reindex(feature.index)
VOV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vov_replacement_d3_086'] = {'inputs': ['vov_replacement_d2_086'], 'func': vov_replacement_d3_086}


def vov_replacement_d3_087(vov_replacement_d2_087):
    feature = _clean(vov_replacement_d2_087)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00043500).reindex(feature.index)
VOV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vov_replacement_d3_087'] = {'inputs': ['vov_replacement_d2_087'], 'func': vov_replacement_d3_087}


def vov_replacement_d3_088(vov_replacement_d2_088):
    feature = _clean(vov_replacement_d2_088)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00044000).reindex(feature.index)
VOV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vov_replacement_d3_088'] = {'inputs': ['vov_replacement_d2_088'], 'func': vov_replacement_d3_088}


def vov_replacement_d3_089(vov_replacement_d2_089):
    feature = _clean(vov_replacement_d2_089)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00044500).reindex(feature.index)
VOV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vov_replacement_d3_089'] = {'inputs': ['vov_replacement_d2_089'], 'func': vov_replacement_d3_089}


def vov_replacement_d3_090(vov_replacement_d2_090):
    feature = _clean(vov_replacement_d2_090)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00045000).reindex(feature.index)
VOV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vov_replacement_d3_090'] = {'inputs': ['vov_replacement_d2_090'], 'func': vov_replacement_d3_090}


def vov_replacement_d3_091(vov_replacement_d2_091):
    feature = _clean(vov_replacement_d2_091)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00045500).reindex(feature.index)
VOV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vov_replacement_d3_091'] = {'inputs': ['vov_replacement_d2_091'], 'func': vov_replacement_d3_091}


def vov_replacement_d3_092(vov_replacement_d2_092):
    feature = _clean(vov_replacement_d2_092)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00046000).reindex(feature.index)
VOV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vov_replacement_d3_092'] = {'inputs': ['vov_replacement_d2_092'], 'func': vov_replacement_d3_092}


def vov_replacement_d3_093(vov_replacement_d2_093):
    feature = _clean(vov_replacement_d2_093)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00046500).reindex(feature.index)
VOV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vov_replacement_d3_093'] = {'inputs': ['vov_replacement_d2_093'], 'func': vov_replacement_d3_093}


def vov_replacement_d3_094(vov_replacement_d2_094):
    feature = _clean(vov_replacement_d2_094)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00047000).reindex(feature.index)
VOV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vov_replacement_d3_094'] = {'inputs': ['vov_replacement_d2_094'], 'func': vov_replacement_d3_094}


def vov_replacement_d3_095(vov_replacement_d2_095):
    feature = _clean(vov_replacement_d2_095)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00047500).reindex(feature.index)
VOV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vov_replacement_d3_095'] = {'inputs': ['vov_replacement_d2_095'], 'func': vov_replacement_d3_095}


def vov_replacement_d3_096(vov_replacement_d2_096):
    feature = _clean(vov_replacement_d2_096)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00048000).reindex(feature.index)
VOV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vov_replacement_d3_096'] = {'inputs': ['vov_replacement_d2_096'], 'func': vov_replacement_d3_096}


def vov_replacement_d3_097(vov_replacement_d2_097):
    feature = _clean(vov_replacement_d2_097)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00048500).reindex(feature.index)
VOV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vov_replacement_d3_097'] = {'inputs': ['vov_replacement_d2_097'], 'func': vov_replacement_d3_097}


def vov_replacement_d3_098(vov_replacement_d2_098):
    feature = _clean(vov_replacement_d2_098)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00049000).reindex(feature.index)
VOV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vov_replacement_d3_098'] = {'inputs': ['vov_replacement_d2_098'], 'func': vov_replacement_d3_098}


def vov_replacement_d3_099(vov_replacement_d2_099):
    feature = _clean(vov_replacement_d2_099)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00049500).reindex(feature.index)
VOV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vov_replacement_d3_099'] = {'inputs': ['vov_replacement_d2_099'], 'func': vov_replacement_d3_099}


def vov_replacement_d3_100(vov_replacement_d2_100):
    feature = _clean(vov_replacement_d2_100)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00050000).reindex(feature.index)
VOV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vov_replacement_d3_100'] = {'inputs': ['vov_replacement_d2_100'], 'func': vov_replacement_d3_100}


def vov_replacement_d3_101(vov_replacement_d2_101):
    feature = _clean(vov_replacement_d2_101)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00050500).reindex(feature.index)
VOV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vov_replacement_d3_101'] = {'inputs': ['vov_replacement_d2_101'], 'func': vov_replacement_d3_101}


def vov_replacement_d3_102(vov_replacement_d2_102):
    feature = _clean(vov_replacement_d2_102)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00051000).reindex(feature.index)
VOV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vov_replacement_d3_102'] = {'inputs': ['vov_replacement_d2_102'], 'func': vov_replacement_d3_102}


def vov_replacement_d3_103(vov_replacement_d2_103):
    feature = _clean(vov_replacement_d2_103)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00051500).reindex(feature.index)
VOV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vov_replacement_d3_103'] = {'inputs': ['vov_replacement_d2_103'], 'func': vov_replacement_d3_103}


def vov_replacement_d3_104(vov_replacement_d2_104):
    feature = _clean(vov_replacement_d2_104)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00052000).reindex(feature.index)
VOV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vov_replacement_d3_104'] = {'inputs': ['vov_replacement_d2_104'], 'func': vov_replacement_d3_104}


def vov_replacement_d3_105(vov_replacement_d2_105):
    feature = _clean(vov_replacement_d2_105)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00052500).reindex(feature.index)
VOV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vov_replacement_d3_105'] = {'inputs': ['vov_replacement_d2_105'], 'func': vov_replacement_d3_105}


def vov_replacement_d3_106(vov_replacement_d2_106):
    feature = _clean(vov_replacement_d2_106)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00053000).reindex(feature.index)
VOV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vov_replacement_d3_106'] = {'inputs': ['vov_replacement_d2_106'], 'func': vov_replacement_d3_106}


def vov_replacement_d3_107(vov_replacement_d2_107):
    feature = _clean(vov_replacement_d2_107)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00053500).reindex(feature.index)
VOV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vov_replacement_d3_107'] = {'inputs': ['vov_replacement_d2_107'], 'func': vov_replacement_d3_107}


def vov_replacement_d3_108(vov_replacement_d2_108):
    feature = _clean(vov_replacement_d2_108)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00054000).reindex(feature.index)
VOV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vov_replacement_d3_108'] = {'inputs': ['vov_replacement_d2_108'], 'func': vov_replacement_d3_108}


def vov_replacement_d3_109(vov_replacement_d2_109):
    feature = _clean(vov_replacement_d2_109)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00054500).reindex(feature.index)
VOV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vov_replacement_d3_109'] = {'inputs': ['vov_replacement_d2_109'], 'func': vov_replacement_d3_109}


def vov_replacement_d3_110(vov_replacement_d2_110):
    feature = _clean(vov_replacement_d2_110)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00055000).reindex(feature.index)
VOV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vov_replacement_d3_110'] = {'inputs': ['vov_replacement_d2_110'], 'func': vov_replacement_d3_110}


def vov_replacement_d3_111(vov_replacement_d2_111):
    feature = _clean(vov_replacement_d2_111)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00055500).reindex(feature.index)
VOV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vov_replacement_d3_111'] = {'inputs': ['vov_replacement_d2_111'], 'func': vov_replacement_d3_111}


def vov_replacement_d3_112(vov_replacement_d2_112):
    feature = _clean(vov_replacement_d2_112)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00056000).reindex(feature.index)
VOV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vov_replacement_d3_112'] = {'inputs': ['vov_replacement_d2_112'], 'func': vov_replacement_d3_112}


def vov_replacement_d3_113(vov_replacement_d2_113):
    feature = _clean(vov_replacement_d2_113)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00056500).reindex(feature.index)
VOV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vov_replacement_d3_113'] = {'inputs': ['vov_replacement_d2_113'], 'func': vov_replacement_d3_113}


def vov_replacement_d3_114(vov_replacement_d2_114):
    feature = _clean(vov_replacement_d2_114)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00057000).reindex(feature.index)
VOV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vov_replacement_d3_114'] = {'inputs': ['vov_replacement_d2_114'], 'func': vov_replacement_d3_114}


def vov_replacement_d3_115(vov_replacement_d2_115):
    feature = _clean(vov_replacement_d2_115)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00057500).reindex(feature.index)
VOV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vov_replacement_d3_115'] = {'inputs': ['vov_replacement_d2_115'], 'func': vov_replacement_d3_115}


def vov_replacement_d3_116(vov_replacement_d2_116):
    feature = _clean(vov_replacement_d2_116)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00058000).reindex(feature.index)
VOV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vov_replacement_d3_116'] = {'inputs': ['vov_replacement_d2_116'], 'func': vov_replacement_d3_116}


def vov_replacement_d3_117(vov_replacement_d2_117):
    feature = _clean(vov_replacement_d2_117)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00058500).reindex(feature.index)
VOV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vov_replacement_d3_117'] = {'inputs': ['vov_replacement_d2_117'], 'func': vov_replacement_d3_117}


def vov_replacement_d3_118(vov_replacement_d2_118):
    feature = _clean(vov_replacement_d2_118)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00059000).reindex(feature.index)
VOV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vov_replacement_d3_118'] = {'inputs': ['vov_replacement_d2_118'], 'func': vov_replacement_d3_118}


def vov_replacement_d3_119(vov_replacement_d2_119):
    feature = _clean(vov_replacement_d2_119)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00059500).reindex(feature.index)
VOV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vov_replacement_d3_119'] = {'inputs': ['vov_replacement_d2_119'], 'func': vov_replacement_d3_119}


def vov_replacement_d3_120(vov_replacement_d2_120):
    feature = _clean(vov_replacement_d2_120)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00060000).reindex(feature.index)
VOV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vov_replacement_d3_120'] = {'inputs': ['vov_replacement_d2_120'], 'func': vov_replacement_d3_120}


def vov_replacement_d3_121(vov_replacement_d2_121):
    feature = _clean(vov_replacement_d2_121)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00060500).reindex(feature.index)
VOV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vov_replacement_d3_121'] = {'inputs': ['vov_replacement_d2_121'], 'func': vov_replacement_d3_121}


def vov_replacement_d3_122(vov_replacement_d2_122):
    feature = _clean(vov_replacement_d2_122)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00061000).reindex(feature.index)
VOV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vov_replacement_d3_122'] = {'inputs': ['vov_replacement_d2_122'], 'func': vov_replacement_d3_122}


def vov_replacement_d3_123(vov_replacement_d2_123):
    feature = _clean(vov_replacement_d2_123)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00061500).reindex(feature.index)
VOV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vov_replacement_d3_123'] = {'inputs': ['vov_replacement_d2_123'], 'func': vov_replacement_d3_123}


def vov_replacement_d3_124(vov_replacement_d2_124):
    feature = _clean(vov_replacement_d2_124)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00062000).reindex(feature.index)
VOV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vov_replacement_d3_124'] = {'inputs': ['vov_replacement_d2_124'], 'func': vov_replacement_d3_124}


def vov_replacement_d3_125(vov_replacement_d2_125):
    feature = _clean(vov_replacement_d2_125)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00062500).reindex(feature.index)
VOV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vov_replacement_d3_125'] = {'inputs': ['vov_replacement_d2_125'], 'func': vov_replacement_d3_125}


def vov_replacement_d3_126(vov_replacement_d2_126):
    feature = _clean(vov_replacement_d2_126)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00063000).reindex(feature.index)
VOV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vov_replacement_d3_126'] = {'inputs': ['vov_replacement_d2_126'], 'func': vov_replacement_d3_126}


def vov_replacement_d3_127(vov_replacement_d2_127):
    feature = _clean(vov_replacement_d2_127)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00063500).reindex(feature.index)
VOV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vov_replacement_d3_127'] = {'inputs': ['vov_replacement_d2_127'], 'func': vov_replacement_d3_127}


def vov_replacement_d3_128(vov_replacement_d2_128):
    feature = _clean(vov_replacement_d2_128)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00064000).reindex(feature.index)
VOV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vov_replacement_d3_128'] = {'inputs': ['vov_replacement_d2_128'], 'func': vov_replacement_d3_128}


def vov_replacement_d3_129(vov_replacement_d2_129):
    feature = _clean(vov_replacement_d2_129)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00064500).reindex(feature.index)
VOV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vov_replacement_d3_129'] = {'inputs': ['vov_replacement_d2_129'], 'func': vov_replacement_d3_129}


def vov_replacement_d3_130(vov_replacement_d2_130):
    feature = _clean(vov_replacement_d2_130)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00065000).reindex(feature.index)
VOV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vov_replacement_d3_130'] = {'inputs': ['vov_replacement_d2_130'], 'func': vov_replacement_d3_130}


def vov_replacement_d3_131(vov_replacement_d2_131):
    feature = _clean(vov_replacement_d2_131)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00065500).reindex(feature.index)
VOV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vov_replacement_d3_131'] = {'inputs': ['vov_replacement_d2_131'], 'func': vov_replacement_d3_131}


def vov_replacement_d3_132(vov_replacement_d2_132):
    feature = _clean(vov_replacement_d2_132)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00066000).reindex(feature.index)
VOV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vov_replacement_d3_132'] = {'inputs': ['vov_replacement_d2_132'], 'func': vov_replacement_d3_132}


def vov_replacement_d3_133(vov_replacement_d2_133):
    feature = _clean(vov_replacement_d2_133)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00066500).reindex(feature.index)
VOV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vov_replacement_d3_133'] = {'inputs': ['vov_replacement_d2_133'], 'func': vov_replacement_d3_133}


def vov_replacement_d3_134(vov_replacement_d2_134):
    feature = _clean(vov_replacement_d2_134)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00067000).reindex(feature.index)
VOV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vov_replacement_d3_134'] = {'inputs': ['vov_replacement_d2_134'], 'func': vov_replacement_d3_134}


def vov_replacement_d3_135(vov_replacement_d2_135):
    feature = _clean(vov_replacement_d2_135)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00067500).reindex(feature.index)
VOV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vov_replacement_d3_135'] = {'inputs': ['vov_replacement_d2_135'], 'func': vov_replacement_d3_135}


def vov_replacement_d3_136(vov_replacement_d2_136):
    feature = _clean(vov_replacement_d2_136)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00068000).reindex(feature.index)
VOV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vov_replacement_d3_136'] = {'inputs': ['vov_replacement_d2_136'], 'func': vov_replacement_d3_136}


def vov_replacement_d3_137(vov_replacement_d2_137):
    feature = _clean(vov_replacement_d2_137)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00068500).reindex(feature.index)
VOV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vov_replacement_d3_137'] = {'inputs': ['vov_replacement_d2_137'], 'func': vov_replacement_d3_137}


def vov_replacement_d3_138(vov_replacement_d2_138):
    feature = _clean(vov_replacement_d2_138)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00069000).reindex(feature.index)
VOV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vov_replacement_d3_138'] = {'inputs': ['vov_replacement_d2_138'], 'func': vov_replacement_d3_138}


def vov_replacement_d3_139(vov_replacement_d2_139):
    feature = _clean(vov_replacement_d2_139)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00069500).reindex(feature.index)
VOV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vov_replacement_d3_139'] = {'inputs': ['vov_replacement_d2_139'], 'func': vov_replacement_d3_139}


def vov_replacement_d3_140(vov_replacement_d2_140):
    feature = _clean(vov_replacement_d2_140)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00070000).reindex(feature.index)
VOV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vov_replacement_d3_140'] = {'inputs': ['vov_replacement_d2_140'], 'func': vov_replacement_d3_140}


def vov_replacement_d3_141(vov_replacement_d2_141):
    feature = _clean(vov_replacement_d2_141)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00070500).reindex(feature.index)
VOV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vov_replacement_d3_141'] = {'inputs': ['vov_replacement_d2_141'], 'func': vov_replacement_d3_141}


def vov_replacement_d3_142(vov_replacement_d2_142):
    feature = _clean(vov_replacement_d2_142)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00071000).reindex(feature.index)
VOV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vov_replacement_d3_142'] = {'inputs': ['vov_replacement_d2_142'], 'func': vov_replacement_d3_142}


def vov_replacement_d3_143(vov_replacement_d2_143):
    feature = _clean(vov_replacement_d2_143)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00071500).reindex(feature.index)
VOV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vov_replacement_d3_143'] = {'inputs': ['vov_replacement_d2_143'], 'func': vov_replacement_d3_143}


def vov_replacement_d3_144(vov_replacement_d2_144):
    feature = _clean(vov_replacement_d2_144)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00072000).reindex(feature.index)
VOV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vov_replacement_d3_144'] = {'inputs': ['vov_replacement_d2_144'], 'func': vov_replacement_d3_144}


def vov_replacement_d3_145(vov_replacement_d2_145):
    feature = _clean(vov_replacement_d2_145)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00072500).reindex(feature.index)
VOV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vov_replacement_d3_145'] = {'inputs': ['vov_replacement_d2_145'], 'func': vov_replacement_d3_145}


def vov_replacement_d3_146(vov_replacement_d2_146):
    feature = _clean(vov_replacement_d2_146)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00073000).reindex(feature.index)
VOV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vov_replacement_d3_146'] = {'inputs': ['vov_replacement_d2_146'], 'func': vov_replacement_d3_146}


def vov_replacement_d3_147(vov_replacement_d2_147):
    feature = _clean(vov_replacement_d2_147)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00073500).reindex(feature.index)
VOV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vov_replacement_d3_147'] = {'inputs': ['vov_replacement_d2_147'], 'func': vov_replacement_d3_147}


def vov_replacement_d3_148(vov_replacement_d2_148):
    feature = _clean(vov_replacement_d2_148)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00074000).reindex(feature.index)
VOV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vov_replacement_d3_148'] = {'inputs': ['vov_replacement_d2_148'], 'func': vov_replacement_d3_148}


def vov_replacement_d3_149(vov_replacement_d2_149):
    feature = _clean(vov_replacement_d2_149)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00074500).reindex(feature.index)
VOV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vov_replacement_d3_149'] = {'inputs': ['vov_replacement_d2_149'], 'func': vov_replacement_d3_149}


def vov_replacement_d3_150(vov_replacement_d2_150):
    feature = _clean(vov_replacement_d2_150)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00075000).reindex(feature.index)
VOV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vov_replacement_d3_150'] = {'inputs': ['vov_replacement_d2_150'], 'func': vov_replacement_d3_150}


def vov_replacement_d3_151(vov_replacement_d2_151):
    feature = _clean(vov_replacement_d2_151)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00075500).reindex(feature.index)
VOV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vov_replacement_d3_151'] = {'inputs': ['vov_replacement_d2_151'], 'func': vov_replacement_d3_151}


def vov_replacement_d3_152(vov_replacement_d2_152):
    feature = _clean(vov_replacement_d2_152)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00076000).reindex(feature.index)
VOV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vov_replacement_d3_152'] = {'inputs': ['vov_replacement_d2_152'], 'func': vov_replacement_d3_152}


def vov_replacement_d3_153(vov_replacement_d2_153):
    feature = _clean(vov_replacement_d2_153)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00076500).reindex(feature.index)
VOV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vov_replacement_d3_153'] = {'inputs': ['vov_replacement_d2_153'], 'func': vov_replacement_d3_153}


def vov_replacement_d3_154(vov_replacement_d2_154):
    feature = _clean(vov_replacement_d2_154)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00077000).reindex(feature.index)
VOV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vov_replacement_d3_154'] = {'inputs': ['vov_replacement_d2_154'], 'func': vov_replacement_d3_154}


def vov_replacement_d3_155(vov_replacement_d2_155):
    feature = _clean(vov_replacement_d2_155)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00077500).reindex(feature.index)
VOV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vov_replacement_d3_155'] = {'inputs': ['vov_replacement_d2_155'], 'func': vov_replacement_d3_155}


def vov_replacement_d3_156(vov_replacement_d2_156):
    feature = _clean(vov_replacement_d2_156)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00078000).reindex(feature.index)
VOV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vov_replacement_d3_156'] = {'inputs': ['vov_replacement_d2_156'], 'func': vov_replacement_d3_156}


def vov_replacement_d3_157(vov_replacement_d2_157):
    feature = _clean(vov_replacement_d2_157)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00078500).reindex(feature.index)
VOV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vov_replacement_d3_157'] = {'inputs': ['vov_replacement_d2_157'], 'func': vov_replacement_d3_157}


def vov_replacement_d3_158(vov_replacement_d2_158):
    feature = _clean(vov_replacement_d2_158)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00079000).reindex(feature.index)
VOV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vov_replacement_d3_158'] = {'inputs': ['vov_replacement_d2_158'], 'func': vov_replacement_d3_158}


def vov_replacement_d3_159(vov_replacement_d2_159):
    feature = _clean(vov_replacement_d2_159)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00079500).reindex(feature.index)
VOV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vov_replacement_d3_159'] = {'inputs': ['vov_replacement_d2_159'], 'func': vov_replacement_d3_159}


def vov_replacement_d3_160(vov_replacement_d2_160):
    feature = _clean(vov_replacement_d2_160)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00080000).reindex(feature.index)
VOV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vov_replacement_d3_160'] = {'inputs': ['vov_replacement_d2_160'], 'func': vov_replacement_d3_160}


def vov_replacement_d3_161(vov_replacement_d2_161):
    feature = _clean(vov_replacement_d2_161)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00080500).reindex(feature.index)
VOV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vov_replacement_d3_161'] = {'inputs': ['vov_replacement_d2_161'], 'func': vov_replacement_d3_161}


def vov_replacement_d3_162(vov_replacement_d2_162):
    feature = _clean(vov_replacement_d2_162)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00081000).reindex(feature.index)
VOV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vov_replacement_d3_162'] = {'inputs': ['vov_replacement_d2_162'], 'func': vov_replacement_d3_162}


def vov_replacement_d3_163(vov_replacement_d2_163):
    feature = _clean(vov_replacement_d2_163)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00081500).reindex(feature.index)
VOV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vov_replacement_d3_163'] = {'inputs': ['vov_replacement_d2_163'], 'func': vov_replacement_d3_163}


def vov_replacement_d3_164(vov_replacement_d2_164):
    feature = _clean(vov_replacement_d2_164)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00082000).reindex(feature.index)
VOV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vov_replacement_d3_164'] = {'inputs': ['vov_replacement_d2_164'], 'func': vov_replacement_d3_164}


def vov_replacement_d3_165(vov_replacement_d2_165):
    feature = _clean(vov_replacement_d2_165)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00082500).reindex(feature.index)
VOV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vov_replacement_d3_165'] = {'inputs': ['vov_replacement_d2_165'], 'func': vov_replacement_d3_165}


def vov_replacement_d3_166(vov_replacement_d2_166):
    feature = _clean(vov_replacement_d2_166)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00083000).reindex(feature.index)
VOV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vov_replacement_d3_166'] = {'inputs': ['vov_replacement_d2_166'], 'func': vov_replacement_d3_166}


def vov_replacement_d3_167(vov_replacement_d2_167):
    feature = _clean(vov_replacement_d2_167)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00083500).reindex(feature.index)
VOV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vov_replacement_d3_167'] = {'inputs': ['vov_replacement_d2_167'], 'func': vov_replacement_d3_167}


def vov_replacement_d3_168(vov_replacement_d2_168):
    feature = _clean(vov_replacement_d2_168)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00084000).reindex(feature.index)
VOV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vov_replacement_d3_168'] = {'inputs': ['vov_replacement_d2_168'], 'func': vov_replacement_d3_168}


def vov_replacement_d3_169(vov_replacement_d2_169):
    feature = _clean(vov_replacement_d2_169)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00084500).reindex(feature.index)
VOV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vov_replacement_d3_169'] = {'inputs': ['vov_replacement_d2_169'], 'func': vov_replacement_d3_169}


def vov_replacement_d3_170(vov_replacement_d2_170):
    feature = _clean(vov_replacement_d2_170)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00085000).reindex(feature.index)
VOV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vov_replacement_d3_170'] = {'inputs': ['vov_replacement_d2_170'], 'func': vov_replacement_d3_170}


def vov_replacement_d3_171(vov_replacement_d2_171):
    feature = _clean(vov_replacement_d2_171)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00085500).reindex(feature.index)
VOV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vov_replacement_d3_171'] = {'inputs': ['vov_replacement_d2_171'], 'func': vov_replacement_d3_171}


def vov_replacement_d3_172(vov_replacement_d2_172):
    feature = _clean(vov_replacement_d2_172)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00086000).reindex(feature.index)
VOV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vov_replacement_d3_172'] = {'inputs': ['vov_replacement_d2_172'], 'func': vov_replacement_d3_172}


def vov_replacement_d3_173(vov_replacement_d2_173):
    feature = _clean(vov_replacement_d2_173)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00086500).reindex(feature.index)
VOV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vov_replacement_d3_173'] = {'inputs': ['vov_replacement_d2_173'], 'func': vov_replacement_d3_173}


def vov_replacement_d3_174(vov_replacement_d2_174):
    feature = _clean(vov_replacement_d2_174)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00087000).reindex(feature.index)
VOV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vov_replacement_d3_174'] = {'inputs': ['vov_replacement_d2_174'], 'func': vov_replacement_d3_174}


def vov_replacement_d3_175(vov_replacement_d2_175):
    feature = _clean(vov_replacement_d2_175)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00087500).reindex(feature.index)
VOV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vov_replacement_d3_175'] = {'inputs': ['vov_replacement_d2_175'], 'func': vov_replacement_d3_175}


# Third-derivative extensions for repaired first-base features.
VOV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY = {}


def _base_universe_d3(feature, idx):
    feature = _clean(feature) if '_clean' in globals() else _s(feature).replace([np.inf, -np.inf], np.nan)
    windows = [1, 2, 3, 5, 8, 13, 21, 34, 55]
    lag = windows[(idx * 2) % len(windows)]
    smooth = windows[(idx * 5 + 2) % len(windows)]
    accel = feature.diff(lag)
    curve = feature - feature.rolling(max(3, smooth), min_periods=2).mean()
    out = accel + curve.fillna(0.0) * (0.00019 * ((idx % 19) + 1))
    return out.replace([np.inf, -np.inf], np.nan).reindex(feature.index)


def vov_base_universe_d3_001_vov_002_range_expansion_10_002(vov_base_universe_d2_001_vov_002_range_expansion_10_002):
    return _base_universe_d3(vov_base_universe_d2_001_vov_002_range_expansion_10_002, 1)
VOV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vov_base_universe_d3_001_vov_002_range_expansion_10_002'] = {'inputs': ['vov_base_universe_d2_001_vov_002_range_expansion_10_002'], 'func': vov_base_universe_d3_001_vov_002_range_expansion_10_002}


def vov_base_universe_d3_002_vov_004_close_location_42_004(vov_base_universe_d2_002_vov_004_close_location_42_004):
    return _base_universe_d3(vov_base_universe_d2_002_vov_004_close_location_42_004, 2)
VOV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vov_base_universe_d3_002_vov_004_close_location_42_004'] = {'inputs': ['vov_base_universe_d2_002_vov_004_close_location_42_004'], 'func': vov_base_universe_d3_002_vov_004_close_location_42_004}


def vov_base_universe_d3_003_vov_005_atr_move_63_005(vov_base_universe_d2_003_vov_005_atr_move_63_005):
    return _base_universe_d3(vov_base_universe_d2_003_vov_005_atr_move_63_005, 3)
VOV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vov_base_universe_d3_003_vov_005_atr_move_63_005'] = {'inputs': ['vov_base_universe_d2_003_vov_005_atr_move_63_005'], 'func': vov_base_universe_d3_003_vov_005_atr_move_63_005}


def vov_base_universe_d3_004_vov_008_range_expansion_189_008(vov_base_universe_d2_004_vov_008_range_expansion_189_008):
    return _base_universe_d3(vov_base_universe_d2_004_vov_008_range_expansion_189_008, 4)
VOV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vov_base_universe_d3_004_vov_008_range_expansion_189_008'] = {'inputs': ['vov_base_universe_d2_004_vov_008_range_expansion_189_008'], 'func': vov_base_universe_d3_004_vov_008_range_expansion_189_008}


def vov_base_universe_d3_005_vov_010_close_location_378_010(vov_base_universe_d2_005_vov_010_close_location_378_010):
    return _base_universe_d3(vov_base_universe_d2_005_vov_010_close_location_378_010, 5)
VOV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vov_base_universe_d3_005_vov_010_close_location_378_010'] = {'inputs': ['vov_base_universe_d2_005_vov_010_close_location_378_010'], 'func': vov_base_universe_d3_005_vov_010_close_location_378_010}


def vov_base_universe_d3_006_vov_011_atr_move_504_011(vov_base_universe_d2_006_vov_011_atr_move_504_011):
    return _base_universe_d3(vov_base_universe_d2_006_vov_011_atr_move_504_011, 6)
VOV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vov_base_universe_d3_006_vov_011_atr_move_504_011'] = {'inputs': ['vov_base_universe_d2_006_vov_011_atr_move_504_011'], 'func': vov_base_universe_d3_006_vov_011_atr_move_504_011}


def vov_base_universe_d3_007_vov_014_range_expansion_1260_014(vov_base_universe_d2_007_vov_014_range_expansion_1260_014):
    return _base_universe_d3(vov_base_universe_d2_007_vov_014_range_expansion_1260_014, 7)
VOV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vov_base_universe_d3_007_vov_014_range_expansion_1260_014'] = {'inputs': ['vov_base_universe_d2_007_vov_014_range_expansion_1260_014'], 'func': vov_base_universe_d3_007_vov_014_range_expansion_1260_014}


def vov_base_universe_d3_008_vov_016_close_location_5_016(vov_base_universe_d2_008_vov_016_close_location_5_016):
    return _base_universe_d3(vov_base_universe_d2_008_vov_016_close_location_5_016, 8)
VOV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vov_base_universe_d3_008_vov_016_close_location_5_016'] = {'inputs': ['vov_base_universe_d2_008_vov_016_close_location_5_016'], 'func': vov_base_universe_d3_008_vov_016_close_location_5_016}


def vov_base_universe_d3_009_vov_017_atr_move_10_017(vov_base_universe_d2_009_vov_017_atr_move_10_017):
    return _base_universe_d3(vov_base_universe_d2_009_vov_017_atr_move_10_017, 9)
VOV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vov_base_universe_d3_009_vov_017_atr_move_10_017'] = {'inputs': ['vov_base_universe_d2_009_vov_017_atr_move_10_017'], 'func': vov_base_universe_d3_009_vov_017_atr_move_10_017}


def vov_base_universe_d3_010_vov_020_range_expansion_63_020(vov_base_universe_d2_010_vov_020_range_expansion_63_020):
    return _base_universe_d3(vov_base_universe_d2_010_vov_020_range_expansion_63_020, 10)
VOV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vov_base_universe_d3_010_vov_020_range_expansion_63_020'] = {'inputs': ['vov_base_universe_d2_010_vov_020_range_expansion_63_020'], 'func': vov_base_universe_d3_010_vov_020_range_expansion_63_020}


def vov_base_universe_d3_011_vov_022_close_location_126_022(vov_base_universe_d2_011_vov_022_close_location_126_022):
    return _base_universe_d3(vov_base_universe_d2_011_vov_022_close_location_126_022, 11)
VOV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vov_base_universe_d3_011_vov_022_close_location_126_022'] = {'inputs': ['vov_base_universe_d2_011_vov_022_close_location_126_022'], 'func': vov_base_universe_d3_011_vov_022_close_location_126_022}


def vov_base_universe_d3_012_vov_023_atr_move_189_023(vov_base_universe_d2_012_vov_023_atr_move_189_023):
    return _base_universe_d3(vov_base_universe_d2_012_vov_023_atr_move_189_023, 12)
VOV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vov_base_universe_d3_012_vov_023_atr_move_189_023'] = {'inputs': ['vov_base_universe_d2_012_vov_023_atr_move_189_023'], 'func': vov_base_universe_d3_012_vov_023_atr_move_189_023}


def vov_base_universe_d3_013_vov_026_range_expansion_504_026(vov_base_universe_d2_013_vov_026_range_expansion_504_026):
    return _base_universe_d3(vov_base_universe_d2_013_vov_026_range_expansion_504_026, 13)
VOV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vov_base_universe_d3_013_vov_026_range_expansion_504_026'] = {'inputs': ['vov_base_universe_d2_013_vov_026_range_expansion_504_026'], 'func': vov_base_universe_d3_013_vov_026_range_expansion_504_026}


def vov_base_universe_d3_014_vov_028_close_location_1008_028(vov_base_universe_d2_014_vov_028_close_location_1008_028):
    return _base_universe_d3(vov_base_universe_d2_014_vov_028_close_location_1008_028, 14)
VOV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vov_base_universe_d3_014_vov_028_close_location_1008_028'] = {'inputs': ['vov_base_universe_d2_014_vov_028_close_location_1008_028'], 'func': vov_base_universe_d3_014_vov_028_close_location_1008_028}


def vov_base_universe_d3_015_vov_029_atr_move_1260_029(vov_base_universe_d2_015_vov_029_atr_move_1260_029):
    return _base_universe_d3(vov_base_universe_d2_015_vov_029_atr_move_1260_029, 15)
VOV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vov_base_universe_d3_015_vov_029_atr_move_1260_029'] = {'inputs': ['vov_base_universe_d2_015_vov_029_atr_move_1260_029'], 'func': vov_base_universe_d3_015_vov_029_atr_move_1260_029}


def vov_base_universe_d3_016_vov_basefill_001(vov_base_universe_d2_016_vov_basefill_001):
    return _base_universe_d3(vov_base_universe_d2_016_vov_basefill_001, 16)
VOV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vov_base_universe_d3_016_vov_basefill_001'] = {'inputs': ['vov_base_universe_d2_016_vov_basefill_001'], 'func': vov_base_universe_d3_016_vov_basefill_001}


def vov_base_universe_d3_017_vov_basefill_003(vov_base_universe_d2_017_vov_basefill_003):
    return _base_universe_d3(vov_base_universe_d2_017_vov_basefill_003, 17)
VOV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vov_base_universe_d3_017_vov_basefill_003'] = {'inputs': ['vov_base_universe_d2_017_vov_basefill_003'], 'func': vov_base_universe_d3_017_vov_basefill_003}


def vov_base_universe_d3_018_vov_basefill_006(vov_base_universe_d2_018_vov_basefill_006):
    return _base_universe_d3(vov_base_universe_d2_018_vov_basefill_006, 18)
VOV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vov_base_universe_d3_018_vov_basefill_006'] = {'inputs': ['vov_base_universe_d2_018_vov_basefill_006'], 'func': vov_base_universe_d3_018_vov_basefill_006}


def vov_base_universe_d3_019_vov_basefill_007(vov_base_universe_d2_019_vov_basefill_007):
    return _base_universe_d3(vov_base_universe_d2_019_vov_basefill_007, 19)
VOV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vov_base_universe_d3_019_vov_basefill_007'] = {'inputs': ['vov_base_universe_d2_019_vov_basefill_007'], 'func': vov_base_universe_d3_019_vov_basefill_007}


def vov_base_universe_d3_020_vov_basefill_009(vov_base_universe_d2_020_vov_basefill_009):
    return _base_universe_d3(vov_base_universe_d2_020_vov_basefill_009, 20)
VOV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vov_base_universe_d3_020_vov_basefill_009'] = {'inputs': ['vov_base_universe_d2_020_vov_basefill_009'], 'func': vov_base_universe_d3_020_vov_basefill_009}


def vov_base_universe_d3_021_vov_basefill_012(vov_base_universe_d2_021_vov_basefill_012):
    return _base_universe_d3(vov_base_universe_d2_021_vov_basefill_012, 21)
VOV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vov_base_universe_d3_021_vov_basefill_012'] = {'inputs': ['vov_base_universe_d2_021_vov_basefill_012'], 'func': vov_base_universe_d3_021_vov_basefill_012}


def vov_base_universe_d3_022_vov_basefill_013(vov_base_universe_d2_022_vov_basefill_013):
    return _base_universe_d3(vov_base_universe_d2_022_vov_basefill_013, 22)
VOV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vov_base_universe_d3_022_vov_basefill_013'] = {'inputs': ['vov_base_universe_d2_022_vov_basefill_013'], 'func': vov_base_universe_d3_022_vov_basefill_013}


def vov_base_universe_d3_023_vov_basefill_015(vov_base_universe_d2_023_vov_basefill_015):
    return _base_universe_d3(vov_base_universe_d2_023_vov_basefill_015, 23)
VOV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vov_base_universe_d3_023_vov_basefill_015'] = {'inputs': ['vov_base_universe_d2_023_vov_basefill_015'], 'func': vov_base_universe_d3_023_vov_basefill_015}


def vov_base_universe_d3_024_vov_basefill_018(vov_base_universe_d2_024_vov_basefill_018):
    return _base_universe_d3(vov_base_universe_d2_024_vov_basefill_018, 24)
VOV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vov_base_universe_d3_024_vov_basefill_018'] = {'inputs': ['vov_base_universe_d2_024_vov_basefill_018'], 'func': vov_base_universe_d3_024_vov_basefill_018}


def vov_base_universe_d3_025_vov_basefill_019(vov_base_universe_d2_025_vov_basefill_019):
    return _base_universe_d3(vov_base_universe_d2_025_vov_basefill_019, 25)
VOV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vov_base_universe_d3_025_vov_basefill_019'] = {'inputs': ['vov_base_universe_d2_025_vov_basefill_019'], 'func': vov_base_universe_d3_025_vov_basefill_019}


def vov_base_universe_d3_026_vov_basefill_021(vov_base_universe_d2_026_vov_basefill_021):
    return _base_universe_d3(vov_base_universe_d2_026_vov_basefill_021, 26)
VOV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vov_base_universe_d3_026_vov_basefill_021'] = {'inputs': ['vov_base_universe_d2_026_vov_basefill_021'], 'func': vov_base_universe_d3_026_vov_basefill_021}


def vov_base_universe_d3_027_vov_basefill_024(vov_base_universe_d2_027_vov_basefill_024):
    return _base_universe_d3(vov_base_universe_d2_027_vov_basefill_024, 27)
VOV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vov_base_universe_d3_027_vov_basefill_024'] = {'inputs': ['vov_base_universe_d2_027_vov_basefill_024'], 'func': vov_base_universe_d3_027_vov_basefill_024}


def vov_base_universe_d3_028_vov_basefill_025(vov_base_universe_d2_028_vov_basefill_025):
    return _base_universe_d3(vov_base_universe_d2_028_vov_basefill_025, 28)
VOV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vov_base_universe_d3_028_vov_basefill_025'] = {'inputs': ['vov_base_universe_d2_028_vov_basefill_025'], 'func': vov_base_universe_d3_028_vov_basefill_025}


def vov_base_universe_d3_029_vov_basefill_027(vov_base_universe_d2_029_vov_basefill_027):
    return _base_universe_d3(vov_base_universe_d2_029_vov_basefill_027, 29)
VOV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vov_base_universe_d3_029_vov_basefill_027'] = {'inputs': ['vov_base_universe_d2_029_vov_basefill_027'], 'func': vov_base_universe_d3_029_vov_basefill_027}


def vov_base_universe_d3_030_vov_basefill_030(vov_base_universe_d2_030_vov_basefill_030):
    return _base_universe_d3(vov_base_universe_d2_030_vov_basefill_030, 30)
VOV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vov_base_universe_d3_030_vov_basefill_030'] = {'inputs': ['vov_base_universe_d2_030_vov_basefill_030'], 'func': vov_base_universe_d3_030_vov_basefill_030}


def vov_base_universe_d3_031_vov_basefill_031(vov_base_universe_d2_031_vov_basefill_031):
    return _base_universe_d3(vov_base_universe_d2_031_vov_basefill_031, 31)
VOV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vov_base_universe_d3_031_vov_basefill_031'] = {'inputs': ['vov_base_universe_d2_031_vov_basefill_031'], 'func': vov_base_universe_d3_031_vov_basefill_031}


def vov_base_universe_d3_032_vov_basefill_032(vov_base_universe_d2_032_vov_basefill_032):
    return _base_universe_d3(vov_base_universe_d2_032_vov_basefill_032, 32)
VOV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vov_base_universe_d3_032_vov_basefill_032'] = {'inputs': ['vov_base_universe_d2_032_vov_basefill_032'], 'func': vov_base_universe_d3_032_vov_basefill_032}


def vov_base_universe_d3_033_vov_basefill_033(vov_base_universe_d2_033_vov_basefill_033):
    return _base_universe_d3(vov_base_universe_d2_033_vov_basefill_033, 33)
VOV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vov_base_universe_d3_033_vov_basefill_033'] = {'inputs': ['vov_base_universe_d2_033_vov_basefill_033'], 'func': vov_base_universe_d3_033_vov_basefill_033}


def vov_base_universe_d3_034_vov_basefill_034(vov_base_universe_d2_034_vov_basefill_034):
    return _base_universe_d3(vov_base_universe_d2_034_vov_basefill_034, 34)
VOV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vov_base_universe_d3_034_vov_basefill_034'] = {'inputs': ['vov_base_universe_d2_034_vov_basefill_034'], 'func': vov_base_universe_d3_034_vov_basefill_034}


def vov_base_universe_d3_035_vov_basefill_035(vov_base_universe_d2_035_vov_basefill_035):
    return _base_universe_d3(vov_base_universe_d2_035_vov_basefill_035, 35)
VOV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vov_base_universe_d3_035_vov_basefill_035'] = {'inputs': ['vov_base_universe_d2_035_vov_basefill_035'], 'func': vov_base_universe_d3_035_vov_basefill_035}


def vov_base_universe_d3_036_vov_basefill_036(vov_base_universe_d2_036_vov_basefill_036):
    return _base_universe_d3(vov_base_universe_d2_036_vov_basefill_036, 36)
VOV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vov_base_universe_d3_036_vov_basefill_036'] = {'inputs': ['vov_base_universe_d2_036_vov_basefill_036'], 'func': vov_base_universe_d3_036_vov_basefill_036}


def vov_base_universe_d3_037_vov_basefill_037(vov_base_universe_d2_037_vov_basefill_037):
    return _base_universe_d3(vov_base_universe_d2_037_vov_basefill_037, 37)
VOV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vov_base_universe_d3_037_vov_basefill_037'] = {'inputs': ['vov_base_universe_d2_037_vov_basefill_037'], 'func': vov_base_universe_d3_037_vov_basefill_037}


def vov_base_universe_d3_038_vov_basefill_038(vov_base_universe_d2_038_vov_basefill_038):
    return _base_universe_d3(vov_base_universe_d2_038_vov_basefill_038, 38)
VOV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vov_base_universe_d3_038_vov_basefill_038'] = {'inputs': ['vov_base_universe_d2_038_vov_basefill_038'], 'func': vov_base_universe_d3_038_vov_basefill_038}


def vov_base_universe_d3_039_vov_basefill_039(vov_base_universe_d2_039_vov_basefill_039):
    return _base_universe_d3(vov_base_universe_d2_039_vov_basefill_039, 39)
VOV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vov_base_universe_d3_039_vov_basefill_039'] = {'inputs': ['vov_base_universe_d2_039_vov_basefill_039'], 'func': vov_base_universe_d3_039_vov_basefill_039}


def vov_base_universe_d3_040_vov_basefill_040(vov_base_universe_d2_040_vov_basefill_040):
    return _base_universe_d3(vov_base_universe_d2_040_vov_basefill_040, 40)
VOV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vov_base_universe_d3_040_vov_basefill_040'] = {'inputs': ['vov_base_universe_d2_040_vov_basefill_040'], 'func': vov_base_universe_d3_040_vov_basefill_040}


def vov_base_universe_d3_041_vov_basefill_041(vov_base_universe_d2_041_vov_basefill_041):
    return _base_universe_d3(vov_base_universe_d2_041_vov_basefill_041, 41)
VOV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vov_base_universe_d3_041_vov_basefill_041'] = {'inputs': ['vov_base_universe_d2_041_vov_basefill_041'], 'func': vov_base_universe_d3_041_vov_basefill_041}


def vov_base_universe_d3_042_vov_basefill_042(vov_base_universe_d2_042_vov_basefill_042):
    return _base_universe_d3(vov_base_universe_d2_042_vov_basefill_042, 42)
VOV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vov_base_universe_d3_042_vov_basefill_042'] = {'inputs': ['vov_base_universe_d2_042_vov_basefill_042'], 'func': vov_base_universe_d3_042_vov_basefill_042}


def vov_base_universe_d3_043_vov_basefill_043(vov_base_universe_d2_043_vov_basefill_043):
    return _base_universe_d3(vov_base_universe_d2_043_vov_basefill_043, 43)
VOV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vov_base_universe_d3_043_vov_basefill_043'] = {'inputs': ['vov_base_universe_d2_043_vov_basefill_043'], 'func': vov_base_universe_d3_043_vov_basefill_043}


def vov_base_universe_d3_044_vov_basefill_044(vov_base_universe_d2_044_vov_basefill_044):
    return _base_universe_d3(vov_base_universe_d2_044_vov_basefill_044, 44)
VOV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vov_base_universe_d3_044_vov_basefill_044'] = {'inputs': ['vov_base_universe_d2_044_vov_basefill_044'], 'func': vov_base_universe_d3_044_vov_basefill_044}


def vov_base_universe_d3_045_vov_basefill_045(vov_base_universe_d2_045_vov_basefill_045):
    return _base_universe_d3(vov_base_universe_d2_045_vov_basefill_045, 45)
VOV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vov_base_universe_d3_045_vov_basefill_045'] = {'inputs': ['vov_base_universe_d2_045_vov_basefill_045'], 'func': vov_base_universe_d3_045_vov_basefill_045}


def vov_base_universe_d3_046_vov_basefill_046(vov_base_universe_d2_046_vov_basefill_046):
    return _base_universe_d3(vov_base_universe_d2_046_vov_basefill_046, 46)
VOV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vov_base_universe_d3_046_vov_basefill_046'] = {'inputs': ['vov_base_universe_d2_046_vov_basefill_046'], 'func': vov_base_universe_d3_046_vov_basefill_046}


def vov_base_universe_d3_047_vov_basefill_047(vov_base_universe_d2_047_vov_basefill_047):
    return _base_universe_d3(vov_base_universe_d2_047_vov_basefill_047, 47)
VOV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vov_base_universe_d3_047_vov_basefill_047'] = {'inputs': ['vov_base_universe_d2_047_vov_basefill_047'], 'func': vov_base_universe_d3_047_vov_basefill_047}


def vov_base_universe_d3_048_vov_basefill_048(vov_base_universe_d2_048_vov_basefill_048):
    return _base_universe_d3(vov_base_universe_d2_048_vov_basefill_048, 48)
VOV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vov_base_universe_d3_048_vov_basefill_048'] = {'inputs': ['vov_base_universe_d2_048_vov_basefill_048'], 'func': vov_base_universe_d3_048_vov_basefill_048}


def vov_base_universe_d3_049_vov_basefill_049(vov_base_universe_d2_049_vov_basefill_049):
    return _base_universe_d3(vov_base_universe_d2_049_vov_basefill_049, 49)
VOV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vov_base_universe_d3_049_vov_basefill_049'] = {'inputs': ['vov_base_universe_d2_049_vov_basefill_049'], 'func': vov_base_universe_d3_049_vov_basefill_049}


def vov_base_universe_d3_050_vov_basefill_050(vov_base_universe_d2_050_vov_basefill_050):
    return _base_universe_d3(vov_base_universe_d2_050_vov_basefill_050, 50)
VOV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vov_base_universe_d3_050_vov_basefill_050'] = {'inputs': ['vov_base_universe_d2_050_vov_basefill_050'], 'func': vov_base_universe_d3_050_vov_basefill_050}


def vov_base_universe_d3_051_vov_basefill_051(vov_base_universe_d2_051_vov_basefill_051):
    return _base_universe_d3(vov_base_universe_d2_051_vov_basefill_051, 51)
VOV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vov_base_universe_d3_051_vov_basefill_051'] = {'inputs': ['vov_base_universe_d2_051_vov_basefill_051'], 'func': vov_base_universe_d3_051_vov_basefill_051}


def vov_base_universe_d3_052_vov_basefill_052(vov_base_universe_d2_052_vov_basefill_052):
    return _base_universe_d3(vov_base_universe_d2_052_vov_basefill_052, 52)
VOV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vov_base_universe_d3_052_vov_basefill_052'] = {'inputs': ['vov_base_universe_d2_052_vov_basefill_052'], 'func': vov_base_universe_d3_052_vov_basefill_052}


def vov_base_universe_d3_053_vov_basefill_053(vov_base_universe_d2_053_vov_basefill_053):
    return _base_universe_d3(vov_base_universe_d2_053_vov_basefill_053, 53)
VOV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vov_base_universe_d3_053_vov_basefill_053'] = {'inputs': ['vov_base_universe_d2_053_vov_basefill_053'], 'func': vov_base_universe_d3_053_vov_basefill_053}


def vov_base_universe_d3_054_vov_basefill_054(vov_base_universe_d2_054_vov_basefill_054):
    return _base_universe_d3(vov_base_universe_d2_054_vov_basefill_054, 54)
VOV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vov_base_universe_d3_054_vov_basefill_054'] = {'inputs': ['vov_base_universe_d2_054_vov_basefill_054'], 'func': vov_base_universe_d3_054_vov_basefill_054}


def vov_base_universe_d3_055_vov_basefill_055(vov_base_universe_d2_055_vov_basefill_055):
    return _base_universe_d3(vov_base_universe_d2_055_vov_basefill_055, 55)
VOV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vov_base_universe_d3_055_vov_basefill_055'] = {'inputs': ['vov_base_universe_d2_055_vov_basefill_055'], 'func': vov_base_universe_d3_055_vov_basefill_055}


def vov_base_universe_d3_056_vov_basefill_056(vov_base_universe_d2_056_vov_basefill_056):
    return _base_universe_d3(vov_base_universe_d2_056_vov_basefill_056, 56)
VOV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vov_base_universe_d3_056_vov_basefill_056'] = {'inputs': ['vov_base_universe_d2_056_vov_basefill_056'], 'func': vov_base_universe_d3_056_vov_basefill_056}


def vov_base_universe_d3_057_vov_basefill_057(vov_base_universe_d2_057_vov_basefill_057):
    return _base_universe_d3(vov_base_universe_d2_057_vov_basefill_057, 57)
VOV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vov_base_universe_d3_057_vov_basefill_057'] = {'inputs': ['vov_base_universe_d2_057_vov_basefill_057'], 'func': vov_base_universe_d3_057_vov_basefill_057}


def vov_base_universe_d3_058_vov_basefill_058(vov_base_universe_d2_058_vov_basefill_058):
    return _base_universe_d3(vov_base_universe_d2_058_vov_basefill_058, 58)
VOV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vov_base_universe_d3_058_vov_basefill_058'] = {'inputs': ['vov_base_universe_d2_058_vov_basefill_058'], 'func': vov_base_universe_d3_058_vov_basefill_058}


def vov_base_universe_d3_059_vov_basefill_059(vov_base_universe_d2_059_vov_basefill_059):
    return _base_universe_d3(vov_base_universe_d2_059_vov_basefill_059, 59)
VOV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vov_base_universe_d3_059_vov_basefill_059'] = {'inputs': ['vov_base_universe_d2_059_vov_basefill_059'], 'func': vov_base_universe_d3_059_vov_basefill_059}


def vov_base_universe_d3_060_vov_basefill_060(vov_base_universe_d2_060_vov_basefill_060):
    return _base_universe_d3(vov_base_universe_d2_060_vov_basefill_060, 60)
VOV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vov_base_universe_d3_060_vov_basefill_060'] = {'inputs': ['vov_base_universe_d2_060_vov_basefill_060'], 'func': vov_base_universe_d3_060_vov_basefill_060}


def vov_base_universe_d3_061_vov_basefill_061(vov_base_universe_d2_061_vov_basefill_061):
    return _base_universe_d3(vov_base_universe_d2_061_vov_basefill_061, 61)
VOV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vov_base_universe_d3_061_vov_basefill_061'] = {'inputs': ['vov_base_universe_d2_061_vov_basefill_061'], 'func': vov_base_universe_d3_061_vov_basefill_061}


def vov_base_universe_d3_062_vov_basefill_062(vov_base_universe_d2_062_vov_basefill_062):
    return _base_universe_d3(vov_base_universe_d2_062_vov_basefill_062, 62)
VOV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vov_base_universe_d3_062_vov_basefill_062'] = {'inputs': ['vov_base_universe_d2_062_vov_basefill_062'], 'func': vov_base_universe_d3_062_vov_basefill_062}


def vov_base_universe_d3_063_vov_basefill_063(vov_base_universe_d2_063_vov_basefill_063):
    return _base_universe_d3(vov_base_universe_d2_063_vov_basefill_063, 63)
VOV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vov_base_universe_d3_063_vov_basefill_063'] = {'inputs': ['vov_base_universe_d2_063_vov_basefill_063'], 'func': vov_base_universe_d3_063_vov_basefill_063}


def vov_base_universe_d3_064_vov_basefill_064(vov_base_universe_d2_064_vov_basefill_064):
    return _base_universe_d3(vov_base_universe_d2_064_vov_basefill_064, 64)
VOV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vov_base_universe_d3_064_vov_basefill_064'] = {'inputs': ['vov_base_universe_d2_064_vov_basefill_064'], 'func': vov_base_universe_d3_064_vov_basefill_064}


def vov_base_universe_d3_065_vov_basefill_065(vov_base_universe_d2_065_vov_basefill_065):
    return _base_universe_d3(vov_base_universe_d2_065_vov_basefill_065, 65)
VOV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vov_base_universe_d3_065_vov_basefill_065'] = {'inputs': ['vov_base_universe_d2_065_vov_basefill_065'], 'func': vov_base_universe_d3_065_vov_basefill_065}


def vov_base_universe_d3_066_vov_basefill_066(vov_base_universe_d2_066_vov_basefill_066):
    return _base_universe_d3(vov_base_universe_d2_066_vov_basefill_066, 66)
VOV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vov_base_universe_d3_066_vov_basefill_066'] = {'inputs': ['vov_base_universe_d2_066_vov_basefill_066'], 'func': vov_base_universe_d3_066_vov_basefill_066}


def vov_base_universe_d3_067_vov_basefill_067(vov_base_universe_d2_067_vov_basefill_067):
    return _base_universe_d3(vov_base_universe_d2_067_vov_basefill_067, 67)
VOV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vov_base_universe_d3_067_vov_basefill_067'] = {'inputs': ['vov_base_universe_d2_067_vov_basefill_067'], 'func': vov_base_universe_d3_067_vov_basefill_067}


def vov_base_universe_d3_068_vov_basefill_068(vov_base_universe_d2_068_vov_basefill_068):
    return _base_universe_d3(vov_base_universe_d2_068_vov_basefill_068, 68)
VOV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vov_base_universe_d3_068_vov_basefill_068'] = {'inputs': ['vov_base_universe_d2_068_vov_basefill_068'], 'func': vov_base_universe_d3_068_vov_basefill_068}


def vov_base_universe_d3_069_vov_basefill_069(vov_base_universe_d2_069_vov_basefill_069):
    return _base_universe_d3(vov_base_universe_d2_069_vov_basefill_069, 69)
VOV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vov_base_universe_d3_069_vov_basefill_069'] = {'inputs': ['vov_base_universe_d2_069_vov_basefill_069'], 'func': vov_base_universe_d3_069_vov_basefill_069}


def vov_base_universe_d3_070_vov_basefill_070(vov_base_universe_d2_070_vov_basefill_070):
    return _base_universe_d3(vov_base_universe_d2_070_vov_basefill_070, 70)
VOV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vov_base_universe_d3_070_vov_basefill_070'] = {'inputs': ['vov_base_universe_d2_070_vov_basefill_070'], 'func': vov_base_universe_d3_070_vov_basefill_070}


def vov_base_universe_d3_071_vov_basefill_071(vov_base_universe_d2_071_vov_basefill_071):
    return _base_universe_d3(vov_base_universe_d2_071_vov_basefill_071, 71)
VOV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vov_base_universe_d3_071_vov_basefill_071'] = {'inputs': ['vov_base_universe_d2_071_vov_basefill_071'], 'func': vov_base_universe_d3_071_vov_basefill_071}


def vov_base_universe_d3_072_vov_basefill_072(vov_base_universe_d2_072_vov_basefill_072):
    return _base_universe_d3(vov_base_universe_d2_072_vov_basefill_072, 72)
VOV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vov_base_universe_d3_072_vov_basefill_072'] = {'inputs': ['vov_base_universe_d2_072_vov_basefill_072'], 'func': vov_base_universe_d3_072_vov_basefill_072}


def vov_base_universe_d3_073_vov_basefill_073(vov_base_universe_d2_073_vov_basefill_073):
    return _base_universe_d3(vov_base_universe_d2_073_vov_basefill_073, 73)
VOV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vov_base_universe_d3_073_vov_basefill_073'] = {'inputs': ['vov_base_universe_d2_073_vov_basefill_073'], 'func': vov_base_universe_d3_073_vov_basefill_073}


def vov_base_universe_d3_074_vov_basefill_074(vov_base_universe_d2_074_vov_basefill_074):
    return _base_universe_d3(vov_base_universe_d2_074_vov_basefill_074, 74)
VOV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vov_base_universe_d3_074_vov_basefill_074'] = {'inputs': ['vov_base_universe_d2_074_vov_basefill_074'], 'func': vov_base_universe_d3_074_vov_basefill_074}


def vov_base_universe_d3_075_vov_basefill_075(vov_base_universe_d2_075_vov_basefill_075):
    return _base_universe_d3(vov_base_universe_d2_075_vov_basefill_075, 75)
VOV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vov_base_universe_d3_075_vov_basefill_075'] = {'inputs': ['vov_base_universe_d2_075_vov_basefill_075'], 'func': vov_base_universe_d3_075_vov_basefill_075}
