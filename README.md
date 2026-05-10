# motion-concept-generator

# Motion Concept Generator

> Turn creative briefs into motion design plans â€” timing breakdowns, transition suggestions, and a pattern library for motion designers.

![Python](https://img.shields.io/badge/Python-3.9+-blue?logo=python)
![Streamlit](https://img.shields.io/badge/Streamlit-1.28-FF4B4B?logo=streamlit)
![License](https://img.shields.io/badge/License-MIT-green)

## The Problem

Motion designers can execute any storyboard in After Effects but freeze at the concept stage. Given "5-second logo animation for a coffee shop, Instagram, $100" â€” they can't structure timing, decide on transitions, or know if their idea is too generic. Tutorials teach software, not creative decision-making.

## The Solution

```bash
pip install streamlit
streamlit run app.py
```

Describe your brief and get:
- **Timing breakdown** â€” frame-by-frame beats with easing
- **Motion pattern suggestions** â€” matched to your platform, tone, duration
- **Easing recommendations** â€” context-aware transition suggestions
- **Practice briefs** â€” randomized prompts with suggested approaches

## Features

### Brief â†’ Concept
Enter product, platform, tone, duration â†’ get matched motion patterns with detailed timing beats.

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

MIT License â€” see [LICENSE](LICENSE) for details.


## Installation

### Prerequisites

- Python 3.8 or higher
- pip (Python package manager)

### Clone the Repository

```bash
git clone https://github.com/darshd9941/motion-concept-generator.git
cd motion-concept-generator
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Environment Setup

1. Copy the example environment file:
   ```bash
   cp .env.example .env
   ```

2. Edit .env and add your API keys:
   ```bash
   # Required for Claude vision features
   ANTHROPIC_API_KEY=your-api-key-here
   ```

## Usage

### Web App (if applicable)

```bash
streamlit run app.py
```

### CLI Usage

```bash
python main.py --help
```

### Python API

```python
from module import MainClass

# Initialize the tool
tool = MainClass()

# Use the tool
result = tool.process("input")
print(result)
```

## Configuration

- .env - Environment variables (API keys, settings)
- config.yaml - Configuration file (if applicable)

## Examples

See the examples/ directory for detailed usage examples.

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## License

See LICENSE file for details.
