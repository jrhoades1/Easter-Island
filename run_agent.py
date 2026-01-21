#!/usr/bin/env python3
"""
CLI entry point for running Rongorongo analysis agents.

Usage:
    python run_agent.py segmentation --image input/tablets/tablet_a.jpg
    python run_agent.py pattern-mining --lexicon output/rongorongo_lexicon.json
    python run_agent.py lexical-validation --cross-refs output/cross_reference_lexicon.json

Options:
    --provider anthropic|openai|mock  (default: mock)
    --model MODEL_ID                   (default: provider default)
    --cache-dir .cache/llm            (default: .cache/llm)
    --no-cache                         Disable response caching
    --output output/                   (default: output/)
    --verbose                          Show detailed progress
"""

import argparse
import json
import sys
from datetime import datetime
from pathlib import Path

# Import agents
from agents import LLMProviderFactory, LLMCache
from agents.base.providers import MockProvider, AnthropicProvider, OpenAIProvider
from agents.segmentation import GlyphSegmentationAgent
from agents.pattern_mining import PatternMiningAgent
from agents.lexical_validation import LexicalValidationAgent


def load_json(path: str) -> dict:
    """Load JSON file."""
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def save_json(data: dict, path: str) -> None:
    """Save JSON file."""
    Path(path).parent.mkdir(parents=True, exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)


def create_provider(args) -> "LLMProvider":
    """Create LLM provider based on arguments."""
    provider_name = args.provider

    if provider_name == "mock":
        return MockProvider()
    elif provider_name == "anthropic":
        kwargs = {}
        if args.model:
            kwargs["model"] = args.model
        return LLMProviderFactory.create("anthropic", **kwargs)
    elif provider_name == "openai":
        kwargs = {}
        if args.model:
            kwargs["model"] = args.model
        return LLMProviderFactory.create("openai", **kwargs)
    else:
        raise ValueError(f"Unknown provider: {provider_name}")


def create_cache(args) -> LLMCache | None:
    """Create cache if enabled."""
    if args.no_cache:
        return None
    return LLMCache(cache_dir=args.cache_dir)


def run_segmentation(args) -> dict:
    """Run glyph segmentation agent."""
    print(f"Running segmentation agent on: {args.image}")

    provider = create_provider(args)
    cache = create_cache(args)

    agent = GlyphSegmentationAgent(provider, cache)

    # Load CV segmentation results if available
    cv_path = Path(args.output) / "cv_segmentation.json"
    if cv_path.exists():
        cv_seg = load_json(str(cv_path))
    else:
        # Create minimal input for demo
        cv_seg = {
            "glyphs": [],
            "ambiguous_regions": [],
        }
        print("Warning: No CV segmentation found. Running with empty input.")

    input_data = {
        "source_image": args.image,
        "cv_segmentation": cv_seg,
        "glyph_images": {},
        "analyze_ligatures": True,
        "analyze_damage": True,
    }

    result = agent.execute(input_data)

    # Save results
    output_path = Path(args.output) / "segmentation_results.json"
    save_json(result, str(output_path))
    print(f"Results saved to: {output_path}")

    return result


def run_pattern_mining(args) -> dict:
    """Run pattern mining agent."""
    print(f"Running pattern mining agent on: {args.lexicon}")

    provider = create_provider(args)
    cache = create_cache(args)

    agent = PatternMiningAgent(provider, cache)

    # Load glyph lexicon
    lexicon = load_json(args.lexicon)

    input_data = {
        "glyph_lexicon": lexicon,
        "glyph_features": {},
        "glyph_images": {},
        "max_ngram": 5,
        "min_pattern_frequency": 2,
        "similarity_threshold": 0.7,
    }

    result = agent.execute(input_data)

    # Save results
    output_path = Path(args.output) / "pattern_mining_results.json"
    save_json(result, str(output_path))
    print(f"Results saved to: {output_path}")

    return result


