"""Motion Concept Generator — Streamlit app for motion designers."""
import sys
import streamlit as st
from patterns import (
    get_patterns_for_context, generate_timing_breakdown,
    suggest_easing, generate_random_brief, TRANSITIONS,
    LOGO_ANIMATIONS, TEXT_REVEALS, PRODUCT_INTROS,
)

st.set_page_config(page_title="Motion Concept Generator", page_icon="🎬", layout="wide")

st.title("🎬 Motion Concept Generator")
st.caption("Turn creative briefs into motion design plans — timing, transitions, patterns")


# ── Sidebar ────────────────────────────────────────────────────────────────────

with st.sidebar:
    st.header("Quick Actions")
    if st.button("🎲 Generate Random Brief", use_container_width=True):
        brief = generate_random_brief()
        st.session_state["product"] = brief["product"]
        st.session_state["platform"] = brief["platform"]
        st.session_state["tone"] = brief["tone"]
        st.session_state["duration"] = brief["duration"]
        st.rerun()

    st.divider()
    st.header("Motion Pattern Library")

    with st.expander("Logo Animations"):
        for p in LOGO_ANIMATIONS:
            st.markdown(f"**{p['name']}**")
            st.caption(f"Best for: {', '.join(p.get('best_for', []))}")
            st.caption(f"Duration: {p.get('duration_range', (1, 3))}s")

    with st.expander("Text Reveals"):
        for p in TEXT_REVEALS:
            st.markdown(f"**{p['name']}**")
            st.caption(f"Best for: {', '.join(p.get('best_for', []))}")

    with st.expander("Product Intros"):
        for p in PRODUCT_INTROS:
            st.markdown(f"**{p['name']}**")
            st.caption(f"Best for: {', '.join(p.get('best_for', []))}")

    with st.expander("Easing Reference"):
        for name, desc in TRANSITIONS.items():
            st.markdown(f"**{name}**: {desc}")


# ── Main Tabs ──────────────────────────────────────────────────────────────────

tab_brief, tab_timing, tab_easing, tab_practice = st.tabs(
    ["📝 Brief → Concept", "⏱️ Timing Breakdown", "📐 Easing Guide", "🎯 Practice Briefs"]
)

with tab_brief:
    st.subheader("Describe Your Motion")

    col1, col2 = st.columns(2)
    with col1:
        product = st.text_input("Product / Subject", value=st.session_state.get("product", ""), placeholder="e.g. coffee brand logo")
        platform = st.selectbox("Platform", [
            "instagram-reel", "youtube", "tiktok", "website-hero",
            "linkedin", "broadcast", "presentation", "app-icon",
        ], index=0)
    with col2:
        tone = st.selectbox("Tone", [
            "energetic", "minimal", "cinematic", "playful",
            "professional", "elegant", "bold", "organic",
        ], index=0)
        duration = st.slider("Duration (seconds)", 0.5, 30.0, 3.0, 0.5)
        fps = st.selectbox("FPS", [24, 25, 30, 60], index=2)

    description = st.text_area("Additional context (optional)", placeholder="e.g. 'text cards slide in from bottom, staggered'")

    if st.button("🎬 Generate Concept", use_container_width=True):
        if not product:
            st.warning("Enter a product/subject")
        else:
            st.markdown("---")
            st.subheader(f"Concept: {product}")

            # Get matching patterns
            patterns = get_patterns_for_context(duration, platform, tone)

            if patterns:
                st.markdown("### Recommended Motion Patterns")
                for i, p in enumerate(patterns):
                    with st.expander(f"{'⭐ ' if i == 0 else ''}{p['name']}", expanded=(i == 0)):
                        st.markdown("**Timing Beats:**")
                        for beat in p["beats"]:
                            st.markdown(f"- `{beat['time']}` — {beat['action']} _{beat['easing']}_")

                        if p.get("transitions"):
                            st.markdown(f"**Transitions:** {', '.join(p['transitions'])}")
                        if p.get("best_for"):
                            st.markdown(f"**Best for:** {', '.join(p['best_for'])}")
            else:
                st.info("No exact pattern match — using generic timing breakdown.")

            # Always show timing breakdown
            st.markdown("### Timing Breakdown")
            timeline = generate_timing_breakdown(duration, fps)
            for t in timeline:
                st.markdown(
                    f"**{t['section']}** — `{t['start_time']}` to `{t['end_time']}` "
                    f"({t['duration_frames']} frames)\n"
                    f"  {t['action']}"
                )

