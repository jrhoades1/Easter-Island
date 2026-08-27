"""Data models for Rongorongo glyph cataloging."""

from dataclasses import dataclass, field
from datetime import datetime
from typing import Optional


@dataclass
class BoundingBox:
    """Represents the location of a glyph in an image."""

    x: int
    y: int
    width: int
    height: int

    @property
    def area(self) -> int:
        """Calculate the area of the bounding box."""
        return self.width * self.height

    @property
    def center(self) -> tuple[int, int]:
        """Calculate the center point of the bounding box."""
        return (self.x + self.width // 2, self.y + self.height // 2)

    def overlaps(self, other: "BoundingBox") -> bool:
        """Check if this bounding box overlaps with another."""
        return not (
            self.x + self.width <= other.x
            or other.x + other.width <= self.x
            or self.y + self.height <= other.y
            or other.y + other.height <= self.y
        )

    def to_dict(self) -> dict:
        """Convert to dictionary for JSON serialization."""
        return {
            "x": self.x,
            "y": self.y,
            "width": self.width,
            "height": self.height,
        }

    @classmethod
    def from_dict(cls, data: dict) -> "BoundingBox":
        """Create from dictionary."""
        return cls(
            x=data["x"],
            y=data["y"],
            width=data["width"],
            height=data["height"],
        )


@dataclass
class GlyphPosition:
    """Represents the position of a glyph within the text structure."""

    line_number: int
    position_in_line: int
    total_in_line: int = 0

    def to_dict(self) -> dict:
        """Convert to dictionary for JSON serialization."""
        return {
            "line_number": self.line_number,
            "position_in_line": self.position_in_line,
            "total_in_line": self.total_in_line,
        }

    @classmethod
    def from_dict(cls, data: dict) -> "GlyphPosition":
        """Create from dictionary."""
        return cls(
            line_number=data["line_number"],
            position_in_line=data["position_in_line"],
            total_in_line=data.get("total_in_line", 0),
        )

    def __lt__(self, other: "GlyphPosition") -> bool:
        """Compare positions for ordering (top to bottom, left to right)."""
        if self.line_number != other.line_number:
            return self.line_number < other.line_number
        return self.position_in_line < other.position_in_line


@dataclass
class PositionStats:
    """Statistics about where a glyph type appears."""

    line_distribution: dict[int, int] = field(default_factory=dict)
    avg_position_in_line: float = 0.0
    common_neighbors: list[str] = field(default_factory=list)

    def to_dict(self) -> dict:
        """Convert to dictionary for JSON serialization."""
        return {
            "line_distribution": {str(k): v for k, v in self.line_distribution.items()},
            "avg_position_in_line": round(self.avg_position_in_line, 3),
            "common_neighbors": self.common_neighbors,
        }

    @classmethod
    def from_dict(cls, data: dict) -> "PositionStats":
        """Create from dictionary."""
        return cls(
            line_distribution={int(k): v for k, v in data.get("line_distribution", {}).items()},
            avg_position_in_line=data.get("avg_position_in_line", 0.0),
            common_neighbors=data.get("common_neighbors", []),
        )


@dataclass
class GlyphInstance:
    """Represents a single detected glyph occurrence."""

    instance_id: str
    source_image: str
    bounding_box: BoundingBox
    features: list[float] = field(default_factory=list)
    cluster_id: Optional[str] = None
    position: Optional[GlyphPosition] = None
    confidence: float = 1.0
    image_path: Optional[str] = None
    from_ligature_split: bool = False
    ink_profile: list[float] = field(default_factory=list)

    def to_dict(self) -> dict:
        """Convert to dictionary for JSON serialization."""
        result = {
            "instance_id": self.instance_id,
            "source_image": self.source_image,
            "bounding_box": self.bounding_box.to_dict(),
            "confidence": round(self.confidence, 3),
        }
        if self.cluster_id:
            result["cluster_id"] = self.cluster_id
        if self.position:
            result["position"] = self.position.to_dict()
        if self.image_path:
            result["image_path"] = self.image_path
        # Features excluded from JSON output (too large)
        return result

    @classmethod
    def from_dict(cls, data: dict) -> "GlyphInstance":
        """Create from dictionary."""
        return cls(
            instance_id=data["instance_id"],
            source_image=data["source_image"],
            bounding_box=BoundingBox.from_dict(data["bounding_box"]),
            cluster_id=data.get("cluster_id"),
            position=GlyphPosition.from_dict(data["position"]) if data.get("position") else None,
            confidence=data.get("confidence", 1.0),
            image_path=data.get("image_path"),
        )

    @staticmethod
    def generate_id(source_image: str, index: int) -> str:
        """Generate a unique instance ID."""
        # Remove extension and use as prefix
        import os

        base = os.path.splitext(os.path.basename(source_image))[0]
        return f"{base}_{index:04d}"


@dataclass
class GlyphCluster:
    """Represents a glyph type (group of similar instances)."""

    cluster_id: str
    instances: list[str] = field(default_factory=list)
    representative_image: Optional[str] = None
    mean_features: list[float] = field(default_factory=list)
    positions: PositionStats = field(default_factory=PositionStats)

    @property
    def frequency(self) -> int:
        """Return the number of instances in this cluster."""
        return len(self.instances)

    def add_instance(self, instance_id: str) -> None:
        """Add an instance to this cluster."""
        if instance_id not in self.instances:
            self.instances.append(instance_id)

    def to_dict(self) -> dict:
        """Convert to dictionary for JSON serialization."""
        result = {
            "cluster_id": self.cluster_id,
            "frequency": self.frequency,
            "instances": self.instances,
            "positions": self.positions.to_dict(),
        }
        if self.representative_image:
            result["representative_image"] = self.representative_image
        # Mean features excluded from JSON output (too large)
        return result

    @classmethod
    def from_dict(cls, data: dict) -> "GlyphCluster":
        """Create from dictionary."""
        return cls(
            cluster_id=data["cluster_id"],
            instances=data.get("instances", []),
            representative_image=data.get("representative_image"),
            positions=PositionStats.from_dict(data.get("positions", {})),
        )

    @staticmethod
    def generate_id(index: int) -> str:
        """Generate a cluster ID in format G001, G002, etc."""
        return f"G{index:03d}"


@dataclass
class LexiconStatistics:
    """Statistics about the entire lexicon."""

    avg_glyphs_per_line: float = 0.0
    most_frequent_glyphs: list[str] = field(default_factory=list)
    hapax_legomena: int = 0  # Glyphs that appear only once
    clustering_params: dict = field(default_factory=dict)

    def to_dict(self) -> dict:
        """Convert to dictionary for JSON serialization."""
        return {
            "avg_glyphs_per_line": round(self.avg_glyphs_per_line, 2),
            "most_frequent_glyphs": self.most_frequent_glyphs,
            "hapax_legomena": self.hapax_legomena,
            "clustering_params": self.clustering_params,
        }

    @classmethod
    def from_dict(cls, data: dict) -> "LexiconStatistics":
        """Create from dictionary."""
        return cls(
            avg_glyphs_per_line=data.get("avg_glyphs_per_line", 0.0),
            most_frequent_glyphs=data.get("most_frequent_glyphs", []),
            hapax_legomena=data.get("hapax_legomena", 0),
            clustering_params=data.get("clustering_params", {}),
        )


@dataclass
class RongorongoLexicon:
    """The complete glyph lexicon output."""

    version: str = "1.0.0"
    created_at: datetime = field(default_factory=datetime.now)
    source_images: list[str] = field(default_factory=list)
    clusters: list[GlyphCluster] = field(default_factory=list)
    statistics: LexiconStatistics = field(default_factory=LexiconStatistics)

    @property
    def total_glyphs_detected(self) -> int:
        """Return the total number of glyph instances."""
        return sum(cluster.frequency for cluster in self.clusters)

    @property
    def unique_glyph_types(self) -> int:
        """Return the number of unique glyph clusters."""
        return len(self.clusters)

    def add_cluster(self, cluster: GlyphCluster) -> None:
        """Add a cluster to the lexicon."""
        self.clusters.append(cluster)

    def get_cluster(self, cluster_id: str) -> Optional[GlyphCluster]:
        """Get a cluster by ID."""
        for cluster in self.clusters:
            if cluster.cluster_id == cluster_id:
                return cluster
        return None

    def compute_statistics(self, instances: list[GlyphInstance]) -> None:
        """Compute lexicon statistics from instances."""
        # Count hapax legomena (clusters with only one instance)
        self.statistics.hapax_legomena = sum(1 for c in self.clusters if c.frequency == 1)

        # Find most frequent glyphs (top 10)
        sorted_clusters = sorted(self.clusters, key=lambda c: c.frequency, reverse=True)
        self.statistics.most_frequent_glyphs = [c.cluster_id for c in sorted_clusters[:10]]

        # Calculate average glyphs per line
        if instances:
            lines = {}
            for inst in instances:
                if inst.position:
                    key = (inst.source_image, inst.position.line_number)
                    lines[key] = lines.get(key, 0) + 1
            if lines:
                self.statistics.avg_glyphs_per_line = sum(lines.values()) / len(lines)

    def to_dict(self) -> dict:
        """Convert to dictionary for JSON serialization."""
        return {
            "version": self.version,
            "created_at": self.created_at.isoformat(),
            "source_images": self.source_images,
            "total_glyphs_detected": self.total_glyphs_detected,
            "unique_glyph_types": self.unique_glyph_types,
            "clusters": [c.to_dict() for c in self.clusters],
            "statistics": self.statistics.to_dict(),
        }

    @classmethod
    def from_dict(cls, data: dict) -> "RongorongoLexicon":
        """Create from dictionary."""
        return cls(
            version=data.get("version", "1.0.0"),
            created_at=datetime.fromisoformat(data["created_at"]),
            source_images=data.get("source_images", []),
            clusters=[GlyphCluster.from_dict(c) for c in data.get("clusters", [])],
            statistics=LexiconStatistics.from_dict(data.get("statistics", {})),
        )
