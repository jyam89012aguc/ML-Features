"""Audition high-signal feature additions against the existing feature library.

This script does not generate feature implementation files. It is a gate that
checks whether proposed additions are structurally new, backed by silver DB
columns, and worth implementing before expanding the generated feature set.
"""

from __future__ import annotations

import ast
import json
from collections import Counter, defaultdict
from dataclasses import dataclass, asdict
from pathlib import Path

import duckdb


ROOT = Path(__file__).resolve().parent
SILVER_DB = Path(r"C:\Users\jyama\Desktop\silver db\trading.duckdb")
REPORT_PATH = ROOT / "FEATURE_ADDITION_AUDITION.md"
JSON_PATH = ROOT / "feature_addition_audition.json"


@dataclass(frozen=True)
class Candidate:
    family: str
    placement: str
    candidate_name: str
    source_tables: tuple[str, ...]
    source_fields: tuple[str, ...]
    operation: str
    horizon: str
    expected_signal: str
    duplication_guard: str
    upstream_requirement: str
    score: int


def _safe_slug(value: str) -> str:
    return (
        value.lower()
        .replace(" ", "_")
        .replace("/", "_")
        .replace("-", "_")
        .replace("__", "_")
    )


def load_existing_signals() -> tuple[set[str], dict[str, Counter[str]], Counter[str]]:
    names: set[str] = set()
    family_args: dict[str, Counter[str]] = defaultdict(Counter)
    global_args: Counter[str] = Counter()

    for path in ROOT.glob("f*/*.py"):
        tree = ast.parse(path.read_text(encoding="utf-8"))
        family = path.parts[-2]
        for node in tree.body:
            if isinstance(node, ast.FunctionDef) and node.name.endswith("_signal"):
                names.add(node.name)
                args = [arg.arg for arg in node.args.args]
                global_args.update(args)
                family_args[family].update(args)

    return names, family_args, global_args


def load_db_schema() -> dict[str, set[str]]:
    con = duckdb.connect(str(SILVER_DB), read_only=True)
    rows = con.execute(
        """
        select table_name, column_name
        from information_schema.columns
        where table_schema = 'main'
        order by table_name, ordinal_position
        """
    ).fetchall()

    schema: dict[str, set[str]] = defaultdict(set)
    for table, column in rows:
        schema[table].add(column)
    return dict(schema)


