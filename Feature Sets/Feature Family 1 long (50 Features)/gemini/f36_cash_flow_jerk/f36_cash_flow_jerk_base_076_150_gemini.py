import pandas as pd
import numpy as np

def _sma(s, w): return s.rolling(w, min_periods=min(w, 20) if w > 20 else min(w, 2)).mean()
def _std(s, w): return s.rolling(w, min_periods=min(w, 20) if w > 20 else min(w, 2)).std()
def _z(s, w): return (s - _sma(s, w)) / _std(s, w).replace(0, np.nan)

def _cfj_growth(s, w):
    return s.pct_change(w)

def _cfj_accel(s, w1, w2):
    return s.pct_change(w1).pct_change(w2)

def _cfj_jerk(s, w1, w2, w3):
    accel = s.pct_change(w1).pct_change(w2)
    return accel.diff(w3)

def _cfj_slope(s, w):
    return s.pct_change(w)

def _cfj_jerk_deriv(s, w):
    return s.diff(w)

def _cfj_zscore(s, w):
    return _z(s, w)

def f36_cash_flow_jerk_accel_v076_signal(ncfo) -> pd.Series:
    """Cash flow acceleration variation 76. Component of higher order momentum. Variation 76."""
    res = _cfj_accel(ncfo, 76, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_cash_flow_jerk_accel_v077_signal(ncfo) -> pd.Series:
    """Cash flow acceleration variation 77. Component of higher order momentum. Variation 77."""
    res = _cfj_accel(ncfo, 77, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_cash_flow_jerk_accel_v078_signal(ncfo) -> pd.Series:
    """Cash flow acceleration variation 78. Component of higher order momentum. Variation 78."""
    res = _cfj_accel(ncfo, 78, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_cash_flow_jerk_accel_v079_signal(ncfo) -> pd.Series:
    """Cash flow acceleration variation 79. Component of higher order momentum. Variation 79."""
    res = _cfj_accel(ncfo, 79, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_cash_flow_jerk_accel_v080_signal(ncfo) -> pd.Series:
    """Cash flow acceleration variation 80. Component of higher order momentum. Variation 80."""
    res = _cfj_accel(ncfo, 80, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_cash_flow_jerk_accel_v081_signal(ncfo) -> pd.Series:
    """Cash flow acceleration variation 81. Component of higher order momentum. Variation 81."""
    res = _cfj_accel(ncfo, 81, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_cash_flow_jerk_accel_v082_signal(ncfo) -> pd.Series:
    """Cash flow acceleration variation 82. Component of higher order momentum. Variation 82."""
    res = _cfj_accel(ncfo, 82, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_cash_flow_jerk_accel_v083_signal(ncfo) -> pd.Series:
    """Cash flow acceleration variation 83. Component of higher order momentum. Variation 83."""
    res = _cfj_accel(ncfo, 83, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_cash_flow_jerk_accel_v084_signal(ncfo) -> pd.Series:
    """Cash flow acceleration variation 84. Component of higher order momentum. Variation 84."""
    res = _cfj_accel(ncfo, 84, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_cash_flow_jerk_accel_v085_signal(ncfo) -> pd.Series:
    """Cash flow acceleration variation 85. Component of higher order momentum. Variation 85."""
    res = _cfj_accel(ncfo, 85, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_cash_flow_jerk_accel_v086_signal(ncfo) -> pd.Series:
    """Cash flow acceleration variation 86. Component of higher order momentum. Variation 86."""
    res = _cfj_accel(ncfo, 86, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_cash_flow_jerk_accel_v087_signal(ncfo) -> pd.Series:
    """Cash flow acceleration variation 87. Component of higher order momentum. Variation 87."""
    res = _cfj_accel(ncfo, 87, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_cash_flow_jerk_accel_v088_signal(ncfo) -> pd.Series:
    """Cash flow acceleration variation 88. Component of higher order momentum. Variation 88."""
    res = _cfj_accel(ncfo, 88, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_cash_flow_jerk_accel_v089_signal(ncfo) -> pd.Series:
    """Cash flow acceleration variation 89. Component of higher order momentum. Variation 89."""
    res = _cfj_accel(ncfo, 89, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_cash_flow_jerk_accel_v090_signal(ncfo) -> pd.Series:
    """Cash flow acceleration variation 90. Component of higher order momentum. Variation 90."""
    res = _cfj_accel(ncfo, 90, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_cash_flow_jerk_accel_v091_signal(ncfo) -> pd.Series:
    """Cash flow acceleration variation 91. Component of higher order momentum. Variation 91."""
    res = _cfj_accel(ncfo, 91, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_cash_flow_jerk_accel_v092_signal(ncfo) -> pd.Series:
    """Cash flow acceleration variation 92. Component of higher order momentum. Variation 92."""
    res = _cfj_accel(ncfo, 92, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_cash_flow_jerk_accel_v093_signal(ncfo) -> pd.Series:
    """Cash flow acceleration variation 93. Component of higher order momentum. Variation 93."""
    res = _cfj_accel(ncfo, 93, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_cash_flow_jerk_accel_v094_signal(ncfo) -> pd.Series:
    """Cash flow acceleration variation 94. Component of higher order momentum. Variation 94."""
    res = _cfj_accel(ncfo, 94, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_cash_flow_jerk_accel_v095_signal(ncfo) -> pd.Series:
    """Cash flow acceleration variation 95. Component of higher order momentum. Variation 95."""
    res = _cfj_accel(ncfo, 95, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_cash_flow_jerk_accel_v096_signal(ncfo) -> pd.Series:
    """Cash flow acceleration variation 96. Component of higher order momentum. Variation 96."""
    res = _cfj_accel(ncfo, 96, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_cash_flow_jerk_accel_v097_signal(ncfo) -> pd.Series:
    """Cash flow acceleration variation 97. Component of higher order momentum. Variation 97."""
    res = _cfj_accel(ncfo, 97, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_cash_flow_jerk_accel_v098_signal(ncfo) -> pd.Series:
    """Cash flow acceleration variation 98. Component of higher order momentum. Variation 98."""
    res = _cfj_accel(ncfo, 98, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_cash_flow_jerk_accel_v099_signal(ncfo) -> pd.Series:
    """Cash flow acceleration variation 99. Component of higher order momentum. Variation 99."""
    res = _cfj_accel(ncfo, 99, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_cash_flow_jerk_accel_v100_signal(ncfo) -> pd.Series:
    """Cash flow acceleration variation 100. Component of higher order momentum. Variation 100."""
    res = _cfj_accel(ncfo, 100, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_cash_flow_jerk_accel_v101_signal(ncfo) -> pd.Series:
    """Cash flow acceleration variation 101. Component of higher order momentum. Variation 101."""
    res = _cfj_accel(ncfo, 101, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_cash_flow_jerk_accel_v102_signal(ncfo) -> pd.Series:
    """Cash flow acceleration variation 102. Component of higher order momentum. Variation 102."""
    res = _cfj_accel(ncfo, 102, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_cash_flow_jerk_accel_v103_signal(ncfo) -> pd.Series:
    """Cash flow acceleration variation 103. Component of higher order momentum. Variation 103."""
    res = _cfj_accel(ncfo, 103, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_cash_flow_jerk_accel_v104_signal(ncfo) -> pd.Series:
    """Cash flow acceleration variation 104. Component of higher order momentum. Variation 104."""
    res = _cfj_accel(ncfo, 104, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_cash_flow_jerk_accel_v105_signal(ncfo) -> pd.Series:
    """Cash flow acceleration variation 105. Component of higher order momentum. Variation 105."""
    res = _cfj_accel(ncfo, 105, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_cash_flow_jerk_accel_v106_signal(ncfo) -> pd.Series:
    """Cash flow acceleration variation 106. Component of higher order momentum. Variation 106."""
    res = _cfj_accel(ncfo, 106, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_cash_flow_jerk_accel_v107_signal(ncfo) -> pd.Series:
    """Cash flow acceleration variation 107. Component of higher order momentum. Variation 107."""
    res = _cfj_accel(ncfo, 107, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_cash_flow_jerk_accel_v108_signal(ncfo) -> pd.Series:
    """Cash flow acceleration variation 108. Component of higher order momentum. Variation 108."""
    res = _cfj_accel(ncfo, 108, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_cash_flow_jerk_accel_v109_signal(ncfo) -> pd.Series:
    """Cash flow acceleration variation 109. Component of higher order momentum. Variation 109."""
    res = _cfj_accel(ncfo, 109, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_cash_flow_jerk_accel_v110_signal(ncfo) -> pd.Series:
    """Cash flow acceleration variation 110. Component of higher order momentum. Variation 110."""
    res = _cfj_accel(ncfo, 110, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_cash_flow_jerk_accel_v111_signal(ncfo) -> pd.Series:
    """Cash flow acceleration variation 111. Component of higher order momentum. Variation 111."""
    res = _cfj_accel(ncfo, 111, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_cash_flow_jerk_accel_v112_signal(ncfo) -> pd.Series:
    """Cash flow acceleration variation 112. Component of higher order momentum. Variation 112."""
    res = _cfj_accel(ncfo, 112, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_cash_flow_jerk_accel_v113_signal(ncfo) -> pd.Series:
    """Cash flow acceleration variation 113. Component of higher order momentum. Variation 113."""
    res = _cfj_accel(ncfo, 113, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_cash_flow_jerk_accel_v114_signal(ncfo) -> pd.Series:
    """Cash flow acceleration variation 114. Component of higher order momentum. Variation 114."""
    res = _cfj_accel(ncfo, 114, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_cash_flow_jerk_accel_v115_signal(ncfo) -> pd.Series:
    """Cash flow acceleration variation 115. Component of higher order momentum. Variation 115."""
    res = _cfj_accel(ncfo, 115, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_cash_flow_jerk_accel_v116_signal(ncfo) -> pd.Series:
    """Cash flow acceleration variation 116. Component of higher order momentum. Variation 116."""
    res = _cfj_accel(ncfo, 116, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_cash_flow_jerk_accel_v117_signal(ncfo) -> pd.Series:
    """Cash flow acceleration variation 117. Component of higher order momentum. Variation 117."""
    res = _cfj_accel(ncfo, 117, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_cash_flow_jerk_accel_v118_signal(ncfo) -> pd.Series:
    """Cash flow acceleration variation 118. Component of higher order momentum. Variation 118."""
    res = _cfj_accel(ncfo, 118, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_cash_flow_jerk_accel_v119_signal(ncfo) -> pd.Series:
    """Cash flow acceleration variation 119. Component of higher order momentum. Variation 119."""
    res = _cfj_accel(ncfo, 119, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_cash_flow_jerk_accel_v120_signal(ncfo) -> pd.Series:
    """Cash flow acceleration variation 120. Component of higher order momentum. Variation 120."""
    res = _cfj_accel(ncfo, 120, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_cash_flow_jerk_accel_v121_signal(ncfo) -> pd.Series:
    """Cash flow acceleration variation 121. Component of higher order momentum. Variation 121."""
    res = _cfj_accel(ncfo, 121, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_cash_flow_jerk_accel_v122_signal(ncfo) -> pd.Series:
    """Cash flow acceleration variation 122. Component of higher order momentum. Variation 122."""
    res = _cfj_accel(ncfo, 122, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_cash_flow_jerk_accel_v123_signal(ncfo) -> pd.Series:
    """Cash flow acceleration variation 123. Component of higher order momentum. Variation 123."""
    res = _cfj_accel(ncfo, 123, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_cash_flow_jerk_accel_v124_signal(ncfo) -> pd.Series:
    """Cash flow acceleration variation 124. Component of higher order momentum. Variation 124."""
    res = _cfj_accel(ncfo, 124, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_cash_flow_jerk_accel_v125_signal(ncfo) -> pd.Series:
    """Cash flow acceleration variation 125. Component of higher order momentum. Variation 125."""
    res = _cfj_accel(ncfo, 125, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_cash_flow_jerk_accel_v126_signal(ncfo) -> pd.Series:
    """Cash flow acceleration variation 126. Component of higher order momentum. Variation 126."""
    res = _cfj_accel(ncfo, 126, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_cash_flow_jerk_accel_v127_signal(ncfo) -> pd.Series:
    """Cash flow acceleration variation 127. Component of higher order momentum. Variation 127."""
    res = _cfj_accel(ncfo, 127, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_cash_flow_jerk_accel_v128_signal(ncfo) -> pd.Series:
    """Cash flow acceleration variation 128. Component of higher order momentum. Variation 128."""
    res = _cfj_accel(ncfo, 128, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_cash_flow_jerk_accel_v129_signal(ncfo) -> pd.Series:
    """Cash flow acceleration variation 129. Component of higher order momentum. Variation 129."""
    res = _cfj_accel(ncfo, 129, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_cash_flow_jerk_accel_v130_signal(ncfo) -> pd.Series:
    """Cash flow acceleration variation 130. Component of higher order momentum. Variation 130."""
    res = _cfj_accel(ncfo, 130, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_cash_flow_jerk_accel_v131_signal(ncfo) -> pd.Series:
    """Cash flow acceleration variation 131. Component of higher order momentum. Variation 131."""
    res = _cfj_accel(ncfo, 131, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_cash_flow_jerk_accel_v132_signal(ncfo) -> pd.Series:
    """Cash flow acceleration variation 132. Component of higher order momentum. Variation 132."""
    res = _cfj_accel(ncfo, 132, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_cash_flow_jerk_accel_v133_signal(ncfo) -> pd.Series:
    """Cash flow acceleration variation 133. Component of higher order momentum. Variation 133."""
    res = _cfj_accel(ncfo, 133, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_cash_flow_jerk_accel_v134_signal(ncfo) -> pd.Series:
    """Cash flow acceleration variation 134. Component of higher order momentum. Variation 134."""
    res = _cfj_accel(ncfo, 134, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_cash_flow_jerk_accel_v135_signal(ncfo) -> pd.Series:
    """Cash flow acceleration variation 135. Component of higher order momentum. Variation 135."""
    res = _cfj_accel(ncfo, 135, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_cash_flow_jerk_accel_v136_signal(ncfo) -> pd.Series:
    """Cash flow acceleration variation 136. Component of higher order momentum. Variation 136."""
    res = _cfj_accel(ncfo, 136, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_cash_flow_jerk_accel_v137_signal(ncfo) -> pd.Series:
    """Cash flow acceleration variation 137. Component of higher order momentum. Variation 137."""
    res = _cfj_accel(ncfo, 137, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_cash_flow_jerk_accel_v138_signal(ncfo) -> pd.Series:
    """Cash flow acceleration variation 138. Component of higher order momentum. Variation 138."""
    res = _cfj_accel(ncfo, 138, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_cash_flow_jerk_accel_v139_signal(ncfo) -> pd.Series:
    """Cash flow acceleration variation 139. Component of higher order momentum. Variation 139."""
    res = _cfj_accel(ncfo, 139, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_cash_flow_jerk_accel_v140_signal(ncfo) -> pd.Series:
    """Cash flow acceleration variation 140. Component of higher order momentum. Variation 140."""
    res = _cfj_accel(ncfo, 140, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_cash_flow_jerk_accel_v141_signal(ncfo) -> pd.Series:
    """Cash flow acceleration variation 141. Component of higher order momentum. Variation 141."""
    res = _cfj_accel(ncfo, 141, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_cash_flow_jerk_accel_v142_signal(ncfo) -> pd.Series:
    """Cash flow acceleration variation 142. Component of higher order momentum. Variation 142."""
    res = _cfj_accel(ncfo, 142, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_cash_flow_jerk_accel_v143_signal(ncfo) -> pd.Series:
    """Cash flow acceleration variation 143. Component of higher order momentum. Variation 143."""
    res = _cfj_accel(ncfo, 143, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_cash_flow_jerk_accel_v144_signal(ncfo) -> pd.Series:
    """Cash flow acceleration variation 144. Component of higher order momentum. Variation 144."""
    res = _cfj_accel(ncfo, 144, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_cash_flow_jerk_accel_v145_signal(ncfo) -> pd.Series:
    """Cash flow acceleration variation 145. Component of higher order momentum. Variation 145."""
    res = _cfj_accel(ncfo, 145, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_cash_flow_jerk_accel_v146_signal(ncfo) -> pd.Series:
    """Cash flow acceleration variation 146. Component of higher order momentum. Variation 146."""
    res = _cfj_accel(ncfo, 146, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_cash_flow_jerk_accel_v147_signal(ncfo) -> pd.Series:
    """Cash flow acceleration variation 147. Component of higher order momentum. Variation 147."""
    res = _cfj_accel(ncfo, 147, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_cash_flow_jerk_accel_v148_signal(ncfo) -> pd.Series:
    """Cash flow acceleration variation 148. Component of higher order momentum. Variation 148."""
    res = _cfj_accel(ncfo, 148, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_cash_flow_jerk_accel_v149_signal(ncfo) -> pd.Series:
    """Cash flow acceleration variation 149. Component of higher order momentum. Variation 149."""
    res = _cfj_accel(ncfo, 149, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_cash_flow_jerk_accel_v150_signal(ncfo) -> pd.Series:
    """Cash flow acceleration variation 150. Component of higher order momentum. Variation 150."""
    res = _cfj_accel(ncfo, 150, 21)
    return res.replace([np.inf, -np.inf], np.nan)

if __name__ == "__main__":
    import inspect
    np.random.seed(42)
    n = 800
    df = pd.DataFrame({
        "fcf": np.random.normal(10, 2, n).cumsum() + 1000,
        "ncfo": np.random.normal(15, 3, n).cumsum() + 1500,
    })
    
    funcs = [obj for name, obj in inspect.getmembers(inspect.getmodule(inspect.currentframe())) if (inspect.isfunction(obj) and name.startswith("f36_cash_flow_jerk_"))]
    
    print(f"Testing {len(funcs)} functions...")
    for func in funcs:
        sig = inspect.signature(func)
        args = [df[p] for p in sig.parameters]
        y1 = func(*args)
        y2 = func(*args)
        pd.testing.assert_series_equal(y1, y2)
        
        q = y1.iloc[504:].dropna()
        assert len(q) > 0
        assert q.nunique() > 10

    print("All tests passed!")

REGISTRY = {fn.__name__: {"inputs": list(inspect.signature(fn).parameters.keys()), "func": fn} for fn in [obj for name, obj in inspect.getmembers(inspect.getmodule(inspect.currentframe())) if (inspect.isfunction(obj) and name.startswith("f36_cash_flow_jerk_"))]}
F36_CASH_FLOW_JERK_REGISTRY_BASE_076_150 = REGISTRY
