"""Motion design pattern database — reusable timing and transition templates."""
import random

# ── Motion Patterns ────────────────────────────────────────────────────────────

LOGO_ANIMATIONS = [
    {
        "name": "Reveal Scale",
        "beats": [
            {"time": "0.0s", "action": "Logo at 0% opacity, scale 0.5", "easing": "ease-out"},
            {"time": "0.0-0.3s", "action": "Scale up to 1.0 with overshoot", "easing": "elastic(1.2, 0.4)"},
            {"time": "0.3-0.5s", "action": "Opacity fade in 0→100%", "easing": "ease-out"},
            {"time": "0.5-1.0s", "action": "Hold", "easing": "none"},
        ],
        "transitions": ["scale-overshoot", "fade-in"],
        "best_for": ["social-media", "presentations"],
        "duration_range": (1, 3),
    },
    {
        "name": "Slide + Blur",
        "beats": [
            {"time": "0.0s", "action": "Logo off-screen left, blur 20px", "easing": "none"},
            {"time": "0.0-0.4s", "action": "Slide in from left", "easing": "ease-out-expo"},
            {"time": "0.2-0.4s", "action": "Blur reduce 20→0", "easing": "ease-out"},
            {"time": "0.4-1.0s", "action": "Hold", "easing": "none"},
        ],
        "transitions": ["slide-in", "blur-reduce"],
        "best_for": ["youtube", "product-videos"],
        "duration_range": (1, 3),
    },
    {
        "name": "Typewriter",
        "beats": [
            {"time": "0.0s", "action": "Blank screen", "easing": "none"},
            {"time": "0.0-0.8s", "action": "Logo text types in character by character", "easing": "linear"},
            {"time": "0.8-1.0s", "action": "Icon/symbol fades in below", "easing": "ease-out"},
            {"time": "1.0-2.0s", "action": "Hold", "easing": "none"},
        ],
        "transitions": ["typewriter", "fade-in"],
        "best_for": ["tech", "minimal"],
        "duration_range": (2, 4),
    },
    {
        "name": "Morph",
        "beats": [
            {"time": "0.0s", "action": "Abstract shape on screen", "easing": "none"},
            {"time": "0.0-0.6s", "action": "Shape morphs into logo form", "easing": "ease-in-out-cubic"},
            {"time": "0.6-0.8s", "action": "Color fill transition", "easing": "ease-out"},
            {"time": "0.8-1.5s", "action": "Hold with subtle pulse", "easing": "sine-in-out (loop)"},
        ],
        "transitions": ["morph", "color-fill"],
        "best_for": ["brand", "entertainment"],
        "duration_range": (1, 3),
    },
]

TEXT_REVEALS = [
    {
        "name": "Split Reveal",
        "beats": [
            {"time": "0.0s", "action": "Text mask applied, invisible", "easing": "none"},
            {"time": "0.0-0.3s", "action": "Mask splits open from center", "easing": "ease-out-cubic"},
            {"time": "0.3-0.5s", "action": "Text slides up 20px into position", "easing": "ease-out"},
            {"time": "0.5-1.0s", "action": "Hold", "easing": "none"},
        ],
        "transitions": ["mask-split", "slide-up"],
        "best_for": ["headlines", "titles"],
    },
    {
        "name": "Counter",
        "beats": [
            {"time": "0.0s", "action": "Numbers start counting from 0", "easing": "none"},
            {"time": "0.0-1.0s", "action": "Count up to target number", "easing": "ease-out-expo"},
            {"time": "1.0-1.5s", "action": "Label text fades in below", "easing": "ease-out"},
            {"time": "1.5-2.5s", "action": "Hold", "easing": "none"},
        ],
        "transitions": ["counter", "fade-in"],
        "best_for": ["data-viz", "stats"],
    },
]

PRODUCT_INTROS = [
    {
        "name": "Turntable",
        "beats": [
            {"time": "0.0s", "action": "Product center frame, dark background", "easing": "none"},
            {"time": "0.0-1.5s", "action": "Slow 360 rotation", "easing": "linear"},
            {"time": "1.5-2.0s", "action": "Camera zoom to detail", "easing": "ease-in-out"},
            {"time": "2.0-2.5s", "action": "Light sweep across surface", "easing": "ease-out"},
        ],
        "transitions": ["rotation", "zoom", "light-sweep"],
        "best_for": ["e-commerce", "product-launch"],
    },
    {
        "name": "Exploded View",
        "beats": [
            {"time": "0.0s", "action": "Assembled product", "easing": "none"},
            {"time": "0.0-0.8s", "action": "Components separate outward", "easing": "ease-out-cubic"},
            {"time": "0.8-1.2s", "action": "Labels appear on each part", "easing": "fade-in staggered"},
            {"time": "1.2-1.8s", "action": "Components reassemble", "easing": "ease-in-out"},
        ],
        "transitions": ["explode", "label-stagger"],
        "best_for": ["tech", "engineering"],
    },
]