def run_lexical_validation(args) -> dict:
    """Run lexical validation agent."""
    print(f"Running lexical validation agent on: {args.cross_refs}")

    provider = create_provider(args)
    cache = create_cache(args)

    agent = LexicalValidationAgent(provider, cache)

    # Load cross-reference lexicon
    cross_refs = load_json(args.cross_refs)

    # Load Polynesian corpora if available
    polynesian_corpora = {}
    corpora_path = Path(args.output) / "polynesian_corpora.json"
    if corpora_path.exists():
        polynesian_corpora = load_json(str(corpora_path))

    # Load Rapa Nui lexicon if available
    rapa_nui = {}
    rn_path = Path(args.output) / "rapa_nui_language.json"
    if rn_path.exists():
        rapa_nui = load_json(str(rn_path))

    input_data = {
        "cross_references": cross_refs,
        "polynesian_corpora": polynesian_corpora,
        "rapa_nui_lexicon": rapa_nui,
        "min_cognate_languages": 2,
        "confidence_boost": 0.15,
    }

    result = agent.execute(input_data)

    # Save results
    output_path = Path(args.output) / "lexical_validation_results.json"
    save_json(result, str(output_path))
    print(f"Results saved to: {output_path}")

    return result


def main():
    parser = argparse.ArgumentParser(
        description="Run Rongorongo analysis agents",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__,
    )

    # Global options
    parser.add_argument(
        "--provider",
        choices=["anthropic", "openai", "mock"],
        default="mock",
        help="LLM provider to use (default: mock)",
    )
    parser.add_argument(
        "--model",
        help="Model ID to use (provider-specific)",
    )
    parser.add_argument(
        "--cache-dir",
        default=".cache/llm",
        help="Directory for response cache (default: .cache/llm)",
    )
    parser.add_argument(
        "--no-cache",
        action="store_true",
        help="Disable response caching",
    )
    parser.add_argument(
        "--output",
        default="output",
        help="Output directory (default: output)",
    )
    parser.add_argument(
        "--verbose",
        action="store_true",
        help="Show detailed progress",
    )

    subparsers = parser.add_subparsers(dest="command", required=True)

    # Segmentation command
    seg_parser = subparsers.add_parser(
        "segmentation",
        help="Run glyph segmentation agent",
    )
    seg_parser.add_argument(
        "--image",
        required=True,
        help="Path to tablet image",
    )

    # Pattern mining command
    pattern_parser = subparsers.add_parser(
        "pattern-mining",
        help="Run pattern mining agent",
    )
    pattern_parser.add_argument(
        "--lexicon",
        required=True,
        help="Path to rongorongo_lexicon.json",
    )

    # Lexical validation command
    lex_parser = subparsers.add_parser(
        "lexical-validation",
        help="Run lexical validation agent",
    )
    lex_parser.add_argument(
        "--cross-refs",
        required=True,
        help="Path to cross_reference_lexicon.json",
    )

    args = parser.parse_args()

    # Create output directory
    Path(args.output).mkdir(parents=True, exist_ok=True)

    # Run appropriate agent
    start_time = datetime.now()

    try:
        if args.command == "segmentation":
            result = run_segmentation(args)
        elif args.command == "pattern-mining":
            result = run_pattern_mining(args)
        elif args.command == "lexical-validation":
            result = run_lexical_validation(args)
        else:
            parser.print_help()
            sys.exit(1)

        # Print summary
        elapsed = datetime.now() - start_time
        print(f"\nCompleted in {elapsed.total_seconds():.2f}s")

        if result.get("success"):
            metadata = result.get("run_metadata", {})
            print(f"Run ID: {metadata.get('run_id', 'N/A')}")
            print(f"LLM calls: {metadata.get('total_llm_calls', 0)}")
            print(f"Cache hits: {metadata.get('cache_hits', 0)}")
            print(f"Total cost: ${metadata.get('total_cost_usd', 0):.4f}")
        else:
            print(f"Error: {result.get('error', 'Unknown error')}")
            sys.exit(1)

    except FileNotFoundError as e:
        print(f"Error: File not found - {e}")
        sys.exit(1)
    except json.JSONDecodeError as e:
        print(f"Error: Invalid JSON - {e}")
        sys.exit(1)
    except Exception as e:
        print(f"Error: {e}")
        if args.verbose:
            import traceback
            traceback.print_exc()
        sys.exit(1)


if __name__ == "__main__":
    main()