def propose_candidates() -> list[Candidate]:
    return [
        Candidate(
            family="f101_price_volume_technicals",
            placement="new_family",
            candidate_name="distance_to_52w_high_low",
            source_tables=("metrics",),
            source_fields=("price", "high52w", "low52w"),
            operation="range_position",
            horizon="52w",
            expected_signal="Captures whether the stock is near breakout, drawdown, or base-building territory.",
            duplication_guard="No existing family uses high52w or low52w as function inputs.",
            upstream_requirement="Join metrics by ticker/date.",
            score=94,
        ),
        Candidate(
            family="f101_price_volume_technicals",
            placement="new_family",
            candidate_name="moving_average_stack",
            source_tables=("metrics",),
            source_fields=("price", "ma50d", "ma200d", "ma50w", "ma200w"),
            operation="trend_stack",
            horizon="50d_200d_50w_200w",
            expected_signal="Separates improving technical regimes from persistent downtrends.",
            duplication_guard="Existing price-context functions use close/closeadj transforms, not precomputed MA stack fields.",
            upstream_requirement="Join metrics by ticker/date.",
            score=92,
        ),
        Candidate(
            family="f102_trading_liquidity",
            placement="new_family",
            candidate_name="dollar_volume_liquidity",
            source_tables=("sep", "daily_prices"),
            source_fields=("closeadj", "volume", "marketcap"),
            operation="dollar_volume_to_marketcap",
            horizon="21d_63d_252d",
            expected_signal="Identifies names where trading capacity is thin relative to market value.",
            duplication_guard="Existing functions use closeadj heavily but do not use volume.",
            upstream_requirement="Join sep and daily_prices by ticker/date.",
            score=95,
        ),
        Candidate(
            family="f102_trading_liquidity",
            placement="new_family",
            candidate_name="volume_shock_vs_average",
            source_tables=("metrics",),
            source_fields=("volume", "volumeavg1m", "volumeavg3m"),
            operation="volume_ratio_and_acceleration",
            horizon="1m_3m",
            expected_signal="Flags attention shocks, liquidity droughts, and abnormal accumulation/distribution windows.",
            duplication_guard="No existing signal uses volumeavg1m or volumeavg3m.",
            upstream_requirement="Join metrics by ticker/date.",
            score=91,
        ),
        Candidate(
            family="f103_corporate_action_risk",
            placement="new_family",
            candidate_name="delisting_bankruptcy_cadence",
            source_tables=("actions",),
            source_fields=("action", "date", "value"),
            operation="action_type_decay_count",
            horizon="63d_252d_504d",
            expected_signal="Distinguishes routine actions from distress-linked actions.",
            duplication_guard="Existing f94 uses placeholder actionvalue, not action-type-specific history.",
            upstream_requirement="Encode actions where action in regulatorydelisting, voluntarydelisting, bankruptcyliquidation.",
            score=96,
        ),
        Candidate(
            family="f103_corporate_action_risk",
            placement="new_family",
            candidate_name="split_ticker_change_instability",
            source_tables=("actions",),
            source_fields=("action", "date", "value", "contraticker"),
            operation="corporate_identity_instability",
            horizon="252d_1008d",
            expected_signal="Captures reverse-split/ticker-change churn often linked to microcap stress.",
            duplication_guard="No existing signal uses action categories or contraticker.",
            upstream_requirement="Encode split, adrratiosplit, tickerchangeto, tickerchangefrom events.",
            score=90,
        ),
        Candidate(
            family="f104_event_code_intensity",
            placement="new_family",
            candidate_name="event_code_entropy",
            source_tables=("events",),
            source_fields=("eventcodes", "date"),
            operation="categorical_entropy",
            horizon="63d_252d",
            expected_signal="Measures whether event activity is broadening beyond a single recurring event type.",
            duplication_guard="Avoids simple event counts already approximated by f95 eventcount placeholder.",
            upstream_requirement="Split pipe-delimited eventcodes into per-code indicators before rolling entropy.",
            score=89,
        ),
        Candidate(
            family="f104_event_code_intensity",
            placement="new_family",
            candidate_name="event_code_transition_rate",
            source_tables=("events",),
            source_fields=("eventcodes", "date"),
            operation="categorical_transition_rate",
            horizon="252d",
            expected_signal="Captures regime change in event mix rather than event volume alone.",
            duplication_guard="Existing f95 does not use eventcodes or code transitions.",
            upstream_requirement="Sort events by ticker/date and compare current code set with prior event code set.",
            score=87,
        ),
        Candidate(
            family="f105_insider_transaction_microstructure",
            placement="new_family",
            candidate_name="open_market_purchase_pressure",
            source_tables=("sf2",),
            source_fields=("transactioncode", "transactionshares", "transactionpricepershare", "transactionvalue"),
            operation="transaction_code_weighted_flow",
            horizon="30d_90d_180d",
            expected_signal="Separates open-market purchases from grants, exercises, gifts, and tax-withholding sales.",
            duplication_guard="Existing insider families use broad transactionvalue, not transactioncode-specific flow.",
            upstream_requirement="Map Form 4 transaction codes; emphasize P and S, downweight A/M/F/G.",
            score=97,
        ),
        Candidate(
            family="f105_insider_transaction_microstructure",
            placement="new_family",
            candidate_name="officer_director_alignment",
            source_tables=("sf2",),
            source_fields=("isdirector", "isofficer", "istenpercentowner", "transactioncode", "transactionvalue"),
            operation="role_weighted_net_flow",
            horizon="90d_365d",
            expected_signal="Weights insider transactions by role and control status.",
            duplication_guard="Existing role-split family does not use the full role flag interaction with transaction codes.",
            upstream_requirement="Convert Y/N role flags to numeric weights.",
            score=93,
        ),
        Candidate(
            family="f106_institutional_security_mix",
            placement="new_family",
            candidate_name="put_call_ownership_skew",
            source_tables=("sf3a",),
            source_fields=("putholders", "cllholders", "putvalue", "cllvalue", "totalvalue"),
            operation="options_holder_value_skew",
            horizon="quarterly",
            expected_signal="Measures institutional downside hedging versus upside positioning.",
            duplication_guard="Existing institutional features use value/units, not put/call holder and value mixes.",
            upstream_requirement="Use sf3a aggregate security-type columns by ticker/calendardate.",
            score=94,
        ),
        Candidate(
            family="f106_institutional_security_mix",
            placement="new_family",
            candidate_name="warrant_debt_preferred_overhang",
            source_tables=("sf3a",),
            source_fields=("wntholders", "dbtholders", "prfholders", "wntvalue", "dbtvalue", "prfvalue", "totalvalue"),
            operation="non_common_security_mix",
            horizon="quarterly",
            expected_signal="Flags non-common institutional exposure that may imply financing complexity or overhang.",
            duplication_guard="Existing holder concentration features do not use warrant/debt/preferred security-type mixes.",
            upstream_requirement="Use sf3a aggregate security-type columns by ticker/calendardate.",
            score=90,
        ),
        Candidate(
            family="f107_listing_lifecycle_metadata",
            placement="new_family",
            candidate_name="public_age_and_delisting_pressure",
            source_tables=("tickers", "sep"),
            source_fields=("firstpricedate", "lastpricedate", "isdelisted", "date"),
            operation="listing_age_and_terminal_flag",
            horizon="point_in_time",
            expected_signal="Separates newly public, mature, stale, and delisting-risk names.",
            duplication_guard="No existing signal uses firstpricedate, lastpricedate, or isdelisted.",
            upstream_requirement="Compute point-in-time age and days-to-last-price without lookahead.",
            score=88,
        ),
        Candidate(
            family="f108_true_sector_industry_relative",
            placement="new_family",
            candidate_name="biotech_peer_relative_cash_runway",
            source_tables=("tickers", "fundamentals"),
            source_fields=("industry", "sector", "cashneq", "ncfo", "marketcap"),
            operation="industry_cross_sectional_percentile",
            horizon="quarterly",
            expected_signal="Ranks runway and cash strength against actual biotech peers rather than the whole market.",
            duplication_guard="Existing f99 appears template-based and does not take sector/industry arguments.",
            upstream_requirement="Compute peer group from tickers industry/sector and avoid future membership leakage.",
            score=95,
        ),
        Candidate(
            family="f109_valuation_normalization_flags",
            placement="new_family",
            candidate_name="negative_valuation_flag_blend",
            source_tables=("fundamentals",),
            source_fields=("has_negative_pe", "has_negative_pb", "has_negative_earnings", "has_negative_equity", "alternative_valuation_needed"),
            operation="boolean_flag_blend",
            horizon="quarterly",
            expected_signal="Captures when conventional valuation metrics are structurally invalid.",
            duplication_guard="No existing signal uses normalized valuation flags.",
            upstream_requirement="Cast boolean flags to numeric point-in-time series.",
            score=87,
        ),
        Candidate(
            family="f21_total_debt",
            placement="existing_family_v151_plus",
            candidate_name="noncurrent_debt_load",
            source_tables=("fundamentals",),
            source_fields=("debtnc", "debt", "assets", "marketcap"),
            operation="debtnc_scaled_level",
            horizon="63d_252d",
            expected_signal="Distinguishes long-term financing burden from current debt pressure.",
            duplication_guard="Existing f21 uses debt broadly; this requires debtnc and rejects debt-only transforms.",
            upstream_requirement="Use fundamentals point-in-time values.",
            score=86,
        ),
        Candidate(
            family="f22_debt_mix",
            placement="existing_family_v151_plus",
            candidate_name="current_noncurrent_debt_mix",
            source_tables=("fundamentals",),
            source_fields=("debtc", "debtnc", "debt"),
            operation="current_to_noncurrent_debt_ratio",
            horizon="63d_252d",
            expected_signal="Captures debt maturity pressure and refinancing risk.",
            duplication_guard="Uses debtnc, which existing f22 signatures do not use.",
            upstream_requirement="Use fundamentals point-in-time values.",
            score=91,
        ),
        Candidate(
            family="f36_asset_composition",
            placement="existing_family_v151_plus",
            candidate_name="investment_liquidity_mix",
            source_tables=("fundamentals",),
            source_fields=("investments", "investmentsc", "investmentsnc", "assets", "cashneq"),
            operation="investment_component_ratios",
            horizon="63d_252d",
            expected_signal="Improves liquidity quality by separating cash from current and noncurrent investments.",
            duplication_guard="Existing asset composition does not use investments/investmentsc/investmentsnc.",
            upstream_requirement="Use fundamentals point-in-time values.",
            score=92,
        ),
        Candidate(
            family="f38_tangible_book",
            placement="existing_family_v151_plus",
            candidate_name="diluted_tangible_book_per_share",
            source_tables=("fundamentals",),
            source_fields=("tbvps", "bvps", "shareswadil", "equity", "intangibles"),
            operation="diluted_tangible_book_context",
            horizon="63d_252d",
            expected_signal="Adds dilution-aware tangible book context for balance sheet support.",
            duplication_guard="Existing f38 uses tangibles but not tbvps, bvps, or shareswadil.",
            upstream_requirement="Use fundamentals point-in-time values.",
            score=85,
        ),
        Candidate(
            family="f55_eps_level",
            placement="existing_family_v151_plus",
            candidate_name="diluted_usd_eps_context",
            source_tables=("fundamentals",),
            source_fields=("eps", "epsdil", "epsusd", "pe", "pe1"),
            operation="diluted_eps_and_multiple_context",
            horizon="63d_252d",
            expected_signal="Separates basic EPS from diluted and USD-normalized EPS context.",
            duplication_guard="Existing f55 uses eps but not epsdil, epsusd, pe, or pe1.",
            upstream_requirement="Use fundamentals point-in-time values.",
            score=84,
        ),
        Candidate(
            family="f73_market_cap",
            placement="existing_family_v151_plus",
            candidate_name="marketcap_liquidity_turnover",
            source_tables=("daily_prices", "sep"),
            source_fields=("marketcap", "closeadj", "volume"),
            operation="dollar_volume_marketcap_turnover",
            horizon="21d_63d_252d",
            expected_signal="Shows whether market cap is supported by actual trading liquidity.",
            duplication_guard="Existing f73 uses marketcap but not volume.",
            upstream_requirement="Join sep and daily_prices by ticker/date.",
            score=89,
        ),
        Candidate(
            family="f77_price_book",
            placement="existing_family_v151_plus",
            candidate_name="normalized_price_book_validity",
            source_tables=("fundamentals",),
            source_fields=("pb", "pb_normalized", "has_negative_pb", "has_negative_equity"),
            operation="pb_validity_adjusted_level",
            horizon="63d_252d",
            expected_signal="Prevents naive price/book signals when equity is negative or PB requires normalization.",
            duplication_guard="Existing f77 uses pb but not pb_normalized or negative-equity flags.",
            upstream_requirement="Cast boolean flags to numeric point-in-time series.",
            score=88,
        ),
        Candidate(
            family="f95_event_density",
            placement="existing_family_v151_plus",
            candidate_name="event_code_specific_density",
            source_tables=("events",),
            source_fields=("eventcodes", "date"),
            operation="event_code_specific_decay_count",
            horizon="63d_252d",
            expected_signal="Adds event-type composition while avoiding generic event count duplication.",
            duplication_guard="Requires parsed eventcodes; rejects simple total eventcount transforms.",
            upstream_requirement="Split pipe-delimited eventcodes into code indicators.",
            score=86,
        ),
        Candidate(
            family="f97_multi_year_price_context",
            placement="existing_family_v151_plus",
            candidate_name="beta_adjusted_drawdown_context",
            source_tables=("metrics",),
            source_fields=("price", "high52w", "low52w", "high5y", "low5y", "beta1y", "beta5y"),
            operation="beta_adjusted_range_position",
            horizon="52w_5y",
            expected_signal="Distinguishes idiosyncratic drawdowns from high-beta market-linked declines.",
            duplication_guard="Existing f97 uses close; this requires range and beta fields.",
            upstream_requirement="Join metrics by ticker/date.",
            score=93,
        ),
    ]