with tab_timing:
    st.subheader("Timing Calculator")

    dur = st.number_input("Total duration (seconds)", 0.5, 60.0, 3.0, 0.1)
    fps_sel = st.number_input("FPS", 1, 120, 30)

    # Custom section split
    st.markdown("**Section Split:**")
    c1, c2, c3 = st.columns(3)
    with c1:
        intro_pct = st.slider("Intro %", 0, 50, 20) / 100
    with c2:
        main_pct = st.slider("Main %", 10, 80, 50) / 100
    with c3:
        outro_pct = st.slider("Outro %", 10, 50, 30) / 100

    total_pct = intro_pct + main_pct + outro_pct
    if abs(total_pct - 1.0) > 0.01:
        st.warning(f"Percentages sum to {total_pct*100:.0f}% (should be 100%)")
    else:
        sections = [
            {"name": "Intro", "pct": intro_pct, "action": "Build anticipation"},
            {"name": "Main", "pct": main_pct, "action": "Core message / reveal"},
            {"name": "Outro", "pct": outro_pct, "action": "Settle + CTA"},
        ]
        timeline = generate_timing_breakdown(dur, fps_sel, sections)

        table_data = []
        for t in timeline:
            table_data.append({
                "Section": t["section"],
                "Start": t["start_time"],
                "End": t["end_time"],
                "Frames": t["duration_frames"],
                "Duration": t["duration_sec"],
                "Action": t["action"],
            })
        st.table(table_data)

        total_frames = int(dur * fps_sel)
        st.info(f"Total: {total_frames} frames at {fps_sel}fps")

with tab_easing:
    st.subheader("Easing Guide")

    context = st.text_input("What are you animating?", placeholder="e.g. logo entrance, text exit, ambient loop")

    if context:
        recommendation = suggest_easing(context)
        st.success(f"**Recommended:** {recommendation}")

    st.markdown("### All Easing Types")
    for name, desc in TRANSITIONS.items():
        with st.expander(name):
            st.write(desc)
            # Visual bar
            import math
            points = []
            for i in range(100):
                t = i / 99
                if name == "ease-in":
                    v = t * t
                elif name == "ease-out":
                    v = 1 - (1 - t) * (1 - t)
                elif name == "ease-in-out":
                    v = 2 * t * t if t < 0.5 else 1 - (-2 * t + 2) ** 2 / 2
                elif name == "elastic":
                    v = 1 if t == 0 or t == 1 else -0.5 * (2 * t - 1) ** 2 * math.sin(12 * math.pi * t) + 0.5
                elif name == "linear":
                    v = t
                else:
                    v = t * t  # default ease-in
                points.append(v)

            # Simple ASCII visualization
            height = 10
            for row in range(height, -1, -1):
                line = ""
                threshold = row / height
                for p in points:
                    line += "█" if abs(p - threshold) < 0.08 else " "
                st.code(line)

with tab_practice:
    st.subheader("Practice Briefs")

    if st.button("🎲 Generate Random Brief"):
        brief = generate_random_brief()
        st.markdown(f"""
        ### Brief
        - **Product:** {brief['product']}
        - **Platform:** {brief['platform']}
        - **Tone:** {brief['tone']}
        - **Duration:** {brief['duration']}s
        - **FPS:** {brief['fps']}
        """)

        with st.expander("Suggested approach"):
            patterns = get_patterns_for_context(brief["duration"], brief["platform"], brief["tone"])
            if patterns:
                st.markdown(f"Try the **{patterns[0]['name']}** pattern:")
                for beat in patterns[0]["beats"]:
                    st.markdown(f"- `{beat['time']}` — {beat['action']}")

    st.markdown("---")
    st.markdown("### Practice Prompts")
    examples = [
        "5s logo animation for a coffee shop — Instagram Reel, warm and organic",
        "10s product reveal for wireless earbuds — YouTube, minimal and clean",
        "3s text card transition — TikTok, energetic and bold",
        "15s app feature showcase — Website hero, professional and smooth",
        "2s notification animation — Mobile app, playful and quick",
    ]
    for ex in examples:
        st.markdown(f"- {ex}")
