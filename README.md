# Motion Concept Generator

> Turn creative briefs into motion design plans — timing breakdowns, transition suggestions, and a pattern library for motion designers.

![Python](https://img.shields.io/badge/Python-3.9+-blue?logo=python)
![Streamlit](https://img.shields.io/badge/Streamlit-1.28-FF4B4B?logo=streamlit)
![License](https://img.shields.io/badge/License-MIT-green)

## The Problem

Motion designers can execute any storyboard in After Effects but freeze at the concept stage. Given "5-second logo animation for a coffee shop, Instagram, $100" — they can't structure timing, decide on transitions, or know if their idea is too generic. Tutorials teach software, not creative decision-making.

## The Solution

```bash
pip install streamlit
streamlit run app.py
```

Describe your brief and get:
- **Timing breakdown** — frame-by-frame beats with easing
- **Motion pattern suggestions** — matched to your platform, tone, duration
- **Easing recommendations** — context-aware transition suggestions
- **Practice briefs** — randomized prompts with suggested approaches

## Features

### Brief → Concept
Enter product, platform, tone, duration → get matched motion patterns with detailed timing beats.

### Timing Calculator
Adjustable intro/main/outro split with frame-accurate breakdown.

### Easing Guide
Visual reference for all easing types with context-aware recommendations.

### Pattern Library
- Logo animations (scale reveal, slide+blur, typewriter, morph)
- Text reveals (split reveal, counter)
- Product intros (turntable, exploded view)

### Practice Mode
Random brief generator with suggested approaches for skill building.

## Quick Start

```bash
git clone https://github.com/darshd9941/motion-concept-generator.git
cd motion-concept-generator
pip install -r requirements.txt
streamlit run app.py
```

## License

MIT License — see [LICENSE](LICENSE) for details.