def evaluate_candidates(
    candidates: list[Candidate],
    existing_names: set[str],
    family_args: dict[str, Counter[str]],
    global_args: Counter[str],
    db_schema: dict[str, set[str]],
) -> list[dict[str, object]]:
    seen_signatures: set[tuple[str, str, tuple[str, ...], str]] = set()
    rows: list[dict[str, object]] = []
    all_db_fields = set().union(*db_schema.values())

    for c in candidates:
        proposed_signal_name = f"{_safe_slug(c.family)}_{_safe_slug(c.candidate_name)}_audition_signal"
        missing_tables = [t for t in c.source_tables if t not in db_schema]
        missing_fields = [f for f in c.source_fields if f not in all_db_fields]
        fields_tuple = tuple(sorted(c.source_fields))
        signature = (c.family, c.operation, fields_tuple, c.horizon)

        used_by_family = set(family_args.get(c.family, Counter()))
        new_to_family = [f for f in c.source_fields if f not in used_by_family]
        new_to_global = [f for f in c.source_fields if f not in global_args]

        implemented = c.family in family_args and any(f in used_by_family for f in c.source_fields)
        rejection_reasons: list[str] = []
        if proposed_signal_name in existing_names:
            rejection_reasons.append("name already exists")
        if missing_tables:
            rejection_reasons.append("missing source tables: " + ", ".join(missing_tables))
        if missing_fields:
            rejection_reasons.append("missing source fields: " + ", ".join(missing_fields))
        if signature in seen_signatures:
            rejection_reasons.append("duplicate candidate signature")
        if c.placement.startswith("existing_family") and not implemented and not new_to_family:
            rejection_reasons.append("no source field is new to the target family")
        if c.placement == "new_family" and not new_to_global and not implemented and "cross_sectional" not in c.operation:
            rejection_reasons.append("new family does not introduce unused source fields or a true peer operation")
        if c.score < 84:
            rejection_reasons.append("score below high-signal threshold")

        status = "implemented" if implemented and not rejection_reasons else "approved" if not rejection_reasons else "rejected"
        seen_signatures.add(signature)
        row = asdict(c)
        row.update(
            {
                "status": status,
                "proposed_signal_name": proposed_signal_name,
                "new_to_target_family": new_to_family,
                "new_to_existing_library": new_to_global,
                "rejection_reasons": rejection_reasons,
            }
        )
        rows.append(row)

    rows.sort(key=lambda r: (r["status"] != "approved", -int(r["score"]), str(r["family"])))
    return rows