TRANSITIONS = {
    "ease-in": "Accelerating — starts slow, ends fast. Good for exits.",
    "ease-out": "Decelerating — starts fast, ends slow. Good for entrances.",
    "ease-in-out": "Symmetric — smooth acceleration and deceleration.",
    "ease-out-expo": "Fast deceleration — dramatic, premium feel.",
    "ease-out-cubic": "Moderate deceleration — clean, professional.",
    "elastic": "Overshoots target then settles — playful, energetic.",
    "linear": "Constant speed — mechanical, precise.",
    "spring": "Bouncy overshoot — fun, casual.",
}


def get_patterns_for_context(duration: float, platform: str, tone: str) -> list:
    """Find motion patterns that match the brief context."""
    all_patterns = LOGO_ANIMATIONS + TEXT_REVEALS + PRODUCT_INTROS
    scored = []

    for pattern in all_patterns:
        score = 0
        min_d, max_d = pattern.get("duration_range", (0.5, 5))
        if min_d <= duration <= max_d:
            score += 2

        best_for = pattern.get("best_for", [])
        for keyword in best_for:
            if keyword in platform.lower():
                score += 2
            if keyword in tone.lower():
                score += 1

        if score > 0:
            scored.append((score, pattern))

    scored.sort(key=lambda x: -x[0])
    return [p for _, p in scored[:5]]


def generate_timing_breakdown(
    duration: float,
    fps: int = 30,
    sections: list = None,
) -> list:
    """Generate a frame-by-frame timing breakdown."""
    if sections is None:
        sections = [
            {"name": "Intro", "pct": 0.2, "action": "Build anticipation"},
            {"name": "Main", "pct": 0.5, "action": "Core message / reveal"},
            {"name": "Outro", "pct": 0.3, "action": "Settle + CTA"},
        ]

    total_frames = int(duration * fps)
    timeline = []
    current_frame = 0

    for section in sections:
        section_frames = int(section["pct"] * total_frames)
        start_time = current_frame / fps
        end_time = (current_frame + section_frames) / fps

        timeline.append({
            "section": section["name"],
            "start_frame": current_frame,
            "end_frame": current_frame + section_frames,
            "start_time": f"{start_time:.2f}s",
            "end_time": f"{end_time:.2f}s",
            "duration_frames": section_frames,
            "duration_sec": f"{section_frames / fps:.2f}s",
            "action": section["action"],
        })
        current_frame += section_frames

    return timeline


def suggest_easing(context: str) -> str:
    """Suggest easing based on motion context."""
    context_lower = context.lower()
    if "entrance" in context_lower or "enter" in context_lower or "in" in context_lower:
        return "ease-out — fast start, gentle landing. Best for elements arriving on screen."
    elif "exit" in context_lower or "leave" in context_lower or "out" in context_lower:
        return "ease-in — gentle start, fast exit. Best for elements leaving screen."
    elif "loop" in context_lower or "ambient" in context_lower:
        return "linear or sine-in-out — continuous, no clear start/end."
    elif "bounce" in context_lower or "playful" in context_lower:
        return "elastic or spring — overshoots target, adds personality."
    elif "dramatic" in context_lower or "cinematic" in context_lower:
        return "ease-out-expo — strong deceleration, premium feel."
    else:
        return "ease-in-out — safe default, works in most contexts."


def generate_random_brief() -> dict:
    """Generate a random motion design brief for practice."""
    products = [
        "coffee brand logo", "tech startup intro", "fitness app icon",
        "restaurant menu reveal", "podcast cover animation", "book launch title",
        "music festival lineup", "SAAS product demo", "wedding invitation",
        "real estate listing", "clothing brand drop", "podcast episode card",
    ]
    platforms = ["instagram-reel", "youtube", "tiktok", "website-hero", "linkedin", "broadcast"]
    tones = ["energetic", "minimal", "cinematic", "playful", "professional", "elegant", "bold"]
    durations = [1, 2, 3, 4, 5, 6, 8, 10, 15, 30]

    return {
        "product": random.choice(products),
        "platform": random.choice(platforms),
        "tone": random.choice(tones),
        "duration": random.choice(durations),
        "fps": 30,
    }