def write_outputs(rows: list[dict[str, object]], existing_names: set[str], family_args: dict[str, Counter[str]]) -> None:
    implemented = [r for r in rows if r["status"] == "implemented"]
    approved = [r for r in rows if r["status"] == "approved"]
    rejected = [r for r in rows if r["status"] != "approved"]
    rejected = [r for r in rows if r["status"] == "rejected"]

    JSON_PATH.write_text(json.dumps(rows, indent=2), encoding="utf-8")

    lines: list[str] = []
    lines.append("# Feature Addition Audition")
    lines.append("")
    lines.append("Silver DB: `C:\\Users\\jyama\\Desktop\\silver db\\trading.duckdb`")
    lines.append("")
    lines.append("## Gate Summary")
    lines.append("")
    lines.append(f"- Existing signal names parsed: {len(existing_names):,}")
    lines.append(f"- Existing target families parsed: {len(family_args):,}")
    lines.append(f"- Curated candidates evaluated: {len(rows):,}")
    lines.append(f"- Implemented candidates detected: {len(implemented):,}")
    lines.append(f"- Approved high-signal candidates still pending: {len(approved):,}")
    lines.append(f"- Rejected candidates: {len(rejected):,}")
    lines.append("")
    lines.append("This is a curated audition set, not a broad combinatorial expansion. A candidate is approved only if it has a unique proposed name, valid silver DB source fields, a unique source-field/operation/horizon signature, and either introduces fields unused by the target family or is a true peer/cross-field composite.")
    lines.append("")
    if implemented:
        lines.append("## Implemented Candidates")
        lines.append("")
        lines.append("| Rank | Family | Candidate | Score | Source fields now present in family |")
        lines.append("| ---: | --- | --- | ---: | --- |")
        for idx, row in enumerate(implemented, 1):
            fields = [f for f in row["source_fields"] if f in family_args.get(row["family"], Counter())]
            lines.append(
                "| {rank} | `{family}` | `{name}` | {score} | {fields} |".format(
                    rank=idx,
                    family=row["family"],
                    name=row["candidate_name"],
                    score=row["score"],
                    fields=", ".join(f"`{f}`" for f in fields),
                )
            )
        lines.append("")

    lines.append("## Approved Pending Candidates")
    lines.append("")
    lines.append("| Rank | Family | Placement | Candidate | Score | Novel source fields | Expected signal | Guard |")
    lines.append("| ---: | --- | --- | --- | ---: | --- | --- | --- |")
    for idx, row in enumerate(approved, 1):
        novelty_fields = (
            row["new_to_existing_library"]
            if row["placement"] == "new_family"
            else row["new_to_target_family"]
        )
        lines.append(
            "| {rank} | `{family}` | `{placement}` | `{name}` | {score} | {fields} | {signal} | {guard} |".format(
                rank=idx,
                family=row["family"],
                placement=row["placement"],
                name=row["candidate_name"],
                score=row["score"],
                fields=", ".join(f"`{f}`" for f in novelty_fields) or "cross-field composite",
                signal=row["expected_signal"],
                guard=row["duplication_guard"],
            )
        )
    lines.append("")
    lines.append("## Implementation Bias")
    lines.append("")
    lines.append("The best first implementation batch should be small and source-aware, not a broad mechanical template expansion. Prioritize:")
    lines.append("")
    lines.append("1. `f105_insider_transaction_microstructure`: transaction-code-weighted Form 4 flow is strongly differentiated from existing broad insider value signals.")
    lines.append("2. `f103_corporate_action_risk`: bankruptcy, delisting, split, and ticker-change histories add real distress/event content.")
    lines.append("3. `f102_trading_liquidity`: volume and dollar-volume turnover add an important tradability layer missing from the current features.")
    lines.append("4. `f106_institutional_security_mix`: put/call/warrant/debt/preferred mixes are materially different from current value/unit ownership features.")
    lines.append("5. `f108_true_sector_industry_relative`: only if the feature pipeline can perform point-in-time peer grouping without lookahead.")
    lines.append("")
    lines.append("## Rejected Candidates")
    lines.append("")
    if rejected:
        lines.append("| Family | Candidate | Reasons |")
        lines.append("| --- | --- | --- |")
        for row in rejected:
            lines.append(
                "| `{}` | `{}` | {} |".format(
                    row["family"],
                    row["candidate_name"],
                    "; ".join(row["rejection_reasons"]),
                )
            )
    else:
        lines.append("No candidates were rejected in this audition pass.")
    lines.append("")
    lines.append("## Next Gate Before Code Generation")
    lines.append("")
    lines.append("- Define upstream derived columns for categorical sources before writing signal functions: action-type indicators, parsed event-code indicators, transaction-code buckets, and security-type mixes.")
    lines.append("- Generate additions into new files only: new families as `f101+`, existing-family additions as `*_151_225_claude.py` files.")
    lines.append("- Re-run this audition script after any generated feature files are added; any newly duplicated name or signature should fail the gate before more code is produced.")
    lines.append("")

    REPORT_PATH.write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    if not SILVER_DB.exists():
        raise FileNotFoundError(SILVER_DB)

    existing_names, family_args, global_args = load_existing_signals()
    db_schema = load_db_schema()
    rows = evaluate_candidates(propose_candidates(), existing_names, family_args, global_args, db_schema)
    write_outputs(rows, existing_names, family_args)
    approved = sum(1 for row in rows if row["status"] == "approved")
    implemented = sum(1 for row in rows if row["status"] == "implemented")
    rejected = sum(1 for row in rows if row["status"] == "rejected")
    print(f"evaluated={len(rows)} implemented={implemented} approved_pending={approved} rejected={rejected}")
    print(f"report={REPORT_PATH}")
    print(f"json={JSON_PATH}")


if __name__ == "__main__":
    main()
